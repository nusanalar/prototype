const { serve } = require('./_server');
// Kid guidance: first-time onboarding, "start here" island, mission card, saving a lesson, learning book and parent view.
const { chromium } = require('playwright');
const path = require('path');
const URL = 'file://' + path.resolve(__dirname, '../index.html');
const SHOTS = process.env.SHOTS || '';
(async () => {
  const URL_HTTP = await serve();
  const b = await chromium.launch(); const fails = []; const ok = (c, m) => { if (!c) fails.push(m); };
  for (const [locale, w] of [['id-ID', 390], ['en-US', 1000]]) {
    const ctx = await b.newContext({ locale, viewport: { width: w, height: 860 } }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => { HTMLMediaElement.prototype.play = () => Promise.resolve(); });
    const shot = async n => { if (SHOTS) await p.screenshot({ path: `${SHOTS}/g-${locale}-${n}.png`, fullPage: n !== 'onb0' && !n.startsWith('onb') }); };
    const over = async n => { const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(o <= 1, `${locale}: ${n} overflows ${o}px`); };
    await p.goto(URL_HTTP); await p.waitForTimeout(400);
    ok(await p.isVisible('#onb'), `${locale}: onboarding should show on first visit`);
    for (let i = 0; i < 5; i++) {
      await shot('onb' + i); await over('onboarding step ' + (i + 1));
      if (i === 0) await p.click('[data-action="onb-avatar"][data-v="laras"]');
      if (i === 4) { ok(await p.isDisabled('[data-action="onb-done"]'), `${locale}: start should wait for an age`); await p.click('[data-action="onb-age"][data-v="detective"]'); await shot('onb4b'); await p.click('[data-action="onb-done"]'); }
      else await p.click('[data-action="onb-next"]');
      await p.waitForTimeout(150);
    }
    ok(!(await p.isVisible('#onb')), `${locale}: onboarding should close`);
    ok(await p.evaluate(() => st.avatar === 'laras' && st.ageTier === 'detective'), `${locale}: avatar/age not kept`);
    ok(await p.$('.isl.start[data-case="detective"]') && await p.$('.start-t'), `${locale}: start-here island not marked`);
    await shot('map'); await over('map');
    await p.waitForTimeout(1200); await p.reload(); await p.waitForTimeout(300);
    ok(!(await p.isVisible('#onb')), `${locale}: onboarding should not repeat after reload`);
    // help button replays it
    await p.click('#helpBtn'); ok(await p.isVisible('#onb'), `${locale}: help should reopen onboarding`); await p.click('[data-action="onb-skip"]');
    // mission card on an activity
    await p.click('[data-action="open"][data-case="detective"]'); await p.waitForTimeout(200);
    ok(await p.isVisible('details.mission[open] .m-goal'), `${locale}: mission card missing`); await shot('mission'); await over('mission');
    // finish the case and save the lesson
    await p.evaluate(() => { st.det.step = 5; st.det.sus = 'bayu'; solve('detective'); render(); });
    await p.waitForTimeout(150);
    ok(await p.isVisible('.learn .use-opt'), `${locale}: lesson card missing on result`);
    ok(await p.isDisabled('[data-action="learn-save"]'), `${locale}: save should wait for a choice`);
    await p.click('.use-opt[data-v="1"]'); await shot('learn'); await p.click('[data-action="learn-save"]'); await p.waitForTimeout(150);
    ok(await p.isVisible('.learn.done'), `${locale}: lesson not saved`); await shot('learned');
    ok(await p.evaluate(() => JSON.parse(localStorage.getItem('mi-learn')).detective.use === 1), `${locale}: lesson not stored`);
    // learning book and parent view
    await p.click('.learn.done [data-action="learnbook"]'); await p.waitForTimeout(150);
    ok(await p.$$eval('.lb-item.got', e => e.length) === 1 && await p.$$eval('.lb-item.locked', e => e.length) === 8, `${locale}: learning book counts wrong`);
    await shot('book'); await over('book');
    await p.click('[data-action="parent"]'); await p.waitForTimeout(150);
    ok(await p.$$eval('.plearn li', e => e.length) === 1, `${locale}: parent view should list the saved lesson`); await shot('parent');
    // next child starts over, including onboarding and lessons
    p.once('dialog', d => d.accept()); await p.click('[data-action="new-player"]'); await p.waitForTimeout(200);
    ok(await p.isVisible('#onb'), `${locale}: onboarding should restart for the next child`);
    ok(await p.evaluate(() => !localStorage.getItem('mi-learn') && !Object.keys(st.learned).length && !st.ageTier), `${locale}: lessons/age not cleared`);
    ok(!errs.length, `${locale}: page errors ${errs}`);
    await ctx.close();
  }
  console.log(fails.length ? 'FAIL\n ' + fails.join('\n ') : 'PASS: onboarding, start-here island, mission card, lesson saving, learning book and parent view');
  await b.close(); process.exit(fails.length ? 1 : 0);
})();

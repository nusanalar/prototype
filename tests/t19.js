require('./_setup');
// 6-year-old playtest fixes: age-matched daily puzzle, locked islands with a grown-up check, spoken/collapsed mission,
// feedback kept on screen, train payoff and third train, short boat route, tappable pets, parent-only benefits, "Next" marker.
const { chromium } = require('playwright');
const { serve } = require('./_server');
(async () => {
  const URL = await serve();
  const b = await chromium.launch(); const fails = []; const ok = (c, m) => { if (!c) fails.push(m); };
  for (const [locale, w] of [['id-ID', 390], ['en-US', 1000]]) {
    const ctx = await b.newContext({ locale, viewport: { width: w, height: 760 }, reducedMotion: 'reduce' }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => { window.__said = []; window.__played = []; HTMLMediaElement.prototype.play = function () { window.__played.push(this.src); return Promise.resolve(); }; try { localStorage.setItem('mi-age', 'explorer'); } catch (e) {} });
    await p.goto(URL); await p.waitForTimeout(300);
    const over = async n => { const o = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(o <= 1, `${locale}: ${n} overflows ${o}px`); };
    // onboarding: 4 steps, no parent benefits step, pets respond
    ok(await p.evaluate(() => G().onb.length === 4 && !G().onb.some(s => /good for you|bagus untukmu/i.test(s.t))), `${locale}: benefits step still in onboarding`);
    await p.click('#helpBtn'); await p.click('[data-action="onb-next"]'); await p.click('[data-action="onb-next"]');
    ok(await p.$$eval('.onb-pet[data-action="pet"]', e => e.length) === 5, `${locale}: onboarding pets not tappable`);
    await p.click('.onb-pet[data-v="oyen"]'); await p.waitForTimeout(100);
    await p.click('[data-action="onb-skip"]');
    // map: Pulau Pola marked, higher islands locked
    ok(await p.$('.isl.start[data-case="explorer"]'), `${locale}: start island not explorer`);
    ok(await p.$('.isl.locked[data-case="detective"]') && await p.$('.isl.locked[data-case="strategist"]'), `${locale}: higher islands not locked`);
    await over('map');
    await p.click('.isl[data-case="detective"]'); await p.waitForTimeout(100);
    ok(await p.isVisible('#gate') && await p.evaluate(() => st.screen === 'map'), `${locale}: locked island should show the gate`);
    await p.fill('#gateIn', '1'); await p.click('[data-action="gate-open"]');
    ok(await p.isVisible('#gate') && await p.evaluate(() => st.screen === 'map'), `${locale}: wrong answer should keep it locked`);
    await p.click('[data-action="gate-close"]'); ok(!(await p.isVisible('#gate')), `${locale}: gate should close`);
    // daily puzzle opens on the child's band, harder bands locked
    await p.click('.daily-card'); await p.waitForTimeout(150);
    ok(await p.evaluate(() => st.daily.tier === 'explorer'), `${locale}: daily should open on Mudah`);
    await p.click('[data-action="dy-tier"][data-v="detective"]');
    ok(await p.isVisible('#gate') && await p.evaluate(() => st.daily.tier === 'explorer'), `${locale}: harder daily should be gated`);
    await p.click('[data-action="gate-close"]');
    await p.click('.back'); await p.waitForTimeout(100);
    // pattern case: mission collapsed, no duplicate "not quite", feedback on screen, third train, train rolls away
    await p.click('[data-action="open"][data-case="explorer"]'); await p.waitForTimeout(450);
    ok(await p.$('details.mission:not([open])'), `${locale}: mission should start collapsed for 6–9`);
    ok(await p.evaluate(() => document.body.classList.contains('young')), `${locale}: young class missing`);
    await over('pattern');
    const lab = await p.$$eval('.shape-opt .opt', e => e.map(x => x.scrollWidth <= x.clientWidth + 1 && x.getAttribute('aria-label')));
    ok(lab.every(Boolean), `${locale}: answer buttons clipped or unlabeled`);
    const cars = await p.evaluate(() => { const t = document.querySelector('.train').getBoundingClientRect(), c = [...document.querySelectorAll('.train .car')].pop().getBoundingClientRect(); return c.right <= t.right + 1 && c.right <= innerWidth; });
    ok(cars, `${locale}: ? car clipped`);
    await p.click('[data-action="e-pick"][data-v="sq"]'); await p.waitForTimeout(250);
    const t = await p.textContent('.fb');
    ok(!/(Belum tepat\.|Not quite\.)\s*\1/.test(t), `${locale}: duplicate lead in "${t.trim()}"`);
    await p.click('[data-action="e-pick"][data-v="tri"]');
    await p.click('[data-action="e-why"][data-v="0"]'); await p.waitForTimeout(300);
    ok(await p.$('.fb.good') && /Pintar|Clever/.test(await p.textContent('.fb')), `${locale}: no praise for the right reason`);
    ok(await p.evaluate(() => { const want = (st.lang === 'id' ? VOX : VOX_EN)[voxKey('kepi', L().correct)]; return window.__played.some(s => s.endsWith(want)); }), `${locale}: praise should play Kepi's recorded clip, not the device voice`);
    const inView = await p.evaluate(() => { const r = document.querySelector('.fb').getBoundingClientRect(); return r.top >= 0 && r.bottom <= innerHeight; });
    ok(inView, `${locale}: feedback not on screen`);
    await p.click('[data-action="e-step"][data-v="r2"]'); await p.click('[data-action="e-pick2"][data-v="5"]');
    ok(await p.evaluate(() => st.exp.step === 'r3'), `${locale}: third train missing`);
    await p.click('[data-action="e-pick3"][data-v="yellow"]'); await p.waitForTimeout(300);
    ok(await p.$('.train.roll') && await p.evaluate(() => st.solved.explorer), `${locale}: train should roll away on the win`);
    // boat: short route, chips big, fb slot reserved
    await p.click('.result [data-action="open"][data-case="b-explorer"]'); await p.waitForTimeout(150);
    ok(await p.evaluate(() => shortestPath(st.be.grid, st.be.start, st.be.harbor) <= 6), `${locale}: Bangun route too long`);
    ok(await p.evaluate(() => { for (let d = 0; d < 60; d++) { const g = genBoat((20261100 + d) * 10); const f = c => { for (let y = 0; y < g.length; y++) { const i = g[y].indexOf(c); if (i >= 0) return [i, y]; } }; const n = shortestPath(g, f('B'), f('H')); if (n < 4 || n > 6) return false; } return true; }), `${locale}: easy daily routes not 4–6 steps`);
    for (const d of ['right', 'right', 'up']) await p.click(`[data-action="be-add"][data-v="${d}"]`);
    const h0 = await p.evaluate(() => document.querySelector('.fb-slot').getBoundingClientRect().height);
    const chip = await p.evaluate(() => { const r = document.querySelector('.pblock').getBoundingClientRect(); return Math.min(r.width, r.height); });
    ok(chip >= 48, `${locale}: step chip ${chip}px < 48`);
    await p.click('[data-action="be-run"]'); await p.waitForTimeout(1800);
    ok(await p.evaluate(() => st.be.fb === 'crash' || st.be.fb === 'short'), `${locale}: boat should fail`);
    const h1 = await p.evaluate(() => document.querySelector('.fb-slot').getBoundingClientRect().height);
    ok(Math.abs(h1 - h0) <= 30 || h0 >= 70, `${locale}: fb slot not reserved (${h0} -> ${h1})`);
    await p.click('[data-action="be-clear"]');
    for (const d of ['right', 'right', 'right', 'right', 'up', 'up']) await p.click(`[data-action="be-add"][data-v="${d}"]`);
    await p.click('[data-action="be-run"]'); await p.waitForTimeout(3200);
    ok(await p.evaluate(() => st.built.explorer), `${locale}: 6-step route should win`);
    await over('boat result');
    // map: still marked as "Next" (case #10 left), island click goes to it
    await p.click('.result [data-action="home"]'); await p.waitForTimeout(150);
    const mark = await p.textContent('.start-t');
    ok(/Next|Selanjutnya/.test(mark), `${locale}: marker should say Next, got ${mark}`);
    await p.click('.isl[data-case="explorer"]'); await p.waitForTimeout(150);
    ok(await p.evaluate(() => st.screen === 'explorer2'), `${locale}: island should open the next task`);
    await p.click('.back');
    // grown-up unlock
    await p.click('.isl[data-case="detective"]');
    const ans = await p.evaluate(() => st.gate.a * st.gate.b); await p.fill('#gateIn', String(ans)); await p.press('#gateIn', 'Enter'); await p.waitForTimeout(150);
    ok(await p.evaluate(() => st.screen === 'detective' && st.unlocked.detective), `${locale}: grown-up answer should unlock`);
    // parent view carries the benefits + goals
    await p.click('[data-action="parent"]'); await p.waitForTimeout(100);
    ok(await p.$$eval('.pwhy li', e => e.length) >= 12, `${locale}: parent view missing benefits/goals`);
    ok(!errs.length, `${locale}: page errors ${errs}`);
    await ctx.close();
  }
  console.log(fails.length ? 'FAIL\n ' + fails.join('\n ') : 'PASS: 6-year-old playtest fixes');
  await b.close(); process.exit(fails.length ? 1 : 0);
})();

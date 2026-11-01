// Case #07 number check: Bu Sari's baking list, wrong and right answers, hour strip, then on to the accusation. EN and ID, desktop and phone.
require('./_setup');
const { chromium } = require('playwright');
const path = require('path');
const OUT = process.env.SHOTS || __dirname;
(async () => {
  const b = await chromium.launch(); let fails = 0;
  const ok = (c, m) => { if (!c) { fails++; console.log('FAIL', m); } };
  for (const [locale, w] of [['en-US', 1100], ['id-ID', 390]]) {
    const p = await (await b.newContext({ locale, viewport: { width: w, height: 900 } })).newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.goto('file://' + path.resolve(__dirname, '../index.html')); await p.waitForTimeout(800);
    await p.evaluate(() => { st.avatar = st.avatar || 'laras'; go('detective'); });
    await p.click('[data-action="d-step"][data-v="1"]');
    ok(await p.isVisible('[data-action="d-see"][data-v="bread"]'), `${locale}: baking list clue missing`);
    for (const k of ['sari', 'boots', 'net', 'bread']) await p.click(`[data-action="d-see"][data-v="${k}"]`);
    await p.click('[data-action="d-step"][data-v="2"]');
    ok(await p.isVisible('.m-facts'), `${locale}: number check not shown`);
    ok(await p.locator('.steps li.now').innerText().then(t => /Number check|Cek angka/.test(t)), `${locale}: step label`);
    await p.click('[data-action="d-math"][data-v="1"]');
    ok(await p.isVisible('.fb.bad'), `${locale}: wrong answer should give a hint`);
    ok(!(await p.isVisible('[data-action="d-step"][data-v="3"]')), `${locale}: next should wait for the right answer`);
    await p.screenshot({ path: path.join(OUT, `t18-${locale}-hint.png`), fullPage: true });
    await p.click('[data-action="d-math"][data-v="2"]');
    ok(await p.isVisible('.m-hours'), `${locale}: hour strip missing`);
    ok((await p.locator('.m-hours li.bake').count()) === 5, `${locale}: 5 baking hours`);
    await p.screenshot({ path: path.join(OUT, `t18-${locale}-done.png`), fullPage: true });
    ok(await p.evaluate(() => document.documentElement.scrollWidth <= innerWidth), `${locale}: horizontal scroll`);
    await p.click('[data-action="d-step"][data-v="3"]');
    ok(await p.isVisible('[data-action="d-ev"][data-v="bread"]'), `${locale}: baking evidence missing`);
    await p.click('[data-action="d-sus"][data-v="bayu"]'); await p.click('[data-action="d-ev"][data-v="bread"]'); await p.click('[data-action="d-ev"][data-v="boots"]'); await p.click('[data-action="d-accuse"]');
    ok(await p.isVisible('[data-action="d-why"]'), `${locale}: explain step`);
    await p.click('[data-action="d-why"][data-v="0"]'); await p.waitForTimeout(300);
    ok(await p.evaluate(() => st.det.step === 5 && !!st.solved.detective), `${locale}: case not solved`);
    ok(!errs.length, `${locale}: errors ${errs}`);
  }
  console.log(fails ? `${fails} failed` : 'all ok'); await b.close(); process.exit(fails ? 1 : 0);
})();

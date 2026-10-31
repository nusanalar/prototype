const { serve } = require('./_setup');
// Light/dark switch: follows the device by default, the button flips it, the choice is remembered, New player keeps it.
const { chromium } = require('playwright');
const path = require('path');
const URL = 'file://' + path.resolve(__dirname, '../index.html');
(async () => {
  const URL_HTTP = await serve();
  const b = await chromium.launch(); const fails = [];
  const ok = (c, m) => { if (!c) fails.push(m); };
  for (const scheme of ['light', 'dark']) {
    const ctx = await b.newContext({ colorScheme: scheme, locale: 'id-ID' }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => { HTMLMediaElement.prototype.play = () => Promise.resolve(); });
    await p.goto(URL_HTTP); await p.waitForTimeout(300);
    const bg = () => p.evaluate(() => getComputedStyle(document.body).backgroundColor);
    const first = await p.evaluate(() => isDark());
    ok(first === (scheme === 'dark'), `${scheme}: should follow device`);
    const bg1 = await bg();
    await p.click('#themeBtn'); await p.waitForTimeout(150);
    ok(await p.evaluate(() => isDark()) !== first, `${scheme}: button should flip`);
    ok(await bg() !== bg1, `${scheme}: background should change`);
    ok(await p.evaluate(() => localStorage.getItem('mi-theme')) === (first ? 'light' : 'dark'), `${scheme}: choice saved`);
    await p.waitForTimeout(1200); await p.reload(); await p.waitForTimeout(300);
    ok(await p.evaluate(() => isDark()) !== first, `${scheme}: choice kept after reload`);
    await p.evaluate(() => { window.confirm = () => true; newPlayer(); }); await p.waitForTimeout(200);
    ok(await p.evaluate(() => isDark()) !== first, `${scheme}: New player keeps theme`);
    ok(!errs.length, `${scheme}: page errors ${errs}`);
    await ctx.close();
  }
  console.log(fails.length ? 'FAIL\n ' + fails.join('\n ') : 'PASS: theme follows device, flips, is saved and survives New player');
  await b.close(); process.exit(fails.length ? 1 : 0);
})();

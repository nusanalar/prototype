const { serve } = require('./_setup');
// Default language follows the device; "New player" in the parent view gives the next child a fresh start.
const { chromium } = require('playwright');
const PAGE = 'file://' + require('path').resolve(__dirname, '../index.html');
(async () => {
  const PAGE_HTTP = await serve();
  const b = await chromium.launch(); const fails = [];
  const ok = (c, m) => { if (!c) fails.push(m); };
  for (const [locale, want] of [['id-ID', 'id'], ['en-US', 'en']]) {
    const ctx = await b.newContext({ locale, viewport: { width: 390, height: 844 } }); const p = await ctx.newPage();
    const errs = []; p.on('pageerror', e => errs.push(e.message));
    await p.addInitScript(() => { HTMLMediaElement.prototype.play = () => Promise.resolve(); });
    await p.goto(PAGE_HTTP); await p.waitForTimeout(300);
    const lang = await p.evaluate(() => st.lang); ok(lang === want, `${locale}: started in ${lang}, expected ${want}`);
    const brand = await p.evaluate(() => document.title + ' | ' + document.body.innerText);
    ok(!/Pulau Misteri|Mystery Isles/.test(brand), `${locale}: old name visible`); ok(/Nusa Nalar/.test(brand), `${locale}: new name missing`);
    // saved choice wins over the device
    const other = want === 'id' ? 'en' : 'id';
    await p.click(`[data-action="lang"][data-v="${other}"]`); await p.waitForTimeout(1200); await p.reload(); await p.waitForTimeout(300);
    ok(await p.evaluate(() => st.lang) === other, `${locale}: saved language did not win`);
    await p.click(`[data-action="lang"][data-v="${want}"]`);
    // child 1: pick Laras, solve the daily puzzle
    await p.click('[data-action="avatar"][data-v="laras"]');
    await p.evaluate(() => { openDaily(); st.screen = 'daily'; render(); dailySolved(); });
    await p.evaluate(() => { st.solved.detective = true; st.built.explorer = true; });
    await p.waitForTimeout(1200); await p.reload(); await p.waitForTimeout(300);
    ok(await p.evaluate(() => st.avatar) === 'laras', `${locale}: avatar not saved before reset`);
    ok(await p.evaluate(() => Object.keys(st.dailyDone).length) > 0, `${locale}: daily not saved before reset`);
    await p.click('[data-action="parent"]'); await p.waitForTimeout(200);
    if (locale === 'id-ID') await p.screenshot({ path: 'parent-390.png', fullPage: true });
    const over = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(over <= 1, `${locale}: parent view overflows ${over}px`);
    p.once('dialog', d => d.accept());
    await p.click('[data-action="new-player"]'); await p.waitForTimeout(300);
    ok(await p.isVisible('#onb'), `${locale}: onboarding should start again for the next child`); await p.click('[data-action="onb-skip"]'); await p.waitForTimeout(150);
    const s = await p.evaluate(() => ({ screen: st.screen, avatar: st.avatar, daily: Object.keys(st.dailyDone).length, lang: st.lang, stored: localStorage.getItem('mi-daily'), av: localStorage.getItem('mi-avatar'), savedLang: localStorage.getItem('mi-lang'), sel: document.querySelector('.who-btn[aria-pressed="true"], .who-btn.on')?.dataset.v }));
    ok(s.screen === 'map', `${locale}: not back on map`); ok(s.avatar === 'raka', `${locale}: avatar not reset`); ok(s.daily === 0 && !s.stored, `${locale}: daily not reset`);
    ok(!s.av, `${locale}: saved avatar not cleared`); ok(s.lang === want && s.savedLang === want, `${locale}: language not kept`);
    const mapOver = await p.evaluate(() => document.documentElement.scrollWidth - innerWidth); ok(mapOver <= 1, `${locale}: map overflows ${mapOver}px`);
    // cancel keeps progress
    await p.click('[data-action="avatar"][data-v="laras"]'); await p.click('[data-action="parent"]');
    p.once('dialog', d => d.dismiss()); await p.click('[data-action="new-player"]'); await p.waitForTimeout(200);
    ok(await p.evaluate(() => st.avatar) === 'laras' && await p.evaluate(() => st.screen) === 'parent', `${locale}: cancel still reset`);
    ok(!errs.length, `${locale}: errors ${errs}`);
    console.log(`${locale}: lang ${lang}, after New player ${JSON.stringify(s)}`);
    await ctx.close();
  }
  console.log(fails.length ? 'FAIL\n ' + fails.join('\n ') : 'PASS'); await b.close(); process.exit(fails.length ? 1 : 0);
})();

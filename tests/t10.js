require('./_setup');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.addInitScript(() => { const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); window.__played = []; HTMLMediaElement.prototype.play = function () { window.__played.push(Object.entries(SND).find(([k, v]) => v === this.src)?.[0] || '?'); return Promise.resolve(); }; });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(1000);
  await p.click('[data-case="strategist2"]'); await p.waitForTimeout(700);
  await p.screenshot({ path: 'c9-brief.png', fullPage: true });
  await p.click('[data-action="c9-step"][data-v="1"]');
  for (const k of ['darto', 'ijah', 'poster', 'search', 'webcam', 'weather', 'comment']) await p.click(`[data-action="c9-see"][data-v="${k}"]`);
  await p.click('[data-action="c9-step"][data-v="2"]');
  await p.click('[data-action="c9-rate"][data-v="poster"][data-r="rel"]'); // wrong
  await p.screenshot({ path: 'c9-rate-wrong.png', fullPage: true });
  for (const [k, r] of [['poster', 'unrel'], ['webcam', 'rel'], ['comment', 'unrel'], ['search', 'rel'], ['darto', 'rel']]) await p.click(`[data-action="c9-rate"][data-v="${k}"][data-r="${r}"]`);
  await p.screenshot({ path: 'c9-rate-done.png', fullPage: true });
  await p.click('[data-action="c9-step"][data-v="3"]');
  await p.click('[data-action="c9-dec"][data-v="1"]'); console.log('dec wrong step', await p.evaluate(() => st.str2.step));
  await p.click('[data-action="c9-dec"][data-v="2"]');
  await p.click('[data-action="c9-why"][data-v="2"]'); await p.click('[data-action="c9-why"][data-v="0"]'); await p.waitForTimeout(700);
  await p.screenshot({ path: 'c9-result.png', fullPage: true });
  console.log('solved', await p.evaluate(() => st.solved.strategist2));
  await p.click('.back'); await p.click('#parentBtn'); console.log('badges:', await p.$$eval('.blist .badge', n => n.map(x => x.textContent.trim())));
  await p.click('#lang-id'); await p.click('.back'); await p.click('[data-case="strategist2"]'); console.log('ID:', await p.textContent('.stage h2'));
  await p.setViewportSize({ width: 400, height: 860 }); await p.waitForTimeout(300); await p.screenshot({ path: 'c9-mobile.png', fullPage: true });
  console.log('played:', (await p.evaluate(() => window.__played)).join(' '));
  console.log('errors', errs); await b.close();
})();

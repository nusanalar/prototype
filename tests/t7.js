require('./_setup');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.addInitScript(() => { const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); window.__played = []; const op = HTMLMediaElement.prototype.play; HTMLMediaElement.prototype.play = function () { window.__played.push(Object.entries(SND).find(([k, v]) => v === this.src)?.[0] || '?'); return Promise.resolve(); }; });
  const errs = []; p.on('pageerror', e => errs.push(e.message)); p.on('console', m => m.type() === 'error' && errs.push(m.text()));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(1200);
  await p.screenshot({ path: 'proto-map.png', clip: { x: 0, y: 0, width: 1100, height: 900 } });
  await p.click('.pet-map[data-v="oyen"]');
  await p.click('[data-action="avatar"][data-v="laras"]');
  // detective case quick run
  await p.click('[data-case="detective"]'); await p.click('[data-action="d-step"][data-v="1"]');
  for (const k of ['bayu', 'sari', 'dika', 'boots', 'net']) await p.click(`[data-action="d-see"][data-v="${k}"]`);
  await p.screenshot({ path: 'proto-inv.png', fullPage: true });
  await p.click('[data-action="d-step"][data-v="2"]'); await p.click('[data-action="d-sus"][data-v="dika"]'); await p.click('[data-action="d-accuse"]');
  await p.screenshot({ path: 'proto-hint.png', fullPage: true });
  await p.click('[data-action="d-sus"][data-v="bayu"]'); await p.click('[data-action="d-ev"][data-v="boots"]'); await p.click('[data-action="d-ev"][data-v="net"]'); await p.click('[data-action="d-accuse"]');
  await p.click('[data-action="d-why"][data-v="0"]'); await p.waitForTimeout(1000);
  await p.screenshot({ path: 'proto-result.png', fullPage: true });
  // lighthouse level 1 + boat
  await p.click('.back'); await p.click('[data-case="b-detective"]'); await p.click('[data-slot="A"]'); await p.click('[data-action="bd-place"][data-v="or"]'); await p.click('[data-action="bd-test"]');
  await p.click('.back'); await p.click('[data-case="b-explorer"]');
  for (const d of ['right','right','right','right','right','up','up','up']) await p.click(`[data-action="be-add"][data-v="${d}"]`);
  await p.click('[data-action="be-run"]'); await p.waitForTimeout(4200);
  await p.click('.back'); await p.click('.daily-card'); await p.waitForTimeout(800);
  await p.click('[data-action="music"]');
  console.log('played:', (await p.evaluate(() => window.__played)).join(' '));
  console.log('built explorer', await p.evaluate(() => st.built.explorer), 'errors', errs);
  await b.close();
})();

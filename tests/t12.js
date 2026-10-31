const { chromium } = require('playwright');
async function run(noSpeech) {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.addInitScript((noSpeech) => {
    const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); window.__said = []; window.__played = []; window.__speakingSeen = 0;
    HTMLMediaElement.prototype.play = function () { window.__played.push(Object.entries(SND).find(([k, v]) => v === this.src)?.[0] || '?'); return Promise.resolve(); };
    if (noSpeech) { try { delete window.speechSynthesis; Object.defineProperty(window, 'speechSynthesis', { value: undefined }); } catch (e) {} }
    else if (window.speechSynthesis) {
      window.speechSynthesis.speak = u => { window.__said.push(`${u.lang} p${u.pitch} r${u.rate}: ${u.text.slice(0, 38)}`); if (u.onstart) { u.onstart(); window.__speakingSeen += document.querySelectorAll('.speaking').length; setTimeout(() => u.onend && u.onend(), 300); } };
    }
  }, noSpeech);
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(800);
  await p.click('[data-action="avatar"][data-v="laras"]');
  await p.click('.pet-map[data-v="rangga"]'); await p.waitForTimeout(600);
  await p.click('[data-case="detective2"]'); await p.waitForTimeout(800);
  await p.click('[data-action="c2-step"][data-v="1"]'); await p.click('[data-action="c2-see"][data-v="darto"]');
  await p.click('.back'); await p.click('[data-case="explorer2"]'); await p.waitForTimeout(300);
  await p.click('[data-action="e10-step"][data-v="1"]'); await p.click('[data-action="e10-see"][data-v="cici"]'); await p.waitForTimeout(500); for (const k of ['oyen','nyu','prints','bite','window']) await p.click('[data-action="e10-see"][data-v="' + k + '"]');
  await p.click('[data-action="e10-step"][data-v="2"]'); await p.click('[data-action="e10-match"][data-v="paw"]'); await p.waitForTimeout(200);
  await p.click('.fb.helper .pet-mini'); await p.waitForTimeout(200);
  const res = await p.evaluate(() => ({ said: window.__said, speaking: window.__speakingSeen, played: window.__played }));
  await b.close(); return { res, errs };
}
(async () => {
  const a = await run(false);
  console.log('WITH SPEECH\n ' + a.res.said.join('\n ')); console.log(' elements with .speaking during speech:', a.res.speaking, 'errors', a.errs);
  const n = await run(true);
  console.log('NO SPEECH fallback sounds:', n.res.played.join(' '), 'errors', n.errs);
})();

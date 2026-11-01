require('./_setup');
const { chromium } = require('playwright');
(async () => {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.addInitScript(() => {
    localStorage.setItem('mi-lang', 'id'); const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0);
    window.__vox = []; window.__sfx = []; window.__tts = []; window.__spk = 0;
    HTMLMediaElement.prototype.play = function () {
      const vk = Object.keys(VOX).find(k => this.src.endsWith('/' + VOX[k]));
      if (vk) {
        const k = vk; window.__vox.push(k.slice(0, 70));
        setTimeout(() => { window.__spk = Math.max(window.__spk, document.querySelectorAll('.speaking').length); }, 50);
        setTimeout(() => this.onended && this.onended(), 300);
      } else window.__sfx.push(Object.entries(SND).find(([k, v]) => v === this.src)?.[0] || '?');
      return Promise.resolve();
    };
    HTMLMediaElement.prototype.pause = function () {};
    window.SpeechSynthesisUtterance = class { constructor(t) { this.text = t; } };
    Object.defineProperty(window, 'speechSynthesis', { value: { getVoices: () => [], speak: u => window.__tts.push(u.text), cancel() {}, addEventListener() {} }, configurable: true });
  });
  const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(500);
  await p.click('[data-action="avatar"][data-v="laras"]'); await p.waitForTimeout(400);
  for (const k of ['oyen', 'rangga']) { await p.click(`.pet-map[data-v="${k}"]`); await p.waitForTimeout(900); }
  await p.click('[data-case="explorer2"]'); await p.waitForTimeout(1500);
  await p.click('.back'); await p.click('[data-case="detective2"]'); await p.waitForTimeout(900);
  await p.click('[data-action="c2-step"][data-v="1"]');
  for (const k of ['joko', 'darto']) { await p.click(`[data-action="c2-see"][data-v="${k}"]`); await p.waitForTimeout(500); }
  const o = await p.evaluate(() => ({ vox: window.__vox, sfx: window.__sfx.filter(x => !x.startsWith('ui-')), tts: window.__tts, spk: window.__spk }));
  console.log('recorded lines played:\n ' + o.vox.join('\n ') + '\nsounds: ' + o.sfx.join(' ') + '\ndevice TTS used: ' + o.tts.length + '\nspeaking seen: ' + o.spk + '\nerrors: ' + errs);
  await b.close();
})();

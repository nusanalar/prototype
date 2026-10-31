require('./_setup');
const { chromium } = require('playwright');
async function run(voices, lang) {
  const b = await chromium.launch(); const p = await b.newPage({ viewport: { width: 1100, height: 900 } });
  await p.addInitScript(([voices, lang]) => {
    try { localStorage.setItem('mi-lang', lang); } catch (e) {}
    const o = window.scrollTo.bind(window); window.scrollTo = () => o(0, 0); window.__said = []; window.__played = [];
    HTMLMediaElement.prototype.play = function () { window.__played.push(Object.entries(SND).find(([k, v]) => v === this.src)?.[0] || '?'); return Promise.resolve(); };
    window.SpeechSynthesisUtterance = class { constructor(t) { this.text = t; } };
    const fake = { getVoices: () => voices, speak: u => { window.__said.push(`[${u.voice.name} · ${u.lang} · p${u.pitch}] ${u.text.slice(0, 48)}`); u.onstart && u.onstart(); window.__spk = Math.max(window.__spk||0, document.querySelectorAll('.speaking').length); setTimeout(() => u.onend && u.onend(), 200); }, cancel() {}, addEventListener() {} };
    Object.defineProperty(window, 'speechSynthesis', { value: fake, configurable: true });
  }, [voices, lang]);
  let tipSeen = false; const errs = []; p.on('pageerror', e => errs.push(e.message));
  await p.goto('file://' + require('path').resolve(__dirname, '../index.html')); await p.waitForTimeout(800);
  await p.click('[data-action="avatar"][data-v="raka"]');
  for (const k of ['oyen', 'rangga', 'kepi']) { await p.click(`.pet-map[data-v="${k}"]`); await p.waitForTimeout(550); }
  if (await p.$(".voice-tip")) { tipSeen = true; await p.screenshot({ path: "voice-tip.png" }); await p.click(".voice-tip button"); } await p.click('[data-case="detective2"]'); await p.waitForTimeout(800);
  await p.click('[data-action="c2-step"][data-v="1"]');
  for (const k of ['joko', 'darto', 'putri']) { await p.click(`[data-action="c2-see"][data-v="${k}"]`); await p.waitForTimeout(100); }
  await p.evaluate(() => document.querySelector(".voice-tip button")?.click()); await p.click('.back'); await p.click('[data-case="explorer2"]'); await p.waitForTimeout(300);
  const out = await p.evaluate(() => ({ said: window.__said, played: window.__played, spk: window.__spk, tip: document.querySelector('.voice-tip')?.textContent.slice(0, 60) || null }));
  if (out.tip) await p.screenshot({ path: 'voice-tip.png' });
  await b.close(); return { ...out, tip: out.tip || (tipSeen ? "shown (dismissed)" : null), errs };
}
(async () => {
  const both = [{ name: 'Google Bahasa Indonesia', lang: 'id-ID' }, { name: 'Microsoft Andika - Indonesian', lang: 'id-ID' }, { name: 'Microsoft Gadis Online - Indonesian', lang: 'id-ID' },
    { name: 'Samantha', lang: 'en-US' }, { name: 'Daniel', lang: 'en-GB' }, { name: 'Google US English', lang: 'en-US' }];
  const a = await run(both, 'id');
  console.log('DEVICE WITH INDONESIAN VOICES, game in ID:\n ' + a.said.join('\n ') + '\n speaking hosts seen ' + a.spk + ' errors ' + a.errs);
  const c = await run(both, 'en');
  console.log('\nSAME DEVICE, game in EN:\n ' + c.said.slice(0, 6).join('\n ') + '\n errors ' + c.errs);
  const enOnly = [{ name: 'Samantha', lang: 'en-US' }, { name: 'Daniel', lang: 'en-GB' }];
  const d = await run(enOnly, 'id');
  console.log('\nDEVICE WITH ENGLISH VOICES ONLY, game in ID:\n spoken lines: ' + d.said.length + '\n fallback sounds: ' + d.played.filter(x => x.startsWith('voice') || /meow|call|snap/.test(x)).join(' ') + '\n tip: ' + d.tip + '\n errors ' + d.errs);
})();

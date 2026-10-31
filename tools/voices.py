import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:100])
    s = s.replace(a, b)

a = s[s.index("/* Character voices:"):s.index("function speak(text, opts)")]
s = s.replace(a, r'''/* Character voices. Each character has a voice character (gender, pitch, pace, pauses, a small signature sound for animals)
   and gets its own voice from the device's speech voices. Indonesian lines are only ever spoken by an Indonesian voice,
   so they keep an Indonesian accent; if the device has none, the character's own sound plays instead. */
const VOICE_CHAR = {
  narrator: { g: "f", pitch: 1.05, rate: .95 },
  raka: { g: "m", pitch: 1.45, rate: 1.06 }, laras: { g: "f", pitch: 1.55, rate: 1 }, dika: { g: "m", pitch: 1.3, rate: 1.14 },
  bayu: { g: "m", pitch: .55, rate: .86 }, sari: { g: "f", pitch: 1.15, rate: 1.02 }, ratna: { g: "f", pitch: .95, rate: .94 },
  darto: { g: "m", pitch: .42, rate: .84 }, putri: { g: "f", pitch: 1.3, rate: 1.14 }, joko: { g: "m", pitch: .95, rate: 1.06 },
  hasan: { g: "m", pitch: .75, rate: .9 }, ijah: { g: "f", pitch: .9, rate: .78, slow: 1 },
  oyen: { g: "m", pitch: 1.7, rate: 1.08, tic: { en: "Mrrrow. ", id: "Meong. " } },
  kepi: { g: "f", pitch: 1.95, rate: 1.22, tic: { en: "Ooh! ", id: "Wah! " } },
  nyu: { g: "f", pitch: .85, rate: .8, slow: 1, tic: { en: "Hmm... ", id: "Hmm... " } },
  cici: { g: "f", pitch: 2, rate: 1.28, tic: { en: "Psst! ", id: "Ssst! " } },
  rangga: { g: "m", pitch: .62, rate: .88, slow: 1, tic: { en: "Hm. ", id: "Hm. " } }
};
const FEMALE_RE = /female|woman|girl|gadis|damayanti|ayu|siti|wulan|indah|zira|samantha|karen|victoria|susan|tessa|moira|fiona|allison|ava|serena|jenny|aria|sonia|libby|emma|joanna|salli|kimberly/i;
const MALE_RE = /\bmale|\bman\b|boy|andika|ardi|arif|budi|david|daniel|alex|fred|george|guy|mark|james|tom|aaron|arthur|oliver|ryan|eric|brian|matthew|justin|joey/i;
let voicesCache = [], voicesReady = false, voiceTipShown = false;
function loadVoices() { try { voicesCache = speechSynthesis.getVoices() || []; voicesReady = voicesCache.length > 0; } catch (e) {} }
try { loadVoices(); speechSynthesis.addEventListener("voiceschanged", loadVoices); } catch (e) {}
const canSpeak = () => { try { return !!window.speechSynthesis && typeof SpeechSynthesisUtterance !== "undefined"; } catch (e) { return false; } };
const langTag = v => String(v.lang || "").replace("_", "-").toLowerCase();
function voicePool() { return voicesCache.filter(v => st.lang === "id" ? langTag(v).startsWith("id") : langTag(v).startsWith("en")); }
function voiceFor(who) {
  const pool = voicePool(); if (!pool.length) return null;
  const vc = VOICE_CHAR[who] || VOICE_CHAR.narrator;
  const same = pool.filter(v => (vc.g === "f" ? FEMALE_RE : MALE_RE).test(v.name));
  const list = same.length ? same : pool;
  let h = 0; for (const ch of who) h = (h * 31 + ch.charCodeAt(0)) >>> 0;
  return list[h % list.length];
}
function fallbackVoice(who, host) { const b = VOICE_P[who] || VOICE[who]; if (b) sfx(b); if (host) playMove(host, "talk"); }
function showVoiceTip() {
  if (voiceTipShown) return; voiceTipShown = true;
  const l = L(), d = document.createElement("div");
  d.className = "voice-tip"; d.setAttribute("role", "status");
  d.innerHTML = `<b>${l.voiceTipT}</b><p>${l.voiceTip}</p><button class="secondary" type="button">${l.voiceTipOk}</button>`;
  d.querySelector("button").addEventListener("click", () => d.remove());
  document.body.appendChild(d);
}
function sayAs(who, text, host, opts = {}) {
  if (!st.soundOn || !text) return;
  if (!canSpeak()) return fallbackVoice(who, host);
  if (!voicesReady) {
    const t0 = Date.now();
    const retry = () => { loadVoices(); if (voicesReady) sayAs(who, text, host, opts); else if (Date.now() - t0 < 1500) setTimeout(retry, 150); else fallbackVoice(who, host); };
    return void setTimeout(retry, 150);
  }
  const voice = voiceFor(who);
  if (!voice) { fallbackVoice(who, host); if (st.lang === "id") showVoiceTip(); return; }
  const vc = VOICE_CHAR[who] || VOICE_CHAR.narrator;
  let line = String(text).replace(/[“”"]/g, "").trim();
  if (opts.tic && vc.tic) line = vc.tic[st.lang] + line;
  if (vc.slow) line = line.replace(/([.!?]) /g, "$1... ");
  try {
    if (!opts.queue) speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(line);
    u.voice = voice; u.lang = voice.lang; u.pitch = vc.pitch; u.rate = vc.rate;
    if (host) { u.onstart = () => host.classList.add("speaking"); u.onend = u.onerror = () => host.classList.remove("speaking"); }
    speechSynthesis.speak(u);
  } catch (e) { fallbackVoice(who, host); }
}
''')

# signature sounds on greetings and helper hints
rep('''    if (h && line) sayAs(h.dataset.slug, line.textContent, h);''', '''    if (h && line) sayAs(h.dataset.slug, line.textContent, h, { tic: true });''')
rep('''      setTimeout(() => sayAs(v, L().greet[v], host), 450);''', '''      setTimeout(() => sayAs(v, L().greet[v], host, { tic: false }), 450);''')
rep('''      if (fb) { const line = fb.querySelector(".say > span:last-child"); playMove(host, "talk"); sayAs(v, line ? line.textContent : "", host); return; }''',
    '''      if (fb) { const line = fb.querySelector(".say > span:last-child"); playMove(host, "talk"); sayAs(v, line ? line.textContent : "", host, { tic: true }); return; }''')

# tip strings
rep('''    soundL: "Sound effects", musicL: "Island music",''', '''    voiceTipT: "No Indonesian voice on this device yet", voiceTipOk: "OK",
    voiceTip: "So the characters keep their Indonesian accent, they use their own sounds for now. To hear them speak, add an Indonesian voice. Android: Settings → Languages → Text-to-speech. iPhone or iPad: Settings → Accessibility → Spoken Content → Voices. Windows: Settings → Time & language → Speech.",
    soundL: "Sound effects", musicL: "Island music",''')
rep('''    soundL: "Efek suara", musicL: "Musik pulau",''', '''    voiceTipT: "Perangkat ini belum punya suara Bahasa Indonesia", voiceTipOk: "Oke",
    voiceTip: "Supaya logat Indonesianya tetap terjaga, para tokoh memakai suara khas mereka dulu. Untuk mendengar mereka berbicara, tambahkan suara Bahasa Indonesia. Android: Setelan → Bahasa → Teks ke ucapan. iPhone atau iPad: Pengaturan → Aksesibilitas → Konten Lisan → Suara. Windows: Pengaturan → Waktu & bahasa → Ucapan.",
    soundL: "Efek suara", musicL: "Musik pulau",''')
rep('''/* Speaking: mouth loops while the character's voice plays */''', '''/* Voice tip when a device has no Indonesian voice */
.voice-tip { position: fixed; left: max(16px, env(safe-area-inset-left, 0px)); right: max(16px, env(safe-area-inset-right, 0px)); bottom: calc(16px + env(safe-area-inset-bottom, 0px)); z-index: 40; max-width: 560px; margin: 0 auto; background: var(--card-2); border: 1px solid var(--lantern); border-radius: 16px; padding: 14px 16px; display: grid; gap: 6px; box-shadow: 0 10px 30px rgba(0,0,0,.4); font-size: .88rem; }
.voice-tip b { font-family: var(--display); font-size: 1.05rem; }
.voice-tip button { justify-self: end; }
/* Speaking: mouth loops while the character's voice plays */''')
open(P, "w").write(s)
print("ok")

import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:100])
    s = s.replace(a, b)

# greetings
rep('''    soundL: "Sound effects", musicL: "Island music",''', '''    greet: { oyen: "Meow! I'm Oyen. Stuck on a case? I'll give you a hint!", kepi: "Hi hi! I'm Kepi. I count everything twice, just to be sure!",
      nyu: "Hello, I'm Nyu. I bring a new puzzle every morning.", cici: "Psst! I'm Cici. I see everything at night!", rangga: "I'm Rangga. Remember: always ask, where is the proof?",
      raka: "Hi! I'm Raka. Let's solve some mysteries!", laras: "Hi! I'm Laras. Let's look at every clue carefully!" },
    soundL: "Sound effects", musicL: "Island music",''')
rep('''    soundL: "Efek suara", musicL: "Musik pulau",''', '''    greet: { oyen: "Meong! Aku Oyen. Bingung? Aku kasih petunjuk!", kepi: "Halo halo! Aku Kepi. Aku menghitung semuanya dua kali, biar yakin!",
      nyu: "Halo, aku Nyu. Aku membawa teka-teki baru setiap pagi.", cici: "Ssst! Aku Cici. Aku melihat semuanya di malam hari!", rangga: "Aku Rangga. Ingat: selalu tanya, mana buktinya?",
      raka: "Hai! Aku Raka. Ayo pecahkan misteri!", laras: "Hai! Aku Laras. Ayo periksa setiap petunjuk dengan teliti!" },
    soundL: "Efek suara", musicL: "Musik pulau",''')

# voice system
a = s[s.index("function speak(text) {"):s.index("const joinSay =")]
s = s.replace(a, '''/* Character voices: the device's own speech voice, tuned per character (pitch, speed), with the mouth moving while they talk.
   If the device cannot speak, the character's babble sound and talk move play instead. */
const VOICE_PROFILE = { narrator: [1.05, .95], raka: [1.35, 1.05], laras: [1.5, 1], dika: [1.3, 1.1], bayu: [.6, .9], sari: [1.1, .95],
  ratna: [1, .95], darto: [.5, .88], putri: [1.3, 1.05], joko: [.9, 1], hasan: [.75, .9], ijah: [.95, .82],
  oyen: [1.7, 1.12], kepi: [1.9, 1.2], nyu: [.8, .85], cici: [2, 1.25], rangga: [.7, .95] };
let voicesCache = [];
try { speechSynthesis.onvoiceschanged = () => { voicesCache = speechSynthesis.getVoices(); }; } catch (e) {}
function pickVoice() {
  try {
    if (!voicesCache.length) voicesCache = speechSynthesis.getVoices();
    const tag = v => v.lang.replace("_", "-").toLowerCase();
    return st.lang === "id" ? voicesCache.find(v => tag(v).startsWith("id")) || null
      : voicesCache.find(v => tag(v) === "en-us") || voicesCache.find(v => tag(v).startsWith("en")) || null;
  } catch (e) { return null; }
}
const canSpeak = () => { try { return !!window.speechSynthesis && typeof SpeechSynthesisUtterance !== "undefined"; } catch (e) { return false; } };
function sayAs(who, text, host, opts = {}) {
  if (!st.soundOn || !text) return;
  const clean = String(text).replace(/[\\u201c\\u201d"]/g, "").trim();
  if (!canSpeak()) { const b = VOICE_P[who] || VOICE[who]; if (b) sfx(b); if (host) playMove(host, "talk"); return; }
  try {
    if (!opts.queue) speechSynthesis.cancel();
    const u = new SpeechSynthesisUtterance(clean), [pitch, rate] = VOICE_PROFILE[who] || VOICE_PROFILE.narrator;
    u.lang = st.lang === "id" ? "id-ID" : "en-US"; const v = pickVoice(); if (v) u.voice = v;
    u.pitch = pitch; u.rate = rate;
    if (host) { u.onstart = () => host.classList.add("speaking"); u.onend = u.onerror = () => host.classList.remove("speaking"); }
    speechSynthesis.speak(u);
  } catch (e) {}
}
function speak(text, opts) { sayAs("narrator", text, null, opts); }
''')

# helpers speak their feedback
rep('''  if (fb && key !== lastFb) playMove(fb.querySelector("svg[data-slug]"), fb.classList.contains("good") ? "happy" : "no");''',
    '''  if (fb && key !== lastFb) {
    const h = fb.querySelector("svg[data-slug]"), line = fb.querySelector(".say > span:last-child");
    playMove(h, fb.classList.contains("good") ? "happy" : "no");
    if (h && line) sayAs(h.dataset.slug, line.textContent, h);
  }''')

# suspects say their statements
for case, key in (("d-see", "d"), ("c2-see", "d2"), ("c9-see", "s2")):
    rep(f'''      if (VOICE_P[v]) {{ sfx(VOICE_P[v]); playMove(document.querySelector(`[data-action="{case}"][data-v="${{v}}"] svg[data-slug]`), "talk"); }}''',
        f'''      if (VOICE_P[v]) sayAs(v, L().{key}.sus[v].s, document.querySelector(`[data-action="{case}"][data-v="${{v}}"] svg[data-slug]`));''')
rep('''      if (pv) { sfx(pv); playMove(document.querySelector(`[data-action="e10-see"][data-v="${v}"] svg[data-slug]`), "happy"); } else sfx("clue-found");
      speak((x.sus[v] || x.clue[v]).s);''', '''      if (pv) { const host = document.querySelector(`[data-action="e10-see"][data-v="${v}"] svg[data-slug]`); sfx(pv); setTimeout(() => sayAs(v, x.sus[v].s, host), 350); }
      else { sfx("clue-found"); speak(x.clue[v].s); }''')

# case 10: the helper now speaks feedback, so the duplicate narrator lines go
rep('''      if (v === "gecko") { sfx("ui-correct"); sfx("kepi-snap", 400); speak(x.matchOk); } else { sfx("ui-wrong"); sfx("kepi-snap", 350); speak(x.matchNo); }''',
    '''      if (v === "gecko") { sfx("ui-correct"); sfx("kepi-snap", 400); } else { sfx("ui-wrong"); sfx("kepi-snap", 350); }''')
rep('''      if (v === "cici") { c.step = 4; c.why = null; sfx("sting-surprised"); sfx("cici-chirp", 500); speak(x.whoOk + " " + x.whyQ); }
      else { sfx("ui-wrong"); speak(x.whoNo[v]); }
      render();''', '''      if (v === "cici") { c.step = 4; c.why = null; sfx("sting-surprised"); sfx("cici-chirp", 500); }
      else sfx("ui-wrong");
      render();
      if (v === "cici") speak(x.whyQ, { queue: true });''')
rep('''      else { sfx("ui-wrong"); speak(x.why[+v].f); }''', '''      else sfx("ui-wrong");''')

# case givers speak on the brief screen
rep('''sfx("voice-bu-ratna", 900); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "no"), 300);''',
    '''setTimeout(() => { const g = document.querySelector(".giver svg[data-slug]"); playMove(g, "no"); sayAs("ratna", L().d2.giver, g); }, 500);''')
rep('''sfx("voice-nenek-ijah", 700); speak(joinSay(L().e2.title, L().e2.body)); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "wave"), 300);''',
    '''speak(joinSay(L().e2.title, L().e2.body)); const g = document.querySelector(".giver svg[data-slug]"); playMove(g, "wave"); sayAs("ijah", L().e2.giver, g, { queue: true });''')
rep('''sfx("voice-kak-putri", 1200); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "think"), 500);''',
    '''setTimeout(() => { const g = document.querySelector(".giver svg[data-slug]"); playMove(g, "think"); sayAs("putri", L().s2.giver, g); }, 900);''')

# avatars and animals greet you when tapped; a helper repeats its last line
rep('''render(); sfx(VOICE_P[v]); playMove(document.querySelector(`.who-btn[data-v="${v}"] svg[data-slug]`), "wave"); return;''',
    '''render(); { const h = document.querySelector(`.who-btn[data-v="${v}"] svg[data-slug]`); playMove(h, "wave"); sayAs(v, L().greet[v], h); } return;''')
a = s[s.index('    case "pet": {'):]
a = a[:a.index("      return;\n    }") + len("      return;\n    }")]
s = s.replace(a, '''    case "pet": {
      const host = el.matches("svg[data-slug]") ? el : el.querySelector("svg[data-slug]");
      const fb = el.closest(".fb.helper");
      if (fb) { const line = fb.querySelector(".say > span:last-child"); playMove(host, "talk"); sayAs(v, line ? line.textContent : "", host); return; }
      sfx(VOICE[v]);
      playMove(host, ["hop", "happy", "special", "dance", "spin"][Math.floor(Math.random() * 5)]);
      setTimeout(() => sayAs(v, L().greet[v], host), 450);
      return;
    }''')

# mouth keeps moving for as long as the voice speaks
rep('''/* Case 10: picture-first for ages 6 to 9 */''', '''/* Speaking: mouth loops while the character's voice plays */
.speaking .mouth { animation: mvTalkA .24s steps(1) infinite !important; }
.speaking .mouth-open { animation: mvTalkB .24s steps(1) infinite !important; }

/* Case 10: picture-first for ages 6 to 9 */''')
open(P, "w").write(s)
print("ok")

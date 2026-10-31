import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, count=1):
    global s
    n = s.count(a)
    assert n == count, (n, a[:90])
    s = s.replace(a, b)

# ---------- CSS
rep("/* Parent */\n.parent {", """/* Asset kit art */
.av.pic { background: radial-gradient(circle at 50% 70%, #2d5f8c, #1b3d5b); overflow: hidden; width: 56px; height: 56px; }
.av.pic svg { width: 100%; height: 100%; display: block; }
.item { grid-template-columns: 56px minmax(0, 1fr); }
.opt .av.pic { width: 64px; height: 64px; }
.fb.helper { align-items: center; padding: 10px 14px 10px 10px; }
.pet-mini { flex: 0 0 auto; width: 64px; height: 64px; border-radius: 50%; border: 0; padding: 4px; cursor: pointer; background: radial-gradient(circle at 50% 70%, #2d5f8c, #1b3d5b); }
.pet-mini svg { width: 100%; height: 100%; display: block; overflow: visible; }
.fb.helper .say { display: grid; gap: 2px; }
.fb.helper .who { font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.pet-map { cursor: pointer; }
.pet-map:focus { outline: none; }
.act .waver { animation: kitWave .18s ease-in-out 6 alternate; }
.act .head { animation: kitBob .2s ease-in-out 4 alternate; }
.act .mouth { animation: kitTalkA .24s steps(1) 3; }
.act .mouth-open { animation: kitTalkB .24s steps(1) 3; }
.idle .eyes { transform-box: fill-box; transform-origin: center; animation: kitBlink 5s infinite; }
@keyframes kitWave { from { transform: rotate(-8deg); } to { transform: rotate(10deg); } }
@keyframes kitBob { from { transform: translateY(0); } to { transform: translateY(-3px) rotate(2deg); } }
@keyframes kitTalkA { 0% { opacity: 1; } 50% { opacity: 0; } }
@keyframes kitTalkB { 0% { opacity: 0; } 50% { opacity: 1; } }
@keyframes kitBlink { 0%, 94%, 100% { transform: scaleY(1); } 97% { transform: scaleY(.1); } }
.picker { display: flex; align-items: center; gap: 10px; flex-wrap: wrap; font-size: .85rem; color: var(--muted); }
.who-btn { display: inline-flex; align-items: center; gap: 8px; background: var(--card); border: 2px solid var(--line); border-radius: 999px; padding: 3px 14px 3px 3px; cursor: pointer; color: var(--ink); font: inherit; font-size: .88rem; font-weight: 600; }
.who-btn[aria-pressed="true"] { border-color: var(--lantern); background: color-mix(in srgb, var(--lantern) 14%, var(--card)); }
.who-btn .face { width: 34px; height: 34px; border-radius: 50%; overflow: hidden; background: #24507a; }
.who-btn .face svg { width: 100%; height: 100%; display: block; }
.hero-row { display: flex; align-items: flex-end; gap: 4px; }
.hero-row svg { display: block; height: 150px; width: auto; }
.hero-row .pal { height: 96px; }
.icon-btn { width: 32px; height: 32px; border-radius: 50%; border: 1px solid var(--line); background: none; color: var(--muted); cursor: pointer; display: grid; place-items: center; }
.icon-btn svg { width: 16px; height: 16px; }
.icon-btn[aria-pressed="true"] { color: var(--lantern); border-color: var(--lantern); }
.daily-card .ico.pal { background: radial-gradient(circle at 50% 70%, #2d5f8c, #1b3d5b); padding: 2px; }
.daily-card .ico.pal svg { width: 100%; height: 100%; }
@media (prefers-reduced-motion: reduce) { .act *, .idle * { animation: none !important; } }

/* Parent */
.parent {""")

# ---------- header buttons
rep('''    <button class="btn-ghost" data-action="parent" id="parentBtn"></button>''',
'''    <button class="icon-btn" data-action="sound" id="soundBtn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9 H8 L13 5 V19 L8 15 H4 Z" fill="currentColor"/><path id="soundWaves" d="M16 9 Q18 12 16 15 M18.5 6.5 Q22 12 18.5 17.5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>
    <button class="icon-btn" data-action="music" id="musicBtn"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M9 17 V5 L19 3 V15" stroke="currentColor" stroke-width="2" fill="none" stroke-linejoin="round"/><circle cx="6.5" cy="17.5" r="2.8" fill="currentColor"/><circle cx="16.5" cy="15.5" r="2.8" fill="currentColor"/></svg></button>
    <button class="btn-ghost" data-action="parent" id="parentBtn"></button>''')

# ---------- strings
rep('''    brand: "Mystery Isles", proto:''', '''    soundL: "Sound effects", musicL: "Island music", yourDet: "Your detective:", helperSays: n => `${n} says`,
    brand: "Mystery Isles", proto:''')
rep('''    brand: "Pulau Misteri", proto:''', '''    soundL: "Efek suara", musicL: "Musik pulau", yourDet: "Detektifmu:", helperSays: n => `Kata ${n}`,
    brand: "Pulau Misteri", proto:''')

# ---------- state + helpers
rep('''try { const l = localStorage.getItem("mi-lang"); if (l === "en" || l === "id") st.lang = l; } catch (e) {}''',
'''try { const l = localStorage.getItem("mi-lang"); if (l === "en" || l === "id") st.lang = l; } catch (e) {}
st.avatar = "raka"; st.soundOn = true; st.musicOn = false;
try { const a = localStorage.getItem("mi-avatar"); if (a === "raka" || a === "laras") st.avatar = a; if (localStorage.getItem("mi-sound") === "off") st.soundOn = false; } catch (e) {}

/* Art helpers: full figures, head-and-shoulder portraits, and the helper animal for each screen */
const PET_NAME = { oyen: "Oyen", kepi: "Kepi", nyu: "Nyu", cici: "Cici", rangga: "Rangga" };
const VOICE = { oyen: "oyen-meow", kepi: "kepi-snap", nyu: "nyu-blub", cici: "cici-chirp", rangga: "rangga-call" };
const HELPER = { detective: "oyen", "b-detective": "cici", explorer: "kepi", "b-explorer": "kepi", strategist: "rangga", "b-strategist": "rangga", daily: "nyu" };
const isPet = k => k in PET_NAME;
const figure = (k, cls = "") => `<svg class="${cls}" viewBox="0 0 200 ${isPet(k) ? 200 : 280}" aria-hidden="true">${ART[k]}</svg>`;
const portrait = k => `<svg viewBox="${isPet(k) ? "10 20 180 180" : "38 14 124 124"}" aria-hidden="true">${ART[k]}</svg>`;

/* Sound: short effects from the kit, one looping music track */
const sndCache = {};
function sfx(id, delay = 0) {
  if (!st.soundOn || !SND[id]) return;
  const go = () => {
    try {
      let a = sndCache[id];
      if (!a) a = sndCache[id] = new Audio(SND[id]);
      else if (!a.paused && !a.ended) a = a.cloneNode();
      a.currentTime = 0; a.volume = .8; a.play().catch(() => {});
    } catch (e) {}
  };
  delay ? setTimeout(go, delay) : go();
}
let musicEl = null;
function setMusic(on) {
  st.musicOn = on;
  try {
    if (on) { if (!musicEl) { musicEl = new Audio(SND["theme-island-night"]); musicEl.loop = true; musicEl.volume = .45; } musicEl.play().catch(() => {}); }
    else if (musicEl) musicEl.pause();
  } catch (e) {}
}
function wiggle(el) { if (!el) return; el.classList.remove("act"); void el.getBoundingClientRect(); el.classList.add("act"); setTimeout(() => el.classList.remove("act"), 1200); }''')

# ---------- header(): sound/music state
rep('''  document.documentElement.lang = st.lang;
}''', '''  document.documentElement.lang = st.lang;
  const sb = document.getElementById("soundBtn"), mb = document.getElementById("musicBtn");
  sb.setAttribute("aria-pressed", String(st.soundOn)); sb.setAttribute("aria-label", l.soundL); sb.title = l.soundL;
  document.getElementById("soundWaves").style.opacity = st.soundOn ? 1 : .2;
  mb.setAttribute("aria-pressed", String(st.musicOn)); mb.setAttribute("aria-label", l.musicL); mb.title = l.musicL;
}''')

# ---------- map: animals living on the islands
rep('''      ${pin(722, 248, "strategist")}
      ${label("strategist", 650, 394)}
    </g>
  </svg>`;''', '''      ${pin(722, 248, "strategist")}
      ${label("strategist", 650, 394)}
    </g>
    <g class="pets idle">
      ${[["kepi", 52, 316, .26], ["oyen", 362, 168, .2], ["cici", 446, 118, .13], ["rangga", 648, 172, .22], ["nyu", 268, 392, .28]].map(([k, x, y, sc]) =>
        `<g class="pet-map" data-action="pet" data-v="${k}" role="button" tabindex="0" aria-label="${PET_NAME[k]}" transform="translate(${x} ${y}) scale(${sc})">${ART[k]}</g>`).join("")}
    </g>
  </svg>`;''')

# ---------- map head: avatar picker; daily card shows Nyu
rep('''      <div class="legend"><span><i class="dot"></i><b>${l.legendS}</b> · ${l.legendSd}</span><span><i class="sq"></i><b>${l.legendB}</b> · ${l.legendBd}</span></div></div>''',
'''      <div class="legend"><span><i class="dot"></i><b>${l.legendS}</b> · ${l.legendSd}</span><span><i class="sq"></i><b>${l.legendB}</b> · ${l.legendBd}</span></div>
      <div class="picker"><span>${l.yourDet}</span>${["raka", "laras"].map(k => `<button class="who-btn" data-action="avatar" data-v="${k}" aria-pressed="${st.avatar === k}"><span class="face">${portrait(k)}</span>${k === "raka" ? "Raka" : "Laras"}</button>`).join("")}</div></div>''')
rep('''      <span class="ico b"><svg viewBox="0 0 24 24" aria-hidden="true"><rect x="3" y="5" width="18" height="16" rx="3" fill="none" stroke="currentColor" stroke-width="2"/><path d="M3 10 H21 M8 3 V7 M16 3 V7" stroke="currentColor" stroke-width="2" stroke-linecap="round"/><rect x="7" y="13" width="4" height="4" rx="1" fill="currentColor"/></svg></span>''',
'''      <span class="ico pal">${portrait("nyu")}</span>''')

# ---------- feedback with the helper animal
rep('''const fbBox = (good, text) => `<div class="fb ${good ? "good" : "bad"}" role="status"><b>${good ? L().correct : L().notQuite}</b><span>${text}</span></div>`;''',
'''const fbBox = (good, text) => {
  const h = HELPER[st.screen];
  if (!h) return `<div class="fb ${good ? "good" : "bad"}" role="status"><b>${good ? L().correct : L().notQuite}</b><span>${text}</span></div>`;
  return `<div class="fb helper ${good ? "good" : "bad"}" role="status"><button class="pet-mini idle" data-action="pet" data-v="${h}" aria-label="${PET_NAME[h]}">${figure(h)}</button>
    <div class="say"><span class="who">${L().helperSays(PET_NAME[h])}</span><span><b>${good ? L().correct : L().notQuite}</b> ${text}</span></div></div>`;
};''')

# ---------- result screens: player + helper celebrate
rep('''  return `<div class="result first"><span class="kicker">${l.resK}</span><h2>${title}</h2>''',
'''  return `<div class="result first"><div class="hero-row idle">${figure(st.avatar)}${figure(HELPER[st.screen] || "oyen", "pal")}${k === "detective" ? figure("bayu") : ""}</div><span class="kicker">${l.resK}</span><h2>${title}</h2>''')
rep('''  return `<div class="result"><span class="kicker build">${l.resKB}</span><h2>${x.resT}</h2>''',
'''  return `<div class="result"><div class="hero-row idle">${figure(st.avatar)}${figure(HELPER[st.screen] || "kepi", "pal")}</div><span class="kicker build">${l.resKB}</span><h2>${x.resT}</h2>''')

# ---------- suspects get their portraits
rep('''<span class="av" style="background:${AVC[k]}">${d.sus[k].n.split(" ").pop()[0]}</span>''', '''<span class="av pic idle">${portrait(k)}</span>''', 2)

# ---------- sounds in the boat run
rep('''    b.running = false;
    b.fb = "short";
    return render();''', '''    b.running = false;
    b.fb = "short";
    sfx("ui-wrong");
    return render();''')
rep('''    b.running = false; b.fb = "crash"; b.bad = b.step; b.crashAt = [nx, ny];
    return render();''', '''    b.running = false; b.fb = "crash"; b.bad = b.step; b.crashAt = [nx, ny];
    sfx("boat-bonk"); sfx("kepi-snap", 350);
    return render();''')
rep('''    b.running = false; b.done = true;
    if (b.mode === "daily") dailySolved(); else markBuilt("explorer");
    return render();
  }
  render();''', '''    b.running = false; b.done = true;
    sfx("boat-arrive");
    if (b.mode === "daily") dailySolved(); else { markBuilt("explorer"); sfx("badge-earned", 900); }
    return render();
  }
  sfx("boat-move");
  render();''')
rep('''function dailySolved() {
  st.dailyDone''', '''function dailySolved() {
  sfx("badge-earned", 500); sfx("nyu-blub", 1400);
  st.dailyDone''')

# ---------- sounds in the drawbridge run
rep('''      up = true; $("leaf")?.classList.add("up");''', '''      up = true; $("leaf")?.classList.add("up"); sfx("bridge-lift");''')
rep('''      $("alarm")?.classList.add("on");
      if (up)''', '''      $("alarm")?.classList.add("on"); sfx("bridge-alarm");
      if (up)''')
rep('''  const verdict = () => cap(`${x.out[r.got]} · ${r.pass ? x.good : x.bad}`, r.pass ? "ok" : "warn");''',
'''  const verdict = () => { cap(`${x.out[r.got]} · ${r.pass ? x.good : x.bad}`, r.pass ? "ok" : "warn"); sfx(r.pass ? "ui-correct" : "ui-wrong"); };''')
rep('''  if (b.results.every(r => r.pass)) { b.done = true; markBuilt("strategist"); }
  render();''', '''  if (b.results.every(r => r.pass)) { b.done = true; markBuilt("strategist"); sfx("badge-earned"); }
  else sfx("rangga-call", 300);
  render();''')

# ---------- sounds and new actions in act()
rep('''  const d = st.det, e = st.exp, s = st.str, be = st.be, bd = st.bd, bs = st.bs;
  switch (a) {''', '''  const d = st.det, e = st.exp, s = st.str, be = st.be, bd = st.bd, bs = st.bs;
  if (TAP.has(a)) sfx("ui-tap");
  switch (a) {
    case "sound": st.soundOn = !st.soundOn; try { localStorage.setItem("mi-sound", st.soundOn ? "on" : "off"); } catch (err) {} if (st.soundOn) sfx("ui-tap"); return render();
    case "music": setMusic(!st.musicOn); return render();
    case "avatar": st.avatar = v; try { localStorage.setItem("mi-avatar", v); } catch (err) {} return render();
    case "pet": sfx(VOICE[v]); wiggle(el); return;''')
rep('''function act(el) {''', '''const TAP = new Set(["home", "parent", "lang", "island", "open", "d-step", "d-sus", "d-ev", "e-step", "s-step", "be-add", "be-rm", "be-clear", "bd-slot", "bd-place", "bd-next", "dy-tier", "dy-day", "bs-open", "bs-cond", "bs-swap", "avatar"]);
function act(el) {''')
rep('''    case "d-see": if (!d.seen.includes(v)) d.seen.push(v); return render();''',
'''    case "d-see": if (!d.seen.includes(v)) { d.seen.push(v); sfx("notebook-write"); } return render();''')
rep('''      else { d.fb = null; d.step = 3; }
      return render();''', '''      else { d.fb = null; d.step = 3; }
      if (d.fb) { sfx("ui-wrong"); sfx("oyen-meow", 350); } else sfx("ui-correct");
      return render();''')
rep('''    case "d-why": d.why = +v; if (L().d.why[+v].ok) { solve("detective"); d.step = 4; } return render();''',
'''    case "d-why": d.why = +v; if (L().d.why[+v].ok) { solve("detective"); d.step = 4; sfx("badge-earned"); sfx("oyen-purr", 900); } else { sfx("ui-wrong"); sfx("oyen-meow", 350); } return render();''')
rep('''    case "e-pick": if (v === "tri") { e.step = "why"; e.fb = null; } else e.fb = true; return render();
    case "e-why": e.why = +v; return render();''', '''    case "e-pick": if (v === "tri") { e.step = "why"; e.fb = null; sfx("ui-correct"); } else { e.fb = true; sfx("ui-wrong"); sfx("kepi-snap", 350); } return render();
    case "e-why": e.why = +v; sfx(L().e.why[+v].ok ? "ui-correct" : "ui-wrong"); return render();''')
rep('''    case "e-pick2": if (v === "5") { e.step = "done"; solve("explorer"); } else e.fb = true; return render();
    case "s-flag": if (!s.flags.includes(v)) s.flags.push(v); s.last = v; return render();''', '''    case "e-pick2": if (v === "5") { e.step = "done"; solve("explorer"); sfx("badge-earned"); sfx("kepi-snap", 900); } else { e.fb = true; sfx("ui-wrong"); } return render();
    case "s-flag": if (!s.flags.includes(v)) s.flags.push(v); s.last = v; sfx(["urgent", "source", "spread", "hide"].includes(v) ? "clue-found" : "ui-wrong"); return render();''')
rep('''    case "s-dec": s.dec = +v; if (L().s.dec[+v].ok) { s.step = "done"; solve("strategist"); } return render();''',
'''    case "s-dec": s.dec = +v; if (L().s.dec[+v].ok) { s.step = "done"; solve("strategist"); sfx("badge-earned"); sfx("rangga-call", 900); } else { sfx("ui-wrong"); sfx("rangga-call", 350); } return render();''')
rep('''    case "bd-tog": { const c = curCircuit().b; c.vals[v] = !c.vals[v]; return render(); }''',
'''    case "bd-tog": {
      const { b: c, lv } = curCircuit(), before = nodeVal(lv, c.slots, c.vals, lv.out);
      c.vals[v] = !c.vals[v];
      sfx(!before && nodeVal(lv, c.slots, c.vals, lv.out) ? "lamp-on" : "ui-tap");
      return render();
    }''')
rep('''      if (Object.keys(lv.slots).some(k => !c.slots[k])) { c.fb = true; return render(); }''',
'''      if (Object.keys(lv.slots).some(k => !c.slots[k])) { c.fb = true; sfx("ui-wrong"); return render(); }''')
rep('''      if (c.results.every(r => r.pass)) {
        c.lvlDone = true;''', '''      if (!c.results.every(r => r.pass)) { sfx("ui-wrong"); sfx(st.screen === "daily" ? "nyu-blub" : "cici-chirp", 350); }
      if (c.results.every(r => r.pass)) {
        c.lvlDone = true; sfx("lamp-on");
        if (st.screen !== "daily" && bd.lvl === LV.length - 1) sfx("badge-earned", 700);''')
rep('''    case "open-daily": openDaily(); return go("daily");''', '''    case "open-daily": openDaily(); sfx("daily-chime"); sfx("nyu-blub", 700); return go("daily");''')

# drag and drop ends with a tap sound
rep('''  cleanupDrag();
  suppressClick = true;''', '''  cleanupDrag();
  sfx("ui-tap");
  suppressClick = true;''')

open(P, "w").write(s)
print("ok")

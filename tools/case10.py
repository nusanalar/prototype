import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:90])
    s = s.replace(a, b)

EN = r'''    e2: {
      kicker: "Picture case #10 · Pattern Isle", title: "Who Bit the Kue?", tags: "Look closely · Match the prints",
      body: "Nenek Ijah made kue lapis for story time. Now one piece has a bite in it! Who did it?",
      giverSays: "Nenek Ijah says", giver: "\"Help me find out, little detective!\"", start: "Let's look!", listen: "Listen",
      lookT: "Look closely", lookS: "Tap every picture.",
      sus: { oyen: { n: "Oyen the cat", s: "Oyen loves food!" }, cici: { n: "Cici the gecko", s: "Cici can climb walls." }, nyu: { n: "Nyu the turtle", s: "Nyu lives in the sea." } },
      clue: { prints: { n: "Footprints", s: "Tiny footprints in the flour." }, bite: { n: "The bite", s: "A very small bite." }, window: { n: "The window", s: "A tiny open window, high on the wall." } },
      need: n => `Tap ${n} more`, toMatch: "Match the prints →",
      matchT: "Whose feet?", matchS: "Look at the footprints. Which feet match?",
      feet: { paw: "Cat paw", gecko: "Gecko toes", flipper: "Turtle flipper" },
      matchOk: "They match! Little round toes, just like a gecko.", matchNo: "Look again. Count the toes and look at their shape.", toWho: "Who did it? →",
      whoQ: "Who bit the kue?", whoNo: { oyen: "Oyen loves food, but these are not paw prints.", nyu: "Nyu lives in the sea and has flippers, not toes." }, whoOk: "Yes! It was Cici!",
      whyQ: "How do you know?",
      why: [
        { t: "The footprints match Cici's toes.", ok: true, icon: "gecko" },
        { t: "Cici is green.", f: "Colour is not a clue here. Look at the footprints!", icon: "color" },
        { t: "I guessed.", f: "Guessing is OK to start. Now use the clues!", icon: "guess" }
      ],
      resT: "Cici says sorry",
      story: "Cici climbed in through the tiny window because the kue smelled so good. \"Sorry, Nenek!\" Nenek Ijah laughs, cuts the kue into pieces, and shares it with everyone at story time.",
      lesson: "Explorer lesson: footprints are a pattern. Look closely and match them!",
      badge: "Print Matcher", gain: "+ Patterns   + Evidence",
      steps: ["Story", "Look", "Match", "Who?", "Why?", "Done"]
    },
'''
ID = r'''    e2: {
      kicker: "Kasus gambar #10 · Pulau Pola", title: "Siapa yang Menggigit Kue?", tags: "Amati · Cocokkan jejak",
      body: "Nenek Ijah membuat kue lapis untuk waktu dongeng. Sekarang ada satu potong yang tergigit! Siapa pelakunya?",
      giverSays: "Kata Nenek Ijah", giver: "\"Aduh, Cuu... bantu Nenek cari tahu, ya, detektif kecil!\"", start: "Ayo amati!", listen: "Dengar",
      lookT: "Amati baik-baik", lookS: "Ketuk setiap gambar.",
      sus: { oyen: { n: "Oyen si kucing", s: "Oyen suka makanan!" }, cici: { n: "Cici si cicak", s: "Cici bisa memanjat dinding." }, nyu: { n: "Nyu si penyu", s: "Nyu tinggal di laut." } },
      clue: { prints: { n: "Jejak kaki", s: "Jejak kaki kecil di tepung." }, bite: { n: "Gigitannya", s: "Gigitan yang sangat kecil." }, window: { n: "Jendela", s: "Jendela kecil terbuka, tinggi di dinding." } },
      need: n => `Ketuk ${n} lagi`, toMatch: "Cocokkan jejak →",
      matchT: "Kaki siapa?", matchS: "Lihat jejaknya. Kaki mana yang cocok?",
      feet: { paw: "Telapak kucing", gecko: "Jari cicak", flipper: "Sirip penyu" },
      matchOk: "Cocok! Jari kecil yang bulat, seperti cicak.", matchNo: "Lihat lagi. Hitung jarinya dan lihat bentuknya.", toWho: "Siapa pelakunya? →",
      whoQ: "Siapa yang menggigit kue?", whoNo: { oyen: "Oyen suka makanan, tapi ini bukan jejak kucing.", nyu: "Nyu tinggal di laut dan punya sirip, bukan jari." }, whoOk: "Betul! Pelakunya Cici!",
      whyQ: "Bagaimana kamu tahu?",
      why: [
        { t: "Jejaknya cocok dengan jari Cici.", ok: true, icon: "gecko" },
        { t: "Cici berwarna hijau.", f: "Warna bukan petunjuk di sini. Lihat jejaknya!", icon: "color" },
        { t: "Aku menebak.", f: "Menebak boleh untuk mulai. Sekarang pakai petunjuknya!", icon: "guess" }
      ],
      resT: "Cici minta maaf",
      story: "Cici masuk lewat jendela kecil karena kuenya wangi sekali. \"Maaf, Nek!\" Nenek Ijah tertawa, memotong kue, dan membagikannya kepada semua saat waktu dongeng.",
      lesson: "Pelajaran penjelajah: jejak kaki itu pola. Amati baik-baik dan cocokkan!",
      badge: "Pencocok Jejak", gain: "+ Pola   + Bukti",
      steps: ["Cerita", "Amati", "Cocokkan", "Siapa?", "Kenapa?", "Selesai"]
    },
'''
i = s.index("    e: {\n      kicker: \"Pattern Isle · Explorer\"")
s = s[:i] + EN + s[i:]
i = s.index("    e: {\n      kicker: \"Pulau Pola · Penjelajah\"")
s = s[:i] + ID + s[i:]

rep('''        strategist2: "\\"If you saw a shocking photo online, how would you check whether it's real before sharing it?\\""''',
    '''        strategist2: "\\"If you saw a shocking photo online, how would you check whether it's real before sharing it?\\"",
        explorer2: "\\"Can you find footprints or tracks around our house? Whose are they?\\""''')
rep('''        strategist2: "\\"Kalau kamu melihat foto mengejutkan di internet, bagaimana cara mengecek apakah itu asli sebelum membagikannya?\\""''',
    '''        strategist2: "\\"Kalau kamu melihat foto mengejutkan di internet, bagaimana cara mengecek apakah itu asli sebelum membagikannya?\\"",
        explorer2: "\\"Bisakah kamu menemukan jejak kaki di sekitar rumah? Jejak siapa itu?\\""''')

rep('''  str2: { step: 0, seen: [], rated: {}, rfb: null, dec: null, why: null },''',
    '''  str2: { step: 0, seen: [], rated: {}, rfb: null, dec: null, why: null },
  exp2: { step: 0, seen: [], match: null, who: null, why: null },''')
rep('''const HELPER = { detective: "oyen", detective2: "oyen", strategist2: "rangga",''', '''const HELPER = { detective: "oyen", detective2: "oyen", strategist2: "rangga", explorer2: "kepi",''')
rep('''const FRESH_KEY = { strategist2: "str2",''', '''const FRESH_KEY = { explorer2: "exp2", strategist2: "str2",''')

rep('''${k === "strategist" ? case9Row() : ""}''', '''${k === "strategist" ? case9Row() : ""}${k === "explorer" ? case10Row() : ""}''')
rep('''function case9Row() {''', '''function case10Row() {
  const l = L(), done = !!st.solved.explorer2;
  return `<button class="act" data-action="open" data-case="explorer2">
    <span class="ico s">${ICON.solve}</span>
    <span><span class="mode">${l.solveL} · #10</span><span class="nm">${l.e2.title}</span><span class="tg">${l.e2.tags}</span></span>
    <span class="chip ${done ? "ok" : ""}">${done ? l.solved : l.isNew}</span></button>`;
}
function case9Row() {''')
rep('''${k === "strategist2" ? figure("putri").replace("<svg ", '<svg data-mood="cheer" ') + figure("ratna").replace("<svg ", '<svg data-mood="yes" ') : ""}''',
    '''${k === "strategist2" ? figure("putri").replace("<svg ", '<svg data-mood="cheer" ') + figure("ratna").replace("<svg ", '<svg data-mood="yes" ') : ""}${k === "explorer2" ? figure("ijah").replace("<svg ", '<svg data-mood="yes" ') + figure("cici", "pal").replace("<svg ", '<svg data-mood="sad" ') : ""}''')

rep('''function renderExplorer() {''', r'''/* Read-aloud for young players: the browser's own voice reads short lines in Indonesian or English */
function speak(text) {
  if (!st.soundOn || !text) return;
  try {
    const synth = window.speechSynthesis; if (!synth) return;
    synth.cancel();
    const u = new SpeechSynthesisUtterance(text.replace(/[“”"]/g, ""));
    u.lang = st.lang === "id" ? "id-ID" : "en-US"; u.rate = .92; u.pitch = 1.1;
    synth.speak(u);
  } catch (e) {}
}
const escAttr = t => String(t).replace(/&/g, "&amp;").replace(/"/g, "&quot;");
const sayBtn = (text, label) => `<button class="say-btn" data-action="say" data-say="${escAttr(text)}" aria-label="${label}"><svg viewBox="0 0 24 24" aria-hidden="true"><path d="M4 9 H8 L13 5 V19 L8 15 H4 Z" fill="currentColor"/><path d="M16 9 Q18 12 16 15 M18.5 6.5 Q22 12 18.5 17.5" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/></svg></button>`;

const GECKO_PRINT = (x, y, r) => `<g transform="translate(${x} ${y}) rotate(${r})" fill="#8a6d3b" stroke="#8a6d3b" stroke-width="1.6" stroke-linecap="round"><circle r="3.2"/><path d="M0 0 L-7 -5 M0 0 L-4 -9 M0 0 L0 -10 M0 0 L4 -9 M0 0 L7 -5" fill="none"/><circle cx="-7" cy="-5" r="1.9"/><circle cx="-4" cy="-9" r="1.9"/><circle cx="0" cy="-10" r="1.9"/><circle cx="4" cy="-9" r="1.9"/><circle cx="7" cy="-5" r="1.9"/></g>`;
const PIC10 = {
  bite: '<svg viewBox="0 0 120 90" aria-hidden="true"><ellipse cx="60" cy="66" rx="52" ry="14" fill="#eef4f2"/><ellipse cx="60" cy="63" rx="44" ry="10" fill="#d6e2e6"/>' + [24, 52, 80].map((x, i) => `<g>${[0, 1, 2, 3, 4].map(j => `<rect x="${x}" y="${30 + j * 6}" width="22" height="6" fill="${j % 2 ? "#f2c46d" : "#b5651d"}"/>`).join("")}${i === 1 ? '<circle cx="74" cy="31" r="5" style="fill:var(--card-2)"/><circle cx="68" cy="29" r="4" style="fill:var(--card-2)"/>' : ""}</g>`).join("") + '</svg>',
  prints: '<svg viewBox="0 0 120 90" aria-hidden="true"><ellipse cx="60" cy="48" rx="52" ry="34" fill="#f3ead2"/>' + GECKO_PRINT(30, 66, 30) + GECKO_PRINT(48, 50, 20) + GECKO_PRINT(68, 40, 35) + GECKO_PRINT(88, 26, 25) + '</svg>',
  window: '<svg viewBox="0 0 120 90" aria-hidden="true"><rect width="120" height="90" rx="6" fill="#d9cdb8"/><rect x="72" y="10" width="30" height="24" rx="2" fill="#7fc8f8"/><rect x="70" y="8" width="34" height="28" rx="3" fill="none" stroke="#6b4f35" stroke-width="3"/><path d="M104 9 L116 14 V34 L104 36 Z" fill="#a0784f"/><rect x="0" y="66" width="120" height="24" fill="#c9b8a0"/><rect x="20" y="52" width="40" height="16" rx="2" fill="#a0784f"/></svg>',
};
const FEET10 = {
  paw: '<svg viewBox="0 0 80 80" aria-hidden="true"><path d="M40 70 Q22 70 22 56 Q24 44 40 44 Q56 44 58 56 Q58 70 40 70 Z" fill="#8a6d3b"/><ellipse cx="22" cy="34" rx="6" ry="8" fill="#8a6d3b"/><ellipse cx="34" cy="24" rx="6" ry="8" fill="#8a6d3b"/><ellipse cx="47" cy="24" rx="6" ry="8" fill="#8a6d3b"/><ellipse cx="59" cy="34" rx="6" ry="8" fill="#8a6d3b"/></svg>',
  gecko: '<svg viewBox="0 0 80 80" aria-hidden="true">' + GECKO_PRINT(40, 52, 0).replace('translate(40 52) rotate(0)', 'translate(40 52) scale(2.6)') + '</svg>',
  flipper: '<svg viewBox="0 0 80 80" aria-hidden="true"><path d="M20 22 Q50 14 64 40 Q70 58 54 64 Q36 66 24 48 Q14 34 20 22 Z" fill="#8a6d3b"/><path d="M30 30 Q46 30 54 46" stroke="#a8875a" stroke-width="2" fill="none"/></svg>',
};
const WHY_ICON10 = { gecko: FEET10.gecko, color: '<svg viewBox="0 0 80 80" aria-hidden="true"><circle cx="40" cy="40" r="26" fill="#9ed8a4"/></svg>', guess: '<svg viewBox="0 0 80 80" aria-hidden="true"><circle cx="40" cy="40" r="28" fill="#ffc857"/><path d="M31 32 Q32 22 40 22 Q50 22 50 31 Q50 37 43 40 Q40 42 40 47" stroke="#2b1d00" stroke-width="5" fill="none" stroke-linecap="round"/><circle cx="40" cy="57" r="3.5" fill="#2b1d00"/></svg>' };

function renderExplorer2() {
  const l = L(), x = l.e2, s = st.exp2;
  const steps = `<ol class="steps">${x.steps.map((t, i) => `<li class="${i < s.step ? "done" : i === s.step ? "now" : ""}">${i + 1}. ${t}</li>`).join("")}</ol>`;
  const say = t => sayBtn(t, x.listen);
  let body = "";
  if (s.step === 0) {
    body = `<div class="head"><span class="kicker">${x.kicker}</span><h2>${x.title} ${say(x.title + ". " + x.body)}</h2></div>
      <div class="story10"><div class="pic-big">${PIC10.bite}</div><p class="big-line">${x.body}</p></div>
      <div class="giver"><div class="giver-fig">${figure("ijah")}</div><div class="giver-say"><span class="who">${x.giverSays}</span><p>${x.giver} ${say(x.giver)}</p></div></div>
      <button class="primary big" data-action="e10-step" data-v="1">${x.start}</button>`;
  } else if (s.step === 1) {
    const keys = ["oyen", "cici", "nyu", "prints", "bite", "window"], need = Math.max(0, keys.length - s.seen.length);
    const tile = k => {
      const pet = !!x.sus[k], item = x.sus[k] || x.clue[k], seen = s.seen.includes(k);
      return `<button class="pic-tile ${seen ? "seen" : ""}" data-action="e10-see" data-v="${k}"><span class="pic-art ${pet ? "pet" : ""}">${pet ? figure(k) : PIC10[k]}</span>
        <b>${item.n}</b>${seen ? `<span class="pic-line">${item.s}</span>` : ""}${seen ? '<span class="tick">✓</span>' : ""}</button>`;
    };
    body = `<div class="head"><h2>${x.lookT} ${say(x.lookS)}</h2><p class="sub">${x.lookS}</p></div>
      <div class="pic-grid">${keys.map(tile).join("")}</div>
      <button class="primary big" data-action="e10-step" data-v="2" ${need ? "disabled" : ""}>${need ? x.need(need) : x.toMatch}</button>`;
  } else if (s.step === 2) {
    const ok = s.match === "gecko";
    body = `<div class="head"><h2>${x.matchT} ${say(x.matchS)}</h2><p class="sub">${x.matchS}</p></div>
      <div class="pic-big">${PIC10.prints}</div>
      <div class="feet">${["paw", "gecko", "flipper"].map(k => `<button class="foot ${s.match === k ? (k === "gecko" ? "right" : "wrong") : ""}" data-action="e10-match" data-v="${k}" ${ok ? "disabled" : ""}>${FEET10[k]}<b>${x.feet[k]}</b></button>`).join("")}</div>
      ${s.match ? fbBox(ok, ok ? x.matchOk : x.matchNo) : ""}
      ${ok ? `<button class="primary big" data-action="e10-step" data-v="3">${x.toWho}</button>` : ""}`;
  } else if (s.step === 3) {
    body = `<div class="head"><h2>${x.whoQ} ${say(x.whoQ)}</h2></div>
      <div class="pic-grid three">${["oyen", "cici", "nyu"].map(k => `<button class="pic-tile ${s.who === k ? (k === "cici" ? "right" : "wrong") : ""}" data-action="e10-who" data-v="${k}"><span class="pic-art pet">${figure(k)}</span><b>${x.sus[k].n}</b></button>`).join("")}</div>
      ${s.who && s.who !== "cici" ? fbBox(false, x.whoNo[s.who]) : ""}`;
  } else if (s.step === 4) {
    body = `${fbBox(true, x.whoOk)}<div class="head"><h2>${x.whyQ} ${say(x.whyQ)}</h2></div>
      <div class="why10">${x.why.map((w, i) => `<button class="why-card ${s.why === i ? (w.ok ? "right" : "wrong") : ""}" data-action="e10-why" data-v="${i}">${WHY_ICON10[w.icon]}<b>${w.t}</b></button>`).join("")}</div>
      ${s.why !== null && !x.why[s.why].ok ? fbBox(false, x.why[s.why].f) : ""}`;
  } else {
    body = solveResult("explorer2", x, x.resT, x.story).replace(`<h2>${x.resT}</h2>`, `<h2>${x.resT} ${say(x.resT + ". " + x.story)}</h2>`);
  }
  $app.innerHTML = stage(steps + body);
}

function renderExplorer() {''')
rep('''  detective: renderDetective, detective2: renderDetective2, strategist2: renderStrategist2,''',
    '''  detective: renderDetective, detective2: renderDetective2, strategist2: renderStrategist2, explorer2: renderExplorer2,''')

# actions
rep('''    case "c9-step": st.str2.step = +v; return go("strategist2");''', '''    case "say": speak(el.dataset.say); return;
    case "e10-step": {
      st.exp2.step = +v; go("explorer2");
      const x = L().e2; speak([x.body, x.lookS, x.matchS, x.whoQ][+v] || "");
      return;
    }
    case "e10-see": {
      const c = st.exp2, x = L().e2, fresh = !c.seen.includes(v);
      if (fresh) c.seen.push(v);
      render();
      const pv = { oyen: "oyen-meow", cici: "cici-chirp", nyu: "nyu-blub" }[v];
      if (pv) { sfx(pv); playMove(document.querySelector(`[data-action="e10-see"][data-v="${v}"] svg[data-slug]`), "happy"); } else sfx("clue-found");
      speak((x.sus[v] || x.clue[v]).s);
      return;
    }
    case "e10-match": {
      const c = st.exp2, x = L().e2; c.match = v;
      if (v === "gecko") { sfx("ui-correct"); sfx("kepi-snap", 400); speak(x.matchOk); } else { sfx("ui-wrong"); sfx("kepi-snap", 350); speak(x.matchNo); }
      return render();
    }
    case "e10-who": {
      const c = st.exp2, x = L().e2; c.who = v;
      if (v === "cici") { c.step = 4; c.why = null; sfx("sting-surprised"); sfx("cici-chirp", 500); speak(x.whoOk + " " + x.whyQ); }
      else { sfx("ui-wrong"); speak(x.whoNo[v]); }
      render();
      if (v !== "cici") playMove(document.querySelector(`[data-action="e10-who"][data-v="${v}"] svg[data-slug]`), "no");
      return;
    }
    case "e10-why": {
      const c = st.exp2, x = L().e2; c.why = +v;
      if (x.why[+v].ok) { solve("explorer2"); c.step = 5; sfx("badge-earned"); sfx("kepi-snap", 900); speak(x.resT + ". " + x.lesson); }
      else { sfx("ui-wrong"); speak(x.why[+v].f); }
      return render();
    }
    case "c9-step": st.str2.step = +v; return go("strategist2");''')
rep('''      if (k === "strategist2") {''', '''      if (k === "explorer2") { sfx("kepi-snap", 150); sfx("voice-nenek-ijah", 700); speak(L().e2.title + ". " + L().e2.body); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "wave"), 300); }
      if (k === "strategist2") {''')

# skills, badges
rep('''  if (st.solved.strategist2) { v[5] += 15; v[3] += 8; v[4] += 8; }''', '''  if (st.solved.strategist2) { v[5] += 15; v[3] += 8; v[4] += 8; }
  if (st.solved.explorer2) { v[0] += 12; v[3] += 8; }''')
rep('''st.solved.strategist2 ? badge(l.s2.badge) : ""].filter(Boolean);''', '''st.solved.strategist2 ? badge(l.s2.badge) : "", st.solved.explorer2 ? badge(l.e2.badge) : ""].filter(Boolean);''')

# styles: picture-first layout
rep('''/* Parent */
.parent {''', '''/* Case 10: picture-first for ages 6 to 9 */
.say-btn { width: 34px; height: 34px; border-radius: 50%; border: 0; background: var(--lantern); color: #2b1d00; cursor: pointer; display: inline-grid; place-items: center; vertical-align: middle; margin-left: 6px; flex: 0 0 auto; }
.say-btn svg { width: 18px; height: 18px; }
.primary.big { font-size: 1.15rem; padding: 14px 26px; border-radius: 16px; }
.story10 { display: grid; grid-template-columns: minmax(0, 260px) minmax(0, 1fr); gap: 16px; align-items: center; }
.pic-big { background: var(--card-2); border-radius: 18px; padding: 10px; max-width: 360px; }
.pic-big svg { width: 100%; height: auto; display: block; }
.big-line { font-size: 1.2rem; line-height: 1.5; font-weight: 500; max-width: 34ch; }
.pic-grid { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.pic-tile { position: relative; background: var(--card-2); border: 3px solid transparent; border-radius: 18px; padding: 12px; cursor: pointer; display: grid; gap: 6px; justify-items: center; text-align: center; font-size: 1rem; }
.pic-tile:hover { border-color: var(--line); }
.pic-tile.seen { border-color: color-mix(in srgb, var(--palm) 55%, transparent); }
.pic-tile.right { border-color: var(--palm); }
.pic-tile.wrong { border-color: var(--coral); }
.pic-art { width: 100%; max-width: 150px; aspect-ratio: 4 / 3; display: grid; place-items: center; }
.pic-art svg { width: 100%; height: 100%; display: block; }
.pic-art.pet svg { width: auto; height: 100%; }
.pic-line { font-size: .95rem; color: var(--ink); }
.tick { position: absolute; top: 8px; right: 10px; width: 26px; height: 26px; border-radius: 50%; background: var(--palm); color: #0b2338; display: grid; place-items: center; font-weight: 800; }
.feet { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; max-width: 560px; }
.foot { background: #f3ead2; color: #2b2416; border: 4px solid transparent; border-radius: 18px; padding: 10px; cursor: pointer; display: grid; gap: 4px; justify-items: center; font-size: .95rem; }
.foot svg { width: 100%; max-width: 96px; height: auto; }
.foot.right { border-color: var(--palm); }
.foot.wrong { border-color: var(--coral); }
.foot:disabled { cursor: default; }
.why10 { display: grid; grid-template-columns: repeat(3, minmax(0, 1fr)); gap: 12px; }
.why-card { background: var(--card-2); border: 3px solid transparent; border-radius: 18px; padding: 14px; cursor: pointer; display: grid; gap: 8px; justify-items: center; text-align: center; font-size: 1rem; }
.why-card svg { width: 72px; height: 72px; }
.why-card.right { border-color: var(--palm); }
.why-card.wrong { border-color: var(--coral); }
@media (max-width: 680px) { .story10 { grid-template-columns: minmax(0, 1fr); } .pic-grid, .why10 { grid-template-columns: repeat(2, minmax(0, 1fr)); } .pic-grid.three { grid-template-columns: repeat(3, minmax(0, 1fr)); } }

/* Parent */
.parent {''')
open(P, "w").write(s)
print("ok")

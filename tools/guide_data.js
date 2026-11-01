/* Guidance for kids: first-time onboarding, a mission card on every activity, and a lesson the child saves at the end */
const GUIDE = {
  en: {
    help: "How to play", startHere: "Start here",
    next: "Next", prev: "Back", skip: "Skip", go: "Let's go!",
    onb: [
      { t: "Welcome to Nusa Nalar!", b: "Hi! Let's become island detectives. First, pick your detective." },
      { t: "The islands have gone dark", b: "A storm put out the lamps on the islands. Each island has two tasks. Every task you finish lights a lamp again.",
        items: [["s", "Solve", "Find clues and evidence to crack the mystery."], ["b", "Build", "Put steps and rules in order to fix what's broken."]] },
      { t: "Why is this good for you?", b: "Every task trains your brain, and you can use it every day:",
        items: [["1", "You don't fall for fake news easily", ""], ["2", "You can explain your reasons clearly", ""], ["3", "You can solve problems step by step", ""]],
        foot: "At the end of every task, save what you learned in My Learning Book." },
      { t: "Animal friends are here to help", b: "If you're stuck, Oyen, Kepi, Cici, Nyu and Rangga give you hints. Mistakes are okay. Just try again!" },
      { t: "How old are you?", b: "We'll mark the best island to start on.", ages: ["6–9", "10–13", "14–17"] }
    ],
    mTitle: "Your mission", mSkill: "You practise", mWhy: "How it helps you",
    lk: "Your lesson", useQ: "When could you use this lesson?", noWrong: "Pick one. There's no wrong answer.",
    save: "I get it! Save it", saved: "Saved in My Learning Book. You'll use it:", savedSay: "Great! Your lesson is saved in your learning book.", openBook: "Open My Learning Book",
    book: { t: "My Learning Book", k: "Lessons you saved", sub: "Every finished task gives you one lesson. Save it, then try it in real life!",
      count: n => `${n}/9 lessons saved`, cta: "Open →", locked: "Finish this task to unlock its lesson.", play: "Play", willUse: "I'll use it:" },
    par: { t: "Lessons your child saved", none: "None yet. Lessons appear here after your child saves them.", tip: "Ask: \"When did you last use this?\"" },
    m: {
      explorer: { goal: "Find what repeats in the train's cars and choose the next one.", skill: "Patterns: spotting what repeats.", why: "Patterns help with counting, music, reading and math.",
        uses: ["When I count or do math", "When I learn a song or a dance", "When I tidy my toys or things"] },
      explorer2: { goal: "Look at the footprints and the bite, then match them to the right animal.", skill: "Observing: looking closely and matching.", why: "You notice small things that others miss.",
        uses: ["When I look for something I lost", "When I compare pictures in a book", "When I play outside and spot animal tracks"] },
      "b-explorer": { goal: "Line up arrows, step by step, to guide the boat home around the rocks.", skill: "Planning steps in the right order.", why: "You can follow and give clear directions.",
        uses: ["When I give directions to a friend", "When I follow a recipe or instructions", "When I plan my way to school"] },
      detective: { goal: "Find out who took the lighthouse lamp. Talk to everyone, collect clues, check a witness with numbers, then point to the person the clues lead to.", skill: "Evidence: deciding from clues and numbers, not guesses.", why: "You stay fair and don't blame someone without proof.",
        uses: ["When something goes missing at home or school", "When friends argue about who did something", "When I hear a story and want to know if it's true"] },
      detective2: { goal: "Put what everyone did in time order to find when the jar disappeared and who was there.", skill: "Timelines: putting events in order.", why: "You can plan your day and check if a story makes sense.",
        uses: ["When I plan homework and play time", "When someone's story about the day doesn't add up", "When I tell a teacher or parent what happened"] },
      "b-detective": { goal: "Choose the right switch blocks so the lamp turns on at exactly the right times.", skill: "Rules and logic: \"both\", \"either\", \"opposite\".", why: "You think through \"what if\" before you decide.",
        uses: ["When I decide if I can go out (homework done AND not raining)", "When I make the rules for a game with friends", "When I check every possibility before choosing"] },
      strategist: { goal: "Read the panicky chat message, tap its warning signs, then decide what to do.", skill: "Spotting warning signs in messages.", why: "You stay calm and smart when scary messages spread.",
        uses: ["When a chain message says \"share this now!\"", "When a post uses ALL CAPS and lots of !!!", "When I'm not sure and ask a trusted adult"] },
      strategist2: { goal: "Check where the viral photo really came from before deciding whether to share it.", skill: "Checking sources: who posted it, when, and what others say.", why: "You don't spread hoaxes, and you protect people you care about.",
        uses: ["Before I forward a message in a family group", "When I see a shocking photo or video online", "When a friend says \"everyone knows\""] },
      "b-strategist": { goal: "Read the problem report, test the bridge, find the wrong step and fix it.", skill: "Fixing problems: find the cause, change one thing, test again.", why: "You fix problems calmly instead of guessing.",
        uses: ["When an app or game on my phone stops working", "When my school project doesn't turn out right", "When a plan with friends goes wrong"] }
    }
  },
  id: {
    help: "Cara bermain", startHere: "Mulai di sini",
    next: "Lanjut", prev: "Kembali", skip: "Lewati", go: "Ayo mulai!",
    onb: [
      { t: "Selamat datang di Nusa Nalar!", b: "Halo! Ayo jadi detektif pulau. Pilih detektifmu dulu." },
      { t: "Pulau-pulau sedang gelap", b: "Badai memadamkan lampu di pulau-pulau. Di setiap pulau ada dua tugas. Setiap tugas yang selesai menyalakan lampunya lagi.",
        items: [["s", "Pecahkan", "Cari petunjuk dan bukti untuk memecahkan misteri."], ["b", "Bangun", "Susun langkah dan aturan untuk memperbaiki yang rusak."]] },
      { t: "Kenapa ini bagus untukmu?", b: "Setiap tugas melatih otakmu, dan kamu bisa memakainya setiap hari:",
        items: [["1", "Tidak gampang percaya kabar bohong", ""], ["2", "Bisa menjelaskan alasanmu dengan jelas", ""], ["3", "Bisa memecahkan masalah langkah demi langkah", ""]],
        foot: "Di akhir setiap tugas, simpan pelajaranmu di Buku Pelajaranku." },
      { t: "Teman hewan siap membantu", b: "Kalau bingung, Oyen, Kepi, Cici, Nyu, dan Rangga memberi petunjuk. Salah itu tidak apa-apa. Coba lagi, ya!" },
      { t: "Berapa umurmu?", b: "Kami tandai pulau yang cocok untuk mulai.", ages: ["6–9", "10–13", "14–17"] }
    ],
    mTitle: "Misimu", mSkill: "Kamu berlatih", mWhy: "Gunanya untukmu",
    lk: "Pelajaranmu", useQ: "Kapan kamu bisa memakai pelajaran ini?", noWrong: "Pilih satu. Tidak ada jawaban yang salah.",
    save: "Aku paham! Simpan", saved: "Tersimpan di Buku Pelajaranku. Kamu akan memakainya:", savedSay: "Hebat! Pelajaranmu sudah tersimpan di buku pelajaranmu.", openBook: "Buka Buku Pelajaranku",
    book: { t: "Buku Pelajaranku", k: "Pelajaran yang kamu simpan", sub: "Setiap tugas yang selesai memberi satu pelajaran. Simpan, lalu coba pakai di dunia nyata!",
      count: n => `${n}/9 pelajaran tersimpan`, cta: "Buka →", locked: "Selesaikan tugas ini untuk membuka pelajarannya.", play: "Mainkan", willUse: "Aku akan memakainya:" },
    par: { t: "Pelajaran yang disimpan anak", none: "Belum ada. Pelajaran muncul di sini setelah anak menyimpannya.", tip: "Tanyakan: \"Kapan terakhir kamu memakai ini?\"" },
    m: {
      explorer: { goal: "Temukan apa yang berulang di gerbong kereta, lalu pilih gerbong berikutnya.", skill: "Pola: menemukan yang berulang.", why: "Pola membantumu berhitung, bermusik, membaca, dan belajar matematika.",
        uses: ["Saat berhitung atau belajar matematika", "Saat belajar lagu atau tarian", "Saat merapikan mainan atau barang"] },
      explorer2: { goal: "Lihat jejak kaki dan bekas gigitan, lalu cocokkan dengan hewan yang benar.", skill: "Mengamati: melihat dengan teliti lalu mencocokkan.", why: "Kamu jadi memperhatikan hal kecil yang sering terlewat.",
        uses: ["Saat mencari barang yang hilang", "Saat membandingkan gambar di buku", "Saat bermain di luar dan melihat jejak hewan"] },
      "b-explorer": { goal: "Susun panah langkah demi langkah untuk memandu perahu pulang melewati batu.", skill: "Merencanakan langkah dengan urutan yang benar.", why: "Kamu bisa mengikuti dan memberi petunjuk arah dengan jelas.",
        uses: ["Saat memberi petunjuk arah ke teman", "Saat mengikuti resep atau petunjuk", "Saat merencanakan jalan ke sekolah"] },
      detective: { goal: "Cari tahu siapa yang mengambil lampu mercusuar. Ajak bicara semua warga, kumpulkan petunjuk, lalu tunjuk orang yang sesuai dengan petunjuk.", skill: "Bukti: memutuskan dari petunjuk dan angka, bukan tebakan.", why: "Kamu bersikap adil dan tidak menuduh tanpa bukti.",
        uses: ["Saat ada barang hilang di rumah atau sekolah", "Saat teman-teman ribut soal siapa yang melakukan sesuatu", "Saat mendengar cerita dan ingin tahu apakah itu benar"] },
      detective2: { goal: "Susun apa yang dilakukan setiap orang menurut waktu, untuk tahu kapan toples hilang dan siapa yang ada di sana.", skill: "Garis waktu: menyusun kejadian berurutan.", why: "Kamu bisa mengatur harimu dan mengecek apakah sebuah cerita masuk akal.",
        uses: ["Saat mengatur waktu PR dan main", "Saat cerita seseorang tentang harinya tidak cocok", "Saat menceritakan kejadian ke guru atau orang tua"] },
      "b-detective": { goal: "Pilih blok saklar yang tepat supaya lampu menyala tepat pada waktunya.", skill: "Aturan dan logika: \"keduanya\", \"salah satu\", \"kebalikan\".", why: "Kamu memikirkan \"bagaimana kalau\" sebelum memutuskan.",
        uses: ["Saat memutuskan boleh main (PR selesai DAN tidak hujan)", "Saat membuat aturan main bersama teman", "Saat mengecek semua kemungkinan sebelum memilih"] },
      strategist: { goal: "Baca pesan berantai yang bikin panik, ketuk tanda bahayanya, lalu putuskan apa yang harus dilakukan.", skill: "Mengenali tanda bahaya dalam pesan.", why: "Kamu tetap tenang dan cerdas saat pesan menakutkan menyebar.",
        uses: ["Saat pesan berantai bilang \"sebarkan sekarang!\"", "Saat unggahan pakai HURUF BESAR dan banyak !!!", "Saat ragu lalu bertanya ke orang dewasa yang dipercaya"] },
      strategist2: { goal: "Cek dari mana foto viral itu sebenarnya berasal sebelum memutuskan untuk membagikannya.", skill: "Cek sumber: siapa yang mengunggah, kapan, dan apa kata sumber lain.", why: "Kamu tidak ikut menyebarkan hoaks dan melindungi orang yang kamu sayangi.",
        uses: ["Sebelum meneruskan pesan di grup keluarga", "Saat melihat foto atau video yang mengejutkan di internet", "Saat teman bilang \"semua orang sudah tahu\""] },
      "b-strategist": { goal: "Baca laporan masalah, uji jembatan, temukan langkah yang salah, lalu perbaiki.", skill: "Memperbaiki masalah: cari penyebab, ubah satu hal, uji lagi.", why: "Kamu memperbaiki masalah dengan tenang, bukan menebak.",
        uses: ["Saat aplikasi atau game di HP tidak jalan", "Saat tugas sekolah hasilnya belum benar", "Saat rencana bersama teman berantakan"] }
    }
  }
};
const G = () => GUIDE[st.lang];
const LEARN_ORDER = ["explorer", "explorer2", "b-explorer", "detective", "detective2", "b-detective", "strategist", "strategist2", "b-strategist"];
const LEARN_TIER = { explorer: "explorer", explorer2: "explorer", "b-explorer": "explorer", detective: "detective", detective2: "detective", "b-detective": "detective", strategist: "strategist", strategist2: "strategist", "b-strategist": "strategist" };
const LESSON_SRC = { explorer: "e", explorer2: "e2", "b-explorer": "be", detective: "d", detective2: "d2", "b-detective": "bd", strategist: "s", strategist2: "s2", "b-strategist": "bs" };
const actTitle = k => { const l = L(); return { detective2: l.d2.title, strategist2: l.s2.title, explorer2: l.e2.title }[k] || (k.startsWith("b-") ? l.bTitle[k.slice(2)] : l.title[k]); };
const lessonOf = k => L()[LESSON_SRC[k]].lesson;
const isDone = k => k.startsWith("b-") ? !!st.built[k.slice(2)] : !!st.solved[k];
function saveLearn() { try { localStorage.setItem("mi-learn", JSON.stringify(st.learned)); } catch (e) {} }

/* Mission card at the top of every activity: what to do, the skill, why it matters */
function missionCard() {
  const k = st.screen, m = G().m[k];
  if (!m) return "";
  const open = st.missionOpen[k] !== false;
  return `<details class="mission" data-k="${k}" ${open ? "open" : ""}><summary><span class="m-ico" aria-hidden="true">${ICON_TARGET}</span><span class="m-k">${G().mTitle}</span><span class="m-goal">${m.goal}</span></summary>
    <div class="m-body"><div><span class="m-l">${G().mSkill}</span><p>${m.skill}</p></div><div><span class="m-l">${G().mWhy}</span><p>${m.why}</p></div>${sayBtn(m.goal + " " + m.why, G().mTitle)}</div></details>`;
}
const ICON_TARGET = '<svg viewBox="0 0 24 24" width="18" height="18"><circle cx="12" cy="12" r="9" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="5" fill="none" stroke="currentColor" stroke-width="2"/><circle cx="12" cy="12" r="1.8" fill="currentColor"/></svg>';
const ICON_BOOK = '<svg viewBox="0 0 24 24" width="22" height="22" aria-hidden="true"><path d="M4 5.5 C4 4.7 4.7 4 5.5 4 H11 V20 H5.5 C4.7 20 4 19.3 4 18.5 Z M13 4 H18.5 C19.3 4 20 4.7 20 5.5 V18.5 C20 19.3 19.3 20 18.5 20 H13 Z" fill="currentColor"/></svg>';

/* End of every activity: the child picks when they'd use the lesson, then saves it */
function learnCard() {
  const k = st.screen, m = G().m[k];
  if (!m) return "";
  const got = st.learned[k];
  if (got) return `<div class="learn done"><span class="kicker">${G().lk}</span><p>✓ ${G().saved} <b>${m.uses[got.use]}</b></p><button class="secondary" data-action="learnbook">${G().openBook}</button></div>`;
  const pick = st.learnPick[k];
  return `<div class="learn"><span class="kicker">${G().lk}</span><h3>${G().useQ} ${sayBtn(G().useQ + " " + m.uses.join(". "), G().useQ)}</h3><p class="note">${G().noWrong}</p>
    <div class="uses">${m.uses.map((u, i) => `<button class="use-opt" data-action="learn-pick" data-v="${i}" aria-pressed="${pick === i}">${u}</button>`).join("")}</div>
    <button class="primary" data-action="learn-save" ${pick == null ? "disabled" : ""}>${G().save}</button></div>`;
}

function renderLearn() {
  const l = L(), b = G().book, n = LEARN_ORDER.filter(k => st.learned[k]).length;
  const entry = k => {
    const m = G().m[k], got = st.learned[k];
    return `<div class="lb-item ${got ? "got" : "locked"}"><span class="lb-ico ${k.startsWith("b-") ? "b" : "s"}">${k.startsWith("b-") ? ICON.build : ICON.solve}</span><div>
      <span class="mode">${l.tier[LEARN_TIER[k]]}</span><h3>${actTitle(k)}</h3><p class="lb-skill">${m.skill}</p>
      ${got ? `<p class="lb-lesson">${lessonOf(k)}</p><p class="lb-use"><b>${b.willUse}</b> ${m.uses[got.use]}</p>` : `<p class="note">${b.locked}</p><button class="secondary" data-action="open" data-case="${k}">${b.play}</button>`}
    </div></div>`;
  };
  $app.innerHTML = stage(`<div class="head"><span class="kicker">${b.k}</span><h2>${b.t}</h2><p class="sub">${b.sub}</p><p class="lb-count">${b.count(n)}</p></div>
    <div class="lb-list">${LEARN_ORDER.map(entry).join("")}</div>`);
}

/* First-time onboarding: a short, spoken walk-through that can be skipped and replayed */
function renderOnb() {
  let o = document.getElementById("onb");
  if (st.onb == null) { if (o) o.remove(); return; }
  if (!o) { o = document.createElement("div"); o.id = "onb"; o.className = "onb"; o.setAttribute("role", "dialog"); o.setAttribute("aria-modal", "true"); document.body.appendChild(o); }
  const g = G(), i = st.onb, s = g.onb[i], last = i === g.onb.length - 1;
  let extra = "";
  if (i === 0) extra = `<div class="onb-pick">${["raka", "laras"].map(k => `<button class="who-btn big" data-action="onb-avatar" data-v="${k}" aria-pressed="${st.avatar === k}"><span class="face">${portrait(k)}</span>${k === "raka" ? "Raka" : "Laras"}</button>`).join("")}</div>`;
  if (s.items) extra = `<ul class="onb-items">${s.items.map(([ic, t, d]) => `<li><span class="onb-ic ${ic}">${ic === "s" ? ICON.solve : ic === "b" ? ICON.build : ic}</span><span><b>${t}</b>${d ? `<br>${d}` : ""}</span></li>`).join("")}</ul>${s.foot ? `<p class="onb-foot">${ICON_BOOK} ${s.foot}</p>` : ""}`;
  if (i === 3) extra = `<div class="onb-pets">${["oyen", "kepi", "cici", "nyu", "rangga"].map(k => `<span class="onb-pet">${figure(k)}<small>${PET_NAME[k]}</small></span>`).join("")}</div>`;
  if (s.ages) extra = `<div class="onb-ages">${s.ages.map((a, j) => `<button class="age-btn" data-action="onb-age" data-v="${ORDER[j]}" aria-pressed="${st.ageTier === ORDER[j]}"><b>${a}</b><small>${L().isl[ORDER[j]]}</small></button>`).join("")}</div>`;
  o.innerHTML = `<div class="onb-card"><div class="onb-dots">${g.onb.map((_, j) => `<i class="${j === i ? "on" : j < i ? "done" : ""}"></i>`).join("")}</div>
    <h2>${s.t} ${sayBtn(s.t + ". " + s.b, s.t)}</h2><p class="sub">${s.b}</p>${extra}
    <div class="onb-btns"><button class="btn-ghost" data-action="onb-skip">${g.skip}</button>${i > 0 ? `<button class="secondary" data-action="onb-prev">${g.prev}</button>` : ""}
      <button class="primary" data-action="${last ? "onb-done" : "onb-next"}" ${last && !st.ageTier ? "disabled" : ""}>${last ? g.go : g.next}</button></div></div>`;
}
function onbSay() { const s = G().onb[st.onb]; if (s) sayAs("narrator", s.t + ". " + s.b); }
function onbClose() { st.onb = null; try { localStorage.setItem("mi-onboard", "done"); } catch (e) {} render(); }
document.addEventListener("toggle", ev => { const d = ev.target; if (d.classList && d.classList.contains("mission")) st.missionOpen[d.dataset.k] = d.open; }, true);

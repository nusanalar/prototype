import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:90])
    s = s.replace(a, b)

EN = r'''    s2: {
      kicker: "Case file #09 · News Port", title: "The Viral Beach Photo", tags: "Sources · Fact-check", resK: "Story published",
      body: "It's Thursday morning. A photo of Pattern Isle beach covered in trash is spreading fast, with the caption: \"Pattern Isle beach TODAY. Bu Ratna's warung festival ruined it!\" People are angry, and some want Saturday's festival cancelled.",
      giverSays: "Kak Putri says", giver: "\"My editor wants a story by noon. Do we publish the photo? Help me check it first.\"",
      goal: "Your goal: check every source, decide what News Port should publish, and explain why.",
      post: { user: "@pulau_fakta_88", caption: "Pattern Isle beach TODAY. Bu Ratna's warung festival RUINED it! Share before they delete this!!", stats: "2,340 shares · posted 1 hour ago", viral: "Viral" },
      sus: {
        darto: { n: "Pak Darto", r: "Ferry captain, eyewitness", s: "\"I sailed past Pattern Isle beach at 8 this morning. It was clean. Kepi was sunbathing on the sand.\"" },
        ijah: { n: "Nenek Ijah", r: "Storyteller grandma", s: "\"That photo reminds me of the big storm two years ago. The whole coast looked like that, but on another island.\"" }
      },
      clue: {
        poster: { n: "Account check", s: "@pulau_fakta_88 was created yesterday. No name, no photo, 40 posts in one hour, all about the festival." },
        search: { n: "Reverse image search", s: "The same photo was first published two years ago by a news site, about a storm on a different island." },
        webcam: { n: "Harbor webcam, 9:00 today", s: "Live picture of Pattern Isle beach: clean sand, blue sky." },
        weather: { n: "Weather log", s: "Thursday: sunny, no wind. The photo shows dark storm clouds." },
        comment: { n: "Top comment", s: "\"My cousin saw the trash too!!! Everyone knows it's true.\"" }
      },
      csT: "Check the sources", csS: "Is each source solid enough to build a news story on? Tap Reliable or Not reliable.", rel: "Reliable", unrel: "Not reliable",
      rateWhy: {
        poster: "No name, created yesterday, posting nonstop. You can't check who is behind it.",
        comment: "An unnamed cousin can't be checked, and \"everyone knows\" is not evidence.",
        search: "It shows where and when the photo really comes from.",
        webcam: "A live camera at a known place and time. Anyone can check it.",
        darto: "A named eyewitness who was there this morning and can be asked again."
      },
      csDone: "All sources checked. Three reliable sources say the photo is old and the beach is clean today.", csNext: "Decide what to publish",
      dcQ: "What should News Port publish today?",
      dec: [
        { t: "The photo, with the headline \"Festival ruins beach!\"", f: "That spreads a false claim and hurts Bu Ratna. Reliable sources say the opposite." },
        { t: "Nothing. It's just a rumor, so ignore it.", f: "Many people already believe it. Staying quiet lets the rumor grow." },
        { t: "A fact-check: \"This photo is two years old and from another island. The beach is clean today.\"", ok: true }
      ],
      whyQ: "Why is the viral post false?",
      why: [
        { t: "The photo is two years old and from another island, the webcam shows a clean beach today, and the festival hasn't even happened yet.", ok: true },
        { t: "Because it was posted by an account with no name.", f: "That's a warning sign, but not proof. What do the reliable sources show?" },
        { t: "Because Bu Ratna is kind, so she wouldn't make a mess.", f: "Liking someone isn't evidence. What do the photo's date and the webcam say?" }
      ],
      resT: "The fact-check wins",
      story: "News Port publishes Kak Putri's fact-check with the webcam picture and the original two-year-old photo. Within an hour, people start sharing the truth instead. The account deletes its post. On Saturday the warung festival goes ahead, and everyone helps keep the beach clean, Kepi included.",
      lesson: "Strategist lesson: before you share, check who posted it, when the photo is really from, and what other sources say. A clear fact-check stops a rumor better than silence.",
      badge: "Fact Checker", gain: "+ Checking sources   + Evidence   + Explaining why",
      steps: ["Brief", "Investigate", "Check sources", "Decide", "Explain", "Published"]
    },
'''
ID = r'''    s2: {
      kicker: "Berkas kasus #09 · Pelabuhan Berita", title: "Foto Pantai yang Viral", tags: "Sumber · Cek fakta", resK: "Berita terbit",
      body: "Kamis pagi. Foto Pantai Pulau Pola yang penuh sampah menyebar cepat dengan keterangan: \"Pantai Pulau Pola HARI INI. Festival warung Bu Ratna merusaknya!\" Orang-orang marah, dan sebagian ingin festival hari Sabtu dibatalkan.",
      giverSays: "Kata Kak Putri", giver: "\"Redakturku minta beritanya sebelum siang. Apa kita terbitkan fotonya? Bantu aku mengeceknya dulu.\"",
      goal: "Tujuanmu: cek setiap sumber, putuskan apa yang harus diterbitkan Pelabuhan Berita, dan jelaskan alasannya.",
      post: { user: "@pulau_fakta_88", caption: "Pantai Pulau Pola HARI INI. Festival warung Bu Ratna MERUSAKNYA! Sebarkan sebelum dihapus!!", stats: "2.340 kali dibagikan · diunggah 1 jam lalu", viral: "Viral" },
      sus: {
        darto: { n: "Pak Darto", r: "Kapten feri, saksi mata", s: "\"Aku berlayar melewati Pantai Pulau Pola jam 8 pagi tadi. Pantainya bersih. Kepi sedang berjemur di pasir.\"" },
        ijah: { n: "Nenek Ijah", r: "Nenek pendongeng", s: "\"Cuu... foto itu mengingatkan Nenek pada badai besar dua tahun lalu. Seluruh pantai terlihat seperti itu, tapi di pulau lain, Cu.\"" }
      },
      clue: {
        poster: { n: "Cek akun", s: "@pulau_fakta_88 dibuat kemarin. Tanpa nama, tanpa foto, 40 unggahan dalam satu jam, semuanya tentang festival." },
        search: { n: "Pencarian gambar", s: "Foto yang sama pertama kali diterbitkan dua tahun lalu oleh situs berita, tentang badai di pulau lain." },
        webcam: { n: "Kamera pelabuhan, 09.00 hari ini", s: "Gambar langsung Pantai Pulau Pola: pasir bersih, langit biru." },
        weather: { n: "Catatan cuaca", s: "Kamis: cerah, tanpa angin. Di foto ada awan badai gelap." },
        comment: { n: "Komentar teratas", s: "\"Sepupuku juga lihat sampahnya!!! Semua orang tahu itu benar.\"" }
      },
      csT: "Cek sumbernya", csS: "Apakah setiap sumber cukup kuat untuk dijadikan dasar berita? Ketuk Bisa dipercaya atau Tidak bisa dipercaya.", rel: "Bisa dipercaya", unrel: "Tidak bisa dipercaya",
      rateWhy: {
        poster: "Tanpa nama, baru dibuat kemarin, mengunggah terus-menerus. Kamu tidak bisa mengecek siapa di baliknya.",
        comment: "Sepupu tanpa nama tidak bisa dicek, dan \"semua orang tahu\" bukan bukti.",
        search: "Ini menunjukkan dari mana dan kapan foto itu sebenarnya berasal.",
        webcam: "Kamera langsung di tempat dan waktu yang jelas. Siapa pun bisa mengeceknya.",
        darto: "Saksi mata yang jelas namanya, ada di sana pagi ini, dan bisa ditanya lagi."
      },
      csDone: "Semua sumber sudah dicek. Tiga sumber yang bisa dipercaya bilang fotonya lama dan pantainya bersih hari ini.", csNext: "Putuskan apa yang diterbitkan",
      dcQ: "Apa yang sebaiknya diterbitkan Pelabuhan Berita hari ini?",
      dec: [
        { t: "Foto itu, dengan judul \"Festival merusak pantai!\"", f: "Itu menyebarkan klaim palsu dan merugikan Bu Ratna. Sumber yang bisa dipercaya mengatakan sebaliknya." },
        { t: "Tidak ada. Itu cuma kabar burung, abaikan saja.", f: "Banyak orang sudah memercayainya. Diam saja membuat kabar burung makin besar." },
        { t: "Cek fakta: \"Foto ini berumur dua tahun dan dari pulau lain. Pantainya bersih hari ini.\"", ok: true }
      ],
      whyQ: "Kenapa unggahan viral itu salah?",
      why: [
        { t: "Fotonya berumur dua tahun dan dari pulau lain, kamera pelabuhan menunjukkan pantai bersih hari ini, dan festivalnya bahkan belum terjadi.", ok: true },
        { t: "Karena diunggah oleh akun tanpa nama.", f: "Itu tanda bahaya, tapi bukan bukti. Apa yang ditunjukkan sumber yang bisa dipercaya?" },
        { t: "Karena Bu Ratna baik, jadi dia tidak akan membuat berantakan.", f: "Menyukai seseorang bukan bukti. Apa kata tanggal foto dan kamera pelabuhan?" }
      ],
      resT: "Cek fakta menang",
      story: "Pelabuhan Berita menerbitkan cek fakta Kak Putri dengan gambar kamera pelabuhan dan foto asli dua tahun lalu. Dalam satu jam, orang-orang mulai membagikan kebenarannya. Akun itu menghapus unggahannya. Hari Sabtu festival warung tetap berjalan, dan semua orang membantu menjaga pantai tetap bersih, termasuk Kepi.",
      lesson: "Pelajaran ahli strategi: sebelum membagikan, cek siapa yang mengunggah, kapan foto itu sebenarnya diambil, dan apa kata sumber lain. Cek fakta yang jelas menghentikan kabar burung lebih baik daripada diam.",
      badge: "Pemeriksa Fakta", gain: "+ Cek sumber   + Bukti   + Menjelaskan alasan",
      steps: ["Briefing", "Selidiki", "Cek sumber", "Putuskan", "Jelaskan", "Terbit"]
    },
'''
i = s.index("    e: {\n      kicker: \"Pattern Isle · Explorer\"")
s = s[:i] + EN + s[i:]
i = s.index("    e: {\n      kicker: \"Pulau Pola · Penjelajah\"")
s = s[:i] + ID + s[i:]

rep('''        detective2: "\\"What did you do yesterday afternoon, in order? Let's make a timeline together.\\""''',
    '''        detective2: "\\"What did you do yesterday afternoon, in order? Let's make a timeline together.\\"",
        strategist2: "\\"If you saw a shocking photo online, how would you check whether it's real before sharing it?\\""''')
rep('''        detective2: "\\"Apa saja yang kamu lakukan kemarin sore, sesuai urutannya? Ayo buat garis waktunya bersama.\\""''',
    '''        detective2: "\\"Apa saja yang kamu lakukan kemarin sore, sesuai urutannya? Ayo buat garis waktunya bersama.\\"",
        strategist2: "\\"Kalau kamu melihat foto mengejutkan di internet, bagaimana cara mengecek apakah itu asli sebelum membagikannya?\\""''')

rep('''  det2: { step: 0, seen: [], order: [], tlfb: null, suspect: null, ev: [], fb: null, why: null },''',
    '''  det2: { step: 0, seen: [], order: [], tlfb: null, suspect: null, ev: [], fb: null, why: null },
  str2: { step: 0, seen: [], rated: {}, rfb: null, dec: null, why: null },''')
rep('''const HELPER = { detective: "oyen", detective2: "oyen",''', '''const HELPER = { detective: "oyen", detective2: "oyen", strategist2: "rangga",''')
rep('''  ratna: "voice-bu-ratna", darto: "voice-pak-darto", putri: "voice-kak-putri", joko: "voice-mas-joko", hasan: "voice-pak-hasan" };''',
    '''  ratna: "voice-bu-ratna", darto: "voice-pak-darto", putri: "voice-kak-putri", joko: "voice-mas-joko", hasan: "voice-pak-hasan", ijah: "voice-nenek-ijah" };''')
rep('''const FRESH_KEY = { detective2: "det2",''', '''const FRESH_KEY = { strategist2: "str2", detective2: "det2",''')

# map row on the News Port card
rep('''${k === "detective" ? case2Row() : ""}''', '''${k === "detective" ? case2Row() : ""}${k === "strategist" ? case9Row() : ""}''')
rep('''const fbBox = (good, text) => {''', '''function case9Row() {
  const l = L(), done = !!st.solved.strategist2;
  return `<button class="act" data-action="open" data-case="strategist2">
    <span class="ico s">${ICON.solve}</span>
    <span><span class="mode">${l.solveL} · #09</span><span class="nm">${l.s2.title}</span><span class="tg">${l.s2.tags}</span></span>
    <span class="chip ${done ? "ok" : ""}">${done ? l.solved : l.isNew}</span></button>`;
}
const fbBox = (good, text) => {''')

# result screen
rep('''${k === "detective2" ? figure("darto").replace("<svg ", '<svg data-mood="sad" ') + figure("hasan").replace("<svg ", '<svg data-mood="cheer" ') : ""}</div><span class="kicker">${l.resK}</span>''',
    '''${k === "detective2" ? figure("darto").replace("<svg ", '<svg data-mood="sad" ') + figure("hasan").replace("<svg ", '<svg data-mood="cheer" ') : ""}${k === "strategist2" ? figure("putri").replace("<svg ", '<svg data-mood="cheer" ') + figure("ratna").replace("<svg ", '<svg data-mood="yes" ') : ""}</div><span class="kicker">${x.resK || l.resK}</span>''')

# renderer
rep('''function renderExplorer() {''', r'''const CLUE9 = {
  poster: '<circle cx="13" cy="10" r="5" fill="#9bb5c3"/><path d="M4 23 Q4 15 13 15 Q22 15 22 23 Z" fill="#9bb5c3"/><circle cx="20" cy="6" r="5" fill="#ff8a74"/><path d="M18.6 4.6 Q20 3 21.4 4.6 Q21.4 6 20 6.4 V7.2" stroke="#15324c" stroke-width="1.3" fill="none" stroke-linecap="round"/>',
  search: '<rect x="3" y="4" width="15" height="12" rx="1.5" fill="#d6eefc"/><path d="M3 14 L8 9 L12 13 L15 10 L18 13 V16 H3 Z" fill="#9bb5c3"/><circle cx="17" cy="16" r="5" fill="none" stroke="#ffc857" stroke-width="2.2"/><path d="M20.5 19.5 L24 23" stroke="#ffc857" stroke-width="2.6" stroke-linecap="round"/>',
  webcam: '<rect x="5" y="5" width="16" height="11" rx="3" fill="#4a5b6b"/><circle cx="13" cy="10.5" r="3.6" fill="#7fc8f8" stroke="#eef4f2" stroke-width="1.4"/><circle cx="19" cy="7.5" r="1.2" fill="#ff8a74"/><path d="M13 16 V23 M8 23 H18" stroke="#9bb5c3" stroke-width="2" stroke-linecap="round"/>',
  weather: '<circle cx="10" cy="10" r="5" fill="#ffc857"/><path d="M10 2 V3.5 M10 16.5 V18 M2 10 H3.5 M16.5 10 H18 M4.4 4.4 L5.4 5.4 M14.6 14.6 L15.6 15.6" stroke="#ffc857" stroke-width="1.6" stroke-linecap="round"/><path d="M9 22 Q9 17 14 17 Q15 13 19 14 Q23 14 23 18 Q25 19 24 22 Z" fill="#eef4f2"/>',
  comment: '<path d="M3 5 H23 V17 H12 L7 22 V17 H3 Z" fill="#eef4f2"/><path d="M7 9 H19 M7 13 H15" stroke="#9bb5c3" stroke-width="1.6" stroke-linecap="round"/><path d="M20 10 V12.5 M20 14.5 V15" stroke="#ff8a74" stroke-width="1.8" stroke-linecap="round"/>'
};
const TRASH_PHOTO = '<svg viewBox="0 0 320 170" aria-hidden="true"><defs><linearGradient id="tpSky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#3b4452"/><stop offset="1" stop-color="#6b7280"/></linearGradient></defs><rect width="320" height="170" fill="url(#tpSky)"/><ellipse cx="80" cy="34" rx="60" ry="16" fill="#2b313b"/><ellipse cx="230" cy="26" rx="80" ry="18" fill="#2b313b"/><rect y="78" width="320" height="34" fill="#3b5568"/><path d="M0 104 Q160 92 320 104 V170 H0 Z" fill="#a8997a"/><g fill="#1e232b"><ellipse cx="60" cy="130" rx="18" ry="12"/><ellipse cx="96" cy="140" rx="14" ry="10"/><ellipse cx="170" cy="126" rx="20" ry="12"/><ellipse cx="240" cy="138" rx="16" ry="11"/><ellipse cx="280" cy="124" rx="12" ry="8"/></g><g fill="#7fc8f8" opacity=".8"><rect x="130" y="140" width="10" height="4" rx="2" transform="rotate(-20 135 142)"/><rect x="200" y="150" width="12" height="4" rx="2" transform="rotate(15 206 152)"/><rect x="30" y="150" width="9" height="4" rx="2"/></g><g fill="#ff8a74" opacity=".7"><rect x="120" y="118" width="8" height="5" rx="1"/><rect x="260" y="150" width="7" height="5" rx="1"/></g></svg>';
const RATE9 = { poster: "unrel", comment: "unrel", search: "rel", webcam: "rel", darto: "rel" };

function renderStrategist2() {
  const l = L(), d = l.d, x = l.s2, s = st.str2;
  const steps = `<ol class="steps">${x.steps.map((t, i) => `<li class="${i < s.step ? "done" : i === s.step ? "now" : ""}">${i + 1}. ${t}</li>`).join("")}</ol>`;
  const PEOPLE9 = ["darto", "ijah"], CLUES9 = ["poster", "search", "webcam", "weather", "comment"];
  const art = k => x.sus[k] ? `<span class="av pic">${portrait(k)}</span>` : `<span class="av clue"><svg viewBox="0 0 26 26" aria-hidden="true">${CLUE9[k]}</svg></span>`;
  const nameOf = k => (x.sus[k] || x.clue[k]).n;
  const post = `<div class="vpost"><div class="vpost-h"><span class="vpost-av"></span><b>${x.post.user}</b><span class="chip">${x.post.viral}</span></div>${TRASH_PHOTO}<p>${x.post.caption}</p><span class="role">${x.post.stats}</span></div>`;
  let body = "";
  if (s.step === 0) {
    body = `<div class="head"><span class="kicker">${x.kicker}</span><h2>${x.title}</h2><p class="sub">${x.body}</p></div>
      <div class="brief9">${post}<div class="giver col"><div class="giver-fig">${figure("putri")}</div><div class="giver-say"><span class="who">${x.giverSays}</span><p>${x.giver}</p></div></div></div>
      <div class="goal">${x.goal}</div>
      <button class="primary" data-action="c9-step" data-v="1">${d.start}</button>`;
  } else if (s.step === 1) {
    const need = Math.max(0, 6 - s.seen.length);
    const item = k => `<button class="item ${s.seen.includes(k) ? "seen" : ""}" data-action="c9-see" data-v="${k}">${art(k)}
        <span><span class="name">${nameOf(k)}</span>${x.sus[k] ? ` <span class="role">· ${x.sus[k].r}</span>` : ""}
        ${s.seen.includes(k) ? `<p class="said">${(x.sus[k] || x.clue[k]).s}</p>` : `<p class="hint">${x.sus[k] ? d.listen : d.inspect}</p>`}</span></button>`;
    const nbItem = k => `<li><b>${nameOf(k)}:</b> ${(x.sus[k] || x.clue[k]).s}</li>`;
    body = `<div class="head"><h2>${d.invT}</h2><p class="sub">${d.invS}</p></div>
      <div class="inv">
        <div class="col"><span class="col-t">${d.people}</span>${PEOPLE9.map(item).join("")}
          <span class="col-t" style="margin-top:6px">${d.clues}</span>${CLUES9.map(item).join("")}</div>
        <div class="notebook"><h3>${d.nb}</h3>${s.seen.length ? `<ul>${s.seen.map(nbItem).join("")}</ul>` : `<p class="empty">${d.nbEmpty}</p>`}</div>
      </div>
      <button class="primary" data-action="c9-step" data-v="2" ${need ? "disabled" : ""}>${need ? d.need(need) : x.csT + " →"}</button>`;
  } else if (s.step === 2) {
    const keys = ["poster", "webcam", "comment", "search", "darto"], done = keys.every(k => s.rated[k]);
    const row = k => {
      const ok = s.rated[k], wrongHere = s.rfb && s.rfb.k === k && !s.rfb.ok;
      return `<div class="rate-row ${ok ? "ok" : ""} ${wrongHere ? "bad" : ""}">${art(k)}
        <div class="rate-body"><b>${nameOf(k)}</b><span>${(x.sus[k] || x.clue[k]).s}</span>${ok || wrongHere ? `<em>${ok ? "✓ " : ""}${x.rateWhy[k]}</em>` : ""}</div>
        <div class="rate-btns">${ok ? `<span class="chip ${RATE9[k] === "rel" ? "ok" : ""}">${RATE9[k] === "rel" ? x.rel : x.unrel}</span>` :
          `<button class="ev" data-action="c9-rate" data-v="${k}" data-r="rel">${x.rel}</button><button class="ev" data-action="c9-rate" data-v="${k}" data-r="unrel">${x.unrel}</button>`}</div></div>`;
    };
    body = `<div class="head"><h2>${x.csT}</h2><p class="sub">${x.csS}</p></div>
      <div class="rate-list">${keys.map(row).join("")}</div>
      ${s.rfb && !s.rfb.ok ? fbBox(false, x.rateWhy[s.rfb.k]) : done ? fbBox(true, x.csDone) : ""}
      ${done ? `<button class="primary" data-action="c9-step" data-v="3">${x.csNext}</button>` : ""}`;
  } else if (s.step === 3) {
    body = `<div class="head"><h2>${x.dcQ}</h2></div>${post}
      <div class="answers">${x.dec.map((o, i) => `<button class="ans ${s.dec === i ? (o.ok ? "right" : "wrong") : ""}" data-action="c9-dec" data-v="${i}">${o.t}</button>`).join("")}</div>
      ${s.dec !== null && !x.dec[s.dec].ok ? fbBox(false, x.dec[s.dec].f) : ""}`;
  } else if (s.step === 4) {
    body = `<div class="head"><h2>${d.whyT}</h2><p class="q">${x.whyQ}</p></div>
      <div class="answers">${x.why.map((w, i) => `<button class="ans ${s.why === i ? (w.ok ? "right" : "wrong") : ""}" data-action="c9-why" data-v="${i}">${w.t}</button>`).join("")}</div>
      ${s.why !== null && !x.why[s.why].ok ? fbBox(false, x.why[s.why].f) : ""}`;
  } else {
    body = solveResult("strategist2", x, x.resT, x.story);
  }
  $app.innerHTML = stage(steps + body);
}

function renderExplorer() {''')
rep('''  detective: renderDetective, detective2: renderDetective2,''', '''  detective: renderDetective, detective2: renderDetective2, strategist2: renderStrategist2,''')

# actions
rep('''    case "c2-step": st.det2.step = +v; return go("detective2");''', '''    case "c9-step": st.str2.step = +v; return go("strategist2");
    case "c9-see": {
      const c = st.str2, fresh = !c.seen.includes(v);
      if (fresh) c.seen.push(v);
      render();
      if (VOICE_P[v]) { sfx(VOICE_P[v]); playMove(document.querySelector(`[data-action="c9-see"][data-v="${v}"] svg[data-slug]`), "talk"); }
      if (fresh) sfx(VOICE_P[v] ? "notebook-write" : "clue-found", VOICE_P[v] ? 900 : 0);
      return;
    }
    case "c9-rate": {
      const c = st.str2, ok = RATE9[v] === el.dataset.r;
      c.rfb = { k: v, ok };
      if (ok) { c.rated[v] = true; sfx(Object.keys(RATE9).every(k => c.rated[k]) ? "ui-correct" : "clue-found"); }
      else { sfx("ui-wrong"); sfx("rangga-call", 350); }
      return render();
    }
    case "c9-dec": {
      const c = st.str2; c.dec = +v;
      if (L().s2.dec[+v].ok) { sfx("ui-correct"); c.step = 4; c.why = null; } else { sfx("ui-wrong"); sfx("rangga-call", 350); }
      return render();
    }
    case "c9-why": {
      const c = st.str2; c.why = +v;
      if (L().s2.why[+v].ok) { solve("strategist2"); c.step = 5; sfx("news-sting"); sfx("badge-earned", 900); sfx("rangga-call", 1900); }
      else { sfx("ui-wrong"); sfx("rangga-call", 350); }
      return render();
    }
    case "c2-step": st.det2.step = +v; return go("detective2");''')
rep('''const TAP = new Set(["c2-step",''', '''const TAP = new Set(["c9-step", "c2-step",''')
rep('''      if (k === "detective2") { sfx("market-hello", 150); sfx("voice-bu-ratna", 900); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "no"), 300); }''',
    '''      if (k === "detective2") { sfx("market-hello", 150); sfx("voice-bu-ratna", 900); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "no"), 300); }
      if (k === "strategist2") { sfx("news-sting", 150); sfx("voice-kak-putri", 1200); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "think"), 500); }''')

# skills, badges
rep('''  if (st.solved.detective2) { v[2] += 12; v[3] += 10; v[0] += 12; v[4] += 8; }''', '''  if (st.solved.detective2) { v[2] += 12; v[3] += 10; v[0] += 12; v[4] += 8; }
  if (st.solved.strategist2) { v[5] += 15; v[3] += 8; v[4] += 8; }''')
rep('''  const extra = st.solved.detective2 ? [badge(l.d2.badge)] : [];''', '''  const extra = [st.solved.detective2 ? badge(l.d2.badge) : "", st.solved.strategist2 ? badge(l.s2.badge) : ""].filter(Boolean);''')

# styles
rep('''/* Parent */
.parent {''', '''/* Case 9: viral post and source check */
.brief9 { display: grid; grid-template-columns: minmax(0, 1fr) minmax(0, 1fr); gap: 16px; align-items: end; }
.giver.col { flex-direction: column; align-items: flex-start; }
.vpost { background: #f5f7fa; color: #1e232b; border-radius: 16px; padding: 12px; display: grid; gap: 8px; max-width: 380px; box-shadow: 0 6px 18px rgba(0,0,0,.25); }
.vpost-h { display: flex; align-items: center; gap: 8px; font-size: .85rem; }
.vpost-av { width: 28px; height: 28px; border-radius: 50%; background: #c3ccd6; }
.vpost .chip { margin-left: auto; background: #ffe1d9; color: #c0392b; }
.vpost svg { width: 100%; height: auto; display: block; border-radius: 10px; }
.vpost p { font-size: .9rem; font-weight: 500; }
.vpost .role { color: #5b6573; }
.rate-list { display: grid; gap: 8px; }
.rate-row { display: grid; grid-template-columns: 56px minmax(0, 1fr) auto; gap: 12px; align-items: center; background: var(--card-2); border: 2px solid transparent; border-radius: 14px; padding: 10px 12px; }
.rate-row.ok { border-color: color-mix(in srgb, var(--palm) 50%, transparent); }
.rate-row.bad { border-color: color-mix(in srgb, var(--coral) 60%, transparent); }
.rate-body { display: grid; gap: 2px; font-size: .88rem; min-width: 0; }
.rate-body span { color: var(--muted); }
.rate-body em { font-style: normal; color: var(--ink); font-size: .84rem; }
.rate-row.ok .rate-body em { color: var(--palm); }
.rate-btns { display: flex; gap: 6px; flex-wrap: wrap; justify-content: flex-end; }
@media (max-width: 760px) { .brief9 { grid-template-columns: minmax(0, 1fr); } .rate-row { grid-template-columns: 48px minmax(0, 1fr); } .rate-btns { grid-column: 1 / -1; justify-content: flex-start; } }

/* Parent */
.parent {''')
open(P, "w").write(s)
print("ok")

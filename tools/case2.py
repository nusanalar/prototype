import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "mystery-isles.html")
s = open(P).read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:90])
    s = s.replace(a, b)

EN = r'''    d2: {
      kicker: "Case file #08 · Harbor Town, Lighthouse Isle", title: "The Vanishing Donation Jar", tags: "Timeline · Alibis",
      body: "Bu Ratna's warung had a jar of coins for the island school's new library. At 3:30 pm yesterday, during a sudden rainstorm, the jar disappeared from the counter. Three islanders were around the harbor that afternoon.",
      goal: "Your goal: put the afternoon in the right order, then find out who took the jar and prove it.",
      giverSays: "Bu Ratna says", giver: "\"Please help! Pak Hasan was going to buy storybooks with that money.\"",
      sus: {
        joko: { n: "Mas Joko", r: "Mail carrier", s: "\"I brought Bu Ratna a letter at 2 pm. The jar was so full! After that I was at the post office all afternoon, stamping letters.\"" },
        darto: { n: "Pak Darto", r: "Ferry captain", s: "\"I bought a coffee at 3 pm, then my ferry left at 3:10 sharp. I was out at sea when the jar went missing.\"" },
        putri: { n: "Kak Putri", r: "Junior reporter", s: "\"I was taking photos of the rain for News Port. I photographed the warung at 3:20, then walked back to the office.\"" }
      },
      clue: {
        ticket: { n: "Harbor board", s: "\"3:10 ferry: DELAYED by rain. Left at 3:40.\"" },
        photo: { n: "Kak Putri's photo, 3:20", s: "The jar is still on the counter. A big navy umbrella leans by the door." },
        umbrella: { n: "Navy umbrella", s: "Left at the warung door. It has a ferry company badge on the handle." },
        stamp: { n: "Post office log", s: "Letters stamped by Mas Joko at 2:30, 3:00, 3:15, 3:30 and 3:45." },
        coin: { n: "Coin trail", s: "Three coins on the path from the warung to the harbor." }
      },
      tlT: "Build the timeline", tlS: "Tap the events in the order they happened. The times are your best clue!",
      events: ["2:00 · Mas Joko delivers a letter. The jar is on the counter.", "3:00 · The rain starts. Pak Darto buys a coffee.", "3:20 · Kak Putri's photo: the jar is still there, a navy umbrella by the door.", "3:30 · Bu Ratna finds the jar missing.", "3:40 · The delayed ferry finally leaves."],
      tlWrong: "Not that one yet. Look at the times: which happened next?", tlDone: "Timeline complete! The jar vanished between 3:20 and 3:30.", tlNext: "Make your accusation",
      ev: { ticket: "Ferry left at 3:40", photo: "Photo: umbrella at 3:20", umbrella: "Ferry-badge umbrella", stamp: "Post office log", coin: "Coin trail", joko: "Mas Joko: the jar was full", darto: "Pak Darto: left at 3:10", putri: "Kak Putri was there" },
      fbJoko: "The post office log shows Mas Joko stamping letters at 3:15 and 3:30. He couldn't have been at the warung.",
      fbPutri: "Kak Putri's photo helped the case! Being nearby isn't proof. Whose story doesn't match the times?",
      fbWeak: "Right person! But a detective needs proof. Pick at least 2 clues that point to Pak Darto.",
      fbGood: "Strong case. The times don't lie.",
      whyQ: "Why are you sure it was Pak Darto?",
      why: [
        { t: "He said his ferry left at 3:10, but it left at 3:40. And his umbrella was at the warung at 3:20, just before the jar vanished.", ok: true },
        { t: "Mas Joko talked about how full the jar was, so he must have wanted it.", f: "Talking about something isn't taking it. What does the post office log say?" },
        { t: "Reporters are always snooping, so it was Kak Putri.", f: "That's a guess about a kind of person, not evidence. Check what the times say." }
      ],
      resT: "The jar was safe all along",
      story: "Pak Darto takes off his cap. \"You're right, I'm sorry. When the rain started, water was dripping right onto the counter. I put the jar on my ferry to keep the money dry, then the horn blew and I forgot to tell anyone.\" He brings the jar back, adds a few coins of his own, and Pak Hasan can buy the storybooks after all.",
      lesson: "Detective lesson: put events on a timeline. When someone's time doesn't fit, ask why. Honest people can make mistakes too.",
      badge: "Timeline Keeper", gain: "+ Deduction   + Evidence   + Patterns (time order)",
      steps: ["Brief", "Investigate", "Timeline", "Accuse", "Explain", "Solved"]
    },
'''
ID = r'''    d2: {
      kicker: "Berkas kasus #08 · Kota Pelabuhan, Pulau Mercusuar", title: "Toples Donasi yang Lenyap", tags: "Garis waktu · Alibi",
      body: "Warung Bu Ratna punya toples koin untuk perpustakaan baru sekolah pulau. Kemarin jam 15.30, saat hujan deras tiba-tiba turun, toples itu hilang dari meja. Ada tiga warga di sekitar pelabuhan sore itu.",
      goal: "Tujuanmu: susun kejadian sore itu dengan urutan yang benar, lalu cari tahu siapa yang mengambil toples dan buktikan.",
      giverSays: "Kata Bu Ratna", giver: "\"Tolong bantu! Pak Hasan mau membeli buku cerita dengan uang itu.\"",
      sus: {
        joko: { n: "Mas Joko", r: "Pengantar surat", s: "\"Aku mengantar surat untuk Bu Ratna jam 14.00. Toplesnya penuh sekali! Setelah itu aku di kantor pos sepanjang sore, mengecap surat.\"" },
        darto: { n: "Pak Darto", r: "Kapten feri", s: "\"Aku beli kopi jam 15.00, lalu feriku berangkat tepat jam 15.10. Aku sudah di laut waktu toplesnya hilang.\"" },
        putri: { n: "Kak Putri", r: "Reporter muda", s: "\"Aku memotret hujan untuk Pelabuhan Berita. Aku memotret warung jam 15.20, lalu berjalan kembali ke kantor.\"" }
      },
      clue: {
        ticket: { n: "Papan pelabuhan", s: "\"Feri 15.10: TERLAMBAT karena hujan. Berangkat 15.40.\"" },
        photo: { n: "Foto Kak Putri, 15.20", s: "Toplesnya masih di meja. Ada payung biru tua besar bersandar di pintu." },
        umbrella: { n: "Payung biru tua", s: "Tertinggal di pintu warung. Di gagangnya ada lencana perusahaan feri." },
        stamp: { n: "Catatan kantor pos", s: "Surat yang dicap Mas Joko jam 14.30, 15.00, 15.15, 15.30, dan 15.45." },
        coin: { n: "Jejak koin", s: "Tiga koin di jalan dari warung ke pelabuhan." }
      },
      tlT: "Susun garis waktu", tlS: "Ketuk kejadian sesuai urutan terjadinya. Jam adalah petunjuk terbaikmu!",
      events: ["14.00 · Mas Joko mengantar surat. Toples ada di meja.", "15.00 · Hujan mulai. Pak Darto membeli kopi.", "15.20 · Foto Kak Putri: toples masih ada, payung biru tua di pintu.", "15.30 · Bu Ratna mendapati toplesnya hilang.", "15.40 · Feri yang terlambat akhirnya berangkat."],
      tlWrong: "Belum yang itu. Lihat jamnya: kejadian apa yang berikutnya?", tlDone: "Garis waktu lengkap! Toples hilang antara jam 15.20 dan 15.30.", tlNext: "Ajukan tuduhan",
      ev: { ticket: "Feri berangkat 15.40", photo: "Foto: payung jam 15.20", umbrella: "Payung berlencana feri", stamp: "Catatan kantor pos", coin: "Jejak koin", joko: "Mas Joko: toplesnya penuh", darto: "Pak Darto: berangkat 15.10", putri: "Kak Putri ada di sana" },
      fbJoko: "Catatan kantor pos menunjukkan Mas Joko mengecap surat jam 15.15 dan 15.30. Dia tidak mungkin ada di warung.",
      fbPutri: "Foto Kak Putri justru membantu kasus ini! Berada di dekat sana bukan bukti. Cerita siapa yang tidak cocok dengan jamnya?",
      fbWeak: "Orangnya benar! Tapi detektif butuh bukti. Pilih minimal 2 petunjuk yang mengarah ke Pak Darto.",
      fbGood: "Kasusmu kuat. Jam tidak bisa berbohong.",
      whyQ: "Kenapa kamu yakin pelakunya Pak Darto?",
      why: [
        { t: "Dia bilang ferinya berangkat jam 15.10, padahal berangkat jam 15.40. Payungnya juga ada di warung jam 15.20, tepat sebelum toples hilang.", ok: true },
        { t: "Mas Joko membicarakan toples yang penuh, jadi pasti dia menginginkannya.", f: "Membicarakan sesuatu bukan berarti mengambilnya. Apa kata catatan kantor pos?" },
        { t: "Reporter selalu suka mengintip, jadi pasti Kak Putri.", f: "Itu tebakan tentang jenis orang, bukan bukti. Cek apa kata jamnya." }
      ],
      resT: "Toplesnya aman sejak awal",
      story: "Pak Darto melepas topinya. \"Kamu benar, maafkan aku. Waktu hujan mulai, air menetes tepat ke meja. Aku menaruh toples di feriku supaya uangnya tetap kering, lalu klakson berbunyi dan aku lupa memberi tahu siapa pun.\" Dia mengembalikan toples itu, menambahkan beberapa koin miliknya, dan Pak Hasan tetap bisa membeli buku cerita.",
      lesson: "Pelajaran detektif: susun kejadian dalam garis waktu. Kalau jam seseorang tidak cocok, tanyakan kenapa. Orang jujur pun bisa berbuat salah.",
      badge: "Penjaga Waktu", gain: "+ Deduksi   + Bukti   + Pola (urutan waktu)",
      steps: ["Briefing", "Selidiki", "Garis waktu", "Tuduh", "Jelaskan", "Selesai"]
    },
'''
# insert the case text before each language's explorer block
i_en = s.index("    e: {\n      kicker: \"Pattern Isle · Explorer\"")
s = s[:i_en] + EN + s[i_en:]
i_id = s.index("    e: {\n      kicker: \"Pulau Pola · Penjelajah\"")
s = s[:i_id] + ID + s[i_id:]

# parent prompts
rep('''        "strategist-b": "\\"When something you made didn't work, how did you find the problem?\\""''',
    '''        "strategist-b": "\\"When something you made didn't work, how did you find the problem?\\"",
        detective2: "\\"What did you do yesterday afternoon, in order? Let's make a timeline together.\\""''')
rep('''        "strategist-b": "\\"Waktu sesuatu yang kamu buat tidak berhasil, bagaimana kamu menemukan masalahnya?\\""''',
    '''        "strategist-b": "\\"Waktu sesuatu yang kamu buat tidak berhasil, bagaimana kamu menemukan masalahnya?\\"",
        detective2: "\\"Apa saja yang kamu lakukan kemarin sore, sesuai urutannya? Ayo buat garis waktunya bersama.\\""''')

# state
rep('''  det: { step: 0, seen: [], suspect: null, ev: [], fb: null, why: null },''',
    '''  det: { step: 0, seen: [], suspect: null, ev: [], fb: null, why: null },
  det2: { step: 0, seen: [], order: [], tlfb: null, suspect: null, ev: [], fb: null, why: null },''')
rep('''const HELPER = { detective: "oyen",''', '''const HELPER = { detective: "oyen", detective2: "oyen",''')
rep('''const VOICE_P = { raka: "voice-raka", laras: "voice-laras", bayu: "voice-pak-bayu", sari: "voice-bu-sari", dika: "voice-dika" };''',
    '''const VOICE_P = { raka: "voice-raka", laras: "voice-laras", bayu: "voice-pak-bayu", sari: "voice-bu-sari", dika: "voice-dika",
  ratna: "voice-bu-ratna", darto: "voice-pak-darto", putri: "voice-kak-putri", joko: "voice-mas-joko", hasan: "voice-pak-hasan" };''')
rep('''const FRESH_KEY = { detective: "det",''', '''const FRESH_KEY = { detective2: "det2", detective: "det",''')

# map row for the second case
rep('''      <div class="case-card"><div class="top"><span class="tier">${l.tier[k]}</span><h3>${l.isl[k]}</h3></div>${act(k, "s")}${act(k, "b")}</div>`).join("")}''',
    '''      <div class="case-card"><div class="top"><span class="tier">${l.tier[k]}</span><h3>${l.isl[k]}</h3></div>${act(k, "s")}${k === "detective" ? case2Row() : ""}${act(k, "b")}</div>`).join("")}''')
rep('''const fbBox = (good, text) => {''', '''function case2Row() {
  const l = L(), done = !!st.solved.detective2;
  return `<button class="act" data-action="open" data-case="detective2">
    <span class="ico s">${ICON.solve}</span>
    <span><span class="mode">${l.solveL} · #08</span><span class="nm">${l.d2.title}</span><span class="tg">${l.d2.tags}</span></span>
    <span class="chip ${done ? "ok" : ""}">${done ? l.solved : l.isNew}</span></button>`;
}
const fbBox = (good, text) => {''')

# result screen: Pak Darto (sad, confessing) and Pak Hasan (happy) for case 2; no Build link for it
rep('''${k === "detective" ? figure("bayu") : ""}</div>''',
    '''${k === "detective" ? figure("bayu") : ""}${k === "detective2" ? figure("darto").replace("<svg ", '<svg data-mood="sad" ') + figure("hasan").replace("<svg ", '<svg data-mood="cheer" ') : ""}</div>''')
rep('''    <div class="btnrow">${!st.built[k] ? `<button class="primary build"''', '''    <div class="btnrow">${ORDER.includes(k) && !st.built[k] ? `<button class="primary build"''')
rep('''    playMove(s[0], "cheer"); if (s[1]) setTimeout(() => playMove(s[1], "happy"), 200); if (s[2]) setTimeout(() => playMove(s[2], "yes"), 400);''',
    '''    playMove(s[0], "cheer"); if (s[1]) setTimeout(() => playMove(s[1], "happy"), 200);
    [...s].slice(2).forEach((el, i) => setTimeout(() => playMove(el, el.dataset.mood || "yes"), 400 + i * 250));''')

# renderer
rep('''function renderExplorer() {''', r'''function renderDetective2() {
  const l = L(), d = l.d, x = l.d2, s = st.det2;
  const steps = `<ol class="steps">${x.steps.map((t, i) => `<li class="${i < s.step ? "done" : i === s.step ? "now" : ""}">${i + 1}. ${t}</li>`).join("")}</ol>`;
  const PEOPLE2 = ["joko", "darto", "putri"], CLUES2 = ["ticket", "photo", "umbrella", "stamp", "coin"];
  const clueArt = k => `<svg viewBox="0 0 26 26" aria-hidden="true">${CLUE_SVG[k]}</svg>`;
  let body = "";
  if (s.step === 0) {
    body = `<div class="head"><span class="kicker">${x.kicker}</span><h2>${x.title}</h2><p class="sub">${x.body}</p></div>
      <div class="giver"><div class="giver-fig">${figure("ratna")}</div><div class="giver-say"><span class="who">${x.giverSays}</span><p>${x.giver}</p></div></div>
      <div class="goal">${x.goal}</div>
      <button class="primary" data-action="c2-step" data-v="1">${d.start}</button>`;
  } else if (s.step === 1) {
    const need = Math.max(0, 6 - s.seen.length);
    const person = k => `<button class="item ${s.seen.includes(k) ? "seen" : ""}" data-action="c2-see" data-v="${k}">
        <span class="av pic idle">${portrait(k)}</span>
        <span><span class="name">${x.sus[k].n}</span> <span class="role">· ${x.sus[k].r}</span>
        ${s.seen.includes(k) ? `<p class="said">${x.sus[k].s}</p>` : `<p class="hint">${d.listen}</p>`}</span></button>`;
    const clue = k => `<button class="item ${s.seen.includes(k) ? "seen" : ""}" data-action="c2-see" data-v="${k}">
        <span class="av clue">${clueArt(k)}</span>
        <span><span class="name">${x.clue[k].n}</span>
        ${s.seen.includes(k) ? `<p class="said">${x.clue[k].s}</p>` : `<p class="hint">${d.inspect}</p>`}</span></button>`;
    const nbItem = k => x.sus[k] ? `<li><b>${x.sus[k].n}:</b> ${x.sus[k].s}</li>` : `<li><b>${x.clue[k].n}:</b> ${x.clue[k].s}</li>`;
    body = `<div class="head"><h2>${d.invT}</h2><p class="sub">${d.invS}</p></div>
      <div class="inv">
        <div class="col"><span class="col-t">${d.people}</span>${PEOPLE2.map(person).join("")}
          <span class="col-t" style="margin-top:6px">${d.clues}</span>${CLUES2.map(clue).join("")}</div>
        <div class="notebook"><h3>${d.nb}</h3>${s.seen.length ? `<ul>${s.seen.map(nbItem).join("")}</ul>` : `<p class="empty">${d.nbEmpty}</p>`}</div>
      </div>
      <button class="primary" data-action="c2-step" data-v="2" ${need ? "disabled" : ""}>${need ? d.need(need) : x.tlT + " →"}</button>`;
  } else if (s.step === 2) {
    const POOL = [2, 4, 0, 3, 1], done = s.order.length === x.events.length;
    const ev = i => { const [time, text] = x.events[i].split(" · "); return `<b class="tl-time">${time}</b><span>${text}</span>`; };
    body = `<div class="head"><h2>${x.tlT}</h2><p class="sub">${x.tlS}</p></div>
      <ol class="tl">${x.events.map((_, i) => i < s.order.length ? `<li class="tl-row placed">${ev(s.order[i])}</li>` : `<li class="tl-row empty"><b class="tl-time">?</b><span></span></li>`).join("")}</ol>
      ${done ? "" : `<div class="tl-pool">${POOL.filter(i => !s.order.includes(i)).map(i => `<button class="tl-card" data-action="c2-tl" data-v="${i}">${ev(i)}</button>`).join("")}</div>`}
      ${s.tlfb ? fbBox(false, x.tlWrong) : done ? fbBox(true, x.tlDone) : ""}
      ${done ? `<button class="primary" data-action="c2-step" data-v="3">${x.tlNext}</button>` : ""}`;
  } else if (s.step === 3) {
    const evKeys = ["ticket", "photo", "umbrella", "stamp", "coin", "joko", "darto", "putri"].filter(k => s.seen.includes(k));
    body = `<div class="head"><h2>${d.accT}</h2></div>
      <p class="q">${x.whyQ.replace(/Pak Darto\??/, "").trim() ? d.q1.replace(/lamp|lampu/, x.title.includes("Jar") ? "jar" : "toples") : d.q1}</p>
      <div class="pick">${PEOPLE2.map(k => `<button class="opt" data-action="c2-sus" data-v="${k}" aria-pressed="${s.suspect === k}">
        <span class="av pic">${portrait(k)}</span><span><span class="name">${x.sus[k].n}</span><br><span class="role">${x.sus[k].r}</span></span></button>`).join("")}</div>
      <p class="q">${d.q2}</p>
      <div class="evid">${evKeys.map(k => `<button class="ev" data-action="c2-ev" data-v="${k}" aria-pressed="${s.ev.includes(k)}">${x.ev[k]}</button>`).join("")}</div>
      ${s.fb ? fbBox(false, s.fb === "fbNone" ? d.fbNone : x[s.fb]) : ""}
      <button class="primary" data-action="c2-accuse">${d.accuse}</button>`;
  } else if (s.step === 4) {
    body = `${fbBox(true, x.fbGood)}
      <div class="head"><h2>${d.whyT}</h2><p class="q">${x.whyQ}</p></div>
      <div class="answers">${x.why.map((w, i) => `<button class="ans ${s.why === i ? (w.ok ? "right" : "wrong") : ""}" data-action="c2-why" data-v="${i}">${w.t}</button>`).join("")}</div>
      ${s.why !== null && !x.why[s.why].ok ? fbBox(false, x.why[s.why].f) : ""}`;
  } else {
    body = solveResult("detective2", x, x.resT, x.story);
  }
  $app.innerHTML = stage(steps + body);
}

function renderExplorer() {''')
rep('''  detective: renderDetective, explorer: renderExplorer,''', '''  detective: renderDetective, detective2: renderDetective2, explorer: renderExplorer,''')

# actions
rep('''    case "d-step": d.step = +v; return go("detective");''', '''    case "c2-step": st.det2.step = +v; return go("detective2");
    case "c2-see": {
      const c = st.det2, fresh = !c.seen.includes(v);
      if (fresh) c.seen.push(v);
      render();
      if (VOICE_P[v]) { sfx(VOICE_P[v]); playMove(document.querySelector(`[data-action="c2-see"][data-v="${v}"] svg[data-slug]`), "talk"); }
      if (fresh) sfx("notebook-write", VOICE_P[v] ? 900 : 0);
      return;
    }
    case "c2-tl": {
      const c = st.det2;
      if (+v === c.order.length) { c.order.push(+v); c.tlfb = null; sfx(c.order.length === L().d2.events.length ? "ui-correct" : "clue-found"); }
      else { c.tlfb = "wrong"; sfx("ui-wrong"); sfx("oyen-meow", 350); }
      return render();
    }
    case "c2-sus": st.det2.suspect = v; st.det2.fb = null; return render();
    case "c2-ev": { const c = st.det2; c.ev = c.ev.includes(v) ? c.ev.filter(x => x !== v) : [...c.ev, v]; c.fb = null; return render(); }
    case "c2-accuse": {
      const c = st.det2, strong = c.ev.filter(x => ["ticket", "photo", "umbrella", "darto"].includes(x)).length;
      if (!c.suspect) c.fb = "fbNone";
      else if (c.suspect === "joko") c.fb = "fbJoko";
      else if (c.suspect === "putri") c.fb = "fbPutri";
      else if (strong < 2) c.fb = "fbWeak";
      else { c.fb = null; c.step = 4; }
      if (c.fb) { sfx("ui-wrong"); sfx("oyen-meow", 350); } else { sfx("ui-correct"); sfx("sting-surprised", 300); }
      return render();
    }
    case "c2-why": {
      const c = st.det2; c.why = +v;
      if (L().d2.why[+v].ok) { solve("detective2"); c.step = 5; sfx("badge-earned"); sfx("ferry-horn", 1100); sfx("oyen-purr", 2200); }
      else { sfx("ui-wrong"); sfx("oyen-meow", 350); }
      return render();
    }
    case "d-step": d.step = +v; return go("detective");''')
rep('''const TAP = new Set(["home",''', '''const TAP = new Set(["c2-step", "c2-sus", "c2-ev", "home",''')
rep('''    case "open": { const k = el.dataset.case; st[FRESH_KEY[k]] = fresh()[FRESH_KEY[k]]; return go(k); }''',
    '''    case "open": {
      const k = el.dataset.case; st[FRESH_KEY[k]] = fresh()[FRESH_KEY[k]]; go(k);
      if (k === "detective2") { sfx("market-hello", 150); sfx("voice-bu-ratna", 900); setTimeout(() => playMove(document.querySelector(".giver svg[data-slug]"), "no"), 300); }
      return;
    }''')

# skills: case 2 adds deduction, evidence and time-order patterns
rep('''  if (st.solved.detective) { v[2] += 40; v[3] += 45; v[4] += 15; }''', '''  if (st.solved.detective) { v[2] += 40; v[3] += 45; v[4] += 15; }
  if (st.solved.detective2) { v[2] += 12; v[3] += 10; v[0] += 12; v[4] += 8; }''')
rep('''  const names = { explorer: [l.e.badge, l.be.badge], detective: [l.d.badge, l.bd.badge], strategist: [l.s.badge, l.bs.badge] };''',
    '''  const names = { explorer: [l.e.badge, l.be.badge], detective: [l.d.badge, l.bd.badge], strategist: [l.s.badge, l.bs.badge] };
  const extra = st.solved.detective2 ? [badge(l.d2.badge)] : [];''')
rep('''  ORDER.forEach(k => { if (st.solved[k]) earned.push(badge(names[k][0])); if (st.built[k]) earned.push(badge(names[k][1], true)); });''',
    '''  ORDER.forEach(k => { if (st.solved[k]) earned.push(badge(names[k][0])); if (st.built[k]) earned.push(badge(names[k][1], true)); });
  earned.push(...extra);''')

# styles
rep('''/* Parent */
.parent {''', '''/* Case 2: case giver and timeline */
.giver { display: flex; align-items: flex-end; gap: 14px; }
.giver-fig svg { width: 92px; height: auto; display: block; }
.giver-say { background: var(--card-2); border-radius: 16px 16px 16px 4px; padding: 12px 16px; display: grid; gap: 4px; max-width: 520px; }
.giver-say .who { font-size: .72rem; letter-spacing: .08em; text-transform: uppercase; color: var(--muted); font-weight: 600; }
.tl { list-style: none; margin: 0; padding: 0 0 0 18px; display: grid; gap: 8px; border-left: 3px solid var(--line); }
.tl-row { position: relative; display: grid; grid-template-columns: 64px minmax(0, 1fr); gap: 10px; align-items: center; background: var(--card-2); border-radius: 12px; padding: 10px 12px; min-height: 46px; }
.tl-row::before { content: ""; position: absolute; left: -26px; top: 50%; width: 13px; height: 13px; margin-top: -6.5px; border-radius: 50%; background: var(--line); }
.tl-row.placed::before { background: var(--lantern); box-shadow: 0 0 8px var(--lantern); }
.tl-row.empty { border: 2px dashed var(--line); background: none; color: var(--muted); }
.tl-time { font-family: var(--display); font-size: 1.05rem; color: var(--lantern); font-variant-numeric: tabular-nums; }
.tl-pool { display: grid; grid-template-columns: repeat(auto-fill, minmax(230px, 1fr)); gap: 8px; }
.tl-card { display: grid; grid-template-columns: 56px minmax(0, 1fr); gap: 8px; align-items: center; text-align: left; background: var(--card); border: 2px solid var(--line); border-radius: 12px; padding: 10px 12px; cursor: pointer; font-size: .88rem; }
.tl-card:hover { border-color: var(--lantern); }
.av.clue svg { width: 30px; height: 30px; }

/* Parent */
.parent {''')
open(P, "w").write(s)
print("ok")

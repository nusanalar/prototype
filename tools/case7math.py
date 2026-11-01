"""Add a number clue to case #07 (lighthouse): Bu Sari's baking list and a "Number check" step
between Investigate and Accuse. Kids work out how long she was at her window, which shows she saw
the harbor at 11 pm, so Pak Bayu's alibi can't be true. Edits index.html in place; run once."""
import os
P = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "index.html")
s = open(P, encoding="utf-8").read()
def rep(a, b, cnt=1):
    global s
    n = s.count(a)
    assert n == cnt, (n, a[:90])
    s = s.replace(a, b)

# ---------- English text ----------
rep('''        log: { n: "Night-watch log", s: "\\"11:00 pm: lighthouse went dark.\\" Written by the harbor guard." }
      },''', '''        log: { n: "Night-watch log", s: "\\"11:00 pm: lighthouse went dark.\\" Written by the harbor guard." },
        bread: { n: "Bu Sari's baking list", s: "\\"Started at 8 pm. 5 trays of bread, one after another. Each tray bakes for 1 hour.\\"" }
      },
      steps: ["Brief", "Investigate", "Number check", "Accuse", "Explain", "Solved"],
      mT: "Number check", mS: "Bu Sari says nobody was at the harbor all night. But was she really at her window when the lamp went dark? Use the numbers.",
      mFacts: ["Bu Sari started baking at 8 pm.", "She baked 5 trays, one after another. Each tray takes 1 hour.", "The lamp went dark at 11 pm."],
      mQ: "Until what time was Bu Sari baking by her window?",
      mOpts: [
        { t: "11 pm", f: "Count again: start at 8 pm and add 1 hour for each tray. That's 5 hours, not 3." },
        { t: "12 midnight", f: "Close! Count each tray: 9, 10, 11, 12… that's only 4 trays. One more." },
        { t: "1 am", ok: true },
        { t: "5 am", f: "That's 5 o'clock, not 5 hours. Start at 8 pm and count 5 hours on." }
      ],
      mHours: ["8 pm", "9", "10", "11", "12", "1 am"], mDark: "lamp dark",
      mDone: "8 pm + 5 hours = 1 am. Bu Sari was at her window from 8 pm to 1 am, so she was watching the harbor at 11 pm. Her words are strong evidence.",
      mNext: "Make your accusation",''')
rep('''ev: { boots: "Boot prints", net: "Blue net threads", log: "Lamp went dark at 11", sari: "Bu Sari: harbor was empty",''',
    '''ev: { boots: "Boot prints", net: "Blue net threads", log: "Lamp went dark at 11", bread: "Bu Sari baked 8 pm to 1 am", sari: "Bu Sari: harbor was empty",''')
rep('''{ t: "A witness says the harbor was empty, so his alibi isn't true. And the boot prints and net threads match a fisherman.", ok: true },''',
    '''{ t: "Bu Sari was at her window from 8 pm to 1 am and saw nobody at the harbor, so his alibi isn't true. And the boot prints and net threads match a fisherman.", ok: true },''')
rep('''badge: "Evidence Finder", gain: "+ Deduction   + Evidence   + Explaining why"''',
    '''badge: "Evidence Finder", gain: "+ Deduction   + Evidence   + Numbers   + Explaining why"''')

# ---------- Indonesian text ----------
rep('''        log: { n: "Catatan jaga malam", s: "\\"Pukul 23.00: mercusuar padam.\\" Ditulis oleh penjaga pelabuhan." }
      },''', '''        log: { n: "Catatan jaga malam", s: "\\"Pukul 23.00: mercusuar padam.\\" Ditulis oleh penjaga pelabuhan." },
        bread: { n: "Daftar panggang Bu Sari", s: "\\"Mulai jam 8 malam. 5 loyang roti, satu per satu. Setiap loyang dipanggang 1 jam.\\"" }
      },
      steps: ["Briefing", "Selidiki", "Cek angka", "Tuduh", "Jelaskan", "Selesai"],
      mT: "Cek angka", mS: "Bu Sari bilang semalaman tidak ada orang di pelabuhan. Tapi apakah dia benar-benar di dekat jendela saat lampu padam? Pakai angkanya.",
      mFacts: ["Bu Sari mulai memanggang jam 8 malam.", "Dia memanggang 5 loyang, satu per satu. Setiap loyang butuh 1 jam.", "Lampu padam jam 11 malam."],
      mQ: "Sampai jam berapa Bu Sari memanggang di dekat jendela?",
      mOpts: [
        { t: "Jam 11 malam", f: "Hitung lagi: mulai dari jam 8 malam, tambah 1 jam untuk setiap loyang. Itu 5 jam, bukan 3." },
        { t: "Jam 12 tengah malam", f: "Hampir! Hitung setiap loyang: 9, 10, 11, 12… baru 4 loyang. Satu lagi." },
        { t: "Jam 1 dini hari", ok: true },
        { t: "Jam 5 pagi", f: "Itu jam 5, bukan 5 jam. Mulai dari jam 8 malam lalu hitung 5 jam ke depan." }
      ],
      mHours: ["20.00", "21", "22", "23", "24", "01.00"], mDark: "lampu padam",
      mDone: "Jam 8 malam + 5 jam = jam 1 dini hari. Bu Sari di dekat jendela dari jam 8 malam sampai jam 1, jadi dia melihat pelabuhan jam 11 malam. Kata-katanya bukti yang kuat.",
      mNext: "Ajukan tuduhanmu",''')
rep('''ev: { boots: "Jejak sepatu bot", net: "Benang jala biru", log: "Lampu padam jam 11", sari: "Bu Sari: pelabuhan kosong",''',
    '''ev: { boots: "Jejak sepatu bot", net: "Benang jala biru", log: "Lampu padam jam 11", bread: "Bu Sari memanggang jam 8 malam–1 dini hari", sari: "Bu Sari: pelabuhan kosong",''')
rep('''{ t: "Saksi bilang pelabuhan kosong, jadi alibinya tidak benar. Jejak sepatu bot dan benang jala juga cocok dengan nelayan.", ok: true },''',
    '''{ t: "Bu Sari di dekat jendela dari jam 8 malam sampai jam 1 dan tidak melihat siapa pun di pelabuhan, jadi alibinya tidak benar. Jejak sepatu bot dan benang jala juga cocok dengan nelayan.", ok: true },''')
rep('''badge: "Pencari Bukti", gain: "+ Deduksi   + Bukti   + Menjelaskan alasan"''',
    '''badge: "Pencari Bukti", gain: "+ Deduksi   + Bukti   + Angka   + Menjelaskan alasan"''')

# ---------- clue icon ----------
rep('''  log: `<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="5" y="3" width="16" height="20" rx="2" fill="#fff8e6" stroke="#8a6d3b"/><path d="M8 8h10M8 12h10M8 16h6" stroke="#8a6d3b" stroke-width="1.5"/></svg>`''',
    '''  log: `<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="5" y="3" width="16" height="20" rx="2" fill="#fff8e6" stroke="#8a6d3b"/><path d="M8 8h10M8 12h10M8 16h6" stroke="#8a6d3b" stroke-width="1.5"/></svg>`,
  bread: `<svg viewBox="0 0 26 26" aria-hidden="true"><rect x="3" y="17" width="20" height="4" rx="1.5" fill="#8a6d3b"/><path d="M5 17c0-6 3-9 8-9s8 3 8 9z" fill="#e0a95f"/><path d="M9 12l1.5 2.5M13 11l1.5 2.5M17 12l1 2" stroke="#b07a3a" stroke-width="1.4" stroke-linecap="round"/></svg>`''')

# ---------- state ----------
rep("det: { step: 0, seen: [], suspect: null, ev: [], fb: null, why: null },",
    "det: { step: 0, seen: [], suspect: null, ev: [], fb: null, why: null, m: null },")

# ---------- render ----------
rep('''  const l = L(), d = l.d, s = st.det;
  const steps = `<ol class="steps">${l.steps.map(''', '''  const l = L(), d = l.d, s = st.det;
  const steps = `<ol class="steps">${d.steps.map(''')
rep('''${["boots", "net", "log"].map(clue).join("")}</div>
        <div class="notebook"><h3>${d.nb}</h3>${s.seen.length ? `<ul>${s.seen.map(nbItem)''',
    '''${["boots", "net", "log", "bread"].map(clue).join("")}</div>
        <div class="notebook"><h3>${d.nb}</h3>${s.seen.length ? `<ul>${s.seen.map(nbItem)''')
rep('''      <button class="primary" data-action="d-step" data-v="2" ${need ? "disabled" : ""}>${need ? d.need(need) : d.ready}</button>`;
  } else if (s.step === 2) {
    const evKeys = ["boots", "net", "log", "sari", "dika", "bayu"]''',
    '''      <button class="primary" data-action="d-step" data-v="2" ${need ? "disabled" : ""}>${need ? d.need(need) : d.mT + " →"}</button>`;
  } else if (s.step === 2) {
    const done = s.m !== null && d.mOpts[s.m].ok;
    const hours = `<ol class="m-hours">${d.mHours.map((h, i) => `<li class="${i < 5 ? "bake" : ""} ${i === 3 ? "dark" : ""}"><b>${h}</b>${i < 5 ? `<span class="tray">${clueIcon("bread")}</span>` : ""}${i === 3 ? `<span class="m-dark">${d.mDark}</span>` : ""}</li>`).join("")}</ol>`;
    body = `<div class="head"><h2>${d.mT}</h2><p class="sub">${d.mS}</p></div>
      <ul class="m-facts">${d.mFacts.map(f => `<li>${f}</li>`).join("")}</ul>
      <p class="q">${d.mQ}</p>
      <div class="answers m-opts">${d.mOpts.map((o, i) => `<button class="ans ${s.m === i ? (o.ok ? "right" : "wrong") : ""}" data-action="d-math" data-v="${i}" ${done ? "disabled" : ""}>${o.t}</button>`).join("")}</div>
      ${s.m !== null && !d.mOpts[s.m].ok ? fbBox(false, d.mOpts[s.m].f) : ""}
      ${done ? hours + fbBox(true, d.mDone) + `<button class="primary" data-action="d-step" data-v="3">${d.mNext}</button>` : ""}`;
  } else if (s.step === 3) {
    const evKeys = ["boots", "net", "log", "bread", "sari", "dika", "bayu"]''')
rep('''      <button class="primary" data-action="d-accuse">${d.accuse}</button>`;
  } else if (s.step === 3) {
    body = `${fbBox(true, d.fbGood)}''', '''      <button class="primary" data-action="d-accuse">${d.accuse}</button>`;
  } else if (s.step === 4) {
    body = `${fbBox(true, d.fbGood)}''')

# ---------- actions ----------
rep('''    case "d-sus": d.suspect = v; d.fb = null; return render();''',
    '''    case "d-math": {
      d.m = +v;
      if (L().d.mOpts[+v].ok) { sfx("ui-correct"); sfx("oyen-purr", 700); } else { sfx("ui-wrong"); sfx("oyen-meow", 350); }
      return render();
    }
    case "d-sus": d.suspect = v; d.fb = null; return render();''')
rep('''const strong = d.ev.filter(x => ["boots", "net", "sari"].includes(x)).length;''',
    '''const strong = d.ev.filter(x => ["boots", "net", "sari", "bread"].includes(x)).length;''')
rep('''      else { d.fb = null; d.step = 3; }''', '''      else { d.fb = null; d.step = 4; }''')
rep('''if (L().d.why[+v].ok) { solve("detective"); d.step = 4;''', '''if (L().d.why[+v].ok) { solve("detective"); d.step = 5;''')

# ---------- styles ----------
rep(".answers { display: grid; gap: 10px; }", """.answers { display: grid; gap: 10px; }
.m-facts { list-style: none; padding: 0; margin: 0 0 4px; display: grid; gap: 6px; }
.m-facts li { background: var(--card-2); border-radius: var(--r); padding: 10px 14px; border-left: 4px solid var(--lantern); }
.m-opts { grid-template-columns: repeat(auto-fit, minmax(130px, 1fr)); }
.m-opts .ans { text-align: center; font-weight: 600; }
.m-opts .ans:disabled { cursor: default; }
.m-hours { list-style: none; padding: 0; margin: 4px 0; display: grid; grid-template-columns: repeat(6, 1fr); gap: 4px; }
.m-hours li { position: relative; text-align: center; padding: 8px 2px 6px; border-radius: 10px; font-size: .8rem; color: var(--muted); }
.m-hours li.bake { background: color-mix(in srgb, var(--lantern) 16%, transparent); color: inherit; }
.m-hours li.dark { outline: 2px solid var(--coral); }
.m-hours b { display: block; }
.m-hours .tray svg { width: 22px; height: 22px; }
.m-dark { display: block; font-size: .68rem; color: var(--coral); font-weight: 600; }""")

open(P, "w", encoding="utf-8").write(s)
print("case #07 number clue added")

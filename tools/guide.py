"""Add kid guidance to the prototype: onboarding, mission cards, lesson acknowledgment and the learning book. Safe to run once."""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); P = os.path.join(os.path.dirname(HERE), "mystery-isles.html")
s = open(P, encoding="utf-8").read()
assert "const GUIDE = {" not in s, "already applied"
def R(a, b):
    global s
    assert s.count(a) == 1, (s.count(a), a[:90]); s = s.replace(a, b)
css = open(os.path.join(HERE, "guide_css.css"), encoding="utf-8").read()
js = open(os.path.join(HERE, "guide_data.js"), encoding="utf-8").read()
R("</style>", css + "</style>") if s.count("</style>") == 1 else None
i = s.index("</style>"); s = s[:i] + css + s[i:] if "Kid guidance: onboarding" not in s else s
R("/* ---------- CORE ---------- */", js + "\n/* ---------- CORE ---------- */")
# state
R('try { const a = localStorage.getItem("mi-avatar");', '''st.learned = {}; st.learnPick = {}; st.missionOpen = {}; st.ageTier = null; st.onb = null;
try { st.learned = JSON.parse(localStorage.getItem("mi-learn") || "{}") || {}; const t = localStorage.getItem("mi-age"); if (["explorer", "detective", "strategist"].includes(t)) st.ageTier = t; if (!localStorage.getItem("mi-onboard")) st.onb = 0; } catch (e) { st.onb = 0; }
try { const a = localStorage.getItem("mi-avatar");''')
# mission card in every activity stage
R('const stage = inner => `<section class="stage"><button class="back" data-action="home">${L().back}</button>${inner}</section>`;',
  'const stage = inner => `<section class="stage"><button class="back" data-action="home">${L().back}</button>${missionCard()}${inner}</section>`;')
# lesson card before the buttons on every result
a = s.index("const solveResult = (k, x, title, story) => {"); b = s.index("const buildResult", a)
blk = s[a:b]; assert blk.count('<div class="btnrow">') == 1
s = s[:a] + blk.replace('<div class="btnrow">', '${learnCard()}<div class="btnrow">') + s[b:]
R('${badge(x.badge, true)}<span class="gain">${x.gain}</span><button class="primary" data-action="home">', '${badge(x.badge, true)}<span class="gain">${x.gain}</span>${learnCard()}<button class="primary" data-action="home">')
# map: start-here island and learning book card
R('const l = L(), cls = k => `${st.solved[k] ? "on" : ""} ${st.built[k] ? "built" : ""}`;', 'const l = L(), cls = k => `${st.solved[k] ? "on" : ""} ${st.built[k] ? "built" : ""} ${st.ageTier === k ? "start" : ""}`;')
R('const label = (k, x, y) => `', 'const label = (k, x, y) => (st.ageTier === k ? `<text class="start-t" x="${x}" y="${y - 24}" text-anchor="middle">★ ${G().startHere}</text>` : "") + `')
R('''      <span class="open">${l.dy.mapCta}</span>
    </button>''', '''      <span class="open">${l.dy.mapCta}</span>
    </button>
    <button class="daily-card book" data-action="learnbook">
      <span class="ico">${ICON_BOOK}</span>
      <span><span class="mode">${G().book.k}</span><span class="nm">${G().book.t}</span><span class="tg">${G().book.count(LEARN_ORDER.filter(k => st.learned[k]).length)}</span></span>
      <span class="open">${G().book.cta}</span>
    </button>''')
# parent view: lessons the child saved
R('''        <div class="panel"><h3>${p.newT}</h3>''', '''        <div class="panel"><h3>${G().par.t}</h3>${LEARN_ORDER.some(k => st.learned[k]) ? `<ul class="plearn">${LEARN_ORDER.filter(k => st.learned[k]).map(k => `<li><b>${G().m[k].skill}</b> ${G().book.willUse} ${G().m[k].uses[st.learned[k].use]}</li>`).join("")}</ul><p class="note">${G().par.tip}</p>` : `<p class="note">${G().par.none}</p>`}</div>
        <div class="panel"><h3>${p.newT}</h3>''')
R('  map: renderMap, parent: renderParent,', '  map: renderMap, parent: renderParent, learn: renderLearn,')
R('function render() { header(); SCREENS[st.screen](); autoMoves(); }', 'function render() { header(); SCREENS[st.screen](); autoMoves(); renderOnb(); }')
# new player: lessons and onboarding start over too
R('try { ["mi-daily", "mi-avatar"].forEach(k => localStorage.removeItem(k)); } catch (e) {}', 'try { ["mi-daily", "mi-avatar", "mi-learn", "mi-onboard", "mi-age"].forEach(k => localStorage.removeItem(k)); } catch (e) {}')
R('last: null, daily: { tier: "detective", off: 0 }, dc: null, dailyDone: {}, avatar: "raka"\n  });', 'last: null, daily: { tier: "detective", off: 0 }, dc: null, dailyDone: {}, avatar: "raka",\n    learned: {}, learnPick: {}, missionOpen: {}, ageTier: null, onb: 0\n  });')
# help button in the header
theme_line = [l for l in s.split("\n") if 'id="themeBtn"' in l and l.strip().startswith("<button")][0]
R(theme_line, theme_line + '\n    <button class="icon-btn" data-action="help" id="helpBtn"><svg viewBox="0 0 24 24" aria-hidden="true"><circle cx="12" cy="12" r="9.5" fill="none" stroke="currentColor" stroke-width="2"/><path d="M9.3 9.3 Q9.6 6.8 12 6.8 Q14.7 6.8 14.7 9.2 Q14.7 10.9 12.8 11.7 Q12 12.1 12 13.6" stroke="currentColor" stroke-width="2" fill="none" stroke-linecap="round"/><circle cx="12" cy="17" r="1.3" fill="currentColor"/></svg></button>')
R('  tb.setAttribute("aria-pressed", String(dark)); tb.setAttribute("aria-label", l.themeL); tb.title = l.themeL;', '  tb.setAttribute("aria-pressed", String(dark)); tb.setAttribute("aria-label", l.themeL); tb.title = l.themeL;\n  { const hb = document.getElementById("helpBtn"); hb.setAttribute("aria-label", G().help); hb.title = G().help; }')
# actions
R('    case "home": return go("map");', '''    case "help": st.onb = 0; render(); onbSay(); return;
    case "onb-next": st.onb++; render(); onbSay(); return;
    case "onb-prev": st.onb = Math.max(0, st.onb - 1); render(); onbSay(); return;
    case "onb-skip": return onbClose();
    case "onb-avatar": st.avatar = v; try { localStorage.setItem("mi-avatar", v); } catch (err) {} render(); sayAs(v, L().greet[v], document.querySelector(`.onb .who-btn[data-v="${v}"] svg[data-slug]`)); return;
    case "onb-age": st.ageTier = v; try { localStorage.setItem("mi-age", v); } catch (err) {} sfx("ui-tap"); return render();
    case "onb-done": onbClose(); sfx("badge-earned"); { const h = HELPER[st.ageTier] || "oyen"; } return;
    case "learnbook": return go("learn");
    case "learn-pick": st.learnPick[st.screen] = +v; sfx("ui-tap"); return render();
    case "learn-save": {
      const k = st.screen; if (st.learnPick[k] == null) return;
      st.learned[k] = { use: st.learnPick[k], t: Date.now() }; saveLearn(); sfx("notebook-write"); render();
      const h = HELPER[k]; if (h) sayAs(h, G().savedSay, null, { tic: true }); else speak(G().savedSay);
      return;
    }
    case "home": return go("map");''')
open(P, "w", encoding="utf-8").write(s); print("guide applied", len(s) // 1024, "KB")

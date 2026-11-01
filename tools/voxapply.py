"""Put the recorded Indonesian voice lines into the prototype. Safe to run again."""
import json, os, re
SCRATCH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(SCRATCH, "mystery-isles.html"); s = open(P).read()
bundle = json.load(open(os.path.join(SCRATCH, "vox-bundle.json")))
data = "/* Recorded Indonesian voice lines, keyed by character|line: paths to MP3s copied from the asset kit by tools/voxsync.py */\nconst VOX = " + json.dumps(bundle, ensure_ascii=False) + ";\n"
RUNTIME = r'''const voxKey = (who, text) => who + "|" + String(text).replace(/[“”"]/g, "").trim();
let voxTok = 0, voxNow = null, voxNext = null;
function stopVox() {
  voxTok++; voxNext = null;
  if (voxNow) { voxNow.a.onended = voxNow.a.onerror = null; voxNow.a.pause(); if (voxNow.host) voxNow.host.classList.remove("speaking"); voxNow = null; }
}
function playVox(who, src, host, opts) {
  const run = () => {
    const tok = ++voxTok, a = new Audio(src);
    const end = () => { if (tok !== voxTok) return; if (host) host.classList.remove("speaking"); voxNow = null; const n = voxNext; voxNext = null; if (n) n(); };
    voxNow = { a, host }; a.onended = a.onerror = end;
    if (host) host.classList.add("speaking");
    const p = a.play(); if (p && p.catch) p.catch(end);
  };
  if (opts.queue && voxNow) { voxNext = run; return; }
  stopVox(); try { speechSynthesis.cancel(); } catch (e) {}
  if (opts.tic && VOICE[who]) { sfx(VOICE[who]); const tok = voxTok; setTimeout(() => { if (tok === voxTok) run(); }, 420); } else run();
}
'''
s = re.sub(r"/\* Recorded Indonesian voice lines.*?\nconst VOX = .*?;\n", lambda m: data, s, count=1, flags=re.S) if "const VOX = " in s else s.replace("const VOICE_CHAR = {", data + RUNTIME + "const VOICE_CHAR = {", 1)
a = "function sayAs(who, text, host, opts = {}) {\n  if (!st.soundOn || !text) return;\n"
if "playVox(who, vsrc" not in s:
    assert a in s
    s = s.replace(a, a + '  const vsrc = st.lang === "id" && VOX[voxKey(who, text)];\n  if (vsrc) return playVox(who, vsrc, host, opts);\n  if (!opts.queue) stopVox();\n', 1)
open(P, "w").write(s); print("ok", len(bundle), "lines,", len(s) // 1024, "KB page")

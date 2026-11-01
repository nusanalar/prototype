"""Refresh the prototype's recorded voice lines from the asset kit (../assets/voices/<lang>).
Indonesian lines go into VOX, English lines into VOX_EN. Lines are matched by character and text;
lines the kit doesn't have are kept as they are, and kit lines whose MP3 isn't generated yet are skipped.
Usage: python3 tools/voxsync.py [path/to/assets]"""
import base64, json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "assets")
P = os.path.join(HERE, "index.html")
s = open(P, encoding="utf-8").read()
key = lambda who, text: who + "|" + re.sub(r'[“”"]', "", text).strip()
for lang, var in (("id", "VOX"), ("en", "VOX_EN")):
    path = os.path.join(ASSETS, "voices", lang, "lines.json")
    if not os.path.exists(path):
        continue
    m = re.search(r"\nconst " + var + r" = (\{.*?\});\n", s, flags=re.S)
    vox = json.loads(m.group(1))
    lines = json.load(open(path, encoding="utf-8"))
    upd = new = missing = 0
    for ln in lines:
        mp3 = os.path.join(ASSETS, ln["file"])
        if not os.path.exists(mp3):
            missing += 1
            continue
        k = key(ln["who"], ln["text"])
        src = "data:audio/mpeg;base64," + base64.b64encode(open(mp3, "rb").read()).decode()
        if k in vox: upd += vox[k] != src
        else: new += 1
        vox[k] = src
    s = s[:m.start(1)] + json.dumps(vox, ensure_ascii=False) + s[m.end(1):]
    kit = {key(l["who"], l["text"]) for l in lines}
    print(f"[{lang}] {upd} lines updated, {new} added, {missing} not generated yet, "
          f"{len([k for k in vox if k not in kit])} kept (not in the kit)")
open(P, "w", encoding="utf-8").write(s)
print(f"page {len(s)//1024} KB")

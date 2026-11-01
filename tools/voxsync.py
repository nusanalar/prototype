"""Refresh the prototype's recorded Indonesian voice lines from the asset kit (../assets/voices/id).
Lines are matched by character and text; lines the kit doesn't have are kept as they are.
Usage: python3 tools/voxsync.py [path/to/assets]"""
import base64, json, os, re, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "assets")
P = os.path.join(HERE, "index.html")
s = open(P, encoding="utf-8").read()
m = re.search(r"\nconst VOX = (\{.*?\});\n", s, flags=re.S)
vox = json.loads(m.group(1))
key = lambda who, text: who + "|" + re.sub(r'[“”"]', "", text).strip()
lines = json.load(open(os.path.join(ASSETS, "voices", "id", "lines.json"), encoding="utf-8"))
upd, new = 0, 0
for ln in lines:
    k = key(ln["who"], ln["text"])
    src = "data:audio/mpeg;base64," + base64.b64encode(open(os.path.join(ASSETS, ln["file"]), "rb").read()).decode()
    if k in vox: upd += vox[k] != src
    else: new += 1
    vox[k] = src
s = s[:m.start(1)] + json.dumps(vox, ensure_ascii=False) + s[m.end(1):]
open(P, "w", encoding="utf-8").write(s)
kit = {key(l["who"], l["text"]) for l in lines}
print(f"{upd} lines updated, {new} added, {len([k for k in vox if k not in kit])} kept (not in the kit), page {len(s)//1024} KB")

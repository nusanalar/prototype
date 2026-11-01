"""Refresh the prototype's recorded voice lines from the asset kit (../assets/voices/<lang>).

The MP3s are copied next to the page (voices/<lang>/<who>/<file>.mp3, the same paths as in the kit) and
index.html keeps only the path for each line: VOX for Indonesian, VOX_EN for English. The page then loads
just the line it plays instead of carrying every voice inside the HTML.
Lines are matched by character and text. Kit lines whose MP3 isn't generated yet are skipped (the page
falls back to the device voice), and copied files the kit no longer lists are removed.
Usage: python3 tools/voxsync.py [path/to/assets]"""
import json, os, re, shutil, sys
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "assets")
P = os.path.join(HERE, "index.html")
s = open(P, encoding="utf-8").read()
key = lambda who, text: who + "|" + re.sub(r'[“”"]', "", text).strip()
keep = set()
for lang, var in (("id", "VOX"), ("en", "VOX_EN")):
    m = re.search(r"\nconst " + var + r" = (\{.*?\});\n", s, flags=re.S)
    path = os.path.join(ASSETS, "voices", lang, "lines.json")
    lines = json.load(open(path, encoding="utf-8")) if os.path.exists(path) else []
    vox, copied, missing = {}, 0, 0
    for ln in lines:
        src = os.path.join(ASSETS, ln["file"])
        if not os.path.exists(src):
            missing += 1
            continue
        dst = os.path.join(HERE, ln["file"])
        os.makedirs(os.path.dirname(dst), exist_ok=True)
        if not os.path.exists(dst) or open(dst, "rb").read() != open(src, "rb").read():
            shutil.copyfile(src, dst); copied += 1
        vox[key(ln["who"], ln["text"])] = ln["file"]
        keep.add(os.path.normpath(dst))
    s = s[:m.start(1)] + json.dumps(vox, ensure_ascii=False, indent=0) + s[m.end(1):]
    print(f"[{lang}] {len(vox)} lines linked, {copied} files copied, {missing} not generated yet")
removed = 0
for root, _, files in os.walk(os.path.join(HERE, "voices")):
    for f in files:
        full = os.path.normpath(os.path.join(root, f))
        if full not in keep:
            os.remove(full); removed += 1
open(P, "w", encoding="utf-8").write(s)
mb = sum(os.path.getsize(os.path.join(r, f)) for r, _, fs in os.walk(os.path.join(HERE, "voices")) for f in fs) / 1e6
print(f"{removed} old files removed · page {len(s)//1024} KB · voices/ {mb:.1f} MB")

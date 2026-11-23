"""Embed the asset kit's painted characters and animals into the game page.

Replaces only the single `const ART = {...};` line in index.html with entries built from
  characters/painted/<slug>.svg  (people)
  animals/painted/<name>.svg     (animals)
Each entry keeps the format of the entry it replaces: the mv-body wrapper, `class` instead
of `id` on layer groups, the `waver` class on the same group, hoisted <defs>, and the
bayuShirt -> bayuShirtP clip id. Limb rigging comes from the asset kit's tools/rig.py.

Idempotent: running it again on the same asset kit gives the same line.
Aborts (and writes nothing) if a class name from the current entry is missing in the new one.

Usage:
    python3 tools/painted_art.py ../assets
"""

import json
import os
import re
import sys

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PAGE = os.path.join(HERE, "index.html")

PEOPLE = {"raka": "raka", "laras": "laras", "bayu": "pak-bayu", "sari": "bu-sari", "dika": "dika",
          "ratna": "bu-ratna", "darto": "pak-darto", "putri": "kak-putri", "joko": "mas-joko",
          "hasan": "pak-hasan", "ijah": "nenek-ijah"}
ANIMALS = ["oyen", "kepi", "nyu", "cici", "rangga"]

ART_RE = re.compile(r"const ART = (\{.*?\});\n")
OPEN_RE = re.compile(r"<svg\b[^>]*>", re.S)
TITLE_RE = re.compile(r"<title>.*?</title>", re.S)
DEFS_RE = re.compile(r"<defs>.*?</defs>", re.S)
GROUP_CLASS_RE = re.compile(r'<g class="([^"]*)"')


def strip_svg(svg):
    """Return the inner markup of an <svg> document, without <title> and the root tag."""
    body = OPEN_RE.sub("", svg, count=1)
    body = body[: body.rindex("</svg>")]
    return TITLE_RE.sub("", body, count=1).strip()


def class_tokens(markup):
    tokens = set()
    for attr in GROUP_CLASS_RE.findall(markup):
        tokens.update(attr.split())
    return tokens


def waver_class(old):
    """The layer class that carries `waver` in the current entry, if any."""
    for attr in GROUP_CLASS_RE.findall(old):
        parts = attr.split()
        if "waver" in parts:
            return parts[0]
    return None


def build(svg_path, old, waver, bayu, foot):
    from rig import rig_document  # joints from the asset kit (assets/tools/rig.py)

    with open(svg_path, encoding="utf-8") as f:
        markup = strip_svg(f.read())
    markup = re.sub(r'<g id="([a-z-]+)"', r'<g class="\1"', markup)
    markup = rig_document(markup, "class")
    if bayu:
        markup = markup.replace('id="bayuShirt"', 'id="bayuShirtP"').replace("url(#bayuShirt)", "url(#bayuShirtP)")
    defs = "".join(DEFS_RE.findall(markup))
    markup = DEFS_RE.sub("", markup)
    if waver:
        markup = re.sub(r'<g class="%s"' % re.escape(waver), '<g class="%s waver"' % waver, markup, count=1)
    return defs + f'<g class="mv-body" style="transform-origin:100px {foot}px">{markup}</g>'


def main():
    if len(sys.argv) != 2:
        sys.exit("usage: python3 tools/painted_art.py ../assets")
    assets = os.path.abspath(sys.argv[1])
    sys.path.insert(0, os.path.join(assets, "tools"))

    with open(PAGE, encoding="utf-8") as f:
        page = f.read()
    m = ART_RE.search(page)
    if not m:
        sys.exit("const ART line not found in index.html")
    current = json.loads(m.group(1))

    jobs = [(k, os.path.join(assets, "characters/painted", PEOPLE[k] + ".svg"), 258) for k in PEOPLE]
    jobs += [(k, os.path.join(assets, "animals/painted", k + ".svg"), 186) for k in ANIMALS]

    new, total_old, total_new = {}, 0, 0
    for key, path, foot in jobs:
        old = current.get(key, "")
        value = build(path, old, waver_class(old), key == "bayu", foot)
        missing = class_tokens(old) - class_tokens(value)
        if missing:
            sys.exit(f"{key}: class names missing in the new entry: {sorted(missing)}; nothing written")
        new[key] = value
        ko, kn = len(old.encode()) / 1024, len(value.encode()) / 1024
        total_old += ko
        total_new += kn
        print(f"{key:7s} {ko:6.1f} KB -> {kn:6.1f} KB")
    print(f"total   {total_old:6.1f} KB -> {total_new:6.1f} KB")

    line = "const ART = " + json.dumps(new) + ";\n"
    page = page[: m.start()] + line + page[m.end():]
    with open(PAGE, "w", encoding="utf-8") as f:
        f.write(page)
    print("wrote", PAGE)


if __name__ == "__main__":
    main()

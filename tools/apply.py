import os, re, json, base64, sys
sys.path.insert(0, os.path.dirname(__file__))
from chars import CHARS
from animals import ANIMALS
from faces import FACE
from moves import CSS as MV_CSS, faces_data, runtime_js
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
P = os.path.join(HERE, "mystery-isles.html")
s = open(P).read()

def inner(c, foot=258):
    parts = []
    for lid, pivot, markup in c["layers"]:
        style = f' style="transform-origin:{pivot.replace(" ", "px ")}px"' if pivot else ""
        wave = " waver" if lid == c["wave"] else ""
        parts.append(f'<g class="{lid}{wave}"{style}>{markup}</g>')
    out = re.sub(r'<g id="([a-z-]+)"', r'<g class="\1"', "".join(parts))
    body = out.replace("url(#bayuShirt)", "url(#bayuShirtP)")
    return c["defs"].replace('id="bayuShirt"', 'id="bayuShirtP"') + f'<g class="mv-body" style="transform-origin:100px {foot}px">{body}</g>'

from people import NEW_PEOPLE
CHARS.update(NEW_PEOPLE)
from extras import CLUES2
ART = {"raka": inner(CHARS["raka"]), "laras": inner(CHARS["laras"]), "bayu": inner(CHARS["pak-bayu"]),
       "sari": inner(CHARS["bu-sari"]), "dika": inner(CHARS["dika"])}
for k, v in (("ratna", "bu-ratna"), ("darto", "pak-darto"), ("putri", "kak-putri"), ("joko", "mas-joko"), ("hasan", "pak-hasan"), ("ijah", "nenek-ijah")):
    ART[k] = inner(CHARS[v])
for k, c in ANIMALS.items(): ART[k] = inner(c, 186)
_clue = {f: m for _, f, _, _, m in CLUES2}
CLUE_SVG = {"ticket": _clue["clue-ticket"], "photo": _clue["clue-photo"], "umbrella": _clue["clue-umbrella"], "coin": _clue["clue-coin"],
            "stamp": '<rect x="5" y="3" width="16" height="20" rx="2" fill="#fff8e6" stroke="#8a6d3b"/><path d="M8 8h10M8 12h10M8 16h6" stroke="#8a6d3b" stroke-width="1.5"/><circle cx="18" cy="18" r="4" fill="none" stroke="#e8505c" stroke-width="1.6"/>'}
SLUG = {"raka": "raka", "laras": "laras", "bayu": "pak-bayu", "sari": "bu-sari", "dika": "dika",
        "ratna": "bu-ratna", "darto": "pak-darto", "putri": "kak-putri", "joko": "mas-joko", "hasan": "pak-hasan", "ijah": "nenek-ijah"}
PEOPLE = {k: CHARS[v] for k, v in SLUG.items()}
FACES = faces_data(PEOPLE, ANIMALS, lambda k: FACE.get(SLUG.get(k, k)) or (CHARS[SLUG[k]].get("face") if k in SLUG else None))
PORTRAIT = {k: CHARS[v].get("portrait", "38 14 124 124") for k, v in SLUG.items()}
USED = ["ui-tap", "ui-correct", "ui-wrong", "notebook-write", "clue-found", "badge-earned", "boat-move", "boat-bonk", "boat-arrive",
        "lamp-on", "bridge-alarm", "bridge-lift", "daily-chime", "oyen-meow", "oyen-purr", "kepi-snap", "nyu-blub", "cici-chirp", "rangga-call", "theme-island-night",
        "voice-raka", "voice-laras", "voice-pak-bayu", "voice-bu-sari", "voice-dika", "sting-surprised", "sting-thinking",
        "voice-bu-ratna", "voice-pak-darto", "voice-kak-putri", "voice-mas-joko", "voice-pak-hasan", "ferry-horn", "market-hello", "voice-nenek-ijah", "news-sting"]
SND = {k: "data:audio/mpeg;base64," + base64.b64encode(open(os.path.join(HERE, "snd-mp3", k + ".mp3"), "rb").read()).decode() for k in USED}

bundle = ("<script>\n/* Art and sound from the Pulau Misteri asset kit (generated). */\n"
          f"const ART = {json.dumps(ART)};\nconst SND = {json.dumps(SND)};\nconst PORTRAIT = {json.dumps(PORTRAIT)};\nconst CLUE_SVG = {json.dumps(CLUE_SVG)};\n"
          + runtime_js(FACES) + "</script>\n<style>" + MV_CSS + "</style>\n")

def rep(a, b, count=1):
    global s
    n = s.count(a)
    assert n == count, (n, a[:80])
    s = s.replace(a, b)

# remove a previous bundle if re-run
s = re.sub(r"<script>\n/\* Art and sound from the Pulau Misteri asset kit \(generated\). \*/\n.*?</script>\n", "", s, flags=re.S)
rep("<script>\nconst T = {", bundle + "<script>\nconst T = {")
open(P, "w").write(s)
print("bundle bytes", len(bundle))

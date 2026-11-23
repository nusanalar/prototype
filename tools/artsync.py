"""Export the asset kit's painted backgrounds as web-sized WebP into the prototype's art/ folder.

Reads <assets>/environment/painted/map/map-nusa-nalar.jpg and every <island>/<location>.jpg in
pattern-isle, lighthouse-isle and news-port (the _style folder is skipped). Each image is written to
art/<same relative path>.webp: the map at width 1600, locations at width 1280 (aspect kept, LANCZOS,
WebP quality 72, method 6). A file is rewritten only when its new bytes differ, so re-running is a no-op.
Prints one line per file with its size in KB and a total at the end.
Usage: python3 tools/artsync.py [path/to/assets]"""
import os, sys, io
from PIL import Image

HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = sys.argv[1] if len(sys.argv) > 1 else os.path.join(os.path.dirname(HERE), "assets")
SRC = os.path.join(ASSETS, "environment", "painted")
OUT = os.path.join(HERE, "art")
ISLANDS = ("pattern-isle", "lighthouse-isle", "news-port")
MAP_WIDTH, LOCATION_WIDTH = 1600, 1280
QUALITY, METHOD = 72, 6


def sources():
    """Yield (relative path under SRC, target width) for every painted background."""
    yield os.path.join("map", "map-nusa-nalar.jpg"), MAP_WIDTH
    for island in ISLANDS:
        folder = os.path.join(SRC, island)
        if not os.path.isdir(folder):
            continue
        for name in sorted(os.listdir(folder)):
            if name.lower().endswith(".jpg"):
                yield os.path.join(island, name), LOCATION_WIDTH


def encode(path, width):
    """Return the WebP bytes for one source image resized to the given width."""
    with Image.open(path) as im:
        im = im.convert("RGB")
        height = round(im.height * width / im.width)
        im = im.resize((width, height), Image.LANCZOS)
        buf = io.BytesIO()
        im.save(buf, "WEBP", quality=QUALITY, method=METHOD)
        return buf.getvalue()


def main():
    total = 0
    written = 0
    for rel, width in sources():
        src = os.path.join(SRC, rel)
        dst = os.path.join(OUT, os.path.splitext(rel)[0] + ".webp")
        data = encode(src, width)
        old = open(dst, "rb").read() if os.path.exists(dst) else None
        if old != data:
            os.makedirs(os.path.dirname(dst), exist_ok=True)
            with open(dst, "wb") as f:
                f.write(data)
            written += 1
        total += len(data)
        print(f"{os.path.relpath(dst, HERE)}  {len(data) / 1024:.1f} KB")
    print(f"total {total / 1024:.1f} KB ({total} bytes) in {len(list(sources()))} files, {written} rewritten")


if __name__ == "__main__":
    main()

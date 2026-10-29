"""Makes a project folder lighter: converts every PNG in ./assets to WebP and
updates index.html so it uses the new files.

  * big picture-like PNGs (over 1.2 MB: scene backgrounds, splash)  -> lossy WebP, quality 92
    (visually identical, roughly 10x smaller)
  * smaller PNGs (buttons, panels, characters, ...)                  -> lossless WebP (pixel-exact)

How to use (once, whenever you add new PNGs to the assets folder):
    pip install pillow
    python optimize_assets.py            # converts and deletes the PNGs it converted
    python optimize_assets.py --keep     # converts but keeps the original PNGs

Run it from the folder that holds index.html and assets/.
"""
import os
import re
import sys

from PIL import Image

QUALITY = 92
BIG = 1_200_000
KEEP = "--keep" in sys.argv

root = os.path.dirname(os.path.abspath(__file__))
assets = os.path.join(root, "assets")
index = os.path.join(root, "index.html")

with open(index, encoding="utf-8") as f:
    html = f.read()

converted = []
for name in sorted(os.listdir(assets)):
    if not name.lower().endswith(".png"):
        continue
    src = os.path.join(assets, name)
    dst = os.path.join(assets, name[:-4] + ".webp")
    size = os.path.getsize(src)
    im = Image.open(src)
    im.load()
    has_alpha = im.mode in ("RGBA", "LA") or "transparency" in im.info
    im = im.convert("RGBA" if has_alpha else "RGB")
    if size > BIG:
        im.save(dst, "WEBP", quality=QUALITY, method=6, alpha_quality=100)
    else:
        im.save(dst, "WEBP", lossless=True, method=6)
    converted.append(name)
    print(f"{name:32s} {size / 1024:8.0f} KB -> {os.path.getsize(dst) / 1024:6.0f} KB")

for name in converted:
    html = html.replace("assets/" + name, "assets/" + name[:-4] + ".webp")

with open(index, "w", encoding="utf-8") as f:
    f.write(html)

if not KEEP:
    for name in converted:
        os.remove(os.path.join(assets, name))

print(f"Done: {len(converted)} file(s) converted." + ("" if KEEP else " Original PNGs removed."))

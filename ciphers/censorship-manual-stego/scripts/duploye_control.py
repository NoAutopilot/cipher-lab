#!/usr/bin/env python3
"""Rule-3 matched control for the shorthand step (GAPS183, 3 Oct 2026).

Renders a random string of basic Duployan letters (Noto Sans Duployan, Unicode U+1BC00 block) at the stroke height
of the 'Mary Helen Shaw' signature crop (~60 px), blurs and downsamples it to the crop's effective resolution, and
writes the key to a separate file that the reader does not open until its transcription is recorded.

  python3 duploye_control.py --font NotoSansDuployan.ttf --out DIR [--seed 183 --n 7]
  python3 duploye_control.py --score DIR/key.txt --read "A R A ..."     # edit-distance accuracy
"""
import argparse, random, sys

INVENTORY = "P T F K L B D V G R M N J S A O I E".split()


def cp(name):
    import unicodedata
    return unicodedata.lookup("DUPLOYAN LETTER " + name)


def lev(a, b):
    d = list(range(len(b) + 1))
    for i, x in enumerate(a, 1):
        p, d[0] = d[0], i
        for j, y in enumerate(b, 1):
            p, d[j] = d[j], min(d[j] + 1, d[j - 1] + 1, p + (x != y))
    return d[-1]


def acc(key, read):
    return 1 - lev(key, read) / max(len(key), 1)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--font"); ap.add_argument("--out"); ap.add_argument("--seed", type=int, default=183)
    ap.add_argument("--n", type=int, default=7); ap.add_argument("--px", type=int, default=60)
    ap.add_argument("--score"); ap.add_argument("--read")
    a = ap.parse_args()
    if a.score:
        key = open(a.score).read().split()
        r = a.read.split()
        print(f"key={' '.join(key)} read={' '.join(r)} accuracy={acc(key, r):.3f}")
        return
    from PIL import Image, ImageDraw, ImageFont, ImageFilter
    rng = random.Random(a.seed)
    key = [rng.choice(INVENTORY) for _ in range(a.n)]
    f = ImageFont.truetype(a.font, a.px * 2)
    im = Image.new("L", (a.px * 3 * a.n + 100, a.px * 5), 255)
    dr = ImageDraw.Draw(im)
    x = 40
    for k in key:
        g = cp(k)
        dr.text((x, a.px * 2), g, font=f, fill=0)
        bb = dr.textbbox((x, a.px * 2), g, font=f)
        x = max(bb[2], x + 10) + a.px // 2
    im = im.crop((0, 0, x + 40, im.height)).filter(ImageFilter.GaussianBlur(1.5))
    im = im.resize((im.width // 2, im.height // 2)).resize((im.width, im.height))
    im.save(f"{a.out}/control.png")
    open(f"{a.out}/key.txt", "w").write(" ".join(key) + "\n")
    print(f"wrote {a.out}/control.png ({im.width}x{im.height}); key withheld in key.txt, n={a.n}")


if __name__ == "__main__":
    main()

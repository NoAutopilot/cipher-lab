"""Offline test for tools/numeral_page_detect.py: a synthetic digit-group page outscores a synthetic
joined-cursive page, and a blank page scores 0."""
import math
import os
import sys
import tempfile

from PIL import Image, ImageDraw

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import numeral_page_detect as d  # noqa: E402


def digit_page(path):
    im = Image.new("L", (600, 760), 235)
    dr = ImageDraw.Draw(im)
    for r in range(12):
        y = 60 + r * 52
        x = 50
        for g in range(8):
            for k in range(4):
                dr.rectangle([x, y, x + 7, y + 16], outline=20, width=2)  # upright, separate glyphs
                x += 12
            x += 18
    im.save(path)


def cursive_page(path):
    im = Image.new("L", (600, 760), 235)
    dr = ImageDraw.Draw(im)
    for r in range(12):
        y0 = 70 + r * 52
        for w in range(6):
            x0 = 50 + w * 85
            pts = [(x0 + t, y0 + 8 * math.sin(t / 4.0) + (14 * math.sin(t / 9.0) if t % 23 < 6 else 0))
                   for t in range(70)]
            dr.line(pts, fill=20, width=2)  # one joined word per stroke
    im.save(path)


def test_digits_beat_cursive():
    with tempfile.TemporaryDirectory() as t:
        a, b, c = (os.path.join(t, n) for n in ("dig.png", "cur.png", "blank.png"))
        digit_page(a)
        cursive_page(b)
        Image.new("L", (600, 760), 235).save(c)
        sa, sb, sc = d.score_image(a), d.score_image(b), d.score_image(c)
        assert sa > 2 * sb, (sa, sb)
        assert sc == 0.0


if __name__ == "__main__":
    test_digits_beat_cursive()
    print("ok")

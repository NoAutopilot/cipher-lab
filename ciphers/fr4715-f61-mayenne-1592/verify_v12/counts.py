#!/usr/bin/env python3
"""VERIFY-F61-V12 call C3: count crops. Each crop runs from a boxed start sign (red box, my own centres) to past the first word in
ordinary handwriting; the reader lists every mark after the box and before that word, each as cipher sign or punctuation/stray.
Expected (from the pass transcription, NOT from Tomokiyo): X1 L08 from L08/11: 3 cipher (control); X2 L11 from L11/9: 3 cipher
(control); X3 L03 from L03/13: 2 cipher by pass A, 3 if the H407 insertion holds (target); X4 L03 from L03/8: 7 by pass A, 8 if it holds
(target, second start); X5 L04 from L04/1: 0 cipher by the corrected file, 1 by pass A's OTHER (target, claim 4)."""
import os
from PIL import Image, ImageDraw
HERE = os.path.dirname(os.path.abspath(__file__)); SRC = f"{HERE}/../images/src_ark_12148_btv1b52509819x_f137_500_1880_3320_1420.jpg"
CROPS = {"X1": (1183, 990, 1120, 1850), "X2": (893, 1340, 830, 1560), "X3": (1809, 345, 1740, 2560),
         "X4": (1385, 345, 1310, 2560), "X5": (1319, 475, 1250, 1660)}   # box centre x, y, crop x0, x1
def main():
    im = Image.open(SRC).convert("RGB"); os.makedirs(f"{HERE}/sheets", exist_ok=True)
    for k, (cx, cy, x0, x1) in CROPS.items():
        c = im.crop((x0, cy - 120, x1, cy + 130)).copy(); d = ImageDraw.Draw(c)
        d.rectangle((cx - x0 - 48, 25, cx - x0 + 48, 225), outline=(230, 0, 0), width=4)
        c.save(f"{HERE}/sheets/C3_{k}.png")
if __name__ == "__main__": main()

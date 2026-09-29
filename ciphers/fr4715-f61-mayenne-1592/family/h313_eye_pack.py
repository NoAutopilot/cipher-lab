#!/usr/bin/env python3
"""H313 (runner 12 session_012eShPsWwW3quuzzUNV7nW5, 29 Sept 2026): an eye pack for the verifier on one question H302-H311 could not settle -- is
f.61's L02 opening mark the LL sign (read_call_U pass 1) or a clear 'Il' (pass 2)? One labelled sheet, images/person_pack_L02/L02_mark_pack.jpg, at the
crop geometry of family/h311_il_forced.py (LL and the L02 mark centroid-recentred): row 1 the two targets; row 2 f.61's clear 'Il' x2 and 'ella';
row 3 f.211r's doubled l x2 (ville, elle). Labels name every tile (this pack is for a person's eye, not a blind reader).
python3 h313_eye_pack.py SCRATCH   (needs SCRATCH/f211r_native.jpg, Gallica btv1b9059406b f362)"""
import os, sys
from PIL import Image, ImageDraw, ImageOps
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h311_il_forced as h
h.SCR[0] = sys.argv[1]
rows = [[("LL", "LL", "f61sheetB_L05", 3, 1330, "f.61 L05 16: LL (target)"), ("DISP", "", "f61sheetB_L02", 1, 425, "f.61 L02 opening mark (target)")],
        [("TEXT", "", "f61sheetB_L02", 3, 890, "f.61 L02: clear 'Il' (Il seroit)"), ("TEXT", "", "f61sheetB_L04", 2, 2065, "f.61 L04: clear 'Il' (Il a)"), ("TEXT", "", "f61sheetB_L07", 2, 1745, "f.61 L07: clear 'ella'")],
        [("TEXT", "", "f211r", 1790, 2995, "fr.3983 f.211r: 'ville'"), ("TEXT", "", "f211r", 1927, 2485, "fr.3983 f.211r: 'elle'")]]
cw, ch = 420, 380
sh = Image.new("RGB", (3 * cw, 3 * ch), "white"); d = ImageDraw.Draw(sh)
for r, row in enumerate(rows):
    for c, (kind, cls, sheet, seg, x, lab) in enumerate(row):
        k = "LL" if kind in ("LL", "DISP") else "TEXT"
        im = h.crop(k, cls, sheet, seg, x); im = ImageOps.autocontrast(im.resize((int(im.size[0] * 320 / im.size[1]), 320)), cutoff=1); im.thumbnail((cw - 20, 320))
        X, Y = c * cw + 10, r * ch + 40; sh.paste(im.convert("RGB"), (X, Y)); d.text((X, Y - 30), lab, fill=(0, 0, 160))
out = f"{HERE}/../images/person_pack_L02/L02_mark_pack.jpg"; sh.save(out, quality=82); print(out, os.path.getsize(out))

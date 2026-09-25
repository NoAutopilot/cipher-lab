#!/usr/bin/env python3
"""Crop individual sign images for the ciphertext-side atlas (ZX-349, 25 Sept 2026).

Reads the S01-S26 codes already assigned in key_alpha.tsv / key_nomen.tsv and crops one
image per code from the already-fetched key-leaf section images in images/atlas/. Writes
images/atlas/S02..S26_sign.jpg (S01 already exists as S01_letter_B_sign.png, left as-is),
a contact sheet images/atlas/sheet.jpg, and images/atlas/atlas.tsv (code, crop, shape
description only -- no letter value, per the brief).

Boxes below are hand-measured (visual inspection of each source crop this session) in the
source crop's own native pixel coordinates. Regenerate with: python3 build_atlas.py
"""
import csv
from pathlib import Path
from PIL import Image

HERE = Path(__file__).parent
ATLAS = HERE / "images" / "atlas"

# code -> (source_file, box=(l,t,r,b), shape description, output filename)
SIGNS = {
    "S01": (None, None,
            "ornate script capital, a looped flourish with a horizontal cross-stroke "
            "(superficially resembles a stylised N)", "S01_letter_B_sign.png"),
    "S02": ("p57_alpha_seg2.jpg", (10, 400, 150, 610),
            "bold ligature resembling 'H' or a doubled 'ff', two vertical strokes joined "
            "by a loop", "S02_sign.jpg"),
    "S03": ("p57_alpha_seg2.jpg", (310, 430, 470, 610),
            "cursive tailed loop, resembles a script lowercase e with a long trailing "
            "downward stroke", "S03_sign.jpg"),
    "S04": ("p57_alpha_seg5.jpg", (0, 540, 100, 660),
            "hash/lattice mark, two short strokes crossing two others (# shape)", "S04_sign.jpg"),
    "S05": ("p57_alpha_seg5.jpg", (0, 675, 150, 815),
            "small loop/squiggle, a compact cursive scribble", "S05_sign.jpg"),
    "S06": ("p57_doubles_nulles.jpg", (3020, 120, 3245, 275),
            "cursive ligature resembling numeral 2 joined to a looped f", "S06_sign.jpg"),
    "S07": ("p57_doubles_nulles.jpg", (3205, 120, 3390, 275),
            "looped ascender with a small closed loop at the top (resembles h or ff)", "S07_sign.jpg"),
    "S08": ("p57_doubles_nulles.jpg", (3375, 120, 3620, 275),
            "tall flourish with a horizontal cross-bar (resembles the shape of the word "
            "'Tour')", "S08_sign.jpg"),
    "S09": ("p57_doubles_nulles.jpg", (3625, 120, 3850, 275),
            "compact looped mark resembling an 'fc' ligature", "S09_sign.jpg"),
    "S10": ("p57_doubles_nulles.jpg", (3840, 120, 4085, 275),
            "tall looped ascender with a small closed loop at the top, resembling 'ft' or "
            "'gt'", "S10_sign.jpg"),
    "S11": ("p57_monosyl_row2.jpg", (2470, 290, 2615, 400),
            "small circle with a bar or cross through it", "S11_sign.jpg"),
    "S12": ("p57_monosyl_row2.jpg", (2780, 290, 2915, 400),
            "small cross/dagger mark, a short vertical stroke crossed once", "S12_sign.jpg"),
    "S13": ("p57_lastword_row.jpg", (2150, 300, 2265, 400),
            "plus/cross mark, two strokes crossing at right angles", "S13_sign.jpg"),
    "S14": ("p57_lastword_row.jpg", (3105, 280, 3225, 400),
            "script capital E-like loop with an open curl", "S14_sign.jpg"),
    "S15": ("p57_left_wordlist.jpg", (1210, 30, 1350, 140),
            "simple lowercase e-like loop", "S15_sign.jpg"),
    "S16": ("p57_left_wordlist.jpg", (1210, 240, 1360, 360),
            "tall long-s-like flourish, a single rising stroke with a small loop at top", "S16_sign.jpg"),
    "S17": ("p57_left_wordlist.jpg", (1150, 470, 1290, 590),
            "double-cross or ff/H-like ligature, two vertical strokes with a crossbar", "S17_sign.jpg"),
    "S18": ("p57_left_wordlist.jpg", (1070, 910, 1250, 1010),
            "figure-eight / infinity-shaped double loop", "S18_sign.jpg"),
    "S19": ("p57_left_wordlist.jpg", (1090, 1030, 1230, 1135),
            "circle-shaped mark, a simple closed loop", "S19_sign.jpg"),
    "S20": ("p57_left_wordlist.jpg", (1080, 1145, 1230, 1290),
            "looped capital resembling R, a loop with a trailing tail", "S20_sign.jpg"),
    "S21": ("p57_left_wordlist.jpg", (1050, 1270, 1200, 1380),
            "lowercase f-like mark with a descending tail", "S21_sign.jpg"),
    "S22": ("p57_left_wordlist.jpg", (1050, 1360, 1220, 1480),
            "looped/tailed mark, an open loop with a downward hook", "S22_sign.jpg"),
    "S23": ("p57_left_wordlist.jpg", (1050, 1510, 1220, 1600),
            "small x/z-like cursive mark, two crossing diagonal strokes", "S23_sign.jpg"),
    "S24": ("p57_left_wordlist.jpg", (1050, 1610, 1280, 1720),
            "two-letter-looking ligature (resembles L joined to a rounded B or figure 8)", "S24_sign.jpg"),
    "S25": ("p57_left_wordlist.jpg", (1050, 1780, 1210, 1860),
            "single cursive loop, an open oval stroke", "S25_sign.jpg"),
    "S26": ("p57_left_wordlist.jpg", (1020, 2270, 1270, 2360),
            "abbreviation-like mark ('nre') with a trailing flourish sign", "S26_sign.jpg"),
    "X?": (None, None,
           "reserved code for a shape a pass sees on the ciphertext lines that does not "
           "match any crop on this sheet -- describe it in the pass's own note column "
           "rather than guessing an S-code", None),
}


def main():
    ATLAS.mkdir(parents=True, exist_ok=True)
    rows = []
    for code, (src, box, desc, outname) in SIGNS.items():
        if src is None:
            crop_path = outname if outname else ""
            rows.append((code, f"atlas/{crop_path}" if crop_path else "(none)", desc))
            continue
        im = Image.open(ATLAS / src)
        crop = im.crop(box)
        # upscale small crops for legibility, cap width at 500
        if crop.width < 300:
            factor = min(3, max(1, 500 // max(1, crop.width)))
            crop = crop.resize((crop.width * factor, crop.height * factor), Image.LANCZOS)
        crop.save(ATLAS / outname, quality=92)
        rows.append((code, f"atlas/{outname}", desc))

    with open(ATLAS / "atlas.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["code", "crop", "shape_description"])
        for code, crop, desc in rows:
            w.writerow([code, crop, desc])

    # contact sheet: grid of all S01-S26 crops with code labels burned in via filename only
    # (no letter meaning drawn on the sheet)
    from PIL import ImageDraw
    thumb = 160
    cols = 6
    codes_for_sheet = [c for c in SIGNS if c != "X?"]
    rows_n = -(-len(codes_for_sheet) // cols)
    sheet = Image.new("RGB", (cols * thumb, rows_n * (thumb + 30)), "white")
    draw = ImageDraw.Draw(sheet)
    for i, code in enumerate(codes_for_sheet):
        crop_rel = rows[[r[0] for r in rows].index(code)][1]
        img_path = ATLAS.parent.parent / "images" if False else ATLAS.parent
        p = ATLAS.parent / crop_rel if not crop_rel.startswith("atlas/") else ATLAS / crop_rel[len("atlas/"):]
        im = Image.open(p).convert("RGB")
        im.thumbnail((thumb - 10, thumb - 10))
        x = (i % cols) * thumb
        y = (i // cols) * (thumb + 30)
        sheet.paste(im, (x + 5, y + 25))
        draw.text((x + 5, y + 5), code, fill="black")
    sheet.save(ATLAS / "sheet.jpg", quality=90)
    print(f"wrote {len(rows)} atlas rows, sheet.jpg {sheet.size}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""H74 (3 Oct 2026): cut every ink component of the corrected shorthand line crops into sign-sorter tiles.

Line set = H58/H61's corrected mapping (h58/shorthand_lines.tsv): page 1 and page 3 crops from images/shorthand/ as they
are; page 2 by physical line -- phys 2 = page2_L02 (frame 0032), phys 3 = page2_L04, phys 6 = page2_L06 (0032),
phys 10 = page2_L11, phys 1/4/7/11/13 = h58/crops/; page2_L01 (blank header), L03 and L07 (second exposures of phys 2
and 6), L10 and L13 (numeral-only lines) and page1_L03 (the empty band above page 1's first line, H58) are left out.

Cut rule (deterministic, no model): grey < 150 is ink; 3x3 closing joins hairline breaks; 8-connected components;
components within 6 px horizontally and overlapping in x-extent by >= 50 pct of the smaller are NOT merged (a dot over a
stroke stays its own tile, the sorter's ASIDE/BAD-CUT piles take it). Kept: area >= 12 px, darkest pixel < 80 (drops grey bleed-through specks), width < 25 pct of the crop,
height < 85 pct of the crop (drops the black gutter block), and centre within 50 px of the line's row-ink peak (drops
fragments of the lines above and below). Numerals are cut too: the person piles them as non-letters. A component that
joins two signs or splits one is left as cut, for the BAD-CUT pile. Writes h74/signs.tsv, labels.tsv, pages.json,
lines.tsv (count per line), focus.tsv. Labels: every tile starts '?' (no line has positional labels: h59/person_labels.tsv
is empty and B35's / Tomokiyo's type lists carry no x positions)."""
import json, os, sys
import cv2, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
REPO = os.path.dirname(os.path.dirname(T))
SH = "images/shorthand"
LINES = [  # (line id, crop path relative to target, physical line note)
    ("p1L04", f"{SH}/page1_L04_seq3-13_1marks.jpg"),
    ("p1L05", f"{SH}/page1_L05_seq14-25_5marks.jpg"), ("p1L06", f"{SH}/page1_L06_seq26-39_8marks.jpg"),
    ("p1L07", f"{SH}/page1_L07_seq40-50_2marks.jpg"), ("p1L09", f"{SH}/page1_L09_seq61-79_17marks.jpg"),
    ("p1L10", f"{SH}/page1_L10_seq80-93_10marks.jpg"), ("p1L12", f"{SH}/page1_L12_seq106-121_16marks.jpg"),
    ("p1L13", f"{SH}/page1_L13_seq122-141_19marks.jpg"), ("p1L17", f"{SH}/page1_L17_seq173-187_11marks.jpg"),
    ("p2L01", "h58/crops/page2_phys01_f0031_y280-414.jpg"), ("p2L02", f"{SH}/page2_L02_seq198-212_15marks.jpg"),
    ("p2L03", f"{SH}/page2_L04_seq227-240_6marks.jpg"), ("p2L04", "h58/crops/page2_phys04_f0031_y649-783.jpg"),
    ("p2L06", f"{SH}/page2_L06_seq250-264_12marks.jpg"), ("p2L07", "h58/crops/page2_phys07_f0031_y1084-1218.jpg"),
    ("p2L10", f"{SH}/page2_L11_seq312-322_1marks.jpg"), ("p2L11", "h58/crops/page2_phys11_f0031_y1670-1804.jpg"),
    ("p2L13", "h58/crops/page2_phys13_f0031_y1981-2115.jpg"),
    ("p3L01", f"{SH}/page3_L01_seq368-381_8marks.jpg"), ("p3L03", f"{SH}/page3_L03_seq392-403_6marks.jpg"),
    ("p3L04", f"{SH}/page3_L04_seq404-416_5marks.jpg"), ("p3L05", f"{SH}/page3_L05_seq417-426_7marks.jpg"),
    ("p3L06", f"{SH}/page3_L06_seq427-438_2marks.jpg"), ("p3L07", f"{SH}/page3_L07_seq439-451_9marks.jpg"),
    ("p3L08", f"{SH}/page3_L08_seq452-464_7marks.jpg"), ("p3L09", f"{SH}/page3_L09_seq465-476_2marks.jpg"),
    ("p3L12", f"{SH}/page3_L12_seq498-510_7marks.jpg"), ("p3L13", f"{SH}/page3_L13_seq511-528_18marks.jpg"),
]

def cut(img):
    h, w = img.shape
    ink = (img < 150).astype(np.uint8)
    ink = cv2.morphologyEx(ink, cv2.MORPH_CLOSE, np.ones((3, 3), np.uint8))
    prof = np.convolve(ink.sum(1).astype(float), np.ones(15) / 15, "same")
    # gutter block distorts the profile: compute it without columns that are mostly ink
    dense = ink.mean(0) > 0.6
    prof = np.convolve(ink[:, ~dense].sum(1).astype(float), np.ones(15) / 15, "same")
    peak = int(prof.argmax())
    n, lab, st, cen = cv2.connectedComponentsWithStats(ink, 8)
    out = []
    for i in range(1, n):
        x, y, bw, bh, a = st[i]
        if a < 12 or img[lab == i].min() >= 80 or bw >= 0.25 * w or bh >= 0.85 * h or abs(cen[i][1] - peak) > 50:
            continue
        out.append((int(x), int(y), int(bw), int(bh), int(a)))
    return sorted(out), peak

def main():
    signs = ["sid\tpage\tx\ty\tw\th"]; labels = ["sid\tsign\tfamily"]; pages = {}; counts = ["line\tcrop\trow_peak\ttiles"]
    for lid, rel in LINES:
        img = cv2.imread(os.path.join(T, rel), 0)
        comps, peak = cut(img)
        pages[lid] = {"image": f"ciphers/armstrong-madison-1808/{rel}"}
        for k, (x, y, bw, bh, a) in enumerate(comps, 1):
            sid = f"{lid}_{k:02d}"
            signs.append(f"{sid}\t{lid}\t{x}\t{y}\t{bw}\t{bh}"); labels.append(f"{sid}\t?\tunsorted")
        counts.append(f"{lid}\t{rel}\t{peak}\t{len(comps)}")
    for name, rows in (("signs.tsv", signs), ("labels.tsv", labels), ("lines.tsv", counts)):
        open(os.path.join(H, name), "w").write("\n".join(rows) + "\n")
    json.dump(pages, open(os.path.join(H, "pages.json"), "w"), indent=1)
    print("\n".join(counts)); print("tiles:", len(signs) - 1)
    if len(sys.argv) > 1:  # debug overlays to a scratch dir
        for lid, rel in LINES:
            img = cv2.cvtColor(cv2.imread(os.path.join(T, rel), 0), cv2.COLOR_GRAY2BGR)
            for r in signs[1:]:
                s, p, x, y, bw, bh = r.split("\t")
                if p == lid: cv2.rectangle(img, (int(x), int(y)), (int(x) + int(bw), int(y) + int(bh)), (0, 0, 255), 1)
            cv2.imwrite(os.path.join(sys.argv[1], f"{lid}.jpg"), img)

if __name__ == "__main__":
    main()

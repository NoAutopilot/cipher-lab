#!/usr/bin/env python3
"""H59: person-read labelling pack for the Armstrong shorthand signs. Four lines that are shorthand from end to end:
page 1 physical lines 9 and 10 (images/shorthand/page1_L12, page1_L13), page 2 physical line 2 (page2_L03, frame 0031)
and page 3's last shorthand line (page3_L13). Each sheet is the crop at 2x in two overlapping halves with a ruler
under it: a tick and a blue number every 50 native px (the number is the native x in the crop). The person writes, left
to right, the ruler number at the left edge of each sign and its type on Tomokiyo's sheet (tomokiyo_38_types.png).
Components are NOT numbered automatically: tests on these crops (28 Sept 2026) showed connected-component numbering
splits and drops real signs where a line's crop cuts them; H60 matches the person's x positions to components itself.
Nothing here reads the cipher.
usage: python3 h59/build_pack.py"""
import os, shutil, cv2, numpy as np
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); OUT = os.path.join(H, "person_pack")
os.makedirs(OUT, exist_ok=True)
LINES = [("S1", "page1_L12_seq106-121_16marks.jpg"), ("S2", "page1_L13_seq122-141_19marks.jpg"),
         ("S3", "page2_L03_seq213-226_9marks.jpg"), ("S4", "page3_L13_seq511-528_18marks.jpg")]
rows = ["sheet\tsource_crop\twidth_px"]
for tag, f in LINES:
    g = cv2.imread(os.path.join(T, "images", "shorthand", f), 0); s = 2
    img = cv2.cvtColor(cv2.resize(g, None, fx=s, fy=s, interpolation=cv2.INTER_CUBIC), cv2.COLOR_GRAY2BGR)
    ruler = np.full((60, img.shape[1], 3), 255, np.uint8)
    for x in range(0, g.shape[1], 25):
        big = x % 50 == 0; cv2.line(ruler, (x * s, 0), (x * s, 22 if big else 10), (255, 0, 0), 2 if big else 1)
        if big: cv2.putText(ruler, str(x), (x * s - 14, 48), cv2.FONT_HERSHEY_SIMPLEX, 0.6, (255, 0, 0), 2)
    img = np.vstack([img, ruler]); half = img.shape[1] // 2
    cv2.imwrite(os.path.join(OUT, f"{tag}a_{f[:9]}.jpg"), img[:, :half + 150], [cv2.IMWRITE_JPEG_QUALITY, 85])
    cv2.imwrite(os.path.join(OUT, f"{tag}b_{f[:9]}.jpg"), img[:, half - 150:], [cv2.IMWRITE_JPEG_QUALITY, 85])
    rows.append(f"{tag}\timages/shorthand/{f}\t{g.shape[1]}")
shutil.copy(os.path.join(T, "line-b", "b35", "tomokiyo_sheet.png"), os.path.join(OUT, "tomokiyo_38_types.png"))
open(os.path.join(OUT, "sheets.tsv"), "w").write("\n".join(rows) + "\n"); print("\n".join(rows))

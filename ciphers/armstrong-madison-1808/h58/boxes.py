#!/usr/bin/env python3
"""H58: locate every images/shorthand/ line crop in its frame (NCC, coarse 1/4 then native) and draw the boxes on the
page for a look. page1 -> frame 0030; page2 -> frame 0031 left; page3 -> frame 0031 right. Writes h58/crop_positions.tsv
and overlays (scratch dir given as argv[1])."""
import os, sys, cv2
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); out = sys.argv[1]
sys.path.insert(0, os.path.join(T, "h55"))
def locate(tpl, img):
    s = 0.25
    r = cv2.matchTemplate(cv2.resize(img, None, fx=s, fy=s, interpolation=cv2.INTER_AREA), cv2.resize(tpl, None, fx=s, fy=s, interpolation=cv2.INTER_AREA), cv2.TM_CCOEFF_NORMED)
    _, _, _, (x, y) = cv2.minMaxLoc(r); x, y = int(x / s), int(y / s); pad = 24
    x0, y0 = max(0, x - pad), max(0, y - pad); win = img[y0:y0 + tpl.shape[0] + 2 * pad, x0:x0 + tpl.shape[1] + 2 * pad]
    r = cv2.matchTemplate(win, tpl, cv2.TM_CCOEFF_NORMED); _, v, _, (dx, dy) = cv2.minMaxLoc(r)
    return x0 + dx, y0 + dy, v
fr = {"page1": "30", "page2": "31", "page3": "31"}
imgs = {f: cv2.imread(os.path.join(T, "images", f"M34-014-00{f}.jpg"), 0) for f in ("30", "31")}
over = {k: cv2.cvtColor(imgs[f], cv2.COLOR_GRAY2BGR) for k, f in fr.items()}
rows = ["crop\tframe\tx\ty\tw\th\tncc"]; cols = [(0, 0, 255), (0, 160, 0), (255, 0, 0), (0, 140, 255), (200, 0, 200)]
for i, n in enumerate(sorted(f for f in os.listdir(os.path.join(T, "images", "shorthand")) if f.endswith(".jpg"))):
    pg = n[:5]; tpl = cv2.imread(os.path.join(T, "images", "shorthand", n), 0); h, w = tpl.shape
    x, y, v = locate(tpl, imgs[fr[pg]]); rows.append(f"{n}\t{fr[pg]}\t{x}\t{y}\t{w}\t{h}\t{v:.3f}")
    c = cols[i % 5]; cv2.rectangle(over[pg], (x, y), (x + w, y + h), c, 4)
    cv2.putText(over[pg], n[6:9], (x + w - 160, y + 40), cv2.FONT_HERSHEY_SIMPLEX, 1.4, c, 3)
open(os.path.join(H, "crop_positions.tsv"), "w").write("\n".join(rows) + "\n")
cv2.imwrite(os.path.join(out, "p1boxes.jpg"), cv2.resize(over["page1"], None, fx=0.38, fy=0.38))
cv2.imwrite(os.path.join(out, "p3boxes.jpg"), cv2.resize(over["page3"][:, 1900:], None, fx=0.4, fy=0.4))
print("\n".join(rows))

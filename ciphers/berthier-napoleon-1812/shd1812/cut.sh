#!/bin/sh
# GF4d (3 Oct 2026): one tools/iiif_lines.py --image run per table column strip; --centres = the cell centres from
# grid.py, so the tool's band edges fall on the ruled lines and each crop is one 10-code cell.
cd "$(dirname "$0")/../../.."
D=ciphers/berthier-napoleon-1812/shd1812
python3 - "$D" <<'PY'
import json, subprocess, sys
D = sys.argv[1]
g = json.load(open(D + "/grid.json"))
# image -> (hundreds per strip, x bounds per strip, rule y list per strip); strips read by eye from tops.jpg
plan = {
 "1812_0001.jpg": (0, [(375,849),(849,1330),(1330,1832),(1832,2334),(2334,2859),(2859,3352),(3352,3846)]),
 "1812_0051.jpg": (0, [(510,1073),(1073,1551),(1551,2059),(2059,2572),(2572,3094),(3094,3600),(3560,4000)]),
 "1812_0701.jpg": (7, [(60,598),(598,1138),(1138,1682),(1682,2232),(2232,2791),(2791,3356),(3356,3894)]),
 "1812_0751.jpg": (7, [(110,628),(628,1186),(1186,1716),(1716,2288),(2288,2807),(2807,3369),(3369,3942)]),
}
for img, (h0, xs) in plan.items():
    strips = g[img]["strips"]
    for k, (x0, x1) in enumerate(xs):
        mid = (x0 + x1) / 2
        s = min(strips, key=lambda s: abs((s["x0"] + s["x1"]) / 2 - mid))
        ys = [y for i, y in enumerate(s["h"]) if i == 0 or y - s["h"][i - 1] > 200]
        if img == "1812_0001.jpg" and k == 0: ys = [345] + ys
        if img == "1812_0051.jpg": ys = ys[:6]
        ys = ys[:6]
        top, bot = ys[0] - 30, ys[-1] + 30
        cen = [int((a + b) / 2) - top for a, b in zip(ys, ys[1:])]
        x0m, x1m = max(0, x0 - 40), min(4000, x1 + 40)
        half = "a" if img in ("1812_0001.jpg", "1812_0701.jpg") else "b"
        cmd = ["python3", "tools/iiif_lines.py", "--image", f"{D}/{img}", "--out", f"{D}/crops",
               "--region", f"{x0m},{top},{x1m-x0m},{bot-top}", "--centres", ",".join(map(str, cen)),
               "--lines-per-crop", "1", "--prefix", f"h{h0+k:02d}{half}"]
        print(" ".join(cmd)); subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
PY

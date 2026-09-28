#!/usr/bin/env python3
"""F61-CA-HAND (campaign step H63, 28 Sept 2026, runner session_01J8hunWPcE7QYcpCx59CUHV): are f.61's 'cursive a' signs (CA:
Tomokiyo's nulls, H44; H4's dash-share rule) cipher signs at all, or letters of the clear text at the run edges (H2's pass B
flagged extra a-shapes as handwriting)?

Pre-registered before the call (prompt in scripts/PROMPTS.md, H63). Expected CA positions from disk: pass A's CA on the six
span lines (L01/8, L03/1, L03/9, L05/7, L05/8, L07/1, L08/10) and pass U2's on L10 (2, 9, 12): 10 signs on seven sheets B.
The reader lists every a-shaped mark inside or at the edge of a cipher run on those sheets with a hand verdict (cipher /
text) and, as a control, ten clear-text a's from the same lines (which must come back 'text'). Pairing per sheet in order;
a sheet whose CA count differs from the expected count is dropped. Pre-registered verdict: CA = text letters if >= 8 of the
reconciled CA positions are judged 'text' AND >= 9 of the 10 control a's are 'text'; CA = cipher signs (the nulls stand) if
<= 2 are 'text' with the same control; otherwise untestable by this call. Either way no letter is read.
  python3 scripts/f61ca.py score read_call_CA.tsv [--check]
"""
import csv, os, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
EXP = {"f61sheetB_L01": [8], "f61sheetB_L03": [1, 9], "f61sheetB_L05": [7, 8], "f61sheetB_L07": [1], "f61sheetB_L08": [10], "f61sheetB_L10": [2, 9, 12]}
def main(path):
    rows = list(csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"))
    ca = defaultdict(list); ctrl = []
    for r in rows:
        (ctrl if r["kind"].strip().lower() == "control" else ca[r["sheet"].replace(".jpg", "")]).append(r)
    out = [f"{path}: {sum(len(v) for v in ca.values())} a-shaped marks in/at cipher runs listed, {len(ctrl)} control a's"]
    text = cipher = 0; scored = 0
    for sheet, pos in EXP.items():
        g = sorted(ca.get(sheet, []), key=lambda r: (int(r["segment"]), float(r["x_px"])))
        if len(g) != len(pos): out.append(f"  {sheet}: expected {len(pos)}, listed {len(g)} -> NOT reconciled, dropped"); continue
        for r, p in zip(g, pos):
            v = r["hand"].strip().lower(); scored += 1; text += v == "text"; cipher += v == "cipher"
            out.append(f"  {sheet}/{p} CA: {v} ({r.get('note','')[:80]})")
    ctext = sum(1 for r in ctrl if r["hand"].strip().lower() == "text")
    out.append(f"scored {scored} of 10 CA positions: text {text}, cipher {cipher}; control a's judged text {ctext}/{len(ctrl)}")
    if scored < 6 or len(ctrl) < 8: verdict = "untestable (too few reconciled positions or controls)"
    elif ctext < 0.9 * len(ctrl): verdict = "untestable (control a's not judged text)"
    elif text >= 8 and scored >= 8: verdict = "CA = text letters (not cipher signs): drop from the skeleton"
    elif text <= 2: verdict = "CA = cipher signs (Tomokiyo's nulls stand)"
    else: verdict = "untestable by this call (mixed)"
    out.append("VERDICT H63: " + verdict)
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61ca_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main(sys.argv[2])

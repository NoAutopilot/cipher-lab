#!/usr/bin/env python3
"""H414 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: f.61's two OTHER signs (the meter's 'wider 2').
Positions by the runner's eye on the native region image (no position file has L02 or L04): L02/2 x 322, y 215 (the barred double stroke after
the PHI at x ~240); L04/2 x 1420, y 475 (after the LOOPBAR at x ~1330: to the runner's eye a dot). H411's references R1-R12 plus R13 HASH4
(L01/11), R14 ZHOOK (L07/3), R15 4TRI (L03/7); H411's 18 known items; both targets at W1 -45/+92, W2 -60/+55, W3 -70/+110; shuffled (seed 414).
Prompt: H410's, with 'answer P if the marked mark is punctuation or not a cipher sign'.
score -- GATE >= 16/18 known. Pre-stated per target: the same answer at >= 2 of 3 windows is the answer, else 'unclear'.
python3 h414_other_two.py tiles SCRATCH | score [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE); CHECK = "--check" in sys.argv
import h411_class_qa as q
REFS = q.REFS + [("HASH4", "L01", "11"), ("ZHOOK", "L07", "3"), ("4TRI", "L03", "7")]
EYE = {("L02", "2"): ("OTHER", 322, 215), ("L04", "2"): ("OTHER", 1420, 475)}
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    G = q.geo(); G.update(EYE); im = Image.open(h.REG).convert("RGB"); os.makedirs(f"{scratch}/h414", exist_ok=True)
    for c, l, p in REFS: assert G[(l, p)][0] == c, (c, l, p)
    refs = [h.strip(im, G[(l, p)][1], G[(l, p)][2], 45, 92, f"R{k}") for k, (c, l, p) in enumerate(REFS, 1)]
    sh = Image.new("RGB", (4 * 370, 4 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(refs)]; sh.save(f"{scratch}/h414/references.jpg", quality=90)
    its = [(w, l, p, up, dn) for l, p in EYE for w, up, dn in (("W1", 45, 92), ("W2", 60, 55), ("W3", 70, 110))] + [("K", l, p, 45, 92) for c, l, p in q.KNOWN]
    random.Random(414).shuffle(its); cl = [r[0] for r in REFS]; key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, l, p, up, dn) in enumerate(its, 1):
        c, x, yc = G[(l, p)]; ims.append(h.strip(im, x, yc, up, dn, f"I{n:02d}")); key.append(f"I{n:02d}\t{kind}\t{c}\t{l}\t{p}\t{'R' + str(cl.index(c) + 1) if kind == 'K' else ''}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims[s:s + 20])]; sh.save(f"{scratch}/h414/items_{s // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h414_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h414_reply.tsv")}; it = q.rd(f"{HERE}/h414_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn); names = {f"R{k}": c for k, (c, _, _) in enumerate(REFS, 1)}
    out = [f"gate: {g}/18 known (>= 16)"]
    if g < 16: out.append("CONTROL FAIL -- nothing scored")
    else:
        from collections import Counter
        for l, p in EYE:
            w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if (r["line"], r["pos"]) == (l, p)), key=lambda r: r["kind"])]
            top, n = Counter(w).most_common(1)[0]; ro = (names.get(top, "punctuation / not a cipher sign" if top == "P" else top.lower())) if n >= 2 else "unclear"
            out.append(f"{l}/{p} W1-W3: {w} -> {ro}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h414_other_two_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()

#!/usr/bin/env python3
"""H212 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): a blind shape sort of the HASH4 signs on the two f.61-hand leaves of fr.3983 f.108,
whose sequences lean differently (H211: f.108v d/q, f.108r i/x). Written before the call.
 tiles SCRATCH: f.108v = the 14 H59 draft columns coded HASH4 (x from pass A, as h199_bowl_108v.py maps them; 3x crops sheets/f108v3y|3z_*, 600-px
   window scaled 0.6); f.108r = the 10 HASH4 rows of the H108 draft (scripts/f61recon108r_draft.tsv, all on L06; crops images/f108h/, 640-px window
   scaled 0.5625). Each tile marked by two short red ticks, one above and one below the target, numbered T01..T24, shuffled (seed 212), leaf hidden;
   one sheet <scratch>/h212/sheet_01.jpg. Key h212_items.tsv committed before the call.
 One blind call, the H89 sort design: fixed attributes per tile, then 2-4 shape groups and a one-sentence criterion, no letters.
 score: tiles in group 'none' left out. Let G be the group holding the most f.108v tiles: Fisher exact test of (in G / not in G) x (f.108v / f.108r).
   Pre-stated read-out: "the two leaves use different hash forms" iff p < 0.05 and G holds >= 0.7 of f.108v's sorted tiles and <= 0.3 of f.108r's;
   else "no leaf-linked hash form shown". Descriptive; a positive result would license a follow-up against period letters, not a key change.
  python3 h212_hash_sort.py tiles SCRATCH | score [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h199_bowl_108v as H
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def items():
    from collections import defaultdict
    A = defaultdict(list)
    for r in rd(f"{H.P}/f108v3z_signsA.tsv"): A[r["line"]].append(r)
    rec = {(r["line"], r["position"]): r["sign"] for r in rd(f"{H.P}/f108v3z_draft_reconciled.tsv")}; out = []
    for l in sorted(A):
        k = 0
        for c in (r for r in rd(f"{H.P}/f108v3z_recon_task.tsv") if r["line"] == l):
            if c["alt"].startswith("A:-"): continue
            a = A[l][k]; k += 1
            if rec.get((l, c["position"])) == "HASH4": out.append(dict(leaf="108v", line=l, seg=a["segment"], x=int(a["x_px"]), crop=H.crop(l, a["segment"]), W=600, s=0.6))
    for r in rd(f"{HERE}/../scripts/f61recon108r_draft.tsv"):
        if r["sign"] == "HASH4":
            out.append(dict(leaf="108r", line=r["line"], seg=r["segment"], x=int(r["x_px"]), crop=f"{HERE}/../images/f108h/f108h_{r['line']}_{r['segment']}.jpg", W=640, s=0.5625))
    return out
def tiles(scratch):
    from PIL import Image, ImageDraw
    its = items(); random.Random(212).shuffle(its); os.makedirs(f"{scratch}/h212", exist_ok=True); ims = []; key = ["item\tleaf\tline\tsegment\tx_px"]
    for n, t in enumerate(its, 1):
        im = Image.open(t["crop"]).convert("RGB"); W, s = t["W"], t["s"]; x0 = max(0, min(im.width - W, t["x"] - W // 2))
        w = im.crop((x0, 0, x0 + W, im.height)); w = w.resize((int(W * s), int(im.height * s)))
        c = Image.new("RGB", (370, 220), "white"); c.paste(w, (5, 14)); d = ImageDraw.Draw(c); mx = 5 + int((t["x"] - x0) * s); y = 14 + w.height
        d.line([(mx, 0), (mx, 11)], fill=(220, 0, 0), width=3); d.line([(mx, y + 2), (mx, y + 13)], fill=(220, 0, 0), width=3)
        d.text((6, y + 4), f"tile {n}", fill=(0, 0, 0)); ims.append(c); key.append(f"T{n:02d}\t{t['leaf']}\t{t['line']}\t{t['seg']}\t{t['x']}")
    sh = Image.new("RGB", (4 * 370, 6 * 220), "white")
    for k, c in enumerate(ims): sh.paste(c, ((k % 4) * 370, (k // 4) * 220))
    sh.save(f"{scratch}/h212/sheet_01.jpg", quality=88)
    open(f"{HERE}/h212_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "tiles", Counter(t["leaf"] for t in its))
def score():
    import h190_4fam as h190
    key = {r["item"]: r for r in rd(f"{HERE}/h212_items.tsv")}
    rep = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in rd(f"{HERE}/passes/h212_sort.tsv")}
    rows = [(key[m]["leaf"], g) for m, g in rep.items() if g.lower() != "none"]
    G = Counter(g for leaf, g in rows if leaf == "108v").most_common(1)[0][0]
    a = sum(1 for l, g in rows if l == "108v" and g == G); b = sum(1 for l, g in rows if l == "108v" and g != G)
    c = sum(1 for l, g in rows if l == "108r" and g == G); d = sum(1 for l, g in rows if l == "108r" and g != G); p = h190.fisher(a, b, c, d)
    out = ["groups by leaf: " + "; ".join(f"{g}: f.108v {sum(1 for l, x in rows if l == '108v' and x == g)} f.108r {sum(1 for l, x in rows if l == '108r' and x == g)}" for g in sorted({g for _, g in rows})),
           f"group G (most f.108v) = {G}: f.108v in G {a}/{a + b}, f.108r in G {c}/{c + d}; Fisher p {p:.2g}; none {sum(1 for g in rep.values() if g.lower() == 'none')}"]
    ok = p < 0.05 and a / max(1, a + b) >= 0.7 and c / max(1, c + d) <= 0.3
    out.append("read-out: " + ("the two leaves use different hash forms" if ok else "no leaf-linked hash form shown"))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h212_hash_sort_result.txt"
    if "--check" in sys.argv:
        ok2 = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok2 else "STALE"); sys.exit(0 if ok2 else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else score()

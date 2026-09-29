#!/usr/bin/env python3
"""H398 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: VERIFY-F61-V11's own f.101r bowl labels agreed with the
runner's (H362/H365) only at kappa 0.49 (B, 34 tokens) and 0.35 (E, 36), while runner re-reads repeat at 0.81-0.88 (H390/H391). Is the disagreement
V11's design (tiles, prompt, anchors) or reader variation?
 targets -- every f.101r target token of V11's calls c1, c2 (v11_items.tsv) and c4, c5 (v11e_items.tsv), first occurrences only (repeats dropped), cut
   with V11's OWN tile geometry (verify_v11/v11_bowl.tile: 220 native px wide, x1.6, rows centre -75/+60 from V11's pool, 360x262 tile, marker above
   the strip) from the native f.101r (Gallica btv1b9060543f f210) -- ONE CHANGE, disclosed before the call: the marker is drawn red, not V11's blue,
   so that H359's prompt ("a red triangle ABOVE the strip, pointing down") is true of the tiles; its place is V11's.
 known part-2 strips (gate 2) -- H377's 6 known f.61 tiles (h377_items.tsv K rows: 3 yes 4TRI, 3 no C43) cut in the same V11 tile format from the f.61
   native region image, at H367's vertical window (-45/+92: the f61 band midpoint sits high; V11's window would clip f.61's stems -- H367's note).
 shuffled (seed 398), R01.., 12 per sheet, SCRATCH/h398/sheet_NN.jpg. Part 1 = H193's 60 strips (regenerated from natives f327/f328,
   h193_items.tsv byte-identical). One blind Opus call, H359's prompt verbatim with part 2 = the h398 sheets. The runner does not look at the sheets.
 score -- GATE 1 >= 17/20 H193 anchors; GATE 2 >= 5/6 known strips; either failing -> CONTROL FAIL, nothing scored.
   Pre-stated read-out (tokens answered yes/no by both labellers): kappa(new, runner) >= 0.6 and kappa(new, V11) < 0.6 -> "the disagreement is V11's
   design (tiles/prompt)"; the reverse -> "the runner's design"; both >= 0.6 -> "reader variation"; else "unclear". Note: the new read uses V11's
   TILES and the runner's PROMPT and gates, so "V11's design" here can only mean V11's prompt/anchors, and "the runner's design" the runner's tiles.
   Also reported (descriptive known answer, V11's own crosstab functions): period-letter tracking (bowl -> c/p/t, no -> a/n) of each labelling on the
   same tokens. No key, cell or grade change.
 python3 h398_bowl_design.py tiles SCRATCH F61REGION | score [--check]"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; V = f"{HERE}/../verify_v11"; sys.path.insert(0, V); sys.path.insert(0, HERE)
import v11_bowl as B, v11_crosstab as X
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def v11_labels():
    lab = {}
    for items, calls in (("v11_items.tsv", ("c1", "c2")), ("v11e_items.tsv", ("c4", "c5"))):
        its = rd(f"{V}/{items}")
        for c in calls:
            ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{V}/v11_reply_{c}.tsv")}
            for r in its:
                if r["call"] == c and r["role"] == "target" and r["leaf"] == "f101r" and not r["repeat_of"]:
                    lab.setdefault((r["line"], r["pos_or_seg"]), ans.get(r["id"], "missing"))
    return lab
def items():
    geo = {(t[1], t[2]): t for t in B.pool("f101r", 80)}; lab = v11_labels(); out = []
    for k in sorted(lab):
        _, line, pos, x, yc = geo[k]; out.append(("T", "4TRI", line, pos, x, yc - 75, yc + 60, ""))
    for r in rd(f"{HERE}/h377_items.tsv"):
        if r["kind"].startswith("K"):
            x, yc = int(r["x_native"]), int(r["y_centre"]); out.append(("K", r["code"], r["line"], r["pos"], x, yc - 45, yc + 92, r["kind"][1:]))
    random.Random(398).shuffle(out); return out
def tiles(scratch, f61):
    from PIL import Image, ImageDraw
    its = items(); nat = Image.open(f"{scratch}/nat/f101r.jpg").convert("RGB"); F = Image.open(f61).convert("RGB")
    os.makedirs(f"{scratch}/h398", exist_ok=True); key = ["item\tkind\tcode\tline\tpos\tx\ty0\ty1\tref"]; ims = []
    for n, (kind, code, line, pos, x, y0, y1, ref) in enumerate(its, 1):
        cv, d = B.tile(F if kind == "K" else nat, x, y0, y1)
        mx = 4 + int(110 * 1.6); d.polygon([(mx - 8, 16), (mx + 8, 16), (mx, 32)], fill=(220, 0, 0)); d.text((8, 6), f"R{n:02d}", fill=(0, 0, 0))
        ims.append(cv); key.append(f"R{n:02d}\t{kind}\t{code}\t{line}\t{pos}\t{x}\t{y0}\t{y1}\t{ref}")
    for s in range(0, len(ims), 12):
        sh = Image.new("RGB", (4 * 360, 3 * 262), "white")
        for j, cv in enumerate(ims[s:s + 12]): sh.paste(cv, ((j % 4) * 360, (j // 4) * 262))
        sh.save(f"{scratch}/h398/sheet_{s // 12 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h398_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items,", (len(ims) + 11) // 12, "sheets")
def kappa(pairs):
    n = len(pairs)
    if not n: return 0, float("nan"), float("nan")
    po = sum(a == b for a, b in pairs) / n; pa = sum(a == "yes" for a, _ in pairs) / n; pb = sum(b == "yes" for _, b in pairs) / n
    pe = pa * pb + (1 - pa) * (1 - pb); return n, po, ((po - pe) / (1 - pe) if pe < 1 else float("nan"))
def score():
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h398_reply.tsv")}; it = rd(f"{HERE}/h398_items.tsv")
    g1 = sum((ans.get(r["item"]) == "yes") == (r["group"] == "CP") and ans.get(r["item"]) in ("yes", "no") for r in rd(f"{HERE}/h193_items.tsv") if r["group"] in ("CP", "AN"))
    g2 = sum(ans.get(r["item"]) == r["ref"] for r in it if r["kind"] == "K")
    out = [f"gate 1 (H193 anchors): {g1}/20 (>= 17); gate 2 (known f.61 strips): {g2}/6 (>= 5)"]
    if g1 < 17 or g2 < 5: out.append("CONTROL FAIL -- nothing scored")
    else:
        new = {(r["line"], r["pos"]): ans.get(r["item"], "missing") for r in it if r["kind"] == "T"}; v11 = v11_labels(); run = X.runner_labels()
        out.append(f"targets {len(new)}: new " + " ".join(f"{k} {v}" for k, v in sorted(Counter(new.values()).items())))
        yn = lambda d, k: d.get(k) in ("yes", "no")
        kr = kappa([(new[k], run[k]) for k in new if yn(new, k) and yn(run, k)]); kv = kappa([(new[k], v11[k]) for k in new if yn(new, k) and yn(v11, k)])
        kx = kappa([(run[k], v11[k]) for k in new if yn(run, k) and yn(v11, k)])
        out.append(f"new vs runner: n {kr[0]}, agreement {kr[1]:.2f}, kappa {kr[2]:.2f}; new vs V11: n {kv[0]}, agreement {kv[1]:.2f}, kappa {kv[2]:.2f}; "
                   f"runner vs V11 (same tokens): n {kx[0]}, agreement {kx[1]:.2f}, kappa {kx[2]:.2f}")
        a, b = kr[2] >= 0.6, kv[2] >= 0.6
        ro = "reader variation" if a and b else "the disagreement is V11's design (prompt/anchors)" if a else "the runner's design (tiles)" if b else "unclear"
        out.append(f"read-out: {ro}")
        lm = X.letter_map("f101r"); keys = [k for k in new if k in lm]
        for nm, d in (("new", new), ("runner", run), ("V11", v11)):
            out.append("  letters, " + X.fmt(nm, X.test([(d.get(k, "missing"), X.cls(lm[k][0])) for k in keys], seed=398, perms=10000)))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/h398_bowl_design_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1], a[2]) if a[0] == "tiles" else score()

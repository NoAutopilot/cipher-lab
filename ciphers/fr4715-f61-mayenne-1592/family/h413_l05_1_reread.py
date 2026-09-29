#!/usr/bin/env python3
"""H413 (runner 15 session_01BDhspZ38TdrrXYSvLPTpjc, 29 Sept 2026), written before the call: re-read of H411's one flag. f.61 L05/1 (reader code
LOOPSTEM1, fitted cell q/s; Tomokiyo's S3 dash) was answered LOOPBAR (R12). One fresh blind Opus forced choice with H411's references (R1-R12,
same sheet) and prompt: L05/1 at three windows (W1 -45/+92, W2 -60/+55, W3 -70/+110), L03/2 (LOOPBAR, confirmed in H411) as a positive, and H411's
18 known in-span items; shuffled (seed 413), I01..I22.
score -- GATE >= 16/18 known AND L03/2 -> R12. Pre-stated: L05/1 = R12 at >= 2 of 3 windows -> 'L05/1 is the LOOPBAR sign' (the correction is
written to scripts/f61_positions_corrections.tsv and h408 rerun); else 'the flag does not reproduce' (LOOPSTEM1 kept).
python3 h413_l05_1_reread.py tiles SCRATCH | score [--check]"""
import os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"; sys.path.insert(0, HERE); CHECK = "--check" in sys.argv
import h411_class_qa as q
def tiles(scratch):
    from PIL import Image
    import h407_span_miss as h
    G = q.geo(); im = Image.open(h.REG).convert("RGB"); os.makedirs(f"{scratch}/h413", exist_ok=True)
    its = [("W1", "L05", "1", 45, 92), ("W2", "L05", "1", 60, 55), ("W3", "L05", "1", 70, 110), ("P", "L03", "2", 45, 92)] + [("K", l, p, 45, 92) for c, l, p in q.KNOWN]
    random.Random(413).shuffle(its); cl = [r[0] for r in q.REFS]; key = ["item\tkind\tcode\tline\tpos\tref"]; ims = []
    for n, (kind, l, p, up, dn) in enumerate(its, 1):
        c, x, yc = G[(l, p)]; ims.append(h.strip(im, x, yc, up, dn, f"I{n:02d}"))
        ref = "R12" if kind in ("P", "W1", "W2", "W3") and kind == "P" else ("R" + str(cl.index(c) + 1) if kind == "K" else "")
        key.append(f"I{n:02d}\t{kind}\t{c}\t{l}\t{p}\t{ref}")
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * 370, 5 * 190), "white"); [sh.paste(c, ((k % 4) * 370, (k // 4) * 190)) for k, c in enumerate(ims[s:s + 20])]; sh.save(f"{scratch}/h413/items_{s // 20 + 1:02d}.jpg", quality=90)
    open(f"{HERE}/h413_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items")
def score():
    ans = {r["id"]: r["answer"].strip().upper() for r in q.rd(f"{P}/h413_reply.tsv")}; it = q.rd(f"{HERE}/h413_items.tsv")
    kn = [r for r in it if r["kind"] == "K"]; g = sum(ans.get(r["item"]) == r["ref"] for r in kn); pos = [ans.get(r["item"]) for r in it if r["kind"] == "P"][0]
    out = [f"gate: {g}/18 known (>= 16); positive L03/2 -> {pos} (must be R12)"]
    if g < 16 or pos != "R12": out.append("CONTROL FAIL -- nothing scored")
    else:
        w = [ans.get(r["item"], "missing") for r in sorted((r for r in it if r["kind"].startswith("W")), key=lambda r: r["kind"])]
        out.append(f"L05/1 windows W1-W3: {w} -> " + ("L05/1 is the LOOPBAR sign" if w.count("R12") >= 2 else "the flag does not reproduce"))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/h413_l05_1_reread_result.txt"
    if CHECK:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    a = sys.argv[1:]
    tiles(a[1]) if a[0] == "tiles" else score()

#!/usr/bin/env python3
"""H189 (runner 7, 29 Sept 2026): fol. 179 split signs re-adjudicated with context strips and a red marker (H186's 90-px tiles failed their
anchors, 11/20). Written before the call. Each item is a 300-px-wide strip of its crop (the whole crop height) with a red triangle under the
target sign's reader x_px, scale 1.2, numbered M001...; 210 fol. 179 splits (h186_tiles.tsv non-anchor rows, same option order) + 20 anchors from
f.176v L01-L08 (signs both f.176v passes coded the same at x within 30 px, seed 189; decoy = the same confusion family as h186_adj.FAM),
shuffled, 4 x 5 per sheet in <scratch>/h189/. Key: h189_items.tsv. The adjudication reply goes to passes/h189_adjudication.tsv; `merge`
checks anchors >= 17/20 and writes passes/f179_signsC_L01-L08.tsv via h186_adj's merge logic (tiles re-keyed).
  python3 h189_mark.py items SCRATCH | merge [--check]"""
import os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h170_gate as g, h186_adj as H
P = H.P
def f176v_agreed():
    def rows(t):
        R = defaultdict(list)
        for r in g.rd(f"{P}/f176v_signs{t}_L01-L08.tsv"):
            if r["sign"] != "PLAIN": R[r["line"]].append((r["segment"], int(r["x_px"]), {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"], r["sign"])))
        return R
    A, B = rows("A"), rows("B"); out = []
    for l in sorted(A):
        used = set()
        for sg, x, s in A[l]:
            c = [(abs(x - x2), i) for i, (sg2, x2, s2) in enumerate(B[l]) if sg2 == sg and i not in used and abs(x - x2) <= 30]
            if c:
                i = min(c)[1]; used.add(i)
                if B[l][i][2] == s and s in H.FAM: out.append((l, sg, x, s))
    return out
def items(scratch):
    from PIL import Image, ImageDraw
    rng = random.Random(189); split = [r for r in g.rd(f"{HERE}/h186_tiles.tsv") if r["anchor"] == "0"]
    pos = {(l, str(p)): (sg, x) for l, p, sg, x, a, b in H.pairs()}; anc = rng.sample(f176v_agreed(), 20)
    its = [("179", r["line"], *pos[(r["line"], r["pos"])], r["option1"], r["option2"], r["tile"]) for r in split]
    for l, sg, x, s in anc:
        o1, o2 = s, H.FAM[s]
        if rng.random() < 0.5: o1, o2 = o2, o1
        its.append(("176v", l, sg, x, o1, o2, f"anchor:{s}"))
    rng.shuffle(its); os.makedirs(f"{scratch}/h189", exist_ok=True); key = ["item\tleaf\tline\tsegment\tx_px\toption1\toption2\tsource"]; ims = []
    for n, (leaf, l, sg, x, o1, o2, src) in enumerate(its, 1):
        f = f"{scratch}/f179/f179_{l}_{sg}.jpg" if leaf == "179" else f"{scratch}/f176v/f176v_{l}_{sg}.jpg"
        im = Image.open(f).convert("RGB"); x0 = max(0, min(im.width - 300, x - 150)); t = im.crop((x0, 0, x0 + 300, im.height)).resize((360, int(im.height * 1.2)))
        c = Image.new("RGB", (370, t.height + 40), "white"); c.paste(t, (5, 0)); d = ImageDraw.Draw(c); mx = 5 + int((x - x0) * 1.2)
        d.polygon([(mx - 9, t.height + 16), (mx + 9, t.height + 16), (mx, t.height + 2)], fill=(220, 0, 0)); d.text((6, t.height + 22), f"M{n:03d}", fill=(0, 0, 0))
        ims.append(c); key.append(f"M{n:03d}\t{leaf}\t{l}\t{sg}\t{x}\t{o1}\t{o2}\t{src}")
    W, Hh = ims[0].width, max(i.height for i in ims)
    for s in range(0, len(ims), 20):
        sh = Image.new("RGB", (4 * W, 5 * Hh), "white")
        for k, c in enumerate(ims[s:s + 20]): sh.paste(c, ((k % 4) * W, (k // 4) * Hh))
        sh.save(f"{scratch}/h189/sheet_{s // 20 + 1:02d}.jpg", quality=88)
    open(f"{HERE}/h189_items.tsv", "w").write("\n".join(key) + "\n"); print(len(its), "items,", (len(ims) + 19) // 20, "sheets")
def merge():
    key = {r["item"]: r for r in g.rd(f"{HERE}/h189_items.tsv")}; adj = {r["item"]: r["choice"].strip() for r in g.rd(f"{P}/h189_adjudication.tsv")}
    anc = [m for m, r in key.items() if r["source"].startswith("anchor:")]
    hit = sum(adj.get(m) in ("A", "B") and key[m][{"A": "option1", "B": "option2"}[adj[m]]] == key[m]["source"].split(":")[1] for m in anc)
    line = f"anchors (f.176v agreed signs): {hit} of {len(anc)} pick the agreed code (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"
    if hit < 17:
        print(line)
        if "--check" not in sys.argv: open(f"{HERE}/h189_merge_result.txt", "w").write(line + "\n")
        sys.exit(3)
    t186 = {r["tile"]: r for r in g.rd(f"{HERE}/h186_tiles.tsv")}; pick = {}
    for m, r in key.items():
        if r["source"].startswith("anchor:"): continue
        c = adj.get(m, "N"); t = t186[r["source"]]; pick[(t["line"], t["pos"])] = r["option1"] if c == "A" else r["option2"] if c == "B" else "?"
    out = ["# f179_signsC_L01-L08.tsv -- H189 merged sequence (agreed pairs, adjudicated splits, '?' for N/unpaired), h189_mark.py merge", "line\tpos\tsign\tconf\tsegment\tx_px\tnote"]; nq = 0
    for l, pos, sg, x, a, b in H.pairs():
        s_ = a if b == a else pick.get((l, str(pos)), "?") if b else "?"; nq += s_ == "?"; out.append(f"{l}\t{pos}\t{s_}\tm\t{sg}\t{x}\t")
    files = {f"{P}/f179_signsC_L01-L08.tsv": "\n".join(out) + "\n", f"{HERE}/h189_merge_result.txt": line + f"\nmerged {len(out) - 2} signs, {nq} '?'\n"}
    if "--check" in sys.argv:
        bad = [p for p, s in files.items() if not os.path.exists(p) or open(p).read() != s]; print("stale: " + ", ".join(bad) if bad else "OK"); sys.exit(1 if bad else 0)
    for p, s in files.items(): open(p, "w").write(s)
    print(files[f"{HERE}/h189_merge_result.txt"], end="")
if __name__ == "__main__":
    items(sys.argv[2]) if sys.argv[1] == "items" else merge()

#!/usr/bin/env python3
"""H186 (runner 7, 29 Sept 2026): adjudicate fol. 179 L01-L08's split signs (a different instrument, rule 3, after H185 failed on a 0.52 pass
consensus). Written before the adjudication call.
  tiles   : pair pass A and pass B signs by (line, segment, x_px within 30 px); every paired sign whose codes differ becomes a tile (the crop
            region x +- 45 px, full crop height, scale 1.5), plus 20 paired AGREED signs as blind anchors (seed 186), shuffled together,
            numbered T001..., laid out 6 x 6 per sheet in <scratch>/h186/sheet_NN.jpg; the key (tile -> line, pos, codes, anchor?) goes to
            h186_tiles.tsv. The reader sees only the tile number and the two candidate codes (anchors show their agreed code and a
            decoy code from the same confusion family), never a letter.
  merge   : read passes/h186_adjudication.tsv (tile, choice = A|B|N), check the anchor gate (>= 17 of 20 anchors pick the agreed code,
            else stop: CONTROL FAIL, no merged file), and write passes/f179_signsC_L01-L08.tsv: agreed codes, adjudicated codes, '?' for N
            and for unpaired signs, in pass A's order.
  python3 h186_adj.py tiles SCRATCH | merge [--check]"""
import os, random, sys
from collections import defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
import h170_gate as g
P = f"{HERE}/passes"; FAM = {"4TRI": "C43", "C43": "4TRI", "HASH4": "ZHOOK", "ZHOOK": "HASH4", "4PI": "4TRI", "PHI": "DBL", "DBL": "PHI",
                              "SBS": "PHI", "VBAR_A": "VBAR_B", "VBAR_B": "VBAR_A", "INF": "SBS", "EBR": "VBAR_A", "4STEM": "4PI", "CH": "LL"}
def rows(t):
    R = defaultdict(list)
    for r in g.rd(f"{P}/f179_signs{t}_L01-L08.tsv"):
        if r["sign"] == "PLAIN": continue
        R[r["line"]].append((int(r["pos"]), r["segment"], int(r["x_px"]), {"EBR_A": "EBR", "EBR_B": "EBR"}.get(r["sign"], r["sign"])))
    return R
def pairs():
    A, B = rows("A"), rows("B"); out = []
    for l in sorted(A):
        used = set()
        for pos, sg, x, s in A[l]:
            c = [(abs(x - x2), i) for i, (_, sg2, x2, _) in enumerate(B[l]) if sg2 == sg and i not in used and abs(x - x2) <= 30]
            if not c: out.append((l, pos, sg, x, s, None)); continue
            i = min(c)[1]; used.add(i); out.append((l, pos, sg, x, s, B[l][i][3]))
    return out
def tiles(scratch):
    from PIL import Image, ImageDraw
    pr = pairs(); split = [p for p in pr if p[5] and p[4] != p[5]]; agreed = [p for p in pr if p[5] and p[4] == p[5]]
    rng = random.Random(186); anchors = rng.sample(agreed, 20); items = [(p, 0) for p in split] + [(p, 1) for p in anchors]; rng.shuffle(items)
    os.makedirs(f"{scratch}/h186", exist_ok=True); key = ["tile\tline\tpos\tA\tB\tanchor\toption1\toption2"]; ims = []
    for n, (p, anc) in enumerate(items, 1):
        l, pos, sg, x, a, b = p
        o1, o2 = (a, FAM.get(a, "OTHER")) if anc else (a, b)
        if rng.random() < 0.5: o1, o2 = o2, o1
        key.append(f"T{n:03d}\t{l}\t{pos}\t{a}\t{b}\t{anc}\t{o1}\t{o2}")
        im = Image.open(f"{scratch}/f179/f179_{l}_{sg}.jpg").convert("L"); t = im.crop((max(0, x - 45), 0, min(im.width, x + 45), im.height))
        t = t.resize((int(t.width * 1.5), int(t.height * 1.5))); c = Image.new("L", (150, 205), 255); c.paste(t, (8, 0))
        d = ImageDraw.Draw(c); d.text((4, 178), f"T{n:03d}", fill=0); d.line((75, 0, 75, 6), fill=0); ims.append(c)
    for s in range(0, len(ims), 36):
        sh = Image.new("L", (6 * 150, 6 * 205), 255)
        for k, c in enumerate(ims[s:s + 36]): sh.paste(c, ((k % 6) * 150, (k // 6) * 205))
        sh.save(f"{scratch}/h186/sheet_{s // 36 + 1:02d}.jpg")
    open(f"{HERE}/h186_tiles.tsv", "w").write("\n".join(key) + "\n"); print(len(split), "split +", 20, "anchors =", len(items), "tiles,", (len(ims) + 35) // 36, "sheets")
def merge():
    key = {r["tile"]: r for r in g.rd(f"{HERE}/h186_tiles.tsv")}; adj = {r["tile"]: r["choice"].strip() for r in g.rd(f"{P}/h186_adjudication.tsv")}
    anc = [t for t, r in key.items() if r["anchor"] == "1"]; hit = sum(adj.get(t) in ("A", "B") and key[t][{"A": "option1", "B": "option2"}[adj[t]]] == key[t]["A"] for t in anc)
    out = [f"anchors: {hit} of {len(anc)} pick the agreed code (gate >= 17): {'PASS' if hit >= 17 else 'CONTROL FAIL'}"]
    if hit < 17: print(out[0]); sys.exit(3)
    pick = {}
    for t, r in key.items():
        if r["anchor"] == "1": continue
        c = adj.get(t, "N"); pick[(r["line"], r["pos"])] = r["option1"] if c == "A" else r["option2"] if c == "B" else "?"
    rows_ = ["# f179_signsC_L01-L08.tsv -- H186 merged sequence (agreed pairs, adjudicated splits, '?' for neither/unpaired), h186_adj.py merge", "line\tpos\tsign\tconf\tsegment\tx_px\tnote"]
    n = defaultdict(int)
    for l, pos, sg, x, a, b in pairs():
        s = a if b == a else pick.get((l, str(pos)), "?") if b else "?"; n[s == "?"] += 1
        rows_.append(f"{l}\t{pos}\t{s}\tm\t{sg}\t{x}\t")
    out.append(f"merged {sum(n.values())} signs, {n[False]} coded, {n[True]} '?' ({n[False] / sum(n.values()):.2f} coded)")
    files = {f"{P}/f179_signsC_L01-L08.tsv": "\n".join(rows_) + "\n", f"{HERE}/h186_merge_result.txt": "\n".join(out) + "\n"}
    if "--check" in sys.argv:
        bad = [p for p, s in files.items() if not os.path.exists(p) or open(p).read() != s]; print("stale: " + ", ".join(bad) if bad else "OK"); sys.exit(1 if bad else 0)
    for p, s in files.items(): open(p, "w").write(s)
    print("\n".join(out))
if __name__ == "__main__":
    tiles(sys.argv[2]) if sys.argv[1] == "tiles" else merge()

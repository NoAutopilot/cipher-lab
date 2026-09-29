#!/usr/bin/env python3
"""VERIFY-F61-V11 part C (29 Sept 2026, PREREG.md C): does the runner's bowl split of 4TRI raise the v7 order gain more than ANY split of the same
size? Gain = tools/partial_key_test.py's order_gain_test inner gain (real runs minus mean of 10 within-run shuffles, beam 400, fr), cells
family/key_v7_cells_h354.tsv. Per leaf (f101r, f124r): as transcribed, the runner's split draft (rec<leaf>_split), and 30 random splits relabelling the
same number of 4TRI tokens to C43 (seeds 1100-1129): frame 1 (pre-registered) = all 4TRI tokens of the draft; frame 2 (supplementary) = only the
agreed 4TRI tokens the readers answered (the frame the real split was drawn from). Within-run shuffle seeds 342/343/344 for the real split; 342 for
random splits.   python3 v11_gain.py [--check]"""
import csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); FAM = f"{HERE}/../family"; P = f"{FAM}/passes"
sys.path.insert(0, f"{ROOT}/tools"); import partial_key_test as pk
def gain(draft, cells, lp, seed):
    runs = pk.order_runs(draft, cells, 4); rng = random.Random(seed); shuf = []
    for _ in range(10):
        s = []
        for r in runs: r2 = r[:]; rng.shuffle(r2); s.append(r2)
        shuf.append(s)
    cf = lambda c: cells.get(c, ())
    return pk.order_score(runs, cf, lp, 400) - sum(pk.order_score(s, cf, lp, 400) for s in shuf) / len(shuf)
def main():
    cells = pk._cells_load(f"{FAM}/key_v7_cells_h354.tsv"); lp = pk.make_lp("fr"); out = []
    for leaf in ("f101r", "f124r"):
        d0 = pk._draft_load(f"{P}/rec{leaf}/ciphertext_draft.tsv"); d1 = pk._draft_load(f"{P}/rec{leaf}_split/ciphertext_draft.tsv")
        rel = [i for i, ((_, a), (_, b)) in enumerate(zip(d0, d1)) if a != b]; k = len(rel)
        assert all(d0[i][1] == "4TRI" and d1[i][1] == "C43" for i in rel)
        idx4 = [i for i, (_, s) in enumerate(d0) if s == "4TRI"]
        rows = [r for r in csv.DictReader(open(f"{P}/rec{leaf}/ciphertext_draft.tsv"), delimiter="\t")]
        agreed = [i for i in idx4 if rows[i]["why"].startswith("agree")]
        g0 = [gain(d0, cells, lp, s) for s in (342, 343, 344)]; g1 = [gain(d1, cells, lp, s) for s in (342, 343, 344)]
        res = {}
        for fr, frame in (("frame1 all 4TRI", idx4), ("frame2 agreed 4TRI", agreed)):
            gs = []
            for sd in range(1100, 1130):
                pick = set(random.Random(sd).sample(frame, min(k, len(frame))))
                gs.append(gain([(l, "C43" if i in pick else s) for i, (l, s) in enumerate(d0)], cells, lp, 342))
            gs.sort(); res[fr] = gs
        f = lambda v: "/".join(f"{x:.4f}" for x in v)
        out.append(f"{leaf}: 4TRI tokens {len(idx4)} (agreed {len(agreed)}); split relabels {k}; gain as transcribed {f(g0)}; bowl split {f(g1)}")
        for fr, gs in res.items():
            p95 = gs[int(round(0.95 * 30)) - 1]; med = (gs[14] + gs[15]) / 2; ge = sum(x >= g1[0] for x in gs)
            ro = "the bowl split beats random splits" if g1[0] > p95 else "any split does this" if g1[0] <= med else "unclear"
            out.append(f"  {fr}: 30 random splits of {k}: min {gs[0]:.4f} median {med:.4f} p95 {p95:.4f} max {gs[-1]:.4f}; >= bowl split (seed 342) {ge}/30 -> {ro}")
    txt = "\n".join(out) + "\n"; res_ = f"{HERE}/v11_gain_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res_) and open(res_).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res_, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()

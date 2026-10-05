#!/usr/bin/env python3
"""N9-GRA4 scorer (PREREG-N9-GRA4.md, addendum to PREREG-N8-GRA2/N8-GRA3; same instrument): fr.3040 no.6 f.18r L11-L21
(rows f18rB_L01..L11) aligned to N8-GRA2's print span S1 with N8-GRA2's registered functions, unchanged. N1 shuffled print,
N2 shuffled key, 200 reps p99; planted control at 13% on S1 at the target's keyed N, 20 seeds (nulls on 3).
Open codes pooled over this job + N8-GRA2 f.18r L01-L10 + N8-GRA3 f.18v/f.19r (each block vs its own print segment),
per-code shuffled-print null as score3.py. Listing: every HASH, A2, Mx, zb occurrence (zb decoded as a wildcard for the
listing only) with its row and aligned print letter. Secondary (non-gating): agree with every 'z' token as a wildcard.

  python3 n9gra4/score4.py --control      # run first
  python3 n9gra4/score4.py --target       # target, nulls, conflicts, open codes, listing
"""
import argparse, json, random, sys, collections
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "n8gra2")); sys.path.insert(0, str(HERE.parent / "n8gra3"))
import score as S     # N8-GRA2 registered functions
import score3 as S3   # N8-GRA3 blocks, segments, OPEN set
LIST = ("HASH", "A2", "Mx", "zb")


def rowtoks(path, keep=lambda r: True):
    out = []
    for ln in Path(path).read_text().splitlines()[1:]:
        f = ln.split("\t")
        if len(f) == 2 and keep(f[0]):
            out += [(f[0], t) for t in f[1].split()]
    return out


def blocks_all():
    """block name -> (segment string, [(row, token)])"""
    b = collections.OrderedDict()
    b["N9"] = (S3.SEGS["S1"], rowtoks(HERE / "recon.tsv"))
    b["G2"] = (S3.SEGS["S1"], rowtoks(HERE.parent / "n8gra2" / "recon.tsv", lambda r: r in S.ROWS))
    for r, t in rowtoks(HERE.parent / "n8gra3" / "recon.tsv"):
        s = S3.BLOCK[r.split("_")[0]]
        b.setdefault("G3" + s, (S3.SEGS[s], []))[1].append((r, t))
    return b


def occ_rows(rt, key, seg, want):
    kept = [(r, d) for r, t in rt for d in S.decode([t], key)]
    _, _, al = S.align_agree([d for _, d in kept], seg)
    return [(r, t, v, x) for (r, (t, v)), x in zip(kept, al) if want(t, v)]


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--control", action="store_true"); ap.add_argument("--target", action="store_true")
    ap.add_argument("--reps", type=int, default=200); ap.add_argument("--seeds", type=int, default=20)
    a = ap.parse_args()
    key = S.load_key(); pr = S3.SEGS["S1"]
    toks = [t for _, t in rowtoks(HERE / "recon.tsv")]
    dec = S.decode(toks, key); nk = sum(1 for _, v in dec if v)
    res = {"tokens": len(dec), "keyed": nk}
    if a.control:
        sc, p1s, p2s = [], [], []
        for sd in range(a.seeds):
            rng = random.Random(sd)
            t = S.plant(key, pr, nk, rng)
            sc.append(S.align_agree(S.decode(t, key), pr)[0])
            if sd < 3:
                p1, p2 = S.nulls(t, key, pr, rng, a.reps); p1s.append(p1); p2s.append(p2)
        g = max(max(p1s), max(p2s)) + 0.15
        res["control"] = dict(err=S.ERR, n=nk, mean=float(np.mean(sc)), min=float(min(sc)), N1_p99=max(p1s), N2_p99=max(p2s),
                              gate=g, pass_=bool(np.mean(sc) >= g))
    if a.target:
        ag, kn, al = S.align_agree(dec, pr)
        p1, p2 = S.nulls(toks, key, pr, random.Random(99), a.reps)
        res["target"] = dict(keyed=kn, agree=ag, N1_p99=p1, N2_p99=p2, pass_=bool(ag >= 0.5 and ag > max(p1, p2)))
        kz = dict(key); kz["z"] = "?"
        agz, knz, _ = S.align_agree(S.decode(toks, kz), pr)
        res["secondary_z_wildcard"] = dict(keyed=knz, agree=agz)
        per = collections.defaultdict(list)
        for (t, v), x in zip(dec, al):
            if v: per[t].append(f"{v}->{x}")
        res["keyed_conflicts"] = {t: L for t, L in sorted(per.items())
                                  if sum(1 for e in L if e.split("->")[0] != e.split("->")[1]) >= 2}
        # open codes (registered rule): pooled blocks, per-code shuffled-print null
        bl = blocks_all()
        isopen = lambda t, v: t in S3.OPEN or (v is None and t != "?")
        occ = collections.defaultdict(list)
        for name, (seg, rt) in bl.items():
            for r, t, v, x in occ_rows(rt, key, seg, isopen):
                occ[t].append((name, r, x))
        rng = random.Random(7); same = collections.Counter()
        for _ in range(a.reps):
            o = collections.defaultdict(list)
            for name, (seg, rt) in bl.items():
                l = list(seg); rng.shuffle(l)
                for r, t, v, x in occ_rows(rt, key, "".join(l), isopen):
                    o[t].append(x)
            for t, L in o.items():
                if len(L) >= 2 and len(set(L)) == 1 and "-" not in L[0]: same[t] += 1
        res["open_codes"] = {}
        for t, L in sorted(occ.items()):
            xs = [x for _, _, x in L]
            res["open_codes"][t] = dict(n=len(L), aligned=xs, this_job=sum(1 for b, _, _ in L if b == "N9"),
                                        all_same=bool(len(xs) >= 2 and len(set(xs)) == 1 and "-" not in xs[0]),
                                        null_all_same_rate=same[t] / a.reps)
        # listing (not gating): HASH, A2, Mx, zb with zb as wildcard
        kl = dict(key); kl["zb"] = "?"
        res["listing"] = {c: [] for c in LIST}
        for name, (seg, rt) in bl.items():
            for r, t, v, x in occ_rows(rt, kl, seg, lambda t, v: t in LIST):
                res["listing"][t].append(f"{name} {r} -> {x}")
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

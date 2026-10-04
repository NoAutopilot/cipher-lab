#!/usr/bin/env python3
"""N8-GRA3 scorer (PREREG-N8-GRA2.md + PREREG-N8-GRA3.md): three cipher blocks of fr.3040 no.6 (f.18v L01-L03 -> S1,
f.18v L04-L07 -> S2, f.18v L09-L24 + f.19r L01-L02 -> S3; this script's block labels f18vA, f18vB, f18vC+f19r), each
aligned to its own Le Grand III print segment with N8-GRA2's aligner, `agree` pooled. N1 shuffles each segment, N2
permutes key values once per rep; planted control at 13% error on S1[-120:]+S2+S3 at the target's per-block keyed N.
Open-code rule: per-code alignment over this job's blocks plus N8-GRA2's f.18r L01-L10 (n8gra2/recon.tsv vs its span),
with a per-code shuffled-print null (share of 200 shuffles where all occurrences land on one letter).

  python3 score3.py --control     # run first
  python3 score3.py --target      # target, nulls, per-code table
"""
import argparse, json, random, sys, collections
from pathlib import Path
import numpy as np
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "n8gra2"))
import score as S  # N8-GRA2's registered functions (norm, decode, align_agree, plant)

OPEN = {"HASH", "A2", "INF", "TRI", "ST", "BOX", "B8", "ev", "QQ", "v", "lz", "Mx", "Hb", "III"}


def seg(name):
    return S.norm(" ".join(l for l in (HERE / name).read_text().splitlines() if not l.startswith("#")))


SEGS = {"S1": S.load_print(), "S2": seg("print_S2.txt"), "S3": seg("print_S3.txt")}
BLOCK = {"f18vA": "S1", "f18vB": "S2", "f18vC": "S3", "f19r": "S3"}


def blocks(recon):
    out = collections.OrderedDict()
    for ln in Path(recon).read_text().splitlines()[1:]:
        r, c = ln.split("\t")
        s = BLOCK[r.split("_")[0]]
        out.setdefault(s, []).extend(c.split())
    return out


def pooled(bl, key, segs):
    ag = kn = 0
    for s, toks in bl.items():
        a, k, _ = S.align_agree(S.decode(toks, key), segs[s])
        ag += a * k; kn += k
    return ag / kn if kn else 0.0, kn


def shuf(segs, rng):
    o = {}
    for s, p in segs.items():
        l = list(p); rng.shuffle(l); o[s] = "".join(l)
    return o


def permkey(key, rng):
    codes = [c for c, v in key.items() if S.keyed(v)]
    vals = [key[c] for c in codes]; rng.shuffle(vals)
    k2 = dict(key); k2.update(zip(codes, vals)); return k2


def nulls(bl, key, segs, rng, reps):
    n1 = [pooled(bl, key, shuf(segs, rng))[0] for _ in range(reps)]
    n2 = [pooled(bl, permkey(key, rng), segs)[0] for _ in range(reps)]
    return float(np.percentile(n1, 99)), float(np.percentile(n2, 99))


def open_occ(bl, key, segs):
    occ = collections.defaultdict(list)
    for s, toks in bl.items():
        dec = S.decode(toks, key)
        _, _, al = S.align_agree(dec, segs[s])
        for (t, v), x in zip(dec, al):
            if t in OPEN or (v is None and t != "?"):
                occ[t].append(x)
    return occ


def main():
    ap = argparse.ArgumentParser(); ap.add_argument("--control", action="store_true"); ap.add_argument("--target", action="store_true")
    ap.add_argument("--reps", type=int, default=200); ap.add_argument("--seeds", type=int, default=20)
    a = ap.parse_args()
    key = S.load_key(); bl = blocks(HERE / "recon.tsv")
    nk = {s: sum(1 for t, v in S.decode(toks, key) if v) for s, toks in bl.items()}
    res = {"keyed_per_block": nk}
    if a.control:
        csegs = dict(SEGS); csegs["S1"] = SEGS["S1"][-120:]
        sc, p1s, p2s = [], [], []
        for sd in range(a.seeds):
            rng = random.Random(sd)
            cb = {s: S.plant(key, csegs[s], nk[s], rng) for s in bl}
            sc.append(pooled(cb, key, csegs)[0])
            if sd < 3:
                p1, p2 = nulls(cb, key, csegs, rng, a.reps); p1s.append(p1); p2s.append(p2)
        g = max(max(p1s), max(p2s)) + 0.15
        res["control"] = dict(err=S.ERR, mean=float(np.mean(sc)), min=float(min(sc)), N1_p99=max(p1s), N2_p99=max(p2s), gate=g,
                              pass_=bool(np.mean(sc) >= g))
    if a.target:
        ag, kn = pooled(bl, key, SEGS)
        p1, p2 = nulls(bl, key, SEGS, random.Random(99), a.reps)
        res["target"] = dict(keyed=kn, agree=ag, N1_p99=p1, N2_p99=p2, pass_=bool(ag >= 0.5 and ag > max(p1, p2)))
        per = collections.defaultdict(list)
        for s, toks in bl.items():
            dec = S.decode(toks, key); _, _, al = S.align_agree(dec, SEGS[s])
            for (t, v), x in zip(dec, al):
                if v: per[t].append(f"{v}->{x}")
        res["keyed_conflicts"] = {t: L for t, L in sorted(per.items())
                                  if sum(1 for e in L if e.split("->")[0] != e.split("->")[1]) >= 2}
        # open codes: this job + N8-GRA2 f.18r L01-L10
        g2 = [t for ln in (HERE.parent / "n8gra2" / "recon.tsv").read_text().splitlines()[1:]
              for r, c in [ln.split("\t")] if r in S.ROWS for t in c.split()]
        allbl = dict(bl); allbl["G2"] = g2
        segs2 = dict(SEGS); segs2["G2"] = SEGS["S1"]
        occ = open_occ(allbl, key, segs2)
        rng = random.Random(7); same = collections.Counter()
        for _ in range(a.reps):
            o = open_occ(allbl, key, shuf(segs2, rng))
            for t, L in o.items():
                if len(L) >= 2 and len(set(L)) == 1 and "-" not in L[0]: same[t] += 1
        res["open_codes"] = {t: dict(n=len(L), aligned=L, all_same=bool(len(L) >= 2 and len(set(L)) == 1 and "-" not in L[0]),
                                     null_all_same_rate=same[t] / a.reps) for t, L in sorted(occ.items())}
    print(json.dumps(res, indent=1, ensure_ascii=False))


if __name__ == "__main__":
    main()

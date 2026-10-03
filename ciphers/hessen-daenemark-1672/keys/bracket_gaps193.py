#!/usr/bin/env python3
"""GAPS193 bracketing test for hessen-daenemark-1672 (pre-registered in PREREG-GAPS193.md).

S1: Kendall tau between nomenclator code and the gloss headword's alphabetical rank (one-part order).
S2: same-topic adjacent pairs among the sorted gloss-pinned codes (topical blocks).
Each with a matched synthetic control at the letter's own K=16 (structured design = power, two-part random = size),
gloss noise 0/0.2/0.4. Writes keys/bracket_gaps193.tsv; --check exits 1 if the committed TSV is stale.

Usage: python3 keys/bracket_gaps193.py [--check]
"""
import sys, os
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, "bracket_gaps193.tsv")
SEED = 193

# Pre-registered (PREREG-GAPS193.md): code -> (headword, topic)
UNITS = {
    229: ("berlin", "BRAND"), 303: ("alliance", "OTHER"), 437: ("hertzog", "HOLST"), 447: ("kayser", "EMP"),
    601: ("dennemarck", "DK"), 602: ("konig", "DK"), 605: ("k", "DK"), 641: ("von", "HOLST"),
    651: ("cur", "BRAND"), 653: ("cur", "BRAND"), 681: ("cur", "BRAND"), 768: ("sueco", "SWE"),
    774: ("holland", "NL"), 775: ("gen", "NL"), 834: ("rex", "DK"), 5756: ("franckreich", "FRA"),
}
NSHUF_TARGET = 10000
NSHUF_CTRL = 1000
NLET = 1000
NOISES = (0.0, 0.2, 0.4)


def kendall_tau(x, y):
    x = np.asarray(x, float); y = np.asarray(y, float)
    dx = np.sign(x[:, None] - x[None, :]); dy = np.sign(y[:, None] - y[None, :])
    iu = np.triu_indices(len(x), 1)
    s = (dx * dy)[iu].sum()
    n1 = (dx[iu] != 0).sum(); n2 = (dy[iu] != 0).sum()
    return s / np.sqrt(n1 * n2) if n1 and n2 else 0.0


def adj_same(labels_sorted):
    l = np.asarray(labels_sorted)
    return int((l[1:] == l[:-1]).sum())


def perm_p_s1(codes, ranks, rng, nshuf):
    t0 = kendall_tau(codes, ranks)
    ge = sum(kendall_tau(codes, rng.permutation(ranks)) >= t0 - 1e-12 for _ in range(nshuf))
    return t0, (ge + 1) / (nshuf + 1)


def perm_p_s2(labels_by_code_order, rng, nshuf):
    a0 = adj_same(labels_by_code_order)
    lab = np.asarray(labels_by_code_order)
    ge = sum(adj_same(rng.permutation(lab)) >= a0 for _ in range(nshuf))
    return a0, (ge + 1) / (nshuf + 1)


def noisy(labels, rate, rng):
    labels = list(labels)
    pool = sorted(set(labels))
    for i in range(len(labels)):
        if rate and rng.random() < rate:
            labels[i] = rng.choice([p for p in pool if p != labels[i]] or pool)
    return labels


def synth_codes(rng, k):
    return np.sort(rng.choice(np.arange(200, 850), size=k, replace=False))


def control(stat, structured, rate, rng):
    heads = [h for h, _ in UNITS.values()]
    topics = [t for _, t in UNITS.values()]
    k = len(UNITS); hits = 0
    for _ in range(NLET):
        codes = synth_codes(rng, k)
        if stat == "S1":
            alpha = sorted(set(heads)); rank_of = {h: i for i, h in enumerate(alpha)}
            hs = list(rng.permutation(heads))
            if structured:
                hs = sorted(hs, key=lambda h: (rank_of[h], rng.random()))
            hs = noisy(hs, rate, rng)
            _, p = perm_p_s1(codes, [rank_of[h] for h in hs], rng, NSHUF_CTRL)
        else:
            if structured:
                order = list(rng.permutation(sorted(set(topics))))
                ts = [t for t in order for _ in range(topics.count(t))]
            else:
                ts = list(rng.permutation(topics))
            ts = noisy(ts, rate, rng)
            _, p = perm_p_s2(ts, rng, NSHUF_CTRL)
        hits += p < 0.05
    return hits / NLET


def run():
    rng = np.random.default_rng(SEED)
    rows = []
    codes = sorted(UNITS)
    heads = [UNITS[c][0] for c in codes]
    alpha = sorted(set(heads)); rank_of = {h: i for i, h in enumerate(alpha)}
    t, p1 = perm_p_s1(codes, [rank_of[h] for h in heads], rng, NSHUF_TARGET)
    rows.append(("target", "S1", "-", "-", f"{t:.3f}", f"{p1:.4f}"))
    topics = [UNITS[c][1] for c in codes]
    a, p2 = perm_p_s2(topics, rng, NSHUF_TARGET)
    rows.append(("target", "S2", "-", "-", str(a), f"{p2:.4f}"))
    merged = ["DKH" if x in ("DK", "HOLST") else x for x in topics]
    a2, p2m = perm_p_s2(merged, rng, NSHUF_TARGET)
    rows.append(("target", "S2_merged_DK_HOLST(sensitivity)", "-", "-", str(a2), f"{p2m:.4f}"))
    for stat in ("S1", "S2"):
        for structured in (True, False):
            for rate in NOISES:
                share = control(stat, structured, rate, rng)
                rows.append(("control", stat, "structured" if structured else "two-part", f"{rate:.1f}",
                             "share_p<0.05", f"{share:.3f}"))
    lines = ["kind\tstat\tdesign\tnoise\tvalue\tp_or_share"] + ["\t".join(r) for r in rows]
    return "\n".join(lines) + "\n"


if __name__ == "__main__":
    out = run()
    if "--check" in sys.argv:
        ok = os.path.exists(OUT) and open(OUT).read() == out
        print("bracket_gaps193.tsv up to date" if ok else "bracket_gaps193.tsv STALE"); sys.exit(0 if ok else 1)
    open(OUT, "w").write(out); print(out)

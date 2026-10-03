#!/usr/bin/env python3
"""Fixed-key scoring of the fr.4712 f.7r glossed runs (witness/key71/PREREG5_fixedkey.md, GAPS88, 3 Oct 2026).

  python3 scripts/f7r_fixedkey.py [--draws 10000] [--seeds 20]

Decodes each run's unmarked tokens with Tomokiyo's letter table (nothing learned; codes outside the table -> '?',
marked tokens dropped), scores LCS against the run's own gloss, and compares the pooled score with the same runs under
the table's values permuted over its codes. Positive control: the glosses enciphered as g1_power_check.py's K2.
Writes witness/f7r_fixedkey.tsv (per run) and witness/f7r_fixedkey_poscontrol.tsv; exit 0 PASS, 2 FAIL, 4 NON-TEST.
"""
import argparse, csv, random, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from f4712_7r_gates import HERE, p99, tomokiyo  # noqa: E402
from g1_power_check import encipher, norm  # noqa: E402

PAIRS = HERE / "witness/f4712_7r_pairs_img.tsv"


def lcs(a, masks, n):
    """Bit-parallel LCS length (Allison-Dix/Hyyro) of sequence a against the gloss whose per-letter bitmasks are masks."""
    full = (1 << n) - 1
    v = full
    for c in a:
        u = v & masks.get(c, 0)
        v = ((v + u) | (v - u)) & full
    return n - bin(v).count("1")


def prep(gloss):
    masks = {}
    for i, c in enumerate(gloss):
        masks[c] = masks.get(c, 0) | (1 << i)
    return masks


def score(runs, key, draws, seed):
    """runs: list of (codes, gloss). Returns per-run rows, T, R, ctl T list, ctl mean R, per-run p."""
    items = []
    for codes, g in runs:
        dec_len = len(codes)
        m = min(dec_len, len(g))
        if m >= 4:
            items.append((codes, g, prep(g), len(g), m))
    sumM = sum(x[4] for x in items)
    real = [lcs([key.get(c, "?") for c in codes], mk, n) for codes, g, mk, n, m in items]
    T = sum(real)
    keys, vals = list(key), list(key.values())
    rng = random.Random(seed)
    ctlT, ge = [], [0] * len(items)
    for _ in range(draws):
        rng.shuffle(vals)
        perm = dict(zip(keys, vals))
        tot = 0
        for j, (codes, g, mk, n, m) in enumerate(items):
            l = lcs([perm.get(c, "?") for c in codes], mk, n)
            tot += l
            if l >= real[j]:
                ge[j] += 1
        ctlT.append(tot)
    R = T / sumM if sumM else 0.0
    mR = sum(ctlT) / len(ctlT) / sumM if sumM else 0.0
    pr = [(1 + x) / (draws + 1) for x in ge]
    return items, real, T, R, ctlT, mR, pr


def unmarked(toks):
    return [str(int(t)) for t in toks if re.fullmatch(r"\d{1,2}", t)]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--draws", type=int, default=10000)
    ap.add_argument("--seeds", type=int, default=20)
    a = ap.parse_args()
    key = tomokiyo()
    homs = {}
    for code, v in key.items():
        homs.setdefault(v, []).append(code)
    rows = list(csv.DictReader((l for l in open(PAIRS, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))
    gl = lambda t: "".join(c for c in norm(t) if c in homs)

    # positive control first (FK0)
    D, pc = [], []
    for seed in range(1, a.seeds + 1):
        rng = random.Random(seed)
        runs = [(unmarked(encipher(r["plain_raw"], homs, rng, 0.15, 0.10)), gl(r["plain_raw"])) for r in rows]
        _, _, T, R, ctlT, mR, _ = score(runs, key, a.draws, 7715)
        D.append(R - mR)
        pc.append((seed, T, p99(ctlT), R, mR))
    DK2 = sorted(D)[len(D) // 2]
    fk0 = sum(1 for (_, T, q, R, mR) in pc if T > q and R - mR >= 0.5 * DK2)
    with open(HERE / "witness/f7r_fixedkey_poscontrol.tsv", "w", encoding="utf-8") as f:
        f.write("seed\tT\tp99_T\tR\tmeanR_ctl\tD\n")
        for s, T, q, R, mR in pc:
            f.write(f"{s}\t{T}\t{q}\t{R:.3f}\t{mR:.3f}\t{R - mR:.3f}\n")
    print(f"positive control K2: D_K2 median {DK2:.3f}; FK1+FK2 PASS {fk0}/{a.seeds}")

    runs = [(unmarked(r["cipher_raw"].split()), gl(r["plain_raw"])) for r in rows]
    items, real, T, R, ctlT, mR, pr = score(runs, key, a.draws, 7715)
    q = p99(ctlT)
    D0 = R - mR
    fk1, fk2 = T > q, D0 >= 0.5 * DK2
    ids = [r["plain_line"] for r, (codes, g) in zip(rows, runs) if min(len(codes), len(g)) >= 4]
    with open(HERE / "witness/f7r_fixedkey.tsv", "w", encoding="utf-8") as f:
        f.write("run\tdecoded\tgloss\tL\tM\tp\n")
        for i, (codes, g, mk, n, m), l, p in zip(ids, items, real, pr):
            f.write(f"{i}\t{''.join(key.get(c, '?') for c in codes)}\t{g}\t{l}\t{m}\t{p:.4f}\n")
    cov = sum(1 for c, _ in runs for x in c if x in key), sum(len(c) for c, _ in runs)
    print(f"target: {len(items)} scorable runs; unmarked tokens in table {cov[0]}/{cov[1]}; T {T} vs control mean "
          f"{sum(ctlT) / len(ctlT):.1f} p99 {q} max {max(ctlT)}; R {R:.3f} vs meanR_ctl {mR:.3f}, D {D0:.3f} "
          f"vs 0.5*D_K2 {0.5 * DK2:.3f}; runs p<0.01: {sum(p < 0.01 for p in pr)}")
    if fk0 < a.seeds / 2:
        print("NON-TEST (FK0 positive control below 10/20)"); sys.exit(4)
    verdict = "PASS" if fk1 and fk2 else ("FK1 PASS, FK2 FAIL" if fk1 else "FK1 FAIL")
    print(f"FK1 {'PASS' if fk1 else 'FAIL'}; FK2 {'PASS' if fk2 else 'FAIL'} -> {verdict}")
    sys.exit(0 if fk1 and fk2 else 2)


if __name__ == "__main__":
    main()

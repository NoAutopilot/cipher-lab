#!/usr/bin/env python3
"""L2 (24 Sept 2026): cryptanalytic tests on La Garde 1577 (WVO 6179) and Marnix (WVO 6467), each with a matched control.

  python3 ciphers/la-garde-1577/solve_l2.py --corpus FR16.txt --control-plain PLAIN.txt [--seed 3]

L3 rerun (24 Sept 2026) on the reconciled v2 transcription, treating overlined/marked numerals as signs distinct
from their plain form (L1's transcription under-recorded these marks -- see NOTES 'L3'):

  python3 ciphers/la-garde-1577/solve_l2.py --corpus FR16.txt --control-plain PLAIN.txt \
      --ciphertext-6179 ciphertext_6179_v2.tsv --ciphertext-6467 ciphertext_6467_v2.tsv --mark-signs

Tests (all offline; corpus = tools/data/fr16 Catherine de Medicis letters, control prose = Marguerite de Valois,
Lettres inedites, 1580 letter, which is not in the training corpus):
  A  monoalphabetic / homophonic substitution (tools/homophonic_anneal.py), control with 0 and 8 percent token
     noise (the transcription's M rows), then the target 6179 (185 tokens, 24 signs).
  B  periodic polyalphabetic (Vigenere and Beaufort, periods 1-14) over fixed 24-letter alphabets in which number
     n is the n-th letter: control enciphered with a random period-5 key, then the target. Always uses the base
     digit value (marks have no numeric meaning under this design), so --mark-signs does not change test B.
  C  crib: the 6467 marginal note "Justifier le faict du grand" beside run 1, tested for a consistent many-to-one
     sign->letter map with up to 6 nulls.
Prints one line per test; exits 0. Default: overline/loop marks stripped, '07' kept distinct from '7'.
--mark-signs (test A/C only): a marked numeral ('16^', '4~') is a sign distinct from its plain form; a
free-standing '[mark]' row becomes its own sign 'MARK' instead of being dropped.
"""
import argparse, csv, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
from homophonic_anneal import Model, fold, score, solve, make_control  # noqa: E402

ALPHS = {"a24": "abcdefghiklmnopqrstuxyz&", "a24rev": "&zyxutsrqponmlkihgfedcba",
         "a23": "abcdefghiklmnopqrstuxyz"}


def signs(fn, mark_signs=False):
    out = []
    for r in csv.DictReader(open(fn if os.path.isabs(fn) else os.path.join(HERE, fn)), delimiter="\t"):
        raw = r["group"]
        if mark_signs:
            g = "MARK" if raw.startswith("[mark]") and raw == "[mark]" else raw.replace("[mark]", "")
        else:
            g = raw.replace("[mark]", "").rstrip("^~")
        if g:
            out.append(g)
    return out


def base_signs(fn):
    """Plain digit value only, for test B's numeric alphabet (marks are never numeric)."""
    return signs(fn, mark_signs=False)


def share(dec, truth):
    return sum(a == b for a, b in zip(dec, truth)) / len(truth)


def mono(seq, model, seed, restarts=8, iters=30000):
    sc, key = solve(seq, model, restarts, iters, seed, 1.0)[0]
    return sc, "".join(key[x] for x in seq), key


def poly_solve(nums, alpha, period, model, sign):
    m = len(alpha)
    shifts = [0] * period
    def dec(sh):
        out = []
        for i, n in enumerate(nums):
            ch = alpha[(sign * (n - 1) - sh[i % period]) % m]
            out.append(ch if ch in "abcdefghiklmnopqrstuxyz" else "x")
        return "".join(out)
    # init: per column best unigram fit
    for c in range(period):
        best = None
        for s in range(m):
            sh = shifts[:]; sh[c] = s
            p = dec(sh)[c::period]
            v = sum(__import__("math").log(model.freq.get(ch, 1e-6)) for ch in p)
            if best is None or v > best[0]:
                best = (v, s)
        shifts[c] = best[1]
    cur = score(model, dec(shifts), 1.0)
    improved = True
    while improved:
        improved = False
        for c in range(period):
            for s in range(m):
                sh = shifts[:]; sh[c] = s
                v = score(model, dec(sh), 1.0)
                if v > cur + 1e-9:
                    cur, shifts, improved = v, sh, True
    return cur, dec(shifts), shifts


def poly_best(nums, model):
    res = []
    for an, a in ALPHS.items():
        for sign in (1, -1):
            for p in range(1, 15):
                v, d, sh = poly_solve(nums, a, p, model, sign)
                res.append((v / len(nums) + 0.02 * p, v, an, sign, p, d))  # small per-period penalty
    res.sort(key=lambda r: -r[0])
    return res[0]


def crib_fits(seq, crib, max_nulls=6):
    """True if crib embeds in seq in order under one many-to-one sign->letter map, skipping <= max_nulls signs."""
    def go(i, j, m, nulls):
        if j == len(crib):
            return True
        if i == len(seq):
            return False
        t, ch = seq[i], crib[j]
        if m.get(t, ch) == ch and go(i + 1, j + 1, {**m, t: ch}, nulls):
            return True
        return nulls < max_nulls and t not in m and go(i + 1, j, m, nulls + 1)
    return go(0, 0, {}, 0)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", required=True)
    ap.add_argument("--control-plain", required=True)
    ap.add_argument("--seed", type=int, default=3)
    ap.add_argument("--ciphertext-6179", default="ciphertext_6179.tsv")
    ap.add_argument("--ciphertext-6467", default="ciphertext_6467.tsv")
    ap.add_argument("--mark-signs", action="store_true",
                     help="treat a marked numeral ('16^', '4~') as a sign distinct from its plain form (test A/C)")
    a = ap.parse_args()
    model = Model([open(a.corpus, encoding="utf-8").read()], order=3)
    rng = random.Random(a.seed)
    tgt = signs(a.ciphertext_6179, a.mark_signs)
    N, K = len(tgt), len(set(tgt))
    ctrl_text = open(a.control_plain, encoding="utf-8").read()

    # A: homophonic, clean and noisy controls
    seq, plain, truth = make_control(ctrl_text, K, N, model, a.seed)
    s, d, _ = mono(seq, model, a.seed)
    print(f"A control clean N={N} K={K}: {share(d, plain):.1%}  score/tok {s/N:.3f}  {d[:60]}")
    noisy = [x if rng.random() > 0.08 else rng.choice(sorted(set(seq))) for x in seq]
    s, d, _ = mono(noisy, model, a.seed)
    print(f"A control 8% noise: {share(d, plain):.1%}  score/tok {s/N:.3f}  {d[:60]}")
    s, d, _ = mono(tgt, model, a.seed)
    print(f"A target 6179: score/tok {s/N:.3f}  {d[:60]}")

    # B: periodic polyalphabetic
    alpha = ALPHS["a24"]
    p = "".join(ch for ch in fold(ctrl_text) if ch in alpha)[:N]
    key = [rng.randrange(24) for _ in range(5)]
    nums = [(alpha.index(ch) + key[i % 5]) % 24 + 1 for i, ch in enumerate(p)]
    r = poly_best(nums, model)
    print(f"B control period 5 a24: best {r[2]} sign {r[3]} period {r[4]}: {share(r[5], p):.1%}  {r[5][:60]}")
    run1 = signs(a.ciphertext_6467, a.mark_signs)[:27]
    for c in ("iustifierlefaictdugrand", "iustiffierlefaictdugrand"):
        print(f"C crib {c} in 6467 run 1 (27 signs, <=6 nulls): {'fits' if crib_fits(run1, c) else 'no consistent map'}")
    tn = [int(x) for x in base_signs(a.ciphertext_6179)]
    r = poly_best(tn, model)
    print(f"B target 6179: best {r[2]} sign {r[3]} period {r[4]} score/tok {r[1]/N:.3f}  {r[5][:60]}")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""GAPS15-moray-wood-1568 (2 Oct 2026): pre-registered crib test for Bain ii no.804 under key.tsv.

Bain, CSP Scotland ii no.804 (Wood to Cecil, Edinburgh 6 Sept 1568; TNA SP 52/15 by Bain's volume table, not yet imaged)
prints the plaintext of the letter's cipher words: "and says he must neidis haif it be on meinis or uthir". The question:
is that cipher phrase written in the f.213v postscript's key (Aymeloglu's key.tsv, credited, rule 8)?  Fixed here, before
any image of the leaf exists (PREREG.md beside this file gives the same in prose):

  Input   a transcription of the leaf's cipher signs in the Moray label set (ciphertext.tsv's labels), TSV with a 'sign' or
          'moray' column; '|' = gap (ignored), '?' = a sign with no Moray label (never matches). Person-signs 4b/Eb dropped.
  Decode  key.tsv applied sign by sign (word-signs U -> 'the', o2 -> 'and'); a label not in key.tsv decodes to '?'.
  Crib    16 spelling variants, fixed: says|sayis x neidis|nedis x haif|haue x meinis|menis (others as Bain prints), spaces
          dropped, v->u, j->i (key.tsv has one sign class for u/v).  42-44 letters.
  Stat    S = max over variants of LCS(decode letters, variant letters) / len(variant).
  Null A  200 letter-shuffles of every variant (same seed), S recomputed on the same decode -- holds letter frequency of the
          crib, moves only its order.
  Null B  200 shuffled keys (single-letter values permuted among single-letter signs, word- and person-signs fixed, the
          wood_test.py shape), decode recomputed, S against the true crib -- holds the transcription, moves the key.
          Both nulls move S (rule 3: neither is orthogonal to the statistic).
  PASS    S > the 99th percentile (rank 198/200) of null A AND of null B, AND S >= 0.60.  Anything else: FAIL ("not shown
          to be in key.tsv at this length and transcription"), never "different key" unless the positive control at the
          leaf's own measured error level passes >= 80 pct (rule 3, error bracket).

  --control   writes control.tsv: the positive control (the crib itself, a random variant, enciphered under key.tsv with
              random homophones, letters with no sign -> '?', 'and'/'the' as word-signs with p 0.5) at injected sign-error
              0/10/20/30 pct, 40 trials each, scored by the full test above; and the false-pass control (the same phrase
              enciphered under a shuffled key, i.e. a different key with the same sign inventory) at the same levels.
  --score FILE  runs the test on a transcription, writes FILE's stem + '_no804.tsv' beside this script, exits 0 on PASS,
              1 on FAIL.
  --reference  scores the R2989 line (../wood/wood_line.tsv, Bourdeau's sign order relabelled, GAPS9) as a known
              not-read-by-key.tsv reference.  Deterministic (seed 1).   python3 ciphers/moray-wood-1568/no804/no804_crib.py --control
"""
import argparse, itertools, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent; T = HERE.parent
WORD = {"U": "the", "o2": "and"}; DROP = {"4b", "Eb"}
BAIN = "and says he must neidis haif it be on meinis or uthir"
VARIANTS = {"says": ["says", "sayis"], "neidis": ["neidis", "nedis"], "haif": ["haif", "haue"], "meinis": ["meinis", "menis"]}
N_NULL = 200; FLOOR = 0.60; PCT = 0.99


def norm(s):
    return "".join(c for c in s.lower().replace("v", "u").replace("j", "i") if c.isalpha())


def crib_variants():
    words = BAIN.split(); slots = [VARIANTS.get(w, [w]) for w in words]
    return [" ".join(c) for c in itertools.product(*slots)]


CRIBS = crib_variants(); CRIB_LET = [norm(c) for c in CRIBS]


def load_key(path=T / "key.tsv"):
    return {r[0]: r[1] for r in (l.rstrip("\n").split("\t") for l in open(path) if not l.startswith("#")) if r[0] != "code"}


KEY = load_key()
LETTER_SIGNS = sorted(c for c, v in KEY.items() if len(v) == 1 and c not in WORD and c not in DROP)


def shuffled_key(rnd):
    vals = [KEY[c] for c in LETTER_SIGNS]; rnd.shuffle(vals); return dict(KEY, **dict(zip(LETTER_SIGNS, vals)))


def decode(signs, key=KEY):
    out = []
    for s in signs:
        if s in DROP or s == "|":
            continue
        v = WORD.get(s) or key.get(s)
        out.append(norm(v).replace("q", "") if v and v not in ("Q", "Q2") else "?")
    return "".join(out)


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for ca in a:
        cur = [0]
        for j, cb in enumerate(b):
            cur.append(prev[j] + 1 if ca == cb and ca != "?" else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def stat(dec, cribs=CRIB_LET):
    return max(lcs(dec, c) / len(c) for c in cribs)


def pctl(xs, p):
    xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]


def run_test(signs, rnd, cribs=CRIB_LET, n=N_NULL):
    dec = decode(signs); s = stat(dec, cribs)
    na = []
    for _ in range(n):
        sh = []
        for c in cribs:
            l = list(c); rnd.shuffle(l); sh.append("".join(l))
        na.append(stat(dec, sh))
    nb = [stat(decode(signs, shuffled_key(rnd)), cribs) for _ in range(n)]
    pa, pb = pctl(na, PCT), pctl(nb, PCT)
    ok = s > pa and s > pb and s >= FLOOR
    return dict(decode=dec, S=s, nullA_p99=pa, nullB_p99=pb, passed=ok)


def encipher(text, key, rnd):
    inv = {}
    for sgn, v in key.items():
        if len(v) == 1 and sgn not in WORD and sgn not in DROP:
            inv.setdefault(v, []).append(sgn)
    out = []
    for w in text.split():
        if w in ("and", "the") and rnd.random() < 0.5:
            out.append({"and": "o2", "the": "U"}[w]); continue
        for ch in norm(w):
            out.append(rnd.choice(inv[ch]) if ch in inv else "?")
    return out


def corrupt(signs, err, rnd):
    inv = LETTER_SIGNS + list(WORD)
    return [rnd.choice([x for x in inv if x != s]) if rnd.random() < err else s for s in signs]


def _control_row(args):
    kind, err, trials, seed = args
    rnd = random.Random(seed); npass, ss, n = 0, [], 0
    for _ in range(trials):
        k = KEY if kind == "positive" else shuffled_key(rnd)
        signs = corrupt(encipher(rnd.choice(CRIBS), k, rnd), err, rnd); n = len(signs)
        r = run_test(signs, rnd); npass += r["passed"]; ss.append(r["S"])
    return (kind, err, trials, n, npass / trials, sum(ss) / len(ss))


def control(trials=40, levels=(0.0, 0.10, 0.20, 0.30), seed=1):
    from multiprocessing import Pool
    jobs = [(kind, err, trials, seed * 1000 + i) for i, (err, kind) in enumerate(itertools.product(levels, ("positive", "false_pass")))]
    with Pool(4) as pool:
        rows = pool.map(_control_row, jobs)
    with open(HERE / "control.tsv", "w") as f:
        f.write("# no804_crib.py --control, seeds 1000+row, %d trials per row, nulls %d each; GAPS15-moray-wood-1568 2 Oct 2026\n" % (trials, N_NULL))
        f.write("control\tinjected_error\ttrials\tn_signs\tpass_rate\tmean_S\n")
        for r in rows:
            f.write("%s\t%.2f\t%d\t%d\t%.3f\t%.3f\n" % r)
            print("%s\terr=%.2f\ttrials=%d\tN_signs=%d\tpass=%.3f\tmeanS=%.3f" % r)
    return rows


def read_signs(path):
    lines = [l.rstrip("\n").split("\t") for l in open(path) if l.strip() and not l.startswith("#")]
    hdr = lines[0]; col = hdr.index("sign") if "sign" in hdr else hdr.index("moray")
    return [r[col].strip() or "?" for r in lines[1:]]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--control", action="store_true"); g.add_argument("--score"); g.add_argument("--reference", action="store_true")
    a = ap.parse_args(argv)
    if a.control:
        control(); return 0
    path = Path(a.score) if a.score else T / "wood" / "wood_line.tsv"
    r = run_test(read_signs(path), random.Random(1))
    verdict = "PASS" if r["passed"] else "FAIL"
    print(f"{path.name}: decode {r['decode']}\nS={r['S']:.3f} nullA_p99={r['nullA_p99']:.3f} nullB_p99={r['nullB_p99']:.3f} "
          f"floor={FLOOR} -> {verdict}")
    out = HERE / (path.stem + "_no804.tsv")
    with open(out, "w") as f:
        f.write("input\tdecode\tS\tnullA_p99\tnullB_p99\tfloor\tverdict\n")
        f.write(f"{path}\t{r['decode']}\t{r['S']:.3f}\t{r['nullA_p99']:.3f}\t{r['nullB_p99']:.3f}\t{FLOOR}\t{verdict}\n")
    return 0 if r["passed"] or a.reference else 1


if __name__ == "__main__":
    sys.exit(main())

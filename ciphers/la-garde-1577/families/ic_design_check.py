#!/usr/bin/env python3
"""IC design check (GAPS145, 3 Oct 2026): does la-garde-1577's base-code ciphertext have the unigram index of
coincidence of a one-sign-per-letter substitution (masc) or of a running-key Vigenere (flat ciphertext)?

Matched controls (rule 3): 300 French fr16 windows of the target's own N, enciphered (a) under a simple
substitution (IC is substitution-invariant, so the plaintext window's IC) and (b) under a running key (Vigenere,
plain window + key window from a different fr16 book), each clean and under two noise models at the measured
transcription error 0.23, plus (c) homophonic.py's own control at the target's K=26 (40 seeds, clean): 'profile' redraws a share p of tokens from the sequence's own unigram profile (the
homophonic.py _inject_noise recipe), 'uniform' replaces a share p with a uniformly random other type (the
worst case for this statistic, it flattens towards 1/K). IC depends on the design (substitution keeps the
language's peaked profile, running key flattens it), so the two controls can differ on the statistic; IC is
order-invariant, so no shuffled-target control is run (it would be identical by construction).

Run: python3 ciphers/la-garde-1577/families/ic_design_check.py [--check]   (--check: exit 1 if the committed
ic_design_check.tsv differs from a fresh run; seeded, deterministic)."""
import os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, "..", "..", ".."))
sys.path.insert(0, os.path.join(ROOT, "tools"))
sys.path.append(os.path.join(ROOT, "tools", "families"))
import judge_plaintext as jp  # noqa: E402
import running_key as rk  # noqa: E402

ERR, TRIALS = 0.23, 300


def ic(seq):
    n = len(seq)
    return sum(c * (c - 1) for c in Counter(seq).values()) / (n * (n - 1))


def target():
    toks = []
    for line in open(os.path.join(HERE, "basecode_cipher.txt")):
        if not line.startswith("#"):
            toks += line.split()
    return toks


def noisy(seq, p, mode, rng):
    seq = list(seq)
    types = sorted(set(seq))
    pool = list(seq)
    for i in range(len(seq)):
        if rng.random() < p:
            if mode == "profile":
                seq[i] = rng.choice(pool)
            else:
                seq[i] = rng.choice([t for t in types if t != seq[i]] or types)
    return seq


def main():
    tgt = target()
    N = len(tgt)
    d = os.path.join(ROOT, "tools", "data", "fr16")
    books = [rk.fold(jp.read_corpus(os.path.join(d, f))) for f in sorted(os.listdir(d)) if f.endswith(".gz")]
    rng = random.Random(145)
    rows = {}
    for t in range(TRIALS):
        bi, ki = rng.sample(range(len(books)), 2)
        P = books[bi][(s := rng.randrange(len(books[bi]) - N)):s + N]
        K = books[ki][(s := rng.randrange(len(books[ki]) - N)):s + N]
        masc = list(P)
        rkey = [rk.A[rk.encipher("vig", rk.IDX[a], rk.IDX[b])] for a, b in zip(P, K)]
        for name, seq in (("masc", masc), ("running_key", rkey)):
            rows.setdefault((name, "clean"), []).append(ic(seq))
            for mode in ("profile", "uniform"):
                rows.setdefault((name, mode), []).append(ic(noisy(seq, ERR, mode, rng)))
    from families import homophonic as h  # homophonic K=26 control: the family's own make_control, clean
    corp = [jp.read_corpus(os.path.join(d, f)) for f in sorted(os.listdir(d)) if f.endswith(".gz")]
    import contextlib, io
    for s in range(1, 41):
        with contextlib.redirect_stdout(io.StringIO()):
            msgs, _, _ = h.make_control({}, s, corp, {"N": N, "K": len(set(tgt)), "target_msgs": [tgt]})
        rows.setdefault(("homophonic_K26", "clean"), []).append(ic(msgs[0]))
    out = [f"# target N={N} K={len(set(tgt))} IC={ic(tgt):.4f}; controls {TRIALS} fr16 windows each, noise p={ERR}",
           "design\tnoise\tmean\tp05\tp95\tmin\tmax\ttarget_pct_rank"]
    T = ic(tgt)
    for (name, mode), v in rows.items():
        v = sorted(v)
        q = lambda f: v[min(len(v) - 1, int(f * len(v)))]
        rank = sum(1 for x in v if x < T) / len(v)
        out.append(f"{name}\t{mode}\t{sum(v)/len(v):.4f}\t{q(.05):.4f}\t{q(.95):.4f}\t{v[0]:.4f}\t{v[-1]:.4f}\t{rank:.3f}")
    text = "\n".join(out) + "\n"
    path = os.path.join(HERE, "ic_design_check.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path).read() == text
        print("check:", "ok" if ok else "STALE")
        sys.exit(0 if ok else 1)
    open(path, "w").write(text)
    print(text, end="")


if __name__ == "__main__":
    main()

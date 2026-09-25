#!/usr/bin/env python3
"""Breadth-lane cheap test 1 for ciphers/na-oldenbarnevelt-2442-1605 (VX-CT03, 25 Sept 2026).

Design under test: an otherwise-plain Spanish letter where some letters (hypothesised: mostly vowels, maybe a
few consonants) are replaced word-internally by handwritten digits, e.g. "s8crd4r37" for a word that reads
mostly in clear once the digits are resolved. This is NOT a full alphabet substitution -- most characters in
the ciphertext are already known plaintext letters. Reuses tools/homophonic_anneal.py's Model/anneal/solve
(pure Python, no numpy) rather than writing a new annealer: every already-clear letter becomes a "sign" fixed
to itself via --fix (so it never moves), and every digit becomes a free sign the annealer must resolve to a
plaintext letter -- exactly the tool's existing --fix mechanism, just used on ~20 crib signs instead of one or
two.

Usage:
  python3 solve_digit_subst.py target ciphertext.tsv --corpus ../corpus/es16-donquijote/donquijote1605_pg2000_body.txt
      [--restarts 8] [--iters 40000] [--order 4] [--seed 1] [--out reading.json]
  python3 solve_digit_subst.py control --corpus ... --held-out-frac 0.1 --n N --k K --seed 1 [3 seeds: repeat]

target mode: ciphertext.tsv columns block,line,token_index,raw_token,confidence (tools/reconcile_passes.py-style
reconciled output). Builds the sign stream in reading order (block by block, line by line, token by token; a
single space-less run per token, tokens separated by nothing -- word boundaries are not modelled as signs,
matching how the corpus n-gram model itself is built on a space-stripped letter stream).

control mode: draws a held-out passage of the SAME length N as the target's sign stream from the last
--held-out-frac of the corpus (never used to build the solving model, which trains on the first 1-frac), fixes
its K most-frequent letters (rule-3 matched control: same K, i.e. same number of free signs, as the target)
to digit signs 0..K-1, keeps every other letter as a crib sign fixed to itself (matching the target's design:
most letters clear, a fixed few converted), and solves blind with the same solver settings. Reports the number
of digit *positions* correctly recovered against ground truth -- rule 3's matched-control number, alongside
whatever the target run produces.
"""
import argparse, json, sys, os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import homophonic_anneal as ha  # noqa: E402


def fold_letter(ch):
    """Match ha.ALPHA's j->i, v->u folding for a single already-lowercase Latin letter."""
    return {"j": "i", "v": "u"}.get(ch, ch)


def load_ciphertext_tsv(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    h = rows[0]
    bi, li, ti, ri = h.index("block"), h.index("line"), h.index("token_index"), h.index("raw_token")
    data = rows[1:]
    data.sort(key=lambda r: (r[bi], int(r[li]), int(r[ti])))
    return [r[ri] for r in data]


def build_target_seq(tokens):
    """One sign per character, tokens concatenated (no space signs); digit chars are their own sign string,
    letter chars are folded then used as a sign equal to the letter itself (so --fix sign=letter is trivial:
    sign IS the letter). Also returns each token's sign-length, to re-insert spaces between tokens afterwards
    for the judge step (word segmentation needs spaces; the annealer's own n-gram model does not)."""
    seq = []
    n_digit, n_letter = 0, 0
    tok_lengths = []
    for tok in tokens:
        n0 = len(seq)
        for ch in tok:
            if ch.isdigit():
                seq.append(ch)
                n_digit += 1
            elif ch.isalpha():
                seq.append(fold_letter(ch))
                n_letter += 1
            # punctuation (periods, commas) dropped: not part of the sign stream, matching corpus fold()
        tok_lengths.append(len(seq) - n0)
    return seq, n_digit, n_letter, tok_lengths


def spaced(flat, tok_lengths):
    out, i = [], 0
    for n in tok_lengths:
        out.append(flat[i:i + n])
        i += n
    return " ".join(out)


def fix_string_for_letters(seq):
    """Every sign that is itself a lowercase a-z letter (not a digit) is a crib fixed to itself."""
    letters = sorted(set(s for s in seq if s.isalpha()))
    return {s: s for s in letters}


def run_target(args):
    tokens = load_ciphertext_tsv(args.ciphertext)
    seq, n_digit, n_letter, tok_lengths = build_target_seq(tokens)
    fixed = fix_string_for_letters(seq)
    digits_used = sorted(set(s for s in seq if s.isdigit()))
    full_text = open(args.corpus, encoding="utf-8").read()
    train_text = full_text[: int(len(full_text) * (1 - args.held_out_frac))]
    model = ha.Model([train_text], args.order)
    res = ha.solve(seq, model, args.restarts, args.iters, args.seed, args.uni_weight, fixed)
    sc, key = res[0]
    dec = "".join(key[x] for x in seq)
    out = {
        "mode": "target",
        "N_total_chars": len(seq),
        "N_digit_chars": n_digit,
        "N_letter_chars_fixed": n_letter,
        "K_distinct_digits": len(digits_used),
        "digits_used": digits_used,
        "best_score": sc,
        "digit_key": {d: key[d] for d in digits_used},
        "decoded": dec,
        "decoded_spaced": spaced(dec, tok_lengths),
        "restart_scores": [round(r[0], 1) for r in res],
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if args.out:
        json.dump(out, open(args.out, "w"), ensure_ascii=False, indent=1)
    return out


def run_control(args):
    text = open(args.corpus, encoding="utf-8").read()
    folded_all = ha.fold(text)
    split = int(len(folded_all) * (1 - args.held_out_frac))
    train_text, held_out = folded_all[:split], folded_all[split:]
    import random
    rng = random.Random(args.seed + 2000)
    start = rng.randrange(0, max(1, len(held_out) - args.n))
    passage = held_out[start:start + args.n]
    from collections import Counter
    freq = Counter(passage)
    top_k_letters = [a for a, _ in freq.most_common(args.k)]
    digit_of = {a: str(i) for i, a in enumerate(top_k_letters)}
    seq = [digit_of.get(ch, ch) for ch in passage]
    if args.crib_noise:
        # Matches the target's own transcription uncertainty: a --crib-noise share of the FIXED (letter)
        # sign positions are corrupted to a wrong letter, simulating a mis-transcribed crib rather than a
        # wrong digit (the failure mode a low-confidence token actually risks: rule 3, same design).
        alpha = sorted(ha.ALPHA)
        letter_positions = [i for i, s in enumerate(seq) if s.isalpha()]
        n_corrupt = int(round(len(letter_positions) * args.crib_noise))
        corrupt_idx = set(rng.sample(letter_positions, min(n_corrupt, len(letter_positions))))
        for i in corrupt_idx:
            true = seq[i]
            seq[i] = rng.choice([c for c in alpha if c != true])
    fixed = {s: s for s in set(seq) if s.isalpha()}
    model = ha.Model([train_text], args.order)
    res = ha.solve(seq, model, args.restarts, args.iters, args.seed, args.uni_weight, fixed)
    sc, key = res[0]
    dec = "".join(key[x] for x in seq)
    correct_positions = sum(1 for x, y in zip(dec, passage) if x == y)
    digit_positions = sum(1 for s in seq if s.isdigit())
    correct_digit_positions = sum(1 for s, x, y in zip(seq, dec, passage) if s.isdigit() and x == y)
    out = {
        "mode": "control",
        "seed": args.seed,
        "crib_noise": args.crib_noise,
        "N_total_chars": len(seq),
        "K_distinct_digits": args.k,
        "digit_positions": digit_positions,
        "correct_digit_positions": correct_digit_positions,
        "digit_share": round(correct_digit_positions / digit_positions, 3) if digit_positions else None,
        "correct_all_positions": correct_positions,
        "overall_share": round(correct_positions / len(seq), 3),
        "true_key": {v: k for k, v in digit_of.items()},
        "solved_key": {d: key[d] for d in digit_of.values()},
        "plain": passage,
        "decoded": dec,
    }
    print(json.dumps(out, ensure_ascii=False, indent=1))
    if args.out:
        json.dump(out, open(args.out, "w"), ensure_ascii=False, indent=1)
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)
    t = sub.add_parser("target")
    t.add_argument("ciphertext")
    t.add_argument("--corpus", required=True)
    t.add_argument("--held-out-frac", type=float, default=0.1)
    t.add_argument("--order", type=int, default=4)
    t.add_argument("--restarts", type=int, default=8)
    t.add_argument("--iters", type=int, default=40000)
    t.add_argument("--seed", type=int, default=1)
    t.add_argument("--uni-weight", type=float, default=1.0)
    t.add_argument("--out")
    c = sub.add_parser("control")
    c.add_argument("--corpus", required=True)
    c.add_argument("--held-out-frac", type=float, default=0.1)
    c.add_argument("--n", type=int, required=True)
    c.add_argument("--k", type=int, required=True)
    c.add_argument("--order", type=int, default=4)
    c.add_argument("--restarts", type=int, default=8)
    c.add_argument("--iters", type=int, default=40000)
    c.add_argument("--seed", type=int, default=1)
    c.add_argument("--uni-weight", type=float, default=1.0)
    c.add_argument("--crib-noise", type=float, default=0.0, help="fraction of fixed letter positions corrupted to a wrong letter (matches the target's own low-confidence-token rate)")
    c.add_argument("--out")
    a = ap.parse_args()
    if a.cmd == "target":
        run_target(a)
    else:
        run_control(a)


if __name__ == "__main__":
    main()

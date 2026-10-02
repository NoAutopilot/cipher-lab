#!/usr/bin/env python3
"""Alphabetic-order bracketing of a homophonic letter key, with an order-shuffle control
(GAPS-vanbeuningen-dewitt-1657, 2 Oct 2026; CLAUDE.md rules 3 and 4).

Many period keys allot their letter homophones in alphabetical order of the plaintext letter (a = 39-43,
b = 44-45, c = 46-47 ...), often starting the numbering part-way through the alphabet so the sequence wraps
once (k..y at 4-37, then a..i at 39-65). When the well-attested codes show that order, the codes of a letter
that is still uncertain (a one-context homophone, a two-value conflict) are *bracketed* by their attested
neighbours: a code sitting between two codes that both read `a` is predicted to read `a` too. This script
measures how well the attested codes keep the order, checks the bracket rule against its own known answers,
and prints the bracket for each queried code -- a prior that says which value to check first on the image,
never a reading (rule 4: a structural prior does not grade a token).

Two statistics, each beside its control (rule 3). The control re-assigns the same letter labels to the same
code numbers at random, N times; it varies exactly the axis the statistics measure (which letter sits at which
number), so it can fail differently from the real key.

1. descents: sort the attested codes by number; count consecutive pairs whose letters go backwards in the
   alphabet, taking the best of the cyclic rotations of the alphabet so one wrap costs nothing. A key in
   strict order scores 0; random order scores about half the pairs.
2. leave-one-out bracket accuracy: hide each attested code in turn, take its nearest attested neighbours
   below and above by number (cyclically), predict the cyclic letter interval between their letters, and
   score a hit if the hidden code's own letter lies inside. Also report the mean interval width: a wide
   interval is a weak prediction even when it hits.

Pre-registration discipline: write what each outcome will be taken to mean into the target's NOTES.md
before running (the vanbeuningen-dewitt-1657 section of 2 Oct 2026 is the worked example).

Input: a key TSV with columns code, value, grade (tools/decode_key.py's key.tsv). Only numeric codes (an
optional trailing separator such as ',' or ':' is stripped; one row per number) whose value is a single
letter count. Which grades count as attested is set by --grades (default C). Letter classes merged as one
17th-century letter: i/j and u/v (--no-merge keeps them apart).

Usage:
  tools/key_order_test.py ciphers/<t>/key.tsv [--grades C] [--query 40 11 5] [--shuffles 1000] [--seed 1]
  tools/key_order_test.py KEY --json           machine-readable output

Exit 0 always (it reports, it does not gate); the pre-registered reading decides.
"""
import argparse, collections, json, random, sys

ALPHABET = list('abcdefghiklmnopqrstuwxyz')  # i/j merged, u/v merged (24 letters)
ALPHABET_FULL = list('abcdefghijklmnopqrstuvwxyz')


def load_key(path, grades, merge=True, raw=False):
    """Return {code_number: (letter, grade)} for single-letter numeric codes at the given grades
    (raw=True keeps any value, e.g. a 'd|a' conflict, for display)."""
    rows = {}
    for line in open(path, encoding='utf-8'):
        p = line.rstrip('\n').split('\t')
        if len(p) < 3 or p[0] == 'code':
            continue
        code, value, grade = p[0].strip(), p[1].strip(), p[2].strip()
        code = code.rstrip(',:;.')
        if not code.isdigit():
            continue
        if not raw and (len(value) != 1 or not value.isalpha()):
            continue
        v = value.lower()
        if merge and not raw:
            v = {'j': 'i', 'v': 'u'}.get(v, v)
        n = int(code)
        if n in rows:
            continue  # the ',' and ':' variants of one code are one row
        if grades is None or grade in grades:
            rows[n] = (v, grade)
    return rows


def rank_map(alphabet):
    return {c: i for i, c in enumerate(alphabet)}


def descents(seq_letters, alphabet):
    """Minimum over cyclic rotations of the count of backward steps between consecutive letters."""
    L = len(alphabet)
    rk = rank_map(alphabet)
    rs = [rk[c] for c in seq_letters]
    best = None
    for rot in range(L):
        rr = [(r - rot) % L for r in rs]
        d = sum(1 for a, b in zip(rr, rr[1:]) if b < a)
        best = d if best is None else min(best, d)
    return best


def cyclic_interval(lo, hi, alphabet):
    """Letters from lo to hi inclusive, going forward cyclically."""
    rk = rank_map(alphabet)
    L = len(alphabet)
    out, i = [], rk[lo]
    while True:
        out.append(alphabet[i])
        if alphabet[i] == hi:
            return out
        i = (i + 1) % L
        if len(out) > L:
            return out


def bracket(codes_sorted, letters, n, alphabet):
    """Bracket for code number n given attested (code -> letter) in codes_sorted/letters, excluding n itself.
    Returns (lower_code, upper_code, interval_letters)."""
    others = [c for c in codes_sorted if c != n]
    if len(others) < 2:
        return None
    below = [c for c in others if c < n]
    above = [c for c in others if c > n]
    lo = below[-1] if below else others[-1]   # wrap to the largest
    hi = above[0] if above else others[0]     # wrap to the smallest
    return lo, hi, cyclic_interval(letters[lo], letters[hi], alphabet)


def loo_accuracy(letters, alphabet):
    codes = sorted(letters)
    hits, widths = 0, []
    for c in codes:
        b = bracket(codes, letters, c, alphabet)
        if b is None:
            continue
        lo, hi, iv = b
        widths.append(len(iv))
        hits += letters[c] in iv
    return hits, len(codes), (sum(widths) / len(widths) if widths else 0.0)


def shuffle_control(letters, alphabet, n_shuffles, seed):
    rng = random.Random(seed)
    codes = sorted(letters)
    labels = [letters[c] for c in codes]
    out = []
    for _ in range(n_shuffles):
        lab = labels[:]
        rng.shuffle(lab)
        sh = dict(zip(codes, lab))
        d = descents([sh[c] for c in codes], alphabet)
        h, n, w = loo_accuracy(sh, alphabet)
        out.append((d, h, w))
    return out


def summarize(vals):
    vs = sorted(vals)
    n = len(vs)
    mean = sum(vs) / n
    return {'mean': round(mean, 3), 'min': vs[0], 'p05': vs[int(0.05 * (n - 1))], 'p95': vs[int(0.95 * (n - 1))], 'max': vs[-1]}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('key')
    ap.add_argument('--grades', nargs='*', default=['C'], help='grades counted as attested (default C)')
    ap.add_argument('--query', nargs='*', default=[], help='code numbers to bracket (any grade; excluded from the attested set)')
    ap.add_argument('--shuffles', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--no-merge', action='store_true', help='keep i/j and u/v as separate letters')
    ap.add_argument('--json', action='store_true')
    a = ap.parse_args(argv)
    alphabet = ALPHABET_FULL if a.no_merge else ALPHABET
    attested_all = load_key(a.key, set(a.grades), merge=not a.no_merge)
    on_file = load_key(a.key, None, merge=False, raw=True)  # any grade and value, for the query display only
    queries = [int(q) for q in a.query]
    attested = {c: v for c, (v, g) in attested_all.items() if c not in queries}
    letters = {c: v for c, v in attested.items()}
    codes = sorted(letters)
    if len(codes) < 3:
        print('fewer than 3 attested single-letter numeric codes; nothing to test', file=sys.stderr)
        return 0
    real_d = descents([letters[c] for c in codes], alphabet)
    real_h, real_n, real_w = loo_accuracy(letters, alphabet)
    ctl = shuffle_control(letters, alphabet, a.shuffles, a.seed)
    d_ctl = summarize([x[0] for x in ctl])
    h_ctl = summarize([x[1] for x in ctl])
    w_ctl = summarize([x[2] for x in ctl])
    p_d = sum(1 for x in ctl if x[0] <= real_d) / len(ctl)
    p_h = sum(1 for x in ctl if x[1] >= real_h) / len(ctl)
    # the real key's own descents, named
    rk = rank_map(alphabet)
    # choose the rotation that gives the minimum and list its backward steps
    L = len(alphabet)
    rs = [rk[letters[c]] for c in codes]
    best_rot, best_d = 0, None
    for rot in range(L):
        rr = [(r - rot) % L for r in rs]
        d = sum(1 for x, y in zip(rr, rr[1:]) if y < x)
        if best_d is None or d < best_d:
            best_rot, best_d = rot, d
    rr = [(r - best_rot) % L for r in rs]
    named = [f'{codes[i]} {letters[codes[i]]} -> {codes[i+1]} {letters[codes[i+1]]}' for i in range(len(codes) - 1) if rr[i + 1] < rr[i]]
    loo_misses = []
    for c in codes:
        b = bracket(codes, letters, c, alphabet)
        if b and letters[c] not in b[2]:
            loo_misses.append(f'{c} {letters[c]} (bracket {b[0]} {letters[b[0]]} .. {b[1]} {letters[b[1]]} = {"".join(b[2])})')
    qres = []
    all_codes = sorted(set(codes) | set(queries))
    for q in queries:
        b = bracket(codes, letters, q, alphabet)
        if b is None:
            continue
        lo, hi, iv = b
        onfile = on_file.get(q, ('?', '?'))
        qres.append({'code': q, 'on_file': onfile[0], 'grade': onfile[1], 'lower': f'{lo} {letters[lo]}', 'upper': f'{hi} {letters[hi]}', 'bracket': ''.join(iv)})
    res = {'key': a.key, 'grades': a.grades, 'attested_codes': len(codes), 'alphabet_start': alphabet[best_rot],
           'descents_real': real_d, 'descents_named': named, 'descents_shuffle': d_ctl, 'p_descents_le_real': p_d,
           'loo_hits_real': f'{real_h}/{real_n}', 'loo_acc_real': round(real_h / real_n, 3), 'loo_width_real': round(real_w, 2),
           'loo_misses_real': loo_misses, 'loo_hits_shuffle': h_ctl, 'loo_width_shuffle': w_ctl, 'p_loo_ge_real': p_h,
           'shuffles': a.shuffles, 'seed': a.seed, 'queries': qres}
    if a.json:
        print(json.dumps(res, indent=1, ensure_ascii=False))
        return 0
    print(f"key {a.key}: {len(codes)} attested codes at grade {'/'.join(a.grades)}; alphabet read as starting at '{alphabet[best_rot]}' (best rotation)")
    print(f"descents: real {real_d} [{'; '.join(named) or 'none'}] | shuffle mean {d_ctl['mean']} min {d_ctl['min']} p05 {d_ctl['p05']} (N={a.shuffles}) | P(shuffle <= real) = {p_d}")
    print(f"leave-one-out bracket: real {real_h}/{real_n} = {real_h/real_n:.3f} at mean width {real_w:.2f} letters"
          f" [misses: {'; '.join(loo_misses) or 'none'}] | shuffle hits mean {h_ctl['mean']} p95 {h_ctl['p95']} max {h_ctl['max']} at mean width {w_ctl['mean']} | P(shuffle >= real) = {p_h}")
    for q in qres:
        print(f"bracket {q['code']} (on file {q['on_file']}, grade {q['grade']}): {q['lower']} .. {q['upper']} -> {{{','.join(q['bracket'])}}}")
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""AX2-4612 (26 Sept 2026): matched control for the key-seeded anneal (CLAUDE.md rule 3), run BEFORE the
4612 v3 target. 5811's real ciphertext (a letter key_full reads correctly), cut to 4612 v3's N of value-1-120
numerals (833, the same cut ax4612tr/ciphertext_5811_cut833.tsv/word_share_check_v3.py used), annealed with
tools/homophonic_anneal.py's new --init started from key_full with a random 20 percent of codes 1-120
reassigned to a different letter, 3 seeds (each seed perturbs a fresh 20 percent and anneals independently).

Gate, written here before this script was run: the control recovers >= 0.90 of 5811's key_full token reading
(the share of the 833 sign occurrences whose annealed letter matches key_full's own letter for that sign) in
each of the 3 seeds. Only if this gate passes does the 4612 v3 target run (this script does not run the
target; see anneal_target.py)."""
import csv, os, random, sys

R = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..'))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha
import judge_plaintext as jp

SPEC_CORPORA = [
    os.path.join(R, 'tools', 'data', 'fr16', 'lettresdecatheri01cathuoft_djvu.txt.gz'),
    os.path.join(R, 'tools', 'data', 'fr16', 'lettresdecatheri02cathuoft_djvu.txt.gz'),
    os.path.join(R, 'tools', 'data', 'fr16', 'lettresindites00marg_djvu.txt.gz'),
]
D = os.path.dirname(os.path.abspath(__file__))  # ax4612tr/, so this script's own file lives one level below target root


def load_key_full_120(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    key = {}
    for r in rows:
        try:
            code = int(r['code'])
        except (ValueError, KeyError):
            continue
        v = r['value']
        if 1 <= code <= 120 and len(v) == 1 and v.isalpha():
            key[str(code)] = v
    return key


def load_seq(path):
    """Flat sequence of value-1-120 numeral signs (as strings), in file order, run breaks dropped -- the
    anneal treats the whole cut as one long stream of homophonic signs, same as its own --control mode."""
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    seq = []
    for r in rows:
        s = r['sign'].strip()
        if s.isdigit() and 1 <= int(s) <= 120:
            seq.append(s)
    return seq


def perturb(key, frac, rng):
    codes = sorted(key)
    n = round(frac * len(codes))
    chosen = rng.sample(codes, n)
    out = dict(key)
    for c in chosen:
        letters = [l for l in ha.ALPHA if l != key[c]]
        out[c] = rng.choice(letters)
    return out, set(chosen)


if __name__ == '__main__':
    TARGET = os.path.dirname(D)  # ciphers/lodewijk-van-nassau-1573-74
    key_full = load_key_full_120(os.path.join(TARGET, 'key_full.tsv'))
    seq = load_seq(os.path.join(D, 'ciphertext_5811_cut833.tsv'))
    print(f'5811 cut: N={len(seq)} signs, K={len(set(seq))} distinct')

    texts = [jp.read_corpus(p) for p in SPEC_CORPORA]
    model = ha.Model(texts, 3)

    shares = []
    for seed in (1, 2, 3):
        rng = random.Random(seed)
        init_key, changed = perturb(key_full, 0.20, rng)
        res = ha.solve(seq, model, restarts=8, iters=40000, seed=seed, uni_w=1.0, init=init_key)
        sc, best = res[0][:2]
        n_match = sum(1 for s in seq if best.get(s) == key_full.get(s))
        share = n_match / len(seq)
        shares.append(share)
        print(f'seed {seed}: perturbed {len(changed)}/{len(init_key)} codes ({sorted(changed)[:8]}...), '
              f'best score {sc:.1f}, recovers {n_match}/{len(seq)} = {share:.1%} of key_full\'s token reading')

    print()
    print(f'GATE: all 3 seeds recover >= 0.90? {all(s >= 0.90 for s in shares)} (shares: {[round(s,3) for s in shares]})')

"""Structural stats and a one-key pool test for the 8 Hellen->Frederick II ciphertexts.

Reads ciphertext_R<id>.txt (Bourdeau audit projections, credited in NOTES.md), classifies
each whitespace-separated segment as numeric (1-4 digits after stripping '_'/'^' marks) or
unresolved (contains '?' or is not 1-4 digits), following the same rule as cyphersolver's
audit_transcription.py (marks are transcriber uncertainty, not evidence).

Pool test (rule 3, matched control): does the 1763 cluster (six records, 15 Apr-5 Jul 1763)
share one key? Compares real cross-record Jaccard of numeric type-sets against a control that
randomly re-splits the pooled 1763 token stream into six groups of the same sizes -- if the six
records already share one code, their real pairwise Jaccard should sit inside the same range as
random splits of the same pooled stream (a random split trivially shares the pool's vocabulary).
A LOWER real Jaccard than the control would mean the six records draw from different vocabularies
despite being adjacent dates in the same volume -- evidence against a single shared key.

Usage: python3 pool_stats.py [--seed N] [--trials N]
"""
import argparse
import json
import random
import re
from pathlib import Path
from statistics import mean

ROOT = Path(__file__).resolve().parent

RECORDS_1752 = ['1953']
RECORDS_1756 = ['1049']
RECORDS_1763 = ['1045', '1046', '1047', '1048', '1060', '1061']
ALL_RECORDS = RECORDS_1752 + RECORDS_1756 + RECORDS_1763


def classify(raw):
    compact = raw.strip()
    digits = compact.replace('_', '').replace('^', '')
    if re.fullmatch(r'\d{1,4}', digits):
        return 'numeric', int(digits)
    return 'unresolved', None


def load(rid):
    path = ROOT / f'ciphertext_R{rid}.txt'
    text = path.read_text(encoding='utf8').strip()
    segs = text.split()
    numeric = []
    unresolved = 0
    widths = {}
    for s in segs:
        status, val = classify(s)
        if status == 'numeric':
            numeric.append(val)
            w = len(str(val))
            widths[w] = widths.get(w, 0) + 1
        else:
            unresolved += 1
    return dict(segments=len(segs), numeric=numeric, unresolved=unresolved, widths=widths)


def jaccard(a, b):
    a, b = set(a), set(b)
    if not a and not b:
        return 0.0
    return len(a & b) / len(a | b)


def pairwise_mean_jaccard(groups):
    vals = []
    keys = list(groups.keys())
    for i in range(len(keys)):
        for j in range(i + 1, len(keys)):
            vals.append(jaccard(groups[keys[i]], groups[keys[j]]))
    return mean(vals) if vals else 0.0


def random_split_control(pooled_numeric, sizes, trials, seed):
    rng = random.Random(seed)
    results = []
    for _ in range(trials):
        shuffled = pooled_numeric[:]
        rng.shuffle(shuffled)
        groups = {}
        i = 0
        for k, n in enumerate(sizes):
            groups[k] = shuffled[i:i + n]
            i += n
        results.append(pairwise_mean_jaccard(groups))
    return results


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seed', type=int, default=20260925)
    ap.add_argument('--trials', type=int, default=200)
    args = ap.parse_args()

    data = {rid: load(rid) for rid in ALL_RECORDS}

    print('== Per-record structural stats ==')
    for rid in ALL_RECORDS:
        d = data[rid]
        nums = d['numeric']
        rng = (min(nums), max(nums)) if nums else (None, None)
        print(f'R{rid}: segments={d["segments"]} numeric={len(nums)} '
              f'distinct={len(set(nums))} unresolved={d["unresolved"]} '
              f'range={rng[0]}-{rng[1]} widths={dict(sorted(d["widths"].items()))}')

    print()
    print('== Cross-family range overlap (1752 vs 1756 vs 1763 pooled) ==')
    fam_nums = {
        '1752 (R1953)': data['1953']['numeric'],
        '1756 (R1049)': data['1049']['numeric'],
        '1763 pooled (6 records)': [v for rid in RECORDS_1763 for v in data[rid]['numeric']],
    }
    for name, nums in fam_nums.items():
        print(f'{name}: n={len(nums)} distinct={len(set(nums))} range={min(nums)}-{max(nums)}')
    fam_keys = list(fam_nums.keys())
    for i in range(len(fam_keys)):
        for j in range(i + 1, len(fam_keys)):
            a, b = fam_nums[fam_keys[i]], fam_nums[fam_keys[j]]
            print(f'Jaccard {fam_keys[i]} vs {fam_keys[j]}: {jaccard(a, b):.4f}  '
                  f'shared values: {len(set(a) & set(b))}')

    print()
    print('== 1763 cluster: does it plausibly share one key? (pools-first question) ==')
    cluster_groups = {rid: data[rid]['numeric'] for rid in RECORDS_1763}
    sizes = [len(cluster_groups[rid]) for rid in RECORDS_1763]
    real_mean_jaccard = pairwise_mean_jaccard(cluster_groups)
    print(f'Real cross-record mean pairwise Jaccard (6 records, {len(RECORDS_1763)*(len(RECORDS_1763)-1)//2} pairs): '
          f'{real_mean_jaccard:.4f}')
    pooled_numeric = [v for rid in RECORDS_1763 for v in data[rid]['numeric']]
    control_vals = random_split_control(pooled_numeric, sizes, args.trials, args.seed)
    print(f'Random-split control ({args.trials} trials, same pool + same group sizes): '
          f'mean={mean(control_vals):.4f} min={min(control_vals):.4f} max={max(control_vals):.4f}')
    pct_real_below = sum(1 for v in control_vals if v > real_mean_jaccard) / len(control_vals)
    print(f'Fraction of control trials with HIGHER Jaccard than the real split: {pct_real_below:.3f}')
    print('Interpretation: if the real value sits inside/near the control range, the six records '
          'are consistent with drawing from one shared code (their overlap is what a random split '
          'of one shared vocabulary would also show). If the real value is well BELOW the control '
          'range, the records draw from different vocabularies despite sitting in one archival run.')

    total_1763_tokens = sum(data[rid]['segments'] for rid in RECORDS_1763)
    total_pool_tokens = sum(data[rid]['segments'] for rid in ALL_RECORDS)
    print()
    print(f'== Pool size (CLAUDE.md sign-pool threshold: >=2000 signs) ==')
    print(f'1763 cluster alone: {total_1763_tokens} segments ({sum(sizes)} numeric)')
    print(f'All 8 despatches pooled: {total_pool_tokens} segments')

    out = dict(
        per_record={rid: dict(segments=data[rid]['segments'], numeric=len(data[rid]['numeric']),
                               distinct=len(set(data[rid]['numeric'])),
                               range=[min(data[rid]['numeric']), max(data[rid]['numeric'])] if data[rid]['numeric'] else None,
                               unresolved=data[rid]['unresolved'])
                    for rid in ALL_RECORDS},
        cross_family_jaccard={f'{fam_keys[i]}|{fam_keys[j]}': jaccard(fam_nums[fam_keys[i]], fam_nums[fam_keys[j]])
                               for i in range(len(fam_keys)) for j in range(i + 1, len(fam_keys))},
        cluster_1763=dict(real_mean_jaccard=real_mean_jaccard,
                           control_trials=args.trials, control_seed=args.seed,
                           control_mean=mean(control_vals), control_min=min(control_vals),
                           control_max=max(control_vals),
                           frac_control_higher=pct_real_below),
        pool_size=dict(cluster_1763_segments=total_1763_tokens, all_8_segments=total_pool_tokens),
    )
    (ROOT / 'pool_stats_output.json').write_text(json.dumps(out, indent=2), encoding='utf8')
    print()
    print('Written pool_stats_output.json')


if __name__ == '__main__':
    main()

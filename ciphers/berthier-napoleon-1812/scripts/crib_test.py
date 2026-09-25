#!/usr/bin/env python3
"""LANE R6 Y9 crib test: does Chuquet 1912 letter XIX or XXIII (both dated
22 Dec 1812) fit the Berthier cryptogram (325 groups, this repo's
ciphertext_full.tsv)?  Matched control = the same test run against every
other Chuquet Dec-1812 Berthier-to-Napoleon letter on file (34 total incl.
XIX/XXIII), so a fit only means something if XIX/XXIII beat the field.

Three independent, honestly-reported metrics, no cherry-picking:
  1. length fit: |n_words - n_groups| / n_groups  (lower = better)
  2. repeat-rate fit: |word_repeat_rate - group_repeat_rate|  (lower = better)
  3. gap-distribution fit: max difference between the empirical CDFs of
     normalised repeat-gaps (a KS-style statistic; lower = better)
"""
import json, re

def words_of(text):
    return re.findall(r"[a-zàâäéèêëïîôöùûüç]+", text.lower())

def repeat_gaps(seq):
    """normalised gap (as fraction of len(seq)) between each repeat and its
    most recent earlier occurrence of the same token"""
    last_seen = {}
    gaps = []
    n = len(seq)
    for i, tok in enumerate(seq):
        if tok in last_seen:
            gaps.append((i - last_seen[tok]) / n)
        last_seen[tok] = i
    return sorted(gaps)

def ks_stat(a, b):
    """max |CDF_a - CDF_b| over the pooled support, a and b are sorted lists"""
    if not a or not b:
        return 1.0
    pts = sorted(set(a) | set(b))
    na, nb = len(a), len(b)
    ia = ib = 0
    d = 0.0
    for p in pts:
        while ia < na and a[ia] <= p: ia += 1
        while ib < nb and b[ib] <= p: ib += 1
        d = max(d, abs(ia/na - ib/nb))
    return d

if __name__ == '__main__':
    crypto_lines = open('ciphertext_full.tsv').read().strip().split('\n')[1:]
    groups = []
    for line in crypto_lines:
        groups.extend(line.split('\t')[1].split())
    n_groups = len(groups)
    group_repeat_rate = (n_groups - len(set(groups))) / n_groups
    group_gaps = repeat_gaps(groups)

    letters = json.load(open('scripts/letters.json'))
    rows = []
    for roman, d in letters.items():
        w = words_of(d['text'])
        if len(w) < 20:
            continue
        n_words = len(w)
        word_repeat_rate = (n_words - len(set(w))) / n_words
        word_gaps = repeat_gaps(w)
        length_fit = abs(n_words - n_groups) / n_groups
        rate_fit = abs(word_repeat_rate - group_repeat_rate)
        gap_fit = ks_stat(group_gaps, word_gaps)
        rows.append({
            'roman': roman, 'n_words': n_words,
            'word_repeat_rate': round(word_repeat_rate, 4),
            'length_fit': round(length_fit, 4),
            'rate_fit': round(rate_fit, 4),
            'gap_fit': round(gap_fit, 4),
        })

    print(f'cryptogram: {n_groups} groups, {len(set(groups))} unique, repeat_rate={round(group_repeat_rate,4)}')
    print()
    for key in ('length_fit', 'rate_fit', 'gap_fit'):
        print(f'--- ranked by {key} (lower = better fit) ---')
        ranked = sorted(rows, key=lambda r: r[key])
        for rank, r in enumerate(ranked, 1):
            flag = '  <== XIX/XXIII' if r['roman'] in ('XIX', 'XXIII') else ''
            print(f"{rank:2d}. {r['roman']:8s} n_words={r['n_words']:4d} {key}={r[key]:.4f}{flag}")
        print()

    json.dump(rows, open('scripts/crib_test_results.json', 'w'), indent=1)

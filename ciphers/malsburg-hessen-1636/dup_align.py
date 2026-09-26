#!/usr/bin/env python3
"""bMALDUP: global alignment (edit distance / NW) between f.28 and f.30 group sequences,
with a matched control (f.28 vs recon_0003+recon_0012) and a shuffle-null control (200
shuffles of f.30's own groups), for the malsburg-hessen-1636 507/508 duplicate test.
"""
import csv, random, sys

def read_draft(path):
    rows = []
    with open(path, encoding='utf-8') as f:
        r = csv.DictReader(f, delimiter='\t')
        for row in r:
            rows.append((row['line'], int(row['position']), row['sign']))
    # sort by line (as encountered order in file is already line-then-pos for these files
    # since ciphertext_draft.tsv is written in that order); keep sign sequence only
    return [s for (_l, _p, s) in rows]

def nw_align(a, b, match=1, mismatch=-1, gap=-1):
    n, m = len(a), len(b)
    dp = [[0]*(m+1) for _ in range(n+1)]
    for i in range(n+1):
        dp[i][0] = i*gap
    for j in range(m+1):
        dp[0][j] = j*gap
    for i in range(1, n+1):
        for j in range(1, m+1):
            sc = match if a[i-1] == b[j-1] else mismatch
            dp[i][j] = max(dp[i-1][j-1]+sc, dp[i-1][j]+gap, dp[i][j-1]+gap)
    # traceback
    i, j = n, m
    pairs = []
    while i > 0 and j > 0:
        sc = match if a[i-1] == b[j-1] else mismatch
        if dp[i][j] == dp[i-1][j-1] + sc:
            pairs.append((a[i-1], b[j-1]))
            i -= 1; j -= 1
        elif dp[i][j] == dp[i-1][j] + gap:
            pairs.append((a[i-1], None))
            i -= 1
        else:
            pairs.append((None, b[j-1]))
            j -= 1
    while i > 0:
        pairs.append((a[i-1], None)); i -= 1
    while j > 0:
        pairs.append((None, b[j-1])); j -= 1
    pairs.reverse()
    aligned = [(x, y) for (x, y) in pairs if x is not None and y is not None]
    ident = sum(1 for (x, y) in aligned if x == y)
    share = ident / len(aligned) if aligned else 0.0
    return share, ident, len(aligned), pairs

def main():
    f28 = read_draft('recon_0028/ciphertext_draft.tsv')
    f30 = read_draft('recon_0030/ciphertext_draft.tsv')
    r3 = read_draft('recon_0003/ciphertext_draft.tsv')
    r12 = read_draft('recon_0012/ciphertext_draft.tsv')
    control_text = r3 + r12

    print(f'f.28 groups: {len(f28)}')
    print(f'f.30 groups: {len(f30)}')
    print(f'control text (recon_0003+recon_0012) groups: {len(control_text)}')

    # TARGET: f.28 vs f.30
    share, ident, alen, pairs = nw_align(f28, f30)
    print(f'\nTARGET f.28 vs f.30: identity {ident}/{alen} = {share:.4f}')

    # CONTROL A: f.28 vs recon_0003+recon_0012 (different, already-reconciled text, same cipher/design)
    shareA, identA, alenA, _ = nw_align(f28, control_text)
    print(f'CONTROL-A f.28 vs recon_0003+recon_0012: identity {identA}/{alenA} = {shareA:.4f}')

    # CONTROL B: 200 shuffles of f.30's own groups, aligned against f.28
    random.seed(20260926)
    shuffle_shares = []
    f30_list = list(f30)
    for _ in range(200):
        shuffled = f30_list[:]
        random.shuffle(shuffled)
        s, _, _, _ = nw_align(f28, shuffled)
        shuffle_shares.append(s)
    shuffle_shares.sort()
    mean_s = sum(shuffle_shares) / len(shuffle_shares)
    p95_s = shuffle_shares[int(0.95 * len(shuffle_shares)) - 1]
    p99_s = shuffle_shares[int(0.99 * len(shuffle_shares)) - 1]
    print(f'CONTROL-B f.28 vs 200 shuffles of f.30 groups: mean {mean_s:.4f}, p95 {p95_s:.4f}, p99 {p99_s:.4f}, min {shuffle_shares[0]:.4f}, max {shuffle_shares[-1]:.4f}')

    print(f'\nSUMMARY: target={share:.4f}  control-A(diff text)={shareA:.4f}  control-B(shuffle mean/p95)={mean_s:.4f}/{p95_s:.4f}')

    # Write dup_align.tsv: full aligned pair list from the TARGET alignment, with match flag
    with open('dup_align.tsv', 'w', encoding='utf-8') as fh:
        fh.write('idx\tf28_group\tf30_group\tmatch\n')
        for idx, (x, y) in enumerate(pairs, 1):
            m = '1' if (x is not None and y is not None and x == y) else '0'
            fh.write(f'{idx}\t{x if x is not None else ""}\t{y if y is not None else ""}\t{m}\n')
    print("\nwrote dup_align.tsv")

    # differing pairs (both present, both non-empty, not equal) -> candidate equivalences
    diffs = {}
    for (x, y) in pairs:
        if x is not None and y is not None and x != y:
            diffs.setdefault((x, y), 0)
            diffs[(x, y)] += 1
    print(f'\ndiffering aligned pairs (candidate equivalences), {len(diffs)} distinct pairs:')
    for (x, y), c in sorted(diffs.items(), key=lambda kv: -kv[1])[:20]:
        print(f'  {x} <-> {y}  x{c}')

if __name__ == '__main__':
    main()

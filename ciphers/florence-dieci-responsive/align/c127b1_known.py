#!/usr/bin/env python3
"""A2-FLO3, 3 Oct 2026: known-answer control for the instrument. Enciphers the same two c.111 plain spans with a
random simple substitution over 27 signs (homophones: the 5 vowels get 2 signs each, used at random), runs
tools/interlinear_align.py exactly as on the target, and reports the share of tokens whose aligned letter equals the
true letter, and the same 'agrees' count the target and shuffle control report, over 10 seeds. Optional args: DROP (plain letters deleted at random from line 1, an abbreviation model)
and NOISE (share of signs replaced by a random sign, a reader-error model; the target's two passes split on 17%). If the tool cannot recover a known key at N=120 from a flat start, the target's
real-vs-shuffle tie is a non-test at this N, not evidence against a substitution."""
import csv, random, subprocess, sys, os
HERE = os.path.dirname(os.path.abspath(__file__)); TOOL = os.path.join(HERE, '..', '..', '..', 'tools', 'interlinear_align.py')
DROP = int(sys.argv[1]) if len(sys.argv) > 1 else 0; NOISE = float(sys.argv[2]) if len(sys.argv) > 2 else 0.0
rows = list(csv.DictReader(open(os.path.join(HERE, 'c127b1_pairs.tsv')), delimiter='\t'))
res = []; agr = []
for seed in range(10):
    rng = random.Random(100 + seed); letters = sorted(set(''.join(r['plain_raw'].replace(' ', '') for r in rows)))
    signs = [f's{i}' for i in range(40)]; rng.shuffle(signs); key = {}; k = 0
    for ch in letters:
        n = 2 if ch in 'aeio' else 1; key[ch] = signs[k:k + n]; k += n
    p = f'/tmp/c127_known{seed}.tsv'; truth = []
    with open(p, 'w') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(list(rows[0].keys()))
        for li, r in enumerate(rows):
            pl = r['plain_raw'].replace(' ', ''); keep = sorted(rng.sample(range(len(pl)), len(pl) - (DROP if li == 0 else 0))) if DROP else list(range(len(pl)))
            pl2 = ''.join(pl[i] for i in keep); cs = [rng.choice(key[ch]) if rng.random() >= NOISE else rng.choice(signs[:k]) for ch in pl2]; truth.append(list(pl2))
            w.writerow([r['plain_line'], r['plain_raw'], r['cipher_line'], ' '.join('@' + c for c in cs)])
    a = f'/tmp/c127_known{seed}_a.tsv'
    out = subprocess.run([sys.executable, TOOL, 'align', p, a, f'/tmp/c127_known{seed}_k.tsv', '--code-prefix', '@', '--keep-fs'], capture_output=True, text=True).stdout
    import re; m = re.search(r"'agrees': (\d+)", out); agr.append(int(m.group(1)) if m else 0)
    got = list(csv.DictReader(open(a), delimiter='\t')); ok = tot = 0
    byline = {}
    for g in got: byline.setdefault(g['cipher_line'], []).append(g)
    for li, r in enumerate(rows):
        for i, g in enumerate(byline.get(r['cipher_line'], [])):
            tot += 1; ok += (g['plain_chunk'] == truth[li][i]) if i < len(truth[li]) else 0
    res.append(ok / max(tot, 1))
res.sort(); print(f'drop={DROP} noise={NOISE} known-answer recovery per seed:', ' '.join(f'{x:.2f}' for x in res), f'mean {sum(res)/len(res):.3f}; agrees (target statistic) per seed: {sorted(agr)}')

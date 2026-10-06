"""R11-SURY: score PREREG.md (F1 dots, F2 form) against the interlinear gloss; label-permutation control, 10,000x, seed 1781."""
import csv, random
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith('#')), delimiter='\t')]
tok = {r['tok']: r for r in rd('tokens.tsv')}
key = {r['anon']: r['tok'] for r in rd('anon_key.tsv')}
reads = rd('reads.tsv')
for feat, pred in (('F1', {'D': 'n', 'U': 'm'}), ('F2', {'ij': 'n', 'y': 'm'})):
    rows = [(pred[r[feat]], tok[key[r['anon']]]['gloss'], r['anon'], key[r['anon']]) for r in reads if r[feat] in pred]
    p = [a for a, _, _, _ in rows]; g = [b for _, b, _, _ in rows]; n = len(rows)
    agree = sum(a == b for a, b in zip(p, g)) / n
    random.seed(1781); null = []
    for _ in range(10000):
        h = g[:]; random.shuffle(h); null.append(sum(a == b for a, b in zip(p, h)) / n)
    null.sort(); p99 = null[int(0.99 * len(null)) - 1]; mean = sum(null) / len(null)
    pval = sum(x >= agree for x in null) / len(null)
    print(f'{feat}: readable {n}/21, agreement {agree:.3f}, control mean {mean:.3f} p99 {p99:.3f}, P(null>=obs) {pval:.4f}, '
          f'majority floor {max(g.count("m"), g.count("n")) / n:.3f} -> {"PASS" if agree > p99 and n >= 15 else "FAIL"}')
    for cls in ('m', 'n'):
        sub = [(a, r) for a, b, r, t in rows if b == cls]
        print(f'  gloss {cls}: {len(sub)} tokens, predicted n (dotted/ij) {sum(a == "n" for a, _ in sub)}')
    if feat == 'F1':
        for a, b, an, t in sorted(rows, key=lambda x: x[3]):
            print(f'  {t} {tok[t]["line"]} {tok[t]["word"]:<16} gloss {b} read {"dotted" if a == "n" else "undotted"}')

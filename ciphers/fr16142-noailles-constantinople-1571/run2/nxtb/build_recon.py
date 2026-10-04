"""RUN2-NXTB: reconciled.tsv and focus.tsv from after_rules/ (reconcile_passes.py over passA_rules/passB_rules).
reconciled.tsv: leaf, line, pos, label, grade. H = both blind passes wrote the same label with no '?' and no rule touched it;
M = agreed only after recon_rules.py, or agreed with '?', or the passes split (label 'A|B', both readings kept; not settled
from the image -- that is the sorter's job, TRANSCRIPTION.md). No decode. Rerun: python3 recon_rules.py; reconcile_passes.py
passA_rules.tsv passB_rules.tsv --out-dir after_rules; python3 build_recon.py [--check]."""
import csv, collections, sys
dr = list(csv.DictReader(open('after_rules/ciphertext_draft.tsv'), delimiter='\t'))
dis = {(r['line'], r['col']): r for r in csv.DictReader(open('after_rules/disagreements.tsv'), delimiter='\t')}
rows = []; g = collections.Counter()
for r in dr:
    d = dis.get((r['line'], r['position']))
    if d:
        lab, gr = f"{d['A'] or '-'}|{d['B'] or '-'}", 'M'
    else:
        lab = r['sign'].rstrip('?'); gr = 'H' if (r['confidence'] == 'H' and not r['sign'].endswith('?')) else 'M'
    g[gr] += 1; rows.append((r['line'].split('_')[0][:4], r['line'], r['position'], lab, gr))
out = 'leaf\tline\tpos\tlabel\tgrade\n' + ''.join('\t'.join(x) + '\n' for x in rows)
if '--check' in sys.argv:
    sys.exit(0 if open('reconciled.tsv').read() == out else 'reconciled.tsv is stale')
open('reconciled.tsv', 'w').write(out)
pairs = collections.Counter(); ex = {}
for (l, c), d in dis.items():
    k = tuple(sorted(((d['A'] or '-').rstrip('?'), (d['B'] or '-').rstrip('?'))))
    pairs[k] += 1; ex.setdefault(k, f'{l}:{c}')
with open('focus.tsv', 'w') as f:
    f.write('sign_a\tsign_b\tcolumns_split\texample_line_col\tnote\n')
    for k, v in pairs.most_common():
        note = 'one reader skipped or added a sign (segmentation)' if '-' in k else ('unnamed shape vs table label' if any(x.startswith('?{') for x in k) else 'two table labels')
        f.write(f'{k[0]}\t{k[1]}\t{v}\t{ex[k]}\t{note}\n')
print(dict(g), 'focus pairs', len(pairs)); print(open('focus.tsv').read()[:1500])

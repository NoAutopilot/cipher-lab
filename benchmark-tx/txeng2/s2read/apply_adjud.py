"""TXE2-S2READ steps 3b-4: passZ_S2.tsv = rec/ciphertext_draft.tsv with every adjud_out.tsv row applied (NONE drops the
position), pos renumbered; doubt_S2.tsv beside it = the doubt feed per passZ position, never resolved:
  disagree  passes A and B differed at the position (reconcile_passes disagreements.tsv)
  uncertain agreed but a pass was M/L (uncertain.tsv)
  adjlow    the adjudicator's own conf M/L, or viewed=no
  latt      no input: tx_doubt's latt is a key-lattice decode of the line read, i.e. a decode of f.103r, outside S2-READ's
            rules, and tx_doubt signals has no unit entry for this item (benchmark-tx/txeng/units/README.md); column kept, NA."""
import csv
O = '/home/user/cipher-lab/benchmark-tx/outputs/vivonne1573-f103r-confirm2'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
adj = {(r['line'], int(r['col'])): r for r in rd('adjud_out.tsv')}
q = {(r['line'], int(r['col'])): r['kind'] for r in rd('adjud_queue.tsv')}
assert set(adj) == set(q), (len(adj), len(q), list(set(q) - set(adj))[:5])
out, doubt, changed, none = [], [], 0, 0
pos = {}
for r in rd('rec/ciphertext_draft.tsv'):
    k = (r['line'], int(r['position'])); s = r['sign']; c = r['confidence']
    if k in adj:
        a = adj[k]; ns = a['sign'].strip()
        if ns.upper() == 'NONE':
            none += 1; continue
        if ns != s: changed += 1
        s, c = ns, (a['conf'].strip() or 'M')
    pos[k[0]] = pos.get(k[0], 0) + 1; p = pos[k[0]]
    out.append((k[0], p, s, c))
    kind = q.get(k, '')
    al = int(k in adj and (adj[k]['conf'].strip() in ('M', 'L') or adj[k].get('viewed', '').strip() != 'yes'))
    dis, unc = int(kind == 'disagree'), int(kind == 'uncertain')
    doubt.append((k[0], p, s, dis, unc, al, 'NA', dis + unc + al))
with open(f'{O}/passZ_S2.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\n')
    for x in out: f.write('\t'.join(map(str, x)) + '\n')
with open(f'{O}/doubt_S2.tsv', 'w') as f:
    f.write('line\tpos\tsign\tdisagree\tuncertain\tadjlow\tlatt\tn_signals\n')
    for x in doubt: f.write('\t'.join(map(str, x)) + '\n')
v = sum(1 for r in adj.values() if r.get('viewed', '').strip() == 'yes')
print(f'passZ {len(out)} signs; adjudicated {len(adj)} (viewed yes {v}); changed vs draft {changed}; NONE {none}; '
      f'doubt rows with >=1 signal {sum(1 for x in doubt if x[-1])} ({sum(1 for x in doubt if x[-1])/len(doubt):.1%})')

"""TXE2-VIV102-BASE assembly (copy of ../s2adj/assemble.py, leaf and paths changed; the passZ_S2 comparison dropped):
passZ_dv1.tsv = rec/ciphertext_draft.tsv (the reconciler's aligned draft: passes A and B agreed, or pass A at a split) with the
packets' verdicts applied at the disagree positions (NONE drops the position); agreed-uncertain positions keep the agreed
reading. pos renumbered per line. Writes adjud_out.tsv (per row: packet, A, B, verdict, class A/B/other/NONE, conf, viewed, note)."""
import csv, glob, os
from collections import Counter
O = '/home/user/cipher-lab/benchmark-tx/outputs/vivonne1573-f102r-dev'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
dis = {(r['line'], int(r['col'])): r for r in rd('rec/disagreements.tsv')}
q = [r for r in rd('adjud_queue.tsv') if r['kind'] == 'disagree']
adj = {}
for f in sorted(glob.glob('packets/P*_out.tsv')):
    P = os.path.basename(f)[:3]; pq = rd(f'packets/{P}_queue.tsv'); po = rd(f)
    assert [(r['line'], r['col']) for r in pq] == [(r['line'], r['col']) for r in po], P
    for r in po: adj[(r['line'], int(r['col']))] = dict(r, packet=P)
assert set(adj) == {(r['line'], int(r['col'])) for r in q} == set(dis), 'row sets differ'
cls = {}
for k, a in adj.items():
    s = a['sign'].strip(); A, B = dis[k]['A'], dis[k]['B']
    cls[k] = 'NONE' if s.upper() == 'NONE' else 'A' if s == A else 'B' if s == B else 'other'
out, changed_draft, pos = [], 0, {}
for r in rd('rec/ciphertext_draft.tsv'):
    k = (r['line'], int(r['position'])); s, c = r['sign'], r['confidence']
    if k in adj:
        if cls[k] == 'NONE': continue
        ns = adj[k]['sign'].strip(); changed_draft += ns != s; s, c = ns, adj[k]['conf'].strip() or 'M'
    pos[k[0]] = pos.get(k[0], 0) + 1
    out.append((k[0], pos[k[0]], s, c))
with open(f'{O}/passZ_dv1.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\n')
    for x in out: f.write('\t'.join(map(str, x)) + '\n')
with open('adjud_out.tsv', 'w') as f:
    f.write('line\tcol\tpacket\tA\tB\tverdict\tclass\tconf\tviewed\tnote\n')
    for r in q:
        k = (r['line'], int(r['col'])); a = adj[k]
        f.write('\t'.join([k[0], str(k[1]), a['packet'], dis[k]['A'], dis[k]['B'], a['sign'].strip(), cls[k],
                           a['conf'].strip(), a['viewed'].strip(), (a.get('note') or '').strip()]) + '\n')
cc = Counter(cls.values()); vy = sum(a['viewed'].strip() == 'yes' for a in adj.values())
cf = Counter(a['conf'].strip() for a in adj.values())
print(f'passZ_dv1 {len(out)} signs; disagree rows {len(adj)}, viewed yes {vy}; classes {dict(cc)}; conf {dict(cf)}; '
      f'changed vs draft {changed_draft}')
for P in sorted({a['packet'] for a in adj.values()}):
    c = Counter(cls[k] for k, a in adj.items() if a['packet'] == P)
    v = sum(a['viewed'].strip() == 'yes' for a in adj.values() if a['packet'] == P)
    n = sum(1 for a in adj.values() if a['packet'] == P)
    print(P, c.get('A', 0), c.get('B', 0), c.get('other', 0), c.get('NONE', 0), f'{v}/{n}')
print('not viewed:', [k for k, a in adj.items() if a['viewed'].strip() != 'yes'])

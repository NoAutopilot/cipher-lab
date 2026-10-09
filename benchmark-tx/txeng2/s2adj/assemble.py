"""TXE2-S2ADJ assembly: passZ_S2b.tsv = ../s2read/rec/ciphertext_draft.tsv (the reconciler's aligned draft: passes A and B
agreed, or pass A at a split) with the 13 packets' verdicts applied at the 208 disagree positions (NONE drops the position);
the 167 agreed-uncertain positions keep the agreed reading. pos renumbered per line. passZ_S2.tsv is not touched.
Writes adjud_out.tsv (per row: packet, verdict, class A/B/other/NONE, conf, viewed, note) and prints the counts."""
import csv, glob, os
O = '/home/user/cipher-lab/benchmark-tx/outputs/vivonne1573-f103r-confirm2'
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
dis = {(r['line'], int(r['col'])): r for r in rd('../s2read/rec/disagreements.tsv')}
q = [r for r in rd('../s2read/adjud_queue.tsv') if r['kind'] == 'disagree']
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
out, changed_draft = [], 0
pos = {}
for r in rd('../s2read/rec/ciphertext_draft.tsv'):
    k = (r['line'], int(r['position'])); s, c = r['sign'], r['confidence']
    if k in adj:
        if cls[k] == 'NONE': continue
        ns = adj[k]['sign'].strip(); changed_draft += ns != s; s, c = ns, adj[k]['conf'].strip() or 'M'
    pos[k[0]] = pos.get(k[0], 0) + 1
    out.append((k[0], pos[k[0]], s, c))
with open(f'{O}/passZ_S2b.tsv', 'w') as f:
    f.write('line\tpos\tsign\tconf\n')
    for x in out: f.write('\t'.join(map(str, x)) + '\n')
with open('adjud_out.tsv', 'w') as f:
    f.write('line\tcol\tpacket\tA\tB\tverdict\tclass\tconf\tviewed\tnote\n')
    for r in q:
        k = (r['line'], int(r['col'])); a = adj[k]
        f.write('\t'.join([k[0], str(k[1]), a['packet'], dis[k]['A'], dis[k]['B'], a['sign'].strip(), cls[k],
                           a['conf'].strip(), a['viewed'].strip(), a.get('note', '').strip()]) + '\n')
# vs passZ_S2 (same draft, earlier adjudication): compare at the 208 positions
old = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd('../s2read/adjud_out.tsv')}
diff = sum(1 for k in adj if old[k] != adj[k]['sign'].strip())
from collections import Counter
cc = Counter(cls.values()); vy = sum(a['viewed'].strip() == 'yes' for a in adj.values())
cf = Counter(a['conf'].strip() for a in adj.values())
z = rd(f'{O}/passZ_S2.tsv')
print(f'passZ_S2b {len(out)} signs (passZ_S2 {len(z)}); disagree rows {len(adj)}, viewed yes {vy}; classes {dict(cc)}; '
      f'conf {dict(cf)}; changed vs draft {changed_draft}; verdict differs from passZ_S2 adjudication at {diff} of 208 '
      f'(old NONE {sum(v.upper()=="NONE" for v in old.values())} incl. uncertain rows)')
nv = [k for k, a in adj.items() if a['viewed'].strip() != 'yes']
print('not viewed:', nv)

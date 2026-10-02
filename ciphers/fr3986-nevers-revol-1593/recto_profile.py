#!/usr/bin/env python3
"""Sign-frequency profile of the f.198 recto pass A (GAPS4, 2 Oct 2026) against the verso v2 draft
(ciphertext_v2.tsv, 55 signs) and the 264ext atlas inventory (tools/keys/key60_atlas/atlas264*.tsv).
Writes recto_profile.txt; --check exits 1 if the committed file is stale."""
import csv, sys, os, collections
H = os.path.dirname(os.path.abspath(__file__)); R = os.path.join(H, '..', '..')
def rows(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))
rec = [r['tag'].strip() for r in rows(os.path.join(H, 'passes/recto/passA.tsv'))]
conf = collections.Counter(r['confidence'].strip() for r in rows(os.path.join(H, 'passes/recto/passA.tsv')))
ver = [r['sign'].strip() for r in rows(os.path.join(H, 'ciphertext_v2.tsv'))]
atl = set()
for f in ('atlas264.tsv', 'atlas264ext.tsv'):
    atl |= {r['tag'].strip() for r in rows(os.path.join(R, 'tools/keys/key60_atlas', f))}
key = {r['sign'].strip() for r in rows(os.path.join(R, 'tools/keys/key60.tsv'))}
rc, vc = collections.Counter(rec), collections.Counter(ver)
new = [t for t in rec if t.startswith('NEW')]
out = []
p = out.append
p(f'recto pass A: {len(rec)} signs, {len(rc)} distinct tags; confidence {dict(sorted(conf.items()))}')
p(f'  NEW (no atlas/key shape fits): {len(new)} tokens ({100*len(new)/len(rec):.1f}%), {len(set(new))} distinct')
inA = sum(n for t, n in rc.items() if t in atl); inK = sum(n for t, n in rc.items() if t in key)
p(f'  tokens whose tag is an atlas exemplar tag: {inA}/{len(rec)} = {100*inA/len(rec):.1f}% '
  f'({len([t for t in rc if t in atl])} of {len(atl)} atlas tags used)')
p(f'  tokens whose tag is a key60 tag: {inK}/{len(rec)} = {100*inK/len(rec):.1f}%; not key60 and not NEW: '
  f'{len(rec)-inK-len(new)} ({sorted({t for t in rc if t not in key and not t.startswith("NEW")})})')
p(f'verso v2: {len(ver)} signs, {len(vc)} distinct; in atlas tags {sum(n for t,n in vc.items() if t in atl)}/{len(ver)}')
sh = set(rc) & set(vc)
p(f'shared distinct tags recto/verso: {len(sh)} ({sorted(sh)}); verso tokens covered by recto tag set: '
  f'{sum(vc[t] for t in sh)}/{len(ver)}')
# frequency correlation over the union of non-NEW tags (rank profile)
U = sorted((set(rc) | set(vc)) - {t for t in rc if t.startswith('NEW')})
import math
a = [rc[t]/len(rec) for t in U]; b = [vc[t]/len(ver) for t in U]
ma, mb = sum(a)/len(a), sum(b)/len(b)
r = sum((x-ma)*(y-mb) for x, y in zip(a, b)) / math.sqrt(sum((x-ma)**2 for x in a)*sum((y-mb)**2 for y in b))
p(f'Pearson r of tag relative frequencies, recto vs verso, over {len(U)} tags: {r:.4f} (verso N=55: weak test)')
p('matched comparison, same atlas sheet and tag list, blind Sonnet passes (tokens on atlas tags / key60 tags / NEW or described / H-confidence):')
for lab, f in [('leaf 298 office hand, passD (instrument read 65/65)', 'atlas_heldout/heldout298_passD.tsv'),
               ('f.198 verso passA (GAPS3, agreement 36%)', 'passes/v2/passA.tsv'),
               ('f.198 verso passB (GAPS3)', 'passes/v2/passB.tsv'),
               ('f.198 recto passA (this step)', 'passes/recto/passA.tsv')]:
    R = rows(os.path.join(H, f)); t = [x['tag'].strip() for x in R]
    nw = sum(1 for x in t if x.startswith('NEW') or x.startswith('<'))
    hh = sum(1 for x in R if x['confidence'].strip() == 'H')
    p(f'  {lab}: N={len(t)} atlas {100*sum(x in atl for x in t)/len(t):.1f}% key {100*sum(x in key for x in t)/len(t):.1f}% '
      f'new {100*nw/len(t):.1f}% H {100*hh/len(t):.1f}%')
p('top 15 recto tags (count, in atlas?, verso count):')
for t, n in rc.most_common(15):
    p(f'  {t}\t{n}\t{"atlas" if t in atl else ("key" if t in key else "-")}\t{vc.get(t,0)}')
p('top 10 verso tags: ' + ', '.join(f'{t} {n}' for t, n in vc.most_common(10)))
p('NEW shapes: ' + '; '.join(f'{t[4:]} x{n}' for t, n in collections.Counter(new).most_common()))
txt = '\n'.join(out) + '\n'
fp = os.path.join(H, 'recto_profile.txt')
if '--check' in sys.argv:
    ok = open(fp).read() == txt; print('profile up to date' if ok else 'STALE'); sys.exit(0 if ok else 1)
open(fp, 'w').write(txt); print(txt)

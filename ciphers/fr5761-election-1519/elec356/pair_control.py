#!/usr/bin/env python3
"""ELEC-356 shuffled-name control: ELEC-PAIR's pre-registered rule 4 unchanged, run over the pooled both-sided slots of
nr. 357 (../elecpair/pairs.tsv) and nr. 356 (pairs.tsv here), as PREREG-ELEC-356.md states. Permutes the printed names over the
pooled slots 1000 times (seed 357) and reports, per sign with >= 2 pooled pairs, the share of permutations in which the sign still
reads one name at every slot; also the nr. 356-only figures. Names normalised (Bohemia=Boheme, Saxonia=Saxe; roy prefix dropped).
--check compares with the committed control_result.tsv."""
import csv, random, sys, collections, os
here = os.path.dirname(os.path.abspath(__file__))
NORM = {'roy tres-chrestien': 'roy tres-chrestien', 'roy catholique': 'roy catholique'}
def load(p, src):
    out = []
    for r in csv.DictReader(open(p), delimiter='\t'):
        if r['pair'] == 'both':
            out.append((r['sign'], NORM.get(r['printed_name'], r['printed_name']), src))
    return out
rows = load(os.path.join(here, '..', 'elecpair', 'pairs.tsv'), '357') + load(os.path.join(here, 'pairs.tsv'), '356')
def run(rows, tag):
    signs = [s for s, _, _ in rows]; names = [n for _, n, _ in rows]
    cnt = collections.Counter(signs); C = sorted(s for s in cnt if cnt[s] >= 2)
    cons = lambda nm, s: len({n for g, n in zip(signs, nm) if g == s}) == 1
    rng = random.Random(357); N = 1000; per = collections.Counter()
    for _ in range(N):
        nm = names[:]; rng.shuffle(nm)
        for s in C:
            if cons(nm, s): per[s] += 1
    out = [f"{tag}_slots\t{len(rows)}"]
    for s in C:
        nset = sorted({n for g, n in zip(signs, names) if g == s})
        out.append(f"{tag}\t{s}\tpairs={cnt[s]}\tnames={'|'.join(nset)}\treal_consistent={len(nset)==1}\tshuffle_consistent={per[s]}/{N}")
    return out
txt = "\n".join(run(rows, 'pooled') + run([r for r in rows if r[2] == '356'], 'nr356')) + "\n"
res = os.path.join(here, 'control_result.tsv')
if '--check' in sys.argv:
    sys.exit(0 if open(res).read() == txt else 1)
open(res, 'w').write(txt); print(txt, end='')

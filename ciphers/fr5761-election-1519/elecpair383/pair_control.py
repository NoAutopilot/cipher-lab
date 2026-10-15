#!/usr/bin/env python3
"""ELEC-KLU (nr. 383) copy of the ELEC-PAIR shuffled-name control (pre-registered rule 4, NOTES "## ELEC-PAIR").
Reads elecpair/pairs.tsv (sign label, printed name, both-sided pair), permutes the printed names over the
paired slots N times, and reports the share of permutations under which every C-graded sign (>= 2 pairs)
still reads one name at all its slots. Also per sign. Seeded; --check compares with the committed result."""
import csv, random, sys, collections, os
here = os.path.dirname(os.path.abspath(__file__))
rows = [r for r in csv.DictReader(open(os.path.join(here, 'pairs.tsv')), delimiter='\t') if r['pair'] == 'both']
signs = [r['sign'] for r in rows]; names = [r['printed_name'] for r in rows]
cnt = collections.Counter(signs); C = [s for s in cnt if cnt[s] >= 2]
def consistent(nm, s): return len({n for g, n in zip(signs, nm) if g == s}) == 1
real = {s: consistent(names, s) for s in C}
rng = random.Random(383); N = 1000; allok = 0; per = collections.Counter()
for _ in range(N):
    nm = names[:]; rng.shuffle(nm); ok = True
    for s in C:
        if consistent(nm, s): per[s] += 1
        else: ok = False
    allok += ok
out = [f"slots\t{len(rows)}", f"C_candidates\t{','.join(sorted(C))}",
       f"real_all_consistent\t{all(real.values())}", f"shuffle_all_consistent\t{allok}/{N}"]
out += [f"shuffle_consistent_{s}\t{per[s]}/{N}" for s in sorted(C)]
txt = "\n".join(out) + "\n"
res = os.path.join(here, 'control_result.tsv')
if '--check' in sys.argv:
    sys.exit(0 if open(res).read() == txt else 1)
open(res, 'w').write(txt); print(txt, end='')

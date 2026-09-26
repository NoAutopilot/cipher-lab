#!/usr/bin/env python3
"""AX-NAMES2 step 6 caveat: for every code key_full.tsv reads NULL, count the aligner's raw occurrences (axnames/occ_*.tsv,
all four aligned letters, before build_names.py's cluster filter) that absorbed nothing vs absorbed 1-5 letters vs 6+
letters (6+ is typically a transcription gap swallowed by the free code). Writes axnames/null_raw.tsv."""
import csv, glob, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE)
key = {r['code']: r for r in csv.DictReader(open(os.path.join(TGT, 'key_full.tsv')), delimiter='\t')}
nulls = [c for c, r in key.items() if r['value'] == 'NULL']
cnt = collections.defaultdict(lambda: [0, 0, 0, []])
for p in sorted(glob.glob(os.path.join(HERE, 'occ_*.tsv'))):
    for r in csv.DictReader(open(p), delimiter='\t'):
        if r['code'] not in nulls:
            continue
        a = r['absorbed']; c = cnt[r['code']]
        i = 0 if not a else (1 if len(a) <= 5 else 2)
        c[i] += 1
        if i == 1:
            c[3].append(f"{r['letter']} {r['line']}:{r['pos']} '{a}'")
with open(os.path.join(HERE, 'null_raw.tsv'), 'w') as f:
    f.write('code\tkey_full_grade\tempty\tabsorbed_1to5\tabsorbed_6plus\tshort_cases\n')
    for c in sorted(nulls, key=int):
        e, s, l, ex = cnt[c]
        f.write(f"{c}\t{key[c]['grade']}\t{e}\t{s}\t{l}\t{'; '.join(ex)}\n")
tot = [sum(cnt[c][i] for c in nulls) for i in range(3)]
print(f'NULL codes {len(nulls)}: raw occurrences empty {tot[0]}, absorbed 1-5 letters {tot[1]}, 6+ letters {tot[2]}')

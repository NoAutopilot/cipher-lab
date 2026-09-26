#!/usr/bin/env python3
"""AX-NAMES2 step 7: every sign still graded U under key_full.tsv across the 1574-table letters (4613/4615 siblings,
4610, 4611, 4616, 4503, 5810, 5811, 5797 spots), with count and up to four contexts, sorted by count. Decodes to a
temp dir (the jobs of decode.json / decode_wv2.json / decode_5797.json with the key swapped); writes
axnames/still_unread.tsv for AX-GLOSS."""
import collections, csv, json, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(TGT))
JOBS = [('decode.json', 'ciphertext_sib.tsv'), ('decode.json', 'ciphertext_4610.tsv'), ('decode.json', 'ciphertext_4611.tsv'),
        ('decode.json', 'ciphertext_4616.tsv'), ('decode_wv2.json', 'ciphertext_4503.tsv'),
        ('decode_wv2.json', 'ciphertext_5810.tsv'), ('decode_wv2.json', 'ciphertext_5811.tsv'),
        ('decode_5797.json', 'ciphertext_5797.tsv')]
agg = collections.defaultdict(list)
with tempfile.TemporaryDirectory() as tmp:
    for cfg, ct in JOBS:
        job = next(j for j in json.load(open(os.path.join(TGT, cfg)))['jobs'] if j['ciphertext'] == ct)
        tok = os.path.join(tmp, ct + '.tok')
        job = dict(job, key='key_full.tsv', reading=os.path.join(tmp, ct + '.txt'), tokens=tok)
        c = os.path.join(tmp, ct + '.json'); json.dump({'target': 'x', 'jobs': [job]}, open(c, 'w'))
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools/decode_key.py'), TGT, '--config', c], check=True,
                       stdout=subprocess.DEVNULL)
        rows = list(csv.reader(open(tok), delimiter='\t'))[1:]
        letter = ct.replace('ciphertext_', '').replace('.tsv', '')
        for i, r in enumerate(rows):
            if r[-1] != 'U':
                continue
            win = ' '.join(('<' + x[2] + '>' if j == i else ('' if x[-2] == 'NULL' else x[-2]))
                           for j, x in enumerate(rows) if abs(j - i) <= 6 and x[0] == r[0])
            agg[r[2]].append((letter, r[0], ' '.join(win.split())))
out = ['code\tcount\tletters\tcontexts (first 4; NULLs dropped, <code> = this sign)']
for code, occ in sorted(agg.items(), key=lambda kv: (-len(kv[1]), kv[0])):
    letters = ','.join(sorted({o[0] for o in occ}))
    out.append(f"{code}\t{len(occ)}\t{letters}\t" + ' | '.join(f'{o[0]} {o[1]}: {o[2]}' for o in occ[:4]))
open(os.path.join(HERE, 'still_unread.tsv'), 'w').write('\n'.join(out) + '\n')
print(f'{len(agg)} distinct U signs, {sum(len(v) for v in agg.values())} U tokens')

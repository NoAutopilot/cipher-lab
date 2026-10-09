#!/usr/bin/env python3
"""MONLUC-BLIND (9 Oct 2026): rebuild the scratch target for `decode_key.py --try K69=...` from the blind sort.

Usage: python3 blind_try.py OUTDIR [--group B] [--drop-k38] [--try K69=t]

Reads blind_k07_sort.tsv (the pre-registered form-A group is the blind group holding most prevA=1 crops), relabels
the c268 tokens in that group as K69 in a copy of ciphertext_c268.tsv under OUTDIR (with key.tsv and a one-job
decode.json), and runs tools/decode_key.py OUTDIR --try. key.tsv in this folder is never written.
"""
import argparse, collections, json, shutil, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument('outdir'); ap.add_argument('--group'); ap.add_argument('--drop-k38', action='store_true')
ap.add_argument('--try', dest='hyp', default='K69=t'); a = ap.parse_args()
rows = [l.split('\t') for l in (HERE / 'blind_k07_sort.tsv').read_text().splitlines() if l[:1].isdigit()]
cnt = collections.Counter(r[8] for r in rows if r[7] == '1')
top = cnt.most_common(2)
if a.group is None and len(top) > 1 and top[0][1] == top[1][1]:
    sys.exit('tie for form A: undecided (pre-registration), --try not run')
grp = a.group or top[0][0]
sel = {(r[2], r[3]) for r in rows if r[1] == 'c268' and r[8] == grp and not (a.drop_k38 and r[4] == 'K38')}
out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
shutil.copy(HERE / 'key.tsv', out / 'key.tsv')
lines = (HERE / 'ciphertext_c268.tsv').read_text().splitlines()
res = [lines[0]] + ['\t'.join([f[0], f[1], 'K69'] + f[3:]) if (f[0], f[1]) in sel else l
                    for l in lines[1:] if l for f in [l.split('\t')]]
(out / 'ciphertext_c268.tsv').write_text('\n'.join(res) + '\n')
json.dump({"jobs": [{"ciphertext": "ciphertext_c268.tsv", "format": "tsv", "key": "key.tsv", "reading": "reading.txt",
                     "tokens": "reading_tokens.tsv", "style": "spaced", "unkeyed_value": "?",
                     "token_columns": [["line", "line"], ["pos", "pos"], ["sign", "raw"], ["value", "value"], ["grade", "grade"]]}]},
          open(out / 'decode.json', 'w'))
print(f'form A = blind group {grp} (prevA counts {dict(cnt)}); relabelled {len(sel)} c268 tokens', flush=True)
sys.exit(subprocess.call([sys.executable, str(HERE.parents[1] / 'tools' / 'decode_key.py'), str(out), '--try', a.hyp]))

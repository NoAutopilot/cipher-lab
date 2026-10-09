#!/usr/bin/env python3
"""MONLUC-CURL (9 Oct 2026): rebuild a scratch f.86 (c172) target from the binary curl sort and run decode_key.py --try.

Usage: python3 f86_curl_try.py OUTDIR [--try K69=t] [--with-k38] [--control CODE]
--control CODE (known-answer control, added after the target --try, not pre-registered): relabel EVERY occurrence of a
table code whose value the gloss confirms as K69 instead, then --try K69=<its table value>: does --try find it on this decode?
Relabels the f.86 K07 tokens answered Y in f86_curl_answers.tsv as K69 in a copy of ciphertext_c172.tsv under OUTDIR (with key.tsv
and a one-job decode.json) and runs tools/decode_key.py OUTDIR --try. --with-k38 also relabels the K38 token answered Y.
key.tsv and ciphertext_c172.tsv in this folder are never written.
"""
import argparse, json, shutil, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ap = argparse.ArgumentParser(); ap.add_argument('outdir'); ap.add_argument('--try', dest='hyp', default='K69=t')
ap.add_argument('--with-k38', action='store_true'); ap.add_argument('--control'); a = ap.parse_args()
rows = [l.split('\t') for l in (HERE / 'f86_curl_answers.tsv').read_text().splitlines() if l.startswith('L')]
sel = {(r[0], r[1]) for r in rows if r[4] == 'Y' and (r[2] == 'K07' or (a.with_k38 and r[2] == 'K38'))}
if a.control:
    sel = {(f[0], f[1]) for l in (HERE / 'ciphertext_c172.tsv').read_text().splitlines()[1:] if l for f in [l.split('\t')] if f[2] == a.control}
out = Path(a.outdir); out.mkdir(parents=True, exist_ok=True)
shutil.copy(HERE / 'key.tsv', out / 'key.tsv')
lines = (HERE / 'ciphertext_c172.tsv').read_text().splitlines()
res = [lines[0]] + ['\t'.join([f[0], f[1], 'K69'] + f[3:]) if (f[0], f[1]) in sel else l
                    for l in lines[1:] if l for f in [l.split('\t')]]
(out / 'ciphertext_c172.tsv').write_text('\n'.join(res) + '\n')
json.dump({"jobs": [{"ciphertext": "ciphertext_c172.tsv", "format": "tsv", "key": "key.tsv", "reading": "reading.txt",
                     "tokens": "reading_tokens.tsv", "style": "spaced", "unkeyed_value": "?",
                     "token_columns": [["line", "line"], ["pos", "pos"], ["sign", "raw"], ["value", "value"], ["grade", "grade"]]}]},
          open(out / 'decode.json', 'w'))
print(f'relabelled {len(sel)} c172 tokens K69', flush=True)
sys.exit(subprocess.call([sys.executable, str(HERE.parents[1] / 'tools' / 'decode_key.py'), str(out), '--try', a.hyp]))

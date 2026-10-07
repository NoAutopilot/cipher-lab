#!/usr/bin/env python3
"""MONLUC-2 (7 Oct 2026): batch-0507 step 2, the judge's positive control at increasing N from glossed material.

  python3 judge_n_c172.py [--check]

Positive control = the f.86 (c172) decode with key.tsv (Tomokiyo's table, unchanged), the only gloss-confirmed decode
in hand (score_c172.py 0.640 vs shuffle max 0.347 against gloss+line 1). It is judged by tools/judge_plaintext.py
(spec fr4735-monluc-lansac-poland-1573, fr16) on prefixes of N = 50, 100 and all letters, beside the leaf's own gloss
(+ clear line 1) at the same N as the judge's sanity row. The brief: find the N at which the positive control
PASSes; only then decode that many c268 signs. The glossed material in hand ends at ~147 letters, so N cannot grow
past it. Writes results_judge_n_c172.json; --check exits 1 if stale (rule 7).
"""
import json, subprocess, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SPEC = ROOT / 'specs' / 'fr4735-monluc-lansac-poland-1573.json'
sys.path.insert(0, str(HERE))
from score_c172 import norm, load_key  # noqa: E402
from check_cells import load_lines  # noqa: E402


def judge(text):
    r = subprocess.run([sys.executable, str(ROOT / 'tools' / 'judge_plaintext.py'), str(SPEC), '--text', text, '--json'],
                       capture_output=True, text=True)
    j = json.loads(r.stdout)
    l = j['checks']['language']
    return dict(pass_=j['pass'], language=l['score'], real_p05=l['real_p05'], null_p99=l['null_p99'],
                words=j['checks']['words']['cover'])


key = load_key()
lines = load_lines()
dec = norm(''.join(key.get(t, '') for L in sorted(lines) for t in lines[L]))
gl = norm((HERE / 'gloss_c172_withline1.txt').read_text().split('\n#', 1)[0])
rows = []
for n in (50, 100, len(dec)):
    rows.append(dict(N=min(n, len(dec)), decode=judge(dec[:n]), gloss=judge(gl[:n])))
res = dict(decoded_letters=len(dec), gloss_letters=len(gl), rows=rows,
           positive_control_passes_at=[r['N'] for r in rows if r['decode']['pass_']],
           verdict='judge untestable at this N' if not any(r['decode']['pass_'] for r in rows) else 'calibrated')
js = json.dumps(res, indent=1) + '\n'
out = HERE / 'results_judge_n_c172.json'
if '--check' in sys.argv:
    ok = out.exists() and out.read_text() == js
    print(('OK ' if ok else 'STALE ') + out.name)
    sys.exit(0 if ok else 1)
out.write_text(js)
print(js)

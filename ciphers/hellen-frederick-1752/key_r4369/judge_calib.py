#!/usr/bin/env python3
"""Judge calibration for the R4369 decode (READ2-HEL, 3 Oct 2026): real fr18 prose encoded with key_LR100.tsv
(test_sibling.synth_stream), decoded back with the same key, uncovered words dropped as the target's unkeyed tokens
are, in windows of R1953's token count (846); each window goes through tools/judge_plaintext.py with the target's spec.
Shows whether a TRUE decode at this key's coverage can pass the judge at all. Usage: python3 judge_calib.py [--n 10]"""
import os, sys, random, subprocess, re
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(T))
sys.path.insert(0, os.path.join(T, 'sibling_michell'))
import test_sibling as ts
n = int(sys.argv[sys.argv.index('--n') + 1]) if '--n' in sys.argv else 10
key = {c: v for c, v in ts.load_key(os.path.join(HERE, 'key_LR100.tsv')).items() if v.strip()}
rng = random.Random(1); stream = ts.synth_stream(key, rng)
for i in range(n):
    j = rng.randrange(0, len(stream) - 846); win = stream[j:j + 846]
    cov = sum(t in key for t in win)
    txt = ' '.join(key[t] for t in win if t in key)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools/judge_plaintext.py'), os.path.join(ROOT, 'specs/hellen-frederick-1752.json'),
                        '--text', txt], capture_output=True, text=True).stdout
    m = re.search(r'(ok|FAIL)\s+language: score=(\S+), null_p99=(\S+), real_p05=(\S+)', r)
    print(f'window {i}\tcovered {cov}/846\t' + (' '.join(m.groups()) if m else r.strip().splitlines()[-1]))

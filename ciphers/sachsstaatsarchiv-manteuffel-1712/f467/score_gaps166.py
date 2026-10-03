#!/usr/bin/env python3
"""GAPS166 (3 Oct 2026): score f.467's period gloss (gloss.txt = G) and its period plaintext (c2.txt = C2) through the
same fr18 judge as f.410's keyed decode, per f467/PREREG-GAPS166.md. Length matching: L = min(letters(G or C2), 263);
the f.410 candidate is scored on every contiguous L-letter window (step 10) when L < 263. Also: G/C2 letter-shuffled
(20 seeds, null sanity) and the 20 f.410 shuffled-key decodes re-scored. Writes f467/score.tsv. --check: exit 1 if
score.tsv differs from a fresh run."""
import json, os, random, re, statistics, subprocess, sys, tempfile
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
SPEC = os.path.join(R, 'specs', 'sachsstaatsarchiv-manteuffel-1712.json')
def letters(s): return re.sub('[^a-z]', '', s.lower())
def judge_text(s):
    with tempfile.NamedTemporaryFile('w', suffix='.txt', delete=False) as f: f.write(s); p = f.name
    o = subprocess.run([sys.executable, os.path.join(R, 'tools', 'judge_plaintext.py'), SPEC, '--file', p, '--json'],
                       capture_output=True, text=True); os.unlink(p)
    d = json.loads(o.stdout)['checks']['language']
    return d['score'], d['real_p05'], d['null_p99']
def row(name, s):
    sc, p05, n99 = judge_text(s); return (name, len(letters(s)), sc, p05, n99, round(sc - p05, 3))
cand = letters(open(os.path.join(T, 'f410', 'candidate.txt')).read())
rows = []
for nm in ('gloss', 'c2'):
    t = letters(open(os.path.join(H, nm + '.txt')).read())
    if len(t) < 40: rows.append((nm, len(t), 'NA', 'NA', 'NA', 'NA')); continue
    rows.append(row(nm, t))
    for i in range(20):
        l = list(t); random.Random(i).shuffle(l); rows.append(row(f'{nm}_lettershuf_{i:02d}', ''.join(l)))
    L = min(len(t), len(cand))
    if L < len(cand):
        w = [row(f'cand_win{L}_{s:03d}', cand[s:s + L]) for s in range(0, len(cand) - L + 1, 10)]
        rows += w
rows.append(row('candidate_full', cand))
for i in range(20):
    rows.append(row(f'shufkey_{i:02d}', letters(open(os.path.join(T, 'f410', f'shuffled_{i:02d}.txt')).read())))
out = 'text\tletters\tscore\treal_p05\tnull_p99\tmargin\n' + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
sp = os.path.join(H, 'score.tsv')
if '--check' in sys.argv:
    ok = os.path.exists(sp) and open(sp).read() == out
    print('score.tsv up to date' if ok else 'score.tsv STALE'); sys.exit(0 if ok else 1)
open(sp, 'w').write(out); print(out)

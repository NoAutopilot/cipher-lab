#!/usr/bin/env python3
"""GAPS177 (3 Oct 2026, copy of f410/judge_f410.py with the line filter changed): build the f.409v + upper f.410 judge candidate from reading_tokens.tsv (keyed tokens only, first alternative of an
M value, U dropped) and N shuffled-key controls (key values permuted among the key's codes, same tokens, same rule), then
run tools/judge_plaintext.py on each. Writes f409v/candidate.txt, f409v/shuffled_NN.txt and f409v/judge.tsv. --check: exit 1 if
candidate.txt differs from what reading_tokens.tsv gives now."""
import csv, json, random, subprocess, sys, os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H); R = os.path.dirname(os.path.dirname(T))
toks = [r for r in csv.DictReader(open(os.path.join(T, 'reading_tokens.tsv')), delimiter='\t') if ('_0511_f409v_' in r['line'] or '_0511_f410u_' in r['line'])]
key = {r['code']: r['value'] for r in csv.DictReader(open(os.path.join(T, 'key.tsv')), delimiter='\t') if r['value']}
def text(k):
    out, line, cur = [], None, []
    for t in toks:
        if t['line'] != line:
            if cur: out.append(' '.join(cur))
            line, cur = t['line'], []
        v = k.get(t['sign'])
        if v: cur.append(v.split('|')[0])
    if cur: out.append(' '.join(cur))
    return '\n'.join(out) + '\n'
cand = text(key)
cp = os.path.join(H, 'candidate.txt')
if '--check' in sys.argv:
    ok = os.path.exists(cp) and open(cp).read() == cand
    print('candidate up to date' if ok else 'candidate STALE'); sys.exit(0 if ok else 1)
open(cp, 'w').write(cand)
spec = os.path.join(R, 'specs', 'sachsstaatsarchiv-manteuffel-1712.json')
def judge(path):
    o = subprocess.run([sys.executable, os.path.join(R, 'tools', 'judge_plaintext.py'), spec, '--file', path, '--json'],
                       capture_output=True, text=True)
    return json.loads(o.stdout)
rows = [('candidate', judge(cp))]
codes, vals = list(key), list(key.values())
for i in range(int(os.environ.get('NSHUF', 20))):
    rnd = random.Random(i); v = vals[:]; rnd.shuffle(v)
    p = os.path.join(H, f'shuffled_{i:02d}.txt'); open(p, 'w').write(text(dict(zip(codes, v)))); rows.append((f'shuffled_{i:02d}', judge(p)))
with open(os.path.join(H, 'judge.tsv'), 'w') as f:
    f.write('text\tverdict\tscore\treal_p05\tnull_p99\n')
    for n, j in rows:
        d = j['checks'].get('language', {})
        f.write(f"{n}\t{'PASS' if j['pass'] else 'FAIL'}\t{d.get('score')}\t{d.get('real_p05')}\t{d.get('null_p99')}\n")
print(open(os.path.join(H, 'judge.tsv')).read())

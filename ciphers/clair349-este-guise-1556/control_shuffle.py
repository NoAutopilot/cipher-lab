#!/usr/bin/env python3
"""Matched control for the judge (ZX-DEC349 step 4, 25 Sept 2026): the same decoded token values (reading_tokens.tsv,
the key plus exceptions, nulls dropped, homographs at their first value, unread as '·') shuffled within each line,
dividers left where they are, 5 seeds; each rendered in reading.txt's concat layout and judged with
tools/judge_plaintext.py on the same spec. Same letters, same line lengths, same word-break count: only the order
differs, so a PASS on the target and FAIL on the controls says the order carries French, not the letter mix.
Usage: python3 control_shuffle.py [--seeds 5] [--lines 18-33]
--lines (ZX-TR349E, 25 Sept 2026) judges only that line range, target and controls alike."""
import collections, csv, json, os, random, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.join(HERE, '..', '..')
SPEC = os.path.join(ROOT, 'specs', 'clair349-este-guise-1556.json')


def lines():
    ct = list(csv.DictReader(open(os.path.join(HERE, 'ciphertext.tsv'), encoding='utf-8'), delimiter='\t'))
    val = {(t['line'], t['pos']): t for t in csv.DictReader(open(os.path.join(HERE, 'reading_tokens.tsv'),
                                                                   encoding='utf-8'), delimiter='\t')}
    L = collections.OrderedDict()
    for r in ct:
        if r['sign'] == '|':
            L.setdefault(r['line'], []).append(None); continue
        t = val[(r['line'], r['position'])]
        v = t['value'].split('|')[0]
        v = '' if v == 'NULL' else ('·' if t['grade'] == 'U' else v)
        L.setdefault(r['line'], []).append(v)
    return L


def render(L):
    return '\n'.join(ln + ' | ' + ''.join(' ' if v is None else (f'[{v}]' if len(v) > 1 else v) for v in toks)
                     for ln, toks in L.items()) + '\n'


def judge(text, tag):
    p = os.path.join('/tmp', f'clair349_ctl_{tag}.txt')
    open(p, 'w').write(text)
    r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'judge_plaintext.py'), SPEC, '--file', p, '--json'],
                       capture_output=True, text=True)
    os.remove(p)
    return json.loads(r.stdout)


if __name__ == '__main__':
    n = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 5
    L = lines()
    if '--lines' in sys.argv:
        a, b = map(int, sys.argv[sys.argv.index('--lines') + 1].split('-'))
        L = collections.OrderedDict((k, v) for k, v in L.items() if a <= int(k) <= b)
    t = judge(render(L), 'target')
    print('target (unshuffled, same renderer):', 'PASS' if t['pass'] else 'FAIL', json.dumps(t['checks']))
    for s in range(n):
        rnd = random.Random(s); M = collections.OrderedDict()
        for ln, toks in L.items():
            vals = [v for v in toks if v is not None]; rnd.shuffle(vals); it = iter(vals)
            M[ln] = [None if v is None else next(it) for v in toks]
        c = judge(render(M), f's{s}')
        print(f'control seed {s}:', 'PASS' if c['pass'] else 'FAIL', json.dumps(c['checks']))

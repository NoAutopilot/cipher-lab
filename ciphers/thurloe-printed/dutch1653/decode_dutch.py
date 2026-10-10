#!/usr/bin/env python3
"""Decode the Birch vol 1 Dutch 1653 cipher runs under the printed De Witt key (Brieven van Johan de Witt I, ed. Japikse, p.72).

  python3 decode_dutch.py [NAME ...]          write reading_<name>.tsv (default: every name in NAMES; NAME = p351, p301, ...)
  python3 decode_dutch.py [NAME ...] --check  exit 1 if any committed reading is stale
NAMES: ct_p351, ct_p339, ct_p308, ct_p435 (DUTCH-KEY); ct_p301, ct_p418 (DUTCH-MORE, 10 Oct 2026).

Grades (rule 4): H = a key-stated value (codes 1-66 of the printed table) on a token both transcription passes agree on;
M = a token whose transcription is doubtful (pass disagreement settled by eye, flag column) or a code above 66 (name/country
code, outside the printed key, left unread as [code]).
p.435 (Boreel) is decoded only as the control's input: the key fails its own control there (gate_dutchkey.json "p435"),
so every p.435 token is graded '-' (not read), never H.
DUTCH-MORE (PREREG-DUTCHMORE.md): p.418 likewise '-' (its fold does not beat the control max); p.301 capped at M (non-test at N=10).
"""
import csv, os, sys
H = os.path.dirname(os.path.abspath(__file__))
NAMES = ['p351', 'p339', 'p308', 'p435', 'p301', 'p418']
NOT_READ = {'p435', 'p418'}  # p.418: fold does not beat its control max (dutchmore_score.json), not read
CAP_M = {'p301'}  # p.301: fold non-test at N=10 (power 0.62); reading rests on the English context only, graded M

def key():
    return {int(r['code']): r['letter'] for r in csv.DictReader(open(os.path.join(H, 'key_dewitt_1653.tsv')), delimiter='\t')}

def runs(name):
    out = {}
    for r in csv.DictReader(open(os.path.join(H, f'ct_{name}.tsv')), delimiter='\t'):
        out.setdefault((r['page'], int(r['run'])), []).append(r)
    return out

def decode(name, K=None):
    K = K or key()
    rows = []
    for (page, run), toks in runs(name).items():
        for r in toks:
            c = int(r['token'])
            if c in K:
                val, g = K[c], ('H' if r['flag'] == 'agree' else 'M')
            else:
                val, g = f'[{c}]', 'M'
            if name in CAP_M: g = 'M'
            if name in NOT_READ: g = '-'
            rows.append((page, str(run), r['pos'], r['token'], val, g))
    return rows

def text(rows):
    lines = ['page\trun\tpos\ttoken\tvalue\tgrade']
    lines += ['\t'.join(r) for r in rows]
    by = {}
    for p, run, _, _, v, _ in rows:
        by.setdefault((p, run), []).append(v if len(v) == 1 else ' ' + v + ' ')
    lines.append('')
    for (p, run), vs in by.items():
        lines.append(f'# p.{p} run {run}: ' + ''.join(vs).strip())
    return '\n'.join(lines) + '\n'

def main():
    stale = False
    names = [a for a in sys.argv[1:] if not a.startswith('--')] or NAMES
    for n in names:
        rows = decode(n); t = text(rows); p = os.path.join(H, f'reading_{n}.tsv')
        g = {k: sum(1 for r in rows if r[5] == k) for k in 'HM-'}
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p).read() != t:
                print('STALE', p); stale = True
        else:
            open(p, 'w').write(t)
        print(n, len(rows), 'tokens', g)
    if '--check' in sys.argv:
        print('FAIL' if stale else 'OK'); sys.exit(1 if stale else 0)

if __name__ == '__main__':
    main()

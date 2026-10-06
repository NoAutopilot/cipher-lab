#!/usr/bin/env python3
"""Normalise a raw blind pass (tx/PASS_INSTRUCTIONS.md format) into the long format tools/reconcile_passes.py reads.

  python3 tx/prep_passes.py RAW.tsv OUT.tsv

- joins f50v '_s1'/'_s2' half-line rows into one line: s1's tokens, then s2's tokens from the one prefixed '|>' onward
  (if s2 has no '|>' marker, all of s2 is appended and the line is flagged in stderr);
- 'a|b' alternatives: first choice is the sign, confidence M, the rest in 'alt';
- '?{desc}' unreadable: sign '?', confidence L; '[clear words]' -> one 'w:word' row per word (dropped by the reconciler).
"""
import re, sys
from collections import OrderedDict

def toks(s):
    out, i = [], 0
    s = s.strip()
    while i < len(s):
        if s[i].isspace(): i += 1; continue
        if s[i] == '[':
            j = s.find(']', i); j = len(s) if j < 0 else j
            out += ['w:' + w for w in s[i+1:j].split()]; i = j + 1; continue
        m = re.match(r'(\|>)?\?\{[^}]*\}', s[i:])
        if m: out.append(('|>' if m.group(1) else '') + '?'); i += m.end(); continue
        j = i
        while j < len(s) and not s[j].isspace(): j += 1
        out.append(s[i:j]); i = j
    return out

def main(raw, out):
    lines = OrderedDict()
    for row in open(raw, encoding='utf-8'):
        if not row.strip() or row.startswith('#'): continue
        if '\t' not in row: continue
        cid, t = row.rstrip('\n').split('\t', 1)
        cid = cid.strip()
        m = re.match(r'(f50[rv]_L\d+)(?:_s([12]))?$', cid)
        if not m: continue
        key, half = m.group(1), m.group(2)
        tt = toks(t)
        if half == '2':
            k = next((n for n, x in enumerate(tt) if x.startswith('|>')), None)
            if k is None: sys.stderr.write(f'{raw}: {key} s2 has no |> marker; appended whole\n'); k = 0
            tt = tt[k:]
        tt = [x[2:] if x.startswith('|>') else x for x in tt]
        lines.setdefault(key, []).extend(tt)
    with open(out, 'w', encoding='utf-8') as f:
        f.write('line\tpos\tsign\tconf\talt\n')
        for key, tt in lines.items():
            p = 0
            for x in tt:
                if x.startswith('w:'):
                    p += 1; f.write(f'{key}\t{p}\t{x}\tH\t\n'); continue
                alts = [a for a in x.split('|') if a]
                sign, alt = (alts[0] if alts else '?'), '/'.join(alts[1:])
                conf = 'L' if sign.startswith('?') else ('M' if alt or sign.endswith('?') else 'H')
                p += 1
                f.write(f'{key}\t{p}\t{sign.rstrip("?") or "?"}\t{conf}\t{alt}\n')

if __name__ == '__main__':
    main(sys.argv[1], sys.argv[2])

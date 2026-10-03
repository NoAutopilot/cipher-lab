#!/usr/bin/env python3
"""F36-GLOSS (3 Oct 2026): reconcile two blind Opus reads of the clerk's gloss (passA_*.tsv, passB_*.tsv: crop, gloss)
into one running gloss per line (gloss_recon.tsv), normalised to one convention (CLAUDE.md rule 3): lower case, v -> u,
j -> i (the cipher alphabet has neither), anything not a-z, '?' or space dropped.
Segments of a line overlap by 60 native px: consecutive segments are joined dropping the longest suffix/prefix overlap of
up to 3 letters. Per line the two passes are aligned with difflib: equal -> kept; one '?' -> the other; replace of equal
length -> '?' at each disagreeing letter; a letter only one pass has -> kept (counted one-sided).
  python3 recon_gloss.py [--check]
"""
import csv, difflib, re, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent


def norm(s):
    s = s.lower().replace('v', 'u').replace('j', 'i')
    return re.sub(r'[^a-z? ]', '', s)


def load(tag):
    segs = defaultdict(list)
    for pg in ('r36', 'v36'):
        p = HERE / f'pass{tag}_{pg}.tsv'
        for r in csv.DictReader(open(p), delimiter='\t'):
            c = r['crop'].strip(); line, s = c.rsplit('_s', 1)
            segs[line].append((int(s), norm(r.get('gloss') or '')))
    out = {}
    for line, ss in segs.items():
        txt = ''
        for _, g in sorted(ss):
            g = g.strip()
            a, b = txt.replace(' ', ''), g.replace(' ', '')
            k = 0
            for n in (3, 2, 1):
                if len(a) >= n and len(b) >= n and a[-n:] == b[:n] and '?' not in b[:n]:
                    k = n; break
            # drop k letters from the start of g (skipping spaces)
            i = 0; drop = k
            while drop and i < len(g):
                if g[i] != ' ':
                    drop -= 1
                i += 1
            txt = (txt + ' ' + g[i:].strip()).strip()
        out[line] = re.sub(' +', ' ', txt)
    return out


def main(check=False):
    A, B = load('A'), load('B')
    st = Counter(); rows = ['line\tgloss\tA\tB']
    order = [l for p in ('r36n', 'v36top', 'v36mid', 'r37') for l in sorted(set(A) | set(B)) if l.startswith(p)]
    for line in order:
        a, b = A.get(line, '').replace(' ', ''), B.get(line, '').replace(' ', '')
        res = []
        for op, i1, i2, j1, j2 in difflib.SequenceMatcher(None, a, b, autojunk=False).get_opcodes():
            if op == 'equal':
                for ch in a[i1:i2]:
                    res.append(ch); st['agree' if ch != '?' else 'both?'] += 1
            elif op == 'replace' and i2 - i1 == j2 - j1:
                for x, y in zip(a[i1:i2], b[j1:j2]):
                    if x == '?':
                        res.append(y); st['one?'] += 1
                    elif y == '?':
                        res.append(x); st['one?'] += 1
                    else:
                        res.append('?'); st['split'] += 1
            else:
                seg_a, seg_b = a[i1:i2], b[j1:j2]
                keep = seg_a if len(seg_a) >= len(seg_b) else seg_b
                res.extend(keep); st['onesided'] += len(keep)
        rows.append(f"{line}\t{''.join(res)}\t{A.get(line,'')}\t{B.get(line,'')}")
    txt = '\n'.join(rows) + '\n'
    p = HERE / 'gloss_recon.tsv'
    if check:
        ok = p.exists() and p.read_text() == txt
        print('ok' if ok else 'stale: gloss_recon.tsv'); sys.exit(0 if ok else 1)
    p.write_text(txt)
    tot = sum(st.values())
    print(dict(st), 'total', tot, 'E_gloss = (split+onesided)/total = %.3f' % ((st['split'] + st['onesided']) / max(1, tot)))


if __name__ == '__main__':
    main('--check' in sys.argv)

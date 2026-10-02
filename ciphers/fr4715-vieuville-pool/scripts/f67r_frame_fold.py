#!/usr/bin/env python3
"""Fold the three-pass clear-French frame of no.44 f.67r into f67r_ciphertext.tsv (GAPS-fr4715-vieuville-pool-6, 2 Oct 2026).

tools/reconcile_passes.py aligns the three passes token by token, but the passes split the clear words differently
(A 'Jaysouel', C 'Jay sceu de'), so its 3-way agreement (35.4 pct) measures word division, not reading. This script
uses pass C (the strong blind pass, 84 pct H+M) as the backbone and asks, per C word, whether pass A or pass B wrote
the same word (normalised: lower case, u=v, i=j=y, tildes/accents/apostrophes dropped) at the aligned place
(difflib on the line's normalised word lists, plus a no-space substring test for words of 4+ letters, which catches
A/B word-division splits). Frame confidence: H = C plus at least one Sonnet pass agree and C did not mark it L;
M = agreement with C at L, or C alone at H; L = C alone at M/L. Cipher tokens are never taken from C: each line's
runs of cipher tokens are carried over from the current file unchanged (decode values cannot move); a line whose run
count differs from C's keeps its current tokens and is reported.

  python3 scripts/f67r_frame_fold.py            # report only
  python3 scripts/f67r_frame_fold.py --write    # rewrite f67r_ciphertext.tsv (comments kept, one added)
"""
import difflib, re, sys, unicodedata
from collections import OrderedDict

HERE = __file__.rsplit('/scripts/', 1)[0]

def rows(path):
    out = []
    for ln in open(path, encoding='utf-8'):
        if ln.startswith('#') or ln.startswith('line\t'):
            continue
        p = ln.rstrip('\n').split('\t')
        if len(p) < 3:
            continue
        p += [''] * (5 - len(p))
        out.append(dict(line=p[0], pos=p[1], token=p[2], conf=p[3], note=p[4]))
    return out

def bylines(rs):
    d = OrderedDict()
    for r in rs:
        d.setdefault(r['line'], []).append(r)
    return d

def is_cipher(t):
    return bool(re.fullmatch(r'\.?\d+', t))

def norm(w):
    w = unicodedata.normalize('NFD', w.lower())
    w = ''.join(c for c in w if c.isalpha())
    return w.replace('v', 'u').replace('j', 'i').replace('y', 'i')

def words(rs):
    return [r for r in rs if r['token'].startswith('w:')]

def support(cw, other):
    """indices of C words matched by the other pass."""
    a = [norm(r['token'][2:]) for r in cw]
    b = [norm(r['token'][2:]) for r in other]
    hit = set()
    sm = difflib.SequenceMatcher(None, a, b, autojunk=False)
    for blk in sm.get_matching_blocks():
        for k in range(blk.size):
            if a[blk.a + k]:
                hit.add(blk.a + k)
    joined = ''.join(b)
    for i, w in enumerate(a):
        if i not in hit and len(w) >= 4 and w in joined:
            hit.add(i)
    return hit

def runs(rs):
    out, cur = [], []
    for r in rs:
        if is_cipher(r['token']):
            cur.append(r)
        elif r['token'].startswith('w:'):
            if cur:
                out.append(cur); cur = []
    if cur:
        out.append(cur)
    return out

def main():
    write = '--write' in sys.argv
    A = bylines(rows(f'{HERE}/witness/f67r_pass_a.tsv'))
    B = bylines(rows(f'{HERE}/witness/f67r_pass_b.tsv'))
    C = bylines(rows(f'{HERE}/witness/f67r_pass_c.tsv'))
    cur_path = f'{HERE}/f67r_ciphertext.tsv'
    comments = [l for l in open(cur_path, encoding='utf-8') if l.startswith('#')]
    CUR = bylines(rows(cur_path))
    tally = {'H': 0, 'M': 0, 'L': 0}
    nA = nB = n2 = nC = 0
    kept = []
    out = []
    for line, cur in CUR.items():
        crs = C.get(line, [])
        cw = words(crs)
        sa = support(cw, words(A.get(line, [])))
        sb = support(cw, words(B.get(line, [])))
        cur_runs = runs(cur)
        c_runs = runs(crs)
        if len(cur_runs) != len(c_runs):
            kept.append(f'{line} (current {len(cur_runs)} cipher runs, C {len(c_runs)})')
            out.extend(cur)
            continue
        # walk C, replacing each C cipher run with the current run
        new, wi, ri, in_run = [], 0, 0, False
        for r in crs:
            t = r['token']
            if is_cipher(t):
                if not in_run:
                    new.extend(dict(x) for x in cur_runs[ri]); ri += 1; in_run = True
                continue
            if not t.startswith('w:'):
                continue  # punctuation/symbols are not frame tokens in this file's convention
            in_run = False
            i = wi; wi += 1
            agree = (i in sa) + (i in sb)
            cconf = r['conf'] or 'M'
            nC += 1; nA += i in sa; nB += i in sb; n2 += agree >= 1
            if agree >= 1 and cconf != 'L':
                g = 'H'
            elif agree >= 1 or cconf == 'H':
                g = 'M'
            else:
                g = 'L'
            tally[g] += 1
            src = 'C+' + ('A' if i in sa else '') + ('B' if i in sb else '') if agree else 'C only'
            new.append(dict(line=line, pos='', token=t, conf=g, note=f'frame GAPS-6: {src}, C conf {cconf}'))
        out.extend(new)
    # renumber positions per line
    pos = {}
    for r in out:
        pos[r['line']] = pos.get(r['line'], 0) + 1
        r['pos'] = str(pos[r['line']])
    ncipher = sum(is_cipher(r['token']) for r in out)
    print(f'C frame words {nC}: supported by A {nA}, by B {nB}, by A or B {n2} ({n2 / nC:.1%})')
    print(f'frame confidence: H {tally["H"]} / M {tally["M"]} / L {tally["L"]}')
    print(f'cipher tokens carried over unchanged: {ncipher}; lines kept as they were: {", ".join(kept) or "none"}')
    if write:
        with open(cur_path, 'w', encoding='utf-8') as f:
            f.writelines(comments)
            f.write(f'# 2 Oct 2026 (GAPS-fr4715-vieuville-pool-6, account-4): clear-word frame replaced by pass C\'s words, confidence from '
                    f'three-pass support (scripts/f67r_frame_fold.py: C {nC} words, A or B agree {n2}, H {tally["H"]} / M {tally["M"]} / L {tally["L"]}); '
                    f'cipher tokens unchanged; lines kept as before: {", ".join(kept) or "none"}.\n')
            f.write('line\tpos\ttoken\tconf\tnote\n')
            for r in out:
                f.write('\t'.join([r['line'], r['pos'], r['token'], r['conf'], r['note']]) + '\n')
        print('wrote', cur_path)

if __name__ == '__main__':
    main()

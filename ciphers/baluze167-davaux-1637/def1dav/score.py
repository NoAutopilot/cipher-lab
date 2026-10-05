#!/usr/bin/env python3
"""DEF1-DAV gate 1 (PREREG-DEF1DAV.md): blind Tomokiyo-table letter-sign labels on the 167 f.157 control vs the 15 letter-sign
positions fixed by the period gloss (known_answer.py EXPECTED). Aligns pass tokens to ciphertext.txt by difflib on a class key
(L for letter signs, digits for numerals); missing or unaligned positions count wrong. Null: pass labels permuted among its own
letter-sign positions, 2000 draws, seed 1.   python3 def1dav/score.py   (exit 0 = gate met, 3 = control below gate)"""
import difflib, os, random, re, sys
D = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
EXP = {'167f157 L03': [None, None, None, None, None, 'e', 'u', 'o', 'u', None, 'n', None, None, None, None, 'i', 'x', None, None],
       '167f157 R2': [None, None, None, None, 'n', 's', None, 'i', None, 'n', 'n', 'a', 'b', None, 's']}
ref = {}
for l in open(f'{D}/ciphertext.txt'):
    if '|' in l and not l.startswith('#'):
        h, b = l.split('|', 1); ref[h.strip()] = b.split()
rows = dict(l.rstrip('\n').split('\t', 1) for l in open(f'{D}/def1dav/passC_b167f157.tsv') if not l.startswith('line'))
def toks(s): return [t for t in re.sub(r'\{[^}]*\}', ' ', s).split()]
pas = {'167f157 L03': toks(rows['b167f157_run1_L03']) + toks(rows['b167f157_run1_L04']), '167f157 R2': toks(rows['b167f157_run2_L02'])}
def key(t):
    t = t.rstrip('?')
    return 'L' if t.startswith('L:') else 'w' if t.startswith('w:') else re.sub(r'\D', '', t)
pairs = []  # (expected, label)
for line, exp in EXP.items():
    r = [t for t in ref[line]]; p = pas[line]
    sm = difflib.SequenceMatcher(a=[key(t) for t in r], b=[key(t) for t in p], autojunk=False)
    amap = {}
    for blk in sm.get_matching_blocks():
        for k in range(blk.size): amap[blk.a + k] = blk.b + k
    for blk in sm.get_opcodes():  # equal-length replace blocks of letter signs also align position by position
        tag, a0, a1, b0, b1 = blk
        if tag == 'replace' and a1 - a0 == b1 - b0:
            for k in range(a1 - a0): amap[a0 + k] = b0 + k
    for i, e in enumerate(exp):
        if e is None: continue
        j = amap.get(i); lab = p[j].rstrip('?') if j is not None else ''
        lab = lab[2:].split('|')[0] if lab.startswith('L:') else ''
        pairs.append((e, lab))
ok = sum(e == l for e, l in pairs); n = len(pairs)
labs = [l for _, l in pairs]; rng = random.Random(1); nulls = []
for _ in range(2000):
    rng.shuffle(labs); nulls.append(sum(e == l for (e, _), l in zip(pairs, labs)) / n)
nulls.sort()
print('per position (expected:label):', ' '.join(f'{e}:{l or "-"}' for e, l in pairs))
print(f'control letter accuracy {ok}/{n} = {ok/n:.3f}; shuffle floor mean {sum(nulls)/len(nulls):.3f}, p99 {nulls[int(.99*len(nulls))]:.3f}; gate 0.80 ->',
      'MET' if ok / n >= 0.8 else 'CONTROL BELOW GATE')
sys.exit(0 if ok / n >= 0.8 else 3)

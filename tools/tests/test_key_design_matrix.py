#!/usr/bin/env python3
"""Offline tests for tools/key_design.py --matrix (TT-MATRIX, 8 Oct 2026; Tomokiyo matrix.htm, ormonde.htm,
schiner.htm). Catches: one-part runs (one or several homophone series), shuffled and reversed blocks, the paired,
vowel-headed column matrix. Must NOT flag: a random assignment (label none), a table with too few letter codes."""
import random
import subprocess
import sys
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))
import key_design as kd  # noqa: E402

FX = TOOLS / 'tests' / 'fixtures' / 'matrix'
fails = 0


def check(name, cond):
    global fails
    print(('PASS ' if cond else 'FAIL ') + name)
    fails += not cond


def label(pairs):
    return kd.matrix_analyse(pairs, n_null=100)


AL = 'abcdefghilmnopqrstuxz'
one = [(22 + i + 2 * (i // 8), l) for i, l in enumerate(AL)]
check('one-part run labelled one-part', label(one)['label'] == 'one-part')
two = [(10 + i, l) for i, l in enumerate(AL)] + [(40 + i, l) for i, l in enumerate(AL)]
r = label(two)
check('two homophone series -> one-part, 2 series', r['label'] == 'one-part' and r.get('series') == 2)
blocks = [AL[0:5], AL[5:10], AL[10:15], AL[15:21]]
rev = [(10 * (k + 1) + j, l) for k, b in enumerate(reversed(blocks)) for j, l in enumerate(b)]
r = label(rev)
check('reversed blocks (Spanish blocked square shape) -> blockwise, reversed',
      r['label'] == 'blockwise one-part' and r.get('block_order') == 'reversed')
shuf = [(10 * (k + 1) + j, l) for k, b in enumerate([blocks[2], blocks[0], blocks[3], blocks[1]]) for j, l in enumerate(b)]
r = label(shuf)
check('shuffled blocks -> blockwise, shuffled', r['label'] == 'blockwise one-part' and r.get('block_order') == 'shuffled')
# column matrix, vowel-headed, paired first digits (Commendone shape)
cols = {1: 'abcd', 3: 'efgh', 5: 'ilmn', 7: 'opqr', 9: 'stux'}
mat = [(10 * t + u, s[(t - 1) // 2]) for u, s in cols.items() for t in range(1, 9)]
r = label(mat)
check('column matrix -> two-dimensional, paired, vowel-headed',
      r['label'] == 'two-dimensional' and r['paired_first_digits'] == '20/20' and r['vowel_headed'] == '4/5')
rng = random.Random(1)
nones = 0
for i in range(20):
    ls = [l for _, l in two]
    rng.shuffle(ls)
    nones += label(list(zip([c for c, _ in two], ls)))['label'] == 'none'
check(f'must NOT flag: random assignment -> none ({nones}/20)', nones >= 19)
check('must NOT flag: fewer than 8 letter codes -> too-few', label(one[:5])['label'] == 'too-few')
check('nomenclator/non-numeric codes ignored', kd.matrix_letters({'12': 'a', 'A7': 'b', '13': 'Roma', '14': 'null'})
      == [(12, 'a')])
# prediction: Ormonde's breakthrough (ormonde.htm: t=83, o=78, period 24)
tab, _ = kd.load_table(FX / 'ormonde.tsv')
pairs = kd.matrix_letters(tab)
hyp, pred = kd.matrix_predict({83: 't', 59: 't'}, [c for c, _ in pairs], kd.MATRIX_ALPHABETS['en24'])
good = sum(pred.get(c) == l for c, l in pairs)
check(f'Ormonde from t=83,t=59 -> periodic one-part, {good}/{len(pairs)} letters', 'periodic' in (hyp or '') and good >= 40)
hyp, pred = kd.matrix_predict({12: 'a', 19: 'e'}, [c for c, _ in kd.matrix_letters(kd.load_table(FX / 'schiner.tsv')[0])],
                              kd.MATRIX_ALPHABETS['it21'])
check(f'Schiner from a=12,e=19 counts digits 0-4,8,9 ({hyp})', pred.get(18) == 'd' and pred.get(29) == 'n')
hyp, pred = kd.matrix_predict({1: 'a', 2: 'q'}, list(range(1, 22)), AL)
check('must NOT predict: anchors out of alphabetical order with no fit', not pred or hyp is None or pred.get(2) == 'q')
out = subprocess.run([sys.executable, str(TOOLS / 'key_design.py'), '--matrix', str(FX / 'commendone.tsv')],
                     capture_output=True, text=True)
check('CLI --matrix prints label and matrix', out.returncode == 0 and 'two-dimensional' in out.stdout and 'matrix' in out.stdout)
out = subprocess.run([sys.executable, str(TOOLS / 'key_design.py'), '--help'], capture_output=True, text=True)
check('--help names Tomokiyo and matrix.htm', 'Tomokiyo' in out.stdout and 'matrix.htm' in out.stdout)
print(f'{fails} failure(s)')
sys.exit(1 if fails else 0)

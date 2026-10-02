#!/usr/bin/env python3
"""Offline test for tools/key_order_test.py (GAPS-vanbeuningen-dewitt-1657, 2 Oct 2026).
Fixtures only: a synthetic alphabetically allotted homophonic key written to a temp file; no network, no repo
ciphertexts. Run: python3 tools/tests/test_key_order_test.py"""
import random, sys, tempfile, json, io, contextlib
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import key_order_test as kot

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


def write_key(rows):
    f = tempfile.NamedTemporaryFile('w', suffix='.tsv', delete=False, encoding='utf-8')
    f.write('code\tvalue\tgrade\tsource\tnote\n')
    for code, value, grade in rows:
        f.write(f'{code}\t{value}\t{grade}\tfixture\t\n')
    f.close()
    return f.name


# an ordered key that wraps once: k..y at 4-37, a..i at 39-65, two homophones for the common letters
alloc = [('k', 4), ('l', 6), ('l', 7), ('m', 9), ('n', 10), ('o', 12), ('o', 13), ('p', 17), ('r', 21), ('r', 22),
         ('s', 23), ('s', 24), ('t', 25), ('t', 26), ('u', 27), ('w', 32), ('y', 36), ('a', 39), ('a', 41),
         ('a', 42), ('b', 44), ('c', 46), ('c', 47), ('e', 50), ('e', 51), ('e', 52), ('f', 55), ('g', 57),
         ('h', 59), ('i', 61), ('i', 62)]
rows = [(f'{c},', v, 'C') for v, c in alloc] + [(f'{c}:', v, 'C') for v, c in alloc]  # separator variants = one code
rows += [('40,', 'd|a', 'M'), ('11,', 'm|n', 'M'), ('5,', 'k', 'M'), ('143:', 'Vereenichde Nederlanden', 'C'), ('Mijn', 'Mijn', 'clear')]
path = write_key(rows)

letters = kot.load_key(path, {'C'})
check('one row per code number, separators stripped, clear and nomenclator rows skipped', len(letters) == len(alloc))
check('u/v merged by default', kot.load_key(path, {'C'})[27][0] == 'u')

codes = sorted(letters)
seq = [letters[c][0] for c in codes]
check('ordered key with one wrap scores 0 descents', kot.descents(seq, kot.ALPHABET) == 0)
rng = random.Random(0)
sh = seq[:]
rng.shuffle(sh)
check('shuffled labels score many descents', kot.descents(sh, kot.ALPHABET) >= 8)

lt = {c: letters[c][0] for c in codes}
h, n, w = kot.loo_accuracy(lt, kot.ALPHABET)
check('leave-one-out bracket hits every code of an ordered key', h == n)
check('ordered brackets are narrow', w < 4)
shl = dict(zip(codes, sh))
h2, n2, w2 = kot.loo_accuracy(shl, kot.ALPHABET)
check('shuffled key brackets are wide and miss often', w2 > w and h2 < h)

b = kot.bracket(codes, lt, 40, kot.ALPHABET)
check('a code between two a-codes is bracketed {a}', b and ''.join(b[2]) == 'a')
b = kot.bracket(codes, lt, 11, kot.ALPHABET)
check('a code between n and o is bracketed {n,o}', b and ''.join(b[2]) == 'no')
b = kot.bracket(codes, lt, 65, kot.ALPHABET)
check('bracket wraps past the largest code to the smallest', b and b[1] == 4 and ''.join(b[2]) == 'ik')
b = kot.bracket(codes, lt, 2, kot.ALPHABET)
check('bracket wraps below the smallest code to the largest', b and b[0] == 62)

out = io.StringIO()
with contextlib.redirect_stdout(out):
    rc = kot.main([path, '--grades', 'C', '--query', '40', '11', '--shuffles', '50', '--seed', '3', '--json'])
res = json.loads(out.getvalue())
check('main runs and exits 0', rc == 0)
check('real descents 0 and shuffle control higher', res['descents_real'] == 0 and res['descents_shuffle']['min'] > 0)
check('query shows the on-file conflict value', any(q['code'] == 40 and q['on_file'] == 'd|a' and q['bracket'] == 'a' for q in res['queries']))
check('queried codes are excluded from the attested set', res['attested_codes'] == len(alloc))

print('FAILED' if fails else 'OK', fails)
sys.exit(1 if fails else 0)

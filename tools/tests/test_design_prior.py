#!/usr/bin/env python3
"""Offline test for tools/key_design.py and tools/design_prior.py (KEY-DESIGN, 26 Sept 2026).
Fixtures only: synthetic keys and token streams built here, a temp key file; no network, no repo ciphertexts.
Run: python3 tools/tests/test_design_prior.py"""
import random, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import key_design as kd
import design_prior as dp

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


# ---- value classes and design families from the table alone
mono = {str(10 + i): c for i, c in enumerate('abcdefghilmnopqrstuxz')}
check('monoalphabetic table -> alphabet substitution', kd.signature(mono)['design_family'] == 'alphabet substitution')
homo = {str(10 + i): 'aeioustrn'[i % 9] for i in range(45)}
homo.update({str(60 + i): c for i, c in enumerate('bcdfglmpqxz')})
sig = kd.signature(homo)
check('five codes per common letter -> homophonic', sig['design_family'] == 'homophonic')
check('homophones max counted', sig['homophones_max'] == 5)
nom = dict(mono, **{str(100 + i): w for i, w in enumerate(['roy', 'pape', 'armee', 'Espagne', 'Guise', 'NULL'])})
sig = kd.signature(nom)
check('letters + words/names -> nomenclator', sig['design_family'] == 'nomenclator')
check('names and nulls counted', sig['nomenclator_names'] == 2 and sig['nulls_declared'] == 1)
syl = dict(mono, **{str(200 + i): c + v for i, (c, v) in enumerate((c, v) for c in 'bcdmpst' for v in 'aeiou')})
sig = kd.signature(syl)
check('syllable grid detected -> syllabary', sig['syllable_grid'] == 'yes' and sig['design_family'] == 'syllabary')
code = {str(300 + i): w for i, w in enumerate(['guerre', 'paix', 'armee', 'flotte', 'traite', 'secours'] * 3)}
check('words only -> code numbers', kd.signature(code)['design_family'] == 'code numbers')
check('numeral range and digit lengths', kd.signature(code)['numeral_min'] == 300
      and kd.signature(code)['digit_lengths'] == '3:18')

# ---- named-header loader: thurloe shape, the CODE is named 'value' and the plaintext 'meaning'
with tempfile.TemporaryDirectory() as td:
    p = Path(td) / 'key_x.tsv'
    p.write_text('# comment\nvalue\tmeaning\tkind\tsource\n24\te\tletter\tx\n54\te\tletter\tx\n130\tHague\tname\tx\n')
    key, why = kd.load_table(p)
    check('thurloe-shaped header: code=value column, plaintext=meaning', key == {'24': 'e', '54': 'e', '130': 'Hague'})
    p.write_text('item\tshare\tn\nA\t0.5\t3\n')
    key, why = kd.load_table(p)
    check('a statistics table is refused with a reason', key is None and 'not a code->value' in why)

# ---- token statistics
s = kd.ct_stats(['a', 'a', 'b', 'c'])
check('ioc on a known stream', abs(s['ioc'] - 2 / 12) < 1e-9 and s['k'] == 3 and abs(s['singleton'] - 2 / 3) < 1e-9)

# ---- the prior on synthetic families (fixture references, no repo keys)
FREQ = dict(e=12.7, t=9.1, a=8.2, o=7.5, i=7.0, n=6.7, s=6.3, h=6.1, r=6.0, d=4.3, l=4.0, c=2.8, u=2.8, m=2.4,
            w=2.4, f=2.2, g=2.0, y=2.0, p=1.9, b=1.5, v=1.0, k=0.8)
LET, W = list(FREQ), list(FREQ.values())


def plain(rnd, n):
    return rnd.choices(LET, W, k=n)


def mono_stream(rnd, n, off):
    return [str(off + LET.index(c)) for c in plain(rnd, n)]


def homo_stream(rnd, n, off):
    table, k = {}, off
    for c, w in FREQ.items():
        m = max(1, round(w / 1.5))
        table[c] = [str(k + j) for j in range(m)]
        k += m
    return [rnd.choice(table[c]) for c in plain(rnd, n)]


def code_stream(rnd, n, off):
    vocab = [str(off + i) for i in range(900)]
    wts = [1 / (i + 1) for i in range(900)]
    return rnd.choices(vocab, wts, k=n)


def ref(path, folder, fam, stream):
    return dict(key_path=path, _folder=folder, design_family=fam, _signs=stream, _key={}, office=folder,
                decade='1570s', correspondents='', sign_inventory='digits', numeral_min='', numeral_max='')


rnd = random.Random(7)
R = dp.Refs.__new__(dp.Refs)
R.rows = [ref(f'k/{fam}{i}', f'{fam}-f{i}', fam, gen(rnd, 3000, 10 + 100 * i))
          for fam, gen in (('alphabet substitution', mono_stream), ('homophonic', homo_stream),
                           ('code numbers', code_stream)) for i in range(3)]
R.refs, R.by_path, R._syn = R.rows, {r['key_path']: r for r in R.rows}, {}
R.canon = {r['key_path']: r['key_path'] for r in R.rows}

dp.set_mode('class')
for name, gen, want in (('monoalphabetic', mono_stream, 'letter-for-letter'),
                        ('homophonic', homo_stream, dp.MULTI), ('code', code_stream, 'code')):
    res = dp.prior(gen(random.Random(99), 600, 5), R, draws=60, seed=1)
    check(f'{name} target ranks its own class first', res['ranking'][0][0] == want)
    if name == 'homophonic':  # a flat homophonic stream sits near the uniform null: never excluded, may not beat it
        check(f'{name} target: own class not excluded', res['verdict'][want] in ('plausible', 'not above null'))
    else:
        check(f'{name} target: own class plausible', res['verdict'][want] == 'plausible')
    check(f'{name} target: statistics are relabel-invariant (why relabelling is not the control)',
          res['relabel_invariant'])
res = dp.prior(mono_stream(random.Random(3), 600, 5), R, draws=60, seed=1)
check('monoalphabetic target excludes the code class', res['verdict']['code'] == 'excluded')
check('shuffled-input false-positive rate is reported and small', 0.0 <= res['fp'] <= 0.1)
res = dp.prior(['1', '2', '3'] * 5, R, draws=10, seed=1)
check('short input returns a note, no verdict', 'ranking' not in res and res['note'].startswith('short'))
dp.set_mode('family')
res = dp.prior(homo_stream(random.Random(5), 600, 5), R, draws=20, seed=1)
check('fine tier keeps the table family names', res['ranking'][0][0] == 'homophonic')
dp.set_mode('class')

# ---- synthetic enciphering from a key table
key = dict(mono, **{'500': 'de', '501': 'guerre', '502': 'NULL'})
syn, share = dp.synthesize(key, 'fr', seed=1, n=500)
check('synthesize returns n tokens from the key codes', syn is not None and len(syn) == 500 and set(syn) <= set(key))
syn, share = dp.synthesize({'1': 'a', '2': 'e', '3': 'roy', '4': 'pape', '5': 'paix'}, 'fr', seed=1, n=200)
check('a table too partial to spell the corpus gets no synthetic reference', syn is None and share > 0.5)

print(f'{fails} failure(s)')
sys.exit(1 if fails else 0)

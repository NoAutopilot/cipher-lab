#!/usr/bin/env python3
"""Offline test for the plaintext-alphabet option (A2P4-KAL4, 3 Oct 2026): homophonic_anneal.py --alphabet,
families/homophonic.py --param alphabet=, judge_plaintext.py's judge-block "alphabet", translit_ru.py --soft-letters.

(a) Default alphabet unchanged, byte for byte: tools/tests/homophonic_alphabet_default_gen.py run against the current
    tools/ must print exactly tools/tests/fixtures/homophonic_alphabet_default.json, which the same script printed
    against the tools/ of commit 85a7db4e (before the option existed): a CLI control, a CLI target solve of
    kaliningrad-2015's convention-B signs, a families.homophonic profile=target control+solve, and a judge() result.
(b) A synthetic K-36 cipher over the 35-letter ru-s3p-soft alphabet round-trips: a window of
    tools/data/ru19_soft/s3p_soft.txt.gz enciphered with 36 homophones is read back at >= 0.9 of positions,
    soft (upper-case) letters included; the judge with the same alphabet PASSes a real window and FAILs it shuffled.
(c) fold() keeps upper-case soft letters under a custom alphabet and restores the old fold after set_alphabet(None);
    translit_ru.merge_soft joins q to the letter before it.
"""
import gzip, json, os, random, subprocess, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
T = os.path.join(R, 'tools')
sys.path.insert(0, T)

# (a)
got = subprocess.run([sys.executable, os.path.join(T, 'tests', 'homophonic_alphabet_default_gen.py'), T], cwd=R,
                     check=True, capture_output=True, text=True).stdout
want = open(os.path.join(T, 'tests', 'fixtures', 'homophonic_alphabet_default.json'), encoding='utf-8').read()
assert got == want, 'default-alphabet output changed (see homophonic_alphabet_default_gen.py)'
print('ok (a) default alphabet byte-identical to the pre-option fixture')

import homophonic_anneal as ha  # noqa: E402
import judge_plaintext as jp  # noqa: E402
import translit_ru  # noqa: E402

# (c)
assert translit_ru.merge_soft('nqet tqma khqa q') == 'Net Tma kHa ', translit_ru.merge_soft('nqet tqma khqa q')
ha.set_alphabet('ru-s3p-soft')
assert ha.fold('Net, tma! kHa q') == 'NettmakHa', ha.fold('Net, tma! kHa q')
ha.set_alphabet(None)
assert ha.ALPHA == 'abcdefghiklmnopqrstuwxyz' and ha.fold('Jäger V') == 'iageru', ha.fold('Jäger V')
print('ok (c) fold / set_alphabet / merge_soft')

# (b)
COR = os.path.join(T, 'data', 'ru19_soft', 's3p_soft.txt.gz')
ha.set_alphabet('ru-s3p-soft')
text = ha.fold(gzip.open(COR, 'rt', encoding='utf-8').read())
assert set(text) == set(ha.ALPHABETS['ru-s3p-soft']) and len(set(text)) == 35
# a narrative window (Gospels region); an OT name-list window (offset 200000) defeats the anneal's search in the
# default 24-letter alphabet as well (0.13 there, true key scores far above the found one), so it tests the corpus
start = 2000000
plain, train = text[start:start + 1000], text[:start] + text[start + 1000:]
model = ha.Model([train], 3)
seq, p, truth = ha.make_control(plain, 36, 1000, model, 7)
res = ha.solve(seq, model, 3, 40000, 7, 1.0)
key = res[0][1]
dec = ''.join(key[x] for x in seq)
share = sum(a == b for a, b in zip(dec, p)) / len(p)
soft = [i for i, c in enumerate(p) if c.isupper()]
soft_share = sum(dec[i] == p[i] for i in soft) / max(1, len(soft))
assert share >= 0.9, share
print(f'ok (b) K-36 ru-s3p-soft round trip: {share:.3f} of 1000 positions, soft letters {soft_share:.3f} of {len(soft)}')
ha.set_alphabet(None)
spec = {'judge': {'alphabet': 'ru-s3p-soft', 'corpora': [COR], 'control_samples': 60, 'letters_min': 100}}
real = text[2500000:2501000]
r1 = jp.judge(spec, real)
ws = list(real); random.Random(3).shuffle(ws)
r2 = jp.judge(spec, ''.join(ws))
assert r1['pass'] and not r2['pass'], (r1, r2)
assert r1['checks']['length']['got'] == 1000, r1  # upper-case soft letters counted, not dropped or lower-cased
assert jp._ALPHA is None  # the judge restores the a-z fold after the call
print('ok (b) judge alphabet: real window PASS', r1['checks']['language']['score'], 'shuffled FAIL', r2['checks']['language']['score'])

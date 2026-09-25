#!/usr/bin/env python3
"""Offline test for tools/key_crossmatch.py: runs the positive control (own key beats a shuffled-key control
and an unrelated-key control) on three small synthetic monoalphabetic fixtures, using the real English corpus
already on disk (tools/data), so the test needs no network and no repo-built corpus. It calls the same
functions the real sweep uses (decode_with, score_pair, zscore, coverage_of, sign_type) rather than
re-implementing them, so a change to the scoring pipeline that breaks the positive control breaks this test
too. Also checks the whitespace-fallback tokenizer and the majority-vote sign_type classifier directly.
Run: python3 tools/tests/test_key_crossmatch.py"""
import random, string, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx
import judge_plaintext as jp

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


# ---------------------------------------------------------------- fixtures: three unrelated monoalphabetic
# substitutions over three distinct, unrelated English sentences, each long enough (150+ letters) for the
# 4-gram model to have real discriminating power. Codes are single letters (sign_type 'letters', matching
# 'monoalphabetic' design) so each fixture is, from the pipeline's point of view, an ordinary key/ciphertext
# pair -- just built in memory instead of read from ciphers/<t>/key.tsv.
PLAINTEXTS = [
    "the quick brown fox jumps over the lazy dog and runs away into the forest before anyone can see it "
    "happen and nobody in the village ever finds out where the animal went after that long summer day",
    "she walked along the river every morning before the sun had fully risen and watched the boats come "
    "in from the sea carrying fish and salt for the market that opened at the edge of the old stone bridge",
    "the merchant kept his ledger locked in a drawer beneath the counter and never let his apprentice see "
    "the true accounts until the debts owed by the captain of the ship were finally settled in full",
]


def make_fixture(plaintext, seed):
    letters = sorted(set(c for c in plaintext if c.isalpha()))
    rnd = random.Random(seed)
    codes = list(string.ascii_uppercase[:len(letters)])
    rnd.shuffle(codes)
    enc = dict(zip(letters, codes))
    key = {c: {'value': p} for p, c in enc.items()}
    signs = [enc[c] for c in plaintext if c.isalpha()]
    return key, signs


fixtures = [make_fixture(p, seed=i) for i, p in enumerate(PLAINTEXTS)]
model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA['en']])
meta_stub = {'lang': 'en'}

for i, (key, signs) in enumerate(fixtures):
    real, shuffles = kx.score_pair(key, meta_stub, signs, model, n_shuffle=30, seed=i)
    z_sh = kx.zscore(real, shuffles)
    others = [ok for j, (ok, _) in enumerate(fixtures) if j != i]
    null_scores = []
    for ok in others:
        otext, _ = kx.decode_with(ok, signs)
        null_scores.append(model.score(otext))
    z_un = kx.zscore(real, null_scores)
    check(f'fixture {i}: shuffled-key control z >= 4 (got {z_sh:.2f})', z_sh is not None and z_sh >= 4)
    check(f'fixture {i}: unrelated-key control z >= 4 (got {z_un:.2f})', z_un is not None and z_un >= 4)
    cov = kx.coverage_of(key, signs)
    check(f'fixture {i}: coverage is 1.0 (every sign is in its own key)', cov == 1.0)

# a key must rank its OWN ciphertext first among all three fixtures' ciphertexts, not just beat its controls
for i, (key, signs) in enumerate(fixtures):
    scores = []
    for j, (_, other_signs) in enumerate(fixtures):
        text, _ = kx.decode_with(key, other_signs)
        scores.append((model.score(text), j))
    scores.sort(reverse=True)
    check(f'fixture {i}: its own key ranks its own ciphertext first of 3', scores[0][1] == i)

# sign_type: majority vote, not "every code must agree" (a stray non-conforming token must not flip the class)
check('sign_type: pure digits', kx.sign_type(['12', '03', '441']) == 'digits')
check('sign_type: pure letters', kx.sign_type(['ab', 'x', 'qrs']) == 'letters')
check('sign_type: one stray token does not flip a 9-of-10 digit majority to mixed',
      kx.sign_type(['1', '2', '3', '4', '5', '6', '7', '8', '9', 'RAW']) == 'digits')
check('sign_type: a genuine 50/50 split is mixed', kx.sign_type(['1', '2', 'a', 'b']) == 'mixed')

# whitespace fallback tokenizer: numeral cipher groups kept, a run of 4+ letters treated as clear prose
ws = kx.whitespace_signs("240 318 401 Monsieur de le Marquis 34 450")
check('whitespace fallback keeps numeral tokens', ws.count('240') == 1 and ws.count('34') == 1)
check('whitespace fallback drops long alphabetic words as clear prose',
      'Monsieur' not in ws and 'Marquis' not in ws)

print('key_crossmatch:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)

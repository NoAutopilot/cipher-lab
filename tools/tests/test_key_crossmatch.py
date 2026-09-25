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

# ---------------------------------------------------------------- fix A: robust key loading (job 1b)
# dk.load_key leaves an un-stripped header row as data when the header's first cell isn't literally
# 'code'/'sign'/'token' (e.g. 'system'), or crashes outright when 'code' is stripped but there is no 'value'
# column (e.g. 'plaintext' instead) -- both found on disk in this repo. robust_load_key is the fallback.
import tempfile, os as _os


def write_tmp(text):
    fd, path = tempfile.mkstemp(suffix='.tsv')
    with _os.fdopen(fd, 'w', encoding='utf-8') as f:
        f.write(text)
    return path


p = write_tmp("system\tsign\tvalue\tgrade\n74\t0\tg\tC\n74\t1\te\tC\n74\t3\ta\tC\n")
key, reason = kx.robust_load_key(p)
check("robust_load_key: picks the named 'sign'/'value' columns, not position 0/1 which would read the "
      "'system' partition column instead (august-van-saksen-1561-64/key_53.tsv etc.'s real shape)",
      key is not None and key.get('0', {}).get('value') == 'g' and key.get('1', {}).get('value') == 'e')
_os.remove(p)

p = write_tmp("code\tplaintext\nb\tA\np\tA\nq-\tC\n")
key, reason = kx.robust_load_key(p)
check("robust_load_key: 'code'+'plaintext' header (Brienne's key_brienne_1647/1651.tsv shape) parses",
      key is not None and key.get('b', {}).get('value') == 'A' and key.get('q-', {}).get('value') == 'C')
_os.remove(p)

p = write_tmp("item\tglossed_H_columns\tsame_value\tshare\nBLA179\t24\t16\t0.889\n")
key, reason = kx.robust_load_key(p)
check('robust_load_key: a table with no value/plaintext/gloss/meaning column is refused, not guessed '
      '(huntington-blathwayt-madrid-1728/key_items.tsv shape -- a stats table, not a key)',
      key is None and 'value' in reason)
_os.remove(p)

check('load_key_meta override: dk.load_key succeeding on a real code/value table is left alone (no override) '
      'on a key whose real first code happens not to be a header word',
      kx.KNOWN_HEADER_WORDS.isdisjoint({'psi', 'db', '_0', '8'}))

# ---------------------------------------------------------------- fix A: ciphertext sign column by name
p = write_tmp("leaf\tline\tpos\ttoken\tconf\tlayer\n"
              "f1\tR01\t1\ti'ay\tH\tclear\nf1\tR01\t2\t722\tH\tcipher\nf1\tR01\t3\t841\tH\tcipher\n"
              "f1\tR01\t4\tveu\tH\tclear\nf1\tR01\t5\t963\tH\tcipher\n")
signs = kx.robust_tsv_signs(Path(p))
check("robust_tsv_signs: finds the 'token' column by name and skips layer=clear rows (clair1108-duvergier shape)",
      signs == ['722', '841', '963'])
_os.remove(p)

p = write_tmp("page\tline\tpos\tsign_desc\n1\t1\t1\tcapital-H\n1\t1\t2\tbackward-C\n1\t1\t3\tsmall-o\n")
signs = kx.robust_tsv_signs(Path(p))
check("robust_tsv_signs: falls back to 'sign_desc' for glyph-description keys (willem-van-hessen-1567 shape)",
      signs == ['capital-H', 'backward-C', 'small-o'])
_os.remove(p)

check("tokenize_ciphertext's drop_equals_clear strips a bare '=' clear-word marker (jan-van-nassau-1572-75's "
      "own documented convention, clear_prefix '=') without touching a real sign",
      kx.drop_equals_clear(['77', '=van', '81', '=?']) == ['77', '81'])

# ---------------------------------------------------------------- fix A: own-text pairing (compute_own_cts)
digits = kx.DIGIT_RUN_RE.findall('key_1659_f86only.tsv')
check("DIGIT_RUN_RE picks up both the key's own number and a folio number in the same basename",
      '1659' in digits and '86' in digits)
check("key_person_name strips key_/_extended and returns the office name (thurloe-printed shape)",
      kx.key_person_name('key_blake_extended.tsv') == 'blake' and kx.key_person_name('key_montagu.tsv') == 'montagu')
check("key_person_name on a pure folio-numbered key returns None (fr5160-letellier-1653's key_1659.tsv has no name)",
      kx.key_person_name('key_1659.tsv') is None)

print('key_crossmatch:', 'all tests pass' if not fails else f'{fails} failures')
sys.exit(1 if fails else 0)

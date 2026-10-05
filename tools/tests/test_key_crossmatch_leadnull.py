#!/usr/bin/env python3
"""Offline test for tools/key_crossmatch.py's lead filter (N9-XMFIX, 5 Oct 2026): KEY_NAME_EXCLUDE and
pair_lead_null(), the per-pair in-class shuffled-key p99 + order-shuffled z4gram p99 a gated row must beat before it
is reported as a lead. Scope (CLAUDE.md Usage 8a), as stated in pair_lead_null's docstring:
  must DROP  a class-shuffled copy of a true key, scored on the true key's ciphertext (the clair1161 key_shuf* shape
             that the 5 Oct 02:53 nightly posted as two leads), and a shuffled/control/null key file by name;
  must KEEP  a true letter-valued key on its own ciphertext (a few hundred tokens), and a real key file that merely
             sits in a control_* folder.
Fixtures only (a synthetic monoalphabetic encipherment of an English corpus window); no network, no repo ciphertexts.
Run: python3 tools/tests/test_key_crossmatch_leadnull.py"""
import random, re, string, sys
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


# ---- KEY_NAME_EXCLUDE: control keys by file name; a real key in a control_* folder is kept
for name, want in [('ciphers/x/pool/key_shuf3_s1.tsv', True), ('ciphers/x/two/key_shuf4_s1.tsv', True),
                   ('ciphers/x/key_shuffled.tsv', True), ('ciphers/x/key_control_a.tsv', True),
                   ('ciphers/x/key_null.tsv', True), ('ciphers/x/key.tsv', False),
                   ('ciphers/fr15575-syllabic-1592-95/control_fr3641/key_syllabary.tsv', False)]:
    check(f'KEY_NAME_EXCLUDE {name}: {"excluded" if want else "kept"}', bool(kx.key_name_excluded(name)) == want)

# ---- pair_lead_null: one synthetic monoalphabetic fixture on 400 letters of the English corpus
corpus = [jp.read_corpus(p) for p in jp.LANG_CORPORA['en']]
model = jp.NgramModel(corpus)
kx.attach_freqs(model, corpus)
letters = re.sub('[^a-z]', '', ' '.join(corpus).lower())[50000:50400]
rnd = random.Random(11)
codes = [str(10 + i) for i in range(26)]
rnd.shuffle(codes)
enc = dict(zip(string.ascii_lowercase, codes))
true_key = {c: {'value': l} for l, c in enc.items()}
signs = [enc[ch] for ch in letters]

N = kx.LEAD_DRAWS
keep = kx.pair_lead_null(true_key, signs, model, n_draws=N)
check(f"true key on its own ciphertext survives (S {keep['S']} vs in-class p99 {keep['p99_inclass']}; "
      f"z4gram {keep['z_ng']} vs order p99 {keep['p99_order_zng']})", keep['survives'])

# the shuffled-control shape: of 20 class-shuffled copies of the true key, take the one scoring highest on the
# true ciphertext (the nightly's worst case -- the clair1161 controls that cleared the gate were the top of theirs)
cands = []
for i in range(20):
    sk = kx.shuffled_key_by_class(true_key, random.Random(1000 + i))
    cands.append((kx.pair_stats(sk, signs, model, n_shuffle=20, seed=0)['own']['stat'] or -99, i, sk))
top_stat, top_i, shuf_key = max(cands, key=lambda t: t[0])
drop = kx.pair_lead_null(shuf_key, signs, model, n_draws=N)
check(f"best of 20 shuffled control keys (stat {top_stat:.3f}) is dropped ({drop['why']})", not drop['survives'])

print('ALL PASS' if not fails else f'{fails} FAILED')
sys.exit(1 if fails else 0)

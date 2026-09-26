#!/usr/bin/env python3
"""Offline test for tools/key_crossmatch.py's calibrated gate and --since selection (XMATCH-CAL, 26 Sept 2026).
Fixtures only (synthetic keys, a throwaway git repo in a temp dir); no network, no repo ciphertexts.
Run: python3 tools/tests/test_key_crossmatch_gate.py"""
import random, string, subprocess, sys, tempfile
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


# ---- choose_gate: admits every verified pair in the stratum, counts null draws above it, keeps short ones out
verified = [dict(stat=s, n_tokens=n, coverage=c, key_path='k', ciphertext_path='c')
            for s, n, c in [(6.4, 500, 1.0), (3.9, 300, 0.9), (5.1, 150, 0.7), (0.7, 26, 1.0), (2.4, 2000, 0.1)]]
nulls = dict(stratum=[x / 10 for x in range(-20, 30)] + [4.0], all=[x / 10 for x in range(-20, 30)] + [4.0, 1.0])
g = kx.choose_gate(verified, nulls)
check('gate is the smallest in-stratum verified stat, floored', g['stat_min'] == 3.9)
check('every in-stratum verified pair is admitted',
      all(kx.passes_gate(v['stat'], g) for v in verified if v['n_tokens'] >= kx.MIN_TOKENS and v['coverage'] >= 0.5))
check('short and low-coverage verified pairs are reported below the stratum', g['n_verified_below'] == 2)
check('false positives counted on the null draws', g['fp'] == 1 and g['n_null'] == 51)
check('admit-all gate reaches down to the weakest verified pair', g['admit_all_stat_min'] == 0.7)
check('meets_target false when fp rate > 1%', g['meets_target'] is False)

# ---- gate_verdict: hit / short / none / uncalibrated
G = dict(stat_min=3.673, min_tokens=100, min_coverage=0.5)
check('hit above gate, long, covered', kx.gate_verdict(4.0, 0.9, 500, G) == 'hit')
check('short when the text is below the calibrated length', kx.gate_verdict(4.0, 0.9, 60, G) == 'short')
check('none below the gate', kx.gate_verdict(3.6, 0.9, 500, G) == 'none')
check('none below the coverage floor', kx.gate_verdict(9.0, 0.4, 500, G) == 'none')
check('uncalibrated without a gate file', kx.gate_verdict(9.0, 0.9, 500, None) == 'uncalibrated')

# ---- value_freq_score + pair_stats: a true key clears a shuffled-value null on a word-valued code
# a 400-word window of the English corpus, whole-word code (the nomenclator case the 4-gram z could not see)
import re
_en = ' '.join(jp.read_corpus(p) for p in jp.LANG_CORPORA['en'])
text = ' '.join(re.findall(r"[a-z]+", _en.lower())[20000:20400])
words = text.split()
vocab = sorted(set(words))
rnd = random.Random(3)
codes = [str(100 + i) for i in range(len(vocab))]
rnd.shuffle(codes)
enc = dict(zip(vocab, codes))
key = {c: {'value': w} for w, c in enc.items()}
signs = [enc[w] for w in words]
model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA['en']])
kx.attach_freqs(model, [jp.read_corpus(p) for p in jp.LANG_CORPORA['en']])
ps = kx.pair_stats(key, signs, model, n_shuffle=20, seed=1)
check(f"word-valued true key: gated stat clears 3.673 (got {ps['own']['stat']:.2f}; z_vf {ps['own']['z_vf']:.2f})",
      ps['own']['stat'] >= 3.673)
check('value-frequency z is positive for the true key', ps['own']['z_vf'] > 0)
check('null draws are scored leave-one-out, 20 of them', len(ps['nulls']) == 20)
check('no null draw clears the true key', all(d['stat'] < ps['own']['stat'] for d in ps['nulls']))

# ---- select_since: a pair is scored when either side changed, never otherwise
keys = ['ciphers/a/key.tsv', 'ciphers/b/key.tsv']
cts = ['ciphers/a/ciphertext.tsv', 'ciphers/c/ciphertext.tsv']
sel = kx.select_since(keys, cts, {'ciphers/c/ciphertext.tsv'})
check('changed ciphertext pairs with every key', sorted(sel) == sorted([(k, 'ciphers/c/ciphertext.tsv') for k in keys]))
sel = kx.select_since(keys, cts, {'ciphers/b/key.tsv'})
check('changed key pairs with every ciphertext', sorted(sel) == sorted([('ciphers/b/key.tsv', c) for c in cts]))
check('nothing changed, nothing scored', kx.select_since(keys, cts, {'README.md'}) == [])

# ---- changed_paths on a throwaway git repo
with tempfile.TemporaryDirectory() as d:
    def git(*a):
        subprocess.run(['git', '-C', d, *a], check=True, capture_output=True)
    git('init', '-q'); git('config', 'user.email', 't@t'); git('config', 'user.name', 't')
    (Path(d) / 'ciphers' / 'a').mkdir(parents=True)
    (Path(d) / 'ciphers/a/key.tsv').write_text('1\ta\n'); git('add', '.'); git('commit', '-qm', 'one')
    base = subprocess.run(['git', '-C', d, 'rev-parse', 'HEAD'], capture_output=True, text=True).stdout.strip()
    (Path(d) / 'ciphers/a/ciphertext.tsv').write_text('1 1 1\n'); git('add', '.'); git('commit', '-qm', 'two')
    ch = kx.changed_paths(base, root=Path(d))
    check('changed_paths lists the new ciphertext only', ch == {'ciphers/a/ciphertext.tsv'})

print(f"{'OK' if not fails else 'FAILED'}: {fails} failure(s)")
sys.exit(1 if fails else 0)

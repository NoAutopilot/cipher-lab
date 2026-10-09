#!/usr/bin/env python3
"""Offline tests for tools/segmenter.py and its two wired options (MQS-SEGMENTER, 9 Oct 2026):
judge_plaintext.py --fragments K and decode_key.py --consistency --auto-segment LEX. No network.
Must catch: word boundaries ('entrenousbanque' -> 'entre nous banque', the Lasry, Biermann and Tomokiyo 2023 p.190 n.344
fixture); a fragment in a partly wrong decode; --auto-segment divides a job with no word_sep.
Must NOT flag: letters spelling no word (stay one-letter unknowns); a run of short function words only; a wholly
random decode (no fragment); a job WITH word_sep keeps its own breaks under --auto-segment.
Run: python3 tools/tests/test_segmenter.py"""
import os, random, sys, tempfile
from collections import Counter
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import segmenter as sg, judge_plaintext as jp, decode_key as dk

fails = 0
def check(ok, msg):
    global fails
    fails += not ok
    print('PASS' if ok else 'FAIL', msg)

lex = sg.Lexicon(Counter({'entre': 50, 'nous': 80, 'banque': 5, 'de': 900, 'la': 700, 'le': 800, 'en': 400, 'roi': 60,
                          'lettre': 30, 'a': 300, 'votre': 40, 'majeste': 20, 'cat': 9, 'with': 9, 'wards': 9,
                          'zap': 9, 'the': 9, 'cooperate': 9, 'cooperation': 9}))
check(sg.divided('entrenousbanque', lex) == 'entre nous banque', "'entrenousbanque' -> 'entre nous banque'")
check(all(not ok and len(t) == 1 for t, ok in sg.segment('qxzkw', lex)), 'letters spelling no word stay unknown')
f = sg.fragments('qxzkwvotremajestealettreduroiqxzk', lex, K=12)
check(bool(f) and f[0][2][:2] == ['votre', 'majeste'], f'fragment found in a partly wrong decode ({f})')
check(not sg.fragments('delaleendelaleen', lex, K=12), 'a run of function words only is not a fragment')
rnd = random.Random(3)
noise = ''.join(rnd.choice('bcdfghjklmnpqrstvwxz') for _ in range(300))
check(not sg.fragments(noise, lex, K=12), 'a consonant-noise decode lists no fragment')

# judge_plaintext --fragments: a report beside the verdict, verdict unchanged
tmp = tempfile.mkdtemp()
corp = os.path.join(tmp, 'c.txt')
open(corp, 'w').write(('votre majeste a este bien advertie de la lettre du roi et de la royne entre nous ' * 40))
spec = {'judge': {'corpora': [corp]}}
r = jp.fragments_report(spec, 'qxzwkvotremajesteaestebienadvertiekzqx', 12)
check(r['letters'] >= 20 and 'shuffles' in r['null_kind'], f"--fragments lists the run, null labelled ({r['letters']}, {r['null_kind']})")
r2 = jp.fragments_report(spec, 'votremajesteaestebienadvertie', 12, null_text='qxzwkqxzwkqxzwkqxzw')
check(r2['null_letters'] == 0 and r2['null_kind'] == 'shuffled-target decode', '--fragments-null text is the null')
check(jp.fragments_report({'judge': {}}, 'abc', 12).get('error'), 'no corpus: error, no list')

# decode_key --consistency --auto-segment
words = ['the', 'cat', 'with', 'wards', 'cooperate', 'cooperation', 'zap']
codes = {}
rows, pos = ['line\tpos\tsign\tconf'], 0
for w in words:
    for ch in w:
        codes.setdefault(ch, str(10 + len(codes))); rows.append(f'L1\t{pos}\t{codes[ch]}\t'); pos += 1
    rows.append(f'L1\t{pos}\t/\t'); pos += 1
open(os.path.join(tmp, 'ciphertext.tsv'), 'w').write('\n'.join(rows) + '\n')
open(os.path.join(tmp, 'key.tsv'), 'w').write('code\tvalue\n' + ''.join(f'{c}\t{v}\n' for v, c in codes.items()))
rr, meta = dk.consistency(tmp, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'nonsign': ['/']},
                          segment_text=('auto', 'test', lex))
check(rr is not None and meta['words'] == 7 and '--auto-segment' in meta['how'],
      f"--auto-segment divides a job without word_sep ({meta['words']} words; {meta['how']})")
rr2, meta2 = dk.consistency(tmp, {'ciphertext': 'ciphertext.tsv', 'key': 'key.tsv', 'word_sep': '/', 'nonsign': ['/']},
                            segment_text=('auto', 'test', lex))
check(meta2['how'].startswith('word_sep'), 'a job with word_sep keeps its own breaks under --auto-segment')
print(f'test_segmenter: {fails} failures')
sys.exit(1 if fails else 0)

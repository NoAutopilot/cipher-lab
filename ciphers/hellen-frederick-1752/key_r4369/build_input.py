#!/usr/bin/env python3
"""UNA-HELLEN (9 Oct 2026): the input layer that adopts the image corrections into the counted R4369 reading.
Reads R1953_pipe.txt (DECODE's transcription, as ciphertext_R1953.txt; never modified) and applies, in order,
  1. ../image_check_r1953/corrections.tsv, confidence high + medium (R7A-HEL53, 6 Oct 2026; one medium row splits 1426903
     into 1426 903, so positions after 386 shift by one), then
  2. ../zero_eight/corrections.tsv, confidence high only (R8-HEL, 6 Oct 2026; 'ambiguous' rows are listed, never applied;
     positions are in the post-split stream; a settled doubt mark '?' is dropped),
and writes R1953_pipe_img.txt, which decode.json's first job decodes into the counted reading reading_R1953_img.txt.
The result must equal ../zero_eight/R1953_pipe_08.txt token for token (asserted). The DECODE-transcription reading
(reading_R1953.txt, second job) is kept unchanged because retired tests (key_r4372/diag.py, key_r4386, key_r4388,
key_rebuild) read its tokens file and must stay reproducible.
Usage: python3 build_input.py [--check]   (--check: exit 1 if R1953_pipe_img.txt is stale)"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
UP = os.path.join(HERE, '..')
src = open(os.path.join(HERE, 'R1953_pipe.txt')).read().split()
head, toks = src[:3], src[3:]
assert len(toks) == 846, len(toks)
n7 = n8 = 0
for r in csv.DictReader(open(os.path.join(UP, 'image_check_r1953', 'corrections.tsv')), delimiter='\t'):
    if r['confidence'] in ('high', 'medium'):
        toks[int(r['pos'])] = r['image_value']
        n7 += 1
toks = ' '.join(toks).split()  # the 1426 903 split becomes two groups
assert len(toks) == 847, len(toks)
for r in csv.DictReader(open(os.path.join(UP, 'zero_eight', 'corrections.tsv')), delimiter='\t'):
    if r['confidence'] != 'high':
        continue
    p = int(r['pos'])
    assert toks[p].strip('_=?') == r['decode_tx'], (p, toks[p], r['decode_tx'])
    toks[p] = toks[p].replace(r['decode_tx'], r['image_value']).replace('?', '')
    n8 += 1
out = ' '.join(head + toks) + '\n'
ref = open(os.path.join(UP, 'zero_eight', 'R1953_pipe_08.txt')).read().split()
assert out.split() == ref, 'differs from zero_eight/R1953_pipe_08.txt'
path = os.path.join(HERE, 'R1953_pipe_img.txt')
if '--check' in sys.argv:
    ok = os.path.exists(path) and open(path).read() == out
    print('R1953_pipe_img.txt up to date' if ok else 'R1953_pipe_img.txt STALE')
    sys.exit(0 if ok else 1)
open(path, 'w').write(out)
print(f'{n7} R7A-HEL53 + {n8} R8-HEL corrections applied; {len(toks)} tokens; equals zero_eight/R1953_pipe_08.txt')

#!/usr/bin/env python3
"""A2-HAR6 (3 Oct 2026): known-answer check of run_align.py's pipeline (rule 3). Builds a synthetic gloss_pairs file of the
same shape (11 pairs, 7 gloss words each, f.84r's own gloss wording as plaintext, a random 28-sign substitution, 10% sign
error) in a temp dir and runs a copy of run_align.py on it. Expected: consistency well above both nulls.
    python3 known_answer.py
"""
import os, random, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.abspath(os.path.join(HERE, '..', '..', '..', 'tools', 'interlinear_align.py'))
TXT = ("the answers brought us by norice after three dayes attendaunce doe shewe smal hope of any good successe in the great "
       "cause therfore we must go from hence and that by sea it were to represent that we pretending to go to calays and "
       "there to press them resolutely whether they wil condescend to the three poyntes propounded which being refused her "
       "maiestie may with honor break of and we retyre home")
d = tempfile.mkdtemp()
src = open(os.path.join(HERE, 'run_align.py'), encoding='utf-8').read()
src = '\n'.join("TOOL = %r" % TOOL if l.startswith('TOOL = ') else l for l in src.split('\n'))
open(os.path.join(d, 'run_align.py'), 'w', encoding='utf-8').write(src)
words, rng = TXT.split(), random.Random(5)
signs = list("UA+8DT7HGhIklm#nzdcpVy:wXQLK")
key = {ch: signs[i % len(signs)] for i, ch in enumerate("abcdefghijklmnopqrstuvwxyz")}
rows, i, b = [], 0, 0
while i < len(words):
    w = words[i:i + 7]; i += 7; b += 1
    toks = ' / '.join(' '.join(key[ch] for ch in x) for x in w).split(' ')
    toks = [t if t == '/' or rng.random() > 0.1 else rng.choice(signs) for t in toks]
    rows.append('f84r\tL%02d\t1\t%s\t%s' % (b, ' '.join(w), ' '.join(toks)))
open(os.path.join(d, 'gloss_pairs.tsv'), 'w').write('page\tband\tpair\tgloss\tcipher\n' + '\n'.join(rows) + '\n')
sys.exit(subprocess.run([sys.executable, os.path.join(d, 'run_align.py')], cwd=d).returncode)

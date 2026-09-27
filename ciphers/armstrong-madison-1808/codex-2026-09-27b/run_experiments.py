"""Reproduce the provisional Armstrong glyph experiments; no decipherment claimed."""
from pathlib import Path
import subprocess
import sys

D = Path(__file__).resolve().parent

def run(*args):
    subprocess.run([str(a) for a in args], cwd=D, check=True)

run(sys.executable, D / 'glyph_prepare.py')
run(sys.executable, D / 'glyph_variants.py')
run('g++', '-O3', '-std=c++17', D / 'glyph_solve.cpp', '-o', D / 'glyph_solve')
for name in ['glyph', 'control0', 'control1', 'control2', 'control3', 'shuffle0', 'shuffle1', 'shuffle2']:
    run(D / 'glyph_solve', 'glyph_lm.bin', name + '.seq', 150, 30000, 2, name + '_result.tsv')
for name in ['glyph', 'control0', 'control1', 'control2', 'control3']:
    run(D / 'glyph_solve', 'glyph_lm.bin', name + '.seq', 1000, 60000, 2, name + '_strong.tsv')
for name, model, sequence, cap in [
    ('glyph_fr', 'glyph_fr_lm.bin', 'glyph.seq', 2),
    ('glyph_consonants', 'glyph_consonants_lm.bin', 'glyph.seq', 3),
    ('separator65', 'glyph_lm.bin', 'separator65.seq', 2),
    ('coarsemerge', 'glyph_lm.bin', 'coarsemerge.seq', 2),
]:
    run(D / 'glyph_solve', model, sequence, 150, 30000, cap, name + '_result.tsv')
run(sys.executable, D / 'summarize.py')

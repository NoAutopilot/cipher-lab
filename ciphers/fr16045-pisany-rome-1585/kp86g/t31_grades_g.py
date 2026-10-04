#!/usr/bin/env python3
"""PIS1-247 (PREREG kp86g, grades paragraph): kp86e/t31_grades.py run UNCHANGED except file paths -- page 3 becomes
f.247r (tx86g/ciphertext_f247r.tsv vs kp86g/colbert_f247r.txt), outputs go to kp86g/ (t31_witness.tsv, grades_f247r.tsv)
so kp86e's committed files are untouched. Source is read, paths substituted as strings, then executed.
    python3 kp86g/t31_grades_g.py --grade"""
import os
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(HERE)
src = open(os.path.join(T, 'kp86e', 't31_grades.py')).read()
for a, b in [("('4 Nov 1586 f.275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt')",
              "('17 Sept 1586 (second) f.247r', 'tx86g/ciphertext_f247r.tsv', 'kp86g/colbert_f247r.txt')"),
             ("os.path.join(H, 't31_witness.tsv')", "os.path.join(T, 'kp86g', 't31_witness.tsv')"),
             ("os.path.join(H, 'grades_f275r.tsv')", "os.path.join(T, 'kp86g', 'grades_f247r.tsv')"),
             ("'f.275r grades'", "'f.247r grades'")]:
    assert a in src, a
    src = src.replace(a, b)
exec(compile(src, os.path.join(T, 'kp86e', 't31_grades.py'), 'exec'), {'__file__': os.path.join(T, 'kp86e', 't31_grades.py'), '__name__': '__main__'})

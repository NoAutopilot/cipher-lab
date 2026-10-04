#!/usr/bin/env python3
"""PIS1-275V (PREREG kp86f, grades paragraph): kp86e/t31_grades.py run with ONLY its file paths changed -- the third page
becomes f.275v (tx86f/ciphertext_f275v.tsv vs kp86f/colbert_f275v.txt) and both outputs go to kp86f/ (t31_witness.tsv,
grades_f275v.tsv). Alignment, grade rule and the T31-held-at-M rule are the original code, executed unchanged.
    python3 kp86f/grades_f275v.py [--grade]   (--grade only when kp86f arm A is a licensed PASS)"""
import os
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
src = open(os.path.join(T, 'kp86e', 't31_grades.py')).read()
for a, b in (("('4 Nov 1586 f.275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt')",
              "('4 Nov 1586 f.275v', 'tx86f/ciphertext_f275v.tsv', 'kp86f/colbert_f275v.txt')"),
             ("'grades_f275r.tsv'", "'grades_f275v.tsv'"), ("'f.275r grades'", "'f.275v grades'")):
    assert src.count(a) == 1, a; src = src.replace(a, b)
g = {'__file__': os.path.join(H, 't31_grades.py'), '__name__': '__main__'}
exec(compile(src, 't31_grades.py (paths -> f.275v)', 'exec'), g)

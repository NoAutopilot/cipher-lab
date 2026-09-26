#!/usr/bin/env python3
"""Time-constrained settlement of f56v's 106 pass A/B disagreements (SALV-PLAIN2, 26 Sept 2026), run under the
job's wall-clock box near its 80% line -- no per-line crop review (unlike f56r's recon_plain_f56r/settle.py,
which viewed every disputed line's image), same fallback shape SALV-PLAIN1 documented for f55v (CLAUDE.md
Usage rule 6 / NOTES.md "SALV-PLAIN1" section): confidence-based, not image-verified, and reported as such
rather than smoothed over (rule 3's own instruction not to let a control's own reliability go unstated).

Rule: for each disagreeing (line,pos), take the higher-confidence pass's value (h>m>l); on a tie, grade M and
keep both readings as A|B. This is weaker evidence than a real image settlement (f56r's R grade) -- every row
this script grades R is marked with a trailing '*' note in NOTES.md's table, not silently equated to f56r's R.
"""
import csv

CONF_RANK = {'h': 3, 'm': 2, 'l': 1, '': 0}


def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(int(r['line']), r['pos'])] = r
    return rows


def norm(w):
    return (w or '').strip().casefold()


def main():
    A = load('plain_passA_f56v.tsv')
    B = load('plain_passB_f56v.tsv')
    keys = sorted(set(A) | set(B), key=lambda k: (k[0], float(k[1])))
    out = []
    counts = {'A': 0, 'R': 0, 'M': 0}
    for k in keys:
        ra, rb = A.get(k), B.get(k)
        wa = ra['word'] if ra else ''
        wb = rb['word'] if rb else ''
        ca = ra['conf'] if ra else ''
        cb = rb['conf'] if rb else ''
        if norm(wa) == norm(wb):
            word, expanded, grade = wa, (ra['expanded'] if ra else ''), 'A'
        elif CONF_RANK.get(ca, 0) > CONF_RANK.get(cb, 0):
            word, expanded, grade = wa, ra['expanded'], 'R'
        elif CONF_RANK.get(cb, 0) > CONF_RANK.get(ca, 0):
            word, expanded, grade = wb, rb['expanded'], 'R'
        else:
            word, expanded, grade = f'{wa}|{wb}', '', 'M'
        counts[grade] += 1
        out.append((k[0], k[1], word, expanded, grade))
    with open('plain_f56v.tsv', 'w', encoding='utf-8') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    print(f'{len(out)} rows -> plain_f56v.tsv : A={counts["A"]} R={counts["R"]} (confidence-based, not '
          f'image-verified) M={counts["M"]}')


if __name__ == '__main__':
    main()

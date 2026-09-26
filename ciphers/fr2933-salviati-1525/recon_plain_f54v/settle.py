#!/usr/bin/env python3
"""Manual settlement of f54v's 64 pass A/B disagreements (recon_plain_f54v/disagreements.tsv), decided by the
worker from plain_crops/f54v/L*.png (SALV-PLAIN1, 26 Sept 2026). See recon_plain_f54r/settle.py for the method.
Positions not listed here agreed between passes A and B (grade A, value taken as passA's literal reading).
For lines 16 and 17 (long legible stretches where the two passes' word content agreed but their box-to-word
segmentation disagreed throughout the line), passA's segmentation was adopted whole (finer-grained, consistently
h-confidence, and the one that matches the visible box spacing) rather than settled position by position.
"""
import csv

SETTLED = {
    (4, 4): ('+|[C]', '', 'M'),
    (4, 22): ('+|[C]', '', 'M'),
    (4, 30): ('+|[C]', '', 'M'),
    (6, 22): ('+|[C]', '', 'M'),
    (7, 6): ('mettera', '', 'R'),
    (7, 10): ('+', '', 'R'),
    (7, 23): ('H', '', 'R'),
    (7, 26): ('Doma~', 'Domane', 'R'),
    (8, 1): ('Sono', '', 'R'),
    (8, 3): ('vuole', '', 'R'),
    (8, 5): ('.s.', '', 'R'),
    (8, 7): ('M.tn', '', 'R'),
    (8, 9): ('+', '', 'R'),
    (8, 10): ('vt', '', 'R'),
    (8, 11): ('liberare', '', 'R'),
    (8, 15): ('tutta', '', 'R'),
    (8, 17): ('questa', '', 'R'),
    (8, 19): ('+', '', 'R'),
    (8, 23): ('sta?|gt', '', 'M'),
    (8, 25): ('altri', '', 'R'),
    (8, 26): ('+', '', 'R'),
    (11, 11): ('aggiungere', '', 'R'),
    (11, 15): ('levare', '', 'R'),
    (11, 16): ('+', '', 'R'),
    (11, 17): ('+', '', 'R'),
    (11, 18): ('+', '', 'R'),
    (12, 23): ('parrà', '', 'R'),
    (12, 28): ('expe~', 'espediente', 'R'),
    (13, 1): ('Sarà', '', 'R'),
    (13, 5): ('et', '', 'R'),
    (14, 5): ('Cosi', '', 'R'),
    (14, 7): ('vogliono', '', 'R'),
    (15, 11): ('Contra', '', 'R'),
    (15, 13): ('+', '', 'R'),
    (15, 14): ('Turchi', '', 'R'),
    (15, 19): ('luterani', '', 'R'),
    (15, 20): ('et', '', 'R'),
    (15, 23): ('Potr~', 'Potentati', 'R'),
    # line 16: passA's segmentation adopted whole (see docstring)
    (16, 1): ('essere', '', 'R'),
    (16, 2): ('+', '', 'A'),
    (16, 4): ('che', '', 'R'),
    (16, 5): ('+', '', 'A'),
    (16, 7): ('Gra~', 'Gran', 'R'),
    (16, 9): ('Cancellieri', 'Cancelliere', 'R'),
    (16, 10): ('+', '', 'A'),
    (16, 13): ('mi', '', 'R'),
    (16, 14): ('mandera', '', 'R'),
    (16, 15): ('+', '', 'A'),
    (16, 17): ('la', '', 'R'),
    (16, 18): ('nota', '', 'R'),
    (16, 19): ('d\'', 'di', 'R'),
    (16, 20): ('quello', '', 'R'),
    (16, 23): ('vogliono', '', 'R'),
    # line 17: passA's segmentation adopted whole (see docstring)
    (17, 3): ('+', '', 'A'),
    (17, 5): ('quanti', '', 'R'),
    (17, 8): ('et', '', 'R'),
    (17, 9): ('questo', '', 'R'),
    (17, 10): ('Corrieri', '', 'R'),
    (17, 12): ('+', '', 'A'),
    (17, 13): ('Parigi', '', 'R'),
    (17, 16): ('et', '', 'R'),
    (17, 17): ('lamandero', 'la manderò', 'R'),
    (17, 18): ('+', '', 'A'),
}

# mark-only disagreements the diff script's case-fold normalisation missed (rule 3, PX-BRODEC): same word,
# differing only in an apostrophe/abbreviation stroke -- grade A, keep the fuller reading.
MARK_ONLY = {
    (7, 4): "gh'",
}


def main():
    a_rows = {(int(r['line']), r['pos']): r for r in csv.DictReader(open('plain_passA_f54v.tsv'), delimiter='\t')}
    out = []
    for (line, pos), ra in sorted(a_rows.items(), key=lambda kv: (kv[0][0], float(kv[0][1]))):
        key = (line, int(float(pos)))
        if key in SETTLED:
            word, expanded, grade = SETTLED[key]
        elif key in MARK_ONLY:
            word, expanded, grade = MARK_ONLY[key], '', 'A'
        else:
            word, expanded, grade = ra['word'], ra['expanded'], 'A'
        out.append((line, pos, word, expanded, grade))
    with open('plain_f54v.tsv', 'w') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    n = len(out)
    counts = {}
    for *_, g in out:
        counts[g] = counts.get(g, 0) + 1
    print(f'plain_f54v.tsv: {n} rows; grade counts {counts}')


if __name__ == '__main__':
    main()

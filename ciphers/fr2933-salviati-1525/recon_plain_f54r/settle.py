#!/usr/bin/env python3
"""Manual settlement of f54r's 69 pass A/B disagreements (recon_plain_f54r/disagreements.tsv), decided by the
worker from plain_crops/f54r/L*.png (SALV-PLAIN1, 26 Sept 2026). Not a general tool -- one-off per leaf, kept
here for the record next to disagreements.tsv. Positions not listed here agreed between passes A and B (grade A,
value taken as passA's literal reading).

grade R = settled from the image, one of the two pass readings (or a corrected reading) chosen.
grade M = unsettled/illegible even from the image; word field keeps both readings as A|B.
"""
import csv

# (line, pos) -> (word, expanded, grade)
SETTLED = {
    (1, 3): ('tanq3|<none>', '', 'M'),
    (1, 4): ('+|ang~', '', 'M'),
    (1, 8): ('q;|<none>', '', 'M'),
    (1, 9): ('c9|cq', '', 'M'),
    (1, 12): ('Ch|[C]', '', 'M'),
    (2, 18): ('ri|[C]', '', 'M'),
    (3, 11): ('d|[C]', '', 'M'),
    (3, 17): ('quello', '', 'R'),
    (3, 18): ('+', '', 'R'),
    (3, 23): ('desidera', '', 'R'),
    (3, 25): ('+', '', 'R'),
    (3, 28): ('N.', 'Nostro', 'R'),
    (3, 29): ('S.', 'Signore', 'R'),
    (4, 4): ('?|[C]', '', 'M'),
    (5, 12): ('?|[C]', '', 'M'),
    (5, 18): ('my', '', 'R'),
    (5, 25): ('dic', '', 'R'),
    (6, 15): ('?|[C]', '', 'M'),
    (7, 7): ('?|[C]', '', 'M'),
    (8, 11): ('?|[C]', '', 'M'),
    (8, 14): ('a|[C]', '', 'M'),
    (9, 2): ('<none>', '', 'R'),
    (9, 9): ('mh', '', 'R'),
    (9, 15): ('+', '', 'R'),
    (9, 16): ('+', '', 'R'),
    (9, 17): ('?|[C]', '', 'M'),
    (9, 20): ('?|[C]', '', 'M'),
    (9, 22): ('?|[C]', '', 'M'),
    (10, 17): ('ys', '', 'R'),
    (11, 14): ('m|[C]', '', 'M'),
    (12, 3): ('?|[C]', '', 'M'),
    (12, 26): ('?|[C]', '', 'M'),
    (13, 2): ('?|[C]', '', 'M'),
    (13, 9): ('?|[C]', '', 'M'),
    (13, 23): ('amt', '', 'R'),
    (13, 24): ('+', '', 'R'),
    (14, 1): ('H', '', 'R'),
    (14, 10): ('M|[C]', '', 'M'),
    (14, 19): ('lryy|[C]', '', 'M'),
    (15, 5): ('la', '', 'R'),
    (15, 6): ('cosi', 'così', 'R'),
    (15, 14): ('Come', '', 'R'),
    (15, 19): ('Pure', '', 'R'),
    (15, 20): ('+', '', 'R'),
    (16, 3): ('quello', '', 'R'),
    (16, 4): ('+', '', 'R'),
    (16, 7): ('ch~', 'che', 'R'),
    (16, 11): ('li', '', 'R'),
    (16, 13): ('Parra', 'Parrà', 'R'),
    (16, 15): ('e', '', 'R'),
    (16, 17): ('Piaciuto', '', 'R'),
    (16, 19): ('a.s.M~tr', 'a Sua Maestà', 'R'),
    (16, 20): ('+', '', 'R'),
    (16, 29): ('di', '', 'R'),
    (17, 3): ('?|[C]', '', 'M'),
    (17, 25): ('Con', '', 'R'),
    (17, 26): ('+', '', 'R'),
    (18, 8): ('lx|[C]', '', 'M'),
    (18, 10): ('lx|[C]', '', 'M'),
    (18, 19): ('y|[C]', '', 'M'),
    (18, 20): ('o|[C]', '', 'M'),
    (18, 22): ('oppinjoni', 'opinioni', 'R'),
    (19, 1): ('dj', '', 'R'),
    (19, 25): ('ad', '', 'R'),
    (19, 28): ('e', '', 'R'),
}

# mark-only disagreements the diff script's case-fold normalisation missed (rule 3, PX-BRODEC): the two
# passes read the same word, differing only in whether they wrote the abbreviation tilde -- grade A, keep
# the fuller (marked) form as the canonical reading.
MARK_ONLY = {
    (1, 2): 'Dnt~',
    (1, 6): 'Ptr~',
    (3, 20): 'ch.',
    (5, 19): 'h~n',
}


def main():
    a_rows = {(int(r['line']), r['pos']): r for r in csv.DictReader(open('plain_passA_f54r.tsv'), delimiter='\t')}
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
    with open('plain_f54r.tsv', 'w') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    n = len(out)
    counts = {}
    for *_, g in out:
        counts[g] = counts.get(g, 0) + 1
    print(f'plain_f54r.tsv: {n} rows; grade counts {counts}')


if __name__ == '__main__':
    main()

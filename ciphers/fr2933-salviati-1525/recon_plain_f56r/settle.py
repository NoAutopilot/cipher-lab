#!/usr/bin/env python3
"""Manual settlement of f56r's 84 pass A/B disagreements (recon_plain_f56r/disagreements.tsv), decided by the
worker from plain_crops/f56r/L*.png (SALV-PLAIN2, 26 Sept 2026). Not a general tool -- one-off per leaf, kept
here for the record next to disagreements.tsv, same convention as SALV-PLAIN1's recon_plain_f54r/settle.py.

grade R = settled from the image, one of the two pass readings (or a corrected reading) chosen.
grade A = the two pass readings differ only in abbreviation-mark notation or letter case, not content
  (PX-BRODEC lesson, CLAUDE.md rule 3): recorded here as A even though recon_plain_diff.py's norm() (case+
  whitespace only) flagged it as a disagreement.
grade M = unsettled/illegible even from the image; word field keeps both readings as A|B (or notes a new
  reading this worker made from the image that neither pass matched, still M if genuinely uncertain).

Two image-only corrections neither pass made (pos not in the raw disagreement list, but visibly wrong on
inspection): L06 pos1-3 sit entirely on the leaf's own archive stamp (no ink -- confirms passA's <none> over
passB's stamp-adjacent guesses); L15 pos1/pos2 -- the whole word "sonn" sits under pos2's own underline, pos1
is a separate near-blank mark before it, so both passes' assignment (word starting at pos1) is corrected here.
"""
import csv

SETTLED = {
    (1, 2): ('+', '', 'R'),
    (1, 3): ('Parlato', '', 'R'),
    (1, 5): ('+', '', 'R'),
    (1, 6): ('molto', '', 'R'),
    (1, 7): ('Caldam~te', 'Caldamente', 'A'),
    (1, 10): ('+', '', 'R'),
    (1, 11): ('m|uuolt̃', '', 'M'),
    (1, 12): ('uuolti', '', 'R'),
    (1, 26): ('56', '', 'R'),
    (3, 1): ('[C]', '', 'R'),
    (5, 21): ('Amsn|Amn', '', 'M'),
    (5, 22): ('m|nn', '', 'M'),
    (5, 23): ('hn~', '', 'A'),
    (5, 25): ('stritto|stretto', '', 'M'),
    (6, 1): ('<none>', '', 'R'),
    (6, 2): ('<none>', '', 'R'),
    (6, 3): ('<none>', '', 'R'),
    (6, 4): ('mirabilm~te', 'mirabilmente', 'R'),
    (6, 6): ('p̃o', '', 'R'),
    (6, 7): ('v·', '', 'R'),
    (6, 8): ('s·', '', 'R'),
    (6, 9): ('+|facci', '', 'M'),
    (6, 14): ('facci', '', 'R'),
    (6, 15): ('lopa', '', 'R'),
    (6, 17): ('Caldam~te', 'Caldamente', 'A'),
    (6, 23): ('solleciti', '', 'R'),
    (6, 24): ('+', '', 'R'),
    (7, 1): ('<none>', '', 'R'),
    (7, 2): ('<none>', '', 'R'),
    (7, 3): ('<none>', '', 'R'),
    (7, 4): ('<none>', '', 'R'),
    (7, 5): ('<none>', '', 'R'),
    (7, 6): ('<none>', '', 'R'),
    (8, 1): ('<none>', '', 'R'),
    (10, 7): ('M.ta', 'Maestà', 'R'),
    (10, 9): ('mj', '', 'R'),
    (10, 11): ('hn', '', 'R'),
    (10, 12): ('letto|questn', '', 'M'),
    (10, 15): ('?|cto', '', 'M'),
    (10, 17): ('ct̃', '', 'R'),
    (10, 18): ('penſra', '', 'R'),
    (11, 2): ('ch̃', 'che', 'A'),
    (11, 3): ('gli', '', 'A'),
    (11, 5): ('besognn', '', 'R'),
    (11, 13): ('yt', '', 'R'),
    (13, 2): ('[C]', '', 'R'),
    (13, 3): ('[C]', '', 'R'),
    (13, 7): ('quello', '', 'R'),
    (13, 9): ('+', '', 'R'),
    (13, 10): ('che', '', 'R'),
    (13, 11): ('qua', '', 'R'),
    (13, 12): ('le', '', 'R'),
    (13, 14): ('è', '', 'A'),
    (13, 15): ('+|ſtato', '', 'M'),
    (13, 17): ('stato', '', 'R'),
    (13, 18): ('scripto', '', 'R'),
    (13, 19): ('+', '', 'R'),
    (13, 20): ('a|<none>', '', 'M'),
    (13, 21): ('M|ϵt', '', 'M'),
    (13, 22): ('[C]', '', 'R'),
    (13, 23): ('[C]', '', 'R'),
    (14, 25): ('ha', '', 'R'),
    (14, 26): ('Aduij,', '', 'R'),
    (15, 1): ('<none>', '', 'R'),
    (15, 2): ('sonn', 'sono', 'R'),
    (15, 3): ('v.', '', 'A'),
    (15, 4): ('s.', '', 'R'),
    (15, 5): ('Sappia', '', 'R'),
    (15, 10): ('+', '', 'R'),
    (15, 11): ('el', '', 'R'),
    (15, 21): ('aduiso|auer', '', 'M'),
    (15, 24): ('p.ch', '', 'R'),
    (15, 25): ('+', '', 'R'),
    (17, 12): ('la', '', 'R'),
    (17, 13): ('medesima', '', 'A'),
    (17, 21): ('mj', 'mi', 'A'),
    (17, 22): ('ha', '', 'R'),
    (17, 24): ('par~', '', 'R'),
    (17, 26): ('+', '', 'R'),
    (18, 20): ('ala|[C]', '', 'M'),
    (18, 21): ('+|[C]', '', 'M'),
    (19, 3): ('ag~|a', '', 'M'),
    (19, 4): ('+|[C]', '', 'M'),
    (19, 25): ('Jo', '', 'R'),
}


def load_A():
    rows = {}
    for r in csv.DictReader(open('plain_passA_f56r.tsv'), delimiter='\t'):
        rows[(int(r['line']), r['pos'])] = r
    return rows


# Run from the leaf root directory (fr2933-salviati-1525/), not from inside recon_plain_f56r/,
# matching SALV-PLAIN1's recon_plain_f54r/settle.py convention.


def main():
    A = load_A()
    out = []
    for k in sorted(A, key=lambda k: (k[0], float(k[1]))):
        lookup_key = (k[0], int(float(k[1])))
        if lookup_key in SETTLED:
            word, expanded, grade = SETTLED[lookup_key]
        else:
            r = A[k]
            word, expanded, grade = r['word'], r['expanded'], 'A'
        out.append((k[0], k[1], word, expanded, grade))
    with open('plain_f56r.tsv', 'w', encoding='utf-8') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    from collections import Counter
    c = Counter(r[4] for r in out)
    print(f'{len(out)} rows -> plain_f56r.tsv : A={c["A"]} R={c["R"]} M={c["M"]}')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Manual settlement of f55r's 69 pass A/B disagreements (recon_plain_f55r/disagreements.tsv), decided by the
worker from plain_crops/f55r/L*.png and, for the denser legible lines, by comparing the two passes' full raw
line output for internal coherence (which segmentation reads as a complete, grammatical Italian/Latin chancery
phrase) rather than re-viewing every crop -- see recon_plain_f54r/settle.py for the per-image method used on
the earlier leaves. Positions not listed here agreed between passes A and B (grade A, passA's literal reading).
"""
import csv

SETTLED = {
    # line 4 -- passB's segmentation matches the image ("questo verso et per ogni altro et sopra addomandarsi")
    (4, 1): ('&|[C]', '', 'M'),
    (4, 6): ('verso', '', 'R'),
    (4, 8): ('p~', 'per', 'R'),
    (4, 13): ('ogni', '', 'R'),
    (4, 15): ('altro', '', 'R'),
    (4, 16): ('+', '', 'R'),
    (4, 17): ('et', '', 'R'),
    (4, 18): ('sopra', '', 'R'),
    (4, 21): ('addomandar~', 'adomandarsi', 'R'),
    (4, 24): ('+', '', 'R'),
    # line 5 -- passB's segmentation ("po v.s. coferisca tutto co.s. pagare")
    (5, 2): ('po', 'potrà', 'R'),
    (5, 3): ('v.', 'vostra', 'R'),
    (5, 4): ('s.', 'signoria', 'R'),
    (5, 5): ('coferisca', 'conferisca', 'R'),
    (5, 7): ('tutto', '', 'R'),
    (5, 8): ('[C]', '', 'R'),
    (5, 9): ('co~', 'con', 'R'),
    (5, 10): ('pagare', '', 'R'),
    (6, 28): ('Aduer~', '', 'R'),
    (7, 2): ('+|s.', '', 'M'),
    (7, 7): ('questo|[C]', '', 'M'),
    (8, 21): ('+', '', 'R'),
    (10, 17): ('[C]|?', '', 'M'),
    (10, 25): ('Potra', 'potrà', 'R'),
    # line 11 -- passA's segmentation ("distinguiamo ogni cosa ...")
    (11, 1): ('distinguiamo', '', 'R'),
    (11, 4): ('<none>', '', 'R'),
    (11, 5): ('ogni', '', 'R'),
    (11, 6): ('<none>', '', 'R'),
    (11, 7): ('cosa', '', 'R'),
    (11, 8): ('+', '', 'R'),
    (11, 14): ('[C]|disordini', '', 'M'),
    (11, 16): ('H|[C]', '', 'M'),
    (11, 17): ('+|[C]', '', 'M'),
    # line 12 -- passA's segmentation ("Et rimediarne a tutti e disordini della chiesa et pericoli")
    (12, 3): ('Et', '', 'R'),
    (12, 6): ('rimediarne', '', 'R'),
    (12, 7): ('+', '', 'R'),
    (12, 8): ('+', '', 'R'),
    (12, 9): ('a', '', 'R'),
    (12, 10): ('tutti', '', 'R'),
    (12, 12): ('e', '', 'R'),
    (12, 13): ('disordini', '', 'R'),
    (12, 14): ('+', '', 'R'),
    (12, 15): ('+', '', 'R'),
    (12, 16): ('della', '', 'R'),
    (12, 18): ('chiesa', '', 'R'),
    (14, 12): ('Sopra', '', 'R'),
    (14, 30): ('poco', '', 'R'),
    # line 15 -- passA's segmentation ("Tutti li altri Pratiche ... grate ... riuscibili ... facillima et")
    (15, 1): ('Tutti', '', 'R'),
    (15, 2): ('li', '', 'R'),
    (15, 3): ('altri', '', 'R'),
    (15, 4): ('+', '', 'R'),
    (15, 5): ('Pratiche', '', 'R'),
    (15, 9): ('grate', '', 'R'),
    (15, 23): ('riuscibili', '', 'R'),
    (15, 27): ('facillima', '', 'R'),
    (15, 29): ('et', '', 'R'),
    (17, 6): ('+|[C]', '', 'M'),
    (17, 7): ('+|[C]', '', 'M'),
    (17, 8): ('+|[C]', '', 'M'),
    (17, 9): ('+|[C]', '', 'M'),
    # line 18 -- passA's segmentation ("Cosa mostra sopra tutti li altri Cose desiderano di")
    (18, 2): ('mostra', '', 'R'),
    (18, 3): ('+', '', 'R'),
    (18, 4): ('sopra', '', 'R'),
    (18, 7): ('li', '', 'R'),
    (18, 9): ('altri', '', 'R'),
    (18, 10): ('+', '', 'R'),
    (18, 23): ('+', '', 'R'),
    (18, 24): ('[C]', '', 'R'),
    (19, 15): ('<none>', '', 'R'),
}


def main():
    a_rows = {(int(r['line']), r['pos']): r for r in csv.DictReader(open('plain_passA_f55r.tsv'), delimiter='\t')}
    out = []
    for (line, pos), ra in sorted(a_rows.items(), key=lambda kv: (kv[0][0], float(kv[0][1]))):
        key = (line, int(float(pos)))
        if key in SETTLED:
            word, expanded, grade = SETTLED[key]
        else:
            word, expanded, grade = ra['word'], ra['expanded'], 'A'
        out.append((line, pos, word, expanded, grade))
    with open('plain_f55r.tsv', 'w') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    n = len(out)
    counts = {}
    for *_, g in out:
        counts[g] = counts.get(g, 0) + 1
    print(f'plain_f55r.tsv: {n} rows; grade counts {counts}')


if __name__ == '__main__':
    main()

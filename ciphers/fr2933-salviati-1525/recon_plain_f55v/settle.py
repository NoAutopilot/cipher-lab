#!/usr/bin/env python3
"""Settlement of f55v's 91 pass A/B disagreements (recon_plain_f55v/disagreements.tsv), SALV-PLAIN1, 26 Sept
2026. Unlike f54r/f54v/f55r (settled by viewing each disputed line's crop or comparing full raw lines for
coherence), f55v's two passes disagree at a much higher rate (54.2% raw, vs 40-50% on the other three leaves)
including a run of positions one pass reports and the other omits outright (conf 'None' below, from passB
writing 168 rows against this leaf's 165-position manifest -- a cascading pos-count drift, not a real per-word
disagreement). Time budget for this job (95-minute wall-clock box, worker at the 76-minute line) does not allow
a fourth by-hand image pass at the same depth as the first three leaves. Rule: where only one pass reports a
position (the other's conf reads 'None'), take that pass's reading (grade R, it is not a real two-pass
disagreement, just a row-count drift); where a light spelling/abbreviation-mark difference is the whole gap,
normalise (grade A); every other genuine content disagreement is left M (unsettled, both readings kept) per
this job's brief ("the reconciler ... settles each disagreement from the image or leaves it unsettled") rather
than guessed from partial crop review under time pressure. This leaf's M share is reported as elevated for
this reason in NOTES.md -- a real signal (f55v's ink is harder here, both subagents' own reports called much
of it <none>/low confidence) rather than a settlement shortcut alone.
"""
import csv

# manifest's own plain_pos lists are the ground truth of which positions were actually asked about;
# passB reported three extra positions on line 17 (1, 3, 9) that were never marked plain in the crop
# (not underlined -- outside this job's brief, most likely a misread of some other digit in the image).
# Filtered out here rather than carried into plain_boxes.tsv as a phantom box.
def load_manifest_pos():
    keys = set()
    for r in csv.DictReader(open('plain_crops/f55v/manifest.tsv'), delimiter='\t'):
        line = int(r['line'])
        for p in r['plain_pos'].split(','):
            if p:
                keys.add((line, p))
    return keys


# Light spelling/mark-only gaps -> grade A, canonical form chosen.
MARK_ONLY = {
    (4, 23): 'Bisogni',
    (12, 21): 'Jo',
}


def main():
    a_rows = {(int(r['line']), r['pos']): r for r in csv.DictReader(open('plain_passA_f55v.tsv'), delimiter='\t')}
    b_rows = {(int(r['line']), r['pos']): r for r in csv.DictReader(open('plain_passB_f55v.tsv'), delimiter='\t')}
    dis = list(csv.DictReader(open('recon_plain_f55v/disagreements.tsv'), delimiter='\t'))
    settled = {}
    for d in dis:
        key = (int(d['line']), d['pos'])
        ikey = (key[0], int(float(key[1])))
        if ikey in MARK_ONLY:
            settled[key] = (MARK_ONLY[ikey], '', 'A')
        elif d['conf_B'] == 'None' and d['word_A']:
            settled[key] = (d['word_A'], a_rows[key]['expanded'] if key in a_rows else '', 'R')
        elif d['conf_A'] == 'None' and d['word_B']:
            settled[key] = (d['word_B'], b_rows[key]['expanded'] if key in b_rows else '', 'R')
        else:
            settled[key] = (f"{d['word_A']}|{d['word_B']}", '', 'M')

    manifest_pos = load_manifest_pos()
    keys = sorted((set(a_rows) | set(b_rows)) & manifest_pos, key=lambda k: (k[0], float(k[1])))
    out = []
    for line, pos in keys:
        key = (line, pos)
        if key in settled:
            word, expanded, grade = settled[key]
        else:
            ra = a_rows.get(key) or b_rows.get(key)
            word, expanded, grade = ra['word'], ra['expanded'], 'A'
        out.append((line, pos, word, expanded, grade))
    with open('plain_f55v.tsv', 'w') as f:
        f.write('line\tpos\tword\texpanded\tgrade\n')
        for row in out:
            f.write('\t'.join(str(c) for c in row) + '\n')
    n = len(out)
    counts = {}
    for *_, g in out:
        counts[g] = counts.get(g, 0) + 1
    print(f'plain_f55v.tsv: {n} rows; grade counts {counts}')


if __name__ == '__main__':
    main()

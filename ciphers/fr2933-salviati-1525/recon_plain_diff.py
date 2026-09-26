#!/usr/bin/env python3
"""Per-pos diff of two plain-Italian passes (SALV-PLAIN1, 26 Sept 2026).

tools/reconcile_passes.py's long format keys its token column on one of 'sign'/'token'/'group'/'code'
(reconcile_passes.py line ~82); plain_pass{A,B}_<leaf>.tsv's token column is 'word' (a full word, sometimes
with spaces, not a single sign), which that tool cannot key on -- per this job's own brief, falling back to
this small per-pos diff script instead, keyed on (line, pos) rather than a Needleman-Wunsch sign alignment
(unneeded here: both passes report the same pos list from the same manifest, so there is nothing to align).

  python3 recon_plain_diff.py plain_passA_<leaf>.tsv plain_passB_<leaf>.tsv --out-dir recon_plain_<leaf>

Writes <out-dir>/disagreements.tsv (line, pos, word_A, word_B, conf_A, conf_B) for every pos where the two
passes' normalised word differs, and <out-dir>/agreement.tsv (one summary line: agree/total, pct).
Normalising before comparing (PX-BRODEC lesson, CLAUDE.md rule 3): case-fold, strip whitespace, and treat
'~' and the letters it stands for as equivalent only when they visibly abbreviate the same reading is NOT
attempted here (that needs the image) -- this script normalises only case and whitespace, so anything left
after that normalisation is a real disagreement or a punctuation/abbreviation-mark difference for the
reconciler to settle from the crop, not a silent pass.
"""
import csv, os, sys


def load(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[(int(r['line']), r['pos'])] = r
    return rows


def norm(w):
    return (w or '').strip().casefold()


def main():
    args = sys.argv[1:]
    out_dir = 'recon_plain'
    if '--out-dir' in args:
        i = args.index('--out-dir')
        out_dir = args[i + 1]
        del args[i:i + 2]
    pa_path, pb_path = args[0], args[1]
    A, B = load(pa_path), load(pb_path)
    keys = sorted(set(A) | set(B), key=lambda k: (k[0], float(k[1])))
    os.makedirs(out_dir, exist_ok=True)
    dis, agree, total = [], 0, 0
    for k in keys:
        ra, rb = A.get(k), B.get(k)
        wa = ra['word'] if ra else ''
        wb = rb['word'] if rb else ''
        total += 1
        if norm(wa) == norm(wb):
            agree += 1
        else:
            dis.append((k[0], k[1], wa, wb, ra['conf'] if ra else '', rb['conf'] if rb else ''))
    with open(f'{out_dir}/disagreements.tsv', 'w') as f:
        f.write('line\tpos\tword_A\tword_B\tconf_A\tconf_B\n')
        for row in dis:
            f.write('\t'.join(str(c) for c in row) + '\n')
    pct = 100.0 * agree / total if total else 0.0
    with open(f'{out_dir}/agreement.tsv', 'w') as f:
        f.write('agree\ttotal\tpct\n')
        f.write(f'{agree}\t{total}\t{pct:.1f}\n')
    print(f'{agree}/{total} pos agree ({pct:.1f}%); {len(dis)} disagreements -> {out_dir}/disagreements.tsv')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Build the Spinelli c.1519 confirmation item for BENCHMARK-TX.tsv (split=confirm; TX-CONFIRM-SET, 9 Oct 2026).

LANE TX-ENGINEER amendment 2 guard 2 (.claude/briefs/runs/2026-10-09-account4-lane-tx-engineer.md): one known-answer item
from a leaf none of the five dev/eval items use, built by a session outside the lane, scored by the lane ONCE, at the end.
The lane does not open this file, its truth TSV or this item's line crops before that single final score.

Leaf: Beinecke GEN MSS 109 (Spinelli Family Papers), Filza 163, Tommaso Spinelli (Barcelona) to Leonardo Spinelli, c.1519,
the two cipher passages (p.1 lines 1-8, p.2 lines 1-2), ciphers/spinelli-beinecke-c1515. A symbol cipher in a different
hand, century, office and key family from every dev/eval item (Birago 1572, Ceppo-Nevers, Dinteville 1592).

Truth = the sign(s) the published plaintext forces under the published key, per position of the committed transcription
(ciphertext_v6.tsv, 259 signs), exactly the recipe of build_birago87.py:
  - plaintext: the 2017 Cipherbrain reading (Norbert #7 for p.1, Thomas #10 for p.2; snapshot
    verify2/cipherbrain_2017-03-24_tommaso.txt), a modern reading -> grade C with that note, never H;
  - alignment of that text to the 259 signs: verify2/align_2017_signs.tsv (GAPS-spinelli-beinecke-c1515, 2 Oct 2026,
    tools/interlinear_align.py; agreement 0.901 vs shuffled-plaintext control mean 0.316, max 0.360, 0/20);
  - key: key.tsv (Domnina 2016's published table mapped to the atlas codes by two blind matching passes, H39). Only
    H-graded rows (both blind passes agree on the Domnina cell) force a sign; M rows never do.
A plain letter L forces the SET of H codes whose value is L (homophones), so err_true here is value-level, as on no.87.

Excluded (counted, never scored): aligned letter empty (null-empty, letter-sign-empty); a null-graded sign over a letter
(null-took-letter: a dropped or extra sign beside it, alignment uncertain); the two signs under the 2017 readers' '??';
committed sign unkeyed (HOOK, PHI, SEVEN, EIGHTBAR, CIRCLE) or M-graded in key.tsv (PHI_T, THREE, JHOOK, OMEGA2, EPSILON,
STROKE, MU: the key-split analogue of no.87's T88); the que/rr markers (k, w) and any letter with no H code.

Line ids are the line-crop stems (p1c_L01..p1c_L08, p2c_L01..p2c_L02; crops images/<stem>_s1.jpg and _s2.jpg).
Also writes the committed transcription (= the reference sequence, home advantage, scores the conflicts only) as
benchmark-tx/outputs/spinelli-c1519-confirm/committed.tsv.

Flag column (TXV-SPIN, 9 Oct 2026): verifier verdicts in benchmark-tx/spinelli-c1519-confirm.flags.tsv (FLAG/CORRECT/KEEP as
build_birago152.py): FLAG -> class in the flag column (tx_bench --exclude-flagged drops it), CORRECT -> truth re-forced and flag
corrected:<class>, KEEP -> as built.

    python3 benchmark-tx/build_spinelli_confirm.py           # (re)build and print counts + sha256
    python3 benchmark-tx/build_spinelli_confirm.py --check   # rebuild in memory; exit 1 if the committed truth or its
                                                             # sha256 file is stale
"""
import csv, hashlib, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
F = os.path.join(ROOT, 'ciphers/spinelli-beinecke-c1515')
OUT = os.path.join(ROOT, 'benchmark-tx')
TRUTH = os.path.join(OUT, 'spinelli-c1519-confirm.truth.tsv')
SHA = TRUTH + '.sha256'
HEADER = ('# Spinelli c.1519 (Beinecke GEN MSS 109 Filza 163) confirmation item, split=confirm: 2017 published plaintext '
          'under the published key (H rows); built by benchmark-tx/build_spinelli_confirm.py. LANE TX-ENGINEER scores this '
          'ONCE, at the end. Flag column: verifier verdicts from spinelli-c1519-confirm.flags.tsv (TXV-SPIN).'
          '\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')
DROP_CLASS = {'null-empty': 'excluded:unaligned', 'letter-sign-empty': 'excluded:unaligned',
              'null-took-letter': 'excluded:null-over-letter', 'over-unread-??': 'excluded:unread-2017',
              'unkeyed-empty': 'excluded:off-key', 'unkeyed-took-letter': 'excluded:off-key'}


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def build():
    keyrows = rd(os.path.join(F, 'key.tsv'))
    grade = {}
    for r in keyrows:
        grade[r['code']] = 'H' if (r['grade'] == 'H' and grade.get(r['code'], 'H') == 'H') else 'M'
    hval = {r['code']: r['value'] for r in keyrows if grade[r['code']] == 'H'}
    by_val = {}
    for c, v in hval.items():
        by_val.setdefault(v, set()).add(c)

    ct = rd(os.path.join(F, 'ciphertext_v6.tsv'))
    al = rd(os.path.join(F, 'verify2/align_2017_signs.tsv'))
    assert len(ct) == len(al) == 259, (len(ct), len(al))
    # TXV-SPIN (9 Oct 2026): verifier verdicts per position, as build_birago152.py; FLAG -> flag column, CORRECT -> truth changed
    flags = {}
    fp = os.path.join(OUT, 'spinelli-c1519-confirm.flags.tsv')
    if os.path.exists(fp):
        for r in rd(fp):
            flags[(r['line'], int(r['pos']))] = r
    rows, nsc, nex = [], 0, {}
    for c, a in zip(ct, al):
        assert (c['page'], c['line'], c['pos'], c['sign']) == (a['page'], a['line'], a['pos'], a['code']), (c, a)
        line = '%sc_L%02d' % (c['page'], int(c['line']))
        sign, plain, cls = c['sign'], a['aligned_2017'].strip(), a['class']
        truth, st = '', 'scored'
        if cls in DROP_CLASS:
            st = DROP_CLASS[cls]
        elif sign not in grade:
            st = 'excluded:off-key'
        elif grade[sign] != 'H':
            st = 'excluded:key-M-' + sign
        elif plain in ('k', 'w'):
            st = 'excluded:que-rr-marker'
        elif len(plain) != 1:
            st = 'excluded:multi-letter-chunk'
        else:
            truth = '|'.join(sorted(by_val.get(plain, set())))
            if not truth:
                st = 'excluded:no-key-sign-for-' + plain
        if st == 'scored':
            nsc += 1
        else:
            nex[st] = nex.get(st, 0) + 1
        flag = ''
        fr = flags.get((line, int(c['pos'])))
        if fr and st == 'scored':
            if fr['verdict'] == 'CORRECT':
                if fr['correct_plain']:
                    plain = fr['correct_plain']
                ts = set(by_val.get(plain, set())) | set(filter(None, fr['add_signs'].split('|')))
                truth = '|'.join(sorted(ts))
                flag = 'corrected:' + fr['class']
            elif fr['verdict'] == 'FLAG':
                flag = fr['class']
        rows.append((line, int(c['pos']), sign, truth, plain, st, flag))
    text = HEADER + ''.join('\t'.join(map(str, r)) + '\n' for r in rows)
    return text, rows, nsc, nex


def main():
    text, rows, nsc, nex = build()
    digest = hashlib.sha256(text.encode()).hexdigest()
    shaline = '%s  spinelli-c1519-confirm.truth.tsv\n' % digest
    if '--check' in sys.argv:
        ok = (os.path.exists(TRUTH) and open(TRUTH).read() == text and os.path.exists(SHA) and open(SHA).read() == shaline)
        print('spinelli-c1519-confirm: %s (sha256 %s)' % ('ok' if ok else 'STALE', digest))
        sys.exit(0 if ok else 1)
    with open(TRUTH, 'w') as f:
        f.write(text)
    with open(SHA, 'w') as f:
        f.write(shaline)
    od = os.path.join(OUT, 'outputs/spinelli-c1519-confirm')
    os.makedirs(od, exist_ok=True)
    with open(os.path.join(od, 'committed.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n')
        for line, pos, sign, *_ in rows:
            f.write('%s\t%d\t%s\n' % (line, pos, sign))
    print('spinelli-c1519-confirm: %d positions, %d scored, excluded %s; sha256 %s' % (len(rows), nsc, nex, digest))


if __name__ == '__main__':
    main()

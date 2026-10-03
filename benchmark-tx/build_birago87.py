#!/usr/bin/env python3
"""Build the Birago 1572 no.87 known-answer item for BENCHMARK-TX.tsv (TX-BENCH, 3 Oct 2026).

Truth = the sign(s) the clerk's clear sheet (canvas 182) forces under the key, per position of the committed
transcription (harvest/ciphertext_f178r/f178v/f179r.tsv, 853 signs), using the sheet alignment
harvest/align87/align_real.tsv (NEVBIR-87ALIGN, tools/interlinear_align.py, C-grade, 0.896 vs shuffled max 0.376).

Key used for "forces": the printed 1572 table (harvest/key_1572_sheet.tsv) with the clerk-sheet C rows that
override it on this letter: T42 = m (C 11/12). Genuine key conflicts (rule 4: listed, not resolved) accept both
values: T95 in {s, l}, T52 in {i, o}. The off-sheet curled Ce (X_CE, value s, NO87-LABELS) is an s sign.
A plain letter L forces the SET of signs whose value is L (homophones): a homophone swap is invisible to this
known answer, so err_true here is a value-level figure (a lower bound on sign-level error).

Excluded (counted, never scored): sheet chunk null/unaligned; multi-letter chunk that is not the word sign's own
value; committed sign off-sheet (X_*, ?, the key does not force a sign) except X_CE; committed sign T88 (M, e/q
split); f178r L01 pos 1-8 (the readers' opening does not match the sheet, GAPS4: span uncertain).

Also writes normalised pipeline outputs (line, pos, sign) for passA, passB, passC (= committed), passD (look-alike,
f178r/f179r only) and labels (committed + the NO87-LABELS X_CE relabels) to benchmark-tx/outputs/birago1572-no87/.
Run from the repo root: python3 benchmark-tx/build_birago87.py
"""
import csv, os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
H = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572/harvest')
OUT = os.path.join(ROOT, 'benchmark-tx')
LEAVES = ['f178r', 'f178v', 'f179r']


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def main():
    key = {r['sign']: r['value'] for r in rd(os.path.join(H, 'key_1572_sheet.tsv'))}
    key['T42'] = 'm'
    vals = {s: {v} for s, v in key.items()}
    vals['T95'] = {'s', 'l'}
    vals['T52'] = {'i', 'o'}
    vals['X_CE'] = {'s'}
    by_val = {}
    for s, vs in vals.items():
        for v in vs:
            by_val.setdefault(v, set()).add(s)

    committed = []
    for leaf in LEAVES:
        for r in rd(os.path.join(H, 'ciphertext_%s.tsv' % leaf)):
            committed.append((r['line'], int(r['pos']), r['sign']))
    align = rd(os.path.join(H, 'align87/align_real.tsv'))
    assert len(align) == len(committed) == 853, (len(align), len(committed))
    # X_CE relabels from the exceptions files (NO87-LABELS)
    xce = set()
    for leaf in LEAVES:
        p = os.path.join(H, 'exceptions_%s.tsv' % leaf)
        if os.path.exists(p):
            for r in rd(p):
                if 'X_CE' in r.get('reason', ''):
                    xce.add(('%s_%s' % (r['folio'], r['line']), int(r['pos'])))

    rows, nsc, nex = [], 0, {}
    for (line, pos, sign), a in zip(committed, align):
        assert a['cipher_line'] == line.split('_')[0]
        chunk = a['plain_chunk'].strip()
        st = 'scored'
        truth = ''
        ref = 'X_CE' if (line, pos) in xce else sign
        if not chunk or a['status'].startswith('null'):
            st = 'excluded:unaligned'
        elif line == 'f178r_L01' and pos <= 8:
            st = 'excluded:span-uncertain'
        elif ref == 'T88':
            st = 'excluded:key-split-T88'
        elif ref not in vals:
            st = 'excluded:off-sheet'
        elif len(chunk) == 1:
            truth = '|'.join(sorted(by_val.get(chunk, set())))
            if not truth:
                st = 'excluded:no-key-sign-for-' + chunk
        else:
            ws = sorted(s for s, v in key.items() if v == chunk)
            if ws:
                truth = '|'.join(ws)
            else:
                st = 'excluded:multi-letter-chunk'
        if st == 'scored':
            nsc += 1
        else:
            nex[st] = nex.get(st, 0) + 1
        rows.append((line, pos, ref, truth, chunk, st))
    with open(os.path.join(OUT, 'birago1572-no87.truth.tsv'), 'w') as f:
        f.write('# Birago 1572 no.87 (BnF fr.3251 f.178r-179r) known answer: clerk clear sheet under the key; built by '
                'benchmark-tx/build_birago87.py\nline\tpos\tref_sign\ttruth\tplain\tstatus\n')
        for r in rows:
            f.write('\t'.join(map(str, r)) + '\n')

    od = os.path.join(OUT, 'outputs/birago1572-no87')
    os.makedirs(od, exist_ok=True)

    def norm(files, name):
        out = []
        for leaf, p in files:
            for r in rd(os.path.join(H, p)):
                ln = r.get('line') or '%s_%s' % (leaf, r['passage'])
                out.append((ln, r['pos'], r.get('sign') or r.get('sign_id')))
        with open(os.path.join(od, name + '.tsv'), 'w') as f:
            f.write('line\tpos\tsign\n')
            for o in out:
                f.write('\t'.join(o) + '\n')
    norm([('f178r', 'f178r/passA.tsv'), ('f178v', 'f178v/passA.tsv'), ('f178v', 'f178v/passA_L11-23.tsv'),
          ('f179r', 'f179r/passA.tsv')], 'passA')
    norm([('f178r', 'f178r/passB.tsv'), ('f178v', 'f178v/passB.tsv'), ('f178v', 'f178v/passB_L11-23.tsv'),
          ('f179r', 'f179r/passB.tsv')], 'passB')
    norm([(l, 'ciphertext_%s.tsv' % l) for l in LEAVES], 'passC')
    norm([('f178r', 'lookalike_known/f178r_passD.tsv'), ('f179r', 'lookalike_known/f179r_passD.tsv')], 'passD')
    with open(os.path.join(od, 'labels.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n')
        for line, pos, ref, *_ in rows:
            f.write('%s\t%d\t%s\n' % (line, pos, ref))
    print('birago1572-no87: %d positions, %d scored, excluded %s' % (len(rows), nsc, nex))


if __name__ == '__main__':
    main()

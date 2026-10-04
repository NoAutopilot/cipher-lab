#!/usr/bin/env python3
"""N7-VIV54L: adapt the reconcile_passes.py drafts of this folder to tools/lookalike_pass.py's input shapes.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv54L_prep.py

For every tx/rec_<page>/ciphertext_draft.tsv (line, position, sign, confidence, alt, why) writes, under
tx/lookalike54/align/<page>/:
  agreement.tsv  passage, posA, idA, idB, status, merged  (status agree | split | split-gap; merged = the label the
                 committed decode uses at that position, after tx/reconcile_vivk.py's RULES + RULES54 + MAP, or NONE)
  passC.tsv      passage, pos, sign_id  (the committed sequence, one row per merged label)
and, for f173r/f173v only, tx/lookalike54/<page>_pass{A,B,C}_long.tsv (line, pos, sign) for `lookalike_pass.py audit`.
Nothing here changes a label: passC is exactly the sequence tx/viv54_decode.py decodes (asserted for f173r/f173v).
"""
import glob, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import reconcile_vivk as rv  # noqa: E402

RULES = {**rv.RULES, **rv.RULES54}
OUT = os.path.join(HERE, 'lookalike54')


def rows(page):
    for ln in open(os.path.join(HERE, f'rec_{page}', 'ciphertext_draft.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'line':
            continue
        yield (f + [''] * 6)[:6]


def build(page):
    al, pc, pos = [], [], {}
    for line, p, sign, conf, alt, why in rows(page):
        a = sign.rstrip('?')
        b = alt[2:].rstrip('?') if alt.startswith('B:') else ''
        if why == 'gap':
            if alt.startswith('A:'):
                idA, idB = '', a
            else:
                idA, idB = a, ''
            st = 'split-gap'
        elif why == 'differ' and b and b != '-':
            idA, idB = a, b
            w = RULES.get(frozenset((a, b)))
            st = 'agree' if w else 'split'      # a label-rule split counts as settled, as in the committed decode
            if w:
                a = w
        else:
            idA = idB = a
            st = 'agree'
        lab = rv.MAP.get(a, a) if a not in ('', '-') else ''
        merged = lab or 'NONE'
        al.append(dict(passage=line, posA=p, idA=rv.MAP.get(idA, idA), idB=rv.MAP.get(idB, idB), status=st, merged=merged))
        if lab:
            pos[line] = pos.get(line, 0) + 1
            pc.append(dict(passage=line, pos=str(pos[line]), sign_id=lab))
    return al, pc


def write(path, rows_, fields):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, 'w', encoding='utf-8') as o:
        o.write('\t'.join(fields) + '\n')
        for r in rows_:
            o.write('\t'.join(str(r[k]) for k in fields) + '\n')


def long_from_wide(src, dst):
    out = []
    for ln in open(src, encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'row' or len(f) < 2:
            continue
        toks = [t.rstrip('?') for t in f[1].split()]
        for i, s in enumerate([t for t in toks if t], 1):
            out.append(dict(line=f[0], pos=i, sign=rv.MAP.get(s, s)))
    write(dst, out, ['line', 'pos', 'sign'])


def main():
    pages = sorted(os.path.basename(d)[4:] for d in glob.glob(os.path.join(HERE, 'rec_f*')))
    for page in pages:
        al, pc = build(page)
        write(os.path.join(OUT, 'align', page, 'agreement.tsv'), al,
              ['passage', 'posA', 'idA', 'idB', 'status', 'merged'])
        write(os.path.join(OUT, 'align', page, 'passC.tsv'), pc, ['passage', 'pos', 'sign_id'])
        if page in ('f173r', 'f173v'):
            wide = {}
            for ln in open(os.path.join(HERE, f'{page}_rec.tsv'), encoding='utf-8'):
                f = ln.rstrip('\n').split('\t')
                if f[0] != 'row':
                    wide[f[0]] = f[1].split()
            got = {}
            for r in pc:
                got.setdefault(r['passage'], []).append(r['sign_id'])
            assert got == wide, page
            long_from_wide(os.path.join(HERE, f'{page}_passA_c.tsv'), os.path.join(OUT, f'{page}_passA_long.tsv'))
            long_from_wide(os.path.join(HERE, f'{page}_passB_c.tsv'), os.path.join(OUT, f'{page}_passB_long.tsv'))
            write(os.path.join(OUT, f'{page}_passC_long.tsv'),
                  [dict(line=r['passage'], pos=r['pos'], sign=r['sign_id']) for r in pc], ['line', 'pos', 'sign'])
        n = len(pc); sp = sum(r['status'] == 'split' for r in al); gp = sum(r['status'] == 'split-gap' for r in al)
        print(f'{page}: {n} signs, unsettled splits {sp}, one-pass gaps {gp}')


if __name__ == '__main__':
    main()

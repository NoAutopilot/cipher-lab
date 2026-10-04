#!/usr/bin/env python3
"""N7-VIV53L: turn the N6-VIV53/53B two-reader drafts of ink 53 into tools/lookalike_pass.py inputs (PREREG-N7VIV53L.md).

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_prep.py

Reads tx/rec_<page>/ciphertext_draft.tsv (tools/reconcile_passes.py on the _c passes) for f170r f170v f171r f171v and writes, under
tx/lookalike53L/:
  <page>/agreement.tsv  passage, posA, idA, idB, status (agree | split | gap), merged (= passC label), one row per kept draft column
  <page>/passC.tsv      passage, pos, sign_id -- the N6 reconciled sequence (reconcile_vivk RULES + RULES54 + MAP), before "o o" join
  <page>/crops/         symlinks to that page's line crops (images/p53/*_<page>_L??_s?.jpg)
  passA.tsv passB.tsv passC.tsv   (line, pos, sign) whole piece, line = <page>_<Lnn>, for `lookalike_pass.py audit`
  sheet.png sheet_map.json        value-blind id sheet (one cell per label: the id in large type; shapes are described in SIGNS.md)
A split settled by an N6 label rule (reconcile_vivk RULES/RULES54) is status 'agree' (settled before this job, PREREG rule 3).
"""
import json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import reconcile_vivk as rv  # noqa: E402

PAGES = ('f170r', 'f170v', 'f171r', 'f171v')
OUT = os.path.join(HERE, 'lookalike53L')
RULES = {**rv.RULES, **rv.RULES54}


def rows(page):
    out = []
    for ln in open(os.path.join(HERE, f'rec_{page}', 'ciphertext_draft.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] == 'line':
            continue
        line, pos, sign, conf, alt, why = (f + [''] * 6)[:6]
        a = sign.rstrip('?')
        b = alt[2:].rstrip('?') if alt.startswith('B:') else ''
        if why.startswith('agree'):
            A, B, st, lab = a, a, 'agree', a
        elif why == 'differ' and b and b != '-':
            w = RULES.get(frozenset((a, b)))
            A, B, st, lab = a, b, ('agree' if w else 'split'), (w or a)
        else:  # gap: one reader only; the draft sign is that reader's label
            if alt.startswith('A:'):
                A, B = '', a
            else:
                A, B = a, ''
            st, lab = 'gap', a
        if lab in ('', '-'):
            continue
        out.append(dict(passage=f'{page}_{line}', idA=A, idB=B, status=st, merged=rv.MAP.get(lab, lab)))
    return out


def write(p, rws, fields):
    with open(p, 'w', encoding='utf-8') as o:
        o.write('\t'.join(fields) + '\n')
        for r in rws:
            o.write('\t'.join(str(r[k]) for k in fields) + '\n')


def main():
    from PIL import Image, ImageDraw, ImageFont
    os.makedirs(OUT, exist_ok=True)
    allA, allB, allC, labels = [], [], [], set()
    for page in PAGES:
        d = os.path.join(OUT, page); os.makedirs(os.path.join(d, 'crops'), exist_ok=True)
        rw = rows(page)
        pos, pa, pb = {}, {}, {}
        for r in rw:
            k = r['passage']; pos[k] = pos.get(k, 0) + 1; r['posA'] = pos[k]; r['pos'] = pos[k]; r['sign_id'] = r['merged']
            labels.update(x for x in (r['idA'], r['idB'], r['merged']) if x)
            allC.append(dict(line=k, pos=pos[k], sign=r['merged']))
            if r['idA']:
                pa[k] = pa.get(k, 0) + 1; allA.append(dict(line=k, pos=pa[k], sign=rv.MAP.get(r['idA'], r['idA'])))
            if r['idB']:
                pb[k] = pb.get(k, 0) + 1; allB.append(dict(line=k, pos=pb[k], sign=rv.MAP.get(r['idB'], r['idB'])))
        write(os.path.join(d, 'agreement.tsv'), rw, ['passage', 'posA', 'idA', 'idB', 'status', 'merged'])
        write(os.path.join(d, 'passC.tsv'), rw, ['passage', 'pos', 'sign_id'])
        img = os.path.join(T, 'images', 'p53')
        for fn in sorted(os.listdir(img)):
            if f'_{page}_L' in fn and fn.endswith('.jpg') and 'debug' not in fn:
                dst = os.path.join(d, 'crops', fn)
                if not os.path.lexists(dst):
                    os.symlink(os.path.join(img, fn), dst)
        print(page, len(rw), 'signs;', sum(r['status'] == 'split' for r in rw), 'split;', sum(r['status'] == 'gap' for r in rw), 'gap')
    for n, rr in (('passA', allA), ('passB', allB), ('passC', allC)):
        write(os.path.join(OUT, f'{n}.tsv'), rr, ['line', 'pos', 'sign'])
    ids = sorted(labels)
    cell, cols = 110, 9
    im = Image.new('RGB', (cols * cell, ((len(ids) + cols - 1) // cols) * cell), 'white')
    dr = ImageDraw.Draw(im)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf', 26)
    except OSError:
        font = ImageFont.load_default()
    for i, t in enumerate(ids):
        x, y = (i % cols) * cell, (i // cols) * cell
        dr.rectangle((x + 2, y + 2, x + cell - 3, y + cell - 3), outline='grey')
        dr.text((x + 8, y + 40), t[:9], fill='black', font=font)
    im.save(os.path.join(OUT, 'sheet.png'))
    json.dump([{'id': t} for t in ids], open(os.path.join(OUT, 'sheet_map.json'), 'w'), indent=0)
    print('labels', len(ids))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""LOOKALIKE-TOOL known-answer scorer (2 Oct 2026): true sign error of a label sequence against a period witness.

Written and run on passA/passB/passC BEFORE the look-alike re-read was made, so the rule could not be tuned to it.
Each sign is decoded with the fitted 1572 map (sign_id_map_1572_fit.json, printed key + T42=m; no sheet-derived
exceptions, so the witness never feeds the labels). Decode and witness span are folded the align_sheet.py way (a-z,
u/v and i/j merged, car.la -> carmagnola, ma.ta -> maesta, struck words dropped: rule 3's transcription-convention
normalisation). difflib aligns the two; a sign is RIGHT if every letter it decodes to sits in a matching block of at
least --min-block letters, WRONG if any of its letters is not, EMPTY if it decodes to nothing (off-sheet X_*, null).
True error = WRONG / (RIGHT + WRONG); EMPTY is reported separately. Key errors (a sign whose printed value differs from
the clerk's) are counted the same in every sequence, so the before/after difference is reader error only.
--compare BEFORE AFTER lists every position whose label differs and classes it: fixed (wrong -> right), harmed
(right -> wrong), both-wrong, both-right (homophone or same letter), or touches-EMPTY.
  python3 score_known.py SEQ.tsv --span f178r [--compare OTHER.tsv] [--min-block 2]
"""
import argparse, csv, difflib, json, re
from pathlib import Path
H = Path(__file__).resolve().parent.parent
SPANS = {'f178r': ('L01', 'L03', None, 'da loro'), 'f179r': ('L17', 'L19', "se'l se", None)}


def fold(s):
    s = s.lower().replace('v', 'u').replace('j', 'i').replace('&', 'et')
    return re.sub(r'[^a-z]', '', s)


def sheet_span(span, sheet=H / 'f179r_sheet/decipherment_sheet.tsv'):
    lo, hi, frm, cut = SPANS[span]
    t = ' '.join(r['text'] for r in csv.DictReader(open(sheet), delimiter='\t') if lo <= r['line'] <= hi)
    t = re.sub(r'\[[^\]]*\]', '', t)
    if frm:
        t = t[t.index(frm):]
    if cut:
        t = t[:t.index(cut)]
    return fold(t.replace('car.la', 'carmagnola').replace('ma.ta', 'maesta'))


def score(seq_path, span, min_block=2, m=None):
    m = m or {e['id']: e['value'] for e in json.load(open(H / 'sign_id_map_1572_fit.json'))}
    rows = list(csv.DictReader(open(seq_path), delimiter='\t'))
    dec, owner = [], []
    for k, r in enumerate(rows):
        v = m.get(r['sign_id'].strip(), '')
        v = '' if v in ('null', None) else fold(v)
        dec.append(v); owner += [k] * len(v)
    s, clear = ''.join(dec), sheet_span(span)
    ok = [False] * len(s)
    for b in difflib.SequenceMatcher(None, s, clear, autojunk=False).get_matching_blocks():
        if b.size >= min_block:
            for i in range(b.a, b.a + b.size):
                ok[i] = True
    st = []
    for k, v in enumerate(dec):
        if not v:
            st.append('EMPTY'); continue
        idx = [i for i, o in enumerate(owner) if o == k]
        st.append('RIGHT' if all(ok[i] for i in idx) else 'WRONG')
    return rows, st


def summary(st):
    r, w, e = st.count('RIGHT'), st.count('WRONG'), st.count('EMPTY')
    return dict(signs=len(st), right=r, wrong=w, empty=e, true_error=round(w / max(1, r + w), 3))


if __name__ == '__main__':
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('seq'); ap.add_argument('--span', required=True, choices=sorted(SPANS))
    ap.add_argument('--compare'); ap.add_argument('--min-block', type=int, default=2)
    a = ap.parse_args()
    rows, st = score(a.seq, a.span, a.min_block)
    print(a.seq, json.dumps(summary(st)))
    if a.compare:
        rows2, st2 = score(a.compare, a.span, a.min_block)
        print(a.compare, json.dumps(summary(st2)))
        assert [(r['passage'], r['pos']) for r in rows] == [(r['passage'], r['pos']) for r in rows2]
        cls = {}
        for r, r2, x, y in zip(rows, rows2, st, st2):
            if r['sign_id'] == r2['sign_id']:
                continue
            c = ('touches-EMPTY' if 'EMPTY' in (x, y) else 'fixed' if (x, y) == ('WRONG', 'RIGHT') else
                 'harmed' if (x, y) == ('RIGHT', 'WRONG') else 'both-wrong' if x == 'WRONG' else 'both-right')
            cls[c] = cls.get(c, 0) + 1
            print(f"  {r['passage']}.{r['pos']}: {r['sign_id']} ({x}) -> {r2['sign_id']} ({y})  {c}")
        print('changes:', json.dumps(cls))

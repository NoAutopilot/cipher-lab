#!/usr/bin/env python3
"""TXE2-SHEETS-ALL (9 Oct 2026, PREREG-txeng2-8 A2): read-free cross of the atlas-built sheets outside the benchmark
eval items that carry a per-position known answer, writing one TSV row per exemplar.

  1. ciphers/nevers-birago-fr3251-1572/atlas/atlas.tsv (glyph_atlas.py, 45 cells) vs atlas/secure_tokens.tsv (grade S,
     TX-SHEET's three-instrument agreement). Exemplars on f178r/f178v/f179r (no.87) and f152r are eval leaves: skipped
     before any lookup (Openings of eval truth: 0). secure_tokens.tsv is not independent of the atlas (its rule requires
     the atlas kNN to agree), so an OK here is weak; a disagreement is still a disagreement.
  2. tools/keys/key60_atlas/atlas264.tsv + atlas264ext.tsv (key no.60 exemplars cut from the interlined leaf fr.3985
     c.264; value = the contemporary gloss, aligned grade S) vs ciphers/fr3986-nevers-revol-1593/key.tsv (Bourdeau's
     transcription of Tomokiyo's no.60 table; '|' = alternatives). atlas.tsv's own `agreement` column (LANE R5 G,
     24 Sept 2026) is the on-file cross for the 80-row sheet and is reported, not recomputed.

    python3 benchmark-tx/txeng2/sheets-all/cross_all.py > benchmark-tx/txeng2/sheets-all/cross.tsv
"""
import csv, os, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
P = lambda *a: os.path.join(ROOT, *a)
EVAL = ('f178r', 'f178v', 'f179r', 'f152r')


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def main():
    w = csv.writer(sys.stdout, delimiter='\t', lineterminator='\n')
    w.writerow(['folder', 'sheet', 'cell', 'box', 'truth_source', 'truth', 'verdict'])
    A = 'ciphers/nevers-birago-fr3251-1572/atlas'
    rows = rd(P(A, 'atlas.tsv'))
    keep = [(r['code'], s) for r in rows for s in r['exemplars'].split(',') if s and s.split('_')[0] not in EVAL]
    sec = {r['sid']: r['code'] for r in rd(P(A, 'secure_tokens.tsv')) if r['page'] not in EVAL}
    for cell, sid in keep:
        t = sec.get(sid)
        v = 'no-truth (not a secure token)' if t is None else ('OK' if t == cell else 'MISLABELLED')
        w.writerow(['nevers-birago-fr3251-1572', 'atlas/atlas.tsv', cell, sid, 'secure_tokens.tsv (S)', t or '-', v])
    key = {}
    for r in rd(P('ciphers/fr3986-nevers-revol-1593/key.tsv')):
        key.setdefault(r['sign'], set()).update(x.strip().lower() for x in r['value'].split('|'))
    # the 80-row atlas.tsv carries its own key60 reading per exemplar (leaf-264 ids A01-A52 are the same boxes as
    # atlas264.tsv); where key.tsv spells a ligature tag differently (atlas 'pi' = pi-with-i = que, key.tsv 'pi' = o), the
    # on-file column decides
    onfile = {r['sign_id']: r for r in rd(P('tools/keys/key60_atlas/atlas.tsv')) if r['leaf'] == '264'}
    for fn in ('atlas264.tsv', 'atlas264ext.tsv'):
        for r in rd(P('tools/keys/key60_atlas', fn)):
            t, g = r['tag'], r['value_under_gloss'].strip().lower()
            if t not in key:
                v = 'no key cell (tag not in key.tsv)'
            elif g in key[t]:
                v = 'OK'
            elif fn == 'atlas264.tsv' and onfile.get(r['sign_id'], {}).get('agreement') == 'yes':
                v = 'OK (on-file key60 ' + onfile[r['sign_id']]['key60'] + '; key.tsv tag spelled differently)'
            else:
                v = 'VALUE-CONFLICT (gloss not a key value of the cell)'
            w.writerow(['fr3985/fr3986 key60', 'tools/keys/key60_atlas/' + fn, t, r['sign_id'], 'interlined gloss c.264 (S) vs key.tsv',
                        g + ' / key ' + '|'.join(sorted(key.get(t, []))), v])


if __name__ == '__main__':
    main()

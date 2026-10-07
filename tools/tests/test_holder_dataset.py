#!/usr/bin/env python3
"""Offline test for tools/holder_dataset.py (BNF-FOCUS, 7 Oct 2026): builds a two-folder fixture repo.

Catches: a BnF folder whose heading names a fonds + number, the folder-name shelfmark winning over a sibling
volume the prose names first, a classified status.json result attached as a reading row. Must NOT: take a folder
that only says "BnF holdings were not checked" with no fonds + number.

Run: python3 tools/tests/test_holder_dataset.py
"""
import json, os, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import holder_dataset as hd  # noqa: E402


def make(root):
    def w(p, s):
        os.makedirs(os.path.dirname(os.path.join(root, p)), exist_ok=True)
        open(os.path.join(root, p), 'w').write(s)
    w('ciphers/fr3416-nevers-fils-1589/NOTES.md', 'partial\n\n# BnF fr.3995 key; letter BnF fr.3416 f.35r\nGallica btv1b9058240c\n')
    w('ciphers/fr3416-nevers-fils-1589/AUDIT.md', 'N4\n')
    w('ciphers/nara-letter/NOTES.md', 'open\n\n# NARA RG 59 letter\nBnF holdings were not checked.\n')
    json.dump({'results': [{'link': 'ciphers/fr3416-nevers-fils-1589/AUDIT.md', 'document_id': 'BnF fr.3416 f.35r',
                            'novelty': 'N4', 'depth': 'D1', 'depth_pct': 78.4, 'key': 'published', 'text': 'unknown',
                            'title': 'Nevers to his son'}]}, open(os.path.join(root, 'status.json'), 'w'))


def test_build():
    with tempfile.TemporaryDirectory() as d:
        make(d)
        rows = hd.build(d, 'bnf')
        folders = {r['folder'] for r in rows}
        assert folders == {'fr3416-nevers-fils-1589'}            # the NARA folder is not taken
        rd = [r for r in rows if r['row_kind'] == 'reading'][0]
        assert rd['shelfmark'] == 'fr.3416'                        # slug beats the fr.3995 key named first
        assert rd['n_class'] == 'N4' and rd['depth'] == 'D1' and rd['gallica_ark'] == 'btv1b9058240c'
        assert hd.render(rows).splitlines()[0].split('\t') == hd.COLS


if __name__ == '__main__':
    test_build()
    print('ok')

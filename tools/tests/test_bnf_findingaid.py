#!/usr/bin/env python3
"""Offline test for tools/bnf_findingaid.py (BNF-FOCUS, 7 Oct 2026): parse only, no network.

Catches: an item list with folios, the "avec chiffre" / "chiffre et déchiffrement" flags, the duplicate index
list the BnF notice prints after the dépouillement. Must NOT: report a volume-level notice (prose, no "Fol."
lines) as having items, or flag an unmarked letter.

Run: python3 tools/tests/test_bnf_findingaid.py
"""
import os, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as bf  # noqa: E402

ITEMS = """<html><body><h1>Français 3251 • Anc. 8760 • Recueil de lettres</h1>
<div>Fol. 11 • 6 Lettre, avec chiffre, de « LODOVICO BIRAGO » au « duca di Nivers,... il 14 settembre 1570 ».</div>
<div>Fol. 21 • 11 Lettre de « LODOVICO BIRAGO » au « duca di Nevers,... il XII ottobre 1570 ».</div>
<div>Fol. 39 • 20 Lettre, avec chiffre et d&eacute;chiffrement, de « LODOVICO BIRAGO ».</div>
<div>6 Lettre, avec chiffre, de « LODOVICO BIRAGO » au « duca di Nivers,... il 14 settembre 1570 ».</div>
</body></html>"""

PROSE = """<html><body><h1>Dupuy 452 • Recueil de lettres</h1>
<p>A Madame, par Carpi, Rome, 22 oct. 1525, orig., presque entièrement en chiffres (20) ;</p></body></html>"""


def test_items_and_flags():
    title, rows = bf.parse(ITEMS)
    assert title.startswith('Français 3251')
    assert [r['no'] for r in rows] == ['6', '11', '20']          # index duplicate of no.6 dropped
    by = {r['no']: r for r in rows}
    assert by['6']['chiffre'] == 'yes' and by['6']['dechiffre'] == ''
    assert by['11']['chiffre'] == '' and by['11']['folio'] == '21'  # unmarked letter stays unflagged
    assert by['20']['chiffre'] == 'yes' and by['20']['dechiffre'] == 'yes'


def test_volume_level_notice_has_no_items():
    _, rows = bf.parse(PROSE)
    assert rows == []


if __name__ == '__main__':
    test_items_and_flags()
    test_volume_level_notice_has_no_items()
    print('ok')

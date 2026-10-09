#!/usr/bin/env python3
"""Offline tests for tools/bnf_findingaid.py --attribute / --attribute-control (MQS-BNF-S5, 9 Oct 2026); no network.

Must catch: sender/recipient keys of the BnF formula ('Lettre de « BONNYVET,... à monseigneur le tresorier Robertet' ->
BONNYVET, ROBERTET; DE LA TREMOILLE -> TREMOILLE; HENRY [D'ALBRET] -> HENRY; 'au roy' -> ROI); a bare cipher item between
two letters of one sender gets agree=yes; a folio-less index item ('Lettres en chiffre.' no.4) is placed by its number;
a KEY-OFFICES row naming a neighbour; a volume-level row for a notice with no item list; the masked control scores an
ordered volume above its within-volume null.
Must NOT: give a lead row to an attributed cipher letter, a deciphered item or a key sheet; put a neighbour's language
into the default trial set (it is printed as neighbour:<lang> only); match ROI or a longer name in KEY-OFFICES.tsv.
Run: python3 tools/tests/test_bnf_findingaid_attr.py
"""
import os, socket, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as bf  # noqa: E402


def _no_net(*a, **k):
    raise RuntimeError('network used in an offline test')


socket.socket.connect = _no_net


def notice(items, title='Français 9999 • Recueil de lettres, 1520-1530 • x'):
    return '<html><body><p>%s</p>%s</body></html>' % (title, ''.join('<p>%s</p>' % i for i in items))


V1 = notice([
    'Fol. 1 • 1 Lettre de « DE LA TREMOILLE,... à monseigneur le tresorier Robertet,... A Dijon, le XIe septembre ».',
    'Fol. 3 • 2 Lettre en chiffre.',
    'Fol. 5 • 3 Lettre de « DE LA TREMOILLE,... au roy... A Dijon ».',
    'Fol. 7 • 5 Lettre de « BONNYVET,... à monseigneur le tresorier Robertet ».',
    'Fol. 9 • 6 Lettre, en italien, de « GIO. AGOCCHI » au Sr Girolamo Agocchi.',
    'Fol. 11 • 7 Lettre de « BONNYVET,... en chiffre ».',
    'Fol. 13 • 8 Pièce en chiffre déchiffrée.',
    'Fol. 15 • 9 Table de chiffre.',
    '4 Lettres en chiffre.',
])


def test_parties():
    assert bf.letter_parties('Lettre de « BONNYVET,... à monseigneur le tresorier Robertet,... A Dax ».') == ('BONNYVET', 'ROBERTET')
    assert bf.letter_parties('Lettre de « DE LA TREMOILLE,... au roy... A Dijon ».') == ('TREMOILLE', 'ROI')
    assert bf.letter_parties("Lettre d' « HENRY [D'ALBRET, roi de Navarre]... au roy... ».")[0] == 'HENRY'
    assert bf.letter_parties('Lettre en chiffre.') == ('', '')
    assert bf.letter_parties('Lettre, en chiffre, adressée « au roy ».') == ('', '')


def test_leads():
    rows = bf.attribute_volume(V1, ROOT)
    by_no = {r['no']: r for r in rows}
    assert set(by_no) == {'2', '4'}, by_no.keys()           # not no.7 (attributed), 8 (deciphered), 9 (key sheet)
    r = by_no['2']
    assert r['prev_snd'] == r['next_snd'] == 'TREMOILLE' and r['agree'] == 'yes' and r['prev_dist'] == 2
    assert r['grade'].startswith('M lead')
    r4 = by_no['4']                                          # index item placed by number: between no.3 and no.5
    assert r4['prev_snd'] == 'TREMOILLE' and r4['next_snd'] == 'BONNYVET' and r4['agree'] == 'no'
    assert 'France' in r4['powers']


def test_language_never_default():
    rows = bf.attribute_volume(V1, ROOT)
    r = [x for x in rows if x['no'] == '4'][0]
    assert r['lang_neighbour'] == 'neighbour:it', r['lang_neighbour']
    assert r['lang_trial'] == bf.LANG_SETS[16]               # century from the title's 1520; neighbour not promoted
    assert not r['lang_trial'].startswith('it')


def test_keys_on_file():
    d = tempfile.mkdtemp(prefix='bnfattr')
    open(os.path.join(d, 'KEY-OFFICES.tsv'), 'w').write(
        'key_path\toffice\tcorrespondents\tyears\n'
        'ciphers/a/key.tsv\tLa Trémoille household\tLouis de La Tremoille; Robertet\t1520\n'
        'ciphers/b/key.tsv\tRoi de France\tROIX; Bonnyvetti\t1520\n')
    assert bf.keys_on_file(['TREMOILLE'], d) == ['ciphers/a/key.tsv']
    assert bf.keys_on_file(['ROI', 'BONNYVET'], d) == []     # ROI ignored; BONNYVET is not Bonnyvetti


def test_volume_level():
    rows = bf.attribute_volume(notice([], title='Dupuy 155 • Recueil, 1580 • Rome, nonce'), ROOT)
    assert len(rows) == 1 and rows[0]['kind'] == 'volume-level' and 'Papacy' in rows[0]['powers']


def test_control_orders():
    d = tempfile.mkdtemp(prefix='bnfattrc')
    runs = ['Fol. %d • %d Lettre de « %s,... à monseigneur Robertet » en chiffre.' % (2 * i + 1, i + 1, s)
            for i, s in enumerate(['ALPHA'] * 5 + ['BETAA'] * 5 + ['GAMMA'] * 5)]
    p = os.path.join(d, 'cc1.html')
    open(p, 'w').write(notice(runs))
    q = os.path.join(d, 'cc2.html')
    open(q, 'w').write(notice(runs[::-1][:4]))
    r = bf.attribute_control([p, q], n=50)
    assert r['N'] == 19 and r['A'] > r['n1_p95'] and r['n2_mean'] < r['A'], r


if __name__ == '__main__':
    for k, f in list(globals().items()):
        if k.startswith('test_'):
            f()
    print('test_bnf_findingaid_attr: all ok')

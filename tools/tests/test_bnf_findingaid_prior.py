#!/usr/bin/env python3
"""Offline tests for tools/bnf_findingaid.py --pile --prior-work (MQS-BNF-S3, 9 Oct 2026); no network.

Must catch: a ciphers/<slug>/NOTES.md line 'BnF fr.3040 f.18r' marks fr.3040 f.18 ours; a ciphers/_triage note naming
fr.2988 f.1; a folder-context line 'f.22r' (no volume) inside ciphers/fr3040-x/; a range notice gives ours? and keeps its
open count; fr.2988 gets contact_first (active edition, prior_work.py check 3a).
Must NOT: fr.29880 f.18, fr.3040 f.19, fr.3041 f.18 against that line; a bare 'f.22r' in ciphers/_triage/; any line in a
RESTRICTED.md folder or in ciphers/debosnys-1883; contact_first on fr.3413.
Run: python3 tools/tests/test_bnf_findingaid_prior.py
"""
import os, shutil, socket, sys, tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as bf  # noqa: E402


def _no_net(*a, **k):
    raise RuntimeError('network used in an offline test')


socket.socket.connect = _no_net


def fake_root():
    r = tempfile.mkdtemp(prefix='bnfprior')
    os.makedirs(os.path.join(r, 'tools'))
    for f in ('shelfmark.py', 'decode_neighbours_exclude.py'):
        shutil.copy(os.path.join(ROOT, 'tools', f), os.path.join(r, 'tools', f))

    def w(rel, text):
        p = os.path.join(r, rel)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        open(p, 'w').write(text)
    w('ciphers/fr3040-x/NOTES.md', 'status: partial\n- BnF fr.3040 f.18r read at native size.\n- f.22r crop checked.\n')
    w('ciphers/_triage/note.md', 'BnF fr.2988 f.1 is a bare cipher piece.\nf.22r elsewhere\n')
    w('ciphers/fr3041-secret/RESTRICTED.md', 'restricted\n')
    w('ciphers/fr3041-secret/NOTES.md', 'BnF fr.3041 f.18r\n')
    w('ciphers/debosnys-1883/NOTES.md', 'BnF fr.3042 f.5r\n')
    w('ciphers/fr3974-nevers/NOTES.md', 'BnF fr.3983 f.12r read.\n')
    return r


def notice(cote, items):
    body = ''.join('<p>Fol. %s • %d Pièce en chiffre.</p>' % (f, i + 1) for i, f in enumerate(items))
    return '<html><p>%s • Recueil</p>%s</html>' % (cote, body)


def main():
    r = fake_root()
    try:
        bf._OWN.clear()
        assert bf.own_hits('fr.3040', 18, r) == ['fr3040-x'], bf.own_hits('fr.3040', 18, r)
        assert bf.own_hits('fr.3040', 22, r) == ['fr3040-x']               # folder-context line
        assert bf.own_hits('fr.2988', 1, r) == ['_triage']
        assert bf.own_hits('fr.2988', 22, r) == []                         # bare folio in _triage: no context
        assert bf.own_hits('fr.29880', 18, r) == []
        assert bf.own_hits('fr.3040', 19, r) == []
        assert bf.own_hits('fr.3041', 18, r) == []                         # RESTRICTED.md folder skipped
        assert bf.own_hits('fr.3042', 5, r) == []                          # debosnys-1883 skipped
        assert bf.range_vols('fr.3974-3995')[9] == 'fr.3983' and bf.range_vols('fr.3040') == ['fr.3040']
        v = bf.score_volume(notice('Français 3040', ['18', '19', '30']), 'ccx', r, None, False, True)
        assert (v['ours_items'], v['open_bare'], v['ours_slugs']) == (1, 2, 'fr3040-x'), v
        v0 = bf.score_volume(notice('Français 3040', ['18', '19', '30']), 'ccx', r, None, False, False)
        assert v0['open_bare'] == 3 and 'ours_items' in v0                 # without --prior-work: counts unchanged
        v = bf.score_volume(notice('Français 3974-3995', ['12', '40']), 'ccy', r, None, False, True)
        assert (v['ours_items'], v['ours_range'], v['open_bare']) == (0, 1, 2), v
    finally:
        shutil.rmtree(r)
    # active edition reads the real registry (tools/data/prior_portals.tsv), offline
    v = bf.score_volume(open(os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-09/cc49442s.html'), errors='ignore').read(),
                        'cc49442s', ROOT, None, False, True)
    assert v['contact_first'] == 'mary-castelnau-edition', v['contact_first']
    v = bf.score_volume(open(os.path.join(ROOT, 'sources/bnf-findingaids/2026-10-07/cc49884s.html'), errors='ignore').read(),
                        'cc49884s', ROOT, None, False, True)
    assert v['cote'] == 'fr.3413' and v['contact_first'] == '', v
    print('test_bnf_findingaid_prior: all ok')


if __name__ == '__main__':
    main()

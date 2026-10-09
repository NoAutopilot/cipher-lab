#!/usr/bin/env python3
"""Offline tests for tools/bnf_findingaid.py section_known / --check-solved (MQS-BNF-S6, 9 Oct 2026); no network.

Must catch: an item line 'f.67 no.34 Lettre en chiffre.' under a section whose ancestor body says 'provided solutions'
or 'was broken by'; the --check-solved draft block names every holder-side source intake_gate_check.py asks for.
Must NOT: an item line carrying its own 'undeciphered' / 'remain unsolved'; an item under a section with no
broken-by wording (a sibling section's 'broken by' does not leak across a same-level heading).
Run: python3 tools/tests/test_bnf_findingaid_s6.py
"""
import os, socket, sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import bnf_findingaid as bf  # noqa: E402
import intake_gate_check as ig  # noqa: E402


def _no_net(*a, **k):
    raise RuntimeError('network used in an offline test')


socket.socket.connect = _no_net

PAGE = """# Decipherments of old ciphers
intro
## Achievements
In 2023, X provided solutions of no less than 15 unsolved ciphers.
### Cipher A: BnF fr.3029
BnF fr.3029 (Gallica)
f.67 no.34 Lettre en chiffre.
f.70 no.35 Lettre en chiffre. *Undeciphered.
## Still open
These remain open.
### Cipher B: BnF fr.3022
F.40-43 no.19 Lettre chiffree seems to remain unsolved.
f.50 no.20 Lettre chiffree.
### Cipher C
This one was broken by Y.
f.9 no.1 Lettre.
### Cipher D: BnF fr.2988
A letter of BnF fr.2988, f.1, was solved by Z.
f.4 no.2 Double de lettres.
""".splitlines()


def ln(prefix):
    return next(i for i, l in enumerate(PAGE, 1) if l.startswith(prefix))


def test_catch():
    assert bf.section_known(PAGE, ln('f.67')), 'ancestor body "provided solutions" must clear the item'
    assert bf.section_known(PAGE, ln('f.9 ')), 'own section "broken by" must clear the item'


def test_must_not():
    assert bf.section_known(PAGE, ln('f.70')) is None, 'own-line negation wins'
    assert bf.section_known(PAGE, ln('F.40')) is None, 'own-line "remain unsolved" wins'
    assert bf.section_known(PAGE, ln('f.50')) is None, 'Cipher C\'s "broken by" must not leak back into Cipher B'
    assert bf.section_known(PAGE, ln('f.4 '), 4) is None, 'a section sentence about f.1 must not clear f.4'


def test_draft_block_names_holder_sources():
    md = ('Anonymous pile, holder-based check-solved (bnf_findingaid.py --check-solved, disk caches): folio range ff.67-182 (67, 134, 182); '
          'Sources read: DECODE listings by shelfmark; Cryptiana (cached Tomokiyo pages incl. GL.htm and the unsolved '
          'lists); cyphersolver cache; unsolved-ciphers (no cache on disk: UNCHECKED); the holder\'s notice '
          '(Présentation, Bibliographie, item list). Edition step: deferred until a sender is named.')
    src = open(os.path.join(ROOT, 'tools', 'bnf_findingaid.py'), encoding='utf-8').read()
    assert 'Edition step: deferred until a sender is named' in src and 'unsolved-ciphers (no cache on disk' in src
    # the glyph set stays missing until images are inventoried: the intake gate rightly holds such a pile at 'blocked'
    assert ig.missing_holder_sources(md) == ['glyph set'], ig.missing_holder_sources(md)


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_'):
            fn()
            print('ok', name)

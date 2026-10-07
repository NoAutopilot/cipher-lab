#!/usr/bin/env python3
"""Offline test for tools/key_crossmatch.py's identity-key and clear-line filters (FRESH-0914, 7 Oct 2026; the
XMATCH-0307 loader artifact: rah-juan-manuel-1521/key_tomokiyo_alpha.tsv loaded as a=a..z=z and "read" the clear
note/crib lines of trew-posthius-1614-18/ciphertext.tsv). Scope (CLAUDE.md Usage 8a):
  must DROP  a key whose values equal their own codes in >= 80% of cells (the letter->shape table, and a synthetic
             a=a..z=z), and the letters of a line labelled note/crib/clear/gloss/plain ('1614_note1', '1614_crib2');
  must KEEP  a real letter-valued substitution key with a few fixed points (a reciprocal pair table where 3 of 24
             cells map to themselves), a digit key, and cipher lines whose labels merely contain those words inside
             another word ('1618_keynote' is not a whole label part; 'c1', 'spec2', 'L04').
Fixtures are written to a temporary directory; the one repo file read is the Juan Manuel table itself.
Run: python3 tools/tests/test_key_crossmatch_identity.py"""
import random, string, sys, tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx
import decode_key as dk

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


def as_key(pairs):
    return {c: {'value': v} for c, v in pairs}


# ---- identity_share / the gate
ident = as_key((c, c) for c in string.ascii_lowercase)
check('identity a=a..z=z share 1.0', kx.identity_share(ident) == 1.0)
rnd = random.Random(3)
perm = list(string.ascii_lowercase); rnd.shuffle(perm)
sub = as_key(zip(string.ascii_lowercase, perm))
check('random substitution share < 0.8', kx.identity_share(sub) < kx.IDENTITY_MAX_SHARE)
few = as_key([(c, c) for c in 'abc'] + [(c, 'x') for c in 'defghijklmnopqrstuvwxy'])
check('3 fixed points of 25 kept', kx.identity_share(few) < kx.IDENTITY_MAX_SHARE)
digits = as_key((str(10 + i), c) for i, c in enumerate(string.ascii_lowercase))
check('digit key share 0', kx.identity_share(digits) == 0.0)
check('alternatives use first value', kx.identity_share(as_key([('a', 'a|b'), ('b', 'c|b')])) == 0.5)

# ---- the real repo table that caused the artifact is refused by load_key_meta
jm = ROOT / 'ciphers/rah-juan-manuel-1521/key_tomokiyo_alpha.tsv'
if jm.exists():
    key, reason = kx.load_key_meta(jm)
    check(f'Juan Manuel letter->shape table refused ({reason})', key is None and 'identity' in str(reason))
else:
    print('SKIP Juan Manuel table not on disk')

# ---- clear line labels
for lab, want in [('1614_note1', True), ('1614_crib2', True), ('clear', True), ('f12_gloss', True),
                  ('plain-3', True), ('1614_c1', False), ('1618_spec2', False), ('L04', False),
                  ('1618_keynote', False), ('notebook', False), ('', False)]:
    check(f'clear_line_label({lab!r}) is {want}', kx.clear_line_label(lab) == want)

with tempfile.TemporaryDirectory() as td:
    p = Path(td) / 'ciphertext.tsv'
    rows = ['line\tposition\tsign\tconfidence']
    for lab, word in [('1614_note1', 'eandem'), ('1614_c1', 'awsfir'), ('1614_crib1', 'fridericus'), ('1614_c2', 'uao')]:
        rows += [f'{lab}\t{i + 1}\t{ch}\tH' for i, ch in enumerate(word)]
    p.write_text('\n'.join(rows) + '\n', encoding='utf-8')
    recs = dk.LOADERS[dk.detect_format(str(p))](str(p), {})
    check('dk tsv path keeps only cipher lines', ''.join(kx.recs_to_signs(recs)) == 'awsfiruao')
    check('robust_tsv_signs keeps only cipher lines', ''.join(kx.robust_tsv_signs(p) or []) == 'awsfiruao')

# ---- the combined Trew file is skipped by name, its cipher-only job files are not
kept, dropped = kx.find_ciphertext_files()
rels = {str(q.relative_to(ROOT)) for q in kept}
if (ROOT / 'ciphers/trew-posthius-1614-18/ciphertext.tsv').exists():
    check('trew combined ciphertext.tsv skipped', 'ciphers/trew-posthius-1614-18/ciphertext.tsv' not in rels)
    check('trew ciphertext_1614.tsv kept', 'ciphers/trew-posthius-1614-18/ciphertext_1614.tsv' in rels)

print('ALL PASS' if not fails else f'{fails} FAIL')
sys.exit(1 if fails else 0)

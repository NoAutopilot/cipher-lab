#!/usr/bin/env python3
"""Offline test for tools/tool_shelf.py (TOOL-SHELF, 3 Oct 2026).
Part 1 runs against a synthetic temp repository (fixture shelf, tools and target folders); part 2 checks the real shelf
offers the right tool for the brief's own example problems and never hides a weak grade. No network.
Run: python3 tools/tests/test_tool_shelf.py"""
import contextlib
import io
import os
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import tool_shelf as ts

fails = 0


def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name)
    fails += not ok


def run(*argv, root=None):
    buf = io.StringIO()
    args = list(argv) + (['--root', str(root)] if root else [])
    with contextlib.redirect_stdout(buf):
        rc = ts.main(args)
    return rc, buf.getvalue()


# --- part 1: fixture repository
tmp = Path(tempfile.mkdtemp())
(tmp / 'tools' / 'data').mkdir(parents=True)
(tmp / 'tools' / 'families').mkdir()
(tmp / 'tools' / 'digits.py').write_text('"""Solver for unseparated digit ciphers."""\n')
(tmp / 'tools' / 'pages.py').write_text('"""Page detector."""\n')
(tmp / 'tools' / 'families' / 'masc.py').write_text('"""masc family."""\n')
(tmp / 'tools' / 'families' / '__init__.py').write_text('')
hdr = 'tool\tkind\tgrade\tuse_when\tevidence\tlast_outcome\n'
rows = ('digits.py\tinstrument\tcontrolled-only\tunseparated digit cipher no key\tsynthetic 1.000\t-\n'
        'pages.py\tinstrument\tweak\tfind cipher pages in a volume\trecall 0.69\t-\n'
        'families/masc.py\tinstrument\tuntested\tsimple substitution family\t-\t-\n')
(tmp / 'tools' / 'data' / 'tool_shelf.tsv').write_text(hdr + rows)
for folder, text in (('t1', 'ran tools/digits.py'), ('t2', 'see digits.py'), ('t3', 'family_run.py --family masc')):
    (tmp / 'ciphers' / folder).mkdir(parents=True)
    (tmp / 'ciphers' / folder / 'NOTES.md').write_text(text + '\n')

rc, out = run('--check', root=tmp)
check('check passes when every tool is shelved', rc == 0 and '3 rows' in out)
(tmp / 'tools' / 'orphan.py').write_text('"""x"""\n')
rc, out = run('--check', root=tmp)
check('check fails on an unshelved tool', rc == 1 and 'MISSING shelf row: orphan.py' in out)
(tmp / 'tools' / 'orphan.py').unlink()

counts = ts.citation_counts(str(tmp), ['digits.py', 'pages.py', 'families/masc.py'])
check('folder counts are live', counts == {'digits.py': 2, 'pages.py': 0, 'families/masc.py': 1})

rc, out = run('unseparated digits, no key', root=tmp)
check('query offers the digit solver first', rc == 0 and out.startswith('[controlled-only] digits.py'))
check('query prints the live folder count', 'cited by 2 folders' in out)
rc, out = run('find cipher pages', root=tmp)
check('weak grade printed before the tool name', out.startswith('[weak] -- ') and 'pages.py' in out.splitlines()[0])
rc, out = run('simple substitution', root=tmp)
check('untested tool carries the known-answer advice', 'run its known-answer check before trusting it' in out)
rc, out = run('zzzz qqqq', root=tmp)
check('no match says so (nonzero)', rc == 1 and 'no shelf row matches' in out)

(tmp / 'NEXT-STEPS.tsv').write_text('# header\nfolder\tstatus\tblocker\tcost_band\tnear_row\tlast_touched\tnext_step\t'
                                   'parallel\tnext_step_full_len\n'
                                   'tA\topen\trunnable\tS\tn\t3 Oct 2026\tunseparated digit run, no key yet\t--\t30\n'
                                   'tC\tpartial\trunnable\tS\tn\t3 Oct 2026\tfind the volume first\t--\t30\n'
                                   'tB\tclosed-negative\trunnable\tS\tn\t3 Oct 2026\tunseparated digit run\t--\t30\n')
rc, out = run('--underused', root=tmp)
check('underused finds a 0-1-cited tool matching an open/partial step', 'pages.py [weak] cited by 0: tC' in out)
check('underused skips tools cited by 2+ folders', 'digits.py' not in out)
check('underused ignores closed targets', 'tB' not in out)

# --- part 2: the real shelf
rc, out = run('--check')
check('real shelf: every tool shelved, grades valid', rc == 0)
for q, tool in (('unseparated digit cipher, no key', 'seg_homophonic.py'),
                ('a key on disk might read another ciphertext', 'key_crossmatch.py'),
                ('find cipher pages in a whole volume', 'cipher_page_detector.py'),
                ("leaf with a clerk's plaintext", 'decode_witness.py'),
                ('sign shapes unsettled', 'glyph_atlas.py')):
    rc, out = run('--top', '3', q)
    check('real shelf offers %s for %r' % (tool, q), tool in out)
rc, out = run('--top', '1', 'find cipher pages in a whole volume')
check('real shelf: cipher_page_detector shown weak first', out.startswith('[weak]'))

print('ALL PASS' if not fails else '%d FAIL' % fails)
sys.exit(1 if fails else 0)

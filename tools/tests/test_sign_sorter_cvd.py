#!/usr/bin/env python3
"""Offline test for sorter_preflight.py's colour check (check 5, --cvd; MQS-SORTER, 9 Oct 2026). Run: python3 tools/tests/test_sign_sorter_cvd.py
Must catch: the legacy sorter tokens (green/red/orange), a red/green pair, a dark block that leaves light text on the yellow tint, a hint
naming "red", a lede saying "a green check", a box colour under 3:1 against a parchment page median (no under-stroke).
Must NOT block: the updated template; "ordered", "required" and "entered" in a hint; "green" in a pile name or a data value."""
import re, subprocess, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parent.parent.parent
sys.path.insert(0, str(ROOT / 'tools'))
import sorter_preflight as sp
from PIL import Image

fails = 0
def check(name, ok):
    global fails
    print('PASS' if ok else 'FAIL', name); fails += not ok

T = (ROOT / 'tools' / 'sign_sorter' / 'template.html').read_text()
render = lambda t, lede='A lede.', data='{"piles": []}': t.replace('__TITLE__', 'T').replace('__LEDE__', lede).replace('__DATA__', data)
ok = lambda html, data=None, **kw: sp.check_cvd(html, data or {}, **kw)

r = ok(render(T))
check('the updated template passes', r[0] is True)
legacy = T
for new, old in (('--accent:#24211c; --accent-soft:#e4dfd3; --ok:#0072B2; --ok-soft:#dde7ee; --warn:#24211c; --warn-soft:#e9e4d3; --bad:#B35900;',
                  '--accent:#8a3b12; --accent-soft:#f1e2d6; --ok:#2f6b3a; --ok-soft:#dcebdc; --warn:#9a6a00; --warn-soft:#f3e7c4; --bad:#b3261e;'),):
    assert new in legacy; legacy = legacy.replace(new, old)
r = ok(render(legacy))
check('legacy light tokens (green ok, red bad, orange accent) FAIL', r[0] is False and 'dE2000' in r[1])
rg = T.replace('--ok:#0072B2;', '--ok:#2f6b3a;').replace('--bad:#B35900;', '--bad:#b3261e;', 1)
r = ok(render(rg))
check('a red/green pair FAILS', r[0] is False and '#2f6b3a' in r[1] and '#b3261e' in r[1])
dark = T.replace('--on-tint:#1b1916;', '--on-tint:#ece6dc;')
r = ok(render(dark))
check('a dark block with light text on the yellow tint FAILS', r[0] is False and 'dark' in r[1] and 'tint' in r[1])
r = ok(render(T, lede='Tap the red x on a sign.'))
check('a lede naming "red" FAILS', r[0] is False and 'red' in r[1])
r = ok(render(T, lede='Tiles with a green check are the ones you sorted.'))
check('a lede saying "a green check" FAILS', r[0] is False and 'green' in r[1])
r = ok(T.replace('Click the <b>?</b> badge', 'Click the orange <b>?</b>').replace('__TITLE__', 'T').replace('__LEDE__', 'x').replace('__DATA__', '{}'))
check('a hint naming "orange" FAILS', r[0] is False and 'orange' in r[1])
r = ok(render(T), {'focusNote': 'Each is about as close to two piles; the red pile is the machine pick.'})
check('a focus note naming a colour FAILS', r[0] is False)
r = ok(render(T, lede='Piles are ordered, entered by hand and required for the next step.'))
check('must not block: "ordered", "entered", "required" in a hint', r[0] is True)
r = ok(render(T), {'piles': [{'id': 'green-T1', 'items': []}], 'rank': [{'sid': 's', 'why': 'Which pile? green-T1 / T2', 'detail': ''}]})
# the rank caption is person-facing: a pile id inside it is a pile name, exempt only through 'piles'; a colour word there is a caption word
check('must not block: "green" in a pile name or a data value (piles[].id)', ok(render(T), {'piles': [{'id': 'green', 'family': 'green', 'items': []}]})[0] is True)
# box colours against a page median
parch = {'p': Image.new('RGB', (64, 64), (0xd9, 0xc7, 0xa0))}
r = ok(render(T), {}, rgb=parch)
check('box colours with their white under-stroke pass on a parchment page (#d9c7a0)', r[0] is True)
noundr = T.replace("under: '#ffffff'", "under: ''")
r = ok(render(noundr), {}, rgb=parch)
check('a box colour under 3:1 on a parchment median with no under-stroke FAILS (dark orange 2.91:1)', r[0] is False and 'box outline' in r[1])
check('a page with no :root tokens is n/a, not a fail', sp.check_cvd('<html>hi</html>', {})[0] is None)
p = subprocess.run([sys.executable, str(ROOT / 'tools' / 'sorter_preflight.py'), '--cvd'], capture_output=True, text=True)
check('CLI --cvd on the template exits 0', p.returncode == 0 and p.stdout.startswith('PASS'))
print('FAILED' if fails else 'ALL PASS'); sys.exit(1 if fails else 0)

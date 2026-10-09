"""Offline test for tools/tx_register.py (TX-REGISTER, account 4, 9 Oct 2026): the compiler keeps every row (an
unreadable status is written `unparsed`, never dropped), and --check blocks a re-run of a retired family with no stated
difference while letting through a PREREG that names a different instrument."""
import os, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_register

IDEAS = """# TX-IDEAS test

| rank | id | idea | attacks | cheapest test | status |
|---|---|---|---|---|---|
| 1 | M1 | Compare, don't recall | C1 | dev_tune, cap 10 | tested-dev-FAIL |
| 2 | M9 | Deskew | C2 | covered by iiif_lines | covered |
| 3 | M13 | Fatigue caps | -- | none | retired (no mechanism) |
| 4 | M10 | Doubt-only reader | C1 | dev_tune | queued |

## Results log
| date UTC | id | PREREG | dev result | eval result (p; looks so far) | verdict |
|---|---|---|---|---|---|
| 9 Oct 07:26 | M1 | PREREG-a | dev_tune fixed 4 / broken 16, p 0.012 | not taken; looks so far 0 | FAIL |
| 9 Oct 07:28 | M1b | PREREG-a amendment | fixed 2 / broken 12 | not taken; looks so far 0 | retired (three fixes, all wrong way) |
| 9 Oct 07:30 | M2 | PREREG-b | fixed 9 | x | something nobody can map |
"""


def make_root():
    d = tempfile.mkdtemp()
    os.makedirs(os.path.join(d, 'research'))
    with open(os.path.join(d, 'research', 'TX-IDEAS-2026-10-09.md'), 'w') as fh:
        fh.write(IDEAS)
    return d


def test_compile_keeps_every_row():
    root = make_root()
    rows = tx_register.compile_register(root)
    by = {r['id']: r for r in rows}
    assert by['M1']['verdict'] == 'dev-FAIL' and by['M1']['date'] == '2026-10-09 07:26'
    assert by['M1']['eval_looks'] == '0' and 'fixed 4' in by['M1']['dev_result']
    assert by['M1b']['verdict'] == 'retired'
    assert by['M13']['verdict'] == 'retired' and by['M10']['verdict'] == 'queued'
    # unmappable status and verdict cells are kept as unparsed with the source line, never dropped
    assert by['M9']['verdict'] == 'unparsed' and 'covered' in by['M9']['reason']
    assert by['M2']['verdict'] == 'unparsed' and 'nobody can map' in by['M2']['reason']
    assert len(rows) == 6


def register(root):
    rows = tx_register.compile_register(root)
    path = os.path.join(root, 'research', 'TX-REGISTER.tsv')
    with open(path, 'w') as fh:
        tx_register.write_tsv(rows, fh)
    return path


def run_check(root, text):
    p = os.path.join(root, 'PREREG-new.md')
    with open(p, 'w') as fh:
        fh.write(text)
    return tx_register.main(['--root', root, '--check', p])


def test_check_catches_retired_rerun():
    root = make_root()
    register(root)
    # must catch: a retired family (M1b) re-run with no different instrument or new material
    bad = "# PREREG\n\n## Nearest prior\nM1b showed exemplars pull; this run repeats the layout at a lower threshold.\n"
    assert run_check(root, bad) == 1
    # must catch: no Nearest prior section at all
    assert run_check(root, "# PREREG\n\nWe read dev_tune again with M1's layout.\n") == 1
    # a section naming no register id
    assert run_check(root, "# PREREG\n\nNearest prior: nothing like this has been tried before here.\n") == 1


def test_check_allows_retired_with_instrument():
    root = make_root()
    register(root)
    ok = ("# PREREG\n\n## Nearest prior / differs from\nM1b retired the compare layout; this uses a different instrument "
          "(a pixel classifier, no exemplar shown to any reader).\n")
    assert run_check(root, ok) == 0
    inline = ("# PREREG\n\nNearest prior: M13 (fatigue caps, retired); this differs by new material, a 400-sign "
              "eval leaf from another hand.\n")
    assert run_check(root, inline) == 0


def test_check_allows_non_retired():
    root = make_root()
    register(root)
    ok = "# PREREG\n\nNearest prior: M1 (dev-FAIL); this differs in reading tiles at 4x with no sheet at all.\n"
    assert run_check(root, ok) == 0


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
    print('ok')

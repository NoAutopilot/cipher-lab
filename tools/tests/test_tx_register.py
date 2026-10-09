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


IDEAS2 = """# TX-IDEAS-2 test

| rank | id | idea | attacks | cheapest test | status |
|---|---|---|---|---|---|
| 1 | X15 | Atlas features | lattice | read-free | not run: superseded by X3's step 1 |
| 2 | X18 | Office atlas | invent | none | not run: no known answer to score against |

## Results log
| date UTC | id | PREREG | dev result | eval result (p; looks so far) | verdict |
|---|---|---|---|---|---|
| 9 Oct 15:1x | 0a | PREREG-t2-0 | power 0.8-5% | n/a | the gate is set (p < 0.01 at >= 32) |
| 9 Oct 15:31 | 0b-152 | PREREG-t2-0 0b | n/a | built | eval pool 34 -> p < 0.01 branch |
| 9 Oct 16:53 | X9+X17 | PREREG-t2-2 X9 | 10/12 PASS | x | sorter feed updated (benchmark-tx/txeng2/doubt/RESULTS.md) |
| 9 Oct 18:46 | V2 | PREREG-t2-5 V2 | n/a | 2 FLAG | verified; Amendment 4 (benchmark-tx/txeng2/spinflags/RESULTS.md) |
| 9 Oct 19:1x | E-f178r | Amendment 4 | n/a | pool 29 | pool restored (units/labels_f178r.tsv) |
| 9 Oct 18:47 | P1 | PREREG-t2-5 P1 | 4/4 boxed | n/a | product, partial |
| 9 Oct 19:0x | X2c | PREREG-t2-5 X2c | not run | n/a | cancelled (Amendment 4); blocked: no ink |
| 9 Oct 19:24 | X21b | PREREG-t2-6 X21b | 17/11 p 0.345 | not taken; looks 0 | null: untested at this N |
| 9 Oct 19:16 | SC1 | PREREG-t2-6 SC1 | f.162r only | n/a | done: the hand is exhausted |
| 9 Oct 20:07 | B1 | PREREG-t2-6 B1 | n/a | 0.057 | baseline change, never a gain |
| 9 Oct 19:30 | O1 | PREREG-t2-6 O1 | n/a | n/a | audit on file: corrected sentences |
| 9 Oct 19:31 | A1 | PREREG-t2-6 A1 | n/a | n/a | on file; B1 spawned |
| 9 Oct 19:40 | R3b | PREREG-t2-6 R3b | n/a | n/a | gate incomplete as declared; retired for this leaf, instrument tools/gloss_cut.py |
| 9 Oct 17:20 | R2 | PREREG-t2-3 R2 | kp2 0.124 | n/a | pooled by the R2 rule, then REMOVED at check-in 4 |
| 9 Oct 17:30 | C1 | PREREG-t2-3 C1 | n/a | n/a | FAIL: truth-unknown items |
| 9 Oct 20:4x | X1b-v4, A2, REGFIX | PREREG-t2-8 | -- | -- | running |
"""


def make_root2(extra_row=''):
    root = make_root()
    with open(os.path.join(root, 'research', 'TX-IDEAS-2-2026-10-09.md'), 'w') as fh:
        fh.write(IDEAS2 + extra_row)
    return root


def write_results(root, name, text):
    d = os.path.join(root, 'benchmark-tx', 'txeng2', name)
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, 'RESULTS.md'), 'w') as fh:
        fh.write(text)


def test_lane_verdict_shapes():
    by = {r['id']: r for r in tx_register.compile_register(make_root2())}
    want = {'0a': 'measured', '0b-152': 'measured', 'X9+X17': 'measured', 'V2': 'measured', 'E-f178r': 'measured',
            'P1': 'measured', 'X2c': 'retired', 'X21b': 'non-test', 'SC1': 'measured', 'B1': 'measured',
            'O1': 'measured', 'A1': 'measured', 'R3b': 'retired', 'R2': 'non-test', 'C1': 'dev-FAIL',
            'X1b-v4, A2, REGFIX': 'running', 'X15': 'non-test', 'X18': 'non-test'}
    got = {k: by[k]['verdict'] for k in want}
    assert got == want, got
    assert by['X21b']['reason'].startswith('null')
    assert 'reopen when: new material -- ink' in by['X2c']['reason']


def test_results_outcome_fallback():
    root = make_root2()
    write_results(root, 'model2', '# TXE2-MODEL2\n\nSome text.\n\n**Outcome: null.** Opus ahead 17/11, p 0.345.\n')
    write_results(root, 'sheet2', '# TXE2-SHEET2\n\n| a | gate |\n|---|---|\n\n**Declared gate on Spinelli: MET** (0.571).\n')
    write_results(root, 'feed', '# TXE2-FEED\n\nNo experiment, no gate (S4 is a product).\n')
    write_results(root, 'plain', '# TXE2-PLAIN\n\nNumbers only, nothing said about the outcome here.\n')
    # a file cited by a results-log row is covered by that row, not listed again
    write_results(root, 'spinflags', '# TXV-SPIN\n\n## Verdicts (2 FLAG, 4 KEEP)\n')
    by = {r['id']: r for r in tx_register.compile_register(root)}
    assert by['txeng2/model2']['verdict'] == 'non-test'
    assert by['txeng2/sheet2']['verdict'] == 'dev-PASS'
    assert by['txeng2/feed']['verdict'] == 'measured'
    assert by['txeng2/plain']['verdict'] == 'unparsed' and 'no Verdict line' in by['txeng2/plain']['reason']
    assert 'txeng2/spinflags' not in by
    # must catch: the unparsed txeng2 RESULTS row blocks --check
    assert tx_register.main(['--root', root, '--check']) == 1


def test_check_catches_unparsed_current():
    # must catch: a txeng2 results-log row whose verdict text the mapper does not know, with or without a PREREG
    root = make_root2('| 9 Oct 21:00 | Z9 | PREREG-t2-9 | x | y | something nobody can map |\n')
    register(root)
    assert tx_register.main(['--root', root, '--check']) == 1
    ok = "# PREREG\n\nNearest prior: M1 (dev-FAIL); this differs in reading tiles at 4x with no sheet at all.\n"
    assert run_check(root, ok) == 1
    assert tx_register.main(['--root', make_root2(), '--check']) == 0


def test_check_ignores_first_campaign_unparsed():
    # must NOT block: the first campaign's unparsed rows (M9 "covered", M2) stay unparsed and pass --check
    root = make_root2()
    register(root)
    rows = tx_register.compile_register(root)
    assert any(r['campaign'] == 'txeng' and r['verdict'] == 'unparsed' for r in rows)
    assert tx_register.main(['--root', root, '--check']) == 0


if __name__ == '__main__':
    for name, fn in list(globals().items()):
        if name.startswith('test_'):
            fn()
    print('ok')

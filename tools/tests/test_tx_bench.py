"""Offline test for tools/tx_bench.py (TX-BENCH, 3 Oct 2026)."""
import io, json, os, sys, tempfile, contextlib
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import tx_bench


def _w(d, name, text):
    p = os.path.join(d, name)
    with open(p, 'w') as f:
        f.write(text)
    return p


def _run(argv):
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        rc = tx_bench.main(argv)
    return rc, buf.getvalue()


def test_scoring():
    with tempfile.TemporaryDirectory() as d:
        # truth: 6 positions; pos 2 is a homophone set, pos 6 excluded
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'L1\t1\tA\tA\ta\tscored\nL1\t2\tB\tB|C\tb\tscored\nL1\t3\tD\tD\td\tscored\n'
           'L1\t4\tE\tE\te\tscored\nL1\t5\tF\tF\tf\tscored\nL1\t6\tX\t\t\texcluded:off-sheet\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        # perfect, with a homophone swap at pos 2 (C in place of B) -> 0 errors
        o = _w(d, 'o1.tsv', 'line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ACDEFX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert rc == 0 and r['errors'] == 0 and r['scored'] == 5 and r['excluded'] == 1, r
        # misread D->Q, deleted E, one inserted Z: 3 errors / 5
        o = _w(d, 'o2.tsv', 'passage\tpos\tsign_id\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ABQFZX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert (r['wrong'], r['deleted'], r['inserted'], r['errors']) == (1, 1, 1, 3), r
        assert any('<-Q' in c for c in r['top_confusions']) and any('<deleted>' in c for c in r['top_confusions']), r
        rc, out = _run([o, '--bench', bench, '--json', '--legacy'])  # the Wilson interval survives only in --legacy
        lo, hi = json.loads(out)['items'][0]['wilson95']
        assert lo < 0.6 < hi
        # an output on lines the bench does not have -> exit 2
        o = _w(d, 'o3.tsv', 'line\tpos\tsign\nZZ\t1\tA\n')
        rc, _ = _run([o, '--bench', bench])
        assert rc == 2


def test_label_map():
    # reconciler split one instruction label into two (D and 4); a reader given only '4' is right under the map
    with tempfile.TemporaryDirectory() as d:
        _w(d, 't.truth.tsv', 'line\tpos\tref_sign\ttruth\tplain\tstatus\n'
           'L1\t1\tD\tD\ta\tscored\nL1\t2\tq\tq\tq\tscored\nL1\t3\t4\t4\tl\tscored\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\tdev\n')
        o = _w(d, 'o.tsv', 'line\tpos\tsign\nL1\t1\t4\nL1\t2\tq\nL1\t3\t4\n')
        rc, out = _run([o, '--bench', bench, '--json'])
        assert rc == 0 and json.loads(out)['items'][0]['errors'] == 1
        m = _w(d, 'm.tsv', '# c\nfrom\tto\nD\t4\n')
        rc, out = _run([o, '--bench', bench, '--json', '--label-map', m])
        assert rc == 0 and json.loads(out)['items'][0]['errors'] == 0
        # a genuine misread stays wrong under the map
        o2 = _w(d, 'o2.tsv', 'line\tpos\tsign\nL1\t1\tq\nL1\t2\tq\nL1\t3\t4\n')
        rc, out = _run([o2, '--bench', bench, '--json', '--label-map', m])
        assert json.loads(out)['items'][0]['errors'] == 1


def test_wilson():
    lo, hi = tx_bench.wilson(0, 10)
    assert lo == 0.0 and 0.25 < hi < 0.35
    assert tx_bench.wilson(0, 0) == (0.0, 0.0)


def test_repo_bench_parses():
    root = os.path.join(os.path.dirname(__file__), '..', '..')
    b = os.path.join(root, 'BENCHMARK-TX.tsv')
    if not os.path.exists(b):
        return
    for item in tx_bench.read_tsv(b):
        rows = tx_bench.read_tsv(os.path.join(root, item['truth']))
        assert sum(r['status'] == 'scored' for r in rows) == int(item['n_scored']), item['item']
        assert item['split'] in ('dev', 'eval') or item['split'].startswith('confirm'), item['split']  # confirm/confirm2: sealed confirmation items




def test_exclude_flagged():
    with tempfile.TemporaryDirectory() as d:
        # pos 3 flagged (excluded under the switch), pos 4 corrected (stays scored), pos 6 excluded already
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n'
           'L1\t1\tA\tA\ta\tscored\t\nL1\t2\tB\tB\tb\tscored\t\nL1\t3\tD\tD\td\tscored\talignment-doubtful\n'
           'L1\t4\tE\tE|Q\te\tscored\tcorrected:key-doubtful\nL1\t5\tF\tF\tf\tscored\t\nL1\t6\tX\t\t\texcluded:off-sheet\t\n')
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        # wrong at 3 (flagged) and 5 (not flagged); Q at 4 is right after correction
        o = _w(d, 'o.tsv', 'line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate('ABZQZX')))
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert (r['errors'], r['scored']) == (2, 5) and 'flagged_excluded' not in r, r
        rc, out = _run([o, '--bench', bench, '--json', '--exclude-flagged'])
        r = json.loads(out)['items'][0]
        f = r['flagged_excluded']
        assert (r['errors'], r['scored']) == (2, 5), r  # as measured unchanged by the switch
        assert (f['errors'], f['scored'], f['flagged']) == (1, 4, 1), f
        rc, out = _run([o, '--bench', bench, '--exclude-flagged', '--legacy'])
        assert 'as measured 0.400 (2/5) | flagged excluded 0.250 (1/4)' in out, out
        # a truth file with no flag column: both figures equal
        _w(d, 't.truth.tsv', '# x\nline\tpos\tref_sign\ttruth\tplain\tstatus\nL1\t1\tA\tA\ta\tscored\n')
        o = _w(d, 'o3.tsv', 'line\tpos\tsign\nL1\t1\tA\n')
        rc, out = _run([o, '--bench', bench, '--json', '--exclude-flagged'])
        f = json.loads(out)['items'][0]['flagged_excluded']
        assert (f['errors'], f['scored'], f['flagged']) == (0, 1, 0), f



def test_two_rate():
    # TOOL-2RATE (10 Oct 2026): 20 positions, 10 unflagged, 1 wrong at an unflagged position, 2 insertions
    with tempfile.TemporaryDirectory() as d:
        signs = 'ABCDEFGHIJKLMNOPQRST'
        _w(d, 't.truth.tsv', 'line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n' + ''.join(
            'L1\t%d\t%s\t%s\t%s\tscored\t%s\n' % (i + 1, s, s, s.lower(), 'clerk-doubtful' if i >= 10 else '')
            for i, s in enumerate(signs)))
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        read = 'A9' + signs[2:] + 'YZ'  # wrong at pos 2 (unflagged); Y, Z inserted at the line end
        o = _w(d, 'o.tsv', 'line\tpos\tsign\n' + ''.join('L1\t%d\t%s\n' % (i + 1, s) for i, s in enumerate(read)))
        rc, out = _run([o, '--bench', bench, '--json', '--exclude-flagged'])
        r = json.loads(out)['items'][0]
        f = r['flagged_excluded']
        assert (r['errors'], r['scored'], r['err_true']) == (3, 20, 0.15), r  # as measured unchanged
        assert (f['errors'], f['scored'], f['err_true'], f['flagged']) == (3, 10, 0.3, 10), f
        assert (f['position_errors'], f['position_rate']) == (1, 0.1), f
        assert (f['inserted'], f['read'], f['insertion_rate']) == (2, 22, round(2 / 22, 4)), f
        rc, out = _run([o, '--bench', bench, '--exclude-flagged', '--legacy'])
        assert ('as measured 0.150 (3/20) | flagged excluded 0.300 (3/10) 95% ' in out
                and '[10 flagged] | position errors 1/10 = 0.100 | insertions 2 / read 22 = 0.091' in out), out
        # the corrected scorer carries the same decomposition in its flagged-excluded line
        rc, out = _run([o, '--bench', bench, '--exclude-flagged'])
        assert '[10 flagged] | position errors 1/10 = 0.100 | insertions 2 / read 22 = 0.091' in out, out
        # without the switch the (legacy) line format is untouched
        rc, out = _run([o, '--bench', bench, '--legacy'])
        assert 'position errors' not in out and 'flagged excluded' not in out, out


# --- TOOL-SCORER-FIX (PREREG-txeng2-17, 10 Oct 2026): the outside review's reproduced faults
# (research/SO-TX-TRANSCRIPTION-2026-10-10.md "Reproduction snippet"), each asserted in its FIXED form. Every test below
# fails on the pre-fix scorer (sha256 19640dae...) and passes after it.

def _rows(seq, line='L1'):
    return [dict(line=line, pos=str(i + 1), ref_sign=s, truth=s, plain=s.lower(), status='scored', flag='')
            for i, s in enumerate(seq)]


def _tsv(d, name, rows, cols=('line', 'pos', 'ref_sign', 'truth', 'plain', 'status', 'flag')):
    return _w(d, name, '\t'.join(cols) + '\n' + ''.join('\t'.join(r.get(c, '') for c in cols) + '\n' for r in rows))


def _out(d, name, lines):
    return _w(d, name, 'line\tpos\tsign\n' + ''.join('%s\t%d\t%s\n' % (ln, i + 1, s)
                                                     for ln, seq in lines.items() for i, s in enumerate(seq)))


def test_fix1_missing_line_is_deleted():
    # review assert 1, inverted: a truth line absent from the output counts every scored position as deleted
    truth = _rows(['A']) + _rows(['B'], 'L2')
    r = tx_bench.score_item(truth, {'L1': ['A']})
    assert (r['scored'], r['deleted'], r['lines_missing']) == (2, 1, ['L2']), r
    # the old behaviour survives only under its own name
    r = tx_bench.score_item(truth, {'L1': ['A']}, missing='skip')
    assert (r['scored'], r['deleted'], r['lines_missing']) == (1, 0, ['L2']), r
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', truth)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'L1': ['A']})
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert rc == 0 and (r['errors'], r['scored'], r['deleted']) == (1, 2, 1), r
        rc, out = _run([o, '--bench', bench, '--json', '--coverage-diagnostic'])
        r = json.loads(out)['items'][0]
        assert rc == 0 and (r['errors'], r['scored']) == (0, 1) and r['coverage_diagnostic'], r


def test_fix1_unknown_line_id_fails():
    # review row 2: an output line id absent from the truth fails validation with a non-zero exit
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', _rows(['A']))
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'L1': ['A'], 'EXTRA': ['X', 'X']})
        rc, _ = _run([o, '--bench', bench])
        assert rc != 0
        rc, _ = _run([o, '--bench', bench, '--coverage-diagnostic'])
        assert rc == 0


def test_fix2_paired_uses_rate_population():
    # review assert 2 / CLI probe, inverted: under --exclude-flagged the paired count runs on the flagged-excluded rows
    truth = _rows(['A', 'B'])
    truth[1]['flag'] = 'alignment-doubtful'
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', truth)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        base, o = _out(d, 'base.tsv', {'L1': ['A', 'X']}), _out(d, 'o.tsv', {'L1': ['A', 'B']})
        rc, out = _run([o, '--bench', bench, '--paired', base, '--exclude-flagged'])
        fl = [l for l in out.splitlines() if l.startswith('paired') and 'flagged excluded' in l]
        assert rc == 0 and len(fl) == 1, out
        assert 'fixed 0, broken 0' in fl[0] and '1 common scored signs' in fl[0], fl
        assert 'lines improved 0, worsened 0' in fl[0], fl
        # the as-measured paired line still sees the repair at position 2
        am = [l for l in out.splitlines() if l.startswith('paired') and 'as measured' in l]
        assert 'fixed 1' in am[0] and 'lines improved 1' in am[0], am


def test_fix3_insertion_repair_counts():
    # review assert 3, inverted: a pure insertion repair is a line improvement (position McNemar stays 0/0, beside)
    truth = _rows(['A', 'B'])
    p = tx_bench.paired(truth, {'L1': ['A', 'X', 'B']}, {'L1': ['A', 'B']})
    assert (p['lines_improved'], p['lines_worsened'], p['edits_base'], p['edits_out']) == (1, 0, 1, 0), p
    assert (p['fixed'], p['broken']) == (0, 0), p


def test_fix4_abstention_is_wrong_not_flagged():
    # reader abstentions are wrong in the full-output measure; accepted-token error and coverage printed apart;
    # --exclude-flagged drops truth-verifier flags only, never a reader abstention
    truth = _rows(['A', 'B', 'C', 'D'])
    truth[3]['flag'] = 'clerk-doubtful'
    r = tx_bench.score_item(truth, {'L1': ['A', 'UNKNOWN', 'C?', 'Z']})
    assert (r['wrong'], r['abstained'], r['accepted'], r['accepted_wrong']) == (3, 2, 2, 1), r
    # a truth set that happens to contain the abstention token still does not credit it
    t2 = _rows(['A']); t2[0]['truth'] = 'A|NONE'
    assert tx_bench.score_item(t2, {'L1': ['NONE']})['wrong'] == 1
    f = tx_bench.score_item(tx_bench.drop_flagged(truth), {'L1': ['A', 'UNKNOWN', 'C?', 'Z']})
    assert (f['scored'], f['wrong'], f['abstained']) == (3, 2, 2), f
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', truth)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'L1': ['A', 'UNKNOWN', 'C?', 'Z']})
        rc, out = _run([o, '--bench', bench, '--exclude-flagged'])
        assert 'accepted-token error 1/2 = 0.500 | coverage 2/4 = 0.500' in out, out
        assert 'truth-verifier flags only' in out, out


def test_fix5_standard_ser_and_ranking_note():
    # unit-cost Levenshtein SER beside the 0.75-indel figure; truth A B C D, read X A B C: the 0.75 path is
    # insert X + delete D (1.5 cost, counted 2), unit-cost is the same 2 here; and a file pair whose order flips
    truth = _rows(list('ABCD'))
    r = tx_bench.score_item(truth, {'L1': list('XABC')}, G=1.0)
    assert (r['wrong'] + r['deleted'] + r['inserted'], r['scored']) == (2, 4), r
    # 0.75 counts an S as D+I (2 edits) where unit cost takes one S: ABCD read ACD? -> compare a substitution-heavy line
    t = _rows(list('AB'))
    a075 = tx_bench.score_item(t, {'L1': ['Y', 'A', 'B', 'Z']})          # 2 insertions under both
    s1 = tx_bench.score_item(t, {'L1': ['Q', 'R']}, G=1.0)                  # 2 substitutions, unit 2
    s075 = tx_bench.score_item(t, {'L1': ['Q', 'R']})                       # 0.75 also prefers 2 S (cost 2 < 3)
    assert (a075['inserted'], s1['wrong'], s075['wrong']) == (2, 2, 2)
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', _rows(list('ABCD')))
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        base = _out(d, 'base.tsv', {'L1': list('ABCD')})
        o1 = _out(d, 'o1.tsv', {'L1': list('XABC')})
        rc, out = _run([o1, '--bench', bench, '--paired', base])
        assert 'standard SER (unit-cost Levenshtein) 0.500 (2/4)' in out, out
        # o2: one wrong sign (Z for B) and one inserted sign -> 0.75 err 2, unit SER 2; o3: AXCD -> 1 under both
        o2 = _out(d, 'o2.tsv', {'L1': list('AZCDW')})
        o3 = _out(d, 'o3.tsv', {'L1': list('ABQD')})
        rc, out = _run([o2, o3, '--bench', bench, '--paired', base])
        assert 'ranking sensitivity' not in out, out          # same order under both measures
        assert tx_bench.ranking_flips({'a': (0.5, 0.25), 'b': (0.25, 0.5)}) == [('a', 'b')]
        assert tx_bench.ranking_flips({'a': (0.5, 0.5), 'b': (0.25, 0.25)}) == []


def test_fix6_strict_visual_identity():
    # ref_sign A, truth A|HOMOPHONE, read HOMOPHONE: right value-compatible, wrong under --strict
    t = _rows(['A']); t[0]['truth'] = 'A|H'
    assert tx_bench.score_item(t, {'L1': ['H']})['wrong'] == 0
    assert tx_bench.score_item(t, {'L1': ['H']}, strict=True)['wrong'] == 1
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', t)
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'L1': ['H']})
        rc, out = _run([o, '--bench', bench, '--strict'])
        assert 'err_true(0.75-indel align) 0.000 (0/1)' in out and 'strict (exact ref_sign' in out, out
        assert 'strict (exact ref_sign, visual identity): err_true(0.75-indel align) 1.000 (1/1)' in out, out


def test_fix7_no_wilson_with_insertions_and_bootstrap():
    # one reference sign, four extra output signs: rate 4.0 printed, no Wilson interval; --ci gives a line bootstrap
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 't.truth.tsv', _rows(['A']) + _rows(['B'], 'L2'))
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nit1\tt.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'L1': ['A', 'X', 'X', 'X', 'X'], 'L2': ['B']})
        rc, out = _run([o, '--bench', bench])
        assert '2.000 (4/2)' in out and '95%' not in out, out
        rc, out = _run([o, '--bench', bench, '--json'])
        r = json.loads(out)['items'][0]
        assert 'wilson95' not in r, r
        rc, out = _run([o, '--bench', bench, '--ci'])
        assert 'line bootstrap 95% (1000 resamples, conditional on this item\'s 2 lines)' in out, out
        lo, hi = tx_bench.line_bootstrap({'L1': dict(N=1, E=4), 'L2': dict(N=1, E=0)})
        assert 0.0 <= lo <= 2.0 <= hi <= 4.0, (lo, hi)
        lo, hi = tx_bench.line_bootstrap({'L1': dict(N=1, E=4), 'L2': dict(N=1, E=0)},
                                         {'L1': dict(N=1, E=4), 'L2': dict(N=1, E=0)})
        assert (lo, hi) == (0.0, 0.0)


def test_fix8_macro_mean():
    with tempfile.TemporaryDirectory() as d:
        _tsv(d, 'a.truth.tsv', _rows(list('AB'), 'X1'))
        _tsv(d, 'b.truth.tsv', _rows(list('ABCD'), 'Y1'))
        bench = _w(d, 'B.tsv', 'item\ttruth\tsplit\nia\ta.truth.tsv\teval\nib\tb.truth.tsv\teval\n')
        o = _out(d, 'o.tsv', {'X1': ['A', 'Q'], 'Y1': list('ABCD')})
        rc, out = _run([o, '--bench', bench])
        assert 'macro mean over 2 items' in out and '0.250' in out.split('macro mean over 2 items')[1].splitlines()[0], out


def test_fix9_legacy_reproduces_files_on_record():
    # --legacy reproduces the S2 and DV1b score files on record to the digit (the 2RATE suffix is the only addition)
    root = os.path.join(os.path.dirname(__file__), '..', '..')
    cases = [('benchmark-tx/txeng2/s2score/tx_bench_S2.txt', 'benchmark-tx/outputs/vivonne1573-f103r-confirm2',
              ['passZ_S2b', 'passA_S2', 'passB_S2', 'passA', 'passB', 'committed'], 'vivonne1573-f103r-confirm2',
              ['--paired']),
             ('benchmark-tx/txeng2/viv102base/tx_bench_out.txt', 'benchmark-tx/outputs/vivonne1573-f102r-dev',
              ['passZ_dv1', 'passA_dv1', 'passB_dv1'], 'vivonne1573-f102r-dev', ['--paired'])]
    import re
    for rec, od, outs, item, extra in cases:
        rec_p = os.path.join(root, rec)
        if not os.path.exists(rec_p):
            continue
        argv = [os.path.join(root, od, o + '.tsv') for o in outs] + [
            '--bench', os.path.join(root, 'BENCHMARK-TX.tsv'), '--item', item, '--exclude-flagged',
            '--paired', os.path.join(root, od, 'committed.tsv'), '--legacy']
        rc, out = _run(argv)
        got = re.sub(r' \| position errors [^\n]*', '', out)
        assert rc == 0 and got == open(rec_p).read(), (rec, got[:400])


if __name__ == '__main__':
    import inspect
    for n, f in list(globals().items()):
        if n.startswith('test_') and inspect.isfunction(f):
            f()
    print('ok')

#!/usr/bin/env python3
"""Offline test: sign_sorter_apply.py --split-marks and decode_key.py base/mark columns + --merge-mark (MQS-BASE-MARK, 9 Oct 2026).

Must-catch: an attached mark reaches the export beside its base; a compound settled label keeps its mark; one --merge-mark edit
reclassifies a mark text-wide; a merge that collapses two keyed codes is reported. Must-NOT: put a mark on a sign it is not
attached to; change new_sign; change any sign when no merge is given; touch a sign with no ':'; warn on a merge that collapses
nothing keyed. Controls with numbers: tools/tests/mqs_base_mark_control.py (PREREG-MQS-BASE-MARK.md)."""
import csv, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import sign_sorter_apply as ssa
import decode_key as dk

fails = 0


def check(cond, msg):
    global fails
    print(('PASS ' if cond else 'FAIL ') + msg)
    fails += 0 if cond else 1


def w(p, rows):
    with open(p, 'w', newline='') as f:
        csv.writer(f, delimiter='\t').writerows(rows)


def rd(p):
    return list(csv.DictReader(open(p, newline=''), delimiter='\t'))


# unit: split and merge
check(ssa.split_base_mark('T5', ['dot']) == ('T5', 'dot'), 'plain sign + attached mark -> base, mark')
check(ssa.split_base_mark('41:138', []) == ('41', '138'), 'compound settled label keeps its own mark')
check(ssa.split_base_mark('T5', []) == ('T5', ''), 'unmarked sign -> empty mark')
check(ssa.split_base_mark('', ['dot']) == ('', 'dot'), 'unsettled tile keeps its observed mark, no base')
mm = dk.parse_merge('tick=dot,flourish')
check(dk.merge_sign('B3:tick+flourish', mm) == 'B3:dot', 'X=Y renames, X drops')
check(dk.merge_sign('B3', mm) == 'B3', 'must-NOT: sign without ":" untouched')
check(dk.merge_sign('B3:dot', {}) == 'B3:dot', 'must-NOT: no merge, sign unchanged')
check(dk.merge_sign('B3:dot+tick', dk.parse_merge('*')) == 'B3', '* drops every mark')
check(dk.merge_sign('B3:tick+dot', mm) == 'B3:dot', 'renamed mark equal to a present one is not doubled')

with tempfile.TemporaryDirectory() as t:
    # sorter export with --split-marks
    w(os.path.join(t, 'labels.tsv'), [['sid', 'sign'], ['s1', 'T5'], ['s2', 'T5'], ['s3', '41:138'], ['s4', 'T9']])
    w(os.path.join(t, 'marks.tsv'), [['mid', 'page', 'x', 'y', 'w', 'h', 'sid'], ['m1', 'p', '20', '0', '3', '3', 's2'],
                                     ['m2', 'p', '10', '0', '3', '3', 's2'], ['m3', 'p', '40', '0', '3', '3', 's4']])
    w(os.path.join(t, 'clusters.tsv'), [['id', 'kind', 'cluster'], ['s1', 'sign', '1'], ['m1', 'mark', '7'], ['m2', 'mark', '3'], ['m3', 'mark', '7']])
    w(os.path.join(t, 'ml.tsv'), [['cluster', 'mark'], ['7', 'dot']])
    os.makedirs(os.path.join(t, 'db'))
    out = os.path.join(t, 'settled.tsv')
    ssa.main(['--labels', os.path.join(t, 'labels.tsv'), '--db', os.path.join(t, 'db'), '--out', out, '--split-marks',
              os.path.join(t, 'marks.tsv'), '--clusters', os.path.join(t, 'clusters.tsv'), '--mark-labels', os.path.join(t, 'ml.tsv')])
    R = {r['sid']: r for r in rd(out)}
    check(R['s2']['mark'] == 'm3+dot', 'marks ordered left to right; label table beats cluster id: %s' % R['s2']['mark'])
    check(R['s1']['mark'] == '' and R['s1']['base'] == 'T5', 'must-NOT: no mark on a sign it is not attached to')
    check(R['s3']['base'] == '41' and R['s3']['mark'] == '138', 'compound label split in the export')
    check(all(R[s]['new_sign'] == v for s, v in (('s1', 'T5'), ('s3', '41:138'), ('s4', 'T9'))), 'must-NOT: new_sign unchanged')
    ssa.main(['--labels', os.path.join(t, 'labels.tsv'), '--db', os.path.join(t, 'db'), '--out', out])
    check(list(rd(out)[0].keys()) == ['sid', 'old_sign', 'new_sign', 'status', 'mode'], 'without --split-marks the columns are as before')

    # decode_key base/mark columns + --merge-mark
    w(os.path.join(t, 'ct.tsv'), [['line', 'pos', 'base', 'mark', 'conf'], ['L1', '1', 'B1', '', 'H'], ['L1', '2', 'B1', 'tick', 'H'],
                                  ['L1', '3', 'B2', 'flourish', 'H'], ['L1', '4', 'B2', '', 'H']])
    w(os.path.join(t, 'key.tsv'), [['code', 'value'], ['B1', 'a'], ['B1:dot', 'b'], ['B2', 'c']])
    base = [sys.executable, os.path.join(ROOT, 'tools', 'decode_key.py'), t, '--ciphertext', 'ct.tsv', '--key', 'key.tsv',
            '--reading', 'r.txt', '--tokens', 'tok.tsv']
    subprocess.run(base, check=True, capture_output=True)
    v = [r['value'] for r in rd(os.path.join(t, 'tok.tsv'))]
    check(v == ['a', '?', '?', 'c'], 'base/mark columns read as B / B:X, no merge: %s' % v)
    check([r['sign'] for r in rd(os.path.join(t, 'tok.tsv'))] == ['B1', 'B1:tick', 'B2:flourish', 'B2'], 'raw sign column keeps the transcription')
    p = subprocess.run(base + ['--merge-mark', 'tick=dot,flourish'], check=True, capture_output=True, text=True)
    v = [r['value'] for r in rd(os.path.join(t, 'tok.tsv'))]
    check(v == ['a', 'b', 'c', 'c'], 'one edit reclassifies text-wide: %s' % v)
    check('collapses' not in p.stderr, 'must-NOT: no collapse warning when nothing keyed collapses')
    p = subprocess.run(base + ['--merge-mark', 'dot'], check=True, capture_output=True, text=True)
    check('merge-mark collapses B1:dot -> B1' in p.stderr, 'collapse of a keyed distinction reported')

print('base_mark: %s' % ('all passed' if not fails else '%d failures' % fails))
sys.exit(1 if fails else 0)

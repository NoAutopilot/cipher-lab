#!/usr/bin/env python3
"""Offline test of benchmark-tx/txeng4/1/box_token_align.patch (TXE4-1, 12 Oct 2026): applies the patch to a temp copy of
tools/box_token_align.py and runs it on a synthetic two-line page (plus one over-counted line). No network, no model, no truth.
Must catch: (1) a planted 2-token merged box (1:2) never becomes a token; (2) a --keep-pos file drops the read position the
passes disagree on; (3) --count-tol skips a line whose box count is off by more than the tolerance and lists it.
Must NOT block: every other 1:1 box at a kept position is written with the read sign as its code."""
import os, shutil, subprocess, sys, tempfile, csv
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))


def main():
    d = tempfile.mkdtemp()
    shutil.copy(os.path.join(ROOT, 'tools/box_token_align.py'), d)
    shutil.copy(os.path.join(ROOT, 'tools/join_check.py'), d)
    r = subprocess.run(['patch', '-p1', '-d', d, '-i', os.path.join(HERE, 'box_token_align.patch')], capture_output=True, text=True,
                       cwd=d)
    if r.returncode:
        # the patch names tools/box_token_align.py; try stripping the directory
        r = subprocess.run(['patch', '-p0', '-d', d, 'box_token_align.py', '-i', os.path.join(HERE, 'box_token_align.patch')],
                           capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    W = 50
    signs = ['sid\tpage\tline\tx\tw']
    # line 1: 10 boxes, 11 tokens (9% apart, inside the tolerance); box 4 (110 px) covers tokens 4 and 5
    for i, w in enumerate([50, 50, 50, 110, 50, 50, 50, 50, 50, 50], 1):
        signs.append(f'b1_{i}\tpg\t1\t{i * 130}\t{w}')
    # line 2: 6 boxes, 6 tokens, the passes disagree at pos 3 (left out of keep-pos)
    for i in range(1, 7):
        signs.append(f'b2_{i}\tpg\t2\t{i * 130}\t{W}')
    # line 3: 10 boxes, 6 tokens -> count-tol 0.10 skips it
    for i in range(1, 11):
        signs.append(f'b3_{i}\tpg\t3\t{i * 60}\t{W}')
    open(os.path.join(d, 'signs.tsv'), 'w').write('\n'.join(signs) + '\n')
    read = ['line\tpos\tsign']
    for p, s in enumerate('abcdefghijk', 1):
        read.append(f'pg_L01\t{p}\t{s}')
    for p, s in enumerate('hijklm', 1):
        read.append(f'pg_L02\t{p}\t{s}')
    for p, s in enumerate('nopqrs', 1):
        read.append(f'pg_L03\t{p}\t{s}')
    open(os.path.join(d, 'read.tsv'), 'w').write('\n'.join(read) + '\n')
    keep = ['line\tpos'] + [f'pg_L01\t{p}' for p in range(1, 12)] + [f'pg_L02\t{p}' for p in (1, 2, 4, 5, 6)] + [f'pg_L03\t{p}' for p in range(1, 7)]
    open(os.path.join(d, 'keep.tsv'), 'w').write('\n'.join(keep) + '\n')
    out = subprocess.run([sys.executable, os.path.join(d, 'box_token_align.py'), '--signs', os.path.join(d, 'signs.tsv'), '--read',
                          os.path.join(d, 'read.tsv'), '--lam', '0', '--keep-pos', os.path.join(d, 'keep.tsv'), '--count-tol', '0.10',
                          '--tokens-out', os.path.join(d, 'tokens.tsv'), '--out', os.path.join(d, 'map.tsv')],
                         capture_output=True, text=True)
    assert out.returncode == 0, out.stdout + out.stderr
    assert 'skipped 1 line(s): pg_L03 (boxes 10, tokens 6)' in out.stdout, out.stdout
    toks = list(csv.DictReader(open(os.path.join(d, 'tokens.tsv')), delimiter='\t'))
    got = {(t['sid'], t['line'], t['pos'], t['code']) for t in toks}
    assert not any(t['sid'] == 'b1_4' for t in toks), 'the merged box became a token'
    assert not any(t['line'] == 'pg_L03' for t in toks), 'a count-tol-skipped line gave tokens'
    assert ('b2_3', 'pg_L02', '3', 'j') not in got, 'the disagreement position gave a token'
    for sid, line, pos, code in [('b1_1', 'pg_L01', '1', 'a'), ('b1_2', 'pg_L01', '2', 'b'), ('b1_3', 'pg_L01', '3', 'c'),
                                 ('b1_5', 'pg_L01', '6', 'f'), ('b1_6', 'pg_L01', '7', 'g'), ('b1_7', 'pg_L01', '8', 'h'),
                                 ('b1_8', 'pg_L01', '9', 'i'), ('b1_9', 'pg_L01', '10', 'j'), ('b1_10', 'pg_L01', '11', 'k'),
                                 ('b2_1', 'pg_L02', '1', 'h'), ('b2_2', 'pg_L02', '2', 'i'), ('b2_4', 'pg_L02', '4', 'k'),
                                 ('b2_5', 'pg_L02', '5', 'l'), ('b2_6', 'pg_L02', '6', 'm')]:
        assert (sid, line, pos, code) in got, (sid, line, pos, code, sorted(got))
    assert len(toks) == 14, len(toks)
    maprows = list(csv.DictReader(open(os.path.join(d, 'map.tsv')), delimiter='\t'))
    assert not any(r['line'] == 'pg_L03' for r in maprows), 'the skipped line stayed in the map'
    print('ok: patch applies; 14 tokens; merged box, disagreement position and over-counted line all excluded')
    shutil.rmtree(d)


if __name__ == '__main__':
    main()

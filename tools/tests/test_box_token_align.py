#!/usr/bin/env python3
"""Offline test for tools/box_token_align.py (BOXMAP-LA, 11 Oct 2026). No network, no model, no truth file.

1. lam 0, no labels, no statuses: the DP is atlas/no87_map.py's label-blind dp() step for step (a verbatim copy is kept
   below as the reference) on the L06-shaped line and on 200 seeded random lines.
2. The f178v L06 case, synthetic with a known answer by construction: the real L06 box widths (30 boxes, page median 66),
   30 tokens; box 9 is an extra mark (31 px) that is not a letter, box 17 (152 px) holds tokens 16 and 17. The label-blind
   DP maps box 9 1:1 to token 9 and shifts boxes 10-16 one token late (the TXE3-9 second-check defect). With box 9 marked
   not-letter and labels on every box (three of them wrong, and box 9's own label the adversarial one, token 9's sign),
   every box lands on its constructed token, box 9 is skipped, box 17 is 1:2 over tokens 16-17, and nothing is `unsure`.
   Labels alone (no status) also remove the shift (the mark then joins box 10 as one sign, 2:1).
3. One wrong label on a clean line does not move its box (lam below a local shift-and-return).
4. bad-cut comes out with op bad-cut, never 1:1; aside likewise.
5. The CLI end to end on temp files: map rows, 2:1 written one row per box, the not-letter box absent from the map and
   listed in the lines file, the truth-free check printed.
6. If the repository's Birago inputs are present: lam 0 reproduces atlas/no87_box_token.tsv's 1:1 positions on all 26
   lines, and the committed no87_box_token_labelaware.tsv is current (no87_map.py --label-aware --check), with
   f178v_06_009 skipped and f178v_06_010..015 one token earlier than in the old map.
"""
import contextlib, io, json, math, os, random, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import box_token_align as BA  # noqa: E402

L06_W = [66, 40, 77, 66, 70, 43, 61, 97, 31, 41, 71, 74, 66, 78, 64, 109, 152, 40, 63, 63, 71, 57, 64, 55, 58, 39, 75, 96, 47, 33]
W = 66


def old_dp(bw, n, W):
    """Verbatim copy of ciphers/nevers-birago-fr3251-1572/atlas/no87_map.py dp() (3 Oct 2026), the reference."""
    m = len(bw); INF = 1e9
    C = [[INF] * (n + 1) for _ in range(m + 1)]; B = [[None] * (n + 1) for _ in range(m + 1)]; C[0][0] = 0
    for i in range(m + 1):
        for j in range(n + 1):
            c = C[i][j]
            if c >= INF: continue
            opts = []
            if i < m and j < n: opts.append((i + 1, j + 1, abs(math.log(bw[i] / W)), '1:1'))
            if i + 1 < m and j < n: opts.append((i + 2, j + 1, 1.0 + abs(math.log((bw[i] + bw[i + 1]) / W)), '2:1'))
            if i < m and j + 1 < n: opts.append((i + 1, j + 2, 1.0 + abs(math.log(bw[i] / (2 * W))), '1:2'))
            if i < m: opts.append((i + 1, j, 1.2 if bw[i] < 0.5 * W else 2.5, 'skipbox'))
            if j < n: opts.append((i, j + 1, 2.5, 'skiptok'))
            for a, b, k, op in opts:
                if c + k < C[a][b]: C[a][b] = c + k; B[a][b] = (i, j, op)
    path, i, j = [], m, n
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]; path.append((pi, pj, op)); i, j = pi, pj
    return path[::-1]


# the constructed answer: box index (0-based) -> token indices it covers; box 8 (the 9th, 31 px) is not a letter
TRUE = {}
for b in range(8):
    TRUE[b] = [b]
for b in range(9, 16):
    TRUE[b] = [b - 1]
TRUE[16] = [15, 16]
for b in range(17, 30):
    TRUE[b] = [b]
ALPHA = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'J', 'K', 'M', 'N']
TOKS = [ALPHA[(7 * j + j // 3) % len(ALPHA)] for j in range(30)]


def synth_labels(wrong=(3, 12, 21)):
    labs = []
    for b in range(30):
        if b == 8:
            labs.append({TOKS[8]: 1.0})                      # the mark's label is token 9's sign (the real L06 case)
        elif b in wrong:
            labs.append({'Z': 1.0})
        else:
            labs.append({TOKS[TRUE[b][0]]: 1.0})
    return labs


def placed(path):
    out = {}
    for i, j, op in path:
        if op == '1:1':
            out[i] = [j]
        elif op == '1:2':
            out[i] = [j, j + 1]
    return out


def test_lam0_is_the_old_dp():
    toks = [{t} for t in TOKS]
    assert BA.dp(L06_W, toks, W) == old_dp(L06_W, 30, W)
    rng = random.Random(87)
    for _ in range(200):
        m = rng.randint(1, 18); n = rng.randint(1, 18)
        bw = [rng.randint(8, 180) for _ in range(m)]
        assert BA.dp(bw, [{'x'}] * n, 66) == old_dp(bw, n, 66), (bw, n)


def test_l06_shift_reproduced_by_label_blind_dp():
    p = placed(old_dp(L06_W, 30, W))
    assert p[8] == [8]                                       # the not-letter mark takes token 9
    late = [b for b in range(9, 16) if p.get(b) == [TRUE[b][0] + 1]]
    assert len(late) == 7, late                              # boxes 10-16 all one token late


def test_l06_label_aware_with_status():
    skip = [b == 8 for b in range(30)]
    path = BA.dp(L06_W, [{t} for t in TOKS], W, synth_labels(), skip, lam=BA.LAM)
    p = placed(path)
    assert 8 not in p and 8 in [i for i, j, op in path if op == 'skipbox']
    for b, ts in TRUE.items():
        assert p.get(b) == ts, (b, p.get(b), ts)
    boxes = [dict(sid=f'b{b + 1:02d}', w=w, labels=synth_labels()[b], status='NOT-LETTER' if b == 8 else '')
             for b, w in enumerate(L06_W)]
    rows, skipped = BA.align_line(boxes, [dict(pos=str(j + 1), signs={t}) for j, t in enumerate(TOKS)], W)
    assert skipped == ['b09']
    assert not [r for r in rows if r['op'] == 'unsure']
    one = {r['sid']: int(r['pos']) for r in rows if r['op'] == '1:1'}
    assert one['b10'] == 9 and one['b16'] == 15 and one['b18'] == 18
    assert sorted(int(r['pos']) for r in rows if r['sid'] == 'b17') == [16, 17]


def test_l06_labels_alone_remove_the_shift():
    # without the owner's status the mark may join its neighbour as one sign (2:1), but it never takes a token of its
    # own and no later box is late
    path = BA.dp(L06_W, [{t} for t in TOKS], W, synth_labels(), None, lam=BA.LAM)
    p = placed(path)
    assert 8 not in p and (8, 8, '2:1') in path
    for b, ts in TRUE.items():
        if b != 9:
            assert p.get(b) == ts, (b, p.get(b), ts)


def test_one_wrong_label_does_not_move_its_box():
    bw = [60, 70, 66, 64, 72, 58, 66, 69, 61, 67]
    toks = [{c} for c in 'ABCDEFGHJK']
    for bad in range(10):
        labs = [{c: 1.0} for c in 'ABCDEFGHJK']
        labs[bad] = {'ABCDEFGHJK'[(bad + 1) % 10]: 1.0}      # labelled as its right-hand neighbour's sign
        assert placed(BA.dp(bw, toks, 66, labs, None, lam=BA.LAM)) == {i: [i] for i in range(10)}, bad
        boxes = [dict(sid=str(i), w=w, labels=labs[i]) for i, w in enumerate(bw)]
        rows, _ = BA.align_line(boxes, [dict(pos=str(j + 1), signs=t) for j, t in enumerate(toks)], 66)
        assert [r['op'] for r in rows] == ['1:1'] * 10


def test_badcut_and_aside_never_1to1():
    bw = [60, 70, 66, 64]
    toks = [dict(pos=str(j + 1), signs={c}) for j, c in enumerate('ABCD')]
    boxes = [dict(sid=str(i), w=w, labels={'ABCD'[i]: 1.0}, status=st) for i, (w, st) in
             enumerate(zip(bw, ['', 'bad-cut', 'aside', 'kept']))]
    rows, skipped = BA.align_line(boxes, toks, 66)
    assert [r['op'] for r in rows] == ['1:1', 'bad-cut', 'aside', '1:1'] and not skipped


def wtsv(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows))


def test_cli_end_to_end():
    with tempfile.TemporaryDirectory() as d:
        x = 100; signs = []
        for b, w in enumerate(L06_W):
            signs.append((f'pg_01_{b + 1:03d}', 'pg', 1, b + 1, x, 0, w)); x += w + 10
        # a second line on the same page whose last two boxes are halves of one sign (a 2:1 by width)
        for b, w in enumerate([66, 64, 33, 33]):
            signs.append((f'pg_02_{b + 1:03d}', 'pg', 2, b + 1, 100 + 80 * b, 200, w))
        wtsv(os.path.join(d, 'signs.tsv'), ['sid', 'page', 'line', 'pos', 'x', 'y', 'w'], signs)
        read = [('pg_L01', j + 1, t) for j, t in enumerate(TOKS)] + [('pg_L02', j + 1, t) for j, t in enumerate('ABC')]
        wtsv(os.path.join(d, 'read.tsv'), ['line', 'pos', 'sign'], read)
        labs = synth_labels()
        wtsv(os.path.join(d, 'labels.tsv'), ['sid', 'label'], [(f'pg_01_{b + 1:03d}', list(labs[b])[0]) for b in range(30)])
        wtsv(os.path.join(d, 'status.tsv'), ['sid', 'status'], [('pg_01_009', 'not-letter')])
        wtsv(os.path.join(d, 'old.tsv'), ['sid', 'line', 'pos', 'op'],
             [(f'pg_01_{b + 1:03d}', 'pg_L01', b + 1, '1:1') for b in range(30)])
        out, lo = os.path.join(d, 'map.tsv'), os.path.join(d, 'lines.tsv')
        buf = io.StringIO()
        with contextlib.redirect_stdout(buf):
            BA.main(['--signs', os.path.join(d, 'signs.tsv'), '--read', os.path.join(d, 'read.tsv'),
                     '--tile-labels', os.path.join(d, 'labels.tsv'), '--status', os.path.join(d, 'status.tsv'),
                     '--old', os.path.join(d, 'old.tsv'), '--check-labels', os.path.join(d, 'labels.tsv'),
                     '--out', out, '--lines-out', lo])
        rows = BA.rd(out)
        assert list(rows[0]) == BA.COLS
        assert 'pg_01_009' not in {r['sid'] for r in rows}
        two = [r for r in rows if r['op'] == '2:1']
        assert [(r['sid'], r['pos']) for r in two] == [('pg_02_003', '3'), ('pg_02_004', '3')]
        lines = {r['line']: r for r in BA.rd(lo)}
        assert lines['pg_L01']['skipped'] == 'pg_01_009' and int(lines['pg_L01']['moved']) == 7
        assert 'check, new map' in buf.getvalue() and 'check, old map' in buf.getvalue()


def test_check_bound_cli_exit_codes():
    """--check-bound (TXE4-0 unit 1, 12 Oct 2026): writes the join_check sidecar and exits 0/2/3."""
    with tempfile.TemporaryDirectory() as d:
        x = 100; signs = []
        for b, w in enumerate(L06_W):
            signs.append((f'pg_01_{b + 1:03d}', 'pg', 1, b + 1, x, 0, w)); x += w + 10
        wtsv(os.path.join(d, 'signs.tsv'), ['sid', 'page', 'line', 'pos', 'x', 'y', 'w'], signs)
        read = [('pg_L01', j + 1, t) for j, t in enumerate(TOKS)]
        wtsv(os.path.join(d, 'read.tsv'), ['line', 'pos', 'sign'], read)
        labs = synth_labels()
        wtsv(os.path.join(d, 'labels.tsv'), ['sid', 'label'], [(f'pg_01_{b + 1:03d}', list(labs[b])[0]) for b in range(30)])
        wtsv(os.path.join(d, 'status.tsv'), ['sid', 'status'], [('pg_01_009', 'not-letter')])
        out = os.path.join(d, 'map.tsv')
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'box_token_align.py'),
                             '--signs', os.path.join(d, 'signs.tsv'), '--read', os.path.join(d, 'read.tsv'),
                             '--tile-labels', os.path.join(d, 'labels.tsv'), '--status', os.path.join(d, 'status.tsv'),
                             '--check-labels', os.path.join(d, 'labels.tsv'), '--check-bound', '--out', out],
                            capture_output=True, text=True)
        assert os.path.exists(out + '.joincheck.json'), r.stdout + r.stderr
        with open(out + '.joincheck.json') as f:
            sc = json.load(f)
        assert sc['verdict'] == 'PASS' and r.returncode == 0, (sc, r.stdout, r.stderr)
        # a map with no --check-labels + --check-bound is a usage error, not a silent no-op
        r2 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'box_token_align.py'),
                             '--signs', os.path.join(d, 'signs.tsv'), '--read', os.path.join(d, 'read.tsv'),
                             '--check-bound', '--out', os.path.join(d, 'map2.tsv')], capture_output=True, text=True)
        assert r2.returncode != 0 and 'check-bound requires' in (r2.stderr or ''), r2.stderr


def test_repository_birago_no87():
    F = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572')
    need = [os.path.join(F, 'atlas/signs.tsv'), os.path.join(F, 'atlas/no87_box_token.tsv'),
            os.path.join(F, 'atlas/no87_box_token_labelaware.tsv'), os.path.join(F, 'sorter/no87/seed.tsv'),
            os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv'),
            os.path.join(ROOT, 'benchmark-tx/txeng/compare/topk_no87_allheld.tsv')]
    if not all(os.path.exists(p) for p in need):
        print('  (repository Birago inputs absent: skipped)')
        return
    signs = BA.rd(need[0])
    lines = [f'f178v_L{i:02d}' for i in range(1, 24)] + [f'f179r_L{i:02d}' for i in range(1, 4)]
    L = [r for r in BA.rd(need[4]) if r['line'] in lines]
    rows, _ = BA.build_map(signs, L, lines=lines, lam=0.0, loo=False)
    old = BA.read_old(need[1])
    assert {r['sid']: (r['line'], str(r['pos'])) for r in rows if r['op'] == '1:1'} == old
    r = subprocess.run([sys.executable, os.path.join(F, 'atlas/no87_map.py'), '--label-aware', '--check'],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    new = {x['sid']: x for x in BA.rd(need[2])}
    assert 'f178v_06_009' not in new
    for k in range(10, 16):
        sid = f'f178v_06_{k:03d}'
        assert new[sid]['op'] == '1:1' and int(new[sid]['pos']) == int(old[sid][1]) - 1, (sid, new[sid], old[sid])
    assert 'truth' not in BA.rd(need[2])[0]


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            fn(); print('ok', name)
    print('test_box_token_align: all passed')

#!/usr/bin/env python3
"""Offline test for tools/join_check.py (TXE4-0 REPAIR unit 1, 12 Oct 2026). No network, no model, no truth file.

Cases (named again in join_check.py's own docstring, CLAUDE.md 8a):
  MC1 a single line shifted after an early stray mark -> FAIL on B1 for that line (the f178v L06 shape: a few
      correct boxes, then every later box reads one token late, with no resync -- the real L06 also recovers via
      a 1:2 merge partway through, which keeps its correct share above its shifted share and passes B1; this
      synthetic line is built so the shifted boxes outnumber the correct ones, which is what fails B1).
  MC2 every line on a page carries the same shape (not just one) -> FAIL, B1 fails on every line.
  MC3 (repo files present) the committed old atlas/no87_box_token.tsv, checked with sorter/no87/seed.tsv's atlas
      labels -> FAIL.
  MC4 check labels permuted within each page -> UNCHECKABLE, never PASS.
  MC5 require() refuses a map with no sidecar, and a map edited after its sidecar was written.
  NB1 (repo files present) the committed atlas/no87_box_token_labelaware.tsv with the same labels -> PASS.
  NB2 a correct synthetic map with genuine 2:1 and 1:2 steps -> PASS.
  NB3 a correct map with fewer than 5 check tiles on some lines -> PASS, those lines 'unchecked'.
  NB4 a correct map with 30%-accurate check labels -> PASS.
  NB5 a correct map over a repeated sign (the same sign at pos and pos+1) -> PASS.
"""
import json
import os
import random
import string
import subprocess
import sys
import tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import join_check as JC  # noqa: E402
import box_token_align as BA  # noqa: E402

SYMS = list(string.ascii_uppercase) + ['0', '1']  # 28 distinct symbols, enough to avoid chance collisions


def shifted_line(line, n_correct, n_shift, syms):
    """A line shaped like the f178v L06 defect: n_correct boxes at positions 1..n_correct match their own read
    sign; n_shift boxes placed one position late each carry the sign that really belongs one position earlier
    (so they match at offset -1, never 0). Returns (pos_of, labels, read_sign) covering just this line."""
    n = n_correct + n_shift
    assert len(syms) >= n + 1
    sign_at = {p: syms[p - 1] for p in range(1, n + 2)}        # positions 1..n+1 get distinct signs
    pos_of, labels = {}, {}
    for p in range(1, n_correct + 1):
        sid = f'{line}_c{p:02d}'
        pos_of[sid] = (line, str(p))
        labels[sid] = sign_at[p]
    for k, p in enumerate(range(n_correct + 2, n + 2)):        # skip one position (the stray mark, unlabelled)
        sid = f'{line}_s{k:02d}'
        pos_of[sid] = (line, str(p))
        labels[sid] = sign_at[p - 1]                           # true content is one position earlier
    read_sign = {(line, p): {s} for p, s in sign_at.items()}
    return pos_of, labels, read_sign


def merge(*triples):
    pos_of, labels, read_sign = {}, {}, {}
    for p, l, r in triples:
        pos_of.update(p); labels.update(l); read_sign.update(r)
    return pos_of, labels, read_sign


def test_mc1_single_line_fails_b1():
    pos_of, labels, read_sign = shifted_line('PG1_L01', n_correct=4, n_shift=10, syms=SYMS)
    r = JC.evaluate(pos_of, labels, read_sign)
    assert r['lines']['PG1_L01']['verdict'] == 'fail'
    assert r['b1'] is False
    assert r['b3'] is True, r            # the labels plainly correlate with the text (just one off), not noise
    assert r['verdict'] == 'FAIL', r


def test_mc2_whole_page_fails_every_line():
    a = shifted_line('PG2_L01', 4, 10, SYMS)
    b = shifted_line('PG2_L02', 4, 10, [s + '2' for s in SYMS])
    c = shifted_line('PG2_L03', 4, 10, [s + '3' for s in SYMS])
    pos_of, labels, read_sign = merge(a, b, c)
    r = JC.evaluate(pos_of, labels, read_sign)
    assert all(d['verdict'] == 'fail' for d in r['lines'].values()), r['lines']
    assert r['b1'] is False
    assert r['verdict'] == 'FAIL', r


def test_mc4_permuted_check_labels_is_uncheckable():
    pos_of, labels, read_sign = shifted_line('PG4_L01', n_correct=10, n_shift=0, syms=SYMS)
    rng = random.Random(1)
    sids = list(labels); vals = [labels[s] for s in sids]; rng.shuffle(vals)
    permuted = dict(zip(sids, vals))
    r = JC.evaluate(pos_of, permuted, read_sign)
    assert r['verdict'] == 'UNCHECKABLE', r
    assert r['b3'] is False


def test_mc5_require_refuses_missing_and_stale_sidecar():
    with tempfile.TemporaryDirectory() as d:
        mp = os.path.join(d, 'map.tsv')
        with open(mp, 'w') as f:
            f.write('sid\tline\tpos\top\n s1\tL\t1\t1:1\n')
        r = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'join_check.py'), '--map', mp, '--require'],
                            capture_output=True, text=True)
        assert r.returncode == 2 and 'no .joincheck.json sidecar' in r.stderr, r.stderr
        JC.write_sidecar(mp, dict(verdict='PASS', n=1, overall={}, share0=1.0, sharepm1=0.0, b1=True, b2=True,
                                   b3=True, p95_0=0.0, p95_pm1=0.0, b2_bound=0.05, lines={}, draws=1, seed=1))
        r2 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'join_check.py'), '--map', mp, '--require'],
                             capture_output=True, text=True)
        assert r2.returncode == 0, r2.stderr
        with open(mp, 'a') as f:
            f.write('s2\tL\t2\t1:1\n')
        r3 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'join_check.py'), '--map', mp, '--require'],
                             capture_output=True, text=True)
        assert r3.returncode == 2 and 'sha256 mismatch' in r3.stderr, r3.stderr
        r4 = subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'join_check.py'), '--map', mp, '--require',
                              '--allow-unchecked-join', 'reproducing an old result'], capture_output=True, text=True)
        assert r4.returncode == 0 and 'UNCHECKED JOIN: reproducing an old result' in r4.stdout, r4.stdout


def test_nb2_2to1_and_1to2_never_enter_pos_of():
    bw = [60, 70, 66, 33, 33, 72, 64]
    letters = list('ABCDDEF')                                # 7 boxes, 6 tokens: boxes 3,4 (33,33) merge 2:1 -> D
    toks = [{c} for c in 'ABCDEF']
    boxes = [dict(sid=f'b{i}', w=w, labels={c: 1.0}, status='') for i, (w, c) in enumerate(zip(bw, letters))]
    rows, _ = BA.align_line(boxes, [dict(pos=str(j + 1), signs=t) for j, t in enumerate(toks)], 66)
    for r in rows:
        r.update(line='PG_L01', page='PG')
    pos_of = BA.positions(rows)
    assert 'b3' not in pos_of and 'b4' not in pos_of        # the 2:1 pair never enters pos_of
    labels = {f'b{i}': c for i, c in enumerate(letters)}
    read_sign = {('PG_L01', j + 1): t for j, t in enumerate(toks)}
    # pad with enough clean extra lines so B1/B3 have something to measure against
    pad = shifted_line('PG_L02', n_correct=10, n_shift=0, syms=SYMS)
    pos_of2, labels2, read_sign2 = merge((pos_of, labels, read_sign), pad)
    r = JC.evaluate(pos_of2, labels2, read_sign2)
    assert r['verdict'] == 'PASS', r


def test_nb3_short_lines_are_unchecked_not_failed():
    short = shifted_line('PG3_L01', n_correct=3, n_shift=0, syms=SYMS)
    long = shifted_line('PG3_L02', n_correct=12, n_shift=0, syms=[s + 'x' for s in SYMS])
    pos_of, labels, read_sign = merge(short, long)
    r = JC.evaluate(pos_of, labels, read_sign)
    assert r['lines']['PG3_L01']['verdict'] == 'unchecked'
    assert r['lines']['PG3_L02']['verdict'] == 'pass'
    assert r['verdict'] == 'PASS', r


def test_nb4_weak_labels_do_not_fail_a_right_map():
    pos_of, labels, read_sign = shifted_line('PG5_L01', n_correct=20, n_shift=0, syms=SYMS)
    rng = random.Random(2)
    other = [s for s in SYMS if s not in labels.values()] or SYMS
    weak = {}
    for i, sid in enumerate(sorted(labels)):
        weak[sid] = labels[sid] if i % 10 < 3 else rng.choice(other)   # about 30% accurate, 70% wrong-but-random
    r = JC.evaluate(pos_of, weak, read_sign)
    assert r['verdict'] == 'PASS', r


def test_nb5_repeated_sign_offset0_counted_first():
    line = 'PG6_L01'
    read_sign = {(line, 1): {'A'}, (line, 2): {'A'}, (line, 3): {'B'}, (line, 4): {'C'}, (line, 5): {'D'},
                 (line, 6): {'E'}}
    pos_of = {f's{p}': (line, str(p)) for p in range(1, 7)}
    labels = {f's{p}': read_sign[(line, p)].copy().pop() for p in range(1, 7)}
    per = JC.offsets_per_line(pos_of, labels, read_sign)
    assert per[line]['0'] == 6 and per[line].get('-1', 0) == 0 and per[line].get('+1', 0) == 0


def test_repository_no87_old_and_labelaware_maps():
    F = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572')
    need = [os.path.join(F, 'atlas/no87_box_token.tsv'), os.path.join(F, 'atlas/no87_box_token_labelaware.tsv'),
            os.path.join(F, 'sorter/no87/seed.tsv'), os.path.join(F, 'harvest/ciphertext_f178v.tsv'),
            os.path.join(F, 'harvest/ciphertext_f179r.tsv')]
    if not all(os.path.exists(p) for p in need):
        print('  (repository Birago no.87 inputs absent: skipped)')
        return
    seed = {r['sid']: r['atlas'] for r in BA.rd(need[2]) if r.get('atlas') and r['atlas'] != '_'}
    read_rows = BA.rd(need[3]) + BA.rd(need[4])
    read_sign = JC.read_sign_table(read_rows)

    old_rows = BA.rd(need[0])                   # already carries a full "line" column (f178v_L06 style)
    pos_old = BA.positions(old_rows)
    r_old = JC.evaluate(pos_old, seed, read_sign)
    assert r_old['verdict'] == 'FAIL', r_old
    assert r_old['lines']['f178v_L06']['verdict'] == 'pass'     # mid-line shift only: passes B1
    for ln in ('f178v_L09', 'f178v_L11', 'f178v_L13', 'f178v_L17', 'f178v_L21', 'f179r_L02', 'f179r_L03'):
        assert r_old['lines'][ln]['verdict'] == 'fail', (ln, r_old['lines'][ln])

    la_rows = BA.rd(need[1])
    pos_la = BA.positions(la_rows)
    r_la = JC.evaluate(pos_la, seed, read_sign)
    print(f"  repository check: old map {r_old['verdict']} (share0 {r_old['share0']:.3f}); "
          f"label-aware map {r_la['verdict']} (share0 {r_la['share0']:.3f})")
    assert r_la['verdict'] == 'PASS', r_la


if __name__ == '__main__':
    for name, fn in sorted(globals().items()):
        if name.startswith('test_') and callable(fn):
            fn(); print('ok', name)
    print('test_join_check: all passed')

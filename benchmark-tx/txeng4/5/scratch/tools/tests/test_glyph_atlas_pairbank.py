#!/usr/bin/env python3
"""Offline test of tools/glyph_atlas.py classify --pair's TXE4-5 options (12 Oct 2026, PREREG benchmark-tx/PREREG-txeng4-5.md):
--pool-agreed AGREE:MAP (machine-agreed tiles joined by a join_check-PASSed map), --feature-bank (topology + zoning + HOG with L1
selection inside every LOGO fold), --pairs FILE (one gated model per pair, combined output with the conflict rule),
--reverse-labels (must break), --exclude-own-line (own-ink pools never vote on their own line), and the map gate: a --map or a
--pool-agreed map with no PASS sidecar is refused (exit 2). Synthetic tiles only; no repository file, no network, no model."""
import csv, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')
sys.path.insert(0, os.path.join(HERE, '..'))
import join_check as JC


def tile(kind, rng):
    im = Image.new('L', (48, 48), 0); d = ImageDraw.Draw(im)
    cx = 24 + int(rng.integers(-3, 4)); r = 7 + int(rng.integers(-1, 2)); t = int(rng.integers(2, 5))
    if kind == 'A':
        cy = 11 + int(rng.integers(-2, 3)); d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=255, width=t)
        d.line((cx + r - 1, cy, cx + r - 1, 45), fill=255, width=t)
    elif kind == 'B':
        cy = 24 + int(rng.integers(-2, 3)); d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=255, width=t)
        d.line((cx, 3, cx, 45), fill=255, width=t)
    else:  # 'C': a bar, the member of a second pair with 'A'
        d.line((6, 24 + int(rng.integers(-2, 3)), 42, 24), fill=255, width=t + 1)
    return np.asarray(im, np.uint8)


def pass_sidecar(p):
    JC.write_sidecar(p, dict(verdict='PASS', n=0, overall={}, share0=1.0, sharepm1=0.0, b1=True, b2=True, b3=True,
                             p95_0=0.0, p95_pm1=0.0, b2_bound=0.05, lines={}, draws=0, seed=0))


def w(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n' + ''.join('\t'.join(str(x) for x in r) + '\n' for r in rows))


def build(d):
    rng = np.random.default_rng(11)
    sids, bms, rows, agree, amap = [], [], [], [], []
    n = 0
    kinds = {'A': 'TA', 'B': 'TB', 'C': 'TC'}
    for pg in ('p1', 'p2', 'p3'):
        for k in range(24):
            kind = 'ABC'[k % 3]; sid = f'{pg}_01_{n:03d}'; n += 1
            sids.append(sid); bms.append(tile(kind, rng))
            rh = {'A': 1.3, 'B': 1.8, 'C': 0.6}[kind] + rng.normal(0, 0.1); dy = {'A': 0.3, 'B': 0.0, 'C': 0.1}[kind] + rng.normal(0, 0.1)
            rows.append([sid, pg, '1', str(k), '0', '0', '30', '40', f'{rh:.3f}', '0.7', f'{dy:.3f}', ''])
            line, pos = f'{pg}_L01', str(k + 1)
            agree.append([line, pos, kinds[kind]]); amap.append([sid, pg, line, pos, '1:1'])
    # applied page p4: 18 boxed tiles, planted swaps at k 0 (A read as B), 4 (B read as A), 6 (A read as C)
    p4, lab, mp = [], [], []
    for k in range(18):
        kind = 'ABC'[k % 3]; sid = f'p4_01_{n:03d}'; n += 1
        sids.append(sid); bms.append(tile(kind, rng))
        rh = {'A': 1.3, 'B': 1.8, 'C': 0.6}[kind] + rng.normal(0, 0.1); dy = {'A': 0.3, 'B': 0.0, 'C': 0.1}[kind] + rng.normal(0, 0.1)
        rows.append([sid, 'p4', '1', str(k), '0', '0', '30', '40', f'{rh:.3f}', '0.7', f'{dy:.3f}', ''])
        L = kinds[kind]
        if k == 0: L = 'TB'   # an A read as B
        if k == 4: L = 'TA'   # a B read as A
        if k == 6: L = 'TC'   # an A read as C (the second pair)
        lab.append(['p4_L01', str(k + 1), L]); mp.append([sid, 'p4', 'p4_L01', str(k + 1), '1:1'])
    w(os.path.join(d, 'signs.tsv'), 'sid page line pos x y w h rh rw dy marks'.split(), rows)
    np.savez(os.path.join(d, 'bitmaps.npz'), signs=np.stack(bms), marks=np.zeros((1, 48, 48), np.uint8))
    w(os.path.join(d, 'agree.tsv'), ['line', 'pos', 'sign'], agree)
    w(os.path.join(d, 'agree_map.tsv'), ['sid', 'page', 'line', 'pos', 'op'], amap)
    w(os.path.join(d, 'unit.tsv'), ['line', 'pos', 'sign'], lab)
    w(os.path.join(d, 'map.tsv'), ['sid', 'page', 'line', 'pos', 'op'], mp)
    with open(os.path.join(d, 'pairs.txt'), 'w') as f:
        f.write('TA TB\nTA TC\n')


def run(d, *extra, pair=('TA', 'TB'), pairs=False):
    cmd = [sys.executable, TOOL, 'classify', '--out', d, '--map', os.path.join(d, 'map.tsv'),
           '--pool-agreed', os.path.join(d, 'agree.tsv') + ':' + os.path.join(d, 'agree_map.tsv'),
           '--apply-unit', os.path.join(d, 'unit.tsv'), '--tsv', os.path.join(d, 'out.tsv'),
           '--report', os.path.join(d, 'rep.tsv'), '--touched', os.path.join(d, 'touched.tsv')]
    cmd += ['--pairs', os.path.join(d, 'pairs.txt')] if pairs else ['--pair', *pair]
    return subprocess.run(cmd + list(extra), capture_output=True, text=True)


def rd(p):
    return list(csv.DictReader(open(p), delimiter='\t'))


def main():
    d = tempfile.mkdtemp(); build(d)
    # 1. gate: no sidecar -> refused
    r = run(d)
    assert r.returncode == 2 and 'join_check: refuse' in r.stderr, (r.returncode, r.stderr[-300:])
    pass_sidecar(os.path.join(d, 'agree_map.tsv'))
    r = run(d)
    assert r.returncode == 2, 'the --map still has no sidecar'
    pass_sidecar(os.path.join(d, 'map.tsv'))
    # 2. machine-agreed pool, topology features: fixes the two planted A/B swaps, breaks nothing
    r = run(d); assert r.returncode == 0, r.stderr
    rep = rd(os.path.join(d, 'rep.tsv'))[0]
    assert rep['pool_a'] == '24' and rep['pool_b'] == '24' and rep['groups'] == '3', rep
    out = {(x['line'], x['pos']): x['sign'] for x in rd(os.path.join(d, 'out.tsv'))}
    assert out[('p4_L01', '1')] == 'TA' and out[('p4_L01', '5')] == 'TB', out
    assert sum(1 for x in rd(os.path.join(d, 'touched.tsv')) if x['out'] != x['L']) == 2
    # 3. feature bank with L1 selection: still fixes both, reports kept features
    r = run(d, '--feature-bank'); assert r.returncode == 0, r.stderr
    rep = rd(os.path.join(d, 'rep.tsv'))[0]
    assert rep['kept'] and 4 <= int(rep['kept']) <= 173, rep
    out = {(x['line'], x['pos']): x['sign'] for x in rd(os.path.join(d, 'out.tsv'))}
    assert out[('p4_L01', '1')] == 'TA' and out[('p4_L01', '5')] == 'TB', out
    # 4. reversed labels must break: every considered A/B tile flips the wrong way (forced t so the control can act)
    r = run(d, '--reverse-labels', '--force-t', '0'); assert r.returncode == 0, r.stderr
    t = rd(os.path.join(d, 'touched.tsv'))
    broken = sum(1 for x in t if x['L'] in ('TA', 'TB') and x['out'] != x['L'] and x['pos'] not in ('1', '5'))
    assert broken >= 8, broken
    # 5. --pairs: both pairs applied, the A/C swap fixed too, no conflict on this fixture, per-pair files written
    r = run(d, pairs=True); assert r.returncode == 0, r.stderr
    assert os.path.exists(os.path.join(d, 'out_TA_TB.tsv')) and os.path.exists(os.path.join(d, 'rep_TA_TC.tsv'))
    out = {(x['line'], x['pos']): x['sign'] for x in rd(os.path.join(d, 'out.tsv'))}
    assert out[('p4_L01', '1')] == 'TA' and out[('p4_L01', '5')] == 'TB' and out[('p4_L01', '7')] == 'TA', out
    assert 'conflicts kept as base 0' in r.stdout, r.stdout
    tt = rd(os.path.join(d, 'touched.tsv')); assert {x['pair'] for x in tt} == {'TA/TB', 'TA/TC'}
    # 6. --exclude-own-line: the applied page's own agreed tiles enter the pool only for other lines; with the unit's one
    #    line as its own agreement source, the pool for that line holds only the other pages (24/24, groups 3)
    w(os.path.join(d, 'own_agree.tsv'), ['line', 'pos', 'sign'], [[x['line'], x['pos'], x['sign']] for x in rd(os.path.join(d, 'unit.tsv'))])
    r = run(d, '--exclude-own-line', '--pool-agreed', os.path.join(d, 'own_agree.tsv') + ':' + os.path.join(d, 'map.tsv'))
    assert r.returncode == 0, r.stderr
    rep = rd(os.path.join(d, 'rep.tsv'))[0]
    assert rep['pool_a'] == '24' and rep['pool_b'] == '24', rep
    print('test_glyph_atlas_pairbank: all passed')


if __name__ == '__main__':
    main()

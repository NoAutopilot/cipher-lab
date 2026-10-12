#!/usr/bin/env python3
"""Offline test for tools/glyph_atlas.py classify --pair A B (TXE3-10, 11 Oct 2026). Synthetic 48x48 tiles of two
look-alike shapes: A = a loop ON TOP of a stem (the Birago T18 'd' shape), B = a loop in the MIDDLE of a stem that
passes through it (T98 's'); jittered position, radius and stroke. Must catch: pool from secure tokens + a person's sort
gives leave-one-group-out accuracy >= 0.9 and an enabled threshold; applied to a unit whose labels carry 3 planted
swaps, it fixes all 3 and breaks none of the 9 correct positions; a position without a 1:1 box keeps its label. Must
not block / must not pass: the shuffled-label control (--seed 1) reaches no better LOGO accuracy than chance + 0.15
on this separable set, and an apply unit sharing lines with --pool-dev is refused without --loo-lines. The truth file
is written with a 'truth' column only for the dev lines, so a read of an applied line's truth would fail loudly."""
import csv, os, subprocess, sys, tempfile
import numpy as np
from PIL import Image, ImageDraw

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, '..', 'glyph_atlas.py')
sys.path.insert(0, os.path.join(HERE, '..'))
import join_check as JC  # TXE4-5: --map is gated by join_check.require(); the fixture map gets a trivial PASS sidecar



def tile(kind, rng):
    im = Image.new('L', (48, 48), 0)
    d = ImageDraw.Draw(im)
    cx = 24 + int(rng.integers(-3, 4)); r = 7 + int(rng.integers(-1, 2)); t = int(rng.integers(2, 5))
    if kind == 'A':
        cy = 11 + int(rng.integers(-2, 3))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=255, width=t)
        d.line((cx + r - 1, cy, cx + r - 1, 45), fill=255, width=t)
    else:
        cy = 24 + int(rng.integers(-2, 3))
        d.ellipse((cx - r, cy - r, cx + r, cy + r), outline=255, width=t)
        d.line((cx, 3, cx, 45), fill=255, width=t)
    return np.asarray(im, np.uint8)


def main():
    d = tempfile.mkdtemp()
    rng = np.random.default_rng(7)
    sids, bms, rows, sec, own, omap = [], [], [], [], [], []
    pages = ['p1', 'p2', 'p3', 'p4']
    n = 0
    for pg in pages:
        for k in range(16):
            kind = 'AB'[k % 2]
            sid = f'{pg}_01_{n:03d}'; n += 1
            sids.append(sid); bms.append(tile(kind, rng))
            rh = (1.3 if kind == 'A' else 1.8) + rng.normal(0, 0.1); dy = (0.3 if kind == 'A' else 0.0) + rng.normal(0, 0.1)
            rows.append([sid, pg, '1', str(k), '0', '0', '30', '40', f'{rh:.3f}', '0.7', f'{dy:.3f}', ''])
            code = 'TA' if kind == 'A' else 'TB'
            if pg in ('p1', 'p2'):
                sec.append([sid, code, pg, 'S', 'L01', str(k)])
            elif pg == 'p3':
                own.append([f'o_{sid}', code, code, 'kept']); omap.append([f'o_{sid}', pg, sid, '0', '0'])
    with open(os.path.join(d, 'signs.tsv'), 'w') as f:
        f.write('sid\tpage\tline\tpos\tx\ty\tw\th\trh\trw\tdy\tmarks\n' + ''.join('\t'.join(r) + '\n' for r in rows))
    np.savez(os.path.join(d, 'bitmaps.npz'), signs=np.stack(bms), marks=np.zeros((1, 48, 48), np.uint8))
    with open(os.path.join(d, 'secure_tokens.tsv'), 'w') as f:
        f.write('sid\tcode\tpage\tgrade\tpassage\tpos\n' + ''.join('\t'.join(r) + '\n' for r in sec))
    with open(os.path.join(d, 'settled.tsv'), 'w') as f:
        f.write('sid\told_sign\tnew_sign\tstatus\n' + ''.join('\t'.join(r) + '\n' for r in own))
    with open(os.path.join(d, 'owner_map.tsv'), 'w') as f:
        f.write('sid\tatlas_page\tbox\tdist_px\tdup\n' + ''.join('\t'.join(r) + '\n' for r in omap))
    # apply unit = page p4 (16 tiles; 12 with a 1:1 box, 4 without), 3 planted swaps among the boxed ones
    p4 = [r for r in rows if r[1] == 'p4']
    lab, mp, want = [], [], {}
    for i, r in enumerate(p4):
        true = 'TA' if int(r[3]) % 2 == 0 else 'TB'
        L = true
        if i in (1, 4, 6):
            L = 'TB' if true == 'TA' else 'TA'
        line, pos = 'p4_L01', str(i + 1)
        lab.append([line, pos, L]); want[(line, pos)] = (true if i < 12 else L)
        mp.append([r[0], 'p4', line, pos, '1:1' if i < 12 else '2:1'])
    with open(os.path.join(d, 'labels_u.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n' + ''.join('\t'.join(r) + '\n' for r in lab))
    with open(os.path.join(d, 'map.tsv'), 'w') as f:
        f.write('sid\tfol\tline\tpos\top\n' + ''.join('\t'.join(r) + '\n' for r in mp))
    JC.write_sidecar(os.path.join(d, 'map.tsv'), dict(verdict='PASS', n=0, overall={}, share0=1.0, sharepm1=0.0, b1=True, b2=True,
                                                      b3=True, p95_0=0.0, p95_pm1=0.0, b2_bound=0.05, lines={}, draws=0, seed=0))
    base = [sys.executable, TOOL, 'classify', '--pair', 'TA', 'TB', '--out', d, '--pool-secure',
            os.path.join(d, 'secure_tokens.tsv'), '--pool-owner', os.path.join(d, 'settled.tsv'), '--owner-map',
            os.path.join(d, 'owner_map.tsv'), '--map', os.path.join(d, 'map.tsv'), '--apply-unit',
            os.path.join(d, 'labels_u.tsv'), '--tsv', os.path.join(d, 'out.tsv'), '--report', os.path.join(d, 'rep.tsv')]
    r = subprocess.run(base, capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    rep = list(csv.DictReader(open(os.path.join(d, 'rep.tsv')), delimiter='\t'))[0]
    assert rep['pool_a'] == '24' and rep['pool_b'] == '24' and rep['groups'] == '3', rep
    assert float(rep['lolo_acc']) >= 0.9 and rep['enabled'] == '1', rep
    out = {(x['line'], x['pos']): x['sign'] for x in csv.DictReader(open(os.path.join(d, 'out.tsv')), delimiter='\t')}
    assert len(out) == 16
    fixed = sum(out[k] == want[k] and L != want[k] for (k, L) in ((tuple(x[:2]), x[2]) for x in lab))
    broken = sum(out[k] != want[k] and L == want[k] for (k, L) in ((tuple(x[:2]), x[2]) for x in lab))
    assert fixed == 3 and broken == 0, (fixed, broken, out)
    assert all(out[(l, p)] == L for l, p, L in lab[12:]), 'a position without a 1:1 box must keep its label'
    # shuffled-label control: permuted labels on a separable set give near-chance LOGO accuracy
    r = subprocess.run(base + ['--seed', '1', '--tsv', os.path.join(d, 'ctrl.tsv'), '--report', os.path.join(d, 'rc.tsv')],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stderr
    rc = list(csv.DictReader(open(os.path.join(d, 'rc.tsv')), delimiter='\t'))[0]
    assert float(rc['lolo_acc']) <= float(rc['chance']) + 0.15, rc
    # --force-t 0: the shuffled model applies at argmax, so its flips can differ from the real model's (rule 3 can-vary)
    r = subprocess.run(base + ['--seed', '1', '--force-t', '0', '--tsv', os.path.join(d, 'cf.tsv'), '--report',
                       os.path.join(d, 'rf.tsv')], capture_output=True, text=True)
    assert r.returncode == 0 and 'considered 12' in r.stdout, (r.stdout, r.stderr)
    # refusal: an apply unit that shares lines with --pool-dev needs --loo-lines (truth never read for an applied line)
    with open(os.path.join(d, 'truth.tsv'), 'w') as f:
        f.write('line\tpos\tref_sign\ttruth\tplain\tstatus\tflag\n')
    r = subprocess.run(base + ['--pool-dev', os.path.join(d, 'labels_u.tsv'), '--truth', os.path.join(d, 'truth.tsv')],
                       capture_output=True, text=True)
    assert r.returncode != 0 and 'loo-lines' in r.stderr + r.stdout, (r.stdout, r.stderr)
    print('test_glyph_atlas_pair: ok (LOGO acc %s, t %s; fixed 3 broken 0; shuffled %s vs chance %s)'
          % (rep['lolo_acc'], rep['t'], rc['lolo_acc'], rc['chance']))


if __name__ == '__main__':
    main()

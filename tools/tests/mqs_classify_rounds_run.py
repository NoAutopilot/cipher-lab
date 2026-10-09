#!/usr/bin/env python3
"""MQS-CLASSIFY-ROUNDS (9 Oct 2026): measured run of glyph_atlas.py classify --train-labels/--round on Birago no.87,
exactly as pre-registered in tools/tests/PREREG-MQS-CLASSIFY-ROUNDS.md (arm C: simulated careful person on half A of
the held-out no.87 lines, scored on half B; arm T: the owner's 3 Oct 2026 Birago sort, scored on all held-out lines;
each with 20 code-permutation nulls). Disk only, no network. Writes tools/tests/MQS-CLASSIFY-ROUNDS-results.tsv.
Run from the repo root: python3 tools/tests/mqs_classify_rounds_run.py [--seeds 20] [--work DIR]"""
import argparse, csv, os, random, re, subprocess, sys, tempfile

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..'))
F = os.path.join(ROOT, 'ciphers/nevers-birago-fr3251-1572')
A = F + '/atlas'
OWN = F + '/harvest/tx_decode/eye/open/sorter/owner_settled.tsv'
MIX = F + '/harvest/tx_decode/mix/{}_mixmap.tsv'
HELD = [f'f178v_{i}_' for i in range(13, 24)] + [f'f179r_{i:02d}_' for i in (1, 2, 3)]
HALF_A = [f'f178v_{i}_' for i in range(13, 19)]
HALF_B = [h for h in HELD if h not in HALF_A]
R = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
sys.path.insert(0, A)
from name_clusters import value_map  # noqa: E402


def classify(work, name, holdout, train=None):
    out = os.path.join(work, name + '.tsv')
    cmd = [sys.executable, ROOT + '/tools/glyph_atlas.py', 'classify', '--out', A, '--labels', A + '/labels.json',
           '--page', 'all', '--tsv', out, '--topk', '3']
    for h in holdout:
        cmd += ['--holdout', h]
    if train:
        cmd += ['--train-labels', train]
    subprocess.run(cmd, check=True, capture_output=True, text=True)
    return out


def bench(tk, prefixes, out):
    """atlas/topk/no87_heldout_bench.tsv recipe: held-out boxes per line, x order, '_' dropped, k1 as the sign"""
    rows = [r for r in R(tk) if r['box'].startswith(tuple(prefixes)) and r['k1'] != '_']
    with open(out, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in sorted(rows, key=lambda r: (r['page'], int(r['line']), int(r['x']))):
            f.write(f"{r['page']}_L{int(r['line']):02d}\t{r['x']}\t{r['k1']}\n")
    return out


def m1(out, base=None):
    cmd = [sys.executable, ROOT + '/tools/tx_bench.py', out, '--bench', ROOT + '/BENCHMARK-TX.tsv', '--item',
           'birago1572-no87']
    t = subprocess.run(cmd, check=True, capture_output=True, text=True).stdout
    e = re.search(r'err_true ([\d.]+) \((\d+)/(\d+)\)', t)
    p = None
    if base:
        tp = subprocess.run(cmd + ['--paired', base], check=True, capture_output=True, text=True).stdout
        p = re.search(r'fixed (\d+), broken (\d+); sign test p = ([\d.e-]+)', tp)
    return float(e.group(1)), int(e.group(2)), int(e.group(3)), (p.groups() if p else ('', '', '')), t


def m2(tk):
    t = subprocess.run([sys.executable, A + '/score_no87.py', tk], check=True, capture_output=True, text=True).stdout
    return float(re.search(r'atlas top-1:\s+err_true ([\d.]+)', t).group(1))


def write_train(path, pairs):
    with open(path, 'w') as f:
        f.write('box\tcode\tround\n')
        for b, c in pairs:
            f.write(f'{b}\t{c}\t1\n')
    return path


def arm_c():
    V = value_map()
    pairs = [(r['sid'], r['sign']) for r in R(A + '/no87_box_token.tsv')
             if r['split'] == 'heldout' and r['sid'].startswith(tuple(HALF_A)) and r['op'] == '1:1' and r['truth']
             and V.get(r['sign']) == r['truth']]
    return pairs, HALF_B, HALF_B


def arm_t():
    o = {r['sid']: r for r in R(OWN)}
    pairs, seen, dup = [], set(), 0
    for leaf in ('f117', 'f168', 'f144r'):
        for r in R(MIX.format(leaf)):
            t = o.get(r['tile'])
            if not t or not r['box'] or float(r['iou'] or 0) < 0.2:
                continue
            st, code = t['status'], (t['new_sign'] or '').strip()
            if st == 'taken-out':
                code = '_'
            elif st not in ('kept', 'moved') or not code or code == 'UNREAD':
                continue
            if r['box'] in seen:
                dup += 1
                continue
            seen.add(r['box'])
            pairs.append((r['box'], code))
    print(f'arm T: {len(pairs)} owner labels on atlas boxes ({dup} duplicate box hits dropped)')
    return pairs, HELD, HELD


def main():
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument('--seeds', type=int, default=20)
    ap.add_argument('--work', default=tempfile.mkdtemp())
    a = ap.parse_args()
    os.makedirs(a.work, exist_ok=True)
    res = []
    for arm, fn in (('C', arm_c), ('T', arm_t)):
        pairs, hold1, scored = fn()
        tk0 = classify(a.work, f'{arm}_r0', HELD)
        b0 = bench(tk0, scored, os.path.join(a.work, f'{arm}_r0_bench.tsv'))
        e0, k0, n0, _, _ = m1(b0)
        res.append((arm, 'round0', '', len(pairs), e0, f'{k0}/{n0}', '', '', '', m2(tk0)))
        tk1 = classify(a.work, f'{arm}_r1', hold1, write_train(os.path.join(a.work, f'{arm}_train.tsv'), pairs))
        e1, k1, n1, (fx, br, p), _ = m1(bench(tk1, scored, os.path.join(a.work, f'{arm}_r1_bench.tsv')), b0)
        res.append((arm, 'round1', '', len(pairs), e1, f'{k1}/{n1}', e0 - e1, f'{fx}/{br}', p, m2(tk1)))
        codes = [c for _, c in pairs]
        for s in range(1, a.seeds + 1):
            sh = codes[:]
            random.Random(s).shuffle(sh)
            tr = write_train(os.path.join(a.work, f'{arm}_null{s}.tsv'), [(b, c) for (b, _), c in zip(pairs, sh)])
            tks = classify(a.work, f'{arm}_null{s}', hold1, tr)
            es, ks, ns, _, _ = m1(bench(tks, scored, os.path.join(a.work, f'{arm}_null{s}_bench.tsv')))
            res.append((arm, 'null', s, len(pairs), es, f'{ks}/{ns}', e0 - es, '', '', m2(tks)))
        print(arm, 'done', flush=True)
    out = os.path.join(ROOT, 'tools/tests/MQS-CLASSIFY-ROUNDS-results.tsv')
    with open(out, 'w') as f:
        f.write('# MQS-CLASSIFY-ROUNDS, PREREG tools/tests/PREREG-MQS-CLASSIFY-ROUNDS.md; regenerate: '
                'python3 tools/tests/mqs_classify_rounds_run.py\n')
        f.write('arm\trun\tseed\tn_train\tM1_err_true\tM1_k_n\tM1_gain\tfixed_broken\tsign_p\tM2_err_true\n')
        for r in res:
            f.write('\t'.join(f'{x:.4f}' if isinstance(x, float) else str(x) for x in r) + '\n')
    for arm in 'CT':
        g = sorted(r[6] for r in res if r[0] == arm and r[1] == 'null')
        real = [r for r in res if r[0] == arm and r[1] == 'round1'][0]
        p95 = g[int(0.95 * (len(g) - 1) + 0.5)] if g else float('nan')
        print(f'arm {arm}: round0 {[r[4] for r in res if r[0] == arm and r[1] == "round0"][0]:.4f} '
              f'round1 {real[4]:.4f} gain {real[6]:.4f} fixed/broken {real[7]} p {real[8]} | null gain p95 {p95:.4f} '
              f'max {g[-1]:.4f} mean {sum(g) / len(g):.4f} | M2 r1 {real[9]:.3f}')


if __name__ == '__main__':
    main()

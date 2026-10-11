#!/usr/bin/env python3
"""TXE3-4 CALIB: how err_true depends on err_2reader, from committed outputs only (PREREG benchmark-tx/PREREG-txeng3-4.md).

    python3 benchmark-tx/txeng3/4/calib.py [--out benchmark-tx/txeng3/4] [--boot 1000] [--seed 20261011]

No model passes, no network. Imports tools/tx_bench.py (score_item, align, drop_flagged, wilson) and
tools/reconcile_passes.py (nw) so every figure uses the project's own scorer and alignment convention.
Writes calib_pairs.tsv (every pass pair), calib_leaves.tsv (one primary pair per leaf), calib_lines.tsv (per-line
sums behind the bootstrap), calib_fit.json (fits, bootstraps, control, dev->eval report, unread-letter table).
Never opens a confirm item's truth; never opens benchmark-tx/txeng2/oracle1/.
"""
import argparse, csv, json, math, os, random, statistics, sys
from collections import defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench as tb                      # noqa: E402
from reconcile_passes import nw            # noqa: E402

OUT = os.path.join(ROOT, 'benchmark-tx', 'outputs')
FROZEN = {'spinelli-c1519-confirm', 'vivonne1573-f103r-confirm2', 'vivonne1573-f103r-confirm2-w'}

# (leaf, item, split, hand, readers, label, passX, passY, recon or None, primary)  -- fixed in the PREREG
PAIRS = [
    ('no87', 'birago1572-no87', 'eval', 'Birago 1572 clerk', 'Sonnet', 'AB', 'passA', 'passB', 'passC', True),
    ('no87', 'birago1572-no87', 'eval', 'Birago 1572 clerk', 'Opus', 'X21opus', 'passX21_opus_r1', 'passX21_opus_r2',
     'passX21_opus_reconcile', False),
    ('f152r', 'birago1572-f152r', 'eval', 'Birago 1572 clerk', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('bir1591', 'bir1591-f23r-gloss', 'eval', 'Dinteville 1591', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('gunther', 'gunther8246-p2', 'eval', 'Oranje secretary 1561', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('f36v', 'ceppo-f36v-gloss', 'dev', 'Ceppo-Nevers', 'Sonnet', 'AB', 'passA', 'passB', 'passD', True),
    ('f36v', 'ceppo-f36v-gloss', 'dev', 'Ceppo-Nevers', 'Sonnet', 'X21bsonnet', 'passX21b_sonnet_A', 'passX21b_sonnet_B',
     'passX21b_sonnet_reconcile', False),
    ('f36v', 'ceppo-f36v-gloss', 'dev', 'Ceppo-Nevers', 'Opus', 'X21bopus', 'passX21b_opus_r1', 'passX21b_opus_r2',
     'passX21b_opus_reconcile', False),
    ('f21v', 'ceppo-f21v-S', 'dev', 'Ceppo-Nevers', 'Sonnet', 'AB', 'passA', 'passB', None, True),
    ('f87', 'ceppo-f87-S', 'dev', 'Ceppo-Nevers', 'Sonnet', 'AB', 'passA', 'passB', None, True),
    ('f87', 'ceppo-f87-S', 'dev', 'Ceppo-Nevers', 'Opus', 'X21opus', 'passX21_opus_r1', 'passX21_opus_r2',
     'passX21_opus_reconcile', False),
    ('dint128', 'dint-f128-print', 'dev', 'Dinteville office', 'Sonnet', 'AB', 'passA', 'passB', 'passX21_sonnet_reconcile', True),
    ('dint128', 'dint-f128-print', 'dev', 'Dinteville office', 'Opus', 'X21opus', 'passX21_opus_r1', 'passX21_opus_r2',
     'passX21_opus_reconcile', False),
    ('dint128', 'dint-f128-print', 'dev', 'Dinteville office', 'Opus', 'X21bopus', 'passX21b_opus_r1', 'passX21b_opus_r2',
     'passX21b_opus_reconcile', False),
    ('dint98v', 'dint-f98v-gloss', 'dev', 'Dinteville office', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('dint113', 'dint-f113-gloss', 'dev', 'Dinteville office', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('dint89', 'dint-f89-gloss', 'dev', 'Dinteville office', 'Opus', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('luzerne', 'luzerne108a-p1', 'dev', 'La Luzerne digits 1781', 'Sonnet', 'AB', 'passA', 'passB', 'passZ_pipeline', True),
    ('viv102r', 'vivonne1573-f102r-dev2', 'dev', 'Vivonne clerk 1573', 'Sonnet', 'AB', 'passA', 'passB', None, True),
    ('viv102r', 'vivonne1573-f102r-dev2', 'dev', 'Vivonne clerk 1573', 'Opus', 'sv', 'passA_sv', 'passB_sv', 'passZ_sv', False),
    ('viv102r', 'vivonne1573-f102r-dev2', 'dev', 'Vivonne clerk 1573', 'Opus', 'tl', 'passA_tl', 'passB_tl', 'passZ_tl', False),
    ('viv102r', 'vivonne1573-f102r-dev2', 'dev', 'Vivonne clerk 1573', 'Opus', 'dv1',
     '../vivonne1573-f102r-dev/passA_dv1', '../vivonne1573-f102r-dev/passB_dv1', '../vivonne1573-f102r-dev/passZ_dv1', False),
]
# truth-mask sensitivity rows: same leaf, same primary pair, another truth file (never extra points)
VARIANTS = [('bir1591', 'bir1591-f23r-gloss-jk'), ('dint98v', 'dint-f98v-gloss-kp'), ('dint98v', 'dint-f98v-gloss-kp2'),
            ('dint113', 'dint-f113-gloss-kp'), ('dint113', 'dint-f113-gloss-kp2'), ('dint89', 'dint-f89-gloss-kp'),
            ('dint89', 'dint-f89-gloss-kp2'), ('viv102r', 'vivonne1573-f102r-dev')]

# named unread letters and their err_2reader on file (source line in RESULTS.md)
UNREAD = [
    ('Florence c.127 (florence-dieci-responsive)', 0.17, 'TRANSCRIPTION.md Why'),
    ('Florence c.70 L07-L10 gaps117 pair', 0.345, 'ciphers/florence-dieci-responsive/NOTES.md:424'),
    ('Birago 1571 f.36/f.47 (fr.3252)', 0.33, 'TRANSCRIPTION.md Why; birago-fr3252 NOTES.md:598 (0.34 raw)'),
    ('Birago 1571 f.47r L01-04 merged', 0.44, 'ciphers/birago-fr3252-1571-72/NOTES.md:148'),
    ('Birago 1572 f.117r (fr.3252, re-pair)', 0.134, 'ciphers/birago-fr3252-1571-72/NOTES.md:1951 (earlier pair 0.25)'),
    ('Debosnys 1883', 0.28, 'TRANSCRIPTION.md Why'),
    ('Birago 1572 f.144r no.73', 0.24, 'ciphers/nevers-birago-fr3251-1572/NOTES.md:1342'),
    ('Birago 1572 f.168 no.85', 0.13, 'ciphers/nevers-birago-fr3251-1572/NOTES.md:1342'),
    ('Birago 1572 f.185r / f.185v', 0.13, 'ciphers/nevers-birago-fr3251-1572/NOTES.md:1775 (0.12 / 0.29, pooled 0.13)'),
]


def bench_items():
    return {r['item']: r for r in tb.read_tsv(os.path.join(ROOT, 'BENCHMARK-TX.tsv'))}


def load_pass(item_dir, name, lines):
    p = os.path.normpath(os.path.join(OUT, item_dir, name + '.tsv'))
    ol = tb.load_output([p])
    return {k: v for k, v in ol.items() if k in lines}, p


def two_reader(a_lines, b_lines, lines):
    """per line: (agreeing columns, alignment columns) by reconcile_passes' nw (the convention behind every figure on file)."""
    per = {}
    for ln in lines:
        x, y = a_lines.get(ln, []), b_lines.get(ln, [])
        if not x and not y:
            per[ln] = (0, 0); continue
        path = nw(x, y)
        agree = sum(1 for i, j in path if i is not None and j is not None and x[i] == y[j])
        per[ln] = (agree, len(path))
    return per


def aligned_signs(truth_rows, out_lines):
    """{(line,pos): sign or None} at scored positions for lines the output covers (missing line: None everywhere)."""
    by = defaultdict(list)
    for r in truth_rows:
        by[r['line']].append(r)
    res = {}
    for ln, rows in by.items():
        rows.sort(key=lambda r: float(r['pos']))
        if ln not in out_lines:
            for r in rows:
                if r['status'] == 'scored':
                    res[(ln, r['pos'])] = None
            continue
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        for ri, osg in tb.align(ref, ts, out_lines[ln], abstain=True):
            if ri is None or rows[ri]['status'] != 'scored':
                continue
            res[(ln, rows[ri]['pos'])] = osg
    return res


def is_wrong(sign, truthset):
    return sign is None or tb.is_abstention(sign) or sign not in truthset


def score(truth_rows, out_lines):
    r = tb.score_item(truth_rows, out_lines, 'delete', G=0.75)
    k, n, e = tb._measure(r)
    u = tb.score_item(truth_rows, out_lines, 'delete', G=1.0)
    uk, un, ue = tb._measure(u)
    lo, hi = tb.wilson(min(k, n), n)
    return dict(err=e, k=k, n=n, lo=lo, hi=hi, ser=ue, per_line=r['per_line'])


def pair_stats(item, truth, lines, A, B, R):
    tsets = {(r['line'], r['pos']): set(filter(None, r['truth'].split('|'))) for r in truth if r['status'] == 'scored'}
    out = {}
    for mask, rows in (('meas', truth), ('flag', tb.drop_flagged(truth))):
        sc = {'A': score(rows, A), 'B': score(rows, B)}
        if R is not None:
            sc['R'] = score(rows, R)
        out[mask] = sc
    # hidden error on scored positions (as measured mask)
    sa, sb = aligned_signs(truth, A), aligned_signs(truth, B)
    sr = aligned_signs(truth, R) if R is not None else None
    wa = wb = both = same_wrong = 0
    dis_scored = n_scored = 0
    hid_a = hid_b = 0
    dis_err = 0.0
    wr = hid_r = 0
    for key, ts in tsets.items():
        xa, xb = sa.get(key), sb.get(key)
        n_scored += 1
        ea, eb = is_wrong(xa, ts), is_wrong(xb, ts)
        if xa != xb:
            dis_scored += 1; dis_err += (ea + eb) / 2
        wa += ea; wb += eb
        if ea and eb:
            both += 1
            if xa == xb:      # same wrong sign, or both missed the sign: the error agreement cannot see
                same_wrong += 1
        if ea and xa == xb:
            hid_a += 1
        if eb and xa == xb:
            hid_b += 1
        if sr is not None:
            er = is_wrong(sr.get(key), ts)
            wr += er
            if er and xa == xb:
                hid_r += 1
    out['hidden'] = dict(wrongA=wa, wrongB=wb, both_wrong=both, same_wrong=same_wrong, hiddenA=hid_a, hiddenB=hid_b,
                         wrongR=wr, hiddenR=hid_r, scored=n_scored, disagree_scored=dis_scored, dis_err=dis_err)
    return out


def spearman(x, y):
    def rank(v):
        s = sorted(range(len(v)), key=lambda i: v[i]); r = [0.0] * len(v); i = 0
        while i < len(s):
            j = i
            while j + 1 < len(s) and v[s[j + 1]] == v[s[i]]:
                j += 1
            for k in range(i, j + 1):
                r[s[k]] = (i + j) / 2 + 1
            i = j + 1
        return r
    return pearson(rank(x), rank(y))


def pearson(x, y):
    n = len(x)
    if n < 3:
        return float('nan')
    mx, my = sum(x) / n, sum(y) / n
    sx = math.sqrt(sum((a - mx) ** 2 for a in x)); sy = math.sqrt(sum((b - my) ** 2 for b in y))
    if sx == 0 or sy == 0:
        return float('nan')
    return sum((a - mx) * (b - my) for a, b in zip(x, y)) / (sx * sy)


def ratio_fit(x, y):
    """median per-leaf ratio, least-squares through origin, OLS intercept model."""
    ratios = [b / a if a > 0 else float('nan') for a, b in zip(x, y)]
    rr = [r for r in ratios if not math.isnan(r)]
    k_med = statistics.median(rr) if rr else float('nan')
    k_ls = sum(a * b for a, b in zip(x, y)) / sum(a * a for a in x) if sum(a * a for a in x) else float('nan')
    n = len(x); mx, my = sum(x) / n, sum(y) / n
    sxx = sum((a - mx) ** 2 for a in x)
    d = sum((a - mx) * (b - my) for a, b in zip(x, y)) / sxx if sxx else float('nan')
    c = my - d * mx if not math.isnan(d) else float('nan')
    return dict(k_med=k_med, k_ls=k_ls, intercept=c, slope=d, ratios=ratios)


def loo(x, y, model):
    """leave-one-leaf-out absolute errors for: ratio (k_med of the others), intercept OLS, constant mean (null)."""
    errs = {'ratio': [], 'ols': [], 'const': []}
    for i in range(len(x)):
        xs = x[:i] + x[i + 1:]; ys = y[:i] + y[i + 1:]
        f = ratio_fit(xs, ys)
        errs['ratio'].append(abs(f['k_med'] * x[i] - y[i]))
        errs['ols'].append(abs(f['intercept'] + f['slope'] * x[i] - y[i]) if not math.isnan(f['slope']) else float('nan'))
        errs['const'].append(abs(sum(ys) / len(ys) - y[i]))
    return {k: dict(mae=sum(v) / len(v), per_leaf=v) for k, v in errs.items()}


def q(v, p):
    s = sorted(v); i = min(len(s) - 1, max(0, int(round(p * (len(s) - 1)))))
    return s[i]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('--out', default=os.path.join(ROOT, 'benchmark-tx', 'txeng3', '4'))
    ap.add_argument('--boot', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=20261011)
    a = ap.parse_args(argv)
    items = bench_items()
    rows, line_rows = [], []
    for leaf, item, split, hand, readers, label, pa, pb, pr, primary in PAIRS:
        assert item not in FROZEN
        it = items[item]
        truth = tb.read_tsv(os.path.join(ROOT, it['truth']))
        lines = {r['line'] for r in truth}
        A, pathA = load_pass(item, pa, lines)
        B, pathB = load_pass(item, pb, lines)
        R, pathR = load_pass(item, pr, lines) if pr else (None, None)
        covered = set(A) | set(B)
        if covered < lines:   # a pair read on a subset of the item's lines (X21 dev_tune): score that subset only
            lines = covered
            truth = [r for r in truth if r['line'] in lines]
        tr = two_reader(A, B, lines)
        agree, cols = sum(v[0] for v in tr.values()), sum(v[1] for v in tr.values())
        st = pair_stats(item, truth, lines, A, B, R)
        h = st['hidden']
        rec = dict(leaf=leaf, item=item, split=split, hand=hand, readers=readers, pair=label, primary=int(primary),
                   passX=pa, passY=pb, recon=pr or '', lines=len(lines), signsA=sum(len(v) for v in A.values()),
                   signsB=sum(len(v) for v in B.values()), cols=cols, agree=agree,
                   err_2reader=round(1 - agree / cols, 4) if cols else float('nan'),
                   err_2reader_scored=round(h['disagree_scored'] / h['scored'], 4) if h['scored'] else float('nan'),
                   scored=h['scored'])
        for mask in ('meas', 'flag'):
            for who in ('A', 'B', 'R'):
                s = st[mask].get(who)
                if s is None:
                    for f in ('err', 'k', 'n', 'lo', 'hi', 'ser'):
                        rec[f'{who}_{mask}_{f}'] = ''
                    continue
                rec[f'{who}_{mask}_err'] = round(s['err'], 4); rec[f'{who}_{mask}_k'] = s['k']; rec[f'{who}_{mask}_n'] = s['n']
                rec[f'{who}_{mask}_lo'] = round(s['lo'], 4); rec[f'{who}_{mask}_hi'] = round(s['hi'], 4)
                rec[f'{who}_{mask}_ser'] = round(s['ser'], 4)
        rec['single_meas_err'] = round((st['meas']['A']['err'] + st['meas']['B']['err']) / 2, 4)
        rec['single_flag_err'] = round((st['flag']['A']['err'] + st['flag']['B']['err']) / 2, 4)
        rec['ratio_single'] = round(rec['single_meas_err'] / rec['err_2reader'], 3) if rec['err_2reader'] else ''
        rec['ratio_recon'] = round(st['meas']['R']['err'] / rec['err_2reader'], 3) if R is not None and rec['err_2reader'] else ''
        rec.update({k: h[k] for k in ('wrongA', 'wrongB', 'both_wrong', 'same_wrong', 'hiddenA', 'hiddenB', 'wrongR', 'hiddenR')})
        rec['hidden_single'] = round((h['hiddenA'] + h['hiddenB']) / (h['wrongA'] + h['wrongB']), 3) if h['wrongA'] + h['wrongB'] else ''
        # decomposition of the single-pass position error: agreed-wrong rate + visible errors per disagreement x disagreement
        rec['hidden_rate'] = round(h['same_wrong'] / h['scored'], 4) if h['scored'] else ''
        rec['visible_per_disagree'] = round(h['dis_err'] / h['disagree_scored'], 3) if h['disagree_scored'] else ''
        rec['single_pos_err'] = round((h['wrongA'] + h['wrongB']) / 2 / h['scored'], 4) if h['scored'] else ''
        rec['hidden_recon'] = round(h['hiddenR'] / h['wrongR'], 3) if h['wrongR'] else ''
        rows.append(rec)
        for ln in sorted(lines):
            lr = dict(leaf=leaf, item=item, pair=label, primary=int(primary), line=ln, agree=tr[ln][0], cols=tr[ln][1])
            for who in ('A', 'B', 'R'):
                for mask in ('meas', 'flag'):
                    s = st[mask].get(who)
                    pl = s['per_line'].get(ln, dict(N=0, E=0)) if s else dict(N=0, E=0)
                    lr[f'{who}_{mask}_N'] = pl['N']; lr[f'{who}_{mask}_E'] = pl['E']
            line_rows.append(lr)
    # truth-mask sensitivity on the primary pairs
    variants = []
    for leaf, vitem in VARIANTS:
        base = next(p for p in PAIRS if p[0] == leaf and p[9])
        it = items[vitem]
        truth = tb.read_tsv(os.path.join(ROOT, it['truth']))
        lines = {r['line'] for r in truth}
        A, _ = load_pass(base[1], base[6], lines); B, _ = load_pass(base[1], base[7], lines)
        R, _ = load_pass(base[1], base[8], lines) if base[8] else (None, None)
        tr = two_reader(A, B, lines)
        agree, cols = sum(v[0] for v in tr.values()), sum(v[1] for v in tr.values())
        st = pair_stats(vitem, truth, lines, A, B, R)
        variants.append(dict(leaf=leaf, item=vitem, err_2reader=round(1 - agree / cols, 4),
                             single_meas_err=round((st['meas']['A']['err'] + st['meas']['B']['err']) / 2, 4),
                             R_meas_err=round(st['meas']['R']['err'], 4) if R is not None else '',
                             scored=st['hidden']['scored']))
    os.makedirs(a.out, exist_ok=True)
    with open(os.path.join(a.out, 'calib_pairs.tsv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(rows)
    with open(os.path.join(a.out, 'calib_lines.tsv'), 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=list(line_rows[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(line_rows)
    prim = [r for r in rows if r['primary']]
    with open(os.path.join(a.out, 'calib_leaves.tsv'), 'w', newline='') as f:
        cols_ = ['leaf', 'item', 'split', 'hand', 'readers', 'lines', 'scored', 'err_2reader', 'err_2reader_scored',
                 'A_meas_err', 'B_meas_err', 'single_meas_err', 'single_flag_err', 'R_meas_err', 'R_flag_err',
                 'ratio_single', 'ratio_recon', 'hidden_single', 'hidden_recon', 'hidden_rate', 'visible_per_disagree', 'single_pos_err']
        w = csv.DictWriter(f, fieldnames=cols_, delimiter='\t', extrasaction='ignore'); w.writeheader(); w.writerows(prim)

    # ---------- fits on the primary leaves ----------
    rng = random.Random(a.seed)
    x = [r['err_2reader'] for r in prim]
    y1 = [r['single_meas_err'] for r in prim]
    recon_idx = [i for i, r in enumerate(prim) if r['R_meas_err'] != '']
    xr = [x[i] for i in recon_idx]; yr = [prim[i]['R_meas_err'] for i in recon_idx]
    fit = {}
    y1f = [r['single_flag_err'] for r in prim]
    for name, xx, yy, idx in (('single', x, y1, list(range(len(prim)))), ('recon', xr, yr, recon_idx),
                              ('single_flag', x, y1f, list(range(len(prim))))):
        f = ratio_fit(xx, yy)
        rho = spearman(xx, yy); pr_ = pearson(xx, yy)
        # permutation control: shuffle item labels (x across leaves)
        perm_rho, perm_mae = [], []
        for _ in range(a.boot):
            xs = xx[:]; rng.shuffle(xs)
            perm_rho.append(spearman(xs, yy))
            perm_mae.append(loo(xs, yy, 'ratio')['ratio']['mae'])
        lo_ = loo(xx, yy, 'ratio')
        p_rho = sum(1 for v in perm_rho if v >= rho) / len(perm_rho)
        p_mae = sum(1 for v in perm_mae if v <= lo_['ratio']['mae']) / len(perm_mae)
        # line bootstrap within each leaf
        by_leaf = defaultdict(list)
        for lr in line_rows:
            if lr['primary'] and lr['pair'] == 'AB' or (lr['primary'] and lr['leaf'] == 'f36v' and lr['pair'] == 'AB'):
                by_leaf[lr['leaf']].append(lr)
        leaves = [prim[i]['leaf'] for i in idx]
        who = 'R' if name == 'recon' else None
        mk = 'flag' if name == 'single_flag' else 'meas'
        kb, rb = [], []
        for _ in range(a.boot):
            bx, by_ = [], []
            for lf in leaves:
                L = by_leaf[lf]; smp = [L[rng.randrange(len(L))] for _ in L]
                cols = sum(s['cols'] for s in smp); agree = sum(s['agree'] for s in smp)
                if who:
                    N = sum(s['R_meas_N'] for s in smp); E = sum(s['R_meas_E'] for s in smp)
                    yv = E / N if N else float('nan')
                else:
                    NA = sum(s[f'A_{mk}_N'] for s in smp); EA = sum(s[f'A_{mk}_E'] for s in smp)
                    NB = sum(s[f'B_{mk}_N'] for s in smp); EB = sum(s[f'B_{mk}_E'] for s in smp)
                    yv = (EA / NA + EB / NB) / 2 if NA and NB else float('nan')
                xv = 1 - agree / cols if cols else float('nan')
                if not (math.isnan(xv) or math.isnan(yv)) and xv > 0:
                    bx.append(xv); by_.append(yv)
            kb.append(ratio_fit(bx, by_)['k_med']); rb.append(spearman(bx, by_))
        # leaf (cluster) bootstrap: CI of k_med and predictive distribution of a new leaf's ratio
        ratios = [r for r in f['ratios'] if not math.isnan(r)]
        kc, pred = [], []
        for _ in range(a.boot):
            smp = [ratios[rng.randrange(len(ratios))] for _ in ratios]
            kc.append(statistics.median(smp)); pred.append(smp[rng.randrange(len(smp))])
        fit[name] = dict(n_leaves=len(xx), x=xx, y=yy, leaves=leaves, k_med=f['k_med'], k_ls=f['k_ls'],
                         intercept=f['intercept'], slope=f['slope'], ratios=f['ratios'],
                         ratio_min=min(ratios), ratio_max=max(ratios), ratio_q10=q(ratios, .10), ratio_q90=q(ratios, .90),
                         spearman=rho, pearson=pr_, perm_p_rho=p_rho, perm_rho_q95=q(perm_rho, .95),
                         perm_rho_mean=sum(perm_rho) / len(perm_rho),
                         loo=lo_, perm_p_loo_mae=p_mae, perm_loo_mae_q05=q(perm_mae, .05),
                         line_boot_k_med_ci=(q(kb, .025), q(kb, .975)), line_boot_rho_ci=(q(rb, .025), q(rb, .975)),
                         leaf_boot_k_med_ci=(q(kc, .025), q(kc, .975)), leaf_pred_ratio_ci=(q(pred, .025), q(pred, .975)))
    # all pairs (23): Spearman with a leaf cluster bootstrap; sensitivity fit without the two S-token leaves (truth = these passes' reconciliation)
    ax = [r['err_2reader'] for r in rows]; ay = [r['single_meas_err'] for r in rows]
    leaf_of = [r['leaf'] for r in rows]; uleaf = sorted(set(leaf_of))
    cb = []
    for _ in range(a.boot):
        pick = [uleaf[rng.randrange(len(uleaf))] for _ in uleaf]
        bx = [ax[i] for i in range(len(rows)) if leaf_of[i] in pick]; by_ = [ay[i] for i in range(len(rows)) if leaf_of[i] in pick]
        cb.append(spearman(bx, by_) if len(bx) > 2 else float('nan'))
    cb = [v for v in cb if not math.isnan(v)]
    allpairs = dict(n=len(rows), spearman=spearman(ax, ay), cluster_boot_rho_ci=(q(cb, .025), q(cb, .975)))
    noS = [i for i, r in enumerate(prim) if r['leaf'] not in ('f21v', 'f87')]
    fns = ratio_fit([x[i] for i in noS], [y1[i] for i in noS])
    sens_noS = dict(n=len(noS), k_med=fns['k_med'], spearman=spearman([x[i] for i in noS], [y1[i] for i in noS]),
                    loo=loo([x[i] for i in noS], [y1[i] for i in noS], 'ratio'))
    # dev -> eval report (single endpoint, ratio predictor from dev leaves only)
    dev = [i for i, r in enumerate(prim) if r['split'] == 'dev']; ev = [i for i, r in enumerate(prim) if r['split'] == 'eval']
    fd = ratio_fit([x[i] for i in dev], [y1[i] for i in dev])
    dr = [r for r in fd['ratios'] if not math.isnan(r)]
    predd = []
    for _ in range(a.boot):
        smp = [dr[rng.randrange(len(dr))] for _ in dr]; predd.append(smp[rng.randrange(len(smp))])
    band = (q(predd, .025), q(predd, .975))
    lo_dev = loo([x[i] for i in dev], [y1[i] for i in dev], 'ratio')
    evalrep = []
    for i in ev:
        lo_b, hi_b = x[i] * band[0], x[i] * band[1]
        evalrep.append(dict(leaf=prim[i]['leaf'], err_2reader=x[i], true=y1[i], pred=fd['k_med'] * x[i],
                            band=(lo_b, hi_b), inside=lo_b <= y1[i] <= hi_b))
    # per-hand and per-reader spread (all pairs)
    def grp(key):
        g = defaultdict(list)
        for r in rows:
            if r['ratio_single'] != '':
                g[r[key]].append(r['ratio_single'])
        return {k: dict(n=len(v), min=min(v), median=statistics.median(v), max=max(v)) for k, v in g.items()}
    allp = [r['ratio_single'] for r in rows if r['ratio_single'] != '']
    # unread letters
    fs = fit['single']; fr = fit['recon']
    unread = []
    for name, e2, src in UNREAD:
        unread.append(dict(letter=name, err_2reader=e2, source=src,
                           single_point=fs['k_med'] * e2, single_range=(fs['ratio_min'] * e2, fs['ratio_max'] * e2),
                           single_pred95=(fs['leaf_pred_ratio_ci'][0] * e2, fs['leaf_pred_ratio_ci'][1] * e2),
                           recon_point=fr['k_med'] * e2, recon_range=(fr['ratio_min'] * e2, fr['ratio_max'] * e2),
                           recon_pred95=(fr['leaf_pred_ratio_ci'][0] * e2, fr['leaf_pred_ratio_ci'][1] * e2)))
    need = dict(single_point=0.05 / fs['k_med'], single_worst=0.05 / fs['ratio_max'], single_pred95=0.05 / fs['leaf_pred_ratio_ci'][1],
                recon_point=0.05 / fr['k_med'], recon_worst=0.05 / fr['ratio_max'], recon_pred95=0.05 / fr['leaf_pred_ratio_ci'][1])
    gate = dict(g1_perm_p_lt_005=fs['perm_p_rho'] < 0.05,
                g2_loo_ratio_beats_const=fs['loo']['ratio']['mae'] < fs['loo']['const']['mae'],
                g3_eval_inside=sum(1 for e in evalrep if e['inside']), g3_pass=sum(1 for e in evalrep if e['inside']) >= 3,
                g4_spread_factor=fs['ratio_q90'] / fs['ratio_q10'] if fs['ratio_q10'] else float('inf'))
    gate['holds'] = bool(gate['g1_perm_p_lt_005'] and gate['g2_loo_ratio_beats_const'] and gate['g3_pass'])
    out = dict(fit=fit, dev_fit=dict(k_med=fd['k_med'], ratios=fd['ratios'], band=band, loo=lo_dev, n_dev=len(dev)),
               eval_report=evalrep, by_hand=grp('hand'), by_readers=grp('readers'),
               all_pairs_ratio=dict(n=len(allp), min=min(allp), q10=q(allp, .1), median=statistics.median(allp), q90=q(allp, .9), max=max(allp)),
               variants=variants, unread=unread, allpairs=allpairs, sens_noS=sens_noS, need_for_005=need, gate=gate, seed=a.seed, boot=a.boot)
    with open(os.path.join(a.out, 'calib_fit.json'), 'w') as f:
        json.dump(out, f, indent=1, default=lambda o: float(o))
    # console summary
    print('leaf          split rd      x=err2r  A      B      single recon  ratio_s ratio_r hid_s hid_r scored')
    for r in prim:
        print(f"{r['leaf']:13s} {r['split']:5s} {r['readers']:7s} {r['err_2reader']:.3f}   {r['A_meas_err']:.3f}  {r['B_meas_err']:.3f}  "
              f"{r['single_meas_err']:.3f}  {str(r['R_meas_err']):6s} {str(r['ratio_single']):7s} {str(r['ratio_recon']):7s} "
              f"{str(r['hidden_single']):5s} {str(r['hidden_recon']):5s} {r['scored']}")
    for name in ('single', 'recon', 'single_flag'):
        f = fit[name]
        print(f"\n[{name}] n={f['n_leaves']} k_med={f['k_med']:.3f} k_ls={f['k_ls']:.3f} ols y={f['intercept']:.3f}+{f['slope']:.3f}x "
              f"| ratios {f['ratio_min']:.2f}-{f['ratio_max']:.2f} (q10-q90 {f['ratio_q10']:.2f}-{f['ratio_q90']:.2f}) "
              f"| spearman {f['spearman']:.3f} perm p {f['perm_p_rho']:.3f} (perm q95 {f['perm_rho_q95']:.3f}) "
              f"| LOO MAE ratio {f['loo']['ratio']['mae']:.4f} ols {f['loo']['ols']['mae']:.4f} const {f['loo']['const']['mae']:.4f} perm p {f['perm_p_loo_mae']:.3f} "
              f"| line-boot k_med {f['line_boot_k_med_ci']} rho {f['line_boot_rho_ci']} | leaf-boot k_med {f['leaf_boot_k_med_ci']} pred ratio {f['leaf_pred_ratio_ci']}")
    print('\ndev-only k_med %.3f band %s; eval:' % (fd['k_med'], band))
    for e in evalrep:
        print('  %-10s x %.3f true %.3f pred %.3f band %.3f-%.3f %s' % (e['leaf'], e['err_2reader'], e['true'], e['pred'], e['band'][0], e['band'][1], 'IN' if e['inside'] else 'OUT'))
    print('\ngate:', gate)
    print('all pairs:', allpairs, '\nsens no S-items:', {k: v for k, v in sens_noS.items() if k != 'loo'}, 'LOO ratio', sens_noS['loo']['ratio']['mae'], 'const', sens_noS['loo']['const']['mae'])
    print('decomp: leaf hidden_rate visible_per_disagree single_pos_err err2r_scored')
    for r in prim:
        print('  ', r['leaf'].ljust(9), r['hidden_rate'], r['visible_per_disagree'], r['single_pos_err'], r['err_2reader_scored'])
    print('by readers:', out['by_readers']); print('by hand:', out['by_hand'])
    print('variants:', variants)
    return 0


if __name__ == '__main__':
    sys.exit(main())

#!/usr/bin/env python3
"""One blind reading checks itself (TXE4-4 SELF-CHECK, account 3, 12 Oct 2026; PREREG benchmark-tx/PREREG-txeng4-4.md).

A classifier trained ONLY on one pass's own signs at the atlas boxes of the page's OTHER lines (leave-one-line-out, LOLO:
the line being classified never trains) gives every box a top-3 with vote shares; an isotonic map fitted once on dev truth
turns the top-1's score into a probability; a flip rule changes the pass's sign to the top-1 where the top-1 is likely and
the pass's own sign is unlikely. No truth, no other reader, no owner evidence and no labels.json enter the classifier or the
join. The ceiling is structural: a classifier trained on pass A's labels learns A's systematic misreads, so it can only catch
A's INCONSISTENT reads.

Features are tools/glyph_atlas.py's own (`feats`: HOG -> PCA 40 -> unit scale + 3 x log size), imported unchanged, fitted
unsupervised on the whole atlas. The join of pass positions to atlas boxes is tools/box_token_align.py (round 1 width-only
as a seed, round 2 steered by this tool's own LOLO top-3, leave-one-out) gated by tools/join_check.py (R4a). Only `fit`
opens a truth file (the dev lines named on its command line, through tx_bench.read_tsv/align/is_flagged); `map`,
`classify`, `apply` and `null` never do.

Subcommands (run from the repo root):
  map       --atlas DIR --read PASS.tsv --pages PAGE[:line_offset[:L<nn>=cx<N|cx>N]]... --out PREFIX
            round 1 (lam 0) -> LOLO kNN -> round 2 (lam 1.5, loo) -> join_check (leave-one-out row); writes PREFIX_round1.tsv,
            PREFIX_round2.tsv, PREFIX_kept.tsv (sid line pos: 1:1 at the same pos in both rounds on a line that passed),
            PREFIX_joincheck.json and prints the per-line rows and the verdict (exit 0 PASS, 2 FAIL, 3 UNCHECKABLE).
  classify  --atlas DIR --read PASS.tsv --kept KEPT.tsv --out TOPK.tsv [--permute SEED]
            LOLO kNN on the pass's signs at the kept boxes; --permute shuffles the training labels across the kept boxes
            (control (a)). Columns: sid line pos sign k1 s1 d1 k2 s2 d2 k3 s3 d3 sA dA uA u1.
  fit       --topk TOPK.tsv --truth TRUTH.tsv --lines L... --out FIT.json     (dev lines only; isotonic PAV of [k1 in truth set] on u1)
  apply     --topk TOPK.tsv --read PASS.tsv --fit FIT.json --tau T --eps E --out OUT.tsv [--lines L...]
            writes the pass with the flips (line pos sign) and OUT.flips.tsv; --random N --seed S instead flips N random kept
            positions to the top-2 (control (b)).
  ece       --topk TOPK.tsv --fit FIT.json --truth TRUTH.tsv --lines L...   (reported beside; reads truth through tx_bench)

Offline test: tools/tests/test_tx_selfcheck.py (LOLO never trains on the classified line; the isotonic map is monotone; the
flip rule respects tau and eps). No network, no model call.
"""
import argparse, csv, json, os, random, sys, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import box_token_align as BA  # noqa: E402
import join_check as JC       # noqa: E402

K, POOL, LAM_MARGIN = 5, 40, 0.25
TOPK_COLS = ['sid', 'line', 'pos', 'sign', 'k1', 's1', 'd1', 'k2', 's2', 'd2', 'k3', 's3', 'd3', 'sA', 'dA', 'uA', 'u1']


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    with open(p, 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join('' if r.get(c) is None else str(r[c]) for c in cols) + '\n')


# ---------------------------------------------------------------- features (glyph_atlas's own)
def atlas_features(atlas):
    """X (n x D) and the signs.tsv rows, from tools/glyph_atlas.feats on the whole atlas (unsupervised)."""
    import glyph_atlas as GA
    rows = GA.read(atlas, 'signs.tsv')
    bm = np.load(os.path.join(atlas, 'bitmaps.npz'))['signs']
    X = GA.feats(bm, rows)
    return X, rows


# ---------------------------------------------------------------- the LOLO kNN
def lolo_topk(X, rows, labels, targets, own=None, k=K, pool=POOL, line_of=None):
    """labels: {sid: sign} (the training reads at their boxes); targets: sids to classify; own: {sid: the pass's sign at
    that box} for the sA/dA/uA columns. For a target on line L the voters are the labelled boxes whose line != L
    (line_of[sid], default the atlas page_line). Returns rows with k1..k3, shares, distances, sA, dA, uA, u1."""
    from sklearn.neighbors import NearestNeighbors
    idx = {r['sid']: i for i, r in enumerate(rows)}
    if line_of is None:
        line_of = {r['sid']: f"{r['page']}_{r['line']}" for r in rows}
    lab_sids = [s for s in labels if s in idx]
    by_line = collections.defaultdict(list)
    for s in targets:
        by_line[line_of[s]].append(s)
    out = []
    for line, sids in sorted(by_line.items()):
        train = [s for s in lab_sids if line_of[s] != line]
        assert all(line_of[s] != line for s in train), 'LOLO: a voter sits on the classified line'
        if len(train) < 2:
            continue
        T = np.array([idx[s] for s in train])
        npool = min(len(T), max(k + 1, pool))
        nn = NearestNeighbors(n_neighbors=npool).fit(X[T])
        d, ix = nn.kneighbors(X[[idx[s] for s in sids]])
        for n, s in enumerate(sids):
            pairs = [(float(x), labels[train[j]]) for x, j in zip(d[n], ix[n])]
            votes = collections.Counter()
            for x, c in pairs[:k]:
                votes[c] += 1.0 / (x + 1e-6)
            tot = sum(votes.values())
            near = {}
            for x, c in pairs:
                near.setdefault(c, x)
            rank = sorted(votes, key=lambda c: -votes[c]) + sorted((c for c in near if c not in votes), key=near.get)
            row = dict(sid=s, line=line, pos='', sign=(own or {}).get(s, ''))
            for kk in range(3):
                c = rank[kk] if kk < len(rank) else ''
                row[f'k{kk + 1}'] = c
                row[f's{kk + 1}'] = f'{votes.get(c, 0) / tot:.4f}' if c else ''
                row[f'd{kk + 1}'] = f'{near[c]:.4f}' if c else ''

            def u_of(c):
                sh = votes.get(c, 0) / tot
                if c not in near:
                    return sh, -1.0, ''
                dc = near[c]
                others = [near[o] for o in near if o != c]
                if not others:
                    return sh, 1.0, dc
                do = min(others)
                m = (do - dc) / (do + dc) if (do + dc) > 0 else 0.0
                return sh, m, dc
            sh1, m1, _ = u_of(rank[0])
            row['u1'] = f'{sh1 + LAM_MARGIN * m1:.4f}'
            a = row['sign']
            if a:
                shA, mA, dA = u_of(a)
                row['sA'] = f'{shA:.4f}'; row['dA'] = f'{dA:.4f}' if dA != '' else ''
                row['uA'] = f'{shA + LAM_MARGIN * mA:.4f}'
            else:
                row['sA'] = row['dA'] = row['uA'] = ''
            out.append(row)
    return out


# ---------------------------------------------------------------- the join (R4a)
def page_specs(specs):
    """'f152r:1:L01=cx>2520:L04=cx<2460' -> (page, offset, {line: predicate}); offset = atlas line - read line."""
    out = []
    for sp in specs:
        parts = sp.split(':')
        page, off = parts[0], int(parts[1]) if len(parts) > 1 else 0
        bounds = {}
        for b in parts[2:]:
            ln, cond = b.split('=')
            op, v = cond[2], float(cond[3:])
            bounds[f'{page}_{ln}'] = (lambda cx, op=op, v=v: cx > v if op == '>' else cx < v)
        out.append((page, off, bounds))
    return out


def item_signs(rows, specs):
    """The atlas rows of the item's pages, with line renumbered to the READ's line numbers and prose boxes dropped."""
    out = []
    for page, off, bounds in specs:
        for r in rows:
            if r['page'] != page:
                continue
            li = int(r['line']) - off
            if li < 1:
                continue
            pred = bounds.get(f'{page}_L{li:02d}')
            if pred and not pred(int(r['x']) + int(r['w']) / 2):
                continue
            rr = dict(r); rr['line'] = str(li)
            out.append(rr)
    return out


def run_map(a):
    X, rows = atlas_features(a.atlas)
    specs = page_specs(a.pages)
    signs = item_signs(rows, specs)
    read = rd(a.read)
    lines = sorted({r['line'] for r in read if BA.split_line(r['line'])[0] in {p for p, _, _ in specs}})
    sign_at = {(r['line'], str(r['pos'])): r['sign'] for r in read}
    # round 1: width only, a seed
    r1, _ = BA.build_map(signs, read, labels=None, lines=lines, lam=0.0, loo=False)
    wr(a.out + '_round1.tsv', ['sid', 'line', 'pos', 'op'], r1)
    pos1 = {r['sid']: (r['line'], str(r['pos'])) for r in r1 if r['op'] == '1:1' and r['sid']}
    labels1 = {s: sign_at[lp] for s, lp in pos1.items() if lp in sign_at}
    # the LOLO kNN on the round-1 tokens -> a top-3 per box of the item
    line_of = {r['sid']: f"{r['page']}_L{int(r['line']):02d}" for r in signs}
    targets = [r['sid'] for r in signs]
    tk = lolo_topk(X, rows, labels1, targets, line_of=line_of)
    wr(a.out + '_seedtopk.tsv', TOPK_COLS, tk)
    steer = collections.defaultdict(dict)
    for r in tk:
        for kk, w in (('k1', 1.0), ('k2', 0.5), ('k3', 0.5)):
            if r[kk] and r[kk] != '_':
                steer[r['sid']][r[kk]] = max(steer[r['sid']].get(r[kk], 0.0), w)
    # round 2: steered, leave-one-out on
    r2, per = BA.build_map(signs, read, labels=steer, lines=lines, lam=BA.LAM, neutral=BA.NEUTRAL, loo=True)
    wr(a.out + '_round2.tsv', ['sid', 'line', 'pos', 'op', 'labels', 'loo_pos'], r2)
    # the check: labels = the same top-1 (they steered the map -> leave-one-out positions), join_check's bounds
    chk = {r['sid']: r['k1'] for r in tk if r['k1'] and r['k1'] != '_'}
    rs = JC.read_sign_table(read)
    pos_loo = BA.positions(r2, loo=True)
    res = JC.evaluate(pos_loo, chk, rs, draws=a.draws, seed=a.seed)
    res['in_sample'] = dict(BA.offset_check(BA.positions(r2), chk, rs))
    pos2 = {r['sid']: (r['line'], str(r['pos'])) for r in r2 if r['op'] == '1:1' and r['sid']}
    passed = {ln for ln, v in res['lines'].items() if v['verdict'] == 'pass'}
    if a.drop:
        passed -= set(a.drop)
    kept = [dict(sid=s, line=lp[0], pos=lp[1]) for s, lp in sorted(pos2.items(), key=lambda t: (t[1][0], int(t[1][1])))
            if pos1.get(s) == lp and lp[0] in passed]
    wr(a.out + '_kept.tsv', ['sid', 'line', 'pos'], kept)
    cov = collections.Counter(k['line'] for k in kept)
    res['kept_per_line'] = {ln: dict(kept=cov.get(ln, 0), tokens=per[ln]['tokens'], boxes=per[ln]['boxes']) for ln in lines}
    res['dropped_lines'] = list(a.drop or [])
    json.dump(res, open(a.out + '_joincheck.json', 'w'), indent=1)
    print(f"round 1 1:1 {len(pos1)} | round 2 ops {dict(collections.Counter(r['op'] for r in r2))} | kept (1:1 both rounds, line passed) {len(kept)}")
    print(f"in-sample check {BA.fmt_check(collections.Counter(res['in_sample']))}")
    print(f"leave-one-out check n {res['n']}: {res['overall']} share0 {res['share0']:.3f} sharepm1 {res['sharepm1']:.3f} "
          f"(null p95 share0 {res['p95_0']:.3f}, pm1 bound {res['b2_bound']:.3f}) B1 {res['b1']} B2 {res['b2']} B3 {res['b3']}")
    for ln in lines:
        v = res['lines'].get(ln, dict(verdict='unchecked', counts={}, placed=0))
        c = collections.Counter(v['counts'])
        print(f"  {ln}: placed {v['placed']} 0/-1/+1/+-2/none {c['0']}/{c['-1']}/{c['+1']}/{c['+-2']}/{c['none']} "
              f"{v['verdict'].upper()} | kept {cov.get(ln, 0)} of {per[ln]['tokens']} tokens ({per[ln]['boxes']} boxes)")
    print('VERDICT', res['verdict'])
    return {'PASS': 0, 'FAIL': 2, 'UNCHECKABLE': 3}[res['verdict']]


# ---------------------------------------------------------------- classify / fit / apply
def run_classify(a):
    X, rows = atlas_features(a.atlas)
    kept = rd(a.kept)
    read = {(r['line'], str(r['pos'])): r['sign'] for r in rd(a.read)}
    labels = {k['sid']: read[(k['line'], k['pos'])] for k in kept if (k['line'], k['pos']) in read}
    own = dict(labels)
    if a.permute is not None:
        rnd = random.Random(a.permute)
        sids = sorted(labels); vals = [labels[s] for s in sids]; rnd.shuffle(vals)
        labels = dict(zip(sids, vals))
    line_of = {k['sid']: k['line'] for k in kept}
    tk = lolo_topk(X, rows, labels, [k['sid'] for k in kept], own=own, line_of=line_of)
    pos = {k['sid']: k['pos'] for k in kept}
    for r in tk:
        r['pos'] = pos[r['sid']]
    tk.sort(key=lambda r: (r['line'], int(r['pos'])))
    wr(a.out, TOPK_COLS, tk)
    print(f"{a.out}: {len(tk)} kept boxes classified LOLO from {len(labels)} own labels"
          + (f" (labels permuted, seed {a.permute})" if a.permute is not None else ''))


def pav(u, y):
    """Isotonic (increasing) regression by pool-adjacent violators; returns knots [(u, p)] with distinct u."""
    order = np.argsort(u, kind='stable'); u = np.asarray(u, float)[order]; y = np.asarray(y, float)[order]
    blocks = [[u[i], u[i], y[i], 1.0] for i in range(len(u))]   # lo, hi, mean, weight
    i = 0
    while i < len(blocks) - 1:
        if blocks[i][2] > blocks[i + 1][2]:
            a_, b_ = blocks[i], blocks[i + 1]
            w = a_[3] + b_[3]
            blocks[i:i + 2] = [[a_[0], b_[1], (a_[2] * a_[3] + b_[2] * b_[3]) / w, w]]
            i = max(i - 1, 0)
        else:
            i += 1
    knots = []
    for lo, hi, m, _ in blocks:
        knots.append((float(lo), float(m)))
        if hi != lo:
            knots.append((float(hi), float(m)))
    return knots


def calibrate(knots, u):
    xs = [k[0] for k in knots]; ps = [k[1] for k in knots]
    if u <= xs[0]:
        return ps[0]
    if u >= xs[-1]:
        return ps[-1]
    return float(np.interp(u, xs, ps))


def truth_sets_for(read_rows, truth_path, lines):
    """{(line, pos of the READ): truth set} for the read's positions aligned to the unflagged scored truth positions of
    the named lines (tx_bench.align, G 0.75; the set is the truth column only, exactly tx_bench.position_errors's test --
    a first version also admitted ref_sign and under-counted pass A's dev errors 8 for 16, fixed 12 Oct 2026 01:4x UTC
    before any eval look). The only truth read outside tx_bench, for `fit` and `ece`."""
    import tx_bench as TB
    truth = TB.read_tsv(truth_path)
    by = collections.defaultdict(list)
    for r in truth:
        if r['line'] in lines:
            by[r['line']].append(r)
    out_lines = collections.defaultdict(list)
    for r in read_rows:
        out_lines[r['line']].append((int(r['pos']), r['sign']))
    sets = {}
    for ln, trows in by.items():
        trows.sort(key=lambda r: float(r['pos']))
        toks = sorted(out_lines.get(ln, []))
        if not toks:
            continue
        ref = [r['ref_sign'] for r in trows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in trows]   # the truth column only, as tx_bench.position_errors
        path = TB.align(ref, ts, [s for _, s in toks])                   # (ref_sign matches in the ALIGNMENT only)
        j = 0
        for ri, osg in path:
            if ri is None:
                j += 1; continue
            if osg is None:
                continue
            r = trows[ri]
            if r['status'] == 'scored' and not TB.is_flagged(r):
                sets[(ln, str(toks[j][0]))] = ts[ri]
            j += 1
    return sets


def run_fit(a):
    tk = rd(a.topk)
    read = [dict(line=r['line'], pos=r['pos'], sign=r['sign']) for r in tk]
    sets = truth_sets_for(rd(a.read), a.truth, set(a.lines))
    u, y = [], []
    for r in tk:
        key = (r['line'], r['pos'])
        if key in sets and r['k1']:
            u.append(float(r['u1'])); y.append(1.0 if r['k1'] in sets[key] else 0.0)
    knots = pav(u, y)
    fit = dict(knots=knots, n=len(u), lines=sorted(a.lines), lam_margin=LAM_MARGIN, k=K, pool=POOL,
               top1_acc=float(np.mean(y)) if y else None)
    json.dump(fit, open(a.out, 'w'), indent=1)
    print(f'fit: {len(u)} dev boxes, top-1 in truth set {sum(y):.0f}/{len(y)}, {len(knots)} knots, '
          f'p range {knots[0][1]:.3f}-{knots[-1][1]:.3f}')


def flips_for(tk, knots, tau, eps, lines=None):
    out = []
    for r in tk:
        if lines and r['line'] not in lines:
            continue
        if not r['k1'] or not r['uA']:
            continue
        p1, pA = calibrate(knots, float(r['u1'])), calibrate(knots, float(r['uA']))
        if p1 >= tau and pA <= eps and r['k1'] != r['sign']:
            out.append(dict(line=r['line'], pos=r['pos'], sid=r['sid'], old=r['sign'], new=r['k1'], p1=f'{p1:.3f}', pA=f'{pA:.3f}'))
    return out


def run_apply(a):
    tk = rd(a.topk)
    read = rd(a.read)
    lines = set(a.lines) if a.lines else None
    if a.random is not None:
        rnd = random.Random(a.seed)
        cand = [r for r in tk if (not lines or r['line'] in lines) and r['k1']]
        pick = rnd.sample(cand, min(a.random, len(cand)))
        flips = [dict(line=r['line'], pos=r['pos'], sid=r['sid'], old=r['sign'], new=(r['k1'] if r['k1'] != r['sign'] else r['k2']),
                      p1='', pA='') for r in pick]
        flips = [f for f in flips if f['new']]
    else:
        knots = json.load(open(a.fit))['knots']
        flips = flips_for(tk, knots, a.tau, a.eps, lines)
    F = {(f['line'], f['pos']): f['new'] for f in flips}
    out = [dict(line=r['line'], pos=r['pos'], sign=F.get((r['line'], str(r['pos'])), r['sign'])) for r in read
           if not lines or r['line'] in lines]
    wr(a.out, ['line', 'pos', 'sign'], out)
    wr(a.out + '.flips.tsv', ['line', 'pos', 'sid', 'old', 'new', 'p1', 'pA'], flips)
    print(f'{a.out}: {len(flips)} flips')


def run_ece(a):
    tk = rd(a.topk)
    knots = json.load(open(a.fit))['knots']
    sets = truth_sets_for([dict(line=r['line'], pos=r['pos'], sign=r['sign']) for r in rd(a.read)], a.truth, set(a.lines))
    bins = collections.defaultdict(lambda: [0, 0.0, 0.0])
    n = 0
    for r in tk:
        key = (r['line'], r['pos'])
        if key not in sets or not r['k1']:
            continue
        p = calibrate(knots, float(r['u1'])); b = min(int(p * 10), 9)
        bins[b][0] += 1; bins[b][1] += p; bins[b][2] += 1.0 if r['k1'] in sets[key] else 0.0; n += 1
    ece = sum(c * abs(sp / c - sy / c) for c, sp, sy in bins.values()) / n if n else float('nan')
    print(f'ECE {ece:.3f} on {n} boxes; bins (lo, n, mean p, acc): ' +
          ', '.join(f'({b / 10:.1f}, {c}, {sp / c:.2f}, {sy / c:.2f})' for b, (c, sp, sy) in sorted(bins.items())))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest='cmd', required=True)
    m = sub.add_parser('map'); m.add_argument('--atlas', required=True); m.add_argument('--read', required=True)
    m.add_argument('--pages', nargs='+', required=True); m.add_argument('--out', required=True)
    m.add_argument('--drop', nargs='*', default=[], help='lines to drop after a FAIL (the one re-check)')
    m.add_argument('--draws', type=int, default=JC.DEFAULT_DRAWS); m.add_argument('--seed', type=int, default=JC.DEFAULT_SEED)
    m.set_defaults(fn=run_map)
    c = sub.add_parser('classify'); c.add_argument('--atlas', required=True); c.add_argument('--read', required=True)
    c.add_argument('--kept', required=True); c.add_argument('--out', required=True); c.add_argument('--permute', type=int)
    c.set_defaults(fn=run_classify)
    f = sub.add_parser('fit'); f.add_argument('--topk', required=True); f.add_argument('--read', required=True)
    f.add_argument('--truth', required=True); f.add_argument('--lines', nargs='+', required=True); f.add_argument('--out', required=True)
    f.set_defaults(fn=run_fit)
    p = sub.add_parser('apply'); p.add_argument('--topk', required=True); p.add_argument('--read', required=True)
    p.add_argument('--fit'); p.add_argument('--tau', type=float); p.add_argument('--eps', type=float)
    p.add_argument('--out', required=True); p.add_argument('--lines', nargs='*')
    p.add_argument('--random', type=int); p.add_argument('--seed', type=int, default=1)
    p.set_defaults(fn=run_apply)
    e = sub.add_parser('ece'); e.add_argument('--topk', required=True); e.add_argument('--read', required=True)
    e.add_argument('--fit', required=True); e.add_argument('--truth', required=True); e.add_argument('--lines', nargs='+', required=True)
    e.set_defaults(fn=run_ece)
    a = ap.parse_args(argv)
    return a.fn(a) or 0


if __name__ == '__main__':
    sys.exit(main())

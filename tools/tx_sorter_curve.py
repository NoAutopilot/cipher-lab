#!/usr/bin/env python3
"""Sorter value curve: how fast does an owner sorter session drive a line read's err_true down? (X6, TXE2-SORT,
LANE TX-ENGINEER-2, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-1.md section X6; S4 measurement, no gate).

    python3 tools/tx_sorter_curve.py --truth ITEM.truth.tsv --base L.tsv --lines LINES.tsv \\
        [--map no87_box_token.tsv --clusters clusters.tsv] [--signals UNIT_signals.tsv ...] \\
        [--kmax 200] [--seeds 10] [--exclude-flagged] --out curve_<item>_<unit>.tsv [--json summary.json]

Simulation. The benchmark truth plays the owner (an oracle): a "decision" shows one tile (one line-read position)
and the oracle names its true sign (the line read's own sign when that is in the truth set, else the truth row's
ref_sign when in the set, else the set's first member). With a box<->position map (--map: columns sid, line, pos, op;
the map's `truth` column is never read) and atlas clusters (--clusters: id, kind, cluster), the FIRST decision on a
cluster sets every not-yet-decided tile of that cluster in the unit to the shown tile's true sign (TRANSCRIPTION.md
item 6, decisions propagate per cluster; an impure cluster therefore breaks its minority, counted as `broken`); a later
decision on a tile of an already-decided cluster moves that one tile only (the owner taking a tile out of a pile).
Only 1:1 boxes move; 2:1 / 1:2 map rows are left at the line read. --propagate pile narrows the propagation to the
cluster's tiles whose current sign equals the shown tile's (the sorter pile x cluster); --propagate none, or no
--map/--clusters, gives the per-tile curve (no propagation) and the summary says so. The greedy oracle (d) is an upper
bound only within the chosen propagation model: it never takes a zero- or negative-net decision, so under cluster or
pile propagation it can stop with errors left that a per-tile curve would remove. After each decision the output is re-scored with tools/tx_bench.py
position_errors (insertions are not position-level, so err_true here = wrong-or-deleted / scored positions).

Showable tiles: positions whose aligned truth row is scored (and not flagged with --exclude-flagged; the flagged rows
are then also dropped from the score, tx_bench drop_flagged). Orderings:
  a  doubt   tx_doubt signal count descending (the sorter feed today; --signals, ties in line/pos order)
  b  size    atlas cluster size (in the unit) descending, one representative per cluster first (the tile nearest
             its centroid, clusters.tsv `dist`), then the remaining tiles by cluster size, nearest first
  c  random  --seeds random orders (mean and min-max band)
  d  oracle  greedy by net errors removed (fixed - broken) per decision, an upper bound; stops when no decision
             has a positive net (the curve is flat after that)
Output TSV: ordering, k, err_true, wrong, scored, fixed, broken (fixed/broken cumulative vs the base, position-paired);
for random, one row per k with the mean and the band (err_lo, err_hi). The summary gives decisions-to-2% per ordering
("not reached by k=KMAX") and the errors removed by the first 10 and 20 decisions.

Scope: a measurement of the sorter's value under a perfect owner; a real owner is one strong reader, not truth
(TRANSCRIPTION.md), so these are upper bounds per ordering. Read-free: no image, no reader.
Exit 0 on a clean run, 2 on bad input.
"""
import argparse, csv, json, os, random, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402


def read_tsv(p):
    return tx_bench.read_tsv(p)


def load_base(path, lines):
    rows = [r for r in read_tsv(path) if r['line'] in lines]
    by = defaultdict(list)
    for r in rows:
        by[r['line']].append((float(r['pos']), r['pos'], r['sign'].strip()))
    return {ln: [(p, s) for _, p, s in sorted(v)] for ln, v in by.items()}


def to_out_lines(state, order):
    return {ln: [state[(ln, p)] for p in ps] for ln, ps in order.items()}


def oracle_rows(truth_rows, base):
    """{(line, pos_of_line_read): truth row} through tx_bench's alignment of the base read."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    m = {}
    for ln, rows in by_line.items():
        if ln not in base:
            continue
        rows.sort(key=lambda r: float(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        signs = [s for _, s in base[ln]]
        j = 0
        for ri, osg in tx_bench.align(ref, ts, signs):
            if osg is None:
                continue
            if ri is not None:
                m[(ln, base[ln][j][0])] = rows[ri]
            j += 1
    return m


def true_sign(read, row):
    ts = set(filter(None, row['truth'].split('|')))
    if read in ts:
        return read
    if row['ref_sign'] in ts:
        return row['ref_sign']
    return sorted(ts)[0]


class Sim:
    def __init__(self, truth_rows, base, cluster_of, mode='cluster'):
        self.truth, self.base, self.cluster_of, self.mode = truth_rows, base, cluster_of, mode
        self.order = {ln: [p for p, _ in v] for ln, v in base.items()}
        self.base_state = {(ln, p): s for ln, v in base.items() for p, s in v}
        self.e0 = tx_bench.position_errors(truth_rows, to_out_lines(self.base_state, self.order))
        self.members = defaultdict(list)
        for k, c in cluster_of.items():
            self.members[c].append(k)

    def reset(self):
        self.state = dict(self.base_state)
        self.decided, self.pinned = set(), set()

    def moves(self, k, s):
        """The (key, new sign) pairs a decision on tile k with true sign s makes."""
        c = self.group(k)
        if c is None or c in self.decided:
            return [(k, s)]
        return [(m, s) for m in self.members[c[0]] if m == k or (m not in self.pinned and self.group(m) == c)]

    def group(self, k):
        """The unit a decision propagates over: the atlas cluster, or (pile mode) the cluster x the current sign."""
        c = self.cluster_of.get(k) if self.mode != 'none' else None
        if c is None:
            return None
        return (c, self.state[k] if self.mode == 'pile' else None)

    def apply(self, k, s):
        c = self.group(k)
        for m, v in self.moves(k, s):
            self.state[m] = v
        if c is not None:
            self.decided.add(c)
        self.pinned.add(k)

    def score(self):
        e = tx_bench.position_errors(self.truth, to_out_lines(self.state, self.order))
        common = set(e) & set(self.e0)
        return dict(wrong=sum(e.values()), scored=len(e),
                    fixed=sum(1 for q in common if self.e0[q] and not e[q]),
                    broken=sum(1 for q in common if not self.e0[q] and e[q]))


def run_order(sim, tiles, orc, kmax):
    sim.reset()
    rows = [dict(k=0, **sim.score())]
    for i, t in enumerate(tiles[:kmax], 1):
        sim.apply(t, true_sign(sim.state[t], orc[t]))
        rows.append(dict(k=i, **sim.score()))
    return rows


def run_oracle(sim, show, orc, kmax):
    """Greedy upper bound: net = fixed - broken per decision, by direct truth-set membership at the aligned rows."""
    sim.reset()
    rows = [dict(k=0, **sim.score())]

    def ok(key, sign):
        r = orc.get(key)
        return None if r is None else sign in set(filter(None, r['truth'].split('|')))
    for i in range(1, kmax + 1):
        best, bnet = None, 0
        for t in show:
            if t in sim.pinned:
                continue
            s = true_sign(sim.state[t], orc[t])
            net = 0
            for m, v in sim.moves(t, s):
                a, b = ok(m, sim.state[m]), ok(m, v)
                if a is None or a == b:
                    continue
                net += 1 if b else -1
            if net > bnet:
                best, bnet = (t, s), net
        if best is None:
            break
        sim.apply(*best)
        rows.append(dict(k=i, **sim.score()))
    return rows


def err(r):
    return r['wrong'] / r['scored'] if r['scored'] else float('nan')


def to2(rows, kmax, thr=0.02):
    for r in rows:
        if err(r) <= thr:
            return r['k']
    return 'not reached by k=%d' % kmax


def at(rows, k):
    """Errors removed (base wrong - wrong) after k decisions (last row if the curve stopped earlier)."""
    r = rows[min(k, len(rows) - 1)]
    return rows[0]['wrong'] - r['wrong']


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument('--truth', required=True)
    ap.add_argument('--base', required=True, help='the line read L (line, pos, sign)')
    ap.add_argument('--lines', required=True, nargs='+', help='TSV(s) whose `line` column names the unit lines (unit labels files)')
    ap.add_argument('--map', help='box<->position map (sid, line, pos, op); truth column never read')
    ap.add_argument('--clusters', help='atlas clusters.tsv (id, kind, cluster, dist)')
    ap.add_argument('--signals', nargs='*', default=[], help='tx_doubt signals TSV(s) for ordering a')
    ap.add_argument('--propagate', choices=('cluster', 'pile', 'none'), default='cluster',
                    help='cluster (PREREG X6, default): the first decision sets every undecided tile of the atlas '
                         'cluster; pile: only the cluster tiles whose current sign equals the shown tile\'s (the '
                         'sorter pile x cluster); none: per tile')
    ap.add_argument('--kmax', type=int, default=200)
    ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--exclude-flagged', action='store_true')
    ap.add_argument('--out', required=True)
    ap.add_argument('--json')
    a = ap.parse_args(argv)

    lines = {r['line'] for p in a.lines for r in read_tsv(p)}
    base = load_base(a.base, lines)
    if not base:
        print('tx_sorter_curve: no base lines in the unit', file=sys.stderr)
        return 2
    truth = [r for r in read_tsv(a.truth) if r['line'] in lines]
    if a.exclude_flagged:
        truth = tx_bench.drop_flagged(truth)
    orc = oracle_rows(truth, base)
    keys = {(ln, p) for ln, v in base.items() for p, _ in v}

    cluster_of, dist = {}, {}
    if a.map and a.clusters:
        cl = {r['id']: r for r in read_tsv(a.clusters) if r.get('kind', 'sign') == 'sign'}
        with open(a.map, newline='') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                k = (r['line'], r['pos'])
                if r['op'] != '1:1' or k not in keys or r['sid'] not in cl:
                    continue
                cluster_of[k] = cl[r['sid']]['cluster']
                dist[k] = float(cl[r['sid']].get('dist') or 0)
    propagation = bool(cluster_of)

    show = sorted((k for k, r in orc.items() if r['status'] == 'scored'),
                  key=lambda k: (k[0], float(k[1])))
    if a.propagate == 'none':
        cluster_of = {}
    propagation = bool(cluster_of)
    sim = Sim(truth, base, cluster_of, a.propagate)
    curves = {}

    if a.signals:
        n = {}
        for p in a.signals:
            for r in read_tsv(p):
                n[(r['line'], r['pos'])] = int(r['n_signals'])
        curves['a_doubt'] = run_order(sim, sorted(show, key=lambda k: -n.get(k, 0)), orc, a.kmax)
    if propagation:
        size = defaultdict(int)
        for k, c in cluster_of.items():
            size[c] += 1
        inc = [k for k in show if k in cluster_of]
        rep = {}
        for k in sorted(inc, key=lambda k: dist[k]):
            rep.setdefault(cluster_of[k], k)
        first = sorted(rep.values(), key=lambda k: (-size[cluster_of[k]], dist[k]))
        rest = sorted((k for k in show if k not in set(first)),
                      key=lambda k: (-size.get(cluster_of.get(k), 0), dist.get(k, 1e9)))
        curves['b_size'] = run_order(sim, first + rest, orc, a.kmax)
    rnd = []
    for s in range(a.seeds):
        o = list(show)
        random.Random(s).shuffle(o)
        rnd.append(run_order(sim, o, orc, a.kmax))
    curves['d_oracle'] = run_oracle(sim, show, orc, a.kmax)

    os.makedirs(os.path.dirname(a.out) or '.', exist_ok=True)
    with open(a.out, 'w') as f:
        f.write('# tools/tx_sorter_curve.py: truth=%s base=%s lines=%s propagation=%s exclude_flagged=%s\n'
                % (a.truth, a.base, a.lines, a.propagate if propagation else 'none (per tile)', a.exclude_flagged))
        f.write('ordering\tk\terr_true\twrong\tscored\tfixed\tbroken\terr_lo\terr_hi\n')
        for name, rows in curves.items():
            for r in rows:
                f.write('%s\t%d\t%.4f\t%d\t%d\t%d\t%d\t\t\n' % (name, r['k'], err(r), r['wrong'], r['scored'],
                                                              r['fixed'], r['broken']))
        if rnd:
            for k in range(len(rnd[0])):
                es = [err(c[k]) for c in rnd]
                m = lambda f: sum(c[k][f] for c in rnd) / len(rnd)
                f.write('c_random\t%d\t%.4f\t%.1f\t%d\t%.1f\t%.1f\t%.4f\t%.4f\n' % (
                    k, sum(es) / len(es), m('wrong'), rnd[0][k]['scored'], m('fixed'), m('broken'), min(es), max(es)))
    summ = dict(propagation=a.propagate if propagation else 'none (per tile)', showable=len(show),
                tiles_in_clusters=len(cluster_of), clusters=len(set(cluster_of.values())))
    sim.reset()
    s0 = sim.score()
    summ.update(base_wrong=s0['wrong'], scored=s0['scored'], base_err=round(err(s0), 4), orderings={})
    for name, rows in curves.items():
        summ['orderings'][name] = dict(to_2pct=to2(rows, a.kmax), removed_10=at(rows, 10), removed_20=at(rows, 20),
                                       err_10=round(err(rows[min(10, len(rows) - 1)]), 4),
                                       err_20=round(err(rows[min(20, len(rows) - 1)]), 4),
                                       broken_20=rows[min(20, len(rows) - 1)]['broken'], steps=len(rows) - 1)
    if rnd:
        t2 = [to2(c, a.kmax) for c in rnd]
        summ['orderings']['c_random'] = dict(
            to_2pct=t2, removed_10_mean=sum(at(c, 10) for c in rnd) / len(rnd),
            removed_20_mean=sum(at(c, 20) for c in rnd) / len(rnd),
            removed_20_band=[min(at(c, 20) for c in rnd), max(at(c, 20) for c in rnd)])
    print(json.dumps(summ, indent=1))
    if a.json:
        json.dump(summ, open(a.json, 'w'), indent=1)
    return 0


if __name__ == '__main__':
    sys.exit(main())

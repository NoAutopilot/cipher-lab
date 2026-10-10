#!/usr/bin/env python3
"""MARKS-DEV2 scoring (PREREG-txeng2-21 MARKS-DEV2 steps 3-4; TXE2-MARKS, 10 Oct 2026). Committed BEFORE it is run.

The ONLY step that opens the dev2 truth (benchmark-tx/vivonne1573-f102r-dev2.truth.tsv, via BENCHMARK-TX.tsv) and passZ_dv1
(benchmark-tx/outputs/vivonne1573-f102r-dev/passZ_dv1.tsv). Neither is printed: the script prints counts and rates only, and
writes result.json (counts, rates, per-line box/position counts; no sign, no value, no truth content).

Index space: a line's truth rows sorted by float(pos), 0-based index; a candidate's position (rule.py) is its 0-based rank
among the line's units. Fixed here before scoring:
 (3) ':' truth positions = rows whose ref_sign is ':' (any status). A candidate matches a ':' position on the same line at
     |index difference| <= 1 (the lift step's "within one position"), one-to-one, exact matches taken first, then +-1, left to
     right. GATING recall/precision = the +-1 figure; the exact (0) figure is reported beside it. recall = matched ':'
     positions / ':' positions; precision = matched candidates / candidates.
 (4) unflagged positions = rows with status 'scored' and no verifier flag (tx_bench.drop_flagged). passZ_dv1's errors =
     position errors at those positions (tx_bench.position_errors on drop_flagged rows, missing='skip', the default G=0.75
     alignment) + insertions (tx_bench.align, ref index None), an insertion located at the index of the next aligned truth
     row on its line (the previous one at a line end). The label map: none, unless the no-map counts fail to reproduce the
     registered 679 / 43 / 41 and the S2-NOTE norm_map (benchmark-tx/txeng2/s2note/norm_map.tsv, the classify.py map)
     reproduces them -- then that map; both count triples are reported either way.
     near(c) = at or within one index of a candidate on the same line. lift = (errors near / errors) / (unflagged positions
     near / unflagged positions). Null: 200 shuffles (seed 20261010): each line's position errors redrawn without
     replacement from that line's unflagged indices, each insertion redrawn uniformly from them; null lift by the same
     formula; p95 (numpy linear quantile) and max.
Gate (declared): "candidate instrument" iff recall >= 0.70 AND precision >= 0.50 (+-1 figure) AND lift > null p95;
otherwise "FAIL read-free".
  python3 benchmark-tx/txeng2/marks/score.py"""
import csv, json, os, sys, random, hashlib
from collections import defaultdict
import numpy as np

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), '../../..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import tx_bench as T  # noqa: E402

M = os.path.join(ROOT, 'benchmark-tx/txeng2/marks')
ITEM = 'vivonne1573-f102r-dev2'
PASS = os.path.join(ROOT, 'benchmark-tx/outputs/vivonne1573-f102r-dev/passZ_dv1.tsv')
NORM = os.path.join(ROOT, 'benchmark-tx/txeng2/s2note/norm_map.tsv')
REG = (679, 43, 41)


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def truth_path():
    for r in T.read_tsv(os.path.join(ROOT, 'BENCHMARK-TX.tsv')):
        if r.get('item') == ITEM:
            return os.path.join(ROOT, r['truth'])
    sys.exit('item not in BENCHMARK-TX.tsv')


def by_line(rows):
    d = defaultdict(list)
    for r in rows:
        d[r['line']].append(r)
    for v in d.values():
        v.sort(key=lambda r: float(r['pos']))
    return d


def errors(truth, out, lm):
    if lm:
        truth = T.map_truth([dict(r) for r in truth], lm)
        out = {k: [lm.get(s, s) for s in v] for k, v in out.items()}
    tf = T.drop_flagged(truth)
    L = by_line(tf)
    idx = {(ln, r['pos']): i for ln, rows in L.items() for i, r in enumerate(rows)}
    unfl = {ln: [i for i, r in enumerate(rows) if r['status'] == 'scored'] for ln, rows in L.items()}
    pe = T.position_errors(tf, out, missing='skip')
    perr = [(k[0], idx[k]) for k, v in pe.items() if v]
    ins = []
    for ln, rows in L.items():
        if ln not in out:
            continue
        ref = [r['ref_sign'] for r in rows]; ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        path = T.align(ref, ts, out[ln])
        for j, (ri, o) in enumerate(path):
            if ri is None:
                nxt = [p[0] for p in path[j + 1:] if p[0] is not None]
                prv = [p[0] for p in path[:j] if p[0] is not None]
                ins.append((ln, nxt[0] if nxt else (prv[-1] if prv else 0)))
    covered = {ln: v for ln, v in unfl.items() if ln in out}
    return perr, ins, covered, (sum(len(v) for v in covered.values()), len(perr), len(ins))


def main():
    tp = truth_path()
    truth = T.read_tsv(tp)                      # dev opening 1 (this script only)
    out = T.load_output([PASS])
    L = by_line(truth)
    cands = list(csv.DictReader(open(os.path.join(M, 'candidates.tsv')), delimiter='\t'))
    C = defaultdict(list)
    for c in cands:
        C[c['line']].append(int(c['position']))
    nunits = {c['line']: int(c['n_units']) for c in cands}
    nbox = {}
    for b in csv.DictReader(open(os.path.join(M, 'boxes.tsv')), delimiter='\t'):
        nbox[b['line']] = nbox.get(b['line'], 0) + 1
    # (3) recall / precision
    colon = {ln: [i for i, r in enumerate(rows) if r['ref_sign'] == ':'] for ln, rows in L.items()}
    res = {}
    for tol in (0, 1):
        mt = mc = 0
        for ln in L:
            tpos, cpos = list(colon[ln]), sorted(C.get(ln, []))
            usedt, usedc = set(), set()
            for d in ([0] if tol == 0 else [0, 1]):
                for ci, c in enumerate(cpos):
                    if ci in usedc:
                        continue
                    for ti, t in enumerate(tpos):
                        if ti not in usedt and abs(c - t) == d:
                            usedt.add(ti); usedc.add(ci); break
            mt += len(usedt); mc += len(usedc)
        nt, nc = sum(len(v) for v in colon.values()), len(cands)
        res[tol] = {'colon_positions': nt, 'candidates': nc, 'matched': mt,
                    'recall': round(mt / nt, 4) if nt else None, 'precision': round(mc / nc, 4) if nc else None}
    # (4) lift
    trip = {}
    E = {}
    for name, lm in (('no_map', None), ('norm_map', T.load_label_map(NORM))):
        perr, ins, covered, t3 = errors(truth, out, lm)
        trip[name] = t3; E[name] = (perr, ins, covered)
    use = 'no_map' if trip['no_map'] == REG or trip['norm_map'] != REG else 'norm_map'
    perr, ins, covered = E[use]

    def near(ln, i):
        return any(abs(i - c) <= 1 for c in C.get(ln, []))
    allpos = [(ln, i) for ln, v in covered.items() for i in v]
    base = sum(near(*p) for p in allpos) / len(allpos)
    errs = perr + ins
    share = sum(near(*e) for e in errs) / len(errs)
    lift = share / base if base else None
    rng = random.Random(20261010)
    pl, il = defaultdict(int), defaultdict(int)
    for ln, _ in perr:
        pl[ln] += 1
    for ln, _ in ins:
        il[ln] += 1
    nulls = []
    for _ in range(200):
        k = 0
        for ln, v in covered.items():
            draw = rng.sample(v, min(pl[ln], len(v))) + [rng.choice(v) for _ in range(il[ln])] if v else []
            k += sum(near(ln, i) for i in draw)
        nulls.append((k / len(errs)) / base if base else 0.0)
    p95, mx = (float(np.quantile(nulls, 0.95)), float(max(nulls))) if base else (None, None)
    r1 = res[1]
    ok = (r1['recall'] or 0) >= 0.70 and (r1['precision'] or 0) >= 0.50 and lift is not None and lift > p95
    verdict = 'candidate instrument' if ok else 'FAIL read-free'
    lines = sorted(L)
    result = {'item': ITEM, 'truth_sha256': sha(tp), 'pass_sha256': sha(PASS),
              'candidates_sha256': sha(os.path.join(M, 'candidates.tsv')),
              'recall_precision_pm1': res[1], 'recall_precision_exact': res[0],
              'count_triples': {k: dict(zip(('unflagged', 'position_errors', 'insertions'), v)) for k, v in trip.items()},
              'registered_triple': dict(zip(('unflagged', 'position_errors', 'insertions'), REG)), 'map_used': use,
              'errors': len(errs), 'errors_near': sum(near(*e) for e in errs), 'share_errors_near': round(share, 4),
              'unflagged_near': sum(near(*p) for p in allpos), 'share_positions_near': round(base, 4),
              'lift': round(lift, 4) if lift is not None else None,
              'null': {'n': 200, 'seed': 20261010, 'p95': round(p95, 4) if p95 is not None else None,
                       'max': round(mx, 4) if mx is not None else None, 'mean': round(float(np.mean(nulls)), 4)},
              'per_line': [{'line': ln, 'positions': len(L[ln]), 'boxes': nbox.get(ln, 0), 'units': nunits.get(ln),
                            'candidates': len(C.get(ln, []))} for ln in lines],
              'verdict': verdict, 'openings_eval_truth': 0, 'dev_openings': 1}
    json.dump(result, open(os.path.join(M, 'result.json'), 'w'), indent=1)
    print('candidates', len(cands), "':' positions", r1['colon_positions'])
    print('recall/precision +-1: %s / %s | exact: %s / %s' % (r1['recall'], r1['precision'], res[0]['recall'], res[0]['precision']))
    print('triples', trip, 'map used', use)
    print('lift', result['lift'], 'null p95', result['null']['p95'], 'max', result['null']['max'])
    print('verdict:', verdict)


if __name__ == '__main__':
    main()

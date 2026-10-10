#!/usr/bin/env python3
"""Score a transcription pipeline output against the known-answer benchmark BENCHMARK-TX.tsv (TRANSCRIPTION.md step 8).

    python3 tools/tx_bench.py OUTPUT.tsv [OUTPUT2.tsv ...] --bench BENCHMARK-TX.tsv [--item ID] [--top 8] [--json]

OUTPUT.tsv: one row per sign, columns `line`, `pos`, `sign` (also accepted: `passage` for line, `sign_id` for sign;
`--line-prefix f178r` turns a bare `L01` into `f178r_L01`). Lines are matched to the benchmark item by line id; an
item is scored only over the truth lines the output covers (missing lines are reported, not scored).

BENCHMARK-TX.tsv: one row per item; its `truth` column names a truth TSV with columns line, pos, ref_sign, truth,
plain, status. `truth` is one sign or a `|`-set (homophones the known answer cannot tell apart: a sign in the set is
right). Only `status == scored` rows count; the others are the excluded-and-counted ambiguous positions.

Per line the output is aligned to the reference sign sequence by edit distance (substitution free when the output
sign equals ref_sign or lies in the truth set, else 1; insertion and deletion 0.75, so a dropped or extra sign
shifts the alignment instead of turning the rest of the line into misreads). A scored position is WRONG when its
aligned output sign is outside the truth set or it was deleted; output signs inserted against the reference add to
the error numerator. err_true = (wrong + inserted) / scored, with a Wilson 95% interval, per item, per split
(dev/eval) and per truth value, plus the top confusions (truth value <- read sign).

Scope: catches misreads, missed signs and extra signs on positions where a known plain text forces the sign.
It does NOT see a homophone swap (two signs of one value), nor errors on excluded positions, nor a segmentation
error already in the reference transcription; err_true is therefore a lower bound on true sign error.
--label-map MAP.tsv (columns from, to): rename sign labels before scoring, in the output, the reference sign and every
truth-set member alike, so a reader that was given a coarser label inventory than the reconciler (one label for two
glyphs the reconciler later split) is scored on glyph identity, not on notation (CLAUDE.md rule 3, PX-BRODEC). Report
the mapped and unmapped scores side by side (TXB2, 3 Oct 2026).
--paired BASE.tsv (TX-VIEWS, 4 Oct 2026): also score BASE and compare each OUTPUT with it position by position on the same
scored truth signs: fixed = wrong (or deleted) in BASE and right in OUTPUT, broken = the reverse, with a two-sided exact
sign test p on fixed vs broken (insertions are not position-level and are left out of the paired count; they stay in
err_true). A change is adopted on the paired count, never on two overlapping Wilson intervals
(research/TRANSCRIPTION-PRACTICE-2026-10-04.md, Top 5 preamble). position_errors() is the shared per-position scorer
(tools/reconcile_passes.py --err-truth uses it for pairwise error correlation).
--exclude-flagged (TX-TRUTH-VERIFY, 9 Oct 2026): a truth TSV may carry a `flag` column set by a verifier (a truth-doubtful
position: alignment-, clerk- or key-doubtful; `corrected:<class>` means the truth was corrected and stays scored). With the
switch each item prints both figures side by side, as measured first and flagged excluded second (flagged rows are counted
as excluded, never dropped silently); without it the flag column is ignored. Never report the second figure alone.
Two-rate decomposition (TOOL-2RATE, 10 Oct 2026, TX-RED F48): under --exclude-flagged the flagged-excluded err_true keeps
ALL line insertions in its numerator over unflagged positions only, so it mixes two rates. The same line therefore appends
`position errors P/U = r` (wrong + deleted at unflagged positions over unflagged positions) and `insertions I / read R = r`
(insertions over the output's sign count on the covered truth lines); --json carries them in flagged_excluded as
position_errors, position_rate, inserted, read and insertion_rate. No existing number or field changes.
Exit 0 always on a clean score; exit 2 on bad input.
"""
import argparse, csv, json, math, os, sys
from collections import Counter, defaultdict


def wilson(k, n, z=1.96):
    if n == 0:
        return (0.0, 0.0)
    p = k / n
    d = 1 + z * z / n
    c = p + z * z / (2 * n)
    h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return (max(0.0, (c - h) / d), min(1.0, (c + h) / d))


def read_tsv(path):
    with open(path, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def load_output(paths, prefix=None):
    lines = defaultdict(list)
    for p in paths:
        for r in read_tsv(p):
            ln = r.get('line') or r.get('passage')
            sg = r.get('sign') if r.get('sign') is not None else r.get('sign_id')
            if ln is None or sg is None or r.get('pos') is None:
                sys.exit('tx_bench: %s needs line/passage, pos, sign/sign_id columns' % p)
            if prefix and '_' not in ln:
                ln = '%s_%s' % (prefix, ln)
            lines[ln].append((float(r['pos']), sg.strip()))
    return {k: [s for _, s in sorted(v, key=lambda t: t[0])] for k, v in lines.items()}


def align(ref, truthsets, out):
    """Edit-distance alignment; returns list of (ref_index or None, out_sign or None)."""
    n, m = len(ref), len(out)
    G = 0.75  # indel cost below a substitution, so a dropped or extra sign is not smeared into a run of misreads
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i * G
    for j in range(1, m + 1):
        D[0][j] = j * G

    def sub(i, j):
        return 0 if (out[j] == ref[i] or out[j] in truthsets[i]) else 1
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            D[i][j] = min(D[i - 1][j - 1] + sub(i - 1, j - 1), D[i - 1][j] + G, D[i][j - 1] + G)
    i, j, path = n, m, []
    while i > 0 or j > 0:
        if i > 0 and j > 0 and abs(D[i][j] - (D[i - 1][j - 1] + sub(i - 1, j - 1))) < 1e-9:
            path.append((i - 1, out[j - 1])); i -= 1; j -= 1
        elif i > 0 and abs(D[i][j] - (D[i - 1][j] + G)) < 1e-9:
            path.append((i - 1, None)); i -= 1
        else:
            path.append((None, out[j - 1])); j -= 1
    return path[::-1]


def load_label_map(path):
    return {r['from'].strip(): r['to'].strip() for r in read_tsv(path)}


def map_truth(rows, lm):
    out = []
    for r in rows:
        r = dict(r)
        r['ref_sign'] = lm.get(r['ref_sign'], r['ref_sign'])
        r['truth'] = '|'.join(sorted({lm.get(t, t) for t in r['truth'].split('|') if t}))
        out.append(r)
    return out


def score_item(truth_rows, out_lines):
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    res = {'scored': 0, 'wrong': 0, 'deleted': 0, 'inserted': 0, 'excluded': 0, 'read': 0, 'lines_missing': [],
           'per_value': defaultdict(lambda: [0, 0]), 'confusions': Counter()}
    for ln, rows in by_line.items():
        rows.sort(key=lambda r: float(r['pos']))
        if ln not in out_lines:
            res['lines_missing'].append(ln)
            continue
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        res['read'] += len(out_lines[ln])
        prev_scored = False
        for ri, osg in align(ref, ts, out_lines[ln]):
            if ri is None:
                # an output sign with no reference position (anywhere on a covered line)
                res['inserted'] += 1
                continue
            r = rows[ri]
            if r['status'] != 'scored':
                res['excluded'] += 1
                continue
            res['scored'] += 1
            val = r['plain']
            res['per_value'][val][1] += 1
            if osg is None:
                res['deleted'] += 1; res['per_value'][val][0] += 1
                res['confusions'][(val, '<deleted>')] += 1
            elif osg not in ts[ri]:
                res['wrong'] += 1; res['per_value'][val][0] += 1
                res['confusions'][(val, osg)] += 1
    return res


def is_flagged(r):
    f = (r.get('flag') or '').strip()
    return bool(f) and not f.startswith('corrected')


def drop_flagged(rows):
    out = []
    for r in rows:
        if r['status'] == 'scored' and is_flagged(r):
            r = dict(r); r['status'] = 'excluded:flagged'
        out.append(r)
    return out


def position_errors(truth_rows, out_lines):
    """{(line, pos): True if wrong or deleted} over the scored truth positions of lines the output covers."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    errs = {}
    for ln, rows in by_line.items():
        if ln not in out_lines:
            continue
        rows.sort(key=lambda r: float(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        for ri, osg in align(ref, ts, out_lines[ln]):
            if ri is None or rows[ri]['status'] != 'scored':
                continue
            errs[(ln, rows[ri]['pos'])] = osg is None or osg not in ts[ri]
    return errs


def sign_test(fixed, broken):
    """Two-sided exact binomial sign test p for fixed vs broken (p = 0.5)."""
    n, k = fixed + broken, min(fixed, broken)
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def paired(truth_rows, base_lines, out_lines):
    eb, eo = position_errors(truth_rows, base_lines), position_errors(truth_rows, out_lines)
    common = set(eb) & set(eo)
    fixed = sum(1 for k in common if eb[k] and not eo[k])
    broken = sum(1 for k in common if not eb[k] and eo[k])
    return dict(n=len(common), fixed=fixed, broken=broken, p=round(sign_test(fixed, broken), 4),
                base_wrong=sum(eb[k] for k in common), out_wrong=sum(eo[k] for k in common))


def summarise(res):
    k = res['wrong'] + res['deleted'] + res['inserted']
    n = res['scored']
    lo, hi = wilson(min(k, n), n)
    return k, n, (k / n if n else float('nan')), lo, hi


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('outputs', nargs='+')
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv')
    ap.add_argument('--item', action='append', help='score only these item ids')
    ap.add_argument('--line-prefix')
    ap.add_argument('--top', type=int, default=8)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--label-map', help='TSV from/to: rename labels in output, reference and truth before scoring')
    ap.add_argument('--exclude-flagged', action='store_true',
                    help='also score with verifier-flagged truth rows excluded; prints both figures side by side')
    ap.add_argument('--paired', metavar='BASE.tsv', help='paired fixed/broken count of each OUTPUT against BASE (sign test)')
    a = ap.parse_args(argv)
    if a.paired:
        rc = 0
        for o in a.outputs:
            rc |= main([x for x in (argv or sys.argv[1:]) if x not in a.outputs and x != a.paired and x != '--paired']
                       + [o]) or 0
            base_lines, out_lines = load_output([a.paired], a.line_prefix), load_output([o], a.line_prefix)
            lm = load_label_map(a.label_map) if a.label_map else None
            if lm:
                base_lines = {k: [lm.get(x, x) for x in v] for k, v in base_lines.items()}
                out_lines = {k: [lm.get(x, x) for x in v] for k, v in out_lines.items()}
            base = os.path.dirname(os.path.abspath(a.bench))
            for item in read_tsv(a.bench):
                if a.item and item['item'] not in a.item:
                    continue
                truth = read_tsv(os.path.join(base, item['truth']))
                if lm:
                    truth = map_truth(truth, lm)
                if not any(r['line'] in out_lines for r in truth):
                    continue
                pr = paired(truth, base_lines, out_lines)
                print('paired %s vs %s on %s: %d common scored signs; base wrong %d, output wrong %d; fixed %d, broken %d; '
                      'sign test p = %.4f' % (os.path.basename(o), os.path.basename(a.paired), item['item'], pr['n'],
                                              pr['base_wrong'], pr['out_wrong'], pr['fixed'], pr['broken'], pr['p']))
        return rc
    if not os.path.exists(a.bench):
        print('tx_bench: no bench file %s' % a.bench, file=sys.stderr); return 2
    base = os.path.dirname(os.path.abspath(a.bench))
    out_lines = load_output(a.outputs, a.line_prefix)
    lm = load_label_map(a.label_map) if a.label_map else None
    if lm:
        out_lines = {k: [lm.get(x, x) for x in v] for k, v in out_lines.items()}
    report, splits = [], defaultdict(lambda: [0, 0])
    for item in read_tsv(a.bench):
        if a.item and item['item'] not in a.item:
            continue
        tp = os.path.join(base, item['truth'])
        truth = read_tsv(tp)
        if lm:
            truth = map_truth(truth, lm)
        if not any(r['line'] in out_lines for r in truth):
            continue
        res = score_item(truth, out_lines)
        k, n, e, lo, hi = summarise(res)
        splits[item['split']][0] += k; splits[item['split']][1] += n
        report.append({'item': item['item'], 'split': item['split'], 'err_true': round(e, 4),
                       'wilson95': [round(lo, 4), round(hi, 4)], 'errors': k, 'scored': n,
                       'wrong': res['wrong'], 'deleted': res['deleted'], 'inserted': res['inserted'],
                       'excluded': res['excluded'], 'lines_missing': len(res['lines_missing']),
                       'per_value': {v: c for v, c in sorted(res['per_value'].items(), key=lambda t: -t[1][0]) if c[0]},
                       'top_confusions': ['%s<-%s x%d' % (t, s, c) for (t, s), c in res['confusions'].most_common(a.top)]})
        if a.exclude_flagged:
            fres = score_item(drop_flagged(truth), out_lines)
            fk, fn, fe, flo, fhi = summarise(fres)
            report[-1]['flagged_excluded'] = {'err_true': round(fe, 4), 'wilson95': [round(flo, 4), round(fhi, 4)],
                                              'errors': fk, 'scored': fn, 'flagged': n - fn}
            pe = fres['wrong'] + fres['deleted']
            report[-1]['flagged_excluded'].update(
                position_errors=pe, position_rate=round(pe / fn, 4) if fn else None, inserted=fres['inserted'],
                read=fres['read'], insertion_rate=round(fres['inserted'] / fres['read'], 4) if fres['read'] else None)
    if not report:
        print('tx_bench: the output covers no benchmark line', file=sys.stderr); return 2
    split_rows = {}
    for s, (k, n) in splits.items():
        lo, hi = wilson(min(k, n), n)
        split_rows[s] = {'err_true': round(k / n, 4) if n else None, 'wilson95': [round(lo, 4), round(hi, 4)],
                         'errors': k, 'scored': n}
    if a.json:
        print(json.dumps({'items': report, 'splits': split_rows}, indent=1))
        return 0
    for r in report:
        print('%s [%s] err_true %.3f (%d/%d) 95%% %.3f-%.3f | wrong %d deleted %d inserted %d | excluded %d | lines missing %d'
              % (r['item'], r['split'], r['err_true'], r['errors'], r['scored'], r['wilson95'][0], r['wilson95'][1],
                 r['wrong'], r['deleted'], r['inserted'], r['excluded'], r['lines_missing']))
        if 'flagged_excluded' in r:
            f = r['flagged_excluded']
            print('  as measured %.3f (%d/%d) | flagged excluded %.3f (%d/%d) 95%% %.3f-%.3f [%d flagged]'
                  % (r['err_true'], r['errors'], r['scored'], f['err_true'], f['errors'], f['scored'],
                     f['wilson95'][0], f['wilson95'][1], f['flagged'])
                  + ' | position errors %d/%d = %.3f | insertions %d / read %d = %.3f'
                  % (f['position_errors'], f['scored'], f['position_rate'] or 0.0, f['inserted'], f['read'],
                     f['insertion_rate'] or 0.0))
        if r['top_confusions']:
            print('  top confusions (truth value <- read):', ', '.join(r['top_confusions']))
    for s, r in sorted(split_rows.items()):
        print('split %s: err_true %.3f (%d/%d) 95%% %.3f-%.3f' % (s, r['err_true'], r['errors'], r['scored'],
                                                                 r['wilson95'][0], r['wilson95'][1]))
    return 0


if __name__ == '__main__':
    sys.exit(main())

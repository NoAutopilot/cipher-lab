#!/usr/bin/env python3
"""Score a transcription pipeline output against the known-answer benchmark BENCHMARK-TX.tsv (TRANSCRIPTION.md step 8).

    python3 tools/tx_bench.py OUTPUT.tsv [OUTPUT2.tsv ...] --bench BENCHMARK-TX.tsv [--item ID] [--top 8] [--json]

OUTPUT.tsv: one row per sign, columns `line`, `pos`, `sign` (also accepted: `passage` for line, `sign_id` for sign;
`--line-prefix f178r` turns a bare `L01` into `f178r_L01`). Lines are matched to the benchmark item by line id; an
item is scored over ALL its truth lines (a missing line's scored positions are deleted; an unknown output line id fails
validation) -- see "Scorer fix" below; --coverage-diagnostic / --legacy keep the old partial coverage.

BENCHMARK-TX.tsv: one row per item; its `truth` column names a truth TSV with columns line, pos, ref_sign, truth,
plain, status. `truth` is one sign or a `|`-set (homophones the known answer cannot tell apart: a sign in the set is
right). Only `status == scored` rows count; the others are the excluded-and-counted ambiguous positions.

Per line the output is aligned to the reference sign sequence by edit distance (substitution free when the output
sign equals ref_sign or lies in the truth set, else 1; insertion and deletion 0.75, so a dropped or extra sign
shifts the alignment instead of turning the rest of the line into misreads). A scored position is WRONG when its
aligned output sign is outside the truth set or it was deleted; output signs inserted against the reference add to
the error numerator. err_true = (wrong + inserted) / scored (with a Wilson 95% interval in --legacy only), per item, per split
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
Scorer fix (TOOL-SCORER-FIX, PREREG-txeng2-17, 10 Oct 2026; the outside review research/SO-TX-TRANSCRIPTION-2026-10-10.md).
The default is now the corrected scorer; `--legacy` runs the pre-fix code path unchanged and reproduces every figure on
file to the digit (tests: benchmark-tx/txeng2/s2score/tx_bench_S2.txt, txeng2/viv102base/tx_bench_out.txt).
(1) Fixed manifest: an item is selected as before (the output touches one of its lines), and then EVERY truth line of
    the item is scored -- a line absent from the output counts each of its scored positions as deleted (confusion
    `<line missing>`); an output (or --paired base) line id that is not in any selected item's truth fails validation,
    exit 2. `--coverage-diagnostic` keeps the old partial coverage (missing lines listed, not scored; unknown ids
    ignored) under its own label.
(2) --paired: per mask (as measured; and flagged excluded under --exclude-flagged -- the SAME rows as the rate), the
    headline is per-line edit totals (S+D+I under unit-cost Levenshtein), paired by line: lines improved / worsened /
    tied with an exact sign test. The sign-level position McNemar (fixed/broken, 0.75-indel alignment) is printed
    beside it, no longer the headline. So (3) an insertion repair counts.
(4) --exclude-flagged means truth-verifier flags (the truth TSV's `flag` column) ONLY. Reader abstention tokens
    (UNKNOWN, NONE, any token ending in `?`) never match (they are wrong in the full-output measure); `accepted-token
    error` (wrong among non-abstaining reads of scored positions) and `coverage` (non-abstaining reads / scored
    positions) are printed on their own line.
(5) Standard SER = (S+D+I)/N under unit-cost Levenshtein (indel 1) is printed beside err_true from the 0.75-indel
    alignment; N = scored positions of the mask on complete reference lines (excluded positions align, uncharged). When
    several --paired outputs are scored and the two measures order any pair of files differently, a one-line
    `ranking sensitivity` note says so.
(6) --strict also scores exact ref_sign match only (visual identity), beside the value-compatible truth-set score.
(7) No Wilson interval is printed on a rate that carries insertions (any new-mode rate); --ci adds a 1,000-resample
    line-level bootstrap of standard SER (seed 20261010), and under --paired of the SER difference (output - base),
    conditional on the item's lines -- it says nothing about other hands.
(8) Per-item reporting as before; a macro mean (unweighted over items) when several items are scored.
Exit 0 on a clean score; exit 2 on bad input or a validation failure.
"""
import argparse, csv, json, math, os, random, sys
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


ABSTAIN = {'UNKNOWN', 'NONE'}


def is_abstention(s):
    """A reader abstention token: UNKNOWN, NONE (any case) or anything ending in '?'."""
    return s.upper() in ABSTAIN or s.endswith('?')


def align(ref, truthsets, out, G=0.75, strict=False, abstain=False):
    """Edit-distance alignment; returns list of (ref_index or None, out_sign or None).
    G: indel cost (0.75 legacy/default figure, 1.0 standard SER). strict: match ref_sign only. abstain: an abstention
    token never matches."""
    n, m = len(ref), len(out)
    # G = 0.75: indel cost below a substitution, so a dropped or extra sign is not smeared into a run of misreads
    D = [[0.0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        D[i][0] = i * G
    for j in range(1, m + 1):
        D[0][j] = j * G

    def sub(i, j):
        if abstain and is_abstention(out[j]):
            return 1
        if strict:
            return 0 if out[j] == ref[i] else 1
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


def score_item(truth_rows, out_lines, missing='delete', G=0.75, strict=False, abstain=True):
    """Score one item. missing='delete' (fixed manifest: a truth line absent from the output counts every scored
    position as deleted) or 'skip' (legacy / --coverage-diagnostic: listed in lines_missing, not scored). G, strict:
    see align(). abstain: abstention tokens never match (legacy: False). per_line carries N/S/D/I/E per scored line."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    res = {'scored': 0, 'wrong': 0, 'deleted': 0, 'inserted': 0, 'excluded': 0, 'read': 0, 'lines_missing': [],
           'per_value': defaultdict(lambda: [0, 0]), 'confusions': Counter(), 'missing_deleted': 0,
           'abstained': 0, 'accepted': 0, 'accepted_wrong': 0, 'per_line': {}}
    for ln, rows in by_line.items():
        rows.sort(key=lambda r: float(r['pos']))
        if ln not in out_lines:
            res['lines_missing'].append(ln)
            if missing != 'delete':
                continue
            nsc = 0
            for r in rows:
                if r['status'] != 'scored':
                    res['excluded'] += 1
                    continue
                nsc += 1
                res['scored'] += 1; res['deleted'] += 1; res['missing_deleted'] += 1
                res['per_value'][r['plain']][1] += 1; res['per_value'][r['plain']][0] += 1
                res['confusions'][(r['plain'], '<line missing>')] += 1
            res['per_line'][ln] = dict(N=nsc, S=0, D=nsc, I=0, E=nsc)
            continue
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        res['read'] += len(out_lines[ln])
        pl = dict(N=0, S=0, D=0, I=0)
        for ri, osg in align(ref, ts, out_lines[ln], G=G, strict=strict, abstain=abstain):
            if ri is None:
                # an output sign with no reference position (anywhere on a covered line)
                res['inserted'] += 1; pl['I'] += 1
                continue
            r = rows[ri]
            if r['status'] != 'scored':
                res['excluded'] += 1
                continue
            res['scored'] += 1; pl['N'] += 1
            val = r['plain']
            res['per_value'][val][1] += 1
            ab = abstain and osg is not None and is_abstention(osg)
            if osg is not None:
                if ab:
                    res['abstained'] += 1
                else:
                    res['accepted'] += 1
            if osg is None:
                res['deleted'] += 1; res['per_value'][val][0] += 1; pl['D'] += 1
                res['confusions'][(val, '<deleted>')] += 1
            elif ab or (osg != r['ref_sign'] if strict else osg not in ts[ri]):
                res['wrong'] += 1; res['per_value'][val][0] += 1; pl['S'] += 1
                res['confusions'][(val, osg)] += 1
                if not ab:
                    res['accepted_wrong'] += 1
        pl['E'] = pl['S'] + pl['D'] + pl['I']
        res['per_line'][ln] = pl
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


def position_errors(truth_rows, out_lines, missing='skip', abstain=False):
    """{(line, pos): True if wrong or deleted} over the scored truth positions of lines the output covers
    (missing='delete': and of the lines it does not cover, all True)."""
    by_line = defaultdict(list)
    for r in truth_rows:
        by_line[r['line']].append(r)
    errs = {}
    for ln, rows in by_line.items():
        if ln not in out_lines:
            if missing == 'delete':
                for r in rows:
                    if r['status'] == 'scored':
                        errs[(ln, r['pos'])] = True
            continue
        rows.sort(key=lambda r: float(r['pos']))
        ref = [r['ref_sign'] for r in rows]
        ts = [set(filter(None, r['truth'].split('|'))) for r in rows]
        for ri, osg in align(ref, ts, out_lines[ln], abstain=abstain):
            if ri is None or rows[ri]['status'] != 'scored':
                continue
            errs[(ln, rows[ri]['pos'])] = (osg is None or osg not in ts[ri]
                                           or (abstain and is_abstention(osg)))
    return errs


def sign_test(fixed, broken):
    """Two-sided exact binomial sign test p for fixed vs broken (p = 0.5)."""
    n, k = fixed + broken, min(fixed, broken)
    if n == 0:
        return 1.0
    tail = sum(math.comb(n, i) for i in range(k + 1)) / 2 ** n
    return min(1.0, 2 * tail)


def paired_positions(truth_rows, base_lines, out_lines, missing='skip', abstain=False):
    """Sign-level position McNemar (the pre-fix headline; legacy and the 'beside' figure)."""
    eb = position_errors(truth_rows, base_lines, missing, abstain)
    eo = position_errors(truth_rows, out_lines, missing, abstain)
    common = set(eb) & set(eo)
    fixed = sum(1 for k in common if eb[k] and not eo[k])
    broken = sum(1 for k in common if not eb[k] and eo[k])
    return dict(n=len(common), fixed=fixed, broken=broken, p=round(sign_test(fixed, broken), 4),
                base_wrong=sum(eb[k] for k in common), out_wrong=sum(eo[k] for k in common))


def paired(truth_rows, base_lines, out_lines, missing='delete', strict=False):
    """Paired comparison on the given truth rows (pass drop_flagged(rows) for the flagged-excluded mask, as the rate).
    Headline: per-line unit-cost edit totals (S+D+I) paired by line, lines improved / worsened / tied, exact sign test
    line_p. Beside: the position McNemar fields of paired_positions (n, fixed, broken, p, base_wrong, out_wrong)."""
    d = paired_positions(truth_rows, base_lines, out_lines, missing, abstain=True)
    rb = score_item(truth_rows, base_lines, missing, G=1.0, strict=strict)
    ro = score_item(truth_rows, out_lines, missing, G=1.0, strict=strict)
    lines = sorted(set(rb['per_line']) & set(ro['per_line']))
    imp = sum(1 for l in lines if ro['per_line'][l]['E'] < rb['per_line'][l]['E'])
    wor = sum(1 for l in lines if ro['per_line'][l]['E'] > rb['per_line'][l]['E'])
    d.update(lines=len(lines), lines_improved=imp, lines_worsened=wor, lines_tied=len(lines) - imp - wor,
             line_p=round(sign_test(imp, wor), 4), edits_base=sum(rb['per_line'][l]['E'] for l in lines),
             edits_out=sum(ro['per_line'][l]['E'] for l in lines), N=sum(rb['per_line'][l]['N'] for l in lines),
             per_line_base=rb['per_line'], per_line_out=ro['per_line'])
    return d


def line_bootstrap(per_line, per_line_base=None, n=1000, seed=20261010):
    """95% line-level bootstrap (percentile) of sum(E)/sum(N); with per_line_base, of the paired difference
    output - base on the same resampled lines. Conditional on these lines (one item); says nothing about other hands."""
    lines = sorted(l for l in per_line if per_line_base is None or l in per_line_base)
    if not lines:
        return (float('nan'), float('nan'))
    rng = random.Random(seed)
    stats = []
    for _ in range(n):
        smp = [lines[rng.randrange(len(lines))] for _ in lines]
        N = sum(per_line[l]['N'] for l in smp)
        if N == 0:
            continue
        v = sum(per_line[l]['E'] for l in smp) / N
        if per_line_base is not None:
            v -= sum(per_line_base[l]['E'] for l in smp) / N
        stats.append(v)
    stats.sort()
    if not stats:
        return (float('nan'), float('nan'))
    return (round(stats[int(0.025 * len(stats))], 4), round(stats[min(len(stats) - 1, int(0.975 * len(stats)))], 4))


def ranking_flips(scores):
    """scores {name: (err_075, ser_unit)} -> [(a, b)] pairs the two measures order differently (strictly)."""
    names, out = sorted(scores), []
    for i, a in enumerate(names):
        for b in names[i + 1:]:
            d1 = scores[a][0] - scores[b][0]
            d2 = scores[a][1] - scores[b][1]
            if (d1 > 1e-12 and d2 < -1e-12) or (d1 < -1e-12 and d2 > 1e-12) or ((abs(d1) < 1e-12) != (abs(d2) < 1e-12)):
                out.append((a, b))
    return out


def summarise(res):
    k = res['wrong'] + res['deleted'] + res['inserted']
    n = res['scored']
    lo, hi = wilson(min(k, n), n)
    return k, n, (k / n if n else float('nan')), lo, hi


def _main_legacy(argv=None):
    """The pre-fix CLI (sha256 19640dae... of 10 Oct 2026 00:18), kept byte-for-byte in its output. --legacy."""
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
            rc |= _main_legacy([x for x in (argv or sys.argv[1:]) if x not in a.outputs and x != a.paired and x != '--paired']
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
                pr = paired_positions(truth, base_lines, out_lines)
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
        res = score_item(truth, out_lines, missing='skip', abstain=False)
        k, n, e, lo, hi = summarise(res)
        splits[item['split']][0] += k; splits[item['split']][1] += n
        report.append({'item': item['item'], 'split': item['split'], 'err_true': round(e, 4),
                       'wilson95': [round(lo, 4), round(hi, 4)], 'errors': k, 'scored': n,
                       'wrong': res['wrong'], 'deleted': res['deleted'], 'inserted': res['inserted'],
                       'excluded': res['excluded'], 'lines_missing': len(res['lines_missing']),
                       'per_value': {v: c for v, c in sorted(res['per_value'].items(), key=lambda t: -t[1][0]) if c[0]},
                       'top_confusions': ['%s<-%s x%d' % (t, s, c) for (t, s), c in res['confusions'].most_common(a.top)]})
        if a.exclude_flagged:
            fres = score_item(drop_flagged(truth), out_lines, missing='skip', abstain=False)
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


def _rate(k, n):
    return k / n if n else float('nan')


def _measure(res):
    k = res['wrong'] + res['deleted'] + res['inserted']
    return k, res['scored'], _rate(k, res['scored'])


def _score_mask(truth, out_lines, a, missing):
    """All figures for one mask: the 0.75-indel err_true, standard SER, optional strict pair."""
    r = score_item(truth, out_lines, missing, G=0.75)
    u = score_item(truth, out_lines, missing, G=1.0)
    k, n, e = _measure(r)
    uk, un, ue = _measure(u)
    d = {'err_true': round(e, 4), 'errors': k, 'scored': n, 'wrong': r['wrong'], 'deleted': r['deleted'],
         'inserted': r['inserted'], 'excluded': r['excluded'], 'lines_missing': len(r['lines_missing']),
         'missing_deleted': r['missing_deleted'],
         'ser': round(ue, 4), 'ser_errors': uk, 'ser_S': u['wrong'], 'ser_D': u['deleted'], 'ser_I': u['inserted'],
         'abstained': r['abstained'], 'accepted': r['accepted'], 'accepted_wrong': r['accepted_wrong'],
         'accepted_error': round(_rate(r['accepted_wrong'], r['accepted']), 4) if r['accepted'] else None,
         'coverage': round(_rate(r['accepted'], n), 4) if n else None,
         'position_errors': r['wrong'] + r['deleted'], 'read': r['read'],
         'position_rate': round((r['wrong'] + r['deleted']) / n, 4) if n else None,
         'insertion_rate': round(r['inserted'] / r['read'], 4) if r['read'] else None,
         '_res': r, '_per_line': u['per_line']}
    if a.strict:
        sr = score_item(truth, out_lines, missing, G=0.75, strict=True)
        su = score_item(truth, out_lines, missing, G=1.0, strict=True)
        sk, sn, se = _measure(sr)
        suk, sun, sue = _measure(su)
        d['strict'] = {'err_true': round(se, 4), 'errors': sk, 'ser': round(sue, 4), 'ser_errors': suk, 'scored': sn}
    if a.ci:
        d['ci95_ser'] = list(line_bootstrap(u['per_line']))
        d['ci_lines'] = len(u['per_line'])
    return d


def _fmt_mask(label, d, a, flagged=None):
    s = ('%s: err_true(0.75-indel align) %.3f (%d/%d) | standard SER (unit-cost Levenshtein) %.3f (%d/%d): S %d D %d I %d'
         ' | wrong %d deleted %d inserted %d | excluded %d | lines missing %d (%d signs counted deleted)'
         % (label, d['err_true'], d['errors'], d['scored'], d['ser'], d['ser_errors'], d['scored'], d['ser_S'],
            d['ser_D'], d['ser_I'], d['wrong'], d['deleted'], d['inserted'], d['excluded'], d['lines_missing'],
            d['missing_deleted']))
    if flagged is not None:
        s += (' [%d flagged] | position errors %d/%d = %.3f | insertions %d / read %d = %.3f'
              % (flagged, d['position_errors'], d['scored'], d['position_rate'] or 0.0, d['inserted'], d['read'],
                 d['insertion_rate'] or 0.0))
    out = [s, '    reader abstentions %d | accepted-token error %d/%d = %.3f | coverage %d/%d = %.3f'
           % (d['abstained'], d['accepted_wrong'], d['accepted'], d['accepted_error'] or 0.0, d['accepted'],
              d['scored'], d['coverage'] or 0.0)]
    if 'strict' in d:
        t = d['strict']
        out.append('    strict (exact ref_sign, visual identity): err_true(0.75-indel align) %.3f (%d/%d) | standard SER '
                   '%.3f (%d/%d)' % (t['err_true'], t['errors'], t['scored'], t['ser'], t['ser_errors'], t['scored']))
    if 'ci95_ser' in d:
        out.append("    standard SER line bootstrap 95%% (1000 resamples, conditional on this item's %d lines): %.3f-%.3f"
                   % (d['ci_lines'], d['ci95_ser'][0], d['ci95_ser'][1]))
    return out


def main(argv=None):
    argv = list(sys.argv[1:] if argv is None else argv)
    if '--legacy' in argv:
        return _main_legacy([x for x in argv if x != '--legacy'])
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('outputs', nargs='+')
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv')
    ap.add_argument('--item', action='append', help='score only these item ids')
    ap.add_argument('--line-prefix')
    ap.add_argument('--top', type=int, default=8)
    ap.add_argument('--json', action='store_true')
    ap.add_argument('--label-map', help='TSV from/to: rename labels in output, reference and truth before scoring')
    ap.add_argument('--exclude-flagged', action='store_true',
                    help='also score with truth-verifier-flagged rows excluded (never reader abstentions); both figures')
    ap.add_argument('--paired', metavar='BASE.tsv', help='paired per-line edit totals of each OUTPUT against BASE')
    ap.add_argument('--coverage-diagnostic', action='store_true',
                    help='old partial coverage: missing truth lines listed not scored, unknown line ids ignored')
    ap.add_argument('--strict', action='store_true', help='also score exact ref_sign match only (visual identity)')
    ap.add_argument('--ci', action='store_true', help='1,000-resample line-level bootstrap (paired under --paired)')
    ap.add_argument('--legacy', action='store_true', help='the pre-fix scorer, reproducing figures on file')
    a = ap.parse_args(argv)
    if not os.path.exists(a.bench):
        print('tx_bench: no bench file %s' % a.bench, file=sys.stderr); return 2
    missing = 'skip' if a.coverage_diagnostic else 'delete'
    base = os.path.dirname(os.path.abspath(a.bench))
    lm = load_label_map(a.label_map) if a.label_map else None

    def load(paths):
        ol = load_output(paths, a.line_prefix)
        return {k: [lm.get(x, x) for x in v] for k, v in ol.items()} if lm else ol
    groups = [(os.path.basename(o), load([o])) for o in a.outputs] if a.paired else [(None, load(a.outputs))]
    base_lines = load([a.paired]) if a.paired else None
    items = []
    for item in read_tsv(a.bench):
        if a.item and item['item'] not in a.item:
            continue
        truth = read_tsv(os.path.join(base, item['truth']))
        if lm:
            truth = map_truth(truth, lm)
        tl = {r['line'] for r in truth}
        if any(tl & set(ol) for _, ol in groups):
            items.append((item, truth, tl))
    if not items:
        print('tx_bench: the output covers no benchmark line', file=sys.stderr); return 2
    if not a.coverage_diagnostic:
        known = set().union(*(tl for _, _, tl in items))
        for name, ol in groups + ([(os.path.basename(a.paired), base_lines)] if a.paired else []):
            extra = sorted(set(ol) - known)
            if extra:
                print('tx_bench: %s has %d line id(s) not in the selected truth (%s): validation failed '
                      '(--coverage-diagnostic scores partial coverage)' % (name or 'output', len(extra),
                                                                          ', '.join(extra[:8])), file=sys.stderr)
                return 2
    js, text, rank = [], [], defaultdict(dict)
    if a.coverage_diagnostic:
        text.append('COVERAGE DIAGNOSTIC: partial coverage, missing truth lines are listed and not scored, unknown line '
                    'ids ignored; not the fixed-manifest score')
    for name, ol in groups:
        splits, macro = defaultdict(lambda: [0, 0, 0]), defaultdict(list)
        for item, truth, tl in items:
            if a.coverage_diagnostic and not (tl & set(ol)):
                continue
            masks = [('as measured', truth, None)]
            if a.exclude_flagged:
                ft = drop_flagged(truth)
                masks.append(('flagged excluded (truth-verifier flags only)', ft, None))
            rec = {'item': item['item'], 'split': item['split'], 'output': name, 'coverage_diagnostic': a.coverage_diagnostic}
            first = True
            for label, tr, _ in masks:
                d = _score_mask(tr, ol, a, missing)
                res, pline = d.pop('_res'), d.pop('_per_line')
                key = 'as_measured' if label == 'as measured' else 'flagged_excluded'
                if key == 'flagged_excluded':
                    d['flagged'] = rec['scored'] - d['scored']
                    rec[key] = d
                else:
                    rec.update(d)
                    rec['top_confusions'] = ['%s<-%s x%d' % (t, s, c) for (t, s), c in res['confusions'].most_common(a.top)]
                    splits[item['split']][0] += d['ser_errors']; splits[item['split']][1] += d['errors']
                    splits[item['split']][2] += d['scored']
                macro[label].append((d['ser'], d['err_true']))
                rank[(item['item'], label)][name] = (d['err_true'], d['ser'])
                lines = _fmt_mask(label, d, a, d.get('flagged') if key == 'flagged_excluded' else None)
                lines[0] = ('%s [%s] ' % (item['item'], item['split']) if first else '  ') + lines[0]
                text.extend(lines)
                first = False
                if a.paired:
                    pr = paired(tr, base_lines, ol, missing)
                    pb, po = pr.pop('per_line_base'), pr.pop('per_line_out')
                    t = ('paired %s vs %s on %s [%s]: %d lines; lines improved %d, worsened %d, tied %d; line sign test p = '
                         '%.4f; unit-cost edits base %d -> output %d over %d scored signs | beside, sign-level position '
                         'McNemar: %d common scored signs; base wrong %d, output wrong %d; fixed %d, broken %d; exact p = %.4f'
                         % (name, os.path.basename(a.paired), item['item'], label, pr['lines'], pr['lines_improved'],
                            pr['lines_worsened'], pr['lines_tied'], pr['line_p'], pr['edits_base'], pr['edits_out'],
                            pr['N'], pr['n'], pr['base_wrong'], pr['out_wrong'], pr['fixed'], pr['broken'], pr['p']))
                    if a.ci:
                        pr['ci95_ser_diff'] = list(line_bootstrap(po, pb))
                        t += ('\n    paired line bootstrap 95%% of the SER difference output - base (1000 resamples, '
                              "conditional on this item's lines): %.3f..%.3f" % tuple(pr['ci95_ser_diff']))
                    text.append(t)
                    rec.setdefault('paired', {})[key] = pr
            if rec['top_confusions']:
                text.append('  top confusions (truth value <- read): ' + ', '.join(rec['top_confusions']))
            js.append(rec)
        for s, (uk, k, n) in sorted(splits.items()):
            text.append('split %s: err_true(0.75-indel align) %.3f (%d/%d) | standard SER %.3f (%d/%d)'
                        % (s, _rate(k, n), k, n, _rate(uk, n), uk, n))
        for label, v in macro.items():
            if len(v) > 1:
                text.append('macro mean over %d items [%s] (unweighted): standard SER %.3f | err_true(0.75-indel align) %.3f'
                            % (len(v), label, sum(x[0] for x in v) / len(v), sum(x[1] for x in v) / len(v)))
    for (it, label), sc in sorted(rank.items()):
        fl = ranking_flips(sc)
        if fl:
            text.append('ranking sensitivity on %s [%s]: the 0.75-indel and unit-cost measures order %d file pair(s) '
                        'differently: %s' % (it, label, len(fl), '; '.join('%s/%s' % p for p in fl)))
    if a.json:
        print(json.dumps({'items': js}, indent=1))
    else:
        print('\n'.join(text))
    return 0


if __name__ == '__main__':
    sys.exit(main())

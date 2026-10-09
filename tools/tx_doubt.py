#!/usr/bin/env python3
"""Doubt detector: read-free per-position signals that FIND a line read's wrong signs, for the owner's sorter
(TXE-O, LANE TX-ENGINEER, 9 Oct 2026; ideas M22 + M14 in research/TX-IDEAS-2026-10-09.md).

Lesson it answers: twelve instruments tried to FIX Birago no.87's wrong signs and only the crop step moved, but several
left a truth-blind signal that FINDS them (TXE-A's show rule held 11 of L's 14 dev errors, the band-cut rule 6, the
contrast flag 5, jitter stability 1). The owner's sorter time is the scarce resource (TRANSCRIPTION.md item 7: ask the
person only the tiles whose answer moves the reading most), so the useful number is recall of the wrong positions at the
smallest flagged share. This tool computes the signals side by side and measures small OR-combinations of them.

Subcommands
  signals  --unit U: one row per line-read position of the unit's lines (line, pos, sign, one 0/1 column per signal,
           n_signals) -> OUT/<unit>_signals.tsv. Truth-blind: it reads the line read, the atlas boxes, committed
           read-free tables and the printed key, never a truth file. Signals:
             show      TXE-A's show rule (tools/tx_compare.py show_decision: atlas held-out top-1 != the line-read sign,
                       or top-1 share < 0.6, or merged A/B confidence M/L or none on file)
             disagree  passes A and B differ (agreement status != agree; tx_compare.merged_conf field='status')
             bandcut   a box of the position has top or bottom outside its line's crop band (tx_tile_gate band 'cut')
             thin      a box of the position is in the page's lowest erosion-share tercile (tx_taxonomy.erosion_share,
                       tercile_classes; the per-box value from tx_tile_gate's committed tiles table)
             contrast  tx_contrast_sweep's uncertain flag (its committed per-position flags table)
             stab      glyph_atlas --jitter stability < 0.6 (key_decode_lattice.read_stability on TXE-J's table); a
                       page without a stability table gives 0 (coverage reported)
             freq      M22: the sign's count on the page (whole line read) exceeds its expected count by > 2 sd
                       (binomial), expected = page letter-sign total x P(letter) / homophones of the letter, P from
                       the --lm corpus's letter unigrams, values from the printed key (single-letter values only)
             latt      M14: the plain lattice decode (key_decode_lattice, lam 4) chooses a sign other than the line read's
             pair      the line-read sign is in a taxonomy look-alike pair (tools/tx_pair_reread.py PAIRS, PREREG C)
  measure  --unit U: opens truth ONLY through tools/tx_bench.py position_errors (for the line read and, with --base, a
           second read such as pass A), then prints per signal recall of the wrong positions and the flagged share; the
           best OR-combination of k = 1..--kmax signals at each --cap share (highest recall; ties -> smaller share,
           then fewer signals); the recall of n_signals >= 2; and, with --combo a+b, that fixed combination (chosen
           elsewhere, not re-chosen) plus its flagged positions. --json writes the tables. Run it only after the
           signal table is committed.
  list     --unit U --combo a+b: the flagged positions of a combination (read-free; no truth) and the number of
           sorter sessions of --per-session tiles (default 10 and 20) they need.

Usage (repo root, Birago no.87 defaults):
  python3 tools/tx_doubt.py signals --unit dev_tune --latt benchmark-tx/outputs/birago1572-no87/passL_lattice_dev_tune_lam4.tsv
  python3 tools/tx_doubt.py measure --unit dev_tune --base benchmark-tx/txeng/units/passA_dev_tune.tsv
  python3 tools/tx_doubt.py list --unit eval_heldout --combo show+bandcut
  extend   --unit U (X9 + X17, TXE2-DOUBT, LANE TX-ENGINEER-2, 9 Oct 2026; PREREG-txeng2-2.md X9): adds read-free
           columns to OUT/<unit>_signals.tsv -> OUT/<unit>_signals2.tsv (n_signals recomputed over every column).
           Every other read is aligned to the unit's line read L per line (tx_bench.align, L as the reference; a sign
           the other read drops at an L position counts as differing). Specs (repeatable):
             --differ NAME=F1,F2..      1 where any Fi's aligned sign != L's (pairclf = tx_pair_clf output, whose
                                        sign moves only where its margin passes the threshold; vote = X5 weighted
                                        or uniform vote)
             --differ-ref NAME=R:F1,..  1 where any Fi's aligned sign != R's aligned sign (selfcons, X17: the
                                        K2 / V_s0 / V_s1 presentations vs pass A; H vs H2 on geo)
             --below NAME=F:COL:T       1 where F's aligned COL < T (conf = X4's p1 < 0.7)
             --line-flag NAME=F         1 on every position of a line whose `flag` is 1 (countchk = X19)
           A spec whose files do not cover the unit's lines writes 0 there; the coverage per signal is printed.
           `measure` then searches every signal column of the table it is given (--table).
Offline test: tools/tests/test_tx_doubt.py (synthetic 20-position unit with planted signals and errors; no network).
"""
import argparse, csv, itertools, json, math, os, re, sys
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
ROOT = os.path.dirname(HERE)
T = 'ciphers/nevers-birago-fr3251-1572'
SIGNALS = ['show', 'disagree', 'bandcut', 'thin', 'contrast', 'stab', 'freq', 'latt', 'pair']
D = dict(atlas=f'{T}/atlas', topk='benchmark-tx/txeng/compare/topk_no87_allheld.tsv',
         line_read='benchmark-tx/outputs/birago1572-no87/labels.tsv',
         box_pos='benchmark-tx/txeng/compare/box_pos.tsv', units='benchmark-tx/txeng/units/README.md',
         tiles='benchmark-tx/txeng/gate/tiles_{page}.tsv', contrast='benchmark-tx/txeng/sweep/flags_{unit}.tsv',
         stab='benchmark-tx/txeng/stab/stab_{page}.tsv', key=f'{T}/harvest/key_1572_sheet.tsv', lm='it16dip',
         truth='benchmark-tx/birago1572-no87.truth.tsv', out='benchmark-tx/txeng/doubt')


def path(p):
    return p if os.path.isabs(p) else os.path.join(ROOT, p)


def rd(p):
    with open(path(p), newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def ipos(p):
    return int(float(p))


def page_of(line):
    return line.rsplit('_L', 1)[0]


# ---------------------------------------------------------------- signals (truth-blind)
def letter_probs(texts):
    """{letter: P} over a-z from corpus texts (folded to ascii lower case)."""
    from key_decode_lattice import fold
    c = Counter(ch for t in texts for ch in fold(t) if 'a' <= ch <= 'z')
    n = sum(c.values()) or 1
    return {k: v / n for k, v in c.items()}


def freq_flags(L_all, key, probs, sd=2.0):
    """{(page, sign): (count, expected, z)} for the signs over-read on their page: count > expected + sd x binomial sd.
    Expected = the page's letter-sign total x P(letter) / homophones (key signs with that single-letter value)."""
    letters = {s: v for s, v in key.items() if len(v) == 1 and v in probs}
    hom = Counter(letters.values())
    psum = sum(probs[v] for v in hom) or 1.0
    by_page = defaultdict(Counter)
    for r in L_all:
        if r['sign'] in letters:
            by_page[page_of(r['line'])][r['sign']] += 1
    out = {}
    for page, cnt in by_page.items():
        N = sum(cnt.values())
        for s, n in cnt.items():
            q = probs[letters[s]] / psum / hom[letters[s]]
            e = N * q
            z = (n - e) / math.sqrt(max(N * q * (1 - q), 1e-9))
            if z > sd:
                out[(page, s)] = (n, round(e, 2), round(z, 2))
    return out


def build_signals(L_unit, L_all, box_pos, topk, conf, status, tiles, contrast, stab, latt, key, probs, pairs,
                  share=0.6, stab_floor=0.6, freq_sd=2.0):
    """-> (rows, info). Every input is already loaded; no file is read here (the offline test drives this)."""
    from tx_compare import show_decision
    from tx_taxonomy import tercile_classes
    pos2box = {(r['line'], ipos(r['pos'])): r for r in box_pos}
    tk = {r['box']: r for r in topk}
    tile = {r['sid']: r for r in tiles}
    tcls = {}
    for page in {t['page'] for t in tiles}:
        cls = tercile_classes([float(t['erosion']) for t in tiles if t['page'] == page and t.get('erosion') not in ('', None, '-')])
        for t in tiles:
            if t['page'] == page:
                tcls[t['sid']] = cls(float(t['erosion'])) if t.get('erosion') not in ('', None, '-') else '-'
    over = freq_flags(L_all, key, probs, freq_sd)
    pair_signs = {s for p in pairs for s in p.split('/')}
    rows, info = [], Counter()
    for r in L_unit:
        k = (r['line'], ipos(r['pos']))
        b = pos2box.get(k)
        sids = [s for s in (b['sid'].split('+') if b and b['sid'] else []) if s]
        _, why, _, _, _ = show_decision(r, b, tk, {(r['line'], r['pos']): conf.get(k, '')}, share)
        st = status.get(k, '')
        row = dict(line=r['line'], pos=k[1], sign=r['sign'])
        row['show'] = int(bool(why))
        row['disagree'] = int(bool(st) and st != 'agree')
        row['bandcut'] = int(any(tile.get(s, {}).get('band') == 'cut' for s in sids))
        row['thin'] = int(any(tcls.get(s) == 'thin' for s in sids))
        row['contrast'] = int(contrast.get(k, 0))
        sv = stab.get(k)
        row['stab'] = int(sv is not None and sv < stab_floor)
        row['freq'] = int((page_of(r['line']), r['sign']) in over)
        lv = latt.get(k)
        row['latt'] = int(lv is not None and lv != r['sign'])
        row['pair'] = int(r['sign'] in pair_signs)
        row['n_signals'] = sum(row[s] for s in SIGNALS)
        rows.append(row)
        info['positions'] += 1
        info['mapped_box'] += int(bool(sids))
        info['status_on_file'] += int(bool(st))
        info['stab_on_file'] += int(sv is not None)
        info['latt_on_file'] += int(lv is not None)
        info['tile_on_file'] += int(any(s in tile for s in sids))
    info['freq_overread'] = sorted(f'{p}:{s} n={v[0]} exp={v[1]} z={v[2]}' for (p, s), v in over.items())
    return rows, info


def cmd_signals(a):
    from tx_compare import merged_conf, unit_lines
    from tx_pair_reread import PAIRS
    import key_decode_lattice as K
    lines = unit_lines(path(a.units), a.unit)
    L_all = rd(a.line_read)
    L_unit = [r for r in L_all if r['line'] in lines]
    pages = sorted({page_of(l) for l in lines})
    conf_specs = a.conf or [f'{T}/harvest/f178v/passC_agreement.tsv:f178v',
                            f'{T}/harvest/f178v/passC_L11-23_agreement.tsv:f178v',
                            f'{T}/harvest/f179r/passC_agreement.tsv:f179r']
    conf_specs = [f'{path(s.rsplit(":", 1)[0])}:{s.rsplit(":", 1)[1]}' for s in conf_specs]

    def keyed(d):
        return {(ln, ipos(p)): v for (ln, p), v in d.items()}
    conf = keyed(merged_conf(conf_specs, L_all))
    status = keyed(merged_conf(conf_specs, L_all, field='status'))
    tiles = []
    for p in pages:
        f = a.tiles.format(page=p)
        if os.path.exists(path(f)):
            tiles += rd(f)
    contrast = {}
    cf = a.contrast.format(unit=a.unit)
    if os.path.exists(path(cf)):
        for r in rd(cf):
            k = (r['line'], ipos(r['pos']))
            contrast[k] = max(contrast.get(k, 0), int(r.get('uncertain') or 0))
    stab = {}
    for p in pages:
        f = a.stab.format(page=p)
        if os.path.exists(path(f)):
            stab.update(K.read_stability(path(f), path(a.box_pos)))
    latt = {}
    for f in a.latt or []:
        for r in rd(f):
            latt[(r['line'], ipos(r['pos']))] = r['sign']
    from judge_plaintext import LANG_CORPORA, read_corpus
    probs = letter_probs([read_corpus(p) for p in LANG_CORPORA[a.lm]])
    rows, info = build_signals(L_unit, L_all, rd(a.box_pos), rd(a.topk), conf, status, tiles, contrast, stab, latt,
                               K.read_key(path(a.key)), probs, PAIRS, a.share, a.stab_floor, a.freq_sd)
    os.makedirs(path(a.out), exist_ok=True)
    out = os.path.join(path(a.out), f'{a.unit}_signals.tsv')
    cols = ['line', 'pos', 'sign'] + SIGNALS + ['n_signals']
    with open(out, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])
    print(f'{a.unit}: {len(rows)} positions -> {out}')
    print('flagged per signal: ' + ', '.join(f'{s} {sum(r[s] for r in rows)}' for s in SIGNALS))
    print('coverage: ' + ', '.join(f'{k} {v}' for k, v in info.items() if k != 'freq_overread'))
    print('freq over-read signs: ' + ('; '.join(info['freq_overread']) or 'none'))
    return rows


# ---------------------------------------------------------------- measure (truth via tx_bench only)
def stats(rows, wrong, combo):
    """recall, flagged share, flagged count, wrong flagged for an OR-combination over rows keyed (line, pos)."""
    keys = [(r['line'], int(r['pos'])) for r in rows if (r['line'], int(r['pos'])) in wrong]
    flag = {(r['line'], int(r['pos'])) for r in rows if any(int(r[s]) for s in combo)}
    nw = sum(1 for k in keys if wrong[k])
    tp = sum(1 for k in keys if wrong[k] and k in flag)
    nf = sum(1 for k in keys if k in flag)
    return dict(combo='+'.join(combo), recall=tp / nw if nw else float('nan'), share=nf / len(keys) if keys else 0.0,
                flagged=nf, tp=tp, wrong=nw, n=len(keys))


def nmin_stats(rows, wrong, nmin):
    rr = [dict(r, _n=int(int(r['n_signals']) >= nmin)) for r in rows]
    s = stats(rr, wrong, ['_n'])
    s['combo'] = f'n_signals>={nmin}'
    return s


def best_combos(rows, wrong, signals, kmax, caps):
    """{(k, cap): best stats} -- highest recall at share <= cap; ties -> smaller share, then fewer signals, then name."""
    allc = [stats(rows, wrong, list(c)) for k in range(1, kmax + 1) for c in itertools.combinations(signals, k)]
    out = {}
    for k in range(1, kmax + 1):
        for cap in caps:
            ok = [s for s in allc if s['share'] <= cap + 1e-12 and len(s['combo'].split('+')) <= k]
            if ok:
                out[(k, cap)] = sorted(ok, key=lambda s: (-s['tp'], s['share'], len(s['combo'].split('+')), s['combo']))[0]
    return out


def fmt(s):
    return f"| {s['combo']} | {s['tp']}/{s['wrong']} | {s['recall']:.3f} | {s['flagged']}/{s['n']} | {s['share']:.3f} |"


def errors_for(truth_path, read_path):
    import tx_bench
    e = tx_bench.position_errors(tx_bench.read_tsv(path(truth_path)), tx_bench.load_output([path(read_path)]))
    return {(ln, ipos(p)): bool(v) for (ln, p), v in e.items()}


def signal_cols(row):
    return [c for c in row if c not in ('line', 'pos', 'sign', 'n_signals')]


def align_to_L(L_by_line, other):
    """{(line, L pos): other row or None} -- other's rows aligned to L per line (tx_bench.align, L as reference)."""
    import tx_bench
    by = defaultdict(list)
    for r in other:
        ln = r.get('line') or r.get('passage')
        by[ln].append(r)
    out = {}
    for ln, Lr in L_by_line.items():
        if ln not in by:
            continue
        orows = sorted(by[ln], key=lambda r: float(r['pos']))
        osg = [(r.get('sign') if r.get('sign') is not None else r.get('sign_id')).strip() for r in orows]
        ref = [r['sign'] for r in Lr]
        j = 0
        for ri, sg in tx_bench.align(ref, [{x} for x in ref], osg):
            if sg is not None:
                while osg[j] != sg:
                    j += 1
                o = orows[j]; j += 1
            else:
                o = None
            if ri is not None:
                out[(ln, ipos(Lr[ri]['pos']))] = o
    return out


def osign(o):
    return None if o is None else (o.get('sign') if o.get('sign') is not None else o.get('sign_id')).strip()


def extend_rows(rows, L_unit, specs):
    """specs: list of (name, kind, args) with loaded rows; -> (rows with new columns, coverage {name: covered})."""
    L_by_line = defaultdict(list)
    for r in L_unit:
        L_by_line[r['line']].append(r)
    for ln in L_by_line:
        L_by_line[ln].sort(key=lambda r: float(r['pos']))
    Lsign = {(r['line'], ipos(r['pos'])): r['sign'] for r in L_unit}
    cov = {}
    cols = {}
    for name, kind, args in specs:
        col = {}
        if kind == 'differ':
            maps = [align_to_L(L_by_line, f) for f in args]
            for k in Lsign:
                hit = [m for m in maps if any(kk[0] == k[0] for kk in m)]
                col[k] = (int(any(osign(m.get(k)) != Lsign[k] for m in hit)), bool(hit))
        elif kind == 'differ-ref':
            ref, fs = args
            rm, maps = align_to_L(L_by_line, ref), [align_to_L(L_by_line, f) for f in fs]
            for k in Lsign:
                hit = [m for m in maps if any(kk[0] == k[0] for kk in m)]
                on = bool(hit) and any(kk[0] == k[0] for kk in rm)
                col[k] = (int(on and any(osign(m.get(k)) != osign(rm.get(k)) for m in hit)), on)
        elif kind == 'below':
            f, c, t = args
            m = align_to_L(L_by_line, f)
            for k in Lsign:
                o = m.get(k)
                on = any(kk[0] == k[0] for kk in m)
                col[k] = (int(o is not None and o.get(c) not in (None, '', '-') and float(o[c]) < t), on)
        elif kind == 'line-flag':
            fl = {r['line']: int(r.get('flag') or 0) for r in args}
            for k in Lsign:
                col[k] = (fl.get(k[0], 0), k[0] in fl)
        cols[name] = col
        cov[name] = sum(1 for v in col.values() if v[1])
    out = []
    for r in rows:
        r = dict(r)
        k = (r['line'], ipos(r['pos']))
        for name in cols:
            r[name] = cols[name].get(k, (0, False))[0]
        r['n_signals'] = sum(int(r[c]) for c in signal_cols(r))
        out.append(r)
    return out, cov


def cmd_extend(a):
    from tx_compare import unit_lines
    lines = unit_lines(path(a.units), a.unit)
    L_unit = [r for r in rd(a.line_read) if r['line'] in lines]
    rows = rd(a.table or os.path.join(a.out, f'{a.unit}_signals.tsv'))
    specs = []
    for sp in a.differ or []:
        n, fs = sp.split('=', 1); specs.append((n, 'differ', [rd(f) for f in fs.split(',')]))
    for sp in a.differ_ref or []:
        n, rest = sp.split('=', 1); r, fs = rest.split(':', 1)
        specs.append((n, 'differ-ref', (rd(r), [rd(f) for f in fs.split(',')])))
    for sp in a.below or []:
        n, rest = sp.split('=', 1); f, c, t = rest.rsplit(':', 2); specs.append((n, 'below', (rd(f), c, float(t))))
    for sp in a.line_flag or []:
        n, f = sp.split('=', 1); specs.append((n, 'line-flag', rd(f)))
    rows, cov = extend_rows(rows, L_unit, specs)
    out = os.path.join(path(a.out), f'{a.unit}_{a.suffix}.tsv')
    cols = ['line', 'pos', 'sign'] + signal_cols(rows[0]) + ['n_signals']
    with open(out, 'w', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n'); w.writerow(cols)
        for r in rows:
            w.writerow([r[c] for c in cols])
    print(f'{a.unit}: {len(rows)} positions -> {out}')
    for n in cov:
        print(f'  {n}: flagged {sum(int(r[n]) for r in rows)}, positions covered {cov[n]} of {len(rows)}')
    return rows, cov


def cmd_measure(a):
    rows = rd(a.table or os.path.join(a.out, f'{a.unit}_signals.tsv'))
    reads = [('L', os.path.join('benchmark-tx/txeng/units', f'labels_{a.unit}.tsv') if a.read is None else a.read)]
    if a.base:
        reads.append(('A', a.base))
    caps = [float(c) for c in a.cap.split(',')]
    sigs = signal_cols(rows[0]) if not a.signals else a.signals.split('+')
    report = {}
    hdr = '| signal / combination | wrong flagged | recall | flagged | share |\n|---|---|---|---|---|'
    for name, rp in reads:
        wrong = errors_for(a.truth, rp)
        rep = report[name] = {}
        print(f'\n## {a.unit} vs {name} ({rp}): {sum(wrong.values())} wrong of {len(wrong)} scored')
        print('\nPer signal\n' + hdr)
        rep['signals'] = [stats(rows, wrong, [s]) for s in sigs]
        for s in rep['signals']:
            print(fmt(s))
        for n in (int(x) for x in a.nmin.split(',')):
            rep[f'nmin{n}'] = nmin_stats(rows, wrong, n)
            print(fmt(rep[f'nmin{n}']))
        if a.combo:
            rep['combo'] = stats(rows, wrong, a.combo.split('+'))
            print('\nFixed combination (chosen elsewhere, not re-chosen)\n' + hdr + '\n' + fmt(rep['combo']))
        if not a.no_search:
            bc = best_combos(rows, wrong, sigs, a.kmax, caps)
            rep['best'] = {f'k{k}_cap{c:g}': s for (k, c), s in bc.items()}
            print('\nBest OR-combination (k signals at most, share cap)\n| k | cap ' + hdr.replace('\n|', '\n|---|---|', 1))
            for (k, c), s in sorted(bc.items()):
                print(f'| {k} | {c:g} ' + fmt(s))
    if a.json:
        json.dump(report, open(path(a.json), 'w'), indent=1)
    return report


def cmd_list(a):
    rows = rd(a.table or os.path.join(a.out, f'{a.unit}_signals.tsv'))
    combo = a.combo.split('+')
    fl = [r for r in rows if any(int(r[s]) for s in combo)]
    print(f'{a.unit} combo {a.combo}: {len(fl)} of {len(rows)} positions flagged ({len(fl) / len(rows):.1%})')
    for n in a.per_session:
        print(f'  sorter sessions of {n} tiles: {math.ceil(len(fl) / n)}')
    for r in fl:
        print(f"{r['line']}\t{r['pos']}\t{r['sign']}\t" + ','.join(s for s in signal_cols(r) if int(r[s])))
    return fl


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sp = ap.add_subparsers(dest='cmd', required=True)

    def common(p):
        p.add_argument('--unit', required=True); p.add_argument('--out', default=D['out'])
    s = sp.add_parser('signals'); common(s)
    for k in ('atlas', 'topk', 'line_read', 'box_pos', 'units', 'tiles', 'contrast', 'stab', 'key', 'lm'):
        s.add_argument('--' + k.replace('_', '-'), default=D[k])
    s.add_argument('--conf', action='append', help='agreement TSV:page (repeatable; default the no.87 passC files)')
    s.add_argument('--latt', action='append', help='plain lattice decode (line, pos, sign); repeatable')
    s.add_argument('--share', type=float, default=0.6); s.add_argument('--stab-floor', type=float, default=0.6)
    s.add_argument('--freq-sd', type=float, default=2.0)
    m = sp.add_parser('measure'); common(m)
    m.add_argument('--truth', default=D['truth'])
    m.add_argument('--read', help='the line read restricted to the unit (default units/labels_<unit>.tsv)')
    m.add_argument('--base', help='a second read to measure the same signals against, e.g. pass A')
    m.add_argument('--kmax', type=int, default=3); m.add_argument('--cap', default='0.10,0.15,0.20')
    m.add_argument('--signals', help='a+b+c: restrict the search to these signals')
    m.add_argument('--combo', help='a+b: report this fixed combination'); m.add_argument('--no-search', action='store_true')
    m.add_argument('--nmin', default='2,3,4', help='report n_signals >= each of these (default 2,3,4)')
    m.add_argument('--json'); m.add_argument('--table', help='signal table (default OUT/<unit>_signals.tsv)')
    e = sp.add_parser('extend'); common(e)
    e.add_argument('--line-read', default=D['line_read']); e.add_argument('--units', default=D['units'])
    e.add_argument('--table', help='input signal table (default OUT/<unit>_signals.tsv)')
    e.add_argument('--suffix', default='signals2', help='output OUT/<unit>_<suffix>.tsv (default signals2)')
    e.add_argument('--differ', action='append'); e.add_argument('--differ-ref', action='append')
    e.add_argument('--below', action='append'); e.add_argument('--line-flag', action='append')
    li = sp.add_parser('list'); common(li)
    li.add_argument('--table'); li.add_argument('--combo', required=True); li.add_argument('--per-session', type=int, nargs='+', default=[10, 20])
    a = ap.parse_args(argv)
    return {'signals': cmd_signals, 'measure': cmd_measure, 'list': cmd_list, 'extend': cmd_extend}[a.cmd](a)


if __name__ == '__main__':
    main()

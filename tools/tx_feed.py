#!/usr/bin/env python3
"""Sorter feed as a product: ordered tiles + one question per tile for the owner's sign sorter (S4, TXE2-FEED,
LANE TX-ENGINEER-2, 9 Oct 2026; PREREG benchmark-tx/PREREG-txeng2-4.md section S4).

Read-free: it reads a line read (the base the sorter would correct), other reads already on file and committed signal
tables, never a truth file, and it never resolves a tile -- the question names the candidate piles (sorted, so the
order does not reveal which one the base read chose), never a value, never a colour, never a machine pick. Per tile
only: no cluster propagation (TXE2-SORT's X6 curve is per tile; propagation is the sorter's apply step, not this one).

    python3 tools/tx_feed.py --base BASE.tsv --unit U --out DIR \\
        [--differ NAME=FILE ...]      1 where FILE's sign, aligned to BASE per line (tx_bench.align), differs from BASE
        [--lowconf NAME=FILE ...]     1 where FILE's aligned row has conf L (a reader's own doubt)
        [--table SIGNALS.tsv]         extra 0/1 columns already computed (tx_doubt signals3 etc.), joined on line,pos
        [--cand NAME ...]             signal columns whose aligned sign is offered as a candidate pile (default: every --differ)
        --combo a+b+c                 the dev-chosen first tier (X9); a column absent for this unit counts 0 and is reported
        [--rename OLD=NEW]            line-name prefix rewrite for a file whose lines lack the unit prefix (L01 -> f152r_L01)
        [--tile-map box_pos.tsv]      sid,line,pos map; tile id = sid, else <line>_<pos>
        [--pairs taxonomy]            add the look-alike partner from tools/tx_pair_reread.PAIRS as a candidate
        [--focus N]                   focus.tsv rows (default: every combo-flagged tile, at most 30)

Writes DIR/<U>_feed_signals.tsv (line,pos,sign,tile, one column per signal, n_signals, combo),
DIR/<U>_feed.tsv (rank,tile,line,pos,tier,n_signals,candidates,question) and DIR/<U>_focus.tsv (tile, question; the
format of ciphers/nevers-birago-fr3251-1572/sorter/no87/focus.tsv). Order: combo-flagged first, then n_signals desc,
then line/pos.

Question per tile (research/TX-TAXONOMY-2026-10-09.md): a taxonomy look-alike pair names the feature that separates it
(T18/T98 descender length, T90/T53 and T76/e-cells the loop, T64/l-cells the tail); bandcut adds "the band may cut the
sign: open the line view"; thin adds "hairline ink: zoom on the tick or tail"; otherwise "(the reads split)"; a lowconf-only tile asks plainly.
Focus = the combo tier; a unit where no combo column exists falls back to the any-signal tier (stated in the feed header).
Offline test: tools/tests/test_tx_feed.py.
"""
import argparse, csv, os, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)

FEATURE = {frozenset(('T18', 'T98')): 'compare the descender length',
           frozenset(('T90', 'T53')): 'look for the closed loop',
           frozenset(('T76', 'T66')): 'look for the loop', frozenset(('T76', 'T86')): 'look for the loop',
           frozenset(('T76', 'T45')): 'look for the loop',
           frozenset(('T64', 'T95')): 'look at the tail', frozenset(('T64', 'T51')): 'look at the tail',
           frozenset(('T13', 'T64')): 'look at the tail'}


def rd(p):
    with open(p, newline='', encoding='utf-8') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def sg(r):
    for k in ('sign', 'sign_id', 'chosen'):
        if r.get(k) not in (None, ''):
            return r[k].strip()
    return ''


def ln(r, ren):
    x = r.get('line') or r.get('passage')
    for old, new in ren:
        if x.startswith(old):
            return new + x[len(old):]
    return x


def by_line(rows, ren):
    d = defaultdict(list)
    for r in rows:
        d[ln(r, ren)].append(r)
    for k in d:
        d[k].sort(key=lambda r: float(r['pos']))
    return d


def align(base_by, other_by):
    """{(line, base pos): other row or None}, other aligned to base per line (tx_bench.align, base as reference)."""
    import tx_bench
    out = {}
    for line, B in base_by.items():
        O = other_by.get(line)
        if not O:
            continue
        osg = [sg(r) for r in O]
        ref = [sg(r) for r in B]
        j = 0
        for ri, s in tx_bench.align(ref, [{x} for x in ref], osg):
            o = None
            if s is not None:
                while osg[j] != s:
                    j += 1
                o = O[j]; j += 1
            if ri is not None:
                out[(line, B[ri]['pos'])] = o
    return out


def question(sign, cands, flags):
    others = sorted(c for c in cands if c and c != sign)
    piles = sorted(set([sign] + others))
    feat = None
    for o in others:
        feat = feat or FEATURE.get(frozenset((sign, o)))
    if len(piles) < 2:
        q = ('A reader marked this sign unsure: which pile?' if any(flags.get(c) == '1' for c in flags
                                                                    if c.startswith('low')) else
             'Which pile does this tile belong in?')
    else:
        q = 'Which pile: %s?' % ' or '.join(piles)
        q += ' (%s)' % feat if feat else ' (the reads split)'
    if flags.get('bandcut') == '1':
        q += ' The band may cut the sign: open the line view.'
    if flags.get('thin') == '1':
        q += ' Hairline ink: zoom on the tick or tail.'
    return q


def build(base, unit, differ=(), lowconf=(), tables=(), cand=None, combo=(), ren=(), tile_map=None, pairs=None,
          focus_n=30):
    base_by = by_line(base, [])
    sigs, cols, absent = defaultdict(dict), [], []
    candsign = defaultdict(set)
    cand = set(cand) if cand else {n for n, _ in differ}
    for name, rows in differ:
        cols.append(name)
        al = align(base_by, by_line(rows, ren))
        if not al:
            absent.append(name)
        for k, o in al.items():
            s = sg(o) if o is not None else '<deleted>'
            b = next(sg(r) for r in base_by[k[0]] if r['pos'] == k[1])
            sigs[k][name] = '1' if s != b else '0'
            if s != b and name in cand and o is not None:
                candsign[k].add(s)
    for name, rows in lowconf:
        cols.append(name)
        al = align(base_by, by_line(rows, ren))
        if not al:
            absent.append(name)
        for k, o in al.items():
            sigs[k][name] = '1' if (o is not None and (o.get('conf') or '').strip() == 'L') else '0'
    for t in tables:
        for r in t:
            k = (r['line'], r['pos'])
            for c, v in r.items():
                if c in ('line', 'pos', 'sign', 'n_signals'):
                    continue
                if c not in cols:
                    cols.append(c)
                sigs[k][c] = v
    for c in combo:
        if c not in cols:
            absent.append(c)
    tmap = {}
    if tile_map:
        for r in tile_map:
            tmap.setdefault((r['line'], r['pos']), r['sid'])
    pair_of = defaultdict(set)
    for p in pairs or []:
        a, b = p.split('/')
        pair_of[a].add(b); pair_of[b].add(a)
    rows = []
    for line in sorted(base_by):
        for r in base_by[line]:
            k = (line, r['pos'])
            f = sigs.get(k, {})
            vals = {c: f.get(c, '0') for c in cols}
            n = sum(v == '1' for v in vals.values())
            cb = int(any(vals.get(c) == '1' for c in combo))
            s = sg(r)
            cs = set(candsign[k]) | (pair_of.get(s, set()) if (cb or n) else set())
            rows.append(dict(line=line, pos=r['pos'], sign=s, tile=tmap.get(k, '%s_%s' % (line, r['pos'])),
                             n_signals=n, combo=cb, cands=cs, q=question(s, cs, vals), **vals))
    order = sorted(rows, key=lambda r: (-r['combo'], -r['n_signals'], r['line'], float(r['pos'])))
    return cols, rows, order, sorted(set(absent))


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--base', required=True); ap.add_argument('--unit', required=True); ap.add_argument('--out', required=True)
    ap.add_argument('--differ', action='append', default=[]); ap.add_argument('--lowconf', action='append', default=[])
    ap.add_argument('--table', action='append', default=[]); ap.add_argument('--cand', nargs='*')
    ap.add_argument('--combo', default=''); ap.add_argument('--rename', action='append', default=[])
    ap.add_argument('--tile-map'); ap.add_argument('--pairs', choices=['taxonomy'])
    ap.add_argument('--focus', type=int, default=30)
    a = ap.parse_args(argv)
    spec = lambda xs: [(x.split('=', 1)[0], rd(x.split('=', 1)[1])) for x in xs]
    pairs = None
    if a.pairs:
        import tx_pair_reread
        pairs = tx_pair_reread.PAIRS
    cols, rows, order, absent = build(rd(a.base), a.unit, spec(a.differ), spec(a.lowconf), [rd(t) for t in a.table],
                                      a.cand, [c for c in a.combo.split('+') if c],
                                      [tuple(x.split('=', 1)) for x in a.rename],
                                      rd(a.tile_map) if a.tile_map else None, pairs)
    os.makedirs(a.out, exist_ok=True)
    P = lambda s: os.path.join(a.out, '%s_%s.tsv' % (a.unit, s))
    with open(P('feed_signals'), 'w') as f:
        f.write('\t'.join(['line', 'pos', 'sign', 'tile'] + cols + ['n_signals', 'combo']) + '\n')
        for r in rows:
            f.write('\t'.join(str(r[c]) for c in ['line', 'pos', 'sign', 'tile'] + cols + ['n_signals', 'combo']) + '\n')
    nf = sum(r['combo'] for r in order)
    if len(absent) >= len([c for c in a.combo.split('+') if c]) and a.combo:
        nf = sum(1 for r in order if r['n_signals'])
        print('no combo column exists for %s: focus falls back to the any-signal tier' % a.unit)
    with open(P('feed'), 'w') as f:
        f.write('# feed: combo %s first (absent here: %s), then n_signals; read-free, no resolution, per tile%s\n'
                % (a.combo, ','.join(absent) or 'none',
                   '; no combo column exists: focus = the any-signal tier' if nf and not any(r['combo'] for r in order) else ''))
        f.write('rank\ttile\tline\tpos\ttier\tn_signals\tcandidates\tquestion\n')
        for i, r in enumerate(order, 1):
            f.write('%d\t%s\t%s\t%s\t%s\t%d\t%s\t%s\n' % (i, r['tile'], r['line'], r['pos'],
                    'combo' if r['combo'] else ('signal' if r['n_signals'] else 'none'), r['n_signals'],
                    '|'.join(sorted(set([r['sign']]) | r['cands'])), r['q']))
    with open(P('focus'), 'w') as f:
        for r in order[:min(a.focus, nf)]:
            f.write('%s\t%s\n' % (r['tile'], r['q']))
    print('%s: %d positions, focus tier %d (%.1f%%), any signal %d; absent: %s; focus rows %d'
          % (a.unit, len(rows), nf, 100.0 * nf / max(1, len(rows)), sum(1 for r in rows if r['n_signals']),
             ','.join(absent) or 'none', min(a.focus, nf)))


if __name__ == '__main__':
    main()

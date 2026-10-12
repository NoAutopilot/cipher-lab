#!/usr/bin/env python3
"""Label-aware box <-> read-token alignment (BOXMAP-LA, account 3, 11 Oct 2026).

Why it exists: the Birago no.87 box map (ciphers/nevers-birago-fr3251-1572/atlas/no87_map.py -> atlas/no87_box_token.tsv,
3 Oct 2026, copied as the `map` subcommand of tools/tx_compare.py, tools/tx_pair_reread.py and tools/tx_prep.py) is a
per-line DP over box WIDTHS ONLY. One extra box on a line (a dot, a stray mark, a sign cut in two) that it maps 1:1
pushes every later box one token late until a width coincidence lets it catch up. Second check on TXE3-9 (11 Oct 2026):
on f178v L06 it maps f178v_06_009, which the owner marked NOT-LETTER in the no.87 sorter, to token 9, and the next seven
tiles land one position late; of 208 no.87 sorter tiles with a 1:1 box the tile's atlas label equals the line read's
sign at the mapped position for 157, at -1 for 24 and at +1 for 14 -- the joins behind TXE3-9's "wrong" owner and kept
pins (32 of 35 wrong kept pins equal the truth one position over). This tool keeps the same DP and its width costs and
adds two truth-blind kinds of evidence:

  * box status (the sorter's own): `not-letter` / `trash` boxes are always skipped (never mapped, never part of a 2:1);
    `bad-cut` / `aside` boxes are placed by width only (their label is ignored) and come out with op = their status,
    never `1:1`, so no consumer that keeps `op == '1:1'` pins them;
  * box labels (a sorter seed, an owner pile, an atlas top-k): a 1:1 step costs lam * (1 - w), w the box's weight for
    the token's read sign (any of the token's acceptable signs; 0 when absent); a box with no label costs lam * neutral.
    2:1 takes the better of its two boxes; 1:2 the better of its two tokens plus lam * neutral for the other; a skipped
    token costs lam * neutral on top of its width cost, a skipped box no label cost.

lam is kept below the cost of a local shift-and-return (skip box + skip token = 5.0 in width units), so one wrong label
cannot drag its own box off its place; only a run of boxes that agree at another offset moves a stretch. With lam 0, no
labels and no statuses the DP is the old one, step for step (same costs, same option order, same strict-< tie rule):
test_box_token_align.py checks this on a synthetic line and, when the repository files are present, reproduces
atlas/no87_box_token.tsv's positions for every line.

Self-placement guard (--loo, default on): for every labelled box the line is aligned again with that box's own label
hidden. A box whose position changes is written with op `unsure` (not `1:1`) and its leave-one-out position in
`loo_pos`, so a box is never pinned at a place only its own label chose. The leave-one-out check is also the honest form
of the truth-free check below, which is otherwise circular when the checked label also steered the map.

Never reads a truth file: the inputs are boxes, statuses, labels and a line read, and nothing here opens
benchmark-tx/*.truth.tsv, a clerk sheet, an alignment to one, or the `truth` column of an old map (--old reads only
sid/line/pos/op).

Usage (generic; Birago no.87's configuration is `atlas/no87_map.py --label-aware`):

  python3 tools/box_token_align.py --signs ATLAS/signs.tsv --read LINE_READ.tsv [--read-alt TSV ...]
      [--topk CLASSIFY_TOPK.tsv] [--tile-labels TSV ...] [--status TSV ...] [--lines L ...]
      [--lam 1.5] [--neutral 0.5] [--no-loo] [--old OLD_MAP.tsv] [--check-labels TSV]
      --out MAP.tsv [--lines-out LINES.tsv]

  --signs     sid, page, line, x, w (glyph_atlas segment output; line is the box's line number on its page)
  --read      line, pos, sign; line named <page>_L<nn> (f178v_L06). --read-alt adds acceptable signs per (line, pos)
  --topk      glyph_atlas classify --topk output (box, k1, k2, k3): k1 weight 1.0, k2/k3 0.5, '_' ignored
  --tile-labels  sid, label[, weight] (several rows per sid allowed; the larger weight wins)
  --status    sid, status (not-letter, trash -> skipped; bad-cut, aside -> width only, op = status); other values ignored
  --check-labels sid, label: the truth-free check (label == read sign at the mapped position, at -1, +1, +-2, none),
              in sample and leave-one-out, printed and written to --lines-out's last rows

Output MAP.tsv: sid, page, line, pos, op, labels, status, loo_pos, old_pos. One row per box per token it covers:
1:1 / unsure / bad-cut / aside one row; 2:1 one row per box at the same pos (as tools/decipher_sheet.py reads a 2:1);
1:2 one row per token with the same sid; skiptok one row with sid empty. `labels` is the box's weight-1 labels joined
by '|'. Skipped boxes are not map rows (every row has a position); --lines-out lists them per line.

Offline test: tools/tests/test_box_token_align.py (synthetic L06-shaped line; no network, no model, no truth).
"""
import argparse
import csv
import math
import os
import re
import sys
from collections import Counter, defaultdict

SKIP_STATUS = {'not-letter', 'trash'}
COLS = ['sid', 'page', 'line', 'pos', 'op', 'labels', 'status', 'loo_pos', 'old_pos']
NEUTRAL_STATUS = {'bad-cut', 'aside'}
LAM, NEUTRAL = 1.5, 0.5


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader((ln for ln in f if not ln.startswith('#')), delimiter='\t'))


def wr(p, cols, rows):
    os.makedirs(os.path.dirname(os.path.abspath(p)) or '.', exist_ok=True)
    with open(p, 'w', encoding='utf-8') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')


def split_line(line):                                  # f178v_L03 -> ('f178v', 3)
    m = re.match(r'(.+)_L(\d+)$', line)
    return m.group(1), int(m.group(2))


def norm_status(s):
    return (s or '').strip().lower().replace('_', '-')


# ---------------------------------------------------------------- the DP
def dp(bw, toks, W, labels=None, skip=None, lam=0.0, neutral=NEUTRAL):
    """bw: box widths in x order; toks: per token a set (or str) of acceptable read signs; W: the page's median width.
    labels[i]: {code: weight} for box i, or None/{} (no label: neutral). skip[i]: box i is never mapped (not a letter).
    Returns [(box_i, tok_j, op)], op in 1:1, 2:1, 1:2, skipbox, skiptok. With lam 0 and no skip this is
    atlas/no87_map.py's dp() step for step (same costs, same option order, same strict-< tie rule)."""
    m, n = len(bw), len(toks); INF = 1e9
    toks = [{t} if isinstance(t, str) else set(t) for t in toks]
    labels = labels or [None] * m
    skip = skip or [False] * m
    nc = lam * neutral

    def lc(i, j):
        if not lam:
            return 0.0
        d = labels[i]
        if not d:
            return nc
        return lam * (1.0 - max((d.get(s, 0.0) for s in toks[j]), default=0.0))

    C = [[INF] * (n + 1) for _ in range(m + 1)]; B = [[None] * (n + 1) for _ in range(m + 1)]; C[0][0] = 0
    for i in range(m + 1):
        for j in range(n + 1):
            c = C[i][j]
            if c >= INF:
                continue
            opts = []
            if i < m and j < n and not skip[i]:
                opts.append((i + 1, j + 1, abs(math.log(bw[i] / W)) + lc(i, j), '1:1'))
            if i + 1 < m and j < n and not skip[i] and not skip[i + 1]:
                opts.append((i + 2, j + 1, 1.0 + abs(math.log((bw[i] + bw[i + 1]) / W)) + min(lc(i, j), lc(i + 1, j)), '2:1'))
            if i < m and j + 1 < n and not skip[i]:
                opts.append((i + 1, j + 2, 1.0 + abs(math.log(bw[i] / (2 * W))) + (min(lc(i, j), lc(i, j + 1)) + nc if lam else 0.0), '1:2'))
            if i < m:
                opts.append((i + 1, j, 0.0 if skip[i] else (1.2 if bw[i] < 0.5 * W else 2.5), 'skipbox'))
            if j < n:
                opts.append((i, j + 1, 2.5 + nc, 'skiptok'))
            for a, b, k, op in opts:
                if c + k < C[a][b]:
                    C[a][b] = c + k; B[a][b] = (i, j, op)
    out, i, j = [], m, n
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]; out.append((pi, pj, op)); i, j = pi, pj
    return out[::-1]


def one_to_one(path):
    """{box_i: tok_j} for the 1:1 steps of a path."""
    return {i: j for i, j, op in path if op == '1:1'}


def align_line(boxes, toks, W, lam=LAM, neutral=NEUTRAL, loo=True):
    """boxes: [dict(sid, w, labels={code: weight}, status)] in x order; toks: [dict(pos, signs=set)].
    Returns (rows, skipped_sids). rows: sid, pos, op, label, status, loo_pos. A labelled 1:1 box whose position changes
    when its own label is hidden gets op 'unsure' and its leave-one-out position in loo_pos."""
    bw = [int(b['w']) for b in boxes]
    st = [norm_status(b.get('status')) for b in boxes]
    skip = [s in SKIP_STATUS for s in st]
    labs = [None if (s in NEUTRAL_STATUS or s in SKIP_STATUS) else (b.get('labels') or None) for b, s in zip(boxes, st)]
    ts = [t['signs'] for t in toks]
    path = dp(bw, ts, W, labs, skip, lam, neutral)
    full = one_to_one(path)
    loo_pos = {}
    if loo and lam:
        for i in full:
            if not labs[i]:
                continue
            l2 = list(labs); l2[i] = None
            jj = one_to_one(dp(bw, ts, W, l2, skip, lam, neutral)).get(i)
            loo_pos[i] = jj
    rows, skipped = [], []

    def lab_str(i):
        d = boxes[i].get('labels') or {}
        return '|'.join(k for k, v in sorted(d.items(), key=lambda kv: (-kv[1], kv[0])) if v >= 1.0) or ''
    for i, j, op in path:
        if op == '1:1':
            o = st[i] if st[i] in NEUTRAL_STATUS else ('unsure' if i in loo_pos and loo_pos[i] != j else '1:1')
            lp = '' if i not in loo_pos else ('none' if loo_pos[i] is None else toks[loo_pos[i]]['pos'])
            rows.append(dict(sid=boxes[i]['sid'], pos=toks[j]['pos'], op=o, labels=lab_str(i), status=st[i], loo_pos=lp, _i=i, _j=j))
        elif op == '2:1':
            for ii in (i, i + 1):
                rows.append(dict(sid=boxes[ii]['sid'], pos=toks[j]['pos'], op=op, labels=lab_str(ii), status=st[ii], loo_pos='', _i=ii, _j=j))
        elif op == '1:2':
            for jj in (j, j + 1):
                rows.append(dict(sid=boxes[i]['sid'], pos=toks[jj]['pos'], op=op, labels=lab_str(i), status=st[i], loo_pos='', _i=i, _j=jj))
        elif op == 'skiptok':
            rows.append(dict(sid='', pos=toks[j]['pos'], op=op, labels='', status='', loo_pos='', _i=None, _j=j))
        elif op == 'skipbox':
            skipped.append(boxes[i]['sid'])
    return rows, skipped


# ---------------------------------------------------------------- inputs
def read_labels(topk=None, tile_labels=()):
    """{sid: {code: weight}} from a classify --topk TSV (k1 1.0, k2/k3 0.5) and sid/label[/weight] TSVs (max wins)."""
    L = defaultdict(dict)

    def put(sid, code, w):
        code = (code or '').strip()
        if not code or code == '_':
            return
        L[sid][code] = max(L[sid].get(code, 0.0), w)
    if topk:
        for r in rd(topk):
            for k, w in (('k1', 1.0), ('k2', 0.5), ('k3', 0.5)):
                put(r.get('box') or r.get('sid'), r.get(k), w)
    for p in tile_labels or ():
        for r in rd(p):
            put(r['sid'], r.get('label') or r.get('sign'), float(r.get('weight') or 1.0))
    return L


def read_status(paths=()):
    S = {}
    for p in paths or ():
        for r in rd(p):
            S[r['sid']] = norm_status(r.get('status'))
    return S


def build_map(signs, read, labels=None, status=None, lines=None, lam=LAM, neutral=NEUTRAL, loo=True, read_alt=()):
    """signs: atlas signs.tsv rows; read: (line, pos, sign) rows; read_alt: further (line, pos, sign) rows whose sign is
    also acceptable at that token. Returns (rows, per_line) with rows carrying page/line and per_line
    {line: dict(boxes, tokens, skipped)}."""
    labels = labels or {}; status = status or {}
    alt = defaultdict(set)
    for r in read_alt:
        alt[(r['line'], str(r['pos']))].add(r['sign'])
    by_line = defaultdict(list)
    for r in read:
        by_line[r['line']].append(r)
    lines = lines or sorted(by_line)
    rows, per = [], {}
    pages = defaultdict(list)
    for s in signs:
        pages[s['page']].append(s)
    for line in lines:
        page, li = split_line(line)
        pg = pages.get(page, [])
        tk = sorted(by_line.get(line, []), key=lambda r: int(r['pos']))
        toks = [dict(pos=t['pos'], signs={t['sign']} | alt.get((line, str(t['pos'])), set())) for t in tk]
        if not pg:
            continue
        W = sorted(int(s['w']) for s in pg)[len(pg) // 2]
        bx = sorted([s for s in pg if int(s['line']) == li], key=lambda s: int(s['x']))
        boxes = [dict(sid=s['sid'], w=s['w'], labels=labels.get(s['sid']), status=status.get(s['sid'], '')) for s in bx]
        if not boxes:
            lr = [dict(sid='', pos=t['pos'], op='skiptok', labels='', status='', loo_pos='') for t in toks]
            skipped = []
        else:
            lr, skipped = align_line(boxes, toks, W, lam, neutral, loo)
        for r in lr:
            r.update(page=page, line=line)
        rows += lr
        per[line] = dict(boxes=len(boxes), tokens=len(toks), skipped=skipped)
    return rows, per


# ---------------------------------------------------------------- summaries and checks (truth-free)
def positions(rows, loo=False):
    """{sid: (line, pos)} of the boxes a map places on one token (op 1:1 or unsure). loo=True: each labelled box at the
    position it takes with its own label hidden (rows with loo_pos 'none' -- unplaced then -- are left out)."""
    out = {}
    for r in rows:
        if r['op'] not in ('1:1', 'unsure') or not r['sid']:
            continue
        lp = r.get('loo_pos', '')
        if loo and lp == 'none':
            continue
        out[r['sid']] = (r['line'], str(lp if (loo and lp != '') else r['pos']))
    return out


def read_old(p):
    """{sid: (line, pos)} for an earlier map's 1:1 rows; reads only sid, line, pos, op (never a truth column)."""
    return {r['sid']: (r['line'], str(r['pos'])) for r in rd(p) if r.get('op') == '1:1'}


def line_summary(rows, per, old):
    """Per line: boxes, tokens, skipped boxes, new ops, and against `old` ({sid: (line, pos)}): moved (one-token box
    on another position), lost_11 (an old 1:1 box that is now skipped, 2:1, 1:2 or bad-cut/aside), with sid:old>new."""
    out = []
    for line, d in per.items():
        lr = [r for r in rows if r['line'] == line]
        newp = positions(lr)
        mv = [(s, old[s][1], newp[s][1]) for s in newp if s in old and old[s][1] != newp[s][1]]
        lost = [s for s, (ln, _) in old.items() if ln == line and s not in newp]
        ops = Counter(r['op'] for r in lr)
        out.append(dict(line=line, boxes=d['boxes'], tokens=d['tokens'], skipped='|'.join(d['skipped']),
                        ops=' '.join(f'{k}:{v}' for k, v in sorted(ops.items())), moved=len(mv),
                        moved_sids='|'.join(f'{s}:{a}>{b}' for s, a, b in sorted(mv)), lost_11=len(lost),
                        lost_sids='|'.join(sorted(lost))))
    return out


LINE_COLS = ['line', 'boxes', 'tokens', 'skipped', 'ops', 'moved', 'moved_sids', 'lost_11', 'lost_sids']


def offset_check(pos_of, check_labels, read_sign):
    """pos_of: {sid: (line, pos)}; check_labels: {sid: label}; read_sign: {(line, pos): set of signs}.
    -> Counter over '0', '-1', '+1', '+-2', 'none' (first match in that order), for sids in both."""
    c = Counter()
    for sid, lab in check_labels.items():
        if sid not in pos_of:
            continue
        line, p = pos_of[sid]; p = int(p)
        hit = None
        for d, name in ((0, '0'), (-1, '-1'), (1, '+1'), (-2, '+-2'), (2, '+-2')):
            if lab in read_sign.get((line, p + d), ()):
                hit = name; break
        c[hit or 'none'] += 1
    return c


def fmt_check(c):
    n = sum(c.values())
    return f"n {n}: at 0 {c['0']}, -1 {c['-1']}, +1 {c['+1']}, +-2 {c['+-2']}, none {c['none']}"


def check_report(rows, old, check_labels, read_rows):
    """The truth-free check, old map vs new map (in sample, and leave-one-out) -> list of (name, Counter). The old and
    new figures count the tiles placed on one token by that map; `both` restricts to tiles placed by both."""
    rs = defaultdict(set)
    for r in read_rows:
        rs[(r['line'], int(r['pos']))].add(r['sign'])
    new, loo = positions(rows), positions(rows, loo=True)
    both = {s: l for s, l in check_labels.items() if s in old and s in new}
    out = []
    if old:
        out.append(('old map, all its 1:1 tiles', offset_check(old, check_labels, rs)))
    out.append(('new map, all its one-token tiles', offset_check(new, check_labels, rs)))
    out.append(('new map leave-one-out (own label hidden)', offset_check(loo, check_labels, rs)))
    if old:
        out.append(('old map, tiles placed by both', offset_check(old, both, rs)))
        out.append(('new map, tiles placed by both', offset_check(new, both, rs)))
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--signs', required=True); ap.add_argument('--read', required=True)
    ap.add_argument('--read-alt', action='append', default=[])
    ap.add_argument('--topk'); ap.add_argument('--tile-labels', action='append', default=[])
    ap.add_argument('--status', action='append', default=[])
    ap.add_argument('--lines', nargs='+'); ap.add_argument('--lam', type=float, default=LAM)
    ap.add_argument('--neutral', type=float, default=NEUTRAL); ap.add_argument('--no-loo', action='store_true')
    ap.add_argument('--old', help='an earlier map (sid, line, pos, op) for old_pos and the per-line moved count')
    ap.add_argument('--check-labels', help='sid, label: truth-free check at the mapped position')
    ap.add_argument('--check-bound', action='store_true',
                     help='run tools/join_check.py on the map just written (requires --check-labels); writes the '
                          '.joincheck.json sidecar and exits 0 PASS, 2 FAIL, 3 UNCHECKABLE')
    ap.add_argument('--out', required=True); ap.add_argument('--lines-out')
    a = ap.parse_args(argv)
    read = rd(a.read)
    alt = [r for p in a.read_alt for r in rd(p)]
    rows, per = build_map(rd(a.signs), read, read_labels(a.topk, a.tile_labels), read_status(a.status), a.lines,
                          a.lam, a.neutral, not a.no_loo, alt)
    old = read_old(a.old) if a.old else {}
    for r in rows:
        r['old_pos'] = old[r['sid']][1] if r['sid'] in old else ''
    wr(a.out, COLS, rows)
    print(f"map: {len(rows)} rows, ops {dict(Counter(r['op'] for r in rows))} -> {a.out}")
    if a.lines_out:
        wr(a.lines_out, LINE_COLS, line_summary(rows, per, old))
    if a.check_labels:
        chk = {r['sid']: (r.get('label') or r.get('sign')) for r in rd(a.check_labels)}
        for name, c in check_report(rows, old, chk, read + alt):
            print(f'check, {name}: {fmt_check(c)}')
    if a.check_bound:
        if not a.check_labels:
            ap.error('--check-bound requires --check-labels')
        import join_check
        steered = a.check_labels in {a.topk} | set(a.tile_labels or [])
        pos_of = positions(rows, loo=steered)
        chk = {r['sid']: (r.get('label') or r.get('sign')) for r in rd(a.check_labels)}
        rs = defaultdict(set)
        for r in read + alt:
            rs[(r['line'], int(r['pos']))].add(r['sign'])
        result = join_check.evaluate(pos_of, chk, rs)
        sc = join_check.write_sidecar(a.out, result, inputs=[p for p in (a.signs, a.read, a.check_labels) if p])
        print(f"join_check --check-bound: {result['verdict']} (steered={steered}) share0={result['share0']:.3f} "
              f"(null p95 {result['p95_0']:.3f}) share+-1={result['sharepm1']:.3f} (bound {result['b2_bound']:.3f}) "
              f"-> {sc}")
        sys.exit(join_check.EXIT[result['verdict']])
    return rows


if __name__ == '__main__':
    main()

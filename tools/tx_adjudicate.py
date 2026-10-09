#!/usr/bin/env python3
"""Adjudicate two blind readers' splits with a third, value-blind reader from the crops (TXE-K, M19; 9 Oct 2026).

Lesson it answers: TX-FABLE (4 Oct 2026) found Fable a worse plain line reader than Sonnet and named "Fable as the
reconciler or adjudicator" as its untested instrument; the Birago 1572 A/B splits are today settled by a Sonnet third
reader shown the agreed neighbours AS CELL CODES (harvest/*/adjudicate_in.tsv). This tool re-poses the same items with
no code in view: each item is a bracketed stretch of the line image, the two candidate readings (A's and B's cell
sequence) in seeded random order, and the 51-cell blind sheet; the reader answers 1, 2, a third cell sequence, or ?.

Subcommands (repo root):

  items --agreement AGR.tsv [AGR2.tsv ...] --base L.tsv --line-prefix f178v --lines L01,...,L12 --out items.tsv
      An item is a maximal run of consecutive non-'agree' rows of one passage in a reconcile_passes.py-style agreement
      file (columns passage posA idA posB idB status merged). candA / candB = the run's A and B cell sequences (blanks
      dropped); sonnet = the run's merged sequence (NONE / blank dropped) = the committed adjudication; base_pos = the
      base file's positions of that merged sequence (merged order is checked equal to the base line length, else exit 2).
      A run whose merged sequence is empty is anchored after the previous merged position (a pure insertion question).
  packet --items items.tsv --signs signs.tsv --box-pos box_pos.tsv --image PAGE.jpg --page f178v --sheet SHEET.png
         --out DIR [--per 5] [--call 20] [--seed 1] [--scale 2]
      Per item a window of the page image (+-4 median sign widths around the stretch, the line's band) with brackets
      drawn above and below the stretch (dark ink, no value, no code); boxes come from the label-blind box<->position map
      (tx_compare.py map); option order 1/2 is seeded random per item and written to DIR/key.tsv, which the reader never
      gets. Writes DIR/sheet_NN.png (PER items each) and DIR/call_NN.md (CALL items per reader call: image paths, item
      lines "Item k: option 1 = T51 | option 2 = T95", the answer format).
  resolve --items items.tsv --key DIR/key.tsv --reads READS.tsv --base L.tsv --out OUT.tsv
      READS: item<TAB>answer<TAB>conf<TAB>note, answer in {1, 2, ?, a space-separated cell sequence}. 1/2 -> that option's
      sequence, a sequence -> itself, ? -> keep base. The chosen sequence replaces the base positions of the item.
  score --items items.tsv --key DIR/key.tsv --reads R1.tsv [R2.tsv ...] --base L.tsv --bench BENCHMARK-TX.tsv
        --item-id ID [--names fable,opus]
      Item accuracy through tools/tx_bench.py's own scorer, item by item: the item's choice is applied ALONE to the base
      line and the line's error count (wrong + deleted + inserted) is compared with candA alone and candB alone; an item
      is right when its choice reaches the minimum of the offered options. Rows for the committed adjudication
      ('sonnet') and for each read file. Run only after the reads are committed (the truth file is opened here).

Offline test: tools/tests/test_tx_adjudicate.py. Never give a reader items.tsv, key.tsv, the base file or any truth file.
"""
import argparse, csv, json, os, random, sys
from collections import defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader((l for l in f if not l.startswith('#')), delimiter='\t'))


def wr(p, rows, fields):
    os.makedirs(os.path.dirname(os.path.abspath(p)), exist_ok=True)
    with open(p, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=fields, delimiter='\t', lineterminator='\n', extrasaction='ignore')
        w.writeheader(); w.writerows(rows)


def load_base(p):
    L = defaultdict(list)
    for r in rd(p):
        ln = r.get('line') or r.get('passage'); s = r.get('sign') or r.get('sign_id')
        L[ln].append((float(r['pos']), s))
    return {k: [s for _, s in sorted(v)] for k, v in L.items()}


def items(agreements, base, prefix, lines, out):
    B = load_base(base)
    rows = []
    for ag in agreements:
        rows += rd(ag)
    byp = defaultdict(list)
    for r in rows:
        byp[r['passage']].append(r)
    res = []
    for ps in lines:
        R = byp.get(ps, [])
        ln = f'{prefix}_{ps}' if prefix else ps
        merged = [r['merged'] for r in R if r['merged'] and r['merged'] != 'NONE']
        if ln in B and merged != B[ln] and len(merged) != len(B[ln]):
            sys.exit(f'items: {ln}: merged length {len(merged)} != base length {len(B[ln])}')
        k, run = 0, []

        def flush():
            if not run:
                return
            seq = lambda key: [r[key] for r in run if r[key] and r[key] != 'NONE']
            son = seq('merged')
            pos = list(range(k - len(son) + 1, k + 1)) if son else []
            res.append(dict(item=len(res) + 1, line=ln, base_pos=','.join(map(str, pos)), anchor=k,
                            candA=' '.join(seq('idA')), candB=' '.join(seq('idB')), sonnet=' '.join(son) or 'NONE',
                            statuses=','.join(r['status'] for r in run), base_seq=' '.join(B[ln][p - 1] for p in pos)
                            if ln in B else ''))
            run.clear()
        for r in R:
            if r['merged'] and r['merged'] != 'NONE':
                if r['status'] == 'agree':
                    flush(); k += 1; continue
                k += 1
            if r['status'] == 'agree':
                flush(); continue
            run.append(r)
        flush()
    res = _merge_swaps(res, B)
    wr(out, res, ['item', 'line', 'base_pos', 'anchor', 'candA', 'candB', 'sonnet', 'statuses', 'base_seq'])
    return dict(items=len(res), lines=len(lines))


def _merge_swaps(res, B):
    """A one-sided gap run, one agreed sign, then a gap run on the other side (A: x s, B: s x) is one order question:
    merge the two into one item over the base positions they span."""
    out, i = [], 0
    while i < len(res):
        a = res[i]
        b = res[i + 1] if i + 1 < len(res) else None
        if (b and a['line'] == b['line'] and int(b['anchor']) == int(a['anchor']) + 1 and a['base_pos']
                and not b['base_pos'] and bool(a['candA']) != bool(a['candB']) and bool(b['candA']) != bool(b['candB'])
                and bool(a['candA']) != bool(b['candA'])):
            mid = B[a['line']][int(a['anchor'])]
            pos = [int(x) for x in a['base_pos'].split(',')] + [int(a['anchor']) + 1]
            m = dict(a, base_pos=','.join(map(str, pos)), anchor=pos[-1],
                     candA=' '.join(x for x in (a['candA'], mid, b['candA']) if x),
                     candB=' '.join(x for x in (a['candB'], mid, b['candB']) if x),
                     sonnet=' '.join(B[a['line']][p - 1] for p in pos), statuses=a['statuses'] + ',agree,' + b['statuses'],
                     base_seq=' '.join(B[a['line']][p - 1] for p in pos))
            out.append(m); i += 2
        else:
            out.append(a); i += 1
    for k, r in enumerate(out):
        r['item'] = k + 1
    return out


def _boxes(signs, box_pos, page):
    S = {r['sid']: r for r in rd(signs) if r['page'] == page}
    P = defaultdict(list)
    for r in rd(box_pos):   # a 2:1 row joins its boxes with '+'
        for sid in r['sid'].split('+'):
            if sid in S:
                P[(r['line'], int(r['pos']))].append(S[sid])
    byline = defaultdict(list)
    for s in S.values():
        byline[int(s['line'])].append(s)
    return P, byline


def packet(items_p, signs, box_pos, image, page, sheet, out, per=5, call=20, seed=1, scale=2):
    from PIL import Image, ImageDraw, ImageFont
    I = rd(items_p)
    P, byline = _boxes(signs, box_pos, page)
    im = Image.open(image).convert('L')
    rng = random.Random(seed)
    try:
        font = ImageFont.truetype('/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf', 26)
    except OSError:
        font = ImageFont.load_default()
    os.makedirs(out, exist_ok=True)
    keyrows, wins = [], []
    for it in I:
        ln = it['line']; lnum = int(ln.rsplit('L', 1)[1])
        pos = [int(x) for x in it['base_pos'].split(',') if x]
        if not pos:   # pure insertion: bracket the two neighbours
            pos = [p for p in (int(it['anchor']), int(it['anchor']) + 1) if p >= 1]
        bx = [b for p in pos for b in P.get((ln, p), [])]
        if not bx:
            sys.exit(f'packet: item {it["item"]} ({ln} {pos}) has no box in box_pos')
        x0 = min(int(b['x']) for b in bx); x1 = max(int(b['x']) + int(b['w']) for b in bx)
        L = byline[lnum]
        mw = sorted(int(b['w']) for b in L)[len(L) // 2]
        ys = [int(b['y']) for b in L]; ye = [int(b['y']) + int(b['h']) for b in L]
        top = max(0, sorted(ys)[len(ys) // 10] - 30); bot = min(im.height, sorted(ye)[-max(1, len(ye) // 10)] + 30)
        lo, hi = max(0, x0 - 4 * mw), min(im.width, x1 + 4 * mw)
        pad = 22
        w = im.crop((lo, top, hi, bot)).resize(((hi - lo) * scale, (bot - top) * scale))
        W = Image.new('RGB', (w.width, w.height + 2 * pad), 'white'); W.paste(w, (0, pad))
        d = ImageDraw.Draw(W)
        a, b = (x0 - lo) * scale - 6, (x1 - lo) * scale + 6
        for yy, dy in ((2, 1), (W.height - 3, -1)):   # bracket: horizontal bar with end ticks, outside the ink
            d.line((a, yy, b, yy), fill=(20, 20, 140), width=4)
            d.line((a, yy, a, yy + dy * 16), fill=(20, 20, 140), width=4)
            d.line((b, yy, b, yy + dy * 16), fill=(20, 20, 140), width=4)
        opts = [('A', it['candA']), ('B', it['candB'])]
        rng.shuffle(opts)
        keyrows.append(dict(item=it['item'], opt1=opts[0][0], opt2=opts[1][0], seq1=opts[0][1] or 'NONE',
                            seq2=opts[1][1] or 'NONE'))
        wins.append((it['item'], W))
    sheets = []
    for k in range(0, len(wins), per):
        grp = wins[k:k + per]
        M = Image.new('RGB', (max(w.width for _, w in grp) + 10, sum(w.height + 44 for _, w in grp)), 'white')
        d = ImageDraw.Draw(M); y = 0
        for iid, w in grp:
            d.text((8, y + 6), f'Item {iid}', fill='black', font=font); M.paste(w, (5, y + 40)); y += w.height + 44
        p = os.path.join(out, f'sheet_{k // per + 1:02d}.png'); M.save(p); sheets.append(p)
    wr(os.path.join(out, 'key.tsv'), keyrows, ['item', 'opt1', 'opt2', 'seq1', 'seq2'])
    K = {r['item']: r for r in keyrows}
    calls = []
    for c, k in enumerate(range(0, len(I), call)):
        grp = I[k:k + call]
        shs = sorted({sheets[(int(it['item']) - 1) // per] for it in grp})
        lines = '\n'.join(f"Item {it['item']}: option 1 = {fmt(K[it['item']]['seq1'])} | option 2 = "
                          f"{fmt(K[it['item']]['seq2'])}" for it in grp)
        txt = CALL.format(n=len(grp), sheets='\n'.join(f'- {os.path.abspath(s)}' for s in shs),
                          sheet=os.path.abspath(sheet), items=lines, first=grp[0]['item'], last=grp[-1]['item'])
        p = os.path.join(out, f'call_{c + 1:02d}.md'); open(p, 'w').write(txt); calls.append(p)
    return dict(items=len(I), sheets=len(sheets), calls=len(calls))


def fmt(seq):
    if seq == 'NONE' or not seq:
        return 'no sign here'
    parts = [('a mark matching no cell' if s.startswith('X_') else s) for s in seq.split()]
    return ' then '.join(parts) + (' (two signs)' if len(parts) == 2 else ' (three signs)' if len(parts) == 3 else '')


CALL = """You are adjudicating between two readings of hand-drawn cipher signs in a 16th-century manuscript. The task is
VALUE-BLIND: you match shapes to cells of a sign sheet; you do not know and must not try to find out what any sign means.

Look only at these images (open each with your image reader) and no other file:
{sheets}
- the sign sheet, 51 cells labelled T10..T98: {sheet}

Each item on the sheets is a strip of one manuscript line, upscaled 2x. A dark-blue bracket above and below the strip marks
a stretch (usually one sign, sometimes two). Two earlier readers disagreed about that stretch. For each item, decide which
option matches the ink inside the bracket, by shape against the sheet cells (dots, ticks, bars, loops and lean matter; a
stretch may hold one sign or two, and "a mark matching no cell" means no sheet cell fits).

Items {first}-{last}:
{items}

Answer for every item with exactly one of: 1, 2, a different cell or cell sequence you see instead (e.g. T44, or T24 T88),
or ? if you cannot tell. Write one TSV file at the path the task gives you, with header

item	answer	conf	note

conf = H (clear), M (plausible), L (guess); note = a few words on the shape that decided it. No other output. Report in two
lines: how many items answered 1 / 2 / other / ?.
"""


def choose(it, krow, rd_row):
    ans = (rd_row or {}).get('answer', '?').strip() if rd_row else '?'
    if ans in ('1', '2'):
        s = krow['seq' + ans]
        return [] if s == 'NONE' else s.split()
    if ans in ('', '?') or not ans:
        return None
    return [x for x in ans.replace(',', ' ').split() if x]


def apply(base, I, choices):
    B = {k: list(v) for k, v in base.items()}
    edits = defaultdict(list)
    for it in I:
        ch = choices.get(it['item'])
        if ch is None or ch == ([] if it['sonnet'] == 'NONE' else it['sonnet'].split()):
            continue   # abstain, or the committed adjudication's choice: keep the base (it carries later relabels)
        pos = [int(x) for x in it['base_pos'].split(',') if x]
        edits[it['line']].append((pos, int(it['anchor']), ch))
    for ln, E in edits.items():
        seq = B[ln]
        for pos, anchor, ch in sorted(E, key=lambda e: -(e[0][0] if e[0] else e[1] + 0.5)):
            if pos:
                seq[pos[0] - 1:pos[-1]] = ch
            else:
                seq[anchor:anchor] = ch
    return B


def write_lines(p, B, lines=None):
    rows = [dict(line=ln, pos=i + 1, sign=s) for ln in sorted(B) if not lines or ln in lines for i, s in enumerate(B[ln])]
    wr(p, rows, ['line', 'pos', 'sign'])


def resolve(items_p, key_p, reads_p, base_p, out):
    I, K = rd(items_p), {r['item']: r for r in rd(key_p)}
    R = {r['item']: r for r in rd(reads_p)}
    ch = {it['item']: choose(it, K[it['item']], R.get(it['item'])) for it in I}
    base = load_base(base_p)
    B = apply(base, I, ch)
    write_lines(out, B)
    n = lambda f: sum(1 for it in I if f(R.get(it['item'], {}).get('answer', '?').strip()))
    return dict(items=len(I), opt1=n(lambda a: a == '1'), opt2=n(lambda a: a == '2'), abstain=n(lambda a: a in ('', '?')),
                other=n(lambda a: a not in ('1', '2', '', '?')), out=out)


def line_err(truth_rows, seq):
    import tx_bench
    r = tx_bench.score_item(truth_rows, {truth_rows[0]['line']: seq})
    return r['wrong'] + r['deleted'] + r['inserted']


def score(items_p, key_p, reads, base_p, bench, item_id, names=None):
    import tx_bench
    I, K = rd(items_p), {r['item']: r for r in rd(key_p)}
    base = load_base(base_p)
    item = [r for r in tx_bench.read_tsv(bench) if r['item'] == item_id][0]
    T = defaultdict(list)
    for r in tx_bench.read_tsv(os.path.join(os.path.dirname(os.path.abspath(bench)), item['truth'])):
        T[r['line']].append(r)
    arms = [('sonnet', {it['item']: ([] if it['sonnet'] == 'NONE' else it['sonnet'].split()) for it in I})]
    for k, p in enumerate(reads):
        R = {r['item']: r for r in rd(p)}
        nm = names[k] if names and k < len(names) else os.path.basename(p)
        arms.append((nm, {it['item']: choose(it, K[it['item']], R.get(it['item'])) for it in I}))
    out, per = [], []
    for nm, ch in arms:
        right = wrong = abst = 0; vs_son = [0, 0]
        for it in I:
            ln = it['line']
            if ln not in T:
                continue
            e = lambda c: line_err(T[ln], apply(base, [it], {it['item']: c})[ln])
            best = min(e(K[it['item']]['seq1'].split() if K[it['item']]['seq1'] != 'NONE' else []),
                       e(K[it['item']]['seq2'].split() if K[it['item']]['seq2'] != 'NONE' else []))
            c = ch.get(it['item'])
            if c is None:
                abst += 1; per.append(dict(arm=nm, item=it['item'], result='abstain')); continue
            ec = e(c); son = e(arms[0][1][it['item']])
            ok = ec <= best
            right += ok; wrong += not ok
            vs_son[0] += ec < son; vs_son[1] += ec > son
            per.append(dict(arm=nm, item=it['item'], result='right' if ok else 'wrong', err=ec, best=best, sonnet_err=son))
        out.append(dict(arm=nm, items=len(I), right=right, wrong=wrong, abstain=abst,
                        better_than_sonnet=vs_son[0], worse_than_sonnet=vs_son[1]))
    return out, per


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split('\n\n', 1)[1])
    sp = ap.add_subparsers(dest='cmd', required=True)
    a1 = sp.add_parser('items'); a1.add_argument('--agreement', nargs='+', required=True); a1.add_argument('--base', required=True)
    a1.add_argument('--line-prefix', default=''); a1.add_argument('--lines', required=True); a1.add_argument('--out', required=True)
    a2 = sp.add_parser('packet')
    for x in ('--items', '--signs', '--box-pos', '--image', '--page', '--sheet', '--out'):
        a2.add_argument(x, required=True)
    a2.add_argument('--per', type=int, default=5); a2.add_argument('--call', type=int, default=20)
    a2.add_argument('--seed', type=int, default=1); a2.add_argument('--scale', type=int, default=2)
    a3 = sp.add_parser('resolve')
    for x in ('--items', '--key', '--reads', '--base', '--out'):
        a3.add_argument(x, required=True)
    a4 = sp.add_parser('score')
    for x in ('--items', '--key', '--base', '--bench', '--item-id'):
        a4.add_argument(x, required=True)
    a4.add_argument('--reads', nargs='*', default=[]); a4.add_argument('--names', default='')
    a4.add_argument('--per-item', help='write per-item results TSV here')
    a = ap.parse_args(argv)
    if a.cmd == 'items':
        r = items(a.agreement, a.base, a.line_prefix, a.lines.split(','), a.out)
    elif a.cmd == 'packet':
        r = packet(a.items, a.signs, a.box_pos, a.image, a.page, a.sheet, a.out, a.per, a.call, a.seed, a.scale)
    elif a.cmd == 'resolve':
        r = resolve(a.items, a.key, a.reads, a.base, a.out)
    else:
        r, per = score(a.items, a.key, a.reads, a.base, a.bench, a.item_id, [n for n in a.names.split(',') if n])
        if a.per_item:
            wr(a.per_item, per, ['arm', 'item', 'result', 'err', 'best', 'sonnet_err'])
    print(json.dumps(r))
    return r


if __name__ == '__main__':
    main()

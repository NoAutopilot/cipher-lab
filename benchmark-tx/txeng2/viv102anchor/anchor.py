#!/usr/bin/env python3
"""DV1c (PREREG-txeng2-15, TXE2-VIV102-ANCHOR, 9 Oct 2026): read-free anchor checks of the f.102r stretch of the Vivonne stream.

Imports the frozen builders (benchmark-tx/build_vivonne_f102r.py, build_vivonne_confirm2.py) without editing them; prints counts,
shares and per-line status tallies only -- never a truth value, a plain letter or a decode.
    python3 anchor.py ctrl            # (ii) control under each bounds choice, 200 shuffles each (seed 20261009)
    python3 anchor.py lines           # (iii)/(iv) per-line exclusion tallies + runs, f.102r and f.103r
"""
import json, os, random, sys, time
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(HERE)))
sys.path.insert(0, os.path.join(ROOT, 'benchmark-tx'))
import build_vivonne_f102r as B  # noqa: E402

def stream():
    pub, force, grade = B.rd_key()
    j0 = json.load(open(os.path.join(B.TX, 'vivk_result.json')))['j0']
    allet = B.sa.letters(open(os.path.join(B.TX, 'dec_norm.txt'), encoding='utf-8').read())
    let = allet[j0:]
    st = []
    for pg in ('f102r', 'f102v', 'f103r'):
        st += [(pg,) + t for t in B.collapse(B.raw_tokens(os.path.join(B.TX, pg + '_rec.tsv')))]
    seq = [t[1] for t in st]
    amap, dec = B.align(seq, let, pub)
    return pub, let, st, seq, amap, dec

def control(pub, let, seq, amap, a, b, n=200, seed=20261009):
    """B.build()'s control verbatim, on stream[a:b]; returns real, mean, p95, max, rank, segment unaligned share (real key)."""
    js = [amap[k] for k in range(a, b) if k in amap]
    lo, hi = max(0, min(js) - 200), min(len(let), max(js) + 200)
    seg_seq, seg_let = seq[a:b], let[lo:hi]
    def share(key, ret=False):
        am, dc = B.align(seg_seq, seg_let, key)
        n_ = sum(1 for k in range(len(seg_seq)) if dc[k] >= 0 and k in am)
        h = sum(1 for k in range(len(seg_seq)) if dc[k] >= 0 and k in am and dc[k] == seg_let[am[k]])
        return (h / max(1, n_), 1 - len(am) / len(seg_seq)) if ret else h / max(1, n_)
    real, unal = share(pub, True)
    ids, vv = list(pub), [pub[c] for c in pub]
    rng = random.Random(seed)
    sh = []
    for _ in range(n):
        rng.shuffle(vv)
        sh.append(share(dict(zip(ids, vv))))
    s = sorted(sh)
    return dict(real=round(real, 4), mean=round(sum(sh) / n, 4), p95=round(s[int(0.95 * n) - 1], 4), max=round(s[-1], 4),
                rank=1 + sum(1 for x in sh if x >= real), margin_max=round(real - s[-1], 4), margin_p95=round(real - s[int(0.95 * n) - 1], 4),
                seg_unaligned=round(unal, 4), n=b - a, window=(lo, hi))

def line_starts(st, pg):
    """stream indices where each line of page pg begins, in order."""
    out, prev = [], None
    for k, t in enumerate(st):
        if t[0] == pg and t[2] != prev:
            out.append(k); prev = t[2]
        elif t[0] != pg:
            prev = None
    return out

def main():
    pub, let, st, seq, amap, dec = stream()
    if sys.argv[1] == 'ctrl':
        L102, L102v, L103 = line_starts(st, 'f102r'), line_starts(st, 'f102v'), line_starts(st, 'f103r')
        i0, i1, i2, i3 = L102[0], L102v[0], L103[0], len(st)
        variants = [('base f102r [L01, f102v L01)', i0, i1),
                    ('start +1 line', L102[1], i1),
                    ('end -1 line', i0, L102[-1]),
                    ('end +1 line', i0, L102v[1]),
                    ('both -1 line (start at stream start, end -1)', i0, L102[-1]),
                    ('both +1 line', L102[1], L102v[1]),
                    ('f102r+f102v one segment', i0, i2),
                    ('f103r (confirm2 control, base)', i2, i3),
                    ('f103r start +1 line', L103[1], i3),
                    ('f103r start -1 line', L102v[-1], i3)]
        only = sys.argv[2:]
        res = {}
        for name, a, b in variants:
            if only and name not in only:
                continue
            t = time.time()
            r = control(pub, let, seq, amap, a, b)
            r['secs'] = round(time.time() - t)
            res[name] = r
            print(name, json.dumps(r), flush=True)
        json.dump(res, open(os.path.join(HERE, 'ctrl_%s.json' % (time.strftime('%H%M%S'))), 'w'), indent=1)

if __name__ == '__main__':
    main()

def lines_report():
    """(iii)/(iv): per-line status tallies from the frozen builders' in-memory rows (status column only) + unaligned runs."""
    import build_vivonne_confirm2 as C
    out = {}
    for name, mod in (('f102r', B), ('f103r', C)):
        rows = mod.build()[-1]
        per = {}
        for r in rows:
            d = per.setdefault(r[0], {'n': 0, 'scored': 0, 'excluded:unaligned': 0, 'excluded:align-uncertain': 0, 'other': 0})
            d['n'] += 1
            d[r[5] if r[5] in d else 'other'] += 1
        order = sorted(per)
        tot = {k: sum(per[l][k] for l in order) for k in ('n', 'scored', 'excluded:unaligned', 'excluded:align-uncertain', 'other')}
        # runs of consecutive raw positions (row order) that are excluded:unaligned, and the lines each run touches
        runs, cur = [], []
        for r in rows:
            if r[5] == 'excluded:unaligned':
                cur.append(r[0])
            elif cur:
                runs.append(cur); cur = []
        if cur:
            runs.append(cur)
        rl = sorted(((len(x), len(set(x))) for x in runs), reverse=True)
        def longest(pred):
            best = c = 0
            for l in order:
                c = c + 1 if pred(per[l]) else 0
                best = max(best, c)
            return best
        out[name] = dict(total=tot, n_lines=len(order),
                         longest_pos_run=rl[0] if rl else (0, 0), top5_pos_runs=rl[:5],
                         lines_unal_ge50=sum(per[l]['excluded:unaligned'] >= 0.5 * per[l]['n'] for l in order),
                         longest_line_run_unal_ge50=longest(lambda d: d['excluded:unaligned'] >= 0.5 * d['n']),
                         longest_line_run_unal_ge25=longest(lambda d: d['excluded:unaligned'] >= 0.25 * d['n']),
                         longest_line_run_excl_ge50=longest(lambda d: d['excluded:unaligned'] + d['excluded:align-uncertain'] >= 0.5 * d['n']),
                         per_line={l: [per[l]['n'], per[l]['scored'], per[l]['excluded:unaligned'], per[l]['excluded:align-uncertain'], per[l]['other']] for l in order})
    json.dump(out, open(os.path.join(HERE, 'lines.json'), 'w'), indent=1)
    for name, d in out.items():
        print(name, {k: v for k, v in d.items() if k != 'per_line'})
        print(' line n scored unal unc other')
        for l, v in d['per_line'].items():
            print(' ', l, *v)

if len(sys.argv) > 1 and sys.argv[1] == 'lines':
    lines_report()

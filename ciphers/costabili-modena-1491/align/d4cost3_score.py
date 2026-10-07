#!/usr/bin/env python3
"""D4-COST3 scorer (PREREG-D4-COST3.md): R1167 P2 page lines 22-29 vs clear copy P6 lines 1-5, spans cut at markers.

Uses nw/stat from d4cost_score.py unchanged (statistic, shuffle control and gate of PREREG-D4-COST). Sign stream = groups of
c2_L01..L09; {CLEAR}/{CODE} are markers. w1: c2_L02 to the first {CLEAR} on L08; w2: after the last {CLEAR} on L08 to the end of L09. Markers and x removed from the sign string.

    python3 align/d4cost2_score.py align/d4cost3_reads/passA.tsv align/d4cost3_reads/passB.tsv [--key align/key_n9cos2.tsv] [--out F]
"""
import argparse, collections, csv, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d4cost_score import nw, stat, load_key

CLEAR = {
 'w1': "a dixe serendo che ha referito che se sua maesta ne mandasse multo ge piaceriano et cussi geli mando che cussi passano le cose de sua maesta lequale pobe qua se procede cum in ogni cosa diffusamente da li modi de los pareria essere che succedessono ad uotum et ad io priaria",
 'w2': "alcuno buono sigale non li appare et quando dio volesse che le succedessono ad",
}
MARK = {'{CLEAR}', '{CODE}'}

def stream(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        ln = r['line'].replace('c2_', '')
        toks = []
        for grp in r['signs'].split('|'):
            toks += grp.split()
        out = []
        for t in toks:  # x-marker rule: a {CODE} immediately after x is part of x
            if t == '{CODE}' and out and out[-1] == 'x': continue
            out.append(t)
        rows[ln] = out
    return rows

def spans(rows):
    lines = [f'L{i:02d}' for i in range(2, 10)]
    seq = [(ln, t) for ln in lines for t in rows.get(ln, [])]
    l8 = [k for k in range(len(seq)) if seq[k][0] == 'L08' and seq[k][1] == '{CLEAR}']
    if not l8: return {}
    return {'w1': seq[:l8[0]], 'w2': seq[l8[-1] + 1:]}

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('passes', nargs='+')
    ap.add_argument('--key', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'key_n9cos2.tsv'))
    ap.add_argument('--seeds', type=int, default=20); ap.add_argument('--out')
    a = ap.parse_args(); key = load_key(a.key); res = []; newv = {}
    for pf in a.passes:
        name = os.path.basename(pf).split('.')[0]; sp = spans(stream(pf))
        hit = tot = 0; null = [[0, 0] for _ in range(a.seeds)]; vals = collections.defaultdict(list)
        for s in ('w1', 'w2'):
            if s not in sp: print(f'{name}\t{s}\tDROPPED (markers not as registered)'); continue
            sig = [t for _, t in sp[s] if t not in MARK and t != 'x']
            let = [c for c in CLEAR[s] if c.isalpha()]
            pr = nw(sig, let, key); h, t = stat(pr, key); hit += h; tot += t
            for g, l in pr:
                if g not in key and l: vals[g].append((l, s))
            for k in range(a.seeds):
                sh = let[:]; random.Random(k).shuffle(sh); h2, t2 = stat(nw(sig, sh, key), key)
                null[k][0] += h2; null[k][1] += t2
            print(f'{name}\t{s}\tsigns {len(sig)} letters {len(let)}\tC-real {h}/{t}')
        n = sum(1 for s in ('w1', 'w2') if s in sp)
        nv = sorted(h / t if t else 0 for h, t in null); p95 = nv[int(round(0.95 * (len(nv) - 1)))]
        real = hit / tot if tot else 0; ok = n > 0 and real >= p95 + 0.20 and tot / n >= 4
        print(f"{name}\tPOOLED real {real:.3f} ({hit}/{tot})\tnull mean {sum(nv)/len(nv):.3f} p95 {p95:.3f}\tgate {'PASS' if ok else 'FAIL'}")
        res.append((name, n, hit, tot, real, sum(nv) / len(nv), p95, 'PASS' if ok else 'FAIL')); newv[name] = vals
    for name, vals in newv.items():
        for g in sorted(vals):
            c = collections.Counter(l for l, _ in vals[g]); top, k = c.most_common(1)[0]
            print(f"{name}\tnon-C sign {g}\tn {len(vals[g])}\tmodal {top} {k}/{len(vals[g])}\tspans {sorted(set(s for l, s in vals[g] if l == top))}\tall {dict(c)}")
    if a.out:
        with open(a.out, 'w') as f:
            f.write('pass\tspans\tC_hit\tC_tot\treal\tnull_mean\tnull_p95\tgate\n')
            for r in res: f.write('\t'.join(str(round(x, 3)) if isinstance(x, float) else str(x) for x in r) + '\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())

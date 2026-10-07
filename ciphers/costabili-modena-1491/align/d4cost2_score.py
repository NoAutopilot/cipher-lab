#!/usr/bin/env python3
"""D4-COST2 scorer (PREREG-D4-COST2.md): R1167 P1 page lines 7-16 vs clear copy P5 lines 5-11, spans cut at markers.

Uses nw/stat from d4cost_score.py unchanged (statistic, shuffle control and gate of PREREG-D4-COST). Sign stream = groups of
c1b_L01..L10; {CLEAR}/{CODE} are markers. u1: after the leading marker run of L01 to the first x; u2: after that x to the second
{CODE} after it; u3: after that to the first {CLEAR} on L10. Markers and x removed from the sign string.

    python3 align/d4cost2_score.py align/d4cost2_reads/passA.tsv align/d4cost2_reads/passB.tsv [--key align/key_n9cos2.tsv] [--out F]
"""
import argparse, collections, csv, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from d4cost_score import nw, stat, load_key

CLEAR = {
 'u1': "lo oratori regio liquali se ritrovorono presenti alo exponere de la ambassata la ambassata sua non ha contenuto altro se non visitatione e excusatione del",
 'u2': "sel non visita sua maesta personalmente perche ancora il stae alquanto debilo per rispecto de la infirmita passata e confortare",
 'u3': "ad non stare malo contenta ma a stare cum lo animo lieto e cum patientia expectare che il se fari questa dieta che se debbe fare perche a quella hora sua maesta tractara de le cose sue cum li baroni de sua maesta",
}
MARK = {'{CLEAR}', '{CODE}'}

def stream(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        ln = r['line'].replace('c1b_', '')
        toks = []
        for grp in r['signs'].split('|'):
            toks += grp.split()
        rows[ln] = toks
    return rows

def spans(rows):
    lines = [f'L{i:02d}' for i in range(1, 11)]
    seq = [(ln, t) for ln in lines for t in rows.get(ln, [])]
    out = {}
    i = 0
    while i < len(seq) and seq[i][0] == 'L01' and seq[i][1] in MARK: i += 1
    try: jx = next(k for k in range(i, len(seq)) if seq[k][1] == 'x')
    except StopIteration: return out
    out['u1'] = seq[i:jx]
    codes = [k for k in range(jx + 1, len(seq)) if seq[k][1] == '{CODE}']
    if len(codes) < 2: return out
    out['u2'] = seq[jx + 1:codes[1]]
    try: jc = next(k for k in range(codes[1] + 1, len(seq)) if seq[k][0] == 'L10' and seq[k][1] == '{CLEAR}')
    except StopIteration: return out
    out['u3'] = seq[codes[1] + 1:jc]
    return out

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('passes', nargs='+')
    ap.add_argument('--key', default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'key_n9cos2.tsv'))
    ap.add_argument('--seeds', type=int, default=20); ap.add_argument('--out')
    a = ap.parse_args(); key = load_key(a.key); res = []; newv = {}
    for pf in a.passes:
        name = os.path.basename(pf).split('.')[0]; sp = spans(stream(pf))
        hit = tot = 0; null = [[0, 0] for _ in range(a.seeds)]; vals = collections.defaultdict(list)
        for s in ('u1', 'u2', 'u3'):
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
        n = sum(1 for s in ('u1', 'u2', 'u3') if s in sp)
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

#!/usr/bin/env python3
"""D4-COST scorer (PREREG-D4-COST.md): R1167 P1 cipher spans vs the clear copy P5, per blind pass.

Global alignment (NW) of a pass's sign string against the clear span's letters: +2 sign's C value == letter,
-1 differs, 0 sign without C value, gap -1. Real = share of C-valued sign tokens aligned to their own letter.
Null = the same against the span's letters shuffled within the span, 20 seeds. Gate: pooled real >= p95 + 0.20.

    python3 align/d4cost_score.py align/d4cost_reads/passA.tsv align/d4cost_reads/passB.tsv --spans align/d4cost_spans.tsv
"""
import argparse, csv, random, collections, sys, os

def load_key(path):
    k = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        if r['grade'] == 'C':
            k[r['sign']] = r['value']
    return k

def load_pass(path):
    rows = {}
    for r in csv.DictReader(open(path), delimiter='\t'):
        rows[r['line'].replace('c1_', '')] = [g.strip() for g in r['signs'].split('|')]
    return rows

def span_signs(rows, spec, stop=None):
    """spec: L03:-1,L04:*,L05:<CLEAR  -> groups; 'a:b' slices, '*' all, '<CLEAR' up to the first {CLEAR}, '>CLEAR' after the last."""
    out = []
    for part in spec.split(','):
        ln, sel = part.split(':', 1)
        g = rows[ln]
        if sel == '*': sl = g
        elif sel == '<CLEAR': sl = g[:g.index('{CLEAR}')] if '{CLEAR}' in g else g
        elif sel == '>CLEAR': sl = g[len(g) - g[::-1].index('{CLEAR}'):] if '{CLEAR}' in g else g
        else:
            a, b = (sel.split('/') + [''])[:2]
            sl = g[int(a) if a else None:int(b) if b else None]
        for grp in sl:
            out += [s for s in grp.split() if s != '{CLEAR}']
    if stop and stop in out:  # span ends before a code sign (e.g. x), sign-level so both passes cut alike
        out = out[:out.index(stop)]
    return out

def nw(signs, letters, key):
    n, m = len(signs), len(letters)
    S = [[0] * (m + 1) for _ in range(n + 1)]; P = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1): S[i][0] = -i; P[i][0] = 1
    for j in range(1, m + 1): S[0][j] = -j; P[0][j] = 2
    for i in range(1, n + 1):
        v = key.get(signs[i - 1])
        for j in range(1, m + 1):
            sc = 0 if v is None else (2 if v == letters[j - 1] else -1)
            best, p = S[i - 1][j - 1] + sc, 0
            if S[i - 1][j] - 1 > best: best, p = S[i - 1][j] - 1, 1
            if S[i][j - 1] - 1 > best: best, p = S[i][j - 1] - 1, 2
            S[i][j], P[i][j] = best, p
    i, j, pairs = n, m, []
    while i > 0 or j > 0:
        p = P[i][j]
        if p == 0: pairs.append((signs[i - 1], letters[j - 1])); i -= 1; j -= 1
        elif p == 1: pairs.append((signs[i - 1], None)); i -= 1
        else: j -= 1
    return pairs[::-1]

def stat(pairs, key):
    c = [(s, l) for s, l in pairs if s in key]
    return sum(1 for s, l in c if key[s] == l), len(c)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('passes', nargs='+'); ap.add_argument('--spans', required=True)
    ap.add_argument('--key', default=os.path.join(os.path.dirname(__file__), 'key_n9cos2.tsv'))
    ap.add_argument('--seeds', type=int, default=20); ap.add_argument('--out', default=None)
    a = ap.parse_args(); key = load_key(a.key)
    spans = [r for r in csv.DictReader(open(a.spans), delimiter='\t')]
    out = []; newv = {}
    for pf in a.passes:
        rows = load_pass(pf); name = os.path.basename(pf).split('.')[0]
        hit = tot = 0; null = [[0, 0] for _ in range(a.seeds)]; vals = collections.defaultdict(list)
        for sp in spans:
            sig = span_signs(rows, sp['cipher'], sp.get('stop') or None); let = [c for c in sp['clear'].lower() if c.isalpha()]
            pr = nw(sig, let, key); h, t = stat(pr, key); hit += h; tot += t
            for s, l in pr:
                if s not in key and l: vals[s].append((l, sp['span']))
            for k in range(a.seeds):
                sh = let[:]; random.Random(k).shuffle(sh); h2, t2 = stat(nw(sig, sh, key), key)
                null[k][0] += h2; null[k][1] += t2
            print(f"{name}\t{sp['span']}\tsigns {len(sig)} letters {len(let)}\tC-real {h}/{t}")
        nv = sorted(h / t if t else 0 for h, t in null)
        p95 = nv[int(round(0.95 * (len(nv) - 1)))]; real = hit / tot if tot else 0
        ok = real >= p95 + 0.20 and tot / len(spans) >= 4
        print(f"{name}\tPOOLED real {real:.3f} ({hit}/{tot})\tnull mean {sum(nv)/len(nv):.3f} p95 {p95:.3f}\tgate {'PASS' if ok else 'FAIL'}")
        out.append((name, len(spans), hit, tot, real, sum(nv) / len(nv), p95, 'PASS' if ok else 'FAIL'))
        newv[name] = vals
    for name, vals in newv.items():
        for s in sorted(vals):
            c = collections.Counter(l for l, _ in vals[s]); top, n = c.most_common(1)[0]
            print(f"{name}\tnon-C sign {s}\tn {len(vals[s])}\tmodal {top} {n}/{len(vals[s])}\tspans {sorted(set(sp for l, sp in vals[s] if l == top))}\tall {dict(c)}")
    if a.out:
        with open(a.out, 'w') as f:
            f.write('pass\tspans\tC_hit\tC_tot\treal\tnull_mean\tnull_p95\tgate\n')
            for r in out: f.write('\t'.join(str(round(x, 3)) if isinstance(x, float) else str(x) for x in r) + '\n')
    return 0

if __name__ == '__main__':
    sys.exit(main())

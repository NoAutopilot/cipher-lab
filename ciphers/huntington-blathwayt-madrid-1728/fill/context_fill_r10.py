#!/usr/bin/env python3
"""R10-HUNT2 context-fill, attempt 2 (method pre-registered in fill/PREREG-R10.md, pushed 022e9ca7e before this script existed).

Reuses context_fill.py (R9) unchanged except: the inverted-bracket fix, the fixed margin threshold t=2.786, and the
precision-above-margin gate on fresh seeds 4-6 against the shuffled-context control (one-sided Fisher exact).
Usage: python3 fill/context_fill_r10.py [--check]   (run from anywhere)
Writes fill/r10_control.tsv, fill/r10_summary.json, fill/r10_target_fill.tsv; --check exits 1 if they differ from the committed copies.
"""
import csv, json, math, os, random, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import context_fill as cf

T = 2.786; GATE_SEEDS = (4, 5, 6); CMP_SEEDS = (1, 2, 3)

def bracket(code, key, vocab):
    codes = sorted(c for c in key if c != code)
    lo = [c for c in codes if c < code][-3:]; hi = [c for c in codes if c > code][:3]
    lv = sorted(cf.norm(key[c]) for c in lo); hv = sorted(cf.norm(key[c]) for c in hi)
    a, b = cf.median_s(lv), cf.median_s(hv)
    if a and b and a > b:  # R10 change 1: inverted bracket -> [min, max] of all six
        six = sorted(lv + hv); a, b = six[0], six[-1]
    for x, y in ((a, b), (lv[0] if lv else '', hv[-1] if hv else '~')):
        cands = [w for w in vocab if (x or '') <= w <= (y or '~')]
        if len(cands) >= 5: return cands
    return cands

cf.bracket = bracket

def fisher_one_sided(a, b, c, d):
    """P(X >= a) for control hits a of a+b vs shuffled hits c of c+d (hypergeometric)."""
    n1, n2, k = a + b, c + d, a + c; N = n1 + n2
    tot = math.comb(N, k)
    return sum(math.comb(n1, x) * math.comb(n2, k - x) for x in range(a, min(n1, k) + 1)) / tot

def run_seeds(lm, key0, vocab, rows, seq, test, seeds):
    out = []
    for mode in ('control', 'shuffled'):
        for s in seeds:
            rnd = random.Random(s)
            for i in test:
                code = seq[i]; key = {c: v for c, v in key0.items() if c != code}
                others = [j for j in range(len(seq)) if j != i]
                blanked = set(rnd.sample(others, round(cf.BLANK * len(others))))
                k = rnd.choice([j for j in test if seq[j] != code]) if mode == 'shuffled' else i
                left, right = cf.context(seq, k, key, blanked)
                pred, m, top = cf.predict(lm, code, left, right, key, vocab)
                gold = cf.norm(rows[i]['gloss'])
                out.append([mode, s, rows[i]['line'], rows[i]['pos'], code, gold, pred, round(m, 3), int(pred == gold), ' '.join(top)])
    return out

def stats(out, seeds):
    r = {}
    for mode in ('control', 'shuffled'):
        rr = [x for x in out if x[0] == mode and x[1] in seeds]
        sel = [x[8] for x in rr if x[7] >= T]
        r[mode] = {'top1_mean': round(sum(x[8] for x in rr) / len(rr), 4), 'n_above_t': len(sel), 'hits_above_t': sum(sel),
                   'precision_above_t': round(sum(sel) / len(sel), 4) if sel else None}
    return r

def main():
    key0 = cf.load_key(); text, words = cf.corpus(); lm = cf.LM(text)
    vocab = sorted({w for w, c in words.items() if c >= 3} | {cf.norm(v) for v in key0.values()})
    rows = cf.items('BLA185'); seq = [int(r['group']) for r in rows]
    test = [i for i, r in enumerate(rows) if r['conf'] == 'H' and r['gloss'] and int(r['group']) in key0]
    out = run_seeds(lm, key0, vocab, rows, seq, test, CMP_SEEDS + GATE_SEEDS)
    g = stats(out, GATE_SEEDS); c = g['control']; s = g['shuffled']
    p = fisher_one_sided(c['hits_above_t'], c['n_above_t'] - c['hits_above_t'], s['hits_above_t'], s['n_above_t'] - s['hits_above_t'])
    g1 = c['n_above_t'] >= 30 and (c['precision_above_t'] or 0) >= 0.60; g2 = p < 0.05
    summ = {'t': T, 'n_columns_per_seed': len(test), 'gate_seeds': list(GATE_SEEDS), 'gate_seeds_stats': g,
            'fisher_one_sided_p': round(p, 6),
            'gate': {'control_precision>=0.60_on>=30': g1, 'fisher_p<0.05': g2, 'pass': g1 and g2},
            'comparison_seeds_1_3_fixed_bracket (not gated)': stats(out, CMP_SEEDS)}
    tgt = list(csv.DictReader(open(os.path.join(cf.TGT, 'reading_tokens.tsv')), delimiter='\t'))
    tout = []
    for item in ('BLA186_p1', 'BLA186_p3', 'BLA191_p5'):
        rr = [r for r in tgt if r['line'].startswith(item)]; sq = [int(r['group']) for r in rr]
        for i, r in enumerate(rr):
            if int(r['group']) in key0 or int(r['group']) in (585,): continue  # unkeyed groups (R9's 18), stable after the S fills land
            left, right = cf.context(sq, i, key0, set())
            pred, m, top = cf.predict(lm, sq[i], left, right, key0, vocab)
            grade = ('S' if m >= T else 'U') if summ['gate']['pass'] else 'ungraded'
            tout.append([r['line'], r['pos'], sq[i], left, right, pred, round(m, 3), grade, ' '.join(top)])
    files = {'r10_control.tsv': ['mode\tseed\tline\tpos\tcode\tgold\tpred\tmargin\thit\ttop5'] + ['\t'.join(map(str, x)) for x in out],
             'r10_target_fill.tsv': ['line\tpos\tgroup\tleft\tright\tpred\tmargin\tgrade\ttop5'] + ['\t'.join(map(str, x)) for x in tout]}
    blobs = {k: '\n'.join(v) + '\n' for k, v in files.items()}; blobs['r10_summary.json'] = json.dumps(summ, indent=1) + '\n'
    if '--check' in sys.argv:
        bad = [k for k, v in blobs.items() if not os.path.exists(os.path.join(cf.HERE, k)) or open(os.path.join(cf.HERE, k)).read() != v]
        print('stale:' if bad else 'ok', *bad); sys.exit(1 if bad else 0)
    for k, v in blobs.items(): open(os.path.join(cf.HERE, k), 'w').write(v)
    print(json.dumps(summ, indent=1))

if __name__ == '__main__':
    main()

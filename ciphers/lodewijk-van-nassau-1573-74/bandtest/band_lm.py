#!/usr/bin/env python3
"""A2-LVN3 (2 Oct 2026): null-band NULL-vs-letter test for 4610/4611/4616, scored by the fr16 char LM.

For a code X, every occurrence of X in the three letters (reading_*_full_tokens.tsv, key_full v3) is replaced in
turn by NULL (nothing) and by each single letter A-Z; the window is up to W letters of decoded context either side,
cut at any unread token (U, '?') or name/word code (value longer than one letter except NULL). The code's best
letter L* maximises the summed log2 p over its occurrences; the code is classed NULL when
sum logp(NULL windows) - sum logp(L* windows) > 0 (pre-registered, no tuned threshold).

Known-answer gate first (rule 3; AX-NAMES class-imbalance paragraph): the 13 C-graded NULL codes in 121-138 and 13
C-graded single-letter codes matched by occurrence count in the same three letters are each hidden in turn (the
code's own value is withheld; every other code keeps key_full's value) and classed the same way. Gate,
pre-registered: per-class accuracy >= 0.80 for NULL AND for letter at full count, and again with each control
code subsampled to the band codes' occurrence counts (rule 3 subsample paragraph); a band code is classed only at
an N where both classes clear 0.80 over --reps random subsamples. If the full-count gate fails, the band is not
classed (untested-by-this-tool).

  python3 band_lm.py [--w 8] [--reps 200] [--seed 1]  -> writes control.tsv, subsample.tsv, band.tsv beside it
"""
import os, sys, csv, random, argparse, collections
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, os.path.join(T, '..', '..', 'tools'))
from french16_ngram import load, fold

LETTERS = [chr(c) for c in range(65, 91) if chr(c) not in 'JUW']   # folded table: J->I, U->V, W->VV
NULLS = [121, 122, 124, 126, 127, 130, 131, 132, 133, 134, 135, 137, 138]
BAND = [125, 139, 140, 142, 145, 146, 147, 148, 149, 150, 151]

def tokens():
    out = []
    for L in ('4610', '4611', '4616'):
        rows = list(csv.DictReader(open(os.path.join(T, f'reading_{L}_full_tokens.tsv')), delimiter='\t'))
        out.append([(L, r['line'], r['idx'], r['sign'].strip(), r['value'].strip(), r['grade']) for r in rows])
    return out

def unit(value):
    """letters a token contributes, or None for a context break"""
    if value == 'NULL': return ''
    if value in ('', '?') or len(value) != 1: return None
    v = fold(value)
    return v if v.isalpha() else None

def occurrences(streams, code, w):
    occ = []
    for s in streams:
        for i, t in enumerate(s):
            if t[3] != str(code): continue
            left, j = '', i - 1
            while j >= 0 and len(left) < w:
                if s[j][3] == str(code): break           # another hidden copy: stop
                u = unit(s[j][4])
                if u is None: break
                left = u + left; j -= 1
            right, j = '', i + 1
            while j < len(s) and len(right) < w:
                if s[j][3] == str(code): break
                u = unit(s[j][4])
                if u is None: break
                right += u; j += 1
            occ.append((left[-w:], right[:w]))
    return occ

def score_table(m, occ):
    """per occurrence: dict candidate -> logp"""
    tab = []
    for l, r in occ:
        d = {'NULL': m.logp(l + r)}
        for c in LETTERS: d[c] = m.logp(l + c + r)
        tab.append(d)
    return tab

def classify(tab):
    if not tab: return None, None, 0.0
    tot = collections.Counter()
    for d in tab:
        for k, v in d.items(): tot[k] += v
    best = max(LETTERS, key=lambda c: tot[c])
    delta = tot['NULL'] - tot[best]
    return ('NULL' if delta > 0 else 'letter'), best, delta / len(tab)

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--w', type=int, default=8); ap.add_argument('--reps', type=int, default=200)
    ap.add_argument('--seed', type=int, default=1)
    a = ap.parse_args()
    m = load()
    streams = tokens()
    keyf = {r['code']: (r['value'], r['grade']) for r in csv.DictReader(open(os.path.join(T, 'key_full.tsv')), delimiter='\t')}
    cnt = collections.Counter(t[3] for s in streams for t in s)
    # matched letter codes: C-graded single-letter codes, nearest occurrence count to each null, no reuse
    pool = [c for c, (v, g) in keyf.items() if g == 'C' and len(v) == 1 and v.isalpha() and cnt[c] > 0]
    letters_ctl, used = [], set()
    for n in sorted(NULLS, key=lambda x: -cnt[str(x)]):
        c = min((p for p in pool if p not in used), key=lambda p: (abs(cnt[p] - cnt[str(n)]), int(p)))
        used.add(c); letters_ctl.append(c)
    ctl = [(str(n), 'NULL', 'NULL') for n in NULLS] + [(c, 'letter', fold(keyf[c][0])) for c in letters_ctl]
    tabs = {}
    rows = []
    for code, cls, truth in ctl:
        tab = score_table(m, occurrences(streams, code, a.w)); tabs[code] = (cls, truth, tab)
        got, best, dpo = classify(tab)
        rows.append([code, cls, truth, cnt[code], len(tab), got, best, f'{dpo:.3f}', int(got == cls),
                     int(cls == 'letter' and best == truth)])
    with open(os.path.join(HERE, 'control.tsv'), 'w') as f:
        f.write('code\ttrue_class\ttrue_value\ttokens\tscored_occ\tcalled\tbest_letter\tdelta_bits_per_occ\tclass_ok\tletter_ok\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    def acc(rs, cls): x = [r for r in rs if r[1] == cls]; return sum(r[8] for r in x) / len(x), len(x)
    an, nn = acc(rows, 'NULL'); al, nl = acc(rows, 'letter')
    lettok = sum(r[9] for r in rows if r[1] == 'letter')
    print(f'CONTROL full count: NULL {an:.3f} ({nn} codes), letter {al:.3f} ({nl} codes), '
          f'true letter recovered {lettok}/{nl}; gate 0.80 per class -> {"PASS" if an >= .8 and al >= .8 else "FAIL"}')
    # band codes (scored regardless, but classed only where the gate licenses it)
    band = []
    for b in BAND:
        tab = score_table(m, occurrences(streams, str(b), a.w)); got, best, dpo = classify(tab)
        band.append((b, cnt[str(b)], len(tab), got, best, dpo, tab))
    # subsample control to each band code's scored-occurrence count
    rng = random.Random(a.seed)
    sub = {}
    for n in sorted({x[2] for x in band}):
        ok = {'NULL': 0, 'letter': 0}; tot = {'NULL': 0, 'letter': 0}
        for code, (cls, truth, tab) in tabs.items():
            if len(tab) < n: continue
            for _ in range(a.reps):
                got, _, _ = classify(rng.sample(tab, n)); ok[cls] += (got == cls); tot[cls] += 1
        sub[n] = (ok['NULL'] / max(1, tot['NULL']), ok['letter'] / max(1, tot['letter']),
                  tot['NULL'] // a.reps, tot['letter'] // a.reps)
    with open(os.path.join(HERE, 'subsample.tsv'), 'w') as f:
        f.write('n_occ\tnull_acc\tletter_acc\tnull_codes\tletter_codes\tgate\n')
        for n, (x, y, cn, cl) in sorted(sub.items()):
            f.write(f'{n}\t{x:.3f}\t{y:.3f}\t{cn}\t{cl}\t{"pass" if x >= .8 and y >= .8 and cn and cl else "fail"}\n')
    gate_full = an >= .8 and al >= .8
    with open(os.path.join(HERE, 'band.tsv'), 'w') as f:
        f.write('code\ttokens\tscored_occ\tcalled\tbest_letter\tdelta_bits_per_occ\tlicensed\n')
        for b, tk, n, got, best, dpo, _ in band:
            x, y, cn, cl = sub[n]
            lic = gate_full and x >= .8 and y >= .8 and cn and cl
            f.write(f'{b}\t{tk}\t{n}\t{got}\t{best}\t{dpo:.3f}\t{"yes" if lic else "no (untested-by-this-tool at this N)"}\n')
    print(open(os.path.join(HERE, 'subsample.tsv')).read()); print(open(os.path.join(HERE, 'band.tsv')).read())

if __name__ == '__main__':
    main()

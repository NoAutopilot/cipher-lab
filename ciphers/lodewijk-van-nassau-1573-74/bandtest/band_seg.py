#!/usr/bin/env python3
"""GAPS28 (3 Oct 2026, account-4): null-band NULL-vs-letter test for 4610/4611/4616, scored by fr16 WORD SEGMENTATION.

A different instrument from band_lm.py (A2-LVN3, char LM, gate FAIL: an inserted letter always costs ~4 bits, so it
leaned NULL). Here a candidate is judged only by how well its window splits into corpus words, not by its probability.

PRE-REGISTERED (committed before the first scoring run; no parameter is tuned after it):
  lexicon   fr16 corpus words (tools/data/fr16, folded by french16_ngram.fold), length >= 2, corpus count >= 5.
            Single-letter words are excluded (an inserted A or Y would always be "covered").
  window    up to W = 12 decoded letters either side of the occurrence, cut at any unread token (U, '?'), any
            name/word code (value longer than one letter, except NULL) or another copy of the hidden code
            (same context rule as band_lm.py).
  cost      min over segmentations of: 1.0 per letter not inside a lexicon word + 0.1 per word used (DP over
            the whole window). Window-edge fragments cost the same under every candidate.
  candidates NULL (nothing inserted) and each of the 23 folded letters.
  decision  per code, L* = letter with least summed cost over its occurrences (ties: alphabetical first);
            called NULL iff sum cost(NULL) < sum cost(L*) strictly; a tie is called letter.
  gate      known answer, hidden one at a time, the same 26 codes as A2-LVN3: 13 C-graded nulls in 121-138
            and 13 C-graded single-letter codes matched by occurrence count. Per-class accuracy >= 0.80 for
            NULL AND for letter at full count; then each control code subsampled (--reps 200, --seed 1) to each
            band code's scored-occurrence count, and a band code is licensed only at an N where both classes
            clear 0.80. Full-count gate fail -> band untested-by-this-tool, nothing classed.
  can-differ check (rule 3): a letter code can be called NULL and a null code called letter by this rule; the
            per-class breakdown is reported, never a blended accuracy (AX-NAMES lesson).

  python3 band_seg.py   -> writes seg_control.tsv, seg_subsample.tsv, seg_band.tsv beside it
"""
import os, sys, random, collections
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import band_lm as B
sys.path.insert(0, os.path.join(B.T, '..', '..', 'tools'))
from french16_ngram import corpus_words, fold

W, MINCOUNT, MINLEN, UNCOV, PERWORD = 12, 5, 2, 1.0, 0.1

def lexicon():
    c = collections.Counter(corpus_words())
    lex = {w for w, n in c.items() if n >= MINCOUNT and len(w) >= MINLEN}
    return lex, max(len(w) for w in lex)

def seg_cost(s, lex, maxlen):
    n = len(s); best = [0.0] + [float('inf')] * n
    for i in range(1, n + 1):
        b = best[i - 1] + UNCOV
        for k in range(MINLEN, min(maxlen, i) + 1):
            if s[i - k:i] in lex and best[i - k] + PERWORD < b: b = best[i - k] + PERWORD
        best[i] = b
    return best[n]

def score_table(occ, lex, maxlen):
    tab = []
    for l, r in occ:
        d = {'NULL': seg_cost(l + r, lex, maxlen)}
        for c in B.LETTERS: d[c] = seg_cost(l + c + r, lex, maxlen)
        tab.append(d)
    return tab

def classify(tab):
    if not tab: return None, None, 0.0
    tot = collections.Counter()
    for d in tab:
        for k, v in d.items(): tot[k] += v
    best = min(B.LETTERS, key=lambda c: (tot[c], c))
    delta = tot[best] - tot['NULL']               # > 0: NULL segments better
    return ('NULL' if delta > 0 else 'letter'), best, delta / len(tab)

def main():
    import csv
    lex, maxlen = lexicon()
    print(f'lexicon {len(lex)} words, maxlen {maxlen}')
    streams = B.tokens()
    keyf = {r['code']: (r['value'], r['grade']) for r in csv.DictReader(open(os.path.join(B.T, 'key_full.tsv')), delimiter='\t')}
    cnt = collections.Counter(t[3] for s in streams for t in s)
    pool = [c for c, (v, g) in keyf.items() if g == 'C' and len(v) == 1 and v.isalpha() and cnt[c] > 0]
    letters_ctl, used = [], set()
    for n in sorted(B.NULLS, key=lambda x: -cnt[str(x)]):           # identical matching to band_lm.py
        c = min((p for p in pool if p not in used), key=lambda p: (abs(cnt[p] - cnt[str(n)]), int(p)))
        used.add(c); letters_ctl.append(c)
    ctl = [(str(n), 'NULL', 'NULL') for n in B.NULLS] + [(c, 'letter', fold(keyf[c][0])) for c in letters_ctl]
    tabs, rows = {}, []
    for code, cls, truth in ctl:
        tab = score_table(B.occurrences(streams, code, W), lex, maxlen); tabs[code] = (cls, truth, tab)
        got, best, dpo = classify(tab)
        rows.append([code, cls, truth, cnt[code], len(tab), got, best, f'{dpo:.3f}', int(got == cls),
                     int(cls == 'letter' and best == truth)])
    with open(os.path.join(HERE, 'seg_control.tsv'), 'w') as f:
        f.write('code\ttrue_class\ttrue_value\ttokens\tscored_occ\tcalled\tbest_letter\tdelta_cost_per_occ\tclass_ok\tletter_ok\n')
        for r in rows: f.write('\t'.join(map(str, r)) + '\n')
    def acc(cls): x = [r for r in rows if r[1] == cls]; return sum(r[8] for r in x) / len(x), len(x)
    an, nn = acc('NULL'); al, nl = acc('letter')
    lettok = sum(r[9] for r in rows if r[1] == 'letter')
    gate_full = an >= .8 and al >= .8
    print(f'CONTROL full count: NULL {an:.3f} ({nn} codes), letter {al:.3f} ({nl} codes), true letter is L* '
          f'{lettok}/{nl}; gate 0.80 per class -> {"PASS" if gate_full else "FAIL"}')
    band = []
    for b in B.BAND:
        tab = score_table(B.occurrences(streams, str(b), W), lex, maxlen); got, best, dpo = classify(tab)
        band.append((b, cnt[str(b)], len(tab), got, best, dpo))
    rng = random.Random(1); sub = {}
    for n in sorted({x[2] for x in band}):
        ok = {'NULL': 0, 'letter': 0}; tot = {'NULL': 0, 'letter': 0}
        for code, (cls, truth, tab) in tabs.items():
            if len(tab) < n or n == 0: continue
            for _ in range(200):
                got, _, _ = classify(rng.sample(tab, n)); ok[cls] += (got == cls); tot[cls] += 1
        sub[n] = (ok['NULL'] / max(1, tot['NULL']), ok['letter'] / max(1, tot['letter']), tot['NULL'] // 200, tot['letter'] // 200)
    with open(os.path.join(HERE, 'seg_subsample.tsv'), 'w') as f:
        f.write('n_occ\tnull_acc\tletter_acc\tnull_codes\tletter_codes\tgate\n')
        for n, (x, y, cn, cl) in sorted(sub.items()):
            f.write(f'{n}\t{x:.3f}\t{y:.3f}\t{cn}\t{cl}\t{"pass" if x >= .8 and y >= .8 and cn and cl else "fail"}\n')
    with open(os.path.join(HERE, 'seg_band.tsv'), 'w') as f:
        f.write('code\ttokens\tscored_occ\tcalled\tbest_letter\tdelta_cost_per_occ\tlicensed\n')
        for b, tk, n, got, best, dpo in band:
            x, y, cn, cl = sub[n]
            lic = gate_full and x >= .8 and y >= .8 and cn and cl
            f.write(f'{b}\t{tk}\t{n}\t{got}\t{best}\t{dpo:.3f}\t{"yes" if lic else "no (untested-by-this-tool at this N)"}\n')
    print(open(os.path.join(HERE, 'seg_subsample.tsv')).read()); print(open(os.path.join(HERE, 'seg_band.tsv')).read())

if __name__ == '__main__':
    main()

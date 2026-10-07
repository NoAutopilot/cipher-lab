"""DA1-COL2 (7 Oct 2026): reader agreement between two blind word-pairing passes (word_pairs_da1.tsv = DA1-COL, word_pairs_col2.tsv =
DA1-COL2) on c50, c3940, c47. Pre-registered in PREREG-DA1-COL2.md before word_pairs_col2.tsv was compared.
Per unit, over every numeral group (digit or unsettled) in the unit's rows of the committed *_reconciled.tsv:
  group agreement = share of groups that both passes assign to the same gloss word (norm()-equal, same line), or that both leave
  unassigned; exact-span agreement = share of (line, norm(word)) spans in either pass whose [first, last] is identical in the other.
Six-code check: for each of 16, 20, 46, 67, 81, 96, the span-occurrences under each pass (code -> word texts), listed side by side.
Usage: python3 siblings/compare_col2.py
"""
import csv, os, re, collections
H = os.path.dirname(os.path.abspath(__file__))
def norm(s): return re.sub(r'[^a-z]', '', re.sub(r'\[[^\]]*\]', '', s.lower())).replace('v', 'u').replace('j', 'i')
toks = {}
for fn in ('c5051', 'c3940', 'c4749'):
    for r in csv.DictReader(open(f'{H}/{fn}_reconciled.tsv'), delimiter='\t'): toks[r['line']] = r['tokens'].split()
def unit_of(L): return 'c50' if L.startswith('50') else 'c3940' if L[:2] in ('39', '40') else 'c47' if L.startswith('47') else None
def load(fn):
    asg = {}; spans = set(); occ = collections.defaultdict(list)
    for r in csv.DictReader(open(f'{H}/{fn}'), delimiter='\t'):
        L = r['line']; a, b = int(r['first']), int(r['last']); w = norm(r['word'])
        if not w: continue
        spans.add((L, w, a, b))
        for i in range(a, b + 1):
            asg[(L, i)] = w
            if toks[L][i].isdigit(): occ[toks[L][i]].append(f'{w}({L})')
    return asg, spans, occ
A, SA, OA = load('word_pairs_da1.tsv'); B, SB, OB = load('word_pairs_col2.tsv')
print('unit\tgroups\tgroup_agree\tpct\tspans_A\tspans_B\texact_shared\texact_pct')
for u in ('c50', 'c3940', 'c47'):
    gs = [(L, i) for L in toks if unit_of(L) == u for i in range(len(toks[L]))]
    ag = sum(A.get(g) == B.get(g) for g in gs)
    sa = {s for s in SA if unit_of(s[0]) == u}; sb = {s for s in SB if unit_of(s[0]) == u}
    sh = len(sa & sb); un = len(sa | sb)
    print(f'{u}\t{len(gs)}\t{ag}\t{100*ag/len(gs):.1f}\t{len(sa)}\t{len(sb)}\t{sh}\t{100*sh/un:.1f}')
print('six DA1-COL C codes, span-occurrences per pass')
for c in ('16', '20', '46', '67', '81', '96'):
    print(f'{c}\tDA1-COL: {"; ".join(OA[c]) or "-"}\n\tDA1-COL2: {"; ".join(OB[c]) or "-"}')

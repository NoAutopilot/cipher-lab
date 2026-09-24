#!/usr/bin/env python3
"""Compare the aligner's sign reading (ciphertext.tsv) with the two blind passes (passA.tsv, passB.tsv), per page.
Each page is one sign stream (the passes split lines differently); word breaks and commas are dropped, a pass's literal + . - = is
read as [plus] [dot] [dash] [equals] (the passes' own convention); the
passes' tokens are split into atlas signs ([label] or one character). difflib aligns each pass to the aligner's
stream; diff_vs_passes.tsv lists every aligner sign that neither pass has at the aligned position."""
import difflib, re, collections
LIT = {'+': '[plus]', '.': '[dot]', '-': '[dash]', '=': '[equals]'}   # the passes wrote these atlas marks literally
def signs(tok): return [LIT.get(x, x) for x in re.findall(r'\[[^\]]+\]|[^\s,]', tok)]
def load_pass(f):
    pages = collections.defaultdict(list)
    for l in open(f, encoding='utf-8'):
        if l.startswith('#') or l.startswith('line\t') or not l.strip(): continue
        ln, _, tok = l.rstrip('\n').split('\t')[:3]
        pages[ln[:4]] += signs(tok)
    return pages
mine = collections.defaultdict(list)
for l in open('ciphertext.tsv', encoding='utf-8'):
    if l.startswith('#') or l.startswith('line\t'): continue
    ln, i, s, _ = l.rstrip('\n').split('\t')
    if s not in '/.,': mine[ln[:4]].append((ln, i, s))
A, B = load_pass('passA.tsv'), load_pass('passB.tsv')
def aligned(m, p):
    out = {}
    sm = difflib.SequenceMatcher(None, [x[2] for x in m], p, autojunk=False)
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        for k in range(i1, i2):
            j = j1 + (k - i1)
            out[k] = p[j] if j < j2 else ''
    return out
rows, stats = [], []
for pg in sorted(mine):
    m = mine[pg]; a = aligned(m, A[pg]); b = aligned(m, B[pg])
    na = sum(a[k] == m[k][2] for k in range(len(m))); nb = sum(b[k] == m[k][2] for k in range(len(m)))
    stats.append(f'# {pg}: aligner {len(m)} signs; passA {len(A[pg])} signs, {na} agree; passB {len(B[pg])} signs, {nb} agree')
    for k, (ln, i, s) in enumerate(m):
        if a[k] != s and b[k] != s:
            rows.append(f'{ln}\t{i}\t{s}\t{a[k]}\t{b[k]}\n')
open('diff_vs_passes.tsv', 'w', encoding='utf-8').write('\n'.join(stats) + '\nline\tidx\taligner\tpassA\tpassB\n' + ''.join(rows))
print('\n'.join(stats)); print('aligner signs matching neither pass:', len(rows))
c = collections.Counter((r.split('\t')[2], r.split('\t')[3], r.split('\t')[4].strip()) for r in rows)
for k, v in c.most_common(12): print(v, k)

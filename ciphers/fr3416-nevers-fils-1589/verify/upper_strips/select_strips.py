"""DEF1-F3416 (5 Oct 2026): pick <=12 FILS-UPPER line-strip segments holding the most M/U tokens of clear_f35r.tsv
rows U01-U26/B11 (M rows are separate images, f43m_Lnn), and 6 hidden H control words in those strips.
Word position = proportional character offset of the token in the row text; s1 covers 0-0.676 of the line, s2 0.324-1
(manifest boxes 3550-5950 and 4700-7100 of 3550-7100). Controls: random.Random(20261005) over plain H tokens of >= 5
letters (neighbours unrestricted: the pool with the
neighbour rule held only 5 words), at most one per strip, offset inside the chosen segment by >= 0.05 of the line."""
import re, random, csv, sys
rows = {}
for l in open('clear_f35r.tsv', encoding='utf-8'):
    if l.startswith('#') or not l.strip(): continue
    f = l.rstrip('\n').split('\t')
    if re.match(r'^(U\d\d|B11)$', f[0]): rows[f[0]] = f[1]
TOK = re.compile(r'\{[^}]*\}|\[\.\.\.\]|<del>.*?</del>|\^[^^]*\^|\S+')
def toks(t):
    out = []
    for m in TOK.finditer(t):
        s = m.group(0); mid = (m.start() + m.end()) / 2 / len(t)
        kind = 'MU' if s.startswith(('{', '[...]')) else ('X' if s.startswith(('<del>', '^')) else 'H')
        out.append((s, mid, kind))
    return out
SEG = {'s1': (0.0, 0.676), 's2': (0.324, 1.0)}
cands = []
for r, t in rows.items():
    tk = toks(t)
    for s, (a, b) in SEG.items():
        n = sum(1 for w, m, k in tk if k == 'MU' and a <= m <= b)
        cands.append((n, r, s))
cands.sort(key=lambda x: (-x[0], x[1], x[2]))
chosen, seen = [], set()
for n, r, s in cands:          # one segment per line first, then fill
    if r in seen or n == 0: continue
    chosen.append((r, s, n)); seen.add(r)
    if len(chosen) == 12: break
mu_cov = {}
for r, s, n in chosen:
    a, b = SEG[s]
    mu_cov[r] = [w for w, m, k in toks(rows[r]) if k == 'MU' and a <= m <= b]
ctrl_pool = []
for r, s, n in chosen:
    a, b = SEG[s]; tk = toks(rows[r])
    for i, (w, m, k) in enumerate(tk):
        if k != 'H' or not (a + 0.05 <= m <= b - 0.05): continue
        if len(re.sub(r"[^A-Za-zÀ-ÿ]", '', w)) < 5: continue
        ctrl_pool.append((r, s, i, w))
rng = random.Random(20261005)
ctrl = []
for c in rng.sample(ctrl_pool, len(ctrl_pool)):
    if sum(1 for x in ctrl if x[0] == c[0]) >= 1: continue   # spread: at most one per strip
    ctrl.append(c)
    if len(ctrl) == 6: break
with open('verify/upper_strips/targets.tsv', 'w', encoding='utf-8') as o:
    o.write('row\tseg\tstrip\tmu_tokens_in_segment\n')
    for r, s, n in chosen:
        o.write(f"{r}\t{s}\timages/f43u_L{r[1:]}_{s}.jpg\t{' | '.join(mu_cov[r])}\n" if r != 'B11'
                else f"{r}\t{s}\timages/f43b_L03_{s}.jpg\t{' | '.join(mu_cov[r])}\n")
with open('verify/upper_strips/controls.tsv', 'w', encoding='utf-8') as o:
    o.write('row\tseg\ttoken_index\tH_word\n')
    for c in ctrl: o.write('\t'.join(map(str, c)) + '\n')
print(len(chosen), 'strips;', sum(n for _, _, n in chosen), 'M/U tokens covered of',
      sum(1 for t in rows.values() for w, m, k in toks(t) if k == 'MU'), '; controls', len(ctrl), 'pool', len(ctrl_pool))

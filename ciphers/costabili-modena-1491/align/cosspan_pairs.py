# COS-SPAN, 9 Oct 2026: PREREG-COS-SPAN. Short-span pairs for the R1163/R1165 cipher slips against their clear slips.
# Anchors exactly as align/n9cos2_slip_pairs.py (clear words standing in clear in both slips, monotone LCS, exact or edit distance 1
# for words >= 4 letters). New: inside each anchor span, the reader's cipher groups ('|' boundaries; a line end is also a boundary)
# are paired with the clear-slip words by a monotone DP on LENGTHS ONLY (no sign value is used): chunks of k groups : l words,
# 1 <= k, l <= 3, k + l <= 4, cost |signs - letters| / letters + 0.1 * (k + l - 2); an unpaired group or word costs 1.0.
# Each chunk is one pair (crop label <slip>_s<span>_p<n>), handed to the unchanged align/run_align.py (ratio filter 0.8-1.25,
# interlinear_align statistic, gloss-shuffle control 20 seeds). --expand applies the registered sigla table to clear words.
# Usage: python3 .../cosspan_pairs.py OUT.tsv [--expand] SLIP:READER.txt [SLIP:READER.txt ...]
import sys, re, csv, importlib.util, os
spec = importlib.util.spec_from_file_location('n9', os.path.join(os.path.dirname(os.path.abspath(__file__)), 'n9cos2_slip_pairs.py'))
n9 = importlib.util.module_from_spec(spec); spec.loader.exec_module(n9)
norm, ed1, parse = n9.norm, n9.ed1, n9.parse
# registered sigla table (PREREG-COS-SPAN; after PREREG-D4-COST2's table, PX-BRODEC normalisation), keys are normalised words
SIGLA = {'p': 'per', 'ch': 'che', 'chr': 'che', 'pch': 'perche', 'nõ': 'non', 'no': 'non', 'mta': 'maesta', 'z': 'et',
         'vra': 'vostra', 'dl': 'del', 'dla': 'dela', 'lra': 'littera', 'pnte': 'presente'}
def clear_words(clear, expand):
    out = []
    for _, txt in clear:
        for x in txt.split():
            raw = re.sub(r'[\^.]', '', x.lower())
            w = norm(raw) if raw != 'nõ' else 'nõ'
            if not w: continue
            if expand and w in SIGLA: w = SIGLA[w]
            out.append(norm(w))
    return [w for w in out if w]
def items(cipher):
    # ('w', word) clear word in the cipher slip; ('g', [signs]) one group; boundaries at '|', at clear words and at line ends
    out = []
    for _, txt in cipher:
        cur = []
        def flush():
            nonlocal cur
            if cur: out.append(('g', cur)); cur = []
        for m in re.finditer(r'<([^>]*)>|(\|)|([^<|]+)', txt):
            if m.group(1) is not None:
                flush(); w = norm(m.group(1))
                if w: out.append(('w', w))
            elif m.group(2): flush()
            else:
                for t in m.group(3).split():
                    t = t.rstrip('*')
                    if t and t not in (':', '.', '-', ',', ';'): cur.append(t)
        flush()
    return out
def dp(groups, words):
    n, m = len(groups), len(words); INF = float('inf')
    gs = [len(g) for g in groups]; wl = [len(w) for w in words]
    C = [[INF] * (m + 1) for _ in range(n + 1)]; B = [[None] * (m + 1) for _ in range(n + 1)]; C[0][0] = 0
    for i in range(n + 1):
        for j in range(m + 1):
            if C[i][j] == INF: continue
            if i < n and C[i][j] + 1 < C[i + 1][j]: C[i + 1][j] = C[i][j] + 1; B[i + 1][j] = (i, j, 'skip')
            if j < m and C[i][j] + 1 < C[i][j + 1]: C[i][j + 1] = C[i][j] + 1; B[i][j + 1] = (i, j, 'skip')
            for k in (1, 2, 3):
                for l in (1, 2, 3):
                    if k + l > 4 or i + k > n or j + l > m: continue
                    S, L = sum(gs[i:i + k]), sum(wl[j:j + l])
                    c = C[i][j] + abs(S - L) / L + 0.1 * (k + l - 2)
                    if c < C[i + k][j + l]: C[i + k][j + l] = c; B[i + k][j + l] = (i, j, 'pair')
    pairs, i, j = [], n, m
    while (i, j) != (0, 0):
        pi, pj, t = B[i][j]
        if t == 'pair': pairs.append((pi, i, pj, j))
        i, j = pi, pj
    return pairs[::-1]
def main(out, specs, expand):
    rows = []
    for spec in specs:
        slip, path = spec.split(':', 1)
        cipher, clear = parse(path)
        it = items(cipher); cw = clear_words(clear, expand)
        wi = [i for i, (k, _) in enumerate(it) if k == 'w']
        n, m = len(wi), len(cw)
        L = [[0] * (m + 1) for _ in range(n + 1)]
        for i in range(n - 1, -1, -1):
            for j in range(m - 1, -1, -1):
                L[i][j] = L[i + 1][j + 1] + 1 if ed1(it[wi[i]][1], cw[j]) else max(L[i + 1][j], L[i][j + 1])
        anchors, i, j = [], 0, 0
        while i < n and j < m:
            if ed1(it[wi[i]][1], cw[j]) and L[i][j] == L[i + 1][j + 1] + 1: anchors.append((wi[i], j)); i += 1; j += 1
            elif L[i + 1][j] >= L[i][j + 1]: i += 1
            else: j += 1
        bounds = [(-1, -1)] + anchors + [(len(it), m)]
        nsp = 0
        for s, ((a0, c0), (a1, c1)) in enumerate(zip(bounds, bounds[1:])):
            groups = [g for k, g in it[a0 + 1:a1] if k == 'g']; words = cw[c0 + 1:c1]
            if not groups or not words: continue
            nsp += 1
            for p, (g0, g1, w0, w1) in enumerate(dp(groups, words)):
                rows.append((f'{slip}_s{s:02d}_p{p:02d}', ''.join(words[w0:w1]), ' '.join(t for g in groups[g0:g1] for t in g),
                             ' '.join(words[w0:w1])))
        print(f'{slip} {path}: {len(wi)} clear words in cipher slip, {m} clear-slip words, {len(anchors)} anchors, {nsp} spans, '
              f'{sum(1 for r in rows if r[0].startswith(slip + "_"))} short pairs', file=sys.stderr)
    w = csv.writer(open(out, 'w'), delimiter='\t', lineterminator='\n')
    w.writerow(['crop', 'gloss_above', 'signs', 'clear_context']); [w.writerow(r) for r in rows]
if __name__ == '__main__':
    a = sys.argv[1:]; ex = '--expand' in a; a = [x for x in a if x != '--expand']
    main(a[0], a[1:], ex)

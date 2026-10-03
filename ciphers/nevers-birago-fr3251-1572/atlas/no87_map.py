# TX-ATLAS-B72 (3 Oct 2026): map the atlas's segmented boxes on no.87 (f.178v L01-23, f.179r L01-03) to the line-read
# token positions (harvest/ciphertext_*.tsv), so each box inherits the token's line-read sign and the clerk-sheet truth
# (harvest/align87/align_real.tsv plain_chunk). The alignment is LABEL-BLIND: a per-line DP over box widths only
# (1 box:1 token, 2 boxes:1 token, 1 box:2 tokens, skip a box, skip a token), so neither side's sign labels steer it.
# f.178r is left out: its three lines slope across one another and the segmenter's line split mixes them.
# Run from the repo root: python3 ciphers/nevers-birago-fr3251-1572/atlas/no87_map.py -> atlas/no87_box_token.tsv
import csv, os, collections, math
R = os.path.dirname(os.path.abspath(__file__)); H = os.path.join(R, '..', 'harvest')
rd = lambda p: list(csv.DictReader(open(p), delimiter='\t'))
S = rd(os.path.join(R, 'signs.tsv'))
TUNE = {f'f178v_L{i:02d}' for i in range(1, 13)}          # names clusters; everything else is held out


def dp(bw, n, W):
    m = len(bw); INF = 1e9
    C = [[INF] * (n + 1) for _ in range(m + 1)]; B = [[None] * (n + 1) for _ in range(m + 1)]; C[0][0] = 0
    for i in range(m + 1):
        for j in range(n + 1):
            c = C[i][j]
            if c >= INF: continue
            opts = []
            if i < m and j < n: opts.append((i + 1, j + 1, abs(math.log(bw[i] / W)), '1:1'))
            if i + 1 < m and j < n: opts.append((i + 2, j + 1, 1.0 + abs(math.log((bw[i] + bw[i + 1]) / W)), '2:1'))
            if i < m and j + 1 < n: opts.append((i + 1, j + 2, 1.0 + abs(math.log(bw[i] / (2 * W))), '1:2'))
            if i < m: opts.append((i + 1, j, 1.2 if bw[i] < 0.5 * W else 2.5, 'skipbox'))
            if j < n: opts.append((i, j + 1, 2.5, 'skiptok'))
            for a, b, k, op in opts:
                if c + k < C[a][b]: C[a][b] = c + k; B[a][b] = (i, j, op)
    path, i, j = [], m, n
    while (i, j) != (0, 0):
        pi, pj, op = B[i][j]; path.append((pi, pj, op)); i, j = pi, pj
    return path[::-1]


def main():
    out = []
    for fol, lines in (('f178v', range(1, 24)), ('f179r', range(1, 4))):
        toks = rd(os.path.join(H, f'ciphertext_{fol}.tsv'))
        al = {int(r['idx']): r['plain_chunk'] for r in rd(os.path.join(H, 'align87', 'align_real.tsv')) if r['cipher_line'] == fol}
        for k, t in enumerate(toks): t['idx'] = k
        W = sorted(int(s['w']) for s in S if s['page'] == fol)[len([s for s in S if s['page'] == fol]) // 2]
        for li in lines:
            bx = sorted([s for s in S if s['page'] == fol and int(s['line']) == li], key=lambda s: int(s['x']))
            tk = [t for t in toks if t['line'] == f'{fol}_L{li:02d}']
            for i, j, op in dp([int(s['w']) for s in bx], len(tk), W):
                if op == '1:1':
                    t = tk[j]; out.append(dict(sid=bx[i]['sid'], fol=fol, line=t['line'], pos=t['pos'], idx=t['idx'],
                                               sign=t['sign'], truth=al.get(t['idx'], ''), op=op,
                                               split='tune' if t['line'] in TUNE else 'heldout'))
                elif op in ('2:1', '1:2', 'skiptok'):
                    out.append(dict(sid=bx[i]['sid'] if op != 'skiptok' else '', fol=fol, line=tk[j]['line'],
                                    pos=tk[j]['pos'], idx=tk[j]['idx'], sign=tk[j]['sign'], truth='', op=op,
                                    split='tune' if tk[j]['line'] in TUNE else 'heldout'))
    cols = ['sid', 'fol', 'line', 'pos', 'idx', 'sign', 'truth', 'op', 'split']
    with open(os.path.join(R, 'no87_box_token.tsv'), 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in out: f.write('\t'.join(str(r[c]) for c in cols) + '\n')
    print(collections.Counter((r['split'], r['op']) for r in out))


if __name__ == '__main__':
    main()

# TX-ATLAS-B72 (3 Oct 2026): map the atlas's segmented boxes on no.87 (f.178v L01-23, f.179r L01-03) to the line-read
# token positions (harvest/ciphertext_*.tsv), so each box inherits the token's line-read sign and the clerk-sheet truth
# (harvest/align87/align_real.tsv plain_chunk). The alignment is LABEL-BLIND: a per-line DP over box widths only
# (1 box:1 token, 2 boxes:1 token, 1 box:2 tokens, skip a box, skip a token), so neither side's sign labels steer it.
# f.178r is left out: its three lines slope across one another and the segmenter's line split mixes them.
# Run from the repo root: python3 ciphers/nevers-birago-fr3251-1572/atlas/no87_map.py -> atlas/no87_box_token.tsv
#
# --label-aware [--check] (BOXMAP-LA, 11 Oct 2026, account 3): the label-blind map above shifts whole stretches of a line by
# one token when it maps an extra box 1:1 (f178v L06: f178v_06_009, which the owner marked NOT-LETTER, takes token 9 and the
# next tiles land one late; TXE3-9 second check). This option writes atlas/no87_box_token_labelaware.tsv and
# atlas/no87_box_token_labelaware_lines.tsv with tools/box_token_align.py: the same DP and width costs, plus the owner's
# no.87 sorter statuses (sorter/no87/owner-sort-2026-10-04/settled_no87.tsv: not-letter skipped, bad-cut never 1:1) and
# truth-blind labels against the line read L (benchmark-tx/outputs/birago1572-no87/labels.tsv; the reconciled
# harvest/ciphertext_*.tsv sign also accepted): the atlas classify top-3 with every no.87 page held out
# (benchmark-tx/txeng/compare/topk_no87_allheld.tsv; labels.json "override" known answers not used) and the sorter seed
# pile's family (sorter/no87/seed.tsv), or the owner's pile family where he moved the tile. lam 1.5, neutral 0.5, own-label
# leave-one-out on. The old file stays as built (it is cited); the new one has no truth column and no truth file is read.
# --check exits 1 when the committed new map or its lines file differs from a fresh run (CLAUDE.md rule 7).
import csv, os, collections, math, re, sys
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


LINES = [f'f178v_L{i:02d}' for i in range(1, 24)] + [f'f179r_L{i:02d}' for i in range(1, 4)]
ROOT = os.path.normpath(os.path.join(R, '..', '..', '..'))
SORT = os.path.join(R, '..', 'sorter', 'no87')
NEW_MAP = os.path.join(R, 'no87_box_token_labelaware.tsv')
NEW_LINES = os.path.join(R, 'no87_box_token_labelaware_lines.tsv')
NEW_COLS = ['sid', 'fol', 'line', 'pos', 'idx', 'sign', 'op', 'split', 'labels', 'status', 'loo_pos', 'old_pos']


def fam(p):
    m = re.match(r'^(T\d+)(-[a-z])?$', (p or '').strip())
    return m.group(1) if m else None


def label_aware(check=False):
    sys.path.insert(0, os.path.join(ROOT, 'tools'))
    import box_token_align as BA
    rd2 = BA.rd
    L = [r for r in rd2(os.path.join(ROOT, 'benchmark-tx/outputs/birago1572-no87/labels.tsv')) if r['line'] in LINES]
    alt, idx, csign = [], {}, {}
    for fol in ('f178v', 'f179r'):
        for k, t in enumerate(rd2(os.path.join(H, f'ciphertext_{fol}.tsv'))):
            alt.append(t); idx[(t['line'], t['pos'])] = k; csign[(t['line'], t['pos'])] = t['sign']
    labels = BA.read_labels(os.path.join(ROOT, 'benchmark-tx/txeng/compare/topk_no87_allheld.tsv'))
    seed = {r['sid']: r for r in rd2(os.path.join(SORT, 'seed.tsv'))}
    settled = {r['sid']: r for r in rd2(os.path.join(SORT, 'owner-sort-2026-10-04', 'settled_no87.tsv'))}
    for sid, r in settled.items():
        f1 = fam(r['new_sign']) if r['status'] == 'moved' else fam(seed.get(sid, {}).get('seed'))
        if f1:
            labels[sid][f1] = 1.0
    status = {sid: BA.norm_status(r['status']) for sid, r in settled.items()}
    rows, per = BA.build_map(S, L, labels, status, LINES, BA.LAM, BA.NEUTRAL, True, alt)
    old = BA.read_old(os.path.join(R, 'no87_box_token.tsv'))
    for r in rows:
        k = (r['line'], str(r['pos']))
        r.update(fol=r['page'], idx=idx.get(k, ''), sign=csign.get(k, ''), split='tune' if r['line'] in TUNE else 'heldout',
                 old_pos=old[r['sid']][1] if r['sid'] in old else '')
    lines = BA.line_summary(rows, per, old)

    def text(cols, rs):
        return '\t'.join(cols) + '\n' + ''.join('\t'.join(str(r.get(c, '')) for c in cols) + '\n' for r in rs)
    t_map, t_lines = text(NEW_COLS, rows), text(BA.LINE_COLS, lines)
    chk = {sid: r['atlas'] for sid, r in seed.items()}      # the TXE3-9 second check's label: the tile's atlas k1
    for name, c in BA.check_report(rows, old, chk, L + alt):
        print(f'truth-free check (seed.tsv atlas label == read sign), {name}: {BA.fmt_check(c)}')
    print('ops', dict(collections.Counter(r['op'] for r in rows)), '| tiles moved', sum(x['moved'] for x in lines),
          '| old 1:1 tiles no longer one-token', sum(x['lost_11'] for x in lines))
    if check:
        ok = all(os.path.exists(p) and open(p).read() == t for p, t in ((NEW_MAP, t_map), (NEW_LINES, t_lines)))
        print('no87_map --label-aware --check:', 'current' if ok else 'STALE')
        return 0 if ok else 1
    open(NEW_MAP, 'w').write(t_map); open(NEW_LINES, 'w').write(t_lines)
    print('->', NEW_MAP, NEW_LINES)
    return 0


if __name__ == '__main__':
    if '--label-aware' in sys.argv:
        sys.exit(label_aware('--check' in sys.argv))
    main()

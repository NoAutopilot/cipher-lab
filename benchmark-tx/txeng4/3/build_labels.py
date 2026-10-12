#!/usr/bin/env python3
"""TXE4-3 ATLAS-NCA unit 1 (12 Oct 2026, account 3): machine labels for the Birago 1572 atlas with no owner and no known
answer. PREREG benchmark-tx/PREREG-txeng4-3.md "Machine labels".

  stage 1  line correspondence (truth-free, geometric + count-based) -> labels/signs_lines.tsv (atlas signs with page-local
           renumbered lines), labels/read_<page>.tsv (line, pos, sign; <page>_L<nn>), labels/agree_<page>.tsv (the agreed
           tokens: status agree, idA == idB, neither conf L, a T-code); then the width-only seed round
           (tools/box_token_align.py, lam 0, no labels) -> labels/round1_<page>.tsv and labels/step1_tokens.tsv (box, code).
  stage 3  after glyph_atlas.py classify --only-train-labels on step1 (labels/step2_topk.tsv): the label-aware round
           (--topk step2, lam 1.5, leave-one-out) -> labels/round2_<page>.tsv, each gated by tools/join_check.py (check
           labels = step-2 top-1, --steered); FAIL -> failing lines dropped, re-checked once; still FAIL or UNCHECKABLE ->
           the page contributes nothing. Agreed labels = tokens 1:1 at the same position in both rounds on a line whose
           per-line verdict is 'pass' -> labels/agreed_labels.tsv (box, code, page, line, pos).
  stage 4  A4: no.87's passA/passB agreement (LCS per line, runs >= 2) joined the same way -> labels/no87_round2.tsv,
           labels/no87_agreed.tsv.
Never reads a truth file, a sorter file, labels.json or atlas/no87_box_token*.tsv. Run from the repo root.
"""
import csv, os, sys, json, collections, subprocess
import numpy as np
sys.path.insert(0, 'tools')
import box_token_align as BA
import join_check as JC

A = 'ciphers/nevers-birago-fr3251-1572/atlas'; H = 'ciphers/nevers-birago-fr3251-1572/harvest'
W = 'benchmark-tx/txeng4/3'; M = f'{W}/labels'   # (maps/ holds a first run with two defects, uncommitted)
os.makedirs(M, exist_ok=True)
rd = BA.rd
# agreement file -> (page selector) : passage name -> atlas page
LEAVES = [('f139v', f'{H}/f139v/passC_agreement.tsv', lambda p: 'f139v'),
          ('f144r', f'{H}/f144r/passC_agreement.tsv', lambda p: 'f144r'),
          ('f162r', f'{H}/f162r/passC_agreement.tsv', lambda p: 'f162r'),
          ('f174r', f'{H}/f174r/passC_agreement.tsv', lambda p: 'f174r'),
          ('f174v', f'{H}/f174v/passC_agreement.tsv', lambda p: 'f174v'),
          ('f174vB', f'{H}/f174vB/passC_agreement.tsv', lambda p: 'f174vB' if p.startswith('L') else ('f175r' if p.startswith('R') else None)),
          ('f175v', f'{H}/f175v/passC_agreement.tsv', lambda p: 'f175v'),
          ('f184r', f'{H}/f184r/passC_agreement.tsv', lambda p: 'f184r'),
          ('f185r', f'{H}/f185r/passC_rest90_agreement.tsv', lambda p: p.split('_')[0])]
EVAL_PREFIX = ('f152r', 'f178r', 'f178v', 'f179r')
GAP = 0.45          # y-gap split, in median box heights


def passages():
    """{page: [(passage, [tokens...])]} tokens = dict(sign, ok) in file order."""
    out = collections.defaultdict(list)
    for leaf, fn, sel in LEAVES:
        cur = collections.OrderedDict()
        for r in rd(fn):
            page = sel(r['passage'])
            if page is None:
                continue
            sign = r['merged']                      # the reconciled reading's tokens only (= harvest/ciphertext_<leaf>.tsv)
            if not sign:
                continue
            ok = (r['status'] == 'agree' and r['idA'] == r['idB'] and sign.startswith('T')
                  and 'L' not in (r['confA'], r['confB']))
            cur.setdefault((page, r['passage']), []).append(dict(sign=sign, ok=ok))
        for (page, pas), toks in cur.items():
            out[page].append((pas, toks))
    return out


def kmeans1d(ys, k):
    """optimal 1-D k-clustering of sorted ys (DP on within-group SSE) -> list of k groups of indices."""
    n = len(ys); ys = np.asarray(ys, float)
    cs, cs2 = np.concatenate([[0], np.cumsum(ys)]), np.concatenate([[0], np.cumsum(ys ** 2)])
    def sse(i, j):            # [i, j)
        m = j - i; s = cs[j] - cs[i]; return (cs2[j] - cs2[i]) - s * s / m
    INF = float('inf'); D = [[INF] * (n + 1) for _ in range(k + 1)]; P = [[0] * (n + 1) for _ in range(k + 1)]
    D[0][0] = 0.0
    for g in range(1, k + 1):
        for j in range(g, n + 1):
            for i in range(g - 1, j):
                if D[g - 1][i] < INF:
                    v = D[g - 1][i] + sse(i, j)
                    if v < D[g][j]:
                        D[g][j], P[g][j] = v, i
    cuts = []; j = n
    for g in range(k, 0, -1):
        i = P[g][j]; cuts.append((i, j)); j = i
    return [list(range(i, j)) for i, j in reversed(cuts)]


def split_rows(signs_page):
    """atlas rows -> sub-rows by y-gap; returns list of lists of sign rows (top to bottom, x order inside)."""
    mh = float(np.median([int(s['h']) for s in signs_page]))
    rows = collections.defaultdict(list)
    for s in signs_page:
        rows[int(s['line'])].append(s)
    out = []
    for li in sorted(rows):
        bx = sorted(rows[li], key=lambda s: int(s['y']) + int(s['h']) / 2)
        ys = [int(s['y']) + int(s['h']) / 2 for s in bx]
        cur = [bx[0]]
        for a, b, y0, y1 in zip(bx, bx[1:], ys, ys[1:]):
            if y1 - y0 > GAP * mh:
                out.append(cur); cur = []
            cur.append(b)
        out.append(cur)
    return [sorted(g, key=lambda s: int(s['x'])) for g in out], mh


def assign(subrows, pas, mh=None):
    """monotone DP: passages (ordered) -> sub-rows (ordered); a sub-row takes 0 or 1 passage, or k>=2 consecutive
    passages only when its boxes' y-centre spread (p90 - p10) exceeds 0.8 median heights (two baselines in one row);
    cost |boxes - tokens| per assigned sub-row. Returns {subrow index: [passage indices]}."""
    R, P = len(subrows), len(pas)
    b = [len(g) for g in subrows]; t = [len(tk) for _, tk in pas]
    def spread(g):
        ys = [int(s['y']) + int(s['h']) / 2 for s in g]
        return (np.percentile(ys, 90) - np.percentile(ys, 10)) if len(ys) > 1 else 0.0
    multi = [mh is None or spread(g) > 0.8 * mh for g in subrows]
    INF = float('inf')
    D = [[INF] * (P + 1) for _ in range(R + 1)]; back = {}
    D[0][0] = 0.0
    for r in range(1, R + 1):
        for p in range(P + 1):
            # sub-row r-1 takes passages q..p-1 (q == p: none)
            for q in range(p, -1, -1):
                if D[r - 1][q] == INF or (p - q >= 2 and not multi[r - 1]):
                    continue
                c = 0.0 if q == p else abs(b[r - 1] - sum(t[q:p])) + 0.5 * (p - q - 1) * 0  # k passages in one sub-row
                v = D[r - 1][q] + c
                if v < D[r][p]:
                    D[r][p], back[(r, p)] = v, q
    out = {}; p = P
    for r in range(R, 0, -1):
        q = back[(r, p)]
        if q < p:
            out[r - 1] = list(range(q, p))
        p = q
    return out, D[R][P]


def stage1():
    S = rd(f'{A}/signs.tsv')
    pas = passages()
    new_signs = []; log = []
    for page in sorted(pas):
        sp = [s for s in S if s['page'] == page]
        subrows, mh = split_rows(sp)
        asg, cost = assign(subrows, pas[page], mh)
        lines = []            # (passage, boxes)
        for ri, g in enumerate(subrows):
            pidx = asg.get(ri)
            if not pidx:
                lines.append((None, g)); continue
            if len(pidx) == 1:
                lines.append((pas[page][pidx[0]][0], g)); continue
            ys = [int(s['y']) + int(s['h']) / 2 for s in sorted(g, key=lambda s: int(s['y']) + int(s['h']) / 2)]
            gs = sorted(g, key=lambda s: int(s['y']) + int(s['h']) / 2)
            for k, grp in zip(pidx, kmeans1d(ys, len(pidx))):
                lines.append((pas[page][k][0], sorted([gs[i] for i in grp], key=lambda s: int(s['x']))))
        read = []; agree = []
        for ln, (pname, g) in enumerate(lines, 1):
            for k, s in enumerate(g, 1):
                r = dict(s); r['line'] = str(ln); r['pos'] = str(k); new_signs.append(r)
            if pname is None:
                log.append(f'{page} line {ln:02d}: {len(g)} boxes, no passage (prose)'); continue
            toks = dict(pas[page])[pname]
            log.append(f'{page} line {ln:02d} <- {pname}: {len(g)} boxes, {len(toks)} tokens, {sum(t["ok"] for t in toks)} agreed')
            for k, t in enumerate(toks, 1):
                read.append(dict(line=f'{page}_L{ln:02d}', pos=str(k), sign=t['sign']))
                if t['ok']:
                    agree.append(dict(line=f'{page}_L{ln:02d}', pos=str(k), sign=t['sign'], passage=pname))
        BA.wr(f'{M}/read_{page}.tsv', ['line', 'pos', 'sign'], read)
        BA.wr(f'{M}/agree_{page}.tsv', ['line', 'pos', 'sign', 'passage'], agree)
        log.append(f'{page}: assignment cost {cost:.0f}; {len(read)} tokens, {len(agree)} agreed')
    cols = list(S[0].keys())
    BA.wr(f'{M}/signs_lines.tsv', cols, new_signs)
    open(f'{M}/correspondence.txt', 'w').write('\n'.join(log) + '\n'); print('\n'.join(log))
    # seed round, width only
    tokens = []
    for page in sorted(pas):
        read = rd(f'{M}/read_{page}.tsv'); agree = {(r['line'], r['pos']): r['sign'] for r in rd(f'{M}/agree_{page}.tsv')}
        rows, per = BA.build_map(new_signs, read, None, None, sorted({r['line'] for r in read}), 0.0, BA.NEUTRAL, False)
        BA.wr(f'{M}/round1_{page}.tsv', ['sid', 'page', 'line', 'pos', 'op', 'labels', 'status', 'loo_pos'], rows)
        n = 0
        for r in rows:
            if r['op'] == '1:1' and (r['line'], str(r['pos'])) in agree:
                tokens.append(dict(box=r['sid'], code=agree[(r['line'], str(r['pos']))], page=page, line=r['line'], pos=r['pos'])); n += 1
        print(f'round1 {page}: 1:1 {sum(r["op"] == "1:1" for r in rows)}, agreed tokens {n}')
    BA.wr(f'{M}/step1_tokens.tsv', ['box', 'code', 'page', 'line', 'pos'], tokens)
    print('step1 tokens', len(tokens), dict(collections.Counter(t['page'] for t in tokens)))


def check_map(tag, rows, read_path, chk_path, lines_all):
    """write map, run join_check --steered; on FAIL drop failing lines and re-check once. Returns (kept_lines, verdicts)."""
    cols = ['sid', 'page', 'line', 'pos', 'op', 'labels', 'status', 'loo_pos']
    mp = f'{M}/{tag}.tsv'; BA.wr(mp, cols, rows)
    out = subprocess.run([sys.executable, 'tools/join_check.py', '--map', mp, '--check-labels', chk_path, '--read', read_path,
                          '--steered'], capture_output=True, text=True)
    res = json.load(open(JC.sidecar_path(mp)))
    txt = out.stdout.strip()
    v = res['verdict']
    print(f'{tag}: {v} n={res["n"]} 0/-1/+1 {res["overall"]}\n{txt}')
    if v == 'PASS':
        return [l for l, d in res['lines'].items() if d['verdict'] == 'pass'], (v, None), txt
    if v == 'UNCHECKABLE':
        return [], (v, None), txt
    bad = [l for l, d in res['lines'].items() if d['verdict'] == 'fail']
    rows2 = [r for r in rows if r['line'] not in bad]
    mp2 = f'{M}/{tag}_recheck.tsv'; BA.wr(mp2, cols, rows2)
    out2 = subprocess.run([sys.executable, 'tools/join_check.py', '--map', mp2, '--check-labels', chk_path, '--read', read_path,
                           '--steered'], capture_output=True, text=True)
    res2 = json.load(open(JC.sidecar_path(mp2))); v2 = res2['verdict']
    txt2 = f'dropped {bad}; recheck: {v2} n={res2["n"]} {res2["overall"]}\n' + out2.stdout.strip()
    print(txt2)
    if v2 == 'PASS':
        return [l for l, d in res2['lines'].items() if d['verdict'] == 'pass'], (v, v2), txt + '\n' + txt2
    return [], (v, v2), txt + '\n' + txt2


def stage3():
    S = rd(f'{M}/signs_lines.tsv')
    topk = rd(f'{M}/step2_topk.tsv')
    chk = [dict(sid=r['box'], label=r['k1']) for r in topk if r['k1'] not in ('', '_', '_held')]
    BA.wr(f'{M}/step2_top1.tsv', ['sid', 'label'], chk)
    labels = BA.read_labels(topk=f'{M}/step2_topk.tsv')
    pas = sorted({r['page'] for r in S if os.path.exists(f'{M}/read_{r["page"]}.tsv')})
    agreed = []; report = []
    for page in pas:
        read = rd(f'{M}/read_{page}.tsv'); agree = {(r['line'], r['pos']): r['sign'] for r in rd(f'{M}/agree_{page}.tsv')}
        r1 = {r['sid']: (r['line'], str(r['pos'])) for r in rd(f'{M}/round1_{page}.tsv') if r['op'] == '1:1'}
        lines = sorted({r['line'] for r in read})
        rows, per = BA.build_map(S, read, labels, None, lines, BA.LAM, BA.NEUTRAL, True)
        kept, verd, txt = check_map(f'round2_{page}', rows, f'{M}/read_{page}.tsv', f'{M}/step2_top1.tsv', lines)
        n = 0
        for r in rows:
            key = (r['line'], str(r['pos']))
            if r['op'] == '1:1' and r['line'] in kept and key in agree and r1.get(r['sid']) == key:
                agreed.append(dict(box=r['sid'], code=agree[key], page=page, line=r['line'], pos=r['pos'])); n += 1
        report.append(f'{page}: verdict {verd}, lines kept {len(kept)}/{len(lines)}, agreed labels {n}\n{txt}')
    BA.wr(f'{M}/agreed_labels.tsv', ['box', 'code', 'page', 'line', 'pos'], agreed)
    open(f'{M}/round2_report.txt', 'w').write('\n\n'.join(report) + '\n')
    print('AGREED LABELS', len(agreed), dict(collections.Counter(t['page'] for t in agreed)))
    print('per code', dict(sorted(collections.Counter(t['code'] for t in agreed).items())))


def lcs(a, b):
    n, m = len(a), len(b)
    T = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            T[i][j] = T[i + 1][j + 1] + 1 if a[i] == b[j] else max(T[i + 1][j], T[i][j + 1])
    i = j = 0; out = []
    while i < n and j < m:
        if a[i] == b[j]: out.append((i, j)); i += 1; j += 1
        elif T[i + 1][j] >= T[i][j + 1]: i += 1
        else: j += 1
    return out


def stage4():
    """A4: no.87 passA/passB agreement -> box_token_align (atlas signs.tsv as is: f178v/f179r row li = letter line Lli;
    f178r rows 1-3 = L01-03), steered by step-2 top-3, checked by its top-1, leave-one-out."""
    S = rd(f'{A}/signs.tsv')
    pa = collections.defaultdict(list); pb = collections.defaultdict(list)
    for r in rd('benchmark-tx/outputs/birago1572-no87/passA.tsv'): pa[r['line']].append(r)
    for r in rd('benchmark-tx/outputs/birago1572-no87/passB.tsv'): pb[r['line']].append(r)
    read = []; agree = {}
    for line in sorted(pa):
        ta = sorted(pa[line], key=lambda r: int(r['pos'])); tb = sorted(pb.get(line, []), key=lambda r: int(r['pos']))
        m = lcs([t['sign'] for t in ta], [t['sign'] for t in tb]); ms = set(m)
        for k, t in enumerate(ta, 1):
            read.append(dict(line=line, pos=str(k), sign=t['sign']))
        for i, j in m:
            if ((i - 1, j - 1) in ms or (i + 1, j + 1) in ms) and ta[i]['sign'].startswith('T'):
                agree[(line, str(i + 1))] = ta[i]['sign']
    BA.wr(f'{M}/no87_read.tsv', ['line', 'pos', 'sign'], read)
    print('no87 passA tokens', len(read), 'A/B agreed (LCS runs>=2, T-code)', len(agree))
    labels = BA.read_labels(topk=f'{M}/step2_topk.tsv')
    lines = sorted(pa)
    rows, per = BA.build_map(S, read, labels, None, lines, BA.LAM, BA.NEUTRAL, True)
    kept, verd, txt = check_map('no87_round2', rows, f'{M}/no87_read.tsv', f'{M}/step2_top1.tsv', lines)
    out = []
    for r in rows:
        key = (r['line'], str(r['pos']))
        if r['op'] == '1:1' and r['line'] in kept and key in agree:
            out.append(dict(box=r['sid'], code=agree[key], page=r['page'], line=r['line'], pos=r['pos']))
    BA.wr(f'{M}/no87_agreed.tsv', ['box', 'code', 'page', 'line', 'pos'], out)
    open(f'{M}/no87_round2_report.txt', 'w').write(f'verdict {verd}; lines kept {len(kept)}/{len(lines)}; agreed {len(out)}\n{txt}\n')
    print('no87 agreed tiles', len(out), 'lines kept', len(kept), dict(collections.Counter(t['line'] for t in out)))


if __name__ == '__main__':
    {'1': stage1, '3': stage3, '4': stage4}[sys.argv[1]]()

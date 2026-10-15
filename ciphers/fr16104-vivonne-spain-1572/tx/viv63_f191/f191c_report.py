#!/usr/bin/env python3
"""VIV-F191C (15 Oct 2026): report-only analysis of pass E on f.191r L22-L36, PREREG-VIVF191C.md s.3-5.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv63_f191/f191c_report.py [--json OUT]

Reads f191r_passA-E via f191.py's clean(); never writes rec.tsv, decode.tsv or any reading. Prints the drift check (E, and C, D as
instrument controls), per-line err_2reader for E-A, E-B, E-C (and A-B, A-C, B-C), and the fourth-vote table on rec.tsv's flagged columns.
"""
import collections, json, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import f191  # noqa: E402
rp = f191.rp
LINES = ['L%02d' % i for i in range(22, 37)]
PASSES = dict(f191.PASSES, E=os.path.join(HERE, 'f191r_passE.tsv'))


def drift(P, p):
    ids = sorted(P['A']); rows = []
    for l in LINES:
        k = ids.index(l)
        s = lambda m: (lambda a: a[0] / max(1, a[1]))(f191.nw_agree(P[p].get(l, []), P['A'].get(m, [])))
        same = s(l); nb = max(s(ids[k - 1]) if k else 0, s(ids[k + 1]) if k + 1 < len(ids) else 0)
        rows.append((l, round(same, 3), round(nb, 3), same > nb))
    return sum(r[3] for r in rows), rows


def cols5(P, line):
    names = 'ABCDE'
    seqs = [P[p].get(line, []) for p in names]
    ref = seqs[0]
    cs = [[t] + [None] * 4 for t in ref]
    extra = collections.defaultdict(lambda: collections.defaultdict(list))
    for p in range(1, 5):
        last = -1
        for i, j in rp.nw(ref, seqs[p]):
            if i is not None:
                cs[i][p] = seqs[p][j] if j is not None else None; last = i
            else:
                extra[last][p].append(seqs[p][j])
    def ins(anchor):
        e = extra.get(anchor)
        if not e:
            return []
        n = max(len(v) for v in e.values())
        return [[None] + [e[p][t] if t < len(e[p]) else None for p in range(1, 5)] for t in range(n)]
    out = ins(-1)
    for i, c in enumerate(cs):
        out.append(c); out += ins(i)
    out = [[x if x is not None else '-' for x in c] for c in out]
    return [c for c in out if any(x != '-' for x in c[:4])]


def main():
    P = {p: f191.clean(f) for p, f in PASSES.items()}
    res = {}
    for p in 'ECD':
        ok, rows = drift(P, p)
        res['drift_' + p] = {'pass': ok, 'of': len(LINES), 'rows': rows}
        print(f'drift {p}: {ok}/{len(LINES)}  ' + ' '.join(f'{l}:{s}/{n}{"" if g else "*"}' for l, s, n, g in rows))
    pairs = ['EA', 'EB', 'EC', 'AB', 'AC', 'BC']
    per = {}
    tot = {q: [0, 0] for q in pairs}
    for l in LINES:
        per[l] = {}
        for q in pairs:
            a, n = f191.nw_agree(P[q[0]].get(l, []), P[q[1]].get(l, []))
            tot[q][0] += a; tot[q][1] += n
            per[l][q] = round(1 - a / max(1, n), 3)
    res['err_2reader_lines'] = per
    res['err_2reader_pooled'] = {q: round(1 - a / max(1, n), 3) for q, (a, n) in tot.items()}
    print('err_2reader per line (' + ' '.join(pairs) + ')')
    for l in LINES:
        print(' ', l, len(P['E'].get(l, [])), ' '.join(f'{per[l][q]:.3f}' for q in pairs))
    print('  pooled', ' '.join(f'{q} {v}' for q, v in res['err_2reader_pooled'].items()))
    # fourth vote on flagged columns (pre-oo-merge)
    tab = collections.Counter(); settle = collections.Counter(); nflag = 0; detail = []
    for l in LINES:
        for c in cols5(P, l):
            s, flag, how = f191.decide(c[:4])
            if s is None or not flag:
                continue
            nflag += 1
            e = c[4]
            if e == s:
                k = 'agrees-plurality'
            elif e == '-':
                k = 'dash'
            elif e in [x for x in c[:4] if x != '-']:
                k = 'agrees-minority'
            else:
                k = 'other-sign'
            tab[k] += 1
            s2, f2, h2 = f191.decide(c[:3] + [e])
            if not f2 and s2 is not None:
                settle['settled-same' if s2 == s else 'settled-different'] += 1
            elif not f2:
                settle['settled-drop'] += 1
            else:
                settle['still-flagged'] += 1
            detail.append((l, how, ' '.join(c), k, s2 or '-'))
    # rec.tsv flagged count on these lines, pre-merge (count '+'-joined oo rows by their parts)
    recflag = 0
    for ln in open(os.path.join(HERE, 'rec.tsv'), encoding='utf-8'):
        f = ln.rstrip('\n').split('\t')
        if f[0] in LINES and f[3] == '1':
            recflag += 1
    res['fourth_vote'] = {'flagged_columns': nflag, 'rec_tsv_flagged_rows': recflag, 'E': dict(tab), 'ABCE_vote': dict(settle),
                          'detail': detail}
    print(f'flagged columns L22-L36: {nflag} (rec.tsv flagged rows after oo merge: {recflag})')
    print('  E on them:', dict(tab))
    print('  A,B,C,E vote on them:', dict(settle))
    if '--json' in sys.argv:
        json.dump(res, open(sys.argv[sys.argv.index('--json') + 1], 'w'), indent=1)


if __name__ == '__main__':
    main()

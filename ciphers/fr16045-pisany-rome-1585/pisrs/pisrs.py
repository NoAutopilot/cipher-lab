#!/usr/bin/env python3
"""D4-PISRS (6 Oct 2026; pisrs/PREREG_pisrs.md): PIS1-KEY (a) re-run with only the 9 SETTLED tokens of pis2/t31_tokens.tsv
relabelled. pis1key.py imported unchanged (run_files, relabel_file, clear_of, ctrl86, control, identical).
    python3 pisrs/pisrs.py   -> pisrs/tx_relabel/*, pisrs/pisrs_result.json"""
import json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'pis1key'))
import pis1key as P
from pis1key import nw_score, dec, load_tokens

SET = {}
pos = {}
for ln in open(os.path.join(T, 'pis2/tokens_pos.tsv')).read().splitlines()[1:]:
    f = ln.split('\t'); pos[(f[0], f[1], int(f[2]))] = f[3]
ALL_T31 = {}
for ln in open(os.path.join(T, 'pis2/t31_tokens.tsv')).read().splitlines()[1:]:
    f = ln.split('\t'); k = (f[0], f[1], int(f[2]))
    ALL_T31.setdefault(f[0], []).append(k)
    if f[8].startswith('SETTLED-'):
        SET[k] = f[8].split('-')[1]


def relabel_some(body_by_line, picks):
    """picks: {(line, idx): newlabel}; idx over non-'/' tokens. Asserts the token is T31."""
    out = {}
    for lab, body in body_by_line.items():
        t = body.split(); j = 0
        for n, x in enumerate(t):
            if x == '/':
                continue
            if (lab, j) in picks:
                assert x.rstrip('?').lstrip('?') == 'T31', (lab, j, x)
                t[n] = x.replace('T31', picks[(lab, j)])
            j += 1
        out[lab] = ' '.join(t)
    return out


def read(path):
    lines = []
    for ln in open(os.path.join(T, path)):
        if ln.strip():
            lab, body = ln.rstrip('\n').split('\t', 1); lines.append((lab, body))
        else:
            lines.append(None)
    return lines


def write(lines, new, dst):
    p = os.path.join(T, dst); os.makedirs(os.path.dirname(p), exist_ok=True)
    open(p, 'w').write(''.join('\n' if x is None else f'{x[0]}\t{new[x[0]]}\n' for x in lines))
    return dst


def check_context(leaf, path):
    lines = {x[0]: x[1].split() for x in read(path) if x}
    for (lf, l, i), ctx in pos.items():
        if lf != leaf:
            continue
        t = [x for x in lines[l] if x != '/']
        c = ctx.split(); m = c.index(next(x for x in c if x.startswith('[')))
        got = t[i - m:i - m + len(c)]
        want = [x.strip('[]') for x in c]
        assert [g.strip('?[]') for g in got] == [w.strip('?[]') for w in want], (lf, l, i, got, want)


def main():
    key = P.load_key(); out = {}
    pages = [('f244r', 'tx86', 'kp86/colbert_p49_50.txt', '', 0.284),
             ('f275r', 'tx86e', 'kp86d/colbert_p121_123.txt', 'Mais croyant que Monsieur de Luxembourg', 0.215)]
    for pg, d, cl, drop, err in pages:
        clear, ptext = P.clear_of(cl, drop)
        rec = f'{d}/ciphertext_{pg}.tsv'
        check_context(pg, rec)
        picks = {(l, i): v for (lf, l, i), v in SET.items() if lf == pg}
        lines = read(rec); body = {x[0]: x[1] for x in lines if x}
        newf = write(lines, relabel_some(body, picks), f'pisrs/tx_relabel/{d}_ciphertext_{pg}.tsv')
        old = [rec, f'{d}/passA.tsv', f'{d}/passB.tsv']
        r = {"err": err, "picks": {f'{l} i{i}': v for (l, i), v in sorted(picks.items())},
             "old": P.run_files(key, old, clear), "new": P.run_files(key, [newf], clear)}
        if pg == 'f244r':
            r["positive_control"] = P.ctrl86(key, ptext, clear, err)
        else:
            r["positive_control"] = P.control(key, ptext, clear, err, r["new"][newf]["decoded_letters"])
        print(pg, 'control', r["positive_control"]["passed"], '/5', flush=True)
        r["supported"] = bool(r["new"][newf]["score"] > r["old"][rec]["score"] and r["new"][newf]["above_both"])
        # descriptive (ii): random 9-token relabel null, same per-page count and target labels, nw_score only
        rnd = random.Random(20261006); cand = [(l, i) for (_, l, i) in ALL_T31[pg] if (pg, l, i) in pos]
        targets = sorted(picks.values()); draws = []
        for _ in range(200):
            pk = dict(zip(rnd.sample(cand, len(targets)), targets))
            toks = [t for t in ' '.join(relabel_some(body, pk)[x[0]] for x in lines if x).split()]
            tmp = write(lines, relabel_some(body, pk), 'pisrs/tx_relabel/_tmp.tsv')
            tk, _ = load_tokens(tmp); draws.append(float(nw_score(dec(tk, key), clear)))
        os.remove(os.path.join(T, 'pisrs/tx_relabel/_tmp.tsv'))
        draws.sort()
        r["random_relabel_null"] = {"n": 200, "mean": round(sum(draws) / 200, 4), "p95": round(draws[189], 4),
                                    "max": round(draws[-1], 4),
                                    "share_ge_settled": round(sum(x >= r["new"][newf]["score"] - 1e-9 for x in draws) / 200, 3)}
        r["identical"] = P.identical(newf, cl, key, {'T31': 'T36'})
        out[pg] = r
    out["supported_both"] = bool(out['f244r']["supported"] and out['f275r']["supported"])
    json.dump(out, open(os.path.join(H, 'pisrs_result.json'), 'w'), indent=1)
    print('supported_both', out["supported_both"])


if __name__ == '__main__':
    main()

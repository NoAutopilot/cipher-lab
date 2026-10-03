#!/usr/bin/env python3
"""GAPS23: score the 2077 legend decode against the plain Nota of 4.VEL 2078 (prereg.md in this folder).

  python3 score.py            -> result.tsv, confusion.tsv, regrade.tsv (candidates; applied only on PASS by apply step)
Reads ../../reading_2077_legend_nieuw_tokens.tsv, ../../ciphertext_2077_legend.tsv, nota2078.tsv (entry<TAB>text).
"""
import csv, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.normpath(os.path.join(HERE, '..', '..'))
GATING = [('q', 'b'), ('u', 'd'), ('r', 'k'), ('t', 'n'), ('p', 'c')]
SEED, DRAWS = 20261003, 2000
LETTERS = 'abcdefghijklmnopqrstuvwxyz'


def norm(s):
    s = s.lower().replace('ſ', 's').replace('ÿ', 'y').replace('ij', 'y').replace('&', 'en')
    return re.sub('[^a-z]', '', s)


def label_of(word):
    w = word[2:].rstrip('.:,')
    return w if len(w) == 1 else None


def entries_2077():
    """entry label -> list of (line, pos, valueset, grade, raw value)"""
    tok = {}
    with open(os.path.join(TGT, 'reading_2077_legend_nieuw_tokens.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            tok[(r['line'], int(r['pos']))] = (r['value'], r['grade'])
    out, cur = {}, None
    with open(os.path.join(TGT, 'ciphertext_2077_legend.tsv')) as f:
        rows = [l.rstrip('\n').split('\t') for l in f if not l.startswith('#')]
    for r in rows[1:]:
        line, pos, sign = r[0], int(r[1]), r[2]
        if sign.startswith('w:'):
            lab = label_of(sign)
            if lab is not None:
                cur = lab
                if cur in out:  # repeated label (2077 'e e e e'): keep the first run
                    cur = None
            continue
        if cur is None or (line, pos) not in tok:
            continue
        val, grade = tok[(line, pos)]
        out.setdefault(cur, [])
        if val == '?':
            out[cur].append((line, pos, frozenset(), grade, val))
        elif '|' in val:
            out[cur].append((line, pos, frozenset(norm(v) for v in val.split('|')), grade, val))
        else:
            for ch in norm(val):
                out[cur].append((line, pos, frozenset(ch), grade, val))
    return out


def align(toks, text):
    """NW: global on toks, free end gaps on text. Returns list aligned index into text (or None) per token."""
    n, m = len(toks), len(text)
    NEG = -10 ** 9
    S = [[0] * (m + 1) for _ in range(n + 1)]
    B = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        S[i][0], B[i][0] = -i, 1
    for j in range(1, m + 1):
        S[0][j], B[0][j] = 0, 2  # free leading text
    for i in range(1, n + 1):
        vs = toks[i - 1][2]
        for j in range(1, m + 1):
            d = S[i - 1][j - 1] + (2 if text[j - 1] in vs else -1)
            u = S[i - 1][j] - 1
            l = S[i][j - 1] - (0 if i == n else 1)  # free trailing text
            best = max(d, u, l)
            S[i][j] = best
            B[i][j] = 0 if best == d else (1 if best == u else 2)
    i, j, res = n, m, [None] * n
    while i > 0:
        b = B[i][j] if j > 0 else 1
        if b == 0:
            res[i - 1] = j - 1; i -= 1; j -= 1
        elif b == 1:
            i -= 1
        else:
            j -= 1
    return res


def stat(toks, text):
    al = align(toks, text)
    h = sum(1 for t in toks if t[3] == 'H')
    m = sum(1 for t, a in zip(toks, al) if t[3] == 'H' and a is not None and text[a] in t[2])
    return m, h, al


def permuted(toks, rng):
    p = list(LETTERS); rng.shuffle(p); mp = dict(zip(LETTERS, p))
    return [(a, b, frozenset(mp[c] for c in vs), g, r) for a, b, vs, g, r in toks]


def p99(xs):
    xs = sorted(xs); return xs[int(0.99 * (len(xs) - 1))]


def main():
    e77 = entries_2077()
    e78 = {}
    with open(os.path.join(HERE, 'nota2078.tsv')) as f:
        for r in csv.DictReader(f, delimiter='\t'):
            e78[r['entry'].strip()] = norm(r['text'])
    rng = random.Random(SEED)
    out = []
    M = H = 0
    per = {}
    for a, b in GATING:
        m, h, _ = stat(e77[a], e78[b]); M += m; H += h; per[(a, b)] = (m, h)
    real = M / H
    keys78 = sorted(e78)
    n1 = []
    for _ in range(DRAWS):
        mm = hh = 0
        for a, b in GATING:
            other = rng.choice([k for k in keys78 if k != b])
            m, h, _ = stat(e77[a], e78[other]); mm += m; hh += h
        n1.append(mm / hh)
    n2 = []
    for _ in range(DRAWS):
        mm = hh = 0
        for a, b in GATING:
            m, h, _ = stat(permuted(e77[a], rng), e78[b]); mm += m; hh += h
        n2.append(mm / hh)
    thr = max(p99(n1), p99(n2))
    verdict = 'PASS' if real > thr else 'FAIL'
    lines = ['pair\tH_match\tH\tA\tN1_pair_p99\tN1_pair_mean']
    pair_p99 = {}
    for a, b in GATING:
        m, h = per[(a, b)]
        xs = [stat(e77[a], e78[rng.choice([k for k in keys78 if k != b])])[0] / h for _ in range(DRAWS)]
        pair_p99[(a, b)] = p99(xs)
        lines.append(f'77{a}-78{b}\t{m}\t{h}\t{m/h:.3f}\t{p99(xs):.3f}\t{sum(xs)/len(xs):.3f}')
    lines.append(f'POOLED\t{M}\t{H}\t{real:.3f}\tN1_p99={p99(n1):.3f} N1_mean={sum(n1)/len(n1):.3f}\t'
                 f'N2_p99={p99(n2):.3f} N2_mean={sum(n2)/len(n2):.3f}')
    lines.append(f'VERDICT\t{verdict}\tthreshold={thr:.3f}\tN1_above_real={sum(x>=real for x in n1)}/{DRAWS}\t'
                 f'N2_above_real={sum(x>=real for x in n2)}/{DRAWS}')
    open(os.path.join(HERE, 'result.tsv'), 'w').write('\n'.join(lines) + '\n')
    print('\n'.join(lines))
    # confusion + regrade candidates on gating pairs
    conf, cand = {}, []
    for a, b in GATING:
        toks, text = e77[a], e78[b]
        _, _, al = stat(toks, text)
        hidx = [i for i, t in enumerate(toks) if t[3] == 'H']
        for i, (t, x) in enumerate(zip(toks, al)):
            got = text[x] if x is not None else '-'
            if t[3] == 'H':
                conf[(t[4], got)] = conf.get((t[4], got), 0) + 1
            if t[3] in ('M', 'U') and x is not None:
                left = [k for k in hidx if k < i][-3:]; right = [k for k in hidx if k > i][:3]
                ctx = left + right
                ok_ctx = len(ctx) >= 2 and all(al[k] is not None and text[al[k]] in toks[k][2] for k in ctx)
                ok_val = (t[3] == 'U') or (got in t[2])
                cand.append((f'77{a}-78{b}', t[0], t[1], t[4], t[3], got, 'yes' if ok_ctx else 'no',
                             'yes' if ok_val else 'no', 'APPLY' if (ok_ctx and ok_val) else 'keep'))
    with open(os.path.join(HERE, 'confusion.tsv'), 'w') as f:
        f.write('H_value\taligned_2078\tcount\n')
        for (v, g), c in sorted(conf.items(), key=lambda kv: -kv[1]):
            f.write(f'{v}\t{g}\t{c}\n')
    with open(os.path.join(HERE, 'regrade.tsv'), 'w') as f:
        f.write('pair\tline\tpos\tvalue\tgrade\taligned_2078\tctx_ok\tvalue_ok\taction\n')
        for c in cand:
            f.write('\t'.join(map(str, c)) + '\n')
    print(f'regrade candidates: {sum(c[-1]=="APPLY" for c in cand)} APPLY of {len(cand)} M/U aligned')
    return 0


if __name__ == '__main__':
    sys.exit(main())

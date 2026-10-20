#!/usr/bin/env python3
"""M-row pass for the Entick 1781 reading (SHERWOOD-MROWS, 20 Oct 2026; PREREG-SHERWOOD-MROWS.md).

A second column chooser: an interpolated Kneser-Ney word trigram on tools/data/en18, Viterbi over the full col 1 / col 2
lattice per message, the same candidates decode_entick.py builds (image cells, wraps, OCR for the controls). The margin of a
position is the best path through the chosen column minus the best path forced through the other column (max-marginals).
Nothing from Sherwood's sketch enters the model or the lattice.

  python3 mrows.py gate1        known-answer gate 1: the bigram's S rows with margin >= 4, recovered by the trigram
  python3 mrows.py gate2        known-answer gate 2: held-out en18 passages with random Entick distractors, leave-one-file-out
  python3 mrows.py controls     W+1, W-1, 20 P-shuffles (OCR only), mean trigram log-prob per word
  python3 mrows.py mrows        the M rows: bigram margin, trigram pick and margin, proposed grade
Outputs go to mrows/ (TSV).
"""
import math, os, random, re, sys, gzip
from collections import Counter, defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import decode_entick as de  # noqa: E402

OUT = os.path.join(HERE, 'mrows')
D = 0.75


def corpus_words(skip=None):
    for f in sorted(os.listdir(de.EN18)):
        if not f.endswith('.gz') or f == skip:
            continue
        yield None  # document boundary
        for line in gzip.open(os.path.join(de.EN18, f), 'rt', encoding='utf-8', errors='ignore'):
            for w in re.findall(r"[a-z]+", line.lower()):
                yield w


class KN3:
    """Interpolated Kneser-Ney trigram (one discount D at every order), unigram floor for unseen words."""
    def __init__(self, skip=None):
        c3, c2 = Counter(), Counter()
        uni = Counter()
        a = b = None
        for w in corpus_words(skip):
            if w is None:
                a = b = None
                continue
            uni[w] += 1
            if b is not None:
                c2[(b, w)] += 1
                if a is not None:
                    c3[(a, b, w)] += 1
            a, b = b, w
        self.uni = uni
        self.c3 = c3
        self.c2 = c2
        # context totals and type counts
        self.ctx3 = Counter(); self.n3 = Counter()
        for (x, y, z), n in c3.items():
            self.ctx3[(x, y)] += n; self.n3[(x, y)] += 1
        # continuation counts for the bigram level: N1+(., y, z)
        self.cont2 = Counter(); self.cont2ctx = Counter(); self.cont2n = Counter()
        for (x, y, z) in c3:
            self.cont2[(y, z)] += 1
        for (y, z), n in self.cont2.items():
            self.cont2ctx[y] += n; self.cont2n[y] += 1
        # unigram continuation N1+(., z)
        self.cont1 = Counter()
        for (y, z) in c2:
            self.cont1[z] += 1
        self.cont1tot = sum(self.cont1.values())
        self.V = len(uni) + 1
        self.cache = {}

    def p1(self, z):
        return (self.cont1.get(z, 0) + 0.5) / (self.cont1tot + 0.5 * self.V)

    def p2(self, y, z):
        lo = self.p1(z)
        t = self.cont2ctx.get(y, 0)
        if not t:
            return lo
        return max(self.cont2.get((y, z), 0) - D, 0) / t + D * self.cont2n[y] / t * lo

    def lp(self, x, y, z):
        k = (x, y, z)
        if k in self.cache:
            return self.cache[k]
        if y is None:
            v = math.log(self.p1(z))
        else:
            lo = self.p2(y, z)
            t = self.ctx3.get((x, y), 0) if x is not None else 0
            if t:
                p = max(self.c3.get((x, y, z), 0) - D, 0) / t + D * self.n3[(x, y)] / t * lo
            else:
                p = lo
            v = math.log(p)
        self.cache[k] = v
        return v


def viterbi(seq, lm, force=None):
    """seq: list of candidate word lists (normalised). force: (i, j) fixes position i to candidate j. Returns
    (best score, path)."""
    n = len(seq)
    # state: (j_prev, j_cur); score
    st = {}
    for j, w in enumerate(seq[0]):
        if force and force[0] == 0 and force[1] != j:
            continue
        st[(None, j)] = (lm.lp(None, None, w), [j])
    for i in range(1, n):
        ns = {}
        for j, w in enumerate(seq[i]):
            if force and force[0] == i and force[1] != j:
                continue
            for (jp2, jp), (sc, path) in st.items():
                x = seq[i - 2][jp2] if jp2 is not None else None
                y = seq[i - 1][jp]
                s = sc + lm.lp(x, y, w)
                k = (jp, j)
                if k not in ns or s > ns[k][0]:
                    ns[k] = (s, path + [j])
        st = ns
    return max(st.values(), key=lambda v: v[0])


def choose3(seq, lm):
    if not seq:
        return [], []
    best, path = viterbi(seq, lm)
    margins = []
    for i, cands in enumerate(seq):
        if len(cands) < 2:
            margins.append(float('inf'))
            continue
        alt = max(viterbi(seq, lm, (i, j))[0] for j in range(len(cands)) if j != path[i])
        margins.append(best - alt)
    return path, margins


def lattice(msgs, img, grid, use_image=True, transform=None):
    """Per message: list of (token, live) where live = [(word, col, src)], plus the raw rows order."""
    out = []
    for name, toks in msgs:
        pos = []
        for t in toks:
            lid, kind, val = t
            if kind != 'pair':
                continue
            P, W = val[0], val[1]
            if transform:
                P, W = transform(P, W)
            cands = de.candidates(P, W, img, grid, use_image)
            live = [(w, k + 1, s) for k, (w, s) in enumerate(cands) if w]
            if live:
                pos.append((t, live))
        out.append((name, pos))
    return out


def run_choosers(lat, lm2, lm3):
    """Both choosers on every message; returns list of dicts per position."""
    res = []
    for name, pos in lat:
        seq_raw = [[(w, None) for (w, c, s) in live] for (t, live) in pos]
        pick2, m2 = de.choose(seq_raw, lm2)
        seq = [[de.norm(w) for (w, c, s) in live] for (t, live) in pos]
        pick3, m3 = choose3(seq, lm3)
        for k, (t, live) in enumerate(pos):
            res.append(dict(msg=name, line=t[0], val=t[2], live=live, p2=pick2[k], m2=m2[k], p3=pick3[k], m3=m3[k]))
    return res


def setup():
    toks = de.load_tokens()
    msgs = de.messages(toks)
    img, grid = de.load_image_entries(), de.load_ocr_grid()
    return toks, msgs, img, grid


def reading_grades():
    """group -> list of committed grades in order (from reading.tsv)."""
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(HERE, 'reading.tsv'))][1:]
    return [r for r in rows if r[2] == 'pair']


def gate1(lm2, lm3):
    toks, msgs, img, grid = setup()
    res = run_choosers(lattice(msgs, img, grid), lm2, lm3)
    held = [r for r in res if len(r['live']) == 2 and all(s == 'image' for _, _, s in r['live']) and r['m2'] >= 4.0]
    agree_full = sum(1 for r in held if r['p3'] == r['p2'])
    # fixed-context variant (the PREREG's wording): every other position held at the bigram's pick
    agree_fixed = 0
    by_msg = defaultdict(list)
    for r in res:
        by_msg[r['msg']].append(r)
    for r in held:
        rs = by_msg[r['msg']]
        seq = []
        for q in rs:
            ws = [de.norm(w) for (w, c, s) in q['live']]
            seq.append(ws if q is r else [ws[q['p2']]])
        _, path = viterbi(seq, lm3)
        i = rs.index(r)
        if path[i] == r['p2']:
            agree_fixed += 1
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'gate1.tsv'), 'w') as f:
        f.write('msg\tline\tgroup\tcol1\tcol2\tbigram_pick\tbigram_margin\ttrigram_pick\ttrigram_margin\n')
        for r in held:
            f.write('%s\t%s\t%d-%d\t%s\t%s\t%d\t%.2f\t%d\t%.2f\n' % (r['msg'], r['line'], r['val'][0], r['val'][1],
                    r['live'][0][0], r['live'][1][0], r['p2'] + 1, r['m2'], r['p3'] + 1, r['m3']))
    n = len(held)
    print('gate1: held-out S rows (bigram margin >= 4, two image candidates): %d' % n)
    print('  full lattice: trigram agrees %d/%d = %.3f' % (agree_full, n, agree_full / n))
    print('  fixed context: trigram agrees %d/%d = %.3f' % (agree_fixed, n, agree_fixed / n))
    print('  GATE (>= 0.90 on both): %s' % ('PASS' if min(agree_full, agree_fixed) / n >= 0.9 else 'FAIL'))


def gate2(seed=7, per_fold=4, plen=60):
    _, _, _, grid = setup()
    heads = sorted({de.norm(de.ocr_headword(v)) for v in grid.values()} - {''})
    files = sorted(f for f in os.listdir(de.EN18) if f.endswith('.gz'))
    rows = []
    for f in files:
        lm3 = KN3(skip=f)
        lm2 = Bigram2(skip=f)
        words = [w for line in gzip.open(os.path.join(de.EN18, f), 'rt', encoding='utf-8', errors='ignore')
                 for w in re.findall(r"[a-z]+", line.lower())]
        rng = random.Random(seed + len(f))
        for k in range(per_fold):
            st = rng.randrange(len(words) // 10, len(words) - plen - 1)
            passage = words[st:st + plen]
            seq, truth = [], []
            for w in passage:
                d = rng.choice(heads)
                if rng.random() < 0.5:
                    seq.append([w, d]); truth.append(0)
                else:
                    seq.append([d, w]); truth.append(1)
            p3, m3 = choose3(seq, lm3)
            p2, m2 = de.choose([[(x, None) for x in s] for s in seq], lm2)
            for i in range(plen):
                rows.append((f, k, truth[i], p3[i], m3[i], p2[i], m2[i]))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'gate2.tsv'), 'w') as fo:
        fo.write('fold\tn\tall_tri\tn_tri_m2\tprec_tri_m2\tall_bi\tn_bi_m2\tprec_bi_m2\n')
        lines = []
        for f in files + ['POOLED']:
            rs = [r for r in rows if f == 'POOLED' or r[0] == f]
            at = sum(r[2] == r[3] for r in rs) / len(rs)
            ab = sum(r[2] == r[5] for r in rs) / len(rs)
            t2 = [r for r in rs if r[4] >= 2.0]; b2 = [r for r in rs if r[6] >= 2.0]
            pt = sum(r[2] == r[3] for r in t2) / len(t2) if t2 else float('nan')
            pb = sum(r[2] == r[5] for r in b2) / len(b2) if b2 else float('nan')
            ln = '%s\t%d\t%.3f\t%d\t%.3f\t%.3f\t%d\t%.3f' % (f, len(rs), at, len(t2), pt, ab, len(b2), pb)
            fo.write(ln + '\n'); lines.append(ln)
    print('\n'.join(lines))
    pooled = [r for r in rows if r[4] >= 2.0]
    prec = sum(r[2] == r[3] for r in pooled) / len(pooled)
    print('gate2 GATE (trigram precision at margin >= 2 pooled >= 0.90): %s (%.3f)' % ('PASS' if prec >= 0.9 else 'FAIL', prec))


class Bigram2(de.Bigram):
    """decode_entick's bigram, optionally leaving one en18 file out (gate 2's folds)."""
    def __init__(self, skip=None):
        uni, bi = Counter(), Counter()
        prev = None
        for w in corpus_words(skip):
            if w is None:
                continue
            uni[w] += 1
            if prev:
                bi[(prev, w)] += 1
            prev = w
        self.uni, self.bi, self.N, self.V = uni, bi, sum(uni.values()), len(uni) + 1


def score3(lat_res_words, lm3):
    tot = n = 0
    for ws in lat_res_words:
        for i, w in enumerate(ws):
            tot += lm3.lp(ws[i - 2] if i >= 2 else None, ws[i - 1] if i >= 1 else None, w); n += 1
    return tot / n if n else float('-inf')


def controls(lm2, lm3, seeds=20):
    toks, msgs, img, grid = setup()
    def arm(label, tf=None, ms=msgs, use_image=False):
        lat = lattice(ms, img, grid, use_image, tf)
        out = []
        for name, pos in lat:
            seq = [[de.norm(w) for (w, c, s) in live] for (t, live) in pos]
            if seq:
                best, path = viterbi(seq, lm3)
                out.append([seq[i][j] for i, j in enumerate(path)])
        return label, score3(out, lm3)
    rows = [arm('reading (image)', use_image=True), arm('reading (OCR only)'), arm('W plus 1', lambda P, W: (P, W + 1)),
            arm('W minus 1', lambda P, W: (P, max(W - 1, 1)))]
    pairs = [t[2] for t in toks if t[1] == 'pair']
    for s in range(seeds):
        rng = random.Random(1000 + s)
        Ps = [p[0] for p in pairs]; rng.shuffle(Ps)
        k = 0; new = []
        for name, tl in msgs:
            nl = []
            for t in tl:
                if t[1] == 'pair':
                    nl.append((t[0], 'pair', (Ps[k],) + tuple(t[2][1:]))); k += 1
                else:
                    nl.append(t)
            new.append((name, nl))
        rows.append(arm('P-shuffle seed %d' % s, None, new))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'controls3.tsv'), 'w') as f:
        f.write('arm\tmean_trigram_logp\n')
        for lab, sc in rows:
            f.write('%s\t%.4f\n' % (lab, sc))
    sh = [sc for lab, sc in rows if lab.startswith('P-shuffle')]
    for lab, sc in rows[:4]:
        print('%-22s %.4f' % (lab, sc))
    print('P-shuffle x%d: mean %.4f, max %.4f' % (len(sh), sum(sh) / len(sh), max(sh)))


def mrows(lm2, lm3):
    toks, msgs, img, grid = setup()
    res = run_choosers(lattice(msgs, img, grid), lm2, lm3)
    graded = reading_grades()
    # align committed rows with lattice positions (rows with live candidates, in order)
    live_rows = [r for r in graded if r[7]]
    assert len(live_rows) == len(res), (len(live_rows), len(res))
    out = []
    for g, r in zip(live_rows, res):
        if g[8] != 'M':
            continue
        two_img = len(r['live']) == 2 and all(s == 'image' for _, _, s in r['live'])
        unsure = '?' in g[3]
        eligible = two_img and not unsure
        new = 'S' if eligible and r['m3'] >= 2.0 else 'M'
        reason = ('ocr-only' if any(s == 'ocr' for _, _, s in r['live']) else 'unsure-digit' if unsure
                  else 'one-candidate' if len(r['live']) < 2 else 'column-margin')
        out.append((g[0], g[1], g[3], r['live'][0][0], r['live'][1][0] if len(r['live']) > 1 else '', r['p2'] + 1,
                    '%.2f' % r['m2'], r['p3'] + 1, '%.2f' % r['m3'], reason, new,
                    r['live'][r['p3']][0]))
    os.makedirs(OUT, exist_ok=True)
    with open(os.path.join(OUT, 'mrows.tsv'), 'w') as f:
        f.write('msg\tline\tgroup\tcol1\tcol2\tbigram_pick\tbigram_margin\ttrigram_pick\ttrigram_margin\treason\tproposed\ttrigram_word\n')
        for o in out:
            f.write('\t'.join(str(x) for x in o) + '\n')
    c = Counter(o[10] for o in out)
    print('M rows: %d; reasons %s; trigram >= 2.0 on eligible: %d -> S; changed column vs bigram: %d'
          % (len(out), dict(Counter(o[9] for o in out)), c['S'], sum(1 for o in out if o[5] != o[7])))
    for o in out:
        print('\t'.join(str(x) for x in o))


def main():
    cmd = sys.argv[1] if len(sys.argv) > 1 else 'mrows'
    if cmd == 'gate2':
        return gate2()
    lm2, lm3 = de.Bigram(), KN3()
    {'gate1': gate1, 'controls': controls, 'mrows': mrows}[cmd](lm2, lm3)


if __name__ == '__main__':
    main()

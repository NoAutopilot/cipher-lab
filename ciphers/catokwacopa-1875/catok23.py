"""catok23.py -- spec tests 2 and 3 for catokwacopa-1875 (R12-CATOK23, 6 Oct 2026), pre-registered in PREREG-CATOK23.md.

Our own code. The fit model (an order-preserving interleaving of the two ad halves is a subsequence of the reading;
the rest of the reading's letters are W.'s omissions) and the five name frames are David Bourdeau's
(cyphersolver, targets/catokwacopa, MIT; snapshot sources/cyphersolver/2026-10-02/catokwacopa/), read, not copied.

  python3 catok23.py build --src DIR   derive names.tsv.gz / vocab.tsv.gz from the fetched sources (manifest in NOTES.md)
  python3 catok23.py run               test 2 + test 3 with their controls -> catok23.json
  python3 catok23.py --check           re-run and exit 1 if catok23.json is stale
"""
import collections, glob, gzip, json, math, os, random, re, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OMIT, MAX_WORD_OMIT, MAX_LINE_OMIT, BEAM, MARGIN = 2.3, 4, 12, 60, 3.0
FRAMES = [(8, 'I ATTENDED {} LECSURS', 'CONINGTON'), (25, 'I ATTENDED {} LECSURS', 'JOWETT'),
          (24, 'TOLD {}', 'SHIRLEY'), (15, '{} TOLD US TO ADD A SECOND MOTTO', 'CONINGTON'),
          (10, '{} SCHOLARSHIP EXAMINATION', 'HERTFORD')]
UNREAD = [9, 12, 23, 26, 29]
IA = ['alumnioxonienses01univuoft', 'alumnioxonienses02univuoft', 'alumnioxonienses03univ',
      'alumnioxonienses04univuoft', 'historicalregist00univuoft']
PG = [26851, 4644, 40338, 145, 1023, 3409, 883, 5231, 1400, 98]


def pairs():
    out = {}
    for l in open(os.path.join(HERE, 'pairs.tsv')).read().splitlines()[1:]:
        f = l.split('\t')
        out[int(f[0])] = (f[2].lower(), f[3].lower())
    return out


# ---------- build ----------
def pg_body(t):
    s = t.find('*** START'); e = t.find('*** END')
    return t[t.find('\n', s) + 1 if s >= 0 else 0: e if e > 0 else len(t)]


def build(src):
    low, cap = collections.Counter(), collections.Counter()
    novels = [pg_body(open(os.path.join(src, 'pg%d.txt' % i), encoding='utf-8', errors='ignore').read()) for i in PG]
    ia = [open(os.path.join(src, i + '.txt'), encoding='utf-8', errors='ignore').read() for i in IA]
    for t in novels:
        low.update(re.findall(r'[a-z]+', t.lower()))
    surn = set()
    for t in ia[:4]:
        for m in re.finditer(r'(?m)^([A-Z][A-Za-z]{2,13}),\s', t):
            surn.add(m.group(1).upper())
    for t in novels + ia:
        for m in re.finditer(r'(?<=[a-z,;] )([A-Z][a-z]{2,13})\b', t):
            cap[m.group(1)] += 1
    wl = collections.Counter(re.findall(r'\b[a-z]{3,}\b', '\n'.join(novels)))
    caps = {w.upper() for w, c in cap.items() if c >= 3 and wl[w.lower()] <= c // 10}
    names = sorted(n for n in surn | caps if re.fullmatch('[A-Z]{3,14}', n))
    with gzip.open(os.path.join(HERE, 'catok23_names.tsv.gz'), 'wt') as fh:
        fh.write('\n'.join(names) + '\n')
    voc = {w: c for w, c in low.items() if c >= 3 and (len(w) > 1 or w in ('a', 'i'))}
    with gzip.open(os.path.join(HERE, 'catok23_vocab.tsv.gz'), 'wt') as fh:
        for w in sorted(voc): fh.write('%s\t%d\n' % (w, voc[w]))
    # the corpus word stream, for the synthetic control lines (compact: one novel-ordered token list)
    with gzip.open(os.path.join(HERE, 'catok23_stream.txt.gz'), 'wt') as fh:
        for t in novels: fh.write(' '.join(re.findall(r'[a-z]+', t.lower())) + '\n')
    print('names %d (surnames %d), vocab %d' % (len(names), len(surn), len(voc)))


def load():
    names = gzip.open(os.path.join(HERE, 'catok23_names.tsv.gz'), 'rt').read().split()
    cnt = {}
    for l in gzip.open(os.path.join(HERE, 'catok23_vocab.tsv.gz'), 'rt'):
        w, c = l.split('\t'); cnt[w] = int(c)
    stream = gzip.open(os.path.join(HERE, 'catok23_stream.txt.gz'), 'rt').read().split()
    return names, cnt, stream


# ---------- fit model ----------
def fit_omissions(P, A, B):
    """Minimum omissions for an exact (0-misprint) fit of letters P to streams A, B; None if no exact fit."""
    P = re.sub('[^a-z]', '', P.lower()); a, b = len(A), len(B)
    if len(P) < a + b: return None
    reach = {(0, 0)}
    for c in P:
        nxt = set(reach)
        for i, j in reach:
            if i < a and A[i] == c: nxt.add((i + 1, j))
            if j < b and B[j] == c: nxt.add((i, j + 1))
        reach = nxt
    return len(P) - a - b if (a, b) in reach else None


def synth(phrase_letters, omit, la, rng):
    keep = sorted(rng.sample(range(len(phrase_letters)), len(phrase_letters) - omit))
    s = [phrase_letters[k] for k in keep]
    ia = set(rng.sample(range(len(s)), la))
    return ''.join(s[k] for k in range(len(s)) if k in ia), ''.join(s[k] for k in range(len(s)) if k not in ia)


# ---------- test 2 ----------
def frame_fits(frame, A, B, names, maxom):
    out = []
    for n in names:
        o = fit_omissions(frame.format(n), A, B)
        if o is not None and o <= maxom: out.append((o, n))
    return sorted(out)


def test2(P, names, cnt, rng, nctl=50):
    nameset = set(names); res = []
    common = [w for w, c in cnt.items() if c >= 20 and w.upper() not in nameset and len(w) >= 3]
    for ln, frame, pub in FRAMES:
        A, B = P[ln]
        cand = sorted(set(names) | {pub})
        base = fit_omissions(frame.format(pub), A, B)
        fits = frame_fits(frame, A, B, cand, base)
        loose = frame_fits(frame, A, B, cand, base + 2)
        forced = [n for _, n in fits] == [pub]
        ctl = {}
        for kind, pool in (('null', [w.upper() for w in common if abs(len(w) - len(pub)) <= 2]),
                           ('pos', [n for n in names if abs(len(n) - len(pub)) <= 2])):
            uniq = anyf = hit = 0
            for _ in range(nctl):
                w = rng.choice(pool)
                letters = re.sub('[^a-z]', '', frame.format(w).lower())
                if len(letters) - base < len(A) + 1: continue
                a, b = synth(letters, base, len(A), rng)
                f = frame_fits(frame, a, b, cand if kind == 'null' else sorted(set(cand) | {w}), base)
                anyf += bool(f); uniq += len(f) == 1; hit += [n for _, n in f] == [w]
            ctl[kind] = {'n': nctl, 'any_fit': anyf / nctl, 'unique': uniq / nctl, 'planted_unique': hit / nctl}
        backed = forced and ctl['null']['unique'] <= 0.10 and ctl['pos']['planted_unique'] >= 0.50
        res.append({'line': ln, 'frame': frame, 'published': pub, 'published_omissions': base,
                    'fits_le_base': ['%s(%d)' % (n, o) for o, n in fits],
                    'fits_le_base_plus2': len(loose), 'fits_le_base_plus2_sample': ['%s(%d)' % (n, o) for o, n in loose[:12]],
                    'forced_under_our_list': forced, 'control': ctl, 'control_backed': backed})
        print('T2 line %d %s: %d fit <= %d om (%s); +2: %d; null uniq %.2f any %.2f; pos power %.2f; backed %s' % (
            ln, pub, len(fits), base, ','.join(n for _, n in fits[:6]), len(loose), ctl['null']['unique'],
            ctl['null']['any_fit'], ctl['pos']['planted_unique'], backed), flush=True)
    return res


# ---------- test 3 ----------
def trie(words):
    root = {}
    for w in words:
        node = root
        for ch in w: node = node.setdefault(ch, {})
        node['$'] = w
    return root


def edges(i0, j0, A, B, T):
    out, stack = {}, [(T, {(i0, j0): 0})]
    while stack:
        node, states = stack.pop()
        if '$' in node:
            w = node['$']
            for (i, j), om in states.items():
                if (i, j) != (i0, j0) and om < len(w):
                    k = (w, i, j)
                    if om < out.get(k, 99): out[k] = om
        for ch, child in node.items():
            if ch == '$': continue
            nxt = {}
            for (i, j), om in states.items():
                if i < len(A) and A[i] == ch and om < nxt.get((i + 1, j), 99): nxt[(i + 1, j)] = om
                if j < len(B) and B[j] == ch and om < nxt.get((i, j + 1), 99): nxt[(i, j + 1)] = om
                if om < MAX_WORD_OMIT and om + 1 < nxt.get((i, j), 99): nxt[(i, j)] = om + 1
            if nxt: stack.append((child, nxt))
    return [(w, i, j, om) for (w, i, j), om in out.items()]


def kbest(A, B, LP, T, K=20):
    a, b = len(A), len(B)
    best = collections.defaultdict(list); best[(0, 0)] = [(0.0, 0, ())]
    for (i, j) in sorted(((i, j) for i in range(a + 1) for j in range(b + 1)), key=lambda x: x[0] + x[1]):
        cur = best.get((i, j))
        if not cur or (i, j) == (a, b): continue
        cur.sort(reverse=True); del cur[BEAM:]
        for w, ni, nj, om in edges(i, j, A, B, T):
            s = LP[w] - OMIT * om
            lst = best[(ni, nj)]
            for sc, tot, ws in cur:
                if tot + om <= MAX_LINE_OMIT: lst.append((sc + s, tot + om, ws + (w,)))
            if len(lst) > 4 * BEAM:
                lst.sort(reverse=True); del lst[BEAM:]
    seen, final = set(), []
    for sc, tot, ws in sorted(best[(a, b)], reverse=True):
        if ws not in seen: seen.add(ws); final.append((round(sc, 3), tot, ' '.join(ws)))
    return final[:K]


def verdict(res):
    if not res: return False, None
    return (len(res) == 1 or res[0][0] - res[1][0] >= MARGIN), (res[0][0] - res[1][0] if len(res) > 1 else None)


def test3(P, cnt, stream, rng, nctl=20):
    tot = sum(cnt.values()); LP = {w: math.log(c / tot) for w, c in cnt.items()}; T = trie(LP)
    out = []
    for ln in UNREAD:
        A, B = P[ln]; L = len(A) + len(B)
        r = kbest(A, B, LP, T); u, m = verdict(r)
        ctl = {'unique': 0, 'correct_unique': 0, 'wrong_unique': 0, 'planted_in_top20': 0, 'n': 0, 'examples': []}
        while ctl['n'] < nctl:
            target = L + rng.randint(3, 12)
            k = rng.randrange(len(stream) - 40); ws = []
            while sum(map(len, ws)) < target: ws.append(stream[k]); k += 1
            if sum(map(len, ws)) - L > 12 or any(w not in cnt for w in ws): continue
            a, b = synth(''.join(ws), sum(map(len, ws)) - L, len(A), rng)
            rr = kbest(a, b, LP, T); uu, _ = verdict(rr)
            planted = ' '.join(ws); top = rr[0][2] if rr else None
            ctl['n'] += 1; ctl['unique'] += uu
            ctl['correct_unique'] += uu and top == planted; ctl['wrong_unique'] += uu and top != planted
            ctl['planted_in_top20'] += any(x[2] == planted for x in rr)
            if len(ctl['examples']) < 3: ctl['examples'].append({'planted': planted, 'A': a, 'B': b, 'top': top})
        for k in ('unique', 'correct_unique', 'wrong_unique', 'planted_in_top20'): ctl[k] = ctl[k] / nctl
        if not u: tv = 'not unique'
        elif ctl['correct_unique'] >= 0.5 and ctl['wrong_unique'] <= 0.10: tv = 'unique, control-backed (S)'
        else: tv = 'unique but control fails gate (M at most)'
        if ctl['correct_unique'] < 0.5: tv += '; untestable by this method at this length (R_c < 0.50)'
        elif not u: tv += '; control-backed not forced'
        out.append({'line': ln, 'A': A, 'B': B, 'letters': L, 'unique': u, 'margin': m, 'top5': r[:5],
                    'n_readings_kept': len(r), 'control': ctl, 'verdict': tv})
        print('T3 line %d (%d letters): unique %s margin %s top %s | ctl uniq %.2f correct %.2f wrong %.2f top20 %.2f | %s' % (
            ln, L, u, m if m is None else round(m, 2), r[0][2] if r else None, ctl['unique'], ctl['correct_unique'],
            ctl['wrong_unique'], ctl['planted_in_top20'], tv), flush=True)
    return out


def run():
    P = pairs(); names, cnt, stream = load()
    rng = random.Random(2023)
    res = {'prereg': 'PREREG-CATOK23.md', 'n_names': len(names), 'n_vocab': len(cnt),
           'test2': test2(P, names, cnt, rng), 'test3': test3(P, cnt, stream, rng)}
    return res


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['build']: build(a[a.index('--src') + 1])
    elif a[:1] == ['run']:
        json.dump(run(), open(os.path.join(HERE, 'catok23.json'), 'w'), indent=1)
    elif a[:1] == ['--check']:
        new = json.loads(json.dumps(run()))
        old = json.load(open(os.path.join(HERE, 'catok23.json')))
        print('OK' if new == old else 'STALE'); sys.exit(0 if new == old else 1)
    else: print(__doc__)

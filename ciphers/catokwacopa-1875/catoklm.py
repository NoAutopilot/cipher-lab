"""catoklm.py -- phrase-level LM search on the five unread lines (R13-CATOKLM, 6 Oct 2026), pre-registered in PREREG-CATOKLM.md.

Our own code. The fit model (an order-preserving interleaving of the two ad halves is a subsequence of the reading; the
rest of the reading's letters are W.'s omissions) and the positional prior (word-initial letter's source: 8 May stream A,
20 May stream B, or omitted '-', by consonant/vowel initial) are David Bourdeau's (cyphersolver, targets/catokwacopa,
search.py, MIT; snapshot sources/cyphersolver/2026-10-02/catokwacopa/), read, not copied. The trie/edge search is
catok23.py's (R12-CATOK23), imported unmodified; only the scorer changes (word bigram + positional prior).

  python3 catoklm.py run        control first per line, target only if that line's control meets the gate -> catoklm.json
  python3 catoklm.py run --line N / merge   one line per process, then merge into catoklm.json
  python3 catoklm.py --check [--line N]   re-run the completed lines (or one) and exit 1 if catoklm.json is stale
"""
import collections, json, math, os, random, re, sys
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from catok23 import pairs, trie, edges, synth, UNREAD, MAX_LINE_OMIT, MARGIN  # noqa: E402
import gzip

HERE = os.path.dirname(os.path.abspath(__file__))
OMIT, BEAM, K, D, HOLD, NCTL, SEED = 2.3, 80, 20, 0.75, 0.10, 20, 1875
VOW = set('aeiou')
PRIOR = {('c', 'A'): .92, ('c', 'B'): .04, ('c', '-'): .04, ('v', 'A'): .35, ('v', 'B'): .45, ('v', '-'): .20}
LPRIOR = {k: math.log(v) for k, v in PRIOR.items()}


def corpus():
    """Ten 1853-1875 novels (catok23_stream.txt.gz, one novel per line). Last HOLD of each novel held out for controls."""
    train, held = [], []
    for line in gzip.open(os.path.join(HERE, 'catok23_stream.txt.gz'), 'rt'):
        t = line.split(); cut = int(len(t) * (1 - HOLD))
        train.append(t[:cut]); held.append(t[cut:])
    return train, held


class LM:
    """Word bigram, absolute discounting D backed off to the unigram; vocabulary = training words with count >= 3."""
    def __init__(self, train):
        uni, bi = collections.Counter(), collections.Counter()
        for t in train:
            uni.update(t); bi.update(zip(t, t[1:]))
        self.V = {w for w, c in uni.items() if c >= 3 and (len(w) > 1 or w in ('a', 'i'))}
        tot = sum(uni[w] for w in self.V)
        self.pu = {w: uni[w] / tot for w in self.V}
        self.lpu = {w: math.log(p) for w, p in self.pu.items()}
        self.cv = collections.Counter(); self.n1 = collections.Counter(); self.bi = {}
        for (v, w), c in bi.items():
            if v in self.V and w in self.V:
                self.bi[(v, w)] = c; self.cv[v] += c; self.n1[v] += 1
        self.cache = {}

    def lp(self, v, w):
        if v is None or v not in self.cv: return self.lpu[w]
        k = (v, w)
        r = self.cache.get(k)
        if r is None:
            c = self.bi.get(k, 0); cv = self.cv[v]
            r = math.log(max(c - D, 0) / cv + D * self.n1[v] / cv * self.pu[w])
            self.cache[k] = r
        return r


def first_src(w, i, j, A, B):
    """Source of w's first letter given it starts at stream position (i, j): A if A[i]==w[0] is consumed first, etc.
    Ambiguity (both could supply it) is resolved to the better prior; this is a scoring proxy, as in Bourdeau's search."""
    cv = 'v' if w[0] in VOW else 'c'
    opts = []
    if i < len(A) and A[i] == w[0]: opts.append(LPRIOR[(cv, 'A')])
    if j < len(B) and B[j] == w[0]: opts.append(LPRIOR[(cv, 'B')])
    opts.append(LPRIOR[(cv, '-')])
    return max(opts)


def kbest(A, B, lm, T):
    a, b = len(A), len(B)
    best = collections.defaultdict(list); best[(0, 0)] = [(0.0, 0, ())]
    for (i, j) in sorted(((i, j) for i in range(a + 1) for j in range(b + 1)), key=lambda x: x[0] + x[1]):
        cur = best.get((i, j))
        if not cur or (i, j) == (a, b): continue
        cur.sort(reverse=True); del cur[BEAM:]
        for w, ni, nj, om in edges(i, j, A, B, T):
            base = first_src(w, i, j, A, B) - OMIT * om
            lst = best[(ni, nj)]
            for sc, tot, ws in cur:
                if tot + om <= MAX_LINE_OMIT:
                    lst.append((sc + base + lm.lp(ws[-1] if ws else None, w), tot + om, ws + (w,)))
            if len(lst) > 4 * BEAM:
                lst.sort(reverse=True); del lst[BEAM:]
    seen, final = set(), []
    for sc, tot, ws in sorted(best[(a, b)], reverse=True):
        if ws not in seen: seen.add(ws); final.append((round(sc, 3), tot, ' '.join(ws)))
    return final[:K]


def verdict(res):
    if not res: return False, None
    m = res[0][0] - res[1][0] if len(res) > 1 else None
    return (m is None or m >= MARGIN), m


def synth_prior(ws, L, la, rng, tries=4000):
    """Plant phrase ws (letters >= L+3) under the design as the prior models it: excess letters dropped (word-initial
    letters dropped with the prior's '-' rate, the rest uniformly), word-initial letters sent to A/B by the prior,
    other letters A/B by a fair coin; rejection-sampled until |A| == la exactly."""
    letters, init = [], []
    for w in ws:
        for k, ch in enumerate(w): letters.append(ch); init.append(k == 0)
    n = len(letters); om = n - L
    for _ in range(tries):
        drop = set()
        w_init = [p for p in range(n) if init[p] and rng.random() < PRIOR[('v' if letters[p] in VOW else 'c', '-')]]
        if len(w_init) > om: continue
        drop.update(w_init)
        rest = [p for p in range(n) if p not in drop and not init[p]]
        if len(rest) < om - len(drop): continue
        drop.update(rng.sample(rest, om - len(drop)))
        a, b = [], []
        for p in range(n):
            if p in drop: continue
            if init[p]:
                cv = 'v' if letters[p] in VOW else 'c'
                pa = PRIOR[(cv, 'A')] / (PRIOR[(cv, 'A')] + PRIOR[(cv, 'B')])
            else: pa = 0.5
            (a if rng.random() < pa else b).append(letters[p])
        if len(a) == la: return ''.join(a), ''.join(b)
    return None


def wordacc(top, planted):
    """Descriptive only: LCS of word sequences / planted length."""
    x, y = top.split(), planted.split()
    dp = [[0] * (len(y) + 1) for _ in range(len(x) + 1)]
    for i in range(len(x)):
        for j in range(len(y)):
            dp[i + 1][j + 1] = dp[i][j] + 1 if x[i] == y[j] else max(dp[i][j + 1], dp[i + 1][j])
    return dp[-1][-1] / len(y)


def control(A, B, lm, T, held, rng):
    L = len(A) + len(B)
    ctl = {'n': 0, 'unique': 0, 'correct_unique': 0, 'wrong_unique': 0, 'planted_in_top20': 0, 'word_acc_top1': 0.0,
           'examples': []}
    while ctl['n'] < NCTL:
        t = rng.choice(held); target = L + rng.randint(3, 12)
        k = rng.randrange(len(t) - 60); ws = []
        while sum(map(len, ws)) < target: ws.append(t[k]); k += 1
        if sum(map(len, ws)) - L > 12 or any(w not in lm.V for w in ws): continue
        s = synth_prior(ws, L, len(A), rng)
        if s is None: continue
        a, b = s
        rr = kbest(a, b, lm, T); uu, _ = verdict(rr)
        planted = ' '.join(ws); top = rr[0][2] if rr else ''
        ctl['n'] += 1; ctl['unique'] += uu
        ctl['correct_unique'] += uu and top == planted; ctl['wrong_unique'] += uu and top != planted
        ctl['planted_in_top20'] += any(x[2] == planted for x in rr)
        ctl['word_acc_top1'] += wordacc(top, planted) if top else 0.0
        if len(ctl['examples']) < 3: ctl['examples'].append({'planted': planted, 'A': a, 'B': b, 'top': top})
    for k in ('unique', 'correct_unique', 'wrong_unique', 'planted_in_top20', 'word_acc_top1'):
        ctl[k] = round(ctl[k] / NCTL, 4)
    ctl['gate_met'] = ctl['correct_unique'] >= 0.50 and ctl['wrong_unique'] <= 0.10
    return ctl


def run(lines=UNREAD):
    P = pairs(); train, held = corpus(); lm = LM(train); T = trie(lm.V)
    out = []
    for ln in lines:
        A, B = P[ln]; rng = random.Random(SEED + ln)
        ctl = control(A, B, lm, T, held, rng)
        row = {'line': ln, 'A': A, 'B': B, 'letters': len(A) + len(B), 'control': ctl}
        if not ctl['gate_met']:
            row['target'] = None
            row['verdict'] = 'CONTROL BELOW GATE: untestable by this instrument at this N; target not scored'
        else:
            r = kbest(A, B, lm, T); u, m = verdict(r)
            row['target'] = {'unique': u, 'margin': m, 'top5': r[:5]}
            row['verdict'] = 'unique, control-backed (S)' if u else 'control-backed: not forced by this instrument'
        out.append(row)
        print('line %d (%d letters): ctl uniq %.2f correct %.2f wrong %.2f top20 %.2f wordacc %.2f | %s' % (
            ln, row['letters'], ctl['unique'], ctl['correct_unique'], ctl['wrong_unique'], ctl['planted_in_top20'],
            ctl['word_acc_top1'], row['verdict']), flush=True)
    return {'prereg': 'PREREG-CATOKLM.md', 'vocab': len(lm.V), 'bigrams': len(lm.bi), 'lines': out}


if __name__ == '__main__':
    a = sys.argv[1:]
    if a[:1] == ['run'] and '--line' in a:   # one line per process (4 CPUs); merge with 'merge'
        ln = int(a[a.index('--line') + 1])
        json.dump(run([ln]), open(os.path.join(HERE, 'catoklm_line%d.json' % ln), 'w'), indent=1)
    elif a[:1] == ['merge']:
        # a line whose control run did not finish inside the worker's box is recorded as such, not scored
        res = None; rows = []
        for ln in UNREAD:
            f = os.path.join(HERE, 'catoklm_line%d.json' % ln)
            if os.path.exists(f):
                p = json.load(open(f)); res = res or dict(p); rows.append(p['lines'][0]); os.remove(f)
            else:
                rows.append({'line': ln, 'control': None, 'target': None,
                             'verdict': 'control run not completed inside the box; target not scored'})
        res['lines'] = rows
        json.dump(res, open(os.path.join(HERE, 'catoklm.json'), 'w'), indent=1)
    elif a[:1] == ['run']:
        json.dump(run(), open(os.path.join(HERE, 'catoklm.json'), 'w'), indent=1)
    elif a[:1] == ['--check']:   # re-runs the lines that completed (or --line N for one, ~10 min each at 12 letters)
        old = json.load(open(os.path.join(HERE, 'catoklm.json')))
        done = [r['line'] for r in old['lines'] if r['control'] is not None]
        if '--line' in a: done = [int(a[a.index('--line') + 1])]
        new = json.loads(json.dumps(run(done)))['lines']
        ok = new == [r for r in old['lines'] if r['line'] in done]
        print('OK' if ok else 'STALE', done); sys.exit(0 if ok else 1)
    else: print(__doc__)

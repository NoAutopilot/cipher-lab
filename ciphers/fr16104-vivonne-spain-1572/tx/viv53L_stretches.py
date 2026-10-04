#!/usr/bin/env python3
"""N7-VIV53L: the D2-candidate statistic of PREREG-N7VIV53L.md (ii) -- longest repair-free stretches of the ink 53 re-decode.

    python3 ciphers/fr16104-vivonne-spain-1572/tx/viv53L_stretches.py [--null 200] [--top 10]

Per page the decoded letters are joined across line ends (an unread code '_' breaks a stretch). A stretch is a maximal run that splits
entirely into words of the vocabulary V = word tokens of tools/data/fr16 (PREREG-N6VIV63's three files) with count >= 5, folded to
a-z, v->u, j->i, length >= 2 plus the one-letter words 'a' and 'y'. DP: L[e] = longest V-segmentable run ending at e. Only word
division (and the v/u, j/i identification) is allowed -- no letter substitution. For each of the top stretches (non-overlapping, by
length) the liberties are listed as AUDIT 2 4a counts them: words (division), v/u-i/j identifications, M-graded tokens, look-alike-
settled tokens (K), joined ': :' (J), line ends crossed. Control (no gate): the same top-1 / top-3 lengths on --null letter-order
shuffles of each page's letters (unread breaks kept in place), seed "20261053L". Writes tx/viv53L_stretches.json and prints a table.
"""
import collections, json, os, random, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
sys.path.insert(0, HERE)
import viv63_test as t  # noqa: E402
import viv54_decode as vd  # noqa: E402
import viv53L_decode as vl  # noqa: E402
import judge_plaintext as jp  # noqa: E402


def vocab():
    cnt, forms = collections.Counter(), collections.defaultdict(collections.Counter)
    for p in t.FR16:
        for w in re.findall(r"[^\W\d_]+", jp.read_corpus(p).lower()):
            f = jp.fold(w)
            f = re.sub('[^a-z]', '', f)
            n = f.replace('v', 'u').replace('j', 'i')
            if n:
                cnt[n] += 1; forms[n][f] += 1
    V = {w for w, c in cnt.items() if c >= 5 and (len(w) >= 2 or w in ('a', 'y'))}
    return V, {w: forms[w].most_common(1)[0][0] for w in V}


def runs(s, V, maxw=16):
    """Longest V-segmentable run ending at each e, with backpointers."""
    L, bp = [0] * (len(s) + 1), [None] * (len(s) + 1)
    for e in range(1, len(s) + 1):
        for l in range(1, min(maxw, e) + 1):
            w = s[e - l:e]
            if '_' in w or w not in V:
                continue
            v = l + L[e - l]
            if v > L[e]:
                L[e], bp[e] = v, l
    return L, bp


def top(s, V, k):
    L, bp = runs(s, V)
    cands = sorted(((L[e], e) for e in range(len(s) + 1) if L[e]), reverse=True)
    used, out = [False] * len(s), []
    for ln, e in cands:
        b = e - ln
        if any(used[b:e]):
            continue
        for i in range(b, e):
            used[i] = True
        words, x = [], e
        while x > b:
            words.append(s[x - bp[x]:x]); x -= bp[x]
        out.append((ln, b, e, words[::-1]))
        if len(out) >= k:
            break
    return out


def pages():
    k = vd.key()
    res = {}
    for page in vl.PAGES:
        s, meta = [], []
        for line, seq in sorted(vl.page_tokens(page).items()):
            for c, flag, j in seq:
                if c not in k:
                    s.append('_'); meta.append(None); continue
                s.append(k[c][0]); meta.append(dict(line=line, M=flag or k[c][1] == 'M', K='K' in j, J='J' in j))
        res[page] = (''.join(s), meta)
    return res


def main():
    nnull = int(sys.argv[sys.argv.index('--null') + 1]) if '--null' in sys.argv else 200
    ktop = int(sys.argv[sys.argv.index('--top') + 1]) if '--top' in sys.argv else 10
    V, form = vocab()
    P = pages()
    allst = []
    for page, (s, meta) in P.items():
        for ln, b, e, words in top(s, V, ktop):
            m = meta[b:e]
            lines = sorted({x['line'] for x in m})
            allst.append(dict(page=page, lines=f'{lines[0]}-{lines[-1]}' if len(lines) > 1 else lines[0], letters=ln,
                              decoded=s[b:e], words=' '.join(form[w] for w in words), n_words=len(words),
                              uv_ij=sum(sum(a != b2 for a, b2 in zip(w, form[w])) for w in words),
                              M=sum(x['M'] for x in m), K=sum(x['K'] for x in m), J=sum(x['J'] for x in m),
                              line_ends=len(lines) - 1))
    allst.sort(key=lambda r: -r['letters'])
    rng = random.Random('20261053L-stretch')
    t1, t3 = [], []
    for _ in range(nnull):
        lens = []
        for s, _m in P.values():
            segs = s.split('_'); flat = list(''.join(segs)); rng.shuffle(flat); it = iter(flat)
            sh = '_'.join(''.join(next(it) for _ in seg) for seg in segs)
            lens += [x[0] for x in top(sh, V, 3)]
        lens.sort(reverse=True); t1.append(lens[0]); t3.append(sum(lens[:3]) / 3)
    t1.sort(); t3.sort()
    real3 = sum(r['letters'] for r in allst[:3]) / 3
    out = {'vocab': len(V), 'stretches': allst[:ktop],
           'null': {'draws': nnull, 'top1_median': jp.pct(t1, 0.5), 'top1_p99': jp.pct(t1, 0.99),
                    'top3mean_median': round(jp.pct(t3, 0.5), 2), 'top3mean_p99': round(jp.pct(t3, 0.99), 2)},
           'real': {'top1': allst[0]['letters'], 'top3mean': round(real3, 2)}}
    json.dump(out, open(os.path.join(HERE, 'viv53L_stretches.json'), 'w'), indent=1, ensure_ascii=False)
    print('page\tlines\tletters\twords\tM\tK\tJ\tuv_ij\tline_ends\tdivision')
    for r in allst[:ktop]:
        print(f"{r['page']}\t{r['lines']}\t{r['letters']}\t{r['n_words']}\t{r['M']}\t{r['K']}\t{r['J']}\t{r['uv_ij']}\t{r['line_ends']}\t{r['words']}")
    print(json.dumps({'real': out['real'], 'null': out['null'], 'vocab': len(V)}))


if __name__ == '__main__':
    main()

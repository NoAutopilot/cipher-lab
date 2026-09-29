#!/usr/bin/env python3
"""DEB-SWARM-F spacing-design test (29 Sept 2026). The Copiale design (Knight, Megyesi, Schaefer 2011): plain,
unaccented Roman letters are word spaces; the same letters with an accent or dots carry plaintext. Debosnys has the
same visible pattern -- a plain X (152 tokens) beside X-DOT, X-CURL, X-SLASH, X-DASH, X-BAR, X-O, and a plain O
(CIRC-O) beside O-TILDE, O-SLASH, O-DASH2 ... -- and the H39 model already sets X aside as a non-text sign.

Does the plain base class behave like Copiale's spaces? Statistics for a class C, each against 2,000 within-line
shuffles (every statistic can move under the shuffle, rule 3):
  adj   : C C adjacent pairs (a word space is rarely doubled; a shuffle doubles it by chance);
  gap_cv: coefficient of variation of the gaps between consecutive C tokens inside a line (spaces cut words of
          roughly regular length: the CV falls below the shuffle's geometric-like spread);
  gap1  : share of gaps of length 1 (a one-sign word) -- low for letter spaces in German/French.
Control first: Copiale, where the answer is known (C = unaccented lower-case Roman letters), on the whole text and
on consecutive-line windows of Debosnys's settled size; a contrast class of the same token share drawn from
Copiale's letter symbols must NOT show the space signature. Then Debosnys, C = {X}, {X, CIRC-O}, and the marked
variants as the contrast. Writes space_test.json."""
import os, re, json, random, statistics, sys, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, os.path.join(root, 'scripts')); from settled_lines import settled_lines
TR = int(os.environ.get('TRIALS', 2000))

def stats(lines, C):
    adj = 0; gaps = []
    for l in lines:
        last = None
        for i, s in enumerate(l):
            if s in C:
                if i > 0 and l[i - 1] in C: adj += 1
                if last is not None: gaps.append(i - last - 1)
                last = i
    ng = [g for g in gaps if g > 0]
    cv = statistics.pstdev(ng) / statistics.mean(ng) if len(ng) > 2 else 0
    g1 = sum(g == 1 for g in ng) / len(ng) if ng else 0
    return adj, cv, g1

def test(lines, C, seed=3, trials=TR):
    obs = stats(lines, C); rng = random.Random(seed); null = [[], [], []]
    for _ in range(trials):
        sh = []
        for l in lines: c = l[:]; rng.shuffle(c); sh.append(c)
        for k, v in enumerate(stats(sh, C)): null[k].append(v)
    res = dict(lines=len(lines), tokens=sum(map(len, lines)), class_tokens=sum(s in C for l in lines for s in l))
    for k, lab in enumerate(('adj', 'gap_cv', 'gap1')):
        v = sorted(null[k]); res[lab] = dict(obs=round(obs[k], 4), mean=round(sum(v) / trials, 4), band=[round(v[int(.025 * trials)], 4), round(v[int(.975 * trials) - 1], 4)],
                                             p_le=sum(x <= obs[k] for x in v) / trials, p_ge=sum(x >= obs[k] for x in v) / trials)
    return res

def copiale():
    out = []
    for l in open(os.path.join(here, 'data', 'copiale-transcription.txt'), encoding='utf-8', errors='replace'):
        s = l.strip()
        if not s or s.startswith('#'): continue
        t = [x for x in s.split() if x not in ('#', '"', '...', '..', '{', '}', '@', '%%', '.', ':') and not x.startswith('/') and not re.fullmatch(r'[A-Z]{1,2}', x)]
        if t: out.append([x.rstrip('?') or x for x in t])
    return out

def main():
    out = {}
    cl = copiale(); space = {x for l in cl for x in l if re.fullmatch(r'[a-z]', x)}
    cnt = collections.Counter(x for l in cl for x in l)
    share = sum(cnt[x] for x in space) / sum(cnt.values())
    # contrast: letter symbols (not space) greedily chosen from a shuffled list until the same token share
    rng = random.Random(11); letters = [x for x in cnt if x not in space]; rng.shuffle(letters); con = set(); tot = 0
    for x in letters:
        if tot / sum(cnt.values()) >= share: break
        con.add(x); tot += cnt[x]
    out['copiale_space_share'] = round(share, 4)
    out['copiale_spaces_all'] = test(cl, space, trials=300)
    out['copiale_contrast_all'] = test(cl, con, trials=300)
    N = 1147; wins = []; i = 0
    while i < len(cl):
        w = []; n = 0
        while i < len(cl) and n < N: w.append(cl[i]); n += len(cl[i]); i += 1
        if n >= N * .9: wins.append(w)
    ws = [test(w, space, seed=k, trials=500) for k, w in enumerate(wins[::4])]
    wc = [test(w, con, seed=k, trials=500) for k, w in enumerate(wins[::4])]
    def summ(rs):
        return dict(n=len(rs), adj_p_le_05=sum(r['adj']['p_le'] <= .05 for r in rs), cv_p_le_05=sum(r['gap_cv']['p_le'] <= .05 for r in rs),
                    g1_p_le_05=sum(r['gap1']['p_le'] <= .05 for r in rs), adj_p_ge_05=sum(r['adj']['p_ge'] <= .05 for r in rs))
    out['copiale_windows_N1147_spaces'] = summ(ws); out['copiale_windows_N1147_contrast'] = summ(wc)
    # density-matched control: each space token kept with probability 0.134/share (Debosnys X share of settled
    # tokens), dropped ones removed (words merge), so the class is as sparse as X; then the same windows
    xs = 152 / 1138; keep = xs / share; rr = random.Random(5)
    thin = [[x for x in l if x not in space or rr.random() < keep] for l in cl]
    tw = []; i = 0
    while i < len(thin):
        w = []; n = 0
        while i < len(thin) and n < N: w.append(thin[i]); n += len(thin[i]); i += 1
        if n >= N * .9: tw.append(w)
    out['copiale_windows_N1147_spaces_thinned_to_X_share'] = summ([test(w, space, seed=k, trials=500) for k, w in enumerate(tw[::4])])
    PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
    by = [[s for s in v if s not in PUNCT] for v in settled_lines(root, 'c', drop_clear=True).values()]
    marked_x = {'X-DOT', 'X-CURL', 'X-SLASH', 'X-DASH', 'X-BAR', 'X-O', 'XX-TILDE', 'OX-TILDE'}
    marked_o = {'O-TILDE', 'O-SLASH', 'O-DASH2', 'O-DASHBELOW', 'O-BAR-O', 'O-DOT-STEM', 'OO-TILDE', 'O-DASH-DOTS', 'O-DOTS', 'O-PLUS'}
    for name, C in (('X', {'X'}), ('X+CIRC-O', {'X', 'CIRC-O'}), ('marked_X', marked_x), ('marked_O', marked_o), ('CIRC-O', {'CIRC-O'})):
        out['debosnys_' + name] = test(by, C)
    json.dump(out, open(os.path.join(here, 'space_test.json'), 'w'), indent=1)
    for k, v in out.items():
        if isinstance(v, dict) and 'adj' in v:
            print(k, 'tok', v['class_tokens'], '/', v['tokens'], ' '.join(f"{s}={v[s]['obs']} mean {v[s]['mean']} band {v[s]['band']} p_le {v[s]['p_le']} p_ge {v[s]['p_ge']}" for s in ('adj', 'gap_cv', 'gap1')))
        else: print(k, v)
if __name__ == '__main__': main()

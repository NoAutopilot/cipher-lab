#!/usr/bin/env python3
"""A3V3-SAVT: align the c380 cipher (SV-SORT piles, seed table = Tomokiyo pile match) to its printed decipherment
(Charriere IV p.638) under savt/PREREG.md (+ amendment 1). Writes savt/results.json, savt/table_proposed.tsv.
Usage: python3 savt/align.py [--draws 200]   (offline; reads sorter/ and savt/ only)"""
import argparse, json, random, re, unicodedata, os, collections
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
MATCH, MIS, GAP = 2, -1, -2

def norm(s):
    s = unicodedata.normalize('NFD', s.lower())
    s = ''.join(c for c in s if 'a' <= c <= 'z')
    return s.replace('j', 'i').replace('v', 'u')

def load_G():
    txt = ''.join(l for l in open(os.path.join(HERE, 'print_charriere_c380.txt'), encoding='utf-8') if not l.startswith('#'))
    return norm(txt)

def seed_values():
    vals = {}
    for l in open(os.path.join(ROOT, 'sorter', 'tomokiyo_pile_match.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('pile\t'): continue
        f = l.rstrip('\n').split('\t')
        v = f[3].strip()
        if v in ('-', ''): continue
        v = re.split(r' or | / ', v)[0].strip().rstrip('?')
        vals[f[0]] = 'DOUBLE' if v == 'double' else norm(v)
    return vals

def load_tokens(page='c380'):
    toks = []
    for l in open(os.path.join(ROOT, 'sorter', 'inputs', 'labels.tsv'), encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0].startswith(page + '_'):
            toks.append((int(f[0].split('_')[1]), int(f[0].split('_')[2]), f[1]))
    toks.sort(); return toks

def decode(toks, vals):
    """-> list of (letter or '?', token index)"""
    out = []
    for ti, (_, _, p) in enumerate(toks):
        v = vals.get(p)
        if v is None or v == '': out.append(('?', ti))
        elif v == 'DOUBLE':
            prev = next((c for c, _ in reversed(out) if c != '?'), None)
            out.append((prev or '?', ti))
        else: out.extend((c, ti) for c in v)
    return out

def sc_matrix(D, G):
    d = np.array([ord(c) for c in D]); g = np.array([ord(c) for c in G])
    S = np.where(d[:, None] == g[None, :], MATCH, MIS)
    S[d == ord('?'), :] = 0
    return S

def rowfill(T, j):  # H[j] = max_k<=j T[k] + GAP*(j-k)
    return np.maximum.accumulate(T - GAP * j) + GAP * j

def sw_score(D, G):
    S = sc_matrix(D, G); m = len(G); j = np.arange(m + 1)
    prev = np.zeros(m + 1); best = 0
    for i in range(len(D)):
        T = np.zeros(m + 1)
        T[1:] = np.maximum(prev[:-1] + S[i], prev[1:] + GAP)
        T = np.maximum(T, 0); cur = rowfill(T, j); best = max(best, cur.max()); prev = cur
    return float(best)

def semiglobal(D, G):
    """D fully consumed, free end gaps in G. Returns (matched, mapped, pairs[(iD, jG)])."""
    S = sc_matrix(D, G); n, m = len(D), len(G); j = np.arange(m + 1)
    H = np.zeros((n + 1, m + 1))
    for i in range(1, n + 1):
        T = np.full(m + 1, -1e9); T[0] = GAP * i
        T[1:] = np.maximum(H[i - 1, :-1] + S[i - 1], H[i - 1, 1:] + GAP); T[0] = H[i - 1, 0] + GAP
        H[i] = rowfill(T, j)
    i, jj = n, int(H[n].argmax()); pairs = []
    while i > 0 and jj > 0:
        if H[i, jj] == H[i - 1, jj - 1] + S[i - 1, jj - 1]: pairs.append((i - 1, jj - 1)); i -= 1; jj -= 1
        elif H[i, jj] == H[i - 1, jj] + GAP: i -= 1
        else: jj -= 1
    pairs.reverse()
    mapped = sum(c != '?' for c in D); matched = sum(1 for a, b in pairs if D[a] == G[b] and D[a] != '?')
    return matched, mapped, pairs

def S_semi(D, G):
    mt, mp, _ = semiglobal(D, G); return mt / mp if mp else 0.0

def poscontrol(Dlen, wild_rate, G, rng):
    freq = list(G); out = []
    for c in G[:Dlen]:
        if rng.random() < wild_rate: out.append('?')
        elif rng.random() < 0.30: out.append(rng.choice(freq))
        else: out.append(c)
    return ''.join(out)

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--draws', type=int, default=200); a = ap.parse_args()
    G = load_G(); vals = seed_values(); toks = load_tokens()
    late = [t for t in toks if t[0] >= 6]
    res = {'G_len': len(G), 'tokens_c380': len(toks), 'tokens_l6_22': len(late)}
    def both(tk, vv):
        Df = ''.join(c for c, _ in decode(toks if tk is None else tk, vv))
        return Df
    Dfull = both(toks, vals); Dlate = both(late, vals)
    res['D_full_len'] = len(Dfull); res['D_late_len'] = len(Dlate)
    res['wild_rate_full'] = Dfull.count('?') / len(Dfull)
    res['target'] = {'S_loc': sw_score(Dfull, G), 'S_semi_l6_22': S_semi(Dlate, G)}
    mapped_piles = sorted(vals); vlist = [vals[p] for p in mapped_piles]
    N1 = {'S_loc': [], 'S_semi': []}; N2 = {'S_loc': [], 'S_semi': []}; P = {'S_loc': [], 'S_semi': []}
    for s in range(1, a.draws + 1):
        rng = random.Random(s)
        sh = vlist[:]; rng.shuffle(sh); v1 = dict(zip(mapped_piles, sh))
        N1['S_loc'].append(sw_score(both(toks, v1), G)); N1['S_semi'].append(S_semi(both(late, v1), G))
        labs = [t[2] for t in toks]; rng.shuffle(labs)
        t2 = [(t[0], t[1], l) for t, l in zip(toks, labs)]; t2late = [t for t in t2 if t[0] >= 6]
        N2['S_loc'].append(sw_score(both(t2, vals), G)); N2['S_semi'].append(S_semi(both(t2late, vals), G))
        if s <= 20:  # positive control: 20 draws suffice to show power; reported as such
            P['S_loc'].append(sw_score(poscontrol(len(Dfull), res['wild_rate_full'], G, rng), G))
            P['S_semi'].append(S_semi(poscontrol(len(Dlate), Dlate.count('?') / len(Dlate), G, rng), G))
    def summ(x): x = np.array(x); return {'mean': round(float(x.mean()), 4), 'p95': round(float(np.percentile(x, 95)), 4), 'max': round(float(x.max()), 4), 'min': round(float(x.min()), 4), 'n': len(x)}
    for k, d in (('N1_shuffled_table', N1), ('N2_pile_label_shuffle', N2), ('P_positive', P)):
        res[k] = {s: summ(v) for s, v in d.items()}
    t = res['target']
    res['gate'] = {s: bool(t[s2] > res['N1_shuffled_table'][s]['max'] and t[s2] > res['N2_pile_label_shuffle'][s]['max'])
                   for s, s2 in (('S_loc', 'S_loc'), ('S_semi', 'S_semi_l6_22'))}
    res['P_passes'] = {s: bool(res['P_positive'][s]['min'] > max(res['N1_shuffled_table'][s]['max'], res['N2_pile_label_shuffle'][s]['max'])) for s in ('S_loc', 'S_semi')}
    json.dump(res, open(os.path.join(HERE, 'results.json'), 'w'), indent=1)
    print(json.dumps(res, indent=1))

if __name__ == '__main__':
    main()

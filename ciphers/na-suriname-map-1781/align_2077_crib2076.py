#!/usr/bin/env python3
"""SUR-2076 (15 Oct 2026): 4.VEL 2076's plain title/legend (crib_2076_legend.tsv) as known plaintext on 2077's cipher
title + Explicatie legend (ciphertext_2077_legend.tsv + reading_2077_legend_nieuw_tokens.tsv). Pre-registered in
PREREG-SUR-2076.md. Local alignment (Smith-Waterman) of each 2077 entry against every 2076 entry; U and M tokens are
wildcards whose aligned crib letter is a "pin". Fixed pair acceptance; known-H leave-one-out control (must pass) and
letter-shuffled-crib control (must fail). Disk only. --dry prints the entries and stops before any score."""
import csv, random, re, sys, unicodedata
from collections import defaultdict, Counter

MATCH, MISM, GAP = 2, -3, -3
K_MIN, ID_MIN, GAPS_MAX = 6, 0.85, 1
SEEDS = 20
TARGET = '[d-hook]'

def fold(s):
    s = unicodedata.normalize('NFD', s.lower()).replace('̈', '')
    s = s.replace('ij', 'y').replace('ei', 'y')
    return re.sub(r'[^a-z]', '', s)

def load_crib():
    out = []
    for r in csv.reader((l for l in open('crib_2076_legend.tsv') if not l.startswith('#')), delimiter='\t'):
        if r[0] == 'id': continue
        out.append((r[0], fold(r[1])))
    return out

def load_cipher():
    val = {}
    for r in csv.reader(open('reading_2077_legend_nieuw_tokens.tsv'), delimiter='\t'):
        if r[0] == 'line': continue
        val[(r[0], r[1])] = (r[2], r[3], r[4])
    entries, cur, name = [], [], 'title'
    for r in csv.reader((l for l in open('ciphertext_2077_legend.tsv') if not l.startswith('#')), delimiter='\t'):
        if r[0] == 'line': continue
        line, pos, sign = r[0], r[1], r[2]
        if sign.startswith('w:'):
            w = sign[2:]
            if re.fullmatch(r"[a-z]\.?|[^\x00-\x7f]\.?|@", w) or w in ('z.', 'ÿ'):
                if cur: entries.append((name, cur))
                name, cur = line + ':' + w, []
                continue
            if w == 'Explicatie' or w == 'der' or w == 'Signatuuren':
                if cur: entries.append((name, cur)); cur = []
                name = 'heading'; continue
            for ch in fold(w):
                cur.append(dict(c=ch, g='P', line=line, pos=pos, sign=sign))
            continue
        s, v, g = val.get((line, pos), (sign, '?', 'U'))
        known = g in ('H', 'C') and len(v) == 1 and v.isalpha()
        cur.append(dict(c=fold(v) if known else None, g=g, line=line, pos=pos, sign=s, v=v))
    if cur: entries.append((name, cur))
    return [(n, e) for n, e in entries if sum(1 for t in e if t['c'] is None) < len(e)]

def sw(seq, crib):
    n, m = len(seq), len(crib)
    H = [[0]*(m+1) for _ in range(n+1)]; P = [[None]*(m+1) for _ in range(n+1)]
    best, bi, bj = 0, 0, 0
    for i in range(1, n+1):
        c = seq[i-1]['c']
        for j in range(1, m+1):
            d = H[i-1][j-1] + (0 if c is None else (MATCH if c == crib[j-1] else MISM))
            u, l = H[i-1][j] + GAP, H[i][j-1] + GAP
            v = max(0, d, u, l); H[i][j] = v
            P[i][j] = 'd' if v == d and v > 0 else ('u' if v == u and v > 0 else ('l' if v == l and v > 0 else None))
            if v > best: best, bi, bj = v, i, j
    k = mm = gaps = 0; pins = []
    i, j = bi, bj
    while i > 0 and j > 0 and H[i][j] > 0:
        p = P[i][j]
        if p == 'd':
            c = seq[i-1]['c']
            if c is None: pins.append((i-1, crib[j-1]))
            elif c == crib[j-1]: k += 1
            else: mm += 1
            i, j = i-1, j-1
        elif p == 'u': gaps += 1; i -= 1
        elif p == 'l': gaps += 1; j -= 1
        else: break
    return best, k, mm, gaps, pins

def accepted(k, mm, gaps):
    return k >= K_MIN and k / max(1, k+mm) >= ID_MIN and gaps <= GAPS_MAX

def best_pair(seq, cribs):
    res = sorted(((sw(seq, c)[0], cid, c) for cid, c in cribs), reverse=True)
    top = res[0]
    if len(res) > 1 and res[1][0] == top[0]: return None
    s, k, mm, g, pins = sw(seq, top[2])
    return (top[1], s, k, mm, g, pins) if accepted(k, mm, g) else None

def run(entries, cribs, loo=True):
    pairs, pins = [], []
    for name, seq in entries:
        bp = best_pair(seq, cribs)
        if bp:
            pairs.append((name,) + bp[:5])
            for idx, ch in bp[5]: pins.append((name, seq[idx], ch))
    hits = tot = 0
    if loo:
        for name, seq in entries:
            for i, t in enumerate(seq):
                if t['g'] != 'H' or t['c'] is None: continue
                s2 = [dict(x) for x in seq]; s2[i]['c'] = None
                bp = best_pair(s2, cribs)
                if not bp: continue
                for idx, ch in bp[5]:
                    if idx == i: tot += 1; hits += (ch == t['c'])
    return pairs, pins, hits, tot

def main():
    cribs, entries = load_crib(), load_cipher()
    print(f'crib entries {len(cribs)}; 2077 entries {len(entries)}; targets', sum(1 for _, e in entries for t in e if t['sign'] == TARGET))
    if '--dry' in sys.argv:
        for n, e in entries: print(n, ''.join(t['c'] if t['c'] else '·' for t in e))
        return
    pairs, pins, hits, tot = run(entries, cribs)
    print('REAL accepted pairs', len(pairs))
    for p in pairs: print('  pair', p)
    print(f'REAL known-H leave-one-out: pins {tot} correct {hits} precision {hits/max(1,tot):.3f}')
    sh = []
    for seed in range(SEEDS):
        rnd = random.Random(seed)
        sc = [(cid, ''.join(rnd.sample(c, len(c)))) for cid, c in cribs]
        p2, _, h2, t2 = run(entries, sc)
        sh.append((len(p2), h2, t2))
    mp = sum(x[0] for x in sh)/SEEDS; mh = sum(x[1] for x in sh)/SEEDS; mt = sum(x[2] for x in sh)/SEEDS
    print(f'SHUFFLE ({SEEDS} seeds) mean accepted pairs {mp:.2f}, mean LOO pins {mt:.2f}, mean correct {mh:.2f}; per seed {sh}')
    g1 = tot >= 10 and hits/max(1,tot) >= 0.90
    g2 = mp <= 1.0 and mh <= 0.2*hits
    print('GATE known-H', 'PASS' if g1 else 'FAIL', '| GATE shuffle-must-fail', 'PASS' if g2 else 'FAIL')
    print('PINS (U/M positions in accepted pairs):')
    for name, t, ch in pins:
        print(f"  {t['line']}:{t['pos']} {t['sign']} grade {t['g']} current {t.get('v')} -> {ch}  ({name})", '<-- TARGET' if t['sign'] == TARGET else '')
    tp = [x for x in pins if x[1]['sign'] == TARGET]
    print('TARGET [d-hook] pins:', len(tp), [(x[1]['line']+':'+x[1]['pos'], x[2]) for x in tp])
    print('INSTRUMENT', 'VALID' if g1 and g2 else 'NON-TEST')

if __name__ == '__main__':
    main()

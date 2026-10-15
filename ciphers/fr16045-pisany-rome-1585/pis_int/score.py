#!/usr/bin/env python3
"""PIS-INT score (PREREG-PIS-INT.md): does Tomokiyo's 1585 table (key.tsv) decode each interlinear-glossed
cipher group on fr.16045 f.121 to its gloss?  Shuffled-pair control (gloss dealt to another group) and a
power control (gloss enciphered with the table, 25% signs corrupted).

    python3 score.py [--pairs pairs.tsv] [--key ../key.tsv] [--out result.json] [--check]
"""
import argparse, csv, json, os, random, re, sys, unicodedata

HERE = os.path.dirname(os.path.abspath(__file__))
WILD = '*'


def fold(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    s = re.sub(r'[^a-z]', '', s)
    return s.replace('j', 'i').replace('v', 'u').replace('y', 'i')


def load_key(path):
    key = {}
    for r in csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'):
        v = r['value']
        key[r['sign']] = [''] if v == '<null>' else [fold(a) for a in v.split('|')]
    key['S07'] = key.get('S04'); key['S08'] = key.get('S05')
    return key


def options(tok, key):
    t = tok.rstrip('?')
    if t in key and key[t] is not None:
        return key[t]
    return [WILD]  # ?[shape] or unknown label


def best_sim(group, gloss, key):
    """max over alternative choices of 1 - lev(D,G)/max(|D|,|G|); WILD letter = 0.5 substitution."""
    G = fold(gloss)
    toks = group.split()
    if not G or not toks:
        return 0.0, ''
    # DP over (token index, gloss position) with edit costs; each token expands to one of its options
    INF = 1e9
    n = len(G)
    # state: cost row over gloss positions after consuming tokens; track decoded length via best path
    prev = [(float(j), 0, '') for j in range(n + 1)]  # (cost, decoded_len, decoded)
    for tok in toks:
        opts = options(tok, key)
        cur = [(INF, 0, '')] * (n + 1)
        for o in opts:
            row = prev
            for ch in o:
                nxt = [(INF, 0, '')] * (n + 1)
                for j in range(n + 1):
                    c, L, s = row[j]
                    if c + 1 < nxt[j][0]:
                        nxt[j] = (c + 1, L + 1, s + ch)  # D letter unmatched
                    if j < n:
                        sub = 0.0 if ch == G[j] else (0.5 if ch == WILD else 1.0)
                        if c + sub < nxt[j + 1][0]:
                            nxt[j + 1] = (c + sub, L + 1, s + ch)
                for j in range(1, n + 1):  # G letter unmatched
                    c, L, s = nxt[j - 1]
                    if c + 1 < nxt[j][0]:
                        nxt[j] = (c + 1, L, s)
                row = nxt
            for j in range(n + 1):
                if row[j][0] < cur[j][0]:
                    cur[j] = row[j]
        prev = cur
    c, L, s = prev[n]
    return 1 - c / max(L, n, 1), s


def M_of(pairs, key, thr):
    return sum(1 for g, gl in pairs if best_sim(g, gl, key)[0] >= thr)


def derange(n, rng):
    while True:
        p = list(range(n)); rng.shuffle(p)
        if all(i != p[i] for i in range(n)):
            return p


def control(pairs, key, thr, draws, seed):
    rng = random.Random(seed)
    groups = [g for g, _ in pairs]; glosses = [gl for _, gl in pairs]
    out = []
    for _ in range(draws):
        p = derange(len(pairs), rng)
        out.append(M_of([(groups[i], glosses[p[i]]) for i in range(len(pairs))], key, thr))
    out.sort()
    return out


def encipher(gloss, key, rng, err):
    inv = {}
    for s, vs in key.items():
        if vs is None or s in ('S07', 'S08'):
            continue
        for v in vs:
            if len(v) == 1:
                inv.setdefault(v, []).append(s)
    signs = [s for s in key if s not in ('S07', 'S08')]
    toks = [rng.choice(inv[c]) for c in fold(gloss) if c in inv]
    return ' '.join(rng.choice(signs) if rng.random() < err else t for t in toks)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--pairs', default=os.path.join(HERE, 'pairs.tsv'))
    ap.add_argument('--key', default=os.path.join(HERE, '..', 'key.tsv'))
    ap.add_argument('--out', default=os.path.join(HERE, 'result.json'))
    ap.add_argument('--thr', type=float, default=0.60)
    ap.add_argument('--draws', type=int, default=2000)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    key = load_key(a.key)
    rows = [r for r in csv.DictReader(open(a.pairs, encoding='utf-8'), delimiter='\t') if r.get('use', 'y') == 'y']
    pairs = [(r['group'], r['gloss']) for r in rows]
    per = []
    for r in rows:
        s, D = best_sim(r['group'], r['gloss'], key)
        per.append({'id': r['id'], 'gloss': r['gloss'], 'gloss_folded': fold(r['gloss']), 'decode_best': D,
                    'sim': round(s, 3), 'decodes_to_gloss': s >= a.thr})
    M = sum(p['decodes_to_gloss'] for p in per)
    ctl = control(pairs, key, a.thr, a.draws, 1585)
    p95 = ctl[int(0.95 * len(ctl)) - 1]
    power = []
    for seed in range(5):
        rng = random.Random(seed)
        syn = [(encipher(gl, key, rng, 0.25), gl) for _, gl in pairs]
        Ms = M_of(syn, key, a.thr)
        c = control(syn, key, a.thr, 500, seed)
        power.append({'seed': seed, 'M': Ms, 'p95': c[int(0.95 * len(c)) - 1],
                      'pass': Ms > c[int(0.95 * len(c)) - 1] and Ms >= 2})
    res = {'n_pairs': len(pairs), 'thr': a.thr, 'per_pair': per, 'M_real': M,
           'control_mean': round(sum(ctl) / len(ctl), 3), 'control_p95': p95, 'control_max': ctl[-1],
           'p_emp': round(sum(1 for x in ctl if x >= M) / len(ctl), 4),
           'verdict': 'PASS' if (M > p95 and M >= 2) else 'FAIL', 'power': power,
           'power_pass': sum(p['pass'] for p in power)}
    if len(pairs) < 3:
        res['verdict'] = 'NON-TEST (<3 pairs)'
    txt = json.dumps(res, ensure_ascii=False, indent=1) + '\n'
    if a.check:
        old = open(a.out, encoding='utf-8').read() if os.path.exists(a.out) else ''
        print('result up to date' if old == txt else 'STALE'); sys.exit(0 if old == txt else 1)
    open(a.out, 'w', encoding='utf-8').write(txt)
    print(json.dumps({k: v for k, v in res.items() if k != 'per_pair'}, ensure_ascii=False))
    for p in per:
        print(p['id'], p['sim'], p['gloss_folded'], '<-', p['decode_best'])


if __name__ == '__main__':
    main()

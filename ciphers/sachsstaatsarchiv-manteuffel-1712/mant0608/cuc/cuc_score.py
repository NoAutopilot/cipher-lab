#!/usr/bin/env python3
"""MANT-CUC scorer (pre-registered in PREREG-MANTCUC.md before any read was scored).

Usage: python3 mant0608/cuc/cuc_score.py CODES.tsv CLEAR.tsv [--key key.tsv] [--perms 1000] [--seed 6083]
         [--strips mant0608/cuc/strips.tsv] [--out-cand FILE] [--label NAME]
CODES.tsv: leaf<TAB>strip<TAB>codes (dot/space separated; '?' = unread)
CLEAR.tsv: leaf<TAB>strip<TAB>clear text read blind from the clear crop (underlined words)

Letter-class strips (>=2 codes, or one code whose key value is <=3 letters) are aligned to the normalised clear
string by DP: each code consumes 0-4 letters; a code scores 1 when its key value set contains the consumed
substring. S = total matched codes. Control: values of key.tsv permuted among all codes (primary) and among
letter-class codes only (secondary), --perms times; gate PASS when S > p99 of the permuted S (both reported).
Name-class codes (single code, key value > 3 letters or absent with a multi-word clear) are reported, not gated.
Strips flagged 'unaligned' or 'gloss-over-code' in strips.tsv are excluded from the gate.
"""
import argparse, csv, random, re, sys, unicodedata

def norm(s):
    s = unicodedata.normalize('NFKD', s)
    s = ''.join(c for c in s if not unicodedata.combining(c)).lower()
    return re.sub(r'[^a-z]', '', s)

def load_key(p):
    k = {}
    for r in csv.DictReader(open(p), delimiter='\t'):
        vals = [norm(v) for v in (r['value'] or '').split('|')]
        k[r['code'].strip()] = [v for v in vals if v]
    return k

def is_letter_vals(vals):
    return bool(vals) and all(len(v) <= 3 for v in vals)

def align(codes, clear, key):
    n, m = len(codes), len(clear)
    NEG = -10**9
    best = [[NEG] * (m + 1) for _ in range(n + 1)]
    back = [[None] * (m + 1) for _ in range(n + 1)]
    best[0][0] = 0
    for i in range(n):
        vals = key.get(codes[i], [])
        for j in range(m + 1):
            if best[i][j] == NEG:
                continue
            for L in range(0, 5):
                if j + L > m:
                    break
                sub = clear[j:j + L]
                sc = 1 if (L > 0 and sub in vals) else 0
                if best[i][j] + sc > best[i + 1][j + L]:
                    best[i + 1][j + L] = best[i][j] + sc
                    back[i + 1][j + L] = (j, sub, sc)
    if best[n][m] == NEG:
        return 0, []
    out, j = [], m
    for i in range(n, 0, -1):
        pj, sub, sc = back[i][j]
        out.append((codes[i - 1], sub, sc))
        j = pj
    return best[n][m], out[::-1]

def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('codes'); ap.add_argument('clear')
    ap.add_argument('--key', default='key.tsv'); ap.add_argument('--strips', default='mant0608/cuc/strips.tsv')
    ap.add_argument('--perms', type=int, default=1000); ap.add_argument('--seed', type=int, default=6083)
    ap.add_argument('--out-cand'); ap.add_argument('--label', default='')
    a = ap.parse_args()
    key = load_key(a.key)
    strips = {(r['leaf'], r['strip']): r for r in csv.DictReader(open(a.strips), delimiter='\t')}
    codes = {(r[0], r[1]): [c for c in re.split(r'[.\s]+', r[2].strip()) if c] for r in csv.reader(open(a.codes), delimiter='\t') if r and not r[0].startswith('#') and r[0] != 'leaf'}
    clear = {(r[0], r[1]): r[2] for r in csv.reader(open(a.clear), delimiter='\t') if r and not r[0].startswith('#') and r[0] != 'leaf'}
    units, names = [], []
    for k, cs in sorted(codes.items()):
        note = strips.get(k, {}).get('note', '') + ' ' + strips.get(k, {}).get('clear_under_by_worker_eye', '')
        if 'unaligned' in note or 'gloss-over-code' in note or k not in clear:
            continue
        cl = norm(clear[k])
        if len(cs) == 1 and not is_letter_vals(key.get(cs[0], [])):
            names.append((k, cs[0], clear[k])); continue
        units.append((k, [c for c in cs], cl))
    def S(kk):
        return sum(align(cs, cl, kk)[0] for _, cs, cl in units)
    real = S(key)
    ntok = sum(len(cs) for _, cs, _ in units)
    rng = random.Random(a.seed)
    allc = list(key); lc = [c for c in key if is_letter_vals(key[c])]
    res = {}
    for nm, pool in (('all', allc), ('letter', lc)):
        sims = []
        for _ in range(a.perms):
            vals = [key[c] for c in pool]; rng.shuffle(vals)
            kk = dict(key); kk.update(zip(pool, vals)); sims.append(S(kk))
        sims.sort()
        p95, p99 = sims[int(0.95 * len(sims)) - 1], sims[int(0.99 * len(sims)) - 1]
        ge = sum(1 for s in sims if s >= real)
        res[nm] = (p95, p99, ge, sum(sims) / len(sims))
    print(f'{a.label} letter-class strips {len(units)}, tokens {ntok}; S real {real} ({real/ntok:.3f} per token)' if ntok else 'no tokens')
    for nm, (p95, p99, ge, mean) in res.items():
        print(f'  control {nm}-codes permutation x{a.perms}: mean {mean:.1f} p95 {p95} p99 {p99}; >= real {ge}; gate (real > p99) {"PASS" if real > p99 else "FAIL"}')
    perleaf = {}
    cand = []
    for k, cs, cl in units:
        sc, al = align(cs, cl, key)
        perleaf.setdefault(k[0], [0, 0])
        perleaf[k[0]][0] += sc; perleaf[k[0]][1] += len(cs)
        print(f'  {k[0]} {k[1]} {sc}/{len(cs)} clear={cl} ' + ' '.join(f'{c}={s}{"" if m else "*"}' for c, s, m in al))
        for c, s, m in al:
            if not m:
                cand.append((k[0], k[1], c, '|'.join(key.get(c, [])) or '(absent)', s, cl))
    for lf, (s, n) in sorted(perleaf.items()):
        print(f'  leaf {lf}: {s}/{n}')
    for k, c, cl in names:
        kv = '|'.join(key.get(c, [])) or '(absent)'
        strip_art = lambda t: re.sub(r'^(le|la|les|l)', '', t)
        eq = strip_art(norm(kv)) == strip_art(norm(cl))
        print(f'  name {k[0]} {k[1]} {c}: key "{kv}" clear "{cl}" exact-after-article {"agree" if eq else "differ"}')
        if not eq:
            cand.append((k[0], k[1], c, kv, norm(cl), 'name-class'))
    if a.out_cand:
        with open(a.out_cand, 'w') as f:
            f.write('leaf\tstrip\tcode\tkey_value\tclear_substring_aligned\tclear_word\tgrade\tsource\n')
            for r in cand:
                f.write('\t'.join(map(str, r)) + f'\tC (clear word, MANT-CUC; not in key.tsv)\t{a.label}\n')

if __name__ == '__main__':
    main()

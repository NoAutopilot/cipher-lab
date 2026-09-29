#!/usr/bin/env python3
"""R2-3 CRIB-LENGTH (DEB-SWARM2-R2-3, 29 Sept 2026): is c4's verse a copied period poem?

Pre-registered in PLAN.md (pushed before any real score). Statistic per 20-line window of a verse text:
  R = max(pearson(cipher line lengths, window letter counts), pearson(..., window vowel-group counts))
  P = phi over the 190 line pairs of (cipher line-final signs equal) vs (window rhyme keys equal)
  S = R + P
Both survive a running key and word-internal scrambling (R fully; P under designs that keep one sign per rhyme sound);
R is untouched by sign-replacement noise and moves only under insertions/deletions.

Usage: crib_length.py --texts DIR   (DIR/pool/*.txt candidate pool, DIR/decoy/*.txt decoys; Gutenberg plain text)
Writes control.tsv, real.tsv, result.json beside this script. Offline once the texts are on disk.
"""
import argparse, collections, csv, glob, json, os, random, re, sys, unicodedata
import numpy as np

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))  # ciphers/debosnys-1883
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
W = 20
VOW = 'aeiouy'

# ---------- target ----------
def c4_profile():
    clear = {(r['line'], r['position']) for r in csv.DictReader(open(os.path.join(ROOT, 'clear_spans.tsv')), delimiter='\t')}
    by = collections.OrderedDict()
    for r in csv.DictReader(open(os.path.join(ROOT, 'ciphertext_c34_draft.tsv')), delimiter='\t'):
        if not r['line'].startswith('c4'): continue
        if (r['line'], r['position']) in clear: continue
        by.setdefault(r['line'], []).append(r['sign'].rstrip('?'))
    keys = sorted(by, key=lambda k: (0 if k.startswith('c4a0') else 1 if k.startswith('c4a') else 2, k))
    lines = [by[k] for k in keys]
    assert len(lines) == W, len(lines)
    lens = [sum(1 for s in l if s not in PUNCT) for l in lines]
    fin = []
    for l in lines:
        t = l[:]
        while t and t[-1] in PUNCT: t.pop()
        fin.append(t[-1] if t else '')
    return keys, lens, fin

# ---------- texts ----------
def fold(s):
    return ''.join(c for c in unicodedata.normalize('NFD', s.lower()) if unicodedata.category(c) != 'Mn')

def strip_gutenberg(t):
    a = re.search(r'\*\*\* ?START OF (THE|THIS) PROJECT GUTENBERG[^\n]*\n', t)
    b = re.search(r'\*\*\* ?END OF (THE|THIS) PROJECT GUTENBERG', t)
    return t[a.end() if a else 0: b.start() if b else len(t)]

def verse_lines(path):
    """Lines of blocks that look like verse: median length <= 58 chars, >= 60 pct start with a capital, >= 2 lines."""
    t = strip_gutenberg(open(path, encoding='utf-8', errors='replace').read()).replace('\r', '')
    out = []
    for block in re.split(r'\n\s*\n', t):
        ls = [l.strip() for l in block.split('\n') if l.strip()]
        ls = [l for l in ls if len(re.sub(r'[^A-Za-zÀ-ÿ]', '', l)) >= 8 and not re.fullmatch(r'[\WIVXLCDM\d]+', l)
              and l != l.upper()]
        if len(ls) < 2: continue
        med = sorted(len(l) for l in ls)[len(ls) // 2]
        cap = sum(1 for l in ls if re.match(r'^[\W_]*[A-ZÀ-Ý]', l)) / len(ls)
        if med <= 58 and cap >= 0.6 and not any(re.search(r'\[|\]|\bfootnote|http', l, re.I) for l in ls):
            out.extend(ls)
    return out

def letters(line): return re.sub(r'[^a-z]', '', fold(line))

def sylls(line):
    n = 0
    for w in re.findall(r'[a-z]+', fold(line)):
        g = re.findall(r'[aeiouy]+', w)
        k = len(g)
        if k > 1 and w.endswith('e') and not w.endswith(('ee', 'ie', 'ye')): k -= 1  # silent/mute final e
        n += max(k, 1) if g else 0
    return n

def rhyme_key(line, fr):
    ws = re.findall(r'[a-z]+', fold(line))
    if not ws: return ''
    w = ws[-1]
    if fr:
        for suf in ('ent', 'es', 's', 'x', 'e'):
            if len(w) > len(suf) + 1 and w.endswith(suf): w = w[:-len(suf)]; break
    m = re.search(r'[aeiouy]+[^aeiouy]*$', w)
    return m.group(0) if m else w[-2:]

def is_fr(path):
    t = open(path, encoding='utf-8', errors='replace').read(4000)
    return bool(re.search(r'Language: French', t))

# ---------- scoring ----------
def pair_idx():
    return np.triu_indices(W, 1)
PI, PJ = pair_idx()

def window_feats(vlines, fr):
    L = np.array([len(letters(l)) for l in vlines], float)
    S = np.array([sylls(l) for l in vlines], float)
    rk = [rhyme_key(l, fr) for l in vlines]
    ids = {k: i for i, k in enumerate(sorted(set(rk)))}
    R = np.array([ids[k] if k else -1 - i for i, k in enumerate(rk)])  # empty keys never equal
    return L, S, R

def sliding(x):
    return np.lib.stride_tricks.sliding_window_view(x, W)

def pearson_rows(M, v):
    Mc = M - M.mean(1, keepdims=True); vc = v - v.mean()
    den = np.sqrt((Mc ** 2).sum(1) * (vc ** 2).sum())
    with np.errstate(invalid='ignore', divide='ignore'):
        r = (Mc @ vc) / den
    return np.nan_to_num(r, nan=0.0)

def phi_rows(E, c):
    """E: (n, 190) bool window pair-equalities; c: (190,) bool cipher pair-equalities."""
    c = c.astype(float); E = E.astype(float)
    n11 = E @ c; n1_ = E.sum(1); n_1 = c.sum(); N = len(c)
    num = N * n11 - n1_ * n_1
    den = np.sqrt(n1_ * (N - n1_) * n_1 * (N - n_1))
    with np.errstate(invalid='ignore', divide='ignore'):
        r = num / den
    return np.nan_to_num(r, nan=0.0)

def score_text(feats, lens, fin):
    L, S, R = feats
    if len(L) < W: return np.zeros((0, 3))
    v = np.array(lens, float)
    rl = pearson_rows(sliding(L), v); rs = pearson_rows(sliding(S), v)
    Rw = sliding(R)
    E = Rw[:, PI] == Rw[:, PJ]
    c = np.array([fin[i] == fin[j] and fin[i] != '' for i, j in zip(PI, PJ)])
    p = phi_rows(E, c)
    Rm = np.maximum(rl, rs)
    return np.stack([Rm + p, Rm, p], 1)

# ---------- control encipherment ----------
FREQ_EN = 'etaoinshrdlcumwfgypbvkjxqz'
def homo_key(rng, nsigns=60):
    # homophones roughly by English/French frequency rank
    w = np.array([1 / (i + 1.5) for i in range(26)]); k = np.maximum(1, np.round(w / w.sum() * nsigns)).astype(int)
    key = {}; s = 0
    for ch, n in zip(FREQ_EN, k):
        key[ch] = list(range(s, s + n)); s += n
    return key, s

def noise(tokens, rng, nsig, rate=0.15):
    out = []
    for t in tokens:
        u = rng.random()
        if u < rate * 0.75: out.append(('n', rng.randrange(nsig)))
        elif u < rate * 0.875: continue  # deletion
        elif u < rate: out.append(t); out.append(('n', rng.randrange(nsig)))  # insertion
        else: out.append(t)
    return out

def encipher(vlines, design, rng, keytext):
    """Returns (lens, finals) as the cipher profile of 20 plaintext lines under the design, with 15 pct noise."""
    lines_tok = []
    if design == 'homophonic':
        key, nsig = homo_key(rng)
        for l in vlines: lines_tok.append([('h', rng.choice(key[c])) for c in letters(l)])
    elif design == 'running_key':
        nsig = 26; ki = 0
        for l in vlines:
            tk = []
            for c in letters(l):
                tk.append(('r', (ord(c) - 97 + ord(keytext[ki % len(keytext)]) - 97) % 26)); ki += 1
            lines_tok.append(tk)
    elif design == 'syllabic':
        code = {}; nsig = 400
        for l in vlines:
            tk = []
            for w in re.findall(r'[a-z]+', fold(l)):
                for sy in re.findall(r'[^aeiouy]*[aeiouy]+(?:[^aeiouy]+$)?', w) or [w]:
                    if sy not in code: code[sy] = [len(code) * 2, len(code) * 2 + 1]
                    tk.append(('s', rng.choice(code[sy])))
            lines_tok.append(tk)
        nsig = max(2 * len(code), 2)
    noisy = [noise(t, rng, nsig) for t in lines_tok]
    return [len(t) for t in noisy], [t[-1] if t else None for t in noisy]

def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--texts', required=True); ap.add_argument('--seed', type=int, default=29)
    ap.add_argument('--controls-per-lang', type=int, default=5)
    a = ap.parse_args()
    keys, lens, fin = c4_profile()
    texts = {}
    for grp in ('pool', 'decoy'):
        for p in sorted(glob.glob(os.path.join(a.texts, grp, '*.txt'))):
            vl = verse_lines(p); fr = is_fr(p)
            if len(vl) >= W + 5: texts[(grp, os.path.basename(p))] = (vl, fr, window_feats(vl, fr))
    inv = [(g, n, len(v[0]), 'fr' if v[1] else 'en') for (g, n), v in texts.items()]
    decoys = [k for k in texts if k[0] == 'decoy']; pool = [k for k in texts if k[0] == 'pool']
    rng = random.Random(a.seed)

    def decoy_scores(lens_, fin_):
        return np.concatenate([score_text(texts[k][2], lens_, fin_) for k in decoys])

    # ---- control first ----
    ctrl_rows = []
    for lang in ('en', 'fr'):
        pk = [k for k in pool if (texts[k][1]) == (lang == 'fr')]
        for i in range(a.controls_per_lang):
            k = rng.choice(pk); vl = texts[k][0]; st = rng.randrange(len(vl) - W); win = vl[st:st + W]
            other = [x for x in pool if x != k]; kt = letters(' '.join(texts[rng.choice(other)][0][:400]))
            for design in ('homophonic', 'running_key', 'syllabic'):
                cl, cf = encipher(win, design, rng, kt)
                ts = score_text(texts[k][2], cl, cf)[st]
                D = decoy_scores(cl, cf)
                sub = D[np.array(rng.sample(range(len(D)), 1000))]
                row = dict(lang=lang, text=k[1], start=st, design=design, S=round(float(ts[0]), 3), R=round(float(ts[1]), 3),
                           P=round(float(ts[2]), 3), rank_all_S=int((D[:, 0] >= ts[0]).sum()) + 1, n_decoys=len(D),
                           rank_1000_S=int((sub[:, 0] >= ts[0]).sum()) + 1, rank_1000_R=int((sub[:, 1] >= ts[1]).sum()) + 1,
                           decoy_p99_S=round(float(np.percentile(D[:, 0], 99)), 3))
                ctrl_rows.append(row); print('CONTROL', row, flush=True)

    # ---- real ----
    D = decoy_scores(lens, fin)
    p99 = float(np.percentile(D[:, 0], 99)); p99R = float(np.percentile(D[:, 1], 99))
    real = []
    for k in pool:
        sc = score_text(texts[k][2], lens, fin)
        for st, s in enumerate(sc): real.append((float(s[0]), float(s[1]), float(s[2]), k[1], st))
    real.sort(reverse=True)
    best = real[0]; bestR = max(real, key=lambda x: x[1])
    m = len(real); nrep = 1000; rr = np.random.default_rng(a.seed)
    maxS = np.array([D[rr.choice(len(D), m, replace=False), 0].max() for _ in range(nrep)])
    maxR = np.array([D[rr.choice(len(D), m, replace=False), 1].max() for _ in range(nrep)])
    top = []
    for s in real[:10]:
        vl = texts[('pool', s[3])][0][s[4]:s[4] + W]
        top.append(dict(S=round(s[0], 3), R=round(s[1], 3), P=round(s[2], 3), text=s[3], start=s[4], first_line=vl[0], last_line=vl[-1]))
    res = dict(profile=dict(lines=keys, lens=lens, finals=fin), inventory=inv, n_decoy_windows=len(D), n_pool_windows=m,
               decoy_p99_S=round(p99, 3), decoy_p99_R=round(p99R, 3),
               best_S=top[0], best_R=dict(R=round(bestR[1], 3), S=round(bestR[0], 3), text=bestR[3], start=bestR[4]),
               maxcorr_p_S=float((maxS >= best[0]).mean()), maxcorr_p_R=float((maxR >= bestR[1]).mean()), top10=top)
    with open(os.path.join(HERE, 'control.tsv'), 'w') as f:
        w = csv.DictWriter(f, fieldnames=list(ctrl_rows[0]), delimiter='\t'); w.writeheader(); w.writerows(ctrl_rows)
    json.dump(res, open(os.path.join(HERE, 'result.json'), 'w'), indent=1, ensure_ascii=False)
    print('REAL', json.dumps({k: v for k, v in res.items() if k not in ('top10', 'inventory', 'profile')}, ensure_ascii=False))

if __name__ == '__main__':
    main()

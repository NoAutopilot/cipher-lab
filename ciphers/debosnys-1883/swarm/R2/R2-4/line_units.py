#!/usr/bin/env python3
"""R2-4 LINE-UNITS (DEB-SWARM2-R2-4, 29 Sept 2026). Runs exactly PREREG.md (committed before any count): known-answer
controls K1/K1r (Copiale decorative capitals at Debosnys's size, forward = opener, reversed = closer), K2 (planted closer
on Debosnys's own lines), K3 (width-test calibration), then T1 (containers line-final vs within-line shuffles), T2
(width-matched layout control), T3 (picture-opened verse lines vs couplet starts). Writes line_units.json.
Reads the settled drafts, clear_spans.tsv, glyphs/signs.tsv and G-F's public Copiale transcription; nothing under
swarm/controls/; no key, no value, no plaintext."""
import os, sys, re, csv, json, math, random, statistics, collections
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.normpath(os.path.join(here, '..', '..', '..'))
sys.path.insert(0, os.path.join(root, 'scripts')); from settled_lines import settled_lines
FAST = os.environ.get('FAST') == '1'
PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
CLOSERS = {'BUCKET', 'PICT-JUG', 'BOX-M', 'PICT-BOTTLE', 'PICT-BARREL', 'PICT-GLASS'}
def is_opener(s, star=False):
    if s in CLOSERS: return False
    return s.startswith('PICT-') or s in ('SUN', 'HEART', 'RAM', 'CHAIN') or (star and s == 'STAR')

# ---------- Debosnys lines with geometry: list of lines, each a list of (sign, normalised width)
def deb_lines(drop_clear=True):
    geo = collections.defaultdict(dict)
    for r in csv.DictReader(open(os.path.join(root, 'glyphs/signs.tsv')), delimiter='\t'):
        geo[(r['page'], int(r['line']))][int(r['pos'])] = float(r['w'])
    skip = set()
    if drop_clear:
        skip = {(r['line'], int(r['position'])) for r in csv.DictReader(open(os.path.join(root, 'clear_spans.tsv')), delimiter='\t')}
    raw = settled_lines(root, 'c')
    out = collections.OrderedDict()
    for k, v in raw.items():
        pg, ln = k.split('_L'); ln = int(ln); g = geo[(pg, ln)]
        assert len(g) == len(v), k
        toks = []
        for i, s in enumerate(v, 1):
            if s in PUNCT or (k, i) in skip: continue
            if k == 'c2a_L02' and i == 28 and s == 'DASH-V': continue  # page-edge artefact (E, PAGEMAP)
            toks.append([s, g[i]])
        if toks:
            med = statistics.median(w for _, w in toks)
            out[k] = [(s, w / med) for s, w in toks]
    return out

def exact_slot(lines, cls, last=True):
    """Exact within-line-shuffle null for 'class tokens in the first (last) slot': each line (len >= 2) puts a class token
    there with probability c_i/n_i, independently, so the count is Poisson-binomial -- the limit of infinitely many
    shuffles of the same null PREREG names. Returns (obs, p_ge, mean)."""
    dist = [1.0]; obs = 0; mean = 0.0
    for l in lines:
        if len(l) < 2: continue
        q = sum(t in cls for t in l) / len(l); mean += q
        obs += (l[-1] if last else l[0]) in cls
        if q == 0: continue
        nd = [0.0] * (len(dist) + 1)
        for k, v in enumerate(dist): nd[k] += v * (1 - q); nd[k + 1] += v * q
        dist = nd
    return obs, min(1.0, sum(dist[obs:])), mean

def shuffle_p(lines, stat, trials, seed):
    """lines: lists of labels. p_ge of stat under within-line shuffles."""
    obs = stat(lines); rng = random.Random(seed); ge = 0; tot = 0.0
    for _ in range(trials):
        sh = [rng.sample(l, len(l)) for l in lines]; x = stat(sh); ge += x >= obs; tot += x
    return obs, ge / trials, tot / trials
final_in = lambda cls: (lambda ls: sum(1 for l in ls if len(l) >= 2 and l[-1] in cls))
initial_in = lambda cls: (lambda ls: sum(1 for l in ls if len(l) >= 2 and l[0] in cls))

# ---------- Copiale (F's loader and capital class, copied rule-for-rule from G-F/design_test.py)
LOGO = {'nee', 'tri..', 'o..', 'bigx', 'lip', 'star', 'toe', 'gate', 'bigl', 'tribig', 'sci'}
def copiale_lines():
    out = []
    for l in open(os.path.join(root, 'swarm/G-F/data/copiale-transcription.txt'), encoding='utf-8', errors='replace'):
        s = l.strip()
        if not s or s.startswith('#'): continue
        out.append([t for t in s.split() if t not in ('#', '"', '...', '..', '{', '}', '@', '%%') and not t.startswith('/') and not t.endswith('?') or t in LOGO])
    return [l for l in out if l]
is_cap = lambda t: re.fullmatch(r'[A-Z]', t) is not None and t != 'N'

def k1(reverse, windows, shuf, seed):
    C = copiale_lines(); rng = random.Random(seed); det = 0; used = 0; skipped = 0; ps = []
    starts = list(range(0, len(C) - 56))
    for w in range(windows):
        s0 = rng.choice(starts); win = [l[::-1] if reverse else l[:] for l in C[s0:s0 + 56]]
        caps = [(i, j) for i, l in enumerate(win) for j, t in enumerate(l) if is_cap(t)]
        if len(caps) < 8: skipped += 1; continue
        keep = set(rng.sample(caps, 8))
        lab = [['CLS' if (i, j) in keep else ('o' if is_cap(t) else t) for j, t in enumerate(l)] for i, l in enumerate(win)]
        _, p, _ = exact_slot(lab, {'CLS'}, last=reverse); used += 1; det += p < 0.01; ps.append(p)
    full = [l[::-1] if reverse else l for l in C]
    return dict(windows=used, skipped_lt8_caps=skipped, detect_rate=round(det / used, 3), median_p=statistics.median(ps),
                copiale_lines=len(C), gate=0.80, pass_=det / used >= 0.80)

def k2(DL, n_final, plantings, shuf, seed):
    rng = random.Random(seed); base = [[s for s, _ in l] for l in DL.values()]
    finals = [(i, len(l) - 1) for i, l in enumerate(base) if len(l) >= 2 and l[-1] not in CLOSERS]
    mids = [(i, j) for i, l in enumerate(base) for j in range(len(l) - 1) if l[j] not in CLOSERS]
    allp = [(i, j) for i, l in enumerate(base) for j in range(len(l)) if l[j] not in CLOSERS]
    det = 0
    for _ in range(plantings):
        pick = set(rng.sample(allp, 8)) if n_final is None else set(rng.sample(finals, n_final) + rng.sample(mids, 8 - n_final))
        lab = [['PLANT' if (i, j) in pick else s for j, s in enumerate(l)] for i, l in enumerate(base)]
        _, p, _ = exact_slot(lab, {'PLANT'}); det += p < 0.01
    return round(det / plantings, 3)

def width_draws(DL, cls_pos, pool_filter, draws, seed, tol=0.20):
    """cls_pos: list of (line index, pos) of the class tokens. For each, candidates = non-class tokens (pool_filter) with
    normalised width within +-tol. Returns (obs finals, p_layout, pool final rate, candidate counts)."""
    rng = random.Random(seed); L = list(DL.values()); cls = set(cls_pos)
    tok = [(i, j, s, w, j == len(l) - 1) for i, l in enumerate(L) for j, (s, w) in enumerate(l)]
    cand = []
    for (i, j) in cls_pos:
        w0 = L[i][j][1]
        c = [t for t in tok if (t[0], t[1]) not in cls and pool_filter(t[2]) and abs(t[3] - w0) <= tol * w0]
        if len(c) < 5:  # an extreme-width token (K3 random draws only): fall back to its 5 nearest widths
            c = sorted((t for t in tok if (t[0], t[1]) not in cls and pool_filter(t[2])), key=lambda t: abs(t[3] - w0))[:5]
        cand.append(c)
    obs = sum(1 for (i, j) in cls_pos if j == len(L[i]) - 1)
    ge = 0
    for _ in range(draws):
        ge += sum(rng.choice(c)[4] for c in cand) >= obs
    poolset = {(t[0], t[1]): t for c in cand for t in c}
    rate = sum(t[4] for t in poolset.values()) / len(poolset)
    return obs, ge / draws, round(rate, 4), [len(c) for c in cand]

def main():
    S = 300 if FAST else 2000; out = {'prereg': 'PREREG.md (commit 572aa02d)'}
    DL = deb_lines(True); L = [[s for s, _ in l] for l in DL.values()]; keys = list(DL)
    # ---- controls first
    out['K1_copiale_caps_opener_56lines_8tok'] = k1(False, 100 if FAST else 1000, S, 1)
    out['K1r_copiale_caps_reversed_closer'] = k1(True, 100 if FAST else 1000, S, 2)
    out['K2_planted_5of8_final_power'] = dict(detect_rate=k2(DL, 5, 100 if FAST else 500, S, 3), gate=0.80)
    out['K2_planted_3of8_final_power'] = dict(detect_rate=k2(DL, 3, 100 if FAST else 500, S, 4))
    out['K2_random8_false_positive'] = dict(rate=k2(DL, None, 100 if FAST else 500, S, 5), gate=0.05)
    # K3 width calibration
    rng = random.Random(6); allpos = [(i, j) for i, l in enumerate(L) for j in range(len(l)) if l[j] not in CLOSERS]
    finpos = [(i, len(l) - 1) for i, l in enumerate(L) if L[i][-1] not in CLOSERS and 0.8 <= DL[keys[i]][-1][1] <= 1.25]
    nd = 100 if FAST else 500; fp = 0; sep = 0
    for _ in range(nd):
        _, p, _, _ = width_draws(DL, rng.sample(allpos, 8), lambda s: s not in CLOSERS, 1000, rng.randrange(1 << 30)); fp += p < 0.05
        _, p, _, _ = width_draws(DL, rng.sample(finpos, 8), lambda s: s not in CLOSERS, 1000, rng.randrange(1 << 30)); sep += p < 0.05
    out['K3_width_random8_false_system'] = dict(rate=round(fp / nd, 3), gate=0.05)
    out['K3_width_final8_ordinary_width_separated'] = dict(rate=round(sep / nd, 3), gate=0.80)
    ctl = out
    ctl_pass = (ctl['K1_copiale_caps_opener_56lines_8tok']['pass_'] and ctl['K1r_copiale_caps_reversed_closer']['pass_']
                and ctl['K2_planted_5of8_final_power']['detect_rate'] >= 0.80 and ctl['K2_random8_false_positive']['rate'] <= 0.05
                and ctl['K3_width_random8_false_system']['rate'] <= 0.05 and ctl['K3_width_final8_ordinary_width_separated']['rate'] >= 0.80)
    out['controls_pass'] = ctl_pass
    # ---- T1
    cpos = [(i, j) for i, l in enumerate(L) for j, s in enumerate(l) if s in CLOSERS]
    out['closer_tokens'] = [dict(line=keys[i], pos=j + 1, of=len(L[i]), sign=L[i][j], wnorm=round(DL[keys[i]][j][1], 2)) for i, j in cpos]
    obs, p, mean = shuffle_p(L, final_in(CLOSERS), 10000, 7); _, pe, _ = exact_slot(L, CLOSERS)
    out['T1_containers_final'] = dict(tokens=len(cpos), obs=obs, null_mean=round(mean, 3), p_ge=p, p_exact=pe, kill1=pe >= 0.01)
    L_e = [[s for s, _ in l] for l in deb_lines(False).values()]
    o2, p2, m2 = shuffle_p(L_e, final_in(CLOSERS), 10000, 8)
    out['T1_sensitivity_clear_spans_kept'] = dict(obs=o2, null_mean=round(m2, 3), p_ge=p2)
    # ---- T2
    for tag, filt in (('any_sign', lambda s: s not in CLOSERS), ('non_picture', lambda s: s not in CLOSERS and not is_opener(s, True))):
        o, pl, rate, nc = width_draws(DL, cpos, filt, 10000, 9)
        out[f'T2_width_matched_{tag}'] = dict(obs_container_finals=o, p_layout=pl, pool_final_rate=rate, candidates=nc,
                                             expected_finals_if_layout=round(rate * len(cpos), 2), kill2=pl >= 0.05)
    # descriptive: line-final share by width band, all non-container tokens
    bands = collections.defaultdict(lambda: [0, 0])
    for l in DL.values():
        for j, (s, w) in enumerate(l):
            if s in CLOSERS: continue
            b = '<0.8' if w < 0.8 else '0.8-1.25' if w <= 1.25 else '1.25-1.6' if w <= 1.6 else '1.6-2.2' if w <= 2.2 else '>2.2'
            bands[b][0] += 1; bands[b][1] += j == len(l) - 1
    out['T2_final_share_by_width_band'] = {b: dict(n=n, final=f, share=round(f / n, 3)) for b, (n, f) in sorted(bands.items())}
    # ---- T3
    verse = [k for k in keys if k.startswith('c4')]
    assert len(verse) == 20, verse
    for star in (False, True):
        op = [n for n, k in enumerate(verse, 1) if is_opener(DL[k][0][0], star)]
        m = len(op); odd = sum(1 for n in op if n % 2 == 1)
        tot = math.comb(20, m); p = sum(math.comb(10, a) * math.comb(10, m - a) for a in range(odd, m + 1)) / tot if m else 1.0
        pmin = math.comb(10, m) / tot if m else 1.0
        out['T3_couplets' + ('_with_star' if star else '')] = dict(opener_lines=op, opener_first_signs=[DL[verse[n - 1]][0][0] for n in op],
            couplet_first=odd, of=m, p_ge=round(p, 4), min_reachable_p=round(pmin, 4),
            verdict='untestable at this N' if pmin > 0.05 else ('supported' if p <= 0.05 else 'not supported'))
    # opener sanity on all 56 lines (H31 shape, primary class)
    o3, p3, m3 = shuffle_p(L, lambda ls: sum(1 for l in ls if len(l) >= 2 and is_opener(l[0])), 10000, 10)
    out['opener_initial_all_lines'] = dict(obs=o3, null_mean=round(m3, 3), p_ge=p3)
    json.dump(out, open(os.path.join(here, 'line_units.json'), 'w'), indent=1, default=str)
    print(json.dumps(out, indent=1, default=str))

if __name__ == '__main__': main()

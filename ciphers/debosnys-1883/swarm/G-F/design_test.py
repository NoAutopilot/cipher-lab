#!/usr/bin/env python3
"""DEB-SWARM-F design test (29 Sept 2026). Question: do Debosnys's picture signs behave like the Copiale cipher's
word symbols (logograms)? Control first: the Copiale text itself (Knight, Megyesi, Schaefer 2011; transcription and
decipherment from Stockholm University's project page, data/), where the answer is known.

Classes are defined by SHAPE in both texts, before any statistic: Debosnys pictograms = h3_unit_profile.py's class
(PICT-* plus SUN, STAR, HEART, RAM); Copiale logograms = the large symbols the 2011 team listed before reading them
(transcribed nee, tri.., o.., bigx, lip, star, toe, gate, bigl, tribig, sci). Copiale's two other known classes are
reported beside them: decorative capitals (upper-case Roman letters, meaningless, paragraph openers) and the
unaccented lower-case Roman letters (spaces).

Statistics, each against 10,000 within-unit shuffles (the multiset of each unit fixed, so every statistic can move):
  initial  : class tokens in a unit's first slot (the H31 statistic);
  final    : class tokens in a unit's last slot;
Units: physical lines, and (Copiale only) sentences cut at the '.' token. Copiale is scored with its spaces and
capitals dropped (letters + logograms only), the closest analogue of Debosnys with X set aside, and also with
spaces kept. Size-matched windows: Copiale cut into consecutive-line windows of Debosnys's settled N (1147 tokens);
per window, class token count, type count, initial count and its shuffle p.
Writes design_test.json. Nothing here reads a Debosnys value; nothing is plaintext of a control."""
import os, re, json, random, collections, sys
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.abspath(os.path.join(here, '..', '..'))
sys.path.insert(0, os.path.join(root, 'scripts')); from settled_lines import settled_lines
LOGO = {'nee', 'tri..', 'o..', 'bigx', 'lip', 'star', 'toe', 'gate', 'bigl', 'tribig', 'sci'}
TRIALS = int(os.environ.get('TRIALS', 10000))

def copiale_lines():
    out = []
    for l in open(os.path.join(here, 'data', 'copiale-transcription.txt'), encoding='utf-8', errors='replace'):
        s = l.strip()
        if not s or s.startswith('#'): continue
        out.append([t for t in s.split() if t not in ('#', '"', '...', '..', '{', '}', '@', '%%') and not t.startswith('/') and not t.endswith('?') or t in LOGO])
    return [l for l in out if l]
is_space = lambda t: re.fullmatch(r'[a-z]', t) is not None
is_cap = lambda t: re.fullmatch(r'[A-Z]{1,2}', t) is not None and t not in ('DS',)  # DS etc. are letter symbols below
CAPS_LETTERSYM = {'N'}  # upper-case codes that are symbols, not decoration (see SOURCES.md)

def profile(units, cls):
    ini = fin = tok = 0
    for u in units:
        n = len(u)
        for i, s in enumerate(u):
            if not cls(s): continue
            tok += 1
            if n >= 2: ini += i == 0; fin += i == n - 1
    return tok, ini, fin

def test(units, cls, seed=1, trials=TRIALS):
    tok, ini, fin = profile(units, cls); rng = random.Random(seed); ni = []; nf = []
    for _ in range(trials):
        sh = []
        for u in units: c = u[:]; rng.shuffle(c); sh.append(c)
        _, a, b = profile(sh, cls); ni.append(a); nf.append(b)
    ni.sort(); nf.sort(); ei = sum(ni) / trials; ef = sum(nf) / trials
    return dict(units=len(units), tokens=sum(map(len, units)), class_tokens=tok,
                initial=ini, initial_expected=round(ei, 2), initial_band=[ni[int(.025 * trials)], ni[int(.975 * trials) - 1]],
                initial_p_ge=sum(x >= ini for x in ni) / trials, initial_ratio=round(ini / ei, 2) if ei else None,
                final=fin, final_expected=round(ef, 2), final_band=[nf[int(.025 * trials)], nf[int(.975 * trials) - 1]],
                final_p_ge=sum(x >= fin for x in nf) / trials)

def main():
    out = {}
    raw = copiale_lines()
    logo = lambda t: t in LOGO
    cap = lambda t: re.fullmatch(r'[A-Z]', t) is not None and t not in CAPS_LETTERSYM
    lines_ns = [[t for t in l if not is_space(t) and not cap(t)] for l in raw]; lines_ns = [l for l in lines_ns if l]
    lines_sp = [[t for t in l if not cap(t)] for l in raw]; lines_sp = [l for l in lines_sp if l]
    out['copiale_logograms_lines_nospace'] = test(lines_ns, logo)
    out['copiale_logograms_lines_withspace'] = test(lines_sp, logo)
    out['copiale_capitals_lines_raw'] = test(raw, cap)
    # sentences: cut the flat letter+logogram stream at '.'
    flat = [t for l in lines_ns for t in l]; sents = []; cur = []
    for t in flat:
        if t == '.':
            if cur: sents.append(cur); cur = []
        else: cur.append(t)
    if cur: sents.append(cur)
    out['copiale_logograms_sentences_nospace'] = test(sents, logo)
    # which logograms open sentences, census
    cen = collections.defaultdict(lambda: [0, 0, 0])
    for s in sents:
        for i, t in enumerate(s):
            if logo(t): cen[t][0] += 1; cen[t][1] += i == 0; cen[t][2] += i == len(s) - 1
    out['copiale_logogram_census_sentences'] = {k: dict(n=v[0], initial=v[1], final=v[2]) for k, v in sorted(cen.items(), key=lambda kv: -kv[1][0])}
    # size-matched windows of consecutive lines (letters+logograms), Debosnys settled N 1147
    N = 1147; wins = []; i = 0
    while i < len(lines_ns):
        w = []; n = 0
        while i < len(lines_ns) and n < N: w.append(lines_ns[i]); n += len(lines_ns[i]); i += 1
        if n >= N * 0.9: wins.append(w)
    wr = []
    for k, w in enumerate(wins):
        r = test(w, logo, seed=k + 7, trials=2000)
        types = len({t for l in w for t in l if logo(t)})
        wr.append(dict(lines=r['units'], tokens=r['tokens'], logo_tokens=r['class_tokens'], logo_types=types, initial=r['initial'],
                       expected=r['initial_expected'], p_ge=r['initial_p_ge']))
    out['copiale_windows_N1147'] = dict(n=len(wr), windows=wr,
        logo_tokens_median=sorted(x['logo_tokens'] for x in wr)[len(wr) // 2],
        logo_types_median=sorted(x['logo_types'] for x in wr)[len(wr) // 2],
        windows_initial_p_le_0_01=sum(x['p_ge'] <= 0.01 for x in wr), windows_initial_p_le_0_05=sum(x['p_ge'] <= 0.05 for x in wr))
    # Debosnys, same code path (H31's own class and drop list)
    PUNCT = {'BLOB', 'HOOK-L', 'DASH-H', '_', 'MULTI'}
    pict = lambda s: s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM')
    by = [[s for s in v if s not in PUNCT] for v in settled_lines(root, 'c', drop_clear=True).values()]
    out['debosnys_pictograms_lines'] = test(by, pict)
    out['debosnys_pictograms_lines_noX'] = test([[s for s in l if s != 'X'] for l in by], pict)
    pt = collections.Counter(s for l in by for s in l if pict(s))
    out['debosnys_pictogram_types'] = dict(tokens=sum(pt.values()), types=len(pt), once=sum(v == 1 for v in pt.values()))
    lt = collections.Counter(t for l in lines_ns for t in l if logo(t))
    out['copiale_logogram_types'] = dict(tokens=sum(lt.values()), types=len(lt), once=sum(v == 1 for v in lt.values()), counts=dict(lt.most_common()))
    json.dump(out, open(os.path.join(here, 'design_test.json'), 'w'), indent=1)
    for k, v in out.items():
        if isinstance(v, dict) and 'initial' in v:
            print(f"{k}: units {v['units']} tok {v['tokens']} class {v['class_tokens']} initial {v['initial']} exp {v['initial_expected']} band {v['initial_band']} p {v['initial_p_ge']} | final {v['final']} exp {v['final_expected']} p {v['final_p_ge']}")
    w = out['copiale_windows_N1147']; print('windows', w['n'], 'logo tok median', w['logo_tokens_median'], 'types median', w['logo_types_median'], 'p<=.01', w['windows_initial_p_le_0_01'], 'p<=.05', w['windows_initial_p_le_0_05'])
    print('copiale types', out['copiale_logogram_types']); print('debosnys types', out['debosnys_pictogram_types'])
    print('sentence census', out['copiale_logogram_census_sentences'])
if __name__ == '__main__': main()

#!/usr/bin/env python3
"""H3 (28 Sept 2026): which unit could the signs stand for? Token statistics of the target against French (fr19,
1830-1888 prose, the judge corpus) sampled at the same N under six unit hypotheses, each a control that can differ
from the target on every statistic:
  letter      one sign per letter (K about 26-30 at any N)
  homoph      letters with K homophones allotted by frequency (K = the target's own K; a GOLD-D1-shaped control)
  syllable    one sign per syllable (crude onset+nucleus+coda split, count_syllables.vowel_groups convention)
  rime        one sign per syllable rime (nucleus+coda; Sektu's 2017 rhyme-group hypothesis)
  word        one sign per word (a nomenclator / word code)
  shorthand   a phonetic alphabet: letters with silent final e/s/t and doubled consonants dropped (K about 25),
              the token profile a Duployé/Prévost-Delaunay style writing would leave (its sign SHAPES are strokes,
              a separate census below)
Statistics per sequence: K (types), hapax share, top-1 share, top-5 share, IC, doubled-adjacent rate, bigram-repeat
share (share of bigram tokens whose type recurs), mean line length is not used (no lines in prose). 200 samples per
unit at each N (pooled 1251 and per cryptogram), seed 1; a statistic is "consistent" with a unit when the target sits
inside the samples' 2.5-97.5 pct band. Target: ciphertext_draft.tsv (c1 = the H2-settled draft), 160-id and base
levels. Shape census (descriptive, from inventory names): shares of ids that are pictograms, Latin/Greek letters,
typographic/astronomical symbols, composites (base + stacked marks), abstract strokes. Writes h3_profile.json."""
import csv, os, sys, json, gzip, random, re, collections, unicodedata
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
here = os.path.dirname(os.path.abspath(__file__)); root = os.path.dirname(here); repo = os.path.dirname(os.path.dirname(root))
def fold(s):
    s = unicodedata.normalize('NFD', s.lower()); return ''.join(ch for ch in s if unicodedata.category(ch) != 'Mn').replace('œ', 'oe').replace('æ', 'ae')
def corpus_words():
    W = []
    for f in sorted(os.listdir(os.path.join(repo, 'tools/data/fr19'))):
        if f.endswith('.txt.gz'): W += re.findall(r"[a-z]+", fold(gzip.open(os.path.join(repo, 'tools/data/fr19', f), 'rt', encoding='utf-8', errors='ignore').read()))
    return W
def syll(w):
    parts = re.findall(r"[^aeiouy]*[aeiouy]+", w); tail = w[len(''.join(parts)):]
    if not parts: return [w]
    parts[-1] += tail; return parts
def rime(w): return [re.sub(r"^[^aeiouy]+", '', s) for s in syll(w)]
def shorthand(w):
    w = re.sub(r"(.)\1", r"\1", w); w = re.sub(r"[est]$", '', w) if len(w) > 2 else w; return list(w)
UNITS = {'letter': lambda ws: [c for w in ws for c in w], 'syllable': lambda ws: [s for w in ws for s in syll(w)], 'rime': lambda ws: [s for w in ws for s in rime(w)],
         'word': lambda ws: list(ws), 'shorthand': lambda ws: [c for w in ws for c in shorthand(w)]}
def homoph(letters, K, rng):
    cnt = collections.Counter(letters); units = [u for u, _ in cnt.most_common()]; alloc = {u: 1 for u in units}
    extra = K - len(units); tot = sum(cnt.values())
    for _ in range(max(0, extra)):
        u = max(units, key=lambda x: cnt[x] / tot / alloc[x]); alloc[u] += 1
    sid = 0; signs = {}
    for u in units: signs[u] = list(range(sid, sid + alloc[u])); sid += alloc[u]
    return [rng.choice(signs[u]) for u in letters]
def stats(seq):
    n = len(seq); c = collections.Counter(seq); K = len(c); srt = sorted(c.values(), reverse=True)
    ic = sum(v * (v - 1) for v in c.values()) / (n * (n - 1)) if n > 1 else 0
    dbl = sum(seq[i] == seq[i + 1] for i in range(n - 1)) / (n - 1)
    bg = collections.Counter(zip(seq, seq[1:])); brep = sum(v for v in bg.values() if v >= 2) / max(1, n - 1)
    return dict(K=K, hapax=sum(v == 1 for v in c.values()) / K, top1=srt[0] / n, top5=sum(srt[:5]) / n, IC=ic, doubled=dbl, bigram_repeat=brep)
def target(level):
    p = 'ciphertext_draft.tsv' if level == 'id160' else 'ciphertext_draft_base.tsv'
    seqs = collections.defaultdict(list)
    for r in csv.DictReader(open(os.path.join(root, p)), delimiter='\t'):
        if r['sign'] in ('_', 'MULTI'): continue
        g = r['line'].split('_')[0]; g = {'c2a': 'c2', 'c2b': 'c2', 'c4a0': 'c4', 'c4a': 'c4', 'c4b': 'c4'}.get(g, g); seqs[g].append(r['sign']); seqs['all'].append(r['sign'])
    if level == 'id160':  # c1 from the H2-settled draft, c2 from the H21-settled draft when present (28 Sept 2026)
        seqs['c1'] = [r['sign'].rstrip('?') for r in csv.DictReader(open(os.path.join(root, 'ciphertext_c1_draft.tsv')), delimiter='\t') if r['sign'].rstrip('?') not in ('_', 'MULTI')]
        p2 = os.path.join(root, 'ciphertext_c2_draft.tsv')
        if os.path.exists(p2): seqs['c2'] = [r['sign'].rstrip('?') for r in csv.DictReader(open(p2), delimiter='\t') if r['sign'].rstrip('?') not in ('_', 'MULTI')]
        p34 = os.path.join(root, 'ciphertext_c34_draft.tsv')
        if os.path.exists(p34):
            seqs['c3'] = []; seqs['c4'] = []
            for r in csv.DictReader(open(p34), delimiter='\t'):
                s_ = r['sign'].rstrip('?')
                if s_ in ('_', 'MULTI'): continue
                seqs['c3' if r['line'].startswith('c3') else 'c4'].append(s_)
        seqs['all'] = seqs['c1'] + seqs['c2'] + seqs['c3'] + seqs['c4']
    return seqs
def main():
    rng = random.Random(1); W = corpus_words(); print('corpus words', len(W), file=sys.stderr)
    per_unit_stream = {u: f(W) for u, f in UNITS.items()}
    res = {}
    for level in ('id160', 'base'):
        T = target(level)
        for g, seq in T.items():
            N = len(seq); ts = stats(seq); row = dict(N=N, target=ts, units={})
            for u, stream in list(per_unit_stream.items()) + [('homoph', per_unit_stream['letter'])]:
                samp = []
                for _ in range(200):
                    o = rng.randrange(len(stream) - N); s = stream[o:o + N]
                    if u == 'homoph': s = homoph(s, ts['K'], rng)
                    samp.append(stats(s))
                band = {}
                for k in ts:
                    v = sorted(x[k] for x in samp); lo, hi = v[4], v[194]; band[k] = dict(lo=lo, hi=hi, median=v[99], inside=bool(lo <= ts[k] <= hi))
                row['units'][u] = band
            res[f'{level}:{g}'] = row
            cons = {u: sum(b[k]['inside'] for k in ts) for u, b in row['units'].items()}
            print(f"{level} {g} N={N} K={ts['K']} top1={ts['top1']:.3f} hapax={ts['hapax']:.2f} IC={ts['IC']:.4f} dbl={ts['doubled']:.3f} bgrep={ts['bigram_repeat']:.3f} | statistics inside band (of 7): " + ', '.join(f"{u} {n}" for u, n in cons.items()), flush=True)
    # shape census
    inv = [r['sign'] for r in csv.DictReader(open(os.path.join(root, 'glyphs/inventory.tsv')), delimiter='\t') if r['sign'] not in ('_', 'MULTI')]
    cnt = {r['sign']: int(r['count']) for r in csv.DictReader(open(os.path.join(root, 'glyphs/inventory.tsv')), delimiter='\t')}
    def cls(s):
        if s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM'): return 'pictogram'
        if s.endswith('-LETTER') or s in ('LAMBDA', 'PHI', 'RHO', 'DELTA', 'SIGMA', 'OMEGA', 'THETA', 'ALPHA', 'GAMMA', 'PSI', 'LAMBDA-DASH', 'THETA-BAR'): return 'letter'
        if s in ('PCT', 'PCT-SLASH', 'AMP', 'DOLLAR', 'VENUS', 'MARS', 'QUESTION', 'NOTE', 'EIGHT', 'NINE', 'TWO', 'SIX-CURL', 'DIAMOND', 'CROSS-T', 'DAGGER-O'): return 'symbol'
        if re.search(r"TILDE|DASH|BAR|DOT|CC-|II-|ARCH|-O$", s): return 'composite'
        return 'stroke'
    census = collections.Counter(); tokens = collections.Counter()
    for s in inv: census[cls(s)] += 1; tokens[cls(s)] += cnt.get(s, 0)
    res['shape_census'] = dict(types=dict(census), tokens=dict(tokens))
    print('shape census (types):', dict(census), '(tokens):', dict(tokens))
    json.dump(res, open(os.path.join(root, 'h3_profile.json'), 'w'), indent=1)
if __name__ == '__main__': main()

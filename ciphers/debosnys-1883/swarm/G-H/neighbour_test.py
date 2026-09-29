"""Task 3: whole-word signs, the Copiale signature, tested blind.
In the Copiale the word symbols (large logograms) sit between word spaces: 74 pct of their neighbours are space
signs, against 20 pct for letter signs (logogram_copiale.json). Blind form (no space class assumed): the neighbour
tokens of the candidate word signs are concentrated on a few sign types, compared with the global sign curve.
Statistic G = 2 * sum_s o_s ln(o_s / e_s) over the neighbour tokens' sign types (o observed, e expected from the
global frequencies of non-candidate signs). Null: the same number of anchor tokens drawn at random from
non-candidate positions (2000 draws). Control first: Copiale windows holding exactly Debosnys's count of word-symbol
tokens (60), five windows; then Debosnys's pictograms (H31's class: PICT-*, SUN, STAR, HEART, RAM) on all four
settled drafts, within-line neighbours only."""
import collections, csv, math, random, json, sys
from copiale_key import LOGO
def G(seq, anchors, cand):
    nb = []
    for i in anchors:
        if i - 1 >= 0 and seq[i-1] is not None and seq[i-1] not in cand: nb.append(seq[i-1])
        if i + 1 < len(seq) and seq[i+1] is not None and seq[i+1] not in cand: nb.append(seq[i+1])
    glob = collections.Counter(s for s in seq if s is not None and s not in cand); tot = sum(glob.values())
    o = collections.Counter(nb); n = len(nb)
    return 2 * sum(c * math.log(c / (n * glob[s] / tot)) for s, c in o.items())
def test(seq, cand, draws=2000, seed=1):
    anchors = [i for i, s in enumerate(seq) if s in cand]
    pool = [i for i, s in enumerate(seq) if s is not None and s not in cand]
    obs = G(seq, anchors, cand); rng = random.Random(seed)
    null = sorted(G(seq, rng.sample(pool, len(anchors)), cand) for _ in range(draws))
    return {'anchors': len(anchors), 'G': round(obs, 1), 'null_p50': round(null[draws//2], 1),
            'null_p99': round(null[int(draws*.99)], 1), 'p': (sum(x >= obs for x in null) + 1) / (draws + 1)}
out = {}
# control: Copiale windows with exactly 60 logogram tokens (line breaks as None separators)
rows = [l.rstrip('\n').split('\t') for l in open('data/copiale_tokens.tsv')][1:]
seqc = []; prev = None
for pg, li, pos, t, g in rows:
    if (pg, li) != prev and seqc: seqc.append(None)
    seqc.append(t); prev = (pg, li)
logo_pos = [i for i, s in enumerate(seqc) if s in LOGO]
out['copiale_60'] = []
for k in range(5):
    a = logo_pos[k * 80]; b = logo_pos[k * 80 + 59] + 1
    out['copiale_60'].append(dict(test(seqc[a:b], LOGO, seed=k), window_tokens=b - a))
# size-matched control: 1,184-token Copiale windows (Debosnys's N) with the natural logograms removed and 60 whole
# words replaced by one word-symbol token each (23 types, Debosnys's pictogram count curve), so the design is present
# at Debosnys's density and event count
from copiale_key import SPACE
curve = [10, 9, 5, 5, 4, 4, 2, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
out['copiale_planted_1184'] = []
for k in range(5):
    rng = random.Random(100 + k)
    w = [t for t in seqc[k * 12000: k * 12000 + 1600] if t not in LOGO]
    words = []; i = 0
    while i < len(w):
        if w[i] is not None and w[i] not in SPACE:
            j = i
            while j < len(w) and w[j] is not None and w[j] not in SPACE: j += 1
            words.append((i, j)); i = j
        else: i += 1
    pick = sorted(rng.sample(words, 60)); types = [f'W{n}' for n, c in enumerate(curve) for _ in range(c)]
    rng.shuffle(types); new = []; last = 0
    for (i, j), ty in zip(pick, types):
        new += w[last:i] + [ty]; last = j
    new += w[last:]
    new = new[:1184 + new[:1184].count(None)]
    cand = {t for t in new if t and t.startswith('W')}
    out['copiale_planted_1184'].append(dict(test(new, cand, seed=k), tokens=sum(1 for t in new if t)))
# Debosnys: all four settled drafts, lines separated
seqd = []
for f in ['ciphertext_c1_draft.tsv', 'ciphertext_c2_draft.tsv', 'ciphertext_c34_draft.tsv']:
    prev = None
    for r in csv.DictReader(open(f'../../{f}'), delimiter='\t'):
        s = r['sign'].rstrip('?')
        if s in ('_', 'MULTI', ''): continue
        if r['line'] != prev and seqd: seqd.append(None)
        seqd.append(s); prev = r['line']
pict = {s for s in seqd if s and (s.startswith('PICT-') or s in ('SUN', 'STAR', 'HEART', 'RAM'))}
out['debosnys_pictograms'] = dict(test(seqd, pict), tokens=sum(1 for s in seqd if s))
# which signs flank the pictograms most, vs their base rate (descriptive)
nbc = collections.Counter(); 
for i, s in enumerate(seqd):
    if s in pict:
        for j in (i - 1, i + 1):
            if 0 <= j < len(seqd) and seqd[j] and seqd[j] not in pict: nbc[seqd[j]] += 1
glob = collections.Counter(s for s in seqd if s and s not in pict); tot = sum(glob.values()); n = sum(nbc.values())
out['debosnys_top_flankers'] = [(s, c, round(n * glob[s] / tot, 1)) for s, c in nbc.most_common(8)]
print(json.dumps(out, indent=1)); json.dump(out, open('neighbour_test.json', 'w'), indent=1)

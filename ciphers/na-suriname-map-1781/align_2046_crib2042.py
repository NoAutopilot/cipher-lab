#!/usr/bin/env python3
"""SUR-ALIGN (13 Oct 2026): 4.VEL 2046's decoded text block (title, headings, No.1-3, legend a-k) against the plain
Purmerent legend of 4.VEL 2042 (crib_2042_legend.tsv), with the controls pre-registered in PREREG-SUR-ALIGN.md.

Not a DP and not tools/interlinear_align.py: that tool aligns a cipher line to the plain line printed with it; 2042 is a
sibling map's plain legend, not a gloss of 2046 (GAPS6: same-label null for 2039), so the model here is a word-anchor scan.

S  (primary, label-free): number of distinct crib words (>= 5 letters) that anchor somewhere in the 2046 block. A word of
   length L anchors at a segment offset when every slot lies inside one segment (segments are cut at plain tokens: labels,
   gun counts), no keyed slot disagrees (a two-valued M slot such as g|l agrees if either letter fits), keyed agreements
   >= max(4, L-2) and wildcard (U) slots <= 2.
S1 (secondary, the brief's entry-by-entry): mean over 2046 legend entries a-k of the best-offset fraction of keyed slots
   equal to the same-label 2042 entry's letters (GAPS5/6's same-label score).
Controls (seeded, N each): value-shuffle (key values permuted among the sign classes present: every (sign, value) pair
gets another pair's value), crib-letter shuffle (letters permuted within each crib entry, word lengths kept), label
shuffle (crib entries permuted across labels; identical to the target for S by construction, reported as such).

Usage: python3 align_2046_crib2042.py [--n 1000] [--seed 20261013] [--dry] [--anchors]
--dry prints the crib words and slot counts only (no score); --anchors prints the real anchors and the U/M slots they cover.
"""
import csv, os, random, re, statistics, sys
here = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
N = int(args[args.index('--n') + 1]) if '--n' in args else 1000
SEED = int(args[args.index('--seed') + 1]) if '--seed' in args else 20261013

def rows(fn):
    return csv.DictReader((l for l in open(os.path.join(here, fn), encoding='utf-8') if not l.startswith('#')), delimiter='\t')

# ---- target slots ----
lines = {}
for r in rows('reading_2046_legend_nieuw_tokens.tsv'):
    lines.setdefault(r['line'], []).append((int(r['pos']), r['sign'], r['value'], r['grade']))
segments = []   # list of (line, [(pos, sign, value, grade)])
for ln, toks in lines.items():
    toks.sort()
    cur = []; last = None
    for t in toks:
        if last is not None and t[0] != last + 1:
            if cur: segments.append((ln, cur))
            cur = []
        cur.append(t); last = t[0]
    if cur: segments.append((ln, cur))

def slotset(value, grade):
    if grade == 'U' or value in ('?', ''):
        return None
    return frozenset(value.split('|'))

# ---- crib ----
def norm(s):
    s = s.lower().replace('ÿ', 'y').replace('ij', 'y').replace('à', 'a')
    return s
crib_entries = {}; last = None
for r in rows('crib_2042_legend.tsv'):
    e = r['entry']
    if len(e) == 1 and e.islower() and e in crib_entries and not r['label']:
        crib_entries[e] += '\n' + norm(r['text'])   # continuation row (h, i): entry repeated, label empty
    elif len(e) == 1 and e.islower():
        crib_entries[e] = norm(r['text']); last = e
    elif e == '' and last:
        crib_entries[last] += '\n' + norm(r['text'])
def words_of(text):
    text = re.sub(r',\s*\n\s*', '', text)       # "Provi,\nant" -> "proviant" (word broken at the line end)
    return re.findall(r'[a-z]+', text)
entry_words = {e: words_of(t) for e, t in crib_entries.items()}

def crib_words(ew):
    return sorted({w for ws in ew.values() for w in ws if len(w) >= 5})

def anchors(segs_vals, words):
    """segs_vals: list of (line, [(pos, sign, set|None)]); returns list of (word, line, start_pos, slots)."""
    out = []
    for w in words:
        L = len(w)
        for ln, sl in segs_vals:
            for o in range(0, len(sl) - L + 1):
                agree = wild = 0; ok = True
                for k in range(L):
                    s = sl[o + k][2]
                    if s is None: wild += 1
                    elif w[k] in s: agree += 1
                    else: ok = False; break
                if ok and wild <= 2 and agree >= max(4, L - 2):
                    out.append((w, ln, sl[o][0], [(sl[o + k][0], sl[o + k][1], w[k]) for k in range(L)]))
    return out

def S(segs_vals, words):
    return len({a[0] for a in anchors(segs_vals, words)})

def real_vals():
    return [(ln, [(p, sg, slotset(v, g)) for p, sg, v, g in sl]) for ln, sl in segments]

def value_shuffled(rng):
    pairs = sorted({(sg, v) for _, sl in segments for _, sg, v, g in sl if slotset(v, g) is not None})
    vals = [v for _, v in pairs]; rng.shuffle(vals)
    m = dict(zip(pairs, vals))
    return [(ln, [(p, sg, slotset(m[(sg, v)], 'H') if slotset(v, g) is not None else None) for p, sg, v, g in sl])
            for ln, sl in segments]

def crib_letter_shuffled(rng):
    out = {}
    for e, ws in entry_words.items():
        letters = list(''.join(ws)); rng.shuffle(letters)
        i = 0; nw = []
        for w in ws:
            nw.append(''.join(letters[i:i + len(w)])); i += len(w)
        out[e] = nw
    return out

def label_shuffled(rng):
    labs = sorted(entry_words); perm = labs[:]; rng.shuffle(perm)
    return {a: entry_words[b] for a, b in zip(labs, perm)}

# ---- S1: same-label ----
def legend_entries(vals):
    """2046 legend entries a-k from the leg_* lines: entries are the segments of the leg_ lines in reading order."""
    order = {'2046_leg_abc': 'abc', '2046_leg_d': 'd', '2046_leg_efgh': 'efgh', '2046_leg_ki': 'ki'}
    out = {}
    for ln, labs in order.items():
        segs = [sl for l2, sl in vals if l2 == ln]
        for lab, sl in zip(labs, segs):
            out[lab] = sl
    return out

def S1(vals, ew):
    ent = legend_entries(vals); scores = []
    for lab, sl in ent.items():
        if lab not in ew: continue
        text = ''.join(ew[lab]); keyed = [(i, s) for i, (_, _, s) in enumerate(sl) if s is not None]
        if not keyed or not text: continue
        best = 0.0
        for off in range(-len(sl) + 1, len(text)):
            hit = sum(1 for i, s in keyed if 0 <= i + off < len(text) and text[i + off] in s)
            best = max(best, hit / len(keyed))
        scores.append(best)
    return statistics.mean(scores)

if __name__ == '__main__':
    words = crib_words(entry_words)
    rv = real_vals()
    if '--dry' in args:
        print('crib words >=5:', len(words), ' '.join(words))
        print('segments:', len(segments), 'slots:', sum(len(s) for _, s in segments),
              'U slots:', sum(1 for _, s in rv for x in s if x[2] is None))
        ent = legend_entries(rv); print('2046 legend entries (lengths):', {k: len(v) for k, v in ent.items()})
        sys.exit(0)
    rng = random.Random(SEED)
    sr = S(rv, words); s1r = S1(rv, entry_words)
    cv = [S(value_shuffled(rng), words) for _ in range(N)]
    cl = [S(rv, crib_words(crib_letter_shuffled(rng))) for _ in range(N)]
    lb = [S(rv, crib_words(label_shuffled(rng))) for _ in range(N)]
    s1v = [S1(value_shuffled(rng), entry_words) for _ in range(N)]
    s1l = [S1(rv, label_shuffled(rng)) for _ in range(N)]
    def summ(name, real, xs):
        xs2 = sorted(xs); p95 = xs2[int(0.95 * len(xs2)) - 1]; p99 = xs2[int(0.99 * len(xs2)) - 1]
        ge = sum(1 for x in xs if x >= real)
        print(f'{name}: real {real:.4g} | null mean {statistics.mean(xs):.4g} sd {statistics.pstdev(xs):.4g} '
              f'p95 {p95:.4g} p99 {p99:.4g} max {max(xs):.4g} | >= real {ge}/{len(xs)} ({ge/len(xs):.3f}) '
              f'| distinct null values {len(set(xs))}')
        return ge / len(xs)
    print(f'N {N} seed {SEED}; crib words {len(words)}')
    fv = summ('S  vs value-shuffle', sr, cv)
    fc = summ('S  vs crib-letter-shuffle', sr, cl)
    summ('S  vs label-shuffle (identical by construction)', sr, lb)
    f1v = summ('S1 vs value-shuffle', s1r, s1v)
    f1l = summ('S1 vs label-shuffle', s1r, s1l)
    print('S gate (<= 0.01 of both value- and crib-letter-shuffle at or above real):',
          'PASS' if fv <= 0.01 and fc <= 0.01 else 'FAIL')
    print('S1 gate (<= 0.05 of both value- and label-shuffle at or above real):',
          'PASS' if f1v <= 0.05 and f1l <= 0.05 else 'FAIL')
    if '--anchors' in args:
        for w, ln, p, sl in anchors(rv, words):
            cov = []
            for pp, sg, c in sl:
                g = [t for t in lines[ln] if t[0] == pp][0]
                if g[3] in ('U', 'M'):
                    cov.append(f'{pp}:{sg}={g[2]}/{g[3]}->{c}')
            print(f'ANCHOR {w} {ln}:{p}  ' + ' '.join(cov))

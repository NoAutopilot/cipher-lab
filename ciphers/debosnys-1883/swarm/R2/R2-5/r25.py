#!/usr/bin/env python3
"""DEB-SWARM2 R2-5 FOLGER-SPLIT (29 Sept 2026). Does splitting Debosnys's composite ids into their parts, in reading
order, bring out sequential order that D's frozen battery (swarm/G-D/dcore.py, imported, not edited) does not see in
the unsplit text? Known-answer controls first: a Folger-design text (Bennett's Figure 3 plaintext enciphered by the
design Bennett recovered) and a planted French ligature text, both at Debosnys's unsplit N and line lengths.

Texts (each a pair, c1-shaped + c2-shaped, as D's pair score; noise always at the UNSPLIT (box) level, then split):
  real-T   c1, c2 (dcore.target) split by SPLIT_T: parts top-to-bottom as NOTES.md GOLD-4C describes them
  real-N   c1, c2 split by name order (base first, then the mark's parts)
  folger   FOLGER-LIG: Folger symbols, with Folger's own two-letter figures boxed as one id (OU circle, T+crescent H,
           box letter + E); split = the symbols
  folgerW  FOLGER-WORD (descriptive, not gating): every Folger cluster one id; split = the symbols
  planted  French letters, homophonic at the real split curve, frequent adjacent pairs joined into composite ids
           until composites are the real share of boxes (24 pct); split = the original letters' signs
Calibration, per text at its own split shape: FR/EN/PT/LA-HOMO letters and FR-SYLL (dcore designs, generated at the
split level) against NULL-SPLIT = iid boxes drawn from the text's own UNSPLIT id curve, noised, then split with the
text's own map (so composites' internal pairs are in the null too). NULL-IID (dcore, split level) reported as well.
Usage: r25.py calib TEXT P N OUT | r25.py real TEXT OUT | r25.py show"""
import os, sys, json, random, collections, re
HERE = os.path.dirname(os.path.abspath(__file__)); SW = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(SW, 'G-D')); sys.path.insert(0, os.path.join(SW, 'R2', 'R2-1'))
sys.path.insert(0, os.path.join(os.path.dirname(SW), 'scripts'))
import dcore, r21
from base_mark_recount import COMPOSITE

# ---------------- the split maps (pre-registered in PREREG.md) -----------------
MARK_PARTS = {'DASH2': ['DASH', 'DASH'], 'DASH-DOTS': ['DASH', 'DOTS'], 'BAR-X': ['BAR', 'X'], 'BAR-CC': ['BAR', 'CC'],
              'BAR-O': ['BAR', 'O'], 'DASHBELOW': ['DASH']}
ABOVE = {'TILDE', 'DASH', 'DASH2', 'DOT', 'DOTS', 'DASH-DOTS'}          # marks drawn over the base (NOTES.md GOLD-4C)
BASE_OVER = {'CC-DASH', 'ARCH-DASH'}                                    # "cc over dashes", "arch over dashes"

def split_n(s):
    b, m = COMPOSITE[s]; return [b] + MARK_PARTS.get(m, [m])
def split_t(s):
    b, m = COMPOSITE[s]; parts = MARK_PARTS.get(m, [m])
    if m in ABOVE and s not in BASE_OVER: return parts + [b]
    return [b] + parts
REAL_MAPS = {'real-T': {s: split_t(s) for s in COMPOSITE}, 'real-N': {s: split_n(s) for s in COMPOSITE}}

def apply_split(lines, M):
    return [[p for s in l for p in M.get(s, [s])] for l in lines]

# ---------------- Folger design (Bennett 1979-80, sources/folger/) -----------------
WORDSYM = {'THE', 'AND', 'HE', 'HIS', 'THIS', 'THESE', 'THOSE', 'THEM', 'THEY'}
BOX = set('BDPQ')        # Bennett: four box symbols, D plain, B/P/Q shaded variants of it
def folger_clusters(rng, hv=0.8):
    """Bennett's Figure 3 plaintext -> list of clusters, each a list of Folger symbols. A cluster = a space- or
    hyphen-delimited token (Bennett: a hyphen marks a space in the cipher inside a word). Symbols: one per letter,
    U/V/W one symbol, H after T the crescent variant 'h' with prob hv (Bennett: mostly, not always), the nine word
    symbols as single symbols."""
    txt = ' '.join(l for l in open(os.path.join(HERE, 'folger_fig3.txt')) if not l.startswith('#'))
    out = []
    for w in txt.split():
        bare = re.sub(r'[^A-Z]', '', w)
        if bare in WORDSYM and '-' not in w: out.append(['W' + bare]); continue
        for part in w.split('-'):
            p = re.sub(r'[^A-Z]', '', part)
            if not p: continue
            sy = []
            for i, c in enumerate(p):
                c = 'U' if c in 'VW' else c
                if c == 'H' and i and p[i - 1] == 'T' and rng.random() < hv: c = 'h'
                sy.append(c)
            out.append(sy)
    return out

def folger_lig(clusters):
    """FOLGER-LIG boxes: symbols, with Folger's two-letter figures as one id: OU (the circle), T+h (the crescent
    joined to the gamma), and a word opening with a box letter as one figure (Bennett: the rest of the word is
    drawn inside the box; about 150 boxed words on the page). Returns (box stream, split map)."""
    boxes = []
    for cl in clusters:
        if cl[0] in BOX and len(cl) > 1: boxes.append('+'.join(cl)); continue   # Bennett: the box encloses the rest of its word
        i = 0
        while i < len(cl):
            a = cl[i]; b = cl[i + 1] if i + 1 < len(cl) else None
            if (a, b) in (('O', 'U'), ('T', 'h')) or (a in BOX and b == 'E'): boxes.append(a + '+' + b); i += 2
            else: boxes.append(a); i += 1
    return boxes, {s: s.split('+') for s in set(boxes) if '+' in s}

def folger_word(clusters):
    boxes = ['+'.join(c) for c in clusters]
    return boxes, {s: s.split('+') for s in set(boxes) if '+' in s}

# ---------------- planted French ligature -----------------
def planted(rng, lens1, lens2, share):
    """French letters (dcore corpus, random window) encoded homophonic at a curve, then the most frequent adjacent
    sign pairs (within a line) are joined into composite ids, pair type by pair type, until composites are `share`
    of the boxes. Built long (for later noise and cutting); returns (box stream, split map)."""
    N = int((sum(lens1) + sum(lens2)) * (1 + share) * 1.15) + 10
    seq = dcore.encode(dcore.units('fr', N, rng, 'letters'), SPLIT_CURVE_REAL, rng)
    joined = set(); boxes = seq
    while True:
        nb = len(boxes); comp = sum('+' in s for s in boxes)
        if comp / nb >= share: break
        bg = collections.Counter((a, b) for a, b in zip(boxes, boxes[1:]) if '+' not in a and '+' not in b)
        pair = next(p for p, _ in bg.most_common() if p not in joined); joined.add(pair)
        out = []; i = 0
        while i < len(boxes):
            if i + 1 < len(boxes) and (boxes[i], boxes[i + 1]) == pair: out.append(boxes[i] + '+' + boxes[i + 1]); i += 2
            else: out.append(boxes[i]); i += 1
        boxes = out
    return boxes, {s: s.split('+') for s in set(boxes) if '+' in s}

# ---------------- texts -----------------
R1, R2 = dcore.target('c1'), dcore.target('c2')
L1, L2 = [len(l) for l in R1], [len(l) for l in R2]
SHARE = sum(s in COMPOSITE for l in R1 + R2 for s in l) / sum(L1 + L2)
SPLIT_CURVE_REAL = dcore.curve_of(apply_split(R1 + R2, REAL_MAPS['real-T']))

def noisy_pair(boxes, M, rng, p, off=None):
    """A pair cut from a long box stream at a random offset (one text, one key): noise at box level (r21.mixnoise,
    3:1 replacement:indel), cut to the real unsplit line lengths, then split with M."""
    N1, N2 = sum(L1), sum(L2); e1, e2 = int(N1 * 1.12) + 3, int(N2 * 1.12) + 3
    if off is None: off = rng.randrange(0, max(1, len(boxes) - e1 - e2))
    a, b = boxes[off:off + e1], boxes[off + e1:off + e1 + e2]
    if len(b) < e2: b = (b + boxes)[:e2]          # wrap (FOLGER-WORD is shorter than the real text)
    t1 = dcore.cut(r21.mixnoise(a, p, rng, N1), L1); t2 = dcore.cut(r21.mixnoise(b, p, rng, N2), L2)
    return apply_split(t1, M), apply_split(t2, M)

def text_source(tid, rng):
    """(box stream or None, split map) for a text; the real texts have fixed lines instead."""
    if tid == 'folger': return folger_lig(folger_clusters(rng))
    if tid == 'folgerW': return folger_word(folger_clusters(rng))
    if tid == 'planted': return planted(rng, L1, L2, SHARE)
    return None, REAL_MAPS[tid]

def shape(tid):
    """Split-level (lens1, lens2, curve) of one instance of the text, and the unsplit id curve with names (for the
    NULL-SPLIT draw) and the split map. Real: the real text. Controls: one fixed clean instance (seed 0)."""
    if tid.startswith('real'):
        M = REAL_MAPS[tid]; s1, s2 = apply_split(R1, M), apply_split(R2, M); ids = collections.Counter(x for l in R1 + R2 for x in l)
    else:
        rng = random.Random(f'r25-shape-{tid}'); boxes, M = text_source(tid, rng)
        s1, s2 = noisy_pair(boxes, M, rng, 0.0, off=0); ids = collections.Counter(boxes)
    return [len(l) for l in s1], [len(l) for l in s2], dcore.curve_of(s1 + s2), ids, M

def null_split(ids, M, rng, p):
    names = list(ids); w = [ids[n] for n in names]; N1, N2 = sum(L1), sum(L2)
    a = rng.choices(names, w, k=int(N1 * 1.12) + 3); b = rng.choices(names, w, k=int(N2 * 1.12) + 3)
    return apply_split(dcore.cut(r21.mixnoise(a, p, rng, N1), L1), M), apply_split(dcore.cut(r21.mixnoise(b, p, rng, N2), L2), M)

DESIGNS = ['FR-HOMO', 'EN-HOMO', 'PT-HOMO', 'LA-HOMO', 'FR-SYLL', 'NULL-SPLIT', 'NULL-IID']

if __name__ == '__main__':
    mode = sys.argv[1]
    if mode == 'show':
        print('composite share of boxes', round(SHARE, 4), 'N', sum(L1), sum(L2))
        for tid in ('real-T', 'real-N', 'folger', 'folgerW', 'planted'):
            a, b, cv, ids, M = shape(tid)
            comp = sum(c for s, c in ids.items() if s in M) / sum(ids.values())
            print(tid, 'split N', sum(a), sum(b), 'K', len(cv), 'box K', len(ids), 'composite ids', len(M), 'box share', round(comp, 3))
        sys.exit()
    tid = sys.argv[2]; lens1, lens2, cv, ids, M = shape(tid)
    if mode == 'calib':
        p, n, out = float(sys.argv[3]), int(sys.argv[4]), sys.argv[5]
        with open(out, 'w') as fo:
            for d in DESIGNS:
                rng = random.Random(f'r25-calib-{tid}-{d}-{p}')
                for i in range(n):
                    if d == 'NULL-SPLIT': a, b = null_split(ids, M, rng, p)
                    else: a, b = r21.make_pair_mix(d, lens1, lens2, cv, rng, p)
                    fo.write(json.dumps(dict(text=tid, design=d, p=p, f=dcore.features(a, b, rng))) + '\n'); fo.flush()
    elif mode == 'real':
        # real texts: 5 seeds x 400 shuffles (as R2-1). Controls ("known answer"): 40 noisy instances at P.
        out = sys.argv[3]
        if tid.startswith('real'):
            s1, s2 = apply_split(R1, M), apply_split(R2, M); u = []
            for seed in range(5): u.append(dcore.features(R1, R2, random.Random(2000 + seed), 400))
            f = [dcore.features(s1, s2, random.Random(1000 + seed), 400) for seed in range(5)]
            res = dict(text=tid, split_N=(sum(map(len, s1)), sum(map(len, s2))), K=len(cv), feats=f, unsplit_feats=u,
                       score={w: [round(dcore.score(x, w), 2) for x in f] for w in ('c1', 'c2', 'pair')},
                       unsplit_score={w: [round(dcore.score(x, w), 2) for x in u] for w in ('c1', 'c2', 'pair')})
        else:
            p, n = float(sys.argv[4]), int(sys.argv[5]); rows = []
            for i in range(n):
                rng = random.Random(f'r25-ctrl-{tid}-{p}-{i}'); boxes, Mi = text_source(tid, rng)
                s1, s2 = noisy_pair(boxes, Mi, rng, p)
                rng2 = random.Random(f'r25-ctrl-{tid}-{p}-{i}'); boxes, Mi = text_source(tid, rng2)
                u1, u2 = noisy_pair(boxes, {}, rng2, p)        # the same instance, not split
                rows.append(dict(split=dcore.features(s1, s2, rng, 100), unsplit=dcore.features(u1, u2, rng2, 100)))
            res = dict(text=tid, p=p, rows=rows)
        json.dump(res, open(out, 'w'), indent=0); print(tid, 'done')

#!/usr/bin/env python3
"""SUR-2046A (15 Oct 2026): the 4.VEL 2046 [d-hook] = e wider-vocabulary anchor test, pre-registered in
PREREG-SUR-2046A.md before any score.

SUR-ALIGN's anchor rule (align_2046_crib2042.py: a word of length L anchors where every slot lies in one segment, no keyed
slot disagrees, a two-valued slot agrees if either letter fits, keyed agreements >= max(4, L-2), wildcards (U) <= 2) with a
wider frozen vocabulary: every word of >= 5 letters seen >= 3 times in tools/data/nl18 (Dutch print 1770-1799), plus
vocab_prereg.txt (GAPS14), all folded the same way (lowercase, accents stripped, ij/ÿ -> y, j -> i, z -> s; target values
get the same fold).

For a sign class C (n positions on the 2046 block) and a letter X: every C slot is set to {X}; Score(C, X) = the number of
C positions covered by at least one anchor (the C slot is then keyed and agrees). The value-class null is the other 23
letters at the same positions, which can and do move the statistic.
Decision per class: ACCEPT X if Score(X) is the strict maximum over all letters, Score(X) >= ceil(n/2) and Score(X) minus
the runner-up >= 2; otherwise UNDECIDED.
Controls (same sheet, same frequency class n 9-11, all H except one M token of 5 (valued v), none valued e): h=n (primary), 5=v, [hash]=o, [delta]=a,
6=s. Each control class is blanked to U first, then tested exactly as the target. Gate: h ACCEPTs n AND >= 4 of 5 controls
ACCEPT their key value. Gate FAIL -> non-test, no key edit whatever the target does.

Usage: python3 score_2046_dhook_vocab.py [--dry] [--write-exceptions]
--dry prints vocabulary size and class counts only (no score). --write-exceptions appends the PREREG-licensed rows to
exceptions_nieuw_image.tsv only if the gate PASSes and [d-hook] ACCEPTs e.
"""
import collections, csv, glob, gzip, math, os, re, sys, unicodedata
here = os.path.dirname(os.path.abspath(__file__))
args = sys.argv[1:]
LETTERS = 'abcdefghiklmnopqrstuvwxy'          # after the fold (no j, no z)
TARGET = ('[d-hook]', 'e')
CONTROLS = [('h', 'n'), ('5', 'v'), ('[hash]', 'o'), ('[delta]', 'a'), ('6', 's')]
PRIMARY = 'h'

def fold(s):
    s = unicodedata.normalize('NFKD', s.lower().replace('ÿ', 'y'))
    s = ''.join(c for c in s if not unicodedata.combining(c))
    return s.replace('ij', 'y').replace('j', 'i').replace('z', 's')

def build_vocab():
    c = collections.Counter()
    for f in sorted(glob.glob(os.path.join(here, '..', '..', 'tools', 'data', 'nl18', '*.txt.gz'))):
        t = gzip.open(f, 'rt', encoding='utf-8', errors='replace').read()
        c.update(w for w in re.findall(r'[a-z]+', fold(t)))
    v = {w for w, n in c.items() if len(w) >= 5 and n >= 3}
    for l in open(os.path.join(here, 'vocab_prereg.txt'), encoding='utf-8'):
        if l.strip() and not l.startswith('#'):
            w = re.sub(r'[^a-z]', '', fold(l.strip()))
            if len(w) >= 5: v.add(w)
    return sorted(v)

def rows(fn):
    return csv.DictReader((l for l in open(os.path.join(here, fn), encoding='utf-8') if not l.startswith('#')), delimiter='\t')

lines = {}
for r in rows('reading_2046_legend_nieuw_tokens.tsv'):
    lines.setdefault(r['line'], []).append((int(r['pos']), r['sign'], r['value'], r['grade']))
segments = []
for ln, toks in lines.items():
    toks.sort(); cur = []; last = None
    for t in toks:
        if last is not None and t[0] != last + 1:
            if cur: segments.append((ln, cur))
            cur = []
        cur.append(t); last = t[0]
    if cur: segments.append((ln, cur))

def slotset(v, g):
    if g == 'U' or v in ('?', ''): return None
    return frozenset(fold(x) for x in v.split('|'))

def vals(blank=None, setc=None, x=None):
    out = []
    for ln, sl in segments:
        s2 = []
        for p, sg, v, g in sl:
            if sg == setc: s = frozenset(x)
            elif sg == blank: s = None
            else: s = slotset(v, g)
            s2.append((p, sg, s))
        out.append((ln, s2))
    return out

def by_len(vocab):
    d = collections.defaultdict(list)
    for w in vocab: d[len(w)].append(w)
    return d

def covered(segv, cls, vl):
    """positions (line, pos) of class cls covered by >= 1 anchor; dict pos -> list of words."""
    cov = collections.defaultdict(list)
    for ln, sl in segv:
        idx = [i for i, t in enumerate(sl) if t[1] == cls]
        if not idx: continue
        for L, ws in vl.items():
            for o in range(max(0, min(idx) - L + 1), min(len(sl) - L, max(idx)) + 1):
                if not any(o <= i < o + L for i in idx): continue
                win = sl[o:o + L]
                for w in ws:
                    agree = wild = 0; ok = True
                    for k in range(L):
                        s = win[k][2]
                        if s is None:
                            wild += 1
                            if wild > 2: ok = False; break
                        elif w[k] in s: agree += 1
                        else: ok = False; break
                    if ok and agree >= max(4, L - 2):
                        for k in range(L):
                            if win[k][1] == cls: cov[(ln, win[k][0])].append(w)
    return cov

def test(cls, vl, blank_known):
    n = sum(1 for _, sl in segments for t in sl if t[1] == cls)
    sc = {}; covs = {}
    for x in LETTERS:
        c = covered(vals(blank=cls if blank_known else None, setc=cls, x=x), cls, vl)
        sc[x] = len(c); covs[x] = c
    rank = sorted(LETTERS, key=lambda x: -sc[x])
    top, ru = rank[0], rank[1]
    acc = sc[top] > sc[ru] and sc[top] >= math.ceil(n / 2) and sc[top] - sc[ru] >= 2
    return n, sc, rank, (top if acc else None), covs

if __name__ == '__main__':
    vocab = build_vocab(); vl = by_len(vocab)
    if '--dry' in args:
        print('vocab words:', len(vocab), 'by length:', {k: len(v) for k, v in sorted(vl.items())})
        for cls, kv in [TARGET] + CONTROLS:
            toks = [t for _, sl in segments for t in sl if t[1] == cls]
            print(cls, 'n', len(toks), 'grades', collections.Counter(t[3] for t in toks), 'values', collections.Counter(t[2] for t in toks))
        sys.exit(0)
    res = {}
    for cls, kv in CONTROLS + [TARGET]:
        n, sc, rank, acc, covs = test(cls, vl, blank_known=(cls, kv) in CONTROLS)
        res[cls] = (kv, acc)
        top5 = ' '.join(f'{x}:{sc[x]}' for x in rank[:5])
        role = 'TARGET' if cls == TARGET[0] else ('CONTROL*' if cls == PRIMARY else 'CONTROL')
        print(f'{role} {cls} n {n} hypothesis/key {kv}: score({kv}) {sc[kv]} rank {rank.index(kv) + 1} | top5 {top5} | e {sc["e"]} '
              f'| decision {"ACCEPT " + acc if acc else "UNDECIDED"}{" (= key)" if acc == kv else (" (!= key)" if acc else "")}')
        if cls == TARGET[0] or '--cov' in args:
            for pos, ws in sorted(covs[kv].items()):
                print(f'   {pos[0]}:{pos[1]} {kv} <- {len(ws)} words, e.g. {", ".join(sorted(set(ws))[:6])}')
    ctl_ok = [cls for cls, kv in CONTROLS if res[cls][1] == kv]
    gate = res[PRIMARY][1] == 'n' and len(ctl_ok) >= 4
    print(f'gate: primary h {"ACCEPT n" if res[PRIMARY][1] == "n" else "not accepted"}; controls accepting key value '
          f'{len(ctl_ok)}/5 ({", ".join(ctl_ok)}) -> {"PASS" if gate else "FAIL (non-test)"}')
    tacc = res[TARGET[0]][1]
    verdict = ('decided: [d-hook] = e' if gate and tacc == 'e' else
               'undecided (gate FAIL, non-test)' if not gate else
               f'undecided ([d-hook] {"ACCEPT " + tacc + ", not the hypothesis" if tacc else "UNDECIDED"})')
    print('verdict:', verdict)
    if '--write-exceptions' in args and gate and tacc == 'e':
        with open(os.path.join(here, 'exceptions_nieuw_image.tsv'), 'a', encoding='utf-8') as f:
            for ln, toks in lines.items():
                for p, sg, v, g in sorted(toks):
                    if sg == '[d-hook]':
                        f.write(f'{ln}\t{p}\te\tM\tSUR-2046A wider-vocabulary anchor test (PREREG-SUR-2046A.md, '
                                f'score_2046_dhook_vocab.py): class [d-hook] = e accepted, gate PASS; class-level, M\n')
        print('exceptions written')

#!/usr/bin/env python3
"""SUR-POOL (15 Oct 2026): the [d-hook] = e anchor test pooled over 4.VEL 2046 + 2077, pre-registered in PREREG-SUR-POOL.md
before any score. Second attempt of SUR-2046A's instrument (score_2046_dhook_vocab.py) on new material: anchor rule, frozen
vocabulary, statistic, per-class decision rule and control gate are unchanged; only the token pool grows (2046 + 2077 blocks).

Target: [d-hook], all 15 positions (2046: 10 U; 2077: 4 U + L13:3 at C e), every slot set to X together, n = 15.
Controls: the same five classes, pooled over both blocks where they occur: h = n (primary; 2046 only, n 10, unchanged),
5 = v, [hash] = o, [delta] = a, 6 = s. Pooled n is 28-51, so each pooled control is scored on a matched n = 15 subsample
(rule 3: match N): all the class's positions are set to X (as for the target), coverage is computed once per letter, and
Score is counted over the 15 sampled positions only; draw = min(10, n_2046) positions from 2046 and the rest from 2077
(the target's 10:5 mix), 20 draws per control, seeds 0-19 (random.Random(seed).sample over sorted positions).
A pooled control ACCEPTs its key value when the per-draw decision rule ACCEPTs that value in >= 10 of 20 draws.
Gate (unchanged): h ACCEPTs n AND >= 4 of the 5 controls ACCEPT their key value. Gate FAIL -> non-test, no key edit.

Usage: python3 score_pool_dhook_vocab.py [--dry] [--write-exceptions]
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
for fn in ('reading_2046_legend_nieuw_tokens.tsv', 'reading_2077_legend_nieuw_tokens.tsv'):
    for r in rows(fn):
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

import random
NDRAW, NSUB, ACC_MIN = 20, 15, 10

def positions(cls):
    return sorted((ln, t[0]) for ln, sl in segments for t in sl if t[1] == cls)

def draws(cls):
    ps = positions(cls)
    if len(ps) <= NSUB: return [set(ps)]
    a = [p for p in ps if p[0].startswith('2046')]; b = [p for p in ps if not p[0].startswith('2046')]
    k = min(10, len(a)); out = []
    for s in range(NDRAW):
        r = random.Random(s)
        out.append(set(r.sample(a, k)) | set(r.sample(b, NSUB - k)))
    return out

def decide(sc, n):
    rank = sorted(LETTERS, key=lambda x: (-sc[x], LETTERS.index(x)))
    top, ru = rank[0], rank[1]
    return rank, (top if sc[top] > sc[ru] and sc[top] >= math.ceil(n / 2) and sc[top] - sc[ru] >= 2 else None)

def test_pooled(cls, vl):
    covs = {x: covered(vals(setc=cls, x=x), cls, vl) for x in LETTERS}
    out = []
    for d in draws(cls):
        sc = {x: sum(1 for p in covs[x] if p in d) for x in LETTERS}
        rank, acc = decide(sc, len(d))
        out.append((len(d), sc, rank, acc))
    return out, covs

if __name__ == '__main__':
    vocab = build_vocab(); vl = by_len(vocab)
    if '--dry' in args:
        print('vocab words:', len(vocab))
        for cls, kv in [TARGET] + CONTROLS:
            toks = [(ln, t) for ln, sl in segments for t in sl if t[1] == cls]
            print(cls, 'n', len(toks), '2046', sum(1 for ln, _ in toks if ln.startswith('2046')), '2077',
                  sum(1 for ln, _ in toks if ln.startswith('2077')), 'grades', collections.Counter(t[3] for _, t in toks),
                  'values', collections.Counter(t[2] for _, t in toks), 'draws', len(draws(cls)))
        sys.exit(0)
    res = {}
    for cls, kv in CONTROLS + [TARGET]:
        out, covs = test_pooled(cls, vl)
        nacc = sum(1 for o in out if o[3] == kv)
        accs = collections.Counter(o[3] for o in out)
        role = 'TARGET' if cls == TARGET[0] else ('CONTROL*' if cls == PRIMARY else 'CONTROL')
        if len(out) == 1:
            n, sc, rank, acc = out[0]
            dec = acc
            print(f'{role} {cls} n {n} hyp/key {kv}: score({kv}) {sc[kv]} rank {rank.index(kv) + 1} | top5 '
                  f'{" ".join(f"{x}:{sc[x]}" for x in rank[:5])} | decision {"ACCEPT " + acc if acc else "UNDECIDED"}')
        else:
            dec = kv if nacc >= ACC_MIN else None
            sk = sorted(o[1][kv] for o in out)
            print(f'{role} {cls} pooled n {len(positions(cls))} (full-pool covered for {kv}: {len(covs[kv])}), {len(out)} draws of '
                  f'{NSUB}: ACCEPT {kv} in {nacc}/{len(out)}; score({kv}) median {sk[len(sk)//2]} range {sk[0]}-{sk[-1]}; per-draw '
                  f'decisions {dict((k or "UNDECIDED", v) for k, v in accs.items())} -> {"ACCEPT " + kv if dec else "UNDECIDED"}')
        res[cls] = (kv, dec)
        if cls == TARGET[0]:
            for pos, ws in sorted(covs[kv].items()):
                print(f'   {pos[0]}:{pos[1]} {kv} <- {len(ws)} words, e.g. {", ".join(sorted(set(ws))[:6])}')
    ctl_ok = [cls for cls, kv in CONTROLS if res[cls][1] == kv]
    gate = res[PRIMARY][1] == 'n' and len(ctl_ok) >= 4
    print(f'gate: primary h {"ACCEPT n" if res[PRIMARY][1] == "n" else "not accepted"}; controls accepting key value '
          f'{len(ctl_ok)}/5 ({", ".join(ctl_ok)}) -> {"PASS" if gate else "FAIL (non-test)"}')
    tacc = res[TARGET[0]][1]
    print('verdict:', 'decided: [d-hook] = e' if gate and tacc == 'e' else 'undecided (gate FAIL, non-test)' if not gate else
          f'undecided ([d-hook] {"ACCEPT " + tacc + ", not the hypothesis" if tacc else "UNDECIDED"})')
    if '--write-exceptions' in args and gate and tacc == 'e':
        with open(os.path.join(here, 'exceptions_nieuw_image.tsv'), 'a', encoding='utf-8') as f:
            for ln, toks in lines.items():
                for p, sg, v, g in sorted(toks):
                    if sg == '[d-hook]' and g == 'U':
                        f.write(f'{ln}\t{p}\te\tM\tSUR-POOL pooled anchor test (PREREG-SUR-POOL.md, score_pool_dhook_vocab.py): '
                                f'class [d-hook] = e accepted, gate PASS; class-level, M\n')
        print('exceptions written')

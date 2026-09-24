#!/usr/bin/env python3
"""Propose values for signs key.tsv does not cover, by scoring decoded context under a period French model,
with a matched control on hidden keyed signs (CLAUDE.md rule 3). Section "f.30 unkeyed signs (24 Sept 2026)".

  python3 infer_unkeyed.py control   blind runs hiding frequency-matched keyed signs; writes control_f30.tsv
  python3 infer_unkeyed.py target    the same procedure on the unkeyed signs; writes infer_f30.tsv
Deterministic (fixed seeds). Needs tools/french16_ngram.py (model built from tools/data/fr16).

Procedure (identical in both modes): every token whose sign has a key value is decoded with it (key.tsv as is,
M values included, exactly as decode.py reads); every sign in the hidden set, and every other unkeyed sign, has
no value. Greedy: for each still-unassigned hidden sign and each candidate value (23 letters, NULL, word signs),
score all its occurrences on both leaves (f.29r and f.30r-v, lines run on) in a window of +-W tokens:
sum over the unbroken segments of log2 P(segment) + C * len(segment) (C = model bits/char, so a letter costs
nothing on average and NULL gains nothing by shortening the text), minus WPEN per occurrence for a multi-letter value. Fix the sign whose best value leads the
second by the largest margin, decode it, and repeat. The margin (bits, summed over occurrences) at the moment
a sign is fixed is its confidence. A sign with no value inside a window is filled with the model's likeliest
letter (uncharged) so context runs across it (WILD=1).
Settings W=8, WPEN=3, NPEN=0, WILD=1, small word-sign set were chosen on control draws 0-4 only; draws 5-9
are the held-out check. A word-coverage bonus (tested at 0.5 and 1 bit per char in an earlier version of this
script), the large word-sign set and a null penalty (NPEN 3-10) all lowered the control score and are off. Acceptance rule (also fixed on draws 0-4): value not NULL, sign occurs >= 5 times,
margin >= 10 bits.
"""
import os, sys, math, random, functools, collections
if '--help' in sys.argv or '-h' in sys.argv: print(__doc__); sys.exit(0)
H = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(H, '..', '..', 'tools'))
from french16_ngram import load
M = load()
W, WPEN, NPEN = (float(os.environ.get(k, d)) for k, d in (('W', 8), ('WPEN', 3.0), ('NPEN', 0.0)))
W = int(W)
C = M.bits_per_char
WILD = int(os.environ.get('WILD', 1))
WORDSIGNS = {'small': ['ET', 'COM', 'SS', 'LL'],
             'large': ['ET', 'COM', 'CON', 'SS', 'LL', 'PAR', 'POVR', 'QVE', 'DE', 'LE', 'ES', 'EN', 'NT', 'RE', 'ST',
                       'VS', 'ER', 'ON', 'MENT']}[os.environ.get('WS', 'small')]
CANDS = list(M.alpha) + ['NULL'] + WORDSIGNS

def rows(fn):
    for l in open(os.path.join(H, fn), encoding='utf-8'):
        if l.strip() and not l.startswith('#'): yield l.rstrip('\n').split('\t')
KEY = {r[0]: (r[1], r[2]) for r in rows('key.tsv') if r[0] != 'code'}
def keyval(s):
    v = KEY.get(s, ('', ''))[0]
    return None if v in ('', '?') else v

def streams():
    """Two token streams (lists of (sign, where)) with lines run on: f.29r and f.30r-v."""
    s29 = []
    for l in open(os.path.join(H, 'ciphertext.txt'), encoding='utf-8'):
        if not l.strip() or l.startswith('#'): continue
        head, body = l.split('|', 1)
        for i, t in enumerate(body.split()):
            if t != '.': s29.append((t.rstrip('?') if t != '[?]' else t, head.strip() + f' {i}'))
    s30 = [(r[2], f'{r[0]} {r[1]}') for r in rows('ciphertext_f30.tsv') if r[0] != 'line' and r[2] != '.']
    return [s29, s30]
S = streams()
COUNT = collections.Counter(t for s in S for t, _ in s)

@functools.lru_cache(maxsize=None)
def seg_score(seg):
    """Score a string in which '?' marks a sign with no value. With WILD=1 (default) each '?' is filled greedily with
    the letter the model likes best after the preceding context, so context flows across it; with WILD=0 a '?' is a
    break. The filler letters are not charged, only the known letters."""
    if WILD:
        out, tot = '', 0.0
        for ch in seg:
            h = out[-(M.order - 1):]
            if ch == '?': out += max(M.alpha, key=lambda a: M.p(h, a))
            else: tot += math.log2(M.p(h, ch)) + C; out += ch
        return tot
    return sum(M.logp(x) + C * len(x) for x in seg.split('?'))

def score(sign, val, assign):
    tot = 0.0
    for s in S:
        idx = [i for i, (t, _) in enumerate(s) if t == sign]
        for i in idx:
            cur = ''
            for t, _ in s[max(0, i - W):i + W + 1]:
                v = val if t == sign else assign.get(t) or keyval(t)
                cur += '?' if v is None else '' if v == 'NULL' else v
            tot += seg_score(cur)
            if len(val) > 1 and val != 'NULL': tot -= WPEN
            if val == 'NULL': tot -= NPEN
    return tot

def run(hidden, known_hidden_as_breaks=()):
    """Greedy assignment of the hidden signs. Returns [(sign, value, margin, second)] in assignment order."""
    saved = {s: KEY.pop(s) for s in hidden if s in KEY}
    try:
        assign, out, left = {}, [], [s for s in hidden if COUNT[s]]
        while left:
            best = None
            for s in left:
                sc = sorted(((score(s, v, assign), v) for v in CANDS), reverse=True)
                m = sc[0][0] - sc[1][0]
                if best is None or m > best[2]: best = (s, sc[0][1], m, sc[1][1])
            assign[best[0]] = best[1]; out.append(best); left.remove(best[0])
        return out
    finally:
        KEY.update(saved)

UNKEYED = [s for s, n in COUNT.most_common() if keyval(s) is None and n >= 2 and s != '[?]']

# keyed signs whose f.30 contexts the reconciler flagged against the table value (NOTES "f.30 reading"): their
# true value here is in doubt, so they cannot serve as control truth.
DOUBTFUL = {'Tb', 'eh', 'H', 'q'}

def matched_draw(seed):
    """For each unkeyed target sign, a keyed H sign (not word-sign valued) of the nearest total count."""
    rnd = random.Random(seed)
    pool = [s for s in COUNT if keyval(s) and KEY[s][1] == 'H' and s != '[?]' and s not in DOUBTFUL]
    pick = []
    for u in UNKEYED:
        cand = sorted((s for s in pool if s not in pick), key=lambda s: (abs(COUNT[s] - COUNT[u]), rnd.random()))[:5]
        pick.append(rnd.choice(cand))
    return pick

def band(n): return 'n>=10' if n >= 10 else '5-9' if n >= 5 else '2-4'

if __name__ == '__main__':
    mode = sys.argv[1] if len(sys.argv) > 1 else 'target'
    if mode == 'control':
        lines = ['draw\tsign\tcount\tband\ttrue\tproposed\tmargin\tsecond\tcorrect']
        for d in range(*(int(x) for x in (sys.argv[2:4] if len(sys.argv) > 3 else (0, 10)))):
            hid = matched_draw(1000 + d)
            for s, v, m, sec in run(hid):
                ok = v == KEY[s][0]
                lines.append(f'{d}\t{s}\t{COUNT[s]}\t{band(COUNT[s])}\t{KEY[s][0]}\t{v}\t{m:.1f}\t{sec}\t{int(ok)}')
            print(f'draw {d}: {sum(l.endswith("1") for l in lines if l.startswith(str(d)+chr(9)))}/{len(hid)}', flush=True)
        open(os.path.join(H, os.environ.get('OUT', 'control_f30.tsv')), 'w').write('\n'.join(lines) + '\n')
    elif mode == 'doubtful':   # information only: the keyed signs flagged in NOTES, hidden and re-inferred
        for s, v, m, sec in run(sorted(DOUBTFUL)): print(f'{s}\ttable {KEY[s][0]}\tcontext {v}\tmargin {m:.1f}\tsecond {sec}')
    else:
        lines = ['sign\tcount\tband\tproposed\tmargin\tsecond\torder']
        for k, (s, v, m, sec) in enumerate(run(UNKEYED)):
            lines.append(f'{s}\t{COUNT[s]}\t{band(COUNT[s])}\t{v}\t{m:.1f}\t{sec}\t{k}')
            print(lines[-1], flush=True)
        open(os.path.join(H, 'infer_f30.tsv'), 'w').write('\n'.join(lines) + '\n')
        # accepted values -> key_extension_f30.tsv (decode.py reads it); control numbers from control_f30.tsv
        c = [l.rstrip('\n').split('\t') for l in open(os.path.join(H, 'control_f30.tsv'))][1:]
        acc = lambda v, n, m: v != 'NULL' and n >= 5 and m >= 10
        ca = [l for l in c if acc(l[5], int(l[2]), float(l[6]))]
        ctl = lambda b: f'{sum(int(l[8]) for l in ca if l[3] == b)}/{sum(1 for l in ca if l[3] == b)}'
        ext = ['code\tvalue\tgrade\tsource']
        for l in lines[1:]:
            s, n, b, v, m, sec, k = l.split('\t')
            if acc(v, int(n), float(m)):
                ext.append(f'{s}\t{v}\tS\tinfer_unkeyed.py 24 Sept 2026: {n} occurrences, margin {m} bits over {sec}; '
                           f'control, accepted proposals at band {b}: {ctl(b)} correct (control_f30.tsv, 10 draws)')
        kx = os.path.join(H, 'key_extension_f30.tsv')   # keep OVERRIDE rows written by test_f30r_top.py
        ext += [l.rstrip('\n') for l in open(kx) if l.split('\t')[3:4] and l.split('\t')[3].startswith('OVERRIDE')]
        open(kx, 'w').write('\n'.join(ext) + '\n')

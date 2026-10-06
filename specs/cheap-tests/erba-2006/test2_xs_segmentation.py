#!/usr/bin/env python3
"""erba-2006 spec test 2 (R12D-ERBA, 6 Oct 2026): is the xs-segmented word-length profile more Italian-shaped
than random segmentation? Pre-registered in PREREG-test2.md. Disk only. Usage: python3 test2_xs_segmentation.py
[--corpus tools/data/it21news --designs L] (R12D-ERBA3, 6 Oct 2026: era rerun on the modern corpus; default it19, both designs)"""
import glob, gzip, math, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..'))
SEP, FLOOR, NPERM, NPERM_C, NWIN = 'xs', 1e-4, 10000, 2000, 200
V = set('aeiouàèéìíòóùú')
STRONG = set('aeoàèéòó')

def target_streams():
    lines = [l.split() for l in open(os.path.join(HERE, 'transcription_bERB.txt')) if l.strip()]
    toks = [[t.rstrip('-').lower() for t in l] for l in lines]
    return [sum(toks[0:17], []), sum(toks[17:20], []), sum(toks[20:22], [])]

def segment(stream, sep):
    words, n = [], 0
    for t in stream:
        if t == sep: words.append(n); n = 0
        else: n += 1
    words.append(n)
    return words

def S(streams, sep, P):
    w = [x for s in streams for x in segment(s, sep)]
    return sum(math.log(P.get(x, FLOOR)) for x in w) / len(w)

def perm_p(streams, sep, P, n, rng):
    obs = S(streams, sep, P); ge = 0
    for _ in range(n):
        sh = []
        for s in streams:
            s = s[:]; rng.shuffle(s); sh.append(s)  # xs positions random; other-token order irrelevant to S
        if S(sh, sep, P) >= obs: ge += 1
    return obs, (1 + ge) / (n + 1)

def syl(w):
    c, i = 0, 0
    while i < len(w):
        if w[i] in V:
            j = i
            while j < len(w) and w[j] in V: j += 1
            run = w[i:j]; c += 1
            c += sum(1 for a, b in zip(run, run[1:]) if a in STRONG and b in STRONG)
            i = j
        else: i += 1
    return max(c, 1)

CORPUS = sys.argv[sys.argv.index('--corpus') + 1] if '--corpus' in sys.argv else 'tools/data/it19'
DESIGNS = sys.argv[sys.argv.index('--designs') + 1] if '--designs' in sys.argv else 'LY'

def corpus_words():
    words = []
    for f in sorted(glob.glob(os.path.join(ROOT, CORPUS, '*.txt.gz'))):
        txt = gzip.open(f, 'rt', encoding='utf-8', errors='ignore').read().lower()
        words += re.findall(r"[a-zàèéìíòóùú]+", txt)
    return words

def main():
    rng = random.Random(12)
    words = corpus_words()
    units = {'L': [len(w) for w in words], 'Y': [syl(w) for w in words]}
    T = target_streams(); lens = [len(s) for s in T]
    print(f'target streams {lens}, xs count {sum(s.count(SEP) for s in T)}; corpus words {len(words)}')
    out = {}
    print(f'corpus {CORPUS}')
    for d, ul in units.items():
        if d not in DESIGNS: continue
        c = Counter(ul); tot = sum(c.values()); P = {k: v / tot for k, v in c.items()}
        print(f'\n== design {d}: mean word len {sum(ul)/tot:.2f} units; P_ref top {sorted(P.items())[:8]}')
        obs, p = perm_p(T, SEP, P, NPERM, rng)
        uns = S([[t for t in s if t != SEP] for s in T], SEP, P)
        others = {tok: S(T, tok, P) for tok in sorted(set(sum(T, []))) }
        rank = sorted(others.values(), reverse=True).index(others[SEP]) + 1
        print(f'target S={obs:.3f} p={p:.4f} (10,000 perms); unsegmented S={uns:.3f}; xs rank {rank}/9 among split tokens')
        print('  S by split token: ' + ', '.join(f'{k} {v:.3f}' for k, v in sorted(others.items(), key=lambda x: -x[1])))
        print('  target xs word lengths: ' + str([segment(s, SEP) for s in T]))
        # matched control: real prose in units, separator = real space, three streams of target lengths
        hits, seps, cS = 0, [], []
        for _ in range(NWIN):
            streams = []
            for L in lens:
                i = rng.randrange(len(ul) - 200); s = []
                while len(s) < L:
                    s += ['u'] * ul[i] + [SEP]; i += 1
                streams.append(s[:L])
            o, pc = perm_p(streams, SEP, P, NPERM_C, rng)
            hits += pc < 0.05; seps.append(sum(s.count(SEP) for s in streams)); cS.append(o)
        seps.sort()
        power = hits / NWIN
        print(f'control power {hits}/{NWIN} = {power:.1%} (gate 80%); control S median {sorted(cS)[NWIN//2]:.3f}; '
              f'control separator count median {seps[NWIN//2]} (5-95%: {seps[int(.05*NWIN)]}-{seps[int(.95*NWIN)]}) vs target 14')
        if power < 0.8: v = 'NON-TEST (control below power gate)'
        else: v = 'PASS' if p < 0.05 else 'FAIL (control-backed negative)'
        print(f'VERDICT design {d}: {v}')
        out[d] = v
    return 0

if __name__ == '__main__':
    sys.exit(main())

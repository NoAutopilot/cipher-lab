#!/usr/bin/env python3
"""f.176 judge step (LANE R5 G2, 24 Sept 2026): decoded runs vs a matched control.

  python3 ciphers/fr3985-nevers-revol-1593/f176_judge.py --noise R [--seeds 5]

Target: f176_reading_atlas_tokens.tsv (tools/decode_key.py output), first alternative of each a|b value, unknown
tokens dropped, runs joined with spaces -> f176_runs_decoded.txt, judged with tools/judge_plaintext.py.
Control: the same number of runs, each of the same number of plaintext letters as the target's run, cut from held-out
16th-century French (tools/data/fr16, a window chosen by seed), enciphered with key.tsv (greedy: at each position a
random key value that is a prefix of what is left, then a random homophone), each sign replaced by a random key sign
with probability R (the observed pass disagreement rate), decoded back by the same first-alternative rule, judged.
Null: the target's own decoded tokens shuffled across the leaf (same run lengths), judged the same way.
Deviation from the brief: the control plaintext is fr16 letters, not the clear text of f.176, which is not transcribed
on disk. Nothing is fetched.
"""
import argparse, collections, gzip, glob, os, random, re, subprocess, sys, unicodedata
D = os.path.dirname(os.path.abspath(__file__)); R = os.path.abspath(os.path.join(D, '../..'))
SPEC = os.path.join(R, 'specs/fr3985-nevers-f176.json')

def fold(s):
    s = unicodedata.normalize('NFD', s.lower()); return ''.join(c for c in s if 'a' <= c <= 'z')

def load_key():
    k = collections.defaultdict(list)
    for l in open(os.path.join(D, 'key.tsv'), encoding='utf-8'):
        if l.startswith('#') or l.startswith('sign\t'): continue
        p = l.rstrip('\n').split('\t')
        if len(p) > 1 and p[1]: k[p[0]].append(p[1])
    return k

def first(v):
    v = v.split('|')[0]; return '' if ('?' in v or v in ('', 'NULL')) else fold(v)

def target_runs(shuffle_seed=None):
    runs = collections.OrderedDict()
    rows = [l.rstrip('\n').split('\t') for l in open(os.path.join(D, 'f176_reading_atlas_tokens.tsv'), encoding='utf-8')]
    h = rows[0]; il, iv = h.index('line'), h.index('value')
    for r in rows[1:]:
        if len(r) > iv: runs.setdefault(r[il], []).append(first(r[iv]))
    if shuffle_seed is not None:   # null: the leaf's own decoded tokens in random order, same run lengths
        allv = [v for vs in runs.values() for v in vs]; random.Random(shuffle_seed).shuffle(allv); it = iter(allv)
        runs = collections.OrderedDict((k, [next(it) for _ in vs]) for k, vs in runs.items())
    return [''.join(v) for v in runs.values()]

def judge(text, tag):
    p = os.path.join(D, 'f176_judge_%s.txt' % tag); open(p, 'w').write(text + '\n')
    o = subprocess.run([sys.executable, os.path.join(R, 'tools/judge_plaintext.py'), SPEC, '--file', p], capture_output=True, text=True)
    return o.returncode, o.stdout.strip()

def encipher(pt, key, rng):
    inv = collections.defaultdict(list)
    for s, vs in key.items():   # only signs whose decode (first value, first alternative) is that value
        v = first(vs[0])
        if v: inv[v].append(s)
    signs, i = [], 0
    while i < len(pt):
        opts = [v for v in inv if pt.startswith(v, i)]
        if not opts: i += 1; continue
        v = rng.choice(opts); signs.append(rng.choice(inv[v])); i += len(v)
    return signs

def main():
    a = argparse.ArgumentParser(); a.add_argument('--noise', type=float, required=True); a.add_argument('--seeds', type=int, default=5)
    a = a.parse_args(); key = load_key(); allsigns = sorted(key)
    runs = target_runs(); text = ' '.join(r for r in runs if r)
    rc, out = judge(text, 'target'); print('TARGET letters=%d runs=%d rc=%d\n%s\n' % (len(fold(text)), len(runs), rc, out))
    corpus = ''.join(fold(gzip.open(f, 'rt', errors='ignore').read()) for f in sorted(glob.glob(os.path.join(R, 'tools/data/fr16/*.gz'))))
    for seed in range(1, a.seeds + 1):
        rng = random.Random(seed); pos = rng.randrange(len(corpus) // 2, len(corpus) - 5000); outr = []
        for r in runs:
            pt = corpus[pos:pos + max(len(r), 1)]; pos += len(pt) + rng.randrange(200, 2000)
            sg = [rng.choice(allsigns) if rng.random() < a.noise else s for s in encipher(pt, key, rng)]
            outr.append(''.join(first(key[s][0]) if key.get(s) else '' for s in sg))
        rc, out = judge(' '.join(outr), 'control_s%d' % seed)
        print('CONTROL seed=%d noise=%.2f letters=%d rc=%d\n%s\n' % (seed, a.noise, len(fold(' '.join(outr))), rc, out))
    for seed in range(1, a.seeds + 1):
        rc, out = judge(' '.join(target_runs(seed)), 'null_s%d' % seed)
        print('NULL (target tokens shuffled) seed=%d rc=%d\n%s\n' % (seed, rc, out))
main()

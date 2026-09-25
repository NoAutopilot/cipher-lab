#!/usr/bin/env python3
"""Offline test for tools/homophonic_anneal.py: a matched control (German 1562 plaintext from
ciphers/august-van-saksen-1561-64/align_74.txt, N=282, K=20, w as uu) must be read at >= 90 percent."""
import os, re, subprocess, sys, tempfile, json
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
D = os.path.join(R, 'ciphers', 'august-van-saksen-1561-64')
words = []
for l in open(os.path.join(D, 'align_74.txt'), encoding='utf-8'):
    if l.startswith('#') or ':' not in l:
        continue
    for w in l.split(':', 1)[1].split(';;'):
        if '|' in w:
            words.append(w.split('|')[1].replace(' ', ''))
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, 'ctl.txt'); open(p, 'w').write(' '.join(words))
    o = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', p, '--signs', '20',
                    '--length', '282', '--corpus', os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'),
                    '--corpus', os.path.join(D, 'plaintext_98.txt'), '--restarts', '3', '--iters', '200000',
                    '--w-as-uu', '--out', o], check=True, stdout=subprocess.DEVNULL)
    share = json.load(open(o))['share']
    assert share >= 0.9, share
    print('ok', share)

# allowed= restricts a sign's letters (vowel-indicator marks): the restricted sign never leaves its set
sys.path.insert(0, os.path.join(R, 'tools'))
import random, homophonic_anneal as ha
m = ha.Model([open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read()[:20000]])
_, k = ha.anneal(list('abcabcxyzxyz'), m, 2000, random.Random(1), 1.0, allowed={'x': 'aeiou', 'y': 'e'})
assert k['x'] in 'aeiou' and k['y'] == 'e', k
print('ok allowed')

# --noise (anneal_noisy, LANE R6 CM2, 25 Sept 2026): the first block's control (align_74 words, K=20, N=282, w as uu,
# corpus composed_enhg + plaintext_98) with 10 percent of the signs replaced by random signs: the error-tolerant solve
# returns a free set within its cap, letters from ALPHA, and reads the corrected text at >= 75 percent (85.8 percent on
# 25 Sept 2026, plain solver 86.2); the plain solve's reading of the same noisy input is printed beside it. A weak model
# (composed_enhg alone, 8.5 KB) reads the same design at 11-19 percent with either solver, so the model is what this
# block tests the solver under, not the other way round.
import math
ha.W_AS_UU = True
m2 = ha.Model([open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read(),
               open(os.path.join(D, 'plaintext_98.txt'), encoding='utf-8').read()])
seq, p, truth = ha.make_control(' '.join(words), 20, 282, m2, 1)
nr = random.Random(3); types = sorted(set(seq))
seqn = [nr.choice(types) if nr.random() < 0.1 else s for s in seq]
acc = lambda d: sum(a == b for a, b in zip(d, p)) / len(p)
sc, key, free = ha.solve(seqn, m2, 3, 100000, 1, 1.0, noise=0.1)[0]
assert len(free) <= math.ceil(1.5 * 0.1 * len(seqn)), len(free)
assert all(l in ha.ALPHA for l in free.values()) and all(0 <= i < len(seqn) for i in free)
dec = ''.join(free.get(i, key[x]) for i, x in enumerate(seqn))
plain_key = ha.solve(seqn, m2, 3, 100000, 1, 1.0)[0][1]
plain_dec = ''.join(plain_key[x] for x in seqn)
print(f'ok noise: corrected {acc(dec):.1%} (key-only {acc("".join(key[x] for x in seqn)):.1%}, free {len(free)}), plain solver {acc(plain_dec):.1%}')
assert acc(dec) >= 0.75, acc(dec)

# --robust (RobustModel): same interface as Model; logp is bounded below by log(q/V) and never above the plain logp
rm = ha.RobustModel(m2, 0.1)
assert rm.order == m2.order and rm.freq is m2.freq
for g in ('der', 'qxz', 'ung'):
    assert rm.logp(g) >= math.log(0.1 / m2.V) - 1e-9 and rm.logp(g) >= m2.logp(g) + math.log(0.9) - 1e-9, g
print('ok robust')

# --backoff (BackoffModel, LANE R7 CM3, 25 Sept 2026): a proper distribution at every order (the continuations of a
# seen, an unseen and a short context sum to one), the same interface as Model, and it discriminates: the first block's
# German plaintext scores above three shuffles of itself by a wide margin. The anneal itself does NOT converge under it
# at the default schedule (the true key scores far above what it finds: 14 percent on this control, 7-22 percent on the
# Salviati measured-noise control, NOTES.md "CM3"), so the solve is printed as information, not asserted; a schedule that
# works under backoff is owed before --backoff is used for a gate.
bm = ha.BackoffModel([open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read(),
                      open(os.path.join(D, 'plaintext_98.txt'), encoding='utf-8').read()], 4)
assert bm.order == 4 and bm.V == m2.V and set(bm.freq) == set(m2.freq)
for ctx in ('und', 'qxz', 'e', 'ge'):
    tot = sum(bm.prob(ctx + a) for a in ha.ALPHA)
    assert abs(tot - 1.0) < 1e-9, (ctx, tot)
seq4, p4, _ = ha.make_control(' '.join(words), 20, 282, bm, 1)
true4 = ha.score(bm, p4, 1.0)
for i in range(3):
    l = list(p4); random.Random(i).shuffle(l)
    assert ha.score(bm, ''.join(l), 1.0) < true4 - 100, (i, true4)
sc4, key4 = ha.solve(seq4, bm, 2, 100000, 1, 1.0)[0]
acc4 = sum(a == b for a, b in zip(''.join(key4[x] for x in seq4), p4)) / len(p4)
print(f'ok backoff (model): order-4 backoff anneal reads {acc4:.1%}, found {sc4:.1f} vs true {true4:.1f} (search, not asserted)')

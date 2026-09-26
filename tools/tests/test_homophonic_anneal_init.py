#!/usr/bin/env python3
"""Offline test for tools/homophonic_anneal.py's --init (LANE AX2, 26 Sept 2026): a key-seeded anneal starts
from a given sign->letter map instead of a random one; default behaviour (no --init/init=None) is unchanged."""
import os, subprocess, sys, tempfile, json, random
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha

CORPUS = os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt')
m = ha.Model([open(CORPUS, encoding='utf-8').read()[:20000]])

# load_init_key: reads a key.tsv-style file, folds values, keeps only single a-z letters (skips NULL,
# multi-letter names/words, and a header using 'sign' instead of 'code').
with tempfile.TemporaryDirectory() as t:
    p = os.path.join(t, 'key.tsv')
    open(p, 'w', encoding='utf-8').write(
        'code\tvalue\tgrade\n'
        '1\tn\tC\n'
        '2\tNULL\tC\n'
        '3\thollande\tH\n'
        '7\tj\tC\n'  # folds to i
        '9\tV\tM\n'  # folds to u (case-insensitive via fold())
    )
    init = ha.load_init_key(p)
    assert init == {'1': 'n', '7': 'i', '9': 'u'}, init
print('ok load_init_key')

# iters=0: no move is ever proposed, so the returned key is exactly the starting point -- the cleanest possible
# check that --init actually seeds the key (rather than being silently ignored).
seq = list('123123123')
truth = {'1': 'a', '2': 'b', '3': 'c'}
_, key0 = ha.anneal(seq, m, 0, random.Random(1), 1.0, init=truth)
assert key0 == truth, key0
print('ok anneal(iters=0, init=truth) returns exactly the init map')

# a sign in --fix overrides --init for that sign, per the tool's own precedence (fixed > init > allowed > random)
_, key1 = ha.anneal(seq, m, 0, random.Random(1), 1.0, fixed={'1': 'z'}, init=truth)
assert key1['1'] == 'z' and key1['2'] == 'b' and key1['3'] == 'c', key1
print('ok fix overrides init')

# a sign missing from init, or whose init value is not in ALPHA, falls back to the normal random start (no crash,
# no KeyError, always a valid letter) rather than raising or leaving the sign unset.
partial = {'1': 'a', '2': 'NOT-A-LETTER'}
_, key2 = ha.anneal(seq, m, 0, random.Random(1), 1.0, init=partial)
assert key2['1'] == 'a' and key2['2'] in ha.ALPHA and key2['3'] in ha.ALPHA, key2
print('ok partial/invalid init falls back to a valid random letter for the uncovered signs, no crash')

# default behaviour with no --init at all (init=None, the CLI default) is byte-identical to before this change:
# same seeded RNG draws the same key as a call with an explicit empty dict.
_, key_none = ha.anneal(seq, m, 50, random.Random(2), 1.0)
_, key_empty = ha.anneal(seq, m, 50, random.Random(2), 1.0, init={})
assert key_none == key_empty, (key_none, key_empty)
print('ok init=None matches init={} (default behaviour unchanged)')

# anneal_noisy accepts init the same way (iters=0 skips both the key move and the position-move branch since
# pos_start defaults to 0.5 of iters, i.e. never reached at iters=0)
_, key3, free3 = ha.anneal_noisy(seq, m, 0, random.Random(1), 1.0, noise=0.1, init=truth)
assert key3 == truth and free3 == {}, (key3, free3)
print('ok anneal_noisy(iters=0, init=truth) returns exactly the init map, no free positions')

# end-to-end CLI: --init on a real cipher file, key file in key.tsv's own column convention. A short synthetic
# cipher enciphered under a known key, solved --init from a perturbed copy of that same key (one sign flipped) --
# with only one sign wrong and iters=0, the returned key differs from the true key at exactly that one sign.
words = []
D = os.path.join(R, 'ciphers', 'august-van-saksen-1561-64')
for l in open(os.path.join(D, 'align_74.txt'), encoding='utf-8'):
    if l.startswith('#') or ':' not in l:
        continue
    for w in l.split(':', 1)[1].split(';;'):
        if '|' in w:
            words.append(w.split('|')[1].replace(' ', ''))
m2 = ha.Model([open(CORPUS, encoding='utf-8').read(),
               open(os.path.join(D, 'plaintext_98.txt'), encoding='utf-8').read()])
seq_c, p_c, truth_c = ha.make_control(' '.join(words), 20, 282, m2, 1)
with tempfile.TemporaryDirectory() as t:
    cipher_path = os.path.join(t, 'cipher.tsv')
    with open(cipher_path, 'w', encoding='utf-8') as f:
        f.write('line\tposition\tsign\n')
        for i, s in enumerate(seq_c):
            f.write(f'L1\t{i}\t{s}\n')
    perturbed = dict(truth_c)
    one_sign = next(iter(perturbed))
    wrong = 'z' if perturbed[one_sign] != 'z' else 'y'
    perturbed[one_sign] = wrong
    key_path = os.path.join(t, 'init.tsv')
    with open(key_path, 'w', encoding='utf-8') as f:
        f.write('code\tvalue\n')
        for s, l in perturbed.items():
            f.write(f'{s}\t{l}\n')
    out_path = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), cipher_path,
                    '--corpus', CORPUS, '--corpus', os.path.join(D, 'plaintext_98.txt'),
                    '--restarts', '1', '--iters', '0', '--skip', 'DOT,COL', '--init', key_path,
                    '--out', out_path], check=True, stdout=subprocess.DEVNULL)
    result = json.load(open(out_path))
    got_key = result['key']
    diffs = {s for s in truth_c if got_key.get(s) != truth_c[s]}
    assert diffs == {one_sign}, diffs
print('ok CLI --init: iters=0 target-mode run reproduces the perturbed init exactly (one sign wrong, as seeded)')

#!/usr/bin/env python3
"""Offline test for tools/homophonic_anneal.py --profile (exact-profile control, campaign espagnol142-mercy-1648
H1, 27 Sept 2026): the control's sign occurrence multiset must equal the profile cipher's exactly, its plaintext
must be a window of the --control text, and the truth key must decode the sequence back to that window.
Must catch: a control whose counts are only frequency-allotted (make_control) rather than the profile's own.
Must not block: a profile with several count-1 signs and a text window with rare letters (the partition search
handles those by backtracking, not by giving up)."""
import os, sys, json, subprocess, tempfile, random
from collections import Counter
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha

# unit: partition_exact fills every letter exactly, or reports None when impossible
assert ha.partition_exact([5, 3, 2, 1, 1], {'a': 6, 'b': 5, 'c': 1}) is not None
assert ha.partition_exact([5, 5], {'a': 6, 'b': 4}) is None
assign = ha.partition_exact([57, 42, 41, 39, 38, 27, 24, 23, 22, 20, 20, 17, 14, 14, 13, 11, 11, 10, 9, 8, 8, 8,
                             6, 5, 5, 5, 4, 4, 3, 2, 2, 2, 2, 1, 1, 1, 1, 1],
                            {'e': 70, 'a': 65, 'o': 50, 's': 40, 'n': 38, 'r': 35, 'i': 33, 'l': 30, 'd': 28,
                             'u': 25, 't': 22, 'c': 20, 'm': 15, 'p': 13, 'q': 10, 'b': 8, 'g': 6, 'y': 5,
                             'h': 3, 'f': 2, 'z': 2, 'x': 1})
assert assign is not None and len(assign) == 38
print('ok partition')

# end to end: a profile of 20 signs with seven count-1 signs, a 60-letter window of a Spanish sentence repeated
text = ("en un lugar de la mancha de cuyo nombre no quiero acordarme no ha mucho tiempo que vivia un hidalgo "
        "de los de lanza en astillero adarga antigua rocin flaco y galgo corredor ") * 3
with tempfile.TemporaryDirectory() as t:
    prof = os.path.join(t, 'prof.tsv')
    rng = random.Random(3)
    counts = [10, 8, 6, 5, 4, 4, 3, 3, 2, 2, 2, 2, 2, 1, 1, 1, 1, 1, 1, 1]  # K=20, N=60, seven count-1 signs
    with open(prof, 'w') as f:
        f.write('line\tposition\tsign\n')
        pos = 0
        for i, c in enumerate(counts):
            for _ in range(c):
                pos += 1
                f.write(f'l1\t{pos}\t{i}\n')
    ctl = os.path.join(t, 'ctl.txt'); open(ctl, 'w').write(text)
    o = os.path.join(t, 'o.json')
    subprocess.run([sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', ctl, '--profile', prof,
                    '--skip', 'NONE', '--corpus', ctl, '--restarts', '1', '--iters', '300', '--seed', '2', '--out', o],
                   check=True, stdout=subprocess.DEVNULL)
    out = json.load(open(o))
    assert out['N'] == sum(counts) and out['K'] == len(counts), (out['N'], out['K'])
    assert out['sign_counts'] == counts, out['sign_counts']
    assert out['profile_counts'] == counts
    folded = ha.fold(text)
    assert out['plain'] == folded[out['window_start']:out['window_start'] + sum(counts)]
    # the frequency-allotted control of the same N/K does not, in general, reproduce the profile (what --profile adds)
    seq, p, truth = ha.make_control(text, len(counts), sum(counts), None, 2)
    assert sorted(Counter(seq).values(), reverse=True) != counts
    print('ok profile', out['sign_counts'])

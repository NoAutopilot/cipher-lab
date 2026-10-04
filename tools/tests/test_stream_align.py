#!/usr/bin/env python3
"""Offline test for tools/stream_align.py (RUN2-NXALN, 4 Oct 2026): a synthetic homophonic + nomenclator cipher with
nulls, cipher-side insertions and a clear passage missing from the cipher is aligned and its key recovered; the held-out
decode beats a shuffled-key decode by a wide margin, and the interlinear_align.py `stream` subcommand writes a key file."""
import os, random, subprocess, sys, tempfile
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..'))
import stream_align as sa

WORDS = ('le roy ma commande de vous escrire que les affaires de son royaume sont en bon estat et que la paix '
         'sera bientost faicte avec ses voysins mais que les ministres du roy d espagne ne cessent de faire courir '
         'des bruits contraires a la verite par toute la chrestiente').split()


def synth(seed=3, n_words=900):
    rng = random.Random(seed)
    text = ' '.join(rng.choice(WORDS) for _ in range(n_words))
    sym_of, sid = {}, 0
    for c in sorted(set(text.replace(' ', ''))):
        k = 3 if c in 'esa' else 1
        sym_of[c] = list(range(sid, sid + k)); sid += k
    nom = {'roy': sid, 'que': sid + 1}; sid += 2
    null = sid; sid += 1
    words = text.split()
    cipher, truth = [], {}
    for n, w in enumerate(words):
        if w in nom:
            cipher.append(nom[w])
        else:
            for c in w:
                s = rng.choice(sym_of[c]); cipher.append(s); truth[s] = c
        if rng.random() < 0.04:
            cipher.append(null)
    clear = ' '.join(words[:500] + words[520:])  # the copy drops 20 words
    return np.array(cipher), clear, truth, sid


def test_recovers_key():
    cipher, clear, truth, nsym = synth()
    let = sa.letters(clear)
    cut = int(len(cipher) * 0.6)
    counts, path = sa.learn(cipher[:cut], let, nsym)
    key = sa.decode(counts)
    right = sum(1 for s, c in truth.items() if key[s] == ord(c) - 97)
    assert right >= 0.8 * len(truth), (right, len(truth))
    jend = path[-1][1] + 1
    acc = sa.nw_score(key[cipher[cut:]], let[jend:])
    k2 = key.copy(); rng = np.random.default_rng(0); v = k2[k2 >= 0]; rng.shuffle(v); k2[k2 >= 0] = v
    null = sa.nw_score(k2[cipher[cut:]], let[jend:])
    assert acc > 0.75 and acc > null + 0.25, (acc, null)


def test_cli():
    cipher, clear, truth, nsym = synth(seed=5, n_words=400)
    with tempfile.TemporaryDirectory() as d:
        open(os.path.join(d, 's.txt'), 'w').write('\n'.join(f's{x}' for x in cipher))
        open(os.path.join(d, 't.txt'), 'w').write(clear)
        out = os.path.join(d, 'k.tsv')
        subprocess.run([sys.executable, os.path.join(HERE, '..', 'interlinear_align.py'), 'stream',
                        os.path.join(d, 's.txt'), os.path.join(d, 't.txt'), out], check=True, capture_output=True)
        rows = open(out).read().splitlines()
        assert rows[0].startswith('symbol\tvalue') and len(rows) > 10


if __name__ == '__main__':
    test_recovers_key(); test_cli(); print('ok')

#!/usr/bin/env python3
"""Plumbing check for key.tsv + decode.pending.json (SALAZ-KEY, 9 Oct 2026): NOT a test of Tomokiyo's key on any letter.

  python3 scripts/roundtrip_check.py OUTDIR [--seeds 5]

Enciphers Tomokiyo's own printed 1522 plaintext (R9623 last paragraph, AlonsoSanchez.htm, his segmentation: whole words
are nomenclature codes, hyphenated pieces are letters) with key.tsv, choosing for each letter a shape keyed to it alone,
writes the ciphertext as a decode_key.py tsv, decodes it with tools/decode_key.py --config decode.pending.json (job 1),
and scores value agreement. Control: the same ciphertext decoded with key.tsv's values shuffled among its codes (rule 3).
Shows the pipeline reads a text in this key's own design on arrival; says nothing about whether the key fits 1524-28.
"""
import os, random, subprocess, sys, json
HERE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROOT = os.path.dirname(os.path.dirname(HERE))
PLAIN = ("parecia me a c-o-r-d-a-r a vuestra magestad que al p-r-i-n-c-i-p-i-o de se-t-i-en-b-r-e lo-s de esta "
         "r-e-publica por la capitula-c-i-o-n passa-da l-e ha-n de-da-r xx mi-l ducato-s allende de xviii mi-l que")


def load_key(path):
    rows = [l.rstrip('\n').split('\t') for l in open(path, encoding='utf-8') if not l.startswith('#')]
    return rows[0], rows[1:]


def main():
    out = sys.argv[1]; seeds = int(sys.argv[sys.argv.index('--seeds') + 1]) if '--seeds' in sys.argv else 5
    os.makedirs(out, exist_ok=True)
    head, rows = load_key(os.path.join(HERE, 'key.tsv'))
    word2code, letter2shape = {}, {}
    for code, val, *_ in rows:
        if len(code) == 3 and code.islower() and code.isalpha():
            word2code.setdefault(val.rstrip('?'), code)
        elif '|' not in val and val != 'NULL':
            letter2shape.setdefault(val, code)
    for code, val, *_ in rows:  # two-letter codes (xa, ta, ...) after three-letter ones
        if len(code) == 2 and code.islower() and val.rstrip('?') not in word2code:
            word2code[val.rstrip('?')] = code
    toks, truth, skipped = [], [], 0
    for w in PLAIN.split():
        for piece in w.split('-'):
            if piece in word2code:
                toks.append(word2code[piece]); truth.append(piece)
            else:
                for ch in piece:
                    if ch in letter2shape:
                        toks.append(letter2shape[ch]); truth.append(ch)
                    else:
                        skipped += 1
    ct = os.path.join(out, 'ciphertext_item4.tsv')
    with open(ct, 'w') as f:
        f.write('line\tpos\tsign\n')
        for i, t in enumerate(toks):
            f.write('1\t%d\t%s\n' % (i + 1, t))
    cfg = json.load(open(os.path.join(HERE, 'decode.pending.json')))
    job = dict(cfg['jobs'][0])

    def score(keypath, tag):
        j = dict(job, key=keypath, reading=tag + '.txt', tokens=tag + '_tokens.tsv')
        cp = os.path.join(out, tag + '.json'); json.dump({'jobs': [j]}, open(cp, 'w'))
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools/decode_key.py'), out, '--config', cp],
                       check=True, capture_output=True)
        got = [l.rstrip('\n').split('\t') for l in open(os.path.join(out, tag + '_tokens.tsv')) if not l.startswith('#')][1:]
        vals = [g[3] for g in got]
        return sum(a == b for a, b in zip(vals, truth)) / len(truth)

    real = score(os.path.join(HERE, 'key.tsv'), 'real')
    ctl = []
    for s in range(seeds):
        r = random.Random(s); vals = [x[1] for x in rows]; r.shuffle(vals)
        kp = os.path.join(out, 'key_shuf%d.tsv' % s)
        with open(kp, 'w') as f:
            f.write('\t'.join(head) + '\n')
            for x, v in zip(rows, vals):
                f.write('\t'.join([x[0], v] + x[2:]) + '\n')
        ctl.append(score(kp, 'shuf%d' % s))
    print(json.dumps({'tokens': len(truth), 'letters_without_unambiguous_shape_skipped': skipped,
                      'real_key_agreement': round(real, 3), 'shuffled_key_agreement': [round(c, 3) for c in ctl]}))


if __name__ == '__main__':
    main()

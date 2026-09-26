#!/usr/bin/env python3
"""AX-NAMES2: decode one ciphertext with key.tsv and with key_full.tsv (same decode.json job, key swapped, output to a
temp dir) and compare token by token. Used for the known-answer regression check (step 2, ciphertext_sib.tsv) and the
5810/5811 sanity check (step 6).

  python3 axnames/compare_full.py CONFIG.json CIPHERTEXT.tsv [--list]
Prints: tokens, C-graded under key.tsv, regressions (a key.tsv C token whose value or grade changes), changed
tokens, U before/after. Exit 2 if any regression.
"""
import csv, json, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
TGT = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(TGT))


def run(cfg, ct, key, tmp):
    job = next(j for j in json.load(open(os.path.join(TGT, cfg)))['jobs'] if j['ciphertext'] == ct)
    job = dict(job, key=key, reading=os.path.join(tmp, key + '.txt'), tokens=os.path.join(tmp, key + '_tokens.tsv'))
    c = os.path.join(tmp, key + '.json')
    json.dump({'target': 'ciphers/' + os.path.basename(TGT), 'jobs': [job]}, open(c, 'w'))
    subprocess.run([sys.executable, os.path.join(ROOT, 'tools/decode_key.py'), TGT, '--config', c], check=True,
                   stdout=subprocess.DEVNULL)
    return list(csv.reader(open(job['tokens']), delimiter='\t'))[1:]


def main():
    cfg, ct = sys.argv[1], sys.argv[2]
    with tempfile.TemporaryDirectory() as tmp:
        o, f = run(cfg, ct, 'key.tsv', tmp), run(cfg, ct, 'key_full.tsv', tmp)
    assert len(o) == len(f)
    reg = [(a, b) for a, b in zip(o, f) if a[-1] == 'C' and (a[-2], a[-1]) != (b[-2], b[-1])]
    ch = [(a, b) for a, b in zip(o, f) if a != b]
    u0, u1 = sum(a[-1] == 'U' for a in o), sum(b[-1] == 'U' for b in f)
    print(f'{ct}: tokens {len(o)}, C under key.tsv {sum(a[-1] == "C" for a in o)}, regressions {len(reg)}, '
          f'changed {len(ch)}, U {u0} -> {u1}')
    if '--list' in sys.argv:
        for a, b in ch:
            print('\t'.join(a[:3]) + f'\t{a[-2]} {a[-1]} -> {b[-2]} {b[-1]}')
    sys.exit(2 if reg else 0)


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Inputs for the pooled 1653-band control rerun (F5160-POOL, LANE DEFAULT-account-4-20261009-1340, 9 Oct 2026).

  python3 pool_inputs.py [--check]

Extends solve_inputs.py (24 Sept 2026) from f1+f9 (752 tokens) to all four 1653 pieces:
  real_c11.txt, real_c32.txt  ciphertext_c11/c32.tsv (text-level reconciled, H+M) in nomenclator_anneal.py format.
  real_pool.txt              f1, f9, c11, c32 concatenated: the run pattern for the pooled control (synth --pattern).
  control_pool_plain.txt     control_plain.txt (unchanged prefix) + the f.68r clear text (dechiffre_f68.txt, this
                             volume, same office) + Marguerite de Valois letter XIX (25 April 1581, fr16
                             lettresindites00marg OCR lines 1249-1256), to reach the pooled length.
The model is rebuilt by solve_inputs.py's own routine with every paragraph that contains a control sentence dropped:
  FR_MODEL_DIR=<dir> python3 pool_inputs.py --model
--check exits 1 if a committed input file is stale.
"""
import gzip, os, re, sys
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(H, '..', '..', 'tools')
sys.path.insert(0, T); sys.path.insert(0, H)
import italian_ngram as ing
import solve_inputs as si

def f68():
    out = []
    for l in open(os.path.join(H, 'dechiffre_f68.txt'), encoding='utf-8'):
        if l.startswith('#'):
            continue
        l = re.sub(r'\[del:[^\]]*\]', '', l)
        l = re.sub(r'\[ins: ([^\]]*)\]', r'\1', l).replace('[?]', '')
        out.append(l.strip())
    return ' '.join(out)

def marg19():
    m = gzip.open(os.path.join(T, 'data', 'fr16', 'lettresindites00marg_djvu.txt.gz'), 'rt', encoding='utf-8').read().splitlines()
    c = ' '.join(m[1248:1256]).replace('- ', '').replace('(1)', '').replace('(2)', '')
    return c

def want():
    w = {'real_c11.txt': si.real('ciphertext_c11.tsv'), 'real_c32.txt': si.real('ciphertext_c32.tsv')}
    pat = ''
    for k in ('real_f1.txt', 'real_f9.txt'):
        pat += ''.join(l + '\n' for l in open(os.path.join(H, k), encoding='utf-8').read().splitlines() if not l.startswith('#'))
    for k in ('real_c11.txt', 'real_c32.txt'):
        pat += ''.join(l + '\n' for l in w[k].splitlines() if not l.startswith('#'))
    w['real_pool.txt'] = pat
    base = open(os.path.join(H, 'control_plain.txt'), encoding='utf-8').read().strip()
    w['control_pool_plain.txt'] = '#' + (base.strip('#') + '#' + ing.norm(f68() + ' ' + marg19()).strip('#')).strip('#') + '#\n'
    return w

def main():
    w = want()
    if '--check' in sys.argv:
        stale = 0
        for k, v in w.items():
            p = os.path.join(H, k)
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != v:
                print('stale', k); stale = 1
        sys.exit(stale)
    for k, v in w.items():
        open(os.path.join(H, k), 'w', encoding='utf-8').write(v)
    if '--model' in sys.argv:
        import glob, subprocess
        out = os.environ.get('FR_MODEL_DIR', os.path.join(H, '.model'))
        os.makedirs(out, exist_ok=True)
        ctl = w['control_pool_plain.txt'].replace('#', '')
        probes = [ctl[i:i + 40] for i in range(0, len(ctl) - 40, 40)]
        kept = []
        for fn in sorted(glob.glob(os.path.join(T, 'data', 'fr16', '*_djvu.txt*'))):
            op = gzip.open if fn.endswith('.gz') else open
            txt = re.sub(r'-\s*\n\s*', '', op(fn, 'rt', encoding='utf-8', errors='replace').read())
            for par in ing.paragraphs(txt):
                z = ing.norm(par).strip('#')
                if len(z) < 60 or any(p in z.replace('#', '') for p in probes):
                    continue
                kept.append(z)
        open(os.path.join(out, 'fr_corpus.txt'), 'w').write('\n'.join(kept) + '\n')
        subprocess.run([sys.executable, os.path.join(T, 'italian_ngram.py'), 'build', os.path.join(out, 'fr_corpus.txt'),
                        '--out', os.path.join(out, 'fr_model.npz')], check=True)

if __name__ == '__main__':
    main()

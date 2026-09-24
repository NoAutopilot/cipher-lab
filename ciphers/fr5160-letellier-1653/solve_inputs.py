#!/usr/bin/env python3
"""Inputs for the 1653-band constrained solve (LANE G2 worker G, 24 Sept 2026).

  python3 solve_inputs.py [--check]

Writes, from ciphertext_f1.tsv + ciphertext_f9.tsv (reconciled, H+M) and repo plaintext:
  real_f1.txt, real_f9.txt   Bourdeau-format transcriptions for tools/nomenclator_anneal.py: one manuscript line
                             per line, {clear} runs in braces, struck-through ~121 dropped.
  real_f1f9.txt              both, concatenated: the run pattern for the synthetic control.
  control_plain.txt          the control plaintext: the f.87 decipherment (Brienne, 21 Nov 1659, this volume) then
                             the clair1067 1646 reading (Brienne), then a held-out Marguerite de Valois letter of
                             12 March 1581 (from the fr16 corpus, to reach the target's length), normalised with '#' word boundaries.
  fr_corpus.txt (scratch)    period-French corpus from tools/data/fr16 (Catherine de Medici, Marguerite letters),
                             paragraphs containing any control sentence dropped; built into fr_model.npz with
                             tools/italian_ngram.py build (same 21-letter alphabet: j->i, y->i, v->u, k->ch).
--check exits 1 if a committed input file is stale.
"""
import csv, glob, gzip, os, re, sys, subprocess
H = os.path.dirname(os.path.abspath(__file__))
T = os.path.join(H, '..', '..', 'tools')
sys.path.insert(0, T)
import italian_ngram as ing

def real(fn):
    lines, cur = [], None
    out = []
    for r in csv.DictReader(open(os.path.join(H, fn), encoding='utf-8'), delimiter='\t'):
        if r['line'] != cur:
            if out: lines.append(' '.join(out))
            out, cur = [], r['line']
        t = r['token']
        if t.startswith('[PLAIN:'):
            out.append('{' + t[7:-1] + '}')
        elif t.startswith('~'):
            continue
        else:
            out.append(t)
    if out: lines.append(' '.join(out))
    return '# ' + fn + ' (reconciled, H+M), one manuscript line per line\n' + '\n'.join(lines) + '\n'

def control_plain():
    a = open(os.path.join(H, 'dechiffre_f87.txt'), encoding='utf-8').read().split('\n', 2)[2]
    b = []
    for l in open(os.path.join(H, '..', 'clair1067-brienne-poland-1646', 'reading_1646.txt'), encoding='utf-8'):
        if ' | ' in l:
            b.append(l.split(' | ', 1)[1].replace('[', '').replace(']', '').strip())
    # third piece, only to reach 752 tokens: Marguerite de Valois to the King, Cadillac, 12 March 1581 (letter XVIII of
    # tools/data/fr16/lettresindites00marg, OCR lines 1203-1211 + 1235-1239, footnote left out); held out of the model
    import gzip as _g
    m = _g.open(os.path.join(T, 'data', 'fr16', 'lettresindites00marg_djvu.txt.gz'), 'rt', encoding='utf-8').read().splitlines()
    c = ' '.join(m[1202:1211] + m[1234:1239]).replace('- ', '').replace('cTaultant', "d'aultant").replace('>nndir', 'mondit').replace('ponr', 'pour')
    z = ing.norm(a + ' ' + ' '.join(b) + ' ' + c)
    return '#' + z.strip('#') + '#\n'

def main():
    want = {'real_f1.txt': real('ciphertext_f1.tsv'), 'real_f9.txt': real('ciphertext_f9.tsv'),
            'control_plain.txt': control_plain()}
    # run pattern for the control (synth --pattern): both letters, comment lines dropped
    want['real_f1f9.txt'] = ''.join(l + '\n' for k in ('real_f1.txt', 'real_f9.txt')
                                    for l in want[k].splitlines() if not l.startswith('#'))
    stale = 0
    for k, v in want.items():
        p = os.path.join(H, k)
        if '--check' in sys.argv:
            if not os.path.exists(p) or open(p, encoding='utf-8').read() != v:
                print('stale', k); stale = 1
        else:
            open(p, 'w', encoding='utf-8').write(v)
    if '--check' in sys.argv:
        sys.exit(stale)
    # model (not committed: 20 MB; rebuilt here)
    out = os.environ.get('FR_MODEL_DIR', os.path.join(H, '.model'))
    os.makedirs(out, exist_ok=True)
    ctl = want['control_plain.txt'].replace('#', '')
    probes = [ctl[i:i + 40] for i in range(0, len(ctl) - 40, 40)]
    kept = []
    for fn in sorted(glob.glob(os.path.join(T, 'data', 'fr16', '*_djvu.txt*'))):
        op = gzip.open if fn.endswith('.gz') else open
        txt = op(fn, 'rt', encoding='utf-8', errors='replace').read()
        txt = re.sub(r'-\s*\n\s*', '', txt)
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

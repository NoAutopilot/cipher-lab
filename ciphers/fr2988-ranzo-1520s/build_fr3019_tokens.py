#!/usr/bin/env python3
"""Build fr3019_no27_tokens.tsv (fr.3019 no.27, ff.73r-74r) from the blind passes and the reconciler's settlements.

  python3 build_fr3019_tokens.py [--check]

For each page, tools/reconcile_passes.py aligns the passes in passes/ (two per page, three on f.73v); where they split,
the page's PREFERRED pass is taken (the pass read from single-line crops whose superscripts are complete:
B on f.73r, C on f.73v (where an alignment gap leaves C empty the column is dropped); A on f.74r, where both passes are band crops and A matched the overview more often),
then settle.tsv (line, pos, token, note: this worker's reading of the native crop at that position, A1B-RANZO-2WIT,
3 Oct 2026) overrides; a settled token with spaces adds the tokens after the first (pos N+1, N+2), and '-' drops one. pos in settle.tsv is the column of the reconciled draft. conf: H where all passes agree with H
or M confidence and no override, M otherwise, L where a pass marked it L and nothing settled it.
Writes fr3019_no27_tokens.tsv (line, pos, token, conf, why). --check exits 1 if the committed file is stale.
"""
import csv, os, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..'))
PAGES = [('f73r', ['passA-f73r.tsv', 'passB-f73r.tsv'], 'B'),
         ('f73v', ['passA-f73v.tsv', 'passB-f73v.tsv', 'passC-f73v.tsv'], 'C'),
         ('f74r', ['passA-f74r.tsv', 'passB-f74r.tsv'], 'A')]


def rows_for(prefix, files, pref):
    with tempfile.TemporaryDirectory() as td:
        paths = [os.path.join(HERE, 'passes', f) for f in files if os.path.exists(os.path.join(HERE, 'passes', f))]
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools', 'reconcile_passes.py'), *paths, '--out-dir', td],
                       check=True, capture_output=True)
        draft = list(csv.DictReader(open(os.path.join(td, 'ciphertext_draft.tsv')), delimiter='\t'))
    out = []
    for r in draft:
        tok, why, conf = r['sign'], r['why'], r['confidence']
        if why in ('differ', 'gap'):
            alts = dict(a.split(':', 1) for a in r['alt'].replace(';', '/').split('/') if ':' in a)
            if pref in alts:
                tok = alts[pref]
            why, conf = f'{why}, pass {pref} taken', 'M'
        elif conf == 'H' or why == 'agree':
            conf = 'H'
        out.append(dict(line=r['line'], pos=r['position'], token=tok, conf=conf, why=why))
    return out


def main():
    settle = {(r['line'], r['pos']): r for r in csv.DictReader(open(os.path.join(HERE, 'settle.tsv')), delimiter='\t')}
    rows = []
    for prefix, files, pref in PAGES:
        for r in rows_for(prefix, files, pref):
            s = settle.get((r['line'], r['pos']))
            if s:
                r.update(conf='M' if s['token'] not in ('X',) else 'L', why='settled: ' + s['note'])
                for k, t in enumerate(s['token'].split()):  # a settlement may add a token a pass missed
                    if t != '-':
                        rows.append(dict(r, token=t, pos=r['pos'] + ('' if k == 0 else f'+{k}')))
                continue
            if r['token'] != '-':
                rows.append(r)
    path = os.path.join(HERE, 'fr3019_no27_tokens.tsv')
    cols = ['line', 'pos', 'token', 'conf', 'why']
    text = '\t'.join(cols) + '\n' + ''.join('\t'.join(r[c] for c in cols) + '\n' for r in rows)
    if '--check' in sys.argv:
        sys.exit(0 if os.path.exists(path) and open(path).read() == text else 1)
    open(path, 'w').write(text)
    n = sum(1 for r in rows if r['token'] not in ('/',))
    print(f'{n} tokens (+{len(rows) - n} "/"), conf ' +
          ', '.join(f'{c} {sum(1 for r in rows if r["conf"] == c)}' for c in 'HML'))


if __name__ == '__main__':
    main()

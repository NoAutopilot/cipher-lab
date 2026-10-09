#!/usr/bin/env python3
"""BRO-178 (9 Oct 2026): body m0178 code run (tail of Carta 79) against appendix Carta 79's period plaintext and cipher copy.

Pre-registered in PREREG-BRO178.md. Known-text key test and body-vs-appendix copy diff, not a reading.
Reuses scripts/24_bro123_align.py's DP, statistic and key-permutation control unchanged.

  python3 scripts/27_bro178_align.py dryrun            # stand-in: first 40 tokens of appendix Carta 13 (not the target)
  python3 scripts/27_bro178_align.py score [--perms 1000] [--seed 178] [--check]
  python3 scripts/27_bro178_align.py diff  [--check]   # token diff, body m0178 vs appendix Carta 79 cipher line
"""
import csv, difflib, importlib.util, sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location('b123', HERE / 'scripts' / '24_bro123_align.py')
b = importlib.util.module_from_spec(spec); spec.loader.exec_module(b)


def appendix(label, col):
    with open(HERE / 'plaintext_appendix.tsv') as f:
        for r in csv.DictReader(f, delimiter='\t'):
            if r['entry_label'] == label:
                return r[col]
    raise SystemExit(label + ' not found')


def check_or_write(out, text, a):
    if '--check' in a:
        ok = out.exists() and out.read_text() == text
        print(out.name, 'OK' if ok else 'STALE'); sys.exit(0 if ok else 1)
    out.write_text(text); print(text)


def main():
    a = sys.argv[1:]
    mode = a[0] if a else 'score'
    perms = int(a[a.index('--perms') + 1]) if '--perms' in a else 1000
    seed = int(a[a.index('--seed') + 1]) if '--seed' in a else 178
    key = b.load_key()
    if mode == 'dryrun':
        toks = []
        with open(HERE / 'ciphertext_appendix.tsv') as f:
            for r in csv.DictReader(f, delimiter='\t'):
                if r['entry_label'] == 'Carta 13':
                    toks.append(('x', r['position'], r['token']))
        toks = toks[:40]
        units = b.expand(toks)
        let = b.fold(appendix('Carta 13', 'deciffrada_line'))
        pairs, h, n, null = b.run_score(units, let, key, perms, seed)
        print(f'dryrun Carta 13[:40]: S={h}/{n}={h/n:.3f} null mean {null.mean():.3f} p99 {np.percentile(null,99):.3f}')
        return
    stream = b.load_stream(HERE / 'body178_ciphertext.tsv')
    if mode == 'score':
        units = b.expand(stream)
        let = b.fold(appendix('Carta 79', 'deciffrada_line'))
        pairs, h, n, null = b.run_score(units, let, key, perms, seed)
        p99 = float(np.percentile(null, 99))
        rows = [('statistic', 'value'), ('tokens_stream', len(stream)), ('units', len(units)), ('letters', len(let)),
                ('keyed_cipher_tokens', n), ('hits', h), ('S_real', f'{h/n:.4f}'), ('null_mean', f'{null.mean():.4f}'),
                ('null_p99', f'{p99:.4f}'), ('null_max', f'{null.max():.4f}'), ('perms', perms), ('seed', seed),
                ('gate', 'PASS' if h / n > p99 else 'FAIL')]
        text = ''.join(f'{r[0]}\t{r[1]}\n' for r in rows)
        al = ['stream_idx\tline\tpos\ttoken\tkind\tkey_value\taligned_letter\tmatch\n']
        for ui, lj in pairs:
            kind, val, k = units[ui]
            v = key.get(val, '') if kind == 'c' else ''
            L = let[lj] if lj >= 0 else ''
            al.append(f'{k}\t{stream[k][0]}\t{stream[k][1]}\t{stream[k][2] if kind=="c" else val}\t{kind}\t{v}\t{L}\t'
                      f'{int(bool(L) and L == (v if kind=="c" else val))}\n')
        if '--check' not in a:
            (HERE / 'bro178_alignment.tsv').write_text(''.join(al))
        check_or_write(HERE / 'bro178_score.tsv', text, a)
    elif mode == 'diff':
        app = [t for t in appendix('Carta 79', 'cipher_line').replace(' ', '.').split('.') if t]
        app = ['w:' + t if t.isalpha() and len(t) > 2 else t for t in app]
        body = [b.norm_token(t) for _, _, t in stream]
        sm = difflib.SequenceMatcher(a=app, b=body, autojunk=False)
        out = ['op\tappendix_idx\tappendix\tbody_idx\tbody\n']
        for op, i1, i2, j1, j2 in sm.get_opcodes():
            out.append(f'{op}\t{i1}-{i2}\t{".".join(app[i1:i2])}\t{j1}-{j2}\t{".".join(body[j1:j2])}\n')
        check_or_write(HERE / 'bro178_diff.tsv', ''.join(out), a)


if __name__ == '__main__':
    main()

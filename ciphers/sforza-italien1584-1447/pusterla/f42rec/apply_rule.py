#!/usr/bin/env python3
"""f.42 two-reader reconciliation under SFZ-READ2's rule (fixed 9 Oct 2026 before any gate was rerun; NOTES.md
"Second reader on f.81 and f.42"), applied by SFZ-F42 (account 4, 9 Oct 2026) to tools/reconcile_passes.py --method nw
output for A = ciphertext_f42_passA_opus.tsv (SFZ-P) and B = ciphertext_f42_passB2_sonnet.tsv (single-line crops).

Rule (rule-based, no image look): agreed columns kept; a split on a pair the f.71/f.67 reconcilers settled takes their
majority label -- {d,g} -> g, {T=,b-} -> b-, {q,V} -> V, {h,h-} -> h-, {d,d'} -> d'; every other split and every
one-sided gap keeps A (a column B alone wrote is dropped). Writes ../ciphertext_f42_reconciled.tsv (one row per line).

    python3 ciphers/sforza-italien1584-1447/pusterla/f42rec/apply_rule.py [--check]
"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'ciphertext_f42_reconciled.tsv')
PAIRS = {frozenset(('d', 'g')): 'g', frozenset(('T=', 'b-')): 'b-', frozenset(('q', 'V')): 'V',
         frozenset(('h', 'h-')): 'h-', frozenset(('d', "d'")): "d'"}
HEAD = ('# BnF italien 1584 f.42, reconciled SFZ-P (Opus) + SFZ-F42 blind Sonnet pass on single-line crops, 9 Oct 2026, '
        'under the f.71/f.67 label convention (SFZ-READ2 rule, f42rec/apply_rule.py); che joined as g÷.\n')


def build():
    rows, order, n = {}, [], {'agree': 0, 'settled': 0, 'keptA': 0, 'droppedB': 0}
    for l in open(os.path.join(HERE, 'ciphertext_draft.tsv'), encoding='utf-8'):
        f = l.rstrip('\n').split('\t')
        if f[0] == 'line':
            continue
        line, sign, alt, why = f[0], f[2], f[4], f[5]
        if line not in rows:
            rows[line] = []; order.append(line)
        if why == 'agree':
            rows[line].append(sign); n['agree'] += 1
        elif why == 'gap' and alt == 'A:-':
            n['droppedB'] += 1
        elif why == 'gap':
            rows[line].append(sign); n['keptA'] += 1
        else:
            b = alt[2:] if alt.startswith('B:') else ''
            v = PAIRS.get(frozenset((sign, b)))
            if v:
                rows[line].append(v); n['settled'] += 1
            else:
                if sign:
                    rows[line].append(sign)
                n['keptA'] += 1
    text = HEAD + ''.join(f'{k}\t{" ".join(rows[k])}\n' for k in order)
    return text, n


if __name__ == '__main__':
    text, n = build()
    if '--check' in sys.argv:
        ok = os.path.exists(OUT) and open(OUT, encoding='utf-8').read() == text
        print('ok' if ok else 'STALE'); sys.exit(0 if ok else 1)
    open(OUT, 'w', encoding='utf-8').write(text)
    print(n, 'signs', sum(len(r.split('\t')[1].split()) for r in text.splitlines()[1:]))

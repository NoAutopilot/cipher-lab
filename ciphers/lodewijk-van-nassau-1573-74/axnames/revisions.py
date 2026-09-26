#!/usr/bin/env python3
"""AX-NAMES2 step 4: every token whose value or grade differs between reading_<n>_tokens.tsv (key.tsv) and
reading_<n>_full_tokens.tsv (key_full.tsv), for the orchestrator to carry into AUDIT.md and any
SECOND-OPINIONS-QUEUE.tsv row (CLAUDE.md rule 10 revision rule). Reads committed files only.

  python3 axnames/revisions.py          write revisions_for_audit.tsv and print per-letter counts
  python3 axnames/revisions.py --check  exit 1 if revisions_for_audit.tsv is stale
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE)
LETTERS = ['4610', '4611', '4616', '5797']


def load(p):
    return list(csv.reader(open(os.path.join(TGT, p)), delimiter='\t'))[1:]


def build():
    key = {r[0]: r for r in load('key_full.tsv')}
    out = [['letter', 'line', 'pos', 'code', 'old', 'new', 'grade', 'class', 'source', 'context_new']]
    counts = {}
    for n in LETTERS:
        o, f = load(f'reading_{n}_tokens.tsv'), load(f'reading_{n}_full_tokens.tsv')
        assert [r[:3] for r in o] == [r[:3] for r in f], n
        c = {'changed': 0, 'word': 0, 'null': 0}
        for i, (a, b) in enumerate(zip(o, f)):
            if a[3:5] == b[3:5]:
                continue
            k = key.get(b[2], ['', '', '', '', ''])
            cls = 'NULL' if b[3] == 'NULL' else 'word'
            c['changed'] += 1; c[cls if cls == 'word' else 'null'] += 1
            win = ' '.join(('<' + x[3] + '>' if j == i else x[3]) for j, x in enumerate(f)
                           if abs(j - i) <= 4 and x[0] == b[0])
            out.append([n, b[0], b[1], b[2], f'{a[3]} {a[4]}', b[3], b[4], cls, k[3], win])
        c['U'] = (sum(r[4] == 'U' for r in o), sum(r[4] == 'U' for r in f))
        counts[n] = c
    return '\n'.join('\t'.join(r) for r in out) + '\n', counts


def main():
    text, counts = build()
    p = os.path.join(TGT, 'revisions_for_audit.tsv')
    if '--check' in sys.argv:
        if not os.path.exists(p) or open(p).read() != text:
            sys.exit('revisions_for_audit.tsv is stale')
    else:
        open(p, 'w').write(text)
    for n, c in counts.items():
        print(f"{n}: changed {c['changed']} (word/name {c['word']}, NULL {c['null']}), U {c['U'][0]} -> {c['U'][1]}")


if __name__ == '__main__':
    main()

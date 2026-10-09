#!/usr/bin/env python3
"""TXE2-BASE-SPIN: mechanical adjudication queue and application, TXE-Q's format (benchmark-tx/txeng/confirm/adjud_queue.tsv).
  build_queue.py queue REC_DIR OUT_QUEUE        disagreements + uncertain -> queue rows (line col kind candidates left right)
  build_queue.py apply REC_DIR ADJUD_OUT PASSZ  draft with each queue row's chosen sign substituted (NONE drops the row)
No sign is chosen here; the adjudicator chooses, this only copies."""
import csv, sys

def rows(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))

def draft(rec):
    d = {}
    for r in rows(rec + '/ciphertext_draft.tsv'):
        d.setdefault(r['line'], []).append(r)
    return d

def cand(s):
    return '(or: no sign here)' if s in ('-', '') else s

def queue(rec, out):
    d = draft(rec)
    q = []
    for r in rows(rec + '/disagreements.tsv'):
        q.append((r['line'], int(r['col']), 'disagree', ' | '.join(cand(x) for x in (r['A'], r['B']))))
    for r in rows(rec + '/uncertain.tsv'):
        c = [r['A']] + ([r['B']] if r['B'] != r['A'] else [])
        q.append((r['line'], int(r['col']), 'uncertain', ' | '.join(cand(x) for x in c)))
    order = {l: i for i, l in enumerate(d)}
    q.sort(key=lambda t: (order[t[0]], t[1]))
    with open(out, 'w') as f:
        f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
        for line, col, kind, c in q:
            signs = [x['sign'] for x in d[line]]
            i = col - 1
            f.write('\t'.join([line, str(col), kind, c, ' '.join(signs[max(0, i - 2):i]), ' '.join(signs[i + 1:i + 3])]) + '\n')
    print(len(q), 'queue rows')

def apply(rec, adj, out):
    d = draft(rec)
    ch = {(r['line'], int(r['col'])): r['sign'].strip() for r in rows(adj)}
    n = 0
    with open(out, 'w') as f:
        f.write('line\tpos\tsign\n')
        for line, rs in d.items():
            pos = 0
            for r in rs:
                s = r['sign']
                k = (line, int(r['position']))
                if k in ch:
                    n += ch[k] != s
                    s = ch[k]
                if s in ('NONE', '-', ''):
                    continue
                pos += 1
                f.write('%s\t%d\t%s\n' % (line, pos, s))
    print(n, 'positions changed vs the draft')

if __name__ == '__main__':
    {'queue': queue, 'apply': apply}[sys.argv[1]](*sys.argv[2:])

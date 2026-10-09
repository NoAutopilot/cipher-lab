#!/usr/bin/env python3
"""TXP-D98 (9 Oct 2026): the adjudication queue from tools/reconcile_passes.py output, and passZ from the adjudicator's answers.

  python3 benchmark-tx/txeng2/dint-f98v-gloss/adjud_tools.py queue   # rec/ -> adjud_queue.tsv
  python3 benchmark-tx/txeng2/dint-f98v-gloss/adjud_tools.py apply   # rec/ciphertext_draft.tsv + adjud_out.tsv -> passZ_pipeline.tsv
Queue = every disagreements.tsv row plus every uncertain.tsv row (agreed but flagged M/L by a reader), candidates A/B,
neighbours = the draft's two signs either side. Apply: the draft's sign, replaced at queued positions by the adjudicator's
choice (NONE deletes; two codes split into two positions). Line ids f98v_L01..L06.
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))


def rd(p):
    with open(p, newline='') as f:
        return list(csv.DictReader(f, delimiter='\t'))


def draft():
    d = {}
    for r in rd(os.path.join(HERE, 'rec/ciphertext_draft.tsv')):
        d.setdefault(r['line'], []).append(r)
    return d


def queue():
    d = draft()
    q = []
    for kind, fn in (('disagree', 'disagreements.tsv'), ('uncertain', 'uncertain.tsv')):
        for r in rd(os.path.join(HERE, 'rec', fn)):
            q.append((r['line'], int(r['col']), kind, ' '.join(dict.fromkeys([r['A'], r['B']]))))
    q.sort(key=lambda x: (x[0], x[1]))
    with open(os.path.join(HERE, 'adjud_queue.tsv'), 'w') as f:
        f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
        for ln, c, k, cand in q:
            seq = [x['sign'] for x in d[ln]]
            f.write('%s\t%d\t%s\t%s\t%s\t%s\n' % (ln, c, k, cand, ' '.join(seq[max(0, c - 3):c - 1]), ' '.join(seq[c:c + 2])))
    print('queue rows', len(q))


def apply():
    d = draft()
    ans = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(os.path.join(HERE, 'adjud_out.tsv'))}
    with open(os.path.join(HERE, 'passZ_pipeline.tsv'), 'w') as f:
        f.write('line\tpos\tsign\n')
        for ln in sorted(d):
            out = []
            for r in d[ln]:
                s = ans.get((ln, int(r['position'])), r['sign'])
                if s == 'NONE' or s == '-':
                    continue
                out += s.split()
            for i, s in enumerate(out, 1):
                f.write('f98v_%s\t%d\t%s\n' % (ln, i, s))
    print('applied', len(ans))


if __name__ == '__main__':
    {'queue': queue, 'apply': apply}[sys.argv[1]]()

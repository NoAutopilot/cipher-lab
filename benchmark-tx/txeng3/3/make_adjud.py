#!/usr/bin/env python3
"""TXE3-3 CROSSHAND: the no.87 passC recipe on a reconcile_passes.py run, parametrised (a per-folder copy of the shape of
benchmark-tx/txpool/gunther8246-p2/make_queue.py + make_passZ.py; candidate for promotion into reconcile_passes.py as
--adjudication-queue / --apply-adjudication, named in RESULTS.md).

  python3 make_adjud.py queue REC_DIR OUT_QUEUE.tsv          # disagreements only (the no.87 recipe: agreed-uncertain rows
                                                            # are NOT re-read), candidates = reader A | reader B, three
                                                            # agreed neighbours each side from ciphertext_draft.tsv
  python3 make_adjud.py apply REC_DIR ADJ_OUT.tsv PREFIX OUT_PASSC.tsv   # draft + adjudicator rows -> line/pos/sign;
                                                            # NONE drops the column, two labels split it
  python3 make_adjud.py norm PASS.tsv PREFIX OUT.tsv         # a reader pass (passage pos sign_id ...) -> line/pos/sign
"""
import csv, sys
rd = lambda p: list(csv.DictReader(open(p, encoding='utf-8'), delimiter='\t'))

def main():
    mode = sys.argv[1]
    if mode == 'queue':
        rec, out = sys.argv[2], sys.argv[3]
        seq = {}
        for r in rd(rec + '/ciphertext_draft.tsv'):
            seq.setdefault(r['line'], []).append(r['sign'] or '-')
        rows = sorted(rd(rec + '/disagreements.tsv'), key=lambda r: (r['line'], int(r['col'])))
        with open(out, 'w', encoding='utf-8') as f:
            f.write('line\tcol\tkind\tcandidates\tleft_neighbours\tright_neighbours\n')
            for r in rows:
                s, c = seq[r['line']], int(r['col'])
                f.write('\t'.join([r['line'], str(c), 'disagree', '%s | %s' % (r['A'] or '-', r['B'] or '-'),
                                   ' '.join(s[max(0, c - 4):c - 1]), ' '.join(s[c:c + 3])]) + '\n')
        print(len(rows), 'queue rows (disagreements only)')
    elif mode == 'apply':
        rec, adjp, prefix, out = sys.argv[2:6]
        adj = {(r['line'], int(r['col'])): r['sign'].strip() for r in rd(adjp)}
        res, cur, pos, used = [], None, 0, 0
        for r in rd(rec + '/ciphertext_draft.tsv'):
            key = (r['line'], int(r['position']))
            s = r['sign'].strip()
            if key in adj:
                s = adj[key]; used += 1
            if r['line'] != cur:
                cur, pos = r['line'], 0
            if s in ('NONE', '-', ''):
                continue
            for t in s.split():
                pos += 1
                res.append(('%s_%s' % (prefix, r['line']), pos, t))
        with open(out, 'w', encoding='utf-8') as f:
            f.write('line\tpos\tsign\n')
            for o in res:
                f.write('%s\t%d\t%s\n' % o)
        print(len(res), 'signs; adjudicated rows applied', used, 'of', len(adj))
    elif mode == 'norm':
        src, prefix, out = sys.argv[2:5]
        res, cur, pos = [], None, 0
        for r in rd(src):
            ln = r.get('passage') or r.get('line')
            s = (r.get('sign_id') or r.get('sign') or '').strip()
            if ln != cur:
                cur, pos = ln, 0
            if not s:
                continue
            pos += 1
            res.append(('%s_%s' % (prefix, ln), pos, s))
        with open(out, 'w', encoding='utf-8') as f:
            f.write('line\tpos\tsign\n')
            for o in res:
                f.write('%s\t%d\t%s\n' % o)
        print(len(res), 'signs')
    else:
        sys.exit(__doc__)

if __name__ == '__main__':
    main()

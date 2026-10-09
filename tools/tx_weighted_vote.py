#!/usr/bin/env python3
"""Learned per-reader-per-sign weighting of transcription passes already on disk (LANE TX-ENGINEER-2 X5, 9 Oct 2026).

    python3 tools/tx_weighted_vote.py learn   --item ITEM --train UNIT.tsv --reader A=passA.tsv ... --key KEY.tsv --out W.json
    python3 tools/tx_weighted_vote.py vote    --item ITEM --base L.tsv --reader A=... --key KEY.tsv (--weights W.json | --loo
                                              --train UNIT.tsv) --out OUT.tsv
    python3 tools/tx_weighted_vote.py control --item ITEM --base L.tsv --reader A=... --key KEY.tsv --train UNIT.tsv
                                              --out-dir DIR --stem passX5   (uniform + permuted-truth seeds 1-5)

Method (PREREG benchmark-tx/PREREG-txeng2-1.md X5, fixed before any score):
  learn  For every reader r, at every scored truth position of the training lines (tools/tx_taxonomy.py's aligned_reads,
         i.e. tools/tx_bench.py's alignment), count (read sign s, truth sign t). t is the read itself when the read is in
         the position's truth set (key conflicts such as T95 s|l accept both), else the row's ref_sign. A position the
         reader deleted is not counted. w(r, s, t) = (c(r,s,t) + 0.5) / (c(r,s) + 0.5 |T|), T = the key's signs (--key,
         column `sign`) + X_CE + any training truth sign outside the key. The truth file is opened ONLY here, only for
         the training lines (--train names them: any TSV with a `line` column).
  vote   The position frame is the base read (--base, e.g. the L read): every reader's line is aligned to the base line
         with tools/tx_bench.align (truth-free: the base sign is the only "truth" of the frame), so a vote needs no truth
         file and an eval output cannot see the eval truth. At each base position the output sign is
         argmax_t sum_r w(r, s_r, t) over the readers covering the line; a reader that deleted the position, or that read
         a sign it never read in training, contributes a uniform weight (no effect). Ties go to the base sign when it is
         among the tied, else the lexically first. Reader insertions are dropped; base positions are never deleted or
         added (the vote changes signs only). --loo learns, for each line, from every OTHER line of --train (leave-one-
         line-out: a line's own truth never trains the weights that vote on it). --uniform is the plain-majority control
         (every weight 1 for the read sign, 0 otherwise; same frame, same tie rule).
  control  Writes <stem>_uniform_<unit>.tsv and <stem>_perm<seed>_<unit>.tsv (seeds 1-5): the truth (ref_sign, truth set)
         is permuted across all training positions with the seed, then the same leave-one-line-out vote. A permuted-truth
         output that passes the dev gate voids the real one.
The tool never writes a truth, never scores (tools/tx_bench.py scores), never calls a model. Exit 0; 2 on bad input.
Test: tools/tests/test_tx_weighted_vote.py (three readers, one biased: leave-one-line-out weights fix the biased reader's
error, uniform weights do not).
"""
import argparse, json, os, random, sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402
import tx_taxonomy  # noqa: E402

DEL = '<deleted>'


def parse_readers(specs):
    out = []
    for s in specs or []:
        if '=' not in s:
            sys.exit('tx_weighted_vote: --reader wants NAME=PATH, got %r' % s)
        n, p = s.split('=', 1)
        out.append((n, tx_bench.load_output([p])))
    if not out:
        sys.exit('tx_weighted_vote: at least one --reader')
    return out


def key_signs(path):
    T = {r['sign'].strip() for r in tx_bench.read_tsv(path) if r.get('sign')}
    T.add('X_CE')
    return T


def unit_lines(path):
    return sorted({r['line'] for r in tx_bench.read_tsv(path)})


def truth_rows(bench, item):
    base = os.path.dirname(os.path.abspath(bench))
    for it in tx_bench.read_tsv(bench):
        if it['item'] == item:
            return tx_bench.read_tsv(os.path.join(base, it['truth']))
    sys.exit('tx_weighted_vote: item %s not in %s' % (item, bench))


def permute_truth(rows, seed):
    """Permute (ref_sign, truth) across the scored rows of the given rows (one shared permutation for every reader)."""
    idx = [i for i, r in enumerate(rows) if r['status'] == 'scored']
    vals = [(rows[i]['ref_sign'], rows[i]['truth']) for i in idx]
    random.Random(seed).shuffle(vals)
    out = [dict(r) for r in rows]
    for i, (rs, t) in zip(idx, vals):
        out[i]['ref_sign'], out[i]['truth'] = rs, t
    return out


def learn_counts(readers, rows, lines):
    """{reader: {s: Counter(t)}} over the scored positions of `lines` (rows = truth rows, possibly permuted)."""
    rows = [r for r in rows if r['line'] in lines]
    tmap = {(r['line'], r['pos']): r for r in rows}
    counts, extra = {}, set()
    for name, rl in readers:
        sub = {ln: v for ln, v in rl.items() if ln in lines}
        reads, _ = tx_taxonomy.aligned_reads(rows, sub)
        c = defaultdict(Counter)
        for k, s in reads.items():
            if s == DEL:
                continue
            r = tmap[k]
            ts = set(filter(None, r['truth'].split('|')))
            t = s if s in ts else r['ref_sign']
            c[s][t] += 1
            extra.add(t)
        counts[name] = c
    return counts, extra


def weight_fn(counts, T):
    nT = len(T)

    def w(name, s, t):
        c = counts.get(name, {}).get(s)
        if not c:
            return 1.0 / nT
        return (c.get(t, 0) + 0.5) / (sum(c.values()) + 0.5 * nT)
    return w


def frame_reads(readers, base_line, ln):
    """[(reader, [read or None per base position])] for readers covering line ln."""
    out = []
    ts = [{b} for b in base_line]
    for name, rl in readers:
        if ln not in rl:
            continue
        col = [None] * len(base_line)
        for bi, s in tx_bench.align(base_line, ts, rl[ln]):
            if bi is not None:
                col[bi] = s
        out.append((name, col))
    return out


def vote_line(base_line, cols, T, w=None):
    out, changed = [], []
    for i, b in enumerate(base_line):
        cands = set(T) | {b} | {c[i] for _, c in cols if c[i] is not None}
        score = Counter()
        for name, c in cols:
            s = c[i]
            if s is None:
                continue
            if w is None:
                score[s] += 1.0
            else:
                for t in cands:
                    score[t] += w(name, s, t)
        if not score:
            out.append(b); continue
        best = max(score.values())
        tied = sorted(t for t, v in score.items() if abs(v - best) < 1e-12)
        pick = b if b in tied else tied[0]
        out.append(pick)
        if pick != b:
            changed.append((i, b, pick))
    return out, changed


def write_out(path, res, header=''):
    with open(path, 'w') as f:
        if header:
            f.write('# %s\n' % header)
        f.write('line\tpos\tsign\n')
        for ln in sorted(res):
            for i, s in enumerate(res[ln], 1):
                f.write('%s\t%d\t%s\n' % (ln, i, s))


def run_vote(readers, base, T, mode, train_lines=None, rows=None, counts=None, extra=()):
    """mode: 'uniform' | 'weights' (counts given) | 'loo' (rows + train_lines). Returns ({line: signs}, changes)."""
    res, changes = {}, []
    for ln in sorted(base):
        cols = frame_reads(readers, base[ln], ln)
        if mode == 'uniform':
            w, TT = None, T
        elif mode == 'weights':
            TT = set(T) | set(extra)
            w = weight_fn(counts, TT)
        else:
            others = set(train_lines) - {ln}
            c, ex = learn_counts(readers, rows, others)
            TT = set(T) | ex
            w = weight_fn(c, TT)
        res[ln], ch = vote_line(base[ln], cols, TT, w)
        changes += [(ln, i + 1, b, p) for i, b, p in ch]
    return res, changes


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n\n')[0])
    ap.add_argument('cmd', choices=['learn', 'vote', 'control'])
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv')
    ap.add_argument('--item', required=True)
    ap.add_argument('--reader', action='append', help='NAME=PATH (tx_bench format), repeat')
    ap.add_argument('--key', required=True, help='key sheet TSV with a `sign` column (the smoothing inventory)')
    ap.add_argument('--train', help='TSV whose `line` column names the training lines (learn, --loo, control)')
    ap.add_argument('--base', help='the position frame for vote/control (e.g. the L read); only its lines are voted')
    ap.add_argument('--weights', help='vote: counts JSON written by learn')
    ap.add_argument('--loo', action='store_true', help='vote: leave-one-line-out over --train')
    ap.add_argument('--uniform', action='store_true', help='vote: plain majority control')
    ap.add_argument('--permute-seed', type=int, help='learn/--loo: permute the truth across training positions first')
    ap.add_argument('--out', help='learn: JSON; vote: TSV')
    ap.add_argument('--out-dir'); ap.add_argument('--stem', default='passX5'); ap.add_argument('--unit', default='dev_tune')
    ap.add_argument('--changes', help='vote/control: also write the changed positions (line, pos, base, out) here')
    a = ap.parse_args(argv)
    readers = parse_readers(a.reader)
    T = key_signs(a.key)
    if a.cmd == 'learn':
        if not (a.train and a.out):
            print('learn needs --train and --out', file=sys.stderr); return 2
        rows = truth_rows(a.bench, a.item)
        if a.permute_seed is not None:
            rows = permute_truth([r for r in rows if r['line'] in set(unit_lines(a.train))], a.permute_seed)
        counts, extra = learn_counts(readers, rows, set(unit_lines(a.train)))
        json.dump({'readers': [n for n, _ in readers], 'extra_truth_signs': sorted(extra - T),
                   'counts': {n: {s: dict(c) for s, c in cs.items()} for n, cs in counts.items()}},
                  open(a.out, 'w'), indent=1, sort_keys=True)
        print('learn: %d readers, %d training lines -> %s' % (len(readers), len(unit_lines(a.train)), a.out))
        return 0
    if not a.base:
        print('%s needs --base' % a.cmd, file=sys.stderr); return 2
    base = tx_bench.load_output([a.base])
    names = ','.join(n for n, _ in readers)
    if a.cmd == 'vote':
        if a.uniform:
            res, ch = run_vote(readers, base, T, 'uniform'); tag = 'uniform'
        elif a.weights:
            J = json.load(open(a.weights))
            counts = {n: {s: Counter(c) for s, c in cs.items()} for n, cs in J['counts'].items()}
            res, ch = run_vote(readers, base, T, 'weights', counts=counts, extra=J.get('extra_truth_signs', []))
            tag = 'weights %s' % os.path.basename(a.weights)
        elif a.loo and a.train:
            rows = truth_rows(a.bench, a.item)
            tl = set(unit_lines(a.train))
            rows = [r for r in rows if r['line'] in tl]
            if a.permute_seed is not None:
                rows = permute_truth(rows, a.permute_seed)
            res, ch = run_vote(readers, base, T, 'loo', train_lines=tl, rows=rows)
            tag = 'leave-one-line-out' + (' permuted seed %d' % a.permute_seed if a.permute_seed is not None else '')
        else:
            print('vote needs --uniform, --weights or --loo --train', file=sys.stderr); return 2
        write_out(a.out, res, 'tx_weighted_vote %s; readers %s; frame %s' % (tag, names, os.path.basename(a.base)))
        if a.changes:
            with open(a.changes, 'w') as f:
                f.write('line\tpos\tbase\tout\n' + ''.join('%s\t%d\t%s\t%s\n' % c for c in ch))
        print('vote (%s): %d lines, %d positions changed from the base -> %s' % (tag, len(res), len(ch), a.out))
        return 0
    # control
    if not (a.train and a.out_dir):
        print('control needs --train and --out-dir', file=sys.stderr); return 2
    os.makedirs(a.out_dir, exist_ok=True)
    tl = set(unit_lines(a.train))
    res, ch = run_vote(readers, base, T, 'uniform')
    p = os.path.join(a.out_dir, '%s_uniform_%s.tsv' % (a.stem, a.unit))
    write_out(p, res, 'tx_weighted_vote uniform control; readers %s; frame %s' % (names, os.path.basename(a.base)))
    print('control uniform: %d changed -> %s' % (len(ch), p))
    rows0 = [r for r in truth_rows(a.bench, a.item) if r['line'] in tl]
    for seed in range(1, 6):
        res, ch = run_vote(readers, base, T, 'loo', train_lines=tl, rows=permute_truth(rows0, seed))
        p = os.path.join(a.out_dir, '%s_perm%d_%s.tsv' % (a.stem, seed, a.unit))
        write_out(p, res, 'tx_weighted_vote leave-one-line-out, truth permuted seed %d; readers %s; frame %s'
                  % (seed, names, os.path.basename(a.base)))
        print('control perm seed %d: %d changed -> %s' % (seed, len(ch), p))
    return 0


if __name__ == '__main__':
    sys.exit(main())

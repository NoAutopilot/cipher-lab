#!/usr/bin/env python3
"""NEXT-PAG (2 Oct 2026): run tools/interlinear_align.py on pairs.tsv, with its rule-3 controls.

1. Train: align every pair except the held-out ones (pairs.tsv column held_out) -> align_train.tsv, key_train.tsv.
2. Known-answer check: spell each held-out pair's codes from key_train (unknown code -> '?') and count the
   gloss letters recovered (difflib matching blocks, folded f=s, u=v, y=i).
3. Shuffle control (can fail differently: the manipulation is the pairing, the statistic is pairing-driven):
   permute cipher_raw across the training pairs, N seeds, same alignment, same two statistics.
4. Full run (all pairs, held-out included) -> align_all.tsv, key_all.tsv: the key written for the target.
    python3 evaluate.py [--seeds 20] [--null-cost X] [--max-chunk N] [--seg-bonus B] [--len-prior X] [--no-held] [--write]
--no-held: print only the training statistics (used for the parameter grid, so the held-out pairs stay unseen
until the settings are fixed); --write: write align_/key_ files for train and all.
"""
import csv, difflib, os, random, sys, io, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, '..', '..', '..', 'tools'))
import interlinear_align as ia

FLOOR = 1


def fold(s):
    return ia.fold(s).replace('y', 'i')


def stats(prepared, results, counts):
    agree = tot = 0
    for (p, raw, toks, letters, *_), chunks in zip(prepared, results):
        for (kind, val), c in zip(toks, chunks):
            if kind != 'num' or not c or c[1] <= c[0]:
                continue
            tot += 1
            top, n = ia.top_of(counts[val])
            if ia.fold(letters[c[0]:c[1]]) == top and n >= 2:
                agree += 1
    return agree, tot


def key_of(counts):
    return {v: ia.top_of(c)[0] for v, c in counts.items()}


def predict(pairs, key):
    got = want = 0
    lines = []
    for p in pairs:
        toks = [ia.classify_token(t) for t in p['cipher_raw'].split()]
        spelled = ''.join(key.get(v, '?') if k == 'num' else '' for k, v in toks)
        gold = ia.plain_letters(p['plain_raw'])[0]
        m = sum(b.size for b in difflib.SequenceMatcher(None, fold(spelled), fold(gold), autojunk=False).get_matching_blocks())
        got += m
        want += len(gold)
        lines.append('%s\t%s\t%s\t%s\t%d/%d' % (p['plain_line'], p['cipher_raw'], gold,
                     '.'.join(key.get(v, '?') if k == 'num' else '' for k, v in toks), m, len(gold)))
    return got, want, lines


OPTS = {}


def run(pairs, null_cost):
    with contextlib.redirect_stdout(io.StringIO()):
        return ia.run_align(pairs, floor=FLOOR, null_cost=null_cost, **OPTS)


def write(prepared, results, counts, shown, tag):
    rows = ia.token_rows(prepared, results, counts, shown)
    with open(os.path.join(HERE, 'align_%s.tsv' % tag), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['cipher_line', 'idx', 'raw', 'kind', 'value', 'repair', 'plain_chunk', 'status'])
        w.writerows(rows)
    with open(os.path.join(HERE, 'key_%s.tsv' % tag), 'w', encoding='utf-8', newline='') as f:
        w = csv.writer(f, delimiter='\t', lineterminator='\n')
        w.writerow(['value', 'meaning', 'n', 'agree', 'others'])
        for v in sorted(counts):
            top, n = ia.top_of(counts[v])
            rest = sorted(counts[v].items(), key=lambda kv: (-kv[1], kv[0]))[1:]
            w.writerow([v, ia.display(shown, v, top), sum(counts[v].values()), n,
                        ','.join('%s:%d' % (ia.display(shown, v, m), c) for m, c in rest)])


def main():
    a = sys.argv[1:]
    seeds = int(a[a.index('--seeds') + 1]) if '--seeds' in a else 20
    null_cost = float(a[a.index('--null-cost') + 1]) if '--null-cost' in a else -3.0
    for flag, name, typ in (('--max-chunk', 'max_chunk', int), ('--seg-bonus', 'seg_bonus', float),
                            ('--len-prior', 'len_prior', float)):
        if flag in a:
            OPTS[name] = typ(a[a.index(flag) + 1])
    no_held, wr = '--no-held' in a, '--write' in a
    tag = '' if wr else 'x'
    pairs = ia.load_pairs(os.path.join(HERE, 'pairs.tsv'))
    train = [p for p in pairs if p['held_out'] != 'yes']
    held = [p for p in pairs if p['held_out'] == 'yes']
    prep, res, counts, shown = run(train, null_cost)
    if not tag:
        write(prep, res, counts, shown, 'train')
    ag, tot = stats(prep, res, counts)
    got, want, lines = predict(held, key_of(counts))
    print('null_cost %g %s' % (null_cost, OPTS))
    if no_held:
        print('REAL     self-agreement %d/%d = %.3f' % (ag, tot, ag / tot))
    else:
        print('REAL     self-agreement %d/%d = %.3f; held-out letters %d/%d = %.3f' % (ag, tot, ag / tot, got, want, got / want))
        for l in lines:
            print('  held-out\t' + l)
    sa, sh = [], []
    for s in range(seeds):
        rnd = random.Random(s)
        ciphers = [p['cipher_raw'] for p in train]
        rnd.shuffle(ciphers)
        sp = [dict(p, cipher_raw=c) for p, c in zip(train, ciphers)]
        pr, rs, cn, _ = run(sp, null_cost)
        a2, t2 = stats(pr, rs, cn)
        g2, w2, _ = predict(held, key_of(cn))
        sa.append(a2 / t2)
        sh.append(g2 / w2)
    sa.sort(); sh.sort()
    p95 = lambda xs: xs[min(len(xs) - 1, int(round(0.95 * (len(xs) - 1))))]
    if no_held:
        print('SHUFFLE  (%d seeds) self-agreement mean %.3f max %.3f p95 %.3f; margin over p95 %.3f'
              % (seeds, sum(sa) / seeds, sa[-1], p95(sa), ag / tot - p95(sa)))
        return
    print('SHUFFLE  (%d seeds) self-agreement mean %.3f max %.3f p95 %.3f; held-out letters mean %.3f max %.3f p95 %.3f'
          % (seeds, sum(sa) / seeds, sa[-1], p95(sa), sum(sh) / seeds, sh[-1], p95(sh)))
    if not tag:
        pa, ra, ca, sha = run(pairs, null_cost)
        write(pa, ra, ca, sha, 'all')
        ag, tot = stats(pa, ra, ca)
        print('ALL      self-agreement %d/%d = %.3f; values %d' % (ag, tot, ag / tot, len(ca)))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""f.13 (BnF italien 1584, Pusterla, Guastalla 21 Jan 1447) under Pusterla's 1447 key -- SFZ-P, 7 Oct 2026 (S3 of
.claude/briefs/runs/2026-10-07-acct2-st-rebuild-workers.md).

Key: ../sforza-italien1584-1447/pusterla/key.tsv (pooled from the glossed pairs f.81/f.80 and f.42/f.41; G1 PASS,
gate_g1.tsv). Transcription: ciphertext_f13_passA.tsv (SFZ-P's reading; the Sonnet pass B disagrees on 61% of aligned
columns, see NOTES.md). Signs absent from the key decode to '_'.

Control (pre-registered): the same decode under 200 shuffled keys (the key's sign -> value map permuted among key signs),
on two statistics -- lm: mean log10 4-gram probability per letter, tools/judge_plaintext.py NgramModel on it16dip
(16th-c. Italian diplomatic letters; era-mismatched for 1447, flagged); q4: fraction of the decode's 4-grams found in
the pool's clear copies (f.80, f.41). Beside them the decode's letter distribution (degenerate-optimum check).
Grades per token: S where the sign's key value is C (>= 2 attestations, share >= 0.6) and the control passed; M
otherwise; '_' unread.

    python3 ciphers/sforza-pusterla-1447-f13/decode.py [--check]
--check: exit 1 if reading.txt / decode_stats.tsv on disk differ from the recomputation (rule 7).
"""
import collections, os, sys
import numpy as np
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.join(HERE, '..', '..')
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import judge_plaintext as jp  # noqa: E402
POOL = os.path.join(ROOT, 'ciphers', 'sforza-italien1584-1447', 'pusterla')
SEED, NSHUF = 13, 200


def load():
    key, grade = {}, {}
    for l in open(os.path.join(POOL, 'key.tsv')).read().split('\n')[1:]:
        if l:
            a = l.split('\t'); key[a[0]] = a[1]; grade[a[0]] = a[5]
    lines = []
    for l in open(os.path.join(HERE, 'ciphertext_f13_passA.tsv')):
        if l.startswith('#') or not l.strip():
            continue
        n, t = l.rstrip('\n').split('\t')
        toks, i = t.split(), 0
        out = []
        while i < len(toks):
            if i + 1 < len(toks) and toks[i] == 'g' and toks[i + 1] == '÷':
                out.append('g÷'); i += 2
            else:
                out.append(toks[i]); i += 1
        lines.append((n, out))
    return key, grade, lines


def main(check=False):
    key, grade, lines = load()
    body = [x for n, t in lines if n != 'f13_SIG' for x in t]
    signs = sorted(key); vals = [key[s] for s in signs]
    lm = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA['it16dip']])
    clear = ''.join(jp.fold(' '.join(x for x in open(os.path.join(POOL, f)) if not x.startswith('#')))
                    for f in ('clear_f80.txt', 'clear_f41.txt'))
    g4 = {clear[i:i + 4] for i in range(len(clear) - 3)}

    def dec(m):
        return ''.join(m.get(x, '') for x in body)

    def stats(m):
        s = dec(m)
        return lm.score(s), float(np.mean([s[i:i + 4] in g4 for i in range(len(s) - 3)]))
    rl, rq = stats(key)
    rng = np.random.default_rng(SEED); sl, sq = [], []
    for _ in range(NSHUF):
        a, b = stats(dict(zip(signs, rng.permutation(vals)))); sl.append(a); sq.append(b)
    p95l, p95q = float(np.quantile(sl, .95)), float(np.quantile(sq, .95))
    passed = rl > p95l and rq > p95q
    s = dec(key); cnt = collections.Counter(s)
    unk = sum(1 for x in body if x not in key)
    rows = ['statistic\treal\tshuffle_mean\tshuffle_p95\tabove_p95',
            f'lm_it16dip\t{rl:.3f}\t{np.mean(sl):.3f}\t{p95l:.3f}\t{rl > p95l}',
            f'q4_copies\t{rq:.3f}\t{np.mean(sq):.3f}\t{p95q:.3f}\t{rq > p95q}',
            f'# signs {len(body)}; not in key {unk}; decoded letters {len(s)}; verdict {"PASS" if passed else "FAIL"} (both above p95)',
            '# letter distribution: ' + ' '.join(f'{c}:{n}' for c, n in cnt.most_common())]
    out = ['# f.13 decode under Pusterla key.tsv -- TEST OUTPUT' + ('' if passed else ' (control FAILED: not a reading; every token M at best)'),
           '# per line: decoded letters (signs not in key = _), then sign=value/grade']
    ns = nm = 0
    for n, t in lines:
        dl = ''.join(key.get(x, '_') for x in t)
        g = []
        for x in t:
            gr = ('S' if passed and grade.get(x) == 'C' else 'M') if x in key else '_'
            ns += gr == 'S'; nm += gr == 'M'
            g.append(f'{x}={key.get(x, "_")}/{gr}')
        out += [f'{n}\t{dl}', f'{n}_grades\t' + ' '.join(g)]
    out.append(f'# grades: S {ns}, M {nm}, unread {sum(len(t) for _, t in lines) - ns - nm}; no H, no C (cryptanalytic result)')
    rtxt, stxt = '\n'.join(out) + '\n', '\n'.join(rows) + '\n'
    if check:
        bad = [f for f, t in (('reading.txt', rtxt), ('decode_stats.tsv', stxt))
               if not os.path.exists(os.path.join(HERE, f)) or open(os.path.join(HERE, f)).read() != t]
        print('stale: ' + ', '.join(bad) if bad else 'ok: reading.txt and decode_stats.tsv reproduce')
        return 1 if bad else 0
    open(os.path.join(HERE, 'reading.txt'), 'w').write(rtxt)
    open(os.path.join(HERE, 'decode_stats.tsv'), 'w').write(stxt)
    print(stxt + rtxt)
    return 0


if __name__ == '__main__':
    sys.exit(main('--check' in sys.argv))

"""NEXT-HAR (2 Oct 2026): rerun Bourdeau's solve.py (MIT, vendored, see SOURCE.md) on the third-pass sign strings of
ff.80r-81r, 92r and 96v (runs_nexthar.txt), with his loop-1 values (already in SETS: L=e, c=o/a/e, d=o/d, l=l/t/p)
plus '-' = b, and the rule-3 controls:
  null   - each unread group's signs shuffled in place (same signs, same length), 10 shuffles: rate of exact hits;
  known  - words of Cobham's own 1588 clear text (harley287 READING.md, Bourdeau), length-matched to the unread
           groups, enciphered with this sign inventory (each letter -> a random sign whose set holds it) at 0, 10 and
           20 % per-sign substitution error: rate at which the true word is the solver's rank-1 exact candidate, and
           rate at which it is anywhere in its exact or near list.
    python3 run_nexthar.py [--control-text FILE] [--out out_nexthar.txt] [--check]
--set SIGN=LETTERS overrides a value set (RUN1-HAR: --set 8=cd --out out_har_8cd.txt).
--check exits 1 if out_nexthar.txt differs from a fresh run (rule 7).
"""
import argparse, collections, io, os, random, re, sys, contextlib
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import solve
solve.SETS['-'] = 'b'

def parse(path):
    runs = []
    for line in open(path, encoding='utf8'):
        if line.startswith('#') or '|' not in line:
            continue
        rid, before, words, after = [x.strip() for x in line.split('|')]
        ws = []
        for w in words.split():
            if w.startswith('['):
                ws.append((w, 'code', ''))
                continue
            s, st = w.split('=')
            ws.append((s, st[0], st[2:-1] if st[0] == 'R' else ''))
        runs.append((rid, before, ws, after))
    return runs

def target(runs, d, lex):
    out, stats = [], collections.Counter()
    for rid, before, ws, after in runs:
        out.append(f'== {rid}: ...{before} [{" ".join(w for w, _, _ in ws)}] {after}...')
        for s, st, g in ws:
            if st == 'code':
                out.append(f'   {s:14s} code sign'); continue
            c = solve.candidates(s, d)
            f = [x for x in solve.fuzzy(s, lex) if x[0] > 0]
            tag = 'unread' if st == 'U' else f'read[{g}]'
            out.append(f'   {s:14s} {tag:9s} exact: ' + ('  '.join(f'{x}({n})' for n, x in c) if c else '-'))
            if f:
                out.append(f'   {"":24s} near:  ' + '  '.join(f'{x}({n},{e})' for e, x, n in f))
            stats[(st, 'n')] += 1
            stats[(st, 'exact')] += bool(c)
            stats[(st, 'any')] += bool(c or f)
    return out, stats

def null(runs, d, lex, reps=10, seed=1):
    rng = random.Random(seed)
    words = [s for _, _, ws, _ in runs for s, st, _ in ws if st == 'U']
    n = ex = an = 0
    for _ in range(reps):
        for s in words:
            t = list(s); rng.shuffle(t); t = ''.join(t)
            c = solve.candidates(t, d); f = [x for x in solve.fuzzy(t, lex) if x[0] > 0]
            n += 1; ex += bool(c); an += bool(c or f)
    return n, ex, an

def known(runs, d, lex, text, err, reps=3, seed=2):
    rng = random.Random(seed + int(err * 100))
    inv = collections.defaultdict(list)
    for sg, ls in solve.SETS.items():
        if sg in ('K', '?'):
            continue
        for ch in ls:
            inv[ch].append(sg)
    inv['u'] += [':']; inv['v'] += [':']; inv['j'] += ['I', 'X']
    words = [w for w in re.findall(r'[a-z]+', open(text, encoding='utf8').read().lower())
             if all(ch in inv for ch in w)]
    bylen = collections.defaultdict(list)
    for w in words:
        bylen[len(w)].append(w)
    signs = sorted(set(sg for v in inv.values() for sg in v))
    lens = [len(s) for _, _, ws, _ in runs for s, st, _ in ws if st == 'U']
    n = r1 = inl = 0
    for _ in range(reps):
        for L in lens:
            pool = bylen.get(L) or bylen[max(k for k in bylen if k <= L)]
            w = rng.choice(pool)
            enc = ''.join(rng.choice(signs) if rng.random() < err else rng.choice(inv[ch]) for ch in w)
            c = solve.candidates(enc, d); f = solve.fuzzy(enc, lex)
            truth = solve.norm(w)
            n += 1
            r1 += bool(c) and solve.norm(c[0][1]) == truth
            inl += any(solve.norm(x) == truth for _, x in c) or any(solve.norm(x) == truth for _, x, _ in f)
    return n, r1, inl

def by_length(runs, d, text, reps=200, kreps=20):
    """Exact-hit rates on unread groups split at 5 signs: target, shuffled null, and the known-answer control
    (any-exact and true-word rank-1) at 0-40 % sign error, all candidates() only (no fuzzy), so cheap."""
    out = []
    U = [s for _, _, ws, _ in runs for s, st, _ in ws if st == 'U']
    for lo, hi in ((1, 4), (5, 99)):
        W = [s for s in U if lo <= len(s) <= hi]
        t = sum(bool(solve.candidates(s, d)) for s in W)
        rng = random.Random(1); n = e = 0
        for _ in range(reps):
            for s in W:
                x = list(s); rng.shuffle(x); n += 1; e += bool(solve.candidates(''.join(x), d))
        out.append(f'# unread groups of {lo}-{hi if hi < 99 else "+"} signs: {len(W)}; target any exact {t} ({t/len(W):.3f}); '
                   f'shuffled null any exact {e/n:.3f} ({reps} reps)')
    inv = collections.defaultdict(list)
    for sg, ls in solve.SETS.items():
        if sg in ('K', '?'):
            continue
        for ch in ls:
            inv[ch].append(sg)
    inv['u'] += [':']; inv['v'] += [':']; inv['j'] += ['I', 'X']
    words = [w for w in re.findall('[a-z]+', open(text, encoding='utf8').read().lower()) if all(c in inv for c in w)]
    by = collections.defaultdict(list)
    for w in words:
        by[len(w)].append(w)
    signs = sorted({x for v in inv.values() for x in v})
    L = [len(s) for s in U if len(s) >= 5]
    for err in (0, .1, .2, .3, .4):
        rng = random.Random(7); n = ex = r1 = 0
        for _ in range(kreps):
            for l in L:
                w = rng.choice(by.get(l) or by[max(k for k in by if k <= l)])
                e = ''.join(rng.choice(signs) if rng.random() < err else rng.choice(inv[c]) for c in w)
                c = solve.candidates(e, d); n += 1; ex += bool(c)
                r1 += bool(c) and solve.norm(c[0][1]) == solve.norm(w)
        out.append(f'# known-answer, 5+ signs, {int(err*100)}% sign error: any exact {ex/n:.3f}; true word rank-1 {r1/n:.3f} (n={n})')
    return out

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--runs', default=os.path.join(HERE, 'runs_nexthar.txt'))
    ap.add_argument('--control-text', default=os.path.join(HERE, 'control_cobham_clear.txt'))
    ap.add_argument('--out', default=os.path.join(HERE, 'out_nexthar.txt'))
    ap.add_argument('--check', action='store_true')
    ap.add_argument('--set', action='append', default=[], metavar='SIGN=LETTERS',
                    help="override a sign's value set, e.g. --set 8=cd (RUN1-HAR, 4 Oct 2026: gloss/key_f84_f90.tsv)")
    a = ap.parse_args()
    for kv in a.set:
        sg, ls = kv.split('=', 1)
        solve.SETS[sg] = ls
    d = solve.load(); lex = [(v[1], v[0]) for v in d.values() if v[1]]
    runs = parse(a.runs)
    lines, st = target(runs, d, lex)
    lines.append('')
    lines.append('# counts (target)')
    for k, name in (('U', 'unread'), ('R', 'read by Bourdeau')):
        lines.append(f'{name}: {st[(k, "n")]} groups; any exact candidate {st[(k, "exact")]}; exact or near {st[(k, "any")]}')
    n, ex, an = null(runs, d, lex)
    lines.append(f'# null control (unread groups, signs shuffled, 10 reps): {n} strings; any exact {ex} ({ex/n:.3f}); exact or near {an} ({an/n:.3f})')
    for err in (0.0, 0.1, 0.2):
        n, r1, inl = known(runs, d, lex, a.control_text, err)
        lines.append(f'# known-answer control, Cobham clear words length-matched, {int(err*100)}% sign error: {n} words; '
                     f'true word rank-1 exact {r1} ({r1/n:.3f}); true word in exact or near list {inl} ({inl/n:.3f})')
    lines += by_length(runs, d, a.control_text)
    text = '\n'.join(lines) + '\n'
    if a.check:
        old = open(a.out, encoding='utf8').read() if os.path.exists(a.out) else ''
        print('check: ' + ('ok' if old == text else 'STALE')); sys.exit(0 if old == text else 1)
    open(a.out, 'w', encoding='utf8').write(text)
    print(text[text.index('# counts'):])

if __name__ == '__main__':
    main()

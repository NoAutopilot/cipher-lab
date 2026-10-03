#!/usr/bin/env python3
"""Build the numeral -> letter table from R1411 p.1's period interlinear gloss and run the pre-registered held-out gate.

  python3 gloss_table.py [--pairs pairs.tsv] [--seed 1411] [--draws 10000] [--check]

Reads pairs.tsv (line, pos, token, gloss, grade; the reconciled GAPS141 transcription), writes table.tsv
(number, letter, count, conflicts) and heldout.txt (the gate per PREREG.md). --check regenerates both and exits 1 if
the committed copies differ (rule 7).
"""
import argparse, collections, csv, os, random, sys

HERE = os.path.dirname(os.path.abspath(__file__))


def load(path):
    rows = list(csv.DictReader(open(path, encoding='utf-8'), delimiter='\t'))
    clean = [r for r in rows if r['gloss'].strip() and '?' not in r['token'] + r['gloss'] and r['grade'] == 'C']
    doubt = [r for r in rows if r['gloss'].strip() and r not in clean]
    return rows, clean, doubt


def fit(pairs):
    by = collections.defaultdict(collections.Counter)
    for r in pairs:
        by[int(r['token'])][r['gloss'].strip()] += 1
    return {n: c.most_common(1)[0][0] for n, c in by.items()}, by


def acc(table, test):
    cov = [r for r in test if int(r['token']) in table]
    hit = sum(table[int(r['token'])] == r['gloss'].strip() for r in cov)
    return len(cov), hit


def run(pairs_path, seed, draws):
    rows, clean, doubt = load(pairs_path)
    out = []
    table, by = fit(clean)
    tab = ['number\tletter\tcount\tconflicts']
    for n in sorted(by):
        c = by[n]
        tab.append(f"{n}\t{table[n]}\t{sum(c.values())}\t{','.join(f'{k}:{v}' for k, v in c.items() if k != table[n])}")
    letters = collections.defaultdict(list)
    for n in sorted(table):
        letters[table[n]].append(n)
    out.append(f"rows {len(rows)}; glossed clean (grade C, no '?') {len(clean)}; glossed doubtful {len(doubt)}; "
               f"unglossed {len(rows) - len(clean) - len(doubt)}")
    out.append(f"distinct numbers {len(table)}; distinct letters {len(letters)}; homophones per letter: " +
               ', '.join(f"{l}={len(v)}({' '.join(map(str, v))})" for l, v in sorted(letters.items())))
    # held-out
    h = len(clean) // 2
    fitp, test = clean[:h], clean[h:]
    ft, _ = fit(fitp)
    ncov, hit = acc(ft, test)
    a = hit / ncov if ncov else 0.0
    rng = random.Random(seed)
    keys, vals = list(ft), list(ft.values())
    sh = []
    for _ in range(draws):
        rng.shuffle(vals)
        _, hh = acc(dict(zip(keys, vals)), test)
        sh.append(hh / ncov if ncov else 0.0)
    sh.sort()
    p99 = sh[int(0.99 * draws) - 1]
    ge = sum(x >= a for x in sh)
    out.append(f"held-out: fit {len(fitp)} pairs ({len(ft)} numbers), test {len(test)} pairs; coverage {ncov}/{len(test)} "
               f"= {ncov / len(test) if test else 0:.3f}; accuracy {hit}/{ncov} = {a:.3f}")
    out.append(f"control (value-shuffled fit table, {draws} draws, seed {seed}): mean {sum(sh) / draws:.3f}, "
               f"p99 {p99:.3f}, max {sh[-1]:.3f}, draws >= real {ge}")
    if ncov < 8:
        verdict = 'NON-TEST (covered test pairs < 8)'
    elif a >= 0.80 and a > p99:
        verdict = 'PASS'
    else:
        verdict = 'FAIL'
    out.append(f"gate: {verdict}")
    # secondary: self-consistency vs position-shuffled glosses
    def selfcons(ps):
        _, b = fit(ps)
        rep = [c for c in b.values() if sum(c.values()) > 1]
        tot = sum(sum(c.values()) for c in rep)
        return (sum(c.most_common(1)[0][1] for c in rep), tot)
    s, t = selfcons(clean)
    gl = [r['gloss'] for r in clean]
    sc = []
    for _ in range(draws):
        rng.shuffle(gl)
        ss, tt = selfcons([dict(r, gloss=g) for r, g in zip(clean, gl)])
        sc.append(ss / tt if tt else 0.0)
    sc.sort()
    out.append(f"secondary self-consistency: {s}/{t} = {s / t if t else 0:.3f} over repeated numbers; "
               f"position-shuffled glosses mean {sum(sc) / draws:.3f}, p99 {sc[int(0.99 * draws) - 1]:.3f}")
    return '\n'.join(tab) + '\n', '\n'.join(out) + '\n'


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--pairs', default=os.path.join(HERE, 'pairs.tsv'))
    ap.add_argument('--seed', type=int, default=1411); ap.add_argument('--draws', type=int, default=10000)
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    tab, rep = run(a.pairs, a.seed, a.draws)
    tp, rp = os.path.join(HERE, 'table.tsv'), os.path.join(HERE, 'heldout.txt')
    if a.check:
        stale = [p for p, s in ((tp, tab), (rp, rep)) if not os.path.exists(p) or open(p, encoding='utf-8').read() != s]
        print('stale: ' + ', '.join(stale) if stale else 'check ok')
        sys.exit(1 if stale else 0)
    open(tp, 'w', encoding='utf-8').write(tab); open(rp, 'w', encoding='utf-8').write(rep)
    print(rep, end='')


if __name__ == '__main__':
    main()

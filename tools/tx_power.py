#!/usr/bin/env python3
"""Power audit for the paired sign-test gate on BENCHMARK-TX units and pools (LANE TX-ENGINEER-2 round 0a, 9 Oct 2026).

Why: CLAUDE.md rule 3 -- a baseline already near ceiling has no headroom to show a gain. The first campaign gated 23
instruments on units with 12-15 baseline errors at p < 0.01 on the paired sign test; a sign test at that level needs about
8 fixed with 0 broken, so an instrument that cleanly removed a third of the errors could not pass. This tool says, for
every unit and pool, how often a planted instrument of a stated strength would pass each gate, so the gate is chosen on
power BEFORE any instrument result is seen (benchmark-tx/PREREG-txeng2-0.md).

    python3 tools/tx_power.py --bench BENCHMARK-TX.tsv \
        --unit dev_tune=birago1572-no87:benchmark-tx/txeng/units/labels_dev_tune.tsv \
        --unit spinelli=spinelli-c1519-confirm:benchmark-tx/outputs/spinelli-c1519-confirm/passZ_pipeline.tsv[:LABELMAP.tsv] \
        --pool eval_all=eval_heldout,spinelli [--draws 1000] [--fix 0.3,0.5] [--alpha 0.01,0.05] [--seed 1] [--md OUT.md]
    python3 tools/tx_power.py --errors 15,30,60 ...      # no files: simulate from error counts alone (with --n for N)

A unit is a BENCHMARK-TX item plus one baseline output (today's pipeline on those lines); its baseline errors are the
scored positions tx_bench marks wrong or deleted (tools/tx_bench.position_errors, the same alignment the campaign scores
with). A pool is the union of named units (errors and correct positions add).

Planted instruments (per draw): (1) CLEAN fixer: each baseline error is fixed independently with probability FIX,
nothing is broken; (2) NOISY fixer: the same, plus each correct position is broken with probability base_err x NOISE
(NOISE 0.5 per the lane brief, and 0.1 as a milder column: a real instrument that breaks half as many signs as it finds
wrong is already one nobody would adopt); (3) WORSE: a 30%-worse instrument (breaks 0.3 x E correct positions, fixes
none) -- must FAIL; (4) NO-OP and (5) RANDOM 3% (flips 3% of positions at random: an error becomes right only if the
flip lands on it, a correct sign becomes wrong) -- the negative controls, must pass <= 1% / <= 5% at the gate.
A draw PASSES a gate when fixed > broken and the two-sided exact sign test p < alpha (tx_bench.sign_test).

Output: one row per unit/pool x fix rate: E (baseline errors), N, pass share per (alpha, model). The last table gives the
smallest E at which a clean FIX fixer passes >= 80% of draws at each alpha (the headroom the pool needs). Offline test:
tools/tests/test_tx_power.py. Exit 0; exit 2 on bad input.
"""
import argparse, csv, os, random, sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import tx_bench  # noqa: E402


def load_unit(spec, bench_path):
    """spec: NAME=ITEM:OUTPUT[:LABELMAP] -> (name, {pos: wrong_bool})."""
    name, rest = spec.split('=', 1)
    parts = rest.split(':')
    if len(parts) < 2:
        sys.exit('tx_power: --unit needs NAME=ITEM:OUTPUT.tsv[:LABELMAP.tsv]')
    item, out = parts[0], parts[1]
    lm = tx_bench.load_label_map(parts[2]) if len(parts) > 2 else None
    rows = [r for r in tx_bench.read_tsv(bench_path) if r['item'] == item]
    if not rows:
        sys.exit('tx_power: item %s not in %s' % (item, bench_path))
    truth = tx_bench.read_tsv(rows[0]['truth'])
    outl = tx_bench.load_output([out])
    if lm:
        truth = tx_bench.map_truth(truth, lm)
        outl = {k: [lm.get(s, s) for s in v] for k, v in outl.items()}
    errs = tx_bench.position_errors(truth, outl)
    return name, {(item,) + k: v for k, v in errs.items()}


def simulate(E, N, fix, alphas, draws, rng, noise_levels=(0.5, 0.1), flip=0.03):
    """Return {model: {alpha: pass_share}} for a unit with E errors among N scored positions."""
    base_err = E / N if N else 0.0
    C = N - E
    models = {}
    def passes(f, b):
        return {a: (f > b and tx_bench.sign_test(f, b) < a) for a in alphas}
    cnt = {}
    def tally(key, res):
        d = cnt.setdefault(key, {a: 0 for a in alphas})
        for a in alphas:
            d[a] += res[a]
    for _ in range(draws):
        f = sum(1 for _ in range(E) if rng.random() < fix)
        tally('clean', passes(f, 0))
        for nl in noise_levels:
            b = sum(1 for _ in range(C) if rng.random() < base_err * nl)
            tally('noisy%.1f' % nl, passes(f, b))
        bw = sum(1 for _ in range(C) if rng.random() < (0.3 * E / C if C else 0))
        tally('worse', passes(0, bw))
        tally('noop', passes(0, 0))
        # random 3% flips: each position flipped w.p. flip; an error flipped counts as fixed, a correct one as broken
        rf = sum(1 for _ in range(E) if rng.random() < flip)
        rb = sum(1 for _ in range(C) if rng.random() < flip)
        tally('random3', passes(rf, rb))
    for k, d in cnt.items():
        models[k] = {a: d[a] / draws for a in alphas}
    return models


def min_errors(fix, alpha, draws, rng, target=0.8, N=None, emax=200):
    """Smallest E (N = 10 E unless given) at which a clean fixer passes >= target of draws."""
    for E in range(1, emax + 1):
        n = N or 10 * E
        m = simulate(E, n, fix, [alpha], draws, rng, noise_levels=())
        if m['clean'][alpha] >= target:
            return E
    return None


def fmt_table(rows, alphas, models):
    hdr = ['unit', 'E', 'N', 'fix'] + ['%s@%g' % (m, a) for m in models for a in alphas]
    out = ['| ' + ' | '.join(hdr) + ' |', '|' + '---|' * len(hdr)]
    for r in rows:
        cells = [r['unit'], str(r['E']), str(r['N']), '%.1f' % r['fix']]
        for m in models:
            for a in alphas:
                cells.append('%.3f' % r['res'][m][a])
        out.append('| ' + ' | '.join(cells) + ' |')
    return '\n'.join(out)


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split('\n')[0])
    ap.add_argument('--bench', default='BENCHMARK-TX.tsv')
    ap.add_argument('--unit', action='append', default=[], help='NAME=ITEM:OUTPUT.tsv[:LABELMAP.tsv]')
    ap.add_argument('--pool', action='append', default=[], help='NAME=unit1,unit2,...')
    ap.add_argument('--errors', help='comma list of E to simulate without files (N = --n or 10E)')
    ap.add_argument('--n', type=int, help='N for --errors')
    ap.add_argument('--fix', default='0.3,0.5')
    ap.add_argument('--alpha', default='0.01,0.05')
    ap.add_argument('--draws', type=int, default=1000)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--md', help='write the tables to this markdown file too')
    a = ap.parse_args(argv)
    rng = random.Random(a.seed)
    fixes = [float(x) for x in a.fix.split(',')]
    alphas = [float(x) for x in a.alpha.split(',')]
    units = {}
    for spec in a.unit:
        name, errs = load_unit(spec, a.bench)
        units[name] = errs
    pools = {}
    for spec in a.pool:
        name, members = spec.split('=', 1)
        merged = {}
        for m in members.split(','):
            if m not in units:
                sys.exit('tx_power: pool %s names unknown unit %s' % (name, m))
            merged.update(units[m])
        pools[name] = merged
    targets = []
    for name, errs in list(units.items()) + list(pools.items()):
        targets.append((name, sum(errs.values()), len(errs)))
    if a.errors:
        for e in a.errors.split(','):
            E = int(e)
            targets.append(('E=%d' % E, E, a.n or 10 * E))
    if not targets:
        sys.exit('tx_power: give --unit/--pool or --errors')
    rows = []
    for name, E, N in targets:
        for fix in fixes:
            rows.append(dict(unit=name, E=E, N=N, fix=fix, res=simulate(E, N, fix, alphas, a.draws, rng)))
    models = ['clean', 'noisy0.5', 'noisy0.1', 'worse', 'noop', 'random3']
    text = ['# tx_power: pass share of planted instruments per gate (draws %d, seed %d)' % (a.draws, a.seed),
            'A pass is fixed > broken and two-sided sign test p < alpha. clean: fixes FIX of the errors, breaks none; '
            'noisyK: also breaks correct signs at base_err x K; worse: breaks 0.3E, fixes none; noop; random3: 3% of '
            'positions flipped at random.', '', fmt_table(rows, alphas, models), '',
            '## Smallest E (baseline errors) at which a clean fixer passes >= 80% of draws (N = 10E)']
    hdr = ['fix'] + ['alpha %g' % x for x in alphas]
    text += ['| ' + ' | '.join(hdr) + ' |', '|' + '---|' * len(hdr)]
    for fix in fixes:
        cells = ['%.1f' % fix] + [str(min_errors(fix, al, min(a.draws, 400), rng)) for al in alphas]
        text.append('| ' + ' | '.join(cells) + ' |')
    out = '\n'.join(text)
    print(out)
    if a.md:
        with open(a.md, 'w') as f:
            f.write(out + '\n')
    return 0


if __name__ == '__main__':
    sys.exit(main())

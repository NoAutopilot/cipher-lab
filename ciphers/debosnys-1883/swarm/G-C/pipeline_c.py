#!/usr/bin/env python3
"""DEB-SWARM-C fixed pipeline (29 Sept 2026) -- the one method group C reports, blind, on a control or a real text.

  python3 pipeline_c.py --control FR-SYLL [--fit c1+c2]     reads ONLY swarm/controls/FR-SYLL.tsv
  python3 pipeline_c.py --real c2                           reads ONLY c2 through score.py's own loader
Steps (all choices fixed here, none read from a control's answer):
  1. unit LM: harness FR-SYLL unit rules (17 function words, make_controls.py's syllabifier), top 160 syllables,
     the rest spelled in letters; fr19 prose (4 novels) + Fleurs du Mal x3; unit bigram and trigram.
  2. SEEDS independent runs (parallel): bigram anneal (3M iters x 3 restarts, one sign per unit when --injective 1,
     homophones with the channel term when 0), then a trigram anneal (2M, T0 0.5) seeded by the bigram key.
  3. keep the run with the best trigram score (the model's own criterion; on the 03:26-03:33 runs this order matched
     the recovery order on all six seeds).
  4. combined-objective anneal (unit bigram + char 5-gram information gain, 300k iters) and a first-improvement
     polish to convergence (polish.py).
Writes KEY_<tag>.tsv and a JSON line with every seed's scores. For a control, also runs score.py --control.
"""
import argparse, collections, json, multiprocessing as mp, os, subprocess, sys
HERE = os.path.dirname(os.path.abspath(__file__))
SW = os.path.dirname(HERE)
sys.path.insert(0, HERE); sys.path.insert(0, SW)
import syll, polish

S, W = 160, 17


def load(args):
    if args.control:
        import solve_control as sc
        lines = sc.read_control(args.control)
        parts = args.fit.split('+')
        return [l for ln, l in lines.items() if ln.split('_')[0] in parts]
    import score
    return list(score.load_text(args.real).values())


def flat(lines):
    seq, breaks = [], set()
    for l in lines:
        breaks.add(len(seq)); seq.extend(l)
    return seq, breaks


def one_seed(job):
    lines, seed, inj, it2, it3 = job
    seq, breaks = flat(lines)
    _, lm2 = syll.build_lm(S, W, order=2, func='harness', verse=True)
    _, key = syll.Solver(lm2).run(seq, it2, 3, seed, breaks=breaks, injective=inj, T0=2.0, T1=0.05)
    _, lm3 = syll.build_lm(S, W, order=3, func='harness', verse=True)
    sc3, key = syll.Solver(lm3).run(seq, it3, 1, seed, breaks=breaks, injective=inj, T0=0.5, T1=0.05, init=key)
    return seed, sc3, key


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--control')
    ap.add_argument('--fit', default='c1+c2')
    ap.add_argument('--real', choices=['c1', 'c2'])
    ap.add_argument('--injective', type=int, default=1)
    ap.add_argument('--seeds', type=int, default=8)
    ap.add_argument('--seed0', type=int, default=101)
    ap.add_argument('--it2', type=int, default=3000000)
    ap.add_argument('--it3', type=int, default=2000000)
    ap.add_argument('--canneal', type=int, default=300000)
    ap.add_argument('--procs', type=int, default=4)
    ap.add_argument('--tag', required=True)
    a = ap.parse_args()
    lines = load(a)
    inj = bool(a.injective)
    jobs = [(lines, a.seed0 + i, inj, a.it2, a.it3) for i in range(a.seeds)]
    with mp.Pool(a.procs) as pool:
        res = pool.map(one_seed, jobs)
    res.sort(key=lambda r: -r[1])
    seed, sc3, key = res[0]
    _, lm2 = syll.build_lm(S, W, order=2, func='harness', verse=True)
    _, key = polish.anneal_combined(lines, key, lm2, 1.0, a.canneal, 1.0, 0.05, inj, seed)
    scp, key = polish.polish(lines, key, lm2, 1.0, 20, inj, seed)
    out = os.path.join(HERE, f'KEY_{a.tag}.tsv')
    with open(out, 'w') as f:
        f.write('sign\tvalue\n')
        for s in sorted(key):
            f.write(f'{s}\t{key[s]}\n')
    seq, _ = flat(lines)
    info = dict(tag=a.tag, control=a.control, fit=a.fit if a.control else None, real=a.real, injective=a.injective,
                N=len(seq), K=len(set(seq)), seeds=[[r[0], round(r[1], 1)] for r in res], chosen_seed=seed,
                final_score=round(scp, 1), key=os.path.basename(out))
    print(json.dumps(info), flush=True)
    if a.control:
        r = subprocess.run([sys.executable, os.path.join(SW, 'score.py'), out, '--control', a.control,
                            '--shuffles', '10'], capture_output=True, text=True)
        print(r.stdout[-800:], r.stderr[-800:])


if __name__ == '__main__':
    main()

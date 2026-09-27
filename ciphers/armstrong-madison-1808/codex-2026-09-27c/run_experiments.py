"""Reproduce the recorded diagnostic runs; stage selection is explicit.

Run prepare.py first. Compilation uses only C++17; preparation/evaluation need NumPy.
This is a letter/digraph surrogate, NOT an implementation of historical Annet.
"""
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
import argparse
import json
import random
import subprocess

D = Path(__file__).resolve().parent

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('stage', choices=['initial', 'revised', 'strong', 'validation', 'target'])
    args = ap.parse_args()
    exe = D / 'piece_solve'
    subprocess.run(['g++', '-O3', '-std=c++17', str(D/'piece_solve.cpp'), '-o', str(exe)], check=True)
    (D/'results').mkdir(exist_ok=True)
    if args.stage == 'target':
        results = json.loads((D/'results.json').read_text())
        checked = [r for r in results if r['file'] in ['results/strong4.tsv', 'results/strong5.tsv']]
        assert len(checked) == 2 and all(r['accuracy'] >= .8 for r in checked), 'Fresh controls did not pass'
        seq = list(map(int, (D/'target.seq').read_text().split()))
        vals = [t for t in seq if t >= 0]
        for seed in range(3):
            shuffled = vals.copy()
            random.Random(8100+seed).shuffle(shuffled)
            it = iter(shuffled)
            (D/f'shuffle{seed}.seq').write_text(' '.join(str(next(it)) if t >= 0 else '-1' for t in seq)+'\n')
        def attack(name):
            suffix = 0 if name == 'target' else int(name[-1])+1
            first = f'results/{name}-initial.tsv'
            subprocess.run([str(exe), 'lm.bin', 'pieces.txt', f'{name}.seq', '120', '45000',
                            '0', first, str(202609400+suffix)], cwd=D, check=True)
            subprocess.run([str(exe), 'lm.bin', 'pieces.txt', f'{name}.seq', '1000', '120000',
                            '0', f'results/{name}-strong.tsv', str(202609500+suffix), first], cwd=D, check=True)
        with ThreadPoolExecutor(max_workers=4) as ex:
            list(ex.map(attack, ['target', 'shuffle0', 'shuffle1', 'shuffle2']))
        subprocess.run(['python', str(D/'evaluate.py')], cwd=D, check=True)
        return
    def run(seed, bonus, restarts, iters, output, rng_seed, prior=None):
        cmd = [str(exe), 'lm.bin', 'pieces.txt', f'control{seed}.seq', str(restarts),
               str(iters), str(bonus), f'results/{output}.tsv', str(rng_seed)]
        if prior:
            cmd.append(f'results/{prior}.tsv')
        subprocess.run(cmd, cwd=D, check=True)
    jobs = []
    if args.stage in ['initial', 'revised']:
        bs, r, it = ([1., 1.5, 2.], 80, 30000) if args.stage == 'initial' else ([-.5, 0., .5], 120, 45000)
        for seed in [0, 1, 3]:
            for b in bs:
                jobs.append((seed, b, r, it, f'tune{seed}-b{b:.1f}', 20260927+seed))
    elif args.stage == 'strong':
        for seed in [0, 1, 3]:
            jobs.append((seed, 0, 1000, 120000, f'strong{seed}', 202609280+seed, f'tune{seed}-b0.0'))
    elif args.stage == 'validation':
        for seed in [4, 5]:
            run(seed, 0, 120, 45000, f'tune{seed}-b0.0', 20260927+seed)
            jobs.append((seed, 0, 1000, 120000, f'strong{seed}', 202609280+seed, f'tune{seed}-b0.0'))
    with ThreadPoolExecutor(max_workers=3) as ex:
        list(ex.map(lambda job: run(*job), jobs))
    subprocess.run(['python', str(D/'evaluate.py')], cwd=D, check=True)

if __name__ == '__main__':
    main()

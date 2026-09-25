#!/usr/bin/env python3
"""Runs permutation_test.py's exact statistic and both nulls (same seeds, same n each run) on matched-control
draws (matched_control.py's construction, ciphertext.tsv's 33-run/400-token profile) to show what z a real
word-per-code nomenclature of this design gives the test (CLAUDE.md rule 3: report the target's number next
to the control's). ZX-BAR, 25 Sept 2026. Imports permutation_test.py and matched_control.py directly, so this
is the identical statistic/null code the target's run used, not a reimplementation.

Usage: python3 permutation_control.py [--seeds 10] [--n 1000] [--ctpath ciphertext.tsv]
       python3 permutation_control.py --marked --marked-share 0.59 [--seeds 10]   (ZX-BAR2, 25 Sept 2026:
       code+mark control, matched_control.py's build_control_observations_marked() -- same run/profile
       construction, but each observation is tagged 'code-mark' or 'code-none', with marks carrying real
       meaning per (code, word) pair; --marked-share should be set to key_gloss_marked.tsv's own observed
       marked fraction so the control matches the target's design, not an assumed one.)
"""
import argparse
import random

import matched_control as mc
import permutation_test as pt


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('--seeds', type=int, default=10)
    ap.add_argument('--n', type=int, default=1000)
    ap.add_argument('--ctpath', default='ciphertext.tsv')
    ap.add_argument('--marked', action='store_true', help='use the code+mark control instead of the bare-code one')
    ap.add_argument('--marked-share', type=float, default=0.75, dest='marked_share')
    args = ap.parse_args()

    zas, zbs = [], []
    for seed in range(args.seeds):
        if args.marked:
            obs = mc.build_control_observations_marked(seed, args.ctpath, marked_share=args.marked_share)
        else:
            obs = mc.build_control_observations(seed, args.ctpath)
        real = pt.loo_statistic(obs)
        n_obs = len(obs)

        rng_a = random.Random(0)
        nulls_a = [pt.loo_statistic(pt.null_a_draw(obs, rng_a)) for _ in range(args.n)]
        rng_b = random.Random(1)
        nulls_b = [pt.loo_statistic(pt.null_b_draw(obs, rng_b)) for _ in range(args.n)]

        mean_a, sd_a, z_a, p_a = pt.zscore(real, nulls_a)
        mean_b, sd_b, z_b, p_b = pt.zscore(real, nulls_b)
        zas.append(z_a)
        zbs.append(z_b)
        print(f'control seed {seed}: N={n_obs} real={real} ({100 * real / n_obs:.1f}%) '
              f'zA={z_a:.3f} pA={p_a:.4f} zB={z_b:.3f} pB={p_b:.4f}')

    print(f'\nzA range over {args.seeds} seeds: {min(zas):.3f} to {max(zas):.3f}, mean {sum(zas)/len(zas):.3f}')
    print(f'zB range over {args.seeds} seeds: {min(zbs):.3f} to {max(zbs):.3f}, mean {sum(zbs)/len(zbs):.3f}')


if __name__ == '__main__':
    main()

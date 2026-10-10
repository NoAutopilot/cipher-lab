#!/usr/bin/env python3
"""ORACLE-LOCATION-1 line manifest (PREREG-txeng2-19 OL1-MANIFEST; the review's section 4, PREREG-txeng2-17 candidate).

Samples 12 complete lines per hand (all if fewer, minimum 6) with random.Random(20261010) over each hand's SORTED candidate
list, declared in CANDIDATES below from the BENCHMARK-TX.tsv line ranges. A line is dropped before sampling only when its crop
file is absent on disk (listed under 'excluded'); never by content, error or score. Reads no truth, no output, no key.
Writes manifest.tsv (hand, line, crops) and prints it; the lane commits manifest.tsv with its sha256 before any annotation.
Run from the repo root: python3 benchmark-tx/txeng2/oracle1/make_manifest.py
"""
import glob, os, random, sys
SEED = 20261010
PER_HAND = 12
MINIMUM = 6
CANDIDATES = {
    # hand: (line ids in order, glob pattern with {line})
    'vivonne1573-f102r': ([f'f102r_L{i:02d}' for i in range(1, 38)],
                          'ciphers/fr16104-vivonne-spain-1572/images/c105_{line}_s*.jpg'),
    # REDRAWN 10 Oct 2026 01:2x UTC (TX-RED F67, the orchestrator's decision of 01:1x): no.87's candidates are the dev_tune lines
    # f178v_L01-L12 ONLY (exactly 12, so all enter, no sampling); the first manifest (sha256 d12f6cd9..., 4cc8017d9) drew 7 eval-pool
    # lines (f178v L19/L20/L21/L23, f179r L01/L03, f178r L02) and is superseded before any annotation; eval_heldout and f178r untouched.
    'birago1572-no87': ([f'f178v_L{i:02d}' for i in range(1, 13)],
                        'ciphers/nevers-birago-fr3251-1572/harvest/{folio}/{line}_s*.jpg'),
    'luzerne108a-p1': ([f'p1_L{i:02d}' for i in range(1, 12)],
                       'benchmark-tx/txpool/luzerne108a/crops/{line}.jpg'),
}

def crops_for(hand, line, pattern):
    folio = line.split('_')[0]
    return sorted(glob.glob(pattern.format(line=line, folio=folio)))

def main():
    out = ['hand\tline\tcrops']
    report = []
    for hand, (lines, pattern) in CANDIDATES.items():
        lines = sorted(lines)
        have, excluded = [], []
        for ln in lines:
            c = crops_for(hand, ln, pattern)
            (have if c else excluded).append((ln, c))
        if len(have) < MINIMUM:
            print(f'{hand}: only {len(have)} lines with crops, under the minimum {MINIMUM}: feasibility-only', file=sys.stderr)
        rng = random.Random(SEED)
        chosen = sorted(rng.sample(have, PER_HAND)) if len(have) > PER_HAND else have
        for ln, c in chosen:
            out.append(f'{hand}\t{ln}\t{";".join(c)}')
        report.append(f'{hand}: candidates {len(lines)}, with crops {len(have)}, excluded (no crop) {len(excluded)}'
                      f'{" [" + ",".join(l for l, _ in excluded) + "]" if excluded else ""}, selected {len(chosen)}')
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, 'manifest.tsv'), 'w', encoding='utf-8') as f:
        f.write('\n'.join(out) + '\n')
    print('\n'.join(report)); print('\n'.join(out))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""MONLUC-2 (7 Oct 2026): is f.86's 'K07' two signs? Control for split_c172.tsv.

  python3 split_check.py [--labels blind|reader] [--draws 10000] [--seed 1] [--check]

Input: split_c172.tsv (shape group per K07 instance: 'blind' = a Sonnet sorter shown only the shuffled native crops,
'reader' = MONLUC-2 by eye, not blind to the gloss), ciphertext_c172.tsv (gloss letter each token faces, check_cells.py).
1. Association control: statistic = (#group-A instances facing t) + (#group-B instances facing g), over instances that
   face a gloss letter and have a group; null = the same labels permuted over those instances (--draws).
2. Held-out-line gain gate (check_cells.py's procedure): group-A tokens relabelled K69 (starting at the table value g); corrections
   learned on two lines (K69 gets a value only if check_cells' 'contradict' rule fires on the training lines), scored
   on the third against the same corrections on shuffled held-out tokens.
Writes results_split_c172.json; --check exits 1 if stale (rule 7).
"""
import argparse, json, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from score_c172 import norm, load_key  # noqa: E402
from check_cells import load_lines, tok_letters, align_tb, cell_table, corrections  # noqa: E402


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--labels', default='blind', choices=['blind', 'reader'])
    ap.add_argument('--draws', type=int, default=10000)
    ap.add_argument('--seed', type=int, default=1)
    ap.add_argument('--gloss', default='gloss_c172_withline1.txt')
    ap.add_argument('--check', action='store_true')
    a = ap.parse_args()
    rows = [l.split('\t') for l in (HERE / 'split_c172.tsv').read_text().splitlines() if l and not l.startswith(('#', 'line'))]
    col = 7 if a.labels == 'blind' else 6
    grp = {(r[0], int(r[1])): ('A' if r[col] in ('A', 'hook') else 'B' if r[col] in ('B', 'plain') else '?') for r in rows}
    faced = {}
    for l in (HERE / 'ciphertext_c172.tsv').read_text().splitlines()[1:]:
        f = l.split('\t')
        faced[(f[0], int(f[1]))] = f[7] if len(f) > 7 else ''
    inst = [(k, grp[k], faced.get(k, '')) for k in sorted(grp)]
    use = [(g, f) for k, g, f in inst if g in 'AB' and f]
    stat = lambda labs: sum(1 for g, (_, f) in zip(labs, use) if (g == 'A' and f == 't') or (g == 'B' and f == 'g'))
    labs = [g for g, _ in use]
    obs = stat(labs)
    rng = random.Random(a.seed)
    ge = 0
    for _ in range(a.draws):
        p = labs[:]
        rng.shuffle(p)
        ge += stat(p) >= obs
    by = {g: ''.join(sorted(f for gg, f in use if gg == g)) for g in 'AB'}

    key = load_key()
    key['K69'] = key['K07']  # starts as the table's g; only a learned correction changes it
    lines = load_lines()
    for L in lines:
        lines[L] = ['K69' if t == 'K07' and grp.get((L, i), 'B') == 'A' else t
                    for i, t in enumerate(lines[L], 1)]
    gloss = norm((HERE / a.gloss).read_text().split('\n#', 1)[0])
    p95 = lambda v: sorted(v)[int(0.95 * len(v)) - 1]
    held = {}
    for L in sorted(lines):
        train = [t for K in sorted(lines) if K != L for t in lines[K]]
        _, ftr = align_tb(tok_letters(train, key), gloss)
        rows_tr = cell_table(train, ftr, key)
        corr = {c: v for c, v in corrections(rows_tr).items() if c in ('K07', 'K69')}
        key2 = dict(key); key2.update(corr)
        test = lines[L]
        base, _ = align_tb(tok_letters(test, key), gloss)
        new, _ = align_tb(tok_letters(test, key2), gloss)
        gains = []
        for _ in range(200):
            t = test[:]
            rng.shuffle(t)
            gains.append(align_tb(tok_letters(t, key2), gloss)[0] - align_tb(tok_letters(t, key), gloss)[0])
        held[L] = dict(K69_train=rows_tr.get('K69', {}).get('faced', ''), K07_train=rows_tr['K07']['faced'],
                       corrections=corr, base=base, corrected=new, gain=new - base,
                       shuffle_gain_mean=round(sum(gains) / len(gains), 2), shuffle_gain_p95=p95(gains),
                       passes=(new - base) > p95(gains))
    toks = [t for L in sorted(lines) for t in lines[L]]
    allrows = cell_table(toks, align_tb(tok_letters(toks, key), gloss)[1], key)
    res = dict(labels=a.labels, instances=len(inst), used=len(use), faced_by_group=by, statistic=obs,
               perm_p=round((ge + 1) / (a.draws + 1), 4), draws=a.draws, seed=a.seed,
               all_lines={c: allrows[c] for c in ('K07', 'K69')}, held_out=held,
               gate_passed_lines=sum(h['passes'] for h in held.values()))
    js = json.dumps(res, indent=1) + '\n'
    out = HERE / ('results_split_c172.json' if a.labels == 'blind' else 'results_split_c172_reader.json')
    if a.check:
        ok = out.exists() and out.read_text() == js
        print(('OK ' if ok else 'STALE ') + out.name)
        sys.exit(0 if ok else 1)
    out.write_text(js)
    print(js)


if __name__ == '__main__':
    main()

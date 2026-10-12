#!/usr/bin/env python3
"""TXE4-6 unit 5 (PREREG-txeng4-6 Arms / Endpoint / Gate). Two phases, so every file is hashed and committed before a score:
  python3 benchmark-tx/txeng4/6/run_eval.py build   # controls (a) 20 permuted-label seeds, (b) 20 coin seeds at T's own
                                                    # applied rows, per item; eval-line restrictions of T, R, base and
                                                    # controls for no.87 (eval_heldout = f178r L01-03, f178v L13-23,
                                                    # f179r L01-03); appends SHA256SUMS.prescore. No truth opened.
  python3 benchmark-tx/txeng4/6/run_eval.py score   # tx_bench --exclude-flagged --paired <base> --strict per item, both
                                                    # masks; paired position fixed/broken for T and every control; pooled
                                                    # sign test; control (a) p95 of net; gate verdict -> eval.json/eval.txt
t frozen at 0 by dev_sweep.py, so T == R (the replacement arm); both are reported."""
import csv, json, os, subprocess, sys
sys.path.insert(0, 'tools')
import tx_bench as TB
O = 'benchmark-tx/txeng4/6'
A = 'ciphers/nevers-birago-fr3251-1572/atlas'
ITEMS = {
    'no87': dict(id='birago1572-no87', base='benchmark-tx/outputs/birago1572-no87/passC.tsv',
                 eval_lines={f'f178r_L{i:02d}' for i in (1, 2, 3)} | {f'f178v_L{i:02d}' for i in range(13, 24)} | {f'f179r_L{i:02d}' for i in (1, 2, 3)},
                 dev_lines={f'f178v_L{i:02d}' for i in range(1, 13)}),
    'f152r': dict(id='birago1572-f152r', base='benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv', eval_lines=None, dev_lines=None),
}
SEEDS = range(1, 21)
rd = lambda p: list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def restrict(src, dst, lines):
    rows = [r for r in rd(src) if r['line'] in lines]
    with open(dst, 'w') as f:
        f.write('line\tpos\tsign\n')
        for r in rows:
            f.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\n")


def tb(item, out, mode):
    args = ['python3', 'tools/tx_tiebreak.py', '--atlas', A, '--map', f'{O}/map_{item}.tsv', '--tiles', f'{O}/tiles_{item}.tsv',
            '--rec', f'{O}/rec_{item}', '--base', ITEMS[item]['base'], '--out', out, '--margin', '0'] + mode
    r = subprocess.run(args, capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr)
    return r.stdout.strip().splitlines()[-1]


def build():
    os.makedirs(f'{O}/out/ctrl', exist_ok=True)
    files = []
    for item in ITEMS:
        for s in SEEDS:
            pa = f'{O}/out/ctrl/{item}_perm{s}.tsv'; print(tb(item, pa, ['--permute-seed', str(s)])); files += [pa]
            pc = f'{O}/out/ctrl/{item}_coin{s}.tsv'; print(tb(item, pc, ['--coin-seed', str(s), '--coin-from', f'{O}/out/{item}_R.decisions.tsv'])); files += [pc]
    # eval-line and dev-line restrictions for no.87 (scored with --coverage-diagnostic on those lines only)
    for tag, lines in (('eval', ITEMS['no87']['eval_lines']), ('dev', ITEMS['no87']['dev_lines'])):
        restrict(ITEMS['no87']['base'], f'{O}/out/no87_base_{tag}.tsv', lines)
        restrict(f'{O}/out/no87_R.tsv', f'{O}/out/no87_R_{tag}.tsv', lines)
        files += [f'{O}/out/no87_base_{tag}.tsv', f'{O}/out/no87_R_{tag}.tsv']
        for s in SEEDS:
            for k in ('perm', 'coin'):
                restrict(f'{O}/out/ctrl/no87_{k}{s}.tsv', f'{O}/out/ctrl/no87_{k}{s}_{tag}.tsv', lines); files.append(f'{O}/out/ctrl/no87_{k}{s}_{tag}.tsv')
    with open(f'{O}/SHA256SUMS.prescore', 'a') as f:
        for p in files:
            f.write(subprocess.run(['sha256sum', p], capture_output=True, text=True).stdout.replace(O + '/', ''))
    print(len(files), 'control / restricted files hashed into SHA256SUMS.prescore')


def score_one(out, base, item_id, extra=()):
    r = subprocess.run(['python3', 'tools/tx_bench.py', out, '--bench', 'BENCHMARK-TX.tsv', '--item', item_id, '--exclude-flagged',
                        '--paired', base, '--strict', '--json'] + list(extra), capture_output=True, text=True)
    if r.returncode:
        sys.exit(r.stderr + r.stdout)
    return json.loads(r.stdout)


def score():
    res = {}
    text = []
    for item, tag, out, base, extra in (
            ('no87', 'eval_heldout', f'{O}/out/no87_R_eval.tsv', f'{O}/out/no87_base_eval.tsv', ['--coverage-diagnostic']),
            ('no87', 'dev_tune (safety, beside)', f'{O}/out/no87_R_dev.tsv', f'{O}/out/no87_base_dev.tsv', ['--coverage-diagnostic']),
            ('no87', 'whole item', f'{O}/out/no87_R.tsv', ITEMS['no87']['base'], []),
            ('f152r', 'f152r', f'{O}/out/f152r_R.tsv', ITEMS['f152r']['base'], [])):
        j = score_one(out, base, ITEMS[item]['id'], extra)
        res[f'{item}:{tag}'] = j
        # controls
        if tag in ('eval_heldout', 'f152r'):
            suf = '_eval' if item == 'no87' else ''
            ctrl = {}
            for k in ('perm', 'coin'):
                ctrl[k] = []
                for s in SEEDS:
                    jj = score_one(f'{O}/out/ctrl/{item}_{k}{s}{suf}.tsv', base, ITEMS[item]['id'], extra)
                    ctrl[k].append(jj)
            res[f'{item}:{tag}:controls'] = ctrl
        text.append(f'== {item} {tag}: ' + subprocess.run(['python3', 'tools/tx_bench.py', out, '--bench', 'BENCHMARK-TX.tsv', '--item', ITEMS[item]['id'],
                    '--exclude-flagged', '--paired', base, '--strict'] + extra, capture_output=True, text=True).stdout)
    json.dump(res, open(f'{O}/eval.json', 'w'), indent=1)
    open(f'{O}/eval_tx_bench.txt', 'w').write('\n'.join(text))
    print('\n'.join(text))


if __name__ == '__main__':
    {'build': build, 'score': score}[sys.argv[1]]()

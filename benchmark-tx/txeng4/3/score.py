#!/usr/bin/env python3
"""TXE4-3 ATLAS-NCA scorer (12 Oct 2026, account 3): the only step that opens truth, through tools/tx_bench.py (and, for
the top-3 miss, atlas/score_no87.py --map <temp no87_map.py --compat copy>, never committed). Every output is scored once;
the raw tx_bench text and JSON are kept under scores/. Wilson 95% intervals computed here from errors/scored.

  dev     score out/dev_grid_*.tsv (f178v L01-12) -> scores/dev.tsv; choose by flagged-excluded err_true, ties on
          as-measured, then the smaller dim -> frozen.json
  eval    score out/eval_*.tsv and out/f152r_*.tsv, paired A2 vs A1 (and A4 vs A1), top-3 miss for A2/A1/A4/A0 ->
          scores/eval.tsv, scores/eval.json
Run from the repo root."""
import csv, os, sys, json, subprocess, math, glob, re, tempfile
W = 'benchmark-tx/txeng4/3'; O = f'{W}/out'; S = f'{W}/scores'; os.makedirs(S, exist_ok=True)
A = 'ciphers/nevers-birago-fr3251-1572/atlas'


def wilson(k, n, z=1.96):
    if not n:
        return (float('nan'), float('nan'))
    p = k / n; d = 1 + z * z / n; c = p + z * z / (2 * n); h = z * math.sqrt(p * (1 - p) / n + z * z / (4 * n * n))
    return ((c - h) / d, (c + h) / d)


def bench(out, item, paired=None, tag=None):
    cmd = [sys.executable, 'tools/tx_bench.py', '--bench', 'BENCHMARK-TX.tsv', '--item', item, '--exclude-flagged',
           '--coverage-diagnostic', '--strict', out] + (['--paired', paired] if paired else [])
    tag = tag or os.path.basename(out)[:-4]
    txt = subprocess.run(cmd, capture_output=True, text=True)
    open(f'{S}/{tag}.txt', 'w').write(txt.stdout + txt.stderr)
    js = subprocess.run(cmd + ['--json'], capture_output=True, text=True).stdout
    open(f'{S}/{tag}.json', 'w').write(js)
    try:
        rep = json.loads(js)
    except Exception:
        rep = None
    recs = rep if isinstance(rep, list) else (rep.get('items') or rep.get('report') or [rep]) if isinstance(rep, dict) else []
    rec = next((r for r in recs if isinstance(r, dict) and r.get('item') == item and (r.get('output') or '').startswith(os.path.basename(out)[:-4])), None) \
        or next((r for r in recs if isinstance(r, dict) and r.get('item') == item), None)
    row = dict(tag=tag)
    for key in ('as_measured', 'flagged_excluded'):
        d = (rec or {}) if key == 'as_measured' else ((rec or {}).get(key) or {})
        if d:
            lo, hi = wilson(d['errors'], d['scored'])
            row.update({f'{key}_err': d['err_true'], f'{key}_k': d['errors'], f'{key}_n': d['scored'],
                        f'{key}_wilson': f'{lo:.3f}-{hi:.3f}', f'{key}_SDI': f"{d['ser_S']}/{d['ser_D']}/{d['ser_I']}",
                        f'{key}_strict': (d.get('strict') or {}).get('err_true')})
    # paired figures from the text (fixed/broken, p): keep the lines verbatim
    pl = [l for l in txt.stdout.splitlines() if l.startswith('paired ') or 'fixed' in l]
    row['paired'] = ' || '.join(pl)[:600]
    return row, txt.stdout


def dev():
    rows = []
    for out in sorted(glob.glob(f'{O}/dev_grid_*.tsv')):
        m = re.search(r'dev_grid_(\w+?)_d(\d+)_k(\d+)', out)
        row, _ = bench(out, 'birago1572-no87')
        row.update(features='hog+zone+topo' if m.group(1) == 'hogzonetopo' else 'hog', dim=int(m.group(2)), k=int(m.group(3)))
        rows.append(row); print(row['tag'], row.get('as_measured_err'), row.get('flagged_excluded_err'), flush=True)
    cols = ['tag', 'features', 'dim', 'k', 'flagged_excluded_err', 'flagged_excluded_k', 'flagged_excluded_n', 'flagged_excluded_wilson',
            'as_measured_err', 'as_measured_k', 'as_measured_n', 'as_measured_wilson', 'as_measured_SDI', 'as_measured_strict']
    with open(f'{S}/dev.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows:
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')
    best = sorted(rows, key=lambda r: (r['flagged_excluded_err'], r['as_measured_err'], r['dim']))[0]
    fz = dict(features=best['features'], dim=best['dim'], k=best['k'], dev_flagged_excluded=best['flagged_excluded_err'],
              dev_as_measured=best['as_measured_err'], rule='min flagged-excluded err_true; ties as measured, then smaller dim')
    json.dump(fz, open(f'{W}/frozen.json', 'w'), indent=1); print('FROZEN', fz)


def eval_():
    rows = {}
    for out in sorted(glob.glob(f'{O}/eval_*.tsv')):
        tag = os.path.basename(out)[5:-4]
        paired = f'{O}/eval_A1.tsv' if tag in ('A2', 'A4', 'A5', 'A0', 'A0p') else None
        row, _ = bench(out, 'birago1572-no87', paired, f'eval_{tag}'); rows[f'eval_{tag}'] = row
        print(f'eval_{tag}', row.get('as_measured_err'), row.get('flagged_excluded_err'), flush=True)
    for out in sorted(glob.glob(f'{O}/f152r_*.tsv')):
        tag = os.path.basename(out)[6:-4]
        row, _ = bench(out, 'birago1572-f152r', None, f'f152r_{tag}'); rows[f'f152r_{tag}'] = row
        print(f'f152r_{tag}', row.get('as_measured_err'), row.get('flagged_excluded_err'), flush=True)
    cols = ['tag', 'as_measured_err', 'as_measured_k', 'as_measured_n', 'as_measured_wilson', 'as_measured_SDI', 'as_measured_strict',
            'flagged_excluded_err', 'flagged_excluded_k', 'flagged_excluded_n', 'flagged_excluded_wilson', 'flagged_excluded_SDI', 'paired']
    with open(f'{S}/eval.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for t, r in rows.items():
            f.write('\t'.join(str(r.get(c, '')) for c in cols) + '\n')
    json.dump(rows, open(f'{S}/eval.json', 'w'), indent=1)
    # top-3 miss through score_no87.py --map <temp compat copy> (scorer join only; never committed)
    d = tempfile.mkdtemp(); mp = os.path.join(d, 'compat.tsv')
    subprocess.run([sys.executable, f'{A}/no87_map.py', '--compat', mp], capture_output=True, text=True)
    top3 = {}
    for tag in ('A0', 'A0p', 'A1', 'A2', 'A4', 'A5'):
        tk = f'{W}/runs/{tag}.tsv'
        if tag == 'A4':
            # assemble the leave-one-line-out runs' rows for the eval boxes
            rs = []
            for p in sorted(glob.glob(f'{W}/runs/A4_f17*.tsv')):
                line = os.path.basename(p)[3:-4]; page, li = line.split('_L')
                rs += [r for r in csv.DictReader(open(p), delimiter='\t') if r['page'] == page and int(r['line']) == int(li)]
            tk = os.path.join(d, 'A4.tsv')
            with open(tk, 'w') as f:
                w = csv.DictWriter(f, fieldnames=list(rs[0].keys()), delimiter='\t'); w.writeheader(); w.writerows(rs)
        if not os.path.exists(tk):
            continue
        r = subprocess.run([sys.executable, f'{A}/score_no87.py', tk, '--map', mp], capture_output=True, text=True)
        top3[tag] = r.stdout.strip(); print(tag, r.stdout.strip().replace('\n', ' | '))
    json.dump(top3, open(f'{S}/top3.json', 'w'), indent=1)


if __name__ == '__main__':
    {'dev': dev, 'eval': eval_}[sys.argv[1]]()

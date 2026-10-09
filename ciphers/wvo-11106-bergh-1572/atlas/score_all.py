#!/usr/bin/env python3
"""BERGH-ALL1/ALL2: merge two blind sign-GROUP passes on whole-line strips (atlas/strips_grp.py --line) into atlas/group_sign.tsv.

  python3 atlas/score_all.py --job BERGH-ALL1 A1.tsv A2.tsv -- B1.tsv B2.tsv [--check]

Pass files: strip, boxes ('3+4'), labels ('y' | 'd 4' | 'FRAG' | 'OTHERLINE'), note -- the BERGH-GRP reader format
(PREREG-BERGH-GRP.md). Same reconciliation rule as BERGH-GRP (atlas/score_groups.py): a box is `agreed` iff both passes put it
in the same group (same set of numbers) with the same normalized labels (trailing '?' dropped, FRAG and OTHERLINE one class);
otherwise `split`; no arbitration. Key: atlas/strips_all/key.tsv. Nothing here gates (the instrument's gate was BERGH-GRP's
18/19); reported: coverage, A/B agreement, groups of >= 2 boxes, label splits, reader-flagged boxes ('?' or a note), and the
consistency of this job's agreed boxes with BERGH-GRP's agreed boxes where both read the same box.
Writes this job's rows (job column) into atlas/group_sign.tsv, keeping every other job's rows; --check exits 1 if stale.
"""
import collections, csv, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from score_groups import HEAD, norm, job_rows, merge  # noqa: E402


def load(paths):
    m, bad = {}, []
    for p in paths:
        with open(p) as f:
            for r in csv.DictReader(f, delimiter='\t'):
                nums = frozenset(x.strip() for x in (r['boxes'] or '').split('+') if x.strip())
                for n in nums:
                    if (r['strip'], n) in m:
                        bad.append((r['strip'], n))
                    m[(r['strip'], n)] = (nums, norm(r['labels'] or ''), (r['labels'] or '').strip(), (r.get('note') or '').strip())
    return m, bad


def main():
    argv = sys.argv[1:]
    job = argv[argv.index('--job') + 1]
    files = [x for i, x in enumerate(argv) if not x.startswith('--') and argv[i - 1] != '--job']
    cut = argv.index('--')
    fa = [x for x in files if argv.index(x) < cut]; fb = [x for x in files if argv.index(x) > cut]
    (A, dA), (B, dB) = load(fa), load(fb)
    with open(os.path.join(HERE, 'strips_all', 'key.tsv')) as f:
        key = list(csv.DictReader(f, delimiter='\t'))
    rows, agree, multi, miss, flag = [], 0, 0, 0, []
    kinds, labsplit = collections.Counter(), collections.Counter()
    for k in key:
        s, n, sid = k['strip'], k['num'], k['sid']
        a, b = A.get((s, n)), B.get((s, n))
        miss += (a is None) + (b is None)
        same = a is not None and b is not None and a[0] == b[0] and a[1] == b[1]
        agree += same
        if same:
            multi += len(a[0]) >= 2
            kinds['frag' if all(x == 'FRAG' for x in a[1]) else 'one' if len(a[1]) == 1 else 'multi'] += 1
        elif a is not None and b is not None:
            if a[0] == b[0]:
                kinds['split_label'] += 1; labsplit['/'.join(sorted([' '.join(a[1]), ' '.join(b[1])]))] += 1
            else:
                kinds['split_group'] += 1
        for p, g in (('A', a), ('B', b)):
            if g and ('?' in g[2] or g[3]):
                flag.append(f'{sid} {s}/{n} {p}: {g[2]}' + (f' ({g[3]})' if g[3] else ''))
        ga = '+'.join(sorted(a[0], key=int)) if a else ''
        gb = '+'.join(sorted(b[0], key=int)) if b else ''
        rows.append([sid, s, n, ga, a[2] if a else '', gb, b[2] if b else '', ' '.join(a[1]) if same else '',
                     'agreed' if same else 'split', job])
    path = os.path.join(HERE, 'group_sign.tsv')
    lines = ['\t'.join(r) + '\n' for r in rows]
    if '--check' in argv:
        ok = os.path.exists(path) and open(path).readline() == HEAD and job_rows(path, job)[0] == lines
        print('group_sign.tsv', job, 'current' if ok else 'STALE'); sys.exit(0 if ok else 1)
    nk = len(key)
    print(f'{job}: {nk} numbered boxes; missing answers A+B {miss}; duplicate numbers A {len(dA)} B {len(dB)}')
    print(f'A/B agreement (same group and labels): {agree}/{nk} = {agree / nk:.3f}; agreed in groups of >= 2 boxes: {multi}/{agree}')
    print('agreed one sign / two+ signs / FRAG-OTHERLINE:', kinds['one'], '/', kinds['multi'], '/', kinds['frag'],
          '; splits same group label differs / group differs:', kinds['split_label'], '/', kinds['split_group'])
    print('commonest label splits:', ', '.join(f'{k} {v}' for k, v in labsplit.most_common(12)))
    # consistency with BERGH-GRP where both agreed on the same box
    grp = {}
    for ln in job_rows(path, 'BERGH-GRP')[0]:
        f = ln.rstrip('\n').split('\t')
        if f[8] == 'agreed':
            grp.setdefault(f[0], set()).add(f[7])
    both = [(r[0], r[7]) for r in rows if r[8] == 'agreed' and r[0] in grp]
    same_lab = sum(1 for sid, lab in both if lab in grp[sid])
    print(f'boxes agreed in both {job} and BERGH-GRP: {len(both)}; same label: {same_lab}')
    for sid, lab in both:
        if lab not in grp[sid]:
            print(f'  differs: {sid} {job}={lab} BERGH-GRP={"|".join(sorted(grp[sid]))}')
    with open(os.path.join(HERE, 'strips_all', f'{job}_flags.txt'), 'w') as f:
        f.write(''.join(x + '\n' for x in flag))
    print(f'reader-flagged answers (? or note): {len(flag)} -> atlas/strips_all/{job}_flags.txt')
    merge(path, job, lines, False); print('wrote', path)


if __name__ == '__main__':
    main()

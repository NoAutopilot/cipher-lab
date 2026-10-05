#!/usr/bin/env python3
"""N9-BAL3 (PREREG-N9BAL3.md): N9-BAL2's fit_holdout procedure with anchors. Anchors {label: letter} are (i) passed to
tools/interlinear_align.py as --prior (first EM iteration) and (ii) fixed in the decode key. Null 1 shuffles all key values (anchored
included) within class; null 2 shuffles F1's letters. Everything else is n9bal2/fit_holdout.py unchanged.
  python3 anch.py ANCHORS.tsv TRANSCRIPTION.tsv [...]   (ANCHORS.tsv: label<TAB>letter; '#' lines ignored)
"""
import csv, os, random, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(D))
sys.path.insert(0, os.path.join(D, 'n9bal2'))
import fit_holdout as FH
from fit_holdout import load, F1, F2, CANDS, RUN2, T_of, cls

def fit_key(run2, anchors):
    ids, back, raw = {}, {}, []
    for i, t in enumerate(run2):
        if t == '?': t = f'?{i}'
        if t not in ids: ids[t] = f't{len(ids)}'; back[ids[t]] = t
        raw.append('@' + ids[t])
    with tempfile.TemporaryDirectory() as td:
        p, pr = os.path.join(td, 'p.tsv'), os.path.join(td, 'prior.tsv')
        with open(p, 'w') as f:
            f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\nR2\t%s\tR2\t%s\n' % (F2, ' '.join(raw)))
        with open(pr, 'w') as f:
            f.write('code\tmeaning\n' + ''.join(f'{ids[t]}\t{v}\n' for t, v in anchors.items() if t in ids))
        cmd = [sys.executable, os.path.join(ROOT, 'tools/interlinear_align.py'), 'align', p, os.path.join(td, 'a.tsv'),
               os.path.join(td, 'k.tsv'), '--code-prefix', '@', '--code-chunk', '3', '--seg-bonus', '0', '--len-prior', '0.5']
        if any(t in ids for t in anchors): cmd += ['--prior', pr]
        subprocess.run(cmd, check=True, capture_output=True)
        al = list(csv.DictReader(open(os.path.join(td, 'a.tsv')), delimiter='\t'))
    chunks = defaultdict(list)
    for r in al: chunks[back[r['raw'][1:]]].append(r['plain_chunk'])
    key = {t: Counter(c).most_common(1)[0][0] for t, c in chunks.items() if not t.startswith('?')}
    key.update(anchors)
    return key, chunks

def nulls(cands, key, frag, draws, seed=1):
    rng = random.Random(seed); n1, n2 = [], []
    groups = defaultdict(list)
    for t in key: groups[cls(t)].append(t)
    for _ in range(draws):
        k2 = {}
        for g, ts in groups.items():
            vs = [key[t] for t in ts]; rng.shuffle(vs); k2.update(zip(ts, vs))
        n1.append(T_of(cands, k2, frag)[0])
        fl = list(frag); rng.shuffle(fl); n2.append(T_of(cands, key, ''.join(fl))[0])
    p99 = lambda xs: sorted(xs)[int(0.99 * len(xs))]
    return sum(n1) / len(n1), p99(n1), sum(n2) / len(n2), p99(n2)

def run(rows, anchors, draws=1000):
    run2 = [t for r in RUN2 for k, t in rows.get(r, []) if k == 'cipher']
    key, chunks = fit_key(run2, anchors)
    cands = {n: [x for r in rs for x in rows.get(r, [])] for n, rs in CANDS.items()}
    T, where, per = T_of(cands, key, F1)
    m1, p1, m2, p2 = nulls(cands, key, F1, draws)
    den = per[where][1] if where else 0
    ok = T > p1 and T > p2 and den >= 10
    return dict(T=T, where=where, per=per, m1=m1, p1=p1, m2=m2, p2=p2, verdict='PASS' if ok else 'FAIL', nkey=len(key), nrun2=len(run2),
                nanch_run2=sum(1 for t in anchors if t in run2), nanch=len(anchors))

def load_anchors(path):
    return {r[0]: r[1] for r in csv.reader(open(path), delimiter='\t') if len(r) >= 2 and not r[0].startswith('#') and r[0] != 'label'}

def main():
    a = load_anchors(sys.argv[1])
    for path in sys.argv[2:]:
        r = run(load(path), a)
        per = '; '.join(f'{n} {x}/{y}' for n, (x, y) in r['per'].items())
        print(f"{os.path.basename(path)}: anchors {r['nanch']} ({r['nanch_run2']} in run 2); run2 {r['nrun2']} tokens, key {r['nkey']}; "
              f"T = {r['T']:.3f} at {r['where']} [{per}]; null1 mean {r['m1']:.3f} p99 {r['p1']:.3f}; null2 mean {r['m2']:.3f} p99 {r['p2']:.3f} -> {r['verdict']}")
if __name__ == '__main__': main()

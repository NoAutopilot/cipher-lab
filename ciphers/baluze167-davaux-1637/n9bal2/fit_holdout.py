#!/usr/bin/env python3
"""N9-BAL2 (PREREG-N9BAL2.md, pushed before any pass was scored): fit the f.246-248 hand's signs on Tomokiyo's F2 (c511 run 2) with
tools/interlinear_align.py, hold out F1, score F1 against every other bare run of the letter decoded with the F2-fitted key.
  python3 fit_holdout.py TRANSCRIPTION.tsv [...]   (tsv: 'row<TAB>tokens'; rows R510a-c, R1, R2a-b, R3a-b, R4, R5a-b; {clear words})
  python3 fit_holdout.py --show TRANSCRIPTION.tsv   (also print the fitted key and the F2 alignment)
T = max agreement of F1 over the candidate passages (c510, r1, r3, r4, r5), >= 10 compared F1 letters. Null 1: fitted values shuffled
within class (s: signs vs numerals) among run-2 tokens; null 2: F1's letters shuffled. 1000 draws each, seed 1, same max per draw.
Gate: PASS iff T > both p99 and >= 10 letters compared. No key.tsv value is used anywhere.
"""
import csv, os, random, re, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); D = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(D))
sys.path.insert(0, os.path.join(D, 'n8bal'))
from score_f247 import norm, fit, FRAGS
F1, F2 = norm(FRAGS[0]), norm(FRAGS[1])
CANDS = {'c510': ['R510a', 'R510b', 'R510c'], 'r1': ['R1'], 'r3': ['R3a', 'R3b'], 'r4': ['R4'], 'r5': ['R5a', 'R5b']}
RUN2 = ['R2a', 'R2b']

def load(path):
    rows = {}
    for r in csv.reader(open(path), delimiter='\t'):
        if len(r) < 2 or r[0] in ('row', 'line') or r[0].startswith('#'): continue
        toks = []
        for m in re.finditer(r'\{([^}]*)\}|(\S+)', r[1]):
            toks.append(('clear', m.group(1)) if m.group(1) is not None else ('cipher', m.group(2)))
        rows[r[0]] = toks
    return rows

def cls(t): return 's' if t.startswith('s:') else 'n'

def fit_key(run2):
    """run2: list of cipher tokens. Returns {token: chunk}, per-token chunk list, alignment rows."""
    ids, back, raw = {}, {}, []
    for i, t in enumerate(run2):
        if t == '?': t = f'?{i}'
        if t not in ids: ids[t] = f't{len(ids)}'; back[ids[t]] = t
        raw.append('@' + ids[t])
    with tempfile.TemporaryDirectory() as td:
        p = os.path.join(td, 'p.tsv')
        with open(p, 'w') as f:
            f.write('plain_line\tplain_raw\tcipher_line\tcipher_raw\nR2\t%s\tR2\t%s\n' % (F2, ' '.join(raw)))
        subprocess.run([sys.executable, os.path.join(ROOT, 'tools/interlinear_align.py'), 'align', p, os.path.join(td, 'a.tsv'),
                        os.path.join(td, 'k.tsv'), '--code-prefix', '@', '--code-chunk', '3', '--seg-bonus', '0', '--len-prior', '0.5'],
                       check=True, capture_output=True)
        al = list(csv.DictReader(open(os.path.join(td, 'a.tsv')), delimiter='\t'))
    chunks = defaultdict(list); rows = []
    for r in al:
        t = back[r['raw'][1:]]; chunks[t].append(r['plain_chunk']); rows.append((t, r['plain_chunk']))
    key = {t: Counter(c).most_common(1)[0][0] for t, c in chunks.items() if not t.startswith('?')}
    return key, chunks, rows

def passage(toks, key):
    s, flag = [], []
    for kind, t in toks:
        if kind == 'clear':
            for c in norm(t): s.append(c); flag.append(1)
        else:
            v = key.get(t, '#') if t != '?' else '#'
            for c in v: s.append(c); flag.append(0)
    return s, flag

def T_of(cands, key, frag):
    best, where = 0.0, None; per = {}
    for name, toks in cands.items():
        ok, den = fit(frag, *passage(toks, key))
        per[name] = (ok, den)
        if den >= 10 and ok / den > best: best, where = ok / den, name
    return best, where, per

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

def run(rows, draws=1000, show=False):
    run2 = [t for r in RUN2 for k, t in rows.get(r, []) if k == 'cipher']
    key, chunks, al = fit_key(run2)
    cands = {n: [x for r in rs for x in rows.get(r, [])] for n, rs in CANDS.items()}
    T, where, per = T_of(cands, key, F1)
    m1, p1, m2, p2 = nulls(cands, key, F1, draws)
    nC = sum(1 for t, c in chunks.items() if not t.startswith('?') and len(c) >= 2 and len(set(c)) == 1)
    if show:
        print('F2 alignment:', ' '.join(f'{t}={c or "-"}' for t, c in al))
        print('fitted tokens', len(key), '; C (>=2 occurrences, same chunk):', nC,
              [f'{t}={chunks[t][0]}' for t in key if len(chunks[t]) >= 2 and len(set(chunks[t])) == 1])
        for n in cands: print(' ', n, ''.join(passage(cands[n], key)[0]), per[n])
    den = per[where][1] if where else 0
    ok = T > p1 and T > p2 and den >= 10
    return dict(T=T, where=where, per=per, m1=m1, p1=p1, m2=m2, p2=p2, verdict='PASS' if ok else 'FAIL', nC=nC, nkey=len(key), nrun2=len(run2))

def main():
    args = sys.argv[1:]; show = '--show' in args; args = [a for a in args if a != '--show']
    for path in args:
        r = run(load(path), show=show)
        per = '; '.join(f'{n} {a}/{b}' for n, (a, b) in r['per'].items())
        print(f"{os.path.basename(path)}: run2 {r['nrun2']} tokens, {r['nkey']} fitted ({r['nC']} at C); T = {r['T']:.3f} at {r['where']} "
              f"[{per}]; null1 shuffled-key mean {r['m1']:.3f} p99 {r['p1']:.3f}; null2 F1-letter-shuffle mean {r['m2']:.3f} p99 {r['p2']:.3f} "
              f"-> {r['verdict']}")
if __name__ == '__main__': main()

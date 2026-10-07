#!/usr/bin/env python3
"""THU-1 (7 Oct 2026): gate G2 and key extension from Birch-printed glossed siblings.

For every sibling pairs file (verbatim OCR pairs; M3/M4 hand-cut from short inline runs, see NOTES.md):
  1. align with NO prior (tools/interlinear_align.py align) and score the current key against the sibling's
     own gloss vs 200 shuffled keys (thu1/g2_gate.py) -> thu1/g2_result.tsv
  2. for G2 PASS letters only, re-align with the current key as --prior and fold every code the current key
     lacks into key_montagu_extended2.tsv / key_fauconberg_extended.tsv (grade C: printed gloss; a code seen
     once with an OCR-word-boundary chunk is still C but n=1), with the attesting letter;
  3. FAIL letters: codes absent from the key whose in-letter alignment status is 'agrees' or 'single-segment' (a chunk
     bounded by OCR word breaks on both sides) are listed, held,
     in thu1/held_codes.tsv (grade M, NOT merged).
--check: regenerate in memory and exit 1 if any committed output differs.
"""
import csv, io, os, subprocess, sys, tempfile
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(F)); TOOL = os.path.join(ROOT, 'tools', 'interlinear_align.py')
sys.path.insert(0, HERE)
import g2_gate as g

LETTERS = [  # id, pairs file, key, attribution
    ('M3', 'montagu_1656-03-02_vol4_pairs.tsv', 'key_montagu_extended.tsv', 'Mountagu to Thurloe, Naseby in Stokes Bay, 2 Mar 1655/6, Birch vol.4 pp.570-571 (djvu l.51364-51438)'),
    ('M4', 'montagu_1656-04-05_vol4_pairs.tsv', 'key_montagu_extended.tsv', 'Mountagu to Thurloe, Naseby off Lisbon, 5 Apr 1656, Birch vol.4 (djvu l.60600-60608)'),
    ('M1', 'montagu_1656-05-19_vol1_pairs.tsv', 'key_montagu_extended.tsv', 'Mountagu to Thurloe, Naseby in Cales Bay, 19 May 1656, Birch vol.1 (djvu l.62335-62563)'),
    ('M5', 'montagu_1656-07-03_vol5_pairs.tsv', 'key_montagu_extended.tsv', 'Mountagu to Thurloe, 3 July 1656, Birch vol.5 (djvu l.15466-15865)'),
    ('M2', 'montagu_1656-09-11_vol1_pairs.tsv', 'key_montagu_extended.tsv', 'Mountagu to Thurloe, Naseby in Lisbon bay, 11 Sept 1656, Birch vol.1 (djvu l.62564-62798)'),
    ('F1', 'fauconberg_1658-09_vol7_l36328_pairs.tsv', 'key_fauconberg.tsv', 'Fauconberg to H. Cromwell, [Sept 1658], Birch vol.7 (djvu l.36328-36727)'),
]
OUT = {'key_montagu_extended.tsv': 'key_montagu_extended2.tsv', 'key_fauconberg.tsv': 'key_fauconberg_extended.tsv'}

def align(pairs, tmp, prior=None):
    a, k = os.path.join(tmp, 'a.tsv'), os.path.join(tmp, 'k.tsv')
    cmd = [sys.executable, TOOL, 'align', os.path.join(F, pairs), a, k] + (['--prior', os.path.join(F, prior)] if prior else [])
    subprocess.run(cmd, check=True, capture_output=True)
    return list(csv.DictReader(open(a), delimiter='\t'))

def run():
    outs = {}
    g2 = ['letter\tpairs\tkey\tscored\tall_num_tokens\tagree\treal\tshuffle_mean\tshuffle_p95\tverdict']
    new = {k: {} for k in OUT}; held = ['letter\tvalue\tchunk\tn_agrees\tgrade\tnote']
    conflicts = ['letter\tvalue\tkey_meaning\tsibling_chunk\tstatus']
    with tempfile.TemporaryDirectory() as tmp:
        for lid, pairs, key, attr in LETTERS:
            kk = g.load_key(os.path.join(F, key)); rows = align(pairs, tmp)
            toks = [(r['value'], g.norm(r['plain_chunk'])) for r in rows if r['kind'] == 'num' and r['value'] and g.norm(r['plain_chunk'])]
            a, n, real = g.score(kk, toks)
            import random
            rng = random.Random(1656); vals, means = list(kk), list(kk.values()); d = []
            for _ in range(200):
                m = means[:]; rng.shuffle(m); d.append(g.score(dict(zip(vals, m)), toks)[2])
            d.sort(); mean = sum(d) / len(d); p95 = d[int(0.95 * len(d)) - 1]
            ok = n >= 5 and real >= 0.70 and real > p95
            g2.append(f'{lid}\t{pairs}\t{key}\t{n}\t{len(toks)}\t{a}\t{real:.3f}\t{mean:.3f}\t{p95:.3f}\t{"PASS" if ok else "FAIL"}')
            if ok:
                for r in align(pairs, tmp, prior=key):
                    v, c = r['value'], g.norm(r['plain_chunk'])
                    if r['kind'] != 'num' or not v or not c:
                        continue
                    if v in kk:
                        if kk[v] != c:
                            conflicts.append(f'{lid}\t{v}\t{kk[v]}\t{c}\t{r["status"]}')
                        continue
                    e = new[key].setdefault(v, {}); e.setdefault(c, []).append(lid)
            else:
                agg = {}
                for r in rows:
                    v, c = r['value'], g.norm(r['plain_chunk'])
                    if r['kind'] == 'num' and v and c and v not in kk and r['status'].split(':')[0] in ('agrees', 'single-segment'):
                        agg[(v, c)] = agg.get((v, c), 0) + 1
                for (v, c), k2 in sorted(agg.items(), key=lambda x: int(x[0][0])):
                    held.append(f'{lid}\t{v}\t{c}\t{k2}\tM\tG2 FAIL letter; printed-gloss chunk, letter not gated; not merged')
    outs['thu1/g2_result.tsv'] = '\n'.join(g2) + '\n'
    outs['thu1/held_codes.tsv'] = '\n'.join(held) + '\n'
    outs['thu1/conflicts.tsv'] = '\n'.join(conflicts) + '\n'
    attr = {l[0]: l[3] for l in LETTERS}
    for key, okey in OUT.items():
        base = open(os.path.join(F, key)).read().rstrip('\n').split('\n')
        lines = [f'# {okey}: {key} unchanged (all rows below the marker are verbatim), plus codes absent from it attested in',
                 '# G2-PASS Birch siblings (THU-1, 7 Oct 2026; regenerate: python3 thu1/extend.py; --check).'] + base
        lines.append('# --- THU-1 additions: value, meaning, n, grade, attested_by (C = read from the printed gloss)')
        for v in sorted(new[key], key=int):
            for c, ls in sorted(new[key][v].items(), key=lambda x: -len(x[1])):
                grade = 'C' if len(new[key][v]) == 1 else 'M'
                lines.append(f'#+\t{v}\t{c}\t{len(ls)}\t{grade}\t' + '; '.join(sorted({attr[x] for x in ls})))
        outs[okey] = '\n'.join(lines) + '\n'
    return outs

def main():
    outs = run(); stale = []
    for p, txt in outs.items():
        fp = os.path.join(F, p)
        if '--check' in sys.argv:
            if not os.path.exists(fp) or open(fp).read() != txt:
                stale.append(p)
        else:
            open(fp, 'w').write(txt)
    if stale:
        print('STALE:', ', '.join(stale)); sys.exit(1)
    print('ok' if '--check' in sys.argv else 'written: ' + ', '.join(outs))

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""N9-XM (5 Oct 2026): per-pair nulls for key_crossmatch leads, per research/PREREG-N9-XM.md.
Uses tools/key_crossmatch.py's own loaders and statistic (imported). Usage: python3 research/n9xm/xmatch_pair_null.py [--n 200]"""
import sys, json, random, argparse, statistics
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / 'tools'))
import key_crossmatch as kx
import judge_plaintext as jp

LEADS = [
    ('a', 'ciphers/fr3993-villeroy-1595/keys/key_f200_no57_syll.tsv', 'ciphers/sanguszkow-mniszech-dunin-1714/ciphertext.tsv', 4.12),
    ('b', 'ciphers/hellen-frederick-1752/key_r4370/key_decode.tsv', 'ciphers/sanguszkow-mniszech-dunin-1714/ciphertext.tsv', 3.63),
    ('c', 'ciphers/clair1161-avis-flandre-1688/two/key_shuf4_s1.tsv', 'ciphers/decode-1168-modena-costabili-1492/ciphertext.tsv', 3.95),
    ('d', 'ciphers/clair1161-avis-flandre-1688/pool/key_shuf3_s1.tsv', 'ciphers/decode-1168-modena-costabili-1492/ciphertext.tsv', 3.85),
]
GATE = 3.292


def S(key, signs, model):
    st = kx.pair_stats(key, signs, model, n_shuffle=20, seed=0)['own']
    return st['stat'], st['z_ng'], st['z_vf']


def random_key(key, rnd):
    alph = sorted({r['value'] for r in key.values()})
    return {c: {'value': rnd.choice(alph)} for c in key}


def p99(xs):
    xs = sorted(x for x in xs if x is not None)
    return xs[min(len(xs) - 1, int(0.99 * len(xs)))] if xs else None


def main():
    ap = argparse.ArgumentParser(); ap.add_argument('--n', type=int, default=200); a = ap.parse_args()
    by_lang = kx.reading_files_by_lang(); corpora = kx.build_repo_corpora()
    rows, dump = [], {}
    for lab, kp, cp, nightly in LEADS:
        key, meta = kx.load_key_meta(ROOT / kp)
        lang, _ = kx.language_for(meta['folder'], meta['lang_hint'], by_lang)
        c = kx.load_ct_meta(ROOT / cp); signs = c['signs']
        model = kx.get_model(lang, exclude_folder=c['folder'], corpora_map=corpora)
        cov = kx.coverage_of(key, signs)
        s0, zng0, zvf0 = S(key, signs, model)
        nulls = {'N1': [], 'N1c': [], 'N2': [], 'N3': [], 'N3_zng': [], 'N3_zvf': []}
        for i in range(1, a.n + 1):
            r = random.Random(i)
            nulls['N1'].append(S(kx.shuffled_key(key, r), signs, model)[0])
            nulls['N1c'].append(S(kx.shuffled_key_by_class(key, r), signs, model)[0])
            nulls['N2'].append(S(random_key(key, r), signs, model)[0])
            sg = signs[:]; r.shuffle(sg)
            s3, z3n, z3v = S(key, sg, model)
            nulls['N3'].append(s3); nulls['N3_zng'].append(z3n); nulls['N3_zvf'].append(z3v)
        def fr(xs): xs = [x for x in xs if x is not None]; return round(sum(x >= GATE for x in xs) / len(xs), 3)
        row = dict(lead=lab, key=kp, ct=cp, lang=lang, n_tokens=len(signs), coverage=round(cov, 3), nightly=nightly,
                   S=round(s0, 3), z_ng=round(zng0, 3) if zng0 is not None else None, z_vf=round(zvf0, 3) if zvf0 is not None else None)
        for k in ('N1', 'N1c', 'N2', 'N3', 'N3_zng', 'N3_zvf'):
            row[f'p99_{k}'] = round(p99(nulls[k]), 3)
        for k in ('N1', 'N1c', 'N2'):
            row[f'frac_ge_gate_{k}'] = fr(nulls[k])
        row['survives'] = s0 > row['p99_N1'] and s0 > row['p99_N1c']
        rows.append(row); dump[lab] = nulls
        print(json.dumps(row), flush=True)
    out = ROOT / 'research/n9xm'
    cols = list(rows[0])
    with open(out / 'results.tsv', 'w') as f:
        f.write('\t'.join(cols) + '\n')
        for r in rows: f.write('\t'.join(str(r[k]) for k in cols) + '\n')
    json.dump(dump, open(out / 'nulls.json', 'w'))
    # pooled N1c per ciphertext (miscalibration test)
    for cp in sorted({r['ct'] for r in rows}):
        pool = [x for r in rows if r['ct'] == cp for x in dump[r['lead']]['N1c'] if x is not None]
        print(f'POOLED N1c {cp}: {sum(x >= GATE for x in pool)}/{len(pool)} = {sum(x >= GATE for x in pool)/len(pool):.3f} reach gate {GATE}')

if __name__ == '__main__':
    main()

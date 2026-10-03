#!/usr/bin/env python3
"""DIN-PRINT (3 Oct 2026): align the f.128r cipher to the 1882 print of the same letter (Revue de Champagne et de Brie
XII p.340) with tools/interlinear_align.py, under the settings pre-registered in PREREG.md.

    python3 ciphers/fr3621-dinteville-1592/f128/print_align/align_print.py [--check]

Inputs: ../gloss_pairs.tsv (cipher signs per glossed segment, unchanged), print_pairs.tsv (print_norm / gloss_norm, one
convention). Outputs: key_print.tsv, align_print.tsv (primary, syl settings = key_syl's), key_print_letter.tsv (secondary,
letter mode), control_print.tsv (rotation + shuffle controls for print and, for reference, gloss_norm), diff_vs_key_syl.tsv,
result.json. --check exits 1 if any committed output differs from a fresh run (rule 7).
"""
import csv, io, json, os, random, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(os.path.join(HERE, '..', '..', '..', '..'))
sys.path.insert(0, os.path.join(ROOT, 'tools'))
import interlinear_align as ia  # noqa: E402

ia.FOLD_FS = False
SEED, NSHUF = 20261003, 1000


def rd(p):
    with open(p, encoding='utf-8') as f:
        return list(csv.DictReader(f, delimiter='\t'))


SIGNS = {}
for r in rd(os.path.join(HERE, '..', 'gloss_pairs.tsv')):
    g = r['gloss'].strip()
    if g and not g.startswith('CLEAR:') and r['signs'].strip():
        SIGNS['%s.%s' % (r['line'], r['order'])] = r['signs'].split()
PP = rd(os.path.join(HERE, 'print_pairs.tsv'))


def pairs_for(texts, mode):
    codes, out = {}, []
    for r, t in zip(PP, texts):
        sg = SIGNS[r['cipher_line']]
        if mode == 'syl':
            raw = ' '.join(str(codes.setdefault(s, 100 + len(codes))) for s in sg)
        else:
            raw = ' '.join('@' + s for s in sg)
        out.append({'plain_line': r['cipher_line'][:3], 'plain_raw': t, 'cipher_line': r['cipher_line'], 'cipher_raw': raw})
    inv = {str(c): s for s, c in codes.items()}
    return out, inv


def run(texts, mode):
    pairs, inv = pairs_for(texts, mode)
    if mode == 'syl':
        res = ia.run_align(pairs, floor=100, null_cost=-1.0, max_chunk=3, seg_bonus=0.0, len_prior=1.0)
    else:
        res = ia.run_align(pairs, code_prefix='@', null_cost=0.0)
    name = (lambda v: inv.get(str(v), str(v))) if mode == 'syl' else (lambda v: v)
    return res, name


def consistency(counts, name):
    tot = top = 0
    for v, cnt in counts.items():
        if name(v) == '?':
            continue
        n = sum(cnt.values())
        if n >= 2:
            tot += n; top += max(cnt.values())
    return (top / tot if tot else 0.0), tot


def nulls(texts):
    words = [t.split() for t in texts]
    cat = ''.join(''.join(ws) for ws in words)

    def resplit(s):
        out, pos = [], 0
        for ws in words:
            o = []
            for w in ws:
                o.append(s[pos:pos + len(w)]); pos += len(w)
            out.append(' '.join(o))
        return out
    rots = [resplit(cat[k:] + cat[:k]) for k in range(1, len(cat))]
    rnd = random.Random(SEED); shuf = []
    for _ in range(NSHUF):
        l = list(cat); rnd.shuffle(l); shuf.append(resplit(''.join(l)))
    return rots, shuf


def summ(real, xs):
    xs = sorted(xs)
    return {'real': round(real, 3), 'n': len(xs), 'mean': round(sum(xs) / len(xs), 3),
            'p95': round(xs[int(0.95 * (len(xs) - 1))], 3), 'max': round(xs[-1], 3), 'ge_real': sum(1 for x in xs if x >= real)}


def key_tsv(counts, name):
    o = io.StringIO(); w = csv.writer(o, delimiter='\t', lineterminator='\n')
    w.writerow(['sign', 'meaning', 'n', 'agree', 'others'])
    rows = {}
    for v in sorted(counts, key=lambda v: name(v)):
        cnt = counts[v]; top, topn = ia.top_of(cnt)
        rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:]
        w.writerow([name(v), top, sum(cnt.values()), topn, ','.join('%s:%d' % kv for kv in rest)])
        rows[name(v)] = (top, sum(cnt.values()), topn)
    return o.getvalue(), rows


def outputs():
    P = [r['print_norm'] for r in PP]; G = [r['gloss_norm'] for r in PP]
    result, files = {}, {}
    rots_p, shuf_p = nulls(P); rots_g, shuf_g = nulls(G)
    ctl = io.StringIO(); cw = csv.writer(ctl, delimiter='\t', lineterminator='\n')
    cw.writerow(['text', 'mode', 'control', 'real', 'real_n_occ', 'n', 'null_mean', 'null_p95', 'null_max', 'null_ge_real', 'gate_pass'])
    keys = {}
    for label, T, rots, shuf in (('print', P, rots_p, shuf_p), ('gloss_norm', G, rots_g, shuf_g)):
        for mode in ('syl', 'letter'):
            (prep, results, counts, shown), name = run(T, mode)
            real, nocc = consistency(counts, name)
            r_rot = summ(real, [consistency(run(t, mode)[0][2], name)[0] for t in rots])
            r_sh = summ(real, [consistency(run(t, mode)[0][2], name)[0] for t in shuf])
            gate = real > r_rot['max'] and real > r_sh['p95']
            for cname, s in (('rotation', r_rot), ('shuffle', r_sh)):
                cw.writerow([label, mode, cname, s['real'], nocc, s['n'], s['mean'], s['p95'], s['max'], s['ge_real'], gate])
            result['%s_%s' % (label, mode)] = {'real': round(real, 3), 'occ': nocc, 'rotation': r_rot, 'shuffle': r_sh, 'gate_pass': gate}
            keys[(label, mode)] = (prep, results, counts, shown, name)
    files['control_print.tsv'] = ctl.getvalue()
    # primary key + alignment
    prep, results, counts, shown, name = keys[('print', 'syl')]
    files['key_print.tsv'], kp = key_tsv(counts, name)
    files['key_print_letter.tsv'], _ = key_tsv(keys[('print', 'letter')][2], keys[('print', 'letter')][4])
    al = io.StringIO(); w = csv.writer(al, delimiter='\t', lineterminator='\n')
    w.writerow(['cipher_line', 'idx', 'sign', 'plain_chunk', 'status'])
    for cl, idx, raw, kind, value, repair, chunk, status in ia.token_rows(prep, results, counts, shown):
        w.writerow([cl, idx, name(value) if value != '' else value, chunk, status])
    files['align_print.tsv'] = al.getvalue()
    # diff vs key_syl
    ks = {r['sign']: (r['meaning'], int(r['n']), int(r['agree'])) for r in rd(os.path.join(HERE, '..', 'key_syl.tsv'))}
    d = io.StringIO(); w = csv.writer(d, delimiter='\t', lineterminator='\n')
    w.writerow(['sign', 'key_syl', 'key_syl_support', 'key_print', 'key_print_support', 'change'])
    ch = Counter()
    for s in sorted(set(ks) | set(kp)):
        a = ks.get(s); b = kp.get(s)
        c = 'added' if a is None else 'dropped' if b is None else ('same' if a[0] == b[0] else 'changed')
        ch[c] += 1
        w.writerow([s, a[0] if a else '', '%d/%d' % (a[2], a[1]) if a else '', b[0] if b else '',
                    '%d/%d' % (b[2], b[1]) if b else '', c])
    files['diff_vs_key_syl.tsv'] = d.getvalue()
    result['rows_vs_key_syl'] = dict(ch)
    files['result.json'] = json.dumps(result, indent=1, sort_keys=True) + '\n'
    return files


def main():
    files = outputs()
    if '--check' in sys.argv:
        bad = [n for n, t in files.items() if not os.path.exists(os.path.join(HERE, n)) or open(os.path.join(HERE, n), encoding='utf-8').read() != t]
        print(files['result.json'])
        print('check: STALE %s' % bad if bad else 'check: committed outputs match')
        sys.exit(1 if bad else 0)
    for n, t in files.items():
        with open(os.path.join(HERE, n), 'w', encoding='utf-8') as f:
            f.write(t)
    print(files['result.json'])


if __name__ == '__main__':
    main()

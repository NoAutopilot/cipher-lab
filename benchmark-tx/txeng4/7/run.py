#!/usr/bin/env python3
"""TXE4-7 PILE-LM harness (account 3, 12 Oct 2026; benchmark-tx/PREREG-txeng4-7.md). Read-free, no network.

    python3 benchmark-tx/txeng4/7/run.py build    # real arm, 20 shuffled-key arms, 20 shuffled-cluster arms, dev positive and
                                                  # look-alike controls -> out/ ; NO truth read
    python3 benchmark-tx/txeng4/7/run.py score    # after out/ is committed with SHA256SUMS.prescore: tx_bench per unit and
                                                  # arm, both masks, Wilson, pooled gate, d/s set-aside -> score/

Inputs (fixed, PREREG): bases passC (no.87 f178v L01-23 + f179r L01-03) and passZ_pipeline (f152r); other passes A/B of
each item; key harvest/key_1572_sheet.tsv; LM it16dip; confusion_1572.tsv; maps map/map_no87.tsv and map/map_f152r.tsv
(join_check PASS sidecars, every line pass); clusters atlas/clusters.tsv. Tool: tools/key_decode_lattice.py pile-relabel
(the pile_relabel / build_piles API, one LM load for every run)."""
import csv, hashlib, json, os, random, statistics, subprocess, sys, time
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
os.chdir(ROOT)
sys.path.insert(0, str(ROOT / 'tools'))
import key_decode_lattice as K  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402

F = ROOT / 'ciphers/nevers-birago-fr3251-1572'
OUT = HERE / 'out'; SC = HERE / 'score'
DEV = ['f178v_L%02d' % i for i in range(1, 13)]
EVAL = ['f178v_L%02d' % i for i in range(13, 24)] + ['f179r_L%02d' % i for i in range(1, 4)]
F152 = ['f152r_L%02d' % i for i in range(1, 5)]
DS6 = {('f178v_L13', 20), ('f178v_L15', 9), ('f178v_L19', 6), ('f178v_L19', 24), ('f178v_L21', 1), ('f178v_L23', 21)}  # TXE3-10 d/s fixes (T98->T18)
N_ARMS, N_SHUF, N_POS = 20, 20, 20
ITEMS = {
    'no87': dict(base='benchmark-tx/outputs/birago1572-no87/passC.tsv', alts=['benchmark-tx/outputs/birago1572-no87/passA.tsv',
                 'benchmark-tx/outputs/birago1572-no87/passB.tsv'], map=str(HERE / 'map/map_no87.tsv'), lines=DEV + EVAL,
                 units={'dev_tune': DEV, 'eval_heldout': EVAL}, bench='birago1572-no87'),
    'f152r': dict(base='benchmark-tx/outputs/birago1572-f152r/passZ_pipeline.tsv', alts=['benchmark-tx/outputs/birago1572-f152r/passA.tsv',
                  'benchmark-tx/outputs/birago1572-f152r/passB.tsv'], map=str(HERE / 'map/map_f152r.tsv'), lines=F152,
                  units={'f152r': F152}, bench='birago1572-f152r'),
}


def sha(p):
    return hashlib.sha256(open(p, 'rb').read()).hexdigest()


def write_read(p, reading, lines=None, ds=False):
    with open(p, 'w') as f:
        f.write('line\tpos\tsign\n')
        for ln, rows in reading.items():
            if lines is not None and ln not in lines:
                continue
            for pos, s in rows:
                if ds and (ln, pos) in DS6:
                    s = 'T18'
                f.write(f'{ln}\t{pos}\t{s}\n')


def restrict(reading, lines):
    return {ln: list(rows) for ln, rows in reading.items() if ln in lines}


def load_lm():
    return K.LM(NgramModel([read_corpus(p) for p in LANG_CORPORA['it16dip']]))


def build():
    OUT.mkdir(exist_ok=True)
    lm = load_lm(); key = K.read_key(F / 'harvest/key_1572_sheet.tsv'); nb = K.read_confusion(F / 'harvest/confusion_1572.tsv')
    clusters = K.read_clusters(F / 'atlas/clusters.tsv')
    log = {'time_utc': time.strftime('%Y-%m-%d %H:%M UTC', time.gmtime()), 'items': {}}
    for it, cfg in ITEMS.items():
        t0 = time.time()
        base = restrict(K.read_reading(cfg['base']), set(cfg['lines']))
        pos_of = K.read_map_1to1(cfg['map'])
        alts = K.alt_signs(base, cfg['alts'])
        piles = K.build_piles(base, pos_of, clusters, set(cfg['lines']))
        rec = {'mapped_positions': sum(len(v) for v in piles.values()), 'piles': len(piles),
               'piles_ge2': sum(len(v) >= 2 for v in piles.values()), 'arms': {}}
        # --- real arm
        out, rows, st, changed = K.pile_relabel(base, piles, key, lm, nb, alts, N_SHUF, 1, 2)
        rec['real'] = st; rec['real_changed'] = [dict(line=ln, pos=pos, base=sg, to=c) for ln, pos, sg, c in changed]
        write_read(OUT / f'real_{it}.tsv', out)
        with open(OUT / f'real_{it}.piles.tsv', 'w') as f:
            cols = ['cluster', 'sign', 'n', 'cand', 'delta', 'null_max', 'null_mean', 'accept', 'chosen', 'lines']
            f.write('\t'.join(cols) + '\n')
            for r in rows:
                f.write('\t'.join(str(r[c]) for c in cols) + '\n')
        for u, lines in cfg['units'].items():
            write_read(OUT / f'base_{it}_{u}.tsv', base, set(lines))
            write_read(OUT / f'real_{it}_{u}.tsv', out, set(lines))
            if u == 'eval_heldout':
                write_read(OUT / f'base_{it}_{u}_ds.tsv', base, set(lines), ds=True)
                write_read(OUT / f'real_{it}_{u}_ds.tsv', out, set(lines), ds=True)
        # --- shuffled-key arm: shuffled key i as if real, its nulls at seeds 100i+1..
        for i in range(1, N_ARMS + 1):
            k2 = K.shuffled(key, random.Random(i))
            o2, _, s2, ch2 = K.pile_relabel(base, piles, k2, lm, nb, alts, N_SHUF, 100 * i + 1, 2)
            rec['arms'][f'keyshuf_{i}'] = {'accepted': s2['accepted'], 'positions_changed': s2['positions_changed']}
            for u, lines in cfg['units'].items():
                if u == 'dev_tune':
                    continue
                write_read(OUT / f'keyshuf_{i}_{it}_{u}.tsv', o2, set(lines))
                if u == 'eval_heldout':
                    write_read(OUT / f'keyshuf_{i}_{it}_{u}_ds.tsv', o2, set(lines), ds=True)
        # --- shuffled-cluster arm: cluster ids permuted within each read sign, real key
        for s in range(1, N_ARMS + 1):
            ps = K.build_piles(base, pos_of, clusters, set(cfg['lines']), cluster_shuffle=s)
            o3, _, s3, ch3 = K.pile_relabel(base, ps, key, lm, nb, alts, N_SHUF, 1, 2)
            rec['arms'][f'clshuf_{s}'] = {'accepted': s3['accepted'], 'positions_changed': s3['positions_changed']}
            for u, lines in cfg['units'].items():
                if u == 'dev_tune':
                    continue
                write_read(OUT / f'clshuf_{s}_{it}_{u}.tsv', o3, set(lines))
                if u == 'eval_heldout':
                    write_read(OUT / f'clshuf_{s}_{it}_{u}_ds.tsv', o3, set(lines), ds=True)
        rec['seconds'] = round(time.time() - t0, 1)
        log['items'][it] = rec
        print(f'{it}: {rec["mapped_positions"]} mapped positions, {rec["piles"]} piles ({rec["piles_ge2"]} with >= 2), real accepted '
              f'{st["accepted"]} piles / {st["positions_changed"]} positions; {rec["seconds"]} s', flush=True)
    # --- dev controls (no.87 dev_tune lines only)
    cfg = ITEMS['no87']
    base_all = restrict(K.read_reading(cfg['base']), set(cfg['lines']))
    base_dev = restrict(base_all, set(DEV)); pos_of = K.read_map_1to1(cfg['map'])
    piles_dev = K.build_piles(base_dev, pos_of, clusters, set(DEV))
    def top_nb(sg):
        near = sorted(nb.get(sg, {}).items(), key=lambda kv: (-kv[1], kv[0]))
        return [b for b, _ in near if b in key and b != sg]
    cands = sorted((k for k, v in piles_dev.items() if len(v) >= 3 and top_nb(k[1])), key=lambda k: (k[1], str(k[0])))
    pos_runs = []
    for seed in range(1, N_POS + 1):
        rnd = random.Random(seed)
        cl, sg = rnd.choice(cands); new = top_nb(sg)[0]
        b2 = {ln: [(p, new if (ln, p) in set(piles_dev[(cl, sg)]) else s) for p, s in rows] for ln, rows in base_dev.items()}
        p2 = dict(piles_dev); p2[(cl, new)] = p2.pop((cl, sg))
        a2 = K.alt_signs(b2, cfg['alts'])
        o, rows, st, ch = K.pile_relabel(b2, p2, key, lm, nb, a2, N_SHUF, 1, 2)
        acc = next((a for a in st['accepted_list'] if a['cluster'] == cl and a['sign'] == new), None)
        restored = bool(acc and (acc['to'] == sg or key.get(acc['to']) == key.get(sg)))
        pos_runs.append(dict(seed=seed, cluster=cl, sign=sg, planted=new, n=len(p2[(cl, new)]), accepted_to=acc['to'] if acc else None,
                             restored=restored, false_accepts=st['accepted'] - (1 if acc else 0)))
        print(f'positive {seed}: pile ({cl},{sg}) n={len(p2[(cl, new)])} -> {new}: accepted_to={acc["to"] if acc else None} restored={restored} '
              f'false={st["accepted"] - (1 if acc else 0)}', flush=True)
    P = dict(restored=sum(r['restored'] for r in pos_runs), false_mean=statistics.mean(r['false_accepts'] for r in pos_runs), runs=pos_runs)
    P['gate_P'] = P['restored'] >= 12 and P['false_mean'] <= 1.0
    log['positive_control'] = P
    # --- look-alike control: each (p, c) the real arm accepted with a dev position -> plant a random non-neighbour key sign
    real_acc = [a for a in log['items']['no87']['real']['accepted_list']]
    la_runs = []
    piles_all = K.build_piles(base_all, pos_of, clusters, set(cfg['lines']))
    targets = [(a['cluster'], a['sign'], a['to']) for a in real_acc if any(ln in DEV for ln, _ in piles_all[(a['cluster'], a['sign'])])]
    source = 'real dev acceptances'
    if not targets:
        source = 'positive-control piles (no real dev acceptance; declared fallback)'
        targets = [(r['cluster'], r['sign'], None) for r in pos_runs]
    for n, (cl, sg, c) in enumerate(targets, 1):
        rnd = random.Random(1000 + n)
        bad = set(top_nb(sg)[:3]) | {sg, c}
        r = rnd.choice(sorted(s for s in key if s not in bad))
        dev_pos = [(ln, p) for ln, p in piles_all[(cl, sg)] if ln in DEV] if (cl, sg) in piles_all else piles_dev.get((cl, sg), [])
        if not dev_pos:
            continue
        b2 = {ln: [(p, r if (ln, p) in set(dev_pos) else s) for p, s in rows] for ln, rows in base_dev.items()}
        p2 = {k: v for k, v in piles_dev.items() if k != (cl, sg)}; p2[(cl, r)] = dev_pos
        a2 = K.alt_signs(b2, cfg['alts'])
        o, rows, st, ch = K.pile_relabel(b2, p2, key, lm, nb, a2, N_SHUF, 1, 2, exclude_for={(cl, r): [sg]})
        acc = next((a for a in st['accepted_list'] if a['cluster'] == cl and a['sign'] == r), None)
        la_runs.append(dict(cluster=cl, sign=sg, real_to=c, planted=r, n=len(dev_pos), accepted_to=acc['to'] if acc else None, accepted=bool(acc)))
        print(f'look-alike {n}: pile ({cl},{sg}) -> {r} (orig excluded): accepted_to={acc["to"] if acc else None}', flush=True)
    LA = dict(source=source, runs=la_runs, n=len(la_runs), accepted=sum(r['accepted'] for r in la_runs))
    LA['rate'] = LA['accepted'] / LA['n'] if LA['n'] else None
    LA['gate'] = LA['rate'] is not None and LA['rate'] <= 0.05
    log['lookalike_control'] = LA
    json.dump(log, open(OUT / 'build.json', 'w'), indent=1)
    with open(HERE / 'SHA256SUMS.prescore', 'w') as f:
        for p in sorted(OUT.iterdir()):
            f.write(f'{sha(p)}  out/{p.name}\n')
    print(f'positive control: restored {P["restored"]}/20, false accepts mean {P["false_mean"]:.2f}, gate P {"PASS" if P["gate_P"] else "FAIL"}')
    print(f'look-alike control ({source}): accepted {LA["accepted"]}/{LA["n"]} = {LA["rate"]}, gate {"PASS" if LA["gate"] else "FAIL"}')


def score():
    import tx_bench
    SC.mkdir(exist_ok=True)
    bench = {r['item']: r for r in tx_bench.read_tsv('BENCHMARK-TX.tsv')}
    truth = {it: tx_bench.read_tsv(bench[cfg['bench']]['truth']) for it, cfg in ITEMS.items()}
    def one(it, base_p, out_p, strict=False):
        tr = truth[it]
        bl, ol = tx_bench.load_output([str(base_p)]), tx_bench.load_output([str(out_p)])
        res = {}
        for mask, t in (('m', tr), ('x', tx_bench.drop_flagged(tr))):
            pr = tx_bench.paired_positions(t, bl, ol)
            rb = tx_bench.score_item(t, bl, missing='skip', abstain=False, strict=strict)
            ro = tx_bench.score_item(t, ol, missing='skip', abstain=False, strict=strict)
            kb, n, eb, lob, hib = tx_bench.summarise(rb); ko, _, eo, loo, hio = tx_bench.summarise(ro)
            res[mask] = dict(n=n, base_err=kb, base_rate=round(eb, 4), base_ci=[round(lob, 4), round(hib, 4)], out_err=ko,
                             out_rate=round(eo, 4), out_ci=[round(loo, 4), round(hio, 4)], fixed=pr['fixed'], broken=pr['broken'],
                             net=pr['fixed'] - pr['broken'], p=round(pr['p'], 4), base_SDI=[rb['wrong'], rb['deleted'], rb['inserted']],
                             out_SDI=[ro['wrong'], ro['deleted'], ro['inserted']])
        return res
    R = {'units': {}, 'arms': {}}
    units = [('no87', 'dev_tune', ''), ('no87', 'eval_heldout', ''), ('no87', 'eval_heldout', '_ds'), ('f152r', 'f152r', '')]
    for it, u, ds in units:
        key = f'{it}_{u}{ds}'
        b = OUT / f'base_{it}_{u}{ds}.tsv'
        R['units'][key] = {'real': one(it, b, OUT / f'real_{it}_{u}{ds}.tsv'), 'real_strict': one(it, b, OUT / f'real_{it}_{u}{ds}.tsv', strict=True)}
        if u != 'dev_tune':
            for arm in ('keyshuf', 'clshuf'):
                R['units'][key][arm] = [one(it, b, OUT / f'{arm}_{i}_{it}_{u}{ds}.tsv') for i in range(1, N_ARMS + 1)]
    # pooled eval gate, both masks, with and without the d/s six
    def pooled(ds, arm=None, i=None):
        tot = {}
        for mask in ('m', 'x'):
            f = b = 0
            for it, u in (('no87', 'eval_heldout'), ('f152r', 'f152r')):
                key = f'{it}_{u}' + (ds if u == 'eval_heldout' else '')
                r = R['units'][key]['real'][mask] if arm is None else R['units'][key][arm][i][mask]
                f += r['fixed']; b += r['broken']
            tot[mask] = dict(fixed=f, broken=b, net=f - b, p=round(tx_bench.sign_test(f, b), 4))
        return tot
    for ds in ('', '_ds'):
        g = {'real': pooled(ds)}
        for arm in ('keyshuf', 'clshuf'):
            nets = {mask: [pooled(ds, arm, i)[mask]['net'] for i in range(N_ARMS)] for mask in ('m', 'x')}
            g[arm] = {mask: dict(nets=nets[mask], p95=float(__import__('numpy').percentile(nets[mask], 95)), max=max(nets[mask]),
                                 mean=round(statistics.mean(nets[mask]), 3)) for mask in ('m', 'x')}
        strict_ok = {}
        for it, u in (('no87', 'eval_heldout'), ('f152r', 'f152r')):
            key = f'{it}_{u}' + (ds if u == 'eval_heldout' else '')
            s = R['units'][key]['real_strict']
            strict_ok[key] = {mask: s[mask]['out_err'] <= s[mask]['base_err'] for mask in ('m', 'x')}
        gate = {}
        for mask in ('m', 'x'):
            r = g['real'][mask]
            gate[mask] = dict(g1_fixed_gt_broken_p05=r['fixed'] > r['broken'] and r['p'] < 0.05,
                              g2_net_gt_keyshuf_p95=r['net'] > g['keyshuf'][mask]['p95'],
                              g3_strict_not_worse=all(v[mask] for v in strict_ok.values()),
                              g4_net_gt_clshuf_p95=r['net'] > g['clshuf'][mask]['p95'])
            gate[mask]['all'] = all(gate[mask].values())
        g['strict_ok'] = strict_ok; g['gate'] = gate
        R['arms']['pooled' + ds] = g
    json.dump(R, open(SC / 'score.json', 'w'), indent=1)
    for k, v in R['arms'].items():
        print(k, json.dumps({m: dict(real=v['real'][m], keyshuf_p95=v['keyshuf'][m]['p95'], clshuf_p95=v['clshuf'][m]['p95'], gate=v['gate'][m]) for m in ('m', 'x')}))
    for key, v in R['units'].items():
        for m in ('m', 'x'):
            r = v['real'][m]; s = v['real_strict'][m]
            print(f'{key} [{m}] base {r["base_err"]}/{r["n"]} {r["base_rate"]} {r["base_ci"]} -> real {r["out_err"]}/{r["n"]} {r["out_rate"]} {r["out_ci"]}; '
                  f'fixed {r["fixed"]} broken {r["broken"]} p {r["p"]}; strict base {s["base_err"]} -> {s["out_err"]}; SDI base {r["base_SDI"]} out {r["out_SDI"]}')


if __name__ == '__main__':
    {'build': build, 'score': score}[sys.argv[1]]()

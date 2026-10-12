#!/usr/bin/env python3
"""PISA-RS244 (12 Oct 2026; pisa_rs244/PREREG-PISA-RS244.md): re-score of the f.244r relabel candidates PISA-244 settled
(pisa_244/result.tsv), one group per new cell, each relabelled alone in tx86/ciphertext_f244r.tsv. pis1key.py's run_files/clear_of/
ctrl86 and una2_pisa.py's read/write/per_token imported unchanged; key86.tsv unchanged.
    python3 pisa_rs244/rs244.py   -> pisa_rs244/tx/*, pisa_rs244/result.json, pisa_rs244/per_token.tsv
Reads tx86/ciphertext_f244r_preRS244.tsv when present (pre-edit bytes, once a relabel is committed). Paths relative to the target folder."""
import csv, itertools, json, math, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'una2_pisa'))
import una2_pisa as U
P = U.P
from pis1key import nw_score, dec, load_tokens, ctrl86

PG, CL, ERR = 'f244r', 'kp86/colbert_p49_50.txt', 0.284
REC = 'tx86/ciphertext_f244r.tsv'
if os.path.exists(os.path.join(T, 'tx86/ciphertext_f244r_preRS244.tsv')):
    REC = 'tx86/ciphertext_f244r_preRS244.tsv'
GROUPS = [('T45', 'T19'), ('T47', 'T27'), ('T57', 'T32'), ('T57', 'T35'), ('T57', 'T42')]
NOCOMMIT = {('T57', 'T42')}


def candidates():
    """{(old, new): set of (line, pos)} from pisa_244/result.tsv SETTLED tokens on a cell other than their label."""
    out = {}
    for r in csv.DictReader(open(os.path.join(T, 'pisa_244/result.tsv')), delimiter='\t'):
        if r['role'] == 'test' and r['verdict'].startswith('SETTLED-') and r['best_cell'] != r['answer_or_label']:
            _, l, p = r['id'].split('_')
            out.setdefault((r['answer_or_label'], r['best_cell']), set()).add((l, int(p[1:])))
    return out


def relabel(lines, picks, old, new):
    """picks: (line, pos) with pos 1-based counting '/'. Asserts the old label at each pick."""
    out, seen = [], set()
    for x in lines:
        if x is None:
            out.append(None); continue
        lab, body = x; t = body.split()
        for n, w in enumerate(t):
            if (lab, n + 1) in picks:
                assert w.strip('?') == old, (lab, n + 1, w, old); t[n] = w.replace(old, new); seen.add((lab, n + 1))
        out.append([lab, ' '.join(t)])
    assert seen == set(picks), set(picks) - seen
    return out


def ord_of(lines, picks):
    """(line, pos counting '/') -> (line, ord over non-'/' tokens), una2_pisa.per_token's key."""
    m = {}
    for x in lines:
        if x:
            j = 0
            for n, w in enumerate(x[1].split()):
                if w != '/':
                    j += 1
                    if (x[0], n + 1) in picks:
                        m[(x[0], n + 1)] = (x[0], j)
    return m


def all_of(lines, old):
    return {(x[0], n + 1) for x in lines if x for n, w in enumerate(x[1].split()) if w.strip('?') == old}


def score(lines, key, clear, dst):
    f = U.write(lines, dst); tk, _ = load_tokens(f); return float(nw_score(dec(tk, key), clear))


def main():
    key = P.load_key(); clear, ptext = P.clear_of(CL)
    lines = U.read(REC); cands = candidates()
    assert set(cands) == set(GROUPS), cands
    out = {"err": ERR, "file": REC, "copy": CL,
           "old": P.run_files(key, [REC, 'tx86/passA.tsv', 'tx86/passB.tsv'], clear)}
    out["positive_control"] = ctrl86(key, ptext, clear, ERR)
    G2 = bool(out["positive_control"]["passed"] >= 4)
    print('control', out["positive_control"]["passed"], '/5', flush=True)
    o = out["old"][REC]; rows = []; passed = []
    for old, new in GROUPS:
        picks = cands[(old, new)]; g = f'{old}->{new}'
        newf = U.write(relabel(lines, picks, old, new), f'pisa_rs244/tx/ciphertext_f244r_{old}_{new}.tsv')
        n = P.run_files(key, [newf], clear)[newf]
        allo = all_of(lines, old)
        r = {"picks": sorted(f'{l} p{p}' for l, p in picks), "n_old_label_on_page": len(allo), "new": n,
             "all_old_relabel": score(relabel(lines, allo, old, new), key, clear, 'pisa_rs244/tx/_all.tsv')}
        r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = G2
        combos = list(itertools.combinations(sorted(allo), len(picks)))
        sets = combos if len(combos) <= 200 else random.Random(20261012).sample(combos, 200)
        draws = sorted(score(relabel(lines, set(s), old, new), key, clear, 'pisa_rs244/tx/_tmp.tsv') for s in sets)
        r["random_subset_null"] = {"n": len(draws), "degenerate": len(draws) < 20, "mean": round(sum(draws) / len(draws), 4),
                                   "p95": round(draws[int(0.95 * (len(draws) - 1))], 4), "max": round(draws[-1], 4),
                                   "share_ge_ours": round(sum(x >= n["score"] - 1e-9 for x in draws) / len(draws), 3)}
        om = ord_of(lines, picks); tg = set(om.values())
        pt_old = U.per_token(REC, CL, key, tg); pt_new = U.per_token(newf, CL, key, tg); gi_n = gi_o = 0
        for w in sorted(picks):
            a, b = pt_old[om[w]], pt_new[om[w]]; gi_n += b["identical"]; gi_o += a["identical"]
            rows.append([g, w[0], str(w[1]), a["label"], a["copy"], str(a["identical"]), b["label"], b["copy"], str(b["identical"])])
        r["G3"] = {"relabelled": len(picks), "identical_new": gi_n, "identical_old": gi_o,
                   "pass": bool(gi_n >= math.ceil(len(picks) / 2) and gi_n > gi_o)}
        r["PASS"] = bool(r["G1"] and r["G2"] and r["G3"]["pass"]); r["commit"] = bool(r["PASS"] and (old, new) not in NOCOMMIT)
        if r["commit"]:
            passed.append((old, new))
        r["new"].pop("decoded_letters", None); out[g] = r
        print(g, n["score"], {k: r[k] for k in ('G1', 'G2')}, r["G3"], 'PASS', r["PASS"], flush=True)
    for f in ('_all.tsv', '_tmp.tsv'):
        os.remove(os.path.join(H, 'tx', f))
    comb = lines
    for old, new in passed:
        comb = relabel(comb, cands[(old, new)], old, new)
    cf = U.write(comb, 'pisa_rs244/tx/ciphertext_f244r.tsv')
    out["committable_groups"] = [f'{a}->{b}' for a, b in passed]
    out["combined"] = P.run_files(key, [cf], clear)[cf]; out["combined"].pop("decoded_letters", None)
    for f in out["old"].values():
        f.pop("decoded_letters", None)
    json.dump(out, open(os.path.join(H, 'result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'group\tline\tpos\told_label\told_copy\told_identical\tnew_label\tnew_copy\tnew_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print('old', o["score"], 'combined', out["combined"]["score"], 'committable', out["committable_groups"])


if __name__ == '__main__':
    main()

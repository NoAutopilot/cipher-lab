#!/usr/bin/env python3
"""PISA-T32 (9 Oct 2026; pisa_t32/PREREG-PISA-T32.md): T57 -> T32 relabel re-score of the 4 f.275r tokens una_pisa/result.tsv marks
SETTLED-T32 (PISA-275R). una2_pisa.py's relabel/write/per_token and pis1key.py's run_files/clear_of/control imported unchanged;
key86.tsv unchanged.
    python3 pisa_t32/pisa_t32.py   -> pisa_t32/tx86f/ciphertext_f275r.tsv, pisa_t32/result.json, pisa_t32/per_token.tsv
Paths relative to the target folder."""
import itertools, json, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'una2_pisa'))
import una2_pisa as U
P = U.P
from pis1key import nw_score, dec, load_tokens, control

PG, REC, CL, DROP, ERR = ('f275r', 'tx86e/ciphertext_f275r.tsv', 'kp86d/colbert_p121_123.txt',
                          'Mais croyant que Monsieur de Luxembourg', 0.215)
if os.path.exists(os.path.join(T, 'tx86e/ciphertext_f275r_preT32.tsv')):
    REC = 'tx86e/ciphertext_f275r_preT32.tsv'   # pre-edit bytes, once a relabel is committed


def main():
    key = P.load_key(); clear, ptext = P.clear_of(CL, DROP)
    lines = U.read(REC)
    sett = {(l, o): v for (p, l, o), v in U.SETTLED.items() if p == PG}
    picks = {k for k, v in sett.items() if v == 'SETTLED-T32'}
    assert len(picks) == 4, picks
    newf = U.write(U.relabel(lines, PG, picks), 'pisa_t32/tx86f/ciphertext_f275r.tsv')
    allT57 = {(x[0], j + 1) for x in lines if x for j, w in enumerate([w for w in x[1].split() if w != '/'])
              if w.strip('?') == 'T57'}
    allf = U.write(U.relabel(lines, PG, allT57), 'pisa_t32/tx86f/_all.tsv')
    r = {"err": ERR, "file": REC, "picks": sorted(f'{l} o{o}' for l, o in picks), "n_T57": len(allT57),
         "old": P.run_files(key, [REC, 'tx86e/passA.tsv', 'tx86e/passB.tsv'], clear), "new": P.run_files(key, [newf], clear)}
    r["all_T57_relabel"] = P.run_files(key, [allf], clear)[allf]; os.remove(os.path.join(T, allf))
    r["positive_control"] = control(key, ptext, clear, ERR, r["new"][newf]["decoded_letters"])
    print('control', r["positive_control"]["passed"], '/5', flush=True)
    o, n = r["old"][REC], r["new"][newf]
    r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = bool(r["positive_control"]["passed"] >= 4)
    combos = list(itertools.combinations(sorted(allT57), len(picks)))
    draws_sets = combos if len(combos) <= 200 else random.Random(20261009).sample(combos, 200)
    draws = []
    for s in draws_sets:
        tmp = U.write(U.relabel(lines, PG, set(s)), 'pisa_t32/tx86f/_tmp.tsv')
        tk, _ = load_tokens(tmp); draws.append(float(nw_score(dec(tk, key), clear)))
    os.remove(os.path.join(T, 'pisa_t32/tx86f/_tmp.tsv')); draws.sort()
    r["random_relabel_null"] = {"n": len(draws), "mean": round(sum(draws) / len(draws), 4), "max": round(draws[-1], 4),
                                "p95": round(draws[int(0.95 * (len(draws) - 1))], 4),
                                "share_ge_ours": round(sum(x >= n["score"] - 1e-9 for x in draws) / len(draws), 3)}
    pt_old = U.per_token(REC, CL, key, set(sett)); pt_new = U.per_token(newf, CL, key, set(sett)); rows = []
    for w in sorted(sett):
        rows.append([PG, w[0], str(w[1]), sett[w], pt_old[w]["label"], pt_old[w]["copy"], str(pt_old[w]["identical"]),
                     pt_new[w]["label"], pt_new[w]["copy"], str(pt_new[w]["identical"])])
    rel = [x for x in rows if x[3] == 'SETTLED-T32']
    g3n = sum(x[9] == 'True' for x in rel); g3o = sum(x[6] == 'True' for x in rel)
    r["G3"] = {"relabelled": len(rel), "identical_new_n": g3n, "identical_old_la": g3o, "pass": bool(g3n >= 2 and g3n > g3o)}
    r["PASS"] = bool(r["G1"] and r["G2"] and r["G3"]["pass"])
    json.dump(r, open(os.path.join(H, 'result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'page\tline\tord\tuna_pisa\told_label\told_copy\told_identical\tnew_label\tnew_copy\tnew_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print({"G1": r["G1"], "G2": r["G2"]}, r["G3"], 'PASS', r["PASS"])


if __name__ == '__main__':
    main()

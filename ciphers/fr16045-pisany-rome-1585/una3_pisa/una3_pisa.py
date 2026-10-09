#!/usr/bin/env python3
"""UNA3-PISA (9 Oct 2026; una3_pisa/PREREG-UNA3-PISA.md): T47 -> T27 relabel re-score of the 3 tokens una_pisa/result.tsv marks
SETTLED-T27 (f.275r L03 o12, f.301v L07 o1, f.302v L07 o29). una2_pisa.py's read/write/per_token/pos and pis1key.py's
run_files/clear_of/control imported unchanged; key86.tsv unchanged.
    python3 una3_pisa/una3_pisa.py   -> una3_pisa/tx/*, una3_pisa/result.json, una3_pisa/per_token.tsv
Reads the *_preT27 copies when present (pre-edit bytes, once a relabel is committed). Paths relative to the target folder."""
import itertools, json, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'una2_pisa'))
import una2_pisa as U
P = U.P
from pis1key import nw_score, dec, load_tokens, control

PAGES = [('f275r', 'tx86e', 'kp86d/colbert_p121_123.txt', 'Mais croyant que Monsieur de Luxembourg', 0.215),
         ('f301v', 'tx87', 'kp87a/colbert_p338_339.txt', None, 0.192),
         ('f302v', 'tx87b', 'kp87b/colbert_p341_342.txt', None, 0.335)]
OLD, NEW = 'T47', 'T27'


def rec_of(pg, d):
    pre = f'{d}/ciphertext_{pg}_preT27.tsv'
    return pre if os.path.exists(os.path.join(T, pre)) else f'{d}/ciphertext_{pg}.tsv'


def relabel(lines, pg, picks):
    """una2_pisa.relabel with T47 -> T27: asserts T47 at each pick and that tokens_pos `pos` matches."""
    out = []
    for x in lines:
        if x is None:
            out.append(None); continue
        lab, body = x; t = body.split(); j = 0
        for n, w in enumerate(t):
            if w == '/':
                continue
            j += 1
            if (lab, j) in picks:
                assert w.strip('?') == OLD, (pg, lab, j, w)
                if (pg, lab, j) in U.pos:
                    assert U.pos[(pg, lab, j)][0] == n + 1, (pg, lab, j, n + 1)
                t[n] = w.replace(OLD, NEW)
        out.append([lab, ' '.join(t)])
    return out


def picks_of(pg):
    return {(l, o) for (p, l, o), v in U.SETTLED.items() if p == pg and v == 'SETTLED-' + NEW}


def main():
    key = P.load_key(); out = {}; rows = []
    assert key[OLD] == 'm' and key[NEW] == 'f'
    for pg, d, cl, drop, err in PAGES:
        clear, ptext = P.clear_of(cl, drop) if drop else P.clear_of(cl)
        rec = rec_of(pg, d); lines = U.read(rec); picks = picks_of(pg)
        assert len(picks) == 1, (pg, picks)
        newf = U.write(relabel(lines, pg, picks), f'una3_pisa/tx/ciphertext_{pg}.tsv')
        allo = {(x[0], j + 1) for x in lines if x for j, w in enumerate([w for w in x[1].split() if w != '/'])
                if w.strip('?') == OLD}
        allf = U.write(relabel(lines, pg, allo), f'una3_pisa/tx/_all_{pg}.tsv')
        r = {"err": err, "file": rec, "picks": sorted(f'{l} o{o}' for l, o in picks), "n_T47": len(allo),
             "old": P.run_files(key, [rec, f'{d}/passA.tsv', f'{d}/passB.tsv'], clear), "new": P.run_files(key, [newf], clear)}
        r["all_T47_relabel"] = P.run_files(key, [allf], clear)[allf]; os.remove(os.path.join(T, allf))
        r["positive_control"] = control(key, ptext, clear, err, r["new"][newf]["decoded_letters"])
        print(pg, 'control', r["positive_control"]["passed"], '/5', flush=True)
        o, n = r["old"][rec], r["new"][newf]
        r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = bool(r["positive_control"]["passed"] >= 4)
        draws = []
        for s in itertools.combinations(sorted(allo), len(picks)):
            tmp = U.write(relabel(lines, pg, set(s)), f'una3_pisa/tx/_tmp_{pg}.tsv')
            tk, _ = load_tokens(tmp); draws.append(float(nw_score(dec(tk, key), clear)))
        os.remove(os.path.join(T, f'una3_pisa/tx/_tmp_{pg}.tsv')); draws.sort()
        r["random_relabel_null"] = {"n": len(draws), "draws": [round(x, 4) for x in draws],
                                    "share_ge_ours": round(sum(x >= n["score"] - 1e-9 for x in draws) / len(draws), 3)}
        tgt = {(l, o2) for (p, l, o2) in U.SETTLED if p == pg and U.pos[(p, l, o2)][1] == OLD}
        pt_old = U.per_token(rec, cl, key, tgt); pt_new = U.per_token(newf, cl, key, tgt)
        for w in sorted(tgt):
            rows.append([pg, w[0], str(w[1]), U.SETTLED[(pg,) + w], pt_old[w]["label"], pt_old[w]["copy"],
                         str(pt_old[w]["identical"]), pt_new[w]["label"], pt_new[w]["copy"], str(pt_new[w]["identical"])])
        out[pg] = r
    rel = [x for x in rows if x[3] == 'SETTLED-' + NEW]
    g3n = sum(x[9] == 'True' for x in rel); g3o = sum(x[6] == 'True' for x in rel)
    out["G3"] = {"relabelled": len(rel), "identical_new_f": g3n, "identical_old_m": g3o, "pass": bool(g3n >= 2 and g3n > g3o)}
    out["PASS"] = bool(all(out[p]["G1"] and out[p]["G2"] for p, *_ in PAGES) and out["G3"]["pass"])
    json.dump(out, open(os.path.join(H, 'result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'page\tline\tord\tuna_pisa\told_label\told_copy\told_identical\tnew_label\tnew_copy\tnew_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print(json.dumps({p: {"G1": out[p]["G1"], "G2": out[p]["G2"]} for p, *_ in PAGES}), out["G3"], 'PASS', out["PASS"])


if __name__ == '__main__':
    main()

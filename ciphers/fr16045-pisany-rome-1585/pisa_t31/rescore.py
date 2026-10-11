#!/usr/bin/env python3
"""PISA-T31 (11 Oct 2026; PREREG-PISA-T31.md): re-score of the f.275r T31 tokens pisa_t31/result.tsv marks SETTLED-BY-TWO on a
cell of another value. pis1key.py (run_files, clear_of, control) and una2_pisa.py (per_token) imported unchanged; key86.tsv unchanged.
    python3 pisa_t31/rescore.py   -> pisa_t31/tx/ciphertext_f275r.tsv, pisa_t31/rescore_result.json, pisa_t31/per_token.tsv
Paths relative to the target folder."""
import json, math, os, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'pis1key')); sys.path.insert(0, os.path.join(T, 'una2_pisa'))
import pis1key as P
import una2_pisa as U

PG, CL, DROP, ERR = 'f275r', 'kp86d/colbert_p121_123.txt', 'Mais croyant que Monsieur de Luxembourg', 0.215
REC = 'tx86e/ciphertext_f275r.tsv'
if os.path.exists(os.path.join(T, 'tx86e/ciphertext_f275r_preT31.tsv')):
    REC = 'tx86e/ciphertext_f275r_preT31.tsv'   # pre-edit bytes, once a relabel is committed


def picks():
    out = {}
    for ln in open(os.path.join(H, 'result.tsv')).read().splitlines()[1:]:
        f = ln.split('\t')
        if len(f) > 11 and f[0] == PG and f[11].endswith('(relabel candidate)'):
            _, l, i = f[2].split('_'); out[(l, int(i[1:]))] = f[5]
    return out


def relabel(path, pk, dst):
    lines = []
    for ln in open(os.path.join(T, path)):
        if not ln.strip():
            lines.append('\n'); continue
        lab, body = ln.rstrip('\n').split('\t', 1); t = body.split(); j = 0
        for n, x in enumerate(t):
            if x == '/':
                continue
            if (lab, j) in pk:
                assert x.strip('?') == 'T31', (lab, j, x); t[n] = x.replace('T31', pk[(lab, j)])
            j += 1
        lines.append(f'{lab}\t{" ".join(t)}\n')
    p = os.path.join(T, dst); os.makedirs(os.path.dirname(p), exist_ok=True); open(p, 'w').write(''.join(lines))
    return dst


def main():
    key = P.load_key(); clear, ptext = P.clear_of(CL, DROP); pk = picks()
    newf = relabel(REC, pk, 'pisa_t31/tx/ciphertext_f275r.tsv')
    r = {"err": ERR, "file": REC, "picks": {f'{l} i{i}': v for (l, i), v in sorted(pk.items())},
         "old": P.run_files(key, [REC], clear), "new": P.run_files(key, [newf], clear)}
    r["positive_control"] = P.control(key, ptext, clear, ERR, r["new"][newf]["decoded_letters"])
    o, n = r["old"][REC], r["new"][newf]
    r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = bool(r["positive_control"]["passed"] >= 4)
    tg = {(l, i + 1) for (l, i) in pk}
    pt_old = U.per_token(REC, CL, key, tg); pt_new = U.per_token(newf, CL, key, tg); rows = []
    for (l, i), v in sorted(pk.items()):
        w = (l, i + 1)
        rows.append([PG, l, str(i), v, pt_old[w]["label"], pt_old[w]["copy"], str(pt_old[w]["identical"]),
                     pt_new[w]["label"], pt_new[w]["copy"], str(pt_new[w]["identical"])])
    g3n = sum(x[9] == 'True' for x in rows); g3o = sum(x[6] == 'True' for x in rows)
    r["G3"] = {"relabelled": len(rows), "identical_new": g3n, "identical_old_m": g3o,
               "pass": bool(g3n >= math.ceil(len(rows) / 2) and g3n > g3o)}
    r["PASS"] = bool(r["G1"] and r["G2"] and r["G3"]["pass"])
    for k in ('old', 'new'):
        for f in r[k].values():
            f.pop("decoded_letters", None)
    json.dump(r, open(os.path.join(H, 'rescore_result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'page\tline\tidx0\tpisa_t31\told_label\told_copy\told_identical\tnew_label\tnew_copy\tnew_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print(json.dumps({k: r[k] for k in ('picks', 'G1', 'G2', 'G3', 'PASS')}), o["score"], n["score"])


if __name__ == '__main__':
    main()

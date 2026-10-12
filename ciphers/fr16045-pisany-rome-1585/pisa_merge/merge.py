#!/usr/bin/env python3
"""PISA-MERGE (12 Oct 2026; pisa_merge/PREREG-PISA-MERGE.md): re-score of the f.244r merge questions (tokens a double read put in
tx86), one group per merge, each deletion applied alone to tx86/ciphertext_f244r.tsv. pis1key.py's run_files/clear_of/ctrl86 and
una2_pisa.py's read/write/per_token imported unchanged (via pisa_rs244/rs244.py); key86.tsv unchanged.
    python3 pisa_merge/merge.py   -> pisa_merge/tx/*, pisa_merge/result.json, pisa_merge/per_token.tsv
Reads tx86/ciphertext_f244r_preMERGE.tsv when present (pre-edit bytes, once a merge is committed). Paths relative to the target folder."""
import itertools, json, math, os, random, sys
H = os.path.dirname(os.path.abspath(__file__)); T = os.path.dirname(H)
sys.path.insert(0, os.path.join(T, 'pisa_rs244'))
import rs244 as R
U, P = R.U, R.P
from pis1key import ctrl86

CL, ERR = R.CL, R.ERR
BASE = 'tx86/ciphertext_f244r.tsv'
if os.path.exists(os.path.join(T, 'tx86/ciphertext_f244r_preMERGE.tsv')):
    BASE = 'tx86/ciphertext_f244r_preMERGE.tsv'
# group: (deletions {(line, pos): label}, kept partners [(line, pos)], run length for the null (0 = single token), committable)
GROUPS = {
    'G-M5': ({('L05', 30): 'T57'}, [('L05', 29)], 0, True),
    'G-OV6': ({('L06', 27): 'T14', ('L06', 28): 'T30', ('L06', 29): 'T45', ('L06', 30): 'T18'},
              [('L06', 23), ('L06', 24), ('L06', 26)], 4, True),
    'G-OV8': ({('L08', 25): 'T26', ('L08', 26): 'T37'}, [('L08', 23), ('L08', 24)], 2, True),
    'G-X': ({('L02', 11): '?[tcross]', ('L04', 44): '?[tcross]', ('L06', 25): '?[tcross]'},
            [('L02', 12), ('L04', 45), ('L06', 24)], None, False),   # non-test by construction (PREREG)
    'G-M5alt': ({('L05', 29): 'T35'}, [('L05', 30)], None, False),   # descriptive alternative
}


def delete(lines, dels):
    """dels: {(line, pos counting '/'): expected label}; asserts each label, returns new lines."""
    out, seen = [], set()
    for x in lines:
        if x is None:
            out.append(None); continue
        lab, body = x; keep = []
        for n, w in enumerate(body.split()):
            if (lab, n + 1) in dels:
                assert w.rstrip('?') == dels[(lab, n + 1)].rstrip('?') or w == dels[(lab, n + 1)], (lab, n + 1, w)
                seen.add((lab, n + 1)); continue
            keep.append(w)
        out.append([lab, ' '.join(keep)])
    assert seen == set(dels), set(dels) - seen
    return out


def is_t(w):
    w = w.rstrip('?'); return w.startswith('T') and w[1:].isdigit()


def ords(lines, picks, dels=()):
    """(line, pos counting '/') -> (line, ord over non-'/' tokens) after deleting dels (per_token's key)."""
    m = {}
    for x in lines:
        if x:
            j = 0
            for n, w in enumerate(x[1].split()):
                if (x[0], n + 1) in dels:
                    continue
                if w != '/':
                    j += 1
                    if (x[0], n + 1) in picks:
                        m[(x[0], n + 1)] = (x[0], j)
    return m


def null_sets(lines, run, own):
    """Same-size deletions elsewhere: run 0 = one T-token; run k = k contiguous T-tokens in one line ('/' skipped)."""
    out = []
    for x in lines:
        if not x:
            continue
        ts = [n + 1 for n, w in enumerate(x[1].split()) if is_t(w)]
        k = max(run, 1)
        for i in range(len(ts) - k + 1):
            s = frozenset((x[0], p) for p in ts[i:i + k])
            if s != own:
                out.append(s)
    return out


def score(lines, key, clear, dst):
    f = U.write(lines, dst); tk, _ = R.load_tokens(f); return float(R.nw_score(R.dec(tk, key), clear))


def main():
    key = P.load_key(); clear, ptext = P.clear_of(CL)
    lines = U.read(BASE)
    out = {"err": ERR, "file": BASE, "copy": CL, "base": P.run_files(key, [BASE], clear)[BASE]}
    out["base"].pop("decoded_letters", None)
    out["positive_control"] = ctrl86(key, ptext, clear, ERR)
    G2 = bool(out["positive_control"]["passed"] >= 4)
    print('control', out["positive_control"]["passed"], '/5', flush=True)
    o = out["base"]; rows = []; passed = []
    for g, (dels, kept, run, commit) in GROUPS.items():
        newl = delete(lines, dels); newf = U.write(newl, f'pisa_merge/tx/ciphertext_f244r_{g}.tsv')
        n = P.run_files(key, [newf], clear)[newf]; n.pop("decoded_letters", None)
        r = {"deleted": sorted(f'{l} p{p} {v}' for (l, p), v in dels.items()), "kept": [f'{l} p{p}' for l, p in kept], "new": n}
        r["G1"] = bool(n["score"] > o["score"] and n["above_both"]); r["G2"] = G2
        # alignment: deleted tokens in the base, kept partners in base and merged file
        tdel = [w for w in dels if is_t(dels[w])]
        mb = ords(lines, set(tdel) | set(kept)); mn = ords(lines, set(kept), set(dels))
        pb = U.per_token(BASE, CL, key, set(mb.values())); pn = U.per_token(newf, CL, key, set(mn.values()))
        id_del = sum(pb[mb[w]]["identical"] for w in tdel)
        id_kb = sum(pb[mb[w]]["identical"] for w in kept if mb[w] in pb)
        id_kn = sum(pn[mn[w]]["identical"] for w in kept if mn[w] in pn)
        for w in tdel:
            a = pb[mb[w]]; rows.append([g, w[0], str(w[1]), 'deleted', a["label"], a["copy"], str(a["identical"]), '', '', ''])
        for w in kept:
            a = pb.get(mb[w], {}); b = pn.get(mn[w], {})
            rows.append([g, w[0], str(w[1]), 'kept', a.get("label", ''), a.get("copy", ''), str(a.get("identical", '')),
                         b.get("label", ''), b.get("copy", ''), str(b.get("identical", ''))])
        r["G3"] = {"n_del_T": len(tdel), "deleted_identical_base": id_del, "kept_identical_base": id_kb, "kept_identical_merged": id_kn,
                   "pass": bool(len(tdel) > 0 and id_del < math.ceil(len(tdel) / 2) and id_kn >= id_kb)}
        if run is not None:
            own = frozenset(dels); sets = null_sets(lines, run, own)
            sets = sets if len(sets) <= 200 else random.Random(20261012).sample(sets, 200)
            draws = sorted(score(delete(lines, {w: lines_label(lines, w) for w in s}), key, clear, 'pisa_merge/tx/_tmp.tsv') for s in sets)
            share = sum(x >= n["score"] - 1e-9 for x in draws) / len(draws)
            r["G4"] = {"n": len(draws), "mean": round(sum(draws) / len(draws), 4), "p95": round(draws[int(0.95 * (len(draws) - 1))], 4),
                       "max": round(draws[-1], 4), "share_ge_ours": round(share, 3), "pass": bool(share <= 0.05)}
            r["PASS"] = bool(r["G1"] and G2 and r["G3"]["pass"] and r["G4"]["pass"])
        else:
            r["PASS"] = None
        r["commit"] = bool(commit and r["PASS"])
        if r["commit"]:
            passed.append(g)
        out[g] = r
        print(g, n["score"], 'G1', r["G1"], 'G3', r["G3"], 'G4', r.get("G4"), 'PASS', r["PASS"], flush=True)
    if os.path.exists(os.path.join(H, 'tx', '_tmp.tsv')):
        os.remove(os.path.join(H, 'tx', '_tmp.tsv'))
    alld = {}
    for g in passed:
        alld.update(GROUPS[g][0])
    cf = U.write(delete(lines, alld), 'pisa_merge/tx/ciphertext_f244r.tsv')
    out["committable_groups"] = passed
    out["combined"] = P.run_files(key, [cf], clear)[cf]; out["combined"].pop("decoded_letters", None)
    json.dump(out, open(os.path.join(H, 'result.json'), 'w'), indent=1)
    open(os.path.join(H, 'per_token.tsv'), 'w').write(
        'group\tline\tpos\trole\tbase_label\tbase_copy\tbase_identical\tmerged_label\tmerged_copy\tmerged_identical\n'
        + ''.join('\t'.join(x) + '\n' for x in rows))
    print('base', o["score"], 'combined', out["combined"]["score"], 'committable', passed)


def lines_label(lines, w):
    for x in lines:
        if x and x[0] == w[0]:
            return x[1].split()[w[1] - 1]


if __name__ == '__main__':
    main()

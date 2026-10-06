#!/usr/bin/env python3
"""R10-ZESCRIB: crib-drag of fixed French diplomatic formulae for a near-exact seed (PREREG-R10-ZESCRIB.md).

Each crib (greedy longest-match tokens over the generator's unit list, first and last token dropped) is dragged along the
French segments; a placement is kept if the window is consistent with an injective code<->unit key and Bourdeau's 7 pins;
kept placements are ranked by the unchanged word-parse objective J (wordseg_syllabary) of pins + crib codes + freq_init
fill (wordseg_pt). Matched control first (G0 >= 3 true instances, G1 top-3 share >= 0.50, G2 seeded accuracy >= 0.60);
the target runs only if all three pass.
Usage: python3 crib_drag.py control | target | --check   (--check re-runs the control, exits 1 if crib_drag_control.json is stale)
"""
import itertools, json, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import wordseg_syllabary as W  # noqa: E402
import wordseg_pt as P  # noqa: E402
import anneal_syllabary as G  # noqa: E402

CRIBS = ("jailhonneurde monsieurlebaron votreexcellence samajestelempereur samajesteleroi legouvernement lecabinetde "
         "saintpetersbourg lecomtedenesselrode jevousprie veuillezagreer lassurancedemaconsideration tresdistinguee "
         "votredepeche vosrapports lempereur lesaffaires lapolitique lesinstructions queje ilestimportant danslinteret "
         "conformement delapartde relativement").split()
TOP, MARGIN, PASSES, SEED = 3, 50.0, 4, 10200
G0, G1, G2 = 3, 0.50, 0.60
OUT = HERE / "crib_drag_control.json"
_F = {}


def fill(segs, inv, pins, train):
    """wordseg_pt.freq_init, same result, with the unit-frequency table computed once (it does not depend on pins)."""
    from collections import Counter
    import numpy as np
    codes = sorted({int(c) for _, cs in segs for c in cs})
    if "f" not in _F:
        units = P.unit_list(inv, len(codes))
        ntok = Counter(l for l, cs in segs for _ in cs); tot = sum(ntok.values())
        f = P.unit_freq(units, train, {l: ntok[l] / tot for l in ("fr", "de")})
        _F["f"] = [inv.index(u) for u in sorted(units, key=lambda u: -f[u])]
        cc = Counter(int(c) for _, cs in segs for c in cs)
        _F["c"] = sorted(codes, key=lambda c: -cc[c])
    pinned = set(pins.values())
    m = np.zeros(100, dtype=np.int64)
    for c, u in pins.items():
        m[c] = u
    for c, u in zip([c for c in _F["c"] if c not in pins], [u for u in _F["f"] if u not in pinned]):
        m[c] = u
    return m


def tok(s, by_len):
    out, i = [], 0
    while i < len(s):
        u = next((u for u in by_len if s.startswith(u, i)), s[i]); out.append(u); i += len(u)
    return out


def consistent(cs, core, uidx, pins, pin_of_unit):
    u2c, c2u = {}, {}
    for c, u in zip(cs, core):
        c = int(c); ui = uidx[u]
        if c in pins and pins[c] != ui:
            return None
        if ui in pin_of_unit and pin_of_unit[ui] != c:
            return None
        if u2c.setdefault(ui, c) != c or c2u.setdefault(c, ui) != ui:
            return None
    return {c: u for c, u in c2u.items() if c not in pins}


def J(m, ch, lms, inv):
    return sum(lms[l].llr("".join(inv[m[c]] for c in cs)) for l, cs in ch)


def greedy(m, fixed, segs, ch, lms, inv, rng):
    codes = sorted({int(c) for _, cs in segs for c in cs})
    free = [c for c in codes if c not in fixed]
    where = {c: set(k for k, (_, cs) in enumerate(ch) if (cs == c).any()) for c in codes}
    sc = lambda k: lms[ch[k][0]].llr("".join(inv[m[c]] for c in ch[k][1]))
    ss = [sc(k) for k in range(len(ch))]
    for p in range(PASSES):
        pairs = list(itertools.combinations(free, 2)); rng.shuffle(pairs); acc = 0
        for a, b in pairs:
            if m[a] == m[b]:
                continue
            m[a], m[b] = m[b], m[a]
            ks = where[a] | where[b]; new = {k: sc(k) for k in ks}
            if sum(new[k] - ss[k] for k in ks) > 1e-9:
                for k in ks:
                    ss[k] = new[k]
                acc += 1
            else:
                m[a], m[b] = m[b], m[a]
        if acc == 0:
            break
    return m, sum(ss), p + 1


def drag(segs, inv, lms, pins, units, train, truth=None):
    by_len = sorted(units, key=len, reverse=True); uidx = {u: inv.index(u) for u in units}
    pin_of_unit = {u: c for c, u in pins.items()}
    ch = W.chunks_of(segs); rows = []
    for crib in CRIBS:
        core = tok(crib, by_len)[1:-1]
        L = len(core); cands = []
        for si, (lang, cs) in enumerate(segs):
            if lang != "fr":
                continue
            for p in range(len(cs) - L + 1):
                mp = consistent(cs[p:p + L], core, uidx, pins, pin_of_unit)
                if mp is None:
                    continue
                ext = dict(pins); ext.update(mp)
                m = fill(segs, inv, ext, train)
                true_here = truth is not None and truth[si][p:p + L] == core
                cands.append({"seg": si, "pos": p, "J": round(J(m, ch, lms, inv), 2), "true": bool(true_here),
                              "map": {str(c): inv[u] for c, u in mp.items()}})
        cands.sort(key=lambda x: (-x["J"], x["true"]))  # ties counted against the true placement
        for r, c in enumerate(cands):
            c["rank"] = r + 1
        n_true = 0
        if truth is not None:
            for si, (lang, cs) in enumerate(segs):
                if lang == "fr":
                    n_true += sum(truth[si][p:p + L] == core for p in range(len(cs) - L + 1))
        rows.append({"crib": crib, "core": core, "n_consistent": len(cands), "n_true_instances": n_true,
                     "true_ranks": [c["rank"] for c in cands if c["true"]],
                     "margin": round(cands[0]["J"] - cands[1]["J"], 2) if len(cands) > 1 else (1e9 if cands else None),
                     "top": cands[:5]})
    return rows, ch


def seed_key(rows, pins, inv):
    ext = dict(pins); used = []
    for r in sorted([r for r in rows if r["top"] and r["margin"] >= MARGIN], key=lambda r: -r["margin"]):
        mp = {int(c): inv.index(u) for c, u in r["top"][0]["map"].items()}
        owners = {u: c for c, u in ext.items()}
        if any(c in ext and ext[c] != u for c, u in mp.items()) or any(u in owners and owners[u] != c for c, u in mp.items()):
            continue
        ext.update(mp); used.append(r["crib"])
    return ext, used


def control():
    P.init_setup(); train = P.TRAIN
    held, lms, inv, segs, truth, pins, tm, units, K = W.build_control()
    rows, ch = drag(segs, inv, lms, pins, units, train, truth)
    n_inst = sum(r["n_true_instances"] for r in rows)
    ranks = [x for r in rows for x in r["true_ranks"]]
    missed = n_inst - len(ranks)  # true instance made inconsistent (digit error / tokenisation) counts as a miss
    g1 = round(sum(x <= TOP for x in ranks) / n_inst, 3) if n_inst else None
    ext, used = seed_key(rows, pins, inv)
    seed_correct = sum(int(tm[c] == u) for c, u in ext.items() if c not in pins)
    res = {"control": "wordseg_syllabary.build_control()", "cribs": len(CRIBS), "true_instances": n_inst,
           "true_instances_inconsistent": missed, "true_ranks": ranks, "G1_top3_share": g1,
           "seed_cribs": used, "seed_codes_added": len(ext) - len(pins), "seed_codes_correct": seed_correct}
    rng = random.Random(SEED)
    m0 = fill(segs, inv, ext, train)
    res["seeded_start_acc"] = P.acc(m0, segs, truth, pins, inv)
    m, j, np_ = greedy(m0.copy(), set(ext), segs, ch, lms, inv, rng)
    res.update(seeded_acc=P.acc(m, segs, truth, pins, inv), seeded_J=round(j, 1), seeded_passes=np_)
    b0 = fill(segs, inv, pins, train)
    res["baseline_start_acc"] = P.acc(b0, segs, truth, pins, inv)
    b, jb, nb = greedy(b0.copy(), set(pins), segs, ch, lms, inv, random.Random(SEED))
    res.update(baseline_acc=P.acc(b, segs, truth, pins, inv), baseline_J=round(jb, 1), baseline_passes=nb,
               true_key_J=round(J(tm, ch, lms, inv), 1))
    g = [n_inst >= G0, g1 is not None and g1 >= G1, res["seeded_acc"] >= G2]
    res["gates"] = {"G0": g[0], "G1": g[1], "G2": g[2]}
    res["verdict"] = "CONTROL PASSES GATE" if all(g) else "CONTROL BELOW GATE"
    res["rows"] = rows
    return res


if __name__ == "__main__":
    a = sys.argv[1:]
    if a == ["--check"]:
        sys.exit(0 if json.dumps(control(), indent=1) + "\n" == OUT.read_text() else 1)
    if a == ["control"]:
        res = control(); OUT.write_text(json.dumps(res, indent=1) + "\n")
        print({k: v for k, v in res.items() if k != "rows"})
        for r in res["rows"]:
            print(r["crib"], r["n_consistent"], r["n_true_instances"], r["true_ranks"], r["margin"])
    elif a == ["target"]:
        if json.loads(OUT.read_text())["verdict"] != "CONTROL PASSES GATE":
            sys.exit("CONTROL BELOW GATE: target not run (PREREG-R10-ZESCRIB)")
        sys.exit("target mode: see PREREG-R10-ZESCRIB.md; implement only after a passed control")

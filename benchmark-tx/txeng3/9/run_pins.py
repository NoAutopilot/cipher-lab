#!/usr/bin/env python3
"""TXE3-9 PINS (account 3, 11 Oct 2026; benchmark-tx/PREREG-txeng3-9.md): owner decisions as hard pins in the key-constrained
lattice decode, Birago no.87. Read-free: no vision call, no network.

    python3 benchmark-tx/txeng3/9/run_pins.py build    # lattice (TX-DECODE recipe via txeng/conf/run_conf.py), pin sets,
                                                       # arms a/b/b2/b3 (lam 4) and a1/b1 (lam 1) -> outputs/*.tsv; NO truth read
    python3 benchmark-tx/txeng3/9/run_pins.py score    # after the outputs are committed: per-unit err (both masks), changed-sign
                                                       # lists with right/wrong, shuffled-key and random-pin controls -> score/*

Lattice: run_conf.prep() + run_conf.lattice() on all 26 lines (f178v L01-23 + f179r L01-03), passC skeleton, confusion_1572,
no matrix, no stability. Key: harvest/key_1572_sheet.tsv + X_CE = s (key_pins.tsv). LM it16dip, beam 64. f178r lines are
copied from L (benchmark-tx/outputs/birago1572-no87/labels.tsv) in every arm.

Rescore (11 Oct 2026, measurement correction, RESCORE.md): `--map FILE` joins sorter tiles to positions through FILE instead
of atlas/no87_box_token.tsv, `--x20 FILE` names arm c2, `--dir DIR` writes every output under DIR instead of this folder.
With none of the three the run is byte-identical to the committed one.
"""
import csv, json, random, re, statistics, sys, time
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import key_decode_lattice as K  # noqa: E402
import run_conf as RC  # noqa: E402
import tx_bench  # noqa: E402
from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus  # noqa: E402

RC.TMP = HERE / "work"
F = ROOT / "ciphers/nevers-birago-fr3251-1572"
H = RC.H
L_FILE = ROOT / "benchmark-tx/outputs/birago1572-no87/labels.tsv"
X20_FILE = ROOT / "benchmark-tx/outputs/birago1572-no87/passX20_owner.tsv"
MAP_DEFAULT = F / "atlas/no87_box_token.tsv"
MAP = MAP_DEFAULT
TRUTH = ROOT / "benchmark-tx/birago1572-no87.truth.tsv"
OUT = HERE / "outputs"; SC = HERE / "score"
DEV, EVAL = RC.DEV, RC.EVAL
LINES = DEV + EVAL
BEAM = 64
N_SHUF, N_RAND, SEED = 100, 20, 1


def tsv(p):
    return list(csv.DictReader((l for l in open(p) if not l.startswith('#')), delimiter='\t'))


def fam(p):
    m = re.match(r'^(T\d+)(-[a-z])?$', (p or '').strip())
    return m.group(1) if m else None


def unit(ln):
    return 'f178r' if ln.startswith('f178r') else ('dev_tune' if ln in DEV else 'eval_heldout')


def key_with_xce():
    key = K.read_key(H / "key_1572_sheet.tsv")
    key["X_CE"] = "s"
    with open(HERE / "key_pins.tsv", "w") as f:
        f.write("sign\tvalue\tnote\n")
        for s in sorted(key):
            f.write(f"{s}\t{key[s] or 'NULL'}\t{'X_CE = s: clerk sheet 7/7 (build_birago87.py), TXE3-9' if s == 'X_CE' else 'key_1572_sheet.tsv'}\n")
    return key


def pin_sets():
    """P_L (NO87-LABELS X_CE), P_O (owner 4 Oct 2026: moved rows at T family, 1:1 boxes, + the family-sort cluster decision),
    P_LO, P_S (P_LO + kept rows at family). Returns {name: {(line,pos): sign}}."""
    PL = {}
    for r in tsv(H / "exceptions_f178v.tsv"):
        if "X_CE" in r.get("reason", ""):
            PL[(f"{r['folio']}_{r['line']}", int(r["pos"]))] = "X_CE"
    box = {r["sid"]: (r["line"], int(r["pos"])) for r in tsv(MAP) if r["op"] == "1:1"}
    PO, kept = {}, {}
    for r in tsv(F / "sorter/no87/owner-sort-2026-10-04/settled_no87.tsv"):
        f1 = fam(r["new_sign"])
        if r["sid"] not in box or not f1:
            continue
        k = box[r["sid"]]
        if k[0] not in LINES:
            continue
        if r["status"] == "moved":
            PO[k] = f1
        elif r["status"] == "kept":
            kept[k] = f1
    for r in tsv(ROOT / "benchmark-tx/txeng2/sorter/x20_changes.tsv"):
        if r["source"] == "A":
            PO[(r["line"], int(r["pos"]))] = r["new"]
    PLO = dict(PL); PLO.update(PO)          # the owner's sign wins where both touch a position (as X20)
    PS = dict(kept); PS.update(PLO)         # a decision wins over a kept seed
    return {"P_L": PL, "P_O": PO, "P_LO": PLO, "P_S": PS}


def write_pins(name, pins):
    with open(HERE / f"pins_{name}.tsv", "w") as f:
        f.write("line\tpos\tsign\n")
        for (ln, pos), s in sorted(pins.items(), key=lambda kv: (LINES.index(kv[0][0]), kv[0][1])):
            f.write(f"{ln}\t{pos}\t{s}\n")


def whole_output(path, lat, seq, header):
    """L's f178r lines + the lattice lines' chosen signs, as one whole-no.87 file."""
    with open(path, "w") as f:
        f.write(f"# {header}\nline\tpos\tsign\n")
        for r in tsv(L_FILE):
            if r["line"].startswith("f178r"):
                f.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\n")
        for ((ln, pos), _), s in zip(lat, seq):
            f.write(f"{ln}\t{pos}\t{s}\n")


def passA_at(pages):
    """{(line,pos): pass A's sign} aligned to the skeleton by the tool's own difflib rule (positions it does not cover absent)."""
    out = {}
    for page, (a, b, ref) in pages.items():
        A = K.read_pass(a)
        order, R = K.ref_lines(ref)
        for ln in order:
            prow = A.get(K.short(ln), [])
            m = K.align(R[ln], [K.split_cands(r)[0] for r in prow])
            for j, r in enumerate(prow):
                if j in m:
                    out[(ln, m[j] + 1)] = K.split_cands(r)[0]
    return out


def build():
    OUT.mkdir(exist_ok=True)
    pages = RC.prep()
    key = key_with_xce()
    lm = K.LM(NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]]))
    base = RC.lattice(pages, LINES)
    RC.write_topk(HERE / "base_topk.tsv", base)
    P = pin_sets()
    for n, p in P.items():
        write_pins(n, p)
    arms = {"a": ("P_none", 4.0), "b": ("P_L", 4.0), "b2": ("P_LO", 4.0), "b3": ("P_S", 4.0), "a1": ("P_none", 1.0), "b1": ("P_L", 1.0)}
    info = {"positions": len(base), "pins": {n: len(p) for n, p in P.items()},
            "pins_by_unit": {n: {u: sum(1 for k in p if unit(k[0]) == u) for u in ("dev_tune", "eval_heldout")} for n, p in P.items()},
            "arms": {}}
    t1 = K.top1(base)
    for arm, (pn, lam) in arms.items():
        lat, st = (K.apply_pins(base, P[pn]) if pn != "P_none" else (base, None))
        t0 = time.time()
        seq, obj = K.viterbi(lat, key, lm, lam, BEAM)
        dt = time.time() - t0
        mapnote = "" if MAP == MAP_DEFAULT else f"; map {MAP.relative_to(ROOT)}"
        whole_output(OUT / f"pins_{arm}.tsv", lat, seq,
                     f"TXE3-9 arm {arm}: lattice lam {lam:g} + pins {pn} (benchmark-tx/txeng3/9/run_pins.py build); f178r from L{mapnote}")
        with open(HERE / f"decode_{arm}.tsv", "w") as f:
            f.write("line\tpos\ttop1\tchosen\tpinned\n")
            for ((ln, pos), _), a, b in zip(lat, t1, seq):
                f.write(f"{ln}\t{pos}\t{a}\t{b}\t{int((ln, pos) in P.get(pn, {}))}\n")
        info["arms"][arm] = {"pins": pn, "lam": lam, "pin_stats": st, "changed_vs_top1": sum(1 for x, y in zip(t1, seq) if x != y),
                             "seconds": round(dt, 2), "objective": round(obj, 3)}
        print(arm, info["arms"][arm], flush=True)
    json.dump(info, open(HERE / "build.json", "w"), indent=1)


# ---------------------------------------------------------------- scoring (reads truth)
def load_truth():
    rows = tx_bench.read_tsv(TRUTH)
    return rows, tx_bench.drop_flagged(rows)


def errs_by_unit(truth_rows, out_lines):
    e = tx_bench.position_errors(truth_rows, out_lines, missing="skip")
    by = defaultdict(lambda: [0, 0])
    for (ln, pos), w in e.items():
        u = unit(ln); by[u][1] += 1; by[u][0] += int(w)
        by["whole"][1] += 1; by["whole"][0] += int(w)
    return e, {u: (k, n, round(k / n, 4) if n else None, [round(x, 4) for x in tx_bench.wilson(k, n)]) for u, (k, n) in by.items()}


def lines_of(path):
    return tx_bench.load_output([str(path)])


def truth_sets(truth_rows):
    return {(r["line"], int(float(r["pos"]))): set(filter(None, r["truth"].split("|"))) for r in truth_rows if r["status"] == "scored"}


def score():
    SC.mkdir(exist_ok=True)
    info = json.load(open(HERE / "build.json"))
    truth_all, truth_x = load_truth()
    TS = truth_sets(truth_all)
    res = {"units": {}, "paired": {}, "changed": {}, "controls": {}}
    files = {arm: OUT / f"pins_{arm}.tsv" for arm in info["arms"]}
    files["c"] = L_FILE; files["c2"] = X20_FILE
    E = {}
    for arm, p in files.items():
        ol = lines_of(p)
        em, um = errs_by_unit(truth_all, ol)
        ex, ux = errs_by_unit(truth_x, ol)
        E[arm] = (em, ex)
        res["units"][arm] = {"as_measured": um, "flagged_excluded": ux}
    # paired position McNemar on the whole file and per unit, both masks
    def mc(ea, eb, keys):
        common = [k for k in keys if k in ea and k in eb]
        fx = sum(1 for k in common if ea[k] and not eb[k]); br = sum(1 for k in common if not ea[k] and eb[k])
        return {"n": len(common), "fixed": fx, "broken": br, "p": tx_bench.sign_test(fx, br)}
    for arm, base in (("b", "a"), ("b", "c"), ("b2", "a"), ("b2", "c"), ("b2", "c2"), ("b3", "a"), ("b3", "c"), ("a", "c"), ("b1", "a1")):
        for mi, mask in enumerate(("as_measured", "flagged_excluded")):
            ea, eb = E[base][mi], E[arm][mi]
            for u in ("whole", "dev_tune", "eval_heldout"):
                keys = [k for k in ea if u == "whole" or unit(k[0]) == u]
                res["paired"][f"{arm}_vs_{base}|{mask}|{u}"] = mc(ea, eb, keys)
    # changed-sign lists (grade S at best) and pinned positions, right/wrong against truth (as measured)
    for arm in ("a", "b", "b2", "b3"):
        rows = tsv(HERE / f"decode_{arm}.tsv")
        ch, pn = [], []
        for r in rows:
            k = (r["line"], int(r["pos"])); t = TS.get(k)
            rec = {"line": r["line"], "pos": int(r["pos"]), "top1": r["top1"], "chosen": r["chosen"],
                   "truth": "|".join(sorted(t)) if t else "(not scored)",
                   "verdict": ("unscored" if t is None else ("right" if r["chosen"] in t else "wrong")),
                   "top1_was": ("unscored" if t is None else ("right" if r["top1"] in t else "wrong"))}
            if r["pinned"] == "1":
                pn.append(rec)
            elif r["chosen"] != r["top1"]:
                ch.append(rec)
        res["changed"][arm] = {"changed_S": ch, "pinned": pn,
                               "changed_summary": {v: sum(1 for x in ch if x["verdict"] == v and x["top1_was"] != v) for v in ("right", "wrong")},
                               "pinned_summary": {v: sum(1 for x in pn if x["verdict"] == v) for v in ("right", "wrong", "unscored")}}
        with open(SC / f"changed_{arm}.tsv", "w") as f:
            f.write("kind\tline\tpos\ttop1\tchosen\ttruth\ttop1_was\tchosen_is\tgrade\n")
            for kind, lst in (("changed", ch), ("pinned", pn)):
                for x in lst:
                    f.write(f"{kind}\t{x['line']}\t{x['pos']}\t{x['top1']}\t{x['chosen']}\t{x['truth']}\t{x['top1_was']}\t{x['verdict']}\t{'pin' if kind == 'pinned' else 'S'}\n")
    # controls
    pages = RC.prep()
    key = key_with_xce()
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]])
    lm = K.LM(model)
    base = RC.lattice(pages, LINES)
    P = {n: K.read_pins(HERE / f"pins_{n}.tsv") for n in ("P_L", "P_O", "P_LO", "P_S")}
    scored = {k for k in TS}

    def unpinned_err(lat, seq, pins):
        w = n = 0
        for ((ln, pos), _), s in zip(lat, seq):
            k = (ln, pos)
            if k in pins or k not in TS:
                continue
            n += 1; w += int(s not in TS[k])
        return w, n

    # (1) shuffled keys with the same pins
    for pn in ("P_L", "P_LO"):
        lat, _ = K.apply_pins(base, P[pn])
        seq, _ = K.viterbi(lat, key, lm, 4.0, BEAM)
        rw, rn = unpinned_err(lat, seq, P[pn])
        real_s = model.score(K.text_of(seq, key))
        rnd = random.Random(SEED); shuf = []
        t0 = time.time()
        for i in range(N_SHUF):
            k2 = K.shuffled(key, rnd)
            s2, _ = K.viterbi(lat, k2, lm, 4.0, BEAM)
            w2, n2 = unpinned_err(lat, s2, P[pn])
            shuf.append({"err": w2 / n2, "score": model.score(K.text_of(s2, k2))})
        errs = [x["err"] for x in shuf]; scs = [x["score"] for x in shuf]
        res["controls"][f"shuffled_key|{pn}"] = {
            "n_shuffles": N_SHUF, "seconds": round(time.time() - t0, 1),
            "real_unpinned_err": round(rw / rn, 4), "real_unpinned_wrong": rw, "unpinned_scored": rn,
            "shuffled_unpinned_err": {"min": round(min(errs), 4), "mean": round(statistics.mean(errs), 4), "max": round(max(errs), 4)},
            "real_err_rank": 1 + sum(1 for e in errs if e <= rw / rn),
            "real_4gram": round(real_s, 4), "shuffled_4gram_max": round(max(scs), 4),
            "real_4gram_z": round((real_s - statistics.mean(scs)) / (statistics.pstdev(scs) or 1e-9), 2)}
        print("shuffled", pn, res["controls"][f"shuffled_key|{pn}"], flush=True)
    # (2) random pins from pass A, equal counts, outside the owner/labels positions
    pa = passA_at(pages)
    owner_pos = set(P["P_S"])
    pool = sorted(k for k in scored if k[0] in LINES and k not in owner_pos and k in pa)
    base_seq, _ = K.viterbi(base, key, lm, 4.0, BEAM)
    base_e = {k: int(s not in TS[k]) for ((ln, pos), _), s in zip(base, base_seq) for k in [(ln, pos)] if k in TS}
    for pn in ("P_L", "P_LO", "P_S"):
        n = len(P[pn]); rnd = random.Random(SEED + n); runs = []
        for seed in range(N_RAND):
            pick = rnd.sample(pool, n)
            pins = {k: pa[k] for k in pick}
            lat, _ = K.apply_pins(base, pins)
            seq, _ = K.viterbi(lat, key, lm, 4.0, BEAM)
            e = {k: int(s not in TS[k]) for ((ln, pos), _), s in zip(lat, seq) for k in [(ln, pos)] if k in TS}
            runs.append({"err": sum(e.values()) / len(e), "wrong": sum(e.values()),
                         "pins_right": sum(1 for k in pick if pa[k] in TS[k]),
                         "fixed": sum(1 for k in e if base_e[k] and not e[k]), "broken": sum(1 for k in e if not base_e[k] and e[k])})
        own_right = sum(1 for k, s in P[pn].items() if k in TS and s in TS[k]); own_scored = sum(1 for k in P[pn] if k in TS)
        res["controls"][f"random_pins|{pn}"] = {
            "n_pins": n, "seeds": N_RAND, "pool": len(pool), "lattice_scored": len(base_e), "base_wrong": sum(base_e.values()),
            "err": {"min": round(min(r["err"] for r in runs), 4), "mean": round(statistics.mean(r["err"] for r in runs), 4),
                    "max": round(max(r["err"] for r in runs), 4)},
            "wrong": {"min": min(r["wrong"] for r in runs), "mean": round(statistics.mean(r["wrong"] for r in runs), 2), "max": max(r["wrong"] for r in runs)},
            "fixed_mean": round(statistics.mean(r["fixed"] for r in runs), 2), "broken_mean": round(statistics.mean(r["broken"] for r in runs), 2),
            "pins_right_passA_mean": round(statistics.mean(r["pins_right"] for r in runs), 2),
            "pins_right_real": own_right, "pins_scored_real": own_scored}
        print("random", pn, res["controls"][f"random_pins|{pn}"], flush=True)
    json.dump(res, open(SC / "score.json", "w"), indent=1)
    # compact table
    with open(SC / "units.tsv", "w") as f:
        f.write("arm\tmask\tunit\twrong\tscored\terr\twilson_lo\twilson_hi\n")
        for arm, d in res["units"].items():
            for mask, ud in d.items():
                for u in ("whole", "dev_tune", "eval_heldout", "f178r"):
                    if u in ud:
                        k, n, e, (lo, hi) = ud[u]
                        f.write(f"{arm}\t{mask}\t{u}\t{k}\t{n}\t{e}\t{lo}\t{hi}\n")
    with open(SC / "paired.tsv", "w") as f:
        f.write("pair\tmask\tunit\tn\tfixed\tbroken\tp\n")
        for k, d in res["paired"].items():
            pair, mask, u = k.split("|")
            f.write(f"{pair}\t{mask}\t{u}\t{d['n']}\t{d['fixed']}\t{d['broken']}\t{d['p']:.4f}\n")


if __name__ == "__main__":
    a = sys.argv[2:]
    for flag in ("--map", "--x20", "--dir"):
        if flag in a:
            v = Path(a[a.index(flag) + 1]).resolve()
            if flag == "--map":
                MAP = v
            elif flag == "--x20":
                X20_FILE = v
            else:
                HERE = v; HERE.mkdir(parents=True, exist_ok=True)
                OUT = HERE / "outputs"; SC = HERE / "score"; RC.TMP = HERE / "work"
    {"build": build, "score": score}[sys.argv[1]]()

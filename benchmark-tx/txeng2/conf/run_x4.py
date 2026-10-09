#!/usr/bin/env python3
"""TXE2-CONF (PREREG-txeng2-2 X4, 9 Oct 2026), fixed BEFORE any score. Run from the repo root.
  python3 benchmark-tx/txeng2/conf/run_x4.py norm     raw/passX_raw_L*.tsv -> passX_dev_tune.tsv (line pos sign p1 top3),
                                                       and benchmark-tx/outputs/birago1572-no87/passX_conf_dev_tune.tsv
  python3 benchmark-tx/txeng2/conf/run_x4.py decode   truth-free lattice arm (writes out/; commit before score)
  python3 benchmark-tx/txeng2/conf/run_x4.py score    truth read only through tools/tx_bench functions; writes score.json
Scoring, as registered: (1) calibration of X's top-1 p vs accuracy against truth (5 equal-width bins on [0,1], ECE), and the
share of L's dev errors whose truth sits in X's top-3 at the aligned position (gate >= 0.5, else not usable as lattice input);
(2) DOUBT: recall of L's errors among truth positions where X's aligned top-1 p < 0.7 (or X has no sign), with the share
flagged; (3) lattice arm `conf`: L everywhere except tx_doubt's disagree OR latt positions (txeng/doubt/dev_tune_signals.tsv,
the two-signal combination TXE2-LATT used), where the candidates are X's own top-3 distribution (tools/key_decode_lattice.py
from_passes(..., probs=True), X aligned to L's skeleton by its difflib align; L's sign kept where X has no aligned sign);
every other position is fixed to L's sign (p 1); K.viterbi with key_1572_sheet.tsv, it16dip, lam 4, beam 64 over the
dev_tune sequence; paired vs L (labels.tsv), dev gate fixed > broken, two-sided sign test p < 0.05. Reported beside it, not
gating: `conftop1` (X's top-1 at the same positions, no LM). Control (rule 3): the conf arm under 20 value-shuffled keys
(seed 20261009) must not pass. X's own top-1 over all of dev_tune is reported (tx_bench, paired vs L), not an arm."""
import csv, glob, json, random, sys
from collections import defaultdict
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(ROOT / "tools")); sys.path.insert(0, str(ROOT / "benchmark-tx/txeng/conf"))
import key_decode_lattice as K  # noqa: E402
import run_conf as RC  # noqa: E402

DEV = RC.DEV
PX = HERE / "passX_dev_tune.tsv"
OUTX = RC.OUTD / "passX_conf_dev_tune.tsv"
OUT = HERE / "out"
LAM, BEAM, NSHUF = 4.0, 64, 20


def rd(p):
    with open(p) as f:
        return list(csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"))


def norm():
    rows = []
    for p in sorted(glob.glob(str(HERE / "raw/passX_raw_L*.tsv"))):
        for r in rd(p):
            ln = "f178v_" + r["passage"].strip()
            d = K.parse_top3(r)
            s = (r["sign_id"] or "?").strip()
            p1 = d.get(s, max(d.values()) if d else 1.0)
            rows.append((ln, int(r["pos"]), s, p1, (r.get("top3") or "").strip(), r.get("conf", "").strip()))
    rows.sort(key=lambda t: (t[0], t[1]))
    with open(PX, "w") as f:
        f.write("passage\tpos\tsign_id\tconf\tp1\ttop3\n")
        for ln, pos, s, p1, t3, c in rows:
            f.write(f"{ln}\t{pos}\t{s}\t{c}\t{p1:.3f}\t{t3}\n")
    with open(OUTX, "w") as f:
        f.write("line\tpos\tsign\n")
        for ln, pos, s, *_ in rows:
            f.write(f"{ln}\t{pos}\t{s}\n")
    print(len(rows), "signs;", {ln: sum(1 for r in rows if r[0] == ln) for ln in DEV})


def flagged():
    return {(r["line"], int(r["pos"])) for r in rd(ROOT / "benchmark-tx/txeng/doubt/dev_tune_signals.tsv")
            if r["line"] in DEV and (r["disagree"] == "1" or r["latt"] == "1")}


def L_rows():
    return [r for r in rd(RC.OUTD / "labels.tsv") if r["line"] in DEV]


def write(path, rows):
    with open(path, "w") as f:
        f.write("line\tpos\tsign\n")
        for ln, pos, s in rows:
            f.write(f"{ln}\t{pos}\t{s}\n")


def x_on_L():
    """{(line,pos) of L: X's distribution} via from_passes(probs=True) with L as the skeleton (truth-free)."""
    Lr = L_rows()
    ref = OUT / "L_dev_tune_ref.tsv"
    write(ref, [(r["line"], r["pos"], r["sign"]) for r in Lr])
    px = OUT / "passX_short.tsv"  # from_passes keys passes by the short line id
    with open(px, "w") as f:
        f.write("passage\tpos\tsign_id\tconf\ttop3\n")
        for r in rd(PX):
            f.write(f"{K.short(r['passage'])}\t{r['pos']}\t{r['sign_id']}\t{r['conf']}\t{r['top3']}\n")
    rows, st = K.from_passes(str(px), None, str(ref), {}, probs=True)
    seen = defaultdict(dict)
    for ln, pos, c, p in rows:
        seen[(ln, pos)][c] = p
    # positions X did not reach come back as {'?': 1.0} from finish(); treat as "no X sign"
    return Lr, {k: v for k, v in seen.items() if v != {"?": 1.0}}, st


def arm(Lr, X, flags, key, lm):
    lat = []
    for r in Lr:
        k = (r["line"], int(r["pos"]))
        lat.append((k, dict(X[k]) if (k in flags and k in X) else {r["sign"]: 1.0}))
    seq = K.viterbi(lat, key, lm, LAM, BEAM)[0]
    return [(k[0], k[1], s) for (k, _), s in zip(lat, seq)]


def decode():
    from judge_plaintext import LANG_CORPORA, NgramModel, read_corpus
    OUT.mkdir(exist_ok=True)
    Lr, X, st = x_on_L(); flags = flagged()
    key = K.read_key(RC.H / "key_1572_sheet.tsv")
    lm = K.LM(NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]]))
    print("L positions", len(Lr), "flagged", len(flags), "flagged with X", sum(1 for k in flags if k in X), st)
    write(OUT / "conf.tsv", arm(Lr, X, flags, key, lm))
    write(OUT / "conftop1.tsv", [(r["line"], r["pos"], max(X[(r["line"], int(r["pos"]))].items(), key=lambda kv: kv[1])[0]
                                  if (r["line"], int(r["pos"])) in flags and (r["line"], int(r["pos"])) in X else r["sign"])
                                 for r in Lr])
    rnd = random.Random(20261009)
    for i in range(NSHUF):
        write(OUT / f"shuf{i:02d}.tsv", arm(Lr, X, flags, K.shuffled(key, rnd), lm))
    print("written", OUT)


def x_truth_positions(T, xs):
    """per truth row of dev_tune (scored): (truth set, X sign index or None) via tx_bench.align."""
    import tx_bench as B
    by = defaultdict(list)
    for r in T:
        if r["line"] in DEV:
            by[r["line"]].append(r)
    out = {}
    for ln, rows in by.items():
        rows.sort(key=lambda r: float(r["pos"]))
        ref = [r["ref_sign"] for r in rows]
        ts = [set(filter(None, r["truth"].split("|"))) for r in rows]
        seq = [x["sign_id"] for x in xs.get(ln, [])]
        j = 0
        for ri, osg in B.align(ref, ts, seq):
            if ri is None:
                j += 1; continue
            if rows[ri]["status"] == "scored":
                out[(ln, rows[ri]["pos"])] = (ts[ri], xs[ln][j] if osg is not None else None)
            if osg is not None:
                j += 1
    return out


def score():
    import tx_bench as B
    T = B.read_tsv(RC.TRUTH)
    xs = defaultdict(list)
    for r in rd(PX):
        xs[r["passage"]].append(r)
    for v in xs.values():
        v.sort(key=lambda r: int(r["pos"]))
    Lp = str(RC.OUTD / "labels.tsv")
    Ll = {k: v for k, v in B.load_output([Lp]).items() if k in DEV}
    eL = B.position_errors(T, Ll)
    XP = x_truth_positions(T, xs)
    res = {"L_errors": sum(eL.values()), "scored": len(eL)}
    # (1) calibration
    bins = [[0, 0, 0.0] for _ in range(5)]
    for k, (ts, x) in XP.items():
        if x is None:
            continue
        p = float(x["p1"]); ok = x["sign_id"] in ts
        b = min(4, int(p * 5)); bins[b][0] += 1; bins[b][1] += ok; bins[b][2] += p
    n = sum(b[0] for b in bins)
    res["reliability"] = [dict(bin=f"{i/5:.1f}-{(i+1)/5:.1f}", n=b[0], acc=round(b[1] / b[0], 3) if b[0] else None,
                               mean_p=round(b[2] / b[0], 3) if b[0] else None) for i, b in enumerate(bins)]
    res["ECE"] = round(sum(abs(b[1] - b[2]) for b in bins) / n, 4) if n else None
    res["X_top1_acc_aligned"] = round(sum(b[1] for b in bins) / n, 4) if n else None
    errs = [k for k, w in eL.items() if w]
    det = []
    for k in errs:
        ts, x = XP.get(k, (set(), None))
        d = K.parse_top3(x) if x else {}
        det.append(dict(pos=f"{k[0]}:{k[1]}", truth="|".join(sorted(ts)), X=x["sign_id"] if x else None,
                        p1=float(x["p1"]) if x else None, top3=x["top3"] if x else None, in_top3=bool(set(d) & ts)))
    res["L_err_in_top3"] = f"{sum(d['in_top3'] for d in det)}/{len(det)}"
    res["top3_gate_pass"] = sum(d["in_top3"] for d in det) >= 0.5 * len(det)
    res["L_err_detail"] = det
    # (2) doubt signal p1 < 0.7
    fl = {k for k, (ts, x) in XP.items() if x is None or float(x["p1"]) < 0.7}
    keys = [k for k in eL if k in XP]
    res["doubt_p07"] = dict(flagged=len(fl & set(keys)), share=round(len(fl & set(keys)) / len(keys), 4),
                            recall=f"{sum(1 for k in errs if k in fl)}/{len(errs)}")
    # (3) lattice arm + control + X's own top-1
    res["paired_vs_L"] = {}
    for name in ["conf", "conftop1"]:
        res["paired_vs_L"][name] = B.paired(T, Ll, B.load_output([str(OUT / f"{name}.tsv")]))
    res["paired_vs_L"]["X_top1_all"] = B.paired(T, Ll, {k: v for k, v in B.load_output([str(OUTX)]).items() if k in DEV})
    sh = [B.paired(T, Ll, B.load_output([p])) for p in sorted(glob.glob(str(OUT / "shuf*.tsv")))]
    res["shuffle_control"] = dict(n=len(sh), passing=sum(1 for s in sh if s["fixed"] > s["broken"] and s["p"] < 0.05),
                                  fixed_mean=round(sum(s["fixed"] for s in sh) / len(sh), 2),
                                  broken_mean=round(sum(s["broken"] for s in sh) / len(sh), 2))
    c = res["paired_vs_L"]["conf"]
    res["dev_gate_conf"] = "PASS" if c["fixed"] > c["broken"] and c["p"] < 0.05 else "FAIL"
    json.dump(res, open(HERE / "score.json", "w"), indent=1)
    print(json.dumps({k: v for k, v in res.items() if k != "L_err_detail"}, indent=1))


if __name__ == "__main__":
    {"norm": norm, "decode": decode, "score": score}[sys.argv[1]]()

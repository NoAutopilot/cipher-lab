#!/usr/bin/env python3
"""VIV-LAT runner (PREREG-VIVLAT.md, 14 Oct 2026). Key-constrained lattice decode with a confusion matrix learnt on this
hand: dev (f.102r dev2, two folds, lam grid) and confirm (f.103r confirm2, one look). Disk only.
  python3 run_vivlat.py prep            # key + renamed passes
  python3 run_vivlat.py dev             # step 1 (writes dev/, dev_result.json)
  python3 run_vivlat.py confirm --lam L # step 2 (writes confirm/, confirm_result.json)
"""
import csv, json, re, subprocess, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import tx_bench  # noqa: E402

TOOL = ["python3", str(ROOT / "tools/key_decode_lattice.py")]
BENCH = ["python3", str(ROOT / "tools/tx_bench.py")]
FOLDER = ROOT / "ciphers/fr16104-vivonne-spain-1572"
DEV = dict(item="vivonne1573-f102r-dev2", truth=ROOT / "benchmark-tx/vivonne1573-f102r-dev2.truth.tsv",
           passes={k: ROOT / f"benchmark-tx/outputs/vivonne1573-f102r-dev/pass{k}_dv1.tsv" for k in "ABZ"})
CON = dict(item="vivonne1573-f103r-confirm2", truth=ROOT / "benchmark-tx/vivonne1573-f103r-confirm2.truth.tsv",
           passes={"A": ROOT / "benchmark-tx/outputs/vivonne1573-f103r-confirm2/passA_S2.tsv",
                   "B": ROOT / "benchmark-tx/outputs/vivonne1573-f103r-confirm2/passB_S2.tsv",
                   "Z": ROOT / "benchmark-tx/outputs/vivonne1573-f103r-confirm2/passZ_S2b.tsv"})
LAMS = [1, 2, 4, 8]
KEY = HERE / "key_sv.tsv"


def run(cmd, log=None):
    r = subprocess.run([str(c) for c in cmd], capture_output=True, text=True, cwd=ROOT)
    if r.returncode:
        sys.exit(f"FAILED {cmd}\n{r.stderr}")
    if log:
        Path(log).write_text(r.stdout)
    return r.stdout


def prep():
    with open(FOLDER / "key.tsv") as f, open(KEY, "w") as g:
        g.write("sign\tvalue\n")
        for r in csv.DictReader(f, delimiter="\t"):
            g.write(f"{r['code']}\t{r['meaning']}\n")
    for tag, it in (("dev", DEV), ("con", CON)):
        for k, p in it["passes"].items():
            out = HERE / f"in_{tag}_{k}.tsv"
            with open(p) as f, open(out, "w") as g:
                g.write("passage\tpos\tsign_id\talt\tconf\n")
                for r in csv.DictReader(f, delimiter="\t"):
                    g.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\t{r.get('alt') or ''}\t{r.get('conf') or ''}\n")


def truth_lines(truth):
    return sorted({r["line"] for r in tx_bench.read_tsv(str(truth))})


def read_topk(p):
    lat = defaultdict(dict); order = []
    for r in csv.DictReader(open(p), delimiter="\t"):
        k = (r["line"], int(r["pos"]))
        if k not in lat:
            order.append(k)
        lat[k][r["cand"]] = float(r["score"])
    return order, lat


def write_signs(rows, out):
    """rows: [(line, pos, sign)] -> pass-format TSV for tx_bench."""
    with open(out, "w") as f:
        f.write("line\tpos\tsign\n")
        for ln, pos, s in rows:
            f.write(f"{ln}\t{pos}\t{s}\n")


def top1_rows(topk):
    order, lat = read_topk(topk)
    return [(k[0], k[1], max(lat[k].items(), key=lambda kv: kv[1])[0]) for k in order]


def chosen_rows(prefix):
    return [(r["line"], int(r["pos"]), r["chosen"]) for r in csv.DictReader(open(f"{prefix}.decode.tsv"), delimiter="\t")]


def bench(item, out, base):
    return run(BENCH + ["--item", item, "--exclude-flagged", "--paired", base, out])


def parse_bench(txt):
    d = {}
    m = re.search(r"as measured: err_true\(0.75-indel align\) ([\d.]+) \((\d+)/(\d+)\)", txt)
    if m: d["err_meas"] = float(m.group(1)); d["err_meas_n"] = f"{m.group(2)}/{m.group(3)}"
    m = re.search(r"flagged excluded \(truth-verifier flags only\): err_true\(0.75-indel align\) ([\d.]+) \((\d+)/(\d+)\)", txt)
    if m: d["err_fx"] = float(m.group(1)); d["err_fx_n"] = f"{m.group(2)}/{m.group(3)}"
    for tag, pat in (("meas", r"\[as measured\]"), ("fx", r"\[flagged excluded[^\]]*\]")):
        m = re.search(pat + r": (\d+) lines; lines improved (\d+), worsened (\d+), tied (\d+); line sign test p = ([\d.]+)"
                      r".*?fixed (\d+), broken (\d+)", txt, re.S)
        if m:
            d[f"paired_{tag}"] = dict(lines=int(m.group(1)), improved=int(m.group(2)), worsened=int(m.group(3)),
                                      tied=int(m.group(4)), p=float(m.group(5)), fixed=int(m.group(6)), broken=int(m.group(7)))
    return d


def truth_in_lattice(item_truth, top1_file, topk, only=None):
    """of the top-1's wrong scored positions (tx_bench alignment, excluding flagged too reported), share whose truth set
    meets the lattice candidates at the same skeleton position."""
    T = defaultdict(list)
    for r in tx_bench.read_tsv(str(item_truth)):
        T[r["line"]].append(r)
    order, lat = read_topk(topk)
    byline = defaultdict(list)
    for k in order:
        byline[k[0]].append(k)
    rows = defaultdict(list)
    for r in csv.DictReader(open(top1_file), delimiter="\t"):
        rows[r["line"]].append(r["sign"])
    res = {"all": [0, 0], "fx": [0, 0]}
    for ln, trs in T.items():
        if only is not None and ln not in only:
            continue
        trs.sort(key=lambda r: float(r["pos"]))
        out = rows.get(ln, [])
        ref = [r["ref_sign"] for r in trs]
        ts = [set(filter(None, r["truth"].split("|"))) for r in trs]
        j = -1
        for ri, osg in tx_bench.align(ref, ts, out):
            if osg is not None:
                j += 1
            if ri is None or osg is None or trs[ri]["status"] != "scored":
                continue
            if osg in ts[ri]:  # tx_bench counts by truth value; a match to the ref sign alone is still wrong
                continue
            cands = set(lat[byline[ln][j]]) if j < len(byline[ln]) else set()
            hit = bool(cands & ts[ri])
            for tag in ("all", "fx") if not (trs[ri].get("flag") or "").strip() else ("all",):
                res[tag][0] += hit; res[tag][1] += 1
    return {k: {"truth_in_lattice": v[0], "top1_wrong": v[1], "share": round(v[0] / v[1], 3) if v[1] else None}
            for k, v in res.items()}


def dev():
    D = HERE / "dev"; D.mkdir(exist_ok=True)
    lines = truth_lines(DEV["truth"])
    folds = {"odd": [l for l in lines if int(l.split("_L")[1]) % 2 == 1],
             "even": [l for l in lines if int(l.split("_L")[1]) % 2 == 0]}
    A, B, Z = (HERE / f"in_dev_{k}.tsv" for k in "ABZ")
    plain = D / "plain.topk.tsv"
    run(TOOL + ["from-passes", A, B, "--out", plain])
    write_signs(top1_rows(plain), D / "top1.tsv")
    out = {"folds": {k: len(v) for k, v in folds.items()}, "lam": {}}
    out["top1_alone"] = parse_bench(run(BENCH + ["--item", DEV["item"], "--exclude-flagged", D / "top1.tsv"]))
    for ctl in ("real", "shuf1"):
        mats = {}
        for held, other in (("odd", "even"), ("even", "odd")):
            M = D / f"M_{ctl}_learn{other}.tsv"
            cmd = TOOL + ["learn-confusion", A, B, Z, "--truth", DEV["truth"], "--key", KEY, "--out", M,
                          "--lines"] + folds[other]
            if ctl != "real":
                cmd += ["--shuffle-offdiag", "1"]
            run(cmd, D / f"M_{ctl}_learn{other}.log")
            tk = D / f"{ctl}_held{held}.topk.tsv"
            run(TOOL + ["from-passes", A, B, "--confusion-matrix", M, "--matrix-only", "--out", tk])
            mats[held] = tk
        for lam in (LAMS if ctl == "real" else [None]):
            if lam is None:
                continue
            rows, tl = [], {}
            for held, tk in mats.items():
                pre = D / f"{ctl}_held{held}_lam{lam}"
                run(TOOL + ["decode", tk, "--key", KEY, "--lang", "fr16", "--lam", lam, "--out-prefix", pre])
                rows += [r for r in chosen_rows(pre) if r[0] in set(folds[held])]
                tl[held] = truth_in_lattice(DEV["truth"], D / "top1.tsv", tk, set(folds[held]))
            o = D / f"{ctl}_lam{lam}.pooled.tsv"
            write_signs(rows, o)
            txt = bench(DEV["item"], o, D / "top1.tsv")
            (D / f"{ctl}_lam{lam}.bench.txt").write_text(txt)
            out["lam"][f"{ctl}_{lam}"] = parse_bench(txt)
            out["lam"][f"{ctl}_{lam}"]["truth_in_lattice_by_heldfold_matrix"] = tl
        out["mats_" + ctl] = {k: str(v.relative_to(HERE)) for k, v in mats.items()}
    (HERE / "dev_result.json").write_text(json.dumps(out, indent=1) + "\n")
    print(json.dumps(out, indent=1))


def dev_plain(lam):
    """diagnostic (not registered as a gate): plain two-reader lattice + LM, no matrix, at the chosen lam."""
    D = HERE / "dev"
    pre = D / f"plainLM_lam{lam}"
    run(TOOL + ["decode", D / "plain.topk.tsv", "--key", KEY, "--lang", "fr16", "--lam", lam, "--out-prefix", pre])
    write_signs(chosen_rows(pre), D / f"plainLM_lam{lam}.tsv")
    txt = bench(DEV["item"], D / f"plainLM_lam{lam}.tsv", D / "top1.tsv")
    (D / f"plainLM_lam{lam}.bench.txt").write_text(txt)
    r = parse_bench(txt); print(json.dumps(r, indent=1)); return r


def dev_control(lam):
    """shuffled off-diagonal matrices at the chosen lam (not gating)."""
    D = HERE / "dev"
    lines = truth_lines(DEV["truth"])
    folds = {"odd": {l for l in lines if int(l.split("_L")[1]) % 2 == 1},
             "even": {l for l in lines if int(l.split("_L")[1]) % 2 == 0}}
    rows = []
    for held in ("odd", "even"):
        pre = D / f"shuf1_held{held}_lam{lam}"
        run(TOOL + ["decode", D / f"shuf1_held{held}.topk.tsv", "--key", KEY, "--lang", "fr16", "--lam", lam,
                    "--out-prefix", pre])
        rows += [r for r in chosen_rows(pre) if r[0] in folds[held]]
    o = D / f"shuf1_lam{lam}.pooled.tsv"
    write_signs(rows, o)
    txt = bench(DEV["item"], o, D / "top1.tsv")
    (D / f"shuf1_lam{lam}.bench.txt").write_text(txt)
    r = parse_bench(txt)
    print(json.dumps(r, indent=1))
    return r


def confirm(lam):
    C = HERE / "confirm"; C.mkdir(exist_ok=True)
    lines = truth_lines(DEV["truth"])
    A, B, Z = (HERE / f"in_dev_{k}.tsv" for k in "ABZ")
    M = C / "M_alldev.tsv"
    run(TOOL + ["learn-confusion", A, B, Z, "--truth", DEV["truth"], "--key", KEY, "--out", M, "--lines"] + lines,
        C / "M_alldev.log")
    cA, cB = HERE / "in_con_A.tsv", HERE / "in_con_B.tsv"
    plain = C / "plain.topk.tsv"
    run(TOOL + ["from-passes", cA, cB, "--out", plain])
    write_signs(top1_rows(plain), C / "top1.tsv")
    tk = C / "lat.topk.tsv"
    run(TOOL + ["from-passes", cA, cB, "--confusion-matrix", M, "--matrix-only", "--out", tk])
    pre = C / f"lat_lam{lam}"
    dj = json.loads(run(TOOL + ["decode", tk, "--key", KEY, "--lang", "fr16", "--lam", lam, "--shuffles", 100,
                                "--seed", 1, "--out-prefix", pre]))
    write_signs(chosen_rows(pre), C / f"lat_lam{lam}.tsv")
    txt = bench(CON["item"], C / f"lat_lam{lam}.tsv", C / "top1.tsv")
    (C / f"lat_lam{lam}.bench.txt").write_text(txt)
    top1_txt = run(BENCH + ["--item", CON["item"], "--exclude-flagged", C / "top1.tsv"])
    (C / "top1.bench.txt").write_text(top1_txt)
    res = {"lam": lam, "lattice": parse_bench(txt), "top1": parse_bench(top1_txt),
           "control": dj.get("control"), "changed": dj.get("changed"),
           "truth_in_lattice": truth_in_lattice(CON["truth"], C / "top1.tsv", tk),
           "truth_in_plain_lattice": truth_in_lattice(CON["truth"], C / "top1.tsv", plain)}
    pf = res["lattice"].get("paired_fx", {})
    ga = pf.get("improved", 0) > pf.get("worsened", 0) and pf.get("p", 1) < 0.05
    gb = res["lattice"].get("err_meas", 9) <= res["top1"].get("err_meas", -1)
    gc = (dj.get("control") or {}).get("lattice", {}).get("rank") == 1
    res["gate"] = {"a": ga, "b": gb, "c": gc, "PASS": ga and gb and gc}
    (HERE / "confirm_result.json").write_text(json.dumps(res, indent=1) + "\n")
    print(json.dumps(res, indent=1))


if __name__ == "__main__":
    cmd = sys.argv[1]
    if cmd == "prep":
        prep()
    elif cmd == "dev":
        dev()
    elif cmd == "devplain":
        dev_plain(int(sys.argv[2]))
    elif cmd == "devctl":
        dev_control(int(sys.argv[2]))
    elif cmd == "confirm":
        confirm(int(sys.argv[sys.argv.index("--lam") + 1]))

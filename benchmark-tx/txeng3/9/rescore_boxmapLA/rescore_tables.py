#!/usr/bin/env python3
"""BOXMAP-RESCORE tables (account 3, 11 Oct 2026; benchmark-tx/txeng3/9/RESCORE.md). Measurement correction, not a new gate
look: TXE3-9's owner / kept arms and X20 re-scored after the no.87 box<->position map was fixed (off by one on L06, L09, L11,
L13, L21, f179r L03). Reads truth (it is a scorer); writes nothing but rescore.json and stdout.

    python3 benchmark-tx/txeng3/9/run_pins.py build --map M --x20 X --dir D   # (committed; D = this folder)
    python3 benchmark-tx/txeng3/9/run_pins.py score --map M --x20 X --dir D
    python3 benchmark-tx/txeng3/9/rescore_boxmapLA/rescore_tables.py          # -> rescore_boxmapLA/rescore.json

Every err_true figure and every paired count is the committed scorer's CLI output (tools/tx_bench.py --bench BENCHMARK-TX.tsv
--item birago1572-no87 --exclude-flagged [--paired BASE]), parsed; pin accuracy is the harness's own naive position lookup
(run_pins.truth_sets), with the off-by-one symptom counted beside it (a wrong pin whose sign is the truth at pos +/-1).
"""
import json, re, subprocess, sys, tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
sys.path.insert(0, str(HERE.parent))
import tx_bench  # noqa: E402
import run_pins as RP  # noqa: E402

OLD9, NEW9 = HERE.parent, HERE
O = ROOT / "benchmark-tx/outputs/birago1572-no87"
FILES = {
    "a": NEW9 / "outputs/pins_a.tsv", "b": NEW9 / "outputs/pins_b.tsv", "c": O / "labels.tsv",
    "a1": NEW9 / "outputs/pins_a1.tsv", "b1": NEW9 / "outputs/pins_b1.tsv",
    "b2_old": OLD9 / "outputs/pins_b2.tsv", "b2_new": NEW9 / "outputs/pins_b2.tsv",
    "b3_old": OLD9 / "outputs/pins_b3.tsv", "b3_new": NEW9 / "outputs/pins_b3.tsv",
    "c2_old": O / "passX20_owner.tsv", "c2_new": O / "passX20_owner_boxmapLA.tsv",
}
PAIRS = [("b2_old", "a"), ("b2_new", "a"), ("b2_old", "c"), ("b2_new", "c"), ("b2_old", "c2_old"), ("b2_new", "c2_new"),
         ("b2_old", "b"), ("b2_new", "b"), ("b3_old", "a"), ("b3_new", "a"), ("b3_old", "c"), ("b3_new", "c"),
         ("b3_old", "b2_old"), ("b3_new", "b2_new"), ("c2_old", "c"), ("c2_new", "c"),
         ("b2_new", "b2_old"), ("b3_new", "b3_old"), ("c2_new", "c2_old"),
         ("b", "a"), ("b", "c"), ("a", "c"), ("b1", "a1")]
X20 = {"L": O / "labels.tsv",
       "owner_old": O / "passX20_owner.tsv", "family_old": O / "passX20a_family.tsv", "no87sort_old": O / "passX20b_no87sort.tsv",
       "owner_new": O / "passX20_owner_boxmapLA.tsv", "family_new": O / "passX20a_family_boxmapLA.tsv",
       "no87sort_new": O / "passX20b_no87sort_boxmapLA.tsv"}
DEV_BASE = ROOT / "benchmark-tx/txeng/units/labels_dev_tune.tsv"
BENCH = ["python3", str(ROOT / "tools/tx_bench.py"), "--bench", str(ROOT / "BENCHMARK-TX.tsv"), "--item", "birago1572-no87",
         "--exclude-flagged"]
RE_ERR = re.compile(r"(as measured|flagged excluded \(truth-verifier flags only\)): err_true\(0\.75-indel align\) [0-9.]+ \((\d+)/(\d+)\)")
RE_ACC = re.compile(r"accepted-token error (\d+)/(\d+)")
RE_PAIR = re.compile(r"\[(as measured|flagged excluded)[^\]]*\]: .*?McNemar: (\d+) common scored signs; base wrong (\d+), output wrong (\d+); "
                     r"fixed (\d+), broken (\d+); exact p = ([0-9.]+)")


def run(args):
    return subprocess.run(BENCH + [str(a) for a in args], capture_output=True, text=True, cwd=ROOT, check=True).stdout


def single(path):
    out = run([path]); res = {}
    for m in RE_ERR.finditer(out):
        mask = "as_measured" if m.group(1) == "as measured" else "flagged_excluded"
        k, n = int(m.group(2)), int(m.group(3))
        if mask not in res:
            res[mask] = {"k": k, "n": n, "err": round(k / n, 4), "wilson": [round(x, 4) for x in tx_bench.wilson(k, n)]}
    return res


def paired(out_path, base_path):
    out = run([out_path, "--paired", base_path]); res = {}
    for m in RE_PAIR.finditer(out):
        mask = "as_measured" if m.group(1) == "as measured" else "flagged_excluded"
        res[mask] = {"n": int(m.group(2)), "base_wrong": int(m.group(3)), "out_wrong": int(m.group(4)),
                     "fixed": int(m.group(5)), "broken": int(m.group(6)), "p": float(m.group(7))}
    return res


def dev_only(path, tmp):
    dev = {r["line"] for r in RP.tsv(DEV_BASE)}
    p = Path(tmp) / (path.stem + "_dev_tune.tsv")
    with open(p, "w") as f:
        f.write("line\tpos\tsign\n")
        for r in RP.tsv(path):
            if r["line"] in dev:
                f.write(f"{r['line']}\t{r['pos']}\t{r['sign']}\n")
    return p


def dev_scores(path):
    """Accepted-token error on the dev lines (X20's committed figure) and, unless path is L itself, the paired McNemar."""
    is_base = path.name == DEV_BASE.name  # L's own dev lines (dev_only(labels.tsv) -> labels_dev_tune.tsv)
    out = run([path] if is_base else [path, "--paired", DEV_BASE]); res = {}
    accs = RE_ACC.findall(out)
    for mask, (k, n) in zip(("as_measured", "flagged_excluded"), accs):
        res[mask] = {"k": int(k), "n": int(n), "err": round(int(k) / int(n), 4)}
    for m in RE_PAIR.finditer(out):
        mask = "as_measured" if m.group(1) == "as measured" else "flagged_excluded"
        res[mask].update({"fixed": int(m.group(5)), "broken": int(m.group(6)), "p": float(m.group(7))})
    return res


def pin_table(folder, TS):
    P = {n: RP.tsv(folder / f"pins_{n}.tsv") for n in ("P_L", "P_O", "P_LO", "P_S")}
    P = {n: {(r["line"], int(r["pos"])): r["sign"] for r in rows} for n, rows in P.items()}
    P["kept"] = {k: s for k, s in P["P_S"].items() if k not in P["P_LO"]}
    da = {(r["line"], int(r["pos"])): r["chosen"] for r in RP.tsv(folder / "decode_a.tsv")}
    out = {}
    for n, pins in P.items():
        sc = [k for k in pins if k in TS]
        right = [k for k in sc if pins[k] in TS[k]]
        wrong = [k for k in sc if pins[k] not in TS[k]]
        adj = lambda k, d: (k[0], k[1] + d) in TS and pins[k] in TS[(k[0], k[1] + d)]
        out[n] = {"pins": len(pins), "scored": len(sc), "right": len(right), "wrong": len(wrong),
                  "arm_a_right_at_scored": sum(1 for k in sc if da.get(k) in TS[k]),
                  "differ_from_arm_a": sum(1 for k in pins if da.get(k) != pins[k]),
                  "wrong_eq_truth_pm1": sum(1 for k in wrong if adj(k, -1) or adj(k, 1)),
                  "right_eq_truth_pm1": sum(1 for k in right if adj(k, -1) or adj(k, 1)),
                  "wrong_list": [f"{k[0]}.{k[1]} {pins[k]} (truth {'|'.join(sorted(TS[k]))})" for k in sorted(wrong)]}
    return out


def x20_changes(TS):
    res = {}
    for tag, p in (("old", ROOT / "benchmark-tx/txeng2/sorter/x20_changes.tsv"),
                   ("new", ROOT / "benchmark-tx/txeng2/sorter/x20_changes_boxmapLA.tsv")):
        rows = []
        for r in RP.tsv(p):
            k = (r["line"], int(r["pos"])); t = TS.get(k)
            v = "unscored" if t is None else ("right" if r["new"] in t else "wrong")
            lv = "unscored" if t is None else ("right" if r["L"] in t else "wrong")
            rows.append(f"{r['source']} {r['line']}.{r['pos']} {r['L']}->{r['new']}: new {v}, L was {lv}")
        res[tag] = rows
    return res


def after_vs_inside(folder, tmp):
    """The first verifier's own comparison (VERIFY.md): arm a with a pin set written over it afterwards vs the same set pinned
    inside the decode; neighbours = unpinned positions where the two differ."""
    a = RP.tsv(folder / "outputs/pins_a.tsv"); res = {}
    for pn, arm in (("P_LO", "b2"), ("P_S", "b3")):
        pins = {(r["line"], int(r["pos"])): r["sign"] for r in RP.tsv(folder / f"pins_{pn}.tsv")}
        p = Path(tmp) / f"after_{folder.name}_{pn}.tsv"
        with open(p, "w") as f:
            f.write("line\tpos\tsign\n")
            for r in a:
                f.write(f"{r['line']}\t{r['pos']}\t{pins.get((r['line'], int(r['pos'])), r['sign'])}\n")
        inside = folder / f"outputs/pins_{arm}.tsv"
        di = {(r["line"], int(r["pos"])): r["sign"] for r in RP.tsv(inside)}
        da = {(r["line"], int(r["pos"])): r["sign"] for r in a}
        nb = sorted(k for k in di if k not in pins and di[k] != da[k])
        res[pn] = {"after": single(p), "inside": single(inside), "inside_vs_after": paired(inside, p),
                   "neighbours_moved": [f"{k[0]}.{k[1]}" for k in nb]}
    return res


def naive_lattice_wrong(folder, TS):
    """Wrong signs on the 26 lattice lines by the random-pin control's own naive lookup (score.json controls.base_wrong)."""
    out = {}
    for arm in ("a", "b", "b2", "b3"):
        d = RP.tsv(folder / f"decode_{arm}.tsv")
        out[arm] = sum(1 for r in d if (r["line"], int(r["pos"])) in TS and r["chosen"] not in TS[(r["line"], int(r["pos"]))])
    return out


def main():
    truth_all, _ = RP.load_truth()
    TS = RP.truth_sets(truth_all)
    res = {"note": "measurement correction: box-to-position map fixed (off by one), not a new gate look",
           "map_old": "ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token.tsv",
           "map_new": "ciphers/nevers-birago-fr3251-1572/atlas/no87_box_token_labelaware.tsv",
           "single": {a: single(p) for a, p in FILES.items()},
           "paired": {f"{x}_vs_{y}": paired(FILES[x], FILES[y]) for x, y in PAIRS},
           "pins": {"old": pin_table(OLD9, TS), "new": pin_table(NEW9, TS)},
           "x20_changes": x20_changes(TS)}
    with tempfile.TemporaryDirectory() as tmp:
        res["x20_dev"] = {n: dev_scores(dev_only(p, tmp)) for n, p in X20.items()}
        res["after_vs_inside"] = {"old": after_vs_inside(OLD9, tmp), "new": after_vs_inside(NEW9, tmp)}
    res["naive_lattice_wrong"] = {"old": naive_lattice_wrong(OLD9, TS), "new": naive_lattice_wrong(NEW9, TS)}
    json.dump(res, open(HERE / "rescore.json", "w"), indent=1)
    f = lambda d: f"{d['err']:.3f} ({d['k']}/{d['n']})"
    print("== whole no.87 (tx_bench err_true; as measured | flagged excluded)")
    for a, d in res["single"].items():
        print(f"  {a:8s} {f(d['as_measured'])} {d['as_measured']['wilson'][0]:.3f}-{d['as_measured']['wilson'][1]:.3f} | {f(d['flagged_excluded'])}")
    print("== paired (fixed / broken, p; as measured | flagged excluded)")
    for k, d in res["paired"].items():
        m, x = d["as_measured"], d["flagged_excluded"]
        print(f"  {k:20s} {m['fixed']} / {m['broken']}, p {m['p']:.4f} | {x['fixed']} / {x['broken']}, p {x['p']:.4f}")
    print("== pins (naive position lookup)")
    for tag in ("old", "new"):
        for n, d in res["pins"][tag].items():
            print(f"  {tag} {n:5s} pins {d['pins']} scored {d['scored']} right {d['right']} wrong {d['wrong']} | arm a right {d['arm_a_right_at_scored']} | "
                  f"differ from a {d['differ_from_arm_a']} | wrong=truth@+/-1 {d['wrong_eq_truth_pm1']} right=truth@+/-1 {d['right_eq_truth_pm1']}")
    print("== X20 dev_tune (accepted-token error; paired vs labels_dev_tune)")
    for n, d in res["x20_dev"].items():
        m, x = d["as_measured"], d["flagged_excluded"]
        extra = "" if "fixed" not in m else f" | fixed {m['fixed']} / broken {m['broken']}, p {m['p']:.2f} (flagged-excl {x['fixed']} / {x['broken']})"
        print(f"  {n:13s} {f(m)} | {f(x)}{extra}")
    print("== pinned inside vs written over arm a afterwards (err_true as measured; inside vs after fixed / broken; neighbours)")
    for tag in ("old", "new"):
        for pn, d in res["after_vs_inside"][tag].items():
            m = d["inside_vs_after"]["as_measured"]
            print(f"  {tag} {pn:5s} after {f(d['after']['as_measured'])} inside {f(d['inside']['as_measured'])} | {m['fixed']} / {m['broken']} | "
                  f"neighbours {len(d['neighbours_moved'])} {d['neighbours_moved']}")
    print("== naive wrong on the 26 lattice lines (random-pin control's count)", res["naive_lattice_wrong"])
    print("== X20 changed positions")
    for tag, rows in res["x20_changes"].items():
        for r in rows:
            print(f"  {tag} {r}")



if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""R14-RJMTQ (6 Oct 2026): pool the f.194, f.199, f.40 and f.147b alignments for T/Q chunk counts; gate witness/PREREG_tq.md.

f.194/f.199 alignments are regenerated with scripts/test1.py's own align() (unchanged); f.40 and f.147b are read from
passes/align_f40_f42.tsv and passes/align_f147b.tsv. Control: random symbol positions per page, chunks fixed (1000 seeds).

  python3 scripts/pool_tq.py [--check]     (--check: exit 1 if results_pool_tq.json differs from a rerun)
"""
import argparse, csv, importlib.util, json, random, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
spec = importlib.util.spec_from_file_location("t1", HERE / "scripts/test1.py")
t1 = importlib.util.module_from_spec(spec)
spec.loader.exec_module(t1)
fold = t1.ia.fold
SEEDS = 1000


def pages():
    key = t1.load_key()
    out = {}
    for page, gl in (("f194", ["gloss_f197.tsv", "passes/gloss_f197_rest.tsv"]), ("f199", ["passes/gloss_f201.tsv"])):
        rec, *_ = t1.reconcile(t1.load_pass(page, "A"), t1.load_pass(page, "B"), key)
        raw, kinds, chunks, _, _ = t1.align(rec, t1.gloss_text([HERE / g for g in gl]), key)
        out[page] = [(t[1:], fold(c)) for t, k, c in zip(raw, kinds, chunks) if k == "sym"]
    for page, f in (("f40", "passes/align_f40_f42.tsv"), ("f147b", "passes/align_f147b.tsv")):
        with open(HERE / f) as fh:
            out[page] = [(r["token"][1:], fold(r["chunk"] or "")) for r in csv.DictReader(fh, delimiter="\t") if r["kind"] == "sym"]
    return out


def top(chunks):
    c = Counter(x for x in chunks if x)
    return sorted(c.items(), key=lambda kv: (-kv[1], kv[0]))[0] if c else ("", 0)


def null(P, pool, lab, fixed=None):
    vals = []
    for s in range(1, SEEDS + 1):
        rng = random.Random(s)
        draw = []
        for p in pool:
            n = sum(1 for l, _ in P[p] if l == lab)
            draw += [c for _, c in rng.sample(P[p], n)]
        h = sum(1 for c in draw if c == fixed) if fixed is not None else top(draw)[1]
        vals.append(h / len(draw) if draw else 0.0)
    vals.sort()
    return {"mean": round(sum(vals) / len(vals), 4), "p95": round(vals[int(0.95 * len(vals)) - 1], 4), "max": round(vals[-1], 4)}


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    P = pages()
    res = {"sym_tokens": {p: len(v) for p, v in P.items()}, "labels": {}}
    for lab in ("T", "Q", "K"):
        res["labels"][lab] = {p: {"n": sum(1 for l, _ in P[p] if l == lab),
                                   "chunks": dict(sorted(Counter(c or "-" for l, c in P[p] if l == lab).items(), key=lambda kv: (-kv[1], kv[0])))}
                              for p in P}
    gates = {}
    for lab, pool in (("T", ["f199", "f40", "f147b"]), ("Q", ["f194", "f199", "f40", "f147b"])):
        ch = [c for p in pool for l, c in P[p] if l == lab]
        v, h = top(ch)
        npages = sum(1 for p in pool if top([c for l, c in P[p] if l == lab])[0] == v)
        ctl = null(P, pool, lab)
        g = {"pool": pool, "value": v, "h": h, "n": len(ch), "share": round(h / len(ch), 4) if ch else 0.0,
             "pages_top": npages, "control": ctl}
        g["verdict"] = ("NON-TEST (n<8)" if len(ch) < 8 else
                        "PASS" if g["share"] > ctl["p95"] and h >= 4 and npages >= 2 else "FAIL")
        gates[lab + "_free"] = g
    for lab, val, pool in (("T", "s", ["f199", "f40", "f147b"]), ("T", "d", ["f199", "f40", "f147b"]),
                           ("Q", "y", ["f194", "f199", "f40", "f147b"])):
        ch = [(p, c) for p in pool for l, c in P[p] if l == lab]
        h = sum(1 for _, c in ch if c == val)
        pg = len({p for p, c in ch if c == val})
        ctl = null(P, pool, lab, fixed=val)
        g = {"pool": pool, "value": val, "h": h, "n": len(ch), "share": round(h / len(ch), 4) if ch else 0.0,
             "pages_hit": pg, "control": ctl}
        g["verdict"] = ("NON-TEST (n<8)" if len(ch) < 8 else
                        "PASS" if g["share"] > ctl["p95"] and h >= 3 and pg >= 2 else "FAIL")
        gates["%s_eq_%s" % (lab, val)] = g
    kp = [p for p in P if any(l == "K" for l, _ in P[p])]
    kc = [c for p in kp for l, c in P[p] if l == "K"]
    res["K_reference"] = {"pages": kp, "n": len(kc), "y": sum(1 for c in kc if c == "y")}
    res["gates"] = gates
    out = json.dumps(res, indent=1, sort_keys=True) + "\n"
    f = HERE / "results_pool_tq.json"
    if a.check:
        ok = f.exists() and f.read_text() == out
        print("check:", "OK" if ok else "STALE")
        sys.exit(0 if ok else 1)
    f.write_text(out)
    print(out)


if __name__ == "__main__":
    main()

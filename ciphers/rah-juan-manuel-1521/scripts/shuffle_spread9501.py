#!/usr/bin/env python3
"""Shuffled-order control spread for the R9501 f.34 trial decode (R13-RJMV verifier, 6 Oct 2026; PREREG-R13-RJMV.md).

Re-uses scripts/decode9501.py unchanged (reconcile, decode_tok, render); shuffles the reconciled tokens with random.Random(seed) for
seeds 1-20 (seed 1 reproduces reading_f34_shuffled.txt byte for byte) and scores each, and the target (column 2 of
reading_f34_tomokiyo.txt), with tools/judge_plaintext.py on es1600 (a spec copy with judge.language=es1600) and on the spec's es17c.
Writes results_shuffle_spread9501.json.

  python3 ciphers/rah-juan-manuel-1521/scripts/shuffle_spread9501.py [--check]    run from the repository root; ~3 min
"""
import argparse, importlib.util, json, random, re, statistics, subprocess, sys, tempfile
from pathlib import Path

H = Path(__file__).resolve().parent.parent
ROOT = H.parent.parent
sp = importlib.util.spec_from_file_location("d", H / "scripts/decode9501.py")
d = importlib.util.module_from_spec(sp)
sp.loader.exec_module(d)
SEEDS = range(1, 21)


def judge(spec, f):
    o = subprocess.run([sys.executable, str(ROOT / "tools/judge_plaintext.py"), str(spec), "--file", str(f)],
                       capture_output=True, text=True, cwd=ROOT).stdout
    return float(re.search(r"language: score=(-?[\d.]+)", o).group(1))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    key, alp = d.t1.load_key(), d.alpha()
    rec, *_ = d.t1.reconcile(d.load("A"), d.load("B"), key)
    flat = [x for n in sorted(rec) for x in rec[n]]
    tmp = Path(tempfile.mkdtemp())
    spec = json.load(open(ROOT / "specs/rah-juan-manuel-1521.json"))
    spec["judge"]["language"] = "es1600"
    (tmp / "spec_es1600.json").write_text(json.dumps(spec))
    specs = {"es1600": tmp / "spec_es1600.json", "es17c": ROOT / "specs/rah-juan-manuel-1521.json"}
    tgt = tmp / "target.txt"
    tgt.write_text("".join(l.split("\t", 1)[1] for l in open(H / "reading_f34_tomokiyo.txt") if not l.startswith("#")))
    res = {"seeds": list(SEEDS), "target": {k: judge(s, tgt) for k, s in specs.items()}, "shuffled": {k: [] for k in specs}}
    for seed in SEEDS:
        sh = flat[:]
        random.Random(seed).shuffle(sh)
        toks = [(d.decode_tok(t, st, key, alp)[0], d.decode_tok(t, st, key, alp)[2]) for t, st in sh]
        txt = "# control: reconciled f.34 tokens in random order (seed %d), same key\n%s\n" % (seed, d.render(toks))
        if seed == 1 and txt != (H / "reading_f34_shuffled.txt").read_text():
            sys.exit("seed 1 does not reproduce reading_f34_shuffled.txt")
        f = tmp / ("shuf_%02d.txt" % seed)
        f.write_text(txt)
        for k, s in specs.items():
            res["shuffled"][k].append(judge(s, f))
    summ = {}
    for k, v in res["shuffled"].items():
        t, sd = res["target"][k], statistics.stdev(v)
        summ[k] = {"min": min(v), "mean": round(statistics.mean(v), 4), "max": max(v), "sd": round(sd, 4), "target": t,
                   "target_above_all": t > max(v), "z_vs_mean": round((t - statistics.mean(v)) / sd, 2),
                   "z_vs_max": round((t - max(v)) / sd, 2)}
    res["summary"] = summ
    out = json.dumps(res, indent=1, sort_keys=True) + "\n"
    p = H / "results_shuffle_spread9501.json"
    if a.check:
        ok = p.exists() and p.read_text() == out
        print("up to date" if ok else "STALE")
        sys.exit(0 if ok else 1)
    p.write_text(out)
    print(json.dumps(summ, indent=1))


if __name__ == "__main__":
    main()

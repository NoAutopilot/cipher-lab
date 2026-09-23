#!/usr/bin/env python3
"""Run the control and target searches for Dupuy 468 f.28 and log every run to ../runs.tsv (step 4).
Written 23 Sept 2026. Usage: python3 runs.py MODEL.npz [RUN ...]   (default: all runs)
Solver: tools/nomenclator_anneal.py solve, the same settings SET for every run.
Control accuracy: nomenclator_anneal eval against control.truth.json. Target 'agreement': share of
letter-sign tokens whose searched value equals the gloss-derived value in ../key.tsv.
"""
import datetime
import json
import os
import random
import subprocess
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TOOL = os.path.join(HERE, "..", "..", "..", "tools", "nomenclator_anneal.py")
SET = "--restarts 16 --iters 300000 --syl none --max-word 0 --max-null 2 --max-homo 2 --max-syl 0".split()


def gloss_key():
    k = {}
    for l in open(os.path.join(HERE, "..", "key.tsv"), encoding="utf-8"):
        p = l.rstrip("\n").split("\t")
        if l.startswith("#") or p[0] == "token" or len(p) < 3:
            continue
        if not p[1].startswith("="):
            k[p[0]] = p[1]
    return k


def reveal_fix(frac, seed=7):
    """Signs revealed by a random frac of the control's tokens (the target's glossed fraction)."""
    t = json.load(open(os.path.join(HERE, "control.truth.json")))
    toks = [(l, v) for pairs in t["texts"].values() for l, v in pairs if l]
    rng = random.Random(seed)
    shown = rng.sample(toks, int(round(frac * len(toks))))
    fix = sorted({f"{l}={v}" for l, v in shown if v})
    return fix


def run(name, model, files, extra, truth=None, target=False):
    out = os.path.join(HERE, "runs", name + ".json")
    cmd = [sys.executable, TOOL, "solve", *files, "--model", model, *SET, *extra, "--out", out]
    t0 = datetime.datetime.utcnow()
    subprocess.run(cmd, check=True, cwd=HERE, stdout=subprocess.DEVNULL)
    dt = (datetime.datetime.utcnow() - t0).seconds
    r = json.load(open(out))
    best = r["best"]
    at_best = sum(1 for s in r["scores"] if abs(s - r["scores"][0]) < 1e-6)
    acc = ""
    if truth:
        e = subprocess.run([sys.executable, TOOL, "eval", out, truth], capture_output=True, text=True, cwd=HERE)
        ev = json.loads(e.stdout)
        acc = f"tok={ev['token_acc']:.3f} let={ev['letter_acc']:.3f}"
    if target:
        gk, key = gloss_key(), best["key"]
        n = ok = 0
        for l in open(os.path.join(HERE, "target_anneal.txt"), encoding="utf-8"):
            if l.startswith("#"):
                continue
            import re
            for t in re.sub(r"\{.*?\}", " ", l).split():
                if t in gk:
                    n += 1
                    ok += key.get(t) == gk[t]
        acc = f"agree_with_gloss_key={ok}/{n}={ok / n:.3f}"
    head = " ".join(txt[:160] for _, txt in best["reading"])
    fixn = sum(1 for x in extra if "=" in x)
    row = [datetime.date.today().isoformat(), name, "+".join(os.path.basename(f) for f in files),
           " ".join(SET + [x for x in extra if not x.startswith("S") and "=" not in x and x != "--fix"]) + (f" fixed={fixn}" if fixn else ""),
           f"{r['scores'][0]:.1f}", f"{r['per_token']:.3f}", f"{at_best}/{len(r['scores'])}", acc, f"{dt}s", head]
    p = os.path.join(HERE, "..", "runs.tsv")
    new = not os.path.exists(p)
    with open(p, "a", encoding="utf-8") as f:
        if new:
            f.write("date\trun\tfiles\tsettings\tbest_score\tscore_per_token\trestarts_at_best\taccuracy\ttime\tbest_reading_head\n")
        f.write("\t".join(row) + "\n")
    print("\t".join(row[1:9]))


def main():
    model = sys.argv[1]
    want = set(sys.argv[2:])
    frac = float(open(os.path.join(HERE, "reveal.txt")).read())
    gk = gloss_key()
    tfix = []
    for t, v in gk.items():
        tfix += ["--fix", f"{t}={v}"]
    cfix = []
    for f in reveal_fix(frac):
        cfix += ["--fix", f]
    ctl, tgt = ["control.txt"], ["target_anneal.txt"]
    plan = [("C1-blind", ctl, [], "control.truth.json", False),
            ("C1-blind-shuffled1", ctl, ["--shuffle", "1"], None, False),
            ("C1-revealed", ctl, cfix, "control.truth.json", False),
            ("T-blind", tgt, [], None, True),
            ("T-blind-shuffled1", tgt, ["--shuffle", "1"], None, False),
            ("T-glossfixed", tgt, tfix, None, True)]
    for name, files, extra, truth, target in plan:
        if want and name not in want:
            continue
        run(name, model, files, extra, truth, target)


if __name__ == "__main__":
    main()

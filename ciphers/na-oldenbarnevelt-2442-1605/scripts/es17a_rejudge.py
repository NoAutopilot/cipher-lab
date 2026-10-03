#!/usr/bin/env python3
"""OLD-ES17A (3 Oct 2026): re-judge the committed B/C1 reading and shuffled-target decodes under es17a and es17c.

Pre-registered in transcription/PREREG_OLD-ES17A.md. Writes nothing in the repo except --outdir (default: a temp dir);
prints one judge line per (text, corpus). Run from the target folder:
  python3 scripts/es17a_rejudge.py [--outdir DIR] [--langs es17a es17c] [--solver-restarts 4]
"""
import argparse, csv, json, os, random, re, subprocess, sys, tempfile

HERE = os.path.dirname(os.path.abspath(__file__)); TGT = os.path.dirname(HERE); ROOT = os.path.dirname(os.path.dirname(TGT))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from judge_plaintext import judge  # noqa: E402

CORPUS = "corpus/es16-donquijote/donquijote1605_pg2000_body.txt"


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--outdir"); ap.add_argument("--langs", nargs="+", default=["es17a", "es17c"])
    ap.add_argument("--solver-restarts", type=int, default=4)
    a = ap.parse_args()
    out = a.outdir or tempfile.mkdtemp(); os.makedirs(out, exist_ok=True)
    rows = list(csv.DictReader(open(os.path.join(TGT, "reading_tokens.tsv"), encoding="utf-8"), delimiter="\t"))
    bc = [r for r in rows if r["block"] in ("B", "C1")]
    texts = {"BC1_reading": " ".join(r["value"] for r in bc),
             "whole_reading": open(os.path.join(TGT, "reading.txt"), encoding="utf-8").read()}
    toks = [r["raw_used"] for r in bc]; chars = [c for t in toks for c in t]
    key = json.load(open(os.path.join(TGT, "digit_key.json")))
    for seed in (1, 2, 3):
        c = chars[:]; random.Random(seed).shuffle(c); sh, i = [], 0
        for t in toks:
            sh.append("".join(c[i:i + len(t)])); i += len(t)
        texts[f"shuf{seed}_committed_key"] = " ".join("".join(key.get(ch, ch) for ch in t) for t in sh)
        clean = [re.sub(r"[^a-z0-9]", "", t.lower().replace("ç", "c").replace("ñ", "n")) for t in sh]
        tsv = os.path.join(out, f"shuf{seed}.tsv")
        with open(tsv, "w", encoding="utf-8") as f:
            f.write("block\tline\ttoken_index\traw_token\tconfidence\n")
            for j, t in enumerate(x for x in clean if x):
                f.write(f"B\t1\t{j + 1}\t{t}\thigh\n")
        js = os.path.join(out, f"shuf{seed}_solver.json")
        subprocess.run([sys.executable, os.path.join(HERE, "solve_digit_subst.py"), "target", tsv, "--corpus",
                        os.path.join(TGT, CORPUS), "--restarts", str(a.solver_restarts), "--seed", str(seed), "--out", js],
                       check=True, capture_output=True)
        texts[f"shuf{seed}_solver_key"] = json.load(open(js))["decoded_spaced"]
    base = json.load(open(os.path.join(ROOT, "specs", "na-oldenbarnevelt-2442-1605.json")))["judge"]
    for name, t in texts.items():
        open(os.path.join(out, name + ".txt"), "w", encoding="utf-8").write(t + "\n")
        for lang in a.langs:
            j = {k: v for k, v in base.items() if k != "corpora"}; j["language"] = lang; j.setdefault("control_samples", 200)
            r = judge({"judge": j}, t); L = r["checks"]["language"]; W = r["checks"].get("words", {})
            print(f"{name}\t{lang}\t{'PASS' if r['pass'] else 'FAIL'}\tscore={L.get('score')}\treal_p05={L.get('real_p05')}"
                  f"\tnull_p99={L.get('null_p99')}\tN={L.get('N')}\tcover={W.get('cover')}", flush=True)
    print(f"outdir: {out}")


if __name__ == "__main__":
    main()

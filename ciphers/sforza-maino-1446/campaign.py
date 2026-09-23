#!/usr/bin/env python3
"""Run one named solver configuration for sforza-maino-1446 and append a row to runs.tsv.

Usage: python3 campaign.py RUN_ID --model M.npz [--truth T.json ...] -- FILE... [solver options]
Options after '--' go to tools/nomenclator_anneal.py solve unchanged (FILEs first). The full result
JSON goes to runs/RUN_ID.json. 23 Sept 2026.
"""
import json
import os
import subprocess
import sys
import time

HERE = os.path.dirname(os.path.abspath(__file__))
TOOLS = os.path.join(HERE, "..", "..", "tools")
sys.path.insert(0, TOOLS)
import nomenclator_anneal as na  # noqa: E402


def main():
    argv = sys.argv[1:]
    cut = argv.index("--")
    head, rest = argv[:cut], argv[cut + 1:]
    run_id = head[0]
    model = head[head.index("--model") + 1]
    truths = []
    if "--truth" in head:
        i = head.index("--truth") + 1
        while i < len(head) and not head[i].startswith("--"):
            truths.append(head[i])
            i += 1
    os.makedirs(os.path.join(HERE, "runs"), exist_ok=True)
    out = os.path.join(HERE, "runs", run_id + ".json")
    t0 = time.time()
    cmd = [sys.executable, os.path.join(TOOLS, "nomenclator_anneal.py"), "solve"] + rest + \
        ["--model", model, "--out", out]
    subprocess.run(cmd, check=True, stdout=subprocess.DEVNULL)
    r = json.load(open(out))
    best = r["scores"][0]
    hits = sum(1 for s in r["scores"] if s >= best - 1.0)
    ev = ""
    if truths:
        truth = dict(texts={}, key={})
        for t in truths:
            tj = json.load(open(t))
            truth["texts"].update(tj["texts"])
            truth["key"].update(tj["key"])
        e = na.evaluate(r, truth)
        ev = f"tok={e['token_acc']:.3f} let={e['letter_acc']:.3f}"
    opts = " ".join(x for x in rest if not os.path.exists(x))
    reading = " || ".join(f"{n}: {t[:160]}" for n, t in r["best"]["reading"])
    row = [time.strftime("%Y-%m-%d"), run_id, "+".join(r["files"]), opts, f"{best:.1f}",
           f"{r['per_token']:.3f}", f"{hits}/{r['restarts']}", ev, f"{time.time() - t0:.0f}s", reading]
    path = os.path.join(HERE, "runs.tsv")
    new = not os.path.exists(path)
    with open(path, "a") as f:
        if new:
            f.write("date\trun\tfiles\tsettings\tbest_score\tscore_per_token\trestarts_at_best\t"
                    "control_accuracy\ttime\tbest_reading_head\n")
        f.write("\t".join(row) + "\n")
    print("\t".join(row[:9]))


if __name__ == "__main__":
    main()

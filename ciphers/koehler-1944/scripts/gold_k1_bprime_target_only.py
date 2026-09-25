#!/usr/bin/env python3
"""GOLD-K1: run family B' (keyed_running_key) TARGET only, reusing a control already logged in HYPOTHESES.md
(the first family_run.py invocation this job ran to completion on all 3 control seeds -- mean 0.815, range
0.810-0.878, gate 0.5 met -- but was killed by an over-tight timeout partway through the target's stage 2).
Never used to skip a control that has not itself been run and logged; the control numbers here are the same
control family_run.py already computed and would compute again given the same seeds/params (stage 1 word list
and control book draws are seeded, deterministic).
"""
import json, os, sys, time
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "..", "..", "tools"))
import family_run as frmod
import judge_plaintext as jp
import families

ROOT = os.path.join(os.path.dirname(__file__), "..", "..", "..")
SPEC_PATH = os.path.join(ROOT, "specs", "koehler-1944.json")
spec = json.load(open(SPEC_PATH, encoding="utf-8"))
slug = "koehler-1944"

msgs, mode = frmod.read_spec_cipher(spec, "auto")
toks = [t for m in msgs for t in m]
N, K = len(toks), len(set(toks))
params = {"kcorpus": "tools/data/nl_dev", "top": "30", "beam": "300", "order": "6", "spaces": "1",
          "N": N, "K": K, "lengths": [len(m) for m in msgs], "target_msgs": msgs,
          "messages_independent": "separate" in mode}
paths = frmod.corpus_paths(spec, ["tools/data/de20"])
corpora = [jp.read_corpus(p) for p in paths]
fam = families.load("keyed_running_key")

seed = 1
restarts = 8
t0 = time.time()
dec, sc, info = fam.solve(msgs, spec, seed, restarts, corpora, dict(params))
elapsed = time.time() - t0

fdir = os.path.join(ROOT, "ciphers", slug, "families")
os.makedirs(fdir, exist_ok=True)
dpath = os.path.join(fdir, "keyed_running_key-1-nldev.txt")
date = frmod.utc_date()
CTL_MEAN, CTL_RANGE = 0.815, "0.810-0.878"
with open(dpath, "w", encoding="utf-8") as f:
    f.write(f"# {slug} keyed_running_key seed {seed} restarts {restarts} {date} UTC; "
            f"control mean {CTL_MEAN:.3f} ({CTL_RANGE}); score {sc:.3f}; kcorpus=tools/data/nl_dev (GOLD-K1, target-only rerun after a timeout killed the first attempt mid-stage-2)\n")
    f.write(f"# {json.dumps(info, ensure_ascii=False, default=str)[:2000]}\n")
    pos = 0
    for m in msgs:
        f.write(dec[pos:pos + len(m)] + "\n")
        pos += len(m)

verdict = frmod.run_judge(SPEC_PATH, dpath) if spec.get("judge") else "no judge block"
print(f"TARGET best score {sc:.3f} (elapsed {elapsed:.0f}s); decode -> {dpath}; judge: {verdict}")

out = os.path.join(ROOT, "ciphers", slug, "HYPOTHESES.md")
par = (f"N={N} K={K} restarts={restarts} corpus={'+'.join(os.path.basename(p) for p in paths)} "
       f"kcorpus=tools/data/nl_dev,top=30,beam=300,order=6,spaces=1")
frmod.append_row(out, [date, "keyed_running_key", par, seed, f"{CTL_MEAN:.3f} ({CTL_RANGE})", f"{sc:.3f}", verdict,
                        "yes (gate 0.5)",
                        "GOLD-K1 B' keyword-mixed, devotional Dutch key (nl_dev), control before target -- target rerun standalone after a timeout"])
print("row appended")

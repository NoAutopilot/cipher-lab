#!/usr/bin/env python3
"""VERIFY-F61-V6 task 3b: H208 re-scored with the verifier's seeds and a count-preserving relabel null. Written before any call.
 control (seed 6207): the H100 one-swap hard null on f.61's known span lines, built by scripts/f61judge108v.py (build known_h51 --seed 6207
   --swap), files moved into verify_v6/; gate: the fitted map ranks 1 of 21 (ties against). A FAIL stops task 3b.
 target (seeds 6208, 6209, one call each): 21 sets of the f.108v draft (scripts/f61bowl_108v_seq.draft), the 14 cells otherwise:
   T = the runner's H199 bowl labels (yes c/p, no a/n); V = this verifier's call-2 bowl labels (v8_bowl_positions.tsv); CODE = reader code only
   (4STEM c/p, every other 4-family a/n); R = the pass codes' own cells (H85 decode); 17 random relabels giving c/p to exactly as many of the
   68 runner-answered 4-family columns as T does (19), the rest a/n (same yes/no counts), drawn with the seed. Order shuffled (seed); key never
   named. H94 no-leak target prompt, file name changed.
 read-out per seed: T's rank among all 21 and among {T + 17 random}; T vs CODE vs V vs R. "Judge prefers the runner's bowl labelling over a
   same-count random relabel" iff T ranks 1 of 18 in both seeds (ties against). Descriptive.
  python3 judge_v6.py build SEED | score SEED [--check] | control-score [--check]"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); S = os.path.abspath(f"{HERE}/../scripts"); sys.path.insert(0, S)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61bowl_108v_seq as B
import f61judge108v as J
def rd(f): return list(csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t"))
def build(seed):
    D = B.draft(); C = J.cells(); M = dict(C, **{"4BOWL": "c/p", "4NOB": "a/n"})
    run = {(r["line"], r["column"]): r["bowl"] for r in rd(f"{HERE}/../family/h199_bowl_positions.tsv")}
    ver = {(r["line"], r["column"]): r["bowl_verifier"] for r in rd(f"{HERE}/v8_bowl_positions.tsv")}
    cols = [(l, p) for l, v in D.items() for p, s in v if s in B.FAM and run.get((l, p)) in ("yes", "no")]; ny = sum(run[c] == "yes" for c in cols)
    code = {(l, p): ("yes" if s == "4STEM" else "no") for l, v in D.items() for p, s in v if s in B.FAM}
    dec = lambda L, m: {l: [m[c] for c in s if c in m] for l, s in L.items()}
    sets = [("T", dec(B.relabel(D, run), M)), ("V", dec(B.relabel(D, ver), M)), ("CODE", dec(B.relabel(D, code), M)),
            ("R", dec({l: [s for _, s in v] for l, v in D.items()}, C))]
    rng = random.Random(seed); seen = set()
    while len(sets) < 21:
        yes = frozenset(rng.sample(cols, ny))
        if yes in seen: continue
        seen.add(yes); sets.append((f"random{len(sets) - 3}", dec(B.relabel(D, {c: ("yes" if c in yes else "no") for c in cols}), M)))
    order = list(range(21)); random.Random(seed).shuffle(order); key = {}; txt = []
    for k, i in enumerate(order):
        lab = f"SET-{k + 1:02d}"; key[lab] = sets[i][0]; txt.append(f"== {lab}")
        for l, cells in sets[i][1].items(): txt.append(f"{l}: " + " ".join(f"[{c}]" for c in cells))
    open(f"{HERE}/judge_v6_s{seed}_sets.txt", "w").write("\n".join(txt) + "\n"); json.dump({"seed": seed, "key": key}, open(f"{HERE}/judge_v6_s{seed}_key.json", "w"), indent=1)
    print("built", seed, {k: v for k, v in key.items() if not v.startswith("random")})
def score(seed):
    key = json.load(open(f"{HERE}/judge_v6_s{seed}_key.json"))["key"]; rows = rd(f"{HERE}/judge_v6_s{seed}_verdict.tsv")
    sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}; assert set(sc) == set(key)
    lab = {v: k for k, v in key.items()}; t = sc[lab["T"]]
    rnd = [sc[k] for k, v in key.items() if v.startswith("random")]
    out = [f"seed {seed}: T {t:.1f}, V {sc[lab['V']]:.1f}, CODE {sc[lab['CODE']]:.1f}, R {sc[lab['R']]:.1f}; random relabels (17, same yes/no counts) max {max(rnd):.1f} median {sorted(rnd)[8]:.1f}",
           f"  T rank among all 21 {1 + sum(v >= t for k, v in sc.items() if k != lab['T'])}; among T + 17 random {1 + sum(v >= t for v in rnd)} of 18 (ties against)",
           "  all: " + " ".join(f"{key[l]}:{sc[l]:.1f}" for l in sorted(sc, key=lambda l: -sc[l]))]
    return "\n".join(out)
def control_score():
    key = json.load(open(f"{HERE}/judge_v6_ctl_s6207_key.json")); key = key.get("key", key)
    rows = rd(f"{HERE}/judge_v6_ctl_s6207_verdict.tsv"); sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}
    t = [l for l, v in key.items() if v == 0][0]
    rank = 1 + sum(v >= sc[t] for l, v in sc.items() if l != t)
    return f"control (known f.61 span lines, one-swap null, seed 6207): fitted map {t} {sc[t]:.1f}, rank {rank} of 21 -> {'PASS' if rank == 1 else 'CONTROL FAIL'}"
def emit(txt, p):
    if "--check" in ARGS:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    if ARGS[0] == "build": build(int(ARGS[1]))
    elif ARGS[0] == "control-score": emit(control_score() + "\n", f"{HERE}/judge_v6_ctl_s6207_result.txt")
    else: emit(score(int(ARGS[1])) + "\n", f"{HERE}/judge_v6_s{ARGS[1]}_result.txt")

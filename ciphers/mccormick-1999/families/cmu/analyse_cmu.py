"""analyse_cmu.py -- MCC-CMU (15 Oct 2026): criteria of PREREG-MCC-CMU.md on cmu.json (control + target, nulls a/b) and
ncbe_cmu.json (null c), the plain-pool comparison against MCC-JUDGE's 200-draw tm null (../judge/ncbe_null.json), and
the judge renderings A/B of the target and of shuffled draws 6000 (type-mark, re-fitted here: deterministic) and 7000
(NCBE-fixed). Adapted from ../gregg/analyse_gregg.py (pool unfiltered, phonetic key). Usage: python3 analyse_cmu.py"""
import json, random, statistics as st, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent / "judge"))
from ncbe_null import render, T  # noqa: E402

g = json.load(open(HERE / "cmu.json")); c = json.load(open(HERE / "ncbe_cmu.json"))
plain = json.load(open(HERE.parent / "judge" / "ncbe_null.json"))
ctl = g["controls"]["132"]
res = {"control": {"read": ctl["read"], "word_recovery_mean": ctl["word_recovery_mean"],
                   "seeds": [{k: r[k] for k in ("seed", "word_recovery", "mark_map_recovery", "coverage",
                                                "typemark_null_coverage_max")} for r in ctl["runs"]]}}
t = g["target"]
if isinstance(t, str):
    res["target"] = t
    print(json.dumps(res, indent=1)); sys.exit(0)
assert abs(c["target"]["coverage"] - t["coverage"]) < 1e-9, "target refit differs between the two runs"
nulls = {"a_type": (t["type_null_coverage"], t["type_null_spl"]),
         "b_typemark": (t["typemark_null_coverage"], t["typemark_null_spl"]),
         "c_ncbe": ([r["coverage"] for r in c["ncbe"]], [r["spl"] for r in c["ncbe"]])}
tv = {"coverage": t["coverage"], "spl": t["score_per_letter"]}
rows = {}
for name, (nc, ns) in nulls.items():
    for stat, xs in (("coverage", nc), ("spl", ns)):
        rows[f"{name}.{stat}"] = {"target": tv[stat], "mean": st.mean(xs), "sd": st.pstdev(xs), "max": max(xs),
                                  "n": len(xs), "p": (1 + sum(x >= tv[stat] for x in xs)) / (len(xs) + 1),
                                  "z": (tv[stat] - st.mean(xs)) / st.pstdev(xs)}
res["target"] = {"coverage": t["coverage"], "spl": t["score_per_letter"], "fitted_map": t["fitted_map"], "nulls": rows}
above_all = all(rows[k]["target"] > rows[k]["max"] for k in rows)
above_a = rows["a_type.coverage"]["target"] > rows["a_type.coverage"]["max"] and rows["a_type.spl"]["target"] > rows["a_type.spl"]["max"]
neg = above_a and any(rows[f"{n}.coverage"]["p"] >= 0.05 and rows[f"{n}.spl"]["p"] >= 0.05 for n in ("b_typemark", "c_ncbe"))
res["outcome"] = ("stems fit beyond type, type-mark and NCBE-fixed nulls" if above_all else
                  "negative: stems do not fit beyond a mark/NCBE-keeping shuffle" if neg else "mixed")
pt = plain["target"]
pz = {}
for stat in ("coverage", "spl"):
    xs = [r[stat] for r in plain["tm"]]
    pz[stat] = (pt[stat] - st.mean(xs)) / st.pstdev(xs)
gz = {"coverage": rows["b_typemark.coverage"]["z"], "spl": rows["b_typemark.spl"]["z"]}
res["plain_vs_phonetic_z_typemark"] = {"plain": pz, "phonetic": gz,
                                    "word": "better" if all(gz[s] > pz[s] for s in gz) else
                                    "worse" if all(gz[s] < pz[s] for s in gz) else "no difference in kind"}
print(json.dumps(res, indent=1))
(HERE / "analysis.json").write_text(json.dumps(res, indent=1))
# judge renderings
T.load_phonetic(HERE / "cmudict_subset.dict")
wb = T.WordBigram(T.corpus_words_from(T.HELDOUT_EN), 3000)
toks = T.tokenize(T.CIPHER_FILE.read_text())
d6000 = T.fit_marks(wb, T.shuffle_types(toks, random.Random(6000), keep_marks=True), 3.0, 200)[1]
dec = {"target": t["decode"], "tm6000": d6000["decode"],
       "ncbe7000": next(r for r in c["ncbe"] if r["seed"] == 7000)["decode"]}
for name, s in dec.items():
    for tag, ro in (("A", False), ("B", True)):
        (HERE / f"render_{name}_{tag}.txt").write_text(render(s, ro) + "\n")
print("draw 6000 refit coverage", d6000["coverage"], "in null (b) list:", d6000["coverage"] in t["typemark_null_coverage"])

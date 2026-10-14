#!/usr/bin/env python3
"""SALV-LKEY (14 Oct 2026): rule-3 control for Lasry's published key on our transcription (PREREG-SALV-LKEY.md).
Reads lkey/ciphertext_lasry.tsv and lkey/key_lasry.tsv (sign, value, grade, class, ...). Target text = cipher tokens only,
keyed tokens' values concatenated within a sign run, runs separated by a space, unread tokens dropped. Control = the same
with values permuted within class (letter / syllable / other), --draws keys, seed 1. Scored with judge_plaintext's NgramModel
(spec judge corpora, it16) on the same folded letters. Writes lkey/score.json and lkey/cipher_runs_lasry.txt; per leaf too."""
import csv, json, os, random, sys
from collections import defaultdict
D = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(os.path.dirname(os.path.dirname(D)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import judge_plaintext as J
draws = int(sys.argv[sys.argv.index("--draws") + 1]) if "--draws" in sys.argv else 300
allkey = {r["sign"]: r for r in csv.DictReader(open(os.path.join(D, "key_lasry.tsv"), encoding="utf-8"), delimiter="\t")}
# SALV-TRY (14 Oct 2026): --set SIGN=VALUE[,...] overrides values in memory (key_lasry.tsv never written); --out FILE writes the
# result there instead of score.json and skips cipher_runs/judge_input (so SALV-LKEY's committed outputs stay as they are).
sets = dict(p.split("=", 1) for p in sys.argv[sys.argv.index("--set") + 1].split(",")) if "--set" in sys.argv else {}
out = sys.argv[sys.argv.index("--out") + 1] if "--out" in sys.argv else None
for s_, v_ in sets.items(): allkey[s_] = dict(allkey[s_], value=v_)
# SALV-EYE (14 Oct 2026, PREREG-SALV-EYE.md 5): --drop SIGN[,...] removes rows in memory (the sign goes unread), with any
# combination row SIGN|... as in map3/ablate.py; key_lasry.tsv is never written. Use with --out.
drops = sys.argv[sys.argv.index("--drop") + 1].split(",") if "--drop" in sys.argv else []
allkey = {s_: r_ for s_, r_ in allkey.items() if not any(s_ == d_ or s_.startswith(d_ + "|") for d_ in drops)}
key = {s: r for s, r in allkey.items() if r["class"] != "amb"}  # ambiguous a|b rows graded M, not read (PREREG 1)
toks = list(csv.DictReader(open(os.path.join(D, "ciphertext_lasry.tsv"), encoding="utf-8"), delimiter="\t"))
runs, cur, prev = [], [], None   # runs of (leaf, sign)
for t in toks:
    if t["line"] != prev and cur:
        runs.append(cur); cur = []
    prev = t["line"]
    if t["sign"].startswith("w:"):
        if cur: runs.append(cur); cur = []
    else:
        cur.append((t["line"][:4], t["sign"]))
if cur: runs.append(cur)
def text(k, leaf=None):
    return " ".join("".join(k[s] for lf, s in r if s in k) for r in runs if leaf is None or r[0][0] == leaf).strip()
base = {s: r["value"] for s, r in key.items()}
spec = json.load(open(os.path.join(ROOT, "specs", "fr2933-salviati-1525.json"), encoding="utf-8"))
model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA[spec["judge"]["language"]]])
words4 = {w for w in model.words if len(w) >= 4}
def wordcount(s):
    s = J.fold(s); return sum(1 for i in range(len(s)) for L in range(4, min(12, len(s) - i) + 1) if s[i:i + L] in words4)
classes = defaultdict(list)
for s, r in key.items(): classes[r["class"]].append(s)
rnd = random.Random(1)
leaves = sorted({lf for r in runs for lf, _ in r})
def scores(k):
    out = {"all": model.score(text(k)), "words": wordcount(text(k))}
    for lf in leaves: out[lf] = model.score(text(k, lf))
    return out
tgt = scores(base); ctl = defaultdict(list)
for _ in range(draws):
    k = dict(base)
    for c, ss in classes.items():
        vals = [base[s] for s in ss]; rnd.shuffle(vals); k.update(zip(ss, vals))
    for n, v in scores(k).items(): ctl[n].append(v)
p99 = lambda xs: sorted(xs)[min(len(xs) - 1, int(0.99 * (len(xs) - 1)))]
tot = defaultdict(int); mapped = defaultdict(int); amb = defaultdict(int)
for r in runs:
    for lf, s in r:
        tot[lf] += 1; mapped[lf] += s in key; amb[lf] += s in allkey and s not in key
res = {"draws": draws, "target": {n: round(v, 4) for n, v in tgt.items()},
       "control_p99": {n: round(p99(v), 4) for n, v in ctl.items()},
       "control_mean": {n: round(sum(v) / len(v), 4) for n, v in ctl.items()},
       "rank_above": {n: sum(1 for x in ctl[n] if x >= tgt[n]) for n in tgt},
       "mapped_share": {lf: f"{mapped[lf]}/{tot[lf]}" for lf in leaves},
       "mapped_all": f"{sum(mapped.values())}/{sum(tot.values())}", "ambiguous_M": {lf: amb[lf] for lf in leaves}, "letters": len(J.fold(text(base)))}
if out:
    res["set"] = sets; json.dump(res, open(out, "w"), indent=1); print(json.dumps(res, indent=1)); sys.exit(0)
open(os.path.join(D, "cipher_runs_lasry.txt"), "w", encoding="utf-8").write(
    "\n".join(f"{r[0][0]}: " + "".join(base.get(s, ".") for _, s in r) for r in runs) + "\n")
open(os.path.join(D, "judge_input_lasry.txt"), "w", encoding="utf-8").write(text(base).replace(" ", "\n") + "\n")
json.dump(res, open(os.path.join(D, "score.json"), "w"), indent=1)
print(json.dumps(res, indent=1))

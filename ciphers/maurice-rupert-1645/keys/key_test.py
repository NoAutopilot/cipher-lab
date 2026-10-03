#!/usr/bin/env python3
"""GAPS52, 3 Oct 2026: test the DECODE 9119 and 9117 key forms on Maurice to Rupert, 7 July 1645 (rule 3).

usage: key_test.py KEYNAME [--check]     (KEYNAME = key9119 | key9117; reads keys/KEYNAME.tsv)

Applies keys/KEYNAME.tsv (code, value; '[null]' = null, '' = blank on the form) to the 93 cipher codes of ct118.tsv.
Statistics: coverage (cipher tokens whose code has a value on the form), the en16_repo 4-gram score and word cover of
the rendered letters/words (as key118_test.py). Control: 1000 keys in which the value column is permuted over ALL
code slots 1..N_FORM (blanks included, seed 52), so coverage, score and cover all can vary under the control -- a
shuffle among the filled rows only could not move coverage (rule 3, orthogonal control). A second, banded control
permutes values only within each block of 100 codes (the form fills letters in 1-100 by design, and the all-slot
shuffle would credit any key with that design for the target's low codes). Power control: 50 synthetic letters
(en16_repo passages) enciphered with KEYNAME itself (random homophone per letter, word code where the key has the
word, unkeyed letters given unused codes), truncated to the target's token count, then key rows blanked at random
until coverage is at most the target's own; each is ranked against 200 banded shuffles of its own key (seed 520+i);
power = share ranking above that control's p95 on 4-gram. Writes keys/KEYNAME_test.tsv;
--check exits non-zero if it is stale (rule 7)."""
import csv, json, random, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent; TGT = HERE.parent; ROOT = TGT.parents[1]
sys.path.insert(0, str(ROOT / "tools")); import judge_plaintext as jp
name = sys.argv[1]; N_FORM = 600; DRAWS = 1000
rows = [r for r in csv.DictReader((l for l in open(HERE / f"{name}.tsv") if not l.startswith("#")), delimiter="\t")]
key = {int(r["code"]): r["value"] for r in rows if r["value"]}
ct = [l.split("\t")[2] for l in open(TGT / "ct118.tsv") if not l.startswith(("#", "line"))]
codes = [int(s) for s in ct if s.isdigit()]
def render(k): return "".join(k[c].replace("_", "") for c in codes if c in k and k[c] != "[null]")
def cov(k): return sum(1 for c in codes if c in k)
spec = json.load(open(TGT / "judge_key118.json")); spec["judge"]["corpora"] = [str(ROOT / p) for p in spec["judge"]["corpora"]]
model = jp.NgramModel([jp.read_corpus(pathlib.Path(p)) for p in spec["judge"]["corpora"]])
txt = render(key); sc, cv, cg = model.score(txt), model.cover(txt), cov(key)
slots = list(range(1, N_FORM + 1)); vals = [key.get(s, "") for s in slots]; rnd = random.Random(52); ctl = []
for _ in range(DRAWS):
    v = vals[:]; rnd.shuffle(v); k = {s: x for s, x in zip(slots, v) if x}; t = render(k)
    ctl.append((model.score(t) if t else -9.0, model.cover(t) if t else 0.0, cov(k)))
out = "stat\ttarget\tshuffled_key_mean\tshuffled_key_p95\trank_of_%d\n" % (DRAWS + 1)
for i, (lab, val, fmt) in enumerate([("4gram", sc, ".3f"), ("word_cover", cv, ".3f"), ("coverage_tokens", cg, "d")]):
    s = sorted(x[i] for x in ctl); rank = 1 + sum(1 for x in s if x > val)
    out += f"{lab}\t{val:{fmt}}\t{sum(s)/DRAWS:.3f}\t{jp.pct(s,0.95):.3f}\t{rank}\n"
def banded(src, r):
    out = {}
    for b in range(0, N_FORM, 100):
        sl = list(range(b + 1, b + 101)); v = [src.get(x, "") for x in sl]; r.shuffle(v)
        out.update({x: y for x, y in zip(sl, v) if y})
    return out
rb = random.Random(53); ctlb = []
for _ in range(DRAWS):
    k = banded(key, rb); t = render(k); ctlb.append((model.score(t) if t else -9.0, model.cover(t) if t else 0.0, cov(k)))
for i, (lab, val, fmt) in enumerate([("4gram_banded", sc, ".3f"), ("word_cover_banded", cv, ".3f"), ("coverage_banded", cg, "d")]):
    s_ = sorted(x[i] for x in ctlb); rank = 1 + sum(1 for x in s_ if x > val)
    out += f"{lab}\t{val:{fmt}}\t{sum(s_)/DRAWS:.3f}\t{jp.pct(s_,0.95):.3f}\t{rank}\n"
import re
corpus = " ".join(jp.read_corpus(pathlib.Path(p)) for p in spec["judge"]["corpora"][:3]).lower()
words = re.findall(r"[a-z]+", corpus); inv = {}
for c, v in key.items():
    if v != "[null]": inv.setdefault(v.lower(), []).append(c)
free = [c for c in range(1, N_FORM + 1) if c not in key]; hits = 0
for i in range(50):
    r = random.Random(520 + i); st = r.randrange(len(words) - 200); syn = []; fk = dict(key); fi = 0; spare = {}
    for w in words[st:st + 200]:
        if w in inv and len(w) > 1: syn.append(r.choice(inv[w])); continue
        for ch in w:
            if ch in inv: syn.append(r.choice(inv[ch]))
            else:
                if ch not in spare: spare[ch] = free[fi]; fi += 1
                syn.append(spare[ch])
    syn = syn[:len(codes)]
    kk = dict(key); ks = list(kk); r.shuffle(ks)
    while sum(1 for c in syn if c in kk) > cg and ks: kk.pop(ks.pop())
    rs = lambda k: "".join(k[c].replace("_", "") for c in syn if c in k and k[c] != "[null]")
    t0 = rs(kk); s0 = model.score(t0) if t0 else -9.0
    cs = sorted((lambda t: model.score(t) if t else -9.0)(rs(banded(kk, r))) for _ in range(200))
    hits += s0 > jp.pct(cs, 0.95)
out += f"power_4gram_vs_banded_p95\t{hits}/50 synthetic at coverage <= {cg}\t\t\t\n"
j = jp.judge(spec, txt)["checks"]["language"] if len(txt) >= 20 else None
out += (f"judge\tscore {j['score']}\treal_p05 {j['real_p05']}\tnull_p99 {j['null_p99']}\t{'PASS' if j['pass'] else 'FAIL'} N={j['N']}\n"
        if j else f"judge\tnot run: rendered text {len(txt)} chars < 20\t\t\t\n")
out += f"rendered\t{txt}\t\t\t\n"
f = HERE / f"{name}_test.tsv"
if "--check" in sys.argv:
    ok = f.exists() and f.read_text() == out; print(f"{f.name} up to date" if ok else "STALE"); sys.exit(0 if ok else 1)
f.write_text(out); print(out)

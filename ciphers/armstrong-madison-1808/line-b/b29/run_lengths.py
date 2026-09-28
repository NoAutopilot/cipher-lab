"""Line B step B29 -- run lengths (glyphs per fragment, codex glyphs.txt = Tomokiyo's segmentation, 28 fragments)
against (a) function-word stretches of en18 text in letters and (b) proper-name stretches in letters (capitalised
words not at sentence start, from the raw en18 volumes). Band = 60 samples of 28 stretches each per reading."""
import gzip, random, re, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent; REPO = HERE.parents[3]
runs = [len(l.strip().split(';')) for l in open(REPO / "ciphers/armstrong-madison-1808/codex-2026-09-27b/glyphs.txt") if l.strip()]
print("target runs:", sorted(runs), "n", len(runs), "mean %.2f" % (sum(runs)/len(runs)), "share>12 %.2f" % (sum(1 for r in runs if r > 12)/len(runs)))
texts = []
for p in sorted((REPO / "tools/data/en18").glob("*.txt.gz")):
    t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read(); n = len(t); texts.append(t[int(n*0.1):int(n*0.9)])
words_all = [w.lower() for t in texts for w in re.findall(r"[A-Za-z]+", t)]
func = set(w for w, _ in Counter(words_all).most_common(99))
def stretches(t, kind):
    toks = re.findall(r"[A-Za-z]+|[.!?]", t); out = []; cur = 0; prev_end = True
    for w in toks:
        if w in ".!?": 
            if cur: out.append(cur); cur = 0
            prev_end = True; continue
        is_f = w.lower() in func; is_n = w[0].isupper() and not prev_end and w.lower() not in func
        hit = is_f if kind == "func" else is_n
        if hit: cur += len(w)
        elif cur: out.append(cur); cur = 0
        prev_end = False
    return out
def band(kind):
    rng = random.Random(3); rows = []
    for _ in range(60):
        t = rng.choice(texts); s = rng.randint(0, len(t) - 60000); st = stretches(t[s:s+60000], kind)
        samp = rng.sample(st, 28) if len(st) >= 28 else st
        rows.append((sum(samp)/len(samp), sum(1 for r in samp if r > 12)/len(samp), max(samp)))
    return rows
tm = sum(runs)/len(runs); ts = sum(1 for r in runs if r > 12)/len(runs); tx = max(runs)
for kind, label in (("func", "function-word stretches (letters)"), ("name", "proper-name stretches (letters)")):
    rows = band(kind)
    for k, name, tv in ((0, "mean", tm), (1, "share>12", ts), (2, "max", tx)):
        arr = sorted(r[k] for r in rows)
        print(f"{label:36s} {name:9s} band p05 {arr[3]:6.2f} p50 {arr[30]:6.2f} p95 {arr[57]:6.2f}  target {tv:6.2f} pct {100*sum(1 for x in arr if x < tv)/60:4.0f}")

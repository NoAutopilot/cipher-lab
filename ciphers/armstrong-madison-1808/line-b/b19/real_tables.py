"""Line B step B19 -- B1's decade-family statistics under REAL period tables (WE028, THE=972 Bourdeau), 60 en18
letters of 369 coded tokens each (words the table lacks are dropped as the target's shorthand wildcards, as in B2).
Columns as designs.py: r_fam, r_1xyz, r_34, r_row, S_w, z0 share and rare-digit share per tier, 2-digit share."""
import csv, random, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent; REPO = HERE.parents[3]
sys.path.insert(0, str(HERE.parent / "b1")); sys.path.insert(0, str(HERE.parent / "b2"))
from padding_test import target_tokens, en18_words
from designs import stats, KEYS
def load(path):
    code = {}
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        cols = r.fieldnames
        for row in r:
            v = row.get("code") or row.get("value") or row.get(cols[0]); w = row.get("word") or row.get("plain") or row.get("plaintext") or row.get(cols[1])
            try: v = int(str(v).strip())
            except: continue
            w = (w or "").strip().lower()
            if w and w.isalpha() and w not in code: code[w] = v
    return code
def simulate(words, code, rng, n=369):
    ws = rng.choice(words); start = rng.randint(0, len(ws) - 3000); out = []
    for w in ws[start:]:
        if w in code: out.append(code[w])
        if len(out) == n: break
    return out
words = en18_words(); tgt = stats(target_tokens())
for name in ("WE028.tsv", "THE972_bourdeau.tsv"):
    code = load(REPO / "tools/data/uscodes-1800" / name); print(f"\n{name}: {len(code)} words, values {min(code.values())}-{max(code.values())}")
    rows = [stats(simulate(words, code, random.Random(3000 + i))) for i in range(60)]
    print(f"{'stat':11s}{'mean':>8s}{'sd':>7s}{'p05':>8s}{'p95':>8s}{'target':>8s}{'pct':>7s}")
    for k in KEYS:
        arr = sorted(r[k] for r in rows); m = sum(arr)/60; sd = (sum((x-m)**2 for x in arr)/60)**0.5
        print(f"{k:11s}{m:8.3f}{sd:7.3f}{arr[3]:8.3f}{arr[57]:8.3f}{tgt[k]:8.3f}{100*sum(1 for x in arr if x < tgt[k])/60:7.0f}")

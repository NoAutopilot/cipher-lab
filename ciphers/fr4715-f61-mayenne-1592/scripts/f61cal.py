#!/usr/bin/env python3
"""F61-CAL scorer (27 Sept 2026): apply keys/key_mayenne_1592.tsv to the reader's S-labels on the five spans Tomokiyo
marks on BnF fr.4715 f.61r, align each span's markup to its line by a fixed local DP, and score the letter match
against 20 shuffled-key controls (value sets permuted across the 16 inventory symbols, seed 1).

  python3 scripts/f61cal.py [read_call_A.tsv] [--check]   (run from the target folder)
--check exits 1 if the committed f61cal_result.txt differs from a fresh run (rule 7).
"""
import csv, json, random, sys, os
from collections import defaultdict, Counter
HERE = os.path.dirname(os.path.abspath(__file__))
def load_key():
    inv = json.load(open(f"{HERE}/inventory_values.json"))       # S01 -> 'a', 'b/o', 'que' ...
    rows = [l.rstrip("\n").split("\t") for l in open(f"{HERE}/../keys/key_mayenne_1592.tsv") if not l.startswith("#")]
    hdr, rows = rows[0], rows[1:]
    vals = {r[1] for r in rows}
    key = {}
    for s, v in inv.items():
        vs = tuple(v.split("/"))
        assert all(x in vals for x in vs), (s, v)                  # every value comes from the key file
        key[s] = vs
    return key
def load_read(path):
    lines = defaultdict(list)
    for r in csv.DictReader(open(path), delimiter="\t"):
        lines[r["line"]].append(r["symbol"])
    return lines
def load_spans():
    out = []
    for l in open(f"{HERE}/tomokiyo_spans.tsv"):
        if l.startswith("#") or l.startswith("span\t"): continue
        s, line, markup, letters = l.rstrip("\n").split("\t")
        out.append((s, line, markup))
    return out
def align(markup, seq, key):
    """local DP: markup chars (letters or '-') vs sign value sets; match +1, mismatch 0, gap -1. A word-code sign
    consumes len(word) markup chars and scores len(word) if they equal the word. Returns (matched letters, path)."""
    n, m = len(markup), len(seq)
    NEG = -10**9
    D = [[NEG] * (m + 1) for _ in range(n + 1)]; P = {}
    for j in range(m + 1): D[0][j] = 0                              # span may start anywhere in the line
    for i in range(1, n + 1):
        D[i][0] = -i
        for j in range(1, m + 1):
            best, arg = D[i-1][j] - 1, ("gapM",)                   # markup char with no sign
            if D[i][j-1] - 1 > best: best, arg = D[i][j-1] - 1, ("gapS",)
            vs = key.get(seq[j-1], ())
            c = markup[i-1]
            sc = 1 if (c != "-" and c in vs) else 0
            if D[i-1][j-1] + sc > best: best, arg = D[i-1][j-1] + sc, ("m", sc)
            for w in vs:
                if len(w) > 1 and i >= len(w) and markup[i-len(w):i] == w and D[i-len(w)][j-1] + len(w) > best:
                    best, arg = D[i-len(w)][j-1] + len(w), ("w", len(w))
            D[i][j], P[i, j] = best, arg
    j = max(range(m + 1), key=lambda j: D[n][j])
    # traceback: count matched letters, record (markup index -> sign index)
    i, jj, matched, pairs = n, j, 0, []
    while i > 0:
        if jj == 0: i -= 1; continue
        a = P[i, jj]
        if a[0] == "gapM": i -= 1
        elif a[0] == "gapS": jj -= 1
        elif a[0] == "m": matched += a[1]; pairs.append((i-1, jj-1)); i -= 1; jj -= 1
        else: matched += a[1]; pairs.append((i-1, jj-1)); i -= a[1]; jj -= 1
    return matched, pairs[::-1]
def score(key, lines, spans):
    tot = mat = 0; per = []
    for s, line, markup in spans:
        letters = sum(1 for c in markup if c != "-")
        mt, pairs = align(markup, lines[line], key)
        per.append((s, line, mt, letters, pairs)); tot += letters; mat += mt
    return mat, tot, per
def main():
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    path = args[0] if args else f"{HERE}/read_call_A.tsv"
    key, lines, spans = load_key(), load_read(path), load_spans()
    out = []
    mat, tot, per = score(key, lines, spans)
    out.append(f"reader file: {os.path.basename(path)}")
    for s, line, mt, letters, pairs in per:
        out.append(f"{s}\t{line}\tmatched {mt}/{letters}")
    out.append(f"POOLED\t{mat}/{tot} = {mat/tot:.3f}  (gate 0.85)")
    toks = [x for l in lines.values() for x in l]
    known = [x for x in toks if x in key]
    amb = sum(1 for x in known if len(key[x]) > 1)
    out.append(f"coverage (signs with a key symbol): {len(known)}/{len(toks)} = {len(known)/len(toks):.3f}")
    out.append(f"ambiguity (known signs with >1 value): {amb}/{len(known)} = {amb/max(1,len(known)):.3f}; over all signs {amb/len(toks):.3f}")
    rng = random.Random(1); labs = sorted(key); ctrl = []
    for _ in range(20):
        v = [key[l] for l in labs]; rng.shuffle(v); k2 = dict(zip(labs, v))
        ctrl.append(score(k2, lines, spans)[0] / tot)
    out.append("controls (20 shuffled keys, seed 1): " + " ".join(f"{c:.3f}" for c in ctrl))
    out.append(f"control mean {sum(ctrl)/20:.3f} max {max(ctrl):.3f}")
    # diagnostic: letters Tomokiyo reads under each reader label along the target alignment (markup chars, dashes skipped)
    diag = defaultdict(Counter)
    for (s, line, markup) in spans:
        _, pairs = align(markup, lines[line], key)
        for mi, sj in pairs:
            if markup[mi] != "-": diag[lines[line][sj]][markup[mi]] += 1
    out.append("diagnostic (reader label -> Tomokiyo letters under it on the target alignment; key cell):")
    for lab in sorted(diag):
        out.append(f"  {lab}\tkey {'/'.join(key.get(lab, ('-',)))}\t" + " ".join(f"{c}:{n}" for c, n in diag[lab].most_common()))
    txt = "\n".join(out) + "\n"
    res = f"{HERE}/f61cal_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
main()

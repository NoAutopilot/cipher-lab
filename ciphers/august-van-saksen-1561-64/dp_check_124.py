#!/usr/bin/env python3
"""A2-AVS4 (2 Oct 2026): independent check of align_124.txt with tools/interlinear_align.py.
The cipher of each f.134 line (ciphertext_124.tsv) is aligned by dynamic programming to f.135's OWN wording for the same
span (F135 below, this worker's reading of the decipherment, not the cipher-side units of align_124.txt). Letter signs
are numbered 10-99 (single letter each, below --floor 100), word signs 100+ (multi-letter chunks), so the tool's
numeral design applies unchanged. --prior seeds the letter signs from key_98 as built from 98 alone (key_98_from98.tsv);
word signs are never seeded and take their meaning from f.135 alone -- the test is whether f.135 hands each word sign
(R, EL8, M, PAPE, K, S, ...) the meaning align_124.txt gives it. Control: the same run with each line's cipher tokens
shuffled (5 seeds). Writes dp_124/ (scratch outputs, regenerable) and prints both numbers."""
import csv, os, random, subprocess, sys, collections
D = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(D, "..", "..", "tools", "interlinear_align.py")
F135 = {1: "Ferner will E.L. ich in geheimbden vertrauen nit",
 2: "verhalten das mir kurtz auff einander von dreien unter",
 3: "schiedlichen orten gleichlautende Zeittunge vertrau",
 4: "lich zukhommen sindt welcher massen Hertzog Johans Friderich und Hertzog Johans Wilhelm zu Sachssen in",
 5: "grosser werbung von Reutern und landtsknechten sein sollen und besor",
 6: "gen etliche wan bemelte hertzogen zu Sachssen also unversehens",
 7: "auff der fuss sei kamen das sie wol etwas wider E.L. und",
 8: "erneuerung irer alten forderung und ansprache furne",
 9: "hmen mochten wiewol ich nuhn nicht hoffe das deme",
 10: "also sei jedoch dieweil der Weldt seltzam ist das",
 11: "niemand wol zu trauen So habe ich E.L. als dem selben",
 12: "dienern und freundt nicht verhalten konnen damit",
 13: "sich E.L. desto bass versehen und bei zeiten auff der",
 14: "hertzogen zu Sachssen handel achtung geben mit freuntlicher",
 15: "bitt E.L. wollen dieses schreiben anders",
 16: "nit als treuer meinung vermerckhen was ich",
 17: "dann weiter hiervon erfahren werde das will",
 18: "E.L. ich allzeit dienstlich gerne verstendigen"}
WORD = {"R", "EL8", "M", "PAPE", "K", "S", "B", "BAR?", "OM", "NW", "Mf", "HX", "Dl", "BAR"}
rows = list(csv.DictReader(open(f"{D}/ciphertext_124.tsv"), delimiter="\t"))
signs = sorted({r["sign"] for r in rows} | {r["sign"] for r in csv.DictReader(open(f"{D}/key_98_from98.tsv"), delimiter="\t")})
num, nl, nw = {}, 10, 100
for s in signs:
    if s in WORD: num[s] = nw; nw += 1
    else: num[s] = nl; nl += 1
out = os.path.join(D, "dp_124"); os.makedirs(out, exist_ok=True)
with open(f"{out}/prior.tsv", "w") as f:
    f.write("code\tmeaning\n")
    for r in csv.DictReader(open(f"{D}/key_98_from98.tsv"), delimiter="\t"):
        if r["grade"] == "C" and len(r["value"]) == 1: f.write(f"{num[r['sign']]}\t{r['value']}\n")
lines = collections.defaultdict(list)
for r in rows: lines[int(r["line"])].append(r["sign"])
def run(tag, shuffle_seed=None):
    p = f"{out}/pairs_{tag}.tsv"
    with open(p, "w") as f:
        f.write("plain_line\tplain_raw\tcipher_line\tcipher_raw\n")
        for ln in sorted(lines):
            toks = list(lines[ln])
            if shuffle_seed is not None: random.Random(shuffle_seed * 100 + ln).shuffle(toks)
            f.write(f"{ln}\t{F135[ln]}\t{ln}\t{' '.join(str(num[t]) for t in toks)}\n")
    subprocess.run([sys.executable, T, "align", p, f"{out}/align_{tag}.tsv", f"{out}/key_{tag}.tsv", "--floor", "100",
                    "--prior", f"{out}/prior.tsv", "--keep-fs"], check=True, capture_output=True)
    return {r["value"]: r for r in csv.DictReader(open(f"{out}/key_{tag}.tsv"), delimiter="\t")}
inv = {v: k for k, v in num.items()}
EXPECT = {"R": "el", "EL8": "das", "M": "und", "PAPE": "hertzogenzusachssen", "K": "der", "S": "zu"}
def score(tag):
    """per occurrence: the chunk f.135 gives a word sign matches align_124's meaning if one contains the other
    (the shorter at least 2 letters) -- chunk edges shift where f.135 adds or drops a neighbouring word."""
    hits = collections.Counter(); tot = collections.Counter()
    for r in csv.DictReader(open(f"{out}/align_{tag}.tsv"), delimiter="\t"):
        s = inv.get(int(r["raw"])) if r["raw"].isdigit() else None
        if s not in EXPECT: continue
        c, e = r["plain_chunk"].lower(), EXPECT[s]; tot[s] += 1
        hits[s] += bool(c) and (e in c or (len(c) >= 2 and c in e))
    return sum(hits.values()), sum(tot.values()), {s: f"{hits[s]}/{tot[s]}" for s in EXPECT}
real = run("real"); g, n, hits = score("real")
print(f"target: {g}/{n} word-sign occurrences get align_124's meaning from f.135 alone: {hits}")
for s in ("R", "EL8", "M"):
    r = real.get(str(num[s]));
    if r: print(f"  {s}: n={r['n']} agree={r['agree']} others={r['others']}")
cg = []
for seed in range(5):
    run(f"shuf{seed}", seed); gg, nn, hh = score(f"shuf{seed}"); cg.append(gg)
print(f"control (cipher tokens shuffled within line, 5 seeds): {cg} of {n}, mean {sum(cg)/5:.1f}")
def letters(tag):
    """letter-sign tokens whose DP chunk equals align_124's sure unit (u/v merged)"""
    pr = list(csv.DictReader(open(f"{D}/pairs_124.tsv"), delimiter="\t"))
    al = list(csv.DictReader(open(f"{out}/align_{tag}.tsv"), delimiter="\t"))
    ok = n = 0
    for p, a in zip(pr, al):
        if p["sign"] in WORD or p["unit"].endswith("~") or p["unit"] == "?" or p["sign"].endswith("?"): continue
        n += 1; ok += a["plain_chunk"].lower().replace("v", "u") == p["unit"].lower().replace("v", "u")
    return ok, n
ok, n = letters("real"); print(f"target letter signs: DP chunk from f.135 = align_124 unit for {ok}/{n} = {ok/n:.3f}")

#!/usr/bin/env python3
"""H381 (runner 14 session_01N7YQoVMZj1SfiFvc4XG9DH, 29 Sept 2026), script-only, for VERIFY-F61-V11: the bowl answer against a known letter on every
leaf that has letters, per leaf and pooled. 'Agreement' = (bowl & c/p[/t]) + (no bowl & a/n) over tokens whose letter is in {c,p,(t)} or {a,n};
other letters and 'n' answers left out. Sources, read from the result files on disk (no new reading):
  f.101r period gloss (H364/H365, 'period letter by bowl' line; c/p/t as that line groups it) -- in-sample for v7's 4TRI cell;
  f.108r period overlay (H202 result's last count line; c/p) -- f.61's hand;
  f.176r period decipherment (H193 result; c/p) -- Desportes's hand, the anchors' own leaf (its targets are the other folio);
  f.61 Tomokiyo's published spans (H367's fixed-position answers joined to the Tomokiyo column of H194's result; c/p) -- the target, published letters.
Reports each leaf's agreement and n, the pooled agreement, and the spread (min-max) across leaves (CLAUDE.md rule 3: a pooled figure over few folds
is read with its per-fold spread). Descriptive.   python3 h381_shape_letter_pool.py [--check]"""
import csv, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__)); P = f"{HERE}/passes"
def rd(f): return [r for r in csv.DictReader((l for l in open(f) if not l.startswith("#")), delimiter="\t")]
def line(f, start): return next(l for l in open(f"{HERE}/{f}") if l.startswith(start)).strip()
def leaves():
    L = []
    t = line("h365_101r_4tri_split_result.txt", "period letter by bowl")
    g = lambda a, b: int(re.search(rf"\b{a}:{re.escape(b)} (\d+)", t).group(1))
    L.append(("f.101r period gloss (H365; c/p/t)", g("yes", "c/p/t"), g("yes", "a/n"), g("no", "c/p/t"), g("no", "a/n")))
    t = line("h202_bowl_108r_result.txt", "bowl yes:"); m = list(map(int, re.findall(r"(\d+)", t)[:4]))
    L.append(("f.108r period overlay (H202; c/p)", m[0], m[1], m[2], m[3]))
    t = line("h193_attr_result.txt", "f.176r targets:"); m = list(map(int, re.findall(r"(?:c/p|a/n) (\d+)", t)))
    L.append(("f.176r period decipherment (H193; c/p)", m[0], m[1], m[2], m[3]))
    tom = {}
    import h367_bowl_f61 as h
    fam = {}
    for r in rd(f"{HERE}/../scripts/f61_positions_all.tsv"):
        if r["class"] in h.FAM: fam.setdefault(r["line"], []).append(r["pos"])
    for l in open(f"{HERE}/h194_bowl_f61_result.txt"):
        f = l.rstrip("\n").split("\t")
        if len(f) == 5 and f[0].startswith("L") and f[1].isdigit(): tom[(f[0], fam[f[0]][int(f[1]) - 1])] = f[4]
    ans = {r["id"]: r["answer"].strip().lower() for r in rd(f"{P}/h367_reply.tsv")}; c = [0, 0, 0, 0]
    for r in rd(f"{HERE}/h367_items.tsv"):
        a, t = ans.get(r["item"]), tom.get((r["line"], r["pos"]), "-")
        if a in ("yes", "no") and t in "cpan" and t != "-":
            c[(0 if a == "yes" else 2) + (0 if t in "cp" else 1)] += 1
    L.append(("f.61 Tomokiyo spans (H367 answers; c/p)", *c))
    return L
out = ["leaf\tbowl&c/p\tbowl&a/n\tno&c/p\tno&a/n\tn\tagreement"]; tot = [0, 0, 0, 0]; ag = []
for name, yc, ya, nc, na in leaves():
    n = yc + ya + nc + na; a = (yc + na) / max(1, n); ag.append(a); tot = [x + y for x, y in zip(tot, (yc, ya, nc, na))]
    out.append(f"{name}\t{yc}\t{ya}\t{nc}\t{na}\t{n}\t{a:.2f}")
n = sum(tot); out.append(f"pooled\t{tot[0]}\t{tot[1]}\t{tot[2]}\t{tot[3]}\t{n}\t{(tot[0] + tot[3]) / n:.2f}")
f101 = sum(int(x) for x in out[1].split("\t")[1:5])
out.append(f"per-leaf agreement spread {min(ag):.2f}-{max(ag):.2f} over {len(ag)} leaves; f.101r is {100 * f101 / n:.0f}% of the pooled tokens")
txt = "\n".join(out) + "\n"; res = f"{HERE}/h381_shape_letter_pool_result.txt"
if "--check" in sys.argv:
    ok = os.path.exists(res) and open(res).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
open(res, "w").write(txt); print(txt, end="")

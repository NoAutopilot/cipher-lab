#!/usr/bin/env python3
"""F61-108V3X (campaign step H29, 28 Sept 2026): fr.3983 f.108v re-cut at 3x -- do two blind sign passes and two blind
gloss passes agree well enough to read the leaf's period gloss as a key source?

Pre-registered before the four calls' outputs were read. Inputs (verbatim): family/passes/f108v3x_signsA.tsv and
_signsB.tsv (line pos sign conf segment x_px note; PLAIN rows are clear words inside the cipher row and are dropped
before reconciliation), family/passes/f108v3x_glossA.tsv and _glossB.tsv (line pos kind word conf segment x0_px x1_px;
kind = gloss only, inline words dropped). Signs: tools/reconcile_passes.py (nw) over the 7 bands; agreement = identical
columns / columns. Gloss: per band, the two word lists folded to a-z aligned by difflib (scripts/f61gloss.py's rule: a
word both give is kept C-C, a word one gives with no counterpart is kept C-M, a conflicting pair is dropped); agreement
= words both give / max(words A, words B) over the leaf. Gates (H29, CAMPAIGN.md): sign agreement >= 0.80 AND gloss-word
agreement >= 0.50. On a pass: tools/interlinear_align.py align --code-prefix @ --wildcard - --null-cost -1 --clear-
consumes on one pair per band (plain = the kept gloss words, cipher = the reconciled draft's codes) -> family/passes/
f108v3x_key.tsv (class -> letters with counts; grade C; NOT merged into key_period.tsv, which is the H28 owner's merge
gate). On a fail the counts still go to f108v3x_counts.tsv for the record.

  python3 scripts/f61v3x.py [--check]   -> scripts/f61v3x_result.txt
"""
import csv, os, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, HERE)
from f61gloss import reconcile_gloss, TOOL
FAM = f"{HERE}/../family/passes"; BANDS = [f"L0{i}" for i in range(1, 8)]
def strip_plain(src, dst):
    rows = [r for r in csv.DictReader((l for l in open(src) if not l.startswith("#")), delimiter="\t") if r["sign"] != "PLAIN"]
    with open(dst, "w") as f:
        w = csv.DictWriter(f, fieldnames=["line", "pos", "sign", "conf", "segment", "x_px", "note"], delimiter="\t", lineterminator="\n"); w.writeheader()
        for r in rows: w.writerow({k: r.get(k, "") for k in w.fieldnames})
    return len(rows)
def gloss_words(path):
    by = defaultdict(list)
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        if r["kind"].strip().lower() != "gloss": continue
        by[r["line"]].append((int(r["segment"]), float(r["x0_px"]), r["word"], r["conf"]))
    return {b: sorted(v) for b, v in by.items()}
def main():
    d = tempfile.mkdtemp(prefix="f61v3x_"); out = ["H29: fr.3983 f.108v at 3x, 7 cipher rows"]
    na = strip_plain(f"{FAM}/f108v3x_signsA.tsv", f"{d}/A.tsv"); nb = strip_plain(f"{FAM}/f108v3x_signsB.tsv", f"{d}/B.tsv")
    r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{d}/A.tsv", f"{d}/B.tsv", "--out-dir", d, "--method", "nw"], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stdout + r.stderr)
    summ = next(l for l in r.stdout.splitlines() if l.startswith("lines")); out.append("signs: " + summ + f" (PLAIN rows dropped: A {na} signs, B {nb})")
    agree_signs = float(summ.split("agree")[1].split("=")[1].split("%")[0]) / 100
    seq = defaultdict(list)
    for row in csv.DictReader(open(f"{d}/ciphertext_draft.tsv"), delimiter="\t"): seq[row["line"]].append(row["sign"])
    A, B = gloss_words(f"{FAM}/f108v3x_glossA.tsv"), gloss_words(f"{FAM}/f108v3x_glossB.tsv")
    import f61gloss; f61gloss.BANDS = BANDS
    rec = reconcile_gloss(A, B, out)
    both = sum(1 for b in BANDS for _, g in rec.get(b, []) if g == "C-C"); tot = max(sum(len(v) for v in A.values()), sum(len(v) for v in B.values()), 1)
    agree_gloss = both / tot
    out.append(f"gloss: words A {sum(len(v) for v in A.values())}, B {sum(len(v) for v in B.values())}, both {both} -> agreement {agree_gloss:.3f}")
    ok = agree_signs >= 0.80 and agree_gloss >= 0.50
    out.append(f"GATE H29: signs {agree_signs:.3f} (>= 0.80 {'ok' if agree_signs >= 0.80 else 'NO'}), gloss {agree_gloss:.3f} (>= 0.50 {'ok' if agree_gloss >= 0.50 else 'NO'}) -> {'PASS' if ok else 'FAIL'}")
    pairs = f"{d}/pairs.tsv"
    with open(pairs, "w") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
        for b in BANDS:
            if rec.get(b) and seq.get(b): w.writerow([b, " ".join(wd for wd, _ in rec[b]), b, " ".join("@" + c for c in seq[b])])
    subprocess.run([sys.executable, TOOL, "align", pairs, f"{d}/align.tsv", f"{d}/key.tsv", "--code-prefix", "@", "--wildcard", "-", "--null-cost", "-1", "--clear-consumes"], check=True, capture_output=True)
    counts = defaultdict(Counter); bands = defaultdict(set)
    for r in csv.DictReader(open(f"{d}/align.tsv"), delimiter="\t"):
        if r["kind"] == "code" and r["plain_chunk"]: counts[r["value"]][r["plain_chunk"]] += 1; bands[r["value"]].add(r["cipher_line"])
    dst = f"{FAM}/f108v3x_key.tsv" if ok else f"{FAM}/f108v3x_counts.tsv"
    with open(dst, "w") as f:
        f.write(f"# {'f108v3x_key.tsv' if ok else 'f108v3x_counts.tsv (gate FAILED: not a key)'} -- campaign H29, 28 Sept 2026, fr.3983 f.108v at 3x. Key source: period (the leaf's own interlinear decipherment), grade C per pair; not merged into key_period.tsv.\nclass\tletters\tn\tbands\n")
        for c, cnt in sorted(counts.items(), key=lambda kv: -sum(kv[1].values())):
            f.write(f"{c}\t{' '.join(f'{l}:{n}' for l, n in cnt.most_common())}\t{sum(cnt.values())}\t{','.join(sorted(bands[c]))}\n")
    out.append(f"alignment counts -> family/passes/{os.path.basename(dst)}: " + "; ".join(f"{c} " + " ".join(f"{l}:{n}" for l, n in cnt.most_common(3)) for c, cnt in sorted(counts.items(), key=lambda kv: -sum(kv[1].values()))[:14]))
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61v3x_result.txt"
    if "--check" in sys.argv:
        okc = os.path.exists(res) and open(res).read() == txt; print("fresh" if okc else "STALE"); sys.exit(0 if okc else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()

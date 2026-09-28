#!/usr/bin/env python3
"""F61-GLOSS (campaign step H21, 28 Sept 2026): the period interlinear decipherment on fr.3983 f.108r as a key source.

Pre-registered before the four calls' outputs were read (prompts in scripts/PROMPTS.md). Inputs, all verbatim files:
  gloss passes  scripts/gloss108A.tsv, gloss108B.tsv  (Sonnet; sheet, segment, x_start, x_end, word, conf, note)
  sign passes   scripts/pass108A/B_classes.tsv (bands L02, L03; H19) and pass108C/D_classes.tsv (bands L05, L06, L07)
Reconciliation of the gloss (mechanical): per band, the two passes' word lists, main-line words excluded (note contains
'main line'), letters folded to a-z; words are aligned by difflib on the folded strings; a word both passes give is kept
(grade C-C), a word one pass gives with no counterpart is kept and flagged (grade C-M), a conflicting pair is dropped
and listed. Signs: tools/reconcile_passes.py (nw) per band pair; the draft's sign per column (pass A where they differ,
flagged). Alignment: tools/interlinear_align.py align --code-prefix @ --wildcard - --null-cost -1 --clear-consumes,
one pair per band (plain = the reconciled gloss words in order; cipher = the band's atlas codes prefixed @).
Output: keys/key_f108_gloss.tsv (class -> letters with counts and the bands they come from; grade C for every pair:
the meaning is the period decipherer's), scripts/f61gloss_result.txt. Gate (H21): the gloss-derived top letters agree
with the f.61 map's cell on every one of its nine cells (PHI e/r, C43 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, VBAR_B f/s,
DBL b/o, EBR_A f/s, EBR_B l/y -- a cell agrees when the class's top-2 gloss letters are within the cell) AND at least one
new cell (d/q, m/z) or word code reaches 2+ counts.

  python3 scripts/f61gloss.py [--check]
"""
import csv, difflib, os, re, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../.."); sys.path.insert(0, HERE)
TOOL = f"{ROOT}/tools/interlinear_align.py"
BANDS = ["L02", "L03", "L05", "L06", "L07"]
NINE = {"PHI": "e/r", "C43": "a/n", "4TRI": "c/p", "INF": "h/u", "VBAR_A": "g/t", "VBAR_B": "f/s", "DBL": "b/o", "EBR_A": "f/s", "EBR_B": "l/y"}
FOLD = str.maketrans("àâäéèêëîïôöùûüç", "aaaeeeeiioouuuc")
def fold(w): return re.sub(r"[^a-z]", "", w.lower().translate(FOLD))
def gloss(path):
    by = defaultdict(list)
    for r in csv.DictReader((l for l in open(f"{HERE}/{path}") if not l.startswith("#")), delimiter="\t"):
        if "main line" in r["note"].lower(): continue
        band = r["sheet"].replace(".jpg", "").split("_")[-1]
        by[band].append((int(r["segment"]), float(r["x_start"]), r["word"], r["conf"]))
    return {b: sorted(v) for b, v in by.items()}
def reconcile_gloss(A, B, out):
    rec = {}
    for band in BANDS:
        a = [w for _, _, w, _ in A.get(band, [])]; b = [w for _, _, w, _ in B.get(band, [])]
        fa, fb = [fold(w) for w in a], [fold(w) for w in b]
        sm = difflib.SequenceMatcher(a=fa, b=fb, autojunk=False); words = []; dropped = []
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal": words += [(a[k], "C-C") for k in range(i1, i2)]
            elif tag == "replace":
                if i2 - i1 == j2 - j1:
                    for k in range(i2 - i1):
                        # same length, differing spelling: keep the shorter-edit word only if they share 60% of letters
                        x, y = fa[i1 + k], fb[j1 + k]
                        if difflib.SequenceMatcher(a=x, b=y).ratio() >= 0.6: words.append((a[i1 + k], "C-M"))
                        else: dropped.append(f"{a[i1+k]}|{b[j1+k]}")
                else: dropped += [f"{a[k]}|" for k in range(i1, i2)] + [f"|{b[k]}" for k in range(j1, j2)]
            elif tag == "delete": words += [(a[k], "C-M") for k in range(i1, i2)]
            elif tag == "insert": words += [(b[k], "C-M") for k in range(j1, j2)]
        rec[band] = words
        out.append(f"  gloss {band}: A {len(a)} words, B {len(b)}, kept {len(words)} ({sum(1 for _, g in words if g == 'C-C')} both, {sum(1 for _, g in words if g == 'C-M')} one pass), dropped {len(dropped)}" + (": " + " ".join(dropped) if dropped else ""))
    return rec
def signs(pa, pb, out, tag):
    d = tempfile.mkdtemp(prefix=f"f61gloss_{tag}_")
    r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{HERE}/{pa}", f"{HERE}/{pb}", "--out-dir", d, "--method", "nw"], capture_output=True, text=True)
    if r.returncode: raise SystemExit(r.stdout + r.stderr)
    out.append(f"  signs {tag}: " + " | ".join(l for l in r.stdout.strip().splitlines() if l.startswith("lines")))
    seq = defaultdict(list)
    for row in csv.DictReader(open(f"{d}/ciphertext_draft.tsv"), delimiter="\t"): seq[row["line"]].append(row["sign"])
    return seq
def main():
    out = ["H21: period gloss on fr.3983 f.108r aligned to the atlas-coded signs"]
    rec = reconcile_gloss(gloss("gloss108A.tsv"), gloss("gloss108B.tsv"), out)
    seq = signs("pass108A_classes.tsv", "pass108B_classes.tsv", out, "L02-L03"); seq.update(signs("pass108C_classes.tsv", "pass108D_classes.tsv", out, "L05-L07"))
    d = tempfile.mkdtemp(prefix="f61gloss_align_"); pairs = f"{d}/pairs.tsv"
    with open(pairs, "w") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n"); w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
        for band in BANDS:
            if rec.get(band) and seq.get(band): w.writerow([band, " ".join(wd for wd, _ in rec[band]), band, " ".join("@" + c for c in seq[band])])
    subprocess.run([sys.executable, TOOL, "align", pairs, f"{d}/align.tsv", f"{d}/key.tsv", "--code-prefix", "@", "--wildcard", "-", "--null-cost", "-1", "--clear-consumes"], check=True, capture_output=True)
    counts = defaultdict(Counter); bands = defaultdict(set)
    for r in csv.DictReader(open(f"{d}/align.tsv"), delimiter="\t"):
        if r["kind"] == "code" and r["plain_chunk"]:
            counts[r["value"]][r["plain_chunk"]] += 1; bands[r["value"]].add(r["cipher_line"])
    os.makedirs(f"{HERE}/../keys", exist_ok=True)
    with open(f"{HERE}/../keys/key_f108_gloss.tsv", "w") as f:
        f.write("# key_f108_gloss.tsv -- campaign H21, 28 Sept 2026. Key source: period (rule 10 vocabulary). Every (class, letter) pair is read\n# from the contemporary interlinear decipherment on BnF fr.3983 f.108r (two Sonnet gloss passes reconciled, two Opus sign\n# passes per band reconciled, tools/interlinear_align.py), grade C for the pair; no cryptanalysis, no refit. Classes are\n# scripts/f61_atlas.tsv codes (EBR is the pre-split code where a band's passes predate H22).\nclass\tletters\tn\tbands\n")
        for c, cnt in sorted(counts.items(), key=lambda kv: -sum(kv[1].values())):
            f.write(f"{c}\t{' '.join(f'{l}:{n}' for l, n in cnt.most_common())}\t{sum(cnt.values())}\t{','.join(sorted(bands[c]))}\n")
    out.append("gloss key (class: letters): " + "; ".join(f"{c} " + " ".join(f"{l}:{n}" for l, n in cnt.most_common(3)) for c, cnt in sorted(counts.items(), key=lambda kv: -sum(kv[1].values()))))
    agree = []; 
    for c, cell in NINE.items():
        cnt = counts.get(c, Counter()); top2 = [l for l, _ in cnt.most_common(2)]
        ok = bool(top2) and all(l in cell.split("/") for l in top2 if len(l) == 1)
        agree.append((c, cell, top2, ok))
    out.append("nine cells vs the gloss: " + " ".join(f"{c}={cell}:{'/'.join(t) or '-'}:{'ok' if ok else 'NO'}" for c, cell, t, ok in agree))
    new = {c: cnt for c, cnt in counts.items() if c not in NINE and sum(n for l, n in cnt.items() if l in "dqmz" or len(l) > 1) >= 2}
    out.append("new cells/word codes with 2+ counts: " + (" ".join(f"{c}:" + " ".join(f"{l}:{n}" for l, n in cnt.most_common(3)) for c, cnt in new.items()) or "none"))
    out.append(f"GATE H21: nine cells {'all agree' if all(ok for *_, ok in agree) else 'NOT all agree'}; new material {'yes' if new else 'no'} -> {'PASS' if all(ok for *_, ok in agree) and new else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61gloss_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()

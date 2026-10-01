#!/usr/bin/env python3
"""LAU-U3U4 (1 Oct 2026): build key57/f58s_ciphertext.tsv from pass A's full row order, the aligner's sign
columns (f58s_reconcile/ciphertext_draft.tsv) and the per-line settled results (results/L*.tsv from the
one-sheet-per-call reconciliation). Rules: agreed+both H -> H (source AB); agreed but flagged -> lower of the two
confidences (AB); disagreement or uncertain column settled from the sheet -> the settled value/grade (source A/B/
settled); disagreement on a line not sent to vision -> pass A's value at L, alt=B, source 'open'."""
import csv, glob, os, re, sys
K = sys.argv[1]; R = sys.argv[2]; OUT = sys.argv[3]
A = list(csv.DictReader(open(f"{K}/f58s_passA.tsv"), delimiter="\t"))
D = list(csv.DictReader(open(f"{K}/f58s_reconcile/ciphertext_draft.tsv"), delimiter="\t"))
U = {(r["line"], r["col"]): r["both_conf"] for r in csv.DictReader(open(f"{K}/f58s_reconcile/uncertain.tsv"), delimiter="\t")}
DIS = {(r["line"], r["col"]) for r in csv.DictReader(open(f"{K}/f58s_reconcile/disagreements.tsv"), delimiter="\t")}
RES = {}
for f in sorted(glob.glob(f"{R}/L*.tsv")):
    L = os.path.basename(f)[:-4]
    for r in csv.DictReader(open(f), delimiter="\t"):
        RES[(L, r["col"].strip())] = r
def strip(s): return s.rstrip("?")
def is_sign(s): return not s.startswith("[PLAIN:")
lines = []
for r in A:
    if r["line"] not in lines: lines.append(r["line"])
out = []; stats = {"H":0,"M":0,"L":0,"open":0,"plain":0,"vision":0,"merged":0}; nb = 0
for L in lines:
    arows = [r for r in A if r["line"] == L]
    cols = [r for r in D if r["line"] == L]
    ai = 0  # index into arows
    def flush_plain(upto):
        global ai
        while ai < upto:
            r = arows[ai]; ai += 1
            if is_sign(r["sign"]): continue  # should not happen
            out.append([L, r["pos"], r["sign"], r["marks"], r["conf"], "A", ""]); stats["plain"] += 1
    for c in cols:
        col = c["position"]; alt = c["alt"]
        if alt.startswith("B:"): a, b = c["sign"], alt[2:]
        elif alt.startswith("A:"): a, b = alt[2:], c["sign"]
        else: a = b = c["sign"]
        if a != "-":
            # advance to the next sign row in A, flushing plaintext before it
            j = ai
            while j < len(arows) and not is_sign(arows[j]["sign"]): j += 1
            if j >= len(arows): raise SystemExit(f"{L} col {col}: no A sign row left for {a}")
            if strip(arows[j]["sign"]) != a and not (a == "" and arows[j]["sign"] in ("", "?")):
                raise SystemExit(f"{L} col {col}: A value {a!r} != pass A row {arows[j]['sign']!r}")
            flush_plain(j); arow = arows[j]; ai = j + 1
            pos = arow["pos"]; marks = arow["marks"]
        else:
            nb += 1; pos = f"{arows[ai-1]['pos'] if ai else 0}b{nb}"; marks = "B-only"
        key = (L, col)
        if key in RES and (RES[key]["settled"].strip() == "-" or re.match(r"(?i)merged (into|with)|not a separate sign", RES[key]["reason"].strip())):
            stats["merged"] += 1; continue  # a column the sheet reconciler folded into its neighbour
        if key in RES:
            s = RES[key]; val = s["settled"].strip(); grade = s["grade"].strip().upper(); src = s["source"].strip() or "settled"
            why = s["reason"].strip(); stats["vision"] += 1
            if "gloss" in why.lower() and val.startswith("[PLAIN:") and "gloss" not in marks: marks = (marks + "; gloss").strip("; ")
            out.append([L, pos, val, marks, grade, src, f"A:{a} B:{b} | {why}"])
            # extra rows the sheet reconciler added (col '<n>a')
            for extra in sorted(k for k in RES if k[0] == L and k[1] == f"{col}a"):
                e = RES[extra]; out.append([L, f"{pos}a", e["settled"].strip(), marks, e["grade"].strip().upper(), e["source"].strip() or "settled", e["reason"].strip()]); stats["vision"] += 1
            stats[grade if grade in stats else "L"] += 1
        elif key in DIS:
            out.append([L, pos, a if a != "-" else b, marks, "L", "open", f"A:{a} B:{b} | not sent to vision"]); stats["open"] += 1
        elif key in U:
            ca, cb = re.findall(r"[HML]", U[key]); grade = "L" if "L" in (ca, cb) else "M"
            out.append([L, pos, a, marks, grade, "AB", f"agree-flagged {U[key]}"]); stats[grade] += 1
        else:
            out.append([L, pos, a, marks, "H", "AB", "agree"]); stats["H"] += 1
    flush_plain(len(arows))
with open(OUT, "w", newline="") as f:
    w = csv.writer(f, delimiter="\t", lineterminator="\n")
    w.writerow(["line", "pos", "sign", "marks", "conf", "source", "note"]); w.writerows(out)
print(stats, "rows", len(out))

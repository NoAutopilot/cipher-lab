"""N4-C1 (4 Oct 2026): c188L re-pass merge. Two fresh blind passes on the committed slope crops (tx/c188L_passC.tsv top-down,
tx/c188L_passD.tsv bottom-up; prompt tx/c188L_slope_pass_prompt.md, labels tx/labels_v2.md) plus NEAR3-C1TX-c188L's reconciled
tx/c188L_rec_long.tsv as the third reading, aligned by tools/reconcile_passes.py (sign map tx/c188L_signmap2.tsv) into
tx/c188L_rec3/. Rule (fixed before looking at the result): per aligned column the 2-of-3 majority (a gap counts as a reading);
where all three differ, the NEAR3 reconciled sign (settled by eye from slope composites). Grade H only where all three agree at H;
otherwise M. The clear word PLAIN:curou? (L14 end, NEAR3) is carried over. Writes tx/c188L_rec2_long.tsv (line pos sign conf note).
Run from the target folder."""
import csv
rows = list(csv.DictReader(open("tx/c188L_rec3/ciphertext_draft.tsv"), delimiter="\t"))
dis = {(r["line"], r["col"]): r for r in csv.DictReader(open("tx/c188L_rec3/disagreements.tsv"), delimiter="\t")}
out, n3 = [], 0
for r in rows:
    key = (r["line"], r["position"])
    d = dis.get(key)
    sign, conf, note = r["sign"], r["confidence"], r["why"]
    if d:
        a, b, c = d["A"], d["B"], d["C"]
        if a != b and b != c and a != c:
            sign, note = c, f"3-way C:{a} D:{b} NEAR3:{c}; NEAR3 kept"; n3 += 1
        else:
            maj = a if a in (b, c) else b
            sign, note = maj, f"2-of-3 C:{a} D:{b} NEAR3:{c}"
        conf = "M"
    if sign in ("-", ""):
        continue
    out.append([r["line"], sign, conf, note])
# L02: the committed slope crop c188L_L02_s1 frames L01 and cuts L02 at its bottom edge (pass D's report; checked by eye on a
# stacked view of L01-L03 s1). Both fresh passes lost L02's first signs; the cut tops show '6r y + K + p 4 S y a', NEAR3's reading.
i = next(k for k, x in enumerate(out) if x[0] == "L02")
assert out[i][1] == "K", out[i]
out[i:i] = [["L02", s, "M", "L02_s1 crop frames L01; NEAR3 reading, line start seen cut at the crop bottom"] for s in ("6r", "y", "+")]
res, pos, last = [], 0, None
for line, s, conf, note in out:
    pos = pos + 1 if line == last else 1; last = line
    res.append([f"c188L_{line}", str(pos), s, conf, note])
# append the clear word at the end of L14, as NEAR3 placed it
i = max(k for k, x in enumerate(res) if x[0] == "c188L_L14")
res.insert(i + 1, ["c188L_L14", str(int(res[i][1]) + 1), "[PLAIN:curou?]", "M", "clear word, NEAR3-C1TX-c188L"])
with open("tx/c188L_rec2_long.tsv", "w") as f:
    f.write("line\tpos\tsign\tconf\tnote\n" + "".join("\t".join(x) + "\n" for x in res))
n = sum(1 for x in res if not x[2].startswith("["))
print(f"c188L re-pass merge: {n} cipher signs, 3-way kept NEAR3 {n3}, conf H {sum(x[3]=='H' for x in res)}, "
      f"M {sum(x[3]=='M' for x in res)}")

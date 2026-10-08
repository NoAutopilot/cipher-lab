#!/usr/bin/env python3
"""Build ciphertext.tsv / ciphertext.txt / focus.tsv / inventory.tsv for WVO 11106 p.2 from the two reconciled halves
(tx/rec_h1, tx/rec_h2: tools/reconcile_passes.py on blind Sonnet passes A and B) plus the reconciler's picks below
(FAM-11106T, 8 Oct 2026, read from the native line crops images/crops/p2_Lnn.jpg). Every disagreement column not
picked here takes pass A's label at conf M and goes to focus.tsv for the owner's sign sorter. Struck-through signs
(label ending ~) and the DATE row stay in ciphertext.tsv with kind=struck/date but are left out of ciphertext.txt.
--check exits 1 if the committed outputs differ from a rebuild (rule 7)."""
import csv, sys, os, collections
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.dirname(HERE)
# (line, col) -> label chosen from the native crop; '-' = no sign there. Conf M unless noted.
PICK = {("L02", "17"): "5", ("L02", "35"): "z", ("L08", "5"): "g", ("L08", "17"): "g", ("L08", "33"): "c",
        ("L13", "12"): "h", ("L13", "31"): "u", ("L13", "41"): "-", ("L13", "42"): "t", ("L20", "31"): "S",
        ("L20", "11"): "f~", ("L20", "12"): "f~", ("L19", "21"): "-"}
LOOKALIKE = [{"d", "dd"}, {"y", "yx"}, {"s", "S"}, {"g", "G", "q", "9"}, {"z", "2"}, {"s", "5"}, {"n", "u"}, {"S", "sz"}]

def build():
    rows, focus = [], []
    for h in ("h1", "h2"):
        dis = {(r["line"], r["col"]): r for r in csv.DictReader(open(f"{HERE}/rec_{h}/disagreements.tsv"), delimiter="\t")}
        for r in csv.DictReader(open(f"{HERE}/rec_{h}/ciphertext_draft.tsv"), delimiter="\t"):
            key = (r["line"], r["position"]); sign, conf, why = r["sign"], r["confidence"], "2-reader agree"
            if key in dis:
                a, b = dis[key]["A"], dis[key]["B"]
                if key in PICK:
                    sign, conf, why = PICK[key], "M", f"split A={a} B={b}; reconciler pick from crop"
                else:
                    sign = a if a != "-" else b
                    conf, why = "M", f"split A={a} B={b}; A kept pending sorter"
                    focus.append((f"{key[0]}:{key[1]}", f"A read {a}, B read {b}: which sign? (crop images/crops/p2_{key[0]}.jpg)"))
            if sign == "-":
                continue
            sign = sign.rstrip("?")
            kind = "date" if sign == "DATE" else ("struck" if sign.endswith("~") else "cipher")
            rows.append((r["line"], sign, conf, kind, why))
    out, n = [], collections.defaultdict(int)
    for line, sign, conf, kind, why in rows:
        n[line] += 1; out.append((line, n[line], sign, conf, kind, why))
    return out, focus

def render(out, focus):
    tsv = "line\tpos\tsign\tconf\tkind\tnote\n" + "".join("\t".join(map(str, r)) + "\n" for r in out)
    lines = collections.OrderedDict()
    for r in out:
        if r[4] == "cipher":
            lines.setdefault(r[0], []).append(r[2])
    txt = ("# WVO 11106 p.2, FAM-11106T 8 Oct 2026: one line per manuscript line, signs space-separated (labels tx/signlist.md);"
           " struck signs and the clear date omitted; provisional inventory, see NOTES.md\n"
           + "".join(" ".join(v) + "\n" for v in lines.values()))
    foc = "sid\tquestion\n" + "".join(f"{a}\t{b}\n" for a, b in focus)
    cnt = collections.Counter(r[2] for r in out if r[4] == "cipher")
    inv = "sign\tcount\n" + "".join(f"{s}\t{c}\n" for s, c in cnt.most_common())
    one = " ".join(" ".join(v) for v in lines.values()) + "\n"
    return {"tx/ciphertext_oneline.txt": one, "ciphertext.tsv": tsv, "ciphertext.txt": txt, "tx/focus.tsv": foc, "tx/inventory.tsv": inv}

if __name__ == "__main__":
    files = render(*build())
    if "--check" in sys.argv:
        bad = [f for f, t in files.items() if not os.path.exists(f"{ROOT}/{f}") or open(f"{ROOT}/{f}").read() != t]
        print("stale: " + ", ".join(bad) if bad else "ok"); sys.exit(1 if bad else 0)
    for f, t in files.items():
        open(f"{ROOT}/{f}", "w").write(t)
    print("wrote", ", ".join(files))

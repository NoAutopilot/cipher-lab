#!/usr/bin/env python3
"""MONL-KING3: render rec/ciphertext_draft.tsv as the king2 reconciliation prompt (prompt_reconcile.txt, disputes.tsv), and,
with --apply rec_answers.tsv, write c258_L11-L25.tsv (line pos sign conf pass_a pass_b) as king2 did for L01-L10."""
import sys
rows = [l.rstrip("\n").split("\t") for l in open("rec/ciphertext_draft.tsv").read().splitlines()[1:]]
def ab(r):
    sign, conf, alt, why = r[2], r[3], r[4], r[5]
    if conf == "H": return sign, sign
    if why == "differ": return sign, alt[2:]
    return (sign, "(nothing)") if alt.startswith("B:") else ("(nothing)", sign)
if len(sys.argv) > 2 and sys.argv[1] == "--apply":
    ans = dict(l.split("\t")[:2] for l in open(sys.argv[2]).read().splitlines() if l.strip())
    out, n, pos = ["line\tpos\tsign\tconf\tpass_a\tpass_b"], 0, {}
    for r in rows:
        a, b = ab(r)
        if r[3] == "H": s, c = a, "H"
        else:
            n += 1; ch = ans[str(n)].strip(); c = "M"
            s = a if ch == "A" else b if ch == "B" else None if ch == "NONE" else ch
            if s == "(nothing)": s = None
        if s is None: continue
        pos[r[0]] = pos.get(r[0], 0) + 1
        out.append(f"{r[0]}\t{pos[r[0]]}\t{s}\t{c}\t{a if a != '(nothing)' else '-'}\t{b if b != '(nothing)' else '-'}")
    open("c258_L11-L25.tsv", "w").write("\n".join(out) + "\n"); print(len(out) - 1, "tokens,", n, "disputes applied"); sys.exit()
lines, disp, n = {}, ["n\tline\tA\tB"], 0
for r in rows:
    a, b = ab(r)
    if r[3] == "H": lines.setdefault(r[0], []).append(a)
    else:
        n += 1; lines.setdefault(r[0], []).append(f"[{n}: A={a} | B={b}]"); disp.append(f"{n}\t{r[0]}\t{a}\t{b}")
tmpl = open("../king2/prompt_reconcile.txt").read()
head = tmpl.split("\nL01:")[0].replace("TEN lines", "FIFTEEN lines").replace("L01, L02, L03, L04, L05, L06, L07, L08, L09, L10", ", ".join(lines)).replace("scratchking2/crops", "scratchking3/crops")
tail = "\n\nAnswer with one line" + tmpl.split("\n\nAnswer with one line")[1]
open("prompt_reconcile.txt", "w").write(head + "\n" + "\n".join(f"{k}: {' '.join(v)}" for k, v in lines.items()) + tail)
open("disputes.tsv", "w").write("\n".join(disp) + "\n"); print(n, "disputes")

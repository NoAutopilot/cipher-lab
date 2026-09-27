#!/usr/bin/env python3
"""F61-PASS2 (campaign step H2, 27 Sept 2026): does a second blind read reproduce call A's shape classes?

Pre-registered before pass B's output was read. Pass A: scripts/passA_classes.tsv (read_call_A.tsv's marks put through
scripts/f61crib.py's CLASS_RULES, VBAR split by H15). Pass B: scripts/passB_classes.tsv, one fresh Opus vision call on
images/f61sheetB_L*.jpg (whole span lines, segments trimmed so no sign repeats) given only scripts/f61_atlas.tsv (shape
words, no letters, no key) and asked for line, pos, code, conf. Alignment: tools/reconcile_passes.py (long format, NW
over signs) writes agreement.tsv / disagreements.tsv into a temp dir; this script reads the aligned columns.

Statistic: for each of the 10 letter classes of scripts/class_diag.tsv -- PHI, C43, 4TRI, VBAR (A and B counted as one
class here), DBL, INF, ZHOOK, EBR, BETA, 4PI -- the share of pass A's signs of that class whose aligned pass-B code is
the same class (VBAR_A/VBAR_B both count as VBAR); the class AGREES if that share is above one half (a tie or an
unaligned majority is a disagreement). Gate (H2, CAMPAIGN.md): at least 9 of the 10 classes agree. Reported, not
gated: overall aligned-column agreement, the VBAR_A/VBAR_B split agreement, and the null classes.

  python3 scripts/f61pass2.py [--check]   (from the target folder)
"""
import csv, os, subprocess, sys, tempfile
from collections import Counter, defaultdict
HERE = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.abspath(f"{HERE}/../../..")
LETTER = ["PHI", "C43", "4TRI", "VBAR", "DBL", "INF", "ZHOOK", "EBR", "BETA", "4PI"]
def fold(c): return "VBAR" if c.startswith("VBAR") else c

def main():
    # H17 (pre-registered before its call): --a read_call_U.tsv --b passU2_classes.tsv --out f61pass3_result.txt --gate-line L10
    # gate for H17: over the named line's aligned columns, at most 2 differ (gap or other class); the 10-class gate is then reported only.
    a = sys.argv[1:]
    src_a = a[a.index("--a") + 1] if "--a" in a else "passA_classes.tsv"
    src_b = a[a.index("--b") + 1] if "--b" in a else "passB_classes.tsv"
    dst = a[a.index("--out") + 1] if "--out" in a else "f61pass2_result.txt"
    gate_line = a[a.index("--gate-line") + 1] if "--gate-line" in a else None
    d = tempfile.mkdtemp(prefix="f61pass2_")
    r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{HERE}/{src_a}", f"{HERE}/{src_b}",
                        "--out-dir", d, "--method", "nw"], capture_output=True, text=True)
    if r.returncode: raise SystemExit("reconcile_passes.py failed:\n" + r.stdout + r.stderr)
    out = ["reconcile_passes.py summary: " + " | ".join(l for l in r.stdout.strip().splitlines() if not l.startswith("wrote "))]
    cols = []   # (line, A, B) per aligned column, from ciphertext_draft.tsv (sign = pass A's code; alt = 'B:<code>' or 'B:-' when they differ)
    for row in csv.DictReader(open(f"{d}/ciphertext_draft.tsv"), delimiter="\t"):
        a = row["sign"]; alt = row.get("alt", "")
        b = a if row["why"].startswith("agree") else (alt.split(":", 1)[1] if alt.startswith("B:") else "")
        if b == "-": b = ""
        cols.append((row["line"], a, b))
    per = defaultdict(Counter)
    for line, a, b in cols:
        if a: per[fold(a)][fold(b) if b else "(gap)"] += 1
    agree = 0
    for c in LETTER:
        cnt = per.get(c, Counter()); n = sum(cnt.values()); same = cnt.get(c, 0)
        ok = n > 0 and same * 2 > n
        agree += ok
        out.append(f"  {c}\tA signs {n}\tB same {same}\t{'agree' if ok else 'DISAGREE'}\tB codes: " + " ".join(f"{k}:{v}" for k, v in cnt.most_common()))
    tot = len(cols); same_all = sum(1 for _, a, b in cols if a and a == b)
    out.append(f"overall aligned columns {tot}, identical code {same_all} = {same_all/max(1,tot):.3f} (non-gating)")
    vb = Counter((a, b) for _, a, b in cols if a.startswith("VBAR"))
    out.append("VBAR split (non-gating): " + " ".join(f"{a}->{b or '(gap)'}:{n}" for (a, b), n in vb.most_common()))
    nulls = {c: per[c] for c in per if c not in LETTER}
    out.append("null/other classes (non-gating): " + "; ".join(f"{c}: " + " ".join(f"{k}:{v}" for k, v in cnt.most_common()) for c, cnt in nulls.items()))
    if gate_line:
        lc = [(a_, b_) for l, a_, b_ in cols if l == gate_line]; diff = sum(1 for a_, b_ in lc if a_ != b_)
        out.append(f"GATE H17 ({gate_line}: at most 2 of its aligned columns differ): {diff} differ of {len(lc)} -> {'PASS' if diff <= 2 else 'FAIL'}; per column: " + " ".join(f"{a_ or '-'}={b_ or '-'}" for a_, b_ in lc))
        out.append(f"10-class figure, reported only: {agree}/10")
    else:
        out.append(f"GATE H2 (at least 9 of 10 letter classes agree): {agree}/10 -> {'PASS' if agree >= 9 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/{dst}"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()

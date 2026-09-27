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
    d = tempfile.mkdtemp(prefix="f61pass2_")
    r = subprocess.run([sys.executable, f"{ROOT}/tools/reconcile_passes.py", f"{HERE}/passA_classes.tsv", f"{HERE}/passB_classes.tsv",
                        "--out-dir", d, "--method", "nw"], capture_output=True, text=True)
    if r.returncode: raise SystemExit("reconcile_passes.py failed:\n" + r.stdout + r.stderr)
    out = ["reconcile_passes.py summary: " + " | ".join(l for l in r.stdout.strip().splitlines()[-3:])]
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
    out.append(f"GATE H2 (at least 9 of 10 letter classes agree): {agree}/10 -> {'PASS' if agree >= 9 else 'FAIL'}")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61pass2_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")

if __name__ == "__main__":
    main()

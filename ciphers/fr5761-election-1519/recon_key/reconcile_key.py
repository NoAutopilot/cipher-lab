#!/usr/bin/env python3
"""Reconcile two key-list passes (line, section, plain, sign_code, note) by (line, plain).

Rows whose section is a nulls/nulle bucket are matched positionally within the same line
(their 'plain' labels differ between passes, e.g. NULLE x4 vs Null1..Null4), since the
key-list itself only calls them all "Nulle" with no individual label on the page.
Rows present in only one pass (e.g. pass A's header lines) are reported separately and do
not count toward the agreement percentage.
"""
import csv, sys, argparse
from pathlib import Path

def load(path):
    with open(path) as f:
        return list(csv.DictReader(f, delimiter="\t"))

def is_null_section(sec):
    return sec.strip().lower() in ("nulls", "nulle", "null")

def norm(s):
    return (s or "").strip()

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("passA")
    ap.add_argument("passB")
    ap.add_argument("--out-dir", default=".")
    args = ap.parse_args()

    a_rows = load(args.passA)
    b_rows = load(args.passB)

    a_only, b_only, pairs = [], [], []

    # bucket null rows by line, match positionally
    a_null_by_line, b_null_by_line = {}, {}
    a_rest, b_rest = [], []
    for r in a_rows:
        (a_null_by_line.setdefault(r["line"], []).append(r) if is_null_section(r["section"]) else a_rest.append(r))
    for r in b_rows:
        (b_null_by_line.setdefault(r["line"], []).append(r) if is_null_section(r["section"]) else b_rest.append(r))

    for line in sorted(set(a_null_by_line) | set(b_null_by_line), key=lambda x: (len(x), x)):
        al = a_null_by_line.get(line, [])
        bl = b_null_by_line.get(line, [])
        for i in range(max(len(al), len(bl))):
            ar = al[i] if i < len(al) else None
            br = bl[i] if i < len(bl) else None
            if ar and br:
                pairs.append((line, f"{norm(ar['plain'])}~{norm(br['plain'])}", ar, br))
            elif ar:
                a_only.append(ar)
            else:
                b_only.append(br)

    # rest matched by (line, plain) case/space-normalised
    def key(r):
        return (norm(r["line"]), norm(r["plain"]).lower())

    b_index = {}
    for r in b_rest:
        b_index.setdefault(key(r), []).append(r)

    used_b_ids = set()
    for ar in a_rest:
        k = key(ar)
        cand = [r for r in b_index.get(k, []) if id(r) not in used_b_ids]
        if cand:
            br = cand[0]
            used_b_ids.add(id(br))
            pairs.append((ar["line"], ar["plain"], ar, br))
        else:
            a_only.append(ar)
    for br in b_rest:
        if id(br) not in used_b_ids:
            b_only.append(br)

    # fallback: leftover non-header, non-alphabet rows pair by line number alone when
    # exactly one is left over on each side (independent passes read correspondent names
    # very differently letter-for-letter -- e.g. "Treues" vs "Trèves" -- but each line of
    # the key list names exactly one correspondent, so the line number is the real anchor)
    def fallback_eligible(r):
        return r["section"].strip().lower() not in ("header", "alphabet")

    a_left = [r for r in a_only if fallback_eligible(r)]
    b_left = [r for r in b_only if fallback_eligible(r)]
    from collections import Counter
    a_lines = Counter(r["line"] for r in a_left)
    b_lines = Counter(r["line"] for r in b_left)
    still_a_only, still_b_only = [], []
    for r in a_only:
        if fallback_eligible(r) and a_lines[r["line"]] == 1 and b_lines.get(r["line"]) == 1:
            br = next(x for x in b_left if x["line"] == r["line"])
            pairs.append((r["line"], f"{norm(r['plain'])}~{norm(br['plain'])} [line-matched, spelling differs]", r, br))
        else:
            still_a_only.append(r)
    for r in b_only:
        if fallback_eligible(r) and b_lines[r["line"]] == 1 and a_lines.get(r["line"]) == 1:
            pass  # already consumed above via its A partner
        else:
            still_b_only.append(r)
    a_only, b_only = still_a_only, still_b_only

    out_dir = Path(args.out_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    n_match = 0
    with open(out_dir / "agreement.tsv", "w", newline="") as fa, \
         open(out_dir / "disagreements.tsv", "w", newline="") as fd:
        wa = csv.writer(fa, delimiter="\t")
        wd = csv.writer(fd, delimiter="\t")
        wa.writerow(["line", "plain", "sign_code_A", "sign_code_B"])
        wd.writerow(["line", "plain_A", "plain_B", "sign_code_A", "sign_code_B", "note_A", "note_B"])
        for line, plain, ar, br in pairs:
            ca, cb = norm(ar["sign_code"]), norm(br["sign_code"])
            if ca == cb and ca != "":
                n_match += 1
                wa.writerow([line, plain, ca, cb])
            elif ca == "" and cb == "":
                # both blank/uncoded: not a genuine sign_code agreement, but not a conflict either
                wd.writerow([line, ar["plain"], br["plain"], ca, cb, ar.get("note",""), br.get("note","")])
            else:
                wd.writerow([line, ar["plain"], br["plain"], ca, cb, ar.get("note",""), br.get("note","")])

    total_pairs = len(pairs)
    pct = (100.0 * n_match / total_pairs) if total_pairs else 0.0
    print(f"paired rows: {total_pairs}")
    print(f"agreeing (non-blank, matching sign_code): {n_match}")
    print(f"agreement: {pct:.1f}%")
    print(f"A-only rows (no B counterpart): {len(a_only)}")
    print(f"B-only rows (no A counterpart): {len(b_only)}")
    if a_only:
        print("A-only:", [(r["line"], r["plain"]) for r in a_only])
    if b_only:
        print("B-only:", [(r["line"], r["plain"]) for r in b_only])

if __name__ == "__main__":
    main()

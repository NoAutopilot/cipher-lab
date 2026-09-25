#!/usr/bin/env python3
"""Reconcile two blind pass TSVs (leaf, order, code, gloss, note) of the Janssens
decipherment leaves into key.tsv (code -> value) and conflicts.tsv.

Usage: python3 build_key.py passA.tsv passB.tsv --out-dir .
"""
import argparse
import csv
import difflib
import sys
from collections import defaultdict


def load(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            rows.append(row)
    return rows


def norm(s):
    return (s or "").strip()


def glossnorm(s):
    """Comparison key for a gloss: fold trailing punctuation/case/apostrophe-style
    differences that are not a real reading disagreement (e.g. 'Batavia' vs
    'Batavia,', or a curly vs straight apostrophe)."""
    s = norm(s).lower().replace("’", "'")
    return s.rstrip(".,;:!?- ")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("passA")
    ap.add_argument("passB")
    ap.add_argument("--out-dir", default=".")
    args = ap.parse_args()

    a_rows = load(args.passA)
    b_rows = load(args.passB)

    a_by_leaf = defaultdict(list)
    b_by_leaf = defaultdict(list)
    for row in a_rows:
        a_by_leaf[row["leaf"]].append(row)
    for row in b_rows:
        b_by_leaf[row["leaf"]].append(row)

    agree_rows = []
    disagree_rows = []
    unmatched_rows = []
    for leaf in sorted(set(a_by_leaf) | set(b_by_leaf), key=lambda x: int(x)):
        al = a_by_leaf.get(leaf, [])
        bl = b_by_leaf.get(leaf, [])
        # Align by CODE VALUE sequence (difflib), not row index: a pass that
        # skips or adds a whole code cascades every later row-index pairing
        # otherwise (seen on leaf 191, pass A missing one full code-line).
        a_codes = [norm(r["code"]) for r in al]
        b_codes = [norm(r["code"]) for r in bl]
        sm = difflib.SequenceMatcher(None, a_codes, b_codes, autojunk=False)
        for tag, i1, i2, j1, j2 in sm.get_opcodes():
            if tag == "equal":
                for k in range(i2 - i1):
                    ra, rb = al[i1 + k], bl[j1 + k]
                    ca, ga = norm(ra["code"]), norm(ra["gloss"])
                    cb, gb = norm(rb["code"]), norm(rb["gloss"])
                    rec = {
                        "leaf": leaf, "order": i1 + k + 1,
                        "codeA": ca, "glossA": ga, "noteA": norm(ra["note"]),
                        "codeB": cb, "glossB": gb, "noteB": norm(rb["note"]),
                    }
                    if glossnorm(ga) == glossnorm(gb) and ca:
                        agree_rows.append(rec)
                    else:
                        disagree_rows.append(rec)
            else:
                for k in range(i1, i2):
                    ra = al[k]
                    unmatched_rows.append({
                        "leaf": leaf, "order": k + 1, "pass": "A",
                        "code": norm(ra["code"]), "gloss": norm(ra["gloss"]), "note": norm(ra["note"]),
                    })
                for k in range(j1, j2):
                    rb = bl[k]
                    unmatched_rows.append({
                        "leaf": leaf, "order": k + 1, "pass": "B",
                        "code": norm(rb["code"]), "gloss": norm(rb["gloss"]), "note": norm(rb["note"]),
                    })

    # Build key.tsv from agreed (code, gloss) pairs, counting occurrences and pages.
    # Group by normalized gloss so 'Batavia' / 'Batavia,' don't split into a false conflict;
    # the displayed value is the most common (then longest) literal surface form seen.
    # A row either pass flagged corrected/crossed-out is excluded from the *clean* pool
    # (both passes literally agreeing on a struck-through draft word is not the same as
    # both passes reading a clean cell) and only falls back to it if a code has no clean
    # occurrence at all -- seen concretely on code 689 (clean, unanimous "de" at leaf
    # 190/191 line 1) vs one corrected/crossed cell elsewhere both passes render as
    # "le"/"corvette"-then-struck: the clean reading wins.
    def is_shaky(rec):
        return bool(rec["noteA"]) or bool(rec["noteB"])

    key = defaultdict(lambda: defaultdict(lambda: {"n": 0, "pages": set(), "surface": defaultdict(int)}))
    shaky_only = defaultdict(lambda: defaultdict(lambda: {"n": 0, "pages": set(), "surface": defaultdict(int)}))
    for rec in agree_rows:
        code = rec["codeA"]
        gloss = rec["glossA"]
        if not code or not gloss:
            continue
        gnorm = glossnorm(gloss)
        bucket = shaky_only if is_shaky(rec) else key
        bucket[code][gnorm]["n"] += 1
        bucket[code][gnorm]["pages"].add(rec["leaf"])
        bucket[code][gnorm]["surface"][gloss] += 1
    # codes with no clean occurrence at all fall back to their shaky (corrected/crossed) one
    for code, variants in shaky_only.items():
        if code not in key:
            key[code] = variants

    # key.tsv carries every code decode_key.py can use, grade C (clean, single reading)
    # or M (ambiguous: >1 variant seen, or only a corrected/crossed-out cell seen) with the
    # ambiguity spelled out in note. conflicts.tsv is the human-readable log of the M codes.
    conflicts = []
    key_out = []
    for code, variants in sorted(key.items(), key=lambda x: int(x[0])):
        surfaces = {g: max(i["surface"].items(), key=lambda kv: (kv[1], len(kv[0])))[0] for g, i in variants.items()}
        ranked = sorted(variants.items(), key=lambda kv: -kv[1]["n"])
        top_gnorm, top_info = ranked[0]
        value = surfaces[top_gnorm]
        n_total = sum(i["n"] for i in variants.values())
        pages = sorted({p for i in variants.values() for p in i["pages"]}, key=int)
        if len(variants) == 1 and key[code] is not shaky_only.get(code):
            key_out.append({"code": code, "value": value, "n": n_total,
                             "pages": ",".join(pages), "grade": "C", "note": ""})
        else:
            note = "only a corrected/crossed-out cell seen" if key[code] is shaky_only.get(code) else (
                "ambiguous: " + "; ".join(f"{surfaces[g]} (n={i['n']}, pages={','.join(sorted(i['pages'], key=int))})"
                                           for g, i in ranked))
            key_out.append({"code": code, "value": value, "n": n_total,
                             "pages": ",".join(pages), "grade": "M", "note": note})
            if len(variants) > 1:
                conflicts.append({"code": code, "variants": "; ".join(
                    f"{surfaces[g]} (n={i['n']}, pages={','.join(sorted(i['pages'], key=int))})" for g, i in ranked)})

    # Codes only one pass read (the other pass skipped a whole code-line, e.g. leaf 191
    # "encore le certifie t demande par") add a single-pass, grade-M entry when the code
    # has no clean/agreed reading already -- a graded single-witness reading beats no
    # reading at all for a target decode, but it must never displace an agreed one.
    known = {row["code"] for row in key_out}
    single_pass = defaultdict(lambda: defaultdict(lambda: {"n": 0, "pages": set(), "surface": defaultdict(int)}))
    for row in unmatched_rows:
        code, gloss = row["code"], row["gloss"]
        if not code or not gloss or row["note"] == "crossed-out":
            continue
        gnorm = glossnorm(gloss)
        single_pass[code][gnorm]["n"] += 1
        single_pass[code][gnorm]["pages"].add(row["leaf"])
        single_pass[code][gnorm]["surface"][gloss] += 1
    for code, variants in sorted(single_pass.items(), key=lambda x: int(x[0])):
        if code in known:
            continue
        gnorm, info = max(variants.items(), key=lambda kv: kv[1]["n"])
        surface = max(info["surface"].items(), key=lambda kv: (kv[1], len(kv[0])))[0]
        key_out.append({"code": code, "value": surface, "n": info["n"],
                         "pages": ",".join(sorted(info["pages"], key=int)), "grade": "M",
                         "note": "single-pass only, other pass skipped this code"})
        known.add(code)

    key_out.sort(key=lambda r: int(r["code"]))
    with open(f"{args.out_dir}/key.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "value", "n", "pages", "grade", "note"], delimiter="\t")
        w.writeheader()
        for row in key_out:
            w.writerow(row)

    with open(f"{args.out_dir}/conflicts.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["code", "variants"], delimiter="\t")
        w.writeheader()
        for row in conflicts:
            w.writerow(row)

    with open(f"{args.out_dir}/pass_disagreements.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["leaf", "order", "codeA", "glossA", "noteA", "codeB", "glossB", "noteB"], delimiter="\t")
        w.writeheader()
        for row in disagree_rows:
            w.writerow(row)

    with open(f"{args.out_dir}/pass_unmatched.tsv", "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["leaf", "order", "pass", "code", "gloss", "note"], delimiter="\t")
        w.writeheader()
        for row in unmatched_rows:
            w.writerow(row)

    total = len(agree_rows) + len(disagree_rows)
    print(f"aligned code positions: {total}  agree: {len(agree_rows)}  disagree: {len(disagree_rows)}  "
          f"agreement: {len(agree_rows)/total*100:.1f}%" if total else "no aligned positions")
    print(f"codes only one pass saw (sequence gap): {len(unmatched_rows)}")
    print(f"unique codes: {len(key)}  clean (single gloss): {len(key_out)}  conflicting: {len(conflicts)}")


if __name__ == "__main__":
    main()

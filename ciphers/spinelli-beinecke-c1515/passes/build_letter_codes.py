#!/usr/bin/env python3
"""Regenerate the letter's coded transcription files from the two reconciled pass files (rule 7 for a transcription:
a script rebuilds the committed file and exits non-zero if it is stale).

  letter_codes_v3.tsv  = p1_reconciled.tsv + p2_reconciled.tsv, fragments (`_`) dropped, v2 codes folded to the
                         atlas v3 families (H15/H10; the file the spec and H16/H22/H28 used).
  letter_codes_v3b.tsv = the same, with the p.[1] HOOK boxes that BOTH H14 blind passes (p1_HOOK_passE/F.tsv) coded
                         as the same v2 member shape written as that sub-code at grade AB (H27, 28 Sept 2026); a box
                         both passes called FRAG is dropped as a fragment. Boxes the two passes disagreed on stay HOOK.
  letter_codes_v4.tsv  = p1_reconciled_v4.tsv + p2_reconciled_v4.tsv (passes/reconcile_opus.py: the Opus blind pass
                         pairs G/H, I/J, K/L reconciled, H29b/H29c/H30, 28 Sept 2026), fragments dropped; codes are
                         atlas v3 plus JHOOK and EPSILON.
  ciphertext_v3.txt / ciphertext_v3b.txt / ciphertext_v4.txt = the codes as space-separated tokens, one line per cipher line, for
                         tools/family_run.py --cipher ... --tokens space.

  python3 passes/build_letter_codes.py            # write all four files
  python3 passes/build_letter_codes.py --check    # rebuild in memory, exit 1 if any committed file differs
"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
V2_TO_V3 = {"LONGS": "HOOK", "ELOOP": "HOOK", "AMP": "HOOK", "UCURL": "HOOK", "RHO": "HOOK", "TLOOP": "HOOK",
            "ECAP": "HOOK", "MU": "HOOK", "TWOFLAT": "TWO", "DEE": "TWO", "SEVENB": "SEVEN", "CARET": "SEVEN",
            "OMEGA2": "OMEGABAR", "EX": "XCURL", "STROKE": "_"}
HOOK_MEMBERS = {"ELOOP", "ECAP", "RHO", "TLOOP", "UCURL", "MU"}


def rows(path):
    with open(os.path.join(HERE, path), newline="", encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def agreed_hook_subcodes():
    E = {r["label"]: r["code"] for r in rows("p1_HOOK_passE.tsv")}
    F = {r["label"]: r["code"] for r in rows("p1_HOOK_passF.tsv")}
    out = {}
    for lab, c in E.items():
        if F.get(lab) == c and (c in HOOK_MEMBERS or c == "FRAG"):
            out[lab] = "_" if c == "FRAG" else c
    return out


def build(variant):
    sub = agreed_hook_subcodes() if variant == "v3b" else {}
    out = []
    src = (("p1", "p1_reconciled_v4.tsv"), ("p2", "p2_reconciled_v4.tsv")) if variant == "v4" else \
          (("p1", "p1_reconciled.tsv"), ("p2", "p2_reconciled.tsv"))
    for page, path in src:
        for r in rows(path):
            code = r["code"].strip()
            grade = r["grade"].strip()
            lab = f"L{r['line']}.{r['box']}"
            if page == "p1" and lab in sub and code == "HOOK":
                code, grade = sub[lab], "AB"
            else:
                code = V2_TO_V3.get(code, code)
            if code == "_":
                continue
            out.append((page, r["line"], r["pos"], code, grade))
    return out


def tsv(out):
    return "page\tline\tpos\tcode\tgrade\n" + "".join("\t".join(r) + "\n" for r in out)


def txt(out):
    lines, cur, key = [], [], None
    for page, line, pos, code, grade in out:
        if (page, line) != key and cur:
            lines.append(" ".join(cur)); cur = []
        key = (page, line); cur.append(code)
    if cur:
        lines.append(" ".join(cur))
    return "\n".join(lines) + "\n"


def main():
    check = "--check" in sys.argv
    stale = 0
    for variant in ("v3", "v3b", "v4"):
        out = build(variant)
        for name, content in ((f"letter_codes_{variant}.tsv", tsv(out)), (f"ciphertext_{variant}.txt", txt(out))):
            p = os.path.join(HERE, name)
            if check:
                old = open(p, encoding="utf-8").read() if os.path.exists(p) else None
                if old != content:
                    print(f"STALE: {name}"); stale += 1
                else:
                    print(f"ok: {name} ({len(out)} codes)")
            else:
                open(p, "w", encoding="utf-8").write(content)
                print(f"wrote {name} ({len(out)} codes)")
    if check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()

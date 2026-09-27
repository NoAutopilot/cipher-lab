#!/usr/bin/env python3
"""SALV-SPLIT (27 Sept 2026): build a CANDIDATE spec from the 98 [C]-flagged plain boxes this job's blind
crop check independently confirmed as sign (of 137 originally flagged; see NOTES.md "SALV-SPLIT"), leaving
the real spec and ciphertext_<leaf>.tsv files untouched.

Reads ciphertext_<leaf>.split-candidate.tsv for the five leaves with confirmed relabels (f54r, f54v, f55r,
f56r, f56v: written by this job from confirmed.json) and the ordinary ciphertext_<leaf>.tsv for the other
three (f55v, f57r, f57v: unaffected, 0 confirmed). Otherwise identical logic to build_spec.py.

Confirmed-sign boxes get code = the crop check's nearest atlas-glyph guess (or "UNK" if it answered
"unclear"), marks = "" (bare sign placeholder -- this check did not attempt to read a mark, only whether
the box is sign-like). This is a CANDIDATE relabelling for sizing the delta, not a transcription: every
UNK/guessed code needs a real transcription pass before any family is re-run on this text (see NOTES.md).

  python3 ciphers/fr2933-salviati-1525/build_spec_candidate.py
    -> writes specs/fr2933-salviati-1525.split-candidate.json
       and ciphers/fr2933-salviati-1525/ciphertext.split-candidate.txt (one sign-run per line, space-joined
       code^marks tokens, same convention as the real spec's own "ciphertext" list)
"""
import csv, json, os

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(D))
OUT_SPEC = os.path.join(ROOT, "specs", "fr2933-salviati-1525.split-candidate.json")
OUT_TXT = os.path.join(D, "ciphertext.split-candidate.txt")
LEAVES = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")
CANDIDATE_LEAVES = {"f54r", "f54v", "f55r", "f56r", "f56v"}


def rows():
    for lf in LEAVES:
        fname = f"ciphertext_{lf}.split-candidate.tsv" if lf in CANDIDATE_LEAVES else f"ciphertext_{lf}.tsv"
        for x in csv.DictReader(open(os.path.join(D, fname)), delimiter="\t"):
            if lf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15:
                continue
            yield lf, x


def build():
    runs, pattern, cur, prev = [], [], [], None
    for lf, x in rows():
        key = (lf, x["line"])
        if key != prev and cur:
            runs.append(cur); cur = []
        prev = key
        if x["code"] != "_":
            cur.append(f"{x['code']}^{x['marks']}"); pattern.append("S")
        else:
            if cur:
                runs.append(cur); cur = []
            pattern.append("_")
    if cur:
        runs.append(cur)
    return runs, "".join(pattern)


def main():
    runs, pattern = build()
    toks = [t for r in runs for t in r]
    real_spec = json.load(open(os.path.join(ROOT, "specs", "fr2933-salviati-1525.json"), encoding="utf-8"))
    spec = dict(real_spec)
    spec["ciphertext"] = [" ".join(r) for r in runs]
    spec["row_pattern"] = pattern
    spec["cheap_test_done"] = []
    spec["written"] = ("27 Sept 2026, SALV-SPLIT candidate (Sonnet): 98 of 137 [C]-flagged plain boxes "
                        "reclassified sign/mixed by a blind atlas crop check (matched control gate, "
                        "NOTES.md 'SALV-SPLIT'); not adopted, sizing only")
    with open(OUT_SPEC, "w", encoding="utf-8") as f:
        json.dump(spec, f, indent=1, ensure_ascii=False)
    with open(OUT_TXT, "w", encoding="utf-8") as f:
        for r in runs:
            f.write(" ".join(r) + "\n")
    print(f"wrote {OUT_SPEC}: {len(toks)} tokens, {len(set(toks))} types, {len(runs)} runs, "
          f"pattern {len(pattern)} boxes ({pattern.count('_')} plain)")
    print(f"wrote {OUT_TXT}")


if __name__ == "__main__":
    main()

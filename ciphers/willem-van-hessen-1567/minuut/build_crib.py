#!/usr/bin/env python3
"""Build the normalised crib for the 1127 cipher passage from the reconciled minuut transcription.

  python3 build_crib.py           write crib_norm.tsv (one row per minuut line) and crib_stream.txt (letters only)
  python3 build_crib.py --check   exit 1 if the committed outputs are stale

Normalisation (for aligning against a letter cipher, not for reading): {del: ...} dropped, {ins: ...} inlined,
brackets and '?' dropped, lower case, u/v -> u, j/y -> i, umlauts folded (ä->a, ö->o, ü->u), punctuation and
'&c' dropped, word-final hyphens joined to the next line. Abbreviations (E.L., Ld, Kay: Mt:, Kö: Wür:) are kept
as their letters, since the enciphered original may abbreviate the same way or not -- the aligner decides.
Address, signature and date lines (page 4 lines 20-22) are excluded from the stream; they are flagged in the TSV.
"""
import csv, re, sys, os
H = os.path.dirname(os.path.abspath(__file__))
SKIP = {(4, 20), (4, 21), (4, 22)}

def norm(t):
    t = re.sub(r"\{del:[^}]*\}", "", t)
    t = re.sub(r"\{ins:\s*([^}]*)\}", r"\1", t)
    t = re.sub(r"[\[\]?]", "", t).replace("&c", "").lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("v", "u"), ("j", "i"), ("y", "i"), ("ß", "ss")):
        t = t.replace(a, b)
    hyph = t.rstrip().endswith("-")
    t = re.sub(r"[^a-z0-9 ]", " ", t)
    return re.sub(r"\s+", " ", t).strip(), hyph

def build():
    rows, stream, carry = [], [], False
    for r in csv.DictReader(open(os.path.join(H, "reconciled.tsv")), delimiter="\t"):
        p, l = int(r["page"]), int(r["line"])
        n, hyph = norm(r["text"])
        inc = (p, l) not in SKIP
        rows.append((p, l, r["status"], "yes" if inc else "no", n))
        if inc:
            stream.append(("" if carry else " ") + n)
            carry = hyph
    tsv = "page\tline\tstatus\tin_stream\tnorm\n" + "".join("\t".join(map(str, x)) + "\n" for x in rows)
    letters = re.sub(r"[^a-z]", "", "".join(stream))
    return tsv, "".join(stream).strip() + "\n", letters + "\n"

if __name__ == "__main__":
    out = dict(zip(("crib_norm.tsv", "crib_words.txt", "crib_stream.txt"), build()))
    if "--check" in sys.argv:
        stale = [f for f, v in out.items() if not os.path.exists(os.path.join(H, f)) or open(os.path.join(H, f)).read() != v]
        print("stale: " + ", ".join(stale) if stale else "ok: crib outputs current"); sys.exit(1 if stale else 0)
    for f, v in out.items(): open(os.path.join(H, f), "w").write(v)
    print(f"wrote {', '.join(out)}; {len(out['crib_stream.txt'])-1} letters")

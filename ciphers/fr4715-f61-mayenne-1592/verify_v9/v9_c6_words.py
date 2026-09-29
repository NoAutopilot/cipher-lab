#!/usr/bin/env python3
"""VERIFY-F61-V9: does the pooled C6 = e survive Tomokiyo's own words on f.61? For every in-span C6 (and, for comparison, CA) in the runner's
sign-to-markup alignment (family/h259_ca_span_result.txt, taken as given), insert the cell letter into the span's letter string at that sign's
place and say whether it lands inside a word he reads (breaks it) or at a word boundary (no break, no support). Words per span from
scripts/tomokiyo_spans.tsv's letters, cut at the boundaries his own reading implies (est|capable, trop|avancees, eau|beau|pere, me|l|entenoit).
Script-only. python3 v9_c6_words.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
WORDS = {"S1": ["avec"], "S2": ["est", "capable"], "S3": ["trop", "avancees"], "S4a": ["jalousi"], "S4b": ["eau", "beau", "pere"], "S5": ["me", "l", "entenoit"]}
rows = [r for r in csv.DictReader((l for l in open(f"{F}/h259_ca_span_result.txt") if "\t" in l), delimiter="\t") if r.get("span")]
def main():
    out = ["class\tletter\tspan\tline\tpos\tstring_with_letter\tverdict"]; tally = {}
    for cls, letter in (("C6", "e"), ("CA", "a")):
        for s in dict.fromkeys(r["span"] for r in rows):
            sp = [r for r in rows if r["span"] == s]; words = WORDS[s]; ends = []; n = 0
            for w in words: n += len(w); ends.append(n)
            for i, r in enumerate(sp):
                if r["class"] != cls: continue
                k = sum(1 for q in sp[:i] if q["markup"] not in ("-", "(skipped)"))   # letters before this sign
                total = ends[-1]; L = letter.upper(); letters = "".join(words)
                string = letters[:k] + L + letters[k:]
                if k == 0 or k == total: v = "span edge: no test"
                elif k in ends: v = "word boundary (" + "|".join(words) + "): no break, no support"
                else:
                    w = next(j for j, e in enumerate(ends) if k < e); v = f"inside '{words[w]}' -> '{string[(ends[w-1] if w else 0):ends[w] + 1]}': breaks it"
                out.append(f"{cls}\t{letter}\t{s}\t{r['line']}\t{r['pos']}\t{string}\t{v}"); tally.setdefault(cls, []).append(v.split(":")[0].split(" ->")[0])
    for cls, vs in tally.items():
        from collections import Counter
        out.append(f"# {cls}: " + "; ".join(f"{k} {n}" for k, n in Counter(("inside a word" if v.startswith("inside") else v) for v in vs).items()))
    txt = "\n".join(out) + "\n"; p = f"{HERE}/v9_c6_words_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()

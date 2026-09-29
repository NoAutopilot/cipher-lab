#!/usr/bin/env python3
"""VERIFY-F61-V9: does the pooled C6 = e survive Tomokiyo's own words on f.61? For every in-span C6 (family/h259_ca_span_result.txt, the runner's
sign-to-markup alignment, taken as given), print his word around the position with an e inserted there, and say whether the word he reads is
complete without it. Script-only; the same table for CA. python3 v9_c6_words.py [--check]"""
import csv, os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); F = os.path.abspath(f"{HERE}/../family")
rows = [r for r in csv.DictReader((l for l in open(f"{F}/h259_ca_span_result.txt") if "\t" in l), delimiter="\t") if r.get("span")]
def main():
    out = ["span\tline\tpos\tclass\tmarkup_with_letter_inserted\tword_complete_without_it"]
    for cls, letter in (("C6", "e"), ("CA", "a")):
        for s in dict.fromkeys(r["span"] for r in rows):
            sp = [r for r in rows if r["span"] == s]; mk = [r["markup"] if r["markup"] not in ("-", "(skipped)") else "-" for r in sp]
            for i, r in enumerate(sp):
                if r["class"] != cls: continue
                m = mk[:]; m[i] = letter.upper()
                # the word: letters on both sides up to a dash that is not this position
                L = i - 1; R = i + 1
                while L >= 0 and mk[L] != "-": L -= 1
                while R < len(mk) and mk[R] != "-": R += 1
                word = "".join(m[L + 1:R]); sides = (L + 1 < i, R > i + 1)
                out.append(f"{s}\t{r['line']}\t{r['pos']}\t{cls}\t{''.join(m)}\t{'yes: ' + word.replace(letter.upper(), '') + ' -> ' + word if all(sides) else 'no test (a span edge on one side): ' + word}")
    txt = "\n".join(out) + "\n"; p = f"{HERE}/v9_c6_words_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(p) and open(p).read() == txt; print("check", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(p, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()

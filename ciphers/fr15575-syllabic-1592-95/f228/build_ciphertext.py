#!/usr/bin/env python3
"""NV05E: tokenise the reconciled f.228 L01-L04 lines (PREREG.md rule) into ciphertext.tsv; report err_2reader.

  python3 build_ciphertext.py [--check]

Tokens: maximal digit runs split into 2-digit codes from the left (odd final digit = single-digit token); maximal
letter runs as one token; every other sign its own token. conf H where passes A and B agree on the token (difflib
alignment of the tokenised passes), M where the worker settled it from the crop or marked it uncertain.
"""
import difflib, os, re, sys
HERE = os.path.dirname(os.path.abspath(__file__))
FINAL = {
 "L01": "80 . 80 : 23 se 9i ^ 8875 . 68y 48 fel ^ 44527 . 40 . ( 198921 944634 : 8321 4873 ^ /",
 "L02": "65 : 82 n 78 . fq 73 nh 23 7¨ 23 v 8411 q48 ^ 73 87 62 n 78 x 68y 45 55 . 16 . nol 54e . 1022",
 "L03": "89 6334 qnh dol 2451989 68 8175 far v24 . 55 6221 ^ L 4873 4689 . 48 ^ 23 ca n ^ 2394 ^",
 "L04": "80 . 17 c 73 92 16 . 57 90 . 33 6922 n 75 5924 : 45 45 88 : 82 n 75 68y n 48 80 . 23 moe 3464 sc 68y",
}
SETTLED = {("L01", "44527"), ("L01", "("), ("L02", "7¨"), ("L03", "48"), ("L03", "L")}  # worker-settled runs -> M


def toks(line):
    out = []
    for w in line.split():
        w = w.rstrip("?")
        for m in re.finditer(r"\d+|[A-Za-z]+|.", w):
            s = m.group()
            if s.isdigit():
                out += [s[i:i + 2] for i in range(0, len(s), 2)]
            else:
                out.append(s)
    return out


def runs(line):
    return [(w, toks(w)) for w in line.split()]


def passes(name):
    return {l.split("\t")[0]: l.rstrip("\n").split("\t")[1] for l in open(os.path.join(HERE, name), encoding="utf-8")}


def main():
    A, B = passes("passA.tsv"), passes("passB.tsv")
    rows = ["line\tpos\tsign\tconf"]; agree = tot = 0
    for ln in sorted(FINAL):
        ta, tb = toks(A[ln]), toks(B[ln])
        sm = difflib.SequenceMatcher(a=ta, b=tb, autojunk=False)
        same = sum(b.size for b in sm.get_matching_blocks()); agree += same; tot += max(len(ta), len(tb))
        pos = 0
        for w, ts in runs(FINAL[ln]):
            for t in ts:
                pos += 1
                rows.append(f"{ln}\t{pos}\t{t}\t{'M' if (ln, w) in SETTLED else 'H'}")
    text = "\n".join(rows) + "\n"
    path = os.path.join(HERE, "ciphertext.tsv")
    if "--check" in sys.argv:
        ok = os.path.exists(path) and open(path, encoding="utf-8").read() == text
        print("ciphertext.tsv up to date" if ok else "ciphertext.tsv is stale"); sys.exit(0 if ok else 1)
    open(path, "w", encoding="utf-8").write(text)
    print(f"tokens {len(rows) - 1}; err_2reader = {tot - agree}/{tot} = {(tot - agree) / tot:.3f}")


if __name__ == "__main__":
    main()

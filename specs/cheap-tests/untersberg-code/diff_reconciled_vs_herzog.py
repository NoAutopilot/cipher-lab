#!/usr/bin/env python3
"""untersberg-code NEAR step (4b), 26 Sept 2026, LANE B6 worker bUNT8.

Same method as bUNT6's diff_blind_pass.py (character-level SequenceMatcher on
period/space-stripped, lowercased strings per line -- PX-BRODEC / rule 3), run
against the reconciled text (reconciled.tsv) instead of the raw blind pass.
HERZOG_LINES is copied verbatim from diff_blind_pass.py (Herzog 1929 p.28,
witnesses.tsv siglum "1"). The three recurring ligatures (symA, symA-rev,
symB) each collapse to one placeholder character, the same treatment
diff_blind_pass.py already gives Herzog's ETH suspension glyph, so a
multi-character bracket tag does not inflate the character count against
Herzog's one-guess-per-glyph print.

Usage: python3 diff_reconciled_vs_herzog.py
"""
import difflib

HERZOG_LINES = {
    1: ["S", "ETH", "ETH", "occo", "x"],
    2: ["Satrnrop", "5", "a", "f", "5", "l", "d"],
    3: ["P", "6", "m", "6", "a", "t", "5", "q", "o", "t", "m", "5", "r", "u", "a", "t"],
    4: ["m", "519", "r", "l", "v", "e", "p", "55", "a", "tt", "tt", "l", "x", "missm"],
    5: ["ariu", "a", "o", "u", "st", "g", "c", "x", "5", "l", "19", "alto", "mvraco"],
    6: ["mic", "r", "l", "y", "pymi", "l", "o", "p", "m", "i", "v", "m", "l", "t", "t", "g"],
}

RECONCILED_LINES = {
    1: ["S", "9", "9", "occo", "X"],
    2: ["Salr°nro[symA]", "5", "a[symB]5", "l", "h"],
    3: ["P", "G", "m", "G", "a", "l", "5", "g", "o", "l", "m5", "r", "u", "al"],
    4: ["m", "5ig", "r", "l", "[symA]", "e", "[symA]", "55", "a", "ll", "H", "l", "Xmissu"],
    5: ["ariu", "a", "o", "uftgcxs", "l", "ih", "allomVraco"],
    6: ["nicrlr", "[symA][symA-rev]mi", "lo[symA]mi", "vmult", "lg"],
}


def normalize(tokens):
    out = []
    for t in tokens:
        s = t if t == "ETH" else t.lower()
        s = s.replace("eth", "~") if t == "ETH" else s
        s = s.replace("[symA-rev]", "&").replace("[syma-rev]", "&")
        s = s.replace("[symA]", "@").replace("[syma]", "@")
        s = s.replace("[symB]", "%").replace("[symb]", "%")
        if t == "ETH":
            s = "~"
        out.append(s)
    return "".join(out)


def main():
    total_chars = 0
    total_matched = 0
    print("line | herzog (normalized)          | reconciled (normalized)       | char-match ratio")
    print("-" * 100)
    for line_no in range(1, 7):
        h = normalize(HERZOG_LINES[line_no])
        r = normalize(RECONCILED_LINES[line_no])
        sm = difflib.SequenceMatcher(a=h, b=r, autojunk=False)
        ratio = sm.ratio()
        matched = sum(block.size for block in sm.get_matching_blocks())
        total_chars += max(len(h), len(r))
        total_matched += matched
        print(f"{line_no:4} | {h:<29} | {r:<29} | {ratio:.3f} ({matched} matched chars of max({len(h)},{len(r)})={max(len(h), len(r))})")

    overall = total_matched / total_chars
    print("-" * 100)
    print(f"Overall: {total_matched} matched chars / {total_chars} = {overall:.3f}")
    print()
    print("For comparison, bUNT6's raw blind_pass vs Herzog (unreconciled): 75/109 = 0.688")


if __name__ == "__main__":
    main()

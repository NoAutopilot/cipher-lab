#!/usr/bin/env python3
"""untersberg-code NEAR step (2b), 26 Sept 2026, LANE B5 worker bUNT6.

Diffs a blind transcription of the confirmed inscription leaf (Salzburg Museum
Sammlung Online, opening 11, ciphers/untersberg-code/images/hs2398_opening11_
inscription_leaf.jpg) against Herzog 1929's own diplomatic print of Hs 1 (p.28,
as transcribed and image-checked into witnesses.tsv by LANE B4 bUNT5).

The blind pass (a Sonnet subagent given only the image, no prior transcription)
tokenized on its own visual read of letter groups, not on Herzog's period/space
convention -- several of its tokens fuse what Herzog's print separates with a
period (e.g. blind "ak5" where Herzog reads three separate tokens "a. f. 5.").
Per CLAUDE.md rule 3's PX-BRODEC lesson (25 Sept 2026), diffing two renderings
of the same text under different transcription conventions without normalizing
first measures notation, not agreement. So this script normalizes BOTH sides to
one convention per line -- a single lowercase, period/space-stripped character
string -- before diffing, using difflib's character-level SequenceMatcher
(reports a ratio, not a token-position match, since token boundaries differ
between the two passes).

No tokens are graded H, C or S by this diff: there is no key and no known
plaintext for this target (rule 4); this is purely a transcription cross-check,
reported as character-agreement percentage per line and overall.

Usage: python3 diff_blind_pass.py
"""
import difflib

# Herzog 1929 p.28 diplomatic print, from witnesses.tsv siglum "1" (image-checked
# by bUNT5). "ETH" stands for the crossed-d suspension glyph (not a Latin letter,
# OCR misread as "fr"); kept as a single placeholder character '~' for comparison.
HERZOG_LINES = {
    1: ["S", "ETH", "ETH", "occo", "x"],
    2: ["Satrnrop", "5", "a", "f", "5", "l", "d"],
    3: ["P", "6", "m", "6", "a", "t", "5", "q", "o", "t", "m", "5", "r", "u", "a", "t"],
    4: ["m", "519", "r", "l", "v", "e", "p", "55", "a", "tt", "tt", "l", "x", "missm"],
    5: ["ariu", "a", "o", "u", "st", "g", "c", "x", "5", "l", "19", "alto", "mvraco"],
    6: ["mic", "r", "l", "y", "pymi", "l", "o", "p", "m", "i", "v", "m", "l", "t", "t", "g"],
}

# Blind pass (Sonnet subagent, image only), specs/cheap-tests/untersberg-code/blind_pass.tsv
BLIND_LINES = {
    1: ["S", "g", "g", "occo", "X"],
    2: ["Salrnrop", "s", "ak5", "l", "d"],
    3: ["B", "G", "m", "G", "a", "l", "5", "g", "o", "l", "m5", "r", "u", "al"],
    4: ["m", "sig", "r", "l", "H", "e", "p", "55", "a", "ll", "H", "l", "Xmissu"],
    5: ["ariu", "a", "o", "uftgcxs", "l", "ih", "allomVraco"],
    6: ["ueicrlr", "prmi", "loqui", "vult", "lg"],
}


def normalize(tokens):
    """Lowercase, join with no separator -- ETH becomes a single '~' placeholder."""
    out = []
    for t in tokens:
        out.append("~" if t == "ETH" else t.lower())
    return "".join(out)


def main():
    total_chars = 0
    total_matched = 0
    print("line | herzog (normalized)          | blind (normalized)           | char-match ratio")
    print("-" * 95)
    for line_no in range(1, 7):
        h = normalize(HERZOG_LINES[line_no])
        b = normalize(BLIND_LINES[line_no])
        sm = difflib.SequenceMatcher(a=h, b=b, autojunk=False)
        ratio = sm.ratio()
        matched = sum(block.size for block in sm.get_matching_blocks())
        total_chars += max(len(h), len(b))
        total_matched += matched
        print(f"{line_no:4} | {h:<29} | {b:<29} | {ratio:.3f} ({matched} matched chars of max({len(h)},{len(b)})={max(len(h),len(b))})")

    overall = total_matched / total_chars
    print("-" * 95)
    print(f"Overall: {total_matched} matched chars / {total_chars} = {overall:.3f}")
    print()
    print("Distinctive-token cross-check (rare strings, both passes independently landed on):")
    checks = [
        ("line1 'occo'", "occo" in normalize(HERZOG_LINES[1]).lower(), "occo" in normalize(BLIND_LINES[1]).lower()),
        ("line4/5 'missm'/'missu' boundary word", "missm" in normalize(HERZOG_LINES[4]), "xmissu" in normalize(BLIND_LINES[4])),
        ("line5 'mvraco'/'vraco'", "mvraco" in normalize(HERZOG_LINES[5]), "vraco" in normalize(BLIND_LINES[5])),
        ("line6 'pymi'/'prmi'", "pymi" in normalize(HERZOG_LINES[6]), "prmi" in normalize(BLIND_LINES[6])),
    ]
    for label, h_hit, b_hit in checks:
        print(f"  {label}: herzog={h_hit}, blind={b_hit}, {'AGREE' if h_hit==b_hit else 'DISAGREE'}")


if __name__ == "__main__":
    main()

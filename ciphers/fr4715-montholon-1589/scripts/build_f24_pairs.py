#!/usr/bin/env python3
"""Build tools/interlinear_align.py's PAIRS.tsv from f.24's reconciled (line, pos, group, gloss) rows.

MONT-KEY6, 27 Sept 2026. f.24 is an interlinear leaf: the clerk wrote the plain-French decipherment
directly above each cipher line. Two independent blind passes read (group, gloss) per position;
tools/reconcile_passes.py settles them into witness_f24/ciphertext_draft.tsv (columns line, position,
sign, confidence, alt, why, gloss -- the tool's own long format with a carried gloss column). This
script turns that into one (plain_raw, cipher_raw) pair per manuscript line for
tools/interlinear_align.py's `align` command.

Encoding used here, instead of a new tool option (CLAUDE.md Usage 8's own bar: use --floor's existing
below/at-or-above split, which already models exactly "one class takes one letter, the other a variable
span" -- our two classes are not split by numeral SIZE the way Thurloe's are, but by the dot/apostrophe
mark, so this script shifts a dotted group's numeral value by +100 before handing it to the tool, and
--floor 100 keeps every undotted group (values 1-99) as a single letter while every dotted group
(101-199, since this key's own digit range never exceeds 99) is free to take a multi-letter word span,
same as a Thurloe word-code. Reversed after alignment. classify_token() only parses a 1-3 digit numeral
as kind 'num' (`1 <= len(c) <= 3`) -- an earlier +1000 offset produced 4-digit values that silently fell
through to kind 'doubtful' instead (caught by a synthetic round-trip test before this ever touched the
real leaf's data: value 1047 came back with no 'value' column and OCR-candidate repair logic applied to
a token that was never doubtful). +100 keeps every shifted value at 3 digits or fewer. No cryptanalysis
in this script: it only reshapes signs already read from the image.

Symbol signs (key_vieuville_nevers.tsv's two non-numeral rows, printed as <...> bracket names by the
transcribing passes) are mapped to two reserved undotted pseudo-numerals below the floor (and below
every real sign in this key, whose highest value is 95) so they align as ordinary one-letter codes:
96 = the circle-with-bar glyph (value s), 97 = the open-triangle glyph (value x). Never conflated with a
real dotted or undotted digit group (both symbols are always undotted in this key).

    python3 scripts/build_f24_pairs.py witness_f24/ciphertext_draft.tsv witness_f24/pairs.tsv \
        [--shuffle-seed N]

--shuffle-seed N: for the rule-3 control, permute which line's plain_raw (gloss) is attached to which
line's cipher_raw before writing, everything else unchanged. Without it, pairs.tsv is the real
(unshuffled) leaf.
"""
import csv
import random
import sys

SYMBOL_TO_PSEUDO = {
    "<circle-with-bar>": "96", "<circle-bar>": "96", "<circle-crossed-by-bar>": "96",
    "<open-triangle>": "97", "<triangle>": "97", "<open-downward-triangle>": "97",
    "♀": "96", "▽": "97",  # the raw glyphs themselves, in case a pass copied them directly
}
DOTTED_OFFSET = 100


def group_to_token(group):
    """-> cipher_raw token, or None to drop this position (illegible/blank).
    Undotted digit group "47" -> token "47" (kind num, val 47, below floor 100 -- one letter).
    Dotted digit group "'47" -> token "147" (val 147, at/above floor 100 -- a word span).
    Known symbol glyph -> its reserved pseudo-numeral (below floor -- one letter).
    "[PLAIN:word]" or "?" or blank -> dropped (returns None); a literal clear word inline in the
    cipher row is rare enough on this leaf (not observed in either blind pass) not to warrant
    --clear-consumes plumbing this job."""
    g = (group or "").strip()
    if not g or g == "?":
        return None
    if g.startswith("[PLAIN:"):
        return None
    if g in SYMBOL_TO_PSEUDO:
        return SYMBOL_TO_PSEUDO[g]
    dotted = g.startswith("'")
    digits = g[1:] if dotted else g
    if not digits.isdigit():
        return None
    val = int(digits)
    return str(val + DOTTED_OFFSET) if dotted else str(val)


def build_lines(draft_path):
    """-> dict line_id -> (cipher_tokens: list[str], gloss_words: list[str]) in position order."""
    rows_by_line = {}
    with open(draft_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            line = r["line"]
            pos = int(r.get("position") or r.get("pos") or 0)
            rows_by_line.setdefault(line, []).append((pos, r))
    out = {}
    for line, rows in rows_by_line.items():
        rows.sort(key=lambda pr: pr[0])
        cipher_tokens = []
        gloss_words = []
        prev_gloss = None
        for _, r in rows:
            tok = group_to_token(r.get("sign") or r.get("group"))
            if tok is not None:
                cipher_tokens.append(tok)
            gloss = (r.get("gloss") or "").strip()
            if gloss and gloss != prev_gloss:
                gloss_words.append(gloss)
            prev_gloss = gloss if gloss else prev_gloss
        out[line] = (cipher_tokens, gloss_words)
    return out


def main():
    args = sys.argv[1:]
    seed = None
    if "--shuffle-seed" in args:
        k = args.index("--shuffle-seed")
        seed = int(args[k + 1])
        del args[k:k + 2]
    draft_path, out_path = args

    lines = build_lines(draft_path)
    line_ids = sorted(lines, key=lambda x: int(x))
    cipher_by_line = {lid: lines[lid][0] for lid in line_ids}
    gloss_by_line = {lid: lines[lid][1] for lid in line_ids}

    gloss_order = list(line_ids)
    if seed is not None:
        rng = random.Random(seed)
        shuffled = list(gloss_order)
        while True:
            rng.shuffle(shuffled)
            if all(a != b for a, b in zip(gloss_order, shuffled)):
                break
        gloss_order = shuffled

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["plain_line", "plain_raw", "cipher_line", "cipher_raw"])
        for lid, gloss_src_lid in zip(line_ids, gloss_order):
            cipher_raw = " ".join(cipher_by_line[lid])
            plain_raw = " ".join(gloss_by_line[gloss_src_lid])
            if not cipher_raw:
                continue
            w.writerow([lid, plain_raw, lid, cipher_raw])
    n_tok = sum(len(v) for v in cipher_by_line.values())
    print(f"{len(line_ids)} lines, {n_tok} cipher tokens, seed={seed}", file=sys.stderr)


if __name__ == "__main__":
    main()

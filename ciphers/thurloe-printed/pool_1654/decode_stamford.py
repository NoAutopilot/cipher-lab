#!/usr/bin/env python3
"""Regenerate the Stamford key, the cross-letter control and the P4 reading (rule 7).

    python3 decode_stamford.py            # writes key_stamford.tsv, control_stamford.tsv, reading_P4.txt
    python3 decode_stamford.py --check    # regenerates in memory, exits 1 if a committed file is stale

Key: align_stamford.py aligns P5+P6 (30 March) and P7 (20 March) with Birch's printed
decipherments; every meaning is grade C (known plaintext), except Tomokiyo's E values 12 and 25
(grade H, sources/cryptiana/web/thurloe.htm #Stamford). Control (rule 3, on real data): key from
one letter alone decodes the other letter's numerals blind, scored against that letter's own
alignment with its printed decipherment. P4 (13 March) has no printed decipherment; its numerals are
decoded with the full key and graded per token.

P4 source per range (NOTES.md s.16 worker G, s.18 worker I, s.21 this pass): djvu OCR for djvu
15469-15528, 15552-15562 (the real, undisordered "This plott is soe infalible ... naturall
aversion" paragraph between blocks A and B) and 15601-15645 -- all unchanged from worker G; the
page image (../P4/image_transcription.tsv, printed p.188 lines 50-61) replaces worker G's
OCR-disordered "block A" (djvu 15529-15551, s.16 item 4); worker G's "block B" (djvu 15563-15600)
is dropped entirely, since s.18 found it is not separate page content, only the OCR's own displaced
re-read of parts of block A's lines -- once the image gives block A's lines whole and in order,
block B's fragments add nothing that is not already covered.
"""
import sys
from collections import Counter, defaultdict
from pathlib import Path

import align_stamford as A

HERE = Path(__file__).resolve().parent
IMAGE_TSV = HERE.parent / "P4" / "image_transcription.tsv"
TOMOKIYO_H = {12: "e", 25: "e"}
MIN_VOTES, MIN_SHARE = 3, 0.7
ITERS = 4


def build_key(votes, codes):
    rows = {}
    for v, c in votes.items():
        x, n, t = A.best(c)
        grade = "H" if v in TOMOKIYO_H and TOMOKIYO_H[v] == x else (
            "C" if n >= MIN_VOTES and n / t >= MIN_SHARE else "M")
        if v == 34 and set(c) <= {"u", "v"}:
            x, n = "u/v", t
            grade = "C"
        rows[v] = (x, n, t, grade, " ".join(f"{k}:{m}" for k, m in c.most_common(4)))
    for v, c in codes.items():
        # a code value takes the most frequent chunk; the sign @ is "the lord protector"
        x, n, t = A.best(c)
        if v == A.THETA:
            x = "thelordprotector"
            n = sum(m for k, m in c.items() if "lordprote" in k)
        grade = "C" if n >= 2 and n / t >= 0.6 else "M"
        rows[v] = (x, n, t, grade, " ".join(f"{k}:{m}" for k, m in c.most_common(4)))
    return rows


def codes_of(als):
    codes = defaultdict(Counter)
    for al in als:
        for k, c in A.collect(al)[1].items():
            codes[k].update(c)
    return codes


def key_tsv(rows):
    out = ["value\tmeaning\tvotes\ttotal\tshare\tgrade\tall_readings"]
    for v in sorted(rows, key=lambda k: (isinstance(k, str), k if not isinstance(k, str) else 0)):
        x, n, t, g, allr = rows[v]
        out.append(f"{v}\t{x}\t{n}\t{t}\t{n / t:.2f}\t{g}\t{allr}")
    return "\n".join(out) + "\n"


def control(name_key, votes_key, name_test, al_test):
    """Decode the test letter's letter-aligned numerals with a key built from the other letter."""
    right = wrong = unknown = 0
    unk_vals = Counter()
    for i, u, chunk, kind, pj in al_test:
        if kind != "let" or u[0] != "N":
            continue
        truth = chunk
        if u[1] not in votes_key:
            unknown += 1
            unk_vals[u[1]] += 1
            continue
        x = A.best(votes_key[u[1]])[0]
        same = x == truth or {x, truth} <= {"u", "v"} or {x, truth} <= {"i", "j"}
        right += same
        wrong += not same
    n = right + wrong + unknown
    return (f"key from {name_key} -> {name_test}\t{n}\t{right}\t{wrong}\t{unknown}\t{right / n:.3f}\t"
            f"{right / (right + wrong):.3f}\t{' '.join(f'{k}:{m}' for k, m in sorted(unk_vals.items()))}")


def image_units():
    """Tokenize P4's page-image transcription of printed p.188 lines 50-61 (worker I, NOTES.md
    s.18), which stands for worker G's whole "block A" (djvu 15529-15551, s.16 item 4) -- on the
    page this is one continuous, properly ordered paragraph, ending at the same "70." block A's own
    djvu stream ends on. The image gives clean text, so it is read with the ordinary (non-strict)
    tokenizer, unlike the OCR's own garbled block."""
    lines = []
    for ln in IMAGE_TSV.read_text(encoding="utf-8").splitlines():
        if not ln or ln.startswith("#") or ln.startswith("printed_page"):
            continue
        cols = ln.split("\t")
        if len(cols) >= 4 and cols[2] == "cipher":
            lines.append(cols[3])
    return A.tokenize(lines)


def decode_p4(lines, rows):
    """Block A's djvu range is replaced by the image (image_units, above). The djvu text between
    blocks A and B (a real, separate, undisordered paragraph -- "This plott is soe infalible ...
    to [the lord protector] and the naturall aversion") is untouched, still read from the OCR.
    Block B's own djvu range is dropped entirely: NOTES.md s.18 found it is not separate page
    content but the OCR's own displaced re-read of parts of block A's lines, so once the image
    gives block A's lines whole and in order, block B's fragments add nothing and would double
    count what the image already covers."""
    cipher_a, cipher_b = A.SPANS["P4"]["cipher"]
    blockA, blockB = A.P4_COLUMN_BLOCKS
    units = A.tokenize(A.clean_lines(lines, cipher_a, blockA[0] - 1))
    units += image_units()
    units += A.tokenize(A.clean_lines(lines, blockA[1] + 1, blockB[0] - 1))
    units += A.tokenize(A.clean_lines(lines, blockB[1] + 1, cipher_b))
    toks, counts = [], Counter()
    for u in units:
        if u[0] == "W":
            toks.append(("W", u[1], "", "clear"))
            continue
        key = u[1] if u[0] == "N" else A.THETA if u[0] == "T" else None
        if key is None:
            toks.append(("?", u[1], f"[{u[1]}]", "U"))
            counts["U"] += 1
            continue
        if key in rows:
            x, n, t, g, _ = rows[key]
            toks.append((u[0], key, x, g))
            counts[g] += 1
        else:
            toks.append((u[0], key, "_", "U"))
            counts["U"] += 1
    return toks, counts


def reading_text(toks, counts):
    out = ["# P4, W.S. (William Stamford) from Calais, 13 March [1654/5 N.S.], Birch 1742 vol. 3 pp. 187-189,",
           "# djvu lines 15469-15645. Generated by decode_stamford.py; do not edit by hand.",
           "# Source: djvu OCR (sources/ia-fulltext/thurloe-gz) for djvu 15469-15528, 15552-15562 and 15601-15645;",
           "# the page image (../P4/image_transcription.tsv, printed p.188 lines 50-61) replaces djvu 15529-15551",
           "# (worker G's block A, s.16 item 4); djvu 15563-15600 (block B) is dropped, not separate content (s.18/s.21).",
           "# Clear words as printed (lower case, OCR spelling); cipher runs in {braces}: letters graded C/H",
           "# in lower case, M in (x?), U as _ (value not in key) or [raw OCR] (unreadable token), code words <word>; sign @ = <thelordprotector>.",
           "# Per-token counts over numerals and signs: " + ", ".join(f"{g} {counts[g]}" for g in "HCSMU"),
           ""]
    line, run = [], []

    def flush_run():
        if run:
            line.append("{" + "".join(run) + "}")
            run.clear()
    for kind, val, x, g in toks:
        if kind == "W":
            flush_run()
            line.append(val)
            continue
        if g == "U":
            run.append(x if kind == "?" else "_")
        elif len(x) > 1 and x != "u/v":
            run.append(f"<{x}>" if g != "M" else f"<{x}?>")
        else:
            ch = "u" if x == "u/v" else x
            run.append(ch if g in "HCS" else f"({ch}?)")
    flush_run()
    txt, cur = [], ""
    for w in line:
        if len(cur) + len(w) > 100:
            txt.append(cur.rstrip())
            cur = ""
        cur += w + " "
    txt.append(cur.rstrip())
    out.extend(txt)
    out.append("")
    out.append("# token list: kind\tvalue\treading\tgrade")
    for kind, val, x, g in toks:
        if kind != "W":
            out.append(f"{kind}\t{val}\t{x}\t{g}")
    return "\n".join(out) + "\n"


def generate():
    lines = A.djvu_lines()
    pairs = {}
    for name in ("P5_P6", "P7"):
        sp = A.SPANS[name]
        pairs[name] = (A.tokenize(A.clean_lines(lines, *sp["cipher"])),
                       A.plain_words(A.clean_lines(lines, *sp["plain"])))
    als, votes = A.iterate([pairs["P5_P6"], pairs["P7"]], iters=ITERS)
    rows = build_key(votes, codes_of(als))
    (al56,), v56 = A.iterate([pairs["P5_P6"]], iters=ITERS)
    (al7,), v7 = A.iterate([pairs["P7"]], iters=ITERS)
    ctl = ["direction\tletter_tokens\tright\twrong\tvalue_not_in_key\tshare_right_of_all\tshare_right_of_keyed\tunkeyed_values",
           control("P5_P6", v56, "P7", al7), control("P7", v7, "P5_P6", al56)]
    toks, counts = decode_p4(lines, rows)
    return {"key_stamford.tsv": key_tsv(rows),
            "control_stamford.tsv": "\n".join(ctl) + "\n",
            "reading_P4.txt": reading_text(toks, counts)}


def main():
    files = generate()
    if "--check" in sys.argv:
        stale = [f for f, t in files.items() if not (HERE / f).exists() or (HERE / f).read_text() != t]
        if stale:
            print("stale:", " ".join(stale))
            sys.exit(1)
        print("ok: key_stamford.tsv, control_stamford.tsv, reading_P4.txt match")
        return
    for f, t in files.items():
        (HERE / f).write_text(t)
    print(files["control_stamford.tsv"])


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Reading of Thurloe letter P3, John Butler (informant in Holland) to secretary
Thurloe, printed p.575-576 (vol. 2). Date per AUDIT.md (LANE T verifier V1,
24 Sept 2026): Birch places the letter c. Sept 1654 by its position in vol. 2;
Tomokiyo's thurloe.htm page gives 1656; unresolved, not settled here.

LANE T worker H (24 Sept 2026): this is Tomokiyo's own "John Butler (1656)"
cipher (sources/cryptiana/web/thurloe.htm), who states, for THIS letter: "used
a cipher, which seems to have randomly assigned numbers 1-60 and generally
alphabetically assigned numbers 400-424 to represent single letters ... It had
some codes for names such as 62(Spain) and 156(Charles). Other numbers such as
913, 350, etc. may be nulls. (E=3/5/405)." Those six values are kept at grade
H (TOMO below); everything else comes from the print's own interlinear
decipherment, aligned by tools/interlinear_align.py exactly as for P8/
Fauconberg/Montagu (NOTES.md sections 8, 9, 13).

The letter's body (djvu 47926-47997, P3_pairs.tsv) sets the decipherment as a
short caption line of otherwise-unexplained clear English words immediately
before each cipher line (NOTES.md section 13), the same technique as P8, so
tools/interlinear_align.py's "pairs"/"align" commands apply directly:
    python3 tools/interlinear_align.py pairs sources/ia-fulltext/collectionofstat02thur_djvu.txt \
        47926 47997 P3_pairs.tsv
(stopped at 47997, i.e. before "John Butler." at 47998: past that point the
signature would otherwise be read by the tool's own heuristic as a caption for
the postscript's first cipher-heavy line at 48000, which it is not -- see
below.) Two djvu lines carry numerals that are not cipher groups at all and
are excluded from every count: line 47932 ("arrived Rotterdam p. 208.", a
page reference caught by the token scan, tokens.tsv order 15) and line 47966
("576 STATE PAPERS OF", a running head, order 144).

The postscript (djvu 48000-48004, after "John Butler.") has no adjacent
caption line of its own -- confirmed here as in NOTES.md section 13: the line
before 48000 is the signature, not a decipherment; 48002/48003 run on with no
caption between them; 48004 is prose with a handful of cipher groups inline.
Per this brief, the postscript is not aligned; each of its groups is decoded
from the KEY this pass builds from the body (H/C/M by the same rule as any
other unaligned occurrence of a value already established in the body; U for
a value never resolved there).

ciphers/thurloe-printed/P3/tokens.tsv (LANE T worker D, committed, read-only
here) supplies the full run of cipher-shaped tokens across the whole letter,
body and postscript together, in djvu order; this script uses it as the token
universe for reading_P3.txt and reads P3_pairs.tsv only for the body's own
interlinear alignment.

Reproducible per CLAUDE.md rule 7: python3 decode_butler.py regenerates
key_butler.tsv and reading_P3.txt from P3_pairs.tsv + P3/tokens.tsv;
--check recomputes in memory and exits non-zero if either is stale.
"""
import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import interlinear_align as ia  # noqa: E402

PAIRS = HERE / "P3_pairs.tsv"
TOKENS = HERE / "P3" / "tokens.tsv"
OUT_KEY = HERE / "key_butler.tsv"
OUT_READING = HERE / "reading_P3.txt"

# Tomokiyo thurloe.htm, "John Butler (1656)" section, values stated for this exact
# letter (not reconstructed from another Butler letter -- there is no other one).
TOMO = {
    3: ("e", "Tomokiyo thurloe.htm E=3/5/405"),
    5: ("e", "Tomokiyo thurloe.htm E=3/5/405"),
    405: ("e", "Tomokiyo thurloe.htm E=3/5/405"),
    62: ("Spain", "Tomokiyo thurloe.htm: code for a name, 62(Spain)"),
    156: ("Charles", "Tomokiyo thurloe.htm: code for a name, 156(Charles)"),
    913: ("[null]", "Tomokiyo thurloe.htm: 'other numbers such as 913, 350, etc. may be nulls'"),
    350: ("[null]", "Tomokiyo thurloe.htm: 'other numbers such as 913, 350, etc. may be nulls'"),
}

# P3/tokens.tsv 'order' values that are numerals but not cipher groups (a page
# reference and a running head caught by the token scan; see module docstring).
NOT_CIPHER_ORDERS = {15, 144}


def tsv(header, rows):
    return "\n".join("\t".join(str(x) for x in r) for r in [header] + rows) + "\n"


def load_tokens():
    with open(TOKENS, encoding="utf-8") as f:
        return list(csv.DictReader(f, delimiter="\t"))


def build():
    with open(PAIRS, encoding="utf-8") as f:
        pairs = list(csv.DictReader(f, delimiter="\t"))
    prepared, results, counts, shown = ia.run_align(pairs)
    rows = ia.token_rows(prepared, results, counts, shown)

    # every one of the tool's own per-token rows (all kinds), per cipher line,
    # in raw.split() order -- needed whole (not just num/doubtful) because a
    # handful of tokens.tsv's true cipher groups sit next to a bare "I" that
    # the tool's own OCR-confusion table reads as num=1 (I -> l -> 1; this
    # letter, unlike Fauconberg/Blake, mixes clear pronouns into cipher
    # lines). Matched below by exact raw-token string, in order, so such a
    # spurious num is skipped rather than mis-consuming a real cipher token.
    by_line = {}
    for r in rows:
        by_line.setdefault(r[0], []).append(r)

    tokens = load_tokens()
    by_line_tok = {}
    for t in tokens:
        by_line_tok.setdefault(t["djvu_line"], []).append(t)

    occ = {}
    for line, trow in by_line_tok.items():
        if line not in by_line:
            continue
        ia_rows = iter(by_line[line])
        r = next(ia_rows, None)
        for t in trow:
            while r is not None and r[2] != t["raw"]:
                r = next(ia_rows, None)
            if r is None:
                break
            occ[int(t["order"])] = r
            r = next(ia_rows, None)

    def key_meaning(value):
        """H (Tomokiyo), else C/M from the body's own vote, else None."""
        if value in TOMO:
            meaning, src = TOMO[value]
            return "H", meaning, src
        cnt = counts.get(value)
        if not cnt:
            return "U", "", "not aligned in any printed interlinear pair (body or postscript)"
        top, topn = ia.top_of(cnt)
        meaning = ia.display(shown, value, top)
        if topn >= 2:
            return "C", meaning, "printed interlinear, %d agreeing places" % topn
        return "M", meaning, "printed interlinear, one place only"

    key_rows = []
    all_values = sorted({
        int(t["cleaned"]) for t in tokens
        if int(t["order"]) not in NOT_CIPHER_ORDERS and t["cleaned"].isdigit()
    })
    for v in all_values:
        grade, meaning, src = key_meaning(v)
        cnt = counts.get(v, Counter())
        n = sum(cnt.values())
        top, topn = ia.top_of(cnt) if cnt else ("", 0)
        rest = sorted(cnt.items(), key=lambda kv: (-kv[1], kv[0]))[1:] if cnt else []
        others = ",".join("%s:%d" % (ia.display(shown, v, m), c) for m, c in rest)
        key_rows.append([v, meaning, grade, n, topn, others, src])

    grades = Counter()
    out = []
    for t in tokens:
        order = int(t["order"])
        line = t["djvu_line"]
        rawtok = t["raw"]
        if order in NOT_CIPHER_ORDERS:
            g, reading, note = "-", "", "page/running-head numeral, not a cipher group"
            grades[g] += 1
            out.append("L%s\t%s\t%s\t%s\t%s" % (line, rawtok, g, reading, note))
            continue
        value = int(t["cleaned"]) if t["cleaned"].isdigit() else None
        r = occ.get(order)
        if r is not None:
            _, _, _, kind, val, repair, chunk, status = r
            note = status
            if kind == "doubtful":
                if repair:
                    rv = int(repair)
                    g, reading, note = "I", ia.display(shown, rv, ia.top_of(counts[rv])[0]), "repaired to %s" % repair
                else:
                    g, reading = "U", chunk
            elif value is not None and value in TOMO:
                meaning, src = TOMO[value]
                g, reading = "H", meaning
                if chunk and ia.fold(chunk) != ia.fold(meaning.lower()):
                    note = "print aligned %r here; %s" % (chunk, src)
                else:
                    note = src
            elif status == "agrees":
                g, reading = "C", ia.display(shown, value, ia.fold(chunk))
            elif status == "null-or-unaligned":
                g, reading = "U", ""
            else:
                g, reading = "M", chunk
        else:
            # not part of any aligned pair (postscript, or a body line whose
            # embedded cipher fell under the pairs scanner's line threshold):
            # decode from the key built above, per this brief.
            g, reading, note = key_meaning(value)
        grades[g] += 1
        out.append("L%s\t%s\t%s\t%s\t%s" % (line, rawtok, g, reading, note))

    total = sum(grades.values())
    ncipher = total - grades["-"]
    header = [
        "# Reading of Thurloe letter P3 (John Butler, informant in Holland, to secretary",
        "# Thurloe, c. 22 Sept 1656, printed p.575-577, vol. 2 -- Tomokiyo's own 'John Butler",
        "# (1656)' cipher) from the decipherment printed above each cipher line in the body",
        "# (djvu 47926-47997), aligned by tools/interlinear_align.py against P3_pairs.tsv, plus",
        "# the postscript (djvu 48000-48004), which has no adjacent decipherment of its own and",
        "# is decoded here from the body's key alone. Tomokiyo's six stated values (E=3/5/405;",
        "# 62=Spain, 156=Charles; nulls 913/350) kept at H throughout. Regenerate: python3 decode_butler.py",
        "# Grades over %d tokens: %d not cipher groups (-); of %d cipher groups H=%d C=%d I=%d M=%d U=%d"
        % (total, grades["-"], ncipher, grades["H"], grades["C"], grades["I"], grades["M"], grades["U"]),
        "# No matched control run (no S grades; every meaning comes from the print or Tomokiyo).",
        "#",
        "# Columns: djvu-line  raw-token  grade  reading  alignment-status",
        "#" + "=" * 74,
    ]
    reading_text = "\n".join(header + out) + "\n"
    key_text = tsv(["value", "meaning", "grade", "n_in_letter", "n_agree", "other_alignments", "source"], key_rows)
    return key_text, reading_text, grades


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()

    key_text, reading_text, grades = build()
    stale = False
    for path, text in ((OUT_KEY, key_text), (OUT_READING, reading_text)):
        if a.check:
            if not path.exists() or path.read_text(encoding="utf-8") != text:
                print("STALE: %s" % path.name, file=sys.stderr)
                stale = True
        else:
            path.write_text(text, encoding="utf-8")
    total = sum(grades.values())
    print("P3: tokens=%d H=%d C=%d I=%d M=%d U=%d not-cipher=%d"
          % (total, grades["H"], grades["C"], grades["I"], grades["M"], grades["U"], grades["-"]))
    if a.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()

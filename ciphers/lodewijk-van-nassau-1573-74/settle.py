#!/usr/bin/env python3
"""Settle R13's two-pass disagreements for the Lodewijk van Nassau target letters
(4610, 4611, 4612, 4616) using key.tsv and a French character n-gram model built
from the sibling plaintexts plus other French readings already in the repo.

For each row in recon/<nr>/disagreements.tsv, both variants are decoded with
key.tsv and scored in their local context (the neighbouring already-agreed
tokens on the same line, decoded the same way). A variant is taken only when
its score beats the other by MARGIN nats/char; otherwise the row stays M
(unsettled, R18's majority/A reading kept, per CLAUDE.md rule 4). Gap rows
("-" vs a token, i.e. the two passes disagree on segmentation, not on the same
sign) are never settled by this script -- they need the image -- and are
logged as such.

Writes, per letter: ciphertext_<nr>.tsv (decode_key.py input, same six-column
layout as recon/<nr>/ciphertext_draft.tsv) and settle_log.tsv (one row per
disagreement: decision, both scores, margin met). --check regenerates both and
exits non-zero if either differs from what is committed (rule 7).

    python3 settle.py            write ciphertext_<nr>.tsv + settle_log.tsv for all four letters
    python3 settle.py --check    exit 1 if any committed output is stale
    python3 settle.py --letters 4610,4611   only these letters
"""
import argparse
import csv
import math
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
REPO = HERE.parent.parent

LETTERS = ["4610", "4611", "4612", "4616"]
ORDER = 4  # order-4 model: 3 chars of context predict the 4th
MARGIN = 0.35  # nats/char; set by eye on the first run (see NOTES.md "R20")
CONTEXT_TOKENS = 2  # tokens either side of the disagreement, for scoring context

CORPUS_FILES = [
    HERE / "plaintext_4613.txt",
    HERE / "plaintext_4615.txt",
    REPO / "ciphers" / "fr2980-gramont" / "reading.txt",
    REPO / "ciphers" / "fr2980-gramont" / "reading_f30.txt",
    REPO / "ciphers" / "fr2980-gramont" / "reading_f30_extended.txt",
]

ALPHA_RE = re.compile(r"[^a-zàâäéèêëîïôöùûüçñ'\s]")
STRUCK_RE = re.compile(r"\[struck:[^\]]*\]")
DOUBT_RE = re.compile(r"\[\?([a-zàâäéèêëîïôöùûüçñ']*)\]")
BRACKET_RE = re.compile(r"\[[^\]]*\]")
HEADER_RE = re.compile(r"^#.*$", re.MULTILINE)
FOLIO_LINE_RE = re.compile(r"^\S+\s+L?\d+\s*\|\s*", re.MULTILINE)


def clean_text(raw: str) -> str:
    s = raw.lower()
    s = HEADER_RE.sub(" ", s)
    s = FOLIO_LINE_RE.sub(" ", s)
    s = STRUCK_RE.sub(" ", s)
    s = DOUBT_RE.sub(r"\1", s)
    s = BRACKET_RE.sub(" ", s)
    s = ALPHA_RE.sub(" ", s)
    s = re.sub(r"\s+", " ", s).strip()
    return s


def load_plaintext_body(path: Path) -> str:
    """Drop this repo's own English transcription-note header paragraph (ends
    at the first blank line) before folding into the French corpus."""
    lines = path.read_text(encoding="utf-8").splitlines()
    try:
        blank = lines.index("")
        lines = lines[blank + 1:]
    except ValueError:
        pass
    return "\n".join(lines)


def build_lm(paths, order=ORDER):
    parts = []
    for p in paths:
        if not p.exists():
            continue
        raw = p.read_text(encoding="utf-8")
        if p.name.startswith("plaintext_"):
            raw = load_plaintext_body(p)
        parts.append(clean_text(raw))
    text = " ".join(parts)
    padded = ("^" * (order - 1)) + text
    counts = defaultdict(Counter)
    for i in range(len(padded) - order + 1):
        ctx = padded[i:i + order - 1]
        ch = padded[i + order - 1]
        counts[ctx][ch] += 1
    alphabet = set(text)
    return counts, alphabet, len(text)


def score_text(text, counts, alphabet, order=ORDER):
    text = clean_text(text)
    if not text:
        return None, 0
    padded = ("^" * (order - 1)) + text
    V = len(alphabet) + 1
    logp = 0.0
    n = 0
    for i in range(len(padded) - order + 1):
        ctx = padded[i:i + order - 1]
        ch = padded[i + order - 1]
        c = counts.get(ctx)
        total = sum(c.values()) if c else 0
        num = c[ch] if c and ch in c else 0
        p = (num + 1) / (total + V)
        logp += math.log(p)
        n += 1
    return logp / n, n


def load_key(path):
    key = {}
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            code = row.get("code") or row.get("sign") or row.get("token")
            key[code] = row["value"]
    return key


def decode_sign(sign, key):
    """A sign to its plaintext string, for scoring: '=word' -> word; a keyed
    numeral/roman code -> its key value (empty for NULL); unkeyed or a gap
    ('-') -> None (excluded from the scored context, not scored as wrong)."""
    if sign is None or sign == "-":
        return None
    if sign.startswith("="):
        return sign[1:]
    val = key.get(sign)
    if val is None:
        return None
    if val.upper() == "NULL" or val == "?":
        return ""
    return val


def read_draft(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            rows.append(row)
    return rows


def load_overrides(path):
    """Manual corrections from eye-checking a crop image (step 2 of the brief):
    keyed by (letter, line, col), applied after the automated pass so they
    persist across settle.py reruns without being scored by the n-gram model."""
    overrides = {}
    if not path.exists():
        return overrides
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            overrides[(row["nr"], row["line"], row["col"])] = row
    return overrides


def read_disagreements(path):
    rows = []
    with open(path, encoding="utf-8") as f:
        r = csv.DictReader(f, delimiter="\t")
        for row in r:
            rows.append(row)
    return rows


def settle_letter(nr, key, counts, alphabet, overrides):
    recon_dir = HERE / "recon" / nr
    draft = read_draft(recon_dir / "ciphertext_draft.tsv")
    disagreements = read_disagreements(recon_dir / "disagreements.tsv")

    by_line = defaultdict(list)
    index = {}
    for i, row in enumerate(draft):
        by_line[row["line"]].append(row)
        index[(row["line"], row["position"])] = i
    for line in by_line:
        by_line[line].sort(key=lambda r: int(r["position"]))

    log_rows = []
    n_settled_a = n_settled_b = n_gap = n_unsettled = n_override = 0

    for d in disagreements:
        line, col, a, b, flagged = d["line"], d["col"], d["A"], d["B"], d["flagged"]
        key_pos = (line, col)
        if key_pos not in index:
            log_rows.append([line, col, a, b, "", "", "SKIP", "no matching draft row"])
            continue
        row_i = index[key_pos]
        line_rows = by_line[line]
        pos_in_line = next(k for k, r in enumerate(line_rows) if r["position"] == col)

        ov = overrides.get((nr, line, col))
        if ov:
            n_override += 1
            draft[row_i]["sign"] = ov["sign"]
            draft[row_i]["confidence"] = ov["confidence"]
            draft[row_i]["alt"] = a if ov["sign"] != a else b
            draft[row_i]["why"] = f"override: {ov['why']}"
            log_rows.append([line, col, a, b, "", "", "OVERRIDE", ov["why"]])
            continue

        if a == "-" or b == "-":
            n_gap += 1
            log_rows.append([line, col, a, b, "", "", "M", "gap: passes disagree on segmentation, needs image"])
            continue

        dec_a, dec_b = decode_sign(a, key), decode_sign(b, key)
        if dec_a and dec_b and dec_a != dec_b and dec_a.lower() == dec_b.lower():
            # Case-only disagreement (e.g. sentence-initial =Du vs =du): no
            # content difference, so the n-gram model cannot and need not
            # decide it. Prefer the capitalised spelling at the line's first
            # token (secretary hand capitalises sentence starts), else the
            # lower-case one.
            a_cap, b_cap = dec_a[:1].isupper(), dec_b[:1].isupper()
            if pos_in_line == 0:
                chosen = a if a_cap or not b_cap else b
            else:
                chosen = a if not a_cap or b_cap else b
            decision = "A" if chosen == a else "B"
            if decision == "A":
                n_settled_a += 1
            else:
                n_settled_b += 1
            log_rows.append([line, col, a, b, "", "", decision, "case-only, no content difference"])
            draft[row_i]["sign"] = chosen
            draft[row_i]["confidence"] = "H"
            draft[row_i]["alt"] = b if chosen == a else a
            draft[row_i]["why"] = "settled-case-only"
            continue

        def context_text(candidate):
            parts = []
            lo = max(0, pos_in_line - CONTEXT_TOKENS)
            hi = min(len(line_rows), pos_in_line + CONTEXT_TOKENS + 1)
            for k in range(lo, hi):
                if k == pos_in_line:
                    dec = decode_sign(candidate, key)
                else:
                    dec = decode_sign(line_rows[k]["sign"], key)
                if dec:
                    parts.append(dec)
            return " ".join(parts)

        text_a = context_text(a)
        text_b = context_text(b)
        score_a, n_a = score_text(text_a, counts, alphabet)
        score_b, n_b = score_text(text_b, counts, alphabet)

        if score_a is None and score_b is None:
            n_unsettled += 1
            log_rows.append([line, col, a, b, "", "", "M", "both unkeyed/empty in context"])
            continue
        if score_a is None:
            score_a = float("-inf")
        if score_b is None:
            score_b = float("-inf")

        diff = score_a - score_b
        if diff > MARGIN:
            decision, chosen = "A", a
            n_settled_a += 1
        elif diff < -MARGIN:
            decision, chosen = "B", b
            n_settled_b += 1
        else:
            decision, chosen = "M", None
            n_unsettled += 1

        log_rows.append([line, col, a, b, f"{score_a:.3f}", f"{score_b:.3f}", decision,
                          f"margin {MARGIN}" if decision == "M" else "settled"])

        if chosen is not None:
            draft[row_i]["sign"] = chosen
            draft[row_i]["confidence"] = "S"
            draft[row_i]["alt"] = b if chosen == a else a
            draft[row_i]["why"] = f"settled-{decision.lower()} nc={CONTEXT_TOKENS} margin={MARGIN}"

    return draft, log_rows, {
        "settled_a": n_settled_a, "settled_b": n_settled_b,
        "gap": n_gap, "unsettled": n_unsettled, "override": n_override,
        "total": len(disagreements),
    }


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--check", action="store_true")
    ap.add_argument("--letters", default=",".join(LETTERS))
    args = ap.parse_args()
    letters = args.letters.split(",")

    key = load_key(HERE / "key.tsv")
    counts, alphabet, corpus_chars = build_lm(CORPUS_FILES)
    overrides = load_overrides(HERE / "overrides.tsv")

    stale = False
    summary = {}
    for nr in letters:
        draft, log_rows, stats = settle_letter(nr, key, counts, alphabet, overrides)
        summary[nr] = stats
        cipher_path = HERE / f"ciphertext_{nr}.tsv"
        log_path = HERE / f"settle_log_{nr}.tsv"

        import io
        cipher_io = io.StringIO()
        w = csv.writer(cipher_io, delimiter="\t", lineterminator="\n")
        w.writerow(["line", "position", "sign", "confidence", "alt", "why"])
        for row in draft:
            w.writerow([row["line"], row["position"], row["sign"], row["confidence"],
                        row.get("alt", ""), row.get("why", "")])
        new_cipher_text = cipher_io.getvalue()

        log_io = io.StringIO()
        w2 = csv.writer(log_io, delimiter="\t", lineterminator="\n")
        w2.writerow(["line", "col", "A", "B", "score_A", "score_B", "decision", "note"])
        for row in log_rows:
            w2.writerow(row)
        new_log_text = log_io.getvalue()

        if args.check:
            old_cipher = cipher_path.read_text(encoding="utf-8") if cipher_path.exists() else None
            old_log = log_path.read_text(encoding="utf-8") if log_path.exists() else None
            if old_cipher != new_cipher_text:
                print(f"STALE: {cipher_path}", file=sys.stderr)
                stale = True
            if old_log != new_log_text:
                print(f"STALE: {log_path}", file=sys.stderr)
                stale = True
        else:
            cipher_path.write_text(new_cipher_text, encoding="utf-8")
            log_path.write_text(new_log_text, encoding="utf-8")

    for nr, s in summary.items():
        print(f"{nr}: {s['total']} disagreements -> A {s['settled_a']}, B {s['settled_b']}, "
              f"override {s['override']}, gap {s['gap']}, unsettled(M) {s['unsettled']}")
    print(f"corpus: {corpus_chars} chars, order {ORDER}, margin {MARGIN} nats/char")

    if args.check and stale:
        sys.exit(1)


if __name__ == "__main__":
    main()

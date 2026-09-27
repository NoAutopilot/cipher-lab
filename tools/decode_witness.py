#!/usr/bin/env python3
"""Score a symbol/nomenclator key against a witness leaf that carries a period clerk's plaintext
decipherment (CLAUDE.md rule 3, LESSONS.md "Symbol ciphers: known plaintext first, then a reader").

Three inputs, all TSV:
  key    header 'sign  value  kind  grade  source  note' (kind: letter | word | name), one row per drawn
         homophone; '#'-prefixed lines and blank lines are skipped and do not count towards the 1-based
         data-row numbering that --signs' key_row column refers to.
  signs  header 'line  pos  key_row  shape_note  confidence': one row per cipher sign transcribed from the
         witness image. key_row is either an integer (1-based row number in the key file), '?' (sign not
         placed in the key), or 'nNN' for a plain two-digit number kept as drawn (looked up against the
         key's own 'sign' column, e.g. 'n85' against a row whose sign text contains "85"; a number with no
         matching row decodes as unknown, same as '?').
  plain  header 'line  text  confidence': the clerk's plaintext decipherment, one row per line (its own line
         numbers if the witness has no interlinear correspondence -- decode_witness only needs the running
         text, not a line-for-line correspondence, since alignment is global over the whole passage).

    python3 tools/decode_witness.py --key K.tsv --signs S.tsv --plain P.tsv [--shuffles 20] [--seed 1]
            [--sample-lines 2,5,9] [--key-rows-out witness/key_rows_f178.tsv]

Decoding: key_row -> value (a letter for kind=letter, the whole word's letters for kind=word/name; '?' and
an unmatched numeral -> '_', a character that cannot match anything). The decoded stream and the clerk
stream are each normalized (lower-case, letters only, j->i, v->u -- the period Italian i/j and u/v pairs)
then aligned once, globally, over the whole passage (not per line) by a match/mismatch/no-gap dynamic
program (equivalent to longest common subsequence): every clerk letter is either matched by one decoded
letter, in the same order, or left unmatched. agreement = matches / len(clerk letters).

Control (rule 3): the same score under --shuffles keys whose values are permuted among the letter-kind
rows only (the multiset of letter values, hence each letter's homophone count, is preserved; word/name
rows are never shuffled). Reports the shuffled mean, sd, z of the real score, and the real key's rank
among itself plus the shuffled keys (1 = best of all).

--sample-lines restricts both streams to the named line ids first (the honest error measure on a blind
transcription sample with no clerk gloss visible to the reader) and runs its own --shuffles-key control.

--key-rows-out writes one row per key-file row: how many times its value was confirmed (the aligned clerk
letter equals it) vs contradicted (aligned to a different clerk letter), from the same alignment.

Exit 2 on a malformed key/signs/plain file (missing header column, a key_row that is neither an integer,
'?', nor 'nNN', or a plain-file line id that duplicates one already read). Exit 0 otherwise, report on stdout.
"""
import argparse
import random
import sys


def _read_tsv(path, required_cols):
    rows = []
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    header = None
    for ln in lines:
        if not ln.strip() or ln.startswith("#"):
            continue
        cols = ln.split("\t")
        if header is None:
            header = cols
            missing = [c for c in required_cols if c not in header]
            if missing:
                raise ValueError(f"{path}: missing column(s) {missing} in header {header}")
            continue
        row = dict(zip(header, cols))
        rows.append(row)
    if header is None:
        raise ValueError(f"{path}: no header row found")
    return rows


def load_key(path):
    """Returns (rows, letter_row_idxs) -- rows is a 1-based dict {row_num: {sign,value,kind,...}}."""
    raw = _read_tsv(path, ["sign", "value", "kind"])
    rows = {}
    for i, r in enumerate(raw, start=1):
        rows[i] = r
    letter_idxs = [i for i, r in rows.items() if r["kind"] == "letter"]
    return rows, letter_idxs


def _numeral_lookup(rows, digits):
    for i, r in rows.items():
        if digits in r["sign"]:
            return r["value"]
    return None


def key_row_value(rows, key_row):
    key_row = key_row.strip()
    if key_row in ("", "?"):
        return "_"
    if key_row.startswith("n") and key_row[1:].isdigit():
        v = _numeral_lookup(rows, key_row[1:])
        return v if v is not None else "_"
    if key_row.lstrip("-").isdigit():
        idx = int(key_row)
        if idx not in rows:
            raise ValueError(f"signs file: key_row {idx} is out of range for the key file")
        return rows[idx]["value"]
    raise ValueError(f"signs file: malformed key_row {key_row!r} (want an integer, '?', or 'nNN')")


def load_signs(path, key_rows):
    raw = _read_tsv(path, ["line", "pos", "key_row"])
    out = []
    for r in raw:
        value = key_row_value(key_rows, r["key_row"])
        out.append({"line": r["line"], "pos": r["pos"], "key_row": r["key_row"], "value": value})
    return out


def load_plain(path):
    raw = _read_tsv(path, ["line", "text"])
    seen = set()
    out = []
    for r in raw:
        if r["line"] in seen:
            raise ValueError(f"{path}: duplicate line id {r['line']!r}")
        seen.add(r["line"])
        out.append(r)
    return out


NORM_TABLE = str.maketrans({"j": "i", "v": "u"})


def normalize(text):
    return "".join(ch for ch in text.lower().translate(NORM_TABLE) if ch.isalpha())


def decoded_stream(signs, lines=None):
    """Returns a list of (char, key_row) in line/pos order, restricted to `lines` if given."""
    items = signs if lines is None else [s for s in signs if s["line"] in lines]

    def sort_key(s):
        try:
            pos = int(s["pos"])
        except ValueError:
            pos = s["pos"]
        return (s["line"], pos)

    items = sorted(items, key=sort_key)
    out = []
    for s in items:
        for ch in normalize(s["value"]):
            out.append((ch, s["key_row"]))
    return out


def clerk_stream(plain_rows, lines=None):
    items = plain_rows if lines is None else [p for p in plain_rows if p["line"] in lines]
    text = "".join(p["text"] for p in items)
    return list(normalize(text))


def lcs_align(decoded_chars, clerk_chars):
    """decoded_chars: list of chars (or (char, tag) tuples). clerk_chars: list of chars.
    Longest common subsequence by dynamic programming; returns (match_count, pairs) where pairs is a
    list of (decoded_index, clerk_index) for each matched position, in order."""
    a = [c if isinstance(c, str) else c[0] for c in decoded_chars]
    b = clerk_chars
    n, m = len(a), len(b)
    # DP table sized (n+1) x (m+1); fine at the sizes a witness passage reaches (low thousands).
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        ai = a[i - 1]
        row, prow = dp[i], dp[i - 1]
        for j in range(1, m + 1):
            if ai == b[j - 1]:
                row[j] = prow[j - 1] + 1
            else:
                row[j] = row[j - 1] if row[j - 1] >= prow[j] else prow[j]
    pairs = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            pairs.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    return dp[n][m], pairs


def score(signs, plain_rows, key_rows, lines=None):
    dec = decoded_stream(signs, lines)
    clk = clerk_stream(plain_rows, lines)
    if not clk:
        raise ValueError("no clerk letters in scope (empty plain text for the given lines)")
    matches, pairs = lcs_align(dec, clk)
    agreement = matches / len(clk)
    return agreement, matches, len(clk), dec, clk, pairs


def shuffled_key_rows(key_rows, letter_idxs, rng):
    values = [key_rows[i]["value"] for i in letter_idxs]
    shuffled_values = values[:]
    rng.shuffle(shuffled_values)
    new_rows = {i: dict(r) for i, r in key_rows.items()}
    for idx, v in zip(letter_idxs, shuffled_values):
        new_rows[idx] = dict(new_rows[idx])
        new_rows[idx]["value"] = v
    return new_rows


def control(signs_raw, plain_rows, key_rows, letter_idxs, shuffles, seed, lines=None):
    """signs_raw: the raw signs rows (line/pos/key_row) before key lookup, so each shuffled key can be
    applied fresh. Returns (real_agreement, shuffled_scores)."""
    real_signs = [dict(s, value=key_row_value(key_rows, s["key_row"])) for s in signs_raw]
    real_agreement, real_matches, clerk_n, _, _, real_pairs = score(real_signs, plain_rows, key_rows, lines)
    shuffled_scores = []
    rng = random.Random(seed)
    for k in range(shuffles):
        sk_rows = shuffled_key_rows(key_rows, letter_idxs, rng)
        sk_signs = [dict(s, value=key_row_value(sk_rows, s["key_row"])) for s in signs_raw]
        agr, _, _, _, _, _ = score(sk_signs, plain_rows, sk_rows, lines)
        shuffled_scores.append(agr)
    return real_agreement, real_matches, clerk_n, shuffled_scores, real_pairs, real_signs


def summarize(label, real_agreement, real_matches, clerk_n, shuffled_scores):
    n = len(shuffled_scores)
    mean = sum(shuffled_scores) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in shuffled_scores) / n if n else 0.0
    sd = var ** 0.5
    z = (real_agreement - mean) / sd if sd > 0 else float("inf") if real_agreement > mean else 0.0
    rank = 1 + sum(1 for x in shuffled_scores if x > real_agreement)
    lines = [
        f"{label}: real key {real_agreement:.4f} ({real_matches}/{clerk_n} aligned letters); "
        f"{n} shuffled keys mean {mean:.4f} sd {sd:.4f} min {min(shuffled_scores):.4f} max {max(shuffled_scores):.4f}; "
        f"z {z:.2f}; rank {rank} of {n + 1}"
    ]
    return "\n".join(lines), {"agreement": real_agreement, "matches": real_matches, "clerk_n": clerk_n,
                               "shuffled_mean": mean, "shuffled_sd": sd, "z": z, "rank": rank, "n": n}


def key_rows_report(key_rows, real_pairs, dec, clk):
    """One row per key-file row: how often its aligned decoded letters matched (confirmed) or
    mismatched (contradicted) the clerk. Since decoded chars carry a key_row tag, walk the alignment
    pairs (which are always matches under lcs_align) for 'confirmed', and separately count every decoded
    character NOT in the matched set as 'contradicted' for its key_row (it lost to a different clerk
    letter or to no letter at all -- lcs_align only returns matched pairs, so unmatched decoded
    characters are exactly the complement)."""
    matched_dec_idx = {p[0] for p in real_pairs}
    confirmed = {}
    contradicted = {}
    for idx, (ch, tag) in enumerate(dec):
        bucket = confirmed if idx in matched_dec_idx else contradicted
        bucket[tag] = bucket.get(tag, 0) + 1
    rows = []
    for i in sorted(key_rows):
        r = key_rows[i]
        rows.append({
            "row": i, "sign": r["sign"][:40], "value": r["value"], "kind": r["kind"],
            "confirmed": confirmed.get(str(i), 0), "contradicted": contradicted.get(str(i), 0),
        })
    return rows


def write_key_rows_tsv(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("row\tvalue\tkind\tconfirmed\tcontradicted\tsign\n")
        for r in rows:
            f.write(f"{r['row']}\t{r['value']}\t{r['kind']}\t{r['confirmed']}\t{r['contradicted']}\t{r['sign']}\n")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", required=True)
    ap.add_argument("--signs", required=True)
    ap.add_argument("--plain", required=True)
    ap.add_argument("--shuffles", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--sample-lines", default=None, help="comma-separated line ids for the blind-check subset")
    ap.add_argument("--key-rows-out", default=None)
    args = ap.parse_args(argv)

    try:
        key_rows, letter_idxs = load_key(args.key)
        signs_raw = _read_tsv(args.signs, ["line", "pos", "key_row"])
        plain_rows = load_plain(args.plain)
        # validate every key_row up front so a malformed row is caught before any scoring
        for s in signs_raw:
            key_row_value(key_rows, s["key_row"])
    except (ValueError, OSError, KeyError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    real_agreement, real_matches, clerk_n, shuffled, real_pairs, real_signs = control(
        signs_raw, plain_rows, key_rows, letter_idxs, args.shuffles, args.seed)
    text, stats = summarize("full passage", real_agreement, real_matches, clerk_n, shuffled)
    print(text)

    if args.key_rows_out:
        dec = decoded_stream(real_signs)
        clk = clerk_stream(plain_rows)
        rows = key_rows_report(key_rows, real_pairs, dec, clk)
        write_key_rows_tsv(args.key_rows_out, rows)
        print(f"wrote {args.key_rows_out} ({len(rows)} key rows)")

    if args.sample_lines:
        lines = set(args.sample_lines.split(","))
        s_agr, s_matches, s_n, s_shuffled, _, _ = control(
            signs_raw, plain_rows, key_rows, letter_idxs, args.shuffles, args.seed + 1000, lines=lines)
        text2, _ = summarize("blind-check sample", s_agr, s_matches, s_n, s_shuffled)
        print(text2)

    return 0


if __name__ == "__main__":
    sys.exit(main())

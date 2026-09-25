#!/usr/bin/env python3
"""Deterministically apply the fixed digit key to ciphertext.tsv and regenerate the graded reading
(CLAUDE.md rule 7). This target's cipher is word-internal (most letters already clear, only some digit
positions keyed), which does not fit tools/decode_key.py's per-sign key-lookup model (its ciphertext format
needs a literal 'line' header and a 'sign'/'token'/'code' column holding one whole cipher unit per row; ours
is 'block/line/token_index/raw_token/confidence' with raw_token a mixed letter+digit word). This script is
the target's own decode step (CLAUDE.md rule 7's "the target's decode script"), playing the same role
tools/decode_key.py plays for a plain substitution target, kept in this folder rather than genericised into
tools/ since the design (crib letters fixed, digits keyed) is VX-CT03's, not a second target's yet.

Usage:
  python3 apply_key.py DIGIT_KEY.json CIPHERTEXT.tsv [--overrides overrides.tsv] --out reading.txt
      [--tokens reading_tokens.tsv] [--check] [--block B]

DIGIT_KEY.json: {"digit": "letter", ...} (e.g. {"2":"u","3":"i","4":"a","7":"o","8":"e"}); "v" and "j" in the
raw token fold to u/i (period orthography) same as tools/homophonic_anneal.py's ALPHA fold.
overrides.tsv (optional): token_index[TAB]block[TAB]corrected_raw_token[TAB]grade[TAB]note -- one row per
token this pass corrected (a glyph re-read) or re-graded (a dictionary/context confirmation); corrected_raw_token
may be blank to keep the committed raw_token and only change grade/note. grade is one of S/M/I (rule 4); tokens
not listed keep their ciphertext.tsv confidence mapped to a default grade (high/medium->S, low->I).

--check exits 1 if a fresh run (from ciphertext.tsv + digit key + overrides) differs from the committed
reading.txt/reading_tokens.tsv (rule 7: "exits non-zero if the committed reading is stale").
"""
import argparse, csv, json, sys


def fold(ch):
    return {"j": "i", "v": "u"}.get(ch, ch)


def decode_token(tok, key):
    return "".join(key.get(ch, fold(ch)) if ch.isdigit() else ch for ch in tok)


def default_grade(conf):
    return {"high": "S", "medium": "S", "low": "I"}.get(conf, "M")


def load_overrides(path):
    if not path:
        return {}
    out = {}
    with open(path, encoding="utf-8") as f:
        rows = [l.rstrip("\n").split("\t") for l in f if l.strip() and not l.startswith("#")]
    header = rows[0]
    for r in rows[1:]:
        d = dict(zip(header, r))
        out[(d.get("block", "A"), int(d["token_index"]))] = d
    return out


def run(args):
    key = json.load(open(args.digit_key, encoding="utf-8"))
    overrides = load_overrides(args.overrides)
    rows = list(csv.DictReader(open(args.ciphertext, encoding="utf-8"), delimiter="\t"))
    out_tokens = []
    for r in rows:
        block, ti, raw, conf = r["block"], int(r["token_index"]), r["raw_token"], r["confidence"]
        if args.block and block != args.block:
            continue
        ov = overrides.get((block, ti))
        note = ""
        if ov:
            raw_used = ov.get("corrected_raw_token") or raw
            grade = ov.get("grade") or default_grade(conf)
            note = ov.get("note", "")
        else:
            raw_used = raw
            grade = default_grade(conf)
        value = decode_token(raw_used, key)
        out_tokens.append({
            "block": block, "token_index": ti, "raw_token": raw, "raw_used": raw_used,
            "value": value, "grade": grade, "orig_confidence": conf, "note": note,
        })

    counts = {}
    for t in out_tokens:
        counts[t["grade"]] = counts.get(t["grade"], 0) + 1
    # reading.txt is pure decoded text, no header: tools/judge_plaintext.py --file reads the whole file
    # verbatim with no comment-stripping, so an English header here would corrupt the language-model score.
    reading = " ".join(t["value"] for t in out_tokens) + "\n"
    meta = (
        f"na-oldenbarnevelt-2442-1605: {len(out_tokens)} cipher tokens decoded with digit key {key} "
        f"(scripts/apply_key.py, VX-RD04, 25 Sept 2026)\n"
        f"grade counts: " + ", ".join(f"{g}={n}" for g, n in sorted(counts.items())) + "\n"
        "S = cryptanalytic, control on file (VX-CT03); M = plausible but not control-confirmed; "
        "I = inferred/unresolved, glyph fix still needed\n"
    )

    if args.check:
        old = open(args.out, encoding="utf-8").read() if _exists(args.out) else None
        if old != reading:
            print("STALE: reading.txt does not match a fresh decode", file=sys.stderr)
            return 1
        print("OK: reading.txt matches a fresh decode")
        return 0

    open(args.out, "w", encoding="utf-8").write(reading)
    if args.meta:
        open(args.meta, "w", encoding="utf-8").write(meta)
    if args.tokens:
        with open(args.tokens, "w", encoding="utf-8", newline="") as f:
            w = csv.writer(f, delimiter="\t")
            w.writerow(["block", "token_index", "raw_token", "raw_used", "value", "grade", "orig_confidence", "note"])
            for t in out_tokens:
                w.writerow([t["block"], t["token_index"], t["raw_token"], t["raw_used"], t["value"],
                            t["grade"], t["orig_confidence"], t["note"]])
    print(reading)
    return 0


def _exists(p):
    import os
    return os.path.exists(p)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("digit_key")
    ap.add_argument("ciphertext")
    ap.add_argument("--overrides")
    ap.add_argument("--out", default="reading.txt")
    ap.add_argument("--tokens")
    ap.add_argument("--meta")
    ap.add_argument("--block")
    ap.add_argument("--check", action="store_true")
    sys.exit(run(ap.parse_args()))


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Mechanical key trial for BnF fr.5160 (Brienne pere et fils -> Servien).

Applies a code->plaintext key (Tomokiyo's published Brienne's Cipher 1 [1647] or
Brienne's Cipher 2 [1651] tables, cryptiana.web.fc2.com/code/louisxiv0.htm) to a
blind transcription pass (line, position, group, confidence TSV) and reports how
much recognisable French comes out, against a shuffled-key control (rule 3: no
negative without a matched control). This is a rough mechanical trial, not a
reconstruction of fr.5160's own key -- no word-boundary repair, no key editing.

Usage:
  python3 decode.py KEY.tsv PASS.tsv [--seed N] [--check]

--check re-runs the decode twice and exits non-zero if the two runs disagree
(the only staleness check that applies here, since no canonical reading.txt is
committed for this target yet -- this is an exploratory trial, not a claimed
reading).
"""
import argparse
import csv
import random
import sys
from pathlib import Path

# Compact, hand-picked list of common 17th-century French words (function words
# plus vocabulary typical of diplomatic correspondence). Not a full dictionary --
# a mechanical, reproducible yardstick, same list used for the real key and the
# shuffled control.
FRENCH_WORDS = set("""
le la les de des du un une et est sont sa son ses ce cet cette ces qui que quoi
quel quels quelle quelles il elle ils elles on nous vous je tu se soi moi toi
lui leur leurs mon ma mes ton ta tes notre nos votre vos dans en par pour sans
sur sous avec mais ou donc car ni pas plus moins bien mal tout tous toute toutes
rien fait faire fais faites dit dire dites peut peuvent pourra pouvoir doit
doivent devra estre etre suis es sommes etes ai as avons avez ont avoir avait
avaient sera seront serait seraient roy royal roi france francois monsieur
madame mademoiselle lettre lettres escrire escrit ecrit ecrire nouvelles
affaires estat etat cour paix guerre traite trait ambassadeur ambassade
armee arme troupes ville ordre ordres commandement service seruice
tres fort grand grande grands grandes bon bonne bons bonnes homme hommes
temps jour jours mois an ans point encore aussi ainsi comme quand
la ne pas plus jamais toujours ici la meme mesme apres avant depuis
peu assez trop tant si bien mal grand petit
""".split())


def load_key(path):
    key = {}
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            code = row["code"].strip()
            val = row["plaintext"].strip()
            key.setdefault(code, val)  # first occurrence wins on duplicate codes
    return key


def load_pass(path):
    rows = []
    with open(path, newline="", encoding="utf-8") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            rows.append(row)
    return rows


def decode_line_groups(rows, key):
    """Returns {line: [(resolved_or_None, raw_group), ...]} for non-clear rows."""
    lines = {}
    for row in rows:
        if row.get("position") == "clear":
            continue
        line = row["line"]
        group = row["group"].strip()
        code = group[1:] if group.startswith("_") else group
        resolved = key.get(code)
        if resolved is None:
            resolved = key.get(group)  # also try with the underscore literally, in case a key uses it
        lines.setdefault(line, []).append((resolved, group))
    return lines


def cover_words(s, wordset, min_len=2):
    """Longest-match greedy word segmentation; returns (words_found, chars_covered)."""
    s = s.lower()
    n = len(s)
    i = 0
    found = []
    maxw = max((len(w) for w in wordset), default=1)
    while i < n:
        matched = None
        for L in range(min(maxw, n - i), min_len - 1, -1):
            cand = s[i:i + L]
            if cand in wordset:
                matched = cand
                break
        if matched:
            found.append(matched)
            i += len(matched)
        else:
            i += 1
    covered = sum(len(w) for w in found)
    return found, covered


def run_trial(key, pass_rows, label):
    lines = decode_line_groups(pass_rows, key)
    total = resolved_n = 0
    per_line_text = {}
    for line, groups in lines.items():
        text = ""
        for resolved, raw in groups:
            total += 1
            if resolved is not None:
                resolved_n += 1
                text += resolved.replace(" ", "")
        per_line_text[line] = text
    full_text = "".join(per_line_text.values())
    words, covered = cover_words(full_text, FRENCH_WORDS)
    print(f"-- {label} --")
    print(f"  groups: {total}  resolved(H): {resolved_n}  unresolved(U): {total - resolved_n}")
    print(f"  decoded chars: {len(full_text)}  french-word chars covered: {covered} "
          f"({100 * covered / max(1, len(full_text)):.1f}%)")
    print(f"  french words found ({len(words)}): {' '.join(words[:40])}{' ...' if len(words) > 40 else ''}")
    return {"total": total, "resolved": resolved_n, "words": words, "covered": covered, "text_len": len(full_text)}


def shuffled_key(key, seed):
    rnd = random.Random(seed)
    codes = list(key.keys())
    vals = list(key.values())
    rnd.shuffle(vals)
    return dict(zip(codes, vals))


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("key")
    ap.add_argument("passfile")
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--check", action="store_true")
    args = ap.parse_args()

    key = load_key(args.key)
    pass_rows = load_pass(args.passfile)

    if args.check:
        a = run_trial(key, pass_rows, "check run 1 (suppressed)")
        b = run_trial(key, pass_rows, "check run 2 (suppressed)")
        if a != {k: v for k, v in b.items()}:
            pass  # dict compare below handles lists fine since deterministic
        if a["words"] != b["words"] or a["resolved"] != b["resolved"]:
            print("STALE: two runs of the same key+pass disagree", file=sys.stderr)
            sys.exit(1)
        print("check OK: decode is deterministic", file=sys.stderr)

    real = run_trial(key, pass_rows, f"real key {Path(args.key).name}")
    ctrl = run_trial(shuffled_key(key, args.seed), pass_rows, f"shuffled control (seed {args.seed})")

    print()
    print(f"SUMMARY  real: {len(real['words'])} words / {real['covered']} chars covered  "
          f"vs  control: {len(ctrl['words'])} words / {ctrl['covered']} chars covered")


if __name__ == "__main__":
    main()

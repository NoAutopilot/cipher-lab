#!/usr/bin/env python3
"""VX-CS06 cheap test: does invnr 317's keyword-driven reciprocal alphabet
read invnr 209's cipher body?

209's cipher body (leaf 2, both this worker's transcription passes plus one
blind subagent pass -- see ../ciphertext_209_leaf2.tsv and NOTES.md) is a
two-row stream of decimal digits (0-9): no Latin letters appear anywhere in
it. 317's system (key_317.py) is a letter-for-letter reciprocal alphabet: it
takes a plaintext Latin letter and a key Latin letter and returns a Latin
letter; nothing in either item defines an operation on digits. This script
makes that comparison explicit instead of asserting it, and runs a matched
control (CLAUDE.md rule 3) to show the *apparatus* (transcription + table
implementation) does work whenever its input is actually letters.
"""
import csv
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent.parent))
from key_317 import encipher, decipher  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
TARGET_TSV = HERE / "ciphertext_209_leaf2.tsv"
CORPUS = Path(__file__).resolve().parent.parent.parent.parent / "tools/data/nl_repo/breda-statengeneraal-1624-25__plaintext_print.txt"


def load_target_tokens():
    tokens = []
    with open(TARGET_TSV, newline="") as f:
        for row in csv.DictReader(f, delimiter="\t"):
            tokens.append(row["top_digit"])
            if row["bottom_digit"]:
                tokens.append(row["bottom_digit"])
    return tokens


def target_result():
    tokens = load_target_tokens()
    n = len(tokens)
    in_domain = sum(1 for t in tokens if t.isalpha())
    return {
        "N_tokens_transcribed": n,
        "tokens_in_317_alphabet_domain (a-z)": in_domain,
        "share_in_domain": f"{in_domain}/{n} = {in_domain/n:.0%}",
        "note": "every transcribed token is a decimal digit 0-9; 317's system has no operation defined on digits, so it cannot be applied to any of them",
    }


def control_result(seed=1, n_letters=35):
    """Matched control: synthetic run of the SAME mechanism (keyword +
    317's table) on real period-Dutch letters of the same token count as
    the target (35, from target_result). This is not a blind cryptanalytic
    attack -- 317's system is a known, deterministic, reciprocal keyed
    substitution, not a puzzle to be solved -- so the number that matters
    here is not a solve rate but round-trip correctness, which shows the
    implementation is self-consistent and (unlike on 209) has something to
    operate on when the input is actually alphabetic.
    """
    lines = CORPUS.read_text(encoding="utf-8", errors="replace").splitlines()
    body = "\n".join(lines[9:])  # skip the source/provenance header block
    letters = [c.lower() for c in body if c.isalpha()]
    rnd = random.Random(seed)
    start = rnd.randrange(0, len(letters) - n_letters)
    control_plain = "".join(letters[start:start + n_letters])

    keyword = "nebawo"  # the keyword named in 317's own worked example
    ct = encipher(control_plain, keyword)
    rt = decipher(ct, keyword)

    correct = sum(1 for a, b in zip(rt, control_plain) if a == b)
    return {
        "design": f"period Dutch (Breda Staten-Generaal 1624-25 print corpus), N={n_letters} letters, same table+keyword mechanism as the target test",
        "control_plaintext_sample": control_plain,
        "control_ciphertext": ct,
        "round_trip_decode": rt,
        "letters_correct": f"{correct}/{n_letters} = {correct/n_letters:.0%}",
    }


if __name__ == "__main__":
    tgt = target_result()
    ctl = control_result()
    print("=== target (invnr 209 leaf 2) ===")
    for k, v in tgt.items():
        print(f"  {k}: {v}")
    print("=== control (317's own mechanism on matched-length period Dutch) ===")
    for k, v in ctl.items():
        print(f"  {k}: {v}")

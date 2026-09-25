#!/usr/bin/env python3
"""
LANE B3 bFAI, 25 Sept 2026. fair-game-2010 cheap_tests_in_order[0]: test the "Martin Halpin"
hypothesis (Cipherbrain post 36 comment, 2014-15) that the yellow-marked letter in the Fair Game
(2010) end credits marks the letter immediately AFTER it, not the marked letter itself.

Data: James Mulliss's real credit-context transcription (comment #5/#6, 9 Feb 2023, on disk,
see credits_words.py), giving the actual word each marked letter sits in. This is genuinely the
"original unmarked credits text" the spec asked for -- no IMDb fetch needed, since the word-level
context (which letter follows the mark) is already recorded per occurrence, which is exactly
what the hypothesis needs.

Position-alignment procedure (same on real data and both controls): for each marked-letter
occurrence, in list order, the "read" letter is the one immediately following the mark inside
the same word; if the mark is the word's last letter (a real ambiguity: the true next letter
would be the first letter of whatever the next credit word actually was), this script uses the
first letter of the NEXT entry in the list as a documented proxy and records it as such
(boundary=True) in the JSON output -- a limitation, not a resolved fact.

Multiset check (documented in NOTES.md): the 65 marked letters recoverable from this transcription
match the ciphertext's 67 known letters exactly except for one missing S and one missing T (two
marked occurrences the commenter did not record) -- strong independent corroboration this is the
same real marking, not a fabrication, but the transcription is incomplete by 2/67 and its list
order is NOT verified against the official AboveTopSecret numbering (order proxy, not fact).
"""
import json
import random
import subprocess
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
from credits_words import TOKENS, marked_positions

REPO = Path(__file__).resolve().parents[3]
SPEC = REPO / "specs" / "fair-game-2010.json"
JUDGE = REPO / "tools" / "judge_plaintext.py"
OUT = Path(__file__).parent


def next_letter_sequence(entries):
    """entries: list of (word, idx). Returns (sequence_str, n_boundary_proxies)."""
    seq = []
    n_boundary = 0
    for i, (word, idx) in enumerate(entries):
        if idx + 1 < len(word):
            seq.append(word[idx + 1])
        else:
            n_boundary += 1
            if i + 1 < len(entries):
                nxt_word = entries[i + 1][0]
                seq.append(nxt_word[0])
            # else: dropped (last entry, no next word to proxy from)
    return "".join(seq), n_boundary


def judge(text):
    r = subprocess.run(
        [sys.executable, str(JUDGE), str(SPEC), "--text", text, "--json"],
        capture_output=True, text=True,
    )
    try:
        return json.loads(r.stdout)
    except Exception:
        return {"error": r.stdout + r.stderr, "returncode": r.returncode}


def main():
    random.seed(20260925)

    # ---- Test 1: real data ----
    real_entries = marked_positions()
    real_seq, real_boundary = next_letter_sequence(real_entries)
    real_verdict = judge(real_seq)

    # ---- Control A: 3 synthetic sequences hiding a known 13-letter name ----
    NAME = "ROBERTJOHNSON"  # 13 letters, arbitrary, unrelated to the film's plot
    assert len(NAME) == 13
    name_trials = []
    words_pool = [t.lower() for t in TOKENS]
    # for each target letter, every (word, idx) in the pool whose next char is that letter
    by_next_letter = {}
    for word in words_pool:
        for i in range(len(word) - 1):
            by_next_letter.setdefault(word[i + 1], []).append((word, i))
    for trial in range(3):
        rng = random.Random(20260925 + trial)
        synth_entries = []
        ok = True
        for target_next in NAME:
            candidates = by_next_letter.get(target_next.lower(), [])
            if not candidates:
                ok = False
                break
            synth_entries.append(rng.choice(candidates))
        if not ok:
            name_trials.append({"trial": trial, "constructible": False})
            continue
        seq, boundary = next_letter_sequence(synth_entries)
        name_trials.append({
            "trial": trial,
            "constructible": True,
            "recovered": seq.upper(),
            "true_name": NAME,
            "match": seq.upper() == NAME,
            "boundary_proxies_used": boundary,
        })

    # ---- Control B: 3 random-marking false-positive trials ----
    random_trials = []
    for trial in range(3):
        rng = random.Random(9000 + trial)
        n = len(real_entries)  # same N as the real test
        rand_entries = []
        for _ in range(n):
            word = rng.choice(words_pool)
            idx = rng.randrange(len(word))
            rand_entries.append((word, idx))
        seq, boundary = next_letter_sequence(rand_entries)
        verdict = judge(seq)
        random_trials.append({
            "trial": trial,
            "sequence": seq,
            "n_letters": len(seq),
            "boundary_proxies_used": boundary,
            "judge": verdict,
        })

    result = {
        "test": "fair-game-2010 cheap_tests_in_order[0]: Halpin next-letter hypothesis",
        "date": "25 Sept 2026",
        "source_of_real_words": "sources/schmeh/posts/36-fair-game.txt, James Mulliss comment #5/#6 (already on disk)",
        "multiset_check": "65 recoverable marked letters vs 67 known ciphertext letters: matches exactly except missing one S and one T (documented, see NOTES.md) -- corroborates the transcription but it is incomplete by 2/67 and its list order is an unverified proxy for true credit order",
        "real_test": {
            "n_entries": len(real_entries),
            "n_boundary_proxies_used": real_boundary,
            "next_letter_sequence": real_seq,
            "n_letters": len(real_seq),
            "judge": real_verdict,
        },
        "control_A_planted_name": {
            "name": NAME,
            "trials": name_trials,
            "recovered_all_3": len(name_trials) == 3 and all(t.get("constructible") and t.get("match") for t in name_trials),
        },
        "control_B_random_false_positive_rate": {
            "trials": random_trials,
            "n_pass": sum(1 for t in random_trials if t["judge"].get("pass") is True),
            "n_trials": len(random_trials),
        },
    }
    (OUT / "test1_output.json").write_text(json.dumps(result, indent=2))
    print(json.dumps(result, indent=2))


if __name__ == "__main__":
    main()

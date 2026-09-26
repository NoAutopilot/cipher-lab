#!/usr/bin/env python3
"""LANE B5 bRIK, 26 Sept 2026: use R4284's own key-test leaf (four Latin phrases written over
their cipher-letter equivalents, on r4284_transcription_bourdeau.txt) as a crib for R4282's
letter cipher, on the hypothesis (QUEUE.md G4/rank 4) that R4282 may share R4284's key.

Reproducible per CLAUDE.md rule 7: regenerates the crib key, the coverage numbers and the three
controls from the two committed transcriptions (Bourdeau, dbourdeau/cyphersolver,
riksarkivet1628/, commit fc0c9e8, read 26 Sept 2026) with no external state. `--check` re-derives
and diffs against report.json; exits 1 if stale.

Design (rule 3, matched controls):
  A. crib key applied to real R4282                      <- the test
  B. N synthetic keys of the same shape (same symbol groupings from the crib, letters within each
     group's assignment shuffled) applied to real R4282  <- is the crib's SPECIFIC letter
     assignment doing anything, or would any key built from the same symbols do as well?
  C. the real crib key applied to N shuffles of R4282's own cipher-character stream <- is
     whatever the crib key surfaces a property of R4282's real letter order, or would it surface
     on any random re-ordering of the same characters?
Coverage (fraction of R4282 characters whose sign is one the crib key assigns a letter to) is
identical across B given the same symbol groups are reused, and identical across C by
construction (a shuffle preserves the character multiset) -- reported anyway as the mechanical
number the control is entitled to, per rule 3's "report both numbers".
No wired Latin corpus exists (tools/judge_plaintext.py's LANG_CORPORA has no "la" key -- the
comment at that file's line ~62 calls la_repo circular, target's-own-reading-only, "not wired");
Latin-likeness is graded by eye here (M grade) against a small fixed list of common short Latin
function words/endings, applied identically to the target and every control.
"""
import argparse, collections, hashlib, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent

# Common short Latin function words / endings used only as an eyeball aid (rule 4: M grade, not a
# language judge -- no wired "la" corpus exists to do this mechanically per CLAUDE.md LANE B5 note).
LATIN_HINTS = {
    "et", "in", "ad", "ut", "sit", "est", "non", "sed", "per", "cum", "qui", "quod", "de", "ab",
    "ex", "si", "se", "nec", "jam", "tam", "tum", "hoc", "hic", "haec", "ille", "eius", "suis",
    "quae", "quibus", "atque", "que", "tur", "unt", "ent", "ibus", "orum", "arum", "tio", "tas",
}


def read_crib_pairs():
    """Extract the four (plain-phrase, cipher-line) pairs from r4284_transcription_bourdeau.txt's
    key-test leaf (the block starting '## IMG_R4284_I25751_P_hi.jpeg right page (clear line...')."""
    text = (TARGET / "r4284_transcription_bourdeau.txt").read_text(encoding="utf-8")
    lines = text.splitlines()
    start = next(i for i, l in enumerate(lines) if l.startswith("## IMG_R4284_I25751_P_hi.jpeg right page"))
    leaf = lines[start + 1:start + 9]
    # leaf = [effvsorem sangvinis., tbb.k3.dgtb. bpcwkyey3, [pestem, struck through] patrie.,
    #         Ltsico ipigyt, preter natvralem, lgtity. cpikyppatb., distvrbatorem religionis,
    #         sysikggpiagtb gtaygygdieys]
    phrase_lines = [leaf[0], "pestem patrie.", leaf[4], leaf[6]]
    cipher_lines = [leaf[1], leaf[3], leaf[5], leaf[7]]
    pairs = []
    for pl, cl in zip(phrase_lines, cipher_lines):
        pwords = re.findall(r"[A-Za-z]+", pl)
        cwords = cl.split()
        assert len(pwords) == len(cwords), (pl, cl)
        for pw, cw in zip(pwords, cwords):
            pairs.append((pw.lower(), cw.replace(".", "")))
    return pairs


def build_key(pairs):
    letter_to_syms = collections.defaultdict(collections.Counter)
    sym_to_letters = collections.defaultdict(collections.Counter)
    mismatches = []
    for plain, cipher in pairs:
        n = min(len(plain), len(cipher))
        if len(plain) != len(cipher):
            mismatches.append({"plain": plain, "cipher": cipher, "plain_len": len(plain), "cipher_len": len(cipher)})
        for i in range(n):
            p, c = plain[i], cipher[i]
            letter_to_syms[p][c] += 1
            sym_to_letters[c][p] += 1
    return letter_to_syms, sym_to_letters, mismatches


def read_r4282_signs():
    """Pull R4282's cipher signs, dropping bracketed clear-Latin insertions, comments, page
    headings and punctuation-only tokens (':' '.' '-' '?' '^'). Returns (tokens, flat_chars)."""
    text = (TARGET / "r4282_transcription_bourdeau.txt").read_text(encoding="utf-8")
    lines = [l for l in text.splitlines() if l.strip() and not l.startswith("#") and not l.startswith("##")]
    tokens = []
    for line in lines:
        line = re.sub(r"\[[^\]]*\]", " ", line)  # drop bracketed clear Latin
        for raw in line.split():
            tok = raw.strip("?^")
            if not tok or tok in (":", ".", "-"):
                continue
            tok = tok.rstrip(".").rstrip(":")
            if tok:
                tokens.append(tok)
    flat = "".join(tokens)
    return tokens, flat


def decode(tokens, sym_to_letters):
    """Majority-vote decode; uncovered signs left as '_'. Returns (decoded_tokens, covered, total)."""
    out_tokens = []
    covered = 0
    total = 0
    for tok in tokens:
        out = []
        for ch in tok:
            total += 1
            if ch in sym_to_letters:
                covered += 1
                letter = sym_to_letters[ch].most_common(1)[0][0]
                out.append(letter)
            else:
                out.append("_")
        out_tokens.append("".join(out))
    return out_tokens, covered, total


def latin_hint_count(decoded_tokens):
    """Count decoded tokens containing one of LATIN_HINTS as a substring, and tokens that are
    fully covered (no '_') of length >= 3. Both counts are the same eyeball aid applied uniformly
    to target and controls."""
    hint_hits = sum(1 for t in decoded_tokens if any(h in t for h in LATIN_HINTS))
    full_cover_ge3 = sum(1 for t in decoded_tokens if "_" not in t and len(t) >= 3)
    return hint_hits, full_cover_ge3


def synthetic_key_same_shape(sym_to_letters, seed):
    """Same symbol groupings (which signs share a letter) as the real crib key, but the specific
    letter label attached to each group is shuffled. Coverage over R4282 is unchanged (same
    symbols known); only which letter each symbol decodes to changes."""
    rng = random.Random(seed)
    # group signs by which crib letter they belong to (their majority letter in the real key)
    groups = collections.defaultdict(list)
    for sym, letters in sym_to_letters.items():
        real_letter = letters.most_common(1)[0][0]
        groups[real_letter].append(sym)
    real_letters = list(groups.keys())
    shuffled_letters = real_letters[:]
    rng.shuffle(shuffled_letters)
    mapping = dict(zip(real_letters, shuffled_letters))
    new_sym_to_letters = {}
    for real_letter, syms in groups.items():
        new_letter = mapping[real_letter]
        for s in syms:
            new_sym_to_letters[s] = collections.Counter({new_letter: 1})
    return new_sym_to_letters


def shuffled_r4282(tokens, seed):
    """Shuffle R4282's own character stream (flattened, then re-cut into the original token
    lengths) so the multiset of signs -- and hence coverage -- is unchanged, but position/order
    (and hence any word-level Latin-likeness) is destroyed."""
    rng = random.Random(seed)
    chars = list("".join(tokens))
    rng.shuffle(chars)
    out_tokens = []
    i = 0
    for tok in tokens:
        out_tokens.append("".join(chars[i:i + len(tok)]))
        i += len(tok)
    return out_tokens


def run_condition(label, tokens, sym_to_letters):
    decoded, covered, total = decode(tokens, sym_to_letters)
    hints, full3 = latin_hint_count(decoded)
    return {
        "label": label,
        "covered_chars": covered,
        "total_chars": total,
        "coverage_frac": round(covered / total, 4) if total else 0.0,
        "latin_hint_tokens": hints,
        "fully_covered_tokens_ge3": full3,
        "num_tokens": len(decoded),
        "sample_decoded": " ".join(decoded[:24]),
    }


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", action="store_true", help="re-derive and diff against report.json; exit 1 if stale")
    ap.add_argument("--seeds", type=int, default=3, help="number of synthetic-key and shuffle controls (default 3)")
    args = ap.parse_args()

    pairs = read_crib_pairs()
    letter_to_syms, sym_to_letters, mismatches = build_key(pairs)
    tokens, flat = read_r4282_signs()

    report = {
        "crib_pairs": [{"plain": p, "cipher": c} for p, c in pairs],
        "crib_mismatches": mismatches,
        "crib_letter_to_symbols": {k: dict(v) for k, v in sorted(letter_to_syms.items())},
        "r4282_total_chars": len(flat),
        "r4282_num_tokens": len(tokens),
        "r4282_distinct_signs": len(set(flat)),
        "A_real_crib_on_real_R4282": run_condition("A: real crib key vs real R4282", tokens, sym_to_letters),
        "B_synthetic_keys_on_real_R4282": [
            run_condition(f"B{seed}: synthetic same-shape key vs real R4282", tokens,
                          synthetic_key_same_shape(sym_to_letters, seed))
            for seed in range(args.seeds)
        ],
        "C_real_crib_on_shuffled_R4282": [
            run_condition(f"C{seed}: real crib key vs shuffled R4282", shuffled_r4282(tokens, 1000 + seed), sym_to_letters)
            for seed in range(args.seeds)
        ],
    }

    out_path = TARGET / "report.json"
    new_text = json.dumps(report, indent=1, sort_keys=True)
    if args.check:
        if not out_path.exists():
            print("STALE: report.json does not exist"); sys.exit(1)
        old_text = out_path.read_text(encoding="utf-8")
        if json.loads(old_text) != json.loads(new_text):
            print("STALE: report.json does not match a fresh re-derivation"); sys.exit(1)
        print("OK: report.json matches a fresh re-derivation"); sys.exit(0)

    out_path.write_text(new_text, encoding="utf-8")
    print(json.dumps(report["A_real_crib_on_real_R4282"], indent=1))
    for b in report["B_synthetic_keys_on_real_R4282"]:
        print(json.dumps(b, indent=1))
    for c in report["C_real_crib_on_shuffled_R4282"]:
        print(json.dumps(c, indent=1))
    print("wrote", out_path)


if __name__ == "__main__":
    main()

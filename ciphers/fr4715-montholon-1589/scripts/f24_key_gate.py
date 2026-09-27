#!/usr/bin/env python3
"""Rule-3 gate + key recovery report for f.24's interlinear alignment (MONT-KEY6, 27 Sept 2026).

Runs tools/interlinear_align.py align on the real (line,gloss)<->(line,cipher) pairing, with NO --prior
(a blind context-only run, so its own recovered meaning for each already-known letter-homophone code can
be checked against keys/key_vieuville_nevers.tsv as an independent known-answer gate -- the same
known-answer-control shape as AX2-BRO4, not a circular one where the answer was seeded first). Then
repeats the same alignment N times with the gloss-to-line pairing shuffled (scripts/build_f24_pairs.py
--shuffle-seed), and reports the known-letter agreement fraction real vs shuffled mean -- the control can
fail differently from the real run (a shuffled gloss carries no correspondence to the cipher groups it is
now paired with, so its recovered "meanings" are alignment noise, not signal).

    python3 scripts/f24_key_gate.py witness_f24/ciphertext_draft.tsv keys/key_vieuville_nevers.tsv \
        --shuffles 20 --out-dir witness_f24

Writes witness_f24/pairs.tsv, witness_f24/align_real.tsv, witness_f24/key_real.tsv,
keys/key_f24_recovered.tsv (the dotted word-code table, value -> meaning, counts), and prints the gate.
"""
import csv
import subprocess
import sys
import os

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
REPO = os.path.dirname(os.path.dirname(TARGET))

PSEUDO_TO_SIGN = {"96": "♀", "97": "▽"}

# from NOTES.md "An important caveat" -- no.58's own aligned_dump.txt gloss for its dotted word-codes,
# for the agree/conflict cross-check (rule 4: a conflict between two witnesses is logged, not settled
# by majority).
NO58_DOTTED = {
    47: "qui", 30: "ma", 41: "par", 65: "comme", 16: "de", 11: "au", 20: "est", 48: "quil",
    42: "pour", 19: "et", 46: "que", 25: "la", 35: "ne", 50: "se", 99: "vous", 28: "luy",
    64: "catholique", 75: "faire", 52: "si", 22: "je", 31: "me", 40: "ou", 27: "les", 14: "ce",
}


def load_key_signs(path):
    """sign (str) -> value (letter), letter rows only."""
    out = {}
    with open(path, encoding="utf-8") as f:
        header = None
        for ln in f:
            ln = ln.rstrip("\n")
            if not ln.strip() or ln.startswith("#"):
                continue
            cols = ln.split("\t")
            if header is None:
                header = cols
                continue
            r = dict(zip(header, cols))
            if r.get("kind") == "letter":
                out[r["sign"]] = r["value"]
    return out


def run_align(pairs_path, align_out, key_out, floor=100):
    subprocess.run(
        [sys.executable, os.path.join(REPO, "tools", "interlinear_align.py"), "align",
         pairs_path, align_out, key_out, "--floor", str(floor)],
        check=True, cwd=TARGET, capture_output=True, text=True,
    )


def known_letter_agreement(key_out_path, known_signs):
    """-> (matched, total, per_code list) over codes in `known_signs` that appear (n>=1) in key_out."""
    recovered = {}
    with open(key_out_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            recovered[r["value"]] = (r["meaning"], int(r["n"]), int(r["agree"]))
    matched, total, rows = 0, 0, []
    for sign, truth in known_signs.items():
        pseudo = {"♀": "96", "▽": "97"}.get(sign, sign)
        if not pseudo.isdigit():
            continue
        if pseudo not in recovered:
            continue
        meaning, n, agree = recovered[pseudo]
        total += 1
        ok = meaning.strip().lower() == truth.strip().lower()
        matched += int(ok)
        rows.append((sign, truth, meaning, n, agree, ok))
    return matched, total, rows


def dotted_recovered(key_out_path):
    out = {}
    with open(key_out_path, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            v = int(r["value"])
            if v >= 100:
                out[v - 100] = (r["meaning"], int(r["n"]), int(r["agree"]), r["others"])
    return out


def main():
    args = sys.argv[1:]
    shuffles = 20
    out_dir = "witness_f24"
    if "--shuffles" in args:
        k = args.index("--shuffles")
        shuffles = int(args[k + 1])
        del args[k:k + 2]
    if "--out-dir" in args:
        k = args.index("--out-dir")
        out_dir = args[k + 1]
        del args[k:k + 2]
    draft_path, key_path = args

    known_signs = load_key_signs(key_path)
    build = os.path.join(HERE, "build_f24_pairs.py")

    real_pairs = os.path.join(out_dir, "pairs.tsv")
    subprocess.run([sys.executable, build, draft_path, real_pairs], check=True, cwd=TARGET)
    align_real = os.path.join(out_dir, "align_real.tsv")
    key_real = os.path.join(out_dir, "key_real.tsv")
    run_align(os.path.join(TARGET, real_pairs), os.path.join(TARGET, align_real), os.path.join(TARGET, key_real))
    m, t, rows = known_letter_agreement(os.path.join(TARGET, key_real), known_signs)
    real_frac = m / t if t else 0.0
    print(f"REAL: known letter-codes recovered blind (no prior): {m}/{t} = {real_frac:.3f}")
    for sign, truth, meaning, n, agree, ok in sorted(rows, key=lambda r: (-r[3], r[0])):
        print(f"  sign {sign!r} truth={truth} recovered={meaning!r} n={n} agree={agree} {'OK' if ok else 'MISS'}")

    shuffled_fracs = []
    for seed in range(1, shuffles + 1):
        shuf_pairs = os.path.join(out_dir, f"pairs_shuf{seed}.tsv")
        subprocess.run([sys.executable, build, draft_path, shuf_pairs, "--shuffle-seed", str(seed)],
                       check=True, cwd=TARGET)
        align_shuf = os.path.join(out_dir, f"align_shuf{seed}.tsv")
        key_shuf = os.path.join(out_dir, f"key_shuf{seed}.tsv")
        run_align(os.path.join(TARGET, shuf_pairs), os.path.join(TARGET, align_shuf), os.path.join(TARGET, key_shuf))
        sm, st, _ = known_letter_agreement(os.path.join(TARGET, key_shuf), known_signs)
        shuffled_fracs.append(sm / st if st else 0.0)
        os.remove(os.path.join(TARGET, shuf_pairs))
        os.remove(os.path.join(TARGET, align_shuf))
        os.remove(os.path.join(TARGET, key_shuf))

    mean_shuf = sum(shuffled_fracs) / len(shuffled_fracs) if shuffled_fracs else 0.0
    print(f"\nSHUFFLED ({shuffles} seeds): {['%.3f' % x for x in shuffled_fracs]}")
    print(f"shuffled mean = {mean_shuf:.3f}, range {min(shuffled_fracs):.3f}-{max(shuffled_fracs):.3f}")
    print(f"\nGATE: real {real_frac:.3f} ({m}/{t}) vs shuffled mean {mean_shuf:.3f} -- "
          f"{'MET' if real_frac > mean_shuf else 'NOT MET'} (real must exceed shuffled mean)")

    dotted = dotted_recovered(os.path.join(TARGET, key_real))
    rec_path = os.path.join(TARGET, "keys", "key_f24_recovered.tsv")
    with open(rec_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter="\t", lineterminator="\n")
        w.writerow(["sign", "value", "kind", "grade", "source", "n", "agree", "others", "no58_dump_value", "no58_agree"])
        for digits in sorted(dotted):
            meaning, n, agree, others = dotted[digits]
            no58 = NO58_DOTTED.get(digits)
            no58_agree = "" if no58 is None else ("agree" if no58.strip().lower() == meaning.strip().lower() else "CONFLICT")
            w.writerow([f"'{digits}", meaning, "word", "C", "f.24 interlinear (MONT-KEY6)", n, agree, others,
                        no58 or "", no58_agree])
    print(f"\nwrote {rec_path} ({len(dotted)} dotted word-codes recovered)")
    conflicts = [d for d in dotted if NO58_DOTTED.get(d) and NO58_DOTTED[d].strip().lower() != dotted[d][0].strip().lower()]
    agrees = [d for d in dotted if NO58_DOTTED.get(d) and NO58_DOTTED[d].strip().lower() == dotted[d][0].strip().lower()]
    print(f"cross-check vs no.58's aligned_dump.txt dotted glosses: {len(agrees)} agree, {len(conflicts)} conflict")
    for d in conflicts:
        print(f"  CONFLICT '{d}: f.24={dotted[d][0]!r} vs no.58 dump={NO58_DOTTED[d]!r}")


if __name__ == "__main__":
    main()

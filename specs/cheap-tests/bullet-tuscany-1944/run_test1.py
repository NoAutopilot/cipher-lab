#!/usr/bin/env python3
"""Cheap test 1 for specs/bullet-tuscany-1944.json: mechanically test the rejected forum
'solution' (THEYTHROWGRENADESWEPULLPINSANDTHROWBACK) against the 44-letter cipher body under
Vigenere, Beaufort, variant Beaufort and simple-substitution (MASC), with a matched control
(same claimed plaintext enciphered under a real random key of each family, same checks run on
the result). Written 25 Sept 2026, LANE B2 worker bBUL. No network, no external data beyond the
target/spec text and Python's stdlib random.
"""
import json
import random
from collections import Counter
from pathlib import Path

OUT = Path(__file__).resolve().parent

CIPHER_BODY = "CBFUKYYEVOZILOOZVNCWJKQRSAWBYZUGYTZWYBATRSUA"
CLAIMED_PT = "THEYTHROWGRENADESWEPULLPINSANDTHROWBACK"

assert len(CIPHER_BODY) == 44, len(CIPHER_BODY)
assert len(CLAIMED_PT) == 39, len(CLAIMED_PT)
LEN_MISMATCH = len(CIPHER_BODY) - len(CLAIMED_PT)

FAMILIES = ["vigenere", "beaufort", "variant_beaufort"]


def c2i(c):
    return ord(c) - 65


def i2c(i):
    return chr((i % 26) + 65)


def derive_keystream(cipher, plain, family):
    ks = []
    for c, p in zip(cipher, plain):
        ci, pi = c2i(c), c2i(p)
        if family == "vigenere":            # C = P + K  ->  K = C - P
            k = (ci - pi) % 26
        elif family == "beaufort":           # C = K - P  ->  K = C + P
            k = (ci + pi) % 26
        elif family == "variant_beaufort":   # C = P - K  ->  K = P - C
            k = (pi - ci) % 26
        else:
            raise ValueError(family)
        ks.append(k)
    return ks


def apply_family(plain, keystream, family):
    out = []
    for p, k in zip(plain, keystream):
        pi = c2i(p)
        if family == "vigenere":
            ci = (pi + k) % 26
        elif family == "beaufort":
            ci = (k - pi) % 26
        elif family == "variant_beaufort":
            ci = (pi - k) % 26
        else:
            raise ValueError(family)
        out.append(i2c(ci))
    return "".join(out)


def periodicity_score(ks, period):
    n = len(ks)
    total_correct = 0
    for r in range(period):
        vals = [ks[i] for i in range(r, n, period)]
        if not vals:
            continue
        cnt = Counter(vals)
        _, best = cnt.most_common(1)[0]
        total_correct += best
    return total_correct / n


def best_period(ks, max_period=20):
    scores = {p: periodicity_score(ks, p) for p in range(1, min(max_period, len(ks)) + 1)}
    best_p = max(scores, key=lambda p: (scores[p], -p))
    return best_p, scores[best_p], scores


def masc_consistency(cipher, plain):
    c2p, p2c, violations = {}, {}, 0
    for c, p in zip(cipher, plain):
        if c in c2p and c2p[c] != p:
            violations += 1
        else:
            c2p[c] = p
        if p in p2c and p2c[p] != c:
            violations += 1
        else:
            p2c[p] = c
    return {
        "violations": violations,
        "n_pairs": len(cipher),
        "distinct_cipher_letters": len(c2p),
        "distinct_plain_letters": len(p2c),
    }


def scan_alignments(cipher, plain):
    """All contiguous windows of len(plain) letters inside cipher (cipher is longer)."""
    n_offsets = len(cipher) - len(plain) + 1
    results = {"offsets_tested": n_offsets, "per_offset": []}
    for off in range(n_offsets):
        window = cipher[off:off + len(plain)]
        row = {"offset": off, "window": window, "families": {}, "masc": masc_consistency(window, plain)}
        for fam in FAMILIES:
            ks = derive_keystream(window, plain, fam)
            p, score, scores = best_period(ks)
            row["families"][fam] = {"best_period": p, "best_score": round(score, 4)}
        results["per_offset"].append(row)
    return results


def run_target():
    result = {
        "cipher_body_len": len(CIPHER_BODY),
        "claimed_plaintext_len": len(CLAIMED_PT),
        "length_mismatch": LEN_MISMATCH,
        "mismatch_implication": (
            "Vigenere, Beaufort, variant Beaufort and simple substitution are all length-preserving "
            "(one ciphertext letter per plaintext letter); with 44 cipher letters and only 39 claimed "
            "plaintext letters, no key of any of these families can map the full 44-letter body onto "
            "this plaintext under any of them -- 5 cipher letters have no plaintext counterpart at all. "
            "Schmeh's prose rejection is confirmed mechanically, not just on plausibility grounds. The "
            "scan below is a fallback probe: does ANY contiguous 39-letter window of the 44-letter body "
            "(6 possible offsets) look consistent with a short-period key or a MASC under the claimed "
            "plaintext, in case the poster silently dropped 5 letters (e.g. treating part of the body as "
            "further metadata)."
        ),
        "alignment_scan": scan_alignments(CIPHER_BODY, CLAIMED_PT),
    }
    return result


def run_control(seed):
    rng = random.Random(seed)
    result = {"seed": seed, "families": {}}
    for fam in FAMILIES:
        period = rng.choice([3, 4, 5, 6, 7])
        key = [rng.randrange(26) for _ in range(period)]
        keystream = [key[i % period] for i in range(len(CLAIMED_PT))]
        cipher = apply_family(CLAIMED_PT, keystream, fam)
        ks_recovered = derive_keystream(cipher, CLAIMED_PT, fam)
        p, score, _ = best_period(ks_recovered)
        result["families"][fam] = {
            "true_period": period,
            "recovered_best_period": p,
            "recovered_best_score": round(score, 4),
            "period_found": (p == period or (p < period and period % p == 0) or (period < p and p % period == 0)),
        }
    # MASC control: random bijective letter map applied to the claimed plaintext
    letters = list("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
    shuffled = letters[:]
    rng.shuffle(shuffled)
    keymap = dict(zip(letters, shuffled))
    masc_cipher = "".join(keymap[c] for c in CLAIMED_PT)
    result["masc"] = masc_consistency(masc_cipher, CLAIMED_PT)
    return result


def main():
    target = run_target()
    controls = [run_control(seed) for seed in (1, 2, 3)]

    # Summary verdicts: best score achieved for each family across all 6 target offsets,
    # vs the control's recovered score for its true (or a period-divisor) match.
    summary = {"families": {}}
    for fam in FAMILIES:
        target_best = max(row["families"][fam]["best_score"] for row in target["alignment_scan"]["per_offset"])
        control_scores = [c["families"][fam]["recovered_best_score"] for c in controls]
        control_found = [c["families"][fam]["period_found"] for c in controls]
        summary["families"][fam] = {
            "target_best_score_any_offset": round(target_best, 4),
            "control_recovered_scores": [round(s, 4) for s in control_scores],
            "control_period_found_all_seeds": all(control_found),
        }
    target_masc_best = min(row["masc"]["violations"] for row in target["alignment_scan"]["per_offset"])
    control_masc_violations = [c["masc"]["violations"] for c in controls]
    summary["masc"] = {
        "target_min_violations_any_offset": target_masc_best,
        "control_violations": control_masc_violations,
    }

    out = {"target": target, "controls": controls, "summary": summary}
    (OUT / "test1_output.json").write_text(json.dumps(out, indent=1))
    print(json.dumps(summary, indent=1))


if __name__ == "__main__":
    main()

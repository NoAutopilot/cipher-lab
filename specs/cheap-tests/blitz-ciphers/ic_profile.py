#!/usr/bin/env python3
"""Cheap test 1 (specs/blitz-ciphers.json cheap_tests_in_order[0], 25 Sept 2026, bBLZ):
index-of-coincidence and letter-frequency profile of the two transcribed pages (Pelling's own
partial transcription, quoted in Cipherbrain post 41), folded to letters-only, case-sensitive
(N=581, K=48) and case-folded (N=581, K=25), against matched-length/matched-K controls built
from real English plaintext (pg1661_holmes.txt, the corpus already used elsewhere in this repo
for English IC baselines, e.g. mlh-1976 NOTES.md) under three designs, following Pelling's own
"combines monoalphabetic frequency counts with polyalphabetic disorder and homophonic
inscrutability" framing (Cipherbrain post 41, quoted in ciphers/blitz-ciphers/NOTES.md):

  (a) monoalphabetic substitution: a substitution cipher preserves the plaintext's own IC, so
      the control is simply N-letter windows of English plaintext.
  (b) periodic polyalphabetic (Vigenere/Beaufort-style): N-letter English windows encrypted
      with a random period-p key for p in 2..20; report both the naive pooled IC (which drops
      as p grows) and the Kasiski/Friedman periodic-IC-scan (split ciphertext into p residue
      classes by position mod p, average each class's own IC) -- the scan should show a peak
      at the true period on the control, which is the power check for running the same scan on
      the target.
  (c) homophonic substitution: a simple frequency-flattening homophone map (each plaintext
      letter gets a number of code symbols roughly proportional to its English frequency, sized
      to hit the target K) applied to N-letter English windows.
  (d) uniform-random: K-symbol uniform random string of length N, the floor for "no structure
      at all" (IC ~= 1/K).

Every control is sampled 50 times (different corpus windows / random keys / random maps) and
reported as mean and [min, max] (CLAUDE.md rule 3: report both numbers, not one solver's single
verdict). Disk-only, no network.
"""
import random
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent

CORPUS_PATH = ROOT / "tools/data/pg1661_holmes.txt"
SAMPLES = 50


def ic(s):
    c = Counter(s)
    n = len(s)
    if n < 2:
        return 0.0
    return sum(v * (v - 1) for v in c.values()) / (n * (n - 1))


def load_target(path):
    return Path(path).read_text(encoding="utf-8").strip()


def load_corpus_letters(path, casefold):
    t = path.read_text(encoding="utf-8", errors="replace")
    t = re.sub(r"[^A-Za-z]", "", t)
    if casefold:
        t = t.lower()
    return t


def sample_window(corpus, n, rng):
    if len(corpus) <= n:
        return corpus
    start = rng.randrange(len(corpus) - n)
    return corpus[start:start + n]


def periodic_scan(s, pmax):
    """Return {p: mean IC of the p residue classes} for p=2..pmax."""
    out = {}
    for p in range(2, pmax + 1):
        classes = ["" for _ in range(p)]
        for i, ch in enumerate(s):
            classes[i % p] += ch
        ics = [ic(c) for c in classes if len(c) > 1]
        out[p] = sum(ics) / len(ics) if ics else 0.0
    return out


def encode_periodic(plain, period, alphabet, rng):
    """Vigenere-style: shift each letter by a random per-position-in-period offset over `alphabet`."""
    key = [rng.randrange(len(alphabet)) for _ in range(period)]
    idx = {c: i for i, c in enumerate(alphabet)}
    out = []
    for i, ch in enumerate(plain):
        if ch not in idx:
            continue
        shift = key[i % period]
        out.append(alphabet[(idx[ch] + shift) % len(alphabet)])
    return "".join(out)


def build_homophone_map(plain_corpus, k_target, alphabet, rng):
    """Distribute k_target code symbols across the letters roughly proportional to corpus
    frequency (largest-remainder apportionment, Hamilton's method -- always terminates and
    always sums to exactly k_target, even when k_target is less than the number of distinct
    letters, in which case the lowest-frequency letters get zero codes and drop out of the map,
    same as this cipher's own K=48 < 52 case-sensitive letters)."""
    freq = Counter(plain_corpus)
    letters = [c for c in alphabet if freq.get(c, 0) > 0]
    total = sum(freq[c] for c in letters)
    shares = {c: k_target * freq[c] / total for c in letters}
    alloc = {c: int(shares[c]) for c in letters}
    remainder = k_target - sum(alloc.values())
    order = sorted(letters, key=lambda c: shares[c] - alloc[c], reverse=True)
    for c in order[:remainder]:
        alloc[c] += 1
    codes = list(range(k_target))
    rng.shuffle(codes)
    cmap = {}
    ci = 0
    for c in letters:
        n = alloc[c]
        cmap[c] = codes[ci:ci + n]
        ci += n
    return cmap


def encode_homophonic(plain, cmap, rng):
    out = []
    for ch in plain:
        opts = cmap.get(ch)
        if not opts:
            continue
        out.append(rng.choice(opts))
    return out  # list of int codes, not chars -- IC computed on the code stream directly


def report(name, values):
    mean = sum(values) / len(values)
    print(f"{name}\tmean={mean:.4f}\tmin={min(values):.4f}\tmax={max(values):.4f}\tn={len(values)}")
    return mean


def main():
    rng = random.Random(1)
    corpus_cs_raw = CORPUS_PATH.read_text(encoding="utf-8", errors="replace")
    corpus_letters_cs = re.sub(r"[^A-Za-z]", "", corpus_cs_raw)
    corpus_letters_cf = corpus_letters_cs.lower()

    for label, target_path, corpus, alphabet in (
        ("case-sensitive", OUT / "ciphertext_letters_cs.txt", corpus_letters_cs,
         "".join(sorted(set(corpus_letters_cs)))),
        ("case-folded", OUT / "ciphertext_letters_cf.txt", corpus_letters_cf,
         "abcdefghijklmnopqrstuvwxyz"),
    ):
        print(f"\n==== {label} ====")
        target = load_target(target_path)
        n = len(target)
        k = len(set(target))
        print(f"target N={n} K={k}")
        print(f"target pooled IC = {ic(target):.4f}")
        cnt = Counter(target)
        top8 = cnt.most_common(8)
        print("target most common:", top8)

        # (a) monoalphabetic English control
        mono_ics = [ic(sample_window(corpus, n, rng)) for _ in range(SAMPLES)]
        report("control_monoalphabetic_english_pooled_IC", mono_ics)

        # (d) uniform random control (K-matched)
        rand_ics = []
        for _ in range(SAMPLES):
            s = "".join(rng.choice(alphabet) for _ in range(n))
            rand_ics.append(ic(s))
        report("control_uniform_random_pooled_IC (K=%d, theory~%.4f)" % (k, 1.0 / k), rand_ics)

        # (c) homophonic English control (K-matched)
        homo_pooled = []
        for _ in range(SAMPLES):
            window = sample_window(corpus, n, rng)
            cmap = build_homophone_map(corpus, k, "abcdefghijklmnopqrstuvwxyz" if label == "case-folded" else alphabet, rng)
            # window letters must be restricted to alphabet actually mapped
            win2 = "".join(c for c in window if c in cmap)
            codes = encode_homophonic(win2, cmap, rng)
            homo_pooled.append(ic(codes))
        report("control_homophonic_english_pooled_IC", homo_pooled)

        # target periodic scan
        pscan = periodic_scan(target, 20)
        print("target periodic IC scan p=2..20:",
              ", ".join(f"p{p}={v:.4f}" for p, v in pscan.items()))
        best_p = max(pscan, key=pscan.get)
        print(f"target periodic scan peak: p={best_p} IC={pscan[best_p]:.4f} "
              f"(vs pooled IC={ic(target):.4f}, vs uniform~{1.0/k:.4f})")

        # (b) periodic-Vigenere English control: build controls at a spread of periods,
        # report pooled IC and periodic-scan peak (power check + comparison baseline)
        print("control_periodic_vigenere_english (period -> pooled_IC mean[min,max], scan_peak mean[min,max]):")
        for period in (2, 3, 5, 7, 10, 15, 20):
            pooled_vals = []
            peak_vals = []
            recovered_at_true_p = 0
            for _ in range(20):
                window = sample_window(corpus, n, rng)
                enc = encode_periodic(window, period, alphabet, rng)
                pooled_vals.append(ic(enc))
                sc = periodic_scan(enc, 20)
                bp = max(sc, key=sc.get)
                peak_vals.append(sc[bp])
                if bp == period or (bp % period == 0) or (period % bp == 0 if bp else False):
                    recovered_at_true_p += 1
            pm = sum(pooled_vals) / len(pooled_vals)
            km = sum(peak_vals) / len(peak_vals)
            print(f"  p={period:2d}  pooled_IC mean={pm:.4f} [{min(pooled_vals):.4f},{max(pooled_vals):.4f}]  "
                  f"scan_peak mean={km:.4f} [{min(peak_vals):.4f},{max(peak_vals):.4f}]  "
                  f"scan_recovered_true_period={recovered_at_true_p}/20")


if __name__ == "__main__":
    main()

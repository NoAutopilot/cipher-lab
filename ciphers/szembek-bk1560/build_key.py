#!/usr/bin/env python3
"""Merge leaf65/66/67 groups.tsv (period-gloss transcription) with align.tsv (tools/interlinear_align.py,
--floor 100 over pairs.tsv) into ciphertext.tsv, key.tsv, exceptions.tsv and consistency_by_code.tsv.

Regenerates the inputs to tools/decode_key.py ciphers/szembek-bk1560 (bSZM, 26 Sept 2026). Run from the repo root:
    python3 tools/interlinear_align.py align ciphers/szembek-bk1560/pairs.tsv \
        ciphers/szembek-bk1560/align.tsv ciphers/szembek-bk1560/key_aligned.tsv --floor 100
    python3 ciphers/szembek-bk1560/build_key.py
    python3 tools/decode_key.py ciphers/szembek-bk1560 --check
"""
import csv, random
from collections import Counter, defaultdict
from pathlib import Path

T = Path(__file__).parent
LEAVES = ["65", "66", "67"]


def strip_code(tok):
    core = tok.strip(".,;:()'\"=?")
    return core if core.isdigit() and len(core) == 2 else None


def load_groups():
    rows = []
    for lf in LEAVES:
        with open(T / f"leaf{lf}/groups.tsv") as f:
            for row in csv.DictReader(f, delimiter="\t"):
                row["leaf"] = lf
                ln = row["line"]
                row["line_norm"] = ln.split(":", 1)[1] if ":" in ln else ln
                rows.append(row)
    return rows


def load_align():
    m = {}
    with open(T / "align.tsv") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            leaf, line = r["cipher_line"].split(":")
            pos1 = int(r["idx"]) + 1
            m[(leaf, line, pos1)] = r
    return m


def main():
    rows = load_groups()
    align_map = load_align()

    occs = defaultdict(list)  # code -> [(leaf, line, pos, letter_or_None)]
    for row in rows:
        if row["kind"] != "code":
            continue
        code = strip_code(row["token"])
        if code is None:
            continue
        ar = align_map.get((row["leaf"], row["line_norm"], int(row["pos"])))
        letter = None
        if ar and len(ar["plain_chunk"]) == 1 and ar["plain_chunk"].isalpha():
            letter = ar["plain_chunk"].lower()
        occs[code].append((row["leaf"], row["line_norm"], row["pos"], letter))

    mode_letter = {}
    for code, occ in occs.items():
        letters = [l for (_, _, _, l) in occ if l]
        if letters:
            mode_letter[code] = Counter(letters).most_common(1)[0][0]

    # ciphertext.tsv
    ct_rows = []
    for row in rows:
        code = strip_code(row["token"]) if row["kind"] == "code" else None
        sign = code if code is not None else "w:" + row["token"]
        ct_rows.append((row["leaf"], row["line_norm"], row["pos"], sign, row["confidence"]))
    with open(T / "ciphertext.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["leaf", "line", "pos", "sign", "conf"])
        w.writerows(ct_rows)

    # key.tsv
    with open(T / "key.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["code", "value", "grade", "source", "note"])
        for code in sorted(mode_letter, key=int):
            n = len(occs[code])
            nglossed = sum(1 for o in occs[code] if o[3])
            w.writerow([code, mode_letter[code], "C",
                        "gloss(pooled 3-leaf interlinear_align --floor 100)",
                        f"mode of {nglossed}/{n} glossed occurrences"])

    # exceptions.tsv: occurrences whose own aligned letter disagrees with the code's pooled mode
    exc_rows, c_count, m_count = [], 0, 0
    for code, occ_list in occs.items():
        mode = mode_letter.get(code)
        for (leaf, line, pos, letter) in occ_list:
            if mode and letter and letter != mode:
                exc_rows.append((leaf, line, pos, letter))
                m_count += 1
            else:
                c_count += 1
    with open(T / "exceptions.tsv", "w", newline="") as f:
        w = csv.writer(f, delimiter="\t")
        w.writerow(["folio", "line", "pos", "value", "grade", "reason"])
        for row in exc_rows:
            w.writerow([*row, "M", "occurrence's own aligned letter disagrees with code's pooled-mode letter"])

    # consistency control: real mode-agreement rate vs 1000 shuffles of the letter labels
    by_code_letters = {c: [o[3] for o in v if o[3]] for c, v in occs.items()}
    recur = {c: ls for c, ls in by_code_letters.items() if len(ls) >= 2}

    def consistency(m):
        tot = agree = 0
        for ls in m.values():
            if len(ls) < 2:
                continue
            tot += len(ls)
            agree += Counter(ls).most_common(1)[0][1]
        return agree, tot

    real_agree, real_tot = consistency(by_code_letters)
    random.seed(20260926)
    all_letters = [l for ls in by_code_letters.values() for l in ls]
    codes_list = list(by_code_letters.keys())
    counts = [len(by_code_letters[c]) for c in codes_list]
    rates = []
    for _ in range(1000):
        shuf = all_letters[:]
        random.shuffle(shuf)
        idx = tot2 = agree2 = 0
        for c, n in zip(codes_list, counts):
            ls = shuf[idx:idx + n]
            idx += n
            if n < 2:
                continue
            tot2 += n
            agree2 += Counter(ls).most_common(1)[0][1]
        rates.append(agree2 / tot2)
    rates.sort()

    with open(T / "consistency_by_code.tsv", "w") as f:
        f.write("code\tn\tmode_letter\tmode_count\trate\tall_letters\n")
        for c in sorted(recur, key=int):
            ls = recur[c]
            mc = Counter(ls).most_common(1)[0]
            f.write(f"{c}\t{len(ls)}\t{mc[0]}\t{mc[1]}\t{mc[1]/len(ls):.3f}\t{','.join(ls)}\n")

    print(f"codes: {len(occs)} distinct 2-digit codes, {len(mode_letter)} glossed at least once, "
          f"{len(occs) - len(mode_letter)} never glossed")
    print(f"tokens: C {c_count}, M {m_count}, U 0 (of {c_count + m_count} real-code tokens)")
    print(f"real consistency (token-weighted mode-agreement, recurring codes only): "
          f"{real_agree}/{real_tot} = {real_agree/real_tot:.3f}")
    print(f"shuffle control (1000x, seed 20260926): mean={sum(rates)/1000:.3f}, "
          f"95th pct={rates[950]:.3f}")


if __name__ == "__main__":
    main()

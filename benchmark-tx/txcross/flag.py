#!/usr/bin/env python3
"""MQS-TX-CROSSWORD (9 Oct 2026) step 1: crossword flags on Birago no.87, chosen WITHOUT the truth file.

Base reading = benchmark-tx/outputs/birago1572-no87/labels.tsv (reconciled + NO87-LABELS relabels, err_true 0.045).
Each single-letter sign is decoded through the printed 1572 key (harvest/key_1572_sheet.tsv); for every position the
it16dip n-gram LM (tools/judge_plaintext.py LANG_CORPORA, via tools/key_decode_lattice.LM) scores the current letter and
every other letter the key can spell with one sign, over (n-1) chars of left context + the letter + 4 chars of right
context.  gain = best other letter - current letter.  The decipherment flags where the transcription is least plausible,
whether or not any reader proposed another sign there (the lattice ceiling of TX-DECODE / TXD-HOLDOUT / TX-ALTS).

Arms (seed 20261009): T = top 60 positions by gain (gain > 0); D = 30 calibration decoys drawn from positions with
gain <= 0; R = 20 random positions from the rest (a null arm: same reader, same rule, no crossword flag).
Writes positions.tsv (qid, arm, line, pos, current sign, current letter, best letter, gain), the two reader packets
G1 (f178r, f179r, f178v L01-10) and G2 (f178v L11-23) with every question masked [qid] in the orientation.
"""
import csv, random, sys
from pathlib import Path
ROOT = Path(__file__).resolve().parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from key_decode_lattice import LM, read_key, load_model  # noqa: E402

HERE = Path(__file__).resolve().parent
BASE = ROOT / "benchmark-tx/outputs/birago1572-no87/labels.tsv"
KEY = ROOT / "ciphers/nevers-birago-fr3251-1572/harvest/key_1572_sheet.tsv"
NT, ND, NR, RIGHT, SEED = 60, 30, 20, 4, 20261009


class A: corpus = None; lang = "it16dip"


def main():
    rows = list(csv.DictReader(open(BASE, encoding="utf-8"), delimiter="\t"))
    key = read_key(KEY)
    letters = sorted({v for v in key.values() if len(v) == 1})
    lm = LM(load_model(A)); n1 = lm.n - 1
    vals = [key.get(r["sign"], "") for r in rows]
    # char offset of each position in the running text
    text, start = "", []
    for v in vals:
        start.append(len(text)); text += v
    out = []
    for i, r in enumerate(rows):
        v = vals[i]
        if len(v) != 1:
            continue
        left = text[max(0, start[i] - n1):start[i]]
        right = text[start[i] + 1:start[i] + 1 + RIGHT]
        def sc(c):
            return lm.extend(left, c + right)[1]
        cur = sc(v)
        best = max((c for c in letters if c != v), key=sc)
        out.append(dict(line=r["line"], pos=r["pos"], sign=r["sign"], cur=v, best=best, gain=round(sc(best) - cur, 4)))
    rnd = random.Random(SEED)
    pos_g = sorted([o for o in out if o["gain"] > 0], key=lambda o: -o["gain"])
    T = pos_g[:NT]
    rest = [o for o in out if o not in T]
    D = rnd.sample([o for o in rest if o["gain"] <= 0], ND)
    R = rnd.sample([o for o in rest if o not in D], NR)
    qs = [("T", o) for o in T] + [("D", o) for o in D] + [("R", o) for o in R]
    rnd.shuffle(qs)
    with open(HERE / "positions.tsv", "w") as f:
        f.write("qid\tarm\tline\tpos\tsign\tcur\tbest\tgain\n")
        for q, (arm, o) in enumerate(qs, 1):
            o["qid"] = q
            f.write(f"{q}\t{arm}\t{o['line']}\t{o['pos']}\t{o['sign']}\t{o['cur']}\t{o['best']}\t{o['gain']}\n")
    masked = {(o["line"], o["pos"]): o["qid"] for _, o in qs}
    for part, sel in (("G1", lambda l: l.startswith(("f178r", "f179r")) or l <= "f178v_L10"),
                      ("G2", lambda l: l.startswith("f178v") and l > "f178v_L10")):
        lines = [l for l in dict.fromkeys(r["line"] for r in rows) if sel(l)]
        with open(HERE / f"orient_{part}.txt", "w") as f:
            for l in lines:
                seq = [f"[{masked[(r['line'], r['pos'])]}]" if (r["line"], r["pos"]) in masked else r["sign"]
                       for r in rows if r["line"] == l]
                f.write(f"{l}: {' '.join(seq)}\n")
        with open(HERE / f"blind_{part}.tsv", "w") as f:
            f.write("qid\tline\tpos\n")
            for _, o in sorted(qs, key=lambda x: x[1]["qid"]):
                if sel(o["line"]):
                    f.write(f"{o['qid']}\t{o['line']}\t{o['pos']}\n")
    print(f"scored {len(out)} letter positions; T {len(T)} (gain {T[-1]['gain']}..{T[0]['gain']}), D {len(D)}, R {len(R)}")


if __name__ == "__main__":
    main()

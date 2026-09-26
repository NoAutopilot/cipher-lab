#!/usr/bin/env python3
"""Decode ciphertext.txt (BnF fr.7129 f.268, Villeroy to Bongars, 2 Nov 1604) with keys/key_f275.tsv (Bongars cipher
no.3, fr.7129 f.275), token by token, and run the rule 3 control. VB-DECODE, 26 Sept 2026.

  python3 decode_f275.py --control        20 class-shuffled keys vs the real key, numbers only (run this first)
  python3 decode_f275.py                  write reading.txt (one line per cipher line; unknown signs as [?])
  python3 decode_f275.py --check          exit 1 if reading.txt is stale

Deterministic. Letters and syllables join into a run; a word code stands alone; unknown or empty values print [?]
and a null prints nothing. Score: tools/judge_plaintext.py's NgramModel on LANG_CORPORA['fr'] (fr16, Lettres de
Catherine de Medicis t.1) over the letters of the decode, mean log10 4-gram probability per letter.
The class shuffle permutes values within kind (letter values among letter signs, word values among word signs),
so coverage is identical by construction and only the letter stream can differ (the bCAS/AX-5799 lesson).
"""
import argparse
import importlib.util
import random
import re
import statistics
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
SEED = 20260926
N_SHUF = 20


def load_key():
    key = {}
    for line in open(HERE / "keys" / "key_f275.tsv", encoding="utf-8"):
        if line.startswith("#") or line.startswith("sign\t"):
            continue
        f = line.rstrip("\n").split("\t")
        key[f[0]] = {"value": f[1], "kind": f[2], "unclear": f[5]}
    return key


def load_cipher():
    lines = {}
    for line in open(HERE / "ciphertext.txt", encoding="utf-8"):
        if line.startswith("#") or line.startswith("side\t"):
            continue
        side, ln, pos, tok, _ = line.rstrip("\n").split("\t")
        lines.setdefault((side, int(ln)), []).append(tok)
    return [(k, lines[k]) for k in sorted(lines, key=lambda k: (k[0] != "r", k[1]))]


def decode_line(toks, key):
    out, run = [], ""
    for t in toks:
        row = key.get(t)
        if row is None or (row["value"] in ("", "?") and row["kind"] != "null"):
            v, kind = "[?]", "unknown"
        else:
            v, kind = row["value"], row["kind"]
        if kind == "null":
            continue
        if kind == "letter":
            run += v
        else:
            if run:
                out.append(run)
                run = ""
            out.append(v)
    if run:
        out.append(run)
    return " ".join(out)


def letters(text):
    return re.sub(r"[^a-z]", "", text.lower().replace("[?]", ""))


def shuffled(key, rnd):
    new = {k: dict(v) for k, v in key.items()}
    for kind in ("letter", "word"):
        signs = [k for k, v in key.items() if v["kind"] == kind]
        vals = [key[k]["value"] for k in signs]
        rnd.shuffle(vals)
        for k, v in zip(signs, vals):
            new[k]["value"] = v
    return new


def model():
    spec = importlib.util.spec_from_file_location("jp", ROOT / "tools" / "judge_plaintext.py")
    jp = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(jp)
    return jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])


def render(key):
    return [f"{s}{n}\t{decode_line(toks, key)}" for (s, n), toks in load_cipher()]


def control():
    key, m = load_key(), model()
    cipher = load_cipher()
    real_lines = [decode_line(t, key) for _, t in cipher]
    real = m.score(letters(" ".join(real_lines)))
    rnd = random.Random(SEED)
    shuf_keys = [shuffled(key, rnd) for _ in range(N_SHUF)]
    shuf = [m.score(letters(" ".join(decode_line(t, k) for _, t in cipher))) for k in shuf_keys]
    mu, sd = statistics.mean(shuf), statistics.pstdev(shuf)
    rank = 1 + sum(s > real for s in shuf)
    print(f"letters in decode: {len(letters(' '.join(real_lines)))}")
    print(f"real key score {real:.4f}; {N_SHUF} class-shuffled keys mean {mu:.4f} sd {sd:.4f} "
          f"min {min(shuf):.4f} max {max(shuf):.4f}; z {(real - mu) / sd:.2f}; rank {rank} of {N_SHUF + 1}")
    print("per line (z of the real line against the same line under the 20 shuffled keys):")
    for i, ((s, n), toks) in enumerate(cipher):
        r = letters(real_lines[i])
        if len(r) < 8:
            print(f"  {s}{n}: {len(r)} letters, too short")
            continue
        sl = [m.score(letters(decode_line(toks, k))) for k in shuf_keys]
        smu, ssd = statistics.mean(sl), statistics.pstdev(sl)
        print(f"  {s}{n}: letters {len(r)} real {m.score(r):.3f} shuffled {smu:.3f}+-{ssd:.3f} "
              f"z {(m.score(r) - smu) / ssd:.2f} rank {1 + sum(x > m.score(r) for x in sl)}")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--control", action="store_true")
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    if a.control:
        control()
        return
    text = "\n".join(render(load_key())) + "\n"
    target = HERE / "reading.txt"
    header = ("# Candidate decode of ciphertext.txt with keys/key_f275.tsv, generated by decode_f275.py (VB-DECODE,\n"
              "# 26 Sept 2026). Mechanical, ungraded here; see NOTES.md for grades. [?] = sign not in the key.\n")
    if a.check:
        cur = target.read_text(encoding="utf-8") if target.exists() else ""
        if cur != header + text:
            print("reading.txt is stale", file=sys.stderr)
            sys.exit(1)
        print("reading.txt current")
        return
    target.write_text(header + text, encoding="utf-8")
    print(f"wrote {target}")


if __name__ == "__main__":
    main()

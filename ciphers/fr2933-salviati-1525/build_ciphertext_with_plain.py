#!/usr/bin/env python3
"""Interleave the sign-run ciphertext with the plain-Italian boxes transcribed so far (SALV-PLAIN1, job 1a;
job 1b covers the second half). Walks the same eight-leaf, pos-ordered row generator as build_spec.py (same
f.57r line 17 pos>=15 drop), grouping into one output line per manuscript line: a maximal run of sign boxes
becomes "[" code^marks tokens "]"; each plain box becomes its transcribed word, continuation rows ("+") folded
into the word that started them, boxes with no legible ink ("<none>") dropped, and, for a leaf whose plain
boxes have not been transcribed yet, each stretch of plain boxes collapses to one "<untranscribed>" token
(never a per-box guess) rather than being silently skipped -- the reader can see where a real gap in the
context still is. No decoding: sign tokens are printed exactly as ciphertext_<leaf>.tsv already has them.

  python3 build_ciphertext_with_plain.py            writes ciphertext_with_plain.txt
  python3 build_ciphertext_with_plain.py --check     exits 1 if the committed file is stale (rule 7)
"""
import csv, os, sys

D = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(D, "ciphertext_with_plain.txt")
LEAVES = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")


def sign_rows():
    for lf in LEAVES:
        for x in csv.DictReader(open(os.path.join(D, f"ciphertext_{lf}.tsv")), delimiter="\t"):
            if lf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15:
                continue
            yield lf, x


def load_plain_boxes():
    path = os.path.join(D, "plain_boxes.tsv")
    boxes = {}  # (leaf, line, int_pos) -> word
    leaves_done = set()
    if not os.path.exists(path):
        return boxes, leaves_done
    for r in csv.DictReader(open(path), delimiter="\t"):
        leaves_done.add(r["leaf"])
        boxes[(r["leaf"], int(r["line"]), int(float(r["pos"])))] = r["word"]
    return boxes, leaves_done


def build():
    plain_boxes, leaves_done = load_plain_boxes()
    lines_out = []
    cur_key = None
    tokens = []
    sign_buf = []
    last_was_untranscribed = False

    def flush_sign():
        nonlocal sign_buf
        if sign_buf:
            tokens.append("[" + " ".join(sign_buf) + "]")
            sign_buf = []

    def flush_line():
        nonlocal tokens
        if cur_key is not None:
            lines_out.append((cur_key, " ".join(tokens)))
        tokens = []

    for lf, x in sign_rows():
        key = (lf, x["line"])
        if key != cur_key:
            flush_sign()
            flush_line()
            cur_key = key
            last_was_untranscribed = False
        pos = int(float(x["pos"]))
        if x["code"] != "_":
            last_was_untranscribed = False
            sign_buf.append(f"{x['code']}^{x['marks']}")
            continue
        flush_sign()
        if lf not in leaves_done:
            if not last_was_untranscribed:
                tokens.append("<untranscribed>")
                last_was_untranscribed = True
            continue
        last_was_untranscribed = False
        word = plain_boxes.get((lf, int(x["line"]), pos))
        if word is None or word == "+" or word == "<none>":
            continue
        tokens.append(word)
    flush_sign()
    flush_line()
    return lines_out


def main():
    lines_out = build()
    text = "\n".join(f"{lf} L{line}: {content}" for (lf, line), content in lines_out) + "\n"
    if "--check" in sys.argv:
        if not os.path.exists(OUT):
            print("STALE: ciphertext_with_plain.txt does not exist"); return 1
        old = open(OUT, encoding="utf-8").read()
        if old != text:
            print("STALE: committed ciphertext_with_plain.txt differs from plain_boxes.tsv + ciphertext_*.tsv")
            return 1
        print(f"ok: {len(lines_out)} manuscript lines"); return 0
    open(OUT, "w", encoding="utf-8").write(text)
    print(f"wrote {OUT}: {len(lines_out)} manuscript lines")
    return 0


if __name__ == "__main__":
    sys.exit(main())

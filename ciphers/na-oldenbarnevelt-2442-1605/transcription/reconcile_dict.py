#!/usr/bin/env python3
"""Reconcile passA.tsv/passB.tsv per block: difflib sequence-alignment (token content, not (block,line,
token_index) -- the two blind passes split lines/tokens differently almost from the start, so an index join
is wrong; confirmed by spot-checking common (block,line,token_index) keys 25 Sept 2026: most held two
different words, not a transcription variant of the same word) then, for a replace/mismatch, decode both
candidates under the digit key established from dictionary hits in Block A (a=4,e=8,i=3,o=7,u=2 --
secretario, Francisco, palabras, particulares, son, Dios all confirm it) and prefer whichever is a real word
in the es16 corpus wordlist. Where neither or both match, keeps pass A's token (marginally the clearer block
per both transcribers' own notes) at low confidence, flagged unresolved.

Writes reconciled tokens for one block to stdout (block, running index, raw_token, confidence, note).
"""
import argparse, difflib, re
from collections import defaultdict

KEY = {"4": "a", "8": "e", "3": "i", "7": "o", "2": "u"}


def decode(tok):
    return "".join(KEY.get(c, c) for c in tok)


def fold(w):
    return w.translate(str.maketrans("áéíóúñ", "aeioun"))


def load_wordset(corpus_path):
    text = open(corpus_path, encoding="utf-8").read().lower()
    words = re.findall(r"[a-záéíóúñ]+", text)
    return set(fold(w) for w in words if len(w) >= 2)


def load(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip()]
    h = rows[0]
    bi, li, ti, ri = h.index("block"), h.index("line"), h.index("token_index"), h.index("raw_token")
    data = rows[1:]
    data.sort(key=lambda r: (r[bi], int(r[li]), int(r[ti])))
    by_block = defaultdict(list)
    for r in data:
        by_block[r[bi]].append(r[ri])
    return by_block


def reconcile_block(a_toks, b_toks, wordset):
    sm = difflib.SequenceMatcher(None, a_toks, b_toks, autojunk=False)
    out = []
    for tag, i1, i2, j1, j2 in sm.get_opcodes():
        if tag == "equal":
            for k in range(i2 - i1):
                out.append((a_toks[i1 + k], "high", "agree"))
        elif tag == "replace":
            m = max(i2 - i1, j2 - j1)
            for k in range(m):
                av = a_toks[i1 + k] if i1 + k < i2 else None
                bv = b_toks[j1 + k] if j1 + k < j2 else None
                if av is None:
                    out.append((bv, "low", "B-only"))
                elif bv is None:
                    out.append((av, "low", "A-only"))
                else:
                    dA, dB = fold(decode(av.rstrip(".,'"))), fold(decode(bv.rstrip(".,'")))
                    inA, inB = dA in wordset, dB in wordset
                    if inA and not inB:
                        out.append((av, "medium", f"dict-pick-A(vs {bv!r})"))
                    elif inB and not inA:
                        out.append((bv, "medium", f"dict-pick-B(vs {av!r})"))
                    else:
                        out.append((av, "low", f"unresolved(A={av!r} B={bv!r})"))
        elif tag == "delete":
            for k in range(i1, i2):
                out.append((a_toks[k], "low", "A-only"))
        elif tag == "insert":
            for k in range(j1, j2):
                out.append((b_toks[k], "low", "B-only"))
    return out


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--corpus", default="corpus/es16-donquijote/donquijote1605_pg2000_body.txt")
    ap.add_argument("--blocks", default="A,B,C1")
    a = ap.parse_args()
    wordset = load_wordset(a.corpus)
    A = load("passA.tsv")
    B = load("passB.tsv")
    print("block\ttoken_index\traw_token\tconfidence\tnote")
    for block in a.blocks.split(","):
        rec = reconcile_block(A[block], B[block], wordset)
        for i, (tok, conf, note) in enumerate(rec, 1):
            print(f"{block}\t{i}\t{tok}\t{conf}\t{note}")


if __name__ == "__main__":
    main()

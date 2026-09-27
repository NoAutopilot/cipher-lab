#!/usr/bin/env python3
"""Compare the key's decode of a sibling cipher block with the clerk's interlinear decipherment (VB-KP, 27 Sept 2026).

  python3 compare_clerk.py CIPHER.tsv PLAIN.tsv --key ../keys/key_f275_v2.tsv

CIPHER.tsv: side/line/pos/token/agree (merge_passes.py output). PLAIN.tsv: line<TAB>clerk text (the merged plaintext).
Both sides are normalized to one convention before diffing (rule 3, PX-BRODEC lesson): lower case, '&' -> 'et',
letters a-z only, j->i, v->u (the key has no j/v column). Per line, the decode's letter stream (key values joined, word
codes spelled out, nulls dropped, unknown signs dropped) is aligned to the clerk's with difflib; agreement = matched
letters / clerk letters. Token level: a token whose whole decoded span sits inside a matched block is 'confirmed'.
Control: the same agreement under the 20 class-shuffled keys of decode_f275.py (same seed), mean and sd, so the real
number is read against what a wrong key of the same shape gets. Last, every single-token replace span is listed as
sign -> clerk letters (candidate key corrections, to be cited by folio and line).
Degenerate optimum named (README common tail): agreement over clerk letters rewards a decode that spells every letter;
a shuffled key has the same letter count, so the control, not the raw figure, is the test.
"""
import argparse
import collections
import difflib
import importlib.util
import random
import re
import statistics
from pathlib import Path

HERE = Path(__file__).resolve().parent
spec = importlib.util.spec_from_file_location("dec", HERE.parent / "decode_f275.py")
dec = importlib.util.module_from_spec(spec)
spec.loader.exec_module(dec)


def norm(s):
    s = s.lower().replace("&", "et").replace("j", "i").replace("v", "u")
    return re.sub(r"[^a-z]", "", s)


def token_values(toks, key):
    """(token, decoded letters) per token, following decode_f275.decode_line's rules."""
    out, dbl = [], False
    for t in toks:
        row = key.get(t)
        if row is None or (row["value"] in ("", "?") and row["kind"] not in ("null", "double")):
            out.append((t, ""))
            continue
        if row["kind"] == "null":
            out.append((t, ""))
            continue
        if row["kind"] == "double":
            dbl = True
            out.append((t, ""))
            continue
        v = norm(row["value"])
        if row["kind"] == "letter" and dbl:
            v, dbl = v * 2, False
        out.append((t, v))
    return out


def load(cipher, plain):
    lines = collections.OrderedDict()
    for ln in open(cipher, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("side\t"):
            continue
        s, n, p, t = ln.rstrip("\n").split("\t")[:4]
        lines.setdefault(int(n), []).append(t)
    clerk = {}
    for ln in open(plain, encoding="utf-8"):
        if ln.startswith("#") or ln.startswith("line\t") or not ln.strip():
            continue
        n, txt = ln.rstrip("\n").split("\t")[:2]
        clerk[int(n)] = txt
    return lines, clerk


def score(lines, clerk, key, detail=False):
    tot_m = tot_c = conf = valued = 0
    subs, per = [], []
    for n, toks in lines.items():
        tv = token_values(toks, key)
        d = "".join(v for _, v in tv)
        c = norm(clerk.get(n, ""))
        sm = difflib.SequenceMatcher(a=d, b=c, autojunk=False)
        matched = [False] * len(d)
        for blk in sm.get_matching_blocks():
            for k in range(blk.a, blk.a + blk.size):
                matched[k] = True
        m = sum(b.size for b in sm.get_matching_blocks())
        tot_m, tot_c = tot_m + m, tot_c + len(c)
        pos, spans = 0, []
        for t, v in tv:
            spans.append((t, pos, pos + len(v)))
            if v:
                valued += 1
                conf += all(matched[pos:pos + len(v)])
            pos += len(v)
        per.append((n, m, len(c), d, c))
        if detail:
            for op, i1, i2, j1, j2 in sm.get_opcodes():
                if op != "replace":
                    continue
                inside = [t for t, a, b in spans if a < i2 and b > i1]
                if len(inside) == 1:
                    subs.append((n, inside[0], d[i1:i2], c[j1:j2]))
    return tot_m / max(tot_c, 1), conf, valued, per, subs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("cipher")
    ap.add_argument("plain")
    ap.add_argument("--key", default=str(HERE.parent / "keys" / "key_f275_v2.tsv"))
    a = ap.parse_args()
    dec.KEY = Path(a.key)
    key = dec.load_key()
    lines, clerk = load(a.cipher, a.plain)
    rnd = random.Random(dec.SEED)
    shuf = [score(lines, clerk, dec.shuffled(key, rnd))[0] for _ in range(dec.N_SHUF)]
    real, conf, valued, per, subs = score(lines, clerk, key, detail=True)
    mu, sd = statistics.mean(shuf), statistics.pstdev(shuf)
    print(f"letter agreement with the clerk: real key {real:.3f}; {dec.N_SHUF} class-shuffled keys mean {mu:.3f} "
          f"sd {sd:.3f} max {max(shuf):.3f}; z {(real - mu) / sd:.2f}; rank {1 + sum(s > real for s in shuf)} of "
          f"{dec.N_SHUF + 1}")
    print(f"tokens with a key value: {valued}; confirmed by the clerk (whole span matched): {conf} "
          f"({100 * conf / max(valued, 1):.0f}%)")
    for n, m, lc, d, c in per:
        print(f"  line {n}: {m}/{lc} clerk letters matched ({100 * m / max(lc, 1):.0f}%)\n    decode: {d}\n    clerk:  {c}")
    print("single-token disagreements (line, sign, key gives, clerk has):")
    for n, t, dv, cv in subs:
        print(f"  {n}\t{t}\t{dv}\t{cv}")


if __name__ == "__main__":
    main()

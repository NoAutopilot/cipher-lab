#!/usr/bin/env python3
"""OLD-S10 (8 Oct 2026): decode and grade scan 10's cipher block (ff.63v/64r right page, block L10) with the fixed B/C1 key.

Same rules as scripts/decode_L457.py (PREREG_OLD-S10 items 5-7), whose functions it reuses:
reads transcription/reconciled_L10_OLDS10.tsv and the blind passes transcription/passK_OLDS10_L10_{A,B}.tsv.
Grade per cipher token: S when the token, normalised, is in the best-matching line of BOTH blind passes AND its decode is
in the es1600 + Don Quijote lexicon; M otherwise. No H, no C. Clear tokens reported, not graded.

  python3 scripts/decode_L10.py            write reading_L10.txt and reading_L10_tokens.tsv, print counts
  python3 scripts/decode_L10.py --check    exit 1 if either committed file differs from a fresh run
  python3 scripts/decode_L10.py --diff     per-sign A/B disagreement (PREREG item 3; agreement, not accuracy)
  python3 scripts/decode_L10.py --control  lexicon-hit share under all 120 vowel-map permutations (PREREG item 6)
  python3 scripts/decode_L10.py --depth    S share (words, digit tokens) and longest S stretch in digit tokens (item 7)
"""
import csv, itertools, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, ".."))
sys.path.insert(0, HERE)
import decode_L457 as D  # noqa: E402
from decode_L457 import norm_tok, lev, core, fold, best_line, ABBR  # noqa: E402

REC = os.path.join(T, "transcription/reconciled_L10_OLDS10.tsv")
PASS = os.path.join(T, "transcription/passK_OLDS10_L10_{}.tsv")
VOW = "23478"


def pass_lines(side):
    d = {}
    for r in csv.DictReader(open(PASS.format(side)), delimiter="\t"):
        if r["token"] not in ("EMPTY", "[del]"):
            d.setdefault(r["line"], []).append(norm_tok(r["token"]))
    return d


def rows():
    out = {}
    for r in csv.DictReader((l for l in open(REC) if not l.startswith("#")), delimiter="\t"):
        out.setdefault(r["line"], []).append(r["raw_token"])
    return out


def decode(tok, key):
    if ABBR.match(tok):
        return "V.S."
    return "".join(key.get(ch, ch) for ch in core(tok))


def base_key():
    k = dict(D.KEY)
    return k


def run(key=None, lex=None):
    key = key or base_key()
    lex = lex or D.lexicon()
    pa, pb = pass_lines("A"), pass_lines("B")
    toks_out = ["block\tline\ttoken_index\traw_token\tdecode\tcipher\tdigits\tin_A\tin_B\tin_lexicon\tgrade"]
    read, counts = [], Counter()
    for ln, toks in rows().items():
        normed = [norm_tok(core(t)) for t in toks if t != "[del]"]
        ba, bb = best_line(normed, pa), best_line(normed, pb)
        words = []
        for i, t in enumerate(toks, 1):
            if t == "[del]":
                words.append("[del]")
                continue
            cipher = bool(re.search(r"\d", t))
            dec = decode(t, key) if cipher else t
            n = norm_tok(core(t))
            ia, ib = n in ba, n in bb
            inlex = dec == "V.S." or fold(re.sub(r"[^a-zñ]", "", dec.lower())) in lex
            g = ("S" if (ia and ib and inlex) else "M") if cipher else "clear"
            nd = sum(c in VOW for c in core(t)) if cipher else 0
            counts[g] += 1
            words.append(dec.upper() if cipher else dec)
            toks_out.append(f"L10\t{ln}\t{i}\t{t}\t{dec}\t{int(cipher)}\t{nd}\t{int(ia)}\t{int(ib)}\t{int(inlex)}\t{g}")
        read.append(f"{ln}\t{' '.join(words)}")
    ncip = counts["S"] + counts["M"]
    head = ["# OLD-S10 reading of scan 10 (ff.63v/64r right page), fixed B/C1 key; cipher words in CAPITALS, clear words as written.",
            f"# cipher tokens {ncip}: H 0, C 0, S {counts['S']}, M {counts['M']}, I 0 (clear tokens {counts['clear']})."]
    return "\n".join(toks_out) + "\n", "\n".join(head + read) + "\n", counts


def lexshare(key, lex):
    hit = n = 0
    for toks in rows().values():
        for t in toks:
            if t == "[del]" or not re.search(r"\d", t) or ABBR.match(t):
                continue
            n += 1
            hit += fold(re.sub(r"[^a-zñ]", "", decode(t, key).lower())) in lex
    return hit / max(n, 1), n


def control():
    lex = D.lexicon()
    k0 = base_key()
    vals = [k0[d] for d in VOW]
    res = []
    for perm in itertools.permutations(vals):
        k = dict(k0)
        k.update(dict(zip(VOW, perm)))
        res.append((lexshare(k, lex)[0], perm == tuple(vals), "".join(f"{d}={v}" for d, v in zip(VOW, perm))))
    res.sort(reverse=True)
    tgt = [r for r in res if r[1]][0]
    others = [r[0] for r in res if not r[1]]
    rank = 1 + sum(o > tgt[0] for o in others)
    n = lexshare(k0, lex)[1]
    print(f"cipher tokens scored (V.S. excluded): {n}")
    print(f"fixed key {tgt[2]}: lexicon-hit share {tgt[0]:.3f}; rank {rank} of {len(res)}")
    print(f"119 permutations: mean {sum(others)/len(others):.3f}, max {max(others):.3f}; top three: "
          + "; ".join(f"{r[2]} {r[0]:.3f}" for r in res[:3]))


def depth():
    rs = list(csv.DictReader(open(os.path.join(T, "reading_L10_tokens.tsv")), delimiter="\t"))
    cip = [r for r in rs if r["cipher"] == "1"]
    dg = Counter()
    best, cur, words, bw = 0, 0, [], []
    for r in rs:
        if r["cipher"] != "1":
            if cur:
                words.append(r["decode"])
            continue
        n = int(r["digits"])
        dg[r["grade"]] += n
        if r["grade"] == "S":
            cur += n
            words.append(r["decode"])
            if cur > best:
                best, bw = cur, list(words)
        else:
            cur, words = 0, []
    wg = Counter(r["grade"] for r in cip)
    nd = sum(dg.values())
    print(f"cipher words {len(cip)} {dict(wg)} (S {wg['S']/max(len(cip),1):.1%}); digit tokens {nd} {dict(dg)} "
          f"(S {dg['S']/max(nd,1):.1%}); longest S stretch {best} digit tokens: {' '.join(bw)}")


def diff():
    def lines(side):
        d = {}
        for r in csv.DictReader(open(PASS.format(side)), delimiter="\t"):
            if r["token"] != "EMPTY":
                d[r["line"]] = d.get(r["line"], "") + norm_tok(r["token"])
        return d
    a, b = lines("A"), lines("B")
    e = n = 0.0
    for k in sorted(set(a) | set(b)):
        e += lev(a.get(k, ""), b.get(k, ""))
        n += (len(a.get(k, "")) + len(b.get(k, ""))) / 2
    print(f"L10\tedits {e:.0f}\tmean_len {n:.0f}\tdisagreement {100*e/max(n,1):.1f}%")


def main():
    if "--diff" in sys.argv:
        return diff()
    if "--control" in sys.argv:
        return control()
    if "--depth" in sys.argv:
        return depth()
    tok, read, counts = run()
    paths = [os.path.join(T, "reading_L10_tokens.tsv"), os.path.join(T, "reading_L10.txt")]
    if "--check" in sys.argv:
        stale = [p for p, new in zip(paths, (tok, read)) if not os.path.exists(p) or open(p).read() != new]
        if stale:
            print("STALE:", ", ".join(os.path.relpath(p, T) for p in stale))
            sys.exit(1)
        print("decode_L10 --check: committed reading matches a fresh run;", dict(counts))
        return
    for p, new in zip(paths, (tok, read)):
        open(p, "w").write(new)
    print(dict(counts))


if __name__ == "__main__":
    main()

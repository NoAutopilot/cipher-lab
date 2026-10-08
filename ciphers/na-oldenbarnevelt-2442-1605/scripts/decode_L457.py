#!/usr/bin/env python3
"""OLD-SIBS (8 Oct 2026): decode and grade leaves 004/005/007 of invnr 2442 with the fixed B/C1 key.

Reads transcription/reconciled_L457_OLDSIBS.tsv (every token on each reconciled line) and the two blind passes
transcription/passJ_OLDSIBS_<leaf>_{A,B}.tsv. Cipher tokens are those carrying a digit. Key: digit_key.json
(2=u 3=i 4=a 7=o 8=e) plus the folder's settled conventions 5=s, 6=b (PREREG_OLD-PASS2 item 2). `2s^a`, `2s^o`,
`2s.` are the abbreviation V.S. (vuestra senoria) and decode to "V.S.".

Grade per cipher token (brief step 5; PREREG_OLD-SIBS item 4): S when (a) the token, normalised, occurs in the
best-matching line of BOTH blind passes and (b) its decode is a word of the lexicon (tools/data/es1600 +
the folder's Don Quijote corpus, words seen >= 2 times, u/v and i/j/y folded); M otherwise. No H, no C. Clear
tokens (no digit) are reported, not graded.

  python3 scripts/decode_L457.py            write reading_L457.txt and reading_L457_tokens.tsv
  python3 scripts/decode_L457.py --check    exit 1 if either committed file differs from a fresh run
"""
import csv, gzip, glob, json, os, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.normpath(os.path.join(HERE, ".."))
REPO = os.path.normpath(os.path.join(T, "..", ".."))
sys.path.insert(0, os.path.join(T, "transcription"))
from diff_pass2 import norm_tok, lev  # noqa: E402

KEY = dict(json.load(open(os.path.join(T, "digit_key.json"))))
KEY.update({"5": "s", "6": "b"})
ABBR = re.compile(r"^(2s|25)(\^a|\^o|\.)?[,.]?$")


def fold(w):
    return w.replace("v", "u").replace("j", "i").replace("y", "i")


def lexicon():
    c = Counter()
    files = glob.glob(os.path.join(REPO, "tools/data/es1600/*.txt.gz"))
    for f in files:
        c.update(re.findall(r"[a-zñ]+", gzip.open(f, "rt", encoding="utf-8", errors="ignore").read().lower()))
    q = os.path.join(T, "corpus/es16-donquijote/donquijote1605_pg2000_body.txt")
    c.update(re.findall(r"[a-zñ]+", open(q, encoding="utf-8", errors="ignore").read().lower()))
    return {fold(w) for w, n in c.items() if n >= 2}


def core(tok):
    t = tok.lstrip("^").replace("~", "")
    return re.sub(r"[,.;:/\-]", "", t)


def decode(tok):
    if ABBR.match(tok):
        return "V.S."
    return "".join(KEY.get(ch, ch) for ch in core(tok))


def pass_lines(leaf, side):
    d = {}
    for r in csv.DictReader(open(os.path.join(T, f"transcription/passJ_OLDSIBS_{leaf}_{side}.tsv")), delimiter="\t"):
        if r["token"] != "EMPTY":
            d.setdefault(r["line"], []).append(norm_tok(r["token"]))
    return d


def best_line(target, plines):
    s = "".join(target)
    best, bd = [], 1e9
    for toks in plines.values():
        x = "".join(toks)
        dd = lev(s, x) / max(len(s), 1)
        if dd < bd:
            best, bd = toks, dd
    return best if bd < 0.6 else []


def run():
    lex = lexicon()
    rows = [r for r in csv.DictReader((l for l in open(os.path.join(T, "transcription/reconciled_L457_OLDSIBS.tsv"))
                                       if not l.startswith("#")), delimiter="\t")]
    passes = {(lf, s): pass_lines(lf, s) for lf in ("L4", "L5", "L7") for s in "AB"}
    lines = {}
    for r in rows:
        lines.setdefault((r["block"], r["line"]), []).append(r["raw_token"])
    out_tok, out_read = ["block\tline\ttoken_index\traw_token\tdecode\tcipher\tin_A\tin_B\tin_lexicon\tgrade"], []
    counts = Counter()
    for (blk, ln), toks in lines.items():
        normed = [norm_tok(core(t)) for t in toks if t != "[del]"]
        ba, bb = best_line(normed, passes[(blk, "A")]), best_line(normed, passes[(blk, "B")])
        words = []
        for i, t in enumerate(toks, 1):
            if t == "[del]":
                words.append("[del]")
                continue
            cipher = bool(re.search(r"\d", t))
            dec = decode(t) if cipher else t
            n = norm_tok(core(t))
            ia, ib = n in ba, n in bb
            inlex = dec == "V.S." or fold(re.sub(r"[^a-zñ]", "", dec.lower())) in lex
            g = ("S" if (ia and ib and inlex) else "M") if cipher else "clear"
            counts[g] += 1
            words.append(dec.upper() if cipher else dec)
            out_tok.append(f"{blk}\t{ln}\t{i}\t{t}\t{dec}\t{int(cipher)}\t{int(ia)}\t{int(ib)}\t{int(inlex)}\t{g}")
        out_read.append(f"{ln}\t{' '.join(words)}")
    ncip = counts["S"] + counts["M"]
    head = [f"# OLD-SIBS reading of leaves 004/005/007, fixed B/C1 key; cipher words in CAPITALS, clear words as written.",
            f"# cipher tokens {ncip}: H 0, C 0, S {counts['S']}, M {counts['M']}, I 0 (clear tokens {counts['clear']})."]
    return "\n".join(out_tok) + "\n", "\n".join(head + out_read) + "\n", counts


def main():
    tok, read, counts = run()
    paths = [os.path.join(T, "reading_L457_tokens.tsv"), os.path.join(T, "reading_L457.txt")]
    if "--check" in sys.argv:
        stale = [p for p, new in zip(paths, (tok, read)) if not os.path.exists(p) or open(p).read() != new]
        if stale:
            print("STALE:", ", ".join(os.path.relpath(p, T) for p in stale))
            sys.exit(1)
        print("decode_L457 --check: committed reading matches a fresh run;", dict(counts))
        return
    for p, new in zip(paths, (tok, read)):
        open(p, "w").write(new)
    print(dict(counts))


if __name__ == "__main__":
    main()

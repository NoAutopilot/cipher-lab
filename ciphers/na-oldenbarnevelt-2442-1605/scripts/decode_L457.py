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

OLD-O2 (10 Oct 2026, transcription/PREREG_OLD-O2.md): the default now reads transcription/reconciled_L457_OLDO2.tsv,
grades L4/L7 against the masked-crop blind passes transcription/passL_OLDO2_{L4,L7}_{A,B}.tsv and L5 against its
OLD-SIBS passes, with the OLD-O4 S normaliser (v->r, (->l on passes and reconciled tokens alike, S test only), and also
writes transcription/reading_L457_cipher_only.txt (judge input: cipher decodes, V.S. dropped, u/v i/j/y folded).
  --norm sibs   OLD-SIBS's registered grading (OLDSIBS reconciliation, passJ passes, no fold): prints counts, writes nothing
  --decomp      L4/L7 graded against the OLD-SIBS passes with the OLD-O4 normaliser (notation vs crop effect; prints only)
  --diff        per-sign A/B disagreement of the OLD-O2 passes per leaf (PREREG_OLD-O2 item 4)
  --control     lexicon-hit share under all 120 vowel-map permutations, L4+L7 cipher tokens (PREREG item 7a)
  --scontrol    S share under all 120 vowel-map permutations, L4+L7 (PREREG item 7b)
  --depth       digit-token S share per leaf, longest contiguous S stretch, and the AD with every M word a liberty (item 8)
"""
import csv, gzip, glob, itertools, json, math, os, re, sys
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


MODE = "sibs" if "sibs" in sys.argv else "o4"
VOW = "23478"


def sn(t, mode=None):
    """S-test normaliser: norm_tok, then (OLD-O4, default) v->r and (->l, alike on passes and reconciled tokens."""
    t = norm_tok(t)
    return t.replace("v", "r").replace("(", "l") if (mode or MODE) == "o4" else t


def pass_file(leaf, side, which):
    if which == "O2" and leaf in ("L4", "L7"):
        return os.path.join(T, f"transcription/passL_OLDO2_{leaf}_{side}.tsv")
    return os.path.join(T, f"transcription/passJ_OLDSIBS_{leaf}_{side}.tsv")


def pass_lines(leaf, side, which="SIBS", mode=None):
    d = {}
    for r in csv.DictReader(open(pass_file(leaf, side, which)), delimiter="\t"):
        if r["token"] not in ("EMPTY", "[del]"):
            d.setdefault(r["line"], []).append(sn(r["token"], mode))
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


def rec_lines(which):
    f = "reconciled_L457_OLDSIBS.tsv" if which == "SIBS" else "reconciled_L457_OLDO2.tsv"
    rows = [r for r in csv.DictReader((l for l in open(os.path.join(T, "transcription", f)) if not l.startswith("#")),
                                      delimiter="\t")]
    lines = {}
    for r in rows:
        lines.setdefault((r["block"], r["line"]), []).append(r["raw_token"])
    return lines


def tokens(which_rec="O2", which_pass="O2", mode=None, key=None, lex=None, leaves=("L4", "L5", "L7")):
    """Yield (block, line, index, raw, decode, cipher, digits, in_A, in_B, in_lexicon, grade) per token."""
    key = key or KEY
    lex = lex if lex is not None else lexicon()
    passes = {(lf, s): pass_lines(lf, s, which_pass, mode) for lf in leaves for s in "AB"}
    for (blk, ln), toks in rec_lines(which_rec).items():
        if blk not in leaves:
            continue
        normed = [sn(core(t), mode) for t in toks if t != "[del]"]
        ba, bb = best_line(normed, passes[(blk, "A")]), best_line(normed, passes[(blk, "B")])
        for i, t in enumerate(toks, 1):
            if t == "[del]":
                yield (blk, ln, i, t, "[del]", False, 0, False, False, False, "del")
                continue
            cipher = bool(re.search(r"\d", t))
            dec = (("V.S." if ABBR.match(t) else "".join(key.get(ch, ch) for ch in core(t))) if cipher else t)
            n = sn(core(t), mode)
            ia, ib = n in ba, n in bb
            inlex = dec == "V.S." or fold(re.sub(r"[^a-zñ]", "", dec.lower())) in lex
            g = ("S" if (ia and ib and inlex) else "M") if cipher else "clear"
            nd = sum(c in VOW for c in core(t)) if cipher else 0
            yield (blk, ln, i, t, dec, cipher, nd, ia, ib, inlex, g)


def run():
    out_tok = ["block\tline\ttoken_index\traw_token\tdecode\tcipher\tdigits\tin_A\tin_B\tin_lexicon\tgrade"]
    out_read, cur, words, counts, conly = [], None, [], Counter(), []
    for (blk, ln, i, t, dec, cipher, nd, ia, ib, inlex, g) in tokens():
        if (blk, ln) != cur:
            if cur:
                out_read.append(f"{cur[1]}\t{' '.join(words)}")
            cur, words = (blk, ln), []
        if g == "del":
            words.append("[del]")
            continue
        counts[g] += 1
        words.append(dec.upper() if cipher else dec)
        if cipher and dec != "V.S.":
            w = fold(re.sub(r"[^a-zñ ]", "", dec.lower()))
            if w:
                conly.append(w)
        out_tok.append(f"{blk}\t{ln}\t{i}\t{t}\t{dec}\t{int(cipher)}\t{nd}\t{int(ia)}\t{int(ib)}\t{int(inlex)}\t{g}")
    out_read.append(f"{cur[1]}\t{' '.join(words)}")
    ncip = counts["S"] + counts["M"]
    head = ["# OLD-SIBS reading of leaves 004/005/007, fixed B/C1 key; cipher words in CAPITALS, clear words as written.",
            "# OLD-O2 grades: L4/L7 reconciled again and tested against the masked-crop passes (passL_OLDO2), L5 against passJ;"
            " S normaliser OLD-O4 (v->r, (->l).",
            f"# cipher tokens {ncip}: H 0, C 0, S {counts['S']}, M {counts['M']}, I 0 (clear tokens {counts['clear']})."]
    return ("\n".join(out_tok) + "\n", "\n".join(head + out_read) + "\n", " ".join(conly) + "\n", counts)


def sibs():
    c = Counter(g for *_, g in tokens("SIBS", "SIBS", "sibs") if g != "del")
    print("norm sibs (OLD-SIBS registered grading):", dict(c), "(not written)")


def decomp():
    for which, lab in (("SIBS", "OLD-SIBS passes"), ("O2", "OLD-O2 masked passes")):
        rs = [r for r in tokens("O2", which, "o4", leaves=("L4", "L7")) if r[5]]
        d = Counter(); dg = Counter()
        for r in rs:
            d[r[0], r[10]] += 1; dg[r[0], r[10]] += r[6]
        for lf in ("L4", "L7"):
            nd = dg[lf, "S"] + dg[lf, "M"]
            print(f"{lab:22s} {lf}: words S {d[lf,'S']} M {d[lf,'M']}; digit S {dg[lf,'S']}/{nd} ({dg[lf,'S']/max(nd,1):.1%})")


def diff():
    def lines(leaf, side):
        d = {}
        for r in csv.DictReader(open(pass_file(leaf, side, "O2")), delimiter="\t"):
            if r["token"] != "EMPTY":
                d[r["line"]] = d.get(r["line"], "") + sn(r["token"], "o4")
        return d
    te = tn = 0.0
    for lf in ("L4", "L7"):
        a, b = lines(lf, "A"), lines(lf, "B")
        e = n = 0.0
        for k in sorted(set(a) | set(b)):
            e += lev(a.get(k, ""), b.get(k, ""))
            n += (len(a.get(k, "")) + len(b.get(k, ""))) / 2
        te += e; tn += n
        print(f"{lf}\tedits {e:.0f}\tmean_len {n:.0f}\tdisagreement {100*e/max(n,1):.1f}%")
    print(f"pooled\tedits {te:.0f}\tmean_len {tn:.0f}\tdisagreement {100*te/max(tn,1):.1f}%")


def perm_control(stat):
    lex = lexicon()
    base = list(tokens("O2", "O2", "o4", lex=lex, leaves=("L4", "L7")))
    items = [(r[3], r[7] and r[8]) for r in base if r[5] and not ABBR.match(r[3])]
    vals = [KEY[d] for d in VOW]
    res = []
    for perm in itertools.permutations(vals):
        k = dict(KEY); k.update(dict(zip(VOW, perm)))
        hit = sum((m or stat == "lex") and fold(re.sub(r"[^a-zñ]", "", "".join(k.get(ch, ch) for ch in core(t)).lower())) in lex
                  for t, m in items)
        res.append((hit / len(items), perm == tuple(vals), "".join(f"{d}={v}" for d, v in zip(VOW, perm))))
    res.sort(reverse=True)
    tgt = [r for r in res if r[1]][0]
    others = [r[0] for r in res if not r[1]]
    rank = 1 + sum(o > tgt[0] for o in others)
    name = "lexicon-hit share" if stat == "lex" else "S share"
    print(f"{name} control, L4+L7 cipher tokens scored (V.S. excluded): {len(items)}, in both passes: {sum(m for _, m in items)}")
    print(f"fixed key {tgt[2]}: {name} {tgt[0]:.3f}; rank {rank} of {len(res)}")
    print(f"119 permutations: mean {sum(others)/len(others):.3f}, max {max(others):.3f}; top three: "
          + "; ".join(f"{r[2]} {r[0]:.3f}" for r in res[:3]))


def depth():
    rs = list(csv.DictReader(open(os.path.join(T, "reading_L457_tokens.tsv")), delimiter="\t"))
    for lf in ("L4", "L5", "L7", None):
        sub = [r for r in rs if lf is None or r["block"] == lf]
        dg, wg = Counter(), Counter()
        best, cur, words, bw = 0, 0, [], []
        for r in sub:
            if r["cipher"] != "1":
                if cur and r["grade"] == "clear":
                    words.append(r["decode"])
                continue
            n = int(r["digits"]); dg[r["grade"]] += n; wg[r["grade"]] += 1
            if r["grade"] == "S":
                cur += n; words.append(r["decode"])
                if cur > best:
                    best, bw = cur, list(words)
            else:
                cur, words = 0, []
        nd = dg["S"] + dg["M"]
        hk = 6.91 + 2.32 * wg["M"]
        ad = 1.5 * hk / 1.83
        print(f"{lf or 'L4+L5+L7'}: cipher words S {wg['S']} M {wg['M']}; digit tokens {nd}, S {dg['S']} ({dg['S']/max(nd,1):.1%}); "
              f"longest S stretch {best} digits [{' '.join(bw)}]; AD with M liberties {ad:.0f} digits (H(K) {hk:.1f} bits); floor 24.2")


def main():
    if MODE == "sibs":
        return sibs()
    for flag, fn in (("--decomp", decomp), ("--diff", diff), ("--depth", depth),
                     ("--control", lambda: perm_control("lex")), ("--scontrol", lambda: perm_control("S"))):
        if flag in sys.argv:
            return fn()
    tok, read, conly, counts = run()
    paths = [os.path.join(T, "reading_L457_tokens.tsv"), os.path.join(T, "reading_L457.txt"),
             os.path.join(T, "transcription/reading_L457_cipher_only.txt")]
    if "--check" in sys.argv:
        stale = [p for p, new in zip(paths, (tok, read, conly)) if not os.path.exists(p) or open(p).read() != new]
        if stale:
            print("STALE:", ", ".join(os.path.relpath(p, T) for p in stale))
            sys.exit(1)
        print("decode_L457 --check: committed reading matches a fresh run;", dict(counts))
        return
    for p, new in zip(paths, (tok, read, conly)):
        open(p, "w").write(new)
    print(dict(counts))


if __name__ == "__main__":
    main()

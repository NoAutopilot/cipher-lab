#!/usr/bin/env python3
"""Phrase-crib placement of a writer-matched clear corpus into R1953's U-runs (PREREG-HELFAGEL.md, D2-HELFAGEL, 5 Oct 2026).

  python3 key_rebuild/phrase_crib.py --corpus key_rebuild/fagel_corpus_H.txt [--out key_rebuild/phrase_crib_output.txt] [--check]

Steps (PREREG sections 2-6): normalize; cribs = word n-grams n=2..8 seen at >=2 positions, >=8 letters; place each crib on the
R1953 token sequence (first and last token keyed, >=1 U inside, keyed tokens match whole values, a U token takes 1..6 letters);
a placement counts when keyed letters m >= (k*log2(2000)+20)/3.2; a code is proposed when >=2 independent counted placements
give it the same value and none gives another. Controls: C1 fr18 slices of equal word count (Random(5177), 5 offsets), C2 U-code
label shuffles (Random(1953), 20), C3 known-answer folds over keyed codes 801+ (Random(4369), 10 folds). --check re-runs and
exits 1 if the committed output differs.
"""
import argparse, gzip, math, random, re, sys, unicodedata
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET = HERE.parent
TOKENS = TARGET / "key_r4369" / "reading_R1953_tokens.tsv"
REPO = TARGET.parent.parent
FR18 = ["memoiresdemonsie01torc.txt.gz", "memoiresdemonsie02torc.txt.gz", "mmoiresduducde01invill.txt.gz",
        "mmoiresduducde02vill.txt.gz", "mmoiresetlettre01margoog.txt.gz", "lagazettedefran01unkngoog.txt.gz"]
V, R, MAXU = 2000, 3.2, 6
BREAK = None


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    return "".join(ch for ch in s if "a" <= ch <= "z")


def load_tokens():
    toks = []
    for ln in TOKENS.read_text().splitlines()[1:]:
        f = ln.split("\t")
        code, val, grade = f[2], f[4] if len(f) > 4 else "", f[5] if len(f) > 5 else "U"
        if grade in ("H", "S"):
            v = norm(val)
            toks.append((code, "K" if v else "X", v))  # X: keyed but no letters (e.g. a digit) -> break
        elif grade == "U":
            toks.append((code, "U", ""))
        else:
            toks.append((code, "X", ""))  # M and anything else: break
    return toks


def words_of(text):
    """Corpus text -> list of words; a line '#BREAK' or a token '|' marks a phrase break."""
    out = []
    for w in re.split(r"\s+", text):
        if not w:
            continue
        if w == "|":
            out.append(BREAK)
            continue
        n = norm(w)
        if n:
            out.append(n)
    return out


def cribs_of(words):
    pos = defaultdict(set)
    for n in range(2, 9):
        for i in range(len(words) - n + 1):
            g = words[i:i + n]
            if BREAK in g:
                continue
            s = "".join(g)
            if len(s) >= 8:
                pos[s].add(i)
    return sorted(s for s, p in pos.items() if len(p) >= 2)


def place(crib, toks):
    """Yield counted placements: (i, j, codes tuple, {code: value})."""
    L = len(crib)
    for i, (c0, cl0, v0) in enumerate(toks):
        if cl0 != "K" or not crib.startswith(v0):
            continue
        ends = defaultdict(list)  # j -> list of segmentations (dict pos->substr)

        def dfs(t, p, seg, nu):
            if p == L:
                if toks[t - 1][1] == "K" and nu > 0:
                    ends[t - 1].append(dict(seg))
                return
            if t >= len(toks):
                return
            code, cl, v = toks[t]
            if cl == "K":
                if crib.startswith(v, p):
                    dfs(t + 1, p + len(v), seg, nu)
            elif cl == "U":
                for ln in range(1, MAXU + 1):
                    if p + ln > L:
                        break
                    seg[t] = crib[p:p + ln]
                    dfs(t + 1, p + ln, seg, nu + 1)
                    del seg[t]

        dfs(i + 1, len(v0), {}, 0)
        for j, segs in ends.items():
            upos = sorted(segs[0])
            k = len(upos)
            m = sum(len(toks[t][2]) for t in range(i, j + 1) if toks[t][1] == "K")
            if m < (k * math.log2(V) + 20) / R:
                continue
            det = {}
            ok_codes = {}
            for t in upos:
                vals = {s[t] for s in segs}
                if len(vals) == 1:
                    det.setdefault(toks[t][0], set()).add(vals.pop())
            for code, vs in det.items():
                if len(vs) == 1:
                    ok_codes[code] = next(iter(vs))
            yield (i, j, tuple(toks[t][0] for t in range(i, j + 1)), ok_codes)


def propose(cribs, toks):
    by_code = defaultdict(list)  # code -> [(value, i, j, codes, crib)]
    nplace = 0
    for c in cribs:
        for (i, j, codes, det) in place(c, toks):
            nplace += 1
            for code, v in det.items():
                by_code[code].append((v, i, j, codes, c))
    out = {}
    for code, lst in by_code.items():
        vals = {x[0] for x in lst}
        if len(vals) != 1:
            continue
        indep = []
        for x in lst:
            if all((x[2] < y[1] or y[2] < x[1]) and x[3] != y[3] for y in indep):
                indep.append(x)
        if len(indep) >= 2:
            out[code] = (lst[0][0], indep)
    return out, nplace


def fr18_words():
    ws = []
    for f in FR18:
        with gzip.open(REPO / "tools" / "data" / "fr18" / f, "rt", errors="replace") as fh:
            ws.extend(words_of(fh.read()))
    return [w for w in ws if w is not BREAK]


def run(corpus_path):
    lines = []
    P = lines.append
    toks = load_tokens()
    hw = words_of(Path(corpus_path).read_text())
    nwords = sum(1 for w in hw if w is not BREAK)
    hcribs = cribs_of(hw)
    P(f"# phrase_crib.py (PREREG-HELFAGEL). corpus H: {nwords} words, {len(hcribs)} cribs; R1953 tokens {len(toks)} "
      f"(K {sum(t[1]=='K' for t in toks)}, U {sum(t[1]=='U' for t in toks)}, break {sum(t[1]=='X' for t in toks)})")
    # C1
    fw = fr18_words()
    rng = random.Random(5177)
    c1 = []
    for s in range(5):
        off = rng.randrange(len(fw) - nwords)
        cr = cribs_of(fw[off:off + nwords])
        prop, npl = propose(cr, toks)
        c1.append(len(prop))
        P(f"C1 slice {s} offset {off}: cribs {len(cr)}, counted placements {npl}, S = {len(prop)} "
          + " ".join(f"{k}={v[0]}" for k, v in sorted(prop.items())))
    c1m = sum(c1) / len(c1)
    P(f"C1 mean S = {c1m:.2f} (gate <= 1: {'PASS' if c1m <= 1 else 'FAIL'})")
    # C2
    rng = random.Random(1953)
    upos = [n for n, t in enumerate(toks) if t[1] == "U"]
    ucodes = [toks[n][0] for n in upos]
    c2 = []
    for s in range(20):
        sh = ucodes[:]
        rng.shuffle(sh)
        t2 = list(toks)
        for n, c in zip(upos, sh):
            t2[n] = (c, "U", "")
        c2.append(len(propose(hcribs, t2)[0]))
    c2s = sorted(c2)
    c2p95 = c2s[math.ceil(0.95 * len(c2s)) - 1]
    P(f"C2 code-shuffle x20: S values {c2}; mean {sum(c2)/20:.2f}, p95 {c2p95}")
    # C3
    rng = random.Random(4369)
    kcodes = sorted({t[0] for t in toks if t[1] == "K" and t[0].isdigit() and int(t[0]) >= 801})
    rng.shuffle(kcodes)
    truth = {}
    for t in toks:
        if t[1] == "K":
            truth.setdefault(t[0], t[2])
    tot_p = tot_ok = 0
    for f in range(10):
        held = set(kcodes[f::10])
        t3 = [(c, "U", "") if (cl == "K" and c in held) else (c, cl, v) for (c, cl, v) in toks]
        prop, _ = propose(hcribs, t3)
        hp = {c: v for c, v in prop.items() if c in held}
        ok = sum(1 for c, v in hp.items() if v[0] == truth[c])
        tot_p += len(hp)
        tot_ok += ok
    P(f"C3 known-answer, {len(kcodes)} keyed codes 801+ in 10 folds: proposals for held-out codes {tot_p}, correct {tot_ok}")
    # Target
    prop, npl = propose(hcribs, toks)
    P(f"TARGET: counted placements {npl}, S = {len(prop)}")
    for code, (v, indep) in sorted(prop.items()):
        P(f"  code {code} -> {v}: " + "; ".join(f"crib '{x[4]}' tokens {x[1]}-{x[2]}" for x in indep))
    accept = c1m <= 1 and len(prop) > c2p95 and len(prop) > c1m
    P(f"DECISION (PREREG 7): C1 {'pass' if c1m <= 1 else 'FAIL'}; target S {len(prop)} vs C2 p95 {c2p95} and C1 mean {c1m:.2f}"
      f" -> {'ACCEPT values (grade S, key_rebuild only)' if accept else 'no values'}")
    return "\n".join(lines) + "\n"


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--corpus", default=str(HERE / "fagel_corpus_H.txt"))
    ap.add_argument("--out", default=str(HERE / "phrase_crib_output.txt"))
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    txt = run(a.corpus)
    if a.check:
        old = Path(a.out).read_text() if Path(a.out).exists() else ""
        if old != txt:
            print("STALE: committed output differs", file=sys.stderr)
            sys.exit(1)
        print("up to date")
        return
    Path(a.out).write_text(txt)
    print(txt, end="")


if __name__ == "__main__":
    main()

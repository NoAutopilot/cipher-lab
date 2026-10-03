#!/usr/bin/env python3
"""Pre-registered names test (A2-GRA6, 3 Oct 2026; NOTES.md "fr.3019 no.31 (f.84) as a name and topic source").

Does any f.30 open (U) code's set of positions fit a name read on fr.3019 f.84 better than letter-shuffled names?

  python3 f84_names_test.py --names f84_names.tsv [--reps 1000] [--power-only] [--out f84_names_test.tsv]

Statistic B(c,w): every occurrence of code c in the f.30 extended token stream is replaced by w; per occurrence,
LL(window with w) - LL(window with c deleted) - LL(w alone), window 6 chars each side, add-0.5 char 4-gram model on
tools/data/fr16; B = mean over occurrences. Real = max_w B(c,w); control = 1000 replicates of max_w B(c, shuffle(w)).
Gate: real above the control's 99th percentile. Power control first: VOVS, QVIL, POVR, 5 occurrences each masked
(seed 0) as pseudo-codes, the word added to the names; passes if the word is the top candidate and clears the gate.
"""
import argparse, gzip, math, random, re, sys
from collections import Counter, defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent
DATA = HERE.parent.parent / "tools" / "data" / "fr16"
W = 6
N = 4
CODES = ["B8", "HASH", "v", "CROSSp", "INF"]
POWER_WORDS = ["VOVS", "QVIL", "POVR"]


def norm(t):
    t = t.upper().replace("U", "V").replace("J", "I")
    return re.sub(r"[^A-Z]", "", t)


class LM:
    def __init__(self):
        txt = ""
        for f in sorted(DATA.glob("*.txt.gz")):
            txt += norm(gzip.open(f, "rt", errors="ignore").read())
        self.c = Counter(); self.h = Counter()
        for i in range(len(txt) - N + 1):
            self.c[txt[i:i + N]] += 1; self.h[txt[i:i + N - 1]] += 1
        self.V = 26

    def ll(self, s):
        tot = 0.0
        for i in range(N - 1, len(s)):
            g = s[i - N + 1:i + 1]
            tot += math.log((self.c[g] + 0.5) / (self.h[g[:-1]] + 0.5 * self.V))
        return tot


def stream():
    """f.30 tokens -> list of (sign, text) with text = decoded value (letters) or '' for NULL/U."""
    out = []
    for line in (HERE / "reading_f30_extended_tokens.tsv").read_text().splitlines()[1:]:
        f = line.split("\t")
        sign, val, grade = f[3], f[5], f[6]
        if grade == "U" or val in ("?", "NULL"):
            out.append((sign, ""))
        else:
            out.append((sign, norm(val)))
    return out


def occ_contexts(toks, code_pos):
    """For each position, left/right context letters (W each), skipping empty tokens."""
    res = []
    for p in code_pos:
        left = "".join(t for _, t in toks[:p])[-W:]
        right = "".join(t for _, t in toks[p + 1:])[:W]
        res.append((left, right))
    return res


def B(lm, ctxs, w, cache):
    key = w
    if key in cache:
        return cache[key]
    alone = lm.ll(w) if len(w) >= N else 0.0
    s = 0.0
    for left, right in ctxs:
        s += lm.ll(left + w + right) - lm.ll(left + right) - alone
    cache[key] = s / len(ctxs)
    return cache[key]


NO_IDENTITY = False  # post-hoc diagnostic (--no-identity): reject a shuffle that reproduces w; licenses no grade


def shuffle(w, rng):
    for _ in range(50):
        l = list(w); rng.shuffle(l); x = "".join(l)
        if not NO_IDENTITY or x != w or len(set(w)) == 1:
            return x
    return x


def run(lm, ctxs, names, reps, rng):
    cache = {}
    scores = {w: B(lm, ctxs, w, cache) for w in names}
    top = max(scores, key=scores.get)
    ctrl = []
    for _ in range(reps):
        ctrl.append(max(B(lm, ctxs, shuffle(w, rng), cache) for w in names))
    ctrl.sort()
    p99 = ctrl[int(0.99 * reps) - 1]
    p = sum(1 for x in ctrl if x >= scores[top]) / reps
    return top, scores[top], p99, p, scores


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--names", default=str(HERE / "f84_names.tsv"))
    ap.add_argument("--reps", type=int, default=1000)
    ap.add_argument("--power-only", action="store_true")
    ap.add_argument("--out", default=str(HERE / "f84_names_test.tsv"))
    ap.add_argument("--no-identity", action="store_true", help="post-hoc diagnostic, not the registered test")
    a = ap.parse_args()
    global NO_IDENTITY
    NO_IDENTITY = a.no_identity
    lm = LM()
    toks = stream()
    names = []
    if not a.power_only:
        for line in Path(a.names).read_text().splitlines():
            if line and not line.startswith("#") and not line.startswith("form"):
                w = norm(line.split("\t")[0])
                if w and w not in names:
                    names.append(w)
    rows = []
    # power control first
    rng = random.Random(0)
    base_names = names if names else ["PAPE", "EMPEREVR", "ROY", "MARQVIS", "ROME", "FLORENCE", "CAPITAINE"]
    npass = 0
    for pw in POWER_WORDS:
        # word occurrences as runs of whole tokens whose concatenated text equals pw
        texts = [t for _, t in toks]
        starts = []
        for i in range(len(toks)):
            acc = ""; j = i
            while j < len(toks) and len(acc) < len(pw):
                acc += texts[j]; j += 1
            if acc == pw and texts[i]:
                starts.append((i, j))
        pick = sorted(rng.sample(starts, min(5, len(starts))))
        mt = list(toks)
        pos = []
        for i, j in pick:
            mt[i] = ("MASK", "")
            for k in range(i + 1, j):
                mt[k] = ("MASKX", "")
            pos.append(i)
        # drop the MASKX tokens' text already ''; contexts skip empties
        ctxs = occ_contexts(mt, pos)
        cand = base_names + [pw]
        top, s, p99, p, _ = run(lm, ctxs, cand, a.reps, random.Random(1))
        ok = top == pw and s > p99
        npass += ok
        rows.append(("power", pw, len(pos), len(starts), top, f"{s:.3f}", f"{p99:.3f}", f"{p:.3f}", "PASS" if ok else "FAIL"))
    power_ok = npass >= 2
    rows.append(("power-summary", f"{npass}/3", "", "", "", "", "", "", "PASS" if power_ok else "FAIL (non-test)"))
    if not a.power_only:
        for c in CODES:
            pos = [i for i, (s, _) in enumerate(toks) if s == c]
            ctxs = occ_contexts(toks, pos)
            top, s, p99, p, sc = run(lm, ctxs, names, a.reps, random.Random(2))
            ok = s > p99
            second = sorted(sc.values())[-2] if len(sc) > 1 else float("nan")
            rows.append(("code", c, len(pos), len(names), top, f"{s:.3f}", f"{p99:.3f}", f"{p:.3f}",
                         ("PASS" if ok else "FAIL") + ("" if power_ok else " (non-test: power control failed)")))
    hdr = "kind\tword_or_code\tn_occ\tn_cand_or_avail\ttop\tB_top\tctrl_p99\tp\tgate"
    out = hdr + "\n" + "\n".join("\t".join(map(str, r)) for r in rows) + "\n"
    if not a.power_only:
        Path(a.out).write_text(out)
    sys.stdout.write(out)


if __name__ == "__main__":
    main()

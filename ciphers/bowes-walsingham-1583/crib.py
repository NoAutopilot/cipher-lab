#!/usr/bin/env python3
"""Crib (name-list) placement search with its own shuffled-ciphertext control, 24 Sept 2026.

Question: can one substitution key (each sign one letter; at most 2 signs per letter) make many of Tomokiyo's
fragment tokens spell names/words that Bowes actually uses? Word list = every capitalised word of 3+ letters
occurring 3+ times in Surtees Soc. vol.14 (The Correspondence of Robert Bowes, 1842, archive.org
correspondenceof00bowerich, whole volume), normalised i=j, u=v. Placements must respect the sign pattern
(equal signs = equal letters). A randomised longest-first greedy (300 restarts) picks non-overlapping, mutually consistent placements to
maximise tokens covered. The same search on the target's tokens shuffled across fragments (same lengths and
sign counts) is the baseline: how much coverage a meaningless text of this shape gets from this word list.

  python3 crib.py parallel     the matched test (below): writes crib_runs.tsv
  python3 crib.py [--shuffles N] [--restarts R]   blind test with the whole-volume word list (stdout only)
"""
import argparse, os, random, re, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(HERE, "..", "..", "tools"))
import subst_hillclimb as sh

MAXH = 2


def wordlist():
    t = open(os.path.join(HERE, "corpus", "correspondenceof00bowerich_djvu.txt"), encoding="utf-8", errors="replace").read()
    c = Counter(sh.norm(w) for w in re.findall(r"\b[A-Z][a-z]{2,}\b", t))
    return sorted(w for w, n in c.items() if n >= 3 and len(w) >= 3)


def placements(frags, words):
    P = []
    for fi, f in enumerate(frags):
        for w in words:
            L = len(w)
            for o in range(len(f) - L + 1):
                seg = f[o:o + L]
                m, ok = {}, True
                for s, ch in zip(seg, w):
                    if m.setdefault(s, ch) != ch:
                        ok = False; break
                if not ok:
                    continue
                inv = Counter(m.values())
                if max(inv.values()) > MAXH:
                    continue
                P.append((fi, o, L, w, tuple(sorted(m.items()))))
    return P


def consistent(chosen):
    key = {}
    for p in chosen:
        for s, ch in p[4]:
            if key.setdefault(s, ch) != ch:
                return None
    if key and max(Counter(key.values()).values()) > MAXH:
        return None
    return key


def search(frags, P, restarts, seed, noise=3.0):
    """Randomised longest-first greedy: order placements by length plus noise, add each one that overlaps
    nothing chosen and keeps the key consistent. Best coverage over the restarts."""
    rng = random.Random(seed)
    best, bestset = 0, []
    for r in range(restarts):
        order = sorted(P, key=lambda p: -(p[2] + noise * rng.random()))
        occ = [[False] * len(f) for f in frags]
        key, lc, chosen, cov = {}, Counter(), [], 0
        for p in order:
            fi, o, L = p[0], p[1], p[2]
            if any(occ[fi][o:o + L]):
                continue
            ok, newl = True, Counter()
            for sgn, ch in p[4]:
                k = key.get(sgn)
                if k is None:
                    newl[ch] += 1
                elif k != ch:
                    ok = False; break
            if not ok or any(lc[ch] + n > MAXH for ch, n in newl.items()):
                continue
            for sgn, ch in p[4]:
                if sgn not in key:
                    key[sgn] = ch; lc[ch] += 1
            for i in range(o, o + L):
                occ[fi][i] = True
            chosen.append(p); cov += L
        if cov > best:
            best, bestset = cov, chosen
    return best, sorted(bestset)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shuffles", type=int, default=20)
    ap.add_argument("--restarts", type=int, default=300)
    a = ap.parse_args()
    words = wordlist()
    tf = sh.load_cipher(os.path.join(HERE, "ciphertext.txt"))
    rows = ["run\tinput\twords\tplacements\tbest_tokens_covered_of_101\tplacements_chosen"]
    def run(name, frags):
        P = placements(frags, words)
        best = search(frags, P, a.restarts, 7)
        rows.append(f"{name}\t{'target' if name == 'T' else 'shuffled'}\t{len(words)}\t{len(P)}\t{best[0]}\t" +
                    "; ".join(f"F{p[0]+1}@{p[1]}:{p[3]}" for p in best[1]))
        print(rows[-1], flush=True)
        return best[0]
    t = run("T", tf)
    base = [run(f"S{s}", sh.shuffle_frags(tf, s)) for s in range(1, a.shuffles + 1)]
    mean = sum(base) / len(base)
    sd = (sum((b - mean) ** 2 for b in base) / (len(base) - 1)) ** 0.5
    rows.append(f"#summary\ttarget {t}; shuffled mean {mean:.1f} sd {sd:.1f} max {max(base)} over {len(base)}; z {(t-mean)/sd:.1f}")
    print(rows[-1])
    open(os.path.join(HERE, "crib_runs.tsv"), "w").write("\n".join(rows) + "\n")


if __name__ == "__main__" and sys.argv[1:2] != ["parallel"]:
    main()


# ------------------------------------------------------------------ matched test by parallel letter
HDR = re.compile(r"^[CLXVI]{2,}\S{0,3}\s*[—-]")


def letters():
    """Split Surtees vol.14 into letters at the roman-numeral headers; return [(header, text)]."""
    lines = open(os.path.join(HERE, "corpus", "correspondenceof00bowerich_djvu.txt"), encoding="utf-8", errors="replace").read().split("\n")
    out, cur, head = [], [], None
    for i, l in enumerate(lines):
        if i > 1000 and HDR.match(l):
            if head:
                out.append((head, "\n".join(cur)))
            head, cur = l.strip(), []
        elif head:
            cur.append(l)
    out.append((head, "\n".join(cur)))
    return out


def capwords(text):
    """Capitalised words (3+ letters) not at a sentence start, normalised; the candidate cipher words."""
    ws = set()
    for m in re.finditer(r"([.!?;:]?)\s*\b([A-Z][a-z]{2,})\b", text):
        if not m.group(1):
            ws.add(sh.norm(m.group(2)))
    return sorted(ws)


def parallel(restarts=300, nshuf=20):
    L = letters()
    heads = [h for h, _ in L]
    def find(tag):
        return next(i for i, h in enumerate(heads) if h.startswith(tag))
    tgt_ix = [find("CLXXXVIL"), find("CCXXXIX"), find("CCXL.")]
    tw = sorted(set(w for i in tgt_ix for w in capwords(L[i][1])))
    tf = sh.load_cipher(os.path.join(HERE, "ciphertext.txt"))
    rows = ["run\tcipher\tword_source\twords\tplacements\tcovered_of_101\tchosen"]
    def run(name, frags, words, src):
        P = placements(frags, words)
        b, ch = search(frags, P, restarts, 7) if P else (0, [])
        rows.append(f"{name}\t{'target' if name.startswith('T') else 'shuffled'}\t{src}\t{len(words)}\t{len(P)}\t{b}\t" +
                    "; ".join(f"F{p[0]+1}@{p[1]}:{p[3]}" for p in ch))
        print(rows[-1], flush=True)
        return b
    t = run("T0", tf, tw, "CLXXXVII+CCXXXIX+CCXL (the parallel Letter-Book copies)")
    # other letters: pool words of three consecutive other letters so the list size is comparable
    others = []
    idx = [i for i in range(len(L) - 2) if not set(range(i, i + 3)) & set(tgt_ix)]
    rng = random.Random(5)
    for k, i in enumerate(rng.sample(idx, 40)):
        w = sorted(set(x for j in range(i, i + 3) for x in capwords(L[j][1])))
        others.append(run(f"T{k+1}", tf, w, f"other letters {L[i][0][:12]}.. (+2 following)"))
    shuf = [run(f"S{s}", sh.shuffle_frags(tf, s), tw, "CLXXXVII+CCXXXIX+CCXL") for s in range(1, nshuf + 1)]
    def st(v):
        m = sum(v) / len(v); sd = (sum((x - m) ** 2 for x in v) / (len(v) - 1)) ** 0.5
        return m, sd, max(v)
    mo, so, xo = st(others); ms, ss, xs = st(shuf)
    rows.append(f"#summary\ttarget with parallel-letter words: {t} tokens; other-letter word lists (40): mean {mo:.1f} sd {so:.1f} max {xo}; "
                f"shuffled target with parallel words ({nshuf}): mean {ms:.1f} sd {ss:.1f} max {xs}")
    print(rows[-1])
    open(os.path.join(HERE, "crib_runs.tsv"), "w").write("\n".join(rows) + "\n")


if __name__ == "__main__" and sys.argv[1:2] == ["parallel"]:
    parallel()

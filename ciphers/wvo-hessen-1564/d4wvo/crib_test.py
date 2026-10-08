#!/usr/bin/env python3
"""D4-WVO crib-placement test on f.23 (PREREG-D4-WVO.md). Writes d4wvo/result.tsv and d4wvo/summary.txt.
Run from the repo root: python3 ciphers/wvo-hessen-1564/d4wvo/crib_test.py"""
import csv, glob, gzip, math, os, random, re, sys
ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import crib_list_fit as clf  # noqa: E402
T = os.path.join(ROOT, "ciphers", "wvo-hessen-1564"); D = os.path.join(T, "d4wvo")
SPANS, N, SEED = (1,), 1000, 1564


def fold(s):
    s = s.lower().replace("v", "u").replace("j", "i").replace("y", "i")
    return re.sub(r"[^a-z]", "", s)


def load():
    key = {r["code"]: (fold(r["value"]), r["grade"]) for r in csv.DictReader(open(os.path.join(T, "settled/key.tsv")), delimiter="\t")}
    toks = []
    for r in csv.DictReader(open(os.path.join(T, "settled/ciphertext.tsv")), delimiter="\t"):
        l, g = key.get(r["sign"], ("", "U"))
        wild = g != "C" or not l
        toks.append((l if not wild else "_", wild, f"{r['line']}:{r['pos']}:{r['sign']}"))
    return key, toks


def places(word, toks):
    s, a, m, at = clf.fit(word, toks, "free", SPANS)
    return a >= 0.6 * len(word) and m <= 1 and s >= 6, (s, a, m, at)


def T_of(words, toks):
    return sum(places(w, toks)[0] for w in words)


def p95(xs):
    xs = sorted(xs); return xs[int(math.ceil(0.95 * len(xs))) - 1]


def main():
    key, toks = load()
    target = [l.split("\t")[0] for l in open(os.path.join(D, "crib_list.tsv")) if l.strip()]
    vocab = {}
    for f in sorted(glob.glob(os.path.join(ROOT, "tools/data/de1600/*.gz"))):
        for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", gzip.open(f, "rt", errors="ignore").read()):
            if re.search(r"[äöüßÄÖÜ]", w):
                continue
            w = fold(w)
            if w and w not in target:
                vocab.setdefault(len(w), set()).add(w)
    vocab = {k: sorted(v) for k, v in vocab.items()}
    gloss = []
    for r in csv.DictReader(open(os.path.join(T, "r10tx/gloss_r10.tsv")), delimiter="\t"):
        for w in re.split(r"[\s|]+", r["gloss"]):
            w = fold(w)
            if w and w not in gloss:
                gloss.append(w)
    pos = []
    for w in target:
        L = len(w)
        for d in [0, -1, 1, -2, 2, -3, 3, -4, 4]:
            c = [g for g in gloss if len(g) == L + d and g not in pos]
            if c:
                pos.append(c[0]); break
    rng = random.Random(SEED)

    def nullA(lengths):
        return [T_of([rng.choice(vocab[len(w)]) for w in lengths], toks) for _ in range(N)]

    out = [("list", "word", "places", "fit", "agree", "mismatch", "at", "covers_wild")]
    for name, ws in (("positive", pos), ("target", target)):
        for w in ws:
            ok, (s, a, m, at) = places(w, toks)
            cov = ""
            if ok:
                i0 = [t[2] for t in toks].index(at)
                cov = " ".join(f"{toks[i0+k][2]}={w[k]}" for k in range(len(w)) if toks[i0 + k][1])
                mm = " ".join(f"{toks[i0+k][2]}:{toks[i0+k][0]}!={w[k]}" for k in range(len(w))
                              if not toks[i0 + k][1] and toks[i0 + k][0] != w[k])
                cov += (" | mismatch " + mm) if mm else ""
            out.append((name, w, int(ok), s, a, m, at, cov))
    Tpos, Ttar = T_of(pos, toks), T_of(target, toks)
    A_pos = nullA(pos)
    A_tar = nullA(target)
    cs = [c for c, (l, g) in key.items() if g == "C" and l]
    B = []
    for _ in range(N):
        vals = [key[c][0] for c in cs]; rng.shuffle(vals); sk = dict(zip(cs, vals))
        st = [(sk[t[2].split(":")[2]], False, t[2]) if not t[1] else t for t in toks]
        B.append(T_of(target, st))
    gP = Tpos > p95(A_pos); gT = Ttar > p95(A_tar) and Ttar > p95(B)
    mean = lambda x: sum(x) / len(x)
    summ = [f"positive list ({len(pos)}): {' '.join(pos)}",
            f"P: T_pos {Tpos}/{len(pos)} vs wrong-text null mean {mean(A_pos):.2f} p95 {p95(A_pos)} max {max(A_pos)} -> {'PASS' if gP else 'CONTROL BELOW GATE'}",
            f"target: T {Ttar}/{len(target)}; A wrong-text mean {mean(A_tar):.2f} p95 {p95(A_tar)} max {max(A_tar)}; "
            f"B shuffled-key mean {mean(B):.2f} p95 {p95(B)} max {max(B)} -> {('PASS' if gT else 'FAIL') if gP else 'not interpreted (P below gate)'}",
            f"share A >= T: {sum(x >= Ttar for x in A_tar)/N:.3f}; share B >= T: {sum(x >= Ttar for x in B)/N:.3f}"]
    with open(os.path.join(D, "result.tsv"), "w") as f:
        csv.writer(f, delimiter="\t", lineterminator="\n").writerows(out)
    open(os.path.join(D, "summary.txt"), "w").write("\n".join(summ) + "\n")
    print("\n".join(summ))
    for r in out[1:]:
        print("\t".join(map(str, r)))


if __name__ == "__main__":
    main()

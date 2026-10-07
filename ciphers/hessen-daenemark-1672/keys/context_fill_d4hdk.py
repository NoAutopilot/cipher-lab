#!/usr/bin/env python3
"""Context fill of unread nomenclator groups (PREREG-D4HDK.md, 7 Oct 2026).

Word-bigram model on tools/data/de17; held-out control on the C-grade gloss-pinned codes first, then the targets.
Writes keys/context_fill_d4hdk.tsv. --check re-runs and exits 1 if the committed TSV differs.
"""
import csv, glob, gzip, math, os, random, re, sys
from collections import Counter

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
ROOT = os.path.dirname(os.path.dirname(T))
OUT = os.path.join(HERE, "context_fill_d4hdk.tsv")

def fold(w):
    w = w.lower()
    for a, b in (("ä", "a"), ("ö", "o"), ("ü", "u"), ("ae", "a"), ("oe", "o"), ("ue", "u"), ("ß", "s"),
                 ("ck", "k"), ("th", "t"), ("y", "i"), ("dt", "t")):
        w = w.replace(a, b)
    return re.sub(r"(.)\1+", r"\1", w)

REF = {  # referent -> folded surface forms (PREREG candidate set, 28)
 "Dennemarck": ["denemark", "danemark", "dennemark", "denmark"], "Brandenburg": ["brandenburg", "brandenburgk"],
 "Berlin": ["berlin"], "Holland": ["holand"], "Staaten": ["staten", "staden"], "Franckreich": ["frankreich", "frankreih"],
 "Kayser": ["kaiser", "keiser", "kaiserl"], "Konig": ["konig", "konigs", "konige"], "Hertzog": ["hertzog", "herzog", "hertzogs"],
 "Ploen": ["plon", "ploen"], "Alliance": ["aliance", "aliantz", "alianz", "aliantze"], "Schweden": ["schweden", "suecia", "sueco"],
 "Daniae": ["dania", "daniae"], "Bleinenkehl": ["bleinenkehl", "bleinenkohl"], "Holstein": ["holstein", "holsteinische"],
 "Gottorf": ["gotorf", "gotorp"], "Ahlefeldt": ["ahlefelt", "alefelt"], "Statthalter": ["stathalter", "stathalters"],
 "Gabel": ["gabel"], "Griffenfeld": ["grifenfelt", "grifenfeld"], "Schumacher": ["schumacher"], "England": ["england", "engelland"],
 "Hamburg": ["hamburg"], "Lubeck": ["lubek"], "Braunschweig": ["braunschweig"], "Luneburg": ["luneburg"],
 "Sachsen": ["sachsen"], "Spanien": ["spanien", "hispanien"],
}
# fold forms once more so they match the corpus folding
REF = {r: sorted({fold(f) for f in fs}) for r, fs in REF.items()}
CODE2REF = {"229": "Berlin", "447": "Kayser", "437": "Hertzog", "641": "Ploen", "601": "Dennemarck", "602": "Konig",
            "605": "Dennemarck", "651": "Brandenburg", "653": "Brandenburg", "681": "Brandenburg", "774": "Holland",
            "775": "Staaten", "834": "Daniae", "5756": "Franckreich", "303": "Alliance", "768": "Schweden", "690": "Bleinenkehl"}
CTRL_CODES = {"229", "447", "601", "605", "651", "653", "681", "774", "775", "834", "5756"}  # key_gloss grade C
TARGETS = {"p2_7.1": "625", "p3_4.1": "625", "p3_17.2": "634", "p3_26.3": "602"}

def corpus():
    toks = []
    for f in sorted(glob.glob(os.path.join(ROOT, "tools/data/de17/*.txt.gz"))):
        txt = gzip.open(f, "rt", encoding="utf-8", errors="replace").read()
        toks += [fold(w) for w in re.findall(r"[A-Za-zÄÖÜäöüß]+", txt)]
    return toks

def contexts():
    """token id -> (code, left word, right word) from pass A context columns (pass B if A empty)."""
    rows = {}
    for p in (1, 2, 3):
        for s in ("A", "B"):
            fn = os.path.join(T, "transcription", f"p{p}_pass{s}.tsv")
            for r in csv.DictReader(open(fn, encoding="utf-8"), delimiter="\t"):
                tid = f"p{p}_{r['line']}.{r['pos']}"
                if tid not in rows:
                    rows[tid] = {}
                rows[tid][s] = (r["sign"], r.get("context_before") or "", r.get("context_after") or "")
    # the sign comes from the merged ciphertext.tsv
    signs = {}
    for r in csv.DictReader(open(os.path.join(T, "ciphertext.tsv"), encoding="utf-8"), delimiter="\t"):
        signs[f"{r['line']}.{r['pos']}"] = r["sign"]
    out = {}
    for tid, d in rows.items():
        if tid not in signs:
            continue
        for s in ("A", "B"):
            if s in d:
                _, lb, la = d[s]
                L = word(lb, last=True); R = word(la, last=False)
                if L or R:
                    out[tid] = (signs[tid], L, R); break
    return out

def word(ctx, last):
    ws = re.findall(r"[A-Za-zÄÖÜäöüß]+|\d{3,4}", ctx)
    ws = [w for w in ws if not w.isdigit() or w in CODE2REF]
    if not ws:
        return ""
    w = ws[-1] if last else ws[0]
    return ("@" + CODE2REF[w]) if w.isdigit() else fold(w)

class LM:
    def __init__(self, toks):
        f2r = {f: r for r, fs in REF.items() for f in fs}
        toks = ["@" + f2r[t] if t in f2r else t for t in toks]
        self.u = Counter(toks); self.b = Counter(zip(toks, toks[1:])); self.n = len(toks); self.V = len(self.u)
        self.lu = Counter(t for t, _ in self.b)
    def pu(self, w):
        return (self.u[w] + 0.1) / (self.n + 0.1 * self.V)
    def pb(self, a, w):
        if not a:
            return self.pu(w)
        return 0.7 * (self.b[(a, w)] + 0.1) / (self.lu[a] + 0.1 * self.V) + 0.3 * self.pu(w)
    def score(self, r, L, R):
        c = "@" + r
        return math.log(self.pb(L, c)) + (math.log(self.pb(c, R)) if R else 0.0)
    def prior(self, r):
        return math.log(self.pu("@" + r))

def rank(lm, L, R, true=None, prior=False):
    sc = sorted(((lm.prior(r) if prior else lm.score(r, L, R)), r) for r in REF)[::-1]
    names = [r for _, r in sc]
    return sc, (names.index(true) + 1 if true else None)

def main():
    lm = LM(corpus())
    ctx = contexts()
    ctrl = [(t, CODE2REF[c], L, R) for t, (c, L, R) in sorted(ctx.items()) if c in CTRL_CODES]
    def acc(items):
        rk = [rank(lm, L, R, true)[1] for _, true, L, R in items]
        return sum(k == 1 for k in rk) / len(rk), sum(1 / k for k in rk) / len(rk), rk
    top1, mrr, rk = acc(ctrl)
    ptop1 = sum(rank(lm, "", "", true, prior=True)[1] == 1 for _, true, _, _ in ctrl) / len(ctrl)
    rnd = random.Random(4); nulls = []
    cs = [(L, R) for _, _, L, R in ctrl]
    for _ in range(1000):
        p = cs[:]; rnd.shuffle(p)
        nulls.append(acc([(t, tr, L, R) for (t, tr, _, _), (L, R) in zip(ctrl, p)])[1])
    nulls.sort(); p95 = nulls[949]
    gate = top1 >= 0.5 and mrr > p95 and top1 > ptop1
    lines = ["kind\ttoken\tcode\tleft\tright\ttruth\trank_of_truth\ttop1\ttop2\tmargin"]
    for (t, true, L, R), k in zip(ctrl, rk):
        sc, _ = rank(lm, L, R)
        lines.append(f"control\t{t}\t{ctx[t][0]}\t{L}\t{R}\t{true}\t{k}\t{sc[0][1]}\t{sc[1][1]}\t{sc[0][0]-sc[1][0]:.3f}")
    for t, c in TARGETS.items():
        if t not in ctx:
            lines.append(f"target\t{t}\t{c}\t\t\t\t\tno-context\t\t"); continue
        _, L, R = ctx[t]; sc, _ = rank(lm, L, R)
        lines.append(f"target\t{t}\t{c}\t{L}\t{R}\t\t\t{sc[0][1]}\t{sc[1][1]}\t{sc[0][0]-sc[1][0]:.3f}")
    lines.append(f"summary\tcontrol_n={len(ctrl)}\ttop1={top1:.3f}\tmrr={mrr:.3f}\tnull_mrr_p95={p95:.3f}"
                 f"\tprior_top1={ptop1:.3f}\tgate={'PASS' if gate else 'FAIL'}\t\t\t")
    text = "\n".join(lines) + "\n"
    if "--check" in sys.argv:
        old = open(OUT, encoding="utf-8").read() if os.path.exists(OUT) else ""
        print("up to date" if old == text else "STALE"); sys.exit(0 if old == text else 1)
    open(OUT, "w", encoding="utf-8").write(text); print(text)

if __name__ == "__main__":
    main()

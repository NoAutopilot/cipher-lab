#!/usr/bin/env python3
"""F61-APPLY (campaign step H4, 27 Sept 2026): the cell map applied to signs outside Tomokiyo's five spans.

Pre-registered before the unmarked-line read was looked at. Map (scripts/f61crib4_map.tsv, H15b): a class is a LETTER
class if its top cell has count >= 2 and no tie -- PHI e/r, C43 a/n, C6 a/n, 4TRI c/p, INF h/u, VBAR_A g/t, DBL b/o,
LOOPBAR a/n, VBAR_B f/s, EBR l/y, ZHOOK i/x (11); every other code (CA, CROSS, ELOOP, 4PI, BETA, HASH4, LOOPSTEM1, CH,
LL, 4STEM, OTHER) is a null and is dropped. Each letter sign offers its cell's two letters; the line's letters are chosen
by a beam search (width 200) maximising the fr16 4-gram log-probability of tools/judge_plaintext.py's NgramModel (the
'fr' corpus, Lettres de Catherine de Medicis t.1). Statistic: mean log10 4-gram probability per letter of the best
path, pooled over the lines read (letter-weighted). Controls: 20 maps with the 11 cells permuted across the 11 letter
classes (seed 1), same decode; and the judge's own real-text p05 / letter-shuffled p99 at the same N for reference.
Gate (H4): target above every one of the 20 permuted-map scores. Positive control, same pipeline: the five known span
lines from scripts/passA_classes.tsv, whose best path is also compared letter by letter with Tomokiyo's markup where
he reads (H1-H15b never decoded through a language model; this shows the pipeline's power at this N).

  python3 scripts/f61apply.py [--check]    (from the target folder; reads scripts/read_call_U.tsv when present)
"""
import csv, os, random, sys
from collections import Counter
HERE = os.path.dirname(os.path.abspath(__file__)); ROOT = os.path.abspath(f"{HERE}/../../..")
sys.path.insert(0, f"{ROOT}/tools"); sys.path.insert(0, HERE)
import judge_plaintext as J
from f61crib import load_spans, align

def load_map():
    m = {}
    for r in csv.DictReader((l for l in open(f"{HERE}/f61crib4_map.tsv") if not l.startswith("#")), delimiter="\t"):
        if r["cell"] == "null" or r["tie"] == "yes": continue
        top = int(r["cell_counts"].split()[0].rsplit(":", 1)[1])
        if top >= 2: m[r["class"]] = tuple(r["cell"].split("/"))
    return m
def read_pass(path):
    lines = {}
    for r in csv.DictReader((l for l in open(path) if not l.startswith("#")), delimiter="\t"):
        lines.setdefault(r["line"], []).append(r["sign"])
    return lines
def beam(model, options, width=200):
    """options: list of letter tuples; returns (best string, total log10 prob)."""
    n, k, c, ctx = model.n, model.k, model.c, model.ctx
    def lp(s):
        g = s[-n:]
        return __import__("math").log10((c.get(g, 0) + k) / (ctx.get(g[:-1], 0) + 26 * k))
    paths = [("", 0.0)]
    for opts in options:
        new = []
        for s, sc in paths:
            for L in opts:
                t = s + L
                new.append((t, sc + (lp(t) if len(t) >= n else 0.0)))
        new.sort(key=lambda x: -x[1]); paths = new[:width]
    return paths[0]
def decode(model, lines, cmap):
    out, tot_lp, tot_n = {}, 0.0, 0
    for line, seq in lines.items():
        opts = [cmap[c] for c in seq if c in cmap]
        if len(opts) < model.n: out[line] = ("", 0, None); continue
        s, lp = beam(model, opts)
        out[line] = (s, len(s), lp / max(1, len(s) - model.n + 1))
        tot_lp += lp; tot_n += len(s) - model.n + 1
    return out, (tot_lp / tot_n if tot_n else -9.9), sum(v[1] for v in out.values())
def run(model, lines, cmap, tag, out, spans=None):
    rng = random.Random(1)
    dec, score, N = decode(model, lines, cmap)
    out.append(f"[{tag}] letters {N}; best-path mean log10 4-gram {score:.3f}")
    for line, (s, n, sc) in dec.items():
        out.append(f"  {line}\t{n} letters\t{s}\t{'' if sc is None else f'{sc:.3f}'}")
    labs = sorted(cmap); ctrl = []
    for _ in range(20):
        v = [cmap[l] for l in labs]; rng.shuffle(v)
        ctrl.append(decode(model, lines, dict(zip(labs, v)))[1])
    real, null, _ = model.controls(max(N, model.n), samples=200, seed=1)
    out.append(f"[{tag}] 20 permuted-cell maps: mean {sum(ctrl)/20:.3f} max {max(ctrl):.3f}; judge reference at N={N}: real p05 {J.pct(real, 5):.3f}, shuffled-letters p99 {J.pct(null, 99):.3f}")
    out.append(f"[{tag}] GATE (target above every permuted map): {'PASS' if score > max(ctrl) else 'FAIL'}")
    if spans:  # positive control: letters agreeing with Tomokiyo's markup, on the DP alignment of the reference to the class sequence
        agree = tot = 0
        for s_, line, markup in spans:
            seq = [c for c in lines[line]]; letters = [c for c in seq if c in cmap]
            _, pairs = align(markup, seq, cmap)
            best = dec[line][0]; pos = {}
            j = 0
            for i, c in enumerate(seq):
                if c in cmap: pos[i] = j; j += 1
            for mi, sj in pairs:
                if markup[mi] != "-" and sj in pos and pos[sj] < len(best):
                    tot += 1; agree += best[pos[sj]] == markup[mi]
        out.append(f"[{tag}] best path vs Tomokiyo's letters at aligned positions: {agree}/{tot} = {agree/max(1,tot):.3f} (u=v, i=j not folded)")
    return score
def main():
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr"]], n=4)
    cmap = load_map()
    out = ["map (letter classes): " + " ".join(f"{c}={'/'.join(v)}" for c, v in sorted(cmap.items())) + "; all other codes null"]
    run(model, read_pass(f"{HERE}/passA_classes.tsv"), cmap, "positive control: five known span lines, pass A", out, spans=load_spans())
    if os.path.exists(f"{HERE}/read_call_U.tsv"):
        run(model, read_pass(f"{HERE}/read_call_U.tsv"), cmap, "TARGET: unmarked lines", out)
    else:
        out.append("[TARGET] scripts/read_call_U.tsv not present: unmarked lines not yet read")
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61apply_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt
        print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    main()

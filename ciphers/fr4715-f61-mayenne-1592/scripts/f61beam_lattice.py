#!/usr/bin/env python3
"""F61-BEAM-LATTICE (campaign step H136, 28 Sept 2026, runner 5 session_01RbeePKZVn83gNfES8yFmhe), script-only. H134: a word
model must live inside the search. Beam over the x/y choices whose state is (last three letters, position in a trie of the
fr16 word list NgramModel.words, or FREE). Moves per letter: continue the current word along the trie; if the current node
ends a word, close it and start a new word (bonus 0.5 x word length, fixed before any run) or go FREE; from FREE or on any
letter, abandon into FREE (no bonus); from FREE start a word. Score = 4-gram log10 (fr16) + bonuses; a word still open at the
line end earns its bonus only if its node ends a word. Width 2000, recombination on the whole state. Scored on H126's 125
known positions (14-cell map) against the plain beam's 107/125. GATE H136: >= 115/125.
  -> scripts/f61beam_lattice_result.txt [--check]"""
import os, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
ARGS = sys.argv[1:]; sys.argv = sys.argv[:1]
import f61beam_words as W
M14, lp, jp, NM = W.M14, W.lp, W.jp, W.NM
TRIE = [{}]; END = [0]
for w in NM.words:
    w = jp.fold(w)
    if not w: continue
    n = 0
    for ch in w:
        if ch not in TRIE[n]: TRIE.append({}); END.append(0); TRIE[n][ch] = len(TRIE) - 1
        n = TRIE[n][ch]
    END[n] = len(w)
FREE = -1
def best_lattice(sets, B=0.5, W_=2000):
    beam = {("", FREE): ("", 0.0)}
    for st in sets:
        nb = {}
        def push(t, node, v):
            k = (t[-3:], node)
            if k not in nb or nb[k][1] < v: nb[k] = (t, v)
        for (_, node), (s, v) in beam.items():
            for ch in st:
                t = s + ch; v1 = v + (lp(t[-4:]) if len(t) >= 4 else 0.0)
                if node != FREE and ch in TRIE[node]: push(t, TRIE[node][ch], v1)            # continue the word
                bonus = B * END[node] if node != FREE and END[node] else 0.0
                if node == FREE or END[node]:
                    if ch in TRIE[0]: push(t, TRIE[0][ch], v1 + bonus)                       # close (if any) and start a word
                push(t, FREE, v1 + bonus)                                                   # close or abandon into FREE
        beam = dict(sorted(nb.items(), key=lambda kv: -kv[1][1])[:W_])
    return max(((s, v + (B * END[node] if node != FREE and END[node] else 0.0)) for (_, node), (s, v) in beam.items()), key=lambda x: x[1])[0]
def score(L, C, P):
    r = n = rp = 0
    for line, seq in L.items():
        idx = [k for k, c in enumerate(seq) if c in C]; sets = [tuple(jp.fold(x) for x in C[seq[k]].split("/")) for k in idx]
        s = best_lattice(sets); s0 = M14.BM.best(sets)[0]
        for i, k in enumerate(idx):
            if (line, k) in P and P[(line, k)][1] in sets[i]:
                n += 1; r += s[i] == P[(line, k)][1]; rp += s0[i] == P[(line, k)][1]
    return r, rp, n
def main():
    C = M14.J.cells(); L61, sp61 = M14.J.lines("known_h51"), W.load_spans(); L108, sp108 = M14.K.load108()
    a = score(L61, C, M14.known_positions(L61, sp61, C)); b = score(L108, C, M14.known_positions(L108, sp108, C))
    r, rp, n = a[0] + b[0], a[1] + b[1], a[2] + b[2]
    out = [f"trie nodes {len(TRIE)} from {len(NM.words)} words",
           f"f.61 spans: lattice beam {a[0]}/{a[2]}, plain beam {a[1]}/{a[2]}", f"f.108r overlay: lattice beam {b[0]}/{b[2]}, plain beam {b[1]}/{b[2]}",
           f"pooled: lattice beam {r}/{n}, plain beam {rp}/{n}; GATE H136 (>= 115/125): {'PASS' if r >= 115 else 'FAIL'}"]
    txt = "\n".join(out) + "\n"; rpth = f"{HERE}/f61beam_lattice_result.txt"
    if "--check" in ARGS:
        good = os.path.exists(rpth) and open(rpth).read() == txt; print("fresh" if good else "STALE"); sys.exit(0 if good else 1)
    open(rpth, "w").write(txt); print(txt, end="")
if __name__ == "__main__": main()

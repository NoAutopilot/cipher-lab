#!/usr/bin/env python3
"""MONL-KING2 grading (20 Oct 2026): S = keyed token inside a run of fr16 lexicon words (king2_score.py's run statistic) longer
than BOTH the longest run any of the 20 value-shuffled keys yields on the same tokens AND 42 letters (about 1.5 x the 28-letter
unicity distance of a 26-letter simple substitution, a floor for this 68-cell homophonic table); M = any other keyed token;
U = unkeyed (W:, ?x, ?double_slash). Writes votes_c258.tsv (value = key letter for S tokens) for decode_key.py (voted_grade S)."""
import sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE)); sys.path.insert(0, str(HERE.parents[2] / "tools"))
import king2_score as ks, segmenter as sg
key = ks.load_key(); lex = sg.Lexicon.load("fr")
rows = [l.split("\t") for l in (HERE.parent / "ciphertext_c258.tsv").read_text().splitlines()[1:]]
toks = [r[2] for r in rows]

def runs(toks, key):
    """[(start_token_index, end_token_index_excl, letters)] of good-word runs, per keyed segment"""
    out, seg = [], []
    for i, t in enumerate(toks + ["|"]):
        if t in key: seg.append(i); continue
        if seg:
            s = "".join(key[toks[j]] for j in seg); tk = sg.segment(s, lex)
            good = [ok and len(w) >= 2 for w, ok in tk]
            for k, (w, ok) in enumerate(tk):
                if ok and len(w) == 1 and 0 < k < len(tk) - 1 and good[k - 1] and good[k + 1]: good[k] = True
            off, st = 0, None
            for (w, _), g in zip(tk + [("", False)], good + [False]):
                if g and st is None: st = off
                if not g and st is not None:
                    out.append((seg[st], seg[off - 1] + 1, off - st)); st = None
                off += len(w)
            seg = []
    return out
null_max = max(max([r[2] for r in runs(toks, k)] or [0]) for k in ks.shuffled_keys(key, 20, 133))
thr = max(null_max, 42)
S = set()
for a, b, L in runs(toks, key):
    if L > thr: S.update(range(a, b))
lines = ["line\tpos\tvalue"] + [f"{r[0]}\t{r[1]}\t{key[r[2]]}" for i, r in enumerate(rows) if i in S]
(HERE.parent / "votes_c258.tsv").write_text("\n".join(lines) + "\n")
nk = sum(t in key for t in toks)
print(f"null max run {null_max}, threshold {thr}; target runs > thr: {[(a,b,L) for a,b,L in runs(toks,key) if L>thr]}")
print(f"tokens {len(toks)}: S {len(S)}, M {nk-len(S)}, U {len(toks)-nk}")

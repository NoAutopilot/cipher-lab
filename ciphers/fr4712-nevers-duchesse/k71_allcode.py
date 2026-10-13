#!/usr/bin/env python3
"""F4712-71: key no.71's Motz list (11-99) as an all-code text on fr.4712 f.10r S1, per PREREG-F4712-71.md.
python3 k71_allcode.py [--check]   writes k71_allcode_decode.tsv and k71_allcode_score.tsv; --check exits 1 if either is stale."""
import csv, math, random, re, statistics, sys
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[1] / "tools")); sys.path.insert(0, str(H))
import judge_plaintext as jp
from score_key1 import TOMO

MOTZ_K71 = set(range(11, 18)) | set(range(52, 59)) | set(range(92, 100))
PERSONS = {"8": "roy", "10": "royne"}

def fold(w): return w.lower().translate(jp.FOLD)

def load_motz():
    rows = [l for l in open(H / "keys/key_no71.tsv") if not l.startswith("#")]
    m = {}
    for r in csv.DictReader(rows, delimiter="\t"):
        if r["kind"] != "word": continue
        c = int(r["code"]); new = r["source"].startswith("F4712-71")
        if (c in MOTZ_K71 and not new) or (c not in MOTZ_K71 and new):
            m[str(c)] = (fold(r["value"].split("|")[0]), r["grade"])
    assert sorted(map(int, m)) == list(range(11, 100)), sorted(map(int, m))
    return m

def stream(vocab):
    t = " ".join(jp.read_corpus(p) for p in jp.LANG_CORPORA["fr16"])
    return [w for w in (fold(x) for x in re.findall(r"[A-Za-zéèêàçùûîôâëï']+", t)) if w in vocab]

class Bigram:
    def __init__(self, toks, vocab):
        self.u = Counter(toks); self.b = Counter(zip(toks, toks[1:])); self.V = len(vocab)
    def score(self, ws):
        s = [math.log((self.b[(a, b)] + .5) / (self.u[a] + .5 * self.V)) for a, b in zip(ws, ws[1:])]
        return sum(s) / len(s)

def decode(toks, m): return [PERSONS.get(t) or m[t][0] for t in toks]

def perm(m, seed):
    rng = random.Random(seed); cs = sorted(m, key=int); vs = [m[c] for c in cs]; rng.shuffle(vs)
    return dict(zip(cs, vs))

def rank_z(model, toks, m, n=200):
    real = model.score(decode(toks, m))
    null = [model.score(decode(toks, perm(m, s))) for s in range(1, n + 1)]
    return real, 1 + sum(x >= real for x in null), (real - statistics.mean(null)) / (statistics.pstdev(null) or 1e-9)

def main():
    m = load_motz(); inv = {v: c for c, (v, g) in m.items()}
    vocab = set(inv) | set(PERSONS.values())
    st = stream(vocab); cut = int(.7 * len(st))
    model = Bigram(st[:cut], vocab); held = st[cut:]
    pinv = {v: c for c, v in PERSONS.items()}
    toks = [str(int(t)) for l in TOMO for t in l]
    real, rk, z = rank_z(model, toks, m)
    P = []
    for s in range(20):
        i = random.Random(50000 + s).randrange(len(held) - 37)
        P.append(rank_z(model, [inv.get(w) or pinv[w] for w in held[i:i + 37]], m)[1])
    rng = random.Random(99)
    F = [rank_z(model, [str(rng.randint(11, 99)) for _ in range(37)], m)[1] for _ in range(20)]
    p, f = sum(r <= 10 for r in P), sum(r <= 10 for r in F)
    gate = (f"NON-TEST (P {p}/20, F {f}/20)" if p < 10 or f > 3 else ("SIGNAL" if rk <= 10 else "NO SIGNAL"))
    out = [("N_tokens", len(toks)), ("filtered_stream_tokens", len(st)), ("train_tokens", cut),
           ("W_target", f"{real:.4f}"), ("W_rank_of_201", rk), ("W_z", f"{z:.2f}"),
           ("P_ranks", " ".join(map(str, P))), ("P_rank_le10_of_20", p),
           ("F_ranks", " ".join(map(str, F))), ("F_rank_le10_of_20", f), ("gate", gate)]
    score = "stat\tvalue\n" + "".join(f"{a}\t{b}\n" for a, b in out)
    gl = {"82": "D. n.", "21": "Berry", "12": "b. Pal."}
    rows = ["pos\ttoken\tclass\tvalue\tkey_grade\tgrade\tf13r_gloss"]
    for i, t in enumerate(toks, 1):
        if t in PERSONS: rows.append(f"{i}\t{t}\tperson (overline absent on leaf)\t{'Roy' if t == '8' else 'Royne mere'}\tH\tM\t{gl.get(t, '')}")
        else: rows.append(f"{i}\t{t}\tMotz word (dot absent on leaf)\t{m[t][0]}\t{m[t][1]}\tM\t{gl.get(t, '')}")
    dec = "\n".join(rows) + "\n"
    if "--check" in sys.argv:
        ok = (H / "k71_allcode_decode.tsv").read_text() == dec and (H / "k71_allcode_score.tsv").read_text() == score
        print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    (H / "k71_allcode_decode.tsv").write_text(dec); (H / "k71_allcode_score.tsv").write_text(score)
    print(score); print(" ".join(decode(toks, m)))

if __name__ == "__main__":
    main()

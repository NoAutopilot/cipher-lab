#!/usr/bin/env python3
"""F4712-K71: key no.71 (fr.3995 f.133r) on fr.4712 f.10r S1, per PREREG-F4712-K71.md.
python3 k71_decode.py [--check]   writes k71_decode.tsv (per token) and k71_score.tsv; --check exits 1 if either is stale."""
import csv, random, re, statistics, sys
from collections import Counter
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[1] / "tools")); sys.path.insert(0, str(H))
import judge_plaintext as jp
from score_key1 import TOMO

def load_key():
    rows = [l for l in open(H / "keys/key_no71.tsv") if not l.startswith("#")]
    let, wrd = {}, {}
    for r in csv.DictReader(rows, delimiter="\t"):
        if r["kind"] == "letter":
            if r["code"] != "S": let[r["code"]] = (r["value"], r["grade"])
        else:
            wrd.setdefault(r["code"], []).append((r["value"], r["kind"], r["grade"]))
    return let, wrd

def norm(t): return str(int(t))

def corpus_words():
    t = " ".join(jp.read_corpus(p) for p in jp.LANG_CORPORA["fr16"])
    return [w.lower().translate(jp.FOLD) for w in re.findall(r"[A-Za-zéèêàçùûîôâëï']+", t)]

def encipher(words, let, wordcodes, rng, n=37):
    inv = {}
    for c, (v, g) in let.items(): inv.setdefault(v, []).append(c)
    sub = {"j": "i", "v": "u", "k": "c"}
    out = []
    for w in words:
        if w in wordcodes: out.append(wordcodes[w])
        else:
            for ch in re.sub(r"[^a-z]", "", w):
                ch = sub.get(ch, ch)
                if ch == "w": out += [rng.choice(inv["u"]), rng.choice(inv["u"])]
                elif ch == "x": continue          # non-numeric triangle, not counted
                elif ch in inv: out.append(rng.choice(inv[ch]))
        if len(out) >= n: break
    return out[:n]

def ctl(words, let, wordcodes, seed, n=37):
    rng = random.Random(seed); i = rng.randrange(len(words) - 400)
    return encipher(words[i:i + 400], let, wordcodes, rng, n)

def decode(toks, let, wrd):
    out = []
    for t in toks:
        c = norm(t)
        if c in let: out.append(let[c][0])
        elif c in wrd: out.append(wrd[c][0][0])
        else: out.append("?")
    return out

def shuffled(let, wrd, seed):
    rng = random.Random(seed)
    lc = list(let); lv = [let[c] for c in lc]; rng.shuffle(lv)
    wc = list(wrd); wv = [wrd[c] for c in wc]; rng.shuffle(wv)
    return dict(zip(lc, lv)), dict(zip(wc, wv))

def rank_z(model, toks, let, wrd, n=200):
    sc = lambda L, W: model.score("".join(x for x in decode(toks, L, W) if x != "?"))
    real = sc(let, wrd)
    null = [sc(*shuffled(let, wrd, s)) for s in range(1, n + 1)]
    return real, 1 + sum(x >= real for x in null), (real - statistics.mean(null)) / (statistics.pstdev(null) or 1e-9)

def pct(xs, p): xs = sorted(xs); return xs[min(len(xs) - 1, int(p * len(xs)))]

def main():
    let, wrd = load_key()
    toks = [t for l in TOMO for t in l]
    words = corpus_words()
    dot = {v: c for c, vs in wrd.items() for v, k, g in vs if k == "word" and " " not in v and "'" not in v}
    top = [w for w, _ in Counter(words).most_common(89)]
    gen = {w: str(11 + i) for i, w in enumerate(top)}
    L = lambda ts: sum(norm(t) in let for t in ts)
    Lt = L(toks)
    c1 = [L(ctl(words, let, dot, s)) for s in range(1000)]
    c2 = [L(ctl(words, let, gen, 10000 + s)) for s in range(1000)]
    rng = random.Random(99); n0 = [L([str(rng.randint(8, 99)) for _ in range(37)]) for _ in range(1000)]
    c2p05, c2p01, n0p95 = pct(c2, .05), pct(c2, .01), pct(n0, .95)
    gateD = ("CONSISTENT" if Lt >= c2p05 else "INCONSISTENT" if (Lt < c2p01 and c2p05 > n0p95) else "NON-TEST")
    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr16"]])
    real, rk, z = rank_z(model, toks, let, wrd)
    pw = 0
    for s in range(20):
        r_, k_, z_ = rank_z(model, ctl(words, let, dot, 50000 + s), let, wrd)
        pw += (k_ == 1 and z_ >= 3)
    gateR = "NON-TEST (power %d/20 < 10)" % pw if pw < 10 else ("SIGNAL" if rk == 1 and z >= 3 else "NO SIGNAL")
    st = [("N_tokens", 37), ("L_target", Lt),
          ("C1_mean", f"{statistics.mean(c1):.2f}"), ("C1_p05", pct(c1, .05)), ("C1_p01", pct(c1, .01)),
          ("C2_mean", f"{statistics.mean(c2):.2f}"), ("C2_p05", c2p05), ("C2_p01", c2p01),
          ("N0_mean", f"{statistics.mean(n0):.2f}"), ("N0_p95", n0p95), ("gate_D", gateD),
          ("R_target_score", f"{real:.3f}"), ("R_rank_of_201", rk), ("R_z", f"{z:.2f}"), ("R_power_of_20", pw), ("gate_R", gateR)]
    score = "stat\tvalue\n" + "".join(f"{a}\t{b}\n" for a, b in st)
    rows = ["pos\ttoken\tkind\tvalue\tgrade\tnote"]
    for i, t in enumerate(toks, 1):
        c = norm(t)
        if c in let:
            alt = "; also " + " / ".join(f"{v} ({k}, dotted/overlined on the key)" for v, k, g in wrd.get(c, [])) if c in wrd else ""
            rows.append(f"{i}\t{t}\tletter\t{let[c][0]}\tM\tkey row {let[c][1]}{alt}")
        elif c in wrd:
            rows.append(f"{i}\t{t}\tword/person\t{' / '.join(v for v, k, g in wrd[c])}\tM\tnot a letter code; value needs a mark the leaf lacks")
        else:
            rows.append(f"{i}\t{t}\tunread\t\t\tnot a letter code; word/person code not on the crop (unread)")
    dec = "\n".join(rows) + "\n"
    if "--check" in sys.argv:
        ok = (H / "k71_decode.tsv").read_text() == dec and (H / "k71_score.tsv").read_text() == score
        print("OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    (H / "k71_decode.tsv").write_text(dec); (H / "k71_score.tsv").write_text(score)
    print(score)

if __name__ == "__main__":
    main()

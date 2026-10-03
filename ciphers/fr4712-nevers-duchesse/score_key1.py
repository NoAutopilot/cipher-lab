#!/usr/bin/env python3
"""DUCH-KEY1B: apply fr.3995 key no.1 to fr.4712 f.10r under three segmentations and score per PREREG_duchkey1b.md.
python3 score_key1.py [--check]   writes key1_score.tsv and key1_readings.txt; --check exits 1 if either is stale."""
import csv, random, statistics, sys
from pathlib import Path
H = Path(__file__).resolve().parent
sys.path.insert(0, str(H.parents[1] / "tools"))
import judge_plaintext as jp

def load_key():
    rows = [l for l in open(H / "keys/key_no1.tsv") if not l.startswith("#")]
    return {r["code"]: (r["value"], r["kind"]) for r in csv.DictReader(rows, delimiter="\t")}

def load_lines():
    rows = [l for l in open(H / "ciphertext_f10_digits.tsv") if not l.startswith("#")]
    return [r["digits"].lstrip("S") for r in csv.DictReader(rows, delimiter="\t")]

TOMO = [l.split() for l in """82 82 52 14 10 85 92 21 60 13 16 52 74 56 92 8 59
31 72 10 78 12 69 20 21 22 95 85 25 12 19 93
10 24 17 81 26""".splitlines()]

def segs(lines):
    return {"S1_tomokiyo": TOMO,
            "S2_pairs_from_start": [[l[i:i+2] for i in range(0, len(l) - 1, 2)] for l in lines],
            "S3_pairs_from_offset1": [[l[i:i+2] for i in range(1, len(l) - 1, 2)] for l in lines]}

A1 = False  # amendment A1: code tokens are word breaks (no letters)

def decode(toks, key):
    out, unk = [], 0
    for line in toks:
        w = []
        for t in line:
            v = key.get(t)
            if v is None: unk += 1; w.append("?")
            elif v[1] == "null": continue
            elif v[1] == "letter": w.append(v[0])
            else: w.append(" / " if A1 else "[" + v[0] + "]")
        out.append(" ".join(w))
    return "\n".join(out), unk

def shuffled(key, seed):
    codes = [c for c in key]; vals = [key[c] for c in codes]
    random.Random(seed).shuffle(vals); return dict(zip(codes, vals))

def sc_(model, txt):
    if not A1: return model.score(txt)
    runs = [jp.fold(r) for r in txt.replace("\n", " / ").split(" / ")]
    tot = n = 0
    for r in runs:
        if len(r) >= model.n:
            k = len(r) - model.n + 1; tot += model.score(r) * k; n += k
    return tot / n if n else -9.9

def codeshare(toks, key):
    t = [x for l in toks for x in l]
    return sum(key.get(x, ("", ""))[1] == "code" for x in t) / len(t)

def rank_z(model, toks, key, n=200):
    real = sc_(model, decode(toks, key)[0])
    null = [sc_(model, decode(toks, shuffled(key, s))[0]) for s in range(1, n + 1)]
    rank = 1 + sum(x >= real for x in null)
    z = (real - statistics.mean(null)) / (statistics.pstdev(null) or 1e-9)
    return real, rank, z

def main():
    key, lines = load_key(), load_lines()
    model = jp.NgramModel([jp.read_corpus(p) for p in jp.LANG_CORPORA["fr"]])
    spec = {"judge": {"language": "fr", "min_word_cover": 0.5, "control_samples": 200}}
    rows, texts = ["segmentation\ttokens\tunkeyed\tletters\tscore\trank_of_201\tz\tjudge\tnull_p99\treal_p05\tcover"], []
    for name, toks in segs(lines).items():
        txt, unk = decode(toks, key)
        sc, rk, z = rank_z(model, toks, key)
        j = jp.judge(spec, txt)["checks"]; lang = j["language"]
        ok = "PASS" if all(c["pass"] for c in j.values()) else "FAIL"
        rows.append(f"{name}\t{sum(map(len, toks))}\t{unk}\t{len(jp.fold(txt))}\t{sc:.3f}\t{rk}\t{z:.2f}\t{ok}\t{lang['null_p99']}\t{lang['real_p05']}\t{j['words']['cover']}")
        texts.append(f"## {name}\n{txt}\n")
    # power control: synthetic French, enciphered with key no.1 letters only, 37 tokens, 3% digit error, S2 segmentation
    rnd = random.Random(7); inv = {}
    for c, (v, k) in key.items():
        if k == "letter": inv.setdefault(v, []).append(c)
    inv.setdefault("v", inv["u"]); inv.setdefault("j", inv["i"]); inv.setdefault("k", inv["c"]); inv.setdefault("w", inv["u"])
    hits, prow = 0, []
    for t in range(20):
        j0 = rnd.randrange(len(model.raw) - 200); s = model.raw[j0:j0 + 37]
        digits = "".join(rnd.choice(inv[ch]) for ch in s)
        digits = "".join(rnd.choice("0123456789") if rnd.random() < 0.03 else d for d in digits)
        toks = [[digits[i:i+2] for i in range(0, len(digits) - 1, 2)]]
        sc, rk, z = rank_z(model, toks, key)
        hits += (rk == 1 and z >= 3); prow.append(f"{rk}/{z:.1f}")
    rows.append(f"POWER_control_20x37tok_3pct\t37\t-\t37\t-\t-\t-\tpower={hits}/20\t-\t-\t" + " ".join(prow))
    return "\n".join(rows) + "\n", "\n".join(texts)

if __name__ == "__main__":
    if "--a1" in sys.argv:
        A1 = True
        key, lines = load_key(), load_lines()
        tsv, rd = main()
        shares = [f"{n}: real {codeshare(t, key):.2f} vs shuffles mean {statistics.mean(codeshare(t, shuffled(key, s)) for s in range(1, 201)):.2f}" for n, t in segs(lines).items()]
        tsv += "# A1 code-token share: " + "; ".join(shares) + "\n"
        out, outr = H / "key1_score_A1.tsv", H / "key1_readings_A1.txt"
        if "--check" in sys.argv:
            st = out.read_text() != tsv or outr.read_text() != rd
            print("STALE" if st else "OK"); sys.exit(1 if st else 0)
        out.write_text(tsv); outr.write_text(rd); print(tsv); print(rd); sys.exit(0)
    tsv, rd = main()
    if "--check" in sys.argv:
        stale = (H / "key1_score.tsv").read_text() != tsv or (H / "key1_readings.txt").read_text() != rd
        print("STALE" if stale else "OK"); sys.exit(1 if stale else 0)
    (H / "key1_score.tsv").write_text(tsv); (H / "key1_readings.txt").write_text(rd)
    print(tsv); print(rd)

"""JVN-LVN (7 Oct 2026): jan-van-nassau-1572-75/key_5549.tsv on lodewijk letters 4610 and 4616, vs 20 value-shuffled
copies of the same key (rule 3 matched control: same key, same N, same codes; only the code->value map is permuted, so
the fr16 4-gram score and word cover CAN differ -- token-class coverage cannot, and is reported only as a count).
Reference rows: this folder's key.tsv and key_full.tsv under the same instrument. Disk only, no network.
  python3 ciphers/lodewijk-van-nassau-1573-74/jvnlvn/run.py   -> jvnlvn/results.json, jvnlvn/<letter>_<key>.txt
"""
import csv, json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); T = os.path.join(HERE, "..")
sys.path.insert(0, os.path.join(T, "..", "..", "tools"))
import judge_plaintext as J
KEYS = {"key_5549": os.path.join(T, "..", "jan-van-nassau-1572-75", "key_5549.tsv"),
        "key": os.path.join(T, "key.tsv"), "key_full": os.path.join(T, "key_full.tsv")}
NONSIGN = {"[blank]", "[blot]", "[spot]"}
NSHUF = 20

def read_key(p):
    with open(p, encoding="utf-8") as f:
        return {r["code"].strip(): r["value"].strip() for r in csv.DictReader(f, delimiter="\t")}

def shuffled(key, seed):
    codes = list(key); vals = [key[c] for c in codes]; random.Random(seed).shuffle(vals)
    return dict(zip(codes, vals))

def read_ct(letter):
    lines = {}
    with open(os.path.join(T, f"ciphertext_{letter}.tsv"), encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            lines.setdefault(r["line"], []).append(r["sign"].strip())
    return lines

def decode(key, lines):
    cls = dict(clear=0, letter=0, word=0, null=0, unknown=0); out = []
    for toks in lines.values():
        s = ""
        for t in toks:
            if t in NONSIGN or not t:
                continue
            if t.startswith("="):
                cls["clear"] += 1; continue          # clear words excluded: score only what the key produces
            v = key.get(t)
            if v is None or v in ("", "?"):
                cls["unknown"] += 1; s += " "; continue
            if v == "NULL":
                cls["null"] += 1; continue
            f = J.fold(v); cls["letter" if len(f) == 1 else "word"] += 1; s += f
        out.append(s)
    return "\n".join(out), cls

def main():
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["fr"]])
    res = {}
    for letter in ("4610", "4616"):
        lines = read_ct(letter)
        for name, p in KEYS.items():
            key = read_key(p); txt, cls = decode(key, lines); L = J.fold(txt)
            ss, sc = [], []
            for s in range(1, NSHUF + 1):
                t2 = J.fold(decode(shuffled(key, s), lines)[0]); ss.append(model.score(t2)); sc.append(model.cover(t2))
            open(os.path.join(HERE, f"{letter}_{name}.txt"), "w").write(txt + "\n")
            res[f"{letter}/{name}"] = dict(classes=cls, letters=len(L.replace(" ", "").replace("\n", "")),
                lm_real=round(model.score(L), 3), lm_shuf_mean=round(sum(ss) / NSHUF, 3), lm_shuf_max=round(max(ss), 3),
                cover_real=round(model.cover(L), 3), cover_shuf_mean=round(sum(sc) / NSHUF, 3), cover_shuf_max=round(max(sc), 3))
    json.dump(res, open(os.path.join(HERE, "results.json"), "w"), indent=1)
    for k, v in res.items():
        print(k, v)

if __name__ == "__main__":
    main()

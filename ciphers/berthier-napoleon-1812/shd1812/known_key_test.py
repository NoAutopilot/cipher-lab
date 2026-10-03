#!/usr/bin/env python3
"""GF4d (3 Oct 2026): does the SHD 1812 Spanish-campaign grand chiffre read the 22 Dec 1812 Berthier page?

Key: key_shd1812.tsv, the entries of the SHD deciphering table (codes 1-1400) for the 207 codes the target uses, read
from J.-F. Bouchaudy's photographs (jfbouch.fr/crypto/napoleon/IMG/1812_0001/0051/0701/0751.jpg, fetched 3 Oct 2026)
by two blind passes and a reconciliation. Key class `published` (Bouchaudy's images of the SHD table), not H for this
letter unless the test below shows it is this letter's key.

Statistic: decode the 325 target tokens with the key (each entry's first form: "facile, s, ite, ment" -> "facile";
blank or unread -> nothing) and score the letters with the add-k 4-gram model of tools/judge_plaintext.py trained on
tools/data/fr1810 (Napoleonic official/military French, built for this target). Higher = more French.
Null (rule 3): 200 shuffled keys -- the same 207 entries reassigned at random to the same 207 codes, so the entry
inventory is fixed and only the code->entry identity is broken. A key that is this letter's key scores far above
its shuffles; p = share of shuffles >= observed.
Positive control (matched design, N, language): Berthier's own Dec 1812 letters (Chuquet 1912, scripts/letters.json,
XIX and XXIII left out) encoded with a synthetic two-part code of the same shape (frequent words whole, other words
cut into 2-3 letter syllables, codes drawn at random from 1-1400), first 325 code tokens; the true synthetic key vs
200 of its own shuffles, at 0, 15 and 30 percent of key entries replaced by wrong entries (bracketing a table
transcription error rate). `--check` exits 1 if the committed results are stale (rule 7).
"""
import csv, gzip, json, random, re, sys, pathlib
HERE = pathlib.Path(__file__).resolve().parent
TGT = HERE.parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus, fold  # noqa: E402

DRAWS, SEED, N = 200, 1812, 325


def base(entry):
    e = entry.strip()
    if e in ("", "(blank)", "?"): return ""
    e = re.sub(r"\[\?\]|\^", "", e)
    return e.split(",")[0].strip()


def load_key():
    k = {}
    with open(HERE / "key_shd1812.tsv", encoding="utf-8") as f:
        for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"):
            k[int(r["code"])] = base(r["entry"])
    return k


def model():
    fs = sorted((ROOT / "tools/data/fr1810").glob("*.txt.gz"))
    return NgramModel([read_corpus(p) for p in fs])


def test(tokens, key, m, rng):
    codes = sorted(set(tokens))
    obs = m.score("".join(key.get(t, "") for t in tokens))
    vals = [key.get(c, "") for c in codes]; ge = 0; xs = []
    for _ in range(DRAWS):
        rng.shuffle(vals); kk = dict(zip(codes, vals))
        s = m.score("".join(kk[t] for t in tokens)); xs.append(s); ge += s >= obs
    xs.sort()
    return {"obs": round(obs, 4), "null_mean": round(sum(xs) / len(xs), 4), "null_max": round(xs[-1], 4),
            "p": round((ge + 1) / (DRAWS + 1), 4)}


def synthetic(m, rng):
    L = json.load(open(TGT / "scripts/letters.json", encoding="utf-8"))
    text = " ".join(v["text"] for k, v in L.items() if k not in ("XIX", "XXIII"))
    words = [fold(w) for w in re.findall(r"[^\W\d_]+", text)]
    words = [w for w in words if w]
    freq = {}
    for w in words: freq[w] = freq.get(w, 0) + 1
    whole = {w for w, n in sorted(freq.items(), key=lambda x: -x[1])[:300]}
    units = []
    for w in words:
        if w in whole: units.append(w)
        else: units += [w[i:i + 3] for i in range(0, len(w), 3)]
        if len(units) >= N: break
    units = units[:N]
    inv = sorted(set(units)); codes = rng.sample(range(1, 1401), len(inv))
    key = dict(zip(codes, inv)); enc = dict(zip(inv, codes))
    return [enc[u] for u in units], key, inv


def main():
    rng = random.Random(SEED); m = model()
    target = [int(x) for x in (TGT / "structure/flat.txt").read_text().split()]
    key = load_key()
    res = {"n_target": len(target), "distinct": len(set(target)), "key_rows": len(key),
           "key_nonblank_for_target": sum(1 for c in set(target) if key.get(c)), "draws": DRAWS, "seed": SEED,
           "corpus": "tools/data/fr1810"}
    res["target"] = test(target, key, m, rng)
    res["target_decode_first80"] = " ".join(key.get(t, "") or "_" for t in target[:80])
    toks, skey, inv = synthetic(m, rng)
    res["control_n"] = len(toks); res["control_distinct"] = len(set(toks))
    rows = {}
    for err in (0, 15, 30):
        k2 = dict(skey); bad = rng.sample(sorted(k2), round(len(k2) * err / 100))
        for c in bad: k2[c] = rng.choice(inv)
        rows[f"err{err}"] = test(toks, k2, m, rng)
    res["positive_control"] = rows
    out = json.dumps(res, indent=1, ensure_ascii=False)
    f = HERE / "known_key_results.json"
    if "--check" in sys.argv:
        if not f.exists() or f.read_text(encoding="utf-8") != out + "\n": print("STALE"); sys.exit(1)
        print("OK"); return
    f.write_text(out + "\n", encoding="utf-8"); print(out)


if __name__ == "__main__":
    main()

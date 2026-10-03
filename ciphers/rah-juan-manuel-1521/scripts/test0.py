#!/usr/bin/env python3
"""Test 0 for rah-juan-manuel-1521 (LANE-POOLS FT-A, 3 Oct 2026).

Tomokiyo's Juan Manuel nomenclator (sources/cryptiana/keys/AlonsoSanchez_2.tsv, word codes only -- his page gives no
letter alphabet) applied to transcribed code groups, with two statistics a value-shuffle CAN change (rule 3):

  KA (known answer, R9528 f.194 vs the period decipherment f.197): decoded code words aligned to the clerk's text by
     word-level LCS; score = matched decoded words / decoded words. In-sample for Tomokiyo (he built the table from
     this page): it calibrates the transcription, not the key.
  BG (no gloss, R9501 f.34 and, as reference, f.194): share of adjacent decoded code-word pairs whose word bigram
     occurs in the Spanish corpus tools/data/es17c (1640s newsletters -- NOT era-matched to 1522; no 16th-c. Spanish
     corpus is on disk).
Null for both: 200 tables with the key's values permuted among its code rows (seed 1..200).
Coverage (share of plain-letter groups that are key codes) is printed as description only: it cannot change under a
value shuffle, so it is not a test.

  python3 scripts/test0.py [--shuffles 200] [--check]     (--check: exit 1 if results.json differs)
"""
import argparse, gzip, json, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
ROOT = HERE.parent.parent
KEY = ROOT / "sources/cryptiana/keys/AlonsoSanchez_2.tsv"
CORPUS = sorted((ROOT / "tools/data/es17c").glob("*.txt.gz"))


def norm(w):
    w = w.lower().replace("(h)", "h").replace("(e)", "e")
    w = re.sub(r"[^a-zñç]", "", w)
    return w.replace("j", "i").replace("v", "u").replace("y", "i").replace("ç", "z").replace("h", "")


def load_key():
    codes = {}
    for line in KEY.read_text().splitlines():
        if not line or line.startswith("#") or line.startswith("sign\t"):
            continue
        f = line.split("\t")
        codes.setdefault(f[0].strip(), f[1].strip())
    return codes


def load_cipher(path):
    """rows of (line, [token...]); bracketed clear runs become a single CLEAR marker (break adjacency)."""
    out = []
    for line in path.read_text().splitlines()[1:]:
        if not line.strip():
            continue
        ln, toks = line.split("\t", 1)
        toks = re.sub(r"\[[^\]]*\]", " CLEAR ", toks)
        out.append((ln, toks.split()))
    return out


def stream(rows):
    return [t for _, ts in rows for t in ts]


def decode(toks, table):
    """list of decoded word-lists or None per token (None = unknown/symbol/clear: breaks adjacency)."""
    res = []
    for t in toks:
        g = t.rstrip("^").lower()
        if g in table:
            res.append([norm(x) for x in table[g].split() if norm(x)])
        else:
            res.append(None)
    return res


def same(a, b):
    if a == b:
        return True
    s, l = sorted((a, b), key=len)
    return len(s) >= 4 and l.startswith(s)


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if same(x, y) else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def ka_score(toks, gloss, table):
    words = [w for d in decode(toks, table) if d for w in d]
    return (lcs(words, gloss) / len(words) if words else 0.0), len(words)


def corpus_bigrams():
    bg = set()
    for p in CORPUS:
        ws = [norm(w) for w in re.findall(r"[A-Za-zÁÉÍÓÚáéíóúñÑçÇ]+", gzip.open(p, "rt", errors="ignore").read())]
        ws = [w for w in ws if w]
        bg.update(zip(ws, ws[1:]))
    return bg


def bg_score(toks, table, bg):
    d = decode(toks, table)
    pairs = hit = 0
    for a, b in zip(d, d[1:]):
        if a and b:
            pairs += 1
            hit += (a[-1], b[0]) in bg
    return (hit / pairs if pairs else 0.0), pairs


def coverage(toks, table):
    plain = [t.rstrip("^").lower() for t in toks if t != "CLEAR" and re.fullmatch(r"[a-z]+\^?", t.lower())]
    return sum(p in table for p in plain), len(plain)


def shuffled(table, seed):
    ks, vs = list(table), list(table.values())
    random.Random(seed).shuffle(vs)
    return dict(zip(ks, vs))


def summary(real, null):
    s = sorted(null)
    m = sum(s) / len(s)
    sd = (sum((x - m) ** 2 for x in s) / len(s)) ** 0.5
    return {"real": round(real, 4), "null_mean": round(m, 4), "null_sd": round(sd, 4),
            "null_p95": round(s[int(0.95 * len(s)) - 1], 4), "null_max": round(s[-1], 4),
            "rank": 1 + sum(x >= real for x in s), "of": len(s) + 1}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    table = load_key()
    f194 = stream(load_cipher(HERE / "ciphertext_f194.tsv"))
    f34 = stream(load_cipher(HERE / "ciphertext_f34.tsv"))
    gloss = [norm(w) for line in (HERE / "gloss_f197.tsv").read_text().splitlines()[1:] if line.strip()
             for w in line.split("\t")[1].split() if norm(w) and not w.startswith("[?")]
    bg = corpus_bigrams()
    tabs = [shuffled(table, s) for s in range(1, a.shuffles + 1)]
    out = {}
    r, n = ka_score(f194, gloss, table)
    out["KA_f194_vs_f197"] = summary(r, [ka_score(f194, gloss, t)[0] for t in tabs]) | {"N_decoded_words": n, "N_gloss_words": len(gloss)}
    for name, toks in (("BG_f34_target", f34), ("BG_f194_reference", f194)):
        r, n = bg_score(toks, table, bg)
        out[name] = summary(r, [bg_score(toks, t, bg)[0] for t in tabs]) | {"N_pairs": n}
    for name, toks in (("coverage_f194", f194), ("coverage_f34", f34)):
        h, n = coverage(toks, table)
        out[name] = {"in_key": h, "plain_groups": n, "share": round(h / n, 4) if n else 0, "note": "descriptive only (shuffle-invariant)"}
    dec = decode(f34, table)
    out["f34_decoded_words"] = " ".join("/".join(d) if d else "_" for d in dec)
    txt = json.dumps(out, indent=1, ensure_ascii=False)
    res = HERE / "results.json"
    if a.check:
        ok = res.exists() and res.read_text().strip() == txt.strip()
        print("results.json", "current" if ok else "STALE")
        sys.exit(0 if ok else 1)
    res.write_text(txt + "\n")
    print(txt)


if __name__ == "__main__":
    main()

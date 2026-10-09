#!/usr/bin/env python3
"""SUR-372 key test (PREREG-SUR372.md): NA 1.05.03 inv. 372 scan 0189 right page, glossed cipher letter of 26 July 1780.

Decodes each blind pass (passes/sur372/pass{A,B,R}.tsv) under the Oud and the Nieuw period keys (inv. 86 scans 0002 and
0003) with the reader-code tables below (fixed from the sheets' shape names before the passes returned), and scores:
  S1 difflib ratio decode-letters vs the same pass's gloss letters (page order), vs 200 key-shuffled and 200
     shuffled-target nulls (p95); S2 nl18 judge (real_p05 / null_p99) on the decode and on one shuffled-target decode;
  S3 nl18 word-hit share vs the same nulls.
Writes passes/sur372/score.tsv and reading_sur372_<key>_<pass>.txt. --check: exit 1 if score.tsv is stale.
Usage: python3 ciphers/na-suriname-map-1781/score_sur372.py [--check]
"""
import difflib, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parents[1] / "tools"))
from judge_plaintext import LANG_CORPORA, NgramModel, pct, read_corpus  # noqa: E402

P = HERE / "passes" / "sur372"
SEED, NSAMP = 372, 200

# reader code -> letter, by the sheets' shape names (key_period.tsv = Oud, key_period_nieuw.tsv = Nieuw)
COMMON = {"3": "e", "7": "e", "a": "e", "e": "e", "v": "d", "w": "d", "[amp]": "f", "[omega-bar]": "f", "f": "i",
          "m": "i", "c": "l", "h": "n", "l": "n", "k": "o", "[hash]": "o", "[pi]": "o", "S": "p", "s": "p", "q": "p",
          "0": "r", "o": "r", "6": "s", "[psi]": "s", "r": "t", "[lambda]": "t", "5": "u", "4": "w", "[sigma]": "b",
          "[delta]": "a", "C": "c", "[ij]": "n", "x": "q"}
OUD = dict(COMMON, **{"2": "a", "P": "a", "D": "b", "d": "b", "A": "e", "8": "g", "H": "h", "9": "i", "B": "k",
                      "b": "k", "G": "l", "g": "l", "Y": "m", "y": "m", "L": "n", "R": "t", "E": "u", "[I-bar]": "x",
                      "[tau]": "y", "t": "y", "N": "z", "n": "z"})
NIEUW = dict(COMMON, **{"p": "a", "[x-dots]": "a", "d": "b", "9": "g", "[sh-lig]": "h", "[s-dollar]": "h", "8": "i",
                        "b": "k", "g": "l", "y": "m", "[x-cross]": "q", "1": "x", "t": "y", "n": "z"})
KEYS = {"oud": OUD, "nieuw": NIEUW}


def norm(s):
    s = s.lower().replace("ij", "i").replace("ÿ", "i")
    s = s.translate(str.maketrans("yjv", "iiu"))
    return re.sub(r"[^a-z]", "", s)


def load(name):
    gloss, cipher = [], []
    for ln in (P / f"pass{name}.tsv").read_text(encoding="utf-8").splitlines():
        parts = ln.split("\t")
        if len(parts) < 3:
            continue
        kind, content = parts[1].strip(), parts[2]
        if kind == "gloss":
            gloss.append(re.sub(r"\[\.\.\.\]", " ", content))
        elif kind == "cipher":
            content = re.sub(r"\{[^}]*\}", " ", content)
            toks = [t.rstrip("?") if len(t) > 1 else t for t in content.split()]
            cipher.append(toks)
    return " ".join(gloss), cipher


def decode(lines, key):
    words, cur = [], ""
    for toks in lines:
        for t in toks:
            if t == "_" or t in ",.:;-—" or not t:
                if cur:
                    words.append(cur)
                cur = ""
            else:
                cur += key.get(t, "?")
        if cur:
            words.append(cur)
        cur = ""
    return words


def s1(words, gl):
    return difflib.SequenceMatcher(None, norm("".join(words)), gl, autojunk=False).ratio()


def main(check=False):
    texts = [read_corpus(p) for p in LANG_CORPORA["nl18"]]
    model = NgramModel(texts)
    vocab = Counter()
    for t in texts:
        vocab.update(norm(w) for w in re.findall(r"[A-Za-zÀ-ÿ]+", t))
    lex = {w for w, c in vocab.items() if c >= 3 and len(w) >= 2}

    def s3(words):
        ws = [norm(w) for w in words if len(norm(w)) >= 2 and "?" not in w]
        return sum(w in lex for w in ws) / max(1, len(ws))

    rows = []
    for pname in ("A", "B", "R"):
        if not (P / f"pass{pname}.tsv").exists():
            continue
        gtxt, lines = load(pname)
        gl = norm(gtxt)
        signs = sorted({t for l in lines for t in l if t not in ("_",) and t not in ",.:;-—"})
        for kname, key in KEYS.items():
            words = decode(lines, key)
            letters = norm("".join(words))
            (HERE / f"reading_sur372_{kname}_{pname}.txt").write_text(
                f"# SUR-372 inv.372 0189R decode, key {kname}, pass {pname} (score_sur372.py); '?' = sign not in key\n"
                + " ".join(words) + "\n", encoding="utf-8")
            real1, real3 = s1(words, gl), s3(words)
            rnd = random.Random(SEED)
            ks1, ks3, ts1, ts3 = [], [], [], []
            ksigns = [s for s in signs if s in key]
            for _ in range(NSAMP):
                vals = [key[s] for s in ksigns]; rnd.shuffle(vals)
                k2 = dict(key); k2.update(zip(ksigns, vals))
                w = decode(lines, k2); ks1.append(s1(w, gl)); ks3.append(s3(w))
                flat = [t for l in lines for t in l]; rnd.shuffle(flat)
                w = decode([flat], key); ts1.append(s1(w, gl)); ts3.append(s3(w))
            N = len(letters)
            realj, nullj, _ = model.controls(N, samples=NSAMP, seed=1)
            r05, n99 = pct(realj, 0.05), pct(nullj, 0.99)
            jsc = model.score(letters)
            flat = [t for l in lines for t in l]; random.Random(SEED + 1).shuffle(flat)
            jsh = model.score(norm("".join(decode([flat], key))))
            unk = sum(1 for l in lines for t in l if t not in key and t != "_" and t not in ",.:;-—")
            row = dict(pass_=pname, key=kname, tokens=sum(len(l) for l in lines), unkeyed=unk, letters=N,
                       gloss_letters=len(gl),
                       S1=round(real1, 3), S1_keyshuf_p95=round(pct(ks1, .95), 3), S1_tgtshuf_p95=round(pct(ts1, .95), 3),
                       S1_gate="PASS" if real1 > pct(ks1, .95) and real1 > pct(ts1, .95) else "FAIL",
                       S3=round(real3, 3), S3_keyshuf_p95=round(pct(ks3, .95), 3), S3_tgtshuf_p95=round(pct(ts3, .95), 3),
                       S2_score=round(jsc, 3), S2_real_p05=round(r05, 3), S2_null_p99=round(n99, 3),
                       S2="PASS" if jsc > r05 and jsc > n99 else "FAIL", S2_tgtshuf_score=round(jsh, 3),
                       S2_tgtshuf="PASS" if jsh > r05 and jsh > n99 else "FAIL")
            rows.append(row)
    out = "\t".join(rows[0].keys()) + "\n" + "".join("\t".join(str(v) for v in r.values()) + "\n" for r in rows)
    f = P / "score.tsv"
    if check:
        ok = f.exists() and f.read_text() == out
        print("score.tsv", "current" if ok else "STALE"); sys.exit(0 if ok else 1)
    f.write_text(out); print(out)


if __name__ == "__main__":
    main("--check" in sys.argv)

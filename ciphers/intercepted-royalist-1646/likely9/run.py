#!/usr/bin/env python3
"""likely9/run.py -- first cheap test for ciphers/intercepted-royalist-1646 (LIKELY-9, 2 Oct 2026, account-4).

CLAUDE.md rule 3: key129 (key.tsv, Aymeloglu's reconstruction of Digby-cabinet key no. 129) applied to f10_ct.tsv
(715 cipher tokens + 20 illegible) and f9_ct.tsv (151), scored against value-shuffled copies of the same key.
A shuffled key keeps the code set, so *coverage* cannot differ (the bCAS lesson); the statistics below depend on
which value lands where:
  lm     mean log10 4-gram letter probability (tools/judge_plaintext.py's NgramModel) over every maximal readable run
         (clear words + keyed tokens, unkeyed tokens break a run) that contains at least one keyed token
  wbg    mean log10 P(w2|w1) (add-k word bigram with unigram backoff, same corpora) over adjacent readable word pairs
         with at least one keyed token
  cover  NgramModel.cover over the same keyed runs
Shuffles: 'full' permutes all 65 values among the 65 codes (the brief's control, 20 seeds; 200 as a supplement);
'strat' permutes letters among letter codes and words/names among word codes (harder; supplement).
Also writes the judge inputs: text_f10.txt (readable text, unkeyed tokens dropped), text_f10_shuffled_target.txt
(cipher tokens permuted among cipher positions, clear words left in place, seed 1), text_f9.txt.
Disk only.  python3 ciphers/intercepted-royalist-1646/likely9/run.py
"""
import json, random, re, statistics, sys
from collections import Counter
from pathlib import Path
ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import NgramModel, read_corpus, fold, DATA  # noqa: E402

T = ROOT / "ciphers/intercepted-royalist-1646"
OUT = T / "likely9"
EN16 = sorted((DATA / "en16_repo").glob("*.txt"))
EN = [DATA / "pg1661_holmes.txt", DATA / "pg2701_mobydick.txt"]


def load_ct(p):
    rows = []
    for l in open(p, encoding="utf-8"):
        if l.startswith("#") or l.startswith("line\t") or not l.strip():
            continue
        line, pos, sign, conf = l.rstrip("\n").split("\t")
        rows.append((int(line), int(pos), sign, conf))
    return rows


def load_key(p):
    key = {}
    for l in open(p, encoding="utf-8"):
        if l.startswith("#") or l.startswith("code\t") or not l.strip():
            continue
        code, value, grade, source = l.rstrip("\n").split("\t")
        key[code] = (value, grade, source)
    return key


def units(rows, key):
    """list of (kind, text): kind clear | keyed | gap. Consecutive keyed letters join into one word unit."""
    out = []
    for _, _, sign, conf in rows:
        if sign.startswith("[PLAIN:"):
            for w in sign[7:-1].split("_"):
                out.append(("clear", w))
        elif sign in key:
            v = key[sign]
            if len(v) == 1 and out and out[-1][0] == "keyedletter":
                out[-1] = ("keyedletter", out[-1][1] + v)
            else:
                out.append(("keyedletter" if len(v) == 1 else "keyed", v))
        else:
            out.append(("gap", sign))
    return [("keyed" if k == "keyedletter" else k, t) for k, t in out]


def runs(us):
    """maximal readable runs: lists of (kind, text) between gaps."""
    cur, res = [], []
    for k, t in us:
        if k == "gap":
            if cur:
                res.append(cur); cur = []
        else:
            cur.append((k, t))
    if cur:
        res.append(cur)
    return res


class WordBigram:
    def __init__(self, texts, k=0.1):
        self.k = k; self.bg = Counter(); self.ug = Counter()
        for t in texts:
            ws = [w.lower() for w in re.findall(r"[A-Za-z]+", t)]
            self.ug.update(ws); self.bg.update(zip(ws, ws[1:]))
        self.V = len(self.ug); self.N = sum(self.ug.values())

    def lp(self, a, b):
        import math
        pu = (self.ug.get(b, 0) + self.k) / (self.N + self.k * self.V)
        ca = self.ug.get(a, 0)
        return math.log10((self.bg.get((a, b), 0) + self.k * pu * self.V) / (ca + self.k * self.V))


def stats(rows, key, model, wb):
    us = units(rows, key)
    keyed_runs = [r for r in runs(us) if any(k == "keyed" for k, _ in r)]
    texts = ["".join(t for _, t in r) for r in keyed_runs]
    letters = sum(len(fold(t)) for t in texts)
    # letter-weighted lm over runs of >= 4 letters
    num = den = 0.0
    for t in texts:
        f = fold(t)
        if len(f) >= 4:
            num += model.score(f) * (len(f) - 3); den += len(f) - 3
    lm = num / den if den else float("nan")
    cov = sum(model.cover(t) * len(fold(t)) for t in texts) / letters if letters else float("nan")
    pairs = []
    for r in keyed_runs:
        for (k1, w1), (k2, w2) in zip(r, r[1:]):
            if "keyed" in (k1, k2):
                pairs.append((fold(w1), fold(w2)))
    wbg = statistics.mean(wb.lp(a, b) for a, b in pairs) if pairs else float("nan")
    return {"lm": lm, "cover": cov, "wbg": wbg, "letters": letters, "pairs": len(pairs), "runs": len(keyed_runs)}


def shuffled_keys(key, mode, seeds):
    codes = list(key); vals = [key[c] for c in codes]
    for s in seeds:
        rnd = random.Random(s)
        if mode == "full":
            v = vals[:]; rnd.shuffle(v)
            yield dict(zip(codes, v))
        else:
            L = [c for c in codes if len(key[c]) == 1]; W = [c for c in codes if len(key[c]) > 1]
            lv = [key[c] for c in L]; wv = [key[c] for c in W]; rnd.shuffle(lv); rnd.shuffle(wv)
            d = dict(zip(L, lv)); d.update(zip(W, wv)); yield d


def summarize(real, ctrl):
    xs = [c for c in ctrl if c == c]
    if not xs or real != real:
        return {"real": None, "ctrl_mean": None, "ctrl_max": None, "ctrl_sd": None, "z": None, "rank": "n/a (no keyed pairs or runs)"}
    mean = statistics.mean(xs); sd = statistics.pstdev(xs) if len(xs) > 1 else 0.0
    rank = 1 + sum(1 for x in xs if x >= real)
    return {"real": round(real, 4), "ctrl_mean": round(mean, 4), "ctrl_max": round(max(xs), 4), "ctrl_sd": round(sd, 4),
            "z": round((real - mean) / sd, 2) if sd else None, "rank": f"{rank}/{len(xs) + 1}"}


def text_of(rows, key):
    return " ".join(t for k, t in units(rows, key) if k != "gap")


def main():
    # optional: --grades H,M restricts the key to rows of those grades (writes results_<grades>.json, no texts)
    grades = None
    if len(sys.argv) > 2 and sys.argv[1] == "--grades":
        grades = set(sys.argv[2].split(","))
    key_full = load_key(T / "key.tsv"); key = {c: v[0] for c, v in key_full.items() if not grades or v[1] in grades}
    models = {"en16_repo": (NgramModel([read_corpus(p) for p in EN16]), WordBigram([read_corpus(p) for p in EN16])),
              "en": (NgramModel([read_corpus(p) for p in EN]), WordBigram([read_corpus(p) for p in EN]))}
    res = {"key_codes": len(key), "corpora": {"en16_repo": [p.name for p in EN16], "en": [p.name for p in EN]}, "jobs": {}}
    for job in ("f10", "f9"):
        rows = load_ct(T / f"{job}_ct.tsv")
        res["jobs"][job] = {"cipher_tokens": sum(1 for r in rows if not r[2].startswith("[PLAIN:")),
                            "keyed_tokens": sum(1 for r in rows if r[2] in key)}
        if not grades:
            (OUT / f"text_{job}.txt").write_text(text_of(rows, key) + "\n")
        for mname, (model, wb) in models.items():
            real = stats(rows, key, model, wb)
            block = {"real": real}
            for mode, seeds in (("full", range(1, 21)), ("full200", range(1, 201)), ("strat", range(1, 21))):
                ctrl = [stats(rows, k, model, wb) for k in shuffled_keys(key, "strat" if mode == "strat" else "full", seeds)]
                block[mode] = {st: summarize(real[st], [c[st] for c in ctrl]) for st in ("lm", "wbg", "cover")}
            res["jobs"][job][mname] = block
    # shuffled target (f10): cipher tokens permuted among cipher positions, clear words fixed, seed 1
    rows = load_ct(T / "f10_ct.tsv"); rnd = random.Random(1)
    idx = [i for i, r in enumerate(rows) if not r[2].startswith("[PLAIN:")]
    perm = idx[:]; rnd.shuffle(perm); sh = rows[:]
    for i, j in zip(idx, perm):
        sh[i] = rows[j]
    if not grades:
        (OUT / "text_f10_shuffled_target.txt").write_text(text_of(sh, key) + "\n")
    (OUT / ("results.json" if not grades else "results_" + "".join(sorted(grades)) + ".json")).write_text(json.dumps(res, indent=1))
    print("key codes used:", len(key), "grades:", sorted(grades) if grades else "all")
    for job, b in res["jobs"].items():
        print(f"{job}: cipher tokens {b['cipher_tokens']}, keyed {b['keyed_tokens']}")
        for m in models:
            r = b[m]["real"]
            print(f"  [{m}] real: letters {r['letters']} runs {r['runs']} pairs {r['pairs']}")
            for mode in ("full", "full200", "strat"):
                for st in ("lm", "wbg", "cover"):
                    s = b[m][mode][st]
                    if s["real"] is None:
                        print(f"    {mode:8s} {st:6s} {s['rank']}"); continue
                    print(f"    {mode:8s} {st:6s} real {s['real']:8.4f}  ctrl mean {s['ctrl_mean']:8.4f} max {s['ctrl_max']:8.4f} sd {s['ctrl_sd']:.4f}  z {s['z']}  rank {s['rank']}")


if __name__ == "__main__":
    main()

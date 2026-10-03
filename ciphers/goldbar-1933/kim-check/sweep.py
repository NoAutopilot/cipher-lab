"""CHECK-GOLDBAR (3 Oct 2026): the look-elsewhere control for Milton Kim's Swiss-K Enigma readings.
For a ciphertext line and a ring, decode under all 17,576 keys (numpy, same conventions as enigma_k.KIM_CFG) and
report (1) the keys whose decode contains a target word, (2) the best English 4-gram score and best word-cover over
all keys. Run on the real lines and on random lines of the same length (the control: the ciphertext changes, so the
statistic can differ). Usage: python3 sweep.py [--n-random 100] [--out sweep_result.json]"""
import json, random, sys, argparse
from pathlib import Path
import numpy as np
sys.path.insert(0, str(Path(__file__).resolve().parent))
sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from enigma_k import A, ROT, UKW, inv, KIM_CFG, kim, Enigma
import judge_plaintext as J

ORDER = KIM_CFG["order"]
W = np.array([[A.index(c) for c in ROT[n][0]] for n in ORDER])
WI = np.array([inv(ROT[n][0]) for n in ORDER])
NOTCH = np.array([A.index({"I": "G", "II": "M", "III": "V"}[n]) for n in ORDER])
U = np.array([A.index(c) for c in UKW])
KEYS = np.array([(a, b, c) for a in range(26) for b in range(26) for c in range(26)])


def decode_all(ct, ring):
    pos = KEYS.copy(); rg = np.array([A.index(c) for c in ring])
    out = np.zeros((len(KEYS), len(ct)), dtype=np.int8)
    for j, ch in enumerate(ct):
        dbl = pos[:, 1] == NOTCH[1]; mid = (pos[:, 2] == NOTCH[2]) | dbl
        pos[:, 0] = (pos[:, 0] + dbl) % 26; pos[:, 1] = (pos[:, 1] + mid) % 26; pos[:, 2] = (pos[:, 2] + 1) % 26
        c = np.full(len(KEYS), A.index(ch))
        for i in (2, 1, 0):
            s = (pos[:, i] - rg[i]) % 26; c = (W[i][(c + s) % 26] - s) % 26
        c = U[c]
        for i in (0, 1, 2):
            s = (pos[:, i] - rg[i]) % 26; c = (WI[i][(c + s) % 26] - s) % 26
        out[:, j] = c
    return ["".join(A[x] for x in row) for row in out]


_M = None
def model():
    global _M
    if _M is None:
        _M = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["en"]])
    return _M


def stats(ct, ring, words=("BANK",)):
    texts = decode_all(ct, ring); m = model()
    sc = [m.score(t) for t in texts]
    hits = {w: sum(w in t for t in texts) for w in words}
    best = int(np.argmax(sc))
    cov = max(m.cover(t) for t in sorted(texts, key=lambda t: -m.score(t))[:200])
    return {"best_score": sc[best], "best_text": texts[best], "best_cover_top200": cov, "hits": hits}


if __name__ == "__main__":
    ap = argparse.ArgumentParser(); ap.add_argument("--n-random", type=int, default=100)
    ap.add_argument("--out", default="sweep_result.json"); a = ap.parse_args()
    # self-check: the numpy sweep agrees with enigma_k on Kim's line 4
    t = decode_all("FEWGDRHDDEEUMFFTEEMJXZR", "AAA")
    assert t[A.index("E") * 676 + A.index("Q") * 26 + A.index("I")] == "OUSTGOVPBANKIZMUBMHUVOG"
    rnd = random.Random(20261003); m = model(); res = {"seed": 20261003, "n_random": a.n_random}
    # (1) BANK count, line 4 ring AAA vs random 23-letter lines
    real = stats("FEWGDRHDDEEUMFFTEEMJXZR", "AAA", ("BANK", "OUST", "GOV"))
    ctrl = [stats("".join(rnd.choice(A) for _ in range(23)), "AAA", ("BANK", "OUST", "GOV")) for _ in range(a.n_random)]
    res["line4"] = {"real": real, "control_bank_hits": [c["hits"]["BANK"] for c in ctrl],
                    "control_best_score": [c["best_score"] for c in ctrl],
                    "control_best_cover": [c["best_cover_top200"] for c in ctrl]}
    # (2) Kim's chosen readings vs best-of-17,576 on random lines of the same length and ring convention (L3L)
    rows = [l.split("\t") for l in open(Path(__file__).with_name("kim_table.tsv")).read().splitlines()[1:]]
    res["readings"] = []
    for lab, ct, k, r, want in rows:
        if lab == "FEW23b":
            continue
        L = len(ct)
        cs = [stats("".join(rnd.choice(A) for _ in range(L)), "".join(rnd.choice(A) for _ in range(3)))
              for _ in range(max(20, a.n_random // 5))]
        res["readings"].append({"label": lab, "len": L, "kim_reading": want, "kim_score": m.score(want),
                                "kim_cover": m.cover(want),
                                "control_best_scores": sorted(c["best_score"] for c in cs),
                                "control_best_covers": sorted(c["best_cover_top200"] for c in cs),
                                "control_example": cs[0]["best_text"]})
    Path(a.out).write_text(json.dumps(res, indent=1))
    print(json.dumps({"line4_real": real,
                      "ctrl_bank_mean": float(np.mean(res["line4"]["control_bank_hits"])),
                      "ctrl_bank_ge_real": sum(h >= real["hits"]["BANK"] for h in res["line4"]["control_bank_hits"]),
                      "ctrl_best_score_ge_real": sum(s >= real["best_score"] for s in res["line4"]["control_best_score"])},
                     indent=1))
    for r in res["readings"]:
        cb = r["control_best_scores"]; cc = r["control_best_covers"]
        print(r["label"], r["len"], r["kim_reading"], "kim %.3f cov %.2f" % (r["kim_score"], r["kim_cover"]),
              "| random best-of-17576: median %.3f, share >= kim %d/%d; cover median %.2f, share >= kim %d/%d"
              % (cb[len(cb) // 2], sum(x >= r["kim_score"] for x in cb), len(cb), cc[len(cc) // 2],
                 sum(x >= r["kim_cover"] for x in cc), len(cc)), "| e.g.", r["control_example"])

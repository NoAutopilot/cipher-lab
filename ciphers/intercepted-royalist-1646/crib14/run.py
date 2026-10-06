#!/usr/bin/env python3
"""crib14/run.py -- R14-ROYCRIB (6 Oct 2026): crib loop of the unglossed Evelyn figures 19 and 216 over f.10.
Pre-registration: crib14/PREREG.md (committed before the scored run). Reuses likely9/run.py's units/runs/WordBigram.
  python3 ciphers/intercepted-royalist-1646/crib14/run.py --list   # writes candidates_216.txt (before scoring)
  python3 ciphers/intercepted-royalist-1646/crib14/run.py          # scores, writes results.json + results.tsv
Disk only."""
import json, random, re, statistics, sys
from collections import Counter
from pathlib import Path
HERE = Path(__file__).resolve().parent
T = HERE.parent
sys.path.insert(0, str(T / "likely9"))
import run as L9  # noqa: E402
from judge_plaintext import NgramModel, read_corpus, fold, DATA  # noqa: E402

CORP = sorted((DATA / "en16_repo").glob("*.txt")) + sorted((DATA / "en18").glob("*.txt.gz")) + sorted((DATA / "sco16").glob("*.txt.gz"))
LETTERS = "abcdefghijklmnopqrstuvwxyz"
OFFBAND = ["have", "has", "hath", "am"]


def texts():
    return [read_corpus(p) for p in CORP]


def band(ts):
    c = Counter()
    for t in ts:
        c.update(w.lower() for w in re.findall(r"[A-Za-z]+", t))
    return sorted(w for w, n in c.items() if n >= 50 and "if" < w < "left")


def is_num(s):
    return s.isdigit()


def run_texts(rows, key, code):
    """readable runs (>=1 token of `code`) as text, and adjacent pairs involving `code`."""
    us, idx = [], []
    for i, (_, _, sign, conf) in enumerate(rows):
        pass
    # rebuild units carrying a flag for the target code
    out = []
    for _, _, sign, conf in rows:
        if sign.startswith("[PLAIN:"):
            for w in sign[7:-1].split("_"):
                out.append(["clear", w, False])
        elif sign in key:
            v = key[sign]; tgt = sign == code
            if len(v) == 1 and out and out[-1][0] == "kl":
                out[-1][1] += v; out[-1][2] = out[-1][2] or tgt
            else:
                out.append(["kl" if len(v) == 1 else "keyed", v, tgt])
        else:
            out.append(["gap", sign, False])
    runs, cur = [], []
    for u in out:
        if u[0] == "gap":
            if cur: runs.append(cur); cur = []
        else:
            cur.append(u)
    if cur: runs.append(cur)
    rtexts, pairs = [], []
    for r in runs:
        if any(u[2] for u in r):
            rtexts.append("".join(u[1] for u in r))
            for a, b in zip(r, r[1:]):
                if a[2] or b[2]:
                    pairs.append((fold(a[1]), fold(b[1])))
    return rtexts, pairs


def S_letter(rows, key, code, model):
    rt, _ = run_texts(rows, key, code)
    num = den = 0.0
    for t in rt:
        f = fold(t)
        if len(f) >= 4:
            num += model.score(f) * (len(f) - 3); den += len(f) - 3
    return num / den if den else float("nan")


def S_word(rows, key, code, wb):
    _, pairs = run_texts(rows, key, code)
    return statistics.mean(wb.lp(a, b) for a, b in pairs) if pairs else float("nan")


def loop(rows, key, code, cands, f):
    out = {}
    for c in cands:
        k = dict(key); k[code] = c
        out[c] = f(rows, k, code)
    return out


def m_d(sc):
    rn = max(sc["r"], sc["n"]); oth = max(v for c, v in sc.items() if c not in ("r", "n"))
    return rn - oth, sc["r"] - sc["n"]


def g_of(sc):
    xs = sorted(((v, c) for c, v in sc.items() if v == v), reverse=True)
    return (xs[0][0] - xs[1][0], xs[0][1]) if len(xs) > 1 else (float("nan"), None)


def relocate(rows, code, n, lo, hi, seed, key):
    pos = [i for i, r in enumerate(rows) if is_num(r[2]) and lo <= int(r[2]) <= hi and r[2] not in key and r[2] != code]
    rows2 = [r if r[2] != code else (r[0], r[1], "X" + r[2], r[3]) for r in rows]  # remove the real occurrences
    for i in random.Random(seed).sample(pos, n):
        r = rows2[i]; rows2[i] = (r[0], r[1], code, r[3])
    return rows2


def p95(xs):
    xs = sorted(x for x in xs if x == x)
    return xs[int(0.95 * (len(xs) - 1))] if xs else float("nan")


def main():
    ts = texts()
    if "--list" in sys.argv:
        b = band(ts)
        (HERE / "candidates_216.txt").write_text("# in-band (count>=50 in wide corpus, 'if' < w < 'left')\n" + "\n".join(b) +
                                                 "\n# off-band context candidates\n" + "\n".join(OFFBAND) + "\n")
        print(len(b), "in-band:", " ".join(b)); return
    lines = [l.strip() for l in open(HERE / "candidates_216.txt") if l.strip()]
    sep = lines.index("# off-band context candidates")
    inband, offband = lines[1:sep], lines[sep + 1:]
    model = NgramModel(ts); wb = L9.WordBigram(ts)
    rows = L9.load_ct(T / "f10_ct.tsv"); key = {c: v[0] for c, v in L9.load_key(T / "key.tsv").items()}
    cnt = Counter(r[2] for r in rows if is_num(r[2]))
    fl = lambda R, K, C: S_letter(R, K, C, model)
    fw = lambda R, K, C: S_word(R, K, C, wb)
    res = {}
    # ---- 19
    sc = loop(rows, key, "19", LETTERS, fl); m, dd = m_d(sc)
    c1 = [c for c, n in cnt.items() if int(c) <= 99 and c not in key and c != "19" and n >= 8]
    c1r = {c: m_d(loop(rows, key, c, LETTERS, fl)) for c in c1}
    c2r = [m_d(loop(relocate(rows, "19", cnt["19"], 0, 99, s, key), key, "19", LETTERS, fl)) for s in range(1, 51)]
    rank = sorted(sc, key=lambda c: -sc[c])
    res["19"] = {"scores": sc, "rank": rank, "m": m, "d": dd,
                 "C1": {"codes": c1, "m": [c1r[c][0] for c in c1], "d": [c1r[c][1] for c in c1],
                        "m_p95": p95([c1r[c][0] for c in c1]), "absd_p95": p95([abs(c1r[c][1]) for c in c1])},
                 "C2": {"m_p95": p95([x[0] for x in c2r]), "absd_p95": p95([abs(x[1]) for x in c2r]),
                        "m": [x[0] for x in c2r], "d": [x[1] for x in c2r]}}
    # ---- 216
    allc = inband + offband
    sc = loop(rows, key, "216", allc, fw); g, top = g_of({c: sc[c] for c in inband})
    c1 = [c for c, n in cnt.items() if 100 <= int(c) <= 430 and c not in key and c != "216" and 3 <= n <= 8]
    c1g = {c: g_of(loop(rows, key, c, inband, fw)) for c in c1}
    c2g = [g_of(loop(relocate(rows, "216", cnt["216"], 100, 430, s, key), key, "216", inband, fw)) for s in range(1, 51)]
    res["216"] = {"scores": sc, "rank_inband": sorted(inband, key=lambda c: -sc[c]), "rank_all": sorted(allc, key=lambda c: -sc[c]),
                  "g": g, "top": top,
                  "C1": {"codes": c1, "g": [c1g[c][0] for c in c1], "top": [c1g[c][1] for c in c1], "g_p95": p95([c1g[c][0] for c in c1])},
                  "C2": {"g": [x[0] for x in c2g], "top": [x[1] for x in c2g], "g_p95": p95([x[0] for x in c2g])}}
    (HERE / "results.json").write_text(json.dumps(res, indent=1))
    r = res["19"]
    print("19: top5", [(c, round(r["scores"][c], 4)) for c in r["rank"][:5]], "rank r", r["rank"].index("r") + 1, "rank n", r["rank"].index("n") + 1)
    print(f"   m {r['m']:.4f}  C1 p95 {r['C1']['m_p95']:.4f} (n={len(r['C1']['codes'])})  C2 p95 {r['C2']['m_p95']:.4f}")
    print(f"   d(r-n) {r['d']:.4f}  C1 |d| p95 {r['C1']['absd_p95']:.4f}  C2 |d| p95 {r['C2']['absd_p95']:.4f}")
    r = res["216"]
    print("216: top5 in-band", [(c, round(r["scores"][c], 4)) for c in r["rank_inband"][:5]])
    print("     top5 all", [(c, round(r["scores"][c], 4)) for c in r["rank_all"][:5]])
    print(f"     g {r['g']:.4f}  C1 p95 {r['C1']['g_p95']:.4f} (n={len(r['C1']['codes'])}, tops {Counter(r['C1']['top']).most_common(3)})  C2 p95 {r['C2']['g_p95']:.4f} (tops {Counter(r['C2']['top']).most_common(3)})")


if __name__ == "__main__":
    main()

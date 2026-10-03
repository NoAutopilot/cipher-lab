#!/usr/bin/env python3
"""MOD1162 (3 Oct 2026): statistic G and its band-shuffle control, as pre-registered in PREREG-MOD1162.md.

  python3 ciphers/decode-1162-modena-ambung-1492/score_g.py            print the result table, write score_g.json
  python3 ciphers/decode-1162-modena-ambung-1492/score_g.py --check    exit 1 if score_g.json is stale

Inputs: ciphertext.tsv (line, pos, sign, conf; 1168 sign labels), gloss.tsv (line, gloss, kind: letters|code),
the 1168 key (../decode-1168-modena-costabili-1492/key.tsv). G = sum LCS(decoded, gloss) / sum keyed signs over
'letters' groups. Control: 1000 draws, values permuted within grade band (C among C, M among M), seeds 0..999.
J (judge, it16dip) on the real decode and on the first 500 draws: descriptive only.
"""
import csv, json, random, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[1]
sys.path.insert(0, str(ROOT / "tools"))
KEY = HERE.parent / "decode-1168-modena-costabili-1492" / "key.tsv"


def fold(s):
    s = s.lower().replace("v", "u").replace("j", "i")
    return "".join(c for c in s if "a" <= c <= "z")


def lcs(a, b):
    prev = [0] * (len(b) + 1)
    for x in a:
        cur = [0]
        for j, y in enumerate(b):
            cur.append(prev[j] + 1 if x == y else max(prev[j + 1], cur[j]))
        prev = cur
    return prev[-1]


def lcs_pairs(a, b):
    """index pairs (i in a, j in b) of one longest common subsequence."""
    n, m = len(a), len(b)
    L = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            L[i][j] = L[i + 1][j + 1] + 1 if a[i] == b[j] else max(L[i + 1][j], L[i][j + 1])
    i = j = 0; out = []
    while i < n and j < m:
        if a[i] == b[j]:
            out.append((i, j)); i += 1; j += 1
        elif L[i + 1][j] >= L[i][j + 1]:
            i += 1
        else:
            j += 1
    return out


def votes(key, groups, gloss):
    """votes.tsv rows reproducing PREREG grades through tools/decode_key.py: a C-key sign gets a vote (agree -> C,
    disagree -> M); an M-key sign gets a vote only when it disagrees with the gloss (-> M), else none (-> S)."""
    rows = []
    for ln, signs in groups.items():
        if gloss.get(ln, ("", ""))[1] != "letters":
            continue
        g = fold(gloss[ln][0])
        keyed = [(p, key[s][0]) for p, s in enumerate(signs, 1) if s in key]
        al = dict(lcs_pairs([fold(v) or "#" for p, v in keyed], list(g)))
        for k, (p, v) in enumerate(keyed):
            grade = key[signs[p - 1]][1]
            if k in al and grade == "C":
                rows.append((ln, p, v))
            elif k not in al:
                rows.append((ln, p, "#disagree"))
    return rows


def load():
    key = {r["sign"]: (r["value"], r["grade"]) for r in csv.DictReader(open(KEY), delimiter="\t")}
    groups = {}
    for r in csv.DictReader(open(HERE / "ciphertext.tsv"), delimiter="\t"):
        groups.setdefault(r["line"], []).append(r["sign"])
    gloss = {r["line"]: (r["gloss"], r["kind"]) for r in csv.DictReader(open(HERE / "gloss.tsv"), delimiter="\t")}
    return key, groups, gloss


def G(vals, groups, gloss):
    num = den = 0
    per = {}
    for ln, signs in groups.items():
        if gloss.get(ln, ("", ""))[1] != "letters":
            continue
        dec = "".join(vals.get(s, "") for s in signs)
        m = lcs(fold(dec), fold(gloss[ln][0]))
        num += m; den += sum(1 for s in signs if s in vals)
        per[ln] = (dec, m)
    return (num / den if den else 0.0), per


def main():
    key, groups, gloss = load()
    vals = {s: v for s, (v, g) in key.items()}
    g_real, per = G(vals, groups, gloss)
    bands = {b: sorted(s for s, (v, g) in key.items() if g == b) for b in ("C", "M")}
    ctrl, draws = [], []
    for seed in range(1000):
        rnd = random.Random(seed); d = {}
        for b, ss in bands.items():
            vs = [vals[s] for s in ss]; rnd.shuffle(vs); d.update(zip(ss, vs))
        ctrl.append(G(d, groups, gloss)[0]); draws.append(d)
    cs = sorted(ctrl); p99 = cs[int(0.99 * 999)]
    signs = [s for ln, ss in groups.items() if gloss.get(ln, ("", ""))[1] == "letters" for s in ss]
    cover = sum(1 for s in signs if s in vals) / len(signs) if signs else 0.0
    from judge_plaintext import NgramModel, LANG_CORPORA, read_corpus
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA["it16dip"]])
    def dec_all(v):
        return "".join(v.get(s, "") for ln, ss in groups.items() if gloss.get(ln, ("", ""))[1] == "letters" for s in ss)
    j_real = model.score(dec_all(vals))
    j_ctrl = sorted(model.score(dec_all(d)) for d in draws[:500])
    gloss_j = model.score("".join(fold(g) for g, k in gloss.values() if k == "letters"))
    res = {"G_real": round(g_real, 4), "G_ctrl_mean": round(sum(ctrl) / len(ctrl), 4), "G_ctrl_p99": round(p99, 4),
           "G_ctrl_max": round(cs[-1], 4), "p_emp": round(sum(1 for c in ctrl if c >= g_real) / len(ctrl), 4),
           "gate": "PASS" if (g_real > p99 and g_real >= 0.5) else "FAIL",
           "coverage": round(cover, 4), "letter_signs": len(signs),
           "J_real": round(j_real, 3), "J_ctrl_median": round(j_ctrl[250], 3), "J_ctrl_p95": round(j_ctrl[int(0.95 * 499)], 3),
           "J_gloss": round(gloss_j, 3),
           "groups": {ln: {"decoded": d, "gloss": gloss[ln][0], "lcs": m} for ln, (d, m) in per.items()}}
    out = json.dumps(res, indent=1, ensure_ascii=False) + "\n"
    vt = "line\tpos\tvalue\n" + "".join(f"{a}\t{b}\t{c}\n" for a, b, c in votes(key, groups, gloss))
    if "--check" in sys.argv:
        ok = ok2 = True
        ok2 = (HERE / "votes.tsv").read_text() == vt
        ok = (HERE / "score_g.json").read_text() == out
        print("score_g.json, votes.tsv up to date" if ok and ok2 else "STALE score_g.json or votes.tsv")
        sys.exit(0 if ok and ok2 else 1)
    (HERE / "score_g.json").write_text(out)
    (HERE / "votes.tsv").write_text(vt)
    print(out)


if __name__ == "__main__":
    main()

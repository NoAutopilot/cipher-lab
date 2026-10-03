#!/usr/bin/env python3
"""G2 (key no.71) on the fr.4712 f.7r marked codes, each located by fixed-key LCS anchors
(witness/key71/PREREG6_g2anchor.md, GAPS91, 3 Oct 2026).

  python3 scripts/f7r_g2anchor.py [--all]

Per run: unmarked tokens decode with Tomokiyo's letter table, marked tokens are sentinels; LCS against the gloss letters
(traceback tie order: match, drop token, drop gloss letter) gives anchors; a marked token's located text is the gloss
words wholly between its neighbouring anchors (none if empty or the interval is shared with another marked token).
Scored against key no.71 with PREREG3's judge and controls. --all scores every marked token (descriptive only).
Writes witness/f7r_g2anchor.tsv (primary) or witness/f7r_g2anchor_all.tsv. Exit 0 PASS, 3 FAIL, 4 NON-TEST.
"""
import argparse, csv, itertools, random, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from f4712_7r_gates import HERE, KEY71, RANGE, judge, score, tomokiyo  # noqa: E402
from key71_control import load_key, p95  # noqa: E402
from g1_power_check import norm  # noqa: E402

PAIRS = HERE / "witness/f4712_7r_pairs_img.tsv"
LAYER = {"d": "mots", "t": "places", "b": "persons"}
EXCLUDE = {("L01.1.1", "d20"), ("L02.1.1", "t12"), ("L05.2.1", "d16"), ("L06.3.1", "d87"), ("L09.1.2", "d47"),
           ("L09.1.2", "d20"), ("L10.1.1", "b85")}


def anchors(seq, g):
    n, m = len(seq), len(g)
    D = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        for j in range(m - 1, -1, -1):
            D[i][j] = D[i + 1][j + 1] + 1 if seq[i] == g[j] else max(D[i + 1][j], D[i][j + 1])
    out, i, j = [], 0, 0
    while i < n and j < m:  # traceback from the start of the suffix table == from the end of the sequences
        if seq[i] == g[j] and D[i][j] == D[i + 1][j + 1] + 1:
            out.append((i, j)); i += 1; j += 1
        elif D[i + 1][j] == D[i][j]:
            i += 1
        else:
            j += 1
    return out


def locate(row, key, homs):
    toks = row["cipher_raw"].split()
    seq = []
    for t in toks:
        seq.append(key.get(str(int(t)), "?") if re.fullmatch(r"\d{1,2}", t) else "#")
    words = row["plain_raw"].split()
    g, wid = [], []
    for k, w in enumerate(words):
        for c in norm(w):
            if c in homs:
                g.append(c); wid.append(k)
    an = anchors(seq, g)
    res = []
    for i, t in enumerate(toks):
        mm = re.fullmatch(r"([dtb])(\d{1,2})", t)
        if not mm:
            continue
        left = max([gj for ti, gj in an if ti < i], default=-1)
        right = min([gj for ti, gj in an if ti > i], default=len(g))
        lti = max([ti for ti, gj in an if ti < i], default=-1)
        rti = min([ti for ti, gj in an if ti > i], default=len(toks))
        shared = any(seq[k] == "#" for k in range(lti + 1, rti) if k != i)
        inside = [k for k in range(len(words)) if k in wid and all(left < j < right for j, w in enumerate(wid) if w == k)]
        text = " ".join(words[k] for k in inside)
        res.append((row["plain_line"], t, LAYER[mm.group(1)], int(mm.group(2)), text if text and not shared else "",
                    "shared" if shared else ("" if text else "empty")))
    return res


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--all", action="store_true")
    a = ap.parse_args()
    key = tomokiyo()
    homs = set(key.values())
    word, _ = load_key(KEY71)
    rows = list(csv.DictReader((l for l in open(PAIRS, encoding="utf-8") if not l.startswith("#")), delimiter="\t"))
    loc = [x for r in rows for x in locate(r, key, homs) if a.all or (x[0], x[1]) not in EXCLUDE]
    out = HERE / ("witness/f7r_g2anchor_all.tsv" if a.all else "witness/f7r_g2anchor.tsv")
    items = []
    with open(out, "w", encoding="utf-8") as f:
        f.write("run\ttoken\tlayer\tcode\tlocated\tkey71\tverdict\n")
        for run, t, l, n, text, why in loc:
            if text:
                v, cells = judge(word, l, n, text)
                items.append((l, n, text))
            else:
                v, cells = "not-located:" + why, word.get((l, str(n)), [])
            f.write(f"{run}\t{t}\t{l}\t{n}\t{text}\t{' | '.join(cells)}\t{v}\n")
            print(f"{run}\t{t}\t{l} {n}\tlocated={text or '-'}\tkey71={' | '.join(cells) or '-'}\t{v}")
    mt, k = score(word, items)
    sc = mt + k
    share = mt / sc if sc else 0.0
    vals = [v for _, _, v in items]
    if len(items) <= 8:
        perm = [score(word, [(l, n, vals[p[i]]) for i, (l, n, _) in enumerate(items)])[0]
                for p in itertools.permutations(range(len(items)))] or [0]
    else:
        rng = random.Random(4712)
        perm = []
        for _ in range(10000):
            rng.shuffle(vals)
            perm.append(score(word, [(l, n, vals[i]) for i, (l, n, _) in enumerate(items)])[0])
    rng = random.Random(71)
    rnd = [score(word, [(l, rng.randint(*RANGE[l]), v) for l, _, v in items])[0] for _ in range(10000)]
    pp, pr = p95(perm), p95(rnd)
    print(f"G2 {'ALL (descriptive)' if a.all else 'PRIMARY'}: {len(loc)} items, {len(items)} located | REAL {mt} match,"
          f" {k} conflict, {len(items) - sc} absent | SHARE {mt}/{sc} = {share:.3f} | permutation ({len(perm)}) p95 {pp}"
          f" max {max(perm)} | random-code (10000) p95 {pr} max {max(rnd)}")
    if sc < 8:
        print("G2 NON-TEST"); sys.exit(4)
    ok = share >= 0.80 and mt > pp and mt > pr
    print("G2", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()

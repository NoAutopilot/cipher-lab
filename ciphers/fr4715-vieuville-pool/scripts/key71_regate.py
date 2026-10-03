#!/usr/bin/env python3
"""Second known-answer gate for key no.71 (BnF fr.3995 f.133r), on an UNSEEN known answer, as pre-registered in
witness/key71/PREREG2.md (GAPS-fr4715-vieuville-pool-15, 3 Oct 2026).

  python3 scripts/key71_regate.py [--key witness/key71/key71_reconciled.tsv] [--cn PATH] [--seed 71]

U: eight Cabinet Noir sure values (Motz '29 '51 '74 '84 '94 '97; persons ~15 ~37) selected by PREREG2's rule from
sources/cabinet-noir/2026-10-03/montholon1589_complements.tsv. Each is match / conflict / absent against the key cell in
the layer its mark selects. Controls: all 40,320 value permutations (exact); 10,000 random codes in the layer's range.
Exit 0 = PASS, 3 = FAIL, 4 = NON-TEST (fewer than 6 scorable).
"""
import argparse, csv, itertools, random, re, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
from key71_control import load_key, norm_tokens, p95  # noqa: E402

HERE = Path(__file__).resolve().parent.parent
CN = HERE.parent.parent / "sources/cabinet-noir/2026-10-03/montholon1589_complements.tsv"
U_CODES = ["'29", "'51", "'74", "'84", "'94", "'97", "~15", "~37"]
LAYER = {"'": "mots", "~": "persons"}
RANGE = {"mots": (11, 99), "persons": (1, 89)}
KEY71_CITE = re.compile(r"n°71|n° 71|clé d.époque|3995|133r|f\.133")


def select(path):
    rows = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    out = []
    for r in rows:
        typ, code, val, status, proof = (r + [""] * 5)[:5]
        if typ not in ("code", "nom") or not status.startswith("SÛR") or KEY71_CITE.search(proof):
            continue
        c = code.split("/")[0].strip()
        if c in U_CODES:
            out.append((c, val, status))
    assert sorted(c for c, _, _ in out) == sorted(U_CODES), out
    return sorted(out, key=lambda x: U_CODES.index(x[0]))


def alts(val):
    parts = re.split(r"[,;/()]| ou ", val.replace("?", ""))
    return [norm_tokens(p) for p in parts if norm_tokens(p)]


def judge(word, layer, num, val):
    cells = word.get((layer, str(num)), [])
    if not cells:
        return "absent", cells
    for e in cells:
        et = norm_tokens(e)
        for a in alts(val):
            if a <= et or (et and et <= a):
                return "match", cells
    return "conflict", cells


def score(word, items):
    res = [judge(word, l, n, v)[0] for l, n, v in items]
    return res.count("match"), res.count("conflict")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key", default=str(HERE / "witness/key71/key71_reconciled.tsv"))
    ap.add_argument("--cn", default=str(CN))
    ap.add_argument("--seed", type=int, default=71)
    a = ap.parse_args()
    word, _ = load_key(a.key)
    u = select(a.cn)
    items = [(LAYER[c[0]], int(c[1:]), v) for c, v, _ in u]
    for (c, v, st), (l, n, _) in zip(u, items):
        verdict, cells = judge(word, l, n, v)
        print(f"{c}\t{st}\tCN={v}\tkey71[{l} {n}]={' | '.join(cells) or '-'}\t{verdict}")
    m, k = score(word, items)
    scorable = m + k
    share = m / scorable if scorable else 0.0
    vals = [v for _, _, v in items]
    perm = [score(word, [(l, n, vals[p[i]]) for i, (l, n, _) in enumerate(items)])[0]
            for p in itertools.permutations(range(len(items)))]
    rng = random.Random(a.seed)
    rnd = [score(word, [(l, rng.randint(*RANGE[l]), v) for l, _, v in items])[0] for _ in range(10000)]
    pp, pr = p95(perm), p95(rnd)
    print(f"U REAL {m} match, {k} conflict, {len(items) - scorable} absent | SHARE {m}/{scorable} = {share:.3f}"
          f" | permutation ({len(perm)}, exact) mean {sum(perm)/len(perm):.3f} p95 {pp} max {max(perm)}"
          f" | random-code (10000) mean {sum(rnd)/len(rnd):.3f} p95 {pr} max {max(rnd)}")
    print("GAPS-14 (first gate, on record): A 5/5 vs p95 3 / 1; B 25/33 = 0.758 < 0.80 (0 conflicts); FAIL")
    if scorable < 6:
        print("GATE NON-TEST")
        sys.exit(4)
    ok = share >= 0.80 and m > pp and m > pr
    print("GATE", "PASS" if ok else "FAIL")
    sys.exit(0 if ok else 3)


if __name__ == "__main__":
    main()

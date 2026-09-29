#!/usr/bin/env python3
"""H215 (runner 8 session_011Taenrv3JSdk7VjpiBjids, 29 Sept 2026): does the model judge prefer f.108v read with HASH4 split by H212's blind forms
(A 4-head d/q, B looped i/x) over the same text with HASH4 all d/q, all i/x, or dropped (the H208 bowl-only target)? Written before any call.
 build --seed N: f.108v relabelled by bowl (H201) and HASH4 by form (H213's mapping). 21 sets: T = 14 cells + 4BOWL c/p + 4NOB a/n + HASHA d/q +
   HASHB i/x; ALL-DQ, ALL-IX (both hash forms one cell); DROP (HASH4 not decoded, the H208 target); 17 one-swap neighbours of T drawn only from class
   pairs present in the text and excluding the HASHA<->HASHB swap (which is REVERSE, added as the 5th named set, so 16 swaps). Order shuffled (seed N).
 read-out per seed: "prefers the form split" iff T ranks 1 of 21 (ties against) AND scores strictly above ALL-DQ, ALL-IX and REVERSE; "prefers an
   alternative" if any of those scores strictly above T; else "no preference shown". Overall: the same verdict in seeds 215 and 216, else "mixed".
   DROP is reported, not in the rule (it is 14 letters shorter). Calibration: this session's H205 control (rank 1 of 21). Descriptive.
  python3 f61judge108v_hash.py build --seed N | score --seed N [--check]"""
import json, os, random, sys
HERE = os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0, HERE)
def text():
    import f61hash4_form_seq as F, f61bowl_108v_seq as BS
    from collections import defaultdict
    Fm = f"{HERE}/../family"; key = {r["item"]: r for r in BS.rd(f"{Fm}/h212_items.tsv")}
    grp = {f"T{int(r['tile'].split()[-1]):02d}": r["group"].strip() for r in BS.rd(f"{Fm}/passes/h212_sort.tsv")}
    form = {(k["line"], k["segment"], k["x_px"]): grp[m] for m, k in key.items() if k["leaf"] == "108v"}
    A = defaultdict(list)
    for r in BS.rd(f"{Fm}/passes/f108v3z_signsA.tsv"): A[r["line"]].append(r)
    D = BS.draft(); ans = {(r["line"], r["column"]): r["bowl"] for r in BS.rd(f"{Fm}/h199_bowl_positions.tsv")}; colform = {}
    for l in sorted(A):
        k = 0
        for c in (r for r in BS.rd(f"{Fm}/passes/f108v3z_recon_task.tsv") if r["line"] == l):
            if c["alt"].startswith("A:-"): continue
            a = A[l][k]; k += 1; f = form.get((l, a["segment"], a["x_px"]))
            if f: colform[(l, c["position"])] = f
    L = BS.relabel(D, ans)
    return {l: [("HASH" + colform[(l, p)]) if s == "HASH4" and (l, p) in colform else s for (p, _), s in zip(D[l], L[l])] for l in L}
def build(seed):
    import f61judge108v as J
    L = text(); M0 = dict(J.cells(), **{"4BOWL": "c/p", "4NOB": "a/n"}); T = dict(M0, HASHA="d/q", HASHB="i/x")
    named = [("T", T), ("ALL-DQ", dict(M0, HASHA="d/q", HASHB="d/q")), ("ALL-IX", dict(M0, HASHA="i/x", HASHB="i/x")), ("REVERSE", dict(M0, HASHA="i/x", HASHB="d/q")), ("DROP", M0)]
    pres = {c for v in L.values() for c in v}; labs = sorted(T); rng = random.Random(seed)
    pairs = [(a, b) for i, a in enumerate(labs) for b in labs[i + 1:] if T[a] != T[b] and a in pres and b in pres and {a, b} != {"HASHA", "HASHB"}]; rng.shuffle(pairs)
    sets = list(named)
    for a, b in pairs[:16]:
        m = dict(T); m[a], m[b] = T[b], T[a]; sets.append((f"swap {a}<->{b}", m))
    order = list(range(21)); random.Random(seed).shuffle(order); key = {}; txt = []; name = f"f108v_hash_s{seed}"
    for k, i in enumerate(order):
        lab = f"SET-{k+1:02d}"; key[lab] = sets[i][0]; txt.append(f"== {lab}")
        for l, seq in L.items(): txt.append(f"{l}: " + " ".join(f"[{sets[i][1][c]}]" for c in seq if c in sets[i][1]))
    open(f"{HERE}/f61judge_{name}_sets.txt", "w").write("\n".join(txt) + "\n"); json.dump({"tag": name, "key": key}, open(f"{HERE}/f61judge_{name}_key.json", "w"), indent=1)
    print(f"wrote f61judge_{name}_sets.txt; HASHA {sum(s.count('HASHA') for s in L.values())}, HASHB {sum(s.count('HASHB') for s in L.values())}")
def score(seed):
    import csv
    name = f"f108v_hash_s{seed}"; key = json.load(open(f"{HERE}/f61judge_{name}_key.json"))["key"]
    rows = [r for r in csv.DictReader((l for l in open(f"{HERE}/f61judge_{name}_verdict.tsv") if not l.startswith("#")), delimiter="\t")]
    sc = {r["label"].strip(): float(r["score_0_10"]) for r in rows}; assert set(sc) == set(key)
    by = {v: l for l, v in key.items() if not v.startswith("swap")}; t = sc[by["T"]]
    rank = 1 + sum(1 for l, v in sc.items() if l != by["T"] and v >= t); alts = [sc[by[x]] for x in ("ALL-DQ", "ALL-IX", "REVERSE")]
    ro = "prefers the form split" if rank == 1 and all(t > a for a in alts) else ("prefers an alternative" if any(a > t for a in alts) else "no preference shown")
    out = [f"{name}: T {t:.1f} rank {rank} of 21 (ties against); " + ", ".join(f"{x} {sc[by[x]]:.1f}" for x in ("ALL-DQ", "ALL-IX", "REVERSE", "DROP")),
           "all scores: " + " ".join(f"{l}({key[l].split()[0]}):{sc[l]:.1f}" for l in sorted(sc, key=lambda l: -sc[l])), f"read-out: {ro}"]
    txt = "\n".join(out) + "\n"; res = f"{HERE}/f61judge_{name}_result.txt"
    if "--check" in sys.argv:
        ok = os.path.exists(res) and open(res).read() == txt; print("fresh" if ok else "STALE"); sys.exit(0 if ok else 1)
    open(res, "w").write(txt); print(txt, end="")
if __name__ == "__main__":
    s = int(sys.argv[sys.argv.index("--seed") + 1]); sys.argv = [a for a in sys.argv]
    build(s) if sys.argv[1] == "build" else score(s)

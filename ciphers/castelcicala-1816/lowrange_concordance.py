#!/usr/bin/env python3
"""Two-context concordance for the sub-1100 groups of R9558/R9559/R9560/R9587 (A2-CAS, 2 Oct 2026).

Method (the bCAS 154=a / 605=enza method, made mechanical): every keyed group in the 25-record corpus
contributes "frames" -- the key values of its two keyed neighbours on one side or one on each side:
(L2,L1,_), (L1,_,R1), (_,R1,R2). For an unkeyed sub-1100 group t occurring in the four target records,
each of its frames votes for the value that fills that frame most often among keyed groups, provided the
frame was seen >= MIN_FILL times with that value holding >= MIN_SHARE of the fillings. t gets a candidate
value v when v wins votes from >= 2 distinct occurrences of t that lie in >= 2 different records
(the two-context bar, rule 4 S grade).

Nulls are dropped before framing (Bourdeau's corpus.py convention); '?' groups break a frame.

Statistic: number of target groups that get a candidate (and total supporting votes). This depends on
token order, so the controls can fail differently from the target (rule 3, bCAS lesson):
  C1 shuffle the token order inside each of the four target records only (reference frames intact);
  C2 shuffle the token order inside every record.
Known-answer check: every keyed group < 1100 that occurs in the corpus is unkeyed in turn (leave-one-out)
and the same rule is asked to recover its value; scored against key.tsv.

Usage: python3 lowrange_concordance.py [--shuffles 200] [--seed 1] [--single] [--min-fill N] [--min-share F] [--out F]
Pre-declared sweep (A2-CAS): strict (default); --single; --single --min-fill 3 --min-share 0.6.
"""
import argparse, random, collections, os, sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGETS = ["R9558", "R9559", "R9560", "R9587"]
MIN_FILL, MIN_SHARE = 2, 0.5
SINGLE = False


def load():
    recs = collections.OrderedDict()
    for line in open(os.path.join(HERE, "ciphertext.txt")):
        if line.startswith("#") or "|" not in line:
            continue
        head, body = line.split("|", 1)
        rid = head.split()[0]
        toks = [t for t in body.split() if t != "NULL" and not (t.isdigit() and len(t) >= 5)]
        recs.setdefault(rid, []).extend(toks)
    key = {}
    for line in open(os.path.join(HERE, "key.tsv")):
        if line.startswith("#"):
            continue
        p = line.rstrip("\n").split("\t")
        if len(p) >= 2 and p[0] != "NULL" and p[0].isdigit():
            key[p[0]] = p[1]
    return recs, key


def frames_at(seq, i, key):
    v = lambda j: key.get(seq[j]) if 0 <= j < len(seq) else None
    out = []
    l2, l1, r1, r2 = v(i - 2), v(i - 1), v(i + 1), v(i + 2)
    if l2 and l1:
        out.append(("L", l2, l1))
    if l1 and r1:
        out.append(("M", l1, r1))
    if r1 and r2:
        out.append(("R", r1, r2))
    if SINGLE:
        if l1:
            out.append(("l", l1))
        if r1:
            out.append(("r", r1))
    return out


def frame_table(recs, key, exclude=None):
    tab = collections.defaultdict(collections.Counter)
    for rid, seq in recs.items():
        for i, g in enumerate(seq):
            if g in key and g != exclude:
                for f in frames_at(seq, i, key):
                    tab[f][key[g]] += 1
    best = {}
    for f, c in tab.items():
        v, n = c.most_common(1)[0]
        tot = sum(c.values())
        if n >= MIN_FILL and n / tot >= MIN_SHARE:
            best[f] = (v, n, tot)
    return best


def candidates(recs, key, best, groups, where):
    """groups: set of unkeyed groups; where: records whose occurrences count."""
    votes = collections.defaultdict(lambda: collections.defaultdict(list))  # g -> v -> [(rid,i,frame)]
    for rid in where:
        seq = recs[rid]
        for i, g in enumerate(seq):
            if g in groups:
                for f in frames_at(seq, i, key):
                    if f in best:
                        votes[g][best[f][0]].append((rid, i, f))
    out = {}
    for g, byv in votes.items():
        ranked = []
        for v, hits in byv.items():
            occ = {(r, i) for r, i, _ in hits}
            rids = {r for r, _ in occ}
            if len(occ) >= 2 and len(rids) >= 2:
                ranked.append((len(occ), len(rids), v, hits))
        if ranked:
            ranked.sort(reverse=True)
            out[g] = ranked
    return out


def stat(c):
    return len(c), sum(r[0][0] for r in c.values())


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--single", action="store_true", help="also use one-neighbour frames")
    ap.add_argument("--min-fill", type=int, default=2)
    ap.add_argument("--min-share", type=float, default=0.5)
    ap.add_argument("--out", default=os.path.join(HERE, "lowrange_concordance.tsv"))
    a = ap.parse_args()
    global SINGLE, MIN_FILL, MIN_SHARE
    SINGLE, MIN_FILL, MIN_SHARE = a.single, a.min_fill, a.min_share
    recs, key = load()
    low = lambda g: g.isdigit() and int(g) < 1100
    T = {g for r in TARGETS for g in recs[r] if low(g) and g not in key}
    tok = sum(1 for r in TARGETS for g in recs[r] if g in T)
    best = frame_table(recs, key)
    real = candidates(recs, key, best, T, TARGETS)
    rs = stat(real)
    print(f"targets: {len(T)} distinct unkeyed sub-1100 groups, {tok} tokens in {','.join(TARGETS)}")
    print(f"usable frames (>= {MIN_FILL} fills, share >= {MIN_SHARE}): {len(best)}")
    print(f"REAL: {rs[0]} groups with a two-context candidate, {rs[1]} supporting occurrences")

    rng = random.Random(a.seed)
    for name, which in (("C1 shuffle target records only", TARGETS), ("C2 shuffle every record", list(recs))):
        ng, nv = [], []
        for _ in range(a.shuffles):
            sh = {r: list(s) for r, s in recs.items()}
            for r in which:
                rng.shuffle(sh[r])
            b = best if which is TARGETS else frame_table(sh, key)
            s = stat(candidates(sh, key, b, T, TARGETS))
            ng.append(s[0]); nv.append(s[1])
        ng.sort(); nv.sort()
        p95 = lambda xs: xs[int(0.95 * len(xs)) - 1]
        ge = sum(1 for x in ng if x >= rs[0])
        print(f"{name}: groups mean {sum(ng)/len(ng):.2f} p95 {p95(ng)} max {ng[-1]}; "
              f"occurrences mean {sum(nv)/len(nv):.2f} p95 {p95(nv)}; shuffles >= real groups: {ge}/{a.shuffles}")

    # known-answer leave-one-out on keyed groups < 1100 occurring anywhere
    allrids = list(recs)
    kl = sorted({g for s in recs.values() for g in s if low(g) and g in key}, key=int)
    right = wrong = none = 0
    rows = []
    for g in kl:
        k2 = {x: y for x, y in key.items() if x != g}
        b2 = frame_table(recs, k2)
        c = candidates(recs, k2, b2, {g}, allrids)
        if g not in c:
            none += 1; rows.append((g, key[g], "-")); continue
        v = c[g][0][2]
        ok = v == key[g]
        right += ok; wrong += (not ok)
        rows.append((g, key[g], v))
    print(f"KNOWN-ANSWER (leave-one-out, {len(kl)} keyed sub-1100 groups, whole corpus): "
          f"right {right}, wrong {wrong}, no candidate {none}")
    for g, t, v in rows:
        if v != "-":
            print(f"  {g}: key {t!r} -> {v!r}")

    with open(a.out, "w") as fh:
        fh.write("# generated by lowrange_concordance.py (A2-CAS, 2 Oct 2026); grade M at most, not merged into key.tsv\n")
        fh.write("group\tcandidate\toccurrences\trecords\trunner_up\tframes\n")
        for g in sorted(real, key=lambda x: (-real[x][0][0], int(x))):
            top = real[g][0]
            ru = f"{real[g][1][2]}:{real[g][1][0]}" if len(real[g]) > 1 else ""
            fr = "; ".join(f"{r}@{i} {f[0]}({','.join(f[1:])})" for r, i, f in top[3][:6])
            fh.write(f"{g}\t{top[2]}\t{top[0]}\t{top[1]}\t{ru}\t{fr}\n")
    print(f"wrote {a.out}")


if __name__ == "__main__":
    main()

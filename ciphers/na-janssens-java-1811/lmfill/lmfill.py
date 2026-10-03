#!/usr/bin/env python3
"""LM-context fill of the No.4 conflict codes (GAPS17, 3 Oct 2026). Thresholds pre-registered in lmfill/PREREG.md
(commit e5ff7541) before this script scored anything.

Usage: python3 lmfill/lmfill.py   (run from the target folder; writes lmfill/results.tsv and lmfill/known_answer.tsv)
"""
import csv, math, random, re, sys
from collections import defaultdict
from pathlib import Path

HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import judge_plaintext as jp  # noqa: E402

ORDER, WIN, MARGIN, SEEDS, KA_PREC, KA_MIN, MASK = 5, 3, 1.0, 20, 0.85, 15, 56 / 163


class LM:
    def __init__(self, text):
        self.c = [defaultdict(int) for _ in range(ORDER + 1)]
        self.hc = [defaultdict(int) for _ in range(ORDER + 1)]
        self.f = [defaultdict(set) for _ in range(ORDER + 1)]
        t = "^" * (ORDER - 1) + text
        for i in range(ORDER - 1, len(t)):
            for n in range(1, ORDER + 1):
                h, ch = t[i - n + 1:i], t[i]
                self.c[n][h + ch] += 1
                self.hc[n][h] += 1
                self.f[n][h].add(ch)
        self.tot = sum(v for k, v in self.c[1].items())

    def p(self, h, ch):
        pr = (self.c[1].get(ch, 0) + 1) / (self.tot + 27)
        for n in range(2, ORDER + 1):
            hh = h[-(n - 1):]
            if len(hh) < n - 1:
                break
            ch_n = self.hc[n].get(hh, 0)
            if not ch_n:
                continue
            types = len(self.f[n][hh])
            lam = ch_n / (ch_n + types)
            pr = lam * self.c[n].get(hh + ch, 0) / ch_n + (1 - lam) * pr
        return pr

    def score(self, s):
        t = "^" * (ORDER - 1) + s
        return sum(math.log10(self.p(t[i - ORDER + 1:i], t[i])) for i in range(ORDER - 1, len(t)))


def rows(p):
    return list(csv.DictReader(open(HERE / p, encoding="utf-8"), delimiter="\t"))


def sequences(key):
    seqs = []
    for p in ("keysource_passA.tsv", "keysource_no5_passA.tsv", "leaf192_reconciled.tsv", "leaf201_reconciled.tsv",
              "no4/no4_merge.tsv"):
        by = defaultdict(list)
        for r in rows(p):
            by[r["leaf"]].append((int(r["order"]), r["code"].strip(), r["gloss"].strip(), r.get("note", "") or ""))
        for leaf, lst in by.items():
            lst.sort()
            seqs.append((p + ":" + leaf, [(c, g, n) for _, c, g, n in lst]))
    l188 = [(r["sign"].strip(), key.get(r["sign"].strip(), ""), "") for r in rows("ciphertext.tsv")]
    seqs.append(("188", l188))
    return seqs


def contexts(seqs, code, mask_rng=None):
    return [ctx_at(s, i, name, mask_rng) for name, s in seqs for i, (c, _, _) in enumerate(s) if c == code]


def ctx_at(s, i, name, mask_rng=None):
    if True:
        if True:
            L, R = [], []
            for j in range(i - 1, max(-1, i - 1 - WIN), -1):
                v = s[j][1] if not (mask_rng and mask_rng.random() < MASK) else ""
                if not jp.fold(v):
                    break
                L.insert(0, jp.fold(v))
            for j in range(i + 1, min(len(s), i + 1 + WIN)):
                v = s[j][1] if not (mask_rng and mask_rng.random() < MASK) else ""
                if not jp.fold(v):
                    break
                R.append(jp.fold(v))
            return ("".join(L), "".join(R), name)


def total(lm, ctxs, v):
    fv = jp.fold(v)
    return sum(lm.score(l + fv + r) for l, r, _ in ctxs)


def judge_code(lm, ctxs, values, pool, seed0):
    sc = {v: total(lm, ctxs, v) for v in values}
    rank = sorted(values, key=lambda v: -sc[v])
    win, run = rank[0], rank[1]
    margin = sc[win] - sc[run]
    sh = []
    for s in range(SEEDS):
        rng = random.Random(seed0 * 1000 + s)
        draw = [pool[rng.randrange(len(pool))] for _ in ctxs]
        sh.append(total(lm, draw, win) - total(lm, draw, run))
    shmax = max(sh)
    return win, run, margin, shmax, margin >= MARGIN and margin > shmax, sc


def decoy(v):
    f = v.strip()
    if len(jp.fold(f)) > 2 and f[-1].lower() in "stex":
        return f[:-1]
    return f + "s"


def main():
    key = {r["code"].strip(): r["value"].strip() for r in rows("key.tsv")}
    grade = {r["code"].strip(): r["grade"].strip() for r in rows("key.tsv")}
    conf = [r for r in rows("conflicts.tsv") if "no4" in r["variants"]]
    conf_codes = {r["code"].strip() for r in rows("conflicts.tsv")}
    text = "".join(jp.fold(jp.read_corpus(p)) for p in jp.LANG_CORPORA["fr1810"])
    lm = LM(text)
    seqs = sequences(key)
    allctx = {}
    for name, s in seqs:
        for c, _, _ in s:
            if c not in allctx:
                allctx[c] = contexts(seqs, c)

    # known-answer (No.4 matched control) first: the method gate
    no4 = [s for n, s in seqs if n.startswith("no4/")]
    rng = random.Random(17)
    ka = []
    for s in no4:
        for i, (c, g, note) in enumerate(s):
            if note or c in conf_codes or grade.get(c) != "C" or len(jp.fold(g)) < 1:
                continue
            ctx = [ctx_at(s, i, "no4", rng)]
            d = decoy(g)
            if jp.fold(d) == jp.fold(g):
                continue
            pool = [x for cc, xs in allctx.items() if cc != c for x in xs]
            win, run, m, shmax, ok, _ = judge_code(lm, ctx, [g, d], pool, 900 + i)
            ka.append((c, g, d, win, round(m, 3), round(shmax, 3), ok, win == g))
    cleared = [k for k in ka if k[6]]
    prec = sum(k[7] for k in cleared) / len(cleared) if cleared else 0.0
    raw_acc = sum(k[7] for k in ka) / len(ka) if ka else 0.0
    method_ok = prec >= KA_PREC and len(cleared) >= KA_MIN
    with open(HERE / "lmfill/known_answer.tsv", "w", encoding="utf-8") as f:
        f.write("code\ttrue\tdecoy\twinner\tmargin\tshuffle_max\tclears_1_2\tcorrect\n")
        for k in ka:
            f.write("\t".join(map(str, k)) + "\n")
    print(f"known-answer: items {len(ka)}, argmax correct {raw_acc:.3f}; cleared gates 1-2: {len(cleared)}, "
          f"precision {prec:.3f} -> method gate {'PASS' if method_ok else 'FAIL'} (needs >= {KA_PREC} on >= {KA_MIN})")

    out = []
    for r in conf:
        code = r["code"].strip()
        vals = []
        for part in r["variants"].split(";"):
            v = re.sub(r"\s*\(n=.*$", "", part.strip())
            if v and v not in vals:
                vals.append(v)
        folded = {jp.fold(v) for v in vals}
        ctxs = allctx.get(code, [])
        if len(folded) < 2:
            out.append((code, "|".join(vals), len(ctxs), "", "", "", "", "untested-by-this-tool (values fold equal)"))
            continue
        # one representative per folded form, keeping the order of first attestation
        rep, seen = [], set()
        for v in vals:
            if jp.fold(v) not in seen:
                seen.add(jp.fold(v)); rep.append(v)
        pool = [x for cc, xs in allctx.items() if cc != code for x in xs]
        win, run, m, shmax, ok, sc = judge_code(lm, ctxs, rep, pool, int(code))
        moves = ok and method_ok
        out.append((code, "|".join(vals), len(ctxs), win, run, round(m, 3), round(shmax, 3),
                    "MOVE" if moves else ("clears 1-2, method gate failed" if ok else "stays (fails gate 1 or 2)")))
    with open(HERE / "lmfill/results.tsv", "w", encoding="utf-8") as f:
        f.write("code\tvalues\tn_contexts\twinner\trunner_up\tmargin_log10\tshuffle_max\tdecision\n")
        for o in out:
            f.write("\t".join(map(str, o)) + "\n")
    for o in out:
        print("\t".join(map(str, o)))


if __name__ == "__main__":
    main()

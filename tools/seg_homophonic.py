#!/usr/bin/env python3
"""Joint segmentation + homophonic substitution solver for unseparated digit ciphers, with matched controls.

Written 24 Sept 2026 for ciphers/fr4687-paleologue-nevers. Own code (nothing copied from the solver repos).

The ciphertext is a stream of signs (digits, plus any extra sign such as 'y') with no group boundaries. A
design is (P, ymode): P is the set of 'prefix' signs that always open a two-sign unit (e.g. P={1,2} reads
1x and 2x as two-digit numbers and every other sign as a single unit); a prefix sign at a line end or
before a non-digit is read as a single unit and counted as a parse exception. ymode is 'letter' (y is its
own unit) or 'null' (y dropped). Segmentation is searched over the design space (every design in --designs),
and for each design the unit-to-letter key (homophonic: many units may share a letter) is annealed with
several restarts against a period character 5-gram model (tools/italian_ngram.py format, full conditional
log-probabilities), then finished by steepest ascent. Designs are compared by z against the same solver on
sign-shuffled copies of the same text under the same design (more unit types always buy a higher raw
score, so raw scores are not comparable across designs).

Subcommands
  solve    --cipher FILE --model M.npz [--designs 12:letter,12:null,...] [--restarts 8] [--iters 40000]
           [--nulls 5] [--out DIR]
  control  --plain HELDOUT --model M.npz --units N [--noise 0.05] [--seeds 5] [--design 12:letter]
           [--y-rate 0.066] ...   synthetic control: held-out Italian of N letters, random homophonic key
           over the same unit inventory as the design, enciphered to signs, joined per line without
           separators, sign noise (4<->9 swaps, drops, insertions) at --noise, then solved blind; reports
           per-token letter accuracy.
  decode   --cipher FILE --key KEY.tsv --design D   print the reading under a key.

Cipher file: one line per manuscript line, 'line_id<TAB>signs' (signs as a string). Lines sharing the
prefix before '_L' are one passage and are scored as one continuous text.
"""
import argparse
import os
import random
import sys
from collections import Counter

import numpy as np

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from italian_ngram import ALPHA, IDX, K, norm  # noqa: E402

NL = len(ALPHA)


class LM:
    def __init__(self, path, kl_weight=0.0):
        z = np.load(path)
        self.order = int(z["order"])
        self.logp = (z["llr"].reshape(-1, K) + np.log(z["p1"]).reshape(1, K)).reshape(-1).astype(np.float32)
        self.p1 = z["p1"][:NL] / z["p1"][:NL].sum()
        self.kl_weight = kl_weight

    def score_passages(self, arrs):
        o = self.order
        tot = 0.0
        for x in arrs:
            y = np.concatenate([np.full(o - 1, IDX["#"], dtype=np.int64), x])
            n = len(y) - o + 1
            idx = y[:n].copy()
            for j in range(1, o):
                idx = idx * K + y[j:j + n]
            tot += float(self.logp[idx].sum())
        if self.kl_weight:
            # guard against degenerate keys (all units -> one frequent letter): penalise the divergence of
            # the decoded letter distribution from the model's, n * KL(q || p), scaled by kl_weight
            allx = np.concatenate(arrs)
            q = np.bincount(allx, minlength=NL)[:NL] / max(len(allx), 1)
            m = q > 0
            tot -= self.kl_weight * len(allx) * float((q[m] * np.log(q[m] / self.p1[m])).sum())
        return tot


def parse_design(s):
    p, _, ym = s.partition(":")
    return set(p) if p != "-" else set(), (ym or "letter")


def segment(lines, P, ymode):
    """lines: list of (line_id, signs). Returns passages: list of lists of unit strings; exceptions count."""
    passages, cur, curp, exc = [], None, None, 0
    for lid, s in lines:
        pid = lid.split("_L")[0]
        if pid != curp:
            cur = []
            passages.append(cur)
            curp = pid
        i = 0
        while i < len(s):
            c = s[i]
            if c == "y" and ymode == "null":
                i += 1
                continue
            if c in P:
                if i + 1 < len(s) and s[i + 1].isdigit():
                    cur.append(s[i:i + 2])
                    i += 2
                    continue
                exc += 1
            cur.append(c)
            i += 1
    return passages, exc


class Problem:
    def __init__(self, passages):
        self.types = sorted({u for p in passages for u in p}, key=lambda u: (len(u), u))
        self.tid = {u: i for i, u in enumerate(self.types)}
        self.seqs = [np.array([self.tid[u] for u in p], dtype=np.int64) for p in passages]
        self.counts = Counter(u for p in passages for u in p)
        self.n = sum(len(p) for p in passages)

    def text(self, key):
        return [key[s] for s in self.seqs]


def anneal(prob, lm, rng, iters=40000, restarts=8, t0=None):
    T = len(prob.types)
    order_letters = np.argsort(-lm.p1)
    best_key, best = None, -1e18
    t0 = t0 if t0 is not None else 60.0
    for r in range(restarts):
        if r == 0:  # frequency-rank start
            ranked = sorted(range(T), key=lambda t: -prob.counts[prob.types[t]])
            key = np.zeros(T, dtype=np.int64)
            for i, t in enumerate(ranked):
                key[t] = order_letters[i % 12]
        else:
            key = rng.choice(NL, size=T, p=lm.p1).astype(np.int64)
        cur = lm.score_passages(prob.text(key))
        for it in range(iters):
            temp = t0 * (1 - it / iters) + 1e-3
            t = rng.integers(T)
            old = key[t]
            if rng.random() < 0.8:
                key[t] = rng.integers(NL)
                if key[t] == old:
                    continue
                s = lm.score_passages(prob.text(key))
                if s >= cur or rng.random() < np.exp((s - cur) / temp):
                    cur = s
                else:
                    key[t] = old
            else:
                u = rng.integers(T)
                if key[u] == old:
                    continue
                key[t], key[u] = key[u], old
                s = lm.score_passages(prob.text(key))
                if s >= cur or rng.random() < np.exp((s - cur) / temp):
                    cur = s
                else:
                    key[u], key[t] = key[t], old
        # steepest ascent finish
        improved = True
        while improved:
            improved = False
            for t in range(T):
                old = key[t]
                bl, bs = old, cur
                for c in range(NL):
                    if c == old:
                        continue
                    key[t] = c
                    s = lm.score_passages(prob.text(key))
                    if s > bs + 1e-6:
                        bl, bs = c, s
                key[t] = bl
                if bl != old:
                    cur, improved = bs, True
        if cur > best:
            best, best_key = cur, key.copy()
    return best_key, best


def read_cipher(path):
    out = []
    for l in open(path):
        if l.startswith("#") or not l.strip():
            continue
        lid, s = l.rstrip("\n").split("\t")[:2]
        out.append((lid, s))
    return out


def shuffled(lines, rng):
    allsig = [c for _, s in lines for c in s]
    rng.shuffle(allsig)
    out, i = [], 0
    for lid, s in lines:
        out.append((lid, "".join(allsig[i:i + len(s)])))
        i += len(s)
    return out


def solve_design(lines, lm, design, rng, iters, restarts):
    P, ym = parse_design(design)
    passages, exc = segment(lines, P, ym)
    prob = Problem(passages)
    key, sc = anneal(prob, lm, rng, iters=iters, restarts=restarts)
    return prob, key, sc, exc


def cmd_solve(a):
    lm = LM(a.model, a.kl)
    lines = read_cipher(a.cipher)
    rng = np.random.default_rng(a.seed)
    os.makedirs(a.out, exist_ok=True)
    rows = []
    for d in a.designs.split(","):
        prob, key, sc, exc = solve_design(lines, lm, d, rng, a.iters, a.restarts)
        per = sc / prob.n
        nulls = []
        for k in range(a.nulls):
            if a.null_kind == "units":  # same units and counts, order destroyed: tests sequential structure
                us = [u for p in segment(lines, *parse_design(d))[0] for u in p]
                random.Random(a.seed * 100 + k).shuffle(us)
                p2, i = [], 0
                for p in segment(lines, *parse_design(d))[0]:
                    p2.append(us[i:i + len(p)])
                    i += len(p)
                _, s2 = anneal(Problem(p2), lm, rng, iters=a.iters, restarts=max(2, a.restarts // 2))
            else:  # signs shuffled, then segmented: also destroys the unit inventory
                sl = shuffled(lines, random.Random(a.seed * 100 + k))
                _, _, s2, _ = solve_design(sl, lm, d, rng, a.iters, max(2, a.restarts // 2))
                p2, _ = segment(sl, *parse_design(d))
            nulls.append(s2 / sum(len(p) for p in p2))
        mu, sd = (float(np.mean(nulls)), float(np.std(nulls)) or 1e-9) if nulls else (0.0, 1.0)
        z = (per - mu) / sd if nulls else float("nan")
        txt = "|".join("".join(ALPHA[c] for c in t) for t in prob.text(key))
        rows.append((d, prob.n, len(prob.types), exc, per, mu, sd, z, txt))
        tag = d.replace(":", "_")
        with open(os.path.join(a.out, f"key_{tag}.tsv"), "w") as f:
            f.write("unit\tcount\tletter\n")
            for i, u in enumerate(prob.types):
                f.write(f"{u}\t{prob.counts[u]}\t{ALPHA[key[i]]}\n")
        print(f"{d}\tunits={prob.n}\ttypes={len(prob.types)}\texc={exc}\tscore/unit={per:.3f}\t"
              f"null={mu:.3f}+-{sd:.3f}\tz={z:.2f}\n  {txt}", flush=True)
    with open(os.path.join(a.out, "designs.tsv"), "w") as f:
        f.write("design\tunits\ttypes\tparse_exceptions\tscore_per_unit\tnull_mean\tnull_sd\tz\treading\n")
        for r in rows:
            f.write("\t".join(str(round(x, 4)) if isinstance(x, float) else str(x) for x in r) + "\n")


def make_control(plain_lines, n_letters, design, line_lengths, rng, noise, y_rate):
    """Synthetic cipher: n letters of held-out text, random homophonic key over the design's unit
    inventory, enciphered, cut at the target's line lengths (in signs), sign noise added."""
    P, ym = parse_design(design)
    text = "".join(l.replace("#", "") for l in plain_lines)
    st = rng.integers(0, len(text) - n_letters)
    pt = text[st:st + n_letters]
    singles = [d for d in "0123456789" if d not in P] + (["y"] if ym == "letter" else [])
    doubles = [p + d for p in sorted(P) for d in "0123456789"]
    units = singles + doubles
    # homophones: more units to frequent letters, as a period homophonic table would
    freq = Counter(pt)
    letters = [c for c, _ in freq.most_common()]
    assign = {}
    pool = units[:]
    rng.shuffle(pool)
    for i, u in enumerate(pool):
        assign.setdefault(letters[i % len(letters)] if i < len(letters) else
                          letters[int(rng.integers(0, min(8, len(letters))))], []).append(u)
    units_ct = []
    for c in pt:
        u = assign[c][int(rng.integers(len(assign[c])))]
        if ym == "null" and rng.random() < y_rate:
            u = u + "y"
        units_ct.append(u)
    # lines are cut at unit boundaries (the scribe does not split a number across lines)
    raw, cur, k = [], "", 0
    for u in units_ct:
        cur += u
        if len(cur) >= line_lengths[k % len(line_lengths)]:
            raw.append(cur)
            cur, k = "", k + 1
    if cur:
        raw.append(cur)

    def noisy(sg):  # 4<->9 confusions, drops, insertions
        out = []
        for c in sg:
            r = rng.random()
            if r < noise / 3:
                continue
            if r < 2 * noise / 3 and c in "49":
                c = "9" if c == "4" else "4"
            out.append(c)
            if rng.random() < noise / 3:
                out.append(str(rng.integers(0, 10)))
        return "".join(out)
    lines = [(f"c{k // 6}_L{k}", noisy(sg)) for k, sg in enumerate(raw)]
    return lines, pt, assign


def cmd_control(a):
    lm = LM(a.model, a.kl)
    plain = [l.strip() for l in open(a.plain) if l.strip()]
    tgt = read_cipher(a.cipher) if a.cipher else []
    lens = [len(s) for _, s in tgt] or [38]
    accs = []
    for seed in range(a.seeds):
        rng = np.random.default_rng(a.seed0 + seed)
        lines, pt, assign = make_control(plain, a.units, a.design, lens, rng, a.noise, a.y_rate)
        prob, key, sc, exc = solve_design(lines, lm, a.solve_design or a.design, rng, a.iters, a.restarts)
        dec = "".join("".join(ALPHA[c] for c in t) for t in prob.text(key))
        if a.noise == 0 and (a.solve_design or a.design) == a.design:
            acc = sum(x == y for x, y in zip(dec, pt)) / len(pt)
        else:  # noise shifts alignment: score by matching 5-grams of the truth found in the decode
            import difflib
            sm = difflib.SequenceMatcher(None, pt, dec, autojunk=False)
            acc = sum(b.size for b in sm.get_matching_blocks()) / len(pt)
        accs.append(acc)
        print(f"seed {seed}: signs={sum(len(s) for _, s in lines)} units={prob.n} types={len(prob.types)} "
              f"exc={exc} acc={acc:.3f}\n  truth {pt[:90]}\n  read  {dec[:90]}", flush=True)
    print(f"CONTROL design={a.design} solved_as={a.solve_design or a.design} noise={a.noise} units={a.units}: "
          f"mean acc {np.mean(accs):.3f}, per seed {' '.join(f'{x:.2f}' for x in accs)}")


def cmd_decode(a):
    lines = read_cipher(a.cipher)
    P, ym = parse_design(a.design)
    passages, _ = segment(lines, P, ym)
    key = {}
    for l in open(a.key):
        f = l.rstrip("\n").split("\t")
        if f[0] != "unit":
            key[f[0]] = f[2]
    for p in passages:
        print(" ".join(f"{u}={key.get(u, '?')}" for u in p))
        print("".join(key.get(u, "?") for u in p))


def main():
    ap = argparse.ArgumentParser()
    sp = ap.add_subparsers(dest="cmd", required=True)
    s = sp.add_parser("solve")
    s.add_argument("--cipher", required=True)
    s.add_argument("--model", required=True)
    s.add_argument("--designs", default="12:letter,12:null,1:letter,2:letter")
    s.add_argument("--restarts", type=int, default=8)
    s.add_argument("--iters", type=int, default=150000)
    s.add_argument("--kl", type=float, default=3.0, help="weight of the unigram-divergence guard")
    s.add_argument("--nulls", type=int, default=3)
    s.add_argument("--null-kind", choices=["signs", "units"], default="signs")
    s.add_argument("--seed", type=int, default=1)
    s.add_argument("--out", default=".")
    c = sp.add_parser("control")
    c.add_argument("--plain", required=True)
    c.add_argument("--model", required=True)
    c.add_argument("--cipher", help="target cipher file, for line lengths")
    c.add_argument("--units", type=int, default=420)
    c.add_argument("--design", default="12:letter")
    c.add_argument("--solve-design", help="design the solver assumes (default: the true one)")
    c.add_argument("--noise", type=float, default=0.0)
    c.add_argument("--y-rate", type=float, default=0.066)
    c.add_argument("--seeds", type=int, default=5)
    c.add_argument("--seed0", type=int, default=1000)
    c.add_argument("--restarts", type=int, default=8)
    c.add_argument("--iters", type=int, default=150000)
    c.add_argument("--kl", type=float, default=3.0, help="weight of the unigram-divergence guard")
    d = sp.add_parser("decode")
    d.add_argument("--cipher", required=True)
    d.add_argument("--key", required=True)
    d.add_argument("--design", required=True)
    a = ap.parse_args()
    {"solve": cmd_solve, "control": cmd_control, "decode": cmd_decode}[a.cmd](a)


if __name__ == "__main__":
    main()

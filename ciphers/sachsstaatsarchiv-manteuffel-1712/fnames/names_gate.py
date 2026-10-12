#!/usr/bin/env python3
"""MANT-NAMES cross-leaf name-code consistency gate (fnames/PREREG-MANT-NAMES.md, pushed b896c059d before any score).

Power check first (key-validated leaves subsampled to the target's run count); exits 3 without scoring the target if power < 0.80.
Otherwise scores the target set (fpoolu + f0491_08) against a key-permuted null (gate) and a frame-label-shuffled null (reported only).
--check regenerates every output and exits 1 if a committed file differs (rule 7).
"""
import csv, os, random, sys, unicodedata
from itertools import combinations

HERE = os.path.dirname(os.path.abspath(__file__))
T = os.path.dirname(HERE)
SEED = 20261012
NPERM, NPOW, NPOWPERM = 1000, 200, 200


def norm(s):
    s = unicodedata.normalize("NFD", s.lower())
    s = "".join(c for c in s if not unicodedata.combining(c)).strip()
    for art in ("le ", "la ", "l'", "der "):
        if s.startswith(art):
            s = s[len(art):]
            break
    return "".join(c for c in s if c.isalpha())


def load_key():
    vals, names = {}, set()
    for r in csv.DictReader(open(os.path.join(T, "key.tsv")), delimiter="\t"):
        first = r["value"].split("|")[0]
        v = "".join(c for c in norm(first) if c.isalpha()) if not first.lower().startswith(("le ", "la ")) else "".join(
            c for c in first.lower() if c.isalpha())
        vals[r["code"]] = (first, v)
        n = norm(first)
        if r["grade"] == "C" and len(n) >= 4:
            names.add(n)
    letter = {c: v for c, (f, v) in vals.items() if 1 <= len(v) <= 3}
    return letter, sorted(names)


def read_runs(path, signcol="sign"):
    rows = [l for l in open(path) if not l.startswith("#")]
    out = {}
    for r in csv.DictReader(rows, delimiter="\t"):
        out.setdefault(r["line"], []).append(r[signcol].strip())
    return out


def letter_runs(frame, lines, letter):
    """maximal letter-like stretches inside each line -> (frame, line, codes)"""
    res = []
    for ln, codes in lines.items():
        cur = []
        for c in codes + [None]:
            if c is not None and c in letter:
                cur.append(c)
            else:
                if cur:
                    res.append((frame, ln, tuple(cur)))
                cur = []
    return res


def dec(codes, m):
    return [m.get(c, "?") for c in codes]


def prefix_parts(codes, m):
    """per-code decoded parts; the decode string is their concatenation"""
    return dec(codes, m)


def common_prefix_info(a_codes, a_parts, b_codes, b_parts):
    sa, sb = "".join(a_parts), "".join(b_parts)
    k = 0
    while k < min(len(sa), len(sb)) and sa[k] == sb[k] and sa[k] != "?":
        k += 1
    if k < 4:
        return k, False

    def codes_covering(codes, parts, k):
        out, n = [], 0
        for c, p in zip(codes, parts):
            if n >= k:
                break
            out.append(c)
            n += len(p)
        return out
    ca, cb = codes_covering(a_codes, a_parts, k), codes_covering(b_codes, b_parts, k)
    return k, ca != cb


def stat(runs, m, names, detail=False):
    """runs: list of (frame, line, codes); only decodes of length >= 3 enter"""
    items = []
    for fr, ln, codes in runs:
        parts = dec(codes, m)
        if len("".join(parts)) >= 3:
            items.append((fr, ln, codes, parts))
    ta, tb, det = 0, 0, []
    for x, y in combinations(items, 2):
        if x[0] == y[0]:
            continue
        k, differ = common_prefix_info(x[2], x[3], y[2], y[3])
        if k >= 4 and differ:
            ta += 1
            if detail:
                det.append(("pair", f"{x[0]}:{x[1]}", ".".join(x[2]), "".join(x[3]), f"{y[0]}:{y[1]}", ".".join(y[2]), "".join(y[3]), k))
    for fr, ln, codes, parts in items:
        s = "".join(parts)
        hit = [n for n in names if len(os.path.commonprefix([s, n])) >= 4 and "?" not in os.path.commonprefix([s, n])]
        if hit:
            tb += 1
            if detail:
                det.append(("name", f"{fr}:{ln}", ".".join(codes), s, ";".join(hit), "", "", ""))
    return ta + tb, ta, tb, len(items), det


def permuted(letter, rng):
    codes = sorted(letter)
    vals = [letter[c] for c in codes]
    rng.shuffle(vals)
    return dict(zip(codes, vals))


def pval(runs, letter, names, rng, n):
    real = stat(runs, letter, names)[0]
    ge = sum(1 for _ in range(n) if stat(runs, permuted(letter, rng), names)[0] >= real)
    return real, (1 + ge) / (n + 1)


def main():
    letter, names = load_key()
    rng = random.Random(SEED)
    target = []
    pool = read_runs(os.path.join(T, "fpoolu", "ciphertext.tsv"))
    byframe = {}
    for ln, codes in pool.items():
        byframe.setdefault(ln[:4], {})[ln] = codes
    for fr in sorted(byframe):
        target += letter_runs(fr, byframe[fr], letter)
    target += letter_runs("0491", read_runs(os.path.join(T, "f0491_08", "ciphertext.tsv")), letter)
    K = stat(target, letter, names)[3]

    # power pool: key-validated leaves (>= 60% H/C/S)
    power = {}
    for d in sorted(os.listdir(T)):
        p = os.path.join(T, d, "reading_tokens.tsv")
        if d == "fpoolu" or not os.path.isfile(p):
            continue
        rows = list(csv.DictReader(open(p), delimiter="\t"))
        if rows and sum(r["grade"] in ("H", "C", "S") for r in rows) / len(rows) >= 0.60:
            lines = {}
            for r in rows:
                lines.setdefault(r["line"], []).append(r["sign"].strip())
            runs = [x for x in letter_runs(d, lines, letter) if len("".join(dec(x[2], letter))) >= 3]
            power[d] = runs
    pw = [f"# power pool (>=60% H/C/S): {' '.join(f'{d}:{len(r)}' for d, r in power.items())}", f"# target runs (decode>=3): K={K}"]
    hits, reals = 0, []
    frames = sorted(power)
    done = 0
    while done < NPOW:
        pick = rng.sample(frames, min(7, len(frames)))
        allr = [x for d in pick for x in power[d]]
        if len(allr) < K:
            continue
        sub = rng.sample(allr, K)
        real, p = pval(sub, letter, names, rng, NPOWPERM)
        reals.append(real)
        hits += p <= 0.01
        done += 1
    pwr = hits / NPOW
    pw.append(f"power = {hits}/{NPOW} = {pwr:.3f} (subsample real T mean {sum(reals)/len(reals):.2f}); gate power >= 0.80 -> "
              + ("TEST" if pwr >= 0.80 else "NON-TEST at this N"))
    outs = {"power.out": "\n".join(pw) + "\n"}
    code = 0
    det_rows = [("kind", "run_a", "codes_a", "decode_a", "run_b_or_names", "codes_b", "decode_b", "prefix_len")]
    if pwr < 0.80:
        outs["gate.out"] = "NOT SCORED: power check failed (PREREG: stop, log non-test at this N)\n"
        code = 3
    else:
        real, ta, tb, n, det = stat(target, letter, names, detail=True)
        nulls = [stat(target, permuted(letter, rng), names)[0] for _ in range(NPERM)]
        p = (1 + sum(x >= real for x in nulls)) / (NPERM + 1)
        fr_nulls = []
        for _ in range(NPERM):
            labs = [x[0] for x in target]
            rng.shuffle(labs)
            fr_nulls.append(stat([(l, x[1], x[2]) for l, x in zip(labs, target)], letter, names)[0])
        pf = (1 + sum(x >= real for x in fr_nulls)) / (NPERM + 1)
        outs["gate.out"] = (f"target runs {n}; T={real} (T_a {ta}, T_b {tb}); key-permuted null mean {sum(nulls)/NPERM:.2f}, "
                            f"p={p:.4f} -> {'PASS' if p <= 0.01 else 'FAIL'}\n"
                            f"frame-shuffled null (reported only) mean {sum(fr_nulls)/NPERM:.2f}, p={pf:.4f}\n")
        det_rows += det
    for item in ("13 alone (0088 x5)", "103.34.26(.27) on 0483 and 0491 (identical cipher)", "390 / 252 / 150 / 187 / 217 / 257 singletons"):
        det_rows.append(("non-test", item, "", "same codes decode identically under every key", "", "", "", ""))
    outs["per_code.tsv"] = "".join("\t".join(map(str, r)) + "\n" for r in det_rows)
    check = "--check" in sys.argv
    stale = False
    for fn, txt in outs.items():
        fp = os.path.join(HERE, fn)
        if check:
            if not os.path.isfile(fp) or open(fp).read() != txt:
                print(f"STALE {fn}")
                stale = True
        else:
            open(fp, "w").write(txt)
    print(outs["power.out"] + outs["gate.out"], end="")
    if check:
        sys.exit(1 if stale else 0)
    sys.exit(code)


if __name__ == "__main__":
    main()

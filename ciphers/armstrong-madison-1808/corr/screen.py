#!/usr/bin/env python3
"""H26 correspondent-pool signature screen (ARM-CORR, 28 Sept 2026): NOT a result, a screen.

Reuses the ARM3-LIVCODE screen (pool/signature_test.py digit shape, pool/cor/overlap_test.py top-20
overlap with its THE=972 pooled sample and 200 random draws) on a candidate coded letter's group list,
and adds the three H25/H26 statistics the brief names: units-digit 0/1 share on values >= 100 and on
2-digit groups, share of values above 1700, and decade (hundreds-block) coverage. Every candidate number
is printed beside the target's own (computed live from ciphertext.txt) and the THE=972 usage baseline
(the four decoded Armstrong THE=972 letters in tools/data/uscodes-1800/decodes/, pooled), so a MATCH can
only be claimed against both. Rule 3: a screen at N ~ 150 is not a family test; a MATCH here means "pool
candidate for a full transcription", a MISS means "not the target's code on this sample".

Usage:
    python3 screen.py corr/erving1807_groups.tsv [more.tsv ...]
"""
import pathlib, re, sys, random
HERE = pathlib.Path(__file__).resolve().parent
TGT = HERE.parent
sys.path.insert(0, str(TGT / "pool" / "cor"))
import overlap_test as ot  # noqa: E402

def load_groups_tsv(p):
    out = []
    for line in open(p):
        if line.startswith("#") or not line.strip():
            continue
        _, gs = line.rstrip("\n").split("\t", 1)
        for g in gs.split():
            m = re.match(r"^(\d+)", g)
            if m:
                out.append(int(m.group(1)))
    return out

def load_target():
    out = []
    for line in open(TGT / "ciphertext.txt"):
        if line.startswith("#"):
            continue
        out += [int(t) for t in line.split() if t.isdigit()]
    return out

def load_the972_usage():
    out = []
    for p in sorted((TGT.parent.parent / "tools" / "data" / "uscodes-1800" / "decodes").glob("*.txt")):
        out += [int(x) for x in re.findall(r"\{(\d+)\}", open(p).read())]
    return out

def stats(v):
    n = len(v)
    big = [x for x in v if x >= 100]
    two = [x for x in v if 10 <= x < 100]
    u01 = lambda xs: (sum(1 for x in xs if x % 10 in (0, 1)) / len(xs)) if xs else float("nan")
    u2359 = lambda xs: (sum(1 for x in xs if x % 10 in (2, 3, 5, 9)) / len(xs)) if xs else float("nan")
    return dict(n=n, distinct=len(set(v)), max=max(v), u01_big=u01(big), n_big=len(big), u01_two=u01(two), n_two=len(two),
                u2359_big=u2359(big), above1700=sum(1 for x in v if x > 1700) / n, under100=sum(1 for x in v if x < 100) / n,
                decades=len({x // 100 for x in v}), top=sorted(((v.count(x), x) for x in set(v)), reverse=True)[:8])

def fmt(name, s):
    return (f"{name:28s} n={s['n']:4d} dist={s['distinct']:4d} max={s['max']:5d} | units0/1 >=100: {s['u01_big']:.2f} (n={s['n_big']}) "
            f"2-digit: {s['u01_two']:.2f} (n={s['n_two']}) | units2/3/5/9 >=100: {s['u2359_big']:.2f} | >1700: {s['above1700']:.3f} | <100: {s['under100']:.2f} | "
            f"hundreds-blocks: {s['decades']} | top: {' '.join(f'{v}x{c}' for c, v in s['top'])}")

def main():
    target = load_target(); the972 = load_the972_usage()
    print("REFERENCE")
    print(fmt("target 20 Feb 1808", stats(target)))
    print(fmt("THE=972 usage (4 letters)", stats(the972)))
    random.seed(26092026)
    for p in sys.argv[1:]:
        v = load_groups_tsv(p); s = stats(v)
        print("\nCANDIDATE", p)
        print(fmt(pathlib.Path(p).stem, s))
        # subsampled references at the candidate's own n (rule 3: compare at matched N)
        for name, ref in (("target@n", target), ("THE=972@n", the972)):
            draws = [stats(random.sample(ref, min(len(ref), s["n"]))) for _ in range(200)]
            for key in ("u01_big", "above1700", "under100"):
                xs = sorted(d[key] for d in draws)
                print(f"   {name:12s} {key:10s} p05={xs[10]:.3f} median={xs[100]:.3f} p95={xs[190]:.3f}   candidate={s[key]:.3f}")
        k, n = ot.overlap(v); chance = ot.random_draw_chance(n)
        k972, n972 = ot.overlap(ot.THE972_SAMPLE)
        print(f"   top-20 overlap: candidate {k}/{n} shared with target top-20; THE=972 pooled sample {k972}/{n972}; random-draw chance of >=3 at n={n}: {chance}")
        match = (s["u01_big"] >= 0.4 and s["above1700"] >= 0.05 and s["under100"] >= 0.2)
        print("   VERDICT:", "MATCH (pool candidate: target-like on all three -- transcribe in full)" if match else "MISS (not the target's code on this sample)")

if __name__ == "__main__":
    main()

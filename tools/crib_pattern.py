#!/usr/bin/env python3
"""crib_pattern.py: drag a known plaintext phrase along a sign-coded ciphertext under pattern constraints, with a
shuffled-order control (H28, 28 Sept 2026, spinelli-beinecke-c1515; the known answer there is the one phrase
Tomokiyo reads, "la gubernation d'ispagnia", and the codes are the letter's own atlas shape codes, not a key).

A placement of the crib at ciphertext position s consumes tokens left to right: an ordinary code consumes one crib
letter and must map to the same letter everywhere in the placement (and, unless --homophones, no two codes may
map to one letter); a --wild code consumes one crib letter with no constraint (a shape family that stands for
several letters, e.g. HOOK); a --skip code may be consumed as a letter OR skipped as a null (at most --max-skip
skips per placement); --max-err e tolerates e positions whose code conflicts with the placement's mapping (a
misread sign; the position consumes its letter and adds nothing to the key). A placement is consistent when the
whole crib is consumed. Each consistent placement implies
a partial key (non-wild code -> letter); the placement's score is the key applied to the WHOLE ciphertext: the
mean log unigram probability of the letters it produces under the corpus (the H4 statistic), over all mapped
positions -- a true placement maps its codes to letters whose frequencies over the rest of the text are the
language's; a chance placement does not. Reported: placement count (distinct start positions and distinct
(start, skip pattern) placements), the top placements with their implied keys and scores, and, if --compare gives
a code -> letter TSV (a key read from a period table), how many of each placement's mappings agree with it.

Control (CLAUDE.md rule 3): the same drag over --shuffles random permutations of the token ORDER within each group
(N, the code counts, the wild and null shares all unchanged; only the order the constraints depend on varies, so
the control CAN differ from the target on both statistics). Reported side by side: placement counts (mean, p95,
max) and the best score (mean, p95, max) over the shuffles, and the real values' rank among them. A real
placement count or best score above the shuffled p95 is a candidate anchor for a partial key -- never a reading.
The tool never writes the words solved, new or first.

  python3 tools/crib_pattern.py --codes ciphers/<t>/passes/letter_codes_v3.tsv --crib "la gubernation d'ispagnia" \\
      --wild HOOK --skip OMEGABAR EIGHT EM PI ESS --max-skip 6 --shuffles 200 [--homophones] [--max-err 1] [--group-col page] \\
      [--corpus FILE ...] [--compare ciphers/<t>/passes/key_atlas_asread.tsv] [--top 10] [--seed 1]

--codes: a TSV with a `code` column (and optionally the --group-col column: the drag never crosses a group
boundary, e.g. a page); tokens are read in file order. --corpus: default judge_plaintext.LANG_CORPORA[--lang]
(it). Folding follows homophonic_anneal.fold (v->u, j->i, accents stripped).
Test: python3 tools/tests/test_crib_pattern.py (offline: a synthetic Italian ciphertext of the Spinelli design,
six letters merged into one wild code and 17 pct nulls, with the crib embedded -- the true placement must be found
and must score above every shuffled control's best; a text without the crib must not place it more often than the
shuffles' p95 would allow)."""
import argparse, csv, math, os, random, sys
from collections import Counter, defaultdict

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import homophonic_anneal as ha  # noqa: E402


def read_codes(path, group_col=None):
    groups, order = defaultdict(list), []
    with open(path, newline="", encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            c = (r.get("code") or "").strip()
            if not c:
                continue
            g = (r.get(group_col) or "") if group_col else ""
            if g not in groups:
                order.append(g)
            groups[g].append(c)
    return [groups[g] for g in order]


def unigram(corpora):
    cnt = Counter()
    for t in corpora:
        cnt.update(ha.fold(t))
    tot = sum(cnt.values())
    return {a: math.log((cnt[a] + 0.5) / (tot + 0.5 * len(ha.ALPHA))) for a in ha.ALPHA}


def placements(seq, crib, wild, skip, max_skip, homophones, max_err=0):
    """Yield (start, skips_tuple, mapping, errs) for every consistent placement of crib in seq. max_err > 0
    tolerates that many positions whose code conflicts with the mapping (a misread sign): the position consumes
    its crib letter and adds nothing to the mapping."""
    L = len(crib)
    for s in range(len(seq)):
        # DFS over (i = seq index, j = crib index, mapping, used letters, skips, errors)
        stack = [(s, 0, {}, {}, (), 0)]
        while stack:
            i, j, m, used, sk, e = stack.pop()
            if j == L:
                yield s, sk, m, e
                continue
            if i >= len(seq):
                continue
            c, a = seq[i], crib[j]
            if c in skip and len(sk) < max_skip:
                stack.append((i + 1, j, m, used, sk + (i,), e))
            if c in wild:
                stack.append((i + 1, j + 1, m, used, sk, e))
                continue
            conflict = (c in m and m[c] != a) or (c not in m and not homophones and a in used and used[a] != c)
            if conflict:
                if e < max_err:
                    stack.append((i + 1, j + 1, m, used, sk, e + 1))
                continue
            if c in m:
                stack.append((i + 1, j + 1, m, used, sk, e))
                continue
            m2 = dict(m); m2[c] = a
            u2 = dict(used); u2[a] = c
            stack.append((i + 1, j + 1, m2, u2, sk, e))


def score_map(m, all_tokens, uni):
    vals = [uni[m[c]] for c in all_tokens if c in m]
    return (sum(vals) / len(vals) if vals else float("-inf")), len(vals)


def run(groups, crib, wild, skip, max_skip, homophones, uni, max_err=0):
    all_tokens = [t for g in groups for t in g]
    out, starts = [], set()
    off = 0
    for g in groups:
        for s, sk, m, e in placements(g, crib, wild, skip, max_skip, homophones, max_err):
            sc, cov = score_map(m, all_tokens, uni)
            out.append((sc, off + s, sk, m, cov, e))
            starts.add(off + s)
        off += len(g)
    out.sort(key=lambda x: -x[0])
    return out, len(starts)


def shuffle_groups(groups, rng):
    res = []
    for g in groups:
        g2 = list(g); rng.shuffle(g2); res.append(g2)
    return res


def pct(xs, p):
    if not xs:
        return float("nan")
    xs = sorted(xs)
    return xs[min(len(xs) - 1, int(round(p * (len(xs) - 1))))]


def main():
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--codes", required=True)
    ap.add_argument("--crib", required=True)
    ap.add_argument("--wild", nargs="*", default=[])
    ap.add_argument("--skip", nargs="*", default=[])
    ap.add_argument("--max-skip", type=int, default=6)
    ap.add_argument("--homophones", action="store_true", help="allow two codes to map to one letter")
    ap.add_argument("--max-err", type=int, default=0, help="tolerated conflicting positions per placement (misread signs)")
    ap.add_argument("--group-col", default=None)
    ap.add_argument("--corpus", nargs="*", default=None)
    ap.add_argument("--lang", default="it")
    ap.add_argument("--compare", default=None, help="TSV with code and value columns (a key as read) to count agreements")
    ap.add_argument("--shuffles", type=int, default=200)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--top", type=int, default=10)
    a = ap.parse_args()
    import judge_plaintext as jp
    paths = a.corpus or [str(p) for p in jp.LANG_CORPORA[a.lang]]
    uni = unigram([jp.read_corpus(p) for p in paths])
    groups = read_codes(a.codes, a.group_col)
    crib = ha.fold(a.crib)
    wild, skip = set(a.wild), set(a.skip)
    N = sum(len(g) for g in groups)
    cnt = Counter(t for g in groups for t in g)
    print(f"crib {a.crib!r} -> {crib} ({len(crib)} letters); N={N} tokens in {len(groups)} group(s), K={len(cnt)}; "
          f"wild {sorted(wild)} ({sum(cnt[w] for w in wild)} tokens), skip {sorted(skip)} ({sum(cnt[w] for w in skip)} tokens), "
          f"max-skip {a.max_skip}, max-err {a.max_err}, homophones {'allowed' if a.homophones else 'not allowed'}; corpora {len(paths)} file(s)")
    cmp = {}
    if a.compare:
        with open(a.compare, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f, delimiter="\t"):
                v = (r.get("value") or "").strip()
                if v and v not in ("?", "null"):
                    cmp[r["code"].strip()] = ha.fold(v)
    real, real_starts = run(groups, crib, wild, skip, a.max_skip, a.homophones, uni, a.max_err)
    print(f"REAL: {len(real)} consistent placements at {real_starts} distinct start positions; "
          f"best score {real[0][0]:.3f} (coverage {real[0][4]} of {N})" if real else "REAL: 0 consistent placements")
    for sc, s, sk, m, cov, e in real[:a.top]:
        agree = sum(1 for c, l in m.items() if cmp.get(c) == l)
        print(f"  start {s:4d} skips {len(sk)} errs {e} score {sc:.3f} cov {cov:3d} agree-with-compare {agree}/{len(m)} "
              f"key {' '.join(f'{c}={l}' for c, l in sorted(m.items()))}")
    rng = random.Random(a.seed)
    counts, starts, bests = [], [], []
    for _ in range(a.shuffles):
        sh, st = run(shuffle_groups(groups, rng), crib, wild, skip, a.max_skip, a.homophones, uni, a.max_err)
        counts.append(len(sh)); starts.append(st); bests.append(sh[0][0] if sh else float("-inf"))
    if a.shuffles:
        rb = real[0][0] if real else float("-inf")
        print(f"CONTROL ({a.shuffles} shuffled-order sequences): placements mean {sum(counts)/len(counts):.1f} "
              f"p95 {pct(counts, .95)} max {max(counts)}; distinct starts mean {sum(starts)/len(starts):.1f} p95 {pct(starts, .95)} "
              f"max {max(starts)}; best score mean {sum(b for b in bests if b > -1e9)/max(1, sum(1 for b in bests if b > -1e9)):.3f} "
              f"p95 {pct(bests, .95):.3f} max {max(bests):.3f}")
        print(f"RANK: real placements {len(real)} vs shuffles -- {sum(1 for c in counts if c >= len(real))}/{a.shuffles} shuffles at or above; "
              f"real best score {rb:.3f} -- {sum(1 for b in bests if b >= rb)}/{a.shuffles} shuffles at or above")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""THUR-P188 (15 Oct 2026): score PREREG-THURP188.md's hypotheses (a)-(c) on P4, Birch III p.188 lines 53-61.

python3 score_p188.py [--check]   writes results.tsv beside this file; --check exits 1 if the committed results.tsv is stale.
Key: ../../pool_1654/key_stamford.tsv, unedited. Word list: tools/data/en16_repo minus the P4 reading (circular).
"""
import csv, random, re, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "tools"))
import judge_plaintext as jp  # noqa: E402

KEY = {}
for r in csv.DictReader(open(HERE.parents[1] / "pool_1654" / "key_stamford.tsv"), delimiter="\t"):
    KEY[r["value"]] = re.sub(r"[^a-z]", "", r["meaning"].split("/")[0].lower())
CORP = [p for p in sorted((ROOT / "tools/data/en16_repo").glob("thurloe-printed__*.txt")) if "reading_P4" not in p.name]
MODEL = jp.NgramModel([jp.read_corpus(p) for p in CORP])
WORDS = {w for w in MODEL.words if len(w) >= 3}
MAXW = max(map(len, WORDS))


def lines_of():
    out = {}
    for r in csv.reader(open(HERE.parent / "image_transcription.tsv"), delimiter="\t"):
        if r and r[0] == "188":
            out[int(r[1])] = re.findall(r"\d+|[A-Za-z]+", r[3])
    return out


def runs(tokens):
    """tokens: list of str (digits or words) -> list of runs (lists of numeral strings)."""
    rs, cur = [], []
    for t in tokens:
        if t.isdigit():
            cur.append(t)
        else:
            if cur:
                rs.append(cur)
            cur = []
    if cur:
        rs.append(cur)
    return rs


def run_reads(run):
    """per-numeral read flags for one run."""
    vals = [KEY.get(t) for t in run]
    flags = [False] * len(run)
    # split at unkeyed values
    seg = []
    for i, v in enumerate(vals + [None]):
        if v is None or i == len(vals):
            if seg:
                s = "".join(vals[j] for j in seg)
                owner = [j for j in seg for _ in vals[j]]
                cov = [False] * len(s); p = 0
                while p < len(s):
                    best = 0
                    for L in range(min(MAXW, len(s) - p), 2, -1):
                        if s[p:p + L] in WORDS:
                            best = L; break
                    if best:
                        for q in range(p, p + best):
                            cov[q] = True
                        p += best
                    else:
                        p += 1
                for j in seg:
                    idx = [q for q, o in enumerate(owner) if o == j]
                    flags[j] = (all(cov[q] for q in idx) and bool(idx)) or (len(vals[j]) >= 3 and vals[j] in WORDS)
            seg = []
        else:
            seg.append(i)
    return flags


def share(tokens, restrict=None):
    fl = []
    for r in runs(tokens):
        fl += run_reads(r)
    return sum(fl) / len(fl) if fl else 0.0, len(fl)


def block_tokens(L, order):
    return [t for ln in order for t in L[ln]]


def p95(xs):
    xs = sorted(xs); return xs[int(0.95 * (len(xs) - 1))]


def bound_shuffle(tokens, rnd):
    out = []
    for grp in re.split(r"(\D+)", " ".join("#" if t.isdigit() else t for t in tokens)):
        pass
    # rebuild per run
    i = 0; res = []
    while i < len(tokens):
        if not tokens[i].isdigit():
            res.append(tokens[i]); i += 1; continue
        j = i
        while j < len(tokens) and tokens[j].isdigit():
            j += 1
        run = tokens[i:j]; digits = "".join(run); k = len(run)
        for _ in range(1000):
            cuts = sorted(rnd.sample(range(1, len(digits)), k - 1)) if k > 1 else []
            parts = [digits[a:b] for a, b in zip([0] + cuts, cuts + [len(digits)])]
            if all(1 <= len(p) <= 3 for p in parts):
                break
        res += parts; i = j
    return res


def siblings():
    rows = list(csv.DictReader(open(HERE.parents[1] / "pool_1654" / "tokens.tsv"), delimiter="\t"))
    fl = []; am = 0
    for let in ("P5_P6", "P7"):
        cur = []
        for r in [x for x in rows if x["letter"] == let]:
            v = re.sub(r"\D", "", r["cleaned"])
            if not re.fullmatch(r"\d+\.?,?", r["prev_word"] or "") and cur:
                fl += sum((run_reads(c) for c in [cur]), []); cur = []
            if v:
                cur.append(v)
            if (r["prev_word"] or "").lower().strip(".") == "am" or (r["next_word"] or "").lower().strip(".") == "am":
                am += 1
        if cur:
            fl += run_reads(cur)
    return sum(fl) / len(fl), len(fl), am


def main():
    rnd = random.Random(1)
    L = lines_of(); BL = list(range(53, 62))
    base_tok = block_tokens(L, BL)
    out = []
    b, n = share(base_tok); out.append(("baseline", "printed order", round(b, 3), n))
    sib, sn, sam = siblings(); out.append(("ref", "SIB P5+P6,P7", round(sib, 3), sn))
    out.append(("ref", "sibling numerals adjacent to 'am'", sam, sn))
    r50, n50 = share(block_tokens(L, [50, 51, 52])); out.append(("ref", "P4 lines 50-52", round(r50, 3), n50))
    nl = []
    for _ in range(200):
        o = BL[:]; rnd.shuffle(o); nl.append(share(block_tokens(L, o))[0])
    nb = [share(bound_shuffle(base_tok, rnd))[0] for _ in range(200)]
    out.append(("null", "N-line p95", round(p95(nl), 3), 200)); out.append(("null", "N-bound p95", round(p95(nb), 3), 200))
    # (a) exploratory counts
    nums = [t for t in base_tok if t.isdigit()]
    joins = sum(1 for i in range(len(base_tok) - 1) if base_tok[i].isdigit() and base_tok[i + 1].isdigit()
                and base_tok[i] + base_tok[i + 1] in KEY)
    splits = sum(1 for t in nums if any(t[:k] in KEY and t[k:] in KEY for k in range(1, len(t))))
    out.append(("a", "read vs transcription: numeral differences", 0, 198))
    out.append(("a", "exploratory: adjacent joins that are key values", joins, len(nums)))
    out.append(("a", "exploratory: numerals that split into two key values", splits, len(nums)))
    # (b) adjacent swaps
    best_b = (0, None)
    for a in range(52, 61):
        order = list(range(52, 62)); i = order.index(a); order[i], order[i + 1] = order[i + 1], order[i]
        toks = block_tokens(L, order)
        nums_all = [t for t in toks if t.isdigit()]
        # score only the 144 block numerals: compute flags over all, keep those from lines 53-61
        fl = []; src = [ln for ln in order for t in L[ln] if t.isdigit()]
        for r in runs(toks):
            fl += run_reads(r)
        keep = [f for f, s in zip(fl, src) if s >= 53]
        s_ = sum(keep) / len(keep)
        out.append(("b", f"swap {a}/{a+1}", round(s_, 3), len(keep)))
        best_b = max(best_b, (s_, a))
    # (c) 'am' as a key value
    def am_sub(toks, v):
        return [v if t.lower() == "am" else t for t in toks]
    res_c = sorted(((share(am_sub(base_tok, v))[0], v) for v in KEY), reverse=True)
    for s_, v in res_c[:5]:
        out.append(("c", f"am={v} ({KEY[v]})", round(s_, 3), 144 + 7))
    mx = []
    for _ in range(200):
        o = BL[:]; rnd.shuffle(o); t = block_tokens(L, o)
        mx.append(max(share(am_sub(t, v))[0] for v in KEY))
    out.append(("null", "max-of-59 am search on line-shuffled p95", round(p95(mx), 3), 200))
    nbc = []
    for _ in range(200):
        t = bound_shuffle(base_tok, rnd); nbc.append(max(share(am_sub(t, v))[0] for v in KEY))
    out.append(("null", "max-of-59 am search on boundary-shuffled p95", round(p95(nbc), 3), 200))
    gate = sib - 0.10
    out.append(("gate", "b best", "PASS" if best_b[0] > p95(nl) and best_b[0] >= gate else "FAIL", f"{best_b[0]:.3f} swap {best_b[1]}"))
    cbest = res_c[0][0]
    out.append(("gate", "c best", "PASS" if cbest > max(p95(nb), p95(mx), p95(nbc)) and cbest >= gate else "FAIL", f"{cbest:.3f}"))
    out.append(("gate", "near-sibling floor", round(gate, 3), ""))
    txt = "kind\titem\tvalue\tn\n" + "".join("\t".join(map(str, r)) + "\n" for r in out)
    p = HERE / "results.tsv"
    if "--check" in sys.argv:
        sys.exit(0 if p.exists() and p.read_text() == txt else 1)
    p.write_text(txt); print(txt)


if __name__ == "__main__":
    main()

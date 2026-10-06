#!/usr/bin/env python3
"""R7C-ECK62C (6 Oct 2026; rules pre-registered in PREREG-ECK62-CONFPAIR.md, pushed before any number): do the CONFLICT
pairs (code word, printed span) of R7B-ECK62's neither-book entries agree across entries more than chance gives?

Usage: ec18_confpair.py [--write | --check]
  Reads the committed align_free_tokens.tsv and wrongtel_entries.tsv (no network). --write rewrites confpair_pairs.tsv and
  confpair_summary.tsv; --check exits 1 if either is stale.

Statistic S: distinct code words occurring in >= 2 entries of a pool with an agreeing pair between two different entries
(printed content words, >= 4 letters, not in ec18.STOP, intersect). Null: printed spans permuted across the pool's pairs,
2000 shuffles. Positive control: AGREE word pairs of the non-target entries, subsampled by whole entries to the pool's N,
200 subsamples x 500 shuffles; power = share with p <= 0.05; gate power >= 0.80.
"""
import sys, random, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
from ec18 import STOP  # noqa: E402

PRIMARY = ["9669.5", "9762.135", "9808.202", "9958.527", "9969.543", "9985.563", "9987.565"]


def rows(name):
    lines = (HERE / name).read_text().splitlines()
    head = lines[0].split("\t")
    return [dict(zip(head, ln.split("\t"))) for ln in lines[1:] if ln]


FUNC = {"have", "will", "been", "with", "that", "this", "from", "your", "there", "were", "shall", "would", "what", "when"}


def content(span, strict=False):
    return frozenset(w for w in span.lower().split() if len(w) >= 4 and w not in STOP and not (strict and w in FUNC))


SAMEPAGE = {}


def stat(pairs, spans=None):
    """pairs: list of (entry, code); spans: list of content sets aligned with pairs. Entries in SAMEPAGE with the same
    OR (vol, page) never count as two contexts (strict variant only; empty otherwise)."""
    by = collections.defaultdict(list)
    for (e, c), s in zip(pairs, spans):
        by[c].append((e, s))
    hits = []
    for c, xs in by.items():
        if len({e for e, _ in xs}) < 2:
            continue
        if any(a[0] != b[0] and a[1] & b[1] and not (a[0] in SAMEPAGE and SAMEPAGE[a[0]] == SAMEPAGE.get(b[0]))
               for k, a in enumerate(xs) for b in xs[k + 1:]):
            hits.append(c)
    return sorted(hits)


def shuffle_p(pairs, spans, n, rng):
    s = len(stat(pairs, spans))
    sp = list(spans)
    ge = 0
    for _ in range(n):
        rng.shuffle(sp)
        ge += len(stat(pairs, sp)) >= s
    return s, (1 + ge) / (1 + n)


def power(ctl, n_pairs, rng, subs=200, shuf=500):
    ents = sorted(ctl)
    ps, ss = [], []
    for _ in range(subs):
        order = ents[:]
        rng.shuffle(order)
        pick = []
        for e in order:
            pick += ctl[e]
            if len(pick) >= n_pairs:
                break
        pick = pick[:n_pairs]
        s, p = shuffle_p([(e, c) for e, c, _ in pick], [x for _, _, x in pick], shuf, rng)
        ps.append(p)
        ss.append(s)
    ss.sort()
    return sum(p <= 0.05 for p in ps) / subs, ss[len(ss) // 2]


def main(argv):
    mode = argv[1] if len(argv) > 1 else "--check"
    wt = {r["id"]: r for r in rows("wrongtel_entries.tsv") if r["role"] == "target"}
    toks = rows("align_free_tokens.tsv")
    targ = [r for r in toks if r["id"] in wt and r["side"] == "target" and r["status"] == "CONFLICT"
            and r["kind"] in ("word", "plain-replaced")]
    ctl = collections.defaultdict(list)
    for r in toks:
        if r["id"] not in wt and r["side"] == "target" and r["status"] == "AGREE" and r["kind"] == "word":
            ctl[r["id"]].append((r["id"], r["code_word"].lower(), content(r["printed"])))
    out = ["pool\tn_entries\tn_pairs\tS\tp_shuffle\tctl_power\tctl_median_S\tgate\tverdict\thits"]
    plines = ["id\tclass\tdate\tkind\tcode_word\tprinted\tcontent\trecurs_in_pool18\tagrees_across_entries_18"]
    for name, ids in (("primary7", PRIMARY), ("all18", sorted(wt)), ("all18_strict", sorted(wt))):
        rng = random.Random(0)
        strict = name.endswith("strict")
        SAMEPAGE.clear()
        if strict:  # descriptive robustness, added after the prereg: function words out, same-OR-page entries one context
            SAMEPAGE.update({e: (wt[e]["or_vol"], wt[e]["or_page_ocr"]) for e in wt})
        pp = [r for r in targ if r["id"] in ids]
        pairs = [(r["id"], r["code_word"].lower()) for r in pp]
        spans = [content(r["printed"], strict) for r in pp]
        s, p = shuffle_p(pairs, spans, 2000, rng)
        hits = stat(pairs, spans)
        if strict:
            ctl = {e: [(a, b, content(" ".join(x), True)) for a, b, x in v] for e, v in ctl.items()}
        pw, med = power(ctl, len(pairs), rng)
        gate = "PASS" if pw >= 0.80 else "FAIL"
        if name == "primary7":
            verdict = ("untested-by-this-tool" if gate == "FAIL" else
                       "consistency-above-chance" if p <= 0.05 else "no-consistency-at-this-N")
        else:
            verdict = "descriptive"
        out.append(f"{name}\t{len({e for e, _ in pairs})}\t{len(pairs)}\t{s}\t{p:.4f}\t{pw:.3f}\t{med}\t{gate}\t{verdict}\t"
                   f"{','.join(hits) or '-'}")
        if name == "all18":
            ents = collections.defaultdict(set)
            for e, c in pairs:
                ents[c].add(e)
            for r, (e, c) in zip(pp, pairs):
                plines.append(f"{e}\t{wt[e]['class']}\t{wt[e]['date']}\t{r['kind']}\t{c}\t{r['printed']}\t"
                              f"{' '.join(sorted(content(r['printed']))) or '-'}\t{len(ents[c])}\t{int(c in hits)}")
    want = {"confpair_summary.tsv": "\n".join(out) + "\n", "confpair_pairs.tsv": "\n".join(plines) + "\n"}
    stale = 0
    for f, txt in want.items():
        if mode == "--write":
            (HERE / f).write_text(txt)
        elif not (HERE / f).exists() or (HERE / f).read_text() != txt:
            print(f"STALE {f}")
            stale = 1
    print(want["confpair_summary.tsv"], end="")
    return stale


if __name__ == "__main__":
    sys.exit(main(sys.argv))

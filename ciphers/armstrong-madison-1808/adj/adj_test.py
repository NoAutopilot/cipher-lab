#!/usr/bin/env python3
"""ARM3-ADJ (26 Sept 2026, LANE ARM3, Sonnet): family S2, run-adjacency structural test.

Hypothesis: the shorthand runs ('*' marks in ciphertext_ms.txt) spell out proper names and
other words not in the code; if so, the numeric groups immediately adjacent to a run (position
-1 = last numeric group before the run, +1 = first numeric group after it) should behave like a
closed set (titles, prepositions, articles), i.e. fewer distinct values, more share in the 1-99
particle block, and more mass on the letter's own top-10 particle values than groups elsewhere.

Statistic (fixed before looking at the target), for -1 and +1 separately:
  (i)   share of values in 1-99
  (ii)  distinct-value ratio (distinct / count)
  (iii) share covered by the target's own top-10 particle (1-99) values

CONTROLS (CLAUDE.md rule 3 -- each can differ from the target on the exact manipulation tested):
  - shuffled-position null: same run COUNT and LENGTH list, placed at 1,000 random gap positions
    among the target's own 369 numeric groups. This moves WHICH groups are adjacent to a run,
    which is exactly what the statistic reads (unlike a shuffled-VALUE or shuffled-ORDER control,
    which would not change adjacency membership at all -- see CLAUDE.md's bCAS/AX-5799 lesson).
  - positive control: en18 prose windows encoded under ARM-DESIGN's seq_pblock design (particle
    block 1-99 + 1800 random-numbered content words, OOV dropped), with every proper noun
    (capitalised, non-sentence-initial word) replaced by a pseudo-run instead of encoded, scored
    against ITS OWN shuffled-position null the same way. If the positive control does not
    separate from its own null, the method has no resolving power and a target number is a
    non-test (per this job's brief).

Offline, stdlib only.  python3 adj_test.py [--trials 1000] [--seed 1] [--pos-tokens 4000]
"""
import argparse, gzip, random, re, sys
from collections import Counter
from pathlib import Path

HERE = Path(__file__).resolve().parent
TARGET_DIR = HERE.parent
REPO = HERE.parents[2]
MS = TARGET_DIR / "ciphertext_ms.txt"
EN18 = REPO / "tools/data/en18"

NUM_RE = re.compile(r"^(\d+)[\^\?]?$")


# ---------------- target parsing ----------------
def parse_ms(path):
    """Return (numeric_seq, runs) where numeric_seq is the ordered list of int values of every
    numeric group in the letter (ignoring '^'/'?' suffixes -- the flag, not the value), and runs
    is a list of (gap_index, length): gap_index g means the run sits between numeric_seq[g-1]
    and numeric_seq[g] (0 <= g <= N); length is its mark count."""
    numeric_seq = []
    runs = []
    run_len = 0
    for line in open(path, encoding="utf-8"):
        line = line.rstrip("\n")
        if line.startswith("#") or not line.strip():
            continue
        for tok in line.split():
            if tok == "*":
                run_len += 1
                continue
            m = NUM_RE.match(tok)
            if m:
                if run_len:
                    runs.append((len(numeric_seq), run_len))
                    run_len = 0
                numeric_seq.append(int(m.group(1)))
            else:
                # a plain word (e.g. the salutation "Sir", the clear opening "The") -- not part
                # of the numeric/run structure; if it interrupts a run, close the run out (none
                # observed to do so in this letter, checked below).
                if run_len:
                    runs.append((len(numeric_seq), run_len))
                    run_len = 0
    if run_len:
        runs.append((len(numeric_seq), run_len))
    return numeric_seq, runs


def flank_lists(numeric_seq, runs):
    """-1 and +1 flanking values for every run that has a numeric group on that side (edge runs
    at the absolute start/end of the letter, if any, are dropped from that side's list)."""
    N = len(numeric_seq)
    minus1, plus1, dropped_edge = [], [], 0
    for g, length in runs:
        if g - 1 >= 0:
            minus1.append(numeric_seq[g - 1])
        else:
            dropped_edge += 1
        if g < N:
            plus1.append(numeric_seq[g])
        else:
            dropped_edge += 1
    return minus1, plus1, dropped_edge


def stat3(vals, top10set):
    n = len(vals)
    if n == 0:
        return {"share_1_99": float("nan"), "distinct_ratio": float("nan"), "top10_share": float("nan"), "n": 0}
    share = sum(1 for v in vals if 1 <= v <= 99) / n
    distinct = len(set(vals)) / n
    top10 = sum(1 for v in vals if v in top10set) / n
    return {"share_1_99": share, "distinct_ratio": distinct, "top10_share": top10, "n": n}


def shuffled_null(numeric_seq, runs, top10set, trials, rng):
    """1,000 draws: same run count and length list, placed at random DISTINCT gap positions
    among the same numeric sequence (length is carried through for fidelity to the real
    placement process even though the -1/+1 identity depends only on which gap is chosen, not on
    how many marks fill it)."""
    N = len(numeric_seq)
    R = len(runs)
    lengths = [l for _, l in runs]
    out = {"-1": {"share_1_99": [], "distinct_ratio": [], "top10_share": []},
           "+1": {"share_1_99": [], "distinct_ratio": [], "top10_share": []}}
    valid_gaps = list(range(1, N))  # g in 1..N-1 always has both a -1 and a +1 numeric neighbour
    for _ in range(trials):
        gaps = rng.sample(valid_gaps, R) if R <= len(valid_gaps) else valid_gaps
        rng.shuffle(lengths)  # length is carried along per draw; irrelevant to the statistic itself
        m1 = [numeric_seq[g - 1] for g in gaps]
        p1 = [numeric_seq[g] for g in gaps]
        for label, vals in (("-1", m1), ("+1", p1)):
            s = stat3(vals, top10set)
            out[label]["share_1_99"].append(s["share_1_99"])
            out[label]["distinct_ratio"].append(s["distinct_ratio"])
            out[label]["top10_share"].append(s["top10_share"])
    return out


def summarize_null(null, real):
    """mean, p05, p95, and the real (target or positive-control) value's percentile within the
    null. share_1_99 and top10_share read high (p95) for a closed set; distinct_ratio reads LOW
    (p05) for a closed set (fewer distinct values) -- both tails are reported, the relevant one
    named in the write-up rather than assumed."""
    rows = {}
    for label in ("-1", "+1"):
        rows[label] = {}
        for k in ("share_1_99", "distinct_ratio", "top10_share"):
            xs = sorted(null[label][k])
            mu = sum(xs) / len(xs)
            p05 = xs[min(len(xs) - 1, int(0.05 * len(xs)))]
            p95 = xs[min(len(xs) - 1, int(0.95 * len(xs)))]
            tv = real[label][k]
            pct = 100 * sum(1 for x in xs if x < tv) / len(xs) + 50 * sum(1 for x in xs if x == tv) / len(xs)
            rows[label][k] = {"mean": mu, "p05": p05, "p95": p95, "target": tv, "pct": pct}
    return rows


# ---------------- positive control: en18 + seq_pblock + proper-noun runs ----------------
SENT_END = re.compile(r'[.!?]["\')\]]*\s*$')
WORD_RE = re.compile(r"[A-Za-z']+")


def en18_word_stream():
    """Ordered (raw_word, is_sentence_initial) pairs across the whole en18 corpus, corpus by
    corpus (front/back 10% trimmed as design_stats.py does), sentence-initial flagged so a
    capitalised word right after a full stop is NOT treated as a proper noun."""
    stream = []
    for p in sorted(EN18.glob("*.txt.gz")):
        t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read()
        n = len(t)
        t = t[int(n * 0.1):int(n * 0.9)]
        sent_initial = True
        pos = 0
        for m in WORD_RE.finditer(t):
            w = m.group(0)
            stream.append((w, sent_initial))
            tail = t[m.end():m.end() + 3]
            sent_initial = bool(SENT_END.match(t[max(0, m.end() - 3):m.end() + 1])) or bool(re.match(r"^\s*[.!?]", tail))
            pos = m.end()
    return stream


def build_vocab(stream):
    allw = Counter(w.lower() for w, _ in stream if w.isalpha())
    particles_list = [w for w, _ in allw.most_common(400)][:99]
    particle_val = {w: i + 1 for i, w in enumerate(particles_list)}
    stopset = set(particles_list)
    contentc = Counter(w.lower() for w, si in stream if w.isalpha() and w.lower() not in stopset
                        and len(w) > 2 and not (w[0].isupper() and not si))
    content_words = [w for w, _ in contentc.most_common(1800)]
    return particle_val, stopset, content_words


def encode_positive_control(stream, particle_val, stopset, content_words, target_numeric, rng):
    """Walk the corpus once; a proper noun (capitalised, alpha, NOT sentence-initial, not itself
    a common particle) becomes a pseudo-run (length drawn from the target's own real run-length
    list, so the two controls are on the same footing); a particle -> its 1-99 value; a content
    word -> a random-but-fixed 100..1899 slot (seq_pblock: values shuffled once, independent of
    English order, per ARM-DESIGN); anything else is OOV and dropped, matching how the design
    treats the letter's own shorthand passages as an out-of-vocabulary route."""
    vv = list(range(100, 100 + len(content_words)))
    rng.shuffle(vv)
    content_val = dict(zip(content_words, vv))
    lengths = target_numeric[:] if target_numeric else [1]

    numeric_seq, runs = [], []
    run_len = 0
    for w, si in stream:
        if not w.isalpha():
            continue
        lw = w.lower()
        is_proper = w[0].isupper() and not si and lw not in stopset and lw not in content_val
        if is_proper:
            if run_len == 0:
                run_len = rng.choice(lengths)
            continue  # still "inside" a run of the sampled length; consumed below
        if run_len:
            runs.append((len(numeric_seq), run_len))
            run_len = 0
        if lw in particle_val:
            numeric_seq.append(particle_val[lw])
        elif lw in content_val:
            numeric_seq.append(content_val[lw])
        # else: OOV, dropped (no token emitted, no run either -- matches the design's silent drop)
    if run_len:
        runs.append((len(numeric_seq), run_len))
    return numeric_seq, runs


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--trials", type=int, default=1000)
    ap.add_argument("--seed", type=int, default=1)
    a = ap.parse_args()
    rng = random.Random(a.seed)

    numeric_seq, runs = parse_ms(MS)
    print(f"TARGET: {len(numeric_seq)} numeric groups, {len(runs)} runs, "
          f"run lengths {sorted(l for _, l in runs)}")
    top10 = [v for v, _ in Counter(v for v in numeric_seq if 1 <= v <= 99).most_common(10)]
    top10set = set(top10)
    print(f"top-10 particle values (by count, 1-99 block): {top10}")

    m1, p1, dropped = flank_lists(numeric_seq, runs)
    assert dropped == 0, f"{dropped} edge runs with no numeric flank on one side -- brief assumed none"
    real = {"-1": stat3(m1, top10set), "+1": stat3(p1, top10set)}
    print("TARGET -1:", real["-1"])
    print("TARGET +1:", real["+1"])
    print("TARGET -1 value counts:", Counter(m1).most_common())
    print("TARGET +1 value counts:", Counter(p1).most_common())

    null = shuffled_null(numeric_seq, runs, top10set, a.trials, random.Random(a.seed + 1))
    summ = summarize_null(null, real)
    print("\nSHUFFLED-POSITION NULL (target's own runs, gap-shuffled):")
    for label in ("-1", "+1"):
        for k in ("share_1_99", "distinct_ratio", "top10_share"):
            r = summ[label][k]
            print(f"  {label} {k}: target={r['target']:.3f} null_mean={r['mean']:.3f} "
                  f"null_p05={r['p05']:.3f} null_p95={r['p95']:.3f} pct={r['pct']:.0f}")

    # --- positive control ---
    stream = en18_word_stream()
    particle_val, stopset, content_words = build_vocab(stream)
    pc_seq, pc_runs = encode_positive_control(stream, particle_val, stopset, content_words,
                                               [l for _, l in runs], random.Random(a.seed + 2))
    print(f"\nPOSITIVE CONTROL: {len(pc_seq)} numeric groups, {len(pc_runs)} proper-noun runs")
    pc_top10 = [v for v, _ in Counter(v for v in pc_seq if 1 <= v <= 99).most_common(10)]
    pc_top10set = set(pc_top10)
    pc_m1, pc_p1, pc_dropped = flank_lists(pc_seq, pc_runs)
    pc_real = {"-1": stat3(pc_m1, pc_top10set), "+1": stat3(pc_p1, pc_top10set)}
    print(f"POSITIVE CONTROL edge runs dropped from a side: {pc_dropped}")
    print("POSITIVE CONTROL -1:", pc_real["-1"])
    print("POSITIVE CONTROL +1:", pc_real["+1"])

    pc_null = shuffled_null(pc_seq, pc_runs, pc_top10set, a.trials, random.Random(a.seed + 3))
    pc_summ = summarize_null(pc_null, pc_real)
    print("\nPOSITIVE CONTROL vs its OWN shuffled-position null:")
    for label in ("-1", "+1"):
        for k in ("share_1_99", "distinct_ratio", "top10_share"):
            r = pc_summ[label][k]
            print(f"  {label} {k}: real={r['target']:.3f} null_mean={r['mean']:.3f} "
                  f"null_p05={r['p05']:.3f} null_p95={r['p95']:.3f} pct={r['pct']:.0f}")

    out = {
        "target": {"numeric_n": len(numeric_seq), "runs": len(runs), "top10": top10,
                    "real": real, "null_summary": summ},
        "positive_control": {"numeric_n": len(pc_seq), "runs": len(pc_runs),
                              "real": pc_real, "null_summary": pc_summ},
    }
    import json
    (HERE / "run_log.json").write_text(json.dumps(out, indent=1))
    print("\nwrote", HERE / "run_log.json")


if __name__ == "__main__":
    main()

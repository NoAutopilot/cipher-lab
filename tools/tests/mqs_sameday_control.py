#!/usr/bin/env python3
"""MQS-SAMEDAY known-answer control (tools/tests/PREREG-MQS-SAMEDAY.md, pushed before this ran).

Offline: reads Martin's Wellesley Despatches Vols 1-2 OCR already on disk (ciphers/mornington-1798/print/), clear print
only. Prints gate A (dating: true date in the top 10% of candidate dates) and gate B (crib precision), each against 20
date shuffles.  python3 tools/tests/mqs_sameday_control.py
"""
import os
import random
import statistics
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import sameday as sd  # noqa: E402

VOLS = [("v1 ", "35304"), ("v2 ", "35315")]
SENDER = "Mornington to|Wellesley to"


def corpus():
    rows = []
    for pre, v in VOLS:
        text = open(os.path.join(ROOT, "ciphers/mornington-1798/print", v + "_djvu.txt"), encoding="utf-8",
                    errors="replace").read()
        rows += sd.parse_edition(text, SENDER, 120, pre)
    for r in rows:
        r["d"] = sd.date.fromisoformat(r["date"])
        r["toks"] = sd.tokens(r["text"])
    return rows


def run(letters, items, dates, idx):
    """Return (share of items in the top 10%, crib hits, crib proposals) under the given date list."""
    top, hits, props = 0, 0, 0
    for k, (i, rtoks, hidden) in enumerate(items):
        rgrams = {g for g, _ in sd.trigrams(rtoks)}
        ex = {i}
        cands = sorted({x for j, x in enumerate(dates) if j != i} | {letters[i]["d"]})
        scores = sd.date_ranks(idx, rgrams, dates, 7, ex, cands)
        if sd.avg_rank(scores, letters[i]["d"]) <= 0.10 * len(cands):
            top += 1
        ids = sd.window_ids(dates, letters[i]["d"], 7, ex)
        for j, w, g, src in sd.cribs(idx, rtoks, ids):
            props += 1
            hits += (w == hidden[j])
    return top / len(items), hits, props


def main():
    letters = corpus()
    idx = sd.Index(letters)
    dates = [L["d"] for L in letters]
    elig = [i for i in range(len(letters)) if sd.window_ids(dates, dates[i], 7, {i})]
    rng = random.Random(0)
    chosen = sorted(rng.sample(elig, min(60, len(elig))))
    items = []
    for n, i in enumerate(chosen):
        full = letters[i]["toks"][:300]
        r = random.Random(1000 + n)
        items.append((i, [w if r.random() < 0.5 else None for w in full], full))
    print(f"corpus {len(letters)} sender letters, {dates and min(dates)}..{max(dates)}; eligible {len(elig)}; items {len(items)}")
    a, h, p = run(letters, items, dates, idx)
    b = h / p if p else 0.0
    print(f"REAL  A top10% {a:.3f}   B precision {b:.3f} ({h}/{p})")
    na, nb = [], []
    for s in range(1, 21):
        sh = dates[:]
        random.Random(s).shuffle(sh)
        x, hh, pp = run(letters, items, sh, idx)
        na.append(x)
        nb.append(hh / pp if pp else 0.0)
    p95 = lambda v: sorted(v)[int(0.95 * (len(v) - 1))]  # noqa: E731
    print(f"NULL  A mean {statistics.mean(na):.3f} p95 {p95(na):.3f}   B mean {statistics.mean(nb):.3f} p95 {p95(nb):.3f}")
    ga = a >= 0.30 and a > p95(na)
    gb = b >= 0.30 and b > p95(nb) and p >= 30 and p95(nb) < 0.95
    print(f"GATE A {'PASS' if ga else 'FAIL'}   GATE B {'PASS' if gb else 'FAIL'}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

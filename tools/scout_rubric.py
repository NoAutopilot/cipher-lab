#!/usr/bin/env python3
"""scout_rubric.py -- the one scout scoring formula (MQS-SCOUT, 9 Oct 2026; LANE MQS, matrix row M29).

Why: the Mary Stuart talk's lesson on why nobody read the Castelnau letters is "not enough incentive" and "no way to
know that they are from Mary" (talk [00:08:49]-[00:09:40]; paper p.102 n.6). The old scout rubric repeated that:
`language_fit` 0 = "unknown language" and `weight` = "historical interest of the content" both need a name, so an
unnamed, undated, all-cipher pile scored low on every axis. Here an unattributed pile is scored as a pile.

FORMULA (shared with .claude/workflows/scout.js; tests fail if they differ):
    language_fit*3 + material*4 + key_lead*3 + size*2 + competition*2 + weight + unread*3 + pile*2     (max 60)
Tiers are unchanged (A >= 38, B 28-37, C < 28), so an existing row's total and tier do not move (pile absent = 0).

THE WEIGHTS ARE A DECLARED PRIOR, NOT FITTED. The `pending` score, the holder/era weight prior and the x2 pile weight are
chosen by argument (CLAUDE.md pipeline 3, "pools first"), and the one fr.2988-shaped test row cannot fit them; the
held-out shape (fr.20506) was scored after they were fixed.

Changes from scout.js's old rubric, each with its reason:
 * language_fit may be `pending` (scored 2, not 0) for an all-cipher item from a holder whose era's languages are among
   those we read and whose language is unknown (the language is what a trial decipherment would tell us). 0 stays for an
   unknown script with no holder context. `pending` without holder context is scored 0.
 * weight unknown (None / "unknown") takes a holder/era prior instead of 0: 2 for a diplomatic series of a state archive
   or national library, 1 otherwise. Reason: weight is "interest of the content", which an unread pile cannot state.
 * a `pile` axis 0-3 from the estimated signs in one key: 0 under 2,000 (the pools rule's line), 1 to 10,000, 2 to 50,000,
   3 above; weighted x2. est_signs is the item's own estimate or `tools/bnf_findingaid.py --pile` (n_bare x median folio
   gap x 650, calibrated on fr.2988). Absent est_signs = 0, never a guess.
 * prior-work flags apply BEFORE the rank: a row flagged `active-edition` or `known` (prior_work.py check 3) has
   competition forced to 0 and is ranked after every unflagged row ("contact first" / "already read"). Raising
   unattributed piles must not raise solved or claimed ones.

Usage 8a scope. Meant to catch: an unattributed all-cipher pile of >= 50,000 signs ranks in the top decile (test S1); a
flagged copy of it does not (S2). Must NOT: move an existing named row's total or tier (S4), push the three top named
rows out of the top five (S3), score `pending` for an unknown script with no holder context (test), or write any file
(--rerank prints; QUEUE-scores.json and QUEUE.md are never written by this tool).

CLI:  python3 tools/scout_rubric.py --rerank QUEUE-scores.json     print ranking + rows scored under an older formula
Tests: python3 tools/tests/test_scout_rubric.py
"""
import argparse
import json
import math
import os
import re
import sys

FORMULA = "language_fit*3 + material*4 + key_lead*3 + size*2 + competition*2 + weight + unread*3 + pile*2"
AXES = ("language_fit", "material", "key_lead", "size", "competition", "weight", "unread", "pile")
TIERS = (("A", 38), ("B", 28), ("C", 0))
PENDING = 2
FLAGS = ("active-edition", "known")


def pile_axis(est_signs):
    if est_signs is None or est_signs < 2000:
        return 0
    if est_signs <= 10000:
        return 1
    return 2 if est_signs <= 50000 else 3


def est_signs_from_pile(n_bare, median_folio_gap):
    """tools/bnf_findingaid.py --pile: n_bare x median folio gap x 650 signs (calibrated on fr.2988)."""
    return int(n_bare * median_folio_gap * 650)


def weight_prior(holder_kind):
    return 2 if holder_kind in ("state-diplomatic", "national-library-diplomatic") else 1


def language_value(v, all_cipher=False, holder_era_ours=False):
    """int 0-3 passes through; 'pending' = 2 only for an all-cipher item with holder/era context, else 0."""
    if v == "pending":
        return PENDING if (all_cipher and holder_era_ours) else 0
    return int(v)


def score(row):
    """row: dict with the seven original axes (language_fit may be 'pending', weight may be None/'unknown'), optional
    est_signs / pile, all_cipher, holder_era_ours, holder_kind, flag. Returns a dict with axes resolved, total, tier."""
    r = dict(row)
    r["language_fit"] = language_value(r.get("language_fit", 0), r.get("all_cipher", False), r.get("holder_era_ours", False))
    w = r.get("weight")
    r["weight"] = weight_prior(r.get("holder_kind")) if w in (None, "unknown", "") else int(w)
    r["pile"] = int(r["pile"]) if r.get("pile") is not None else pile_axis(r.get("est_signs"))
    r.setdefault("unread", 0)
    if r.get("flag") in FLAGS:
        r["competition"] = 0
    r["total"] = (r["language_fit"] * 3 + r["material"] * 4 + r["key_lead"] * 3 + r["size"] * 2 + r["competition"] * 2
                  + r["weight"] + r["unread"] * 3 + r["pile"] * 2)
    r["tier"] = next(t for t, lo in TIERS if r["total"] >= lo)
    return r


def rank(rows):
    """Scored rows, unflagged by total descending first, then flagged ones (contact first / already read)."""
    s = [score(r) for r in rows]
    return sorted(s, key=lambda r: (r.get("flag") in FLAGS, -r["total"]))


def top_decile(n):
    return math.ceil(n / 10)


def js_formula(path):
    """The total expression of scout.js, normalised to FORMULA's spelling."""
    m = re.search(r"total:\s*(s\.language_fit[^,\n]*?),?\s*\n", open(path, encoding="utf-8").read())
    if not m:
        raise ValueError("no total: expression in " + path)
    return re.sub(r"\s*\*\s*", "*", m.group(1).replace("s.", "")).replace(" + ", " + ").strip()


def normalise(f):
    return re.sub(r"\s+", "", f)


def rerank(path):
    d = json.load(open(path, encoding="utf-8"))
    rows = [dict(r, unread=r.get("unread", 0), total_stored=r.get("total")) for r in d["scored"]]
    ranked = rank(rows)
    stale = normalise(d.get("formula", "")) != normalise(FORMULA)
    print(f"stored formula: {d.get('formula')}\ncurrent FORMULA: {FORMULA}")
    if stale:
        print(f"DRIFT: all {len(rows)} rows were scored under an older formula (stored total vs recomputed shown)")
    for i, r in enumerate(ranked, 1):
        print(f"{i:>3}\t{r['total']:>3}\t{r['tier']}\t(stored {r.get('total_stored', '')})\t{r['name'][:70]}")
    return 1 if stale else 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--rerank", metavar="QUEUE-scores.json", required=True, help="print the ranking; writes nothing")
    a = ap.parse_args(argv)
    rerank(a.rerank)
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Offline tests for tools/scout_rubric.py (MQS-SCOUT, 9 Oct 2026; PREREG tools/tests/PREREG-MQS-SCOUT.md; Usage 8a).
Must catch: an unattributed all-cipher pile (fr.2988 shape) in the top decile; scout.js / FORMULA drift; stale stored formula.
Must NOT: raise a flagged (active-edition / known) copy of the pile; move a named row's total or tier; give 'pending' to an
unknown script with no holder context; write any file.
Run: python3 tools/tests/test_scout_rubric.py"""
import json
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
REPO = os.path.dirname(os.path.dirname(HERE))
sys.path.insert(0, os.path.join(REPO, "tools"))
import scout_rubric as sr  # noqa: E402

fails = 0


def check(label, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), label, "" if ok else f"-> {detail}"[:400])


D = json.load(open(os.path.join(REPO, "QUEUE-scores.json"), encoding="utf-8"))
ROWS = [dict(r, unread=r.get("unread", 0)) for r in D["scored"]]
AXES7 = ("language_fit", "material", "key_lead", "size", "competition", "weight", "unread")
PILE = dict(name="fr.2988-shaped pile", language_fit="pending", all_cipher=True, holder_era_ours=True, material=3, key_lead=0,
            size=3, competition=3, weight=None, holder_kind="national-library-diplomatic", unread=3,
            est_signs=sr.est_signs_from_pile(26, 4))
HELD = dict(name="fr.20506-shaped volume notice", language_fit="pending", all_cipher=True, holder_era_ours=True, material=1,
            key_lead=0, size=1, competition=3, weight=None, holder_kind="national-library-diplomatic", unread=3)


def rank_of(row, rows=ROWS):
    r = sr.rank(rows + [row])
    return 1 + [x["name"] for x in r].index(row["name"]), len(r), r


s = sr.score(PILE)
check("pile axis: est_signs 26 x 4 x 650 = 67,600 -> 3", s["pile"] == 3 and PILE["est_signs"] == 67600, s)
check("S1 total 47", s["total"] == 47, s["total"])
k, n, _ = rank_of(PILE)
check(f"S1 fr.2988-shaped pile ranks {k} of {n}, top decile (<= {sr.top_decile(n)})", k <= sr.top_decile(n))
old = dict(PILE, language_fit=0, weight=0, pile=0)
k0, _, _ = rank_of(old)
check(f"S1 null: the same row under the old rubric ranks {k0}, outside the top decile", k0 > sr.top_decile(n))
kf, nf, _ = rank_of(dict(PILE, flag="active-edition"))
check(f"S2 flagged copy ranks {kf} of {nf}, outside the top decile", kf > sr.top_decile(nf))
check("S2 flagged copy of a 'known' flag too", rank_of(dict(PILE, flag="known"))[0] > sr.top_decile(nf))
base = sr.rank(ROWS)
top3 = [r["name"] for r in sorted(ROWS, key=lambda r: -r["total"])[:3]]
_, _, with_pile = rank_of(PILE)
pos = {r["name"]: i + 1 for i, r in enumerate(with_pile)}
check(f"S3 today's top three named rows stay in the top five with the pile inserted ({[pos[t] for t in top3]})",
      all(pos[t] <= 5 for t in top3))
stepney = next(r for r in ROWS if r["name"].startswith("George Stepney"))
new = sr.score(stepney)
oldtotal = (stepney["language_fit"] * 3 + stepney["material"] * 4 + stepney["key_lead"] * 3 + stepney["size"] * 2
            + stepney["competition"] * 2 + stepney["weight"] + stepney["unread"] * 3)
check("S4 short named letter with a key lead: total unchanged by the new terms, same tier",
      new["total"] == oldtotal and new["tier"] == sr.score(dict(stepney, pile=0))["tier"], (new["total"], oldtotal))
check("every existing row keeps its seven-axis total (pile absent = 0)",
      all(sr.score(r)["total"] == sum(w * r[a] for a, w in zip(AXES7, (3, 4, 3, 2, 2, 1, 3))) for r in ROWS))
check("'pending' without holder context scores 0 (unknown script stays 0)",
      sr.language_value("pending", all_cipher=True, holder_era_ours=False) == 0 and sr.language_value("pending") == 0)
check("weight prior: state diplomatic 2, otherwise 1", sr.weight_prior("state-diplomatic") == 2 and sr.weight_prior("private") == 1)
check("pile axis edges 1999/2000/10000/10001/50000/50001 -> 0/1/1/2/2/3",
      [sr.pile_axis(x) for x in (1999, 2000, 10000, 10001, 50000, 50001)] == [0, 1, 1, 2, 2, 3])
kh, nh, _ = rank_of(HELD)
khf, nhf, _ = rank_of(dict(HELD, flag="active-edition"))
print(f"S5 held-out fr.20506 shape (not used to set weights): total {sr.score(HELD)['total']}, rank {kh} of {nh} unflagged; "
      f"{khf} of {nhf} flagged active-edition")
check("S6 scout.js total expression equals FORMULA",
      sr.normalise(sr.js_formula(os.path.join(REPO, ".claude", "workflows", "scout.js"))) == sr.normalise(sr.FORMULA))
print("S7 stored formula:", D["formula"], "| equal to FORMULA:", sr.normalise(D["formula"]) == sr.normalise(sr.FORMULA))
before = os.path.getmtime(os.path.join(REPO, "QUEUE-scores.json"))
import io, contextlib
with contextlib.redirect_stdout(io.StringIO()) as o:
    code = sr.rerank(os.path.join(REPO, "QUEUE-scores.json"))
check("--rerank reports the drift (returns 1) and writes nothing",
      code == (1 if sr.normalise(D["formula"]) != sr.normalise(sr.FORMULA) else 0)
      and os.path.getmtime(os.path.join(REPO, "QUEUE-scores.json")) == before and "DRIFT" in o.getvalue())
print(f"\n{'all passed' if not fails else f'{fails} FAILED'}")
sys.exit(1 if fails else 0)

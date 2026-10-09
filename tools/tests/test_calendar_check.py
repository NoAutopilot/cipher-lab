#!/usr/bin/env python3
"""Offline tests for tools/calendar_check.py and prior_work.date_variants (MQS-SCOUT, 9 Oct 2026; PREREG C1, C2; Usage 8a).
Must catch: the Gramont weekday (4 May 1531 Julian Thursday, 4 May 1530 Wednesday); the 1700 boundary (10 days, then 11).
Must NOT: change any date_variants output outside Julian 1 Jan - 28 Feb 1700 (old shift 10 before 1700, 11 after, kept
elsewhere), or open a network connection.
Run: python3 tools/tests/test_calendar_check.py"""
import datetime
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, os.path.join(os.path.dirname(HERE)))
import calendar_check as cc  # noqa: E402
import prior_work as pw  # noqa: E402

fails = 0


def check(label, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), label, "" if ok else f"-> {detail}"[:300])


check("21 May 1584 Julian is a Thursday (paper p.136 n.97)", cc.weekday(1584, 5, 21, "julian") == "thursday")
check("4 May 1531 Julian is a Thursday (Gramont AUDIT.md)", cc.weekday(1531, 5, 4, "julian") == "thursday")
check("4 May 1530 Julian is a Wednesday", cc.weekday(1530, 5, 4, "julian") == "wednesday")
check("CLI exit 0 when the weekday fits, 1 when not",
      cc.main(["1531-05-04", "--calendar", "julian", "--weekday", "thursday"]) == 0
      and cc.main(["1530-05-04", "--calendar", "julian", "--weekday", "thursday"]) == 1)
check("Julian 15 Jan 1700 = Gregorian 25 Jan 1700 (10 days)", cc.other_style((1700, 1, 15), "os") == (1700, 1, 25))
check("Julian 28 Feb 1700 = Gregorian 10 Mar 1700; Julian 29 Feb 1700 = Gregorian 11 Mar", 
      cc.other_style((1700, 2, 28), "os") == (1700, 3, 10) and cc.other_style((1700, 2, 29), "os") == (1700, 3, 11))
check("Julian 1 Mar 1700 = Gregorian 12 Mar 1700 (11 days)", cc.other_style((1700, 3, 1), "os") == (1700, 3, 12))
check("Gregorian 25 Jan 1700 = Julian 15 Jan 1700 (ns)", cc.other_style((1700, 1, 25), "ns") == (1700, 1, 15))
check("known anchors: Gregorian reform 5 Oct 1582 Julian = 15 Oct Gregorian; 2 Sep 1752 Julian = 13 Sep Gregorian (Britain's 14 Sep followed it)",
      cc.other_style((1582, 10, 5), "os") == (1582, 10, 15) and cc.other_style((1752, 9, 2), "os") == (1752, 9, 13))
check("year-start: march25 maps 10 Feb 1650 to 1651; 1 Apr 1650 stays; jan1 is identity",
      cc.historical_year(1650, 2, 10, "march25") == 1651 and cc.historical_year(1650, 4, 1, "march25") == 1650
      and cc.historical_year(1650, 2, 10, "jan1") == 1650)
D = datetime.date


def days(d, cal=""):
    return sorted(x for x, lab in pw.date_variants(d, cal) if lab == "other style")


old = lambda d, cal: sorted(d + datetime.timedelta(days=s + k) for s in {"os": [10 if d.year < 1700 else 11],
                            "ns": [-(10 if d.year < 1700 else 11)]}.get(cal, [10 if d.year < 1700 else 11, -(10 if d.year < 1700 else 11)])
                            for k in (-1, 0, 1))
same = all(days(d, c) == old(d, c) for d in (D(1584, 5, 21), D(1650, 6, 1), D(1699, 12, 31), D(1700, 3, 12), D(1700, 6, 1),
                                           D(1752, 9, 1)) for c in ("", "os", "ns"))
check("must not change: date_variants equals the old fixed-shift output outside Julian Jan-Feb 1700", same)
check("1700-03-01 written Gregorian (ns): -10 now (Julian 19 Feb), the old code gave -11 -- the same boundary fixed on the other side",
      days(D(1700, 3, 1), "ns") == [D(1700, 2, 18), D(1700, 2, 19), D(1700, 2, 20)], days(D(1700, 3, 1), "ns"))
check("1700-01-15 as written Julian: other style is 25 Jan +-1 (the old code gave 26 Jan)",
      days(D(1700, 1, 15), "os") == [D(1700, 1, 24), D(1700, 1, 25), D(1700, 1, 26)], days(D(1700, 1, 15), "os"))
check("outside 1582-1752 date_variants adds nothing", days(D(1500, 1, 1)) == [] and days(D(1800, 1, 1)) == [])
print(f"\n{'all passed' if not fails else f'{fails} FAILED'}")
sys.exit(1 if fails else 0)

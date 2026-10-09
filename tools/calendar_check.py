#!/usr/bin/env python3
"""calendar_check.py -- the one Julian/Gregorian routine (MQS-SCOUT, 9 Oct 2026; LANE MQS, matrix rows M37/M39/M40).

Exact Julian Day Number arithmetic, so a letter dated by weekday (Mary Stuart paper p.136 n.97-98) or by Old/New Style can be
tested: `python3 tools/calendar_check.py 1584-05-21 --calendar julian --weekday thursday` exits 0 when the weekday fits,
1 when not. Functions: jdn_julian, jdn_gregorian, weekday, other_style(date, style). `--year-start easter|march25|jan1`
(France before 1567 began the year at Easter; England before 1752 on 25 March) maps a written year to the historical
(1 Jan) year of a date written between 1 Jan and the new-year day, via `historical_year`.

It replaces prior_work.date_variants()'s fixed shift (10 days before 1700, 11 after), which was wrong for Julian 1 Jan -
28 Feb 1700: Julian 15 Jan 1700 = Gregorian 25 Jan 1700 (10 days; the Julian calendar's 29 Feb 1700 exists, so the gap grows
to 11 from Julian 1 Mar 1700). Worked: 21 May 1584 Julian was a Thursday; 4 May 1531 Julian a Thursday, 4 May 1530 a
Wednesday (Gramont AUDIT.md: "Jeudy quatriesme de May" fits 1531).

Usage 8a scope. Catches: a weekday that fits one year and not its neighbour (the Gramont case); a wrong shift across 1700.
Must NOT: flag a date written in the calendar it was written in, change a date outside 1582-1752 in other_style (it is
exact there too, but prior_work only applies it inside that span), or touch the network.
Tests: python3 tools/tests/test_calendar_check.py
"""
import argparse
import sys

DAYS = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]


def jdn_gregorian(y, m, d):
    a = (14 - m) // 12
    yy, mm = y + 4800 - a, m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - yy // 100 + yy // 400 - 32045


def jdn_julian(y, m, d):
    a = (14 - m) // 12
    yy, mm = y + 4800 - a, m + 12 * a - 3
    return d + (153 * mm + 2) // 5 + 365 * yy + yy // 4 - 32083


def _from_jdn(jdn, julian):
    if julian:
        c = jdn + 32082
        d = (4 * c + 3) // 1461
        e = c - 1461 * d // 4
    else:
        a = jdn + 32044
        b = (4 * a + 3) // 146097
        c = a - 146097 * b // 4
        d = (4 * c + 3) // 1461
        e = c - 1461 * d // 4
        d += 100 * b
    m = (5 * e + 2) // 153
    day = e - (153 * m + 2) // 5 + 1
    month = m + 3 - 12 * (m // 10)
    year = d - 4800 + m // 10
    return year, month, day


def weekday(y, m, d, calendar="gregorian"):
    """Name of the weekday of a date written in `calendar` ('julian' or 'gregorian')."""
    jdn = jdn_julian(y, m, d) if calendar == "julian" else jdn_gregorian(y, m, d)
    return DAYS[jdn % 7]


def _ymd(date):
    return (date.year, date.month, date.day) if hasattr(date, "year") else tuple(date)


def other_style(date, style):
    """`date` (a datetime.date or a (y, m, d) tuple, as written) in the other calendar, as a (y, m, d) tuple: style 'os' =
    written Julian -> Gregorian, 'ns' = written Gregorian -> Julian. A tuple is needed for Julian 29 Feb 1700."""
    y, m, d = _ymd(date)
    if style == "os":
        return _from_jdn(jdn_julian(y, m, d), julian=False)
    if style == "ns":
        return _from_jdn(jdn_gregorian(y, m, d), julian=True)
    raise ValueError("style must be 'os' or 'ns'")


def shift_days(date, style):
    """Signed days to add to the date as written, in datetime.date (proleptic Gregorian) arithmetic, to reach the other style's
    label: 'os' (written Julian) +10 up to Julian 28 Feb 1700, +11 from 29 Feb; 'ns' (written Gregorian) -10 up to
    Gregorian 10 Mar 1700, -11 from 12 Mar. Exact from the day numbers. Known limit: Julian 29 Feb 1700 has no
    datetime.date, so a 'ns' target of Gregorian 11 Mar 1700 is labelled 1 Mar (-10); prior_work's +-1 window covers 29 Feb."""
    y, m, d = _ymd(date)
    oy, om, od = other_style((y, m, d), style)
    return jdn_gregorian(oy, om, od) - jdn_gregorian(y, m, d)


def historical_year(year, month, day, year_start):
    """The 1 January-based year of a date written under a year-start convention. march25: Jan 1 - Mar 24 carry the old
    number, so historical = written + 1. easter: approximated as 'before 1 April' -- the true cut is the Easter date of
    that year, so a date in March-April under easter style is uncertain and the caller must check it by hand."""
    if year_start == "jan1":
        return year
    if year_start == "march25":
        return year + 1 if (month, day) < (3, 25) else year
    if year_start == "easter":
        return year + 1 if month < 4 else year
    raise ValueError("year_start must be easter, march25 or jan1")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("date", help="YYYY-MM-DD, as written")
    ap.add_argument("--calendar", choices=["julian", "gregorian"], default="gregorian", help="calendar the date is written in")
    ap.add_argument("--weekday", help="weekday the source states; exit 0 when it fits, 1 when not")
    ap.add_argument("--year-start", choices=["easter", "march25", "jan1"], default="jan1")
    a = ap.parse_args(argv)
    y, m, d = (int(x) for x in a.date.split("-"))
    hy = historical_year(y, m, d, a.year_start)
    if hy != y:
        print(f"year-start {a.year_start}: written {y} is {hy} counted from 1 January")
    got = weekday(hy, m, d, a.calendar)
    style = "os" if a.calendar == "julian" else "ns"
    oy, om, od = other_style((hy, m, d), style)
    print(f"{hy:04d}-{m:02d}-{d:02d} {a.calendar} = {oy:04d}-{om:02d}-{od:02d} {'gregorian' if style == 'os' else 'julian'}; weekday {got}")
    if a.weekday:
        ok = got == a.weekday.lower()
        print("weekday fits" if ok else f"weekday does NOT fit (stated {a.weekday.lower()}, computed {got})")
        return 0 if ok else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())

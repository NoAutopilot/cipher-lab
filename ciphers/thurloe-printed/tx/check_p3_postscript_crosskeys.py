#!/usr/bin/env python3
"""P3 (John Butler) postscript, djvu 48000-48004: s.17 (LANE T worker H) read it from
key_butler.tsv at H9/C15/M33/U2 of 59. This is a one-attempt check (job brief: 'one attempt
only') of whether two *other* letters' independently-built keys -- key_fauconberg.tsv (a
different correspondent and decade, 1658) and pool_1654/key_stamford.tsv (a different
correspondent, 1655) -- assign the same meaning to any of the postscript's 20 distinct
M-graded values, which would be a reason to raise that token's grade. Butler's own letter is a
different cipher system (French/Dutch informant, values into the 900s alongside Tomokiyo's H
values); no positive result here would mean Birch's printers reused one nomenclature across
correspondents, an a priori unlikely finding, but the check costs nothing and the brief asks
for it once. Reports what was found; does not itself change key_butler.tsv or reading_P3.txt.

Usage: python3 check_p3_postscript_crosskeys.py [--check]
"""
import csv
import os
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
TARGET = os.path.dirname(HERE)
sys.path.insert(0, HERE)
from common import load_key

BUTLER_KEY = os.path.join(TARGET, 'key_butler.tsv')
FAUCONBERG_KEY = os.path.join(TARGET, 'key_fauconberg.tsv')
STAMFORD_KEY = os.path.join(TARGET, 'pool_1654', 'key_stamford.tsv')
READING = os.path.join(TARGET, 'reading_P3.txt')
OUT = os.path.join(HERE, 'p3_postscript_crosskey.tsv')

POSTSCRIPT_PREFIX = 'L4800'  # L48000..L48004


def load_postscript_m_values():
    """Pull the postscript's own M-graded (value, meaning) rows straight from reading_P3.txt
    (LANE T worker H, s.17), the same table the brief asks to re-check, not re-derived here."""
    seen = {}
    with open(READING) as f:
        for line in f:
            parts = line.rstrip('\n').split('\t')
            if len(parts) < 4:
                continue
            loc, value, grade, meaning = parts[0], parts[1], parts[2], parts[3]
            if not loc.startswith(POSTSCRIPT_PREFIX):
                continue
            if grade != 'M':
                continue
            v = value.rstrip('.').rstrip(',')
            seen.setdefault(v, meaning)
    return seen


def build_rows():
    m_values = load_postscript_m_values()
    fauconberg = load_key(FAUCONBERG_KEY)
    stamford = load_key(STAMFORD_KEY)
    rows = []
    for v in sorted(m_values, key=lambda x: int(x)):
        butler_meaning = m_values[v]
        f_entry = fauconberg.get(v)
        s_entry = stamford.get(v)
        f_meaning = f_entry['meaning'] if f_entry else ''
        s_meaning = s_entry['meaning'] if s_entry else ''
        f_agrees = bool(f_entry) and f_meaning == butler_meaning
        s_agrees = bool(s_entry) and s_meaning == butler_meaning
        rows.append({
            'value': v,
            'butler_meaning_M': butler_meaning,
            'fauconberg_meaning': f_meaning,
            'fauconberg_agrees': 'yes' if f_agrees else ('present_disagrees' if f_entry else 'absent'),
            'stamford_meaning': s_meaning,
            'stamford_agrees': 'yes' if s_agrees else ('present_disagrees' if s_entry else 'absent'),
        })
    return rows


def write_rows(rows, path=OUT):
    with open(path, 'w', newline='') as f:
        w = csv.DictWriter(f, fieldnames=['value', 'butler_meaning_M', 'fauconberg_meaning',
                                           'fauconberg_agrees', 'stamford_meaning',
                                           'stamford_agrees'], delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow(r)


def summarize(rows):
    raised = [r for r in rows if r['fauconberg_agrees'] == 'yes' or r['stamford_agrees'] == 'yes']
    print(f"{len(rows)} distinct M-graded postscript values checked against key_fauconberg.tsv "
          f"and pool_1654/key_stamford.tsv.")
    print(f"Values present in key_fauconberg.tsv: "
          f"{sum(1 for r in rows if r['fauconberg_agrees'] != 'absent')}/{len(rows)}; "
          f"agreeing with key_butler's own M meaning: "
          f"{sum(1 for r in rows if r['fauconberg_agrees'] == 'yes')}.")
    print(f"Values present in pool_1654/key_stamford.tsv: "
          f"{sum(1 for r in rows if r['stamford_agrees'] != 'absent')}/{len(rows)}; "
          f"agreeing with key_butler's own M meaning: "
          f"{sum(1 for r in rows if r['stamford_agrees'] == 'yes')}.")
    print(f"Values raised from M by either cross-key: {len(raised)}.")
    for r in raised:
        print(f"  value {r['value']}: butler M={r['butler_meaning_M']!r}, "
              f"fauconberg={r['fauconberg_meaning']!r} ({r['fauconberg_agrees']}), "
              f"stamford={r['stamford_meaning']!r} ({r['stamford_agrees']})")
    if not raised:
        print("No value is raised. Result stands as a negative: the postscript's 33 M-graded "
              "token occurrences (20 distinct values) stay M under key_butler.tsv; this "
              "one-attempt cross-key check against key_fauconberg.tsv and "
              "pool_1654/key_stamford.tsv finds no agreement to raise any of them.")


def main():
    check = '--check' in sys.argv
    rows = build_rows()
    if check:
        if not os.path.exists(OUT):
            print(f"FAIL: {OUT} does not exist", file=sys.stderr)
            sys.exit(1)
        with open(OUT, newline='') as f:
            committed = f.read()
        import io
        buf = io.StringIO()
        w = csv.DictWriter(buf, fieldnames=['value', 'butler_meaning_M', 'fauconberg_meaning',
                                             'fauconberg_agrees', 'stamford_meaning',
                                             'stamford_agrees'], delimiter='\t')
        w.writeheader()
        for r in rows:
            w.writerow(r)
        fresh = buf.getvalue()
        if fresh != committed:
            print("FAIL: committed p3_postscript_crosskey.tsv is stale", file=sys.stderr)
            sys.exit(1)
        print("OK: p3_postscript_crosskey.tsv matches a fresh run")
        summarize(rows)
        return
    write_rows(rows)
    summarize(rows)


if __name__ == '__main__':
    main()

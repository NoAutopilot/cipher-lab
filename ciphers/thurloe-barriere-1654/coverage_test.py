#!/usr/bin/env python3
"""First cheap test (breadth rule): apply key_gloss.tsv's 'primary' (non-conflicting) rows to every run in
passA.tsv and report coverage (tokens read / total) across the WHOLE letter, plus how many of the newly-covered
UNGLOSSED runs give a real word where a bare-digit/letter code lands. Marks (trailing '*', '^', etc.) are
stripped before matching, since this pass could not reliably type marks (see NOTES.md); the bare code is treated
as the cipher's matching unit here.

Usage: python3 coverage_test.py [key_gloss.tsv] [passA.tsv]
"""
import csv, re, sys, os

keypath = sys.argv[1] if len(sys.argv) > 1 else 'key_gloss.tsv'
ctpath = sys.argv[2] if len(sys.argv) > 2 else 'passA.tsv'

def strip_mark(tok):
    return re.sub(r'[\*\^`\'´ˇ¨=]+$', '', tok)

def load_primary_key(path):
    key = {}
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            if d.get('status') == 'primary':
                code = strip_mark(d['code'])
                key.setdefault(code, d['value'])
    return key

# Multi-row runs whose combined gloss lives on only one constituent row (R004+R005; R022+R023+R024) --
# every row in the same group counts as "glossed" for the newly-covered-tokens statistic, not just the one
# that carries the printed text in passA.tsv.
GLOSS_GROUPS = [{'R004', 'R005'}, {'R022', 'R023', 'R024'}]

def glossed_group_ids(runs):
    ids = set()
    for r in runs:
        if r.get('gloss_as_printed', '').strip():
            ids.add(r['run_id'])
    for g in GLOSS_GROUPS:
        if g & ids:
            ids |= g
    return ids

def load_runs(path):
    runs = []
    with open(path) as f:
        header = None
        for line in f:
            if line.startswith('#') or not line.strip():
                continue
            row = line.rstrip('\n').split('\t')
            if header is None:
                header = row
                continue
            d = dict(zip(header, row))
            runs.append(d)
    return runs

def main():
    key = load_primary_key(keypath)
    runs = load_runs(ctpath)
    total_tokens = 0
    read_tokens = 0
    glossed_run_ids = glossed_group_ids(runs)
    newly_covered_in_unglossed = 0
    unglossed_runs_with_hit = set()
    for r in runs:
        toks = r['tokens'].split()
        has_gloss = r['run_id'] in glossed_run_ids
        for t in toks:
            total_tokens += 1
            bare = strip_mark(t)
            if bare in key:
                read_tokens += 1
                if not has_gloss:
                    newly_covered_in_unglossed += 1
                    unglossed_runs_with_hit.add(r['run_id'])
    print(f'key size (primary, non-conflicting rows, unique codes): {len(key)}')
    print(f'total code tokens across the letter (all runs, passA): {total_tokens}')
    print(f'tokens read by the primary key: {read_tokens} ({100*read_tokens/total_tokens:.1f}%)')
    print(f'of those, tokens in runs that had NO printed gloss at all: {newly_covered_in_unglossed}')
    print(f'unglossed runs that got at least one hit: {sorted(unglossed_runs_with_hit)}')
    print(f'runs with a printed gloss: {len(glossed_run_ids)} of {len(runs)} runs total')

if __name__ == '__main__':
    main()

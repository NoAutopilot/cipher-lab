#!/usr/bin/env python3
"""The box-to-token join gate (8a; TXE4-0 REPAIR unit 1, 12 Oct 2026, account 3).

Why it exists: `tools/box_token_align.py`'s own truth-free shift check (`offset_check`/`check_report`) prints a
count, but nothing bounds it: a map wrong by one position on 10 of 26 lines still "looked fine" to a reader
skimming the printed numbers, and the KM gate (`tools/tests/km_birago_map.py`) PASSed the shifted map outright
(`ciphers/nevers-birago-fr3251-1572/atlas/README.md` "Label-aware box map"; `tools/tests/RESCORE.md` section 1).
This module turns that same statistic into a bounded verdict any consumer can call before trusting a map, and a
sidecar file a consumer can require before scoring from it.

Statistic (reused, not re-derived): for every check-labelled box placed on one token (or, when the check labels
also steered the map, its own leave-one-out position -- `--steered`, or auto-detected by the caller when the
--check-labels file is the same file used as --topk/--tile-labels), take the first offset in 0, -1, +1, +-2 at
which the label equals an acceptable read sign at (line, pos + offset), else 'none'. Counted per line and overall.

Bounds (registered here, 12 Oct 2026):
  B1, per line: a line with >= 5 placed check tiles has more matches at 0 than at -1, and more than at +1.
      A line under 5 placed tiles is listed 'unchecked', never failed.
  B2, overall: the matches at -1 and +1 together are at most max(0.05, p95) of the placed check tiles, p95 the
      95th percentile of that same share over 20 seeded permutations of the check labels within each page (the
      label values are shuffled among the labelled sids of one page; positions never move).
  B3, overall: the share at 0 exceeds the same null's 95th percentile.
  Verdict: UNCHECKABLE when B3 fails (the labels cannot see a shift at all -- the same thing a fully permuted
  check column looks like, MC4 below); otherwise FAIL when B1 or B2 fails; otherwise PASS.

Sidecar: MAP.tsv.joincheck.json beside the map -- verdict, per-line and overall counts, the null p95s, the map's
own sha256, the inputs' sha256, and the UTC time. `require(map_path)` is for consumers: it refuses (exit 2) a map
with no sidecar, a sidecar that is not PASS, or a map whose sha256 no longer matches its sidecar (edited after
the check ran). The only escape is `--allow-unchecked-join REASON`, which exists only to reproduce old committed
results: it prints the reason and returns a header string 'UNCHECKED JOIN: REASON' for the consumer to stamp into
its own output.

Never reads a truth file: inputs are a box_token_align MAP.tsv (sid/line/pos/op), a check-labels TSV (sid, label)
and the line read(s) the map was built from. No benchmark-tx/*.truth.tsv, BENCHMARK-TX.tsv row, frozen confirm
item or clerk sheet is opened.

CLI:
  python3 tools/join_check.py --map MAP.tsv --check-labels L.tsv --read READ.tsv [--read READ2.tsv] [--steered]
      [--draws 20] [--seed 20261012]
  python3 tools/join_check.py --map MAP.tsv --require [--allow-unchecked-join REASON]

Exit codes: 0 PASS, 2 FAIL (also: --require refusal), 3 UNCHECKABLE.

Offline test: tools/tests/test_join_check.py. The must-catch / must-not-block cases below are documented there and
named again in each test's docstring (CLAUDE.md 8a):
  MC1 a single line shifted after an early stray mark -> FAIL on B1 for that line.
  MC2 every line on a page shifted the same way (not just one) -> FAIL, B1 fails on every line.
  MC3 (repo files present) the committed old atlas/no87_box_token.tsv, checked with sorter/no87/seed.tsv's atlas
      labels -> FAIL (157/24/14 of 208; B1 fails on f178v L09, L11, L13, L17, L21, f179r L02, L03; L06 and L07
      pass B1 -- shifted only after mid-line -- and are caught by B2 instead).
  MC4 check labels permuted within each page -> UNCHECKABLE, never PASS.
  MC5 require() refuses a map with no sidecar, and a map edited after its sidecar was written.
  NB1 (repo files present) the committed atlas/no87_box_token_labelaware.tsv with the same labels -> PASS
      (188/1/2 of 203; leave-one-out 187/2/2).
  NB2 a correct synthetic map with genuine 2:1 and 1:2 steps -> PASS (those boxes are never in pos_of at all).
  NB3 a correct map with fewer than 5 check tiles on some lines -> PASS, those lines 'unchecked'.
  NB4 a correct map with 30%-accurate check labels -> PASS (B2's bound is the null's p95: weak labels alone do
      not fail a right map).
  NB5 a correct map over a repeated sign (the same sign at pos and pos+1) -> PASS (offset 0 counted first).
"""
import argparse
import datetime
import hashlib
import json
import os
import random
import sys
from collections import Counter, defaultdict

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import box_token_align as BA  # noqa: E402

MIN_LINE = 5
DEFAULT_DRAWS = 20
DEFAULT_SEED = 20261012


def offsets_per_line(pos_of, labels, read_sign):
    """{line: Counter({'0','-1','+1','+-2','none'})} over sids that are both labelled and placed by pos_of."""
    per = defaultdict(Counter)
    for sid, lab in labels.items():
        if sid not in pos_of:
            continue
        line, p = pos_of[sid]; p = int(p)
        hit = None
        for d, name in ((0, '0'), (-1, '-1'), (1, '+1'), (-2, '+-2'), (2, '+-2')):
            if lab in read_sign.get((line, p + d), ()):
                hit = name; break
        per[line][hit or 'none'] += 1
    return per


def _overall(per):
    c = Counter()
    for v in per.values():
        c.update(v)
    return c


def null_draws(pos_of, labels, read_sign, draws=DEFAULT_DRAWS, seed=DEFAULT_SEED):
    """Shuffle the label VALUES among the labelled, placed sids of each page (box_token_align.split_line's fol),
    positions untouched; -> (share_at_0 list, share_at_pm1 list), one pair per draw."""
    rng = random.Random(seed)
    placed_sids = [sid for sid in labels if sid in pos_of]
    by_page = defaultdict(list)
    for sid in placed_sids:
        fol, _ = BA.split_line(pos_of[sid][0])
        by_page[fol].append(sid)
    share0, sharepm1 = [], []
    for _ in range(draws):
        shuffled = dict(labels)
        for sids in by_page.values():
            vals = [labels[s] for s in sids]
            rng.shuffle(vals)
            for s, v in zip(sids, vals):
                shuffled[s] = v
        overall = _overall(offsets_per_line(pos_of, shuffled, read_sign))
        n = sum(overall.values())
        share0.append(overall['0'] / n if n else 0.0)
        sharepm1.append((overall['-1'] + overall['+1']) / n if n else 0.0)
    return share0, sharepm1


def percentile(values, pct):
    """The pct-th percentile of values (linear interpolation, numpy's default method). No numpy dependency."""
    if not values:
        return 0.0
    s = sorted(values)
    if len(s) == 1:
        return s[0]
    k = (len(s) - 1) * (pct / 100.0)
    f = int(k)
    c = min(f + 1, len(s) - 1)
    if f == c:
        return s[f]
    frac = k - f
    return s[f] * (1 - frac) + s[c] * frac


def evaluate(pos_of, labels, read_sign, draws=DEFAULT_DRAWS, seed=DEFAULT_SEED):
    """pos_of: {sid: (line, pos)}. labels: {sid: label}. read_sign: {(line, pos): set-of-signs}.
    -> dict(verdict, n, overall, share0, sharepm1, b1, b2, b3, p95_0, p95_pm1, b2_bound, lines, draws, seed)."""
    per = offsets_per_line(pos_of, labels, read_sign)
    overall = _overall(per)
    n = sum(overall.values())
    lines = {}
    b1_ok = True
    for line in sorted(per):
        c = per[line]
        placed = sum(c.values())
        if placed < MIN_LINE:
            lines[line] = dict(counts=dict(c), placed=placed, verdict='unchecked')
            continue
        ok = c['0'] > c['-1'] and c['0'] > c['+1']
        lines[line] = dict(counts=dict(c), placed=placed, verdict='pass' if ok else 'fail')
        b1_ok = b1_ok and ok
    share0_null, sharepm1_null = null_draws(pos_of, labels, read_sign, draws, seed)
    p95_0 = percentile(share0_null, 95)
    p95_pm1 = percentile(sharepm1_null, 95)
    share0 = overall['0'] / n if n else 0.0
    sharepm1 = (overall['-1'] + overall['+1']) / n if n else 0.0
    b3_ok = share0 > p95_0
    b2_bound = max(0.05, p95_pm1)
    b2_ok = sharepm1 <= b2_bound
    verdict = 'UNCHECKABLE' if not b3_ok else ('PASS' if (b1_ok and b2_ok) else 'FAIL')
    return dict(verdict=verdict, n=n, overall=dict(overall), share0=share0, sharepm1=sharepm1,
                b1=b1_ok, b2=b2_ok, b3=b3_ok, p95_0=p95_0, p95_pm1=p95_pm1, b2_bound=b2_bound,
                lines=lines, draws=draws, seed=seed)


def read_sign_table(read_rows):
    rs = defaultdict(set)
    for r in read_rows:
        rs[(r['line'], int(r['pos']))].add(r['sign'])
    return rs


def from_files(map_path, check_labels_path, read_paths, steered=False, draws=DEFAULT_DRAWS, seed=DEFAULT_SEED):
    rows = BA.rd(map_path)
    chk = {r['sid']: (r.get('label') or r.get('sign')) for r in BA.rd(check_labels_path)}
    read_rows = []
    for p in read_paths:
        read_rows += BA.rd(p)
    pos_of = BA.positions(rows, loo=steered)
    return evaluate(pos_of, chk, read_sign_table(read_rows), draws, seed)


def sha256_of(path):
    with open(path, 'rb') as f:
        return hashlib.sha256(f.read()).hexdigest()


def sidecar_path(map_path):
    return map_path + '.joincheck.json'


def write_sidecar(map_path, result, inputs=()):
    sc = dict(result)
    sc['map_sha256'] = sha256_of(map_path)
    sc['inputs_sha256'] = {p: sha256_of(p) for p in inputs if p and os.path.exists(p)}
    sc['utc'] = datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ')
    path = sidecar_path(map_path)
    with open(path, 'w', encoding='utf-8') as f:
        json.dump(sc, f, indent=1, sort_keys=True, default=str)
        f.write('\n')
    return path


def require(map_path, allow_unchecked_join=None):
    """Refuses (prints to stderr and sys.exit(2)) a map with no PASS sidecar, or whose sha256 no longer matches
    its sidecar. --allow-unchecked-join REASON skips the check entirely and returns the header stamp string."""
    if allow_unchecked_join:
        msg = f'UNCHECKED JOIN: {allow_unchecked_join}'
        print(msg)
        return msg
    sc = sidecar_path(map_path)
    reason = None
    if not os.path.exists(sc):
        reason = 'no .joincheck.json sidecar'
    else:
        with open(sc, encoding='utf-8') as f:
            d = json.load(f)
        if d.get('verdict') != 'PASS':
            reason = f"sidecar verdict {d.get('verdict')}, not PASS"
        elif sha256_of(map_path) != d.get('map_sha256'):
            reason = 'sha256 mismatch against sidecar (map edited after the check ran)'
    if reason:
        print(f'join_check: refuse {map_path}: {reason} '
              f'(run box_token_align.py --check-bound, or --allow-unchecked-join REASON to reproduce an old result)',
              file=sys.stderr)
        sys.exit(2)
    return None


EXIT = {'PASS': 0, 'FAIL': 2, 'UNCHECKABLE': 3}


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument('--map', required=True)
    ap.add_argument('--require', action='store_true', help='check --map against its sidecar instead of computing one')
    ap.add_argument('--allow-unchecked-join', help='with --require: skip the check, print and return the UNCHECKED JOIN stamp')
    ap.add_argument('--check-labels')
    ap.add_argument('--read', action='append', default=[])
    ap.add_argument('--steered', action='store_true', help='score at each check tile\'s own leave-one-out position')
    ap.add_argument('--draws', type=int, default=DEFAULT_DRAWS)
    ap.add_argument('--seed', type=int, default=DEFAULT_SEED)
    a = ap.parse_args(argv)
    if a.require:
        require(a.map, a.allow_unchecked_join)
        print('join_check: require OK ->', a.map)
        return 0
    if not a.check_labels or not a.read:
        ap.error('--check-labels and --read are required unless --require')
    result = from_files(a.map, a.check_labels, a.read, a.steered, a.draws, a.seed)
    sc = write_sidecar(a.map, result, inputs=[a.check_labels] + a.read)
    print(f"join_check: {result['verdict']} n={result['n']} share0={result['share0']:.3f} (null p95 {result['p95_0']:.3f}) "
          f"share+-1={result['sharepm1']:.3f} (bound {result['b2_bound']:.3f}) -> {sc}")
    for line in sorted(result['lines']):
        d = result['lines'][line]
        print(f"  {line}: {d['verdict']} placed={d['placed']} {d['counts']}")
    return EXIT[result['verdict']]


if __name__ == '__main__':
    sys.exit(main())

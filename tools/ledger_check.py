#!/usr/bin/env python3
"""Gate for LEDGER.md hygiene (RETRO-2026-09-24e proposal 2): duplicate session
ids and non-standard outcome codes. Both problems already had a wording-only
fix in LEDGER.md's own header -- "grep before you append" (RETRO-2026-09-24b,
row 194) and "use only these five codes" (RETRO-2026-09-24d, row 396) -- and
both kept failing at a higher rate in the very next window (a second exact-
duplicate session id; 64% of rows using a non-standard code, up from 32%).
Per CLAUDE.md Usage item 2 ("scripts read, models judge"), this replaces a
third wording pass with a script a worker runs before pushing, the way
tools/decode_key.py already gates a stale reading.

Usage:
  tools/ledger_check.py [--fix-suggest]
    Reads LEDGER.md. For every data row: (1) extracts the Session column (when
    present) and flags any session id seen on more than one row, printing both
    row numbers and their Outcome/cost so a human can pick which to keep; (2)
    extracts the Outcome column's leading token and flags any row whose token
    is not exactly one of D, D-, F, X, N, Q (case-sensitive, no trailing
    punctuation). Exits 0 if nothing is flagged, 1 and prints every flagged
    row otherwise -- gate it before `tools/room.py --push LEDGER.md`.
    --fix-suggest also prints, for each non-standard code, the nearest
    documented code guessed from that row's own Lesson-column language (e.g.
    a Lesson starting "Ran past its cap" suggests D-), without editing the
    file.

  tools/ledger_check.py --split FROM_ROW
    RETRO-2026-09-27x P5. Prints the S/A/V/C effort table (parent.md "Effort allocation": Solving/
    transcription/recovery, Acquisition of inputs, Validation and novelty research, Coordination and
    maintenance) for every data row at or after line FROM_ROW, classified by matching its Role cell
    against tools/data/effort_roles.tsv (a regex -> bucket list, checked in order, first match wins).
    A row can override the regex match with a literal "[bucket:S]" (or A/V/C) tag anywhere in the row.
    A row matching no pattern and carrying no override tag is listed separately, for the parent to
    classify by hand rather than silently dropped from the table. Also prints, for every self-ledger
    parent row (Role matching "parent <name> (Orchestrator ...)"), that parent's own cost against the
    summed cost of the rows between it and the previous such row (its own tenure's workers), the same
    figure parent.md's "Effort allocation" paragraph asks a parent to state in its handoff line when its
    own cost exceeds a third of that sum. Always also runs the main duplicate/outcome-code check below
    (a --split call is typically the last thing before a push, so this is one command instead of two).

  tools/ledger_check.py --placeholder-report
    RETRO-2026-09-26k proposal 3. Lists every row whose Cost cell is an
    unresolved deferral ("see the lane ledger", "parent's get_session (cap
    15; 22:45-23:09 UTC)", "cap N, running") -- i.e. fails COST_RE -- AND
    whose session id (if the row carries one) is not pasted with a real
    number by any *other* row in the file (cross-checked by session id, the
    same field find_session_index's fallback already extracts). Motivated by
    VB-DECODE's row (RETRO-2026-09-26k): its Cost cell still read "parent's
    get_session (cap 15; 22:45-23:09 UTC)" with no later row resolving it,
    which made that retrospective's own "cost per delivered result" total a
    known undercount. Printed only, never gating (exit is always 0): a lane
    orchestrator's own row legitimately says "so far" while the lane is
    still open, so this is a report a retrospective reads, not a check a
    worker's push is blocked on. Does not itself flag a row using a
    non-standard outcome code (see the main check above for that) -- only a
    row whose outcome token is one of the five standard codes is used to
    locate the Cost cell at all, so a row with both an unresolved cost and a
    non-standard outcome code needs the main check's own pass too.

  (always) The main check also flags a row whose Outcome cell starts with a number rather than a
    code -- the RETRO-2026-09-27x P5 shape (rows 1184, 1186-1188, 1191, 1196-1198): a placeholder cost
    cell pushed the resolved cost figure one column right into Outcome, leaving the real code stranded
    in what should be the Lesson cell. This is a distinct defect from a non-standard *code*: the Outcome
    cell here is not a short token at all, so bad_outcomes above never sees it, and the fix is "move the
    figure into the Cost cell" (done for the rows above), not a code substitution.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
LEDGER = os.path.join(ROOT, "LEDGER.md")
EFFORT_ROLES = os.path.join(ROOT, "tools", "data", "effort_roles.tsv")

BUCKET_NAMES = {
    "S": "Solving / transcription / recovery",
    "A": "Acquisition of inputs",
    "V": "Validation and novelty research",
    "C": "Coordination and maintenance",
}
OVERRIDE_RE = re.compile(r"\[bucket:([SAVC])\]")
LEADING_NUM_RE = re.compile(r"^~?(\d+(?:\.\d+)?)")
PARENT_SELF_RE = re.compile(r"^parent\s+\S+\s*\(Orchestrator", re.IGNORECASE)

VALID_CODES = ("D", "D-", "F", "X", "N", "Q")
# Cost is a plain number, an optional "~" (uncertain reading) prefix, or "n/a",
# and may be followed by an explanatory parenthetical or clause in the same
# cell (e.g. "~2 (226k tokens, no subagents)"), so this matches the leading
# token of the cell, not the whole cell.
COST_RE = re.compile(r'^~?\d+(\.\d+)?(\s|\(|$)|^n/a(\s|\(|$)', re.IGNORECASE)
# The Outcome cell itself is always a short bare token, even when it is one of
# the non-standard ones this script exists to catch (A, B, C, S, S-, B+,
# F-rl, ...); this is what tells a Cost-shaped cell apart from an unrelated
# later cell that happens to start with a digit (e.g. "20 workers" in a Lane
# column), by requiring the cell right after it to look like a code at all.
OUTCOME_TOKEN_RE = re.compile(r'^[A-Za-z]{1,2}[+-]?[A-Za-z]{0,2}$')
SESSION_ID_RE = re.compile(r'^session_[A-Za-z0-9]+$')
SEPARATOR_ROW_RE = re.compile(r'^:?-+:?$')


def split_row(line):
    """Split a markdown table row into trimmed cells, tolerating a missing
    trailing '|' (seen on some rows in this file)."""
    parts = line.rstrip("\n").split("|")
    if parts and parts[0].strip() == "":
        parts = parts[1:]
    if parts and parts[-1].strip() == "":
        parts = parts[:-1]
    return [p.strip() for p in parts]


def find_cost_index(fields):
    """Cost is the first field from index 2 on (after Date, Role) that looks
    like a cost AND is immediately followed by an Outcome-shaped cell --
    every row variant in this file runs Date, Role, Model, [Session], Cost,
    Outcome, .... Requiring both cells to fit stops an unrelated later cell
    (e.g. a Lane column reading "20 workers") from being mistaken for Cost.
    A row where no such pair is found is left unchecked rather than guessed
    at, which is deliberate: skipping a row a human would have to untangle
    beats flagging the wrong cell as its Outcome."""
    for i in range(2, len(fields) - 1):
        if COST_RE.match(fields[i]) and OUTCOME_TOKEN_RE.match(fields[i + 1]):
            return i
    return None


def find_session_index(fields):
    """Fallback when find_cost_index() finds no numeric-cost/outcome pair: locate the Session cell directly
    by SESSION_ID_RE regardless of what sits beside it, so a placeholder-cost row ("cap N, exact figure
    pending...", "parent's get_session") still registers its session id for duplicate detection. Lesson of
    26 Sept 2026: two real duplicate pairs this window (PR-LAND-5, LQ-L20-LAND) each had one row whose Cost
    cell was placeholder text, which made find_cost_index() return None for that row and drop its session id
    out of the check -- the later row with a real number was then seen only once, never flagged."""
    for i, f in enumerate(fields):
        if SESSION_ID_RE.match(f):
            return i
    return None


def leading_token(field):
    if not field:
        return ""
    tok = field.split()[0] if field.split() else field
    return tok.rstrip(".,;:")


def guess_fix(lesson):
    low = lesson.lower()
    if "qa" in low or "audit" in low or "quality" in low:
        return "Q"
    if "over-claim" in low or "over-call" in low or "retract" in low:
        return "X"
    if "ran past" in low or "poke" in low or "idle" in low or "needed a poke" in low:
        return "D-"
    if "blocked" in low or "failed" in low or "init error" in low or "usage limit" in low:
        return "F"
    if "negative" in low or "no hit" in low or "clean" in low or "nothing found" in low:
        return "N"
    return "D"


def check(lines):
    seen_sessions = {}
    bad_outcomes = []
    in_table = False

    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line.startswith("|"):
            in_table = False
            continue
        fields = split_row(line)
        if not fields:
            continue
        if SEPARATOR_ROW_RE.match(fields[0]) and all(SEPARATOR_ROW_RE.match(f) for f in fields):
            in_table = True
            continue
        if not in_table:
            continue  # header row
        cost_i = find_cost_index(fields)
        if cost_i is None or cost_i + 1 >= len(fields):
            si = find_session_index(fields)
            if si is not None and si + 1 < len(fields):
                seen_sessions.setdefault(fields[si], []).append((lineno, "(unparsed)", fields[si + 1]))
            continue
        outcome_field = fields[cost_i + 1]
        session_field = fields[cost_i - 1] if cost_i - 1 >= 3 else None
        lesson = fields[-1] if len(fields) > cost_i + 1 else ""

        if session_field and SESSION_ID_RE.match(session_field):
            seen_sessions.setdefault(session_field, []).append((lineno, outcome_field, fields[cost_i]))

        token = leading_token(outcome_field)
        if token not in VALID_CODES:
            bad_outcomes.append((lineno, outcome_field, lesson))

    dup_sessions = {sid: rows for sid, rows in seen_sessions.items() if len(rows) > 1}
    return dup_sessions, bad_outcomes


def row_cost_and_session(fields):
    """Best-effort per-row (cost_text, session_id) for ANY row, resolved or placeholder alike.
    The outcome cell is located by an exact VALID_CODES match (stricter than OUTCOME_TOKEN_RE,
    which also matches ordinary short words like a Lane column's "LANE") so a placeholder-cost
    row's own prose is never mistaken for the outcome cell; the cost cell is whatever sits
    immediately before it, resolved or not. session_id is the first SESSION_ID_RE-matching cell
    anywhere in the row, present or not. Returns (None, session_id) when no outcome-shaped cell
    is found at all."""
    outcome_i = None
    for i in range(3, len(fields)):
        if leading_token(fields[i]) in VALID_CODES:
            outcome_i = i
            break
    session_id = next((f for f in fields if SESSION_ID_RE.match(f)), None)
    if outcome_i is None or outcome_i == 0:
        return None, session_id
    return fields[outcome_i - 1], session_id


def find_placeholder_rows(lines):
    """--placeholder-report: every row whose Cost cell fails COST_RE and whose session id (when
    the row carries one) is never resolved by a real number on any other row in the file. See the
    module docstring's --placeholder-report section for the motivating incident (VB-DECODE)."""
    all_rows = []
    resolved_sessions = set()
    in_table = False

    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line.startswith("|"):
            in_table = False
            continue
        fields = split_row(line)
        if not fields:
            continue
        if SEPARATOR_ROW_RE.match(fields[0]) and all(SEPARATOR_ROW_RE.match(f) for f in fields):
            in_table = True
            continue
        if not in_table:
            continue  # header row
        cost_text, session_id = row_cost_and_session(fields)
        all_rows.append((lineno, cost_text, session_id))
        if cost_text is not None and session_id and COST_RE.match(cost_text):
            resolved_sessions.add(session_id)

    placeholder_rows = []
    for lineno, cost_text, session_id in all_rows:
        if cost_text is None or COST_RE.match(cost_text):
            continue
        if session_id and session_id in resolved_sessions:
            continue
        placeholder_rows.append((lineno, session_id, cost_text))
    return placeholder_rows


def find_shifted_outcome_rows(lines):
    """RETRO-2026-09-27x P5 (always run): a row whose Cost cell fails COST_RE (a placeholder) AND whose
    following cell starts with a bare number is the row-1184 shape -- the resolved cost figure landed in
    what should be the Outcome cell, pushing the real D/D- code one column further right. Distinct from
    bad_outcomes in check(), which only looks at cells find_cost_index() already believes are Outcome."""
    shifted = []
    in_table = False
    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line.startswith("|"):
            in_table = False
            continue
        fields = split_row(line)
        if not fields:
            continue
        if SEPARATOR_ROW_RE.match(fields[0]) and all(SEPARATOR_ROW_RE.match(f) for f in fields):
            in_table = True
            continue
        if not in_table:
            continue
        # The Cost cell sits at index 3 (no Session column) or 4 (with one) -- restrict the search to
        # those two candidate positions, not an open-ended range, so a legitimate Session cell (never
        # COST_RE-shaped either) two cells before a numeric Cost isn't mistaken for the placeholder
        # itself, and so an older, wider ledger row format (date|role|model|cost|outcome|source-type|
        # count|...|lesson) with a plain descriptive cell later in the row ("Bourdeau offline-only",
        # "12") isn't scanned at all.
        for i in (3, 4):
            if i + 2 >= len(fields) or "session_" in fields[i]:
                continue
            # The row-1184 fingerprint is three cells in a row: a placeholder (not COST_RE), then a
            # bare resolved number, then a cell whose OWN leading token is one of the five valid
            # outcome codes -- that third cell is what tells this apart from ordinary prose.
            if not COST_RE.match(fields[i]) and LEADING_NUM_RE.match(fields[i + 1]) \
                    and not OUTCOME_TOKEN_RE.match(fields[i]) \
                    and leading_token(fields[i + 2]) in VALID_CODES:
                shifted.append((lineno, fields[i], fields[i + 1]))
                break
    return shifted


def load_effort_roles(path=EFFORT_ROLES):
    rules = []
    with open(path, encoding="utf-8") as f:
        for line in f:
            line = line.rstrip("\n")
            if not line or line.startswith("#"):
                continue
            pattern, bucket = line.split("\t")
            rules.append((re.compile(pattern, re.IGNORECASE), bucket.strip()))
    return rules


def classify_bucket(role_text, rules):
    m = OVERRIDE_RE.search(role_text)
    if m:
        return m.group(1)
    for pattern, bucket in rules:
        if pattern.search(role_text):
            return bucket
    return None


def leading_cost(cost_text):
    m = LEADING_NUM_RE.match(cost_text or "")
    return float(m.group(1)) if m else None


def split_table(lines, from_row):
    """[(lineno, fields), ...] for every LEDGER.md data row at or after from_row."""
    rows = []
    in_table = False
    for lineno, raw in enumerate(lines, start=1):
        line = raw.rstrip("\n")
        if not line.startswith("|"):
            in_table = False
            continue
        fields = split_row(line)
        if not fields:
            continue
        if SEPARATOR_ROW_RE.match(fields[0]) and all(SEPARATOR_ROW_RE.match(f) for f in fields):
            in_table = True
            continue
        if not in_table:
            continue
        if lineno >= from_row:
            rows.append((lineno, fields))
    return rows


def print_split(lines, from_row):
    rules = load_effort_roles()
    rows = split_table(lines, from_row)

    totals = {b: [0, 0.0] for b in BUCKET_NAMES}
    unmatched = []
    parent_rows = []
    for lineno, fields in rows:
        role = fields[1] if len(fields) > 1 else ""
        cost_text, _ = row_cost_and_session(fields)
        cost = leading_cost(cost_text) or 0.0
        bucket = classify_bucket(role, rules)
        if bucket is None:
            unmatched.append((lineno, role))
        else:
            totals[bucket][0] += 1
            totals[bucket][1] += cost
        if PARENT_SELF_RE.match(role.strip()):
            parent_rows.append((lineno, role, cost))

    grand_total = sum(v[1] for v in totals.values())
    print(f"Effort split, lines >= {from_row} ({len(rows)} rows, USD {grand_total:.2f}):")
    print("Bucket\tRows\tUSD\tShare")
    for b in ("S", "A", "V", "C"):
        n, usd = totals[b]
        share = (usd / grand_total * 100) if grand_total else 0.0
        print(f"{b} ({BUCKET_NAMES[b]})\t{n}\t{usd:.2f}\t{share:.1f}%")

    if unmatched:
        print(f"\nUnmatched rows ({len(unmatched)}), classify by hand or add a [bucket:X] tag:")
        for lineno, role in unmatched:
            print(f"  line {lineno}: {role[:100]}")

    if parent_rows:
        print("\nParent self-ledger rows vs their own tenure's worker spend:")
        prev_lineno = from_row
        for lineno, role, own_cost in parent_rows:
            worker_total = 0.0
            for wl, wfields in rows:
                if prev_lineno <= wl < lineno:
                    wrole = wfields[1] if len(wfields) > 1 else ""
                    if PARENT_SELF_RE.match(wrole.strip()):
                        continue
                    wcost, _ = row_cost_and_session(wfields)
                    worker_total += leading_cost(wcost) or 0.0
            ratio = (own_cost / worker_total) if worker_total else float("inf")
            flag = " -- OVER A THIRD" if worker_total and ratio > 1 / 3 else ""
            print(f"  line {lineno}: {role[:70]} -- own {own_cost:.2f} vs workers {worker_total:.2f}"
                  f" (ratio {ratio:.2f}){flag}")
            prev_lineno = lineno


def main(argv=None):
    ap = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    ap.add_argument(
        "--fix-suggest",
        action="store_true",
        help="also print a guessed replacement code for each non-standard row, without editing the file",
    )
    ap.add_argument(
        "--placeholder-report",
        action="store_true",
        help="list every row whose Cost cell is an unresolved deferral, session-cross-checked; printed only, always exits 0 (see module docstring)",
    )
    ap.add_argument(
        "--split",
        metavar="FROM_ROW",
        type=int,
        help="print the S/A/V/C effort table for rows at or after FROM_ROW, plus parent-vs-worker spend (see module docstring); the main duplicate/outcome-code check still runs",
    )
    args = ap.parse_args(argv)

    with open(LEDGER, encoding="utf-8") as f:
        lines = f.readlines()

    if args.split is not None:
        print_split(lines, args.split)
        print()

    if args.placeholder_report:
        placeholder_rows = find_placeholder_rows(lines)
        if placeholder_rows:
            print("Unresolved placeholder-cost rows:")
            for lineno, session_id, cost_text in placeholder_rows:
                print(f"  line {lineno}: session={session_id!r} cost={cost_text!r}")
        else:
            print("ok: no unresolved placeholder-cost rows")
        return 0

    dup_sessions, bad_outcomes = check(lines)
    shifted = find_shifted_outcome_rows(lines)

    ok = True

    if shifted:
        ok = False
        print("Outcome cell starts with a number (cost shifted one column right):")
        for lineno, cost_cell, outcome_cell in shifted:
            print(f"  line {lineno}: cost={cost_cell!r} outcome={outcome_cell!r}")

    if dup_sessions:
        ok = False
        print("Duplicate session ids:")
        for sid, rows in dup_sessions.items():
            print(f"  {sid}:")
            for lineno, outcome, cost in rows:
                print(f"    line {lineno}: outcome={outcome!r} cost={cost!r}")

    if bad_outcomes:
        ok = False
        print("Non-standard outcome codes (must be exactly one of D, D-, F, X, N, Q):")
        for lineno, outcome, lesson in bad_outcomes:
            print(f"  line {lineno}: outcome={outcome!r}")
            if args.fix_suggest:
                print(f"    suggest: {guess_fix(lesson)}")

    if ok:
        print("ok: no duplicate session ids, no non-standard outcome codes")
        return 0
    return 1


if __name__ == "__main__":
    sys.exit(main())

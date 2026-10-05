#!/usr/bin/env python3
"""Scan every ciphers/*/NOTES.md whose status is open, partial or blocked and pull out the
folder's own named next step, so the backlog of written-but-unrun next steps is visible instead
of living only in prose nobody re-reads.

Built 26 Sept 2026 (OPTIMIZATION-2026-09-26.md section (c), "Quitting too early"): 63 of 111
open/partial target folders end with a written next step that no worker has run, because lanes
are opened from scout picks, not from that backlog. This tool writes NEXT-STEPS.tsv at the repo
root; `.claude/briefs/parent.md`'s lane-opening duty reads it and takes the top runnable row as
job 1 before spawning a scout.

Status extraction follows CLAUDE.md rule 5's vocabulary (open, partial, solved, closed-negative,
found-solved, blocked, offline-only), scanning down from the top of the file for the first line
that carries one -- either bare ("open", "blocked (fr.3984 nos.6, 8)") or behind a "Status:"/
"status:" label (the more common convention in this repository, e.g. "status: partial"), skipping
a leading title heading, blockquote marker or bullet. This is the same shape as
tools/near_check.py's STATUS_RE with one addition (the "status:" label), needed because
near_check.py's regex silently misses every "Status: X" line in the corpus (checked against
ciphers/eckert-1864/NOTES.md, ciphers/decode-9970-simancas-1527/NOTES.md and others while
building this tool) -- worth a follow-up to near_check.py, not fixed here since it is a separate
tool with its own tests.

The next-step sentence is the *last* paragraph or bullet in the file containing one of the
trigger phrases below, on the theory that a NOTES.md is appended to over time and the most
recent such paragraph is the live one; an earlier "next step" superseded by later work is not
re-surfaced. Blocker type and cost band are both guessed from keywords in that paragraph alone,
not from the whole file -- a cheap, inspectable heuristic, not a claim of certainty (a human or a
lane orchestrator reads the one line and can always open NOTES.md for the rest).

Fixed 26 Sept 2026 (NX-FIX, flagged by NX-UNBLOCK 19:16 on ciphers/vanbeuningen-dewitt-1657): a
NOTES.md that is appended to over time can carry a later dated section (e.g. a verifier's AUDIT.md-
backed key recovery) that never repeats the exact trigger phrase, while an earlier, now-superseded
paragraph still does -- a bare last-block-in-file-order scan then surfaces the stale paragraph
instead of the file's current state. `extract_next_step()` now tracks the most recent date it has
seen (a "<d> Sept[ember] 2026"-style date, whether in a "## ..., <date> (...)" heading or in an
ordinary paragraph) as it walks the file's blocks in order, and among the blocks carrying a
next-step trigger phrase prefers the one(s) stamped with the newest date seen so far, taking the
last such block if more than one shares that date (LIFO within a section, same as before). A file
with no date anywhere falls back to the previous whole-file "last matching block" behaviour
unchanged -- this is a strict refinement, not a new heuristic, so a NOTES.md with no dated
sections is scored exactly as before.

Fixed 27 Sept 2026 (NX-TRIAGE, CODEX-REVIEW-2026-09-27.md section 2): `classify_blocker()` and
`estimate_cost_band()` returned "runnable"/"S" for any text no keyword matched, including an EMPTY
next-step block (a target whose NOTES.md carries no next-step paragraph at all read as cheap
runnable work and sat at the top of a lane's job-1 pick, parent.md "Opening a lane"), and both were
called on `one_line()`'s already-truncated 200-character display text, so a blocker keyword sitting
past the truncation point was missed too. An empty or whitespace-only block now classifies
`needs-triage`/`?` instead of `runnable`/`S`, and both functions run on the full extracted block
before truncation; `one_line()`'s output is kept only for the TSV's display column. A
`next_step_full_len` column records the untruncated block's length. See `classify_blocker()`'s and
`estimate_cost_band()`'s own docstrings for what each must catch and must not block (CLAUDE.md
Usage 8a).

Fixed 3 Oct 2026 (TOOL-NS2, flagged by GAPS144 on ciphers/thurloe-printed): once a folder carries
rule 5's "## Remaining gaps" + "## Escalation" pair, the Escalation step bullets ("planned as the
cheapest next step") matched the prose triggers and the whole Escalation block was quoted as the
next step, burying the Verdict line that states the cheapest next step outright. `verdict_step()`
now reads that Verdict with tools/gaps_check.py's own parser (`last_section` + `parse_escalation`
on the LAST "## Escalation" section, falling back to a "Verdict:" line in the LAST "## Remaining
gaps" section), and when one exists it wins over every prose trigger. Classification for a
"parked" verdict also reads the Remaining gaps body, so its outside blockers (a LOCAL-QUEUE row, a
missing image) still set the blocker class. Must catch: a thurloe-shaped NOTES with both sections
-> next_step is the "Verdict: keep going: ...; cheapest next: ..." line. Must NOT change: a folder
with no Remaining gaps/Escalation sections (or sections with no Verdict line) keeps the prose next
step exactly as before. Both tested in tools/tests/test_next_steps.py.

Usage:
  tools/next_steps.py [--ciphers-dir ciphers] [--ledger LEDGER.md] [--near NEAR.md] [--out NEXT-STEPS.tsv]
  tools/next_steps.py --check     exit nonzero if NEXT-STEPS.tsv on disk is stale against the folders

--ciphers-dir, --ledger, --near and --out default to the real repository paths; all four exist so
the offline test can point the tool at temporary fixtures instead of the real repo.

Added 5 Oct 2026 (SYS1-HC, LANE-SYS1 job 2): `--hot-only [HOT-COLD.tsv]` prints the same TSV filtered to folders that
tools/hot_cold.py marks HOT (a key source on disk, or a pool member with one), to stdout only; it never writes --out,
so the default NEXT-STEPS.tsv output is byte-identical with or without the flag. It must NOT drop a HOT row or keep a
COLD/unlisted one (tools/tests/test_hot_cold.py::test_next_steps_hot_only_filters_and_default_unchanged).
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

STATUS_WORDS = ("open", "partial", "solved", "closed-negative", "found-solved", "blocked", "offline-only")
TARGET_STATUSES = ("open", "partial", "blocked")

STATUS_RE = re.compile(
    r'^[\s\-*>#]*(?:status:?\s*)?\b(' + '|'.join(sorted(STATUS_WORDS, key=len, reverse=True)) + r')\b',
    re.IGNORECASE,
)

# 'follow-up' is a trigger only when it heads a line or labels a clause (TOOL-NS1, 3 Oct 2026,
# flagged by GAPS136 on ciphers/decode-1411-hhsta-vienna-1600): the bare word also occurs in
# ordinary prose -- a cited blog title ("the 2017-10-07 Thomas Ernst follow-up") in a web-check
# sentence, or "- Follow-up 2017-10-07 (<url>)" naming a post -- and was surfaced as the folder's
# next step. Must catch: "Follow-up suggestions (one line each):", "Follow-up:", "## Follow-ups",
# "**Follow-up (not done):**", "Follow-ups (suggestions, not done):", "Follow-up for the next job:",
# "Suggested follow-ups (one line each, not run):".
# Must NOT block (i.e. must not fire on): "follow-up" mid-sentence, or heading a line but followed
# by anything other than an optional "suggestion(s)" / "for <...>" and then ':', '(', '**' or
# end of line. Every other trigger phrase is unchanged.
FOLLOW_UP_LABEL = (
    r'(?m:^[ \t>#*\-]*(?:\*\*)?(?:suggested\s+)?follow-ups?(?:\s+suggestions?|\s+for\b[^:\n]{0,40}(?=:))?'
    r'\s*(?::|\(|\*\*|$))'
)
NEXT_STEP_RE = re.compile(
    r'next step|next:|next job|for whoever picks this up|successor|' + FOLLOW_UP_LABEL,
    re.IGNORECASE,
)

MONTH_NUM = {
    "jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6,
    "jul": 7, "aug": 8, "sep": 9, "oct": 10, "nov": 11, "dec": 12,
}
DATE_RE = re.compile(
    r'\b(\d{1,2})\s+(' + '|'.join(MONTH_NUM) + r')[a-z]*\.?\s+(\d{4})\b',
    re.IGNORECASE,
)


WORK_YEAR_MIN = 2020  # a NOTES.md also cites the target's own historical date (1657, 1812, ...)
                       # in the same heading as the work date ("## ..., 22 December 1812"); only
                       # a year in this project's own working range is a section timestamp.


def latest_date(text):
    """The latest (year, month, day) *working* date (rule 6's "<d> Sept 2026" convention, year
    >= WORK_YEAR_MIN) this repository's own convention can find anywhere in `text`, or None. A
    historical date the section discusses (the target letter's own date, centuries earlier) is
    not a section timestamp and is excluded so it cannot be mistaken for one. Several qualifying
    dates in one block (a heading naming when it was written plus a date it discusses) take the
    latest, not the first, on the theory that a section's own timestamp is usually its most
    prominent or final date."""
    best = None
    for day, mon, year in DATE_RE.findall(text):
        if int(year) < WORK_YEAR_MIN:
            continue
        d = (int(year), MONTH_NUM[mon[:3].lower()], int(day))
        if best is None or d > best:
            best = d
    return best

# Order matters: the first pattern that matches wins (CLAUDE.md Usage 8a's own precedent list order).
BLOCKER_PATTERNS = (
    ("needs-image", re.compile(r'copy order|REQUEST\.md|not digiti[sz]ed|no image', re.IGNORECASE)),
    ("needs-key", re.compile(r'no key\b|below unicity|key source', re.IGNORECASE)),
    ("needs-person", re.compile(r'\bowner\b|LOCAL-QUEUE|\bASKS\b|HathiTrust page|\bJSTOR\b', re.IGNORECASE)),
    ("needs-edition", re.compile(r'check-solved|edition volume|\bedition\b', re.IGNORECASE)),
)

# The blocker classes a row needs a `parallel` action for (job WAIT-CHECK, 27 Sept 2026): the four
# genuinely-blocked kinds, never `runnable` or `needs-triage` (a row with no next step has nothing
# to run in parallel with either).
PARALLEL_BLOCKERS = frozenset(name for name, _ in BLOCKER_PATTERNS)

WHILE_WAITING_RE = re.compile(r'^#{1,6}\s*while waiting', re.IGNORECASE)
BULLET_RE = re.compile(r'^(?:[-*+]|\d+[.)])\s+(.*)$')

COST_L_RE = re.compile(r'full transcription', re.IGNORECASE)
COST_M_RE = re.compile(r'\bcrops?\b|\bpass(es)?\b|\bleaf\b|\balignment\b|\bkey\b|\batlas\b', re.IGNORECASE)
COST_S_RE = re.compile(r'\bgrep\b|\bcheck\b', re.IGNORECASE)

LEDGER_ROW_RE = re.compile(r'^\|\s*([^|]+?)\s*\|')


def first_status_word(text):
    """The first line matching rule 5's status vocabulary (bare or "status:"-labelled), or None."""
    for line in text.splitlines():
        m = STATUS_RE.match(line)
        if m:
            return m.group(1).lower()
    return None


def split_blocks(text):
    """Split a NOTES.md body into blank-line-separated blocks, each block's leading/trailing
    whitespace stripped; empty blocks dropped."""
    blocks = re.split(r'\n\s*\n', text)
    return [b.strip() for b in blocks if b.strip()]


def _is_heading(block):
    return block.lstrip().startswith('#')


def extract_next_step(text):
    """The next-step block from the file's newest dated section, or -- when no block anywhere
    carries a date -- the last block containing a next-step trigger phrase (the original
    whole-file behaviour), or "" if none match at all.

    Walks the file's blocks in order, tracking the newest date seen so far as a section marker
    -- a NOTES.md is appended to over time, so a later section's date supersedes an earlier
    one's. When the file has at least one dated markdown heading ("## ..., <date> (...)" is this
    repository's own convention), only heading blocks advance the tracker: a body paragraph
    that incidentally cites an earlier date (e.g. quoting when a cited AUDIT.md was written)
    must not walk the tracker backwards past the heading it actually sits under. A file with no
    dated heading anywhere falls back to treating any block's own date as a section marker, so a
    flat NOTES.md that dates its paragraphs directly (no "## " headings at all) still works.
    Every block that also matches a next-step trigger phrase is recorded together with the
    tracker's value at that point. Among the recorded candidates, prefers the one(s) stamped
    with the newest date found anywhere in the file, taking the last in file order when more
    than one block shares that date; when no candidate carries a date at all, takes the last
    candidate in file order, exactly as before this fix.
    """
    blocks = split_blocks(text)
    heading_anchored = any(_is_heading(b) and latest_date(b) is not None for b in blocks)

    candidates = []  # (date_or_None, block) in file order
    current_date = None
    for block in blocks:
        if not heading_anchored or _is_heading(block):
            d = latest_date(block)
            if d is not None:
                current_date = d
        if NEXT_STEP_RE.search(block):
            candidates.append((current_date, block))

    if not candidates:
        return ""

    dated = [c for c in candidates if c[0] is not None]
    pool = dated if dated else candidates
    newest = max(c[0] for c in pool) if dated else None
    match = ""
    for date, block in pool:
        if date == newest:
            match = block
    return match


def verdict_step(text):
    """(verdict_line, gaps_body) from rule 5's sections, parsed with tools/gaps_check.py's own
    helpers, or ("", "") when the file carries no Verdict line in its last Escalation (or last
    Remaining gaps) section. Imported lazily: gaps_check imports this module at load time."""
    import gaps_check as gc
    lines = gc.unfenced(text.splitlines())
    gaps_body = gc.last_section(lines, gc.GAPS_HEAD)
    esc_body = gc.last_section(lines, gc.ESC_HEAD)
    verdict = None
    if esc_body is not None:
        _, verdict = gc.parse_escalation(esc_body, [])
    if verdict is None and gaps_body is not None:
        for line in gaps_body:
            m = gc.VERDICT.match(line)
            if m:
                verdict = m.group("text").strip()
    if not verdict:
        return "", ""
    return "Verdict: " + verdict, "\n".join(gaps_body or [])


def extract_while_waiting(text):
    """The first bullet line of the newest '## While waiting' section in `text`, or "" when the
    file has no such section or the section carries no bullet.

    Job WAIT-CHECK (27 Sept 2026): a blocked target's next step often depends on an archive or a
    person, but the folder can still name a parallel action that depends on nobody -- written as
    its own '## While waiting' NOTES.md section, one bullet or one paragraph per action. "Newest" follows the same
    convention as `extract_next_step()`: a heading carrying a dated section timestamp wins over an
    undated one; among undated sections (or when none carry a date), the last one in file order
    wins, since a NOTES.md is appended to over time.
    """
    blocks = split_blocks(text)
    idxs = [i for i, b in enumerate(blocks) if _is_heading(b) and WHILE_WAITING_RE.match(b.strip())]
    if not idxs:
        return ""
    dated = [(latest_date(blocks[i]), i) for i in idxs]
    if any(d is not None for d, _ in dated):
        newest = max(d for d, i in dated if d is not None)
        section_idx = max(i for d, i in dated if d == newest)
    else:
        section_idx = idxs[-1]
    for block in blocks[section_idx + 1:]:
        if _is_heading(block):
            break
        for line in block.splitlines():
            m = BULLET_RE.match(line.strip())
            if m:
                return m.group(1).strip()
    # No bullet: take the section's first prose paragraph (which may share the heading's block when
    # no blank line follows the heading), unless it is marked done. RETRO-2026-10-04-acct1 P1: 13 of
    # 47 wait-only rows had a prose section the bullet-only reader could not see.
    tail = blocks[section_idx].strip().splitlines()[1:]
    for block in (["\n".join(tail)] if tail else []) + blocks[section_idx + 1:]:
        if _is_heading(block):
            break
        flat = " ".join(block.split())
        if flat and not flat.lower().startswith("[done"):
            return flat
    return ""


def one_line(text, limit=200):
    """Collapse a block to one line and cap it at `limit` characters, preferring the sentence
    that actually carries the trigger phrase over the whole (possibly long) paragraph."""
    if not text:
        return ""
    flat = re.sub(r'\s+', ' ', text).strip()
    sentences = re.split(r'(?<=[.!?])\s+', flat)
    for s in sentences:
        if NEXT_STEP_RE.search(s):
            flat = s.strip()
            break
    if len(flat) > limit:
        flat = flat[:limit - 1].rstrip() + "…"
    return flat


def classify_blocker(next_step_text):
    """The blocker type for a next-step block. What this must catch (CLAUDE.md Usage 8a): a row
    with no instruction at all -- an empty or whitespace-only block, meaning `extract_next_step()`
    found no next-step paragraph in the file -- classifies as `needs-triage`, never `runnable`,
    since a lane orchestrator reading `runnable` takes the row as ready-to-run job 1 (parent.md
    "Job 1 from the backlog") and there is nothing here to run. What it must NOT block: a short
    but real instruction with no blocker keyword in it (e.g. "run print_check on the decoded
    phrases") stays `runnable` -- brevity alone is not a reason to flag a row for triage, only the
    total absence of an instruction is (CODEX-REVIEW-2026-09-27.md section 2, NX-TRIAGE)."""
    if not next_step_text or not next_step_text.strip():
        return "needs-triage"
    for name, pat in BLOCKER_PATTERNS:
        if pat.search(next_step_text):
            return name
    return "runnable"


def estimate_cost_band(next_step_text):
    """The cost band for a next-step block. What this must catch: an empty or whitespace-only
    block (no instruction to price) bands as `?`, never the cheapest band `S` -- the same failure
    mode as `classify_blocker()` above, a missing instruction reading as the cheapest possible
    job. What it must NOT block: a short real instruction with no cost keyword in it still bands
    `S` (the existing fallback), since most cheap checks (a grep, a re-run) are genuinely short."""
    if not next_step_text or not next_step_text.strip():
        return "?"
    if COST_L_RE.search(next_step_text):
        return "L"
    if COST_M_RE.search(next_step_text):
        return "M"
    if COST_S_RE.search(next_step_text):
        return "S"
    return "S"


def near_targets(near_text):
    targets = set()
    for line in near_text.splitlines():
        if not line.startswith("|"):
            continue
        cell = line.split("|", 2)
        if len(cell) < 2:
            continue
        name = cell[1].strip().strip("`").strip("*")
        if name and name not in ("Target", "---") and not set(name) <= {"-"}:
            targets.add(name)
    return targets


def last_ledger_date(ledger_text, target):
    last = ""
    for line in ledger_text.splitlines():
        if target not in line:
            continue
        m = LEDGER_ROW_RE.match(line)
        if m and m.group(1) not in ("Date",) and not set(m.group(1)) <= {"-", " "}:
            last = m.group(1).strip()
    return last


def build_rows(ciphers_dir, ledger_text, near_text):
    rows = []
    for target in sorted(os.listdir(ciphers_dir)):
        notes_path = os.path.join(ciphers_dir, target, "NOTES.md")
        if not os.path.isfile(notes_path):
            continue
        text = open(notes_path, encoding="utf-8", errors="replace").read()
        status = first_status_word(text)
        if status not in TARGET_STATUSES:
            continue
        verdict, gaps_body = verdict_step(text)
        if verdict:
            # rule 5's Verdict line wins over Escalation text and older prose triggers (TOOL-NS2);
            # a "parked" verdict names no step itself, so its gap lines carry the blocker keywords.
            block = verdict
            # whole line, not one_line()'s trigger-sentence pick, so "keep going: N" is never cut off
            next_step = verdict if len(verdict) <= 200 else verdict[:199].rstrip() + "…"
            class_text = verdict + ("\n" + gaps_body if re.match(r"Verdict:\s*parked", verdict, re.I) else "")
        else:
            block = extract_next_step(text)
            next_step = one_line(block)
            class_text = block
        # Classify on the FULL extracted block, before one_line()'s truncation -- a blocker
        # keyword past the truncation limit (CODEX-REVIEW-2026-09-27.md section 2) must still be
        # caught, and an empty block must still classify needs-triage/? rather than runnable/S.
        blocker = classify_blocker(class_text)
        cost_band = estimate_cost_band(class_text)
        if blocker in PARALLEL_BLOCKERS:
            bullet = extract_while_waiting(text)
            parallel = one_line(bullet) if bullet else ""
        else:
            parallel = "--"
        row = {
            "folder": target,
            "status": status,
            "blocker": blocker,
            "cost_band": cost_band,
            "near_row": "y" if target in near_targets(near_text) else "n",
            "last_touched": last_ledger_date(ledger_text, target),
            "next_step": next_step,
            "parallel": parallel,
            "next_step_full_len": str(len(block)),
        }
        rows.append(row)
    return rows


# next_step_full_len appended rather than inserted, and `parallel` inserted right after next_step
# (job WAIT-CHECK, 27 Sept 2026) rather than appended after it: the only script reader,
# build_dashboard.py's load_next_steps(), zips the header row to each data row by header name
# (dict(zip(cols, cells))), so a column's position in the file does not matter to it or to any
# other TSV viewer that reads by header name; grepped tools/ and .claude/briefs/ for other readers
# -- none found, CODEX-REVIEW-2026-09-27.md section 2, U1(b).
COLUMNS = ("folder", "status", "blocker", "cost_band", "near_row", "last_touched", "next_step", "parallel", "next_step_full_len")


def render_tsv(rows):
    lines = ["\t".join(COLUMNS)]
    for r in rows:
        lines.append("\t".join(r[c] for c in COLUMNS))
    # needs-triage is always shown, even at 0, so the count cannot silently vanish from the
    # summary line the way an absent key from a plain Counter would (U1(c)).
    counts = {"needs-triage": 0}
    for r in rows:
        counts[r["blocker"]] = counts.get(r["blocker"], 0) + 1
    summary = " ".join(f"{k}={v}" for k, v in sorted(counts.items()))
    lines.append(f"# {len(rows)} rows -- {summary}")
    return "\n".join(lines) + "\n"


def wait_only_rows(rows):
    """The blocked rows (one of the four PARALLEL_BLOCKERS) whose `parallel` cell is empty --
    a target that is only waiting, with no action anyone else can take in the meantime."""
    blocked = [r for r in rows if r["blocker"] in PARALLEL_BLOCKERS]
    missing = [r for r in blocked if not r["parallel"]]
    return blocked, missing


def print_wait_only_summary(rows):
    blocked, missing = wait_only_rows(rows)
    print(f"wait-only: {len(missing)} of {len(blocked)} blocked targets have no parallel action")
    for r in missing:
        print(f"{r['folder']} | {r['blocker']}")


def hot_folders(path):
    """HOT folder names from tools/hot_cold.py's HOT-COLD.tsv (columns folder, hot_cold, ...; '#' comment lines)."""
    lines = [l.rstrip("\n").split("\t") for l in open(path, encoding="utf-8") if l.strip() and not l.startswith("#")]
    if not lines or "folder" not in lines[0] or "hot_cold" not in lines[0]:
        return set()
    fi, hi = lines[0].index("folder"), lines[0].index("hot_cold")
    return {r[fi] for r in lines[1:] if len(r) > hi and r[hi] == "HOT"}


def hot_only_rows(rows, hot):
    """--hot-only filter: keep a NEXT-STEPS row only when its folder is HOT; order unchanged."""
    return [r for r in rows if r["folder"] in hot]


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"))
    ap.add_argument("--ledger", default=os.path.join(ROOT, "LEDGER.md"))
    ap.add_argument("--near", default=os.path.join(ROOT, "NEAR.md"))
    ap.add_argument("--out", default=os.path.join(ROOT, "NEXT-STEPS.tsv"))
    ap.add_argument("--check", action="store_true", help="exit nonzero if --out is stale")
    ap.add_argument("--wait-only", action="store_true",
                     help="print only the blocked rows with no parallel action (folder | blocker), for the "
                          "check-in and the retrospective; exits 0 always (this is a report, not a staleness check)")
    ap.add_argument("--hot-only", nargs="?", const=os.path.join(ROOT, "HOT-COLD.tsv"), default=None, metavar="HOT-COLD.tsv",
                    help="print the NEXT-STEPS rows (header + TSV) for HOT folders only, reading tools/hot_cold.py's "
                         "HOT-COLD.tsv (default path at the repo root); writes nothing and leaves --out untouched, so "
                         "the default output is unchanged. Exit 2 if the HOT-COLD file is missing")
    args = ap.parse_args()

    ledger_text = open(args.ledger, encoding="utf-8", errors="replace").read() if os.path.exists(args.ledger) else ""
    near_text = open(args.near, encoding="utf-8", errors="replace").read() if os.path.exists(args.near) else ""
    rows = build_rows(args.ciphers_dir, ledger_text, near_text)

    if args.hot_only:
        if not os.path.exists(args.hot_only):
            print(f"{args.hot_only} missing; run python3 tools/hot_cold.py first", file=sys.stderr)
            return 2
        hot = hot_folders(args.hot_only)
        sys.stdout.write(render_tsv(hot_only_rows(rows, hot)))
        return 0

    if args.wait_only:
        _, missing = wait_only_rows(rows)
        for r in missing:
            print(f"{r['folder']} | {r['blocker']}")
        return 0

    fresh = render_tsv(rows)
    needs_triage = sum(1 for r in rows if r["blocker"] == "needs-triage")

    if args.check:
        current = open(args.out, encoding="utf-8").read() if os.path.exists(args.out) else None
        if current != fresh:
            print(f"STALE: {args.out} does not match the folders on disk; re-run without --check to refresh.")
            print_wait_only_summary(rows)
            return 1
        print(f"OK: {args.out} is current ({len(rows)} rows, needs-triage={needs_triage}).")
        print_wait_only_summary(rows)
        return 0

    with open(args.out, "w", encoding="utf-8") as f:
        f.write(fresh)
    print(f"wrote {args.out}: {len(rows)} rows, needs-triage={needs_triage}")
    print_wait_only_summary(rows)
    return 0


if __name__ == "__main__":
    sys.exit(main())

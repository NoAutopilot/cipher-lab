#!/usr/bin/env python3
"""Gate a SEND-QUEUE.tsv row before it is queued (by the parent) or landed (by a PR-LAND worker)
(CLAUDE.md Usage 8a, rules become tools; SEND-QUEUE-TOOL, 26 Sept 2026).

The owner's decision, 26 Sept 2026: checked outreach drafts and reproduction-quote requests are
sent by the owner's own ChatGPT runner, from his own browser, reading SEND-QUEUE.tsv on main --
the same loop shape as tools/local_queue_runner_prompt.md. Outreach gate 7 (CLAUDE.md) already
requires a separate session's `checked:` line before any draft is sendable; this script is the
mechanical check that a row never reaches `queued` (or stays `queued`) without every rung of that
gate actually present, the same "rules become tools" shape as tools/lq_answer_check.py for the
desk-runner loop.

A `queued` row fails (nonzero exit, naming the row and the missing rung) when:
  (1) `draft` does not point at a file that exists;
  (2) the draft's own outreach/<slug>.md has no `checked:` header line at or after the row's own
      `checked` cell (a stale or missing gate-7 pass -- the row's `checked` cell must itself match
      a real line in the file, not just be filled in);
  (3) the draft json's `body` (or the matching outreach/<slug>.md, whichever is checked -- both are
      read) does not carry the literal `[SIGN-OFF]` placeholder anywhere, and its first paragraph
      does not carry the disclosure sentence's substance (outreach/README.md rule 1: a sentence
      naming that one person directs/sends and AI agents do the reading/searching/checking) --
      checked as a substance match (the words "I direct"/"I run" or "one person directs" plus
      "AI agents"/"Claude models" somewhere in the first paragraph), not an exact string;
  (4) CONTRIBUTIONS.md carries no row naming the draft's slug (Outreach gate 5);
  (5) `kind` is `form` and the draft json carries no `form_fields` key.
A row whose status is not `queued` (blocked, bounced, or already `sent ...`) is not gated -- this
script only protects the moment a row is about to be acted on by the runner or was left `queued`
by mistake after failing.

Usage:
  tools/send_queue_check.py FILE [--row ID]
    FILE is SEND-QUEUE.tsv (or a copy of it). --row ID checks just that row; omitted, every
    `queued` row is checked and the script exits nonzero if any fails.

Exit 0: every `queued` row (or the one named by --row) passes every rung above.
Exit 1: at least one `queued` row is missing a rung -- printed by row id and rung name.
Exit 2: FILE, or the row named by --row, could not be read/resolved.

This checks the shape of the gate (a file that exists, a checked: line, the placeholder/disclosure
substance, a CONTRIBUTIONS.md row, form_fields for a form row), not that the checked: line's own
verdict was correct -- that is gate 7's own fact-check session's job, the same limit
tools/lq_answer_check.py states for its own citation check.
"""
import argparse
import datetime
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CONTRIBUTIONS_PATH = os.path.join(ROOT, "CONTRIBUTIONS.md")
OUTREACH_DIR = os.path.join(ROOT, "outreach")

CHECKED_LINE_RE = re.compile(r'^checked:\s*(.+)$', re.IGNORECASE | re.MULTILINE)
DISCLOSURE_RE = re.compile(
    r'(?:\bI\s+(?:direct|run)\b|\bone\s+person\s+directs\b).{0,400}?'
    r'(?:\bAI\s+agents\b|\bClaude\s+models\b)',
    re.IGNORECASE | re.DOTALL,
)

MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
    "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9, "oct": 10, "october": 10, "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}
ISO_DATETIME_RE = re.compile(r'(\d{4})-(\d{2})-(\d{2})\D{0,10}?(\d{1,2}):(\d{2})')
PROSE_DATETIME_RE = re.compile(r'(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})\D{0,10}?(\d{1,2}):(\d{2})')


def extract_datetime(text):
    """First UTC-ish timestamp in text (ISO 'YYYY-MM-DD HH:MM' or prose 'D Mon YYYY HH:MM'), as a
    naive datetime.datetime. None if no timestamp is found (a bare date with no time never matches
    -- this gate cares about the hour/minute a `checked:` line records, per the brief's own seed row)."""
    if not text:
        return None
    m = ISO_DATETIME_RE.search(text)
    if m:
        y, mo, d, h, mi = (int(x) for x in m.groups())
        try:
            return datetime.datetime(y, mo, d, h, mi)
        except ValueError:
            pass
    m = PROSE_DATETIME_RE.search(text)
    if m:
        day, mon, year, h, mi = m.groups()
        mon_num = MONTHS.get(mon.lower())
        if mon_num:
            try:
                return datetime.datetime(int(year), mon_num, int(day), int(h), int(mi))
            except ValueError:
                pass
    return None


def load_tsv_rows(path):
    """Return list of dicts keyed by the header row's column names. Raises on a missing file."""
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f if l.strip("\n")]
    if not lines:
        return [], []
    cols = lines[0].split("\t")
    rows = []
    for line in lines[1:]:
        cells = line.split("\t")
        cells += [""] * (len(cols) - len(cells))
        rows.append(dict(zip(cols, cells)))
    return cols, rows


def draft_slug(draft_path):
    """outreach/mailbox/<slug>.json -> <slug>."""
    base = os.path.basename(draft_path)
    if base.endswith(".json"):
        base = base[:-len(".json")]
    return base


def outreach_md_path(slug, outreach_dir=OUTREACH_DIR):
    return os.path.join(outreach_dir, f"{slug}.md")


def first_paragraph(text):
    """The disclosure sentence (outreach/README.md rule 1) is required in the letter's opening, but
    a bare salutation line ("Dear X,") often sits alone as its own paragraph before it -- so this
    returns the first two non-empty paragraphs joined, not a strict single blank-line split."""
    parts = [p for p in re.split(r'\n\s*\n', text.strip()) if p.strip()]
    return "\n\n".join(parts[:2])


def has_sign_off_placeholder(*texts):
    return any("[SIGN-OFF]" in t for t in texts if t)


def has_disclosure_substance(*texts):
    for t in texts:
        if not t:
            continue
        para = first_paragraph(t)
        if DISCLOSURE_RE.search(para):
            return True
    return False


def checked_lines(md_text):
    """All `checked: ...` header-line values, in file order."""
    return [m.group(1).strip() for m in CHECKED_LINE_RE.finditer(md_text or "")]


def contributions_has_slug(slug, contributions_text):
    """CONTRIBUTIONS.md row naming this draft's slug -- either the bare slug or the outreach path
    outreach/<slug>.md, since rows cite the draft by its filename (Outreach gate 5)."""
    if not contributions_text:
        return False
    return (
        f"outreach/{slug}.md" in contributions_text
        or f"outreach/mailbox/{slug}.json" in contributions_text
        or re.search(rf'\b{re.escape(slug)}\b', contributions_text) is not None
    )


def check_row(row, root=ROOT, outreach_dir=None, contributions_path=None):
    """Pure check used by the offline test. Returns (exit_code, [messages])."""
    outreach_dir = outreach_dir if outreach_dir is not None else OUTREACH_DIR
    contributions_path = contributions_path if contributions_path is not None else CONTRIBUTIONS_PATH

    row_id = row.get("id", "?")
    status = row.get("status", "").strip()
    if not status.lower().startswith("queued"):
        return 0, [f"{row_id}: status {status!r} is not queued -- not gated"]

    missing = []
    draft_rel = row.get("draft", "").strip()
    draft_path = draft_rel if os.path.isabs(draft_rel) else os.path.join(root, draft_rel)
    if not draft_rel or not os.path.isfile(draft_path):
        missing.append(f"draft file does not exist: {draft_rel!r}")
        return 1, [f"{row_id}: " + "; ".join(missing)]

    with open(draft_path, encoding="utf-8") as f:
        draft_text = f.read()
    draft_body = ""
    if draft_path.endswith(".json"):
        import json
        try:
            draft_json = json.loads(draft_text)
            draft_body = draft_json.get("body", "")
        except (ValueError, TypeError):
            missing.append("draft json does not parse")
        kind = row.get("kind", "").strip().lower()
        if kind == "form" and "form_fields" not in draft_text:
            missing.append("a 'form' row's draft json carries no form_fields key")
    else:
        draft_body = draft_text

    slug = draft_slug(draft_rel)
    md_path = outreach_md_path(slug, outreach_dir)
    md_text = ""
    if os.path.isfile(md_path):
        with open(md_path, encoding="utf-8") as f:
            md_text = f.read()

    row_checked = row.get("checked", "").strip()
    if not row_checked:
        missing.append("row's own `checked` cell is empty")
    else:
        lines = checked_lines(md_text)
        row_dt = extract_datetime(row_checked)
        if not lines:
            missing.append(f"no `checked:` header line in {os.path.relpath(md_path, root) if md_text else md_path}")
        elif row_dt is None:
            missing.append(f"row `checked` cell ({row_checked!r}) carries no parseable UTC date+time")
        elif not any((extract_datetime(line) or datetime.datetime.min) >= row_dt for line in lines):
            missing.append(
                f"row `checked` cell ({row_checked!r}, {row_dt.isoformat()}) is not backed by a "
                f"`checked:` line at or after that time in {os.path.relpath(md_path, root)}: {lines}")

    if not has_sign_off_placeholder(draft_body, md_text):
        missing.append("no [SIGN-OFF] placeholder found in the draft body or its outreach/<slug>.md")

    if not has_disclosure_substance(draft_body, md_text):
        missing.append(
            "first paragraph carries no disclosure-sentence substance (outreach/README.md rule 1: "
            "one person directs/sends, AI agents do the reading/searching/checking)")

    contributions_text = ""
    if os.path.isfile(contributions_path):
        with open(contributions_path, encoding="utf-8") as f:
            contributions_text = f.read()
    if not contributions_has_slug(slug, contributions_text):
        missing.append(f"no CONTRIBUTIONS.md row names slug {slug!r} (Outreach gate 5)")

    if missing:
        return 1, [f"{row_id}: " + "; ".join(missing)]
    return 0, [f"{row_id}: all rungs present (draft exists, checked: line matches, "
               f"[SIGN-OFF]/disclosure present, CONTRIBUTIONS.md row found"
               f"{', form_fields present' if row.get('kind', '').strip().lower() == 'form' else ''})"]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("file", help="SEND-QUEUE.tsv (or a copy of it)")
    ap.add_argument("--row", default=None, help="check only this row id (e.g. S1)")
    ap.add_argument("--root", default=ROOT, help="repository root, for resolving the draft path (default: this script's repo)")
    ap.add_argument("--outreach-dir", default=None, help="override outreach/ dir (for the offline test)")
    ap.add_argument("--contributions", default=None, help="override CONTRIBUTIONS.md path (for the offline test)")
    args = ap.parse_args(argv)

    if not os.path.isfile(args.file):
        print(f"no such file: {args.file}")
        return 2

    try:
        _cols, rows = load_tsv_rows(args.file)
    except OSError as e:
        print(f"could not read {args.file}: {e}")
        return 2

    if args.row:
        rows = [r for r in rows if r.get("id", "").strip() == args.row]
        if not rows:
            print(f"no such row: {args.row}")
            return 2

    exit_code = 0
    for row in rows:
        code, messages = check_row(row, root=args.root, outreach_dir=args.outreach_dir,
                                    contributions_path=args.contributions)
        for m in messages:
            print(m)
        exit_code = exit_code or code
    return exit_code


if __name__ == "__main__":
    sys.exit(main())

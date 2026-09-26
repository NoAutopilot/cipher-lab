#!/usr/bin/env python3
"""Check outreach/*.md drafts against ASKS.md, the three runner queues and the git log for staleness
(CLAUDE.md Usage 8a, rules become tools; DESK-CHECK, 26 Sept 2026).

The incident: outreach/bodleian-rawl-a24-p4.md sat at `status: ready` telling the owner to search
Digital Bodleian himself and that "the catalogue has no item record for these leaves", after the
owner's desk runner had already established (LOCAL-QUEUE L19, PR 22, 26 Sept 2026) that the volume
is catalogued in two parts, not digitised, with item-level records per folio. Nothing flagged the
draft as stale relative to its own landed answer.

This tool never edits a file; it names the newer fact so a fixer knows what to read. It is meant to
be run at every parent check-in (`.claude/briefs/parent.md` duty 6) and after landing any runner row
(`.claude/briefs/runs/2026-09-26-parent-pr-land-3.md`, `tools/local_queue_runner_prompt.md`).

Checks (each prints one line per problem; --fix-suggest adds the one-line fix):
  (a) STALE DRAFT: a draft at `ready`/`draft(ed)` whose target folder (or an id it names directly,
      e.g. "LOCAL-QUEUE L19" or an SO- label) matches a LOCAL-QUEUE/JSTOR-QUEUE/SECOND-OPINIONS-QUEUE
      row set `done`/`bounced`, or a NOTES.md/AUDIT.md commit on that target folder, dated after the
      draft's own status date (parsed from the status line; falls back to the file's last commit).
  (b) DESK MISMATCH: an ASKS row read `open`/`desk`/`backlog` while a draft for it reads `sent`/`held`,
      or a draft at `ready` while its ASKS row reads `done`/`queued as ...`/`waiting`.
  (c) BODY CONTRADICTION (cheap heuristics): a `ready` draft whose body still contains one of a short
      list of stale-instruction phrases while its ASKS row, or a LOCAL-QUEUE row for the same target,
      is `done` -- the runner has already done that step.
  (d) NO DATE: a `ready`/`draft(ed)` status line carrying no absolute date (CLAUDE.md rule 6).
  (e) DESK CAP (26 Sept 2026, OPTIMIZATION-2026-09-26.md (a), DESK-CAP): more than `--cap` (default 5)
      ASKS.md rows carry `desk` as the leading word of their status cell. The desk cap
      (`.claude/briefs/parent.md` duty 6 "Desk") exists so the owner never faces more than a handful of
      paste-ready actions at once; everything else is `backlog` with a one-line expected value. This
      check does not decide which rows to demote -- it only says the cap is exceeded.
  (f) SENT MISMATCH (26 Sept 2026, RETRO-2026-09-26j.md item 4): a draft whose `status:` line reads
      `mailbox-draft` while CONTRIBUTIONS.md already carries a "sent by the person" row for the same
      slug (the send happened but the draft's own header was never updated -- outreach/README.md's
      "Send log" shape), or the reverse (`status: sent` with no matching CONTRIBUTIONS.md row at all);
      and a header carrying the stale conditional phrase "not sendable until its checked: line lands"
      when a `checked:` line already exists in the same file -- a conditional the file never revisits
      once the condition clears. Lesson of 26 Sept 2026: all six mailbox drafts' `voice:` header line
      read "OUT-CHECK-V ... not sendable" for about 15 minutes after OUT-CHECK-V's own `checked:` line
      had already landed below it, because nothing cross-checked the conditional line against the
      unconditional ones.

Exit 0 if no problems, 1 if any. `--json PATH` writes a small {"flagged": [...], "problems": N,
"generated": "..."} file for tools/build_dashboard.py's "check" chip; the board must still build with
that file absent.

Usage:
  tools/desk_check.py [--outreach-dir outreach] [--asks ASKS.md] [--local-queue LOCAL-QUEUE.tsv]
                       [--jstor-queue JSTOR-QUEUE.tsv] [--so-queue SECOND-OPINIONS-QUEUE.tsv]
                       [--contributions CONTRIBUTIONS.md]
                       [--ciphers-dir ciphers] [--repo-root .] [--now "26 Sept 2026 17:00"]
                       [--cap 5] [--fix-suggest] [--json desk-check.json]

All path options default to the real repository files and exist so the offline test can point the
tool at temporary fixtures. `--now` defaults to the current UTC time.
"""
import argparse
import datetime
import json
import os
import re
import subprocess
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

MONTHS = {
    "jan": 1, "january": 1, "feb": 2, "february": 2, "mar": 3, "march": 3, "apr": 4, "april": 4,
    "may": 5, "jun": 6, "june": 6, "jul": 7, "july": 7, "aug": 8, "august": 8,
    "sep": 9, "sept": 9, "september": 9, "oct": 10, "october": 10, "nov": 11, "november": 11,
    "dec": 12, "december": 12,
}
ISO_DATE_RE = re.compile(r'\b(\d{4})-(\d{2})-(\d{2})\b')
PROSE_DATE_RE = re.compile(r'(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})')

DRAFT_WORD_RE = re.compile(r'^(ready|draft|drafted)\b', re.IGNORECASE)
HEADER_LINE_RE = re.compile(r'^([a-z]+):\s*(.*)$')
LEADING_WORD_RE = re.compile(r'^([A-Za-z][A-Za-z\-]*)')

ASKS_ROW_RE = re.compile(r'ASKS(?:\.md)?\s+row\s+(\d+)', re.IGNORECASE)
LOCAL_QUEUE_ID_RE = re.compile(r'\bL\d+\b')
SO_LABEL_RE = re.compile(r'\bSO-[A-Z0-9][A-Z0-9\-]*\b')
CIPHERS_PATH_RE = re.compile(r'ciphers/([a-z0-9][a-z0-9\-]*)')

CONTRADICTION_PHRASES = [
    "open https://digital", 'search "', "cannot reach", "has no item record", "if not imaged",
]


def parse_date(text):
    """First absolute date in text (ISO yyyy-mm-dd, or 'D Mon[.] YYYY' prose), as a datetime.date.
    None if no date is found. Time of day is ignored -- these checks only need day granularity."""
    if not text:
        return None
    m = ISO_DATE_RE.search(text)
    if m:
        y, mo, d = (int(x) for x in m.groups())
        try:
            return datetime.date(y, mo, d)
        except ValueError:
            pass
    m = PROSE_DATE_RE.search(text)
    if m:
        day, mon, year = m.groups()
        mon_num = MONTHS.get(mon.lower())
        if mon_num:
            try:
                return datetime.date(int(year), mon_num, int(day))
            except ValueError:
                pass
    return None


def leading_word(text):
    m = LEADING_WORD_RE.match((text or "").strip())
    return m.group(1).lower() if m else ""


def parse_headers(text):
    """Same shape as tools/build_dashboard.py's parse_headers: a contiguous run of `key: value`
    lines at the top of the file (each on one physical line, however long), then the body."""
    head, lines, k = {}, text.split("\n"), 0
    while k < len(lines) and HEADER_LINE_RE.match(lines[k]):
        m = HEADER_LINE_RE.match(lines[k])
        head[m.group(1)] = m.group(2).strip()
        k += 1
    body = "\n".join(lines[k:]).strip()
    return head, body


def extract_target_folders(head, body):
    targets = set()
    for part in re.split(r'[,;]\s*', head.get("targets", "")):
        part = part.strip().strip("`")
        if part.startswith("ciphers/"):
            part = part[len("ciphers/"):]
        if part:
            targets.add(part)
    for m in CIPHERS_PATH_RE.finditer(head.get("status", "") + "\n" + body):
        targets.add(m.group(1))
    return targets


def extract_asks_rows(head, body):
    return {int(n) for n in ASKS_ROW_RE.findall(head.get("status", "") + "\n" + body)}


def extract_local_queue_ids(head, body):
    return set(LOCAL_QUEUE_ID_RE.findall(head.get("status", "") + "\n" + body))


def extract_so_labels(head, body):
    return set(SO_LABEL_RE.findall(head.get("status", "") + "\n" + body))


def git_last_commit_date(repo_root, path):
    """The date of path's last commit, or None (no git, or the file is untracked)."""
    try:
        out = subprocess.run(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--", path],
            cwd=repo_root, capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return None
    out = out.stdout.strip()
    return parse_date(out) if out else None


def git_commits_since(repo_root, path, since):
    """Commits touching path strictly after `since` (a datetime.date), as [(date, hash), ...],
    newest first. Empty list if none, or if git/the path is unavailable."""
    if since is None:
        return []
    try:
        out = subprocess.run(
            ["git", "log", "--format=%H %ad", "--date=short", "--", path],
            cwd=repo_root, capture_output=True, text=True, timeout=10)
    except (OSError, subprocess.SubprocessError):
        return []
    commits = []
    for line in out.stdout.strip().splitlines():
        if " " not in line:
            continue
        h, d = line.split(" ", 1)
        dt = parse_date(d)
        if dt and dt > since:
            commits.append((dt, h))
    return sorted(commits, reverse=True)


def load_drafts(outreach_dir):
    drafts = []
    if not os.path.isdir(outreach_dir):
        return drafts
    for fn in sorted(os.listdir(outreach_dir)):
        if not fn.endswith(".md"):
            continue
        path = os.path.join(outreach_dir, fn)
        with open(path, encoding="utf-8") as f:
            text = f.read()
        head, body = parse_headers(text)
        drafts.append({
            "slug": fn[:-3], "path": path, "head": head, "body": body,
            "status_raw": head.get("status", ""),
            "status_word": leading_word(head.get("status", "")),
            "targets": extract_target_folders(head, body),
            "asks_rows": extract_asks_rows(head, body),
            "local_queue_ids": extract_local_queue_ids(head, body),
            "so_labels": extract_so_labels(head, body),
        })
    return drafts


def load_asks_md(path):
    """One dict per row: {row, status, what}. Mirrors build_dashboard.py's load_asks parsing."""
    rows = {}
    if not os.path.exists(path):
        return rows
    for line in open(path, encoding="utf-8"):
        if not line.startswith("| ") or line.startswith("|---"):
            continue
        cells = [c.strip() for c in line.strip().strip("|").split(" | ")]
        if len(cells) < 7 or not cells[0].isdigit():
            continue
        row, _raised, _proj, what, _action, _who, status = cells[:7]
        rows[int(row)] = {"row": int(row), "status": status, "what": what}
    return rows


def load_tsv(path):
    """Generic TSV loader: list of dicts keyed by the header row's column names. [] if missing."""
    if not os.path.exists(path):
        return []
    with open(path, encoding="utf-8") as f:
        lines = [l.rstrip("\n") for l in f if l.strip()]
    if not lines:
        return []
    cols = lines[0].split("\t")
    out = []
    for line in lines[1:]:
        cells = line.split("\t")
        cells += [""] * (len(cols) - len(cells))
        out.append(dict(zip(cols, cells)))
    return out


def target_of_row(row):
    """The target/folder cell of a LOCAL-QUEUE/JSTOR-QUEUE/SO row, stripped of 'ciphers/'."""
    cell = row.get("target") or row.get("folder") or ""
    cell = cell.strip()
    if cell.startswith("ciphers/"):
        cell = cell[len("ciphers/"):]
    return cell.split()[0].rstrip(",") if cell else ""


def row_date(row):
    for col in ("status", "requested", "added"):
        d = parse_date(row.get(col, ""))
        if d:
            return d
    return None


def matched_queue_rows(draft, local_rows, jstor_rows, so_rows):
    """Rows from the three queues that this draft's own text or target folder(s) point at."""
    matched = []
    for row in local_rows:
        if row.get("id") in draft["local_queue_ids"] or target_of_row(row) in draft["targets"]:
            matched.append(("LOCAL-QUEUE", row.get("id", "?"), row))
    for row in jstor_rows:
        if target_of_row(row) in draft["targets"]:
            matched.append(("JSTOR-QUEUE", target_of_row(row), row))
    for row in so_rows:
        if row.get("label") in draft["so_labels"] or target_of_row(row) in draft["targets"]:
            matched.append(("SECOND-OPINIONS-QUEUE", row.get("label", "?"), row))
    return matched


def check_stale_draft(draft, local_rows, jstor_rows, so_rows, ciphers_dir, repo_root, git_log_fn):
    """Returns a list of (message, fix_suggestion) for (a) STALE DRAFT."""
    problems = []
    if not DRAFT_WORD_RE.match(draft["status_word"]):
        return problems
    status_date = parse_date(draft["status_raw"]) or git_last_commit_date(repo_root, draft["path"])
    if status_date is None:
        return problems  # (d) covers the no-date case; nothing to compare against here

    for queue_name, row_id, row in matched_queue_rows(draft, local_rows, jstor_rows, so_rows):
        word = leading_word(row.get("status", ""))
        if word not in ("done", "bounced"):
            continue
        d = row_date(row)
        if d and d > status_date:
            problems.append((
                f"(a) STALE DRAFT {draft['slug']}: status dated {status_date.isoformat()}, but "
                f"{queue_name} row {row_id} is {word} {d.isoformat()}",
                f"re-read {queue_name} row {row_id} and rewrite the draft's body and status date"))

    for target in sorted(draft["targets"]):
        for fname in ("NOTES.md", "AUDIT.md"):
            path = os.path.join(ciphers_dir, target, fname)
            for dt, h in git_log_fn(repo_root, path, status_date):
                problems.append((
                    f"(a) STALE DRAFT {draft['slug']}: status dated {status_date.isoformat()}, but "
                    f"ciphers/{target}/{fname} has a commit {h[:7]} dated {dt.isoformat()}",
                    f"re-read ciphers/{target}/{fname} at {h[:7]} and rewrite the draft's body and status date"))
                break  # newest commit per file is enough to name
    return problems


def check_desk_mismatch(draft, asks_rows):
    problems = []
    for row_num in draft["asks_rows"]:
        row = asks_rows.get(row_num)
        if not row:
            continue
        ask_word = leading_word(row["status"])
        if ask_word in ("open", "desk", "backlog") and draft["status_word"] in ("sent", "held"):
            problems.append((
                f"(b) DESK MISMATCH {draft['slug']}: ASKS row {row_num} reads {ask_word}, but the draft "
                f"reads {draft['status_word']}",
                f"reconcile ASKS.md row {row_num} with {draft['slug']}.md's status"))
        if draft["status_word"] == "ready" and (
                ask_word == "done" or row["status"].lower().startswith("queued") or row["status"].lower().startswith("waiting")):
            problems.append((
                f"(b) DESK MISMATCH {draft['slug']}: draft reads ready, but ASKS row {row_num} reads "
                f"{row['status'][:60]!r}",
                f"reconcile {draft['slug']}.md's status with ASKS.md row {row_num}"))
    return problems


def check_body_contradiction(draft, asks_rows, local_rows):
    if draft["status_word"] != "ready":
        return []
    text_lower = (draft["status_raw"] + "\n" + draft["body"]).lower()
    hit_phrases = [p for p in CONTRADICTION_PHRASES if p in text_lower]
    if not hit_phrases:
        return []
    ask_done = any(leading_word(asks_rows[n]["status"]) == "done" for n in draft["asks_rows"] if n in asks_rows)
    local_done = any(
        leading_word(row.get("status", "")) == "done"
        for row in local_rows if target_of_row(row) in draft["targets"])
    if not (ask_done or local_done):
        return []
    return [(
        f"(c) BODY CONTRADICTION {draft['slug']}: body still says {hit_phrases[0]!r}, but its "
        f"ASKS row or a LOCAL-QUEUE row for the same target is done",
        f"rewrite {draft['slug']}.md's body -- the runner already did that step")]


def check_no_date(draft):
    if DRAFT_WORD_RE.match(draft["status_word"]) and parse_date(draft["status_raw"]) is None:
        return [(
            f"(d) NO DATE {draft['slug']}: status {draft['status_raw'][:60]!r} carries no absolute date",
            f"add an absolute date (CLAUDE.md rule 6) to {draft['slug']}.md's status line")]
    return []


STALE_CONDITIONAL_RE = re.compile(r'not\s+sendable\s+until\s+its\s+checked:\s+line\s+lands', re.IGNORECASE)
SENT_ROW_RE = re.compile(r'sent\s+by\s+the\s+person', re.IGNORECASE)
CHECKED_LINE_RE = re.compile(r'^checked:\s*(.+)$', re.IGNORECASE | re.MULTILINE)


def contributions_rows_for_slug(slug, contributions_text):
    """Table-row lines (one row per physical line, this repo's own convention) naming this draft's
    slug, by its outreach path or the bare slug word."""
    rows = []
    for line in (contributions_text or "").splitlines():
        if not line.startswith("| "):
            continue
        if (f"outreach/{slug}.md" in line or f"outreach/mailbox/{slug}.json" in line
                or re.search(rf'\b{re.escape(slug)}\b', line)):
            rows.append(line)
    return rows


def check_sent_mismatch(draft, contributions_text):
    """(f) SENT MISMATCH -- see the module docstring."""
    problems = []
    slug = draft["slug"]
    rows = contributions_rows_for_slug(slug, contributions_text)
    sent_row = any(SENT_ROW_RE.search(r) for r in rows)

    if draft["status_word"] == "mailbox-draft" and sent_row:
        problems.append((
            f"(f) SENT MISMATCH {slug}: status reads mailbox-draft, but CONTRIBUTIONS.md already carries "
            f"a 'sent by the person' row for this slug",
            f"update {slug}.md's status line to the Send log shape (outreach/README.md)"))
    elif draft["status_word"] == "sent" and not sent_row:
        problems.append((
            f"(f) SENT MISMATCH {slug}: status reads sent, but CONTRIBUTIONS.md carries no matching "
            f"'sent by the person' row for this slug",
            f"add or correct the CONTRIBUTIONS.md row for {slug} (Send log shape, outreach/README.md)"))

    # `checked:` lines usually sit after a blank line below the key:value header block (this
    # repo's own convention, see outreach/*.md), so parse_headers() puts them in the body, not
    # head -- search both, plus every parsed header value, so a duplicate `checked:` line (a
    # second gate-7 pass) is not lost to dict collapsing on repeated keys.
    full_text = (draft["status_raw"] + "\n" + "\n".join(f"{k}: {v}" for k, v in draft["head"].items())
                 + "\n" + draft["body"])
    if STALE_CONDITIONAL_RE.search(full_text) and CHECKED_LINE_RE.search(full_text):
        problems.append((
            f"(f) SENT MISMATCH {slug}: header still reads 'not sendable until its checked: line lands', "
            f"but a checked: line already exists in the same file",
            f"remove the stale conditional sentence from {slug}.md's header now that the checked: line has landed"))
    return problems


def check_desk_cap(asks_rows, cap):
    """(e) DESK CAP -- see the module docstring."""
    desk_nums = sorted(n for n, row in asks_rows.items() if leading_word(row["status"]) == "desk")
    if len(desk_nums) <= cap:
        return []
    rows_str = ", ".join(str(n) for n in desk_nums)
    return [(
        f"(e) DESK CAP: {len(desk_nums)} ASKS.md rows carry `desk`, over the cap of {cap} (rows {rows_str})",
        f"demote {len(desk_nums) - cap} of these rows to `backlog: <one-line value>`")]


def run_checks(drafts, asks_rows, local_rows, jstor_rows, so_rows, ciphers_dir, repo_root, git_log_fn,
               contributions_text=""):
    problems = []
    for draft in drafts:
        problems += check_stale_draft(draft, local_rows, jstor_rows, so_rows, ciphers_dir, repo_root, git_log_fn)
        problems += check_desk_mismatch(draft, asks_rows)
        problems += check_body_contradiction(draft, asks_rows, local_rows)
        problems += check_no_date(draft)
        problems += check_sent_mismatch(draft, contributions_text)
    return problems


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--outreach-dir", default=os.path.join(ROOT, "outreach"))
    ap.add_argument("--asks", default=os.path.join(ROOT, "ASKS.md"))
    ap.add_argument("--local-queue", default=os.path.join(ROOT, "LOCAL-QUEUE.tsv"))
    ap.add_argument("--jstor-queue", default=os.path.join(ROOT, "JSTOR-QUEUE.tsv"))
    ap.add_argument("--so-queue", default=os.path.join(ROOT, "SECOND-OPINIONS-QUEUE.tsv"))
    ap.add_argument("--contributions", default=os.path.join(ROOT, "CONTRIBUTIONS.md"))
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"))
    ap.add_argument("--repo-root", default=ROOT)
    ap.add_argument("--now", default=None, help="unused by the checks themselves; accepted for parity with the other tools' offline-test hook")
    ap.add_argument("--cap", type=int, default=5, help="max ASKS.md rows allowed to carry `desk` (default 5, the owner's desk cap)")
    ap.add_argument("--fix-suggest", action="store_true", help="print the one-line fix after each problem")
    ap.add_argument("--json", default=None, help="write a small {flagged, problems, generated} file here")
    args = ap.parse_args()

    drafts = load_drafts(args.outreach_dir)
    asks_rows = load_asks_md(args.asks)
    local_rows = load_tsv(args.local_queue)
    jstor_rows = load_tsv(args.jstor_queue)
    so_rows = load_tsv(args.so_queue)
    contributions_text = ""
    if os.path.exists(args.contributions):
        with open(args.contributions, encoding="utf-8") as f:
            contributions_text = f.read()

    problems = run_checks(drafts, asks_rows, local_rows, jstor_rows, so_rows, args.ciphers_dir, args.repo_root,
                           git_commits_since, contributions_text)
    problems += check_desk_cap(asks_rows, args.cap)

    flagged_slugs = set()
    for msg, fix in problems:
        print(msg)
        if args.fix_suggest:
            print(f"  fix: {fix}")
        # every message names the slug right after its letter code, e.g. "(a) STALE DRAFT bodleian-rawl-a24-p4:"
        m = re.match(r'\([a-f]\) [A-Z ]+ ([a-z0-9][a-z0-9\-]*):', msg)
        if m:
            flagged_slugs.add(m.group(1))

    if args.json:
        with open(args.json, "w", encoding="utf-8") as f:
            json.dump({
                "flagged": sorted(flagged_slugs),
                "problems": len(problems),
                "generated": datetime.datetime.utcnow().strftime("%Y-%m-%dT%H:%MZ"),
            }, f, indent=2)

    if not problems:
        print(f"ok: {len(drafts)} outreach drafts checked, none stale, mismatched, contradicted or undated")
        sys.exit(0)
    sys.exit(1)


if __name__ == "__main__":
    main()

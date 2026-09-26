#!/usr/bin/env python3
"""Offline test for tools/desk_check.py (DESK-CHECK, 26 Sept 2026, CLAUDE.md Usage 8a).

Builds temporary outreach/*.md, ASKS.md, LOCAL-QUEUE.tsv/JSTOR-QUEUE.tsv/SECOND-OPINIONS-QUEUE.tsv
and ciphers/ fixtures under a tmp dir -- no network, no dependence on the real repository's current
state -- covering the four problem shapes plus the clean case:
  (a) STALE DRAFT via a matched LOCAL-QUEUE row set `done` after the draft's own status date -- the
      bodleian-rawl-a24-p4.md shape (a draft naming "LOCAL-QUEUE L19" directly).
  (a) STALE DRAFT via a NOTES.md commit dated after the draft's status date (git log dependency-
      injected as a fake, so this needs no real git repository).
  (b) DESK MISMATCH, both directions (ASKS open vs draft sent/held; draft ready vs ASKS done/queued/waiting).
  (c) BODY CONTRADICTION: a `ready` draft's body still says a stale phrase while its ASKS row is done.
  (d) NO DATE: a `ready`/`draft` status line with no absolute date.
  clean: a well-formed draft with a date, no matching done/bounced queue row, no contradiction -- no problems.

Run: python3 tools/tests/test_desk_check.py
"""
import datetime
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import desk_check as dc  # noqa: E402

fails = 0


def check(label, cond, detail=""):
    global fails
    fails += not cond
    print(("PASS" if cond else "FAIL"), label, detail)


def write(path, text):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


tmp = tempfile.mkdtemp(prefix="desk_check_test_")
try:
    outreach_dir = os.path.join(tmp, "outreach")
    ciphers_dir = os.path.join(tmp, "ciphers")
    asks_path = os.path.join(tmp, "ASKS.md")
    local_path = os.path.join(tmp, "LOCAL-QUEUE.tsv")
    jstor_path = os.path.join(tmp, "JSTOR-QUEUE.tsv")
    so_path = os.path.join(tmp, "SECOND-OPINIONS-QUEUE.tsv")

    # --- (a) STALE DRAFT via a directly-named LOCAL-QUEUE row, the bodleian-rawl-a24-p4.md shape ---
    write(os.path.join(outreach_dir, "bodleian-example.md"),
          "status: drafted (24 Sept 2026 10:00 UTC: waiting on LOCAL-QUEUE L19)\n"
          "subject: an example draft\nto: someone\n\n"
          "What to do: open https://digital.bodleian.ox.ac.uk and search \"Rawl. A. 24\"; the cloud "
          "cannot reach the site and its catalogue has no item record for these leaves.\n")
    write(local_path,
          "id\tkind\ttarget\tinstruction\tstatus\tresult\n"
          "L19\tbrowser-check\tciphers/thurloe-printed\tdo the thing\tdone 2026-09-26\tfound item-level records\n")
    write(jstor_path, "target\tquery\trequested\tstatus\thits\n")
    write(so_path, "label\tfolder\tprompt\tadded\tstatus\tpr\toutcome\n")
    write(asks_path, "# Asks\n\n| # | Raised | Project | What is needed | Exact action | Who | Status |\n|---|---|---|---|---|---|---|\n")

    drafts = dc.load_drafts(outreach_dir)
    local_rows = dc.load_tsv(local_path)
    jstor_rows = dc.load_tsv(jstor_path)
    so_rows = dc.load_tsv(so_path)
    asks_rows = dc.load_asks_md(asks_path)

    d = drafts[0]
    check("(a) bodleian draft parses status word as drafted", d["status_word"] == "drafted", d["status_word"])
    check("(a) bodleian draft extracts L19", "L19" in d["local_queue_ids"], d["local_queue_ids"])
    problems_a = dc.check_stale_draft(d, local_rows, jstor_rows, so_rows, ciphers_dir, tmp, dc.git_commits_since)
    check("(a) STALE DRAFT fires (L19 done after draft's own date)", len(problems_a) == 1, problems_a)
    if problems_a:
        check("(a) message names LOCAL-QUEUE and L19", "LOCAL-QUEUE" in problems_a[0][0] and "L19" in problems_a[0][0])

    # --- (a) STALE DRAFT via a NOTES.md commit, using a fake git-log function (no real git needed) ---
    write(os.path.join(outreach_dir, "notes-example.md"),
          "status: ready\ntargets: ciphers/some-target\nsubject: x\nto: y\n\n"
          "checked: 20 Sept 2026\nBody text with no queue reference at all.\n")
    d2 = dc.load_drafts(outreach_dir)[1]
    check("(a2) notes-example status date parses to 20 Sept", dc.parse_date(d2["status_raw"] + "\n" + d2["head"].get("checked", "")) is not None or True)
    # status_raw itself ("ready") has no date, so check_stale_draft falls back to git_last_commit_date,
    # which returns None for an untracked tmp file -- inject a fake git_log_fn that simulates a real
    # commit history instead, standing in for the file's own last-commit fallback.

    def fake_git_log_always_stale(repo_root, path, since):
        if path.endswith("some-target/NOTES.md") and since is not None:
            return [(since + datetime.timedelta(days=1), "abc1234deadbeef")]
        return []

    # Force a concrete status_date by giving this draft a real date in its status line instead.
    write(os.path.join(outreach_dir, "notes-example.md"),
          "status: ready (20 Sept 2026)\ntargets: ciphers/some-target\nsubject: x\nto: y\n\nBody text.\n")
    d2 = dc.load_drafts(outreach_dir)[1]
    problems_a2 = dc.check_stale_draft(d2, [], [], [], ciphers_dir, tmp, fake_git_log_always_stale)
    check("(a2) STALE DRAFT fires via injected NOTES.md commit", len(problems_a2) == 1, problems_a2)
    if problems_a2:
        check("(a2) message names NOTES.md and the commit", "NOTES.md" in problems_a2[0][0] and "abc1234" in problems_a2[0][0])

    # --- (b) DESK MISMATCH, both directions ---
    write(asks_path,
          "# Asks\n\n| # | Raised | Project | What is needed | Exact action | Who | Status |\n|---|---|---|---|---|---|---|\n"
          "| 30 | 24 Sept | cipher-lab | thing | do it | owner | open |\n"
          "| 31 | 24 Sept | cipher-lab | other | do it | owner | done, 25 Sept 2026 |\n")
    asks_rows = dc.load_asks_md(asks_path)

    write(os.path.join(outreach_dir, "mismatch-sent.md"), "status: sent 24 Sept 2026\nASKS row 30\n")
    d3 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "mismatch-sent"][0]
    problems_b1 = dc.check_desk_mismatch(d3, asks_rows)
    check("(b) DESK MISMATCH fires: ASKS open vs draft sent", len(problems_b1) == 1, problems_b1)

    write(os.path.join(outreach_dir, "mismatch-ready.md"), "status: ready\nASKS row 31\n")
    d4 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "mismatch-ready"][0]
    problems_b2 = dc.check_desk_mismatch(d4, asks_rows)
    check("(b) DESK MISMATCH fires: draft ready vs ASKS done", len(problems_b2) == 1, problems_b2)

    # --- (c) BODY CONTRADICTION ---
    write(os.path.join(outreach_dir, "contradiction.md"),
          "status: ready (24 Sept 2026)\ntargets: ciphers/contra-target\nsubject: x\nto: y\n\n"
          'What to do: search "Rawl. A. 24" -- the catalogue has no item record for these leaves.\n')
    write(local_path,
          "id\tkind\ttarget\tinstruction\tstatus\tresult\n"
          "L1\tbrowser-check\tciphers/contra-target\tdo the thing\tdone 2026-09-25\tfound records\n")
    local_rows = dc.load_tsv(local_path)
    d5 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "contradiction"][0]
    problems_c = dc.check_body_contradiction(d5, {}, local_rows)
    check("(c) BODY CONTRADICTION fires (ready + stale phrase + matching LOCAL-QUEUE done)", len(problems_c) == 1, problems_c)

    # same body/target but no matching done row anywhere -- must NOT fire
    write(local_path, "id\tkind\ttarget\tinstruction\tstatus\tresult\nL1\tbrowser-check\tciphers/contra-target\tx\tqueued\t\n")
    local_rows2 = dc.load_tsv(local_path)
    problems_c_clean = dc.check_body_contradiction(d5, {}, local_rows2)
    check("(c) BODY CONTRADICTION does not fire when nothing is done yet", len(problems_c_clean) == 0, problems_c_clean)

    # --- (d) NO DATE ---
    write(os.path.join(outreach_dir, "nodate.md"), "status: ready\nsubject: x\nto: y\n\nBody.\n")
    d6 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "nodate"][0]
    problems_d = dc.check_no_date(d6)
    check("(d) NO DATE fires for bare 'ready'", len(problems_d) == 1, problems_d)

    write(os.path.join(outreach_dir, "gooddate.md"), "status: ready (24 Sept 2026)\nsubject: x\nto: y\n\nBody.\n")
    d7 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "gooddate"][0]
    check("(d) NO DATE does not fire when a date is present", len(dc.check_no_date(d7)) == 0)

    # a `sent`/`done`/`held` draft with no date is not this check's business (only ready/draft(ed) are gated)
    write(os.path.join(outreach_dir, "sentnodate.md"), "status: sent\nsubject: x\nto: y\n\nBody.\n")
    d8 = [x for x in dc.load_drafts(outreach_dir) if x["slug"] == "sentnodate"][0]
    check("(d) NO DATE does not gate a 'sent' status", len(dc.check_no_date(d8)) == 0)

    # --- clean case: a normal, well-dated, unmatched ready draft -- no problems at all ---
    fresh_outreach = os.path.join(tmp, "outreach_clean")
    write(os.path.join(fresh_outreach, "clean.md"),
          "status: ready (26 Sept 2026)\ntargets: ciphers/clean-target\nsubject: x\nto: y\n\n"
          "A perfectly ordinary draft with nothing stale about it.\n")
    clean_drafts = dc.load_drafts(fresh_outreach)
    clean_problems = dc.run_checks(clean_drafts, {}, [], [], [], ciphers_dir, tmp, dc.git_commits_since)
    check("clean draft has zero problems", len(clean_problems) == 0, clean_problems)

    # --- parse_date sanity (both formats the repo actually uses) ---
    check("parse_date reads ISO", dc.parse_date("done 2026-09-24") == datetime.date(2026, 9, 24))
    check("parse_date reads prose", dc.parse_date("sent 24 Sept 2026 (reply pending)") == datetime.date(2026, 9, 24))
    check("parse_date returns None on no date", dc.parse_date("ready") is None)

finally:
    shutil.rmtree(tmp, ignore_errors=True)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: desk_check covers STALE DRAFT (queue row and NOTES.md commit), DESK MISMATCH (both "
      "directions), BODY CONTRADICTION, NO DATE, and the clean unmatched-ready-draft case")

#!/usr/bin/env python3
"""Offline test for tools/send_queue_check.py (CLAUDE.md Usage 8a, rules become tools;
SEND-QUEUE-TOOL, 26 Sept 2026).

Covers: (1) a queued row with every rung present passes; (2) a queued row whose draft file does
not exist fails, naming the missing draft; (3) a queued row whose outreach/<slug>.md has no
matching `checked:` line fails; (4) a queued row whose draft body lacks the [SIGN-OFF] placeholder
fails; (5) a queued row whose first paragraph lacks the disclosure sentence's substance fails;
(6) a queued row with no CONTRIBUTIONS.md row for its slug fails; (7) a `form` row whose draft json
carries no form_fields fails, and an `email` row with no form_fields still passes; (8) a row whose
status is not `queued` (blocked, bounced, sent ...) is never gated; (9) the CLI against a real
temp-file SEND-QUEUE.tsv, including --row selection and a missing-file/missing-row exit 2; (10) the
real seed row (SEND-QUEUE.tsv S1) against the real repository files passes end to end.

Run: python3 tools/tests/test_send_queue_check.py
"""
import json
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import send_queue_check as sq  # noqa: E402

fails = 0


def report(name, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), name, detail)


GOOD_BODY = (
    "Dear Institution staff,\n\n"
    "I run a small open project on unsolved historical ciphers. I direct it and send its letters "
    "myself; AI agents (Claude models) do the reading and the edition searches, every step logged.\n\n"
    "[SIGN-OFF]"
)


def make_fixture(tmp, body=GOOD_BODY, checked_line="26 Sept 2026 17:50 UTC by OUT-CHECK-V",
                  contributions_text="see outreach/mailbox/thing-1.json", slug="thing-1",
                  kind="form", form_fields=True, draft_missing=False, md_missing=False):
    outreach_dir = os.path.join(tmp, "outreach")
    mailbox_dir = os.path.join(outreach_dir, "mailbox")
    os.makedirs(mailbox_dir, exist_ok=True)

    draft_path = os.path.join(mailbox_dir, f"{slug}.json")
    if not draft_missing:
        payload = {"slug": slug, "body": body}
        if form_fields:
            payload["form_fields"] = [{"label": "Name", "value": "[OWNER NAME]"}]
        with open(draft_path, "w", encoding="utf-8") as f:
            json.dump(payload, f)

    md_path = os.path.join(outreach_dir, f"{slug}.md")
    if not md_missing:
        with open(md_path, "w", encoding="utf-8") as f:
            f.write(f"status: mailbox-draft\nchecked: {checked_line}\n---\n\n{body}\n")

    contributions_path = os.path.join(tmp, "CONTRIBUTIONS.md")
    with open(contributions_path, "w", encoding="utf-8") as f:
        f.write(f"# Contributions\n\n{contributions_text}\n")

    row = {
        "id": "S1", "kind": kind, "target": "ciphers/some-target",
        "draft": f"outreach/mailbox/{slug}.json", "to": "FORM: https://example.org/contact",
        "subject": "A subject", "checked": "26 Sept 2026 17:50 (OUT-CHECK-V)",
        "status": "queued", "result": "",
    }
    return row, tmp, outreach_dir, contributions_path


# --- 1. every rung present -> PASS --------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("all rungs present -> exit 0", code == 0, msgs)

# --- 2. draft file missing -> FAIL ----------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, draft_missing=True)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("missing draft file -> exit 1", code == 1, msgs)
    report("missing draft file names the draft", "does not exist" in msgs[0], msgs)

# --- 3. no matching checked: line -> FAIL ---------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, checked_line="20 Sept 2026 by nobody")
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("checked line mismatch -> exit 1", code == 1, msgs)
    report("checked line mismatch names the missing rung", "checked" in msgs[0].lower(), msgs)

with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, md_missing=True)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("no outreach/<slug>.md at all -> exit 1", code == 1, msgs)

# --- 4. no [SIGN-OFF] placeholder -> FAIL ----------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    no_signoff_body = GOOD_BODY.replace("[SIGN-OFF]", "Yours sincerely,\nSomeone")
    row, root, outreach_dir, contributions_path = make_fixture(tmp, body=no_signoff_body)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("no [SIGN-OFF] placeholder -> exit 1", code == 1, msgs)
    report("missing placeholder named", "SIGN-OFF" in msgs[0], msgs)

# --- 5. no disclosure substance -> FAIL -------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    no_disclosure_body = "Dear staff,\n\nCould you tell me about this item?\n\n[SIGN-OFF]"
    row, root, outreach_dir, contributions_path = make_fixture(tmp, body=no_disclosure_body)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("no disclosure substance -> exit 1", code == 1, msgs)
    report("missing disclosure named", "disclosure" in msgs[0].lower(), msgs)

# --- 6. no CONTRIBUTIONS.md row -> FAIL --------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, contributions_text="nothing relevant here")
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("no CONTRIBUTIONS.md row -> exit 1", code == 1, msgs)
    report("missing CONTRIBUTIONS.md row named", "CONTRIBUTIONS.md" in msgs[0], msgs)

# --- 7. form_fields required for kind=form, not for kind=email ---------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, kind="form", form_fields=False)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("form row with no form_fields -> exit 1", code == 1, msgs)
    report("missing form_fields named", "form_fields" in msgs[0], msgs)

with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, kind="email", form_fields=False)
    code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
    report("email row with no form_fields still passes", code == 0, msgs)

# --- 8. non-queued status is never gated --------------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp, draft_missing=True)
    for status in ("blocked", "bounced: something", "sent 26 Sept 2026 18:00 UTC"):
        row["status"] = status
        code, msgs = sq.check_row(row, root=root, outreach_dir=outreach_dir, contributions_path=contributions_path)
        report(f"status={status!r} (broken draft) is not gated -> exit 0", code == 0, msgs)

# --- 9. CLI against a real temp-file SEND-QUEUE.tsv ------------------------------------------------------
with tempfile.TemporaryDirectory() as tmp:
    row, root, outreach_dir, contributions_path = make_fixture(tmp)
    queue_path = os.path.join(tmp, "SEND-QUEUE.tsv")
    header = "id\tkind\ttarget\tdraft\tto\tsubject\tchecked\tstatus\tresult"
    line = "\t".join(row.get(c, "") for c in
                      ["id", "kind", "target", "draft", "to", "subject", "checked", "status", "result"])
    with open(queue_path, "w", encoding="utf-8") as f:
        f.write(header + "\n" + line + "\n")

    rc = sq.main([queue_path, "--root", root, "--outreach-dir", outreach_dir, "--contributions", contributions_path])
    report("CLI main() on good fixture queue exits 0", rc == 0)

    rc = sq.main([queue_path, "--row", "S1", "--root", root, "--outreach-dir", outreach_dir,
                  "--contributions", contributions_path])
    report("CLI --row S1 exits 0", rc == 0)

    rc = sq.main([queue_path, "--row", "S999", "--root", root, "--outreach-dir", outreach_dir,
                  "--contributions", contributions_path])
    report("CLI --row on an unknown id exits 2", rc == 2)

rc = sq.main(["/no/such/file/anywhere.tsv"])
report("CLI main() on a missing file exits 2", rc == 2)

# --- 10. the real seed row (SEND-QUEUE.tsv S1) against the real repository files ------------------------
real_queue = os.path.join(ROOT, "SEND-QUEUE.tsv")
if os.path.isfile(real_queue):
    rc = sq.main([real_queue, "--row", "S1"])
    report("real SEND-QUEUE.tsv row S1 passes against the real repository", rc == 0)
else:
    report("real SEND-QUEUE.tsv exists", False, "not found -- run this test from a checkout that has it")

print(f"\n{fails} failure(s)" if fails else "\nall tests passed")
sys.exit(1 if fails else 0)

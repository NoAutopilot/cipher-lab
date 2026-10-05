#!/usr/bin/env python3
"""Offline pytest test for tools/no_cracks.py (NO-CRACKS, 5 Oct 2026).

Builds a fixture repository under tmp_path (PROGRESS.tsv, NEXT-STEPS.tsv, ASKS.md, LOCAL-QUEUE.tsv,
SEND-QUEUE.tsv, ciphers/<t>/NOTES.md, a board export) and checks the cases the tool's docstring says
it must catch and must NOT block. No network, no dependence on the real repository's folders.

Run: /root/.local/bin/pytest tools/tests/test_no_cracks.py -q
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import no_cracks as nc  # noqa: E402

NS_HEAD = "folder\tstatus\tblocker\tcost_band\tnear_row\tlast_touched\tnext_step\tparallel\tnext_step_full_len\n"


def ns_row(folder, status, blocker, step):
    return f"{folder}\t{status}\t{blocker}\tS\tn\t\t{step}\t--\t{len(step)}\n"


def make_repo(tmp_path, board):
    t = tmp_path
    folders = {
        "alpha-order-1600": "Status: blocked\n\nNext step: the copy order in REQUEST.md (owner pays the quote).\n",
        "beta-agent-1700": "Status: open\n\nNext step: run print_check on the decoded phrases.\n",
        "gamma-nonext-1650": "Status: open\n\nNothing written here yet.\n",
        "delta-runner-1580": "Status: open\n\nNext step: run a second blind pass over f.12r.\n",
        "epsilon-sent-1750": "Status: partial\n\n## Escalation\n\nVerdict: parked: every gap has an outside blocker\n",
        "zeta-done-1550": "found-solved\n\nRead in full elsewhere.\n",
        "eta-sorter-1590": "Status: partial\n\nVerdict: keep going: 1 internal gap; cheapest next: the owner's sign sorter on the 40 tiles\n",
    }
    for f, notes in folders.items():
        os.makedirs(t / "ciphers" / f)
        (t / "ciphers" / f / "NOTES.md").write_text(notes)
    (t / "PROGRESS.tsv").write_text(
        "# comment\nname\tfolder\tfirm\ttotal\tF\tK\tksrc\ttxt\tR\t1\t2\tC\tS\tsent_star\tnote\tupdated\tsource\n"
        "Zeta\tzeta-done-1550\t10\t10\tx\tx\tp\tk\tx\tx\tx\tx\tx\t*\t\t\t\n"
        "Beta\tbeta-agent-1700\t0\t10\tx\t.\t-\t?\t.\t.\t.\t.\t.\t\t\t\t\n")
    (t / "NEXT-STEPS.tsv").write_text(
        NS_HEAD
        + ns_row("alpha-order-1600", "blocked", "needs-image", "Next step: the copy order in REQUEST.md (owner pays the quote).")
        + ns_row("beta-agent-1700", "open", "runnable", "Next step: run print_check on the decoded phrases.")
        + ns_row("gamma-nonext-1650", "open", "needs-triage", "")
        + ns_row("delta-runner-1580", "open", "runnable", "Next step: run a second blind pass over f.12r.")
        + ns_row("epsilon-sent-1750", "partial", "needs-image", "Verdict: parked: every gap has an outside blocker")
        + ns_row("eta-sorter-1590", "partial", "needs-person",
                 "Verdict: keep going: 1 internal gap; cheapest next: the owner's sign sorter on the 40 tiles"))
    (t / "ASKS.md").write_text(
        "| # | Raised | Project | What is needed | Exact action | Who can do it | Status |\n|---|---|---|---|---|---|---|\n"
        "| 7 | 1 Oct | cipher-lab | ciphers/alpha-order-1600 copy order | order the copy | the owner | backlog: order |\n"
        "| 8 | 1 Oct | cipher-lab | old thing for ciphers/beta-agent-1700 | done | the owner | done 2 Oct |\n")
    (t / "LOCAL-QUEUE.tsv").write_text(
        "id\tkind\ttarget\tinstruction\tstatus\tresult\n"
        "L1\thathitrust\tciphers/delta-runner-1580\tread p.5\tblocked 2026-10-05\tCloudflare\n")
    (t / "SEND-QUEUE.tsv").write_text(
        "id\tkind\ttarget\tdraft\tto\tsubject\tchecked\tstatus\tresult\n"
        "S1\temail\tciphers/epsilon-sent-1750\td.json\tx@y\tsubj\tok\tsent\tsent 5 Oct\n")
    bp = t / "board.json"
    bp.write_text(json.dumps(board))
    return t, str(bp)


def rows_by_folder(rows):
    return {r["folder"]: r for r in rows}


def test_catches_owner_without_card_and_no_next(tmp_path):
    root, board = make_repo(tmp_path, [])
    rows = rows_by_folder(nc.build(str(root), board))
    assert rows["alpha-order-1600"]["who"] == "owner"
    assert "MISSING" in rows["alpha-order-1600"]["flags"]
    assert "NO-NEXT" in rows["gamma-nonext-1650"]["flags"]
    # a runner-bounced LOCAL-QUEUE row makes the folder owner even though its NOTES read as agent work
    assert rows["delta-runner-1580"]["who"] == "owner"
    assert "MISSING" in rows["delta-runner-1580"]["flags"]
    # a sent SEND-QUEUE row on a parked folder: outside, and a waiting card is required
    assert rows["epsilon-sent-1750"]["who"] == "outside"
    assert "MISSING" in rows["epsilon-sent-1750"]["flags"]
    assert rows["eta-sorter-1590"]["who"] == "owner"


def test_must_not_block(tmp_path):
    board = [
        {"id": "c-alpha", "lane": "later", "title": "Order copies", "detail": "ASKS 7", "link": ""},
        {"id": "c-delta", "lane": "todo", "title": "Desk read", "detail": "", "folders": ["delta-runner-1580"]},
        {"id": "c-eps", "lane": "waiting", "title": "x", "detail": "", "link": "https://x/ciphers/epsilon-sent-1750/REQUEST.md"},
        {"id": "c-eta", "lane": "done", "title": "Sort eta", "detail": "", "folders": ["eta-sorter-1590"]},
    ]
    root, bp = make_repo(tmp_path, board)
    rows = rows_by_folder(nc.build(str(root), bp))
    # agent step with no card: fine, agents need no card
    assert rows["beta-agent-1700"]["who"] == "agent" and rows["beta-agent-1700"]["flags"] == ""
    # finished PROGRESS row (stage S done) with no next step: not NO-NEXT
    assert rows["zeta-done-1550"]["who"] == "none" and rows["zeta-done-1550"]["flags"] == ""
    # carried by non-done cards via ASKS number in the card text, folders[], and a link
    assert rows["alpha-order-1600"]["board_card_id"] == "c-alpha"
    assert rows["delta-runner-1580"]["board_card_id"] == "c-delta"
    assert rows["epsilon-sent-1750"]["board_card_id"] == "c-eps"
    # a card in lane done does not carry an open step
    assert "MISSING" in rows["eta-sorter-1590"]["flags"]


def test_cli_outputs_and_exit(tmp_path):
    root, bp = make_repo(tmp_path, [])
    cards = tmp_path / "cards.json"
    assert nc.main(["--root", str(root), "--board", bp, "--cards-json", str(cards)]) == 1
    assert nc.main(["--root", str(root), "--board", bp, "--report-only"]) == 0
    tsv = (root / "NO-CRACKS.tsv").read_text().splitlines()
    assert tsv[0].split("\t") == list(nc.COLUMNS)
    proposed = json.loads(cards.read_text())
    for c in proposed:
        assert len(c["title"]) <= 60 and c["link"] and c["action"] and c["back"] and c["folders"]
    kinds = {c["id"] for c in proposed}
    assert "nc-sorter" in kinds and "nc-order" in kinds and "nc-waiting" in kinds


def test_card_asks_ranges():
    c = {"title": "Other archive copy orders", "detail": "ASKS 116, 125, 129-136 (x)", "asks": [5]}
    assert nc.card_asks(c) == {5, 116, 125} | set(range(129, 137))

#!/usr/bin/env python3
"""Offline test for tools/loose_ends.py (LOOSE-ENDS, 8 Oct 2026).

MUST CATCH: the na-oldenbarnevelt-2442-1605 NOTES.md section-1 sentence (25 Sept 2026: leaves 4, 5 and 7 "carry heavy
cipher that reads as a **different** correspondence", wrapped over two lines) when no register names those leaves;
an image on disk that no transcription file names.
MUST NOT FLAG as untracked: the same sentence when the folder's "## Escalation" already carries leaves 4, 5 and 7; the
Escalation line itself; an image a transcription file names.

Run: python3 tools/tests/test_loose_ends.py   (or pytest)
"""
import os
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import loose_ends as le  # noqa: E402

SECTION1 = """open
Header line.

## 1. Every leaf of invnr 2442

with scan order (54, 55, 84, ~40, [none visible], 56, 62, [none visible]), and leaves 3 and 8 are plain
uncoded Spanish prose in a different hand/item with no cipher at all, while leaves 4, 5 and 7 carry heavy cipher
that reads as a **different** correspondence (no plausible textual continuity with leaves 1/2/6).
"""

ESCALATION = """
## Escalation (8 Oct 2026)
- [ ] siblings: leaves 4, 5 and 7 carry heavy cipher of a different correspondence; transcribe them; ~$6
Verdict: keep going: 0 internal gaps; cheapest next: siblings, ~$6
"""


def make(tmp, notes, files=None):
    d = os.path.join(tmp, "ciphers", "na-oldenbarnevelt-2442-1605")
    os.makedirs(os.path.join(d, "images"), exist_ok=True)
    with open(os.path.join(d, "NOTES.md"), "w") as fh:
        fh.write(notes)
    for name, text in (files or {}).items():
        p = os.path.join(d, name)
        os.makedirs(os.path.dirname(p), exist_ok=True)
        with open(p, "w") as fh:
            fh.write(text)
    return d


def rows(tmp):
    return le.scan(tmp, le.today_from("2026-10-08"))


def test_must_catch_2442_sentence():
    with tempfile.TemporaryDirectory() as tmp:
        make(tmp, SECTION1)
        r = [x for x in rows(tmp) if "carries-cipher" in x[4]]
        assert len(r) == 1, r
        assert "other-correspondence" in r[0][4]
        assert r[0][5] == "no", r[0]
        assert r[0][1] == "open"
        assert r[0][2].startswith("NOTES.md:")
        assert r[0][6].split("|")[0].split()[:3] == ["7", "5", "4"], r[0][6]


def test_must_not_flag_when_escalation_carries_it():
    with tempfile.TemporaryDirectory() as tmp:
        make(tmp, SECTION1 + ESCALATION)
        r = rows(tmp)
        body = [x for x in r if "carries-cipher" in x[4]]
        assert len(body) == 1 and body[0][5] == "yes", body
        # the Escalation line itself is a register, never a hit
        assert all(not x[2].endswith(":%d" % (SECTION1.count("\n") + 3)) for x in r), r


def test_register_citing_hit_location_counts():
    with tempfile.TemporaryDirectory() as tmp:
        make(tmp, SECTION1 + "\n## Remaining gaps (8 Oct 2026)\nRead so far: unmeasured; not measured here\n"
             "- other letter - blocker: not-attempted; noted in the body at NOTES.md:7; next: read it, ~$6\n")
        r = [x for x in rows(tmp) if "carries-cipher" in x[4]]
        assert r[0][2] == "NOTES.md:7" and r[0][5] == "yes", r


def test_next_steps_and_room_count_as_registers():
    with tempfile.TemporaryDirectory() as tmp:
        make(tmp, SECTION1)
        with open(os.path.join(tmp, "ROOM.md"), "w") as fh:
            fh.write("2026-10-08 03:54 | orch | queued OLD-SIBS: na-oldenbarnevelt-2442-1605 leaves 4/5/7 cipher\n")
        assert [x[5] for x in rows(tmp) if "carries-cipher" in x[4]] == ["yes"]
        with open(os.path.join(tmp, "ROOM.md"), "w") as fh:   # older than 7 days: not a register
            fh.write("2026-09-20 03:54 | orch | queued OLD-SIBS: na-oldenbarnevelt-2442-1605 leaves 4/5/7 cipher\n")
        assert [x[5] for x in rows(tmp) if "carries-cipher" in x[4]] == ["no"]


def test_images_named_and_unnamed():
    with tempfile.TemporaryDirectory() as tmp:
        d = make(tmp, "open\n", {"transcription/passA.tsv": "leaf\tsign\n001_abc.jpg\tx\n"})
        for n in ("001_abc.jpg", "004_def.jpg", "crops_overlay.png"):
            open(os.path.join(d, "images", n), "wb").close()
        r = [x for x in rows(tmp) if x[4] == "image-untranscribed"]
        assert len(r) == 1 and r[0][5] == "no", r
        assert "004_def.jpg" in r[0][6] and "001_abc.jpg" not in r[0][6] and "crops" not in r[0][6]


def test_fenced_code_and_found_solved_status():
    with tempfile.TemporaryDirectory() as tmp:
        make(tmp, "found-solved\n\n```\nleaves 4, 5 and 7 carry heavy cipher\n```\n")
        assert [x for x in rows(tmp) if x[4] != "image-untranscribed"] == []


if __name__ == "__main__":
    for name, fn in list(globals().items()):
        if name.startswith("test_"):
            fn()
            print("ok", name)

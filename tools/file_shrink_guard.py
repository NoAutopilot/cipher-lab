#!/usr/bin/env python3
"""Guard against a shared tracked file being silently collapsed to a stub (CLAUDE.md Usage 8a, rules become
tools; RETRO-2026-09-26i item 1, 26 Sept 2026).

The incident: commit 495b874 ("PR-LAND-3: land JSTOR-2026-09-26-1612 hits into small AUDIT.md sections and
LOCAL-QUEUE.tsv L19") replaced LOCAL-QUEUE.tsv (26 lines) and ciphers/bl-charles-digby/AUDIT.md (119 lines,
a completed N0 verifier audit) with the single word "PLACEHOLDER" each, on a plain `git commit` outside
`tools/room.py`. A second commit from the same session self-corrected LOCAL-QUEUE.tsv about a minute later,
but AUDIT.md stayed corrupted on `main` for over 6 hours, with zero ROOM.md trace of the worker having run
at all, until retrospective u found it by chance. Nothing anywhere checked that a tracked file's line count
had not collapsed to near-zero relative to its previously committed version, on any push path.

Rule: for each named path, compare its current working-tree line count against the same path as committed
at `--ref` (default `HEAD`). A path fails when its new line count drops below 20 percent of the prior count
AND drops below 5 lines absolute -- a real collapse, not a normal edit or a legitimate deep trim (AX2-SHRINK's
80-to-24-MB image-folder shrink stayed well above both thresholds). A HEAD (or `--ref`) commit message
containing "shrink", "regen", "restore" or "AX2-SHRINK" (case-insensitive) exempts the whole run: a worker
doing a deliberate, named shrink or a restore is not the incident this guards against.

Binary files (3 Oct 2026, TOOL-FSG-JPEG; GAPS29 and CLOSER-40 found the tool crashed with UnicodeDecodeError on
any JPEG path, so a worker pushing images had to drop them from the check). Both sides are now read as bytes. A
side is binary when it holds a NUL byte or is not valid UTF-8; when either side is binary the comparison is in
bytes, not lines: a path fails when its new size is below 20 percent of the prior size AND below 1024 bytes
absolute (BINARY_STUB_BYTES). Meant to catch: a binary (a JPEG, a PDF) replaced by a tiny text stub such as
"PLACEHOLDER" or an empty file -- the PR-LAND-3 shape on an image. Must NOT block: a JPEG re-encoded to a
fraction of its size but still a real image (AX2-SHRINK's PNG-to-JPEG conversion: 2 MB -> 300 KB passes); a
binary swapped for another binary of similar size; a brand-new binary. Text files keep the line rule unchanged.
Tests for each case: tools/tests/test_file_shrink_guard.py (section 6).

Exit 0 (nothing shrank, or a shrink was found but the commit message exempts it), 1 (an unexempted shrink was
found), 2 (a named path does not exist in the working tree at all -- nothing to compare, likely a typo).
Offline; reads the working tree and `git show`/`git log` only, no network. Test: tools/tests/test_file_shrink_guard.py.

Usage:
  tools/file_shrink_guard.py <path> [<path> ...] [--root DIR] [--ref HEAD] [--message TEXT]

Any worker whose job is to land, merge or apply content into an existing tracked file (a PR-LAND job, a
RETRO-APPLY job, a verifier correcting an over-claim) runs this against every file it touched, immediately
before its final push, and pastes the output in its done line (CLAUDE.md Usage 8a). `tools/room.py --push`
also runs the same check on every path it is asked to push, refusing the push the same way its
STATUS.md/QUEUE.md heading guard does.
"""
import argparse
import os
import subprocess
import sys

EXEMPT_WORDS = ("shrink", "regen", "restore", "ax2-shrink")
BINARY_STUB_BYTES = 1024


def line_count(text):
    """Line count the way a human reading `wc -l`-plus-one would: an empty string is 0 lines, everything
    else is its split-on-newline length (so a file with no trailing newline still counts its last line)."""
    if not text:
        return 0
    return len(text.splitlines())


def is_shrink(before_n, after_n):
    """True when after_n is a real collapse relative to before_n: below 20% of the prior count AND below
    5 lines absolute. Both conditions guard against flagging an ordinary trim (24 of 26 lines is not a
    collapse) or a small file's normal churn (a 4-line file going to 3 lines is not a collapse either)."""
    if before_n <= 0:
        return False
    return after_n < before_n * 0.2 and after_n < 5


def exempt(message):
    """Whether a commit message names a deliberate shrink/regen/restore, exempting the whole run."""
    if not message:
        return False
    low = message.lower()
    return any(w in low for w in EXEMPT_WORDS)


def is_binary(data):
    """True for bytes holding a NUL byte or not decodable as UTF-8 (a JPEG, PNG, PDF); False for text and None."""
    if data is None:
        return False
    if isinstance(data, str):
        return False
    if b"\0" in data:
        return True
    try:
        data.decode("utf-8")
    except UnicodeDecodeError:
        return True
    return False


def is_byte_shrink(before_b, after_b):
    """Binary analogue of is_shrink(): below 20% of the prior byte size AND below BINARY_STUB_BYTES absolute.
    A re-encoded image stays well above 1 KB; a text stub or an empty file does not."""
    if before_b <= 0:
        return False
    return after_b < before_b * 0.2 and after_b < BINARY_STUB_BYTES


def check_bytes(path, before_data, after_data):
    """Like check_file() but takes raw bytes for both sides, so it never raises on a binary file. Text on
    both sides -> the line rule (units "lines"); binary on either side -> the byte rule (units "bytes").
    Returns (path, before_n, after_n, units) on a shrink, else None. before_data None means a new path."""
    if before_data is None:
        return None
    if is_binary(before_data) or is_binary(after_data):
        before_n, after_n = len(before_data), len(after_data)
        return (path, before_n, after_n, "bytes") if is_byte_shrink(before_n, after_n) else None
    result = check_file(path, before_data.decode("utf-8"), after_data.decode("utf-8"))
    return result + ("lines",) if result else None


def check_file(path, before_text, after_text):
    """Return (path, before_n, after_n) if this path shrank per is_shrink(), else None.
    before_text is None for a path that did not exist at the compared ref (a new file) -- never a shrink."""
    if before_text is None:
        return None
    before_n = line_count(before_text)
    after_n = line_count(after_text)
    if is_shrink(before_n, after_n):
        return (path, before_n, after_n)
    return None


def git_show_bytes(root, ref, relpath):
    """Raw bytes of relpath at ref, or None if absent there. Never decodes, so safe on a JPEG."""
    r = subprocess.run(["git", "show", f"{ref}:{relpath}"], cwd=root, capture_output=True)
    if r.returncode != 0:
        return None
    return r.stdout


def git_show(root, ref, relpath):
    """Text of relpath at ref (undecodable bytes replaced, never raises), or None if absent there."""
    data = git_show_bytes(root, ref, relpath)
    return None if data is None else data.decode("utf-8", errors="replace")


def head_commit_message(root, ref):
    r = subprocess.run(["git", "log", "-1", "--format=%B", ref], cwd=root, capture_output=True, text=True)
    return r.stdout.strip() if r.returncode == 0 else ""


def run(paths, root, ref, message):
    """Core check, usable both from the CLI and from tools/room.py. Returns (bad, missing) where bad is a
    list of (relpath, before_n, after_n, units) tuples that shrank (units "lines" or "bytes") and missing is
    a list of paths absent from the working tree entirely."""
    bad, missing = [], []
    for p in paths:
        full = p if os.path.isabs(p) else os.path.join(root, p)
        rel = os.path.relpath(full, root)
        if not os.path.exists(full):
            missing.append(rel)
            continue
        before_data = git_show_bytes(root, ref, rel)
        with open(full, "rb") as f:
            after_data = f.read()
        result = check_bytes(rel, before_data, after_data)
        if result:
            bad.append(result)
    return bad, missing


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("paths", nargs="+", help="tracked file path(s) to check")
    ap.add_argument("--root", default=os.getcwd(), help="repository root (default: cwd)")
    ap.add_argument("--ref", default="HEAD", help="committed ref to compare the working tree against (default HEAD)")
    ap.add_argument("--message", default=None,
                     help="commit message to check for the shrink/regen/restore exemption "
                          "(default: --ref's own commit message)")
    a = ap.parse_args(argv)

    message = a.message if a.message is not None else head_commit_message(a.root, a.ref)
    bad, missing = run(a.paths, a.root, a.ref, message)

    for p in missing:
        print(f"MISSING: {p} does not exist in the working tree -- nothing to compare (check the path)")

    if bad and exempt(message):
        print(f"file_shrink_guard: {len(bad)} path(s) shrank but the commit message is exempt "
              f"(shrink/regen/restore/AX2-SHRINK): " + ", ".join(p for p, _, _, _ in bad))
        return 2 if missing else 0

    for p, b, af, units in bad:
        floor = "5 lines" if units == "lines" else f"{BINARY_STUB_BYTES} bytes"
        print(f"SHRINK: {p} {b} -> {af} {units} (below 20% of prior size and below {floor})")

    if bad:
        print(f"file_shrink_guard: FAIL -- {len(bad)} of {len(a.paths)} path(s) shrank; if this is a "
              f"legitimate regen/restore, say so in the commit message (shrink/regen/restore/AX2-SHRINK)")
        return 1
    if missing:
        return 2
    print(f"file_shrink_guard: ok -- {len(a.paths)} path(s) checked, none shrank")
    return 0


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""Offline test for tools/file_shrink_guard.py (CLAUDE.md Usage 8a; RETRO-2026-09-26i item 1, the PR-LAND-3
incident of 26 Sept 2026). Pure functions checked directly against synthetic text and a real temp git repo
for the CLI path -- no network.

Covers, with the PR-LAND-3 numbers themselves as the regression case: (1) a 26-line TSV replaced by 1 line
"PLACEHOLDER" must FAIL; (2) the same 26-line TSV edited down to 24 lines (a legitimate row removal) must
PASS; (3) a commit message containing "AX2-SHRINK" or "regen" exempts an otherwise-failing shrink regardless
of the ratio; (4) a brand-new path (nothing at the compared ref) is never a shrink; (5) the CLI end-to-end
against a real temp git repo, both the failing and the exempted case.

Run: python3 tools/tests/test_file_shrink_guard.py
"""
import os
import subprocess
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import file_shrink_guard as fsg  # noqa: E402

fails = 0


def report(name, ok, detail=""):
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), name, detail)


# --- 1/2. is_shrink() on the PR-LAND-3 numbers -------------------------------------------------
TSV_26 = "\n".join(f"row{i}\tval{i}" for i in range(26)) + "\n"
PLACEHOLDER = "PLACEHOLDER\n"
TSV_24 = "\n".join(f"row{i}\tval{i}" for i in range(24)) + "\n"

report("26-line TSV has line_count 26", fsg.line_count(TSV_26) == 26, fsg.line_count(TSV_26))
report("1-line PLACEHOLDER has line_count 1", fsg.line_count(PLACEHOLDER) == 1, fsg.line_count(PLACEHOLDER))

result = fsg.check_file("LOCAL-QUEUE.tsv", TSV_26, PLACEHOLDER)
report("26 -> 1 line (PLACEHOLDER) is flagged as a shrink", result == ("LOCAL-QUEUE.tsv", 26, 1), result)

result = fsg.check_file("LOCAL-QUEUE.tsv", TSV_26, TSV_24)
report("26 -> 24 lines (a legitimate row edit) is not flagged", result is None, result)

# --- 3. exempt() and the commit-message override --------------------------------------------
report("exempt() true for a message naming AX2-SHRINK", fsg.exempt("AX2-SHRINK: image folder trim") is True)
report("exempt() true for a message naming regen", fsg.exempt("regen: rebuild manifest from source") is True)
report("exempt() true for a message naming restore", fsg.exempt("restore ciphers/x/AUDIT.md verbatim") is True)
report("exempt() false for an unrelated message", fsg.exempt("PR-LAND-3: land JSTOR hits") is False)
report("exempt() false for no message at all", fsg.exempt(None) is False)
report("exempt() is case-insensitive", fsg.exempt("SHRINK the file") is True)

# --- 4. a brand-new path (nothing at the compared ref) is never a shrink -----------------------
result = fsg.check_file("brand-new.tsv", None, PLACEHOLDER)
report("a path absent at the ref (new file) is never a shrink", result is None, result)

# --- 5. CLI end-to-end against a real temp git repo ---------------------------------------------
with tempfile.TemporaryDirectory() as d:
    def git(*args):
        return subprocess.run(["git", *args], cwd=d, capture_output=True, text=True, check=True)

    git("init", "-q")
    git("config", "user.email", "test@example.com")
    git("config", "user.name", "test")

    path = os.path.join(d, "LOCAL-QUEUE.tsv")
    open(path, "w").write(TSV_26)
    git("add", "LOCAL-QUEUE.tsv")
    git("commit", "-q", "-m", "seed: 26-row queue")

    # 5a. collapse to PLACEHOLDER, plain commit message -> FAIL
    open(path, "w").write(PLACEHOLDER)
    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "file_shrink_guard.py"), "LOCAL-QUEUE.tsv",
         "--root", d, "--message", "PR-LAND-3: land JSTOR hits into LOCAL-QUEUE.tsv"],
        capture_output=True, text=True,
    )
    report("CLI exits 1 on an unexempted collapse", r.returncode == 1, r.stdout + r.stderr)
    report("CLI names the path and both counts", "LOCAL-QUEUE.tsv" in r.stdout and "26" in r.stdout and "1" in r.stdout, r.stdout)

    # 5b. same collapse, but the commit message is exempt -> exits 0
    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "file_shrink_guard.py"), "LOCAL-QUEUE.tsv",
         "--root", d, "--message", "AX2-SHRINK: intentional placeholder for a follow-up regen"],
        capture_output=True, text=True,
    )
    report("CLI exits 0 when the commit message is exempt", r.returncode == 0, r.stdout + r.stderr)

    # 5c. a legitimate 26 -> 24 edit, default message (no exemption needed) -> exits 0
    open(path, "w").write(TSV_24)
    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "file_shrink_guard.py"), "LOCAL-QUEUE.tsv", "--root", d],
        capture_output=True, text=True,
    )
    report("CLI exits 0 on a legitimate row-count edit", r.returncode == 0, r.stdout + r.stderr)

    # 5d. a path that does not exist at all in the working tree -> exit 2, MISSING
    r = subprocess.run(
        [sys.executable, os.path.join(ROOT, "tools", "file_shrink_guard.py"), "no-such-file.tsv", "--root", d],
        capture_output=True, text=True,
    )
    report("CLI exits 2 naming a missing path", r.returncode == 2 and "MISSING" in r.stdout, r.stdout + r.stderr)

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: file_shrink_guard.py catches the PR-LAND-3 shrink shape, passes a legitimate edit, and honors the "
      "shrink/regen/restore/AX2-SHRINK commit-message exemption, offline")

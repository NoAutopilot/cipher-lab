#!/usr/bin/env python3
"""Offline test for tools/system_map_check.py (SYSTEM-MAP, 26 Sept 2026, CLAUDE.md Usage 8a).

Builds a fake repository under a tmp dir (tools/*.py, a test file that must be ignored, runner prompts, root TSVs,
a CLAUDE.md with an 8a paragraph) and checks: a complete map passes (exit 0); a map missing one tool, one runner,
one TSV, one register or one 8a-only gate fails (exit 1) naming exactly that name; a missing SYSTEM.md exits 2;
tools/tests/ files are never required; 8a parsing stops at the next numbered item.

Run: python3 tools/tests/test_system_map_check.py
"""
import contextlib
import io
import os
import shutil
import sys
import tempfile

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import system_map_check as smc  # noqa: E402

fails = 0


def check(label, cond):
    global fails
    print(("ok   " if cond else "FAIL ") + label)
    if not cond:
        fails += 1


def write(path, text=""):
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8") as f:
        f.write(text)


def run(root, map_text=None):
    if map_text is not None:
        write(os.path.join(root, "SYSTEM.md"), map_text)
    buf = io.StringIO()
    with contextlib.redirect_stdout(buf):
        code = smc.main(["--root", root])
    return code, buf.getvalue()


CLAUDE = """# x
8. **Shared scripts.** `tools/not_a_gate_named_in_8.py` is item 8.
8a. **Rules become tools.** Precedents: `tools/alpha_check.py` (a gate), `tools/gate_only.py` (a gate whose file
   is absent from this fake tools/), and `tools/alpha_check.py` again.
9. **Next.** `tools/after_8a.py` must not be required.
"""

tmp = tempfile.mkdtemp()
try:
    write(os.path.join(tmp, "CLAUDE.md"), CLAUDE)
    write(os.path.join(tmp, "tools", "alpha_check.py"))
    write(os.path.join(tmp, "tools", "beta_solver.py"))
    write(os.path.join(tmp, "tools", "tests", "test_alpha_check.py"))
    write(os.path.join(tmp, "tools", "foo_runner_prompt.md"))
    write(os.path.join(tmp, "tools", "bar_runner_chatgpt_prompt.md"))
    write(os.path.join(tmp, "tools", "baz_runner_brief.md"))
    write(os.path.join(tmp, "tools", "unrelated_notes.md"))
    write(os.path.join(tmp, "ZETA-QUEUE.tsv"), "a\tb\n")

    names = [n for _, n in smc.required(tmp)]
    check("8a parsing takes names inside 8a only", "gate_only.py" in names and "after_8a.py" not in names
          and "not_a_gate_named_in_8.py" not in names)
    check("tests are not required", "test_alpha_check.py" not in names)
    check("chatgpt runner prompt is required", "bar_runner_chatgpt_prompt.md" in names)
    check("unrelated tools/*.md not required", "unrelated_notes.md" not in names)
    check("no duplicate names", len(names) == len(set(names)))

    full = "\n".join(names)
    code, out = run(tmp, full)
    check("complete map passes (exit 0)", code == 0 and "ok" in out)

    for drop in ["beta_solver.py", "baz_runner_brief.md", "ZETA-QUEUE.tsv", "hub-seed/ASSIGNMENTS.md", "gate_only.py"]:
        text = "\n".join(n for n in names if n != drop)
        code, out = run(tmp, text)
        check(f"missing {drop} fails naming it", code == 1 and f": {drop}" in out and out.count("MISSING") == 1)

    os.remove(os.path.join(tmp, "SYSTEM.md"))
    code, out = run(tmp)
    check("missing SYSTEM.md exits 2", code == 2)
finally:
    shutil.rmtree(tmp)

print(f"{'FAILED' if fails else 'passed'}: {fails} failure(s)")
sys.exit(1 if fails else 0)

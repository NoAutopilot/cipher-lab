#!/usr/bin/env python3
"""Offline test for tools/intake_gate_check.py (RETRO-2026-09-25h proposal 4).

Covers the two real-repo cases the proposal named -- antt-linhares-chave, corrected to `blocked`
after the Linhares intake-gate breach, must read blocked; two targets whose `open` verdict names
a standard edition with pages (thurloe-barriere-1654) or a full-text search (colbert26-lathuillerie-1644)
must pass -- plus synthetic fixtures for the directions the real repo doesn't currently hold: a bare
`open` with no citation (must fail, exit 1), a NOTES.md with no open/partial/blocked word at all (must
also fail, erring toward blocked on ambiguity), and `partial` with and without a citation (25 Sept 2026,
`partial` gated exactly like `open` -- clair349-este-guise-1556 and antt-msliv0638-brochado-1712 are the
real-repo cases, both `partial` with a citation, that used to exit 1 as ambiguous before this fix).
Run: python3 tools/tests/test_intake_gate_check.py"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import intake_gate_check as gate  # noqa: E402

fails = 0


def check_real(target, expect_code, expect_word_in_message):
    notes_path = os.path.join(ROOT, "ciphers", target, "NOTES.md")
    with open(notes_path, encoding="utf-8") as f:
        text = f.read()
    code, message = gate.check(text)
    ok = code == expect_code and expect_word_in_message in message
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), target, f"-> code={code} message={message!r}")


# antt-linhares-chave: corrected to `blocked` after the Linhares breach -- must read blocked, exit 0
check_real("antt-linhares-chave", 0, "blocked")

# two open verdicts naming a standard edition with pages, or a full-text search -- must pass, exit 0
check_real("thurloe-barriere-1654", 0, "open")
check_real("colbert26-lathuillerie-1644", 0, "open")

# two real-repo `partial` verdicts with a citation right on the verdict line -- must pass, exit 0
# (these were exiting 1 as ambiguous before partial was gated like open, 25 Sept 2026)
check_real("clair349-este-guise-1556", 0, "partial")
check_real("antt-msliv0638-brochado-1712", 0, "partial")

# synthetic: bare `open` with no citation nearby -- must fail, exit 1
SYNTH_OPEN_NO_CITATION = "open\n\n# A target with no citation\n\nNothing else here about editions or pages.\n"
code, message = gate.check(SYNTH_OPEN_NO_CITATION)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-no-citation", f"-> code={code} message={message!r}")

# synthetic: an open verdict whose citation is more than CONTEXT_LINES away -- must still fail
SYNTH_OPEN_FAR_CITATION = (
    "open\n" + "\n".join(f"filler line {i}" for i in range(gate.CONTEXT_LINES + 2))
    + "\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
)
code, message = gate.check(SYNTH_OPEN_FAR_CITATION)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-citation-too-far", f"-> code={code} message={message!r}")

# synthetic: an open verdict with a page citation right below it -- must pass
SYNTH_OPEN_WITH_PAGES = "open\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
code, message = gate.check(SYNTH_OPEN_WITH_PAGES)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-with-pages", f"-> code={code} message={message!r}")

# synthetic: `partial` with no citation nearby -- must fail, exit 1, same as bare open
SYNTH_PARTIAL_NO_CITATION = "partial\n\n# A target with no citation\n\nNothing else here about editions or pages.\n"
code, message = gate.check(SYNTH_PARTIAL_NO_CITATION)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-no-citation", f"-> code={code} message={message!r}")

# synthetic: `partial` with a page citation right below it -- must pass, exit 0
SYNTH_PARTIAL_WITH_PAGES = "partial\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
code, message = gate.check(SYNTH_PARTIAL_WITH_PAGES)
ok = code == 0 and "partial" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-with-pages", f"-> code={code} message={message!r}")

# synthetic: no open/partial/blocked word at all -- must fail, erring toward blocked
SYNTH_NO_VERDICT = "unclear\n\nSome prose that never uses the bare words open, partial or blocked as a line lead.\n"
code, message = gate.check(SYNTH_NO_VERDICT)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic no-verdict-word", f"-> code={code} message={message!r}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: intake_gate_check reads antt-linhares-chave as blocked, thurloe-barriere-1654 and "
      "colbert26-lathuillerie-1644 as compliant open verdicts, clair349-este-guise-1556 and "
      "antt-msliv0638-brochado-1712 as compliant partial verdicts, and errs toward blocked on the "
      "no-citation, far-citation and no-verdict-word synthetic cases")

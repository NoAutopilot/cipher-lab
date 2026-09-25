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

Also covers two further fixes from the same LANE CX handoff (25 Sept 2026): `found-solved` gated for
citation presence like `open`/`partial`; and an `open`/`partial` verdict whose citation window says a
named edition was NOT read (`unread`, `not read`, `could not open`, `paywalled`) must exit 1 even when
a real citation is also present nearby -- fr4687-paleologue-nevers before its correction is the
real-repo shape (a genuine full-text-search citation for one edition, alongside "Ferrari 1999 ... is
paywalled" for another). The word-boundary match must not fire on antt-msliv0638-brochado-1712's
"unreadable page-by-page" (that edition was read a different way this pass, and must keep passing).
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

# real repo: fr4687-paleologue-nevers is now `blocked` (corrected by the LANE CX orchestrator
# after the worker wrote `open` with an unread edition named two lines down) -- must read blocked
check_real("fr4687-paleologue-nevers", 0, "blocked")

# synthetic: `found-solved` with a citation nearby -- must pass, exit 0, labelled found-solved
SYNTH_FOUND_SOLVED_WITH_CITATION = (
    "found-solved\nBirch 1742 vol.2 pp.685-686 read from page images this pass, letter and key both present.\n"
)
code, message = gate.check(SYNTH_FOUND_SOLVED_WITH_CITATION)
ok = code == 0 and "found-solved" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic found-solved-with-citation", f"-> code={code} message={message!r}")

# synthetic: `found-solved` with no citation nearby -- must fail, exit 1, same as bare open
SYNTH_FOUND_SOLVED_NO_CITATION = "found-solved\n\n# No citation here\n\nJust an assertion, no edition or page named.\n"
code, message = gate.check(SYNTH_FOUND_SOLVED_NO_CITATION)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic found-solved-no-citation", f"-> code={code} message={message!r}")

# synthetic: `open` with a real citation for one edition, but another named edition marked
# unread/paywalled nearby -- must fail, exit 1, not pass on the strength of the other citation.
# This is the fr4687-paleologue-nevers-before-its-correction shape (rule: CLAUDE.md's Pipeline
# intake gate, "or that names an edition it could not open, is `blocked`, whatever word it uses").
SYNTH_OPEN_MIXED_CITATION_AND_UNREAD = (
    "open\nBoltanski 2006 pp.140-145 full-text search read by this worker, no hit; Ferrari 1999, "
    "the other named edition, is paywalled (academia.edu 403) and queued.\n"
)
code, message = gate.check(SYNTH_OPEN_MIXED_CITATION_AND_UNREAD)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-mixed-citation-and-unread", f"-> code={code} message={message!r}")

# synthetic: `partial` with a citation but a nearby "could not open" -- must fail, exit 1
SYNTH_PARTIAL_COULD_NOT_OPEN = (
    "partial\nEdition A pp.10-12 read in full; Edition B could not open (paywalled), queued as next step.\n"
)
code, message = gate.check(SYNTH_PARTIAL_COULD_NOT_OPEN)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-could-not-open", f"-> code={code} message={message!r}")

# synthetic: `open` with a citation and a nearby "not read" -- must fail, exit 1
SYNTH_OPEN_NOT_READ = "open\nEdition A pp.5-9 read in full; Edition B, the sender's own letters, not read this pass.\n"
code, message = gate.check(SYNTH_OPEN_NOT_READ)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-not-read", f"-> code={code} message={message!r}")

# regression: "unreadable" must NOT trip the word-boundary negative match (antt-msliv0638-brochado-1712
# reads through a route other than page-by-page and must still pass at exit 0 -- covered above by
# check_real, but pinned here directly against the substring-vs-word-boundary risk)
SYNTH_OPEN_UNREADABLE_NOT_UNREAD = (
    "open\nEdition A (NO_PAGES/no-preview, so unreadable page-by-page) was read this pass through the "
    "search-within-volume endpoint, pp.12 and pp.40 confirmed present.\n"
)
code, message = gate.check(SYNTH_OPEN_UNREADABLE_NOT_UNREAD)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-unreadable-is-not-unread", f"-> code={code} message={message!r}")

# real repo: huntington-luzerne-destouches-1781, lambeth-bacon-649 and lambeth-casenowe-1586 all say
# "not read cover to cover" -- the established repo idiom for a compliant full-text/phrase-search
# citation (CLAUDE.md's gate names "the pages or full-text search actually read" as sufficient), not
# an inaccessible edition. Must keep passing at exit 0, not trip the new "not read" negative match.
check_real("huntington-luzerne-destouches-1781", 0, "open")
check_real("lambeth-bacon-649", 0, "open")
check_real("lambeth-casenowe-1586", 0, "open")

# synthetic: pin the same idiom directly against the negative-phrase regex
SYNTH_OPEN_NOT_READ_COVER_TO_COVER = (
    "open\nEdition A pp.10-20 (queried by full-text search, not read cover to cover) names no match.\n"
)
code, message = gate.check(SYNTH_OPEN_NOT_READ_COVER_TO_COVER)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-not-read-cover-to-cover", f"-> code={code} message={message!r}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: intake_gate_check reads antt-linhares-chave and fr4687-paleologue-nevers as blocked, "
      "thurloe-barriere-1654 and colbert26-lathuillerie-1644 as compliant open verdicts, "
      "clair349-este-guise-1556 and antt-msliv0638-brochado-1712 as compliant partial verdicts, "
      "gates found-solved for citation presence like open/partial, and errs toward blocked on the "
      "no-citation, far-citation, no-verdict-word and unread/not-read/could-not-open/paywalled "
      "synthetic cases (without tripping on the 'unreadable' substring)")

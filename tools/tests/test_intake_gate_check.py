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

Also covers a third fix (25 Sept 2026, QA/2026-09-25-1740.md failure 2): `solved`, `closed-negative`
and `offline-only` are now recognised terminal verdicts, exiting 0 labelled with their own word and
needing no citation -- antt-fcc-costacabral-1865 (`solved` since 17:03) and thurloe-barriere-1654
(`closed-negative` since 17:18, ahead of a stale `open` correction lower in the file) are the real-repo
cases that used to exit 1 (or resolve to the wrong stale word) before this fix. A synthetic case pins
that a verdict word appearing only inside prose, never as a line's leading word, still leaves a file
ambiguous.
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
    code, message = gate.check(text, require_web=False)
    ok = code == expect_code and expect_word_in_message in message
    global fails
    fails += not ok
    print(("PASS" if ok else "FAIL"), target, f"-> code={code} message={message!r}")


# antt-linhares-chave: corrected to `blocked` after the Linhares breach -- must read blocked, exit 0
check_real("antt-linhares-chave", 0, "blocked")

# thurloe-barriere-1654's current top-of-file status word is `closed-negative` (set 25 Sept 2026
# 17:18 UTC, after the `open` correction below it) -- terminal, exit 0, needs no citation. Before
# this fix `closed-negative` was unrecognised, so find_verdict fell through to the stale `open`
# correction lower in the file; this is the exact real-repo case of the bug this fix targets.
check_real("thurloe-barriere-1654", 0, "closed-negative")
check_real("colbert26-lathuillerie-1644", 0, "partial")  # status open -> partial; expectation updated 9 Oct 2026 (ANON-PILE-RULE)

# two real-repo `partial` verdicts with a citation right on the verdict line -- must pass, exit 0
# (these were exiting 1 as ambiguous before partial was gated like open, 25 Sept 2026)
check_real("clair349-este-guise-1556", 0, "found-solved")  # status moved partial -> found-solved; expectation updated 28 Sept 2026 (CHECK-SOLVED-WEB), was failing before that change
check_real("antt-msliv0638-brochado-1712", 0, "partial")

# synthetic: bare `open` with no citation nearby -- must fail, exit 1
SYNTH_OPEN_NO_CITATION = "open\n\n# A target with no citation\n\nNothing else here about editions or pages.\n"
code, message = gate.check(SYNTH_OPEN_NO_CITATION, require_web=False)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-no-citation", f"-> code={code} message={message!r}")

# synthetic: an open verdict whose citation is more than CONTEXT_LINES away -- must still fail
SYNTH_OPEN_FAR_CITATION = (
    "open\n" + "\n".join(f"filler line {i}" for i in range(gate.CONTEXT_LINES + 2))
    + "\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
)
code, message = gate.check(SYNTH_OPEN_FAR_CITATION, require_web=False)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-citation-too-far", f"-> code={code} message={message!r}")

# synthetic: an open verdict with a page citation right below it -- must pass
SYNTH_OPEN_WITH_PAGES = "open\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
code, message = gate.check(SYNTH_OPEN_WITH_PAGES, require_web=False)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-with-pages", f"-> code={code} message={message!r}")

# synthetic: `partial` with no citation nearby -- must fail, exit 1, same as bare open
SYNTH_PARTIAL_NO_CITATION = "partial\n\n# A target with no citation\n\nNothing else here about editions or pages.\n"
code, message = gate.check(SYNTH_PARTIAL_NO_CITATION, require_web=False)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-no-citation", f"-> code={code} message={message!r}")

# synthetic: `partial` with a page citation right below it -- must pass, exit 0
SYNTH_PARTIAL_WITH_PAGES = "partial\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
code, message = gate.check(SYNTH_PARTIAL_WITH_PAGES, require_web=False)
ok = code == 0 and "partial" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-with-pages", f"-> code={code} message={message!r}")

# synthetic: no open/partial/blocked word at all -- must fail, erring toward blocked
SYNTH_NO_VERDICT = "unclear\n\nSome prose that never uses the bare words open, partial or blocked as a line lead.\n"
code, message = gate.check(SYNTH_NO_VERDICT, require_web=False)
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
code, message = gate.check(SYNTH_FOUND_SOLVED_WITH_CITATION, require_web=False)
ok = code == 0 and "found-solved" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic found-solved-with-citation", f"-> code={code} message={message!r}")

# synthetic: `found-solved` with no citation nearby -- must fail, exit 1, same as bare open
SYNTH_FOUND_SOLVED_NO_CITATION = "found-solved\n\n# No citation here\n\nJust an assertion, no edition or page named.\n"
code, message = gate.check(SYNTH_FOUND_SOLVED_NO_CITATION, require_web=False)
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
code, message = gate.check(SYNTH_OPEN_MIXED_CITATION_AND_UNREAD, require_web=False)
ok = code == 1 and "blocked" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-mixed-citation-and-unread", f"-> code={code} message={message!r}")

# synthetic: `partial` with a citation but a nearby "could not open" -- must fail, exit 1
SYNTH_PARTIAL_COULD_NOT_OPEN = (
    "partial\nEdition A pp.10-12 read in full; Edition B could not open (paywalled), queued as next step.\n"
)
code, message = gate.check(SYNTH_PARTIAL_COULD_NOT_OPEN, require_web=False)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic partial-could-not-open", f"-> code={code} message={message!r}")

# synthetic: `open` with a citation and a nearby "not read" -- must fail, exit 1
SYNTH_OPEN_NOT_READ = "open\nEdition A pp.5-9 read in full; Edition B, the sender's own letters, not read this pass.\n"
code, message = gate.check(SYNTH_OPEN_NOT_READ, require_web=False)
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
code, message = gate.check(SYNTH_OPEN_UNREADABLE_NOT_UNREAD, require_web=False)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-unreadable-is-not-unread", f"-> code={code} message={message!r}")

# real repo: huntington-luzerne-destouches-1781, lambeth-bacon-649 and lambeth-casenowe-1586 all say
# "not read cover to cover" -- the established repo idiom for a compliant full-text/phrase-search
# citation (CLAUDE.md's gate names "the pages or full-text search actually read" as sufficient), not
# an inaccessible edition. Must keep passing at exit 0, not trip the new "not read" negative match.
check_real("huntington-luzerne-destouches-1781", 0, "found-solved")  # status moved to found-solved; updated 9 Oct 2026 (ANON-PILE-RULE)
# 2 Oct 2026 (RETRO-2026-10-02-account4 proposal 2): the two Lambeth folders carry `Status: open` on line 3 with
# their check-solved citation ("not read cover to cover") only at line 61 / line 49 -- the head-only rule now reads
# the line-3 word and finds no citation within CONTEXT_LINES of it, exit 1, where it used to skip to the cited
# `**open.**` lower down. That is the rule working (rule 5: the status word and its citation sit in the head);
# the folders need their citation carried up beside the status line (a check-solved/GAPS edit, not this tool's).
# The idiom itself stays pinned by the synthetic case below.
# 9 Oct 2026 (ANON-PILE-RULE): both folders have since carried their citation up beside line 3, so they now pass.
check_real("lambeth-bacon-649", 0, "open (line 3)")
check_real("lambeth-casenowe-1586", 0, "open (line 3)")

# synthetic: pin the same idiom directly against the negative-phrase regex
SYNTH_OPEN_NOT_READ_COVER_TO_COVER = (
    "open\nEdition A pp.10-20 (queried by full-text search, not read cover to cover) names no match.\n"
)
code, message = gate.check(SYNTH_OPEN_NOT_READ_COVER_TO_COVER, require_web=False)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-not-read-cover-to-cover", f"-> code={code} message={message!r}")

# real repo: antt-fcc-costacabral-1865, status `solved` since 25 Sept 2026 17:03 -- the exact
# case QA/2026-09-25-1740.md failure 2 found exiting 1 as ambiguous before this fix.
check_real("antt-fcc-costacabral-1865", 0, "solved")

# synthetic: `solved` needs no citation nearby -- must pass, exit 0, labelled solved
SYNTH_SOLVED_NO_CITATION = "solved\n\nNo edition or page named anywhere near this line.\n"
code, message = gate.check(SYNTH_SOLVED_NO_CITATION, require_web=False)
ok = code == 0 and "solved" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic solved-no-citation", f"-> code={code} message={message!r}")

# synthetic: `closed-negative` needs no citation nearby -- must pass, exit 0, labelled closed-negative
SYNTH_CLOSED_NEGATIVE_NO_CITATION = "closed-negative\n\nNo edition or page named anywhere near this line.\n"
code, message = gate.check(SYNTH_CLOSED_NEGATIVE_NO_CITATION, require_web=False)
ok = code == 0 and "closed-negative" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic closed-negative-no-citation", f"-> code={code} message={message!r}")

# synthetic: `offline-only` needs no citation nearby -- must pass, exit 0, labelled offline-only
SYNTH_OFFLINE_ONLY_NO_CITATION = "offline-only\n\nNo edition or page named anywhere near this line.\n"
code, message = gate.check(SYNTH_OFFLINE_ONLY_NO_CITATION, require_web=False)
ok = code == 0 and "offline-only" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic offline-only-no-citation", f"-> code={code} message={message!r}")

# synthetic: the only occurrence of a recognised verdict word sits inside prose, not as a line's
# leading word -- must still be ambiguous, exit 1, not mistaken for a real verdict.
SYNTH_VERDICT_WORD_IN_PROSE = (
    "# A target with no leading verdict line\n\n"
    "This letter was solved by the sender's own gloss, but that word never leads a line here, "
    "and the target is not closed-negative or offline-only either -- just prose mentioning those "
    "words in passing.\n"
)
code, message = gate.check(SYNTH_VERDICT_WORD_IN_PROSE, require_web=False)
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic verdict-word-in-prose-only", f"-> code={code} message={message!r}")

# head-only, labelled status line (2 Oct 2026, RETRO-2026-10-02-account4 proposal 2). Must catch: a labelled
# `- **Status:** partial (...)` on line 4 with a bare `offline-only (Bourdeau)` quotation on line 40 -- the exact
# intercepted-royalist-1646 shape (its line 137 quotes Bourdeau's status for the same shelfmark) -- reads
# `partial (line 4)`, never `offline-only`.
SYNTH_LABELLED_HEAD_QUOTED_TERMINAL = (
    "# Intercepted royalist letter\n\n"
    "- **Source:** BL Add MS 72438, f.9r.\n"
    "- **Status:** partial (2 Oct 2026, LIKELY-9: key no. 129 reads 190 of 735 tokens above 20 shuffled keys; "
    "Evelyn iv pp.178-179 read in full)\n"
    "- **Transcription:** ciphertext.txt holds only the opening.\n"
    + "".join(f"filler line {i}\n" for i in range(6, 40))
    + "offline-only (Bourdeau) -- cyphersolver/rupert reaches the same shelfmark but calls it offline-only.\n"
)
code, message = gate.check(SYNTH_LABELLED_HEAD_QUOTED_TERMINAL, require_web=False, require_premise=False)
ok = code == 0 and message.startswith("partial (line 4)") and "offline-only" not in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic labelled-status-line-4-with-quoted-terminal-line-40", f"-> code={code} message={message!r}")
# the same labelled shapes the repo actually uses must all read the labelled word
for shape in ("Status: open", "**Status: open**", "- **Status:** open.", "status: open", "Status: **open**"):
    code, message = gate.check(f"# T\n\n{shape}\nRibier 1666 vol.2 pp.140-145 read by this worker.\n", require_web=False, require_premise=False)
    ok = code == 0 and message.startswith("open (line 3)")
    fails += not ok
    print(("PASS" if ok else "FAIL"), f"synthetic labelled shape {shape!r}", f"-> code={code} message={message[:40]!r}")
# "Solver status (...): Partial by Aymeloglu" is a report of another solver's state, never this folder's word
code, message = gate.check("# T\n\n- **Solver status (19 Sept 2026):** Partial by Aymeloglu, 16 Sept 2026.\n", require_web=False)
ok = code == 1 and "verdict word found" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic solver-status-label-is-not-a-verdict", f"-> code={code} message={message[:60]!r}")
# Must catch: no status word anywhere in the first STATUS_HEAD_LINES lines, a bare one at line 137 -- exit 1
# naming the head, never `offline-only (line 137)`.
SYNTH_STATUS_ONLY_PAST_HEAD = (
    "# A folder whose status word sits past the head\n\n"
    + "".join(f"prose line {i} with no leading status word\n" for i in range(3, 137))
    + "offline-only with no key identified -- Bourdeau's call for the same shelfmark.\n"
)
assert SYNTH_STATUS_ONLY_PAST_HEAD.splitlines()[136].startswith("offline-only")
code, message = gate.check(SYNTH_STATUS_ONLY_PAST_HEAD, require_web=False)
ok = code == 1 and f"first {gate.STATUS_HEAD_LINES} lines" in message and "line 137" not in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic status-word-only-past-head-exit-1", f"-> code={code} message={message[:90]!r}")
# Must NOT block: a `blocked` correction just past the head after a `partial` inside it is still honoured
SYNTH_BLOCKED_JUST_PAST_HEAD = "# T\n" * 10 + "partial\n\nblocked (pending the edition) -- corrected 2 Oct 2026.\n"
code, message = gate.check(SYNTH_BLOCKED_JUST_PAST_HEAD, require_web=False)
ok = code == 0 and message.startswith("blocked (line 13)")
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic blocked-correction-just-past-head", f"-> code={code} message={message[:50]!r}")

# synthetic (26 Sept 2026, RETRO-2026-09-26c): a markdown-bold subheading whose leading word is a
# recognised verdict word, followed immediately by a comma, must NOT be mistaken for a rule-5
# status line -- thurloe-printed's pre-26-Sept-2026 shape (no bare status word anywhere, only
# "**Open, for the next owner (LANE W...**" as a subheading). Must fall through to "no verdict
# word found", exit 1, not read `open`.
SYNTH_HEADING_NOT_VERDICT = (
    "# Thurloe printed cipher letters\n\nsome prose\n\n**Open, for the next owner (LANE W...**\n"
)
code, message = gate.check(SYNTH_HEADING_NOT_VERDICT, require_web=False)
ok = code == 1 and "no" in message and "verdict word found" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic heading-not-verdict-thurloe-printed", f"-> code={code} message={message!r}")

# synthetic (26 Sept 2026, RETRO-2026-09-26b): a reused/re-cited search must still exit 0 (a
# citation is present) but print a soft WARNING, never change the exit code -- check-solved.md's
# own nuance is that a reused search that blocked nothing is a QA finding, not a gate failure.
SYNTH_OPEN_REUSED_SEARCH = (
    "open\nBourdeau's own 2026-09-21 search covers this edition; not re-run, per intake gate cost "
    "discipline. pp.10-12 named there.\n"
)
code, message = gate.check(SYNTH_OPEN_REUSED_SEARCH, require_web=False)
ok = code == 0 and "WARNING" in message and "reused/re-cited" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-reused-search-soft-warning", f"-> code={code} message={message!r}")

# real-repo negative (26 Sept 2026, RETRO-2026-09-26d item 6, V8-QA7 05:56): lope-hurtado-1522's NOTES.md
# describes a PRIOR, now-corrected verdict as having "re-cited" a stale search -- this worker itself opened
# the whole Calendar of State Papers Spain II djvu.txt, so this must NOT trip the reused-search warning.
with open(os.path.join(ROOT, "ciphers", "lope-hurtado-1522", "NOTES.md"), encoding="utf-8") as f:
    LOPE_HURTADO_TEXT = f.read()
code, message = gate.check(LOPE_HURTADO_TEXT, require_web=False)
ok = code == 0 and "WARNING" not in message
fails += not ok
print(("PASS" if ok else "FAIL"), "real lope-hurtado-1522 partial, no reused-search false positive",
      f"-> code={code} message={message!r}")

# synthetic: a full-text-search citation naming only one quoted term must still exit 0 but print
# a soft WARNING naming check-solved.md's whole-volume rule (matignon-mayenne-1586's shape).
SYNTH_OPEN_SINGLE_TERM_FTS = (
    'open\nfull-text search for "Bellebourg" returns 0 hits in the volume.\n'
)
code, message = gate.check(SYNTH_OPEN_SINGLE_TERM_FTS, require_web=False)
ok = code == 0 and "WARNING" in message and "one quoted term" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-single-term-fts-soft-warning", f"-> code={code} message={message!r}")

# synthetic: a full-text-search citation with the date, both names and the place (several quoted
# terms) must exit 0 with no soft warning at all -- the compliant shape check-solved.md now asks for.
SYNTH_OPEN_WHOLE_VOLUME_FTS = (
    'open\nfull-text search for "Bellebourg" returns 0 hits; also searched "1586" and "Mayenne" '
    'and "Matignon", each logged separately, all read in full.\n'
)
code, message = gate.check(SYNTH_OPEN_WHOLE_VOLUME_FTS, require_web=False)
ok = code == 0 and "WARNING" not in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic open-whole-volume-fts-no-warning", f"-> code={code} message={message!r}")

# Fourth fix (28 Sept 2026, CHECK-SOLVED-WEB): the web/blog-comment check.
WEB_CITED_OPEN = "open\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n"
code, message = gate.check(WEB_CITED_OPEN)
ok = code == 1 and "web and blog-comment" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic cited-open-no-web-check -> blocked", f"-> code={code}")

code, message = gate.check(WEB_CITED_OPEN + "\n## Web and blog check (CHECK-SOLVED-WEB, 28 Sept 2026)\n\nno hit.\n", require_premise=False)
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic cited-open-with-web-heading -> pass", f"-> code={code}")

# Fifth fix (2 Oct 2026, GATE-TOOL): the three-blog paragraph route is withdrawn -- the heading is required
code, message = gate.check(WEB_CITED_OPEN + "\n## Check-solved\n\nSearched Cipherbrain (klausis-krypto-kolumne), "
                           "the Cryptiana blog and its comments, and ciphermysteries.com: no reading.\n", require_premise=False)
ok = code == 1 and "web and blog-comment" in message
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic cited-open-three-blog-paragraph-no-heading -> blocked", f"-> code={code}")

# two of three blogs only is not the logged pass
code, message = gate.check(WEB_CITED_OPEN + "\nSearched Cipherbrain and the Cryptiana blog.\n")
ok = code == 1
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic cited-open-two-blogs-only -> blocked", f"-> code={code}")

# must NOT block a terminal verdict
code, message = gate.check("closed-negative\nnothing else.\n")
ok = code == 0
fails += not ok
print(("PASS" if ok else "FAIL"), "synthetic terminal-no-web-check -> pass", f"-> code={code}")

# real repo: the three live campaigns logged the pass on 28 Sept 2026; spinelli-beinecke-c1515 never did
for tgt in ("armstrong-madison-1808", "espagnol142-mercy-1648", "fr4715-f61-mayenne-1592"):
    with open(os.path.join(ROOT, "ciphers", tgt, "NOTES.md"), encoding="utf-8") as f:
        ok = gate.has_web_blog_check(f.read())
    fails += not ok
    print(("PASS" if ok else "FAIL"), tgt, "has the logged web/blog check")

# Fifth fix (2 Oct 2026, GATE-TOOL after A2-HDK): pasting the gate's own FAIL output must not satisfy either
# section test. FAIL_LINE is the shape pasted into hessen-daenemark-1672/NOTES.md (it names all three blogs).
FAIL_LINE = ("hessen-daenemark-1672: partial (line 1) has an edition citation but no logged open-web and blog-comment "
             "check (no 'Web and blog check' heading, no paragraph naming Cipherbrain, the Cryptiana blog and Cipher "
             "Mysteries) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, "
             "28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)")
PREMISE_FAIL = ("t: open (line 1) passes the citation and web/blog checks but has no '## Premise check' section -- "
                "run check-solved.md's adversarial Premise check")
GOOD_WEB = "\n## Web and blog check (w, 2 Oct 2026)\nCipherbrain, the Cryptiana blog and Cipher Mysteries searched: no hit.\n"
GOOD_PREMISE = "\n## Premise check (w, 2 Oct 2026)\n(a) not found (b) not found (c) not found (d) not found\n"
cases = [
    # must catch
    ("pasted FAIL line, bare", WEB_CITED_OPEN + "\n## Gate run\n\n" + FAIL_LINE + "\n", 1, "web and blog-comment"),
    ("pasted FAIL line, fenced", WEB_CITED_OPEN + "\n```\n$ python3 tools/intake_gate_check.py t\n" + FAIL_LINE + "\n```\n", 1, "web and blog-comment"),
    ("web heading inside a fenced paste", WEB_CITED_OPEN + "\n```\n## Web and blog check\nCipherbrain etc.\n```\n", 1, "web and blog-comment"),
    ("web heading with only pasted gate output under it", WEB_CITED_OPEN + "\n## Web and blog check\n" + FAIL_LINE + "\n## Next\nx\n", 1, "web and blog-comment"),
    ("premise heading inside a fenced paste", WEB_CITED_OPEN + GOOD_WEB + "\n```\n## Premise check\n(a) none\n```\n", 1, "Premise check"),
    ("premise heading with only pasted gate output under it", WEB_CITED_OPEN + GOOD_WEB + "\n## Premise check\n" + PREMISE_FAIL + "\n", 1, "Premise check"),
    # must NOT block: genuine sections that also quote an earlier gate FAIL
    ("genuine web+premise sections quoting an earlier FAIL", WEB_CITED_OPEN + "\n## Web and blog check (w, 2 Oct 2026)\n"
     "Earlier gate output, now answered:\n" + FAIL_LINE + "\nCipherbrain, the Cryptiana blog and Cipher Mysteries searched: no hit.\n"
     "\n## Premise check (w, 2 Oct 2026)\n```\n" + PREMISE_FAIL + "\n```\n(a) not found (b) not found (c) not found (d) not found\n", 0, "citation found"),
]
for name, text, want, needle in cases:
    code, message = gate.check(text)
    ok = code == want and needle in message
    fails += not ok
    print(("PASS" if ok else "FAIL"), "synthetic gate-quote:", name, f"-> code={code} message={message[:80]!r}")

if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("ok: intake_gate_check reads antt-linhares-chave and fr4687-paleologue-nevers as blocked, "
      "thurloe-barriere-1654 as a terminal closed-negative and colbert26-lathuillerie-1644 as a "
      "compliant open verdict, clair349-este-guise-1556 and antt-msliv0638-brochado-1712 as "
      "compliant partial verdicts, gates found-solved for citation presence like open/partial, "
      "treats solved/closed-negative/offline-only as terminal verdicts needing no citation "
      "(antt-fcc-costacabral-1865 real-repo case), and errs toward blocked on the no-citation, "
      "far-citation, no-verdict-word, verdict-word-in-prose-only and "
      "unread/not-read/could-not-open/paywalled synthetic cases (without tripping on the "
      "'unreadable' substring)")

# Premise check (2 Oct 2026): an open target with citation + web/blog check still fails without the section;
# passes with it; found-solved is never blocked by it.
WEBP = "\n\n## Web and blog check (w, 2 Oct 2026)\nCipherbrain, the Cryptiana blog and Cipher Mysteries searched.\n"
BASE = "open\nRibier 1666 vol.2 pp.140-145 read by this worker, letter absent.\n" + WEBP
code, message = gate.check(BASE)
assert code == 1 and "Premise check" in message, (code, message)
code, message = gate.check(BASE + "\n## Premise check (w, 2 Oct 2026)\n(a) not found (b) not found (c) not found (d) not found\n")
assert code == 0, (code, message)
code, message = gate.check(BASE.replace("open\n", "found-solved\n", 1))
assert code == 0 or "Premise" not in message, (code, message)
print("premise-check tests: ok")


# Anonymous-pile path (9 Oct 2026, ANON-PILE-RULE, ASKS 158): holder-based check-solved replaces the edition citation
# for an unattributed pile; an attributed target cannot use it.
SECTIONS = WEBP + "\n## Premise check (w, 9 Oct 2026)\n(a) not found (b) not found (c) not found (d) none: no recipient\n"
HOLDER_OK = ("open\n- **Pile:** anonymous\n- **Holder:** BnF, Français 3029, ff. 12-48, glyph set A (Greek-letter homophones)\n"
             "Check-solved by holder: DECODE, Cryptiana GL.htm and the unsolved lists, dbourdeau/cyphersolver and "
             "aaymeloglu/unsolved-ciphers checked, the BnF notice (Présentation, Bibliographie) read; no decipherment.\n"
             "Edition step: deferred until a sender is named.\n")
anon_cases = [
    # must NOT block: a complete holder-based citation on a marked anonymous pile
    ("anon-pile holder citation complete", HOLDER_OK + SECTIONS, 0, "anonymous pile"),
    # the verdict-line phrase marks the pile too
    ("anon-pile marked by verdict phrase", HOLDER_OK.replace("- **Pile:** anonymous\n", "unattributed pile, mostly cipher\n") + SECTIONS, 0, "anonymous pile"),
    # must catch: an anonymous pile naming no holder-side sources
    ("anon-pile with no holder sources", "open\n- **Pile:** anonymous\nA pile of cipher letters.\n" + SECTIONS, 1, "DECODE"),
    ("anon-pile missing deferral and repos", HOLDER_OK.replace("Edition step: deferred until a sender is named.\n", "")
     .replace("dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers checked, ", "") + SECTIONS, 1, "unsolved-ciphers"),
    # still needs the web/blog and premise sections
    ("anon-pile without premise section", HOLDER_OK + WEBP, 1, "Premise check"),
    # a pasted gate line naming the sources does not count
    ("anon-pile sources only in a fenced paste", "open\n- **Pile:** anonymous\n```\n" + HOLDER_OK + "```\n" + SECTIONS, 1, "anonymous pile"),
    # must catch: an attributed target trying the holder path
    ("attributed target deferring the edition", HOLDER_OK.replace("- **Pile:** anonymous\n", "- **Sender:** Paul de Foix\n") + SECTIONS, 1, "holder path is for anonymous piles"),
    ("pile marker beside a named sender", HOLDER_OK.replace("- **Pile:** anonymous\n", "- **Pile:** anonymous\n- **Sender:** Paul de Foix\n") + SECTIONS, 1, "a sender is named"),
    # must NOT block: an attributed target with a full edition citation (unchanged behaviour)
    ("attributed target with edition citation", BASE + "\n## Premise check (w)\n(a) none\n", 0, "edition/page or full-text-search citation"),
]
for name, text, want, needle in anon_cases:
    code, message = gate.check(text)
    ok = code == want and needle in message
    fails += not ok
    print(("PASS" if ok else "FAIL"), "synthetic", name, f"-> code={code} message={message[:110]!r}")
if fails:
    print(f"{fails} failure(s)")
    sys.exit(1)
print("anon-pile tests: ok")

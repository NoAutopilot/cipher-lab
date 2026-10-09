#!/usr/bin/env python3
"""Flag a target's NOTES.md open/partial/blocked/found-solved verdict as intake-gate-compliant
or not (RETRO-2026-09-25h proposal 4).

CLAUDE.md's Pipeline "Intake gate (25 Sept 2026)" rule says an `open` verdict whose sentence
does not name the standard edition and the pages or full-text search actually read, or that
names an edition it could not open, is `blocked`, whatever word it uses -- and the rule alone
did not stop three workers doing deep work on antt-linhares-chave while it still read `open`
(a QA pass caught it after the fact). This script is the mechanical check a lane orchestrator
runs and pastes before briefing any deep-work worker (transcription, key application,
cryptanalysis) on a target, so the gate does not depend on a model re-noticing the prose rule
under load. `partial` is treated exactly like `open` (25 Sept 2026, QA run 3): a partially-read
target still needs the same edition-plus-page-or-full-text citation to justify further deep
work, and clair349-este-guise-1556 and antt-msliv0638-brochado-1712 -- both `partial` with a
full check-solved citation on the verdict line -- were exiting 1 as ambiguous before this fix,
which is wrong; they should exit 0 the same way a cited `open` does.

Head-only, labelled status line (2 Oct 2026, RETRO-2026-10-02-account4 proposal 2, Usage 8a): the verdict
is read from the first STATUS_HEAD_LINES (12) lines only, and may carry a `Status:` label (`- **Status:**
partial`). Twice in one window (LIKELY-9, GAPS-intercepted-royalist) the gate read intercepted-royalist-1646
as `offline-only (line 137)` -- a quotation of Bourdeau's status for the same shelfmark -- while line 4 read
`- **Status:** partial`, because the labelled line did not match and the scan ran to the end of the file.
Must catch: a labelled status line in the head with a bare terminal word quoted further down (reads the head
line); a file whose only status word sits past the head (exit 1 naming the head). Must NOT block: the terminal
fixtures (`blocked`, `solved`, `closed-negative`, `offline-only` on line 1) and every cited open/partial
fixture already in the offline test. Offline test: tools/tests/test_intake_gate_check.py.

Two further fixes (25 Sept 2026, LANE CX handoff via STATUS.md):

1. `found-solved` is now a recognised verdict word, gated the same way as `open`/`partial`: a
   citation (edition/page or full-text-search phrase) nearby exits 0 labelled `found-solved`;
   no citation nearby exits 1, same as an uncited `open`.
2. An `open` or `partial` verdict whose citation window itself says the named edition was NOT
   read -- the words `unread`, `not read`, `could not open` or `paywalled` -- now exits 1, not
   0, even when a page number or full-text-search phrase is also present nearby. CLAUDE.md's
   rule reads "or that names an edition it could not open, is `blocked`", which is unconditional:
   naming one unread edition forces `blocked` even when another, cited edition in the same
   paragraph genuinely was read. fr4687-paleologue-nevers before its correction is the example
   this fix targets: line 2 reported a real full-text search of Boltanski 2006 (citation
   evidence present) alongside "Ferrari 1999, the other named edition, is paywalled" -- the old
   check passed this as a cited `open`; the rule says it must be `blocked`. The negative-phrase
   match uses word boundaries so it does not fire on words that merely contain one of these
   phrases as a substring (`unreadable` does not match `unread`, confirmed against
   antt-msliv0638-brochado-1712's "NO_PAGES/no-preview, so unreadable page-by-page" line, which
   must keep passing -- that edition *was* read, through a different route, this pass).

Third fix (25 Sept 2026, QA/2026-09-25-1740.md failure 2): the verdict regex knew only
`open|partial|blocked|found-solved`, so a NOTES.md whose status word is `solved`,
`closed-negative` or `offline-only` (CLAUDE.md rule 5's status vocabulary, ungated by the
intake-gate rule -- that rule only speaks to `open`) fell through to "no verdict word found"
and exited 1 as ambiguous (antt-fcc-costacabral-1865, status `solved` since 17:03 that day).
`solved`, `closed-negative` and `offline-only` are now recognised terminal verdicts, exiting 0
labelled with their own word and gated for citation evidence exactly like `blocked` -- the
intake gate has nothing to say about a target that is no longer in play.

Fourth fix (28 Sept 2026, CHECK-SOLVED-WEB, after spinelli-beinecke-c1515 was closed at N0): that letter had
been read in public on 24 Mar 2017 in the comment thread of a Cipherbrain post, which a single web search on
sender, recipient and date finds as its second result -- but the gate asked only for a printed-edition
citation, and our print-check tools (IA, Google Books, OpenAlex, CrossRef) cannot see blog comments. An
`open`, `partial` or `found-solved` verdict now also needs a logged open-web and blog-comment check anywhere in
NOTES.md: either a heading "Web and blog check" (the section `.claude/briefs/check-solved.md` step "Open web and
blog comment threads" writes), or one paragraph that names all three blogs (Cipherbrain / klausis-krypto-kolumne,
the Cryptiana blog / cryptiana.blogspot, and Cipher Mysteries / ciphermysteries). Scope, stated as rule 8a asks:
it is meant to catch a gated target whose NOTES.md never logged the web/blog pass at all (the Spinelli shape);
it must NOT block a terminal verdict (`blocked`, `solved`, `closed-negative`, `offline-only` -- nothing left to
gate), and it must NOT block a gated target that logged the pass in its own prose under another heading, as
long as that paragraph names the three blogs. It does not check the queries were good; the verifier does.

Fifth fix (2 Oct 2026, GATE-TOOL, after A2-HDK on hessen-daenemark-1672): the web/blog test was satisfied by
pasting this tool's own FAIL message into NOTES.md, because that message names all three blogs. Both section
tests now (a) ignore fenced code blocks and any line quoting this tool's command or diagnostic phrasing
(GATE_QUOTE_RE), and (b) require the section heading itself -- "Web and blog check" / "Premise check" -- with at
least one unquoted line under it; the three-blog-paragraph route above is withdrawn (no gated target passing on
2 Oct 2026 used it). Must catch: a NOTES.md whose only blog names are a pasted FAIL line (bare or fenced); a
heading inside a fenced paste; a heading with nothing under it but pasted gate output. Must NOT block: a genuine
"## Web and blog check" section that also quotes an earlier gate FAIL inside it, and the same for "## Premise
check". Offline tests: tools/tests/test_intake_gate_check.py.

Anonymous-pile path (9 Oct 2026, ANON-PILE-RULE; owner's yes on ASKS 158, CLAUDE.md Pipeline 2 "Anonymous piles"): an
unattributed, undated, mostly-cipher pile has no sender and so no edition to cite. A target whose NOTES.md head
(first STATUS_HEAD_LINES lines) carries `- **Pile:** anonymous`, or whose verdict window says "anonymous pile" /
"unattributed pile", passes the citation step on a HOLDER-based check-solved instead: the window or a "## Check-solved"
section names a folio range, the glyph set, DECODE, Cryptiana (GL.htm / the unsolved lists), both solver repositories
(cyphersolver and unsolved-ciphers) and the holder's own notice as read, and records the edition step as "deferred until
a sender is named". The web/blog and Premise check sections and the not-read test still apply unchanged.
Must catch: an anonymous pile whose verdict names no holder-side sources read (exit 1, the missing items listed); an
attributed target -- no pile marker, or a pile marker beside a head `Sender:` line naming someone -- trying to use the
holder path ("deferred until a sender is named" with no edition citation: exit 1, the normal gate applies).
Must NOT block: an attributed target with a full edition citation (behaviour unchanged). Offline tests:
tools/tests/test_intake_gate_check.py ("anon-pile" cases).

Usage:
  tools/intake_gate_check.py <target>
    <target> is either a path (ciphers/<name>) or a bare target name under ciphers/.

Exit 0: the verdict word found in NOTES.md is `blocked`, `solved`, `closed-negative` or
  `offline-only` (already terminal, nothing to gate), or it is `open`, `partial` or
  `found-solved` and the same NOTES.md names a standard edition together with a page number or
  a full-text-search phrase within a few lines of the verdict word, with no nearby phrase saying
  that (or another) named edition was not actually read.
  The gated verdicts also need the 'Web and blog check' heading (fourth and fifth fixes above) in NOTES.md.
Exit 1: the verdict is `open`, `partial` or `found-solved` with no such citation nearby, or with no
  'Web and blog check' heading (with an unquoted line under it) anywhere in NOTES.md, or
  `open`/`partial` with a citation but also a nearby phrase (`unread`, `not read`, `could not
  open`, `paywalled`) saying a named edition was not read -- CLAUDE.md's Pipeline intake gate
  says either shape must read `blocked` instead -- or no recognised verdict word (open, partial,
  blocked, found-solved, solved, closed-negative, offline-only) was found at all. Either way this
  errs toward blocked: an ambiguous NOTES.md is not treated as a pass.

This checks the citation is present near the verdict word; it does not itself verify the
citation is real or that the edition was genuinely read (that is still the check-solved
worker's and the verifier's job) -- it only catches the shape of breach RETRO-2026-09-25h found,
an `open` (or `partial`) verdict with no citation at all, or one naming an unread edition.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A verdict line, after stripping markdown list/heading markers, starts with the bare word
# (CLAUDE.md rule 5's status vocabulary) followed by a non-word character or end of line.
# `partial` and `found-solved` are gated like `open` (25 Sept 2026); `solved`, `closed-negative`
# and `offline-only` are terminal like `blocked` -- no citation needed (25 Sept 2026, this fix).
# The word may carry a `Status:` label in any of the repo's own spellings (`Status: open`, `**Status: open**`,
# `- **Status:** partial`, `status: partial`, `Status: **found-solved**`); the label is optional and only
# `status` qualifies -- `Solver status (19 Sept 2026): Partial by Aymeloglu` must not match, since that is a
# report of someone else's state, not this folder's rule-5 word.
VERDICT_RE = re.compile(
    r'^[\s\-*>#]*(?:[*_]*status[*_]*\s*:?[\s*_]*)?\b(open|partial|blocked|found-solved|solved|closed-negative|offline-only)\b',
    re.IGNORECASE,
)

# Rule 5 puts the status word in the first lines of NOTES.md; a status word matched further down is a
# quotation (intercepted-royalist-1646 line 137 quotes Bourdeau's `offline-only` for the same shelfmark while
# line 4 reads `- **Status:** partial`; LIKELY-9 and GAPS-intercepted-royalist, 2 Oct 2026, RETRO-2026-10-02-
# account4 proposal 2). Scan at most the first STATUS_HEAD_LINES lines for the verdict; past that, report
# "no status line in the head" and exit 1. The `blocked` correction lookahead (find_verdict) still runs from
# the line found, so a correction just past the head is honoured.
STATUS_HEAD_LINES = 12

def _is_heading_not_verdict(line, match_end):
    """True when the verdict word is followed immediately (after any closing markdown emphasis
    and whitespace) by a comma -- the shape of a descriptive subheading ('**Open, for the next
    owner (LANE W...**', thurloe-printed's pre-26-Sept-2026 line 15) rather than a rule-5 status
    declaration. Checked against every NOTES.md in the repo (26 Sept 2026, RETRO-2026-09-26c): no
    real verdict line, first-line or a nearby `blocked` correction alike, puts a comma directly
    after the word; only a subheading does."""
    rest = line[match_end:].lstrip(" *_")
    return rest.startswith(",")


# Verdicts that need no citation evidence: already compliant/terminal, nothing to gate.
TERMINAL_WORDS = ("blocked", "solved", "closed-negative", "offline-only")

CONTEXT_LINES = 6  # how many lines after the verdict line count as "nearby"

PAGE_RE = re.compile(r'\bpp?\.\s?\d|\bpages?\s+\d+|\bvol\.?\s*\d+|\bfo\.\s?\d|\bfolios?\s+\d+', re.IGNORECASE)
FULLTEXT_PHRASES = (
    "full-text search", "full text", "search-within", "search within",
    "read by this worker", "read in full", "grepped", "djvu",
    "read from page images", "be-api", "phrase search", "read and grepped",
)

# A nearby phrase saying a named edition was NOT read forces `blocked` even when a citation is
# also present (fr4687-paleologue-nevers before its correction). Word-bounded so `unreadable`
# does not match `unread` (antt-msliv0638-brochado-1712's "unreadable page-by-page", an edition
# that *was* read a different way this pass, must keep passing). `not read` excludes the
# established repo idiom "not read cover to cover" (huntington-luzerne-destouches-1781,
# lambeth-bacon-649, lambeth-casenowe-1586): that phrase reports the same accepted route
# CLAUDE.md's gate names as compliant -- "the pages or full-text search actually read" -- just
# being explicit that the worker phrase-searched rather than reading the whole volume page by
# page; it is the opposite of an edition the worker could not open at all.
NEGATIVE_RE = re.compile(
    r'\bunread\b|\bnot read\b(?!\s+cover\s+to\s+cover)|\bcould not open\b|\bpaywalled\b',
    re.IGNORECASE,
)

# Soft warnings (26 Sept 2026, RETRO-2026-09-26b): these do not change the exit code (check-solved.md's own
# nuance -- a reused search or a narrow one that blocked nothing is a QA finding, not always a gate failure --
# stays a human/verifier call), but both shapes have now been flagged once each by V7-QA5 in the same sweep, one
# of them (a single-quoted-term full-text search) a second occurrence of the V7-CL349 failure the whole-volume
# rule already exists for (matignon-mayenne-1586, 26 Sept 2026: searched only "Bellebourg", not the date or
# either correspondent's name).
REUSED_SEARCH_RE = re.compile(
    r'\bnot re-?run\b|\bre-?cited\b|\bcost discipline\b|\breusing\b.{0,20}\bsearch\b',
    re.IGNORECASE,
)
# A match describing a PRIOR, now-corrected verdict is not this pass's own reused search (lope-hurtado-1522,
# RETRO-2026-09-26d item 6, V8-QA7 05:56: "correcting the prior verdict, which re-cited Bourdeau's ... search
# instead of opening the edition" -- the worker itself opened the edition this pass; "re-cited" describes the
# OLD verdict being fixed, not this citation). Checked in the 80 characters immediately before the match.
CORRECTION_CONTEXT_RE = re.compile(
    r'\b(?:prior|previous|earlier|old|stale)\s+verdict\b|\bcorrecting\b|\bcorrected from\b',
    re.IGNORECASE,
)
SINGLE_TERM_FTS_RE = re.compile(
    r'\b(?:full-text search|fts|searched)\b[^.]{0,80}\bfor\b\s+"[^"]+"\s+(?:returns?|found|gave)',
    re.IGNORECASE,
)


def soft_warnings(context):
    """Non-blocking flags for check-solved.md corner-cuts V7-QA5 found 26 Sept 2026 -- printed alongside the
    exit-code message, never changing it."""
    out = []
    reused_matches = [m for m in REUSED_SEARCH_RE.finditer(context)
                       if not CORRECTION_CONTEXT_RE.search(context[max(0, m.start() - 80):m.start()])]
    if reused_matches:
        out.append("WARNING: citation reads as a reused/re-cited search, not one this worker independently "
                    "opened (check-solved.md: quoting another party's summary does not satisfy the citation)")
    if SINGLE_TERM_FTS_RE.search(context) and context.count('"') <= 2:
        out.append("WARNING: full-text-search citation names only one quoted term -- check-solved.md's "
                    "'Whole volume, not one page range' rule (V7-CL349) asks for the date and both "
                    "correspondents' names alongside any place name")
    return out


def find_verdict(lines):
    """Return (word, line_index) for the effective verdict line, or (None, None).

    Scans top-down for the first recognised verdict line (open, partial, blocked, found-solved,
    solved, closed-negative, offline-only). If that line reads anything but `blocked` and a
    `blocked` line follows within CONTEXT_LINES, `blocked` is the effective verdict, whatever
    word came first -- this is the exact shape of antt-linhares-chave/NOTES.md (`partial` on
    line 1, then "blocked (pending ...) ... this verdict is corrected from `open` to `blocked`"
    starting two lines later): CLAUDE.md's own intake-gate wording is "is `blocked`, whatever
    word it uses", so a nearby correction to blocked always wins over the stale word before it,
    exactly as it did before `partial` was added to VERDICT_RE (25 Sept 2026).

    Only the first STATUS_HEAD_LINES lines are scanned for the verdict itself (2 Oct 2026, proposal 2 of
    RETRO-2026-10-02-account4): rule 5 puts the word in the first lines, and the first match below the head
    was twice a quotation of another solver's status (intercepted-royalist-1646 line 137). An optional
    `Status:` label before the word is accepted (VERDICT_RE).
    """
    for i, line in enumerate(lines[:STATUS_HEAD_LINES]):
        m = VERDICT_RE.match(line)
        if m and not _is_heading_not_verdict(line, m.end()):
            word = m.group(1).lower()
            if word != "blocked":
                for j in range(i + 1, min(i + 1 + CONTEXT_LINES, len(lines))):
                    m2 = VERDICT_RE.match(lines[j])
                    if m2 and not _is_heading_not_verdict(lines[j], m2.end()) and m2.group(1).lower() == "blocked":
                        return "blocked", j
            return word, i
    return None, None


def nearby_context(lines, idx):
    return "\n".join(lines[idx:idx + 1 + CONTEXT_LINES])


def has_citation_evidence(context):
    if PAGE_RE.search(context):
        return True
    low = context.lower()
    return any(phrase in low for phrase in FULLTEXT_PHRASES)


def negative_evidence_phrase(context):
    """Return the matched phrase (lowercase) if `context` says a named edition was not read,
    else None."""
    m = NEGATIVE_RE.search(context)
    return m.group(0).lower() if m else None


# Fourth fix (28 Sept 2026, CHECK-SOLVED-WEB): a logged open-web and blog-comment check.
# Fifth fix (2 Oct 2026, GATE-TOOL after A2-HDK): both section tests read the heading itself, outside any fenced
# code block, with at least one line of its own under it that is not a quotation of this tool's output.
WEB_HEADING_RE = re.compile(r'^\s*#+\s*Web and blog check\b', re.IGNORECASE)
PREMISE_HEADING_RE = re.compile(r'^\s*#+\s*Premise check\b', re.IGNORECASE)
ANY_HEADING_RE = re.compile(r'^\s*#+\s')
FENCE_RE = re.compile(r'^\s*(```|~~~)')
# Lines that quote this tool's own command or diagnostics (its FAIL messages name all three blogs and both
# section headings, so a pasted FAIL used to satisfy the very test it reports failing).
GATE_QUOTE_RE = re.compile(
    r'intake_gate_check'
    r"|no logged open-web and blog-comment check"
    r"|no 'Web and blog check' heading"
    r"|has no '## Premise check' section"
    r"|passes the citation and web/blog checks"
    r"|Open web and blog comment threads' step first",
    re.IGNORECASE,
)


def unquoted_lines(notes_text):
    """NOTES.md lines with fenced code blocks and lines quoting this tool's own output removed (blanked, so line
    structure survives). A pasted gate run -- in a fence or bare -- is evidence the gate was run, not that the
    check it asks for was done."""
    out, in_fence = [], False
    for line in notes_text.splitlines():
        if FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence or GATE_QUOTE_RE.search(line) else line)
    return out


def _has_section(notes_text, heading_re):
    lines = unquoted_lines(notes_text)
    for i, line in enumerate(lines):
        if heading_re.match(line):
            for body in lines[i + 1:]:
                if ANY_HEADING_RE.match(body):
                    break
                if body.strip():
                    return True
    return False


def has_web_blog_check(notes_text):
    """True when NOTES.md carries a real "Web and blog check" heading (check-solved.md step "Open web and blog
    comment threads") with a line of its own under it. A paragraph naming the three blogs no longer counts
    (2 Oct 2026): this tool's FAIL message names all three, so pasting it passed the gate (hessen-daenemark-1672,
    A2-HDK); no gated target passing on 2 Oct 2026 relied on the paragraph route."""
    return _has_section(notes_text, WEB_HEADING_RE)


def has_premise_check(notes_text):
    """True when NOTES.md carries the adversarial Premise check section (.claude/briefs/check-solved.md,
    2 Oct 2026): the folder's own mentioned decipherments opened, the other solvers' working files read,
    the physical neighbours of the leaf looked at, and recipient-side editions searched. Same quoting rule as
    has_web_blog_check: the heading in a fence, or a heading with only pasted gate output under it, does not count."""
    return _has_section(notes_text, PREMISE_HEADING_RE)



# Anonymous-pile path (9 Oct 2026, ANON-PILE-RULE, ASKS 158). See the module docstring.
PILE_MARK_RE = re.compile(r'^[\s\-*>]*[*_]*pile[*_]*\s*:?[\s*_]*anonymous\b', re.IGNORECASE)
PILE_PHRASE_RE = re.compile(r'\b(?:anonymous|unattributed)\s+pile\b', re.IGNORECASE)
SENDER_LINE_RE = re.compile(r'^[\s\-*>]*[*_]*sender[*_]*\s*:[\s*_]*(.*)$', re.IGNORECASE)
NO_SENDER_RE = re.compile(r'^\s*(?:$|-+\s*$|\?+|(?:none|unknown|anonymous|unattributed|n/?a|not named|none named)\b)', re.IGNORECASE)
DEFERRED_RE = re.compile(r'deferred until a sender is named', re.IGNORECASE)
CHECK_SOLVED_HEADING_RE = re.compile(r'^\s*#+\s*Check-solved\b', re.IGNORECASE)
FOLIO_RANGE_RE = re.compile(r'\bff?\.\s?\d+\s*[rv]?\s*[-\u2013]\s*\d+|\bfolios?\s+\d+\s*[rv]?\s*[-\u2013]\s*\d+'
                            r'|\bfo\.\s?\d+\s*[rv]?\s*[-\u2013]\s*\d+', re.IGNORECASE)
HOLDER_SOURCES = (
    ("folio range", lambda t: bool(FOLIO_RANGE_RE.search(t))),
    ("glyph set", lambda t: "glyph set" in t.lower()),
    ("DECODE", lambda t: bool(re.search(r'\bDECODE\b|de-crypt\.org', t))),
    ("Cryptiana (GL.htm / unsolved lists)", lambda t: "cryptiana" in t.lower()),
    ("cyphersolver", lambda t: "cyphersolver" in t.lower()),
    ("unsolved-ciphers", lambda t: "unsolved-ciphers" in t.lower()),
    ("holder's notice", lambda t: bool(re.search(r'\bnotice\b|pr[ée]sentation|finding[- ]aid', t, re.IGNORECASE))),
    ("edition step 'deferred until a sender is named'", lambda t: bool(DEFERRED_RE.search(t))),
)


def pile_status(lines, idx):
    """('anonymous', None) when the head marks an anonymous pile and names no sender; ('attributed', sender)
    when a pile marker sits beside a head Sender: line naming someone; (None, None) when not a pile."""
    head = lines[:STATUS_HEAD_LINES]
    marked = any(PILE_MARK_RE.match(l) for l in head) or bool(PILE_PHRASE_RE.search(nearby_context(lines, idx)))
    if not marked:
        return None, None
    for l in head:
        m = SENDER_LINE_RE.match(l)
        if m and not NO_SENDER_RE.match(m.group(1).strip(" *_")):
            return "attributed", m.group(1).strip(" *_")
    return "anonymous", None


def holder_citation_text(lines, idx):
    """The verdict window plus any '## Check-solved' section, quoted gate output removed."""
    clean = unquoted_lines("\n".join(lines))
    parts = [nearby_context(clean, idx)]
    for i, line in enumerate(clean):
        if CHECK_SOLVED_HEADING_RE.match(line):
            for body in clean[i + 1:]:
                if ANY_HEADING_RE.match(body):
                    break
                parts.append(body)
    return "\n".join(parts)


def missing_holder_sources(text):
    return [name for name, test in HOLDER_SOURCES if not test(text)]


def resolve_target(target):
    if os.path.isdir(target):
        return target
    candidate = os.path.join(ROOT, target)
    if os.path.isdir(candidate):
        return candidate
    candidate = os.path.join(ROOT, "ciphers", target)
    if os.path.isdir(candidate):
        return candidate
    return None


def check(notes_text, require_web=True, require_premise=None):
    """Pure check used by the offline test. Returns (exit_code, message).
    require_web=False runs only the citation gate (the offline tests of the first three fixes use it).
    require_premise defaults to require_web: an open/partial target with a passing citation and web/blog
    check still exits 1 until a "## Premise check" section exists (2 Oct 2026: of four likely-solves first
    tests a verifier later classed N0, two had their decipherment in the folder's own notes, in the other
    solver's working files or bound beside the leaf -- things a pre-reading adversarial pass finds).
    Must NOT block: terminal statuses (solved, closed-negative, offline-only, blocked) and found-solved."""
    lines = notes_text.splitlines()
    word, idx = find_verdict(lines)
    if word is None:
        return 1, (
            "no open/partial/blocked/found-solved/solved/closed-negative/offline-only verdict "
            f"word found in the first {STATUS_HEAD_LINES} lines of NOTES.md (rule 5: the status word is in the "
            "first lines; a match further down is a quotation, not this folder's status) -- ambiguous, treat as blocked"
        )
    if word in TERMINAL_WORDS:
        return 0, f"{word} (line {idx + 1}) -- already terminal, nothing to gate"
    # word in ("open", "partial", "found-solved") -- gated identically for citation presence
    context = nearby_context(lines, idx)
    if word != "found-solved":
        neg = negative_evidence_phrase(context)
        if neg is not None:
            return 1, (
                f"{word} (line {idx + 1}) names an edition not read ({neg!r} within {CONTEXT_LINES} lines) -- "
                f"CLAUDE.md's Pipeline intake gate says this must read `blocked` instead"
            )
    pile, sender = pile_status(lines, idx)
    holder_ok = False
    if pile == "anonymous":
        missing = missing_holder_sources(holder_citation_text(lines, idx))
        if missing:
            return 1, (
                f"{word} (line {idx + 1}) is an anonymous pile but its holder-based check-solved does not name: "
                f"{', '.join(missing)} -- CLAUDE.md Pipeline 2 'Anonymous piles' (ASKS 158); otherwise `blocked`"
            )
        holder_ok = True
    elif not has_citation_evidence(context) and DEFERRED_RE.search("\n".join(unquoted_lines(notes_text))):
        why = (f"a sender is named ({sender!r})" if pile == "attributed"
               else "the head carries no '- **Pile:** anonymous' marker")
        return 1, (
            f"{word} (line {idx + 1}) defers the edition step but {why} -- the holder path is for anonymous piles "
            f"only; the normal gate applies: name the standard edition and the pages or full-text search read"
        )
    if holder_ok or has_citation_evidence(context):
        if require_web and not has_web_blog_check(notes_text):
            return 1, (
                f"{word} (line {idx + 1}) has an edition citation but no logged open-web and blog-comment check "
                f"(no 'Web and blog check' heading with a line of its own under it; pasted gate output does not count) -- run check-solved.md's 'Open web and blog comment threads' step first (CHECK-SOLVED-WEB, "
                f"28 Sept 2026: spinelli-beinecke-c1515 was read in a Cipherbrain comment thread in 2017)"
            )
        if require_premise is None:
            require_premise = require_web
        if require_premise and word in ("open", "partial") and not has_premise_check(notes_text):
            return 1, (
                f"{word} (line {idx + 1}) passes the citation and web/blog checks but has no '## Premise check' "
                f"section -- run check-solved.md's adversarial Premise check (mentioned decipherments opened, other "
                f"solvers' working files, neighbouring leaves, recipient-side editions) before any first test"
            )
        msg = (f"{word} (line {idx + 1}) -- anonymous pile: holder-based check-solved citation found, edition step deferred"
               if holder_ok else
               f"{word} (line {idx + 1}) -- edition/page or full-text-search citation found within {CONTEXT_LINES} lines")
        for w in soft_warnings(context):
            msg += f"\n{w}"
        return 0, msg
    return 1, (
        f"{word} (line {idx + 1}) with no standard-edition citation (page number or full-text-search phrase) "
        f"within {CONTEXT_LINES} lines -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead"
    )


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("target", help="path to ciphers/<name> or a bare target name")
    args = ap.parse_args(argv)

    target_dir = resolve_target(args.target)
    if target_dir is None:
        print(f"no such target directory: {args.target}")
        return 1
    notes_path = os.path.join(target_dir, "NOTES.md")
    if not os.path.isfile(notes_path):
        print(f"no NOTES.md in {target_dir} -- ambiguous, treat as blocked")
        return 1

    with open(notes_path, encoding="utf-8") as f:
        text = f.read()

    code, message = check(text)
    print(f"{args.target}: {message}")
    return code


if __name__ == "__main__":
    sys.exit(main())

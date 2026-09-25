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

Usage:
  tools/intake_gate_check.py <target>
    <target> is either a path (ciphers/<name>) or a bare target name under ciphers/.

Exit 0: the verdict word found in NOTES.md is `blocked`, `solved`, `closed-negative` or
  `offline-only` (already terminal, nothing to gate), or it is `open`, `partial` or
  `found-solved` and the same NOTES.md names a standard edition together with a page number or
  a full-text-search phrase within a few lines of the verdict word, with no nearby phrase saying
  that (or another) named edition was not actually read.
Exit 1: the verdict is `open`, `partial` or `found-solved` with no such citation nearby, or
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
VERDICT_RE = re.compile(
    r'^[\s\-*>#]*\b(open|partial|blocked|found-solved|solved|closed-negative|offline-only)\b',
    re.IGNORECASE,
)

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
    """
    for i, line in enumerate(lines):
        m = VERDICT_RE.match(line)
        if m:
            word = m.group(1).lower()
            if word != "blocked":
                for j in range(i + 1, min(i + 1 + CONTEXT_LINES, len(lines))):
                    m2 = VERDICT_RE.match(lines[j])
                    if m2 and m2.group(1).lower() == "blocked":
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


def check(notes_text):
    """Pure check used by the offline test. Returns (exit_code, message)."""
    lines = notes_text.splitlines()
    word, idx = find_verdict(lines)
    if word is None:
        return 1, (
            "no open/partial/blocked/found-solved/solved/closed-negative/offline-only verdict "
            "word found in NOTES.md -- ambiguous, treat as blocked"
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
    if has_citation_evidence(context):
        return 0, f"{word} (line {idx + 1}) -- edition/page or full-text-search citation found within {CONTEXT_LINES} lines"
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

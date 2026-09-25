#!/usr/bin/env python3
"""Flag a target's NOTES.md open/blocked verdict as intake-gate-compliant or not
(RETRO-2026-09-25h proposal 4).

CLAUDE.md's Pipeline "Intake gate (25 Sept 2026)" rule says an `open` verdict whose sentence
does not name the standard edition and the pages or full-text search actually read, or that
names an edition it could not open, is `blocked`, whatever word it uses -- and the rule alone
did not stop three workers doing deep work on antt-linhares-chave while it still read `open`
(a QA pass caught it after the fact). This script is the mechanical check a lane orchestrator
runs and pastes before briefing any deep-work worker (transcription, key application,
cryptanalysis) on a target, so the gate does not depend on a model re-noticing the prose rule
under load.

Usage:
  tools/intake_gate_check.py <target>
    <target> is either a path (ciphers/<name>) or a bare target name under ciphers/.

Exit 0: the verdict word found in NOTES.md is `blocked` (already compliant, nothing to gate),
  or it is `open` and the same NOTES.md names a standard edition together with a page number
  or a full-text-search phrase within a few lines of the verdict word.
Exit 1: the verdict is `open` with no such citation nearby -- CLAUDE.md's Pipeline intake gate
  says this must read `blocked` instead -- or no open/blocked verdict word was found at all.
  Either way this errs toward blocked: an ambiguous NOTES.md is not treated as a pass.

This checks the citation is present near the verdict word; it does not itself verify the
citation is real or that the edition was genuinely read (that is still the check-solved
worker's and the verifier's job) -- it only catches the shape of breach RETRO-2026-09-25h found,
an `open` verdict with no citation at all.
"""
import argparse
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# A verdict line, after stripping markdown list/heading markers, starts with the bare word
# (CLAUDE.md rule 5's status vocabulary) followed by a non-word character or end of line.
VERDICT_RE = re.compile(r'^[\s\-*>#]*\b(open|blocked)\b', re.IGNORECASE)

CONTEXT_LINES = 6  # how many lines after the verdict line count as "nearby"

PAGE_RE = re.compile(r'\bpp?\.\s?\d|\bpages?\s+\d+|\bvol\.?\s*\d+|\bfo\.\s?\d|\bfolios?\s+\d+', re.IGNORECASE)
FULLTEXT_PHRASES = (
    "full-text search", "full text", "search-within", "search within",
    "read by this worker", "read in full", "grepped", "djvu",
    "read from page images", "be-api", "phrase search", "read and grepped",
)


def find_verdict(lines):
    """Return (word, line_index) for the first line matching VERDICT_RE, or (None, None)."""
    for i, line in enumerate(lines):
        m = VERDICT_RE.match(line)
        if m:
            return m.group(1).lower(), i
    return None, None


def nearby_context(lines, idx):
    return "\n".join(lines[idx:idx + 1 + CONTEXT_LINES])


def has_citation_evidence(context):
    if PAGE_RE.search(context):
        return True
    low = context.lower()
    return any(phrase in low for phrase in FULLTEXT_PHRASES)


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
        return 1, "no open/blocked verdict word found in NOTES.md -- ambiguous, treat as blocked"
    if word == "blocked":
        return 0, f"blocked (line {idx + 1}) -- already compliant, nothing to gate"
    # word == "open"
    context = nearby_context(lines, idx)
    if has_citation_evidence(context):
        return 0, f"open (line {idx + 1}) -- edition/page or full-text-search citation found within {CONTEXT_LINES} lines"
    return 1, (
        f"open (line {idx + 1}) with no standard-edition citation (page number or full-text-search phrase) "
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

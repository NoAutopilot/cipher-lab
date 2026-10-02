#!/usr/bin/env python3
"""Finish or name the blocker: check the "## Remaining gaps" and "## Escalation" sections of a `partial`
target's NOTES.md (CLAUDE.md rule 5, "Finish or name the blocker", 1 Oct 2026, from D. Bourdeau's practice:
github.com/dbourdeau/cyphersolver CLAUDE.md and writeup skill section 0a, snapshotted unmodified at
sources/cyphersolver/2026-10-01/; his text is CC BY 4.0, this tool is written here, not copied from his code).

    python3 tools/gaps_check.py <target> [<target> ...]
    python3 tools/gaps_check.py --all            # every target whose NOTES.md status is `partial`
    python3 tools/gaps_check.py --all --ciphers-dir DIR

Why it exists. "Read in part" had become a default: on 1 Oct 2026, 34 targets read `partial`, most with a written
next step nobody ran. Bourdeau stops at a partial reading only when every unread piece is blocked by something outside
the session, and otherwise works through a fixed escalation ladder (siblings, clear pages, known keys, print, key
rebuild, retry) before writing up; on espagnol142-mercy-1648 that ladder (an image check of out-of-key tokens and
the clear sibling instructions on ff. 20r/21r) took our reading to 98.5%. This tool makes the stopping point
explicit and parseable.

The format it parses (the LAST "## Remaining gaps..." and the LAST "## Escalation..." heading in the file; each
section runs to the next "#"/"##" heading or end of file):

    ## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
    Read so far: <measured fraction with its source; or "unmeasured" plus why>
    - <piece> - blocker: <blocker>; <why, with the evidence file or NOTES step> [; next: <step>, ~$<cost>]

    ## Escalation (1 Oct 2026)
    - [x|n/a|retired| ] siblings: ...
    - [x|n/a|retired| ] clear-pages: ...
    - [x|n/a|retired| ] known-keys: ...
    - [x|n/a|retired| ] print: ...
    - [x|n/a|retired| ] key-rebuild: ...
    - [x|n/a|retired| ] image-check: ...
    - [x|n/a|retired| ] retry: ...
    Verdict: <"keep going: N internal gaps; cheapest next: <step>, ~$<cost>" | "parked: every gap has an outside blocker">

Blockers. Outside the session: no-key-material, too-short, illegible, needs-physical-access, waiting-on (which must
name what is awaited: an ASKS row, a LOCAL-/JSTOR-/SEND-QUEUE row, or a named archive's or person's reply).
Internal: open-codes (scattered codes no context narrows; allowed, but the target stays workable), not-attempted
(must carry "; next: <step>"). Marks: [x] done, [n/a] does not apply (reason of 3+ words), [retired] closed for one
instrument by rule 3's third-attempt clause (name the instrument, 3+ words; it does not hold the target open, but a
different instrument or new material reopens it), [ ] not yet tried (say the planned step).

What it is meant to CATCH (each has an offline test in tools/tests/test_gaps_check.py):
  - a `partial` target with either section missing, or with no gap lines;
  - a gap bullet with no "- blocker:", or a blocker outside the vocabulary, or no reason after it;
  - "waiting-on" that names nothing checkable; "not-attempted" without "; next:";
  - an escalation step missing, duplicated, unknown, or carrying an invalid mark; [n/a]/[retired] with a reason
    under three words; a step with no text at all;
  - a missing or malformed Verdict line; "parked" while any gap is internal or any step is still [ ];
    "keep going: N internal gaps" whose N disagrees with the gap lines.

What it must NOT block (also tested):
  - an `open`, `solved`, `blocked` or other non-partial target with no sections (reported SKIP, exit 0);
  - a `partial` target parked with every gap behind an outside blocker and no [ ] step, including one whose
    steps are [retired] under rule 3 rather than [x];
  - a `partial` target that says "keep going" with internal gaps (that is an honest state, reported, not a FAIL);
  - an earlier, superseded pair of sections above the current one (only the LAST of each is read);
  - prose lines inside a section that are not bullets (notes, continuation text).

A non-partial target that does carry the sections is checked for format too (a malformed section is still wrong),
but never required to have them.

Output: one line per target -- "OK parked", "OK keep-going (N internal gaps, M steps untried)", "FAIL: reasons",
or "SKIP" -- then a summary line. Exit 0 when nothing FAILs, 1 on any FAIL, 2 on a usage error (unknown target).
Offline; reads files only. Status words are read with tools/next_steps.py's first_status_word (rule 5 vocabulary,
bare or behind a "Status:" label).
"""
import argparse
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "tools"))
from next_steps import first_status_word  # noqa: E402

OUTSIDE = ("no-key-material", "too-short", "illegible", "needs-physical-access", "waiting-on")
INTERNAL = ("open-codes", "not-attempted")
BLOCKERS = OUTSIDE + INTERNAL
STEPS = ("siblings", "clear-pages", "known-keys", "print", "key-rebuild", "image-check", "retry")
MARKS = ("x", "n/a", "retired", " ")

GAPS_HEAD = re.compile(r"^##\s+Remaining gaps\b", re.I)
ESC_HEAD = re.compile(r"^##\s+Escalation\b", re.I)
ANY_HEAD = re.compile(r"^#{1,2}\s")
BULLET = re.compile(r"^\s*[-*]\s+")
GAP_LINE = re.compile(r"^\s*[-*]\s+(?P<piece>.+?)\s+[-–—]+\s+blocker:\s*(?P<rest>.*)$", re.I)
STEP_LINE = re.compile(r"^\s*[-*]\s+\[(?P<mark>[^\]]*)\]\s*(?P<step>[A-Za-z][\w-]*)\s*:\s*(?P<text>.*)$")
VERDICT = re.compile(r"^\s*Verdict:\s*(?P<text>.*)$", re.I)
READ_SO_FAR = re.compile(r"^\s*Read so far:\s*(?P<text>.*)$", re.I)
KEEP = re.compile(r"^keep going\s*:\s*(?P<n>\d+)\s+internal gaps?\b(?P<rest>.*)$", re.I)
PARKED = re.compile(r"^parked\b", re.I)
# What a waiting-on gap may name: a register row, or a reply/answer awaited from a named party.
WAIT_ROW = re.compile(r"\b(ASKS(\.md)?\s*(row\s*)?#?\d+|(LOCAL|JSTOR|SEND)-QUEUE(\.tsv)?\s*(row\s*)?\w*\d+|L\d+\b)", re.I)
WAIT_REPLY = re.compile(r"\b(reply|replies|answer|response|quote|copy order|order|loan)\b", re.I)


def words(s):
    return len(re.findall(r"[A-Za-z0-9][\w./'()$~-]*", s or ""))


def last_section(lines, head_re):
    """Body lines of the LAST heading matching head_re, up to the next #/## heading; None if absent."""
    start = None
    for i, line in enumerate(lines):
        if head_re.match(line):
            start = i
    if start is None:
        return None
    body = []
    for line in lines[start + 1:]:
        if ANY_HEAD.match(line):
            break
        body.append(line.rstrip("\n"))
    return body


def parse_gaps(body, problems):
    """Return a list of gap dicts; append problems. Also checks the 'Read so far:' line."""
    gaps = []
    read_line = None
    for line in body:
        m = READ_SO_FAR.match(line)
        if m:
            read_line = m.group("text").strip()
            continue
        if not BULLET.match(line):
            continue
        g = GAP_LINE.match(line)
        if not g:
            problems.append("gap bullet without ' - blocker:' (%s)" % line.strip()[:60])
            continue
        piece, rest = g.group("piece").strip(), g.group("rest").strip()
        segs = [s.strip() for s in rest.split(";")]
        spec = segs[0]
        word = (spec.split() or [""])[0].rstrip(":,").lower()
        if word not in BLOCKERS:
            problems.append("gap '%s': blocker '%s' not in vocabulary" % (piece[:40], word or "(empty)"))
            continue
        nexts = [s for s in segs[1:] if s.lower().startswith("next:")]
        whys = [s for s in segs[1:] if s and not s.lower().startswith("next:")]
        if not whys:
            problems.append("gap '%s': no reason after the blocker ('; <why>')" % piece[:40])
        if word == "waiting-on":
            awaited = spec[len("waiting-on"):].strip(" :")
            if not awaited or not (WAIT_ROW.search(awaited) or (WAIT_REPLY.search(awaited) and words(awaited) >= 2)):
                problems.append("gap '%s': waiting-on names no ASKS/queue row or awaited reply" % piece[:40])
        if word == "not-attempted" and not any(words(n[len("next:"):]) >= 1 for n in nexts):
            problems.append("gap '%s': not-attempted without '; next: <step>'" % piece[:40])
        gaps.append({"piece": piece, "blocker": word, "outside": word in OUTSIDE,
                     "next": nexts[0][len("next:"):].strip() if nexts else ""})
    if read_line is None:
        problems.append("Remaining gaps: no 'Read so far:' line")
    elif words(read_line) < 1 or (read_line.lower().startswith("unmeasured") and words(read_line) < 3):
        problems.append("Remaining gaps: 'Read so far:' gives no fraction (or 'unmeasured' without why)")
    if not gaps and not any("gap" in p for p in problems):
        problems.append("Remaining gaps: no gap lines (a partial with nothing unread is not partial)")
    return gaps


def parse_escalation(body, problems):
    """Return (steps {name: (mark, text)}, verdict text or None); append problems."""
    steps, verdict = {}, None
    for line in body:
        v = VERDICT.match(line)
        if v:
            verdict = v.group("text").strip()
            continue
        if not BULLET.match(line):
            continue
        s = STEP_LINE.match(line)
        if not s:
            problems.append("escalation bullet not '- [mark] step: text' (%s)" % line.strip()[:60])
            continue
        mark = s.group("mark").strip().lower()
        mark = " " if mark == "" else mark
        step, text = s.group("step").lower(), s.group("text").strip()
        if step not in STEPS:
            problems.append("escalation: unknown step '%s'" % step)
            continue
        if step in steps:
            problems.append("escalation: step '%s' listed twice" % step)
            continue
        if mark not in MARKS:
            problems.append("escalation %s: mark [%s] not one of [x] [n/a] [retired] [ ]" % (step, mark))
            continue
        if not text:
            problems.append("escalation %s: no text (say what was done, why n/a, or the planned step)" % step)
        elif mark in ("n/a", "retired") and words(text) < 3:
            problems.append("escalation %s: [%s] needs a reason of at least three words" % (step, mark))
        steps[step] = (mark, text)
    for step in STEPS:
        if step not in steps and not any(("'%s'" % step) in p for p in problems):
            problems.append("escalation: step '%s' missing" % step)
    return steps, verdict


def check_text(text, status):
    """Check one NOTES.md body. Returns (kind, message): kind in OK-parked, OK-keep, FAIL, SKIP."""
    lines = text.splitlines()
    gaps_body = last_section(lines, GAPS_HEAD)
    esc_body = last_section(lines, ESC_HEAD)
    if status != "partial" and gaps_body is None and esc_body is None:
        return "SKIP", "status %s; sections not required" % (status or "unknown")
    problems = []
    if gaps_body is None:
        problems.append("no '## Remaining gaps' section")
    if esc_body is None:
        problems.append("no '## Escalation' section")
    gaps = parse_gaps(gaps_body, problems) if gaps_body is not None else []
    steps, verdict = parse_escalation(esc_body, problems) if esc_body is not None else ({}, None)
    internal = [g for g in gaps if not g["outside"]]
    untried = [s for s, (m, _) in steps.items() if m == " "]
    if esc_body is not None:
        if verdict is None:
            problems.append("no 'Verdict:' line")
        elif PARKED.match(verdict):
            if internal:
                problems.append("verdict 'parked' but %d gap(s) are internal (%s)"
                                % (len(internal), ", ".join(sorted({g["blocker"] for g in internal}))))
            if untried:
                problems.append("verdict 'parked' but step(s) not yet tried: %s" % ", ".join(untried))
        else:
            k = KEEP.match(verdict)
            if not k:
                problems.append("verdict is neither 'keep going: N internal gaps; cheapest next: ...' nor 'parked: ...'")
            else:
                if gaps_body is not None and int(k.group("n")) != len(internal):
                    problems.append("verdict says %s internal gaps, gap lines give %d" % (k.group("n"), len(internal)))
                if "cheapest next:" not in k.group("rest").lower():
                    problems.append("verdict 'keep going' without 'cheapest next: <step>'")
    if problems:
        return "FAIL", "; ".join(problems)
    if PARKED.match(verdict):
        return "OK-parked", "parked: %d gap(s), all outside blockers" % len(gaps)
    return "OK-keep", "keep going: %d internal gap(s), %d step(s) untried" % (len(internal), len(untried))


def check_target(ciphers_dir, target):
    path = os.path.join(ciphers_dir, target, "NOTES.md")
    if not os.path.exists(path):
        return None
    text = open(path, encoding="utf-8").read()
    return check_text(text, first_status_word(text))


def partial_targets(ciphers_dir):
    out = []
    for p in sorted(glob.glob(os.path.join(ciphers_dir, "*", "NOTES.md"))):
        if first_status_word(open(p, encoding="utf-8").read()) == "partial":
            out.append(os.path.basename(os.path.dirname(p)))
    return out


def main(argv=None, out=sys.stdout):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog="Format, blockers, marks and scope: see the module docstring (head -60 tools/gaps_check.py).")
    ap.add_argument("targets", nargs="*", help="target folder names under ciphers/ (or paths to them)")
    ap.add_argument("--all", action="store_true", help="check every target whose NOTES.md status is partial")
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"), help="default: the repository's ciphers/")
    args = ap.parse_args(argv)
    targets = [os.path.basename(os.path.normpath(t)) for t in args.targets]
    if args.all:
        targets += [t for t in partial_targets(args.ciphers_dir) if t not in targets]
    if not targets:
        ap.error("name a target or pass --all")
    counts = {"OK-parked": 0, "OK-keep": 0, "FAIL": 0, "SKIP": 0}
    usage_error = False
    for t in targets:
        r = check_target(args.ciphers_dir, t)
        if r is None:
            print("ERROR %s: no NOTES.md under %s" % (t, args.ciphers_dir), file=out)
            usage_error = True
            continue
        kind, msg = r
        counts[kind] += 1
        label = {"OK-parked": "OK parked", "OK-keep": "OK keep-going", "FAIL": "FAIL", "SKIP": "SKIP"}[kind]
        print("%s %s: %s" % (label, t, msg), file=out)
    print("gaps_check: %d checked: %d parked, %d keep-going, %d FAIL, %d skipped"
          % (len(targets), counts["OK-parked"], counts["OK-keep"], counts["FAIL"], counts["SKIP"]), file=out)
    if counts["FAIL"]:
        return 1
    return 2 if usage_error else 0


if __name__ == "__main__":
    sys.exit(main())

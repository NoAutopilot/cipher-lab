#!/usr/bin/env python3
"""Gate: a brief that sends images to a model states its vision-call count and per-call price (Usage 6, README
"Vision calls are a counted unit"; RETRO-2026-10-03-acct3 proposal 2).

Catches: a brief under .claude/briefs/runs/ whose text names an image step (blind pass, crops, tiles, readers,
gloss read, transcribe / transcription pass, iiif_lines, vision call) but has no line matching
    vision calls: <N> x USD <r> [+ <k> reconciliation] = <X>
and, when one exists, X greater than the brief's "Cap USD <c>" / "Cap $<c>" (exit 1 either way). Also catches a
line whose own arithmetic is wrong ((N + k) x r differs from X by more than 1 cent).
Must NOT block: a brief with no image step (a gate-fix, a print check, a family_run on disk data, a brief that
only reads an existing transcription file), or a brief that says "no images" / "disk only" with no blind-pass or
transcribe verb (tests cover both, plus F36-GLOSS's own text as the failing case). A worker's report wording
such as "report vision calls used" is not an image step on its own.
Rates: Sonnet about USD 1.5 a call on native crops (AX-COMP2); Opus has no recorded rate -- the brief writes
"Opus rate unmeasured: first call measured and reported, stop if over USD 3" and the gate accepts that wording.

Usage: python3 tools/brief_price_check.py BRIEF.md [BRIEF.md ...]   (exit 1 if any FAILs)
       python3 tools/brief_price_check.py --summary BRIEFS...       (also prints ok/FAIL/no-image counts)
Offline test: python3 tools/tests/test_brief_price_check.py
"""
import re
import sys

# "transcription" alone is a file name more often than a job (a disk brief reads "the 993-sign transcription"),
# so only the verb forms and "transcription pass" count; "vision call" counts only outside report wording.
IMG = re.compile(r'blind (?:pass|read)|\bcrops?\b|\btiles?\b|\breaders?\b|gloss read|\btranscribe[sd]?\b|'
                 r'transcription pass|iiif_lines|image reader|vision calls? (?:on|per|at most)|at most \d+ vision', re.I)
LINE = re.compile(r'vision calls:\s*(\d+)\s*x\s*(?:USD|\$)\s*([\d.]+)(?:\s*\+\s*(\d+)\s*reconciliation)?\s*=\s*'
                  r'(?:USD\s*|\$)?([\d.]+)', re.I)
NOIMG = re.compile(r'\bno images?\b|\bdisk only\b', re.I)
NOIMG_OVERRIDE = re.compile(r'blind (?:pass|read)|\btranscribe[sd]?\b|transcription pass', re.I)
OPUS_UNMEASURED = re.compile(r'Opus rate unmeasured', re.I)
CAP = re.compile(r'\bCap (?:USD ?|\$)?([\d.]+)', re.I)


def check(text):
    """Return (rc, reason, kind) with kind in {'no-image', 'ok', 'fail'}."""
    if not IMG.search(text) or (NOIMG.search(text) and not NOIMG_OVERRIDE.search(text)):
        return 0, 'no image step', 'no-image'
    m = LINE.search(text)
    if not m:
        if OPUS_UNMEASURED.search(text):
            return 0, 'ok (Opus rate unmeasured wording)', 'ok'
        return 1, 'image step but no "vision calls: N x USD r = X" line', 'fail'
    n, r, k, x = int(m.group(1)), float(m.group(2)), int(m.group(3) or 0), float(m.group(4))
    if abs((n + k) * r - x) > 0.01:
        return 1, f'vision calls arithmetic: ({n}+{k}) x {r} = {(n + k) * r:.2f}, not {x}', 'fail'
    cap = CAP.search(text)
    if cap and x > float(cap.group(1).rstrip('.')) * 1.0001:
        return 1, f'vision calls price {x} exceeds cap {cap.group(1).rstrip(".")}', 'fail'
    return 0, 'ok', 'ok'


def main(argv):
    summary = '--summary' in argv
    paths = [a for a in argv if a != '--summary']
    if not paths or '-h' in paths or '--help' in paths:
        print(__doc__)
        return 0 if paths else 2
    worst, counts = 0, {'ok': 0, 'fail': 0, 'no-image': 0}
    for p in paths:
        with open(p, encoding='utf-8') as f:
            rc, why, kind = check(f.read())
        worst = max(worst, rc)
        counts[kind] += 1
        print(f'{p}: {"FAIL" if rc else "ok"} -- {why}')
    if summary:
        print(f'summary: {len(paths)} briefs, {counts["ok"]} ok (image step priced), '
              f'{counts["no-image"]} ok (no image step), {counts["fail"]} FAIL')
    return worst


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

#!/usr/bin/env python3
"""Gate: a brief that sends images to a model states its vision-call count and per-call price (Usage 6, README
"Vision calls are a counted unit"; RETRO-2026-10-03-acct3 proposal 2).

Catches: a brief under .claude/briefs/runs/ whose text names an image step (blind pass, crops, tiles, readers,
gloss read, transcribe / transcription pass, iiif_lines, vision call) but has no line matching
    vision calls: <N> x USD <r> [+ <k> reconciliation] = <X>
and, when one exists, X greater than the brief's "Cap USD <c>" / "Cap $<c>" (exit 1 either way). Also catches a
line whose own arithmetic is wrong ((N + k) x r differs from X by more than 1 cent).
Floor check (RETRO-2026-10-04-acct1 P2, see floor_check()): per '## JOB' section, a named Fable or Opus model whose
cap is under its floor (Fable 5, Opus 3.0 since 16 Oct 2026, was 2.5) prints "FLOOR <job> <model> cap <c> < <floor>" and exits 1. Must NOT
block: no model or no cap in the section, a Sonnet job at any cap, a cap at or above the floor.
Must NOT block: a brief with no image step (a gate-fix, a print check, a family_run on disk data, a brief that
only reads an existing transcription file), or a brief that says "no images" / "disk only" with no blind-pass or
transcribe verb (tests cover both, plus F36-GLOSS's own text as the failing case). A worker's report wording
such as "report vision calls used" is not an image step on its own.
Rates: Sonnet about USD 1.5 a call on native crops (AX-COMP2); Opus about USD 1.3 a call on top of the 3.0 session floor
(HAR-41R, ledger 4772: 5 reader calls measured, 16 Oct 2026, EXC-2026-10-16 fix B). The "Opus rate unmeasured" wording is
retired (it let HAR-41R through at 2.1x): an Opus image brief writes the line with r = 1.3 like any other.
"Disk only" means no network, not no images: a blind sort, a blind labelling pass or an exemplar-crop check is an image
step (EXC-2026-10-16 fix A; tests cover the four leaked shapes and keep the family_run disk case passing).

Usage: python3 tools/brief_price_check.py BRIEF.md [BRIEF.md ...]   (exit 1 if any FAILs)
       python3 tools/brief_price_check.py --summary BRIEFS...       (also prints ok/FAIL/no-image counts)
Offline test: python3 tools/tests/test_brief_price_check.py
"""
import re
import sys

# "transcription" alone is a file name more often than a job (a disk brief reads "the 993-sign transcription"),
# so only the verb forms and "transcription pass" count; "vision call" counts only outside report wording.
# 16 Oct 2026 (EXC-2026-10-16 fix A): a blind sort, a blind labelling pass, a "blind Sonnet/Opus call" and an exemplar-crop
# check are image steps, and "disk only" (which means no network, not no images) does not exempt them: MONL-SORT, CL1161-S7,
# MONL-VB and LIN-LAB2 (ledger 4490/4536/4537/4551, 2.2-3.0x cap) all passed as "no image step" before this.
IMG = re.compile(r'blind (?:pass|read|sort|label\w*)|blind (?:\w+ )?(?:vision|Sonnet|Opus) (?:pass|call|read)|vision pass|'
                 r'\bcrops?\b|\btiles?\b|\breaders?\b|gloss read|\btranscribe[sd]?\b|'
                 r'transcription pass|iiif_lines|image reader|vision calls? (?:on|per|at most)|at most \d+ vision', re.I)
LINE = re.compile(r'vision calls:\s*(\d+)\s*x\s*(?:USD|\$)\s*([\d.]+)(?:\s*\+\s*(\d+)\s*reconciliation)?\s*=\s*'
                  r'(?:USD\s*|\$)?([\d.]+)', re.I)
NOIMG = re.compile(r'\bno images?\b|\bdisk only\b', re.I)
NOIMG_OVERRIDE = re.compile(r'blind (?:pass|read|sort|label\w*)|blind (?:\w+ )?(?:vision|Sonnet|Opus) (?:pass|call|read)|'
                            r'vision pass|exemplar crops?|image check|\btranscribe[sd]?\b|transcription pass', re.I)
OPUS_UNMEASURED = re.compile(r'Opus rate unmeasured', re.I)
CAP = re.compile(r'\bCap (?:USD ?|\$)?([\d.]+)', re.I)

# Model-cap floors (RETRO-2026-10-04-acct1 P2). Fable: README "Fable floor" (2 Oct). Opus: window p10/p25/median cost
# 1.49/1.83/2.56 over 578 non-CLOSER rows; 13 of the 17 jobs briefed below these floors on 4 Oct ran over cap.
# 16 Oct 2026 (mission "Close the Learning Loop"): Opus floor raised 2.5 -> 3.0 on the whole-ledger evidence (2,858
# Opus rows with a numeric cost; 749 with a stated cap): cap <= 1.5 ran over 70-100% of the time, cap 2 38%, cap 2.5
# 35%, cap >= 3 16-20% (median ratio 0.71 at cap 3). The 2.5 floor left the 35%-over band open; over-cap rows rose
# every week (W39 62, W40 76, W41 176, W42 152 by 15 Oct). Regression test: a cap-2.5 Opus job is refused.
FLOORS = {'fable': 5.0, 'opus': 3.0}
SECTION = re.compile(r'^#{2,3} +(\S+).*$', re.M)
MODEL = re.compile(r'\b(Fable|Opus|Sonnet)\b', re.I)
SCAP = re.compile(r'\bcap (?:USD ?|\$)?([\d.]+)', re.I)


def floor_check(text, floors=FLOORS):
    """Per '## JOB -- ...' heading (or its first 200 body characters): a named model whose cap is under its floor.
    Catches A3V2-THUR275 '(Fable; cap USD 1.5; ...)'. Must NOT block: a heading with no model or no cap, a Sonnet
    job at any cap, a Fable job at 5 or more."""
    out = []
    for m in SECTION.finditer(text):
        head, body = m.group(0), text[m.end():m.end() + 400].split('\n## ')[0]
        mm = MODEL.search(head) or MODEL.search(body[:200])
        cm = SCAP.search(head) or SCAP.search(body[:200])
        if mm and cm and mm.group(1).lower() in floors and float(cm.group(1).rstrip('.')) < floors[mm.group(1).lower()]:
            out.append((m.group(1), mm.group(1), float(cm.group(1).rstrip('.')), floors[mm.group(1).lower()]))
    return out


JOB_SPLIT = re.compile(r'^(?=#{2,3} +(?:JOB\s+)?\S)', re.M)


def check(text):
    """Return (rc, reason, kind) with kind in {'no-image', 'ok', 'fail'}. A file with several '## JOB' / '### ' sections is checked
    section by section and reports the worst (16 Oct 2026, CLIN-F49: a two-job file passed as "no image step" because the OTHER job
    said "no images" -- a file-level NOIMG exempted a section with two blind Opus reads and a priced line)."""
    parts = [p for p in JOB_SPLIT.split(text) if p.strip()]
    if len(parts) > 1 and not JOB_SPLIT.match(parts[0]):
        # A multi-job file's preamble (title + common tail) is not a job: it prices nothing and names no step of its own
        # (17 Oct 2026, wave 6: a title that said "tiles" failed the file). It is skipped only when a job section follows.
        parts = parts[1:]
    if len(parts) > 1:
        worst = (0, 'no image step', 'no-image')
        rank = {'no-image': 0, 'ok': 1, 'fail': 2}
        for part in parts:
            r = check_one(part)
            if rank[r[2]] > rank[worst[2]]:
                worst = r
        return worst
    return check_one(text)


def check_one(text):
    if not IMG.search(text) or (NOIMG.search(text) and not NOIMG_OVERRIDE.search(text)):
        return 0, 'no image step', 'no-image'
    m = LINE.search(text)
    if not m:
        if OPUS_UNMEASURED.search(text):
            return 1, 'image step; "Opus rate unmeasured" is retired (Opus about USD 1.3 a call, HAR-41R) -- write the line', 'fail'
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
            text = f.read()
        rc, why, kind = check(text)
        worst = max(worst, rc)
        counts[kind] += 1
        print(f'{p}: {"FAIL" if rc else "ok"} -- {why}')
        for job, model, c, fl in floor_check(text):
            print(f'FLOOR {job} {model} cap {c:g} < {fl:g}')
            worst = 1
    if summary:
        print(f'summary: {len(paths)} briefs, {counts["ok"]} ok (image step priced), '
              f'{counts["no-image"]} ok (no image step), {counts["fail"]} FAIL')
    return worst


if __name__ == '__main__':
    sys.exit(main(sys.argv[1:]))

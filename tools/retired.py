#!/usr/bin/env python3
"""retired.py: one register of every retired step, so a retired instrument can be found and reopened later
(RETIRED-REGISTER, 9 Oct 2026, for orchestrator account-4; owner: "for those that are retired, just make sure
that we're noting it somewhere, so if we want to return to it later, we can").

    python3 tools/retired.py [--root DIR] [--out RETIRED.tsv] [--check] [--stdout]

Scans, best-effort and read-only:
  - every ciphers/*/NOTES.md line carrying `[retired]` (any case);
  - every ciphers/*/HYPOTHESES.md line saying `untested-by-this-tool` or `retired` (negations such as
    "nothing is retired" / "not retired" are skipped);
  - every research/TX-REGISTER.tsv row whose verdict column says `retired` (folder = `transcription`).
and writes RETIRED.tsv at the repository root, columns:
  folder, step, instrument, date, attempts, why, reopen_when, source
`source` is file:line; an identical line repeated in the same file (a status block copied forward) is written
once, with the repeat count appended to source. A line the parser cannot read is written with step = the raw
line and the other cells `?`, never dropped. The register is regenerated, never edited by hand; repairs go into
the target's own NOTES.md / HYPOTHESES.md, then this tool is re-run.

--check exits 1 and prints the rows whose reopen_when is `not stated` (CLAUDE.md rule 5: a [retired] step names
the instrument and what reopens it -- a different instrument or new material). It reports; it never repairs.

Scope (CLAUDE.md Usage 8a), each backed by an offline test in tools/tests/test_retired.py:
  must catch:     a `[retired]` line with no reopen condition at all ("... is [retired] after three FAILs.")
                  -> reopen_when `not stated`, --check exits 1.
  must not block: a `[retired]` line that names "a different instrument or new material" (or "only X
                  reopens it", "reopened only by X", "next: X") -> reopen_when filled, --check exits 0.
"""
import argparse
import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
COLS = ["folder", "step", "instrument", "date", "attempts", "why", "reopen_when", "source"]
MAXCELL = 300

RETIRED_TAG = re.compile(r"\[retired\]", re.I)
HYP_PAT = re.compile(r"untested-by-this-tool|\bretired\b", re.I)
NEGATION = re.compile(r"(nothing|none|not|never|no instrument[^.;]*)\s+(is\s+|was\s+|been\s+)?retired", re.I)
MONTHS = r"(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.?"
DATE = re.compile(r"\b(\d{1,2} " + MONTHS + r" 20\d\d)\b|\b(20\d\d-\d\d-\d\d)\b")
RESULT = re.compile(r"\b\d+\s*/\s*\d+\b|\b\d\.\d{2,3}\b")
REOPEN = [
    re.compile(r"(?:only )?([^;:.]+?) (?:would )?reopens? (?:it|this|the step)", re.I),
    re.compile(r"\[retired\]\*?\*? (?:until|unless) ([^;.]+)", re.I),
    re.compile(r"reopen(?:ed|s)? only (?:by|with|when|if) ([^;]+)", re.I),
    re.compile(r"reopen(?:ed|s)? (?:by|with|when|if) ([^;]+)", re.I),
    re.compile(r"a different instrument is untried:? ([^;]+)", re.I),
    re.compile(r"\bnext:? ([^;]+)", re.I),
    re.compile(r"\bneeds? ((?:longer|more|new|a |another|better)[^;|]+)", re.I),
    re.compile(r"((?:a )?different instrument[^;|]*|new material[^;|]*|another scan[^;|]*|a better image[^;|]*"
               r"|owner(?:'s)? tiles[^;|]*|a person's [^;|]*)", re.I),
]
WHY = [
    (re.compile(r"wrong way|not moving together|never all three", re.I), "numbers not moving together (rule 3)"),
    (re.compile(r"non-test|at this N\b|too short", re.I), "non-test at this N"),
    (re.compile(r"third-attempt|three (?:instruments|attempts|fixes|specimens)|rule 3|3\(c\)|three", re.I),
     "rule 3 third-attempt clause"),
    (re.compile(r"control[^;]{0,40}(below gate|FAIL)|BELOW GATE|FAILED its|gate FAIL|at chance", re.I),
     "control/known-answer failed its gate"),
]
INSTRUMENT_NAMED = re.compile(r"instrument:? ((?:tools/)?[\w/-]+\.py\b[^,;)]{0,60})", re.I)
TRAILING_VERBS = re.compile(r"(\s+\b(is|was|are|were|stays|stay|now|logged|the|as|and|for|been|has|have)\b)+\s*$", re.I)


def clean(s, n=MAXCELL):
    s = re.sub(r"\s+", " ", (s or "").replace("\t", " ")).strip().strip("|").strip()
    return s if len(s) <= n else s[: n - 3] + "..."


def strip_md(line):
    s = line.strip()
    s = re.sub(r"^(#+\s*|[-*]\s*(\[[ xn/aretid]*\]\s*)?|\|\s*)", "", s, flags=re.I)
    return s.replace("**", "")


def find_date(text, anchor):
    """Date nearest before the anchor position, else the first in the line."""
    best = None
    for m in DATE.finditer(text):
        if m.start() <= anchor:
            best = m.group(0)
    if best is None:
        m = DATE.search(text)
        best = m.group(0) if m else "unknown"
    return best


def parse(text, context=""):
    """Return dict of step/instrument/date/attempts/why/reopen_when for one line of prose; raises on nothing.
    `context` (the rest of the paragraph after the line) is consulted only for a reopen condition or a date
    the line itself does not carry."""
    s = strip_md(text)
    if not s:
        raise ValueError("empty")
    m = RETIRED_TAG.search(s) or re.search(r"retired|untested-by-this-tool", s, re.I)
    anchor = m.start() if m else len(s)
    step = re.split(r" - blocker:|: |;|\(", s, maxsplit=1)[0]
    mi = INSTRUMENT_NAMED.search(s)
    lead = re.match(r"\s*[-*]?\s*\[retired\]", text, re.I)
    if mi:
        instrument = mi.group(1)
    elif lead:  # "- [retired] step: <instrument> did not / failed ..." -- the clause after the step names it
        tool = re.search(r"(?:tools/)?[\w/-]+\.py\b", s)
        body = s.split(": ", 1)[1] if ": " in s else s
        instrument = tool.group(0) if tool else re.split(
            r"[;,(]| (?:did not|failed|from|on|at|is|was)\b", body, maxsplit=1)[0]
    else:
        seg = re.split(r"[;(]|, |: ", s[:anchor])[-1]
        instrument = TRAILING_VERBS.sub("", seg.strip()).strip(" -,.") or step
    results = RESULT.findall(s)
    attempts = ", ".join(r.replace(" ", "") for r in results[:3]) if results else "not given"
    why = next((label for pat, label in WHY if pat.search(s)), "not stated")
    reopen = "not stated"
    for pat in REOPEN:
        mr = pat.search(s, anchor) or pat.search(s)
        if mr and len(mr.group(1).strip()) >= 6:
            reopen = mr.group(1)
            break
    if reopen == "not stated" and context:
        c = strip_md(context)
        for pat in REOPEN:
            mr = pat.search(c)
            if mr and len(mr.group(1).strip()) >= 6:
                reopen = mr.group(1) + " [next lines]"
                break
    date = find_date(s, anchor)
    if date == "unknown" and context:
        date = find_date(context, len(context))
    return {"step": clean(step, 160), "instrument": clean(instrument, 160), "date": date,
            "attempts": clean(attempts), "why": why, "reopen_when": clean(reopen)}


def row_for(folder, text, source, context=""):
    try:
        d = parse(text, context)
    except Exception:
        d = None
    if not d:
        d = {"step": clean(text), "instrument": "?", "date": "?", "attempts": "?", "why": "?", "reopen_when": "?"}
    d["folder"], d["source"] = folder, source
    return d


def _finish(rows_with_dups):
    out = []
    for r in rows_with_dups:
        n = r.pop("_dups", 0)
        if n:
            r["source"] += " (+%d identical)" % n
        out.append(r)
    return out


def scan_file(path, rel, folder, match):
    rows, seen = [], {}
    with open(path, encoding="utf-8", errors="replace") as f:
        lines = f.read().split("\n")
    for i, line in enumerate(lines, 1):
        if not match(line):
            continue
        key = line.strip()
        if key in seen:
            seen[key]["_dups"] += 1
            continue
        ctx = []
        for nxt in lines[i:i + 4]:
            if not nxt.strip() or nxt.lstrip().startswith(("#", "- ")):
                break
            ctx.append(nxt)
        r = row_for(folder, line, "%s:%d" % (rel, i), " ".join(ctx))
        r["_dups"] = 0
        seen[key] = r
        rows.append(r)
    return _finish(rows)


def notes_match(line):
    return bool(RETIRED_TAG.search(line))


def hyp_match(line):
    return bool(HYP_PAT.search(line)) and not (NEGATION.search(line) and not re.search(
        r"untested-by-this-tool|\[retired\]|\*\*retired", line, re.I))


def scan_tx(path, rel):
    rows = []
    with open(path, encoding="utf-8", errors="replace", newline="") as f:
        reader = csv.reader(f, delimiter="\t")
        header = next(reader, None) or []
        idx = {h: k for k, h in enumerate(header)}
        for i, rec in enumerate(reader, 2):
            get = lambda c: rec[idx[c]] if c in idx and idx[c] < len(rec) else ""  # noqa: E731
            if "retired" not in get("verdict").lower():
                continue
            reason = get("reason")
            try:
                reopen = parse(reason)["reopen_when"] if reason else "not stated"
            except Exception:
                reopen = "not stated"
            why = next((label for pat, label in WHY if pat.search(reason)), clean(reason, 160) or "not stated")
            rows.append({"folder": "transcription", "step": clean(get("family"), 160),
                         "instrument": clean("%s %s: %s" % (get("id"), get("campaign"), get("mechanism_attacked")), 160),
                         "date": clean(get("date")) or "unknown",
                         "attempts": clean("dev: %s; eval: %s" % (get("dev_result"), get("eval_result"))),
                         "why": why, "reopen_when": reopen, "source": "%s:%d" % (rel, i)})
    return rows


def build_rows(root):
    rows = []
    for path in sorted(glob.glob(os.path.join(root, "ciphers", "*", "NOTES.md"))):
        folder = os.path.basename(os.path.dirname(path))
        rows += scan_file(path, os.path.relpath(path, root), folder, notes_match)
    for path in sorted(glob.glob(os.path.join(root, "ciphers", "*", "HYPOTHESES.md"))):
        folder = os.path.basename(os.path.dirname(path))
        rows += scan_file(path, os.path.relpath(path, root), folder, hyp_match)
    tx = os.path.join(root, "research", "TX-REGISTER.tsv")
    if os.path.exists(tx):
        rows += scan_tx(tx, os.path.relpath(tx, root))
    return rows


def render(rows):
    lines = ["\t".join(COLS)]
    for r in rows:
        lines.append("\t".join(clean(str(r.get(c, "?")), 10_000) or "?" for c in COLS))
    return "\n".join(lines) + "\n"


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 epilog=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--out", default=None, help="default <root>/RETIRED.tsv")
    ap.add_argument("--check", action="store_true", help="exit 1 if any row has reopen_when 'not stated'")
    ap.add_argument("--stdout", action="store_true", help="print the TSV instead of writing it")
    a = ap.parse_args(argv)
    rows = build_rows(a.root)
    text = render(rows)
    if a.stdout:
        sys.stdout.write(text)
    else:
        out = a.out or os.path.join(a.root, "RETIRED.tsv")
        with open(out, "w", encoding="utf-8") as f:
            f.write(text)
        print("retired.py: %d rows -> %s" % (len(rows), os.path.relpath(out, a.root)), file=sys.stderr)
    if a.check:
        bad = [r for r in rows if r["reopen_when"] == "not stated"]
        for r in bad:
            print("not stated: %s | %s | %s" % (r["source"], r["folder"], r["step"][:80]))
        print("retired.py --check: %d of %d rows name no reopen condition" % (len(bad), len(rows)),
              file=sys.stderr)
        return 1 if bad else 0
    return 0


if __name__ == "__main__":
    sys.exit(main())

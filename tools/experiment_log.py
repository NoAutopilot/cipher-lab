#!/usr/bin/env python3
"""The experiment loop as a record, not a narrative (16 Oct 2026, mission "Close the Learning Loop").

Every measurement job already writes a PREREG-<JOB>.md before scoring (rule 3) and a HYPOTHESES.md row with its
control. What was missing is the decision and its transfer: 270 ledger rows say "non-test", 35 say "untested-by-
this-tool", 15 say "third attempt" -- and 194 of the 270 are coded D (delivered on brief), so the research outcome
is invisible to anyone reading the ledger, and the next lane re-runs the same instrument on the same target (the
Vivonne g-split went to a seventh variant; Oldenbarnevelt had 22 N rows of screens; Salviati ran 40 route-5 rows
before a published key surfaced). This tool makes the five-line decision block a checked part of every PREREG and
builds one cross-target index of it.

A PREREG written on or after 16 Oct 2026 ends with:

    ## Decision
    Belief: <what we believe and why, one line>
    Would change it: <the observation that would make us drop or keep the belief; the gate's number>
    Observed: <what the run measured, both numbers (control / target)>          -- filled in after the run
    Decision: continue | change | stop  -- <one clause: what runs next or why nothing does>  -- after the run
    Lesson: <what another lane should know before using this instrument on this design or N>  -- after the run

Usage:
  tools/experiment_log.py --check PREREG.md [...]     exit 1 when a PREREG dated on/after 2026-10-16 lacks the block
                                                      or its Decision word is not continue/change/stop (a PREREG whose
                                                      Observed/Decision/Lesson lines are still '<pending>' passes
                                                      --check before the run and fails --check --done after it);
                                                      older files: WARN only.
  tools/experiment_log.py --index [--out EVIDENCE.tsv] scan ciphers/*/PREREG-*.md (Decision blocks) and
                                                      ciphers/*/HYPOTHESES.md (family rows with a control) into one
                                                      TSV: target, source, date, instrument, n, control, target_stat,
                                                      decision, lesson.
  tools/experiment_log.py --family NAME [--design D]   print the prior evidence rows for an instrument (and design
                                                      word) before a brief re-uses it: the "what should other agents
                                                      learn" read, done by the orchestrator, not remembered.
Offline test: python3 tools/tests/test_experiment_log.py
"""
import argparse
import csv
import datetime
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CUTOFF = datetime.date(2026, 10, 16)
FIELDS = ("Belief", "Would change it", "Observed", "Decision", "Lesson")
DECISION_WORDS = ("continue", "change", "stop")
MONTHS = {m: i for i, m in enumerate(["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"], 1)}
DATE_RE = re.compile(r'(\d{1,2})\s+([A-Za-z]{3})[a-z]*\.?\s+(\d{4})')
INSTRUMENT_RE = re.compile(r'\b(homophonic|anneal|family_run|interlinear_align|lookalike(?:_pass)?|name_candidates|sign_sorter|sorter|packet|g-?split|blind (?:pass|read(?:er)?s?)|transcription|check-solved|print_check|screen|sweep|crib|wordcode|nomenclator|syllabary|masc|vigenere|running_key|decode_key --try|segmenter|glyph_atlas|design_prior|key_crossmatch)\b', re.I)


def file_date(text, path):
    m = DATE_RE.search(text[:600])
    if m and m.group(2).lower() in MONTHS:
        return datetime.date(int(m.group(3)), MONTHS[m.group(2).lower()], int(m.group(1)))
    try:
        return datetime.date.fromtimestamp(os.path.getmtime(path))
    except OSError:
        return None


def decision_block(text):
    """{field: value} for the '## Decision' section, or None when absent."""
    m = re.search(r'^##\s*Decision\s*$', text, re.M)
    if not m:
        return None
    body = text[m.end():]
    nxt = re.search(r'^##\s', body, re.M)
    if nxt:
        body = body[:nxt.start()]
    out = {}
    for f in FIELDS:
        fm = re.search(r'^\s*(?:[-*]\s*)?' + re.escape(f) + r'\s*:\s*(.*)$', body, re.M | re.I)
        if fm:
            out[f] = fm.group(1).strip()
    return out


def check_file(path, done=False, cutoff=CUTOFF):
    """Return (level, message): level 'ok', 'warn' or 'fail'."""
    text = open(path, encoding="utf-8").read()
    d = file_date(text, path)
    blk = decision_block(text)
    new = d is None or d >= cutoff
    if blk is None:
        return ("fail" if new else "warn", f"{path}: no '## Decision' block")
    missing = [f for f in FIELDS if f not in blk or not blk[f]]
    if missing:
        return ("fail" if new else "warn", f"{path}: Decision block lacks {missing}")
    pending = [f for f in ("Observed", "Decision", "Lesson") if "<pending>" in blk[f].lower()]
    if done and pending:
        return ("fail", f"{path}: run is done but {pending} still read <pending>")
    if not pending:
        word = blk["Decision"].split()[0].strip(" -:").lower() if blk["Decision"] else ""
        if word not in DECISION_WORDS:
            return ("fail" if new else "warn", f"{path}: Decision must start with one of {DECISION_WORDS}, got {blk['Decision'][:40]!r}")
    return ("ok", f"{path}: ok")


def instrument_of(text):
    m = INSTRUMENT_RE.search(text)
    return m.group(1).lower() if m else ""


def index_rows(ciphers_dir):
    rows = []
    for path in sorted(glob.glob(os.path.join(ciphers_dir, "*", "PREREG-*.md"))):
        target = os.path.basename(os.path.dirname(path))
        text = open(path, encoding="utf-8").read()
        blk = decision_block(text)
        if not blk:
            continue
        d = file_date(text, path)
        rows.append(dict(target=target, source=os.path.basename(path), date=d.isoformat() if d else "",
                         instrument=instrument_of(text[:1500]) or instrument_of(text), n="", control=blk.get("Would change it", "")[:160],
                         target_stat=blk.get("Observed", "")[:160], decision=blk.get("Decision", "")[:120], lesson=blk.get("Lesson", "")[:200]))
    for path in sorted(glob.glob(os.path.join(ciphers_dir, "*", "HYPOTHESES.md"))):
        target = os.path.basename(os.path.dirname(path))
        for line in open(path, encoding="utf-8"):
            if not line.startswith("| ") or line.startswith("| date") or line.startswith("| hypothesis"):
                continue
            cells = [c.strip() for c in line.strip().strip("|").split("|")]
            if len(cells) < 6:
                continue
            # family rows: date | family | parameters | seeds | CONTROL | TARGET | judge | gate met | label
            fam = cells[1]
            if not re.match(r'^[a-z_\-]+$', fam):
                continue
            nm = re.search(r'\bN=(\d+)', cells[2])
            rows.append(dict(target=target, source="HYPOTHESES.md", date=cells[0][:16], instrument=fam, n=nm.group(1) if nm else "",
                             control=cells[4][:80], target_stat=cells[5][:80],
                             decision=("stop" if re.search(r'retired|untest|non-test|FAIL', " ".join(cells[6:]), re.I) else ""),
                             lesson=" ".join(cells[6:])[:200]))
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--check", nargs="*", metavar="PREREG.md")
    ap.add_argument("--done", action="store_true", help="with --check: the run is finished, so <pending> lines fail")
    ap.add_argument("--index", action="store_true")
    ap.add_argument("--out", default=os.path.join(ROOT, "EVIDENCE.tsv"))
    ap.add_argument("--family")
    ap.add_argument("--design")
    ap.add_argument("--ciphers-dir", default=os.path.join(ROOT, "ciphers"))
    a = ap.parse_args(argv)

    if a.check is not None:
        worst = 0
        for p in a.check:
            level, msg = check_file(p, a.done)
            print(f"{level.upper()}: {msg}")
            worst = max(worst, {"ok": 0, "warn": 0, "fail": 1}[level])
        return worst

    if a.index or a.family:
        rows = index_rows(a.ciphers_dir)
        if a.index:
            with open(a.out, "w", encoding="utf-8", newline="") as f:
                w = csv.DictWriter(f, fieldnames=["target", "source", "date", "instrument", "n", "control", "target_stat", "decision", "lesson"], delimiter="\t", lineterminator="\n")
                w.writeheader()
                w.writerows(rows)
            print(f"experiment_log: {len(rows)} evidence rows -> {a.out}")
        if a.family:
            hits = [r for r in rows if a.family.lower() in (r["instrument"] + " " + r["source"] + " " + r["lesson"]).lower()
                    and (not a.design or a.design.lower() in (r["lesson"] + " " + r["control"]).lower())]
            print(f"prior evidence for {a.family!r}{' / ' + a.design if a.design else ''}: {len(hits)} rows")
            for r in hits[-40:]:
                print(f"  {r['date'][:10]:10} {r['target'][:34]:34} N={r['n'] or '?':>5} {r['decision'][:12]:12} {r['lesson'][:90]}")
        return 0
    ap.error("give --check PREREG.md..., --index, or --family NAME")


if __name__ == "__main__":
    sys.exit(main())

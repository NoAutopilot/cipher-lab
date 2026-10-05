#!/usr/bin/env python3
"""Verifier backlog: every reading with Audit 1 done and Audit 2 or Counted missing, oldest first (LANE-SYS1, 5 Oct 2026).

    python3 tools/verify_backlog.py                       # write VERIFY-BACKLOG.tsv
    python3 tools/verify_backlog.py --stdout              # print, write nothing
    python3 tools/verify_backlog.py --check               # exit 1 if the committed VERIFY-BACKLOG.tsv is stale
    python3 tools/verify_backlog.py --progress P --status S --out O

Two registers, read from disk, never merged by guesswork:
  PROGRESS.tsv  one row per leaf/letter; stage columns `1` Audit 1, `2` Audit 2, `C` Counted (x done, ~ partial,
                . not yet; tools/progress_block.py STAGES). Audit 1 done = `1` is x. Missing = `2` / `C` not x
                (a ~ counts as missing and is noted). Date key = the row's `updated` cell.
  status.json   `results[]`. Audit 1 done = audit_status 'one audit'/'two audits', or a `novelty`/`class` or
                `audit_refs` set (a verifier class exists). Audit 2 done = audit_status 'two audits'. Counted = a
                `depth` field set (rule 4a; tools/depth_check.py is the counting gate). Date key = the result's
                `date`. Readings only: claim_scope recovered-passages, completed-reading, key-to-known-text, or none;
                corrections and catalogue contributions are skipped (not readings). key-to-known-text is never
                counted (depth_check.py: N0-N2 / key-to-known-text are not counted), so it is listed only when
                Audit 2 is missing.
priority: high = actionable; low = Audit 2 missing on an N0/N1 or key-to-known-text item (Outreach gate 2 applies
above N1 only); none = Counted '.' but the count is already decided ('not counted' in the note, or latest class N0-N2):
listed so nothing is dropped, with "no verifier action". status.json counted-missing likewise skips N0-N2 classes.
Order: priority (high, low, none), then audit1_date ascending (unparseable dates last), then source, then name.
Reconciliation: each register's rows are listed independently; the note says whether the other register has the same
folder, and with what audit state, or that the folder is absent from it. Nothing is dropped for being in one only.

Catches: a reading that sat at one audit or uncounted with no verifier assigned (the 5 Oct 2026 parent review: the
backlog was spread over two registers nobody diffed).
Must NOT: mark a decided 'not counted' / N0-N2 row as an open count (priority none); list a row whose Audit 1 is not done (Armstrong, '1' = .); list a correction/catalogue-contribution result;
list a key-to-known-text result with two audits as "counted missing"; drop a status.json result whose folder has no
PROGRESS.tsv row (it is listed with note 'absent from PROGRESS.tsv'). Offline tests: tools/tests/test_verify_backlog.py.
"""
import argparse, csv, datetime, json, re, sys

PROGRESS = "PROGRESS.tsv"
STATUS = "status.json"
OUT = "VERIFY-BACKLOG.tsv"
COLS = ["name", "folder", "leaf_row", "audit1_date", "missing", "priority", "next_action", "source", "note"]
READING_SCOPES = {None, "", "recovered-passages", "completed-reading", "key-to-known-text"}
NOT_COUNTABLE = {"key-to-known-text"}
MONTHS = {m: i + 1 for i, m in enumerate(
    ["jan", "feb", "mar", "apr", "may", "jun", "jul", "aug", "sep", "oct", "nov", "dec"])}


def parse_date(s):
    """'2 Oct 2026', '26 Sept 2026', '2026-10-03', '2026-10-03 15:3x' -> 'YYYY-MM-DD', or '' when unparseable."""
    s = (s or "").strip()
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s)
    if m:
        return "%s-%s-%s" % m.groups()
    m = re.match(r"(\d{1,2})\s+([A-Za-z]+)\.?\s+(\d{4})", s)
    if m and m.group(2)[:3].lower() in MONTHS:
        try:
            return datetime.date(int(m.group(3)), MONTHS[m.group(2)[:3].lower()], int(m.group(1))).isoformat()
        except ValueError:
            return ""
    return ""


def folder_of(link):
    m = re.search(r"/ciphers/([^/\s]+)", link or "")
    return m.group(1) if m else ""


def load_progress(path):
    with open(path, encoding="utf-8") as fh:
        lines = [l for l in fh if not l.startswith("#") and l.strip()]
    rows = list(csv.DictReader(lines, delimiter="\t"))
    for i, r in enumerate(rows, 1):
        r["_n"] = i
    return rows


def load_results(path):
    with open(path, encoding="utf-8") as fh:
        return json.load(fh).get("results", [])


def next_action(folder, miss, scope_note=""):
    a2 = ("second adversarial audit per CLAUDE.md Outreach gate 2 (separate session from Audit 1's): search to disprove "
          "novelty, open-index + Google Books + JSTOR-QUEUE.tsv rows; append to ciphers/%s/AUDIT.md, set status.json "
          "audit_status 'two audits', PROGRESS.tsv `2`" % folder)
    cnt = ("count per rule 4/4a: verifier sets depth/depth_pct/depth_sentence/depth_check/decode_status in status.json "
           "+ ciphers/%s/AUDIT.md, then python3 tools/depth_check.py; PROGRESS.tsv `C`" % folder)
    if miss == "audit2":
        return a2
    if miss == "counted":
        return cnt
    return "1) " + a2 + "; 2) " + cnt


LOW_CLASS = {"N0", "N1", "N2"}


def last_class(text):
    """Latest N-class named in a PROGRESS.tsv note ('audit 2 N0 confirmed' -> 'N0'), '' when none."""
    m = re.findall(r"\bN([0-5])\b", text or "")
    return "N" + m[-1] if m else ""


def progress_state(rows):
    return ",".join("%s:1%s2%sC%s" % (r["name"], r.get("1", "?"), r.get("2", "?"), r.get("C", "?")) for r in rows)


def result_state(rs):
    return ",".join("[%d]%s/%s" % (i, (e.get("audit_status") or "none").replace(" ", "-"),
                                   e.get("depth") or "nodepth") for i, e in rs)


def build(progress, results):
    by_folder_p, by_folder_s = {}, {}
    for r in progress:
        by_folder_p.setdefault(r["folder"], []).append(r)
    for i, e in enumerate(results):
        by_folder_s.setdefault(folder_of(e.get("link")), []).append((i, e))
    out = []
    for r in progress:
        if r.get("1") != "x":
            continue
        m2, mc = r.get("2") != "x", r.get("C") != "x"
        if not (m2 or mc):
            continue
        cls = last_class(r.get("note"))
        decided = bool(re.search(r"not counted", r.get("note") or "", re.I)) or cls in LOW_CLASS
        if mc and decided:
            mc = False
            decided_note = "count decided: " + ("note says 'not counted'" if cls not in LOW_CLASS else
                                                "class %s, not countable (depth_check.py)" % cls)
        else:
            decided_note = ""
        if not (m2 or mc):
            out.append({"name": r["name"], "folder": r["folder"], "leaf_row": "PROGRESS.tsv row %d" % r["_n"],
                        "audit1_date": parse_date(r.get("updated")), "missing": "counted",
                        "priority": "none",
                        "next_action": "no verifier action: %s; PROGRESS.tsv `C` stays '.' until the reading changes"
                                       % decided_note, "source": "PROGRESS.tsv", "note": decided_note})
            continue
        miss = "both" if (m2 and mc) else ("audit2" if m2 else "counted")
        notes = ["latest class in note: %s" % cls] if cls else []
        if decided_note:
            notes.append(decided_note)
        partial = [k for k in ("2", "C") if r.get(k) == "~"]
        if partial:
            notes.append("partial mark in " + "/".join(partial))
        rs = by_folder_s.get(r["folder"])
        notes.append("status.json: " + result_state(rs) if rs else "absent from status.json results")
        out.append({"name": r["name"], "folder": r["folder"], "leaf_row": "PROGRESS.tsv row %d" % r["_n"],
                    "audit1_date": parse_date(r.get("updated")), "missing": miss,
                    "priority": "low" if (miss == "audit2" and cls in ("N0", "N1")) else "high",
                    "next_action": next_action(r["folder"], miss), "source": "PROGRESS.tsv",
                    "note": "; ".join(notes)})
    for i, e in enumerate(results):
        folder = folder_of(e.get("link"))
        scope = e.get("claim_scope")
        if not folder or scope not in READING_SCOPES:
            continue
        st = e.get("audit_status") or ""
        a1 = st in ("one audit", "two audits") or bool(e.get("novelty") or e.get("class") or e.get("audit_refs"))
        if not a1:
            continue
        cls = e.get("novelty") or e.get("class") or ""
        m2 = st != "two audits"
        mc = not e.get("depth") and scope not in NOT_COUNTABLE and cls not in LOW_CLASS
        if not (m2 or mc):
            continue
        miss = "both" if (m2 and mc) else ("audit2" if m2 else "counted")
        notes = ["scope %s" % (scope or "unset"), "class %s" % (cls or "unset")]
        ps = by_folder_p.get(folder)
        notes.append("PROGRESS.tsv: " + progress_state(ps) if ps else "absent from PROGRESS.tsv")
        if ps and m2 and all(p.get("2") == "x" for p in ps):
            notes.append("REGISTERS DISAGREE: PROGRESS.tsv has Audit 2 done for every row of this folder")
        title = re.sub(r"\s+", " ", e.get("title") or "")[:90]
        out.append({"name": title, "folder": folder, "leaf_row": "status.json results[%d]" % i,
                    "audit1_date": parse_date(e.get("date")), "missing": miss,
                    "priority": "low" if (miss == "audit2" and (cls in ("N0", "N1") or scope in NOT_COUNTABLE))
                    else "high",
                    "next_action": next_action(folder, miss), "source": "status.json", "note": "; ".join(notes)})
    rank = {"high": 0, "low": 1, "none": 2}
    out.sort(key=lambda d: (rank[d["priority"]], d["audit1_date"] or "9999", d["source"], d["name"]))
    return out


def render(rows, today):
    head = ["# VERIFY-BACKLOG.tsv -- generated by tools/verify_backlog.py on %s UTC; do not edit by hand, re-run it." % today,
            "# Readings with Audit 1 done and Audit 2 and/or Counted missing, from PROGRESS.tsv and status.json results.",
            "# Sort: priority (high, low, none) then audit1_date ascending = PROGRESS.tsv `updated` / status.json `date` (a register date, not the audit's "
            "own); see the tool's docstring for what counts as done. missing: audit2 | counted | both.",
            "# Consumer: LANE-VER1. A row listed from both registers for the same folder may be the same reading: read note."]
    body = ["\t".join(COLS)] + ["\t".join(d[c].replace("\t", " ") for c in COLS) for d in rows]
    return "\n".join(head + body) + "\n"


def strip_gen(text):
    return [l for l in text.splitlines() if not l.startswith("# VERIFY-BACKLOG.tsv -- generated")]


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--progress", default=PROGRESS)
    ap.add_argument("--status", default=STATUS)
    ap.add_argument("--out", default=OUT)
    ap.add_argument("--stdout", action="store_true")
    ap.add_argument("--check", action="store_true", help="exit 1 if --out differs from a fresh build")
    a = ap.parse_args(argv)
    rows = build(load_progress(a.progress), load_results(a.status))
    text = render(rows, datetime.datetime.now(datetime.timezone.utc).strftime("%Y-%m-%d %H:%M"))
    if a.check:
        try:
            old = open(a.out, encoding="utf-8").read()
        except FileNotFoundError:
            print("STALE: %s missing" % a.out)
            return 1
        if strip_gen(old) != strip_gen(text):
            print("STALE: %s differs from a fresh build; re-run python3 tools/verify_backlog.py" % a.out)
            return 1
        print("OK: %s current (%d rows)" % (a.out, len(rows)))
        return 0
    if a.stdout:
        sys.stdout.write(text)
    else:
        with open(a.out, "w", encoding="utf-8") as fh:
            fh.write(text)
    counts = {}
    for d in rows:
        counts[d["missing"]] = counts.get(d["missing"], 0) + 1
    print("%d rows: %s" % (len(rows), ", ".join("%s %d" % kv for kv in sorted(counts.items()))), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

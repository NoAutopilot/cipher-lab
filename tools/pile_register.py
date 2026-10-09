#!/usr/bin/env python3
"""pile_register.py: one register per pool of letters -- the letters held, the letters referenced but not held -- and a
text timeline; plus a scan of an edition's text for back-references ('your letter of the 19th') as leads.

After Lasry, Biermann and Tomokiyo 2023 (Cryptologia 47:2), App. C pp.200-202, Figs 17 and C25-C26 (the per-pile list
of letters known and referenced-but-missing, and the timeline drawn from it), which follow Bossy 2001 in reading the
letters a correspondent mentions as part of the pile. MQS-PILE-REGISTER (LANE MQS-3, 9 Oct 2026); paper row M05 + M32.

Held rows come from tools/holder_export.py's own row builder (read_list + build_rows: status.json joined to the
folder's reading files), so the register has no second parser of a target's files. Pool input, one of:
  LIST.tsv        a holder_export list (columns 'document' and 'folder' at least; comment lines start with '#')
  --pool FOLDER   every status.json result whose link contains FOLDER (repeatable; superseded results skipped)

  --refs REFS.tsv  referenced letters: columns date (YYYY-MM-DD or as written), from, to, mentioned_in, note. A
                   referenced row whose date is within --tol days of a held row with the same from/to (or with either
                   side blank) is reported as 'held?' with that row id instead of 'referenced' -- a letter is never
                   counted twice.

Output: STEM.tsv (class, iso date, date as written, from, to, place, row id, folder or mentioned in, note) and
STEM-timeline.txt (one line per letter by date, undated last). --check (rule 7) regenerates both and exits 1 if the
committed files differ.

--refs-scan EDITION.txt --dates DATES.tsv [--window N] [--tol N] [--scan-out FILE]
  Leads, never a decision. The edition text is cut into letters at its date lines (place, month, day, 4-digit year in
  English, French, Spanish, Italian, Dutch, German or Latin month names; OCR suffixes such as '18t', '20%', '19°'
  tolerated). Each letter whose own date is within --window days (default 3) of a date in DATES.tsv (column 'iso' or
  'date'; a register STEM.tsv also works) is grepped for REF_PATTERNS, and the date each reference names is resolved
  against the letter's own date: an explicit month (year = latest year not after the letter); 'instant' = the
  letter's month; 'ult(imo)' = the month before; a bare day = this month if not after the letter's day, else the month
  before ('inferred'); 'to-day' = the letter's date. Each lead row: letter date, resolved date, how resolved, whether a
  DATES row is within --tol days (held) or not (lead for a referenced-but-missing letter), and the phrase as printed.

Shelf grade (tools/data/tool_shelf.tsv): the register is plumbing (offline tests only); --refs-scan is graded from the
known-answer control in tools/tests/PREREG-MQS-PILE-REGISTER.md (tools/tests/mqs_pile_register_control.py, Bowdoin
and Temple Papers II, MHS 1907): see the shelf row for the numbers.

Must catch (tools/tests/test_pile_register.py): held rows built through holder_export.build_rows; a referenced letter
that is already held reported 'held?' not counted twice; timeline order by date with undated last; 'your favour of the
19° instant' resolved to the letter's month; 'of the 24 ult' to the month before; 'of Oct. 20' with the year of the
letter; a French 'votre lettre du 3 mars'; --check failing on a stale register. Must NOT flag: a date line inside a
letter's body that is not a reference ('Boston, Jany 21, 1787' is a segment boundary, not a lead); 'your letter' with
no date after it (no lead: nothing to resolve); a reference whose date matches a DATES row (reported held, not as a
missing letter).

Usage:
  python3 tools/pile_register.py LIST.tsv --out DIR/STEM [--refs REFS.tsv] [--status status.json] [--check]
  python3 tools/pile_register.py --pool ciphers/<slug> --out DIR/STEM [--refs REFS.tsv]
  python3 tools/pile_register.py --refs-scan EDITION.txt --dates DATES.tsv [--window 3] [--tol 1] [--scan-out leads.tsv]
"""
import argparse
import csv
import datetime as dt
import filecmp
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import holder_export as he  # noqa: E402

ROOT = HERE.parent
REG_COLS = ["class", "iso", "date as written", "from", "to", "place", "row id", "source", "note"]

MONTHS = {}
for i, names in enumerate([
        "jan january janv janvier januarius januari januar enero gennaio jany", "feb february feby fev fevr fevrier fevrier "
        "februarius februari februar febrero febbraio feb'", "mar march mars martius maart marz marzo",
        "apr april avr avril aprilis abril aprile", "may mai maius mei mayo maggio",
        "jun june juin junius juni junio giugno", "jul july juil juillet julius juli julio luglio",
        "aug august aout augustus augusti agosto augt", "sep sept september septembre septembris septiembre settembre 7ber",
        "oct october octobre octobris oktober octubre ottobre 8ber", "nov noy november novembre novembris noviembre 9ber",
        "dec december decembre decembris dezember diciembre dicembre 10ber"], 1):
    for n in names.split():
        MONTHS[n] = i
MONTH_RE = r"(?:%s)" % "|".join(sorted((re.escape(m) for m in MONTHS), key=len, reverse=True))
# OCR'd day: digits plus up to three suffix marks (18t, 20%, 19°, 21st, 3d, 2°)
DAY = r"(\d{1,2})(?:st|nd|rd|th|d|[^\s\d,.;:]{1,3})?"
PUNCT = r"\w*[.’'`,?*‘]*"  # OCR tail of a month word: Decemr, Oct?, Sept*, Feb'
FILL = r"(?:(?:the|y\S{0,2})\s+)?"  # 'March the 7', 'Feby y* 20'

SKIP = r"(?:(?:the|y[^\s]{0,2}|le|del?|du|of|instant)\s+)*"
REF_PATTERNS = [
    r"your\s+(?:excellency[’']?s\s+|honou?r[’']?s\s+)?(?:last\s+)?(?:letters?|favou?rs?|despatch(?:es)?|dispatch(?:es)?|"
    r"note|communication)\s+of",
    r"my\s+(?:last\s+)?(?:letters?|despatch(?:es)?|dispatch(?:es)?)\s+of",
    r"v[oô]s?tre\s+(?:derni[eè]re\s+)?(?:lettre|depesche|d[ée]p[eê]che)s?\s+du",
    r"ma\s+(?:derni[eè]re\s+)?(?:lettre|depesche|d[ée]p[eê]che)s?\s+du", r"la\s+v[oô]s?tre\s+du",
    r"(?:vuestra|su|mi)\s+carta\s+de", r"(?:la\s+sua|la\s+vostra|la\s+mia)\s+(?:lettera\s+)?del?",
    r"uwen?\s+brief\s+van", r"(?:ihr|euer|mein)\s+schreiben\s+vom",
]
# the context is a lookahead, so a reference inside another's context is still found ('your letter of Oct. 20 and
# my letter of Dec 31')
REF_RE = re.compile("(" + "|".join(REF_PATTERNS) + r")\s+(?=(.{0,48}))", re.I | re.S)
DATELINE_RE = re.compile(r"^[\[\s]*.{0,40}?\b(?:(" + MONTH_RE + r")" + PUNCT + r"\s*" + FILL + DAY +
                         r"[,.]?\s*(1[6-8]\d\d)|" + DAY + r"[,.]?\s+(?:(?:de|of)\s+)?(" + MONTH_RE + r")" + PUNCT +
                         r"\s*(?:de\s+)?(1[6-8]\d\d))[\s.,*—\-\]]*$", re.I)


def norm_month(s):
    s = re.sub(r"[^a-z0-9]", "", s.lower().replace("é", "e").replace("û", "u").replace("ä", "a"))
    return MONTHS.get(s) or MONTHS.get(s[:3]) if s else None


def safe_date(y, m, d):
    try:
        return dt.date(y, m, d)
    except ValueError:
        return None


def parse_dateline(line):
    """A letter's own place-and-date line -> date, else None. Short lines only (a body sentence is not a header)."""
    line = line.strip()
    if len(line) > 60:
        return None
    m = DATELINE_RE.match(line)
    if not m:
        return None
    if m.group(1):
        mo, day, yr = norm_month(m.group(1)), m.group(2), m.group(3)
    else:
        day, mo, yr = m.group(4), norm_month(m.group(5)), m.group(6)
    return safe_date(int(yr), mo, ocr_day(day)) if mo else None


def ocr_day(s):
    """'34' (3d) and '224' (22d) read as days: an impossible two-digit day keeps its first digit."""
    d = int(s)
    return d if d <= 31 else int(s[0])


def segments(text):
    """Cut an edition text into letters at its date lines: [(date, first line number, body text)]."""
    lines = text.splitlines()
    starts = [(i, d) for i, d in ((i, parse_dateline(l)) for i, l in enumerate(lines)) if d]
    out = []
    for k, (i, d) in enumerate(starts):
        j = starts[k + 1][0] if k + 1 < len(starts) else len(lines)
        out.append((d, i + 1, "\n".join(lines[i + 1:j])))
    return out


def month_back(d, n=1):
    y, m = d.year, d.month - n
    while m < 1:
        m, y = m + 12, y - 1
    return y, m


def resolve(after, letter):
    """The words after a reference phrase -> (date, how) or (None, why)."""
    s = re.sub(r"\s+", " ", after)
    if re.match(r"\s*(?:the\s+)?(?:to-?day|this\s+day|ce\s+jour|hoy)\b", s, re.I):
        return letter, "today"
    m = re.match(r"\s*" + SKIP + r"(" + MONTH_RE + r")" + PUNCT + r"\s*" + FILL + DAY +
                 r"(?:[,.]?\s*(1[6-8]\d\d))?", s, re.I)
    if m and norm_month(m.group(1)):
        mo, day, yr = norm_month(m.group(1)), ocr_day(m.group(2)), m.group(3)
        return _with_year(letter, mo, day, yr), "explicit"
    m = re.match(r"\s*" + SKIP + DAY + r"\s*(?:(?:of|de|du)\s+)?(?:(" + MONTH_RE + r")" + PUNCT + r"\s*(?:(1[6-8]\d\d))?|"
                 r"(inst\w*|ins[‘'’`]?\w*)|(ult\w*|ulto?\b[.’'`?]?|der\w* passé|pass[ée]))?", s, re.I)
    if not m:
        return None, "no date"
    day = ocr_day(m.group(1))
    if not 1 <= day <= 31:
        return None, "no date"
    if m.group(2) and norm_month(m.group(2)):
        return _with_year(letter, norm_month(m.group(2)), day, m.group(3)), "explicit"
    if m.group(4):
        return safe_date(letter.year, letter.month, day), "instant"
    if m.group(5):
        y, mo = month_back(letter)
        return safe_date(y, mo, day), "ult"
    if day <= letter.day:
        return safe_date(letter.year, letter.month, day), "inferred"
    y, mo = month_back(letter)
    return safe_date(y, mo, day), "inferred"


def _with_year(letter, mo, day, yr):
    if yr:
        return safe_date(int(yr), mo, day)
    d = safe_date(letter.year, mo, day)
    if d and d > letter:
        d = safe_date(letter.year - 1, mo, day)
    return d


def scan_refs(text, dates, window=3, tol=1):
    """Leads: one dict per back-reference found in a letter dated within `window` days of one of `dates`."""
    dates = sorted(set(dates))
    leads = []
    for d, line, body in segments(text):
        if not any(abs((d - x).days) <= window for x in dates):
            continue
        for m in REF_RE.finditer(body):
            got, how = resolve(m.group(2), d)
            if not got:
                continue
            near = [x for x in dates if abs((got - x).days) <= tol]
            leads.append({"letter": d.isoformat(), "line": line, "refers_to": got.isoformat(), "how": how,
                          "status": "held" if near else "lead",
                          "phrase": he.clean(m.group(1) + " " + m.group(2)[:30])})
    return leads


def read_dates(path):
    rows = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    rd = csv.DictReader(rows, delimiter="\t", quoting=csv.QUOTE_NONE)
    out = []
    for r in rd:
        v = (r.get("iso") or r.get("date") or "").strip()
        try:
            out.append(dt.date.fromisoformat(v[:10]))
        except ValueError:
            continue
    return out


# ---------------------------------------------------------------- register

def pool_list(status, folders):
    rows = []
    for r in status.get("results", []):
        link = r.get("link") or ""
        if r.get("superseded_by") or not any(f in link for f in folders):
            continue
        rows.append({k: "" for k in ("title", "class", "depth (", "depth_pct", "completeness", "unresolved", "weak",
                                     "key", "documents")} | {"document": r.get("document_id", ""), "folder": link})
    return rows


def builder_args(status, repo_root):
    """The argparse namespace holder_export.build_rows reads, at its own defaults (no holder, no URL)."""
    return argparse.Namespace(alias=[], url_template="", holder="", holder_short="holder", book_object=[],
                              book_label="", volunteer_project="", pin="", prepared="", credit="", about="",
                              status=status, repo_root=repo_root, list="", meta="", out="", no_xlsx=True, check=False,
                              accept_count=[], select_class="", select_min_audits=0, select_scope="", select_folder="")


def held_rows(list_rows, status, repo_root, status_path):
    he.GRADE_LABEL.setdefault("H", "from the cipher book")
    rows, _ = he.build_rows(list_rows, status, repo_root, {}, builder_args(status_path, repo_root))
    K = he.KEYS
    out = []
    for r in rows:
        c = dict(zip(K, r))
        out.append({"class": "held", "iso": c["iso"], "date as written": c["date"], "from": c["from"], "to": c["to"],
                    "place": c["place"], "row id": c["row_id"], "source": c["rlink"] or c["call"], "note": ""})
    return out


def iso_of(s):
    s = (s or "").strip()
    try:
        return dt.date.fromisoformat(s[:10])
    except ValueError:
        i = he.iso_date(s)
        try:
            return dt.date.fromisoformat(i) if i else None
        except ValueError:
            return None


def same_party(a, b):
    a, b = he.clean(a).lower(), he.clean(b).lower()
    return not a or not b or a in b or b in a


def referenced_rows(path, held, tol):
    rows = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    out = []
    for n, r in enumerate(csv.DictReader(rows, delimiter="\t", quoting=csv.QUOTE_NONE), 1):
        r = {k: (v or "").strip() for k, v in r.items() if k}
        d = iso_of(r.get("date"))
        row = {"class": "referenced", "iso": d.isoformat() if d else "", "date as written": r.get("date", ""),
               "from": r.get("from", ""), "to": r.get("to", ""), "place": r.get("place", ""), "row id": f"ref{n}",
               "source": r.get("mentioned_in", ""), "note": r.get("note", "")}
        for h in held:
            hd = iso_of(h["iso"])
            if d and hd and abs((d - hd).days) <= tol and same_party(row["from"], h["from"]) and \
                    same_party(row["to"], h["to"]):
                row["class"], row["note"] = "held?", ("matches held " + h["row id"] + "; " + row["note"]).strip("; ")
                break
        out.append(row)
    return out


def timeline(rows):
    key = (lambda r: (r["iso"] == "", r["iso"], r["row id"]))
    lines = ["# timeline: held = in the pool; referenced = mentioned, not held; held? = a reference matching a held row"]
    for r in sorted(rows, key=key):
        lines.append(f"{r['iso'] or 'undated':10}  {r['class']:10}  {r['from'] or '?'} -> {r['to'] or '?'}"
                     f"  [{r['row id']}]" + (f"  {r['note']}" if r["note"] else ""))
    n = {c: sum(r["class"] == c for r in rows) for c in ("held", "referenced", "held?")}
    lines.append(f"# {n['held']} held, {n['referenced']} referenced-not-held, {n['held?']} references matching a held row")
    return "\n".join(lines) + "\n"


def write_register(rows, stem):
    stem = Path(stem)
    stem.parent.mkdir(parents=True, exist_ok=True)
    rows = sorted(rows, key=lambda r: (r["iso"] == "", r["iso"], r["row id"]))
    with open(f"{stem}.tsv", "w", encoding="utf-8", newline="") as f:
        f.write("\t".join(REG_COLS) + "\n")
        for r in rows:
            f.write("\t".join(he.clean(r[c]) for c in REG_COLS) + "\n")
    Path(f"{stem}-timeline.txt").write_text(timeline(rows), encoding="utf-8")


def build_register(args):
    status = json.loads(Path(args.status).read_text(encoding="utf-8"))
    list_rows = he.read_list(args.list) if args.list else pool_list(status, args.pool)
    held = held_rows(list_rows, status, args.repo_root, args.status)
    refs = referenced_rows(args.refs, held, args.tol) if args.refs else []
    return held + refs


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("list", nargs="?", help="holder_export list TSV (or use --pool)")
    ap.add_argument("--pool", action="append", help="folder substring of status.json result links (repeatable)")
    ap.add_argument("--out", help="output stem: writes STEM.tsv and STEM-timeline.txt")
    ap.add_argument("--refs", help="referenced letters TSV (date, from, to, mentioned_in, note)")
    ap.add_argument("--status", default=str(ROOT / "status.json"))
    ap.add_argument("--repo-root", default=str(ROOT))
    ap.add_argument("--tol", type=int, default=1, help="days within which two dates are the same letter (default 1)")
    ap.add_argument("--check", action="store_true", help="exit 1 if the committed register is stale (rule 7)")
    ap.add_argument("--refs-scan", metavar="EDITION.txt", help="scan an edition text for back-references (leads)")
    ap.add_argument("--dates", help="TSV with an 'iso' or 'date' column: the held letters' dates for --refs-scan")
    ap.add_argument("--window", type=int, default=3, help="--refs-scan: days around each date whose letters are "
                    "scanned (default 3)")
    ap.add_argument("--scan-out", help="--refs-scan: write the leads TSV here (default: stdout)")
    a = ap.parse_args(argv)

    if a.refs_scan:
        if not a.dates:
            ap.error("--refs-scan needs --dates")
        leads = scan_refs(Path(a.refs_scan).read_text(encoding="utf-8", errors="replace"), read_dates(a.dates),
                          a.window, a.tol)
        cols = ["letter", "line", "refers_to", "how", "status", "phrase"]
        body = "\t".join(cols) + "\n" + "".join("\t".join(str(x[c]) for c in cols) + "\n" for x in leads)
        if a.scan_out:
            Path(a.scan_out).write_text(body, encoding="utf-8")
        else:
            sys.stdout.write(body)
        n = sum(x["status"] == "lead" for x in leads)
        print(f"refs-scan: {len(leads)} reference(s) resolved, {n} to no held date (leads, not decisions)",
              file=sys.stderr)
        return 0
    if not a.out or not (a.list or a.pool):
        ap.error("give LIST.tsv or --pool, and --out")
    rows = build_register(a)
    if a.check:
        tmp = Path(tempfile.mkdtemp())
        try:
            write_register(rows, tmp / "r")
            stale = [ext for ext in (".tsv", "-timeline.txt")
                     if not Path(f"{a.out}{ext}").exists() or not filecmp.cmp(f"{a.out}{ext}", tmp / f"r{ext}",
                                                                             shallow=False)]
        finally:
            shutil.rmtree(tmp)
        for s in stale:
            print(f"stale: {a.out}{s}")
        print("check: " + ("FAIL" if stale else "ok") + f" ({len(rows)} rows)")
        return 1 if stale else 0
    write_register(rows, a.out)
    n = {c: sum(r["class"] == c for r in rows) for c in ("held", "referenced", "held?")}
    print(f"wrote {a.out}.tsv and -timeline.txt: {n['held']} held, {n['referenced']} referenced, {n['held?']} held?")
    return 0


if __name__ == "__main__":
    sys.exit(main())

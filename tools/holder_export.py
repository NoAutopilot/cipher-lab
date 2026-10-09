#!/usr/bin/env python3
"""holder_export.py: turn a list of read items into a spreadsheet a holding library can load against its own records.

Reads a list TSV like outreach/huntington-decipherments-list-2026-10-08.tsv (comment lines start with '#'; columns
'document', 'depth (rule 4a)', 'depth_pct', 'completeness', 'unresolved', a 'weak ...' column, 'key used', 'documents'
and 'folder'), joins each row to its status.json result (by document_id) and to the target folder named in 'folder',
and writes ONE ROW PER ITEM (telegram, letter, enclosure) keyed by the holder's own collection alias and record number
(a CONTENTdm number), so the holder can match it to its catalogue records. Output: STEM.csv (UTF-8 with a byte-order
mark, for Excel), STEM.tsv (plain UTF-8, for a CONTENTdm import; no tab or line break inside a cell) and
STEM-README.txt always; STEM.xlsx when openpyxl is importable ('Read me first' sheet first, then 'Readings' and a
long-form 'Code words' sheet); without openpyxl it says so and writes the text files only.

Columns, in this order (COLUMN_SPEC; '{h}' is --holder-short): CONTENTdm collection alias; CONTENTdm number; record
level; row id (our entry); {h} call number; page title (Digital Library) or pages read; telegram numbers on this page;
Digital Library URL; date and time as written; date (YYYY-MM-DD); from; to; place; transcribed from; ledger/page text
as we transcribed it; reading (marked up); reading (plain text); summary (one sentence); code words and meanings;
cipher book or key used; cipher book (Digital Library URL); uncertain or unread words; how much is read; adds less?
(and why); prior print checked; partly in print?; prior-publication check (class); reading (repository link); search
log (repository link); suggested credit line.

Target layouts read (auto-detected, no per-target configuration):
  md-blocks   reading*.md files with a '<!-- decode.py: derived block starts -->' block of '**ID | ...**' paragraphs
              and the matching ciphertext*.txt '### ID | ...' blocks and key*.md (same suffix: reading-no2.md <->
              ciphertext-no2.txt <-> key-no2.md). The code-word list comes from the folder's own decode.py: its
              decode_entry(..., tokens=[]) when it takes a tokens list (one tuple per counted token, so the list is
              exactly what the derived block counts, the folder's plain:/variant:/gloss:/graded: notes included), else
              a walk with its lookup(); never a private copy of its rules. A mismatch with the reading's 'Code-word
              tokens:' line is warned. Holder page titles and the 'telnum' field come from the folder's cached
              CONTENTdm records sources/**/p<pointer>.json; a header 'continues on page N' is matched to the next
              pointer's record.
  decode-key  decode.json jobs of tools/decode_key.py (ciphertext TSV, reading TSV, token TSV with grades); an item is a
              line-id prefix (BLA186 in BLA186_p1_L01), matched against the document text with spaces removed;
              page pointers from images/manifest.json (item, page, pointer) when present. An unread group [n] in the
              reading is shown as [?n].

Splitting: a row whose status.json 'documents' name two items the reading files keep apart (E4 and E5) becomes two
rows. A row whose 'documents' count is larger than the items found (two telegrams in one ledger entry) stays one row
and its reading cell says 'N telegrams in this entry'. A list document naming '(first telegram)' or '(second
telegram)' gets only that part of the ledger entry (split at the clerk's 'another' after the first signature): text,
reading, code words and counts.

Count check: each row's token counts by grade are compared with the audited 'completeness' of the list row (parsed
where it gives figures: '28/30 code words H', '13 H + 1 I of 14', '17 H/C of 21 (H 15, C 2, M 2, I 1)'); every
difference is printed. A difference is a fact for a verifier, not something this tool settles: the row shows the
token counts (they match its own code-word list); --accept-count ID names a difference already reported.

--meta FILE: TSV with an 'item' column and any of META_KEYS (a 'source' column is allowed and ignored); a non-empty
cell replaces the computed value ('-' blanks it); 'note' is put in front of the reading; 'unresolved' replaces the
list's own 'unresolved' text for that item. Use it for what the folder does not state in a parseable form.

--select-*: re-run a selection rule on status.json and report drift against the list (rows that no longer pass, and
results that pass but are not listed). The list is never edited by the tool, and the export follows the list: a
listed row that no longer passes is a stale list (fix the list); a passing result not on the list is printed only,
since adding an item to an outward list needs its own gates (CLAUDE.md Outreach gates 2 and 7).

--check (rule 7): regenerate into a temporary directory and compare STEM.csv, STEM.tsv and STEM-README.txt with the
committed files; exit 1 on any difference, on a listed row that no longer passes the selection, or on a count
difference not named by --accept-count. The .xlsx is not compared byte for byte (it carries a zip timestamp); it is
written from the same rows.

Why a separate tool and not a mode of tools/holder_dataset.py (BNF-FOCUS, 7 Oct 2026): that tool writes one row per
folder or per classified reading for catalogue enrichment; this one writes one row per telegram or letter keyed by
the holder's page or object number, which needs the folder's decoder, the split/part rules and the holder's records.

Wording rules (CLAUDE.md rules 4, 4a, 10): grades spelled out; depth by the rule-4a outward words, without the
percentage or the D-number; class by its N-class meaning; the prior-print cell says 'not found in ...' and never
new/first/unpublished. Personal data (rule 9): the tool writes only the list, status.json and the folder's files;
nothing from the environment.

Must catch (tests/test_holder_export.py): column order; the E4/E5-style split; the 'N telegrams in this entry' note;
a '(second telegram)' row cut to its part; a 'graded:' token counted and listed as written; a count that differs from
the audited completeness reported and failing --check; the fallback without openpyxl; no '[SIGN-OFF]' and no e-mail
address in any output; a prior-print cell without a source and a date warned; --check on stale outputs. Must NOT
block: a list row with no status.json result or no readable folder (written with the list's own fields, warned on
stderr); a passing result missing from the list (printed, not fatal).

Usage:
  python3 tools/holder_export.py LIST.tsv --out DIR/STEM [--meta META.tsv] [--status status.json]
      [--url-template 'https://host/digital/collection/{alias}/id/{pointer}'] [--alias mssEC=p16003coll11 ...]
      [--holder 'the Huntington Library'] [--holder-short Huntington] [--volunteer-project NAME]
      [--book-object 'mssEC 41=351' ...] [--about TEXT] [--prepared '9 Oct 2026'] [--pin COMMIT]
      [--credit TEXT] [--no-xlsx] [--check] [--accept-count ID ...]
      [--select-class N3,N4 --select-min-audits 2 --select-scope completed-reading,recovered-passages
       --select-folder eckert-1864,huntington-blathwayt-madrid-1728]
Exit 0 on success; 1 when --check finds a difference; 2 on a usage error.
"""
import argparse
import csv
import datetime
import filecmp
import importlib.util
import inspect
import json
import re
import shutil
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
REPO_URL = "https://github.com/NoAutopilot/cipher-lab"

COLUMN_SPEC = [
    ("alias", "CONTENTdm collection alias"),
    ("number", "CONTENTdm number"),
    ("level", "record level"),
    ("row_id", "row id (our entry)"),
    ("call", "{h} call number"),
    ("page", "page title (Digital Library) or pages read"),
    ("telnum", "telegram numbers on this page ({h} 'Telegram Number' field)"),
    ("url", "Digital Library URL"),
    ("date", "date and time as written"),
    ("iso", "date (YYYY-MM-DD)"),
    ("from", "from"),
    ("to", "to"),
    ("place", "place"),
    ("source", "transcribed from"),
    ("ledger", "ledger/page text as we transcribed it"),
    ("reading", "reading (marked up)"),
    ("plain", "reading (plain text)"),
    ("summary", "summary (one sentence)"),
    ("codes", "code words and meanings"),
    ("book", "cipher book or key used"),
    ("book_url", "cipher book (Digital Library URL)"),
    ("uncertain", "uncertain or unread words"),
    ("read", "how much is read"),
    ("adds", "adds less? (and why)"),
    ("prior", "prior print checked"),
    ("inprint", "partly in print?"),
    ("class", "prior-publication check (class)"),
    ("rlink", "reading (repository link)"),
    ("alink", "search log (repository link)"),
    ("credit", "suggested credit line"),
]
KEYS = [k for k, _ in COLUMN_SPEC]
META_KEYS = {"holder_call": "call", "holder_page": "page", "pointer": "number", "url": "url", "date": "date",
             "iso_date": "iso", "from": "from", "to": "to", "place": "place", "prior_print": "prior",
             "in_print": "inprint", "summary": "summary", "plain": "plain", "text_source": "source", "book": "book",
             "book_url": "book_url", "level": "level", "telnum": "telnum", "alias": "alias"}
META_EXTRA = ("note", "unresolved")


def columns(short="holder"):
    return [h.replace("{h}", short) for _, h in COLUMN_SPEC]


COLUMNS = columns()

GRADE_LABEL = {"H": "from the cipher book", "C": "from a printed or period decipherment", "S": "cryptanalytic",
               "I": "inferred", "M": "uncertain", "U": "unread"}
GRADE_ORDER = "HCSIMU"
CLASS_MEANING = {
    "N0": "the plaintext and a decipherment of this very item were already known",
    "N1": "the plaintext is already published; ours is an independent re-decipherment",
    "N2": "the plaintext is known elsewhere, but no prior mapping of this cipher text to it was found",
    "N3": "no prior plaintext or decipherment located after a logged search",
    "N4": "no prior decipherment located, with the principal editions, catalogues and project pages searched "
          "(internal or unpublished work not excluded)",
    "N5": "confirmed by the holding archive or a specialist",
}
NUMBER_WORDS = {"one": 1, "two": 2, "three": 3, "four": 4, "five": 5, "six": 6}
MONTH_NUM = {"jan": 1, "feb": 2, "mar": 3, "apr": 4, "may": 5, "jun": 6, "jul": 7, "aug": 8, "sep": 9, "oct": 10,
             "nov": 11, "dec": 12}

START = "<!-- decode.py: derived block starts -->"
END = "<!-- decode.py: derived block ends -->"
MONTH = r"(?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]*\.?"
DATE_RE = re.compile(r"\b(\d{1,2}(?:-\d{1,2})? " + MONTH + r" \d{4})")
TIME_RE = re.compile(r"^\s*(\d{1,2}(?:[.:]\d{2})?\s?(?:AM|PM|A\.\s?M\.|P\.\s?M\.|M\b|noon)|midnight|noon)", re.I)
LEDGER_MONTH = re.compile(r"\b(?:Jan|Jany|Feb|Feby|Mar|Mch|Apr|Apl|April|May|June|July|Jul|Aug|Sept|Sep|Oct|Octo|"
                          r"Nov|Novr|Dec|Decr)\b\.?", re.I)
WASH_RE = re.compile(r"\bWash(?:ington|'n|n|\.)?(?=[\s.,]|$)")
NOTE_PREFIXES = ("plain:", "variant:", "split:", "plain-at:", "gloss:", "join:", "merge:", "graded:", "note:", "#",
                 "<!--")
NEG_RE = re.compile(r"\b(no prior|not located|not found|neither|unprinted|not printed|nothing|unread|not in the)\b", re.I)
PRINT_RE = re.compile(r"\bprints\b|\bin print\b|\bprinted\b(?!\s+(?:correspondence|papers|editions?|volumes?|works|"
                      r"sources|text|accounts?|prints?)\b)", re.I)
JARGON_RE = re.compile(r"(?-i:\b(?:AUD\w*|LS\d*|FM|V1|G3|PROP|FIX|SO)-[A-Z0-9])|\baudit|\bN[0-5]\b|code clause|"
                       r"\bheld\b|\bweak|be-api|snippet|decoded|verifier|grade [A-Z]\b", re.I)
CITE_RE = re.compile(r"\bp\.\s?\d|\bpp\.\s?\d|\b1[5-9]\d\d\b|\bORN?\b|Official Records")
SEARCH_DATE_RE = re.compile(r"\b\d{1,2}(?:-\d{1,2})? (?:Jan|Feb|Mar|Apr|May|June?|July?|Aug|Sept?|Oct|Nov|Dec)[a-z]* "
                            r"20\d\d\b")
ABBR = {"ser", "vol", "vols", "pt", "p", "pp", "no", "nos", "st", "gen", "col", "capt", "lt", "maj", "mr", "dr", "u", "s",
        "jr", "ed", "eds", "cf", "corr", "rec", "i", "ii", "iii", "iv", "v", "a", "b", "c", "d", "e", "f", "g", "h", "j",
        "k", "l", "m", "n", "o", "q", "r", "t", "w", "x", "y", "z", "brig", "lieut", "govr", "esq", "misc", "doc",
        "sess", "cong", "hd", "qrs", "ft", "mss"}
PLACE_NORMAL = [
    (re.compile(r"^(?:Ft\.?|Fortress) Monroe$"), "Fort Monroe"),
    (re.compile(r"^Hd\.? ?Qrs\.? A\.? ?of J\.?$"), "Headquarters, Army of the James"),
    (re.compile(r"^But(?:l|t)ers?'?s? Hd\.?(?: Qrs\.?)?$"), "Butler's headquarters"),
    (re.compile(r"^Bermuda Hundreds$"), "Bermuda Hundred"),
]
NAME_NORMAL = [(re.compile(r"^the\s+"), ""), (re.compile(r"Quartermaster-General"), "Quartermaster General"),
               (re.compile(r"\bFt\.? Monroe\b"), "Fort Monroe")]
# common nouns whose code-word plural the decoder writes "[X]'s": the plain text gives the plural
PLURAL_NOUNS = {"horse", "regiment", "report", "force", "mile", "order", "movement", "gunboat", "department",
                "battery", "volunteer", "rail-road", "rail road", "road", "river", "division", "recruit", "equipment",
                "brigade", "bridge", "rebel", "scout", "steamer", "transport", "cipher", "telegram", "communication",
                "vessel", "boat", "wagon", "gun", "officer", "prisoner", "picket", "corps", "man", "battalion",
                "company", "train", "pontoon", "depot", "dispatch", "despatch", "supply", "troop", "follow"}
SAME_PLURAL = {"men", "troops", "reinforcements", "transports", "telegraphs", "arms", "corps", "cavalry", "infantry",
               "artillery", "ammunition"}
U_STOP = {"unread", "uncertain", "inferred", "signature", "group", "groups", "word", "words", "code", "graded", "and",
          "the", "a", "an", "of", "m", "i", "u", "h", "x2", "x3", "its", "token", "tokens", "one", "two", "both"}


def warn(msg):
    sys.stderr.write("holder_export: " + msg + "\n")


def clean(s):
    """One line per cell: no tab, no line break (a tab-delimited import splits on both)."""
    return re.sub(r"\s+", " ", str(s or "")).strip()


# ---------------------------------------------------------------- list, status, meta

def read_list(path):
    lines = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    if not lines:
        sys.exit("holder_export: empty list " + str(path))
    rows = list(csv.reader(lines, delimiter="\t", quoting=csv.QUOTE_NONE))
    head = rows[0]

    def col(prefix):
        for i, h in enumerate(head):
            if h.strip().lower().startswith(prefix):
                return i
        return None
    idx = {k: col(k) for k in ("document", "title", "class", "depth (", "depth_pct", "completeness", "unresolved",
                               "weak", "key", "documents", "folder")}
    if idx["document"] is None or idx["folder"] is None:
        sys.exit("holder_export: list needs 'document' and 'folder' columns")
    out = []
    for r in rows[1:]:
        r = r + [""] * (len(head) - len(r))
        out.append({k: (r[i].strip() if i is not None else "") for k, i in idx.items()})
    return out


def read_meta(path):
    if not path:
        return {}
    rows = [l for l in Path(path).read_text(encoding="utf-8").splitlines() if l.strip() and not l.startswith("#")]
    rd = list(csv.DictReader(rows, delimiter="\t", quoting=csv.QUOTE_NONE))
    return {r["item"].strip(): {k: (v or "").strip() for k, v in r.items() if k} for r in rd if r.get("item")}


def folder_path(folder, repo_root):
    if "/tree/" in folder:
        rel = folder.split("/tree/", 1)[1].split("/", 1)[1] if folder.split("/tree/", 1)[1].count("/") else ""
        return Path(repo_root) / rel
    return Path(repo_root) / folder


def folder_rel(folder, repo_root):
    try:
        return folder.resolve().relative_to(Path(repo_root).resolve()).as_posix()
    except ValueError:
        return folder.name


# ---------------------------------------------------------------- md-blocks layout

def _load_module(path):
    spec = importlib.util.spec_from_file_location("holder_export_decoder_" + str(abs(hash(str(path)))), path)
    mod = importlib.util.module_from_spec(spec)
    sys.path.insert(0, str(path.parent))
    try:
        spec.loader.exec_module(mod)
    finally:
        sys.path.pop(0)
    return mod


def strip_core(w):
    return w.strip(" .,;:'\"()\\").replace("[?]", "").strip(" \\")


class MdBlocks:
    """reading*.md derived blocks + ciphertext*.txt blocks + key*.md, read with the folder's own decode.py."""

    def __init__(self, folder):
        self.folder = folder
        self.decoder = _load_module(folder / "decode.py") if (folder / "decode.py").exists() else None
        self.items = {}      # id -> dict(header, lines, reading, counts, key, reading_file, line)
        for rpath in sorted(folder.glob("reading*.md")):
            text = rpath.read_text(encoding="utf-8")
            if START not in text or END not in text:
                continue
            suffix = rpath.stem[len("reading"):]
            cpath, kpath = folder / f"ciphertext{suffix}.txt", folder / f"key{suffix}.md"
            if not cpath.exists():
                continue
            key = self.decoder.load_key(kpath) if (self.decoder and kpath.exists()) else None
            if self.decoder:  # the folder's own loader: same block and comment rules as its readings
                blocks = {h.split("|")[0].strip(): (h, ls) for h, ls in self.decoder.load_ciphertext(cpath)}
            else:
                blocks = self._blocks(cpath)
            lines_at = {}
            for n, l in enumerate(text.splitlines(), 1):
                m = re.match(r"^\*\*([^|*]+?)\s*\|", l)
                if m and START in "\n".join(text.splitlines()[:n]):
                    lines_at.setdefault(m.group(1).strip(), n)
            for iid, para, counts in self._readings(text.split(START, 1)[1].split(END, 1)[0]):
                if iid in blocks:
                    header, lines = blocks[iid]
                    self.items[iid] = {"header": header, "lines": lines, "reading": para, "counts": counts,
                                       "key": key, "reading_file": rpath.name, "cipher_file": cpath.name,
                                       "line": lines_at.get(iid, 0)}

    @staticmethod
    def _blocks(path):
        out, cur = {}, None
        for raw in path.read_text(encoding="utf-8").splitlines():
            if raw.startswith("### "):
                header = raw[4:].strip()
                cur = header.split("|")[0].strip()
                out[cur] = (header, [])
            elif cur is not None and not raw.startswith(("#", "<!--", "note:")):
                out[cur][1].append(raw.rstrip())
        return out

    @staticmethod
    def _readings(block):
        parts = re.split(r"^\*\*(.+?)\*\*\s*$", block, flags=re.M)
        for i in range(1, len(parts) - 1, 2):
            iid = parts[i].split("|")[0].strip()
            body = parts[i + 1]
            m = re.search(r"^Code-word tokens:\s*(.*?)\.?\s*$", body, flags=re.M)
            counts = {}
            if m:
                for g, n in re.findall(r"\b([A-Z]) (\d+)", m.group(1)):
                    counts[g] = int(n)
                body = body[:m.start()]
            para = " ".join(l.strip() for l in body.strip().splitlines() if l.strip())
            yield iid, para, counts

    def match(self, text):
        found = []
        for iid in self.items:
            m = re.search(r"(?<![\w-])" + re.escape(iid) + r"(?![\w-])", text)
            if m:
                found.append((m.start(), iid))
        return [i for _, i in sorted(found)]

    def _text(self, iid):
        return self.decoder.entry_text(self.items[iid]["lines"]) if self.decoder else ""

    def tokens(self, iid):
        """[(index, code word as written, meaning, grade, kind)] for every counted code-word token, in order."""
        it = self.items[iid]
        if not (self.decoder and it["key"]):
            return []
        d, key, text = self.decoder, it["key"], self._text(iid)
        if "tokens" in inspect.signature(d.decode_entry).parameters if hasattr(d, "decode_entry") else False:
            toks = []
            d.decode_entry(text, key, tokens=toks)
            return [(i, strip_core(w), m, g, k) for i, w, m, g, k in toks]
        out = []  # fallback: a decoder without a tokens list (no numeral runs, no notes beyond variant/gloss)
        for i, w in enumerate(text.split(" ")):
            if w == "|" or not w:
                continue
            if "~" in w:
                surface, target, ovr = w.split("~")
                if target == "=":
                    out.append((i, strip_core(surface), "", ovr or "M", "as-written"))
                    continue
                if target.startswith("!"):
                    out.append((i, strip_core(surface), target[1:].replace("_", " "), ovr or "M", "word"))
                    continue
                stem, flag, row = d.lookup(target.strip(" .,;:'\"()"), key, True)
                if row is not None and ovr:
                    row = (row[0], ovr, row[2])
                stem = surface
            else:
                stem, flag, row = d.lookup(w.strip(" .,;:'\"()"), key, False)
            if row is None or row[2] in ("blind", "line"):
                continue
            out.append((i, strip_core(stem), row[0], row[1], row[2]))
        return out

    def split_index(self, iid, toks):
        """Word index of the clerk's 'another' that starts the second telegram (after the first signature)."""
        words = self._text(iid).split(" ")
        sig = next((i for i, _, _, _, k in toks if k == "sig"), -1)
        for i, w in enumerate(words):
            if i > sig and w.strip(" .,;:'\"()\\").lower() == "another":
                return i
        return None

    def ledger_text(self, iid):
        lines = [l for l in self.items[iid]["lines"] if l.strip() and not l.startswith(NOTE_PREFIXES)]
        return " / ".join(l.strip() for l in lines)

    def word_count(self, iid, part=0, cut=None):
        words = [w for w in self._text(iid).split(" ") if w and w != "|"]
        if part and cut is not None:
            words = [w for i, w in enumerate(self._text(iid).split(" ")) if w and w != "|" and
                     ((i >= cut) if part == 2 else (i < cut))]
        return len(words)


def cut_reading(reading, part):
    """Part 1 or 2 of a derived reading whose second telegram follows 'another' inside {tail: ...}."""
    m = re.search(r"\{tail: (.*)\}\s*$", reading)
    if not m or " another " not in " " + m.group(1) + " ":
        return reading
    tail = m.group(1)
    pos = (" " + tail).find(" another ")
    if part == 1:
        return (reading[:m.start()] + "{tail: " + tail[:pos].rstrip() + "}").strip()
    rest = tail[pos + len("another "):].strip()
    k = rest.rfind(" [signed] ")
    if k >= 0:
        rest = rest[:k] + "  {tail: [signed] " + rest[k + len(" [signed] "):] + "}"
    return rest


def cut_ledger(text, part):
    m = re.search(r"(?<![\w-])another(?![\w-])", text)
    if not m:
        return text
    return text[:m.start()].rstrip(" /") if part == 1 else text[m.start():]


# ---------------------------------------------------------------- decode-key layout

class DecodeKey:
    """tools/decode_key.py jobs: ciphertext TSV (line, pos, group), reading TSV (line, text), tokens TSV (grades)."""

    def __init__(self, folder):
        self.folder = folder
        self.items = {}
        cfg = json.loads((folder / "decode.json").read_text(encoding="utf-8"))
        for job in cfg.get("jobs", []):
            tok = folder / job.get("tokens", "")
            rdg = folder / job.get("reading", "")
            cip = folder / job.get("ciphertext", "")
            if not (job.get("tokens") and tok.exists() and rdg.exists()):
                continue
            for r in csv.DictReader(tok.read_text(encoding="utf-8").splitlines(), delimiter="\t"):
                item = r["line"].split("_")[0]
                it = self.items.setdefault(item, {"tokens": [], "reading": [], "cipher": {}, "pages": [],
                                                  "reading_file": job.get("reading", ""), "line": 0})
                it["tokens"].append((r.get("group", ""), r.get("value", ""), r.get("grade", "")))
                page = r["line"].split("_")[1] if r["line"].count("_") >= 2 else ""
                if page and page not in it["pages"]:
                    it["pages"].append(page)
            for n, l in enumerate(rdg.read_text(encoding="utf-8").splitlines(), 1):
                if l.startswith("#") or "\t" not in l:
                    continue
                lid, txt = l.split("\t", 1)
                if lid.split("_")[0] in self.items:
                    it = self.items[lid.split("_")[0]]
                    it["reading"].append(re.sub(r"\[(\d+)\]", r"[?\1]", txt.strip()))
                    it["line"] = it["line"] or n
            if cip.exists():
                for r in csv.DictReader([l for l in cip.read_text(encoding="utf-8").splitlines()
                                         if not l.startswith("#")], delimiter="\t"):
                    item = r["line"].split("_")[0]
                    if item in self.items:
                        self.items[item]["cipher"].setdefault(r["line"], []).append(r.get("group", ""))
        self.manifest = {}
        man = folder / "images" / "manifest.json"
        if man.exists():
            try:
                for m in json.loads(man.read_text(encoding="utf-8")):
                    if isinstance(m, dict) and m.get("item") and m.get("pointer"):
                        self.manifest[(m["item"], str(m.get("page", "")))] = m
            except (ValueError, TypeError):
                pass

    def match(self, text):
        flat = re.sub(r"\s+", "", text).lower()
        found = [(flat.find(i.lower()), i) for i in self.items if i.lower() in flat]
        return [i for _, i in sorted(found)]


# ---------------------------------------------------------------- field helpers

def holder_record(folder, pointer):
    if not pointer:
        return {}
    for p in sorted(folder.glob(f"sources/**/p{pointer}.json")):
        try:
            return json.loads(p.read_text(encoding="utf-8"))
        except ValueError:
            continue
    return {}


def record_title(rec):
    for k in ("title_dm", "title"):
        v = rec.get(k)
        if isinstance(v, str) and v.strip() and not v.strip().endswith("_"):
            return v.strip()
    return record_field(rec, "title")


def record_field(rec, key):
    """A CONTENTdm field ('callid', 'telnum', 'title') from the record, flat or inside its 'fields' list."""
    if isinstance(rec.get(key), str) and rec[key].strip():
        return rec[key].strip()
    f = rec.get("fields")
    if isinstance(f, str):
        m = re.search(r"'key': '" + re.escape(key) + r"'.*?'value': '([^']*)'", f)
        if m:
            return m.group(1).strip()
    elif isinstance(f, list):
        for x in f:
            if isinstance(x, dict) and x.get("key") == key:
                return str(x.get("value", "")).strip()
    return ""


def record_callid(rec):
    return record_field(rec, "callid")


def pointers_from_header(header):
    fields = [f.strip() for f in header.split("|")]
    for f in fields[1:3]:
        if re.fullmatch(r"\d+(?:\s*[-,]\s*\d+)*", f):
            return re.findall(r"\d+", f)
    m = re.search(r"pointers? (\d+)(?:\s*[-,]\s*(\d+))?", header)
    return [g for g in m.groups() if g] if m else []


def continuation(folder, header, ptrs):
    """A 'continues on page N' header matched to the next pointer's cached record titled 'Page N'."""
    m = re.search(r"continues on page (\d+)", header, flags=re.I)
    if not m or len(ptrs) != 1:
        return []
    nxt = str(int(ptrs[0]) + 1)
    return [nxt] if record_title(holder_record(folder, nxt)) == f"Page {m.group(1)}" else []


def page_from_header(header):
    m = re.search(r"\bPage (\d+(?:-\d+)?)", header) or re.search(r"\bp\.\s?(\d+(?:-\d+)?)", header)
    return ("Page " + m.group(1)) if m else ""


def call_from_text(text):
    m = re.search(r"\b(mss[A-Za-z]+ ?\d+[A-Za-z]*)", text)
    return m.group(1) if m else ""


def date_and_rest(text):
    m = DATE_RE.search(text)
    if not m:
        return "", text, ""
    after = re.sub(r"^\s*\([^)]*\)", "", text[m.end():])
    t = TIME_RE.match(after)
    when = m.group(1) + (", " + t.group(1).strip() if t else "")
    return when, text[:m.start()], after[t.end():] if t else after


def header_date(header):
    body = header.split("|")[-1]
    return date_and_rest(body)[0]


def iso_date(when):
    """'21 Apr 1864, 9.30 PM' -> '1864-04-21'; '[1727-1728] (catalogue date)' -> '1727/1728'; 'undated ...' or else ''."""
    if re.match(r"\s*undated\b", when or "", flags=re.I):
        return ""
    m = re.search(r"\b(\d{1,2})(?:-\d{1,2})? (" + MONTH + r") (\d{4})\b", when or "")
    if m:
        mon = MONTH_NUM.get(m.group(2)[:3].lower())
        if mon:
            return f"{int(m.group(3)):04d}-{mon:02d}-{int(m.group(1)):02d}"
    m = re.search(r"\b(1[5-9]\d\d)\s*[-/]\s*(1[5-9]\d\d)\b", when or "")
    return f"{m.group(1)}/{m.group(2)}" if m else ""


def header_place(header):
    body = re.sub(r"^\s*mss\w+ \d+ \([^)]*\),\s*", "", header.split("|")[-1].strip())
    _, _, after = date_and_rest(body)
    if not after or after.lstrip().startswith(","):
        return ""
    seg = after.split(",")[0].strip()
    if not seg or seg.lower().startswith(("to ", "for ", "operator")) or " to " in seg:
        return ""
    return seg


def ledger_place(lines):
    body = [l for l in lines if l.strip() and not l.startswith(NOTE_PREFIXES)][:3]
    for l in body:
        if WASH_RE.search(l):
            return "Washington"
        m = LEDGER_MONTH.search(l)
        if m:
            before = re.sub(r"\d{1,4}\s?(?:am|pm|a\.\s?m\.|p\.\s?m\.)", " ", l[:m.start()], flags=re.I)
            seg = re.split(r"\s{2,}", before.strip())[-1].strip(" ,.-") if before.strip() else ""
            if seg and len(seg.split()) <= 4 and not re.search(r"\d", seg):
                return seg
    return ""


def normal_place(p):
    for rx, rep in PLACE_NORMAL:
        if rx.match(p):
            return rep
    return p


def normal_name(s):
    for rx, rep in NAME_NORMAL:
        s = rx.sub(rep, s)
    return s


def correspondents(cands):
    """(from, to): the first 'to' and the first non-empty 'from' over the candidates, in order. side 'before' reads
    the phrase before the date (a title or document text), 'after' the phrase after it (a block header), 'tail' the
    signature of a reading ('[signed] X' -> 'signed: X', used only when nothing names a sender)."""
    frm, to = "", ""
    for text, side in cands:
        if not text or (frm and to):
            continue
        if side == "tail":
            m = re.search(r"\{tail: \[signed\] ([^{}]*?)(?:\s+another\b|\s*\{|\}|$)", text)
            if m and not frm and m.group(1).strip():
                frm = "signature as written: " + m.group(1).strip()[:80]
            continue
        t = re.sub(r"^[^:]{0,60}:\s+", "", text) if side == "before" else text
        _, before, after = date_and_rest(t)
        seg = before if side == "before" else after
        seg = re.sub(r"\s*\((?:operator|signed|Cipher|LS|FM|row|page|image|transcription|sent|first|second)[^)]*\)",
                     "", seg).strip(" ,;")
        if not seg:
            continue
        if seg.lower().startswith("to "):
            f, t2 = "", seg[3:]
        elif " to " in seg:
            f, t2 = seg.split(" to ", 1)
        else:
            continue
        to = to or t2.strip(" ,")
        frm = frm or f.strip(" ,")
    return frm, to


def doc_parenthetical(doc):
    m = re.search(r"\(([^()]*(?:\([^()]*\)[^()]*)*)\)\s*$", doc)
    return m.group(1) if m else ""


def sentences(text):
    """Split on ';' and on '. X' at parenthesis depth 0, not after a known abbreviation."""
    out, cur, depth, i = [], [], 0, 0
    while i < len(text):
        ch = text[i]
        cur.append(ch)
        if ch == "(":
            depth += 1
        elif ch == ")":
            depth = max(0, depth - 1)
        elif depth == 0 and ch == ";":
            out.append("".join(cur[:-1]).strip())
            cur = []
        elif depth == 0 and ch == "." and i + 2 < len(text) and text[i + 1] == " " and text[i + 2].isupper():
            word = re.findall(r"[A-Za-z]+$", "".join(cur[:-1]))
            if not word or word[0].lower() not in ABBR:
                out.append("".join(cur).strip())
                cur = []
        i += 1
    if "".join(cur).strip():
        out.append("".join(cur).strip())
    return [s for s in out if s]


def split_top(s):
    """Split a sentence at ', its ' / ', the ' / ', and its ' outside parentheses only."""
    out, depth, start = [], 0, 0
    for i, ch in enumerate(s):
        depth += (ch == "(") - (ch == ")" and depth > 0)
        if depth == 0 and s.startswith(", ", i) and re.match(r",\s+(?:its |the |and its )", s[i:]):
            out.append(s[start:i])
            start = i + 2
    out.append(s[start:])
    return [x.strip() for x in out if x.strip()]


def prior_print_sentence(line):
    """One plain sentence: what was searched and that the item was not found there."""
    for s in sentences(line or ""):
        m = re.search(r"no prior [^;()]*?located\s*\((.*)\)\s*\.?$", s, flags=re.I)
        if m:
            what = m.group(1)
            d = re.search(r",?\s*(searched [^,]*)$", what)
            return "Not found in " + (what[:d.start()] + " (" + d.group(1) + ")" if d else what) + "."
        m = re.search(r"(?:no prior [^;]*?|\bnot )(?:was )?(?:located|found)\s+(?:(after [^;]*? of)|in|there, in)\s+(.*)",
                      s, flags=re.I)
        if m:
            what = m.group(2).rstrip(" .")
            if m.group(1):
                how = re.sub(r"\s*\(([^()]*)\)$", r", \1", m.group(1)[6:-3].strip())  # no '(... (8 Oct 2026))'
                what = m.group(2).rstrip(" .") + " (" + how + ")"
            return "Not found in " + what + "."
        if re.search(r"\bprint neither\b|\bnot located\b|\bnot found\b", s, flags=re.I):
            return s[0].upper() + s[1:].rstrip(".") + "."
    for s in sentences(line or ""):
        if re.search(r"\bno prior\b.*\b(located|found)\b", s, flags=re.I):
            return s[0].upper() + s[1:].rstrip(".") + "."
    return clean(line)


def prior_print_ok(cell):
    """A prior-print cell names at least one source and the date of the search."""
    return bool(SEARCH_DATE_RE.search(cell or "")) and bool(re.search(r"\b(?:in|Official|Records|OR|ORN|Google|"
                                                                     r"Internet Archive|Papers|press|catalogue|"
                                                                     r"correspondence)\b", cell or ""))


def print_clauses(rec, label="", others=()):
    """Positive 'in print' clauses from the verifier's fields (an outcome, reply, sequel or clear text printed); for a
    split row only the clauses about this item (or about no item of the row); near-duplicates dropped."""
    out = []
    for k in ("line", "grade", "gap", "unresolved_spans", "depth_check", "verifier_note", "plaintext_novelty_note"):
        v = rec.get(k)
        if not isinstance(v, str):
            continue
        for s in sentences(v):
            for part in split_top(s):
                part = re.sub(r"^[^:]{0,80}?\b(?:weak(?:est)?|N\d)\b[^:]{0,60}:\s*", "", part).strip()
                part = re.sub(r"^external(?: check)?(?: \([^)]*\))?:\s*", "", part).strip()
                part = re.sub(r"\s*\([^()]*\)", lambda m: "" if JARGON_RE.search(m.group(0)) else m.group(0), part)
                if (PRINT_RE.search(part) and not NEG_RE.search(part) and CITE_RE.search(part)
                        and not JARGON_RE.search(part) and not part.lower().startswith(("on ", "read at"))):
                    if not part or len(part) >= 400 or (others and not filter_unresolved(part, label, list(others))):
                        continue
                    part = part[0].upper() + part[1:].rstrip(".") + "."
                    words = set(re.findall(r"[a-z0-9]{3,}", part.lower()))
                    dup = None
                    for j, o in enumerate(out):
                        ow = set(re.findall(r"[a-z0-9]{3,}", o.lower()))
                        if len(words & ow) >= 0.6 * max(1, min(len(words), len(ow))):
                            dup = j
                    if dup is None:
                        out.append(part)
                    elif len(part) > len(out[dup]):
                        out[dup] = part
    return " ".join(out[:3])


def weak_reason(rec, row, words, codes, holder_short):
    if row.get("weak", "").lower() not in ("yes", "y", "true", "1"):
        return "no"
    text = " ".join(str(rec.get(k, "")) for k in ("gap", "line", "unresolved_spans", "verifier_note"))
    why = []
    own = f"the {holder_short}'s" if holder_short != "holder" else "the holder's"
    if re.search(r"(clear|in clear)[^.;]{0,80}(transcription|since 2018)|public in clear|clear words are in", text, re.I):
        why.append(f"much of the message is already readable in the clear in {own} volunteer transcription; "
                   "what we add is the meaning of the code words")
    if re.search(r"\b(outcome|topic|exchange|order it answers|replies|reply|sequel|messages on the same)\b[^.;]{0,120}"
                 r"\b(printed|in print)\b|is in print", text, re.I):
        why.append("its outcome, reply or a related message is already in print (see 'partly in print?')")
    if not why:
        why.append(f"the review passes noted that the body is largely in the clear in {own} volunteer transcription, "
                   "or that its topic is in print")
    if words and codes is not None:
        why.append(f"about {round(100 * (words - codes) / words)}% of its words are written in the clear in the "
                   "ledger")
    return "yes: " + "; ".join(why)


def class_cell(rec, row):
    g = rec.get("grade") or row.get("class") or ""
    m = re.search(r"\bN([0-5])\b", g)
    if not m:
        return clean(g)
    n = "N" + m.group(1)
    audits = clean(rec.get("audit_status", ""))
    k = re.match(r"(\w+) audits?", audits)
    tail = ""
    if k and NUMBER_WORDS.get(k.group(1).lower(), 0) >= 2:
        tail = f"; {k.group(1).lower()} separate AI review passes searched for prior print"
    elif k:
        tail = "; one AI review pass searched for prior print"
    return f"{n}: {CLASS_MEANING[n]}{tail}"


def depth_words(depth):
    return {"D0": "not yet read", "D1": "fragments read", "D2": "partially deciphered", "D3": "largely deciphered",
            "D4": "deciphered"}.get(depth, "")


def count_phrase(counts, unit="code words"):
    """'16 of 18 code words read from the cipher book; 1 inferred, 1 uncertain'."""
    total = sum(counts.values())
    if not total:
        return ""
    lab = GRADE_LABEL
    read = sum(counts.get(g, 0) for g in "HCS")
    main = [f"{counts[g]} {lab[g]}" for g in "HCS" if counts.get(g)]
    if len(main) == 1:
        head = f"{read} of {total} {unit} read {main[0].split(' ', 1)[1]}"
    else:
        head = f"{read} of {total} {unit} read" + (" (" + ", ".join(main) + ")" if main else "")
    rest = [f"{counts[g]} {lab[g]}" for g in "IMU" if counts.get(g)]
    return head + ("; " + ", ".join(rest) if rest else "")


def show(meaning):
    """A key value with alternatives ('s|que') shown as 's or que'."""
    return " or ".join(x for x in str(meaning).split("|")) if "|" in str(meaning) else str(meaning)


def token_label(word, meaning, grade):
    lab = GRADE_LABEL.get(grade, grade)
    if grade == "U" or meaning in ("?",):
        return f"{word} (unread)"
    if meaning == "":
        return f"{word} (as written; {lab})"
    return f"{word} = {show(meaning)} ({lab})"


def pair_list(tokens):
    seen, order = {}, []
    for word, meaning, grade in tokens:
        k = (word.lower(), meaning, grade)
        if k not in seen:
            seen[k] = [word, meaning, grade, 0]
            order.append(k)
        seen[k][3] += 1
    out = []
    for k in order:
        word, meaning, grade, n = seen[k]
        out.append(token_label(word, meaning, grade) + (f" x{n}" if n > 1 else ""))
    return "; ".join(out)


def dejargon(text):
    """Internal names in a reviewer's note, in words a holder can read."""
    text = re.sub(r"\s*and a G3 check", "", text)
    text = re.sub(r"\bkey(?:-no\d+)?\.md\b", "the cipher book", text)
    text = re.sub(r"\breading(?:-no\d+)?\.md\b", "our reading file", text)
    text = re.sub(r"\b(?:the )?decoder H\b", "the decoder's cipher-book reading", text)
    return re.sub(r"\b(\w+) \1\b", r"\1", text)


def plain_grades(text):
    """Spell out grade letters in a reviewer's note: '(M)' -> '(uncertain)', 'graded I' -> 'graded inferred'."""
    text = dejargon(text)
    lab = GRADE_LABEL
    text = re.sub(r"\(([HCSIMU])\)", lambda m: "(" + lab[m.group(1)] + ")", text)
    text = re.sub(r",\s*([HCSIMU])\)", lambda m: ", " + lab[m.group(1)] + ")", text)
    text = re.sub(r"\bgraded ([HCSIMU])\b", lambda m: "graded " + lab[m.group(1)], text)
    text = re.sub(r"\bone ([HCSIMU]) token", lambda m: "one token graded " + lab[m.group(1)], text)
    text = re.sub(r"\bword ([HCSIMU])\b(?!\.)", lambda m: "word graded " + lab[m.group(1)], text)
    text = re.sub(r"(?<=[\w'\]]) ([HCSIMU])(?=[\s;,)]|$)", lambda m: " (" + lab[m.group(1)] + ")", text)
    return text


def split_semis(text):
    """Split on ';' outside parentheses."""
    out, depth, cur = [], 0, []
    for ch in text or "":
        depth += (ch == "(") - (ch == ")" and depth > 0)
        if ch == ";" and depth == 0:
            out.append("".join(cur))
            cur = []
        else:
            cur.append(ch)
    out.append("".join(cur))
    return [x.strip() for x in out if x.strip()]


def filter_unresolved(text, label, others):
    if not text or text.strip().lower() in ("none", "-"):
        return ""
    if not others:
        return text

    def hit(lab, clause):
        pat = r"\s*".join(re.escape(ch) for ch in lab.replace(" ", ""))
        return re.search(r"(?<![\w-])" + pat + r"(?![\w-]|\d)", clause, flags=re.I) is not None
    keep = [c for c in split_semis(text) if hit(label, c) or not any(hit(o, c) for o in others)]
    return "; ".join(keep)


def extra_unresolved(text, token_words):
    """The list's or status.json's 'unresolved' text, minus what other columns carry: 'none ...' restatements, clauses
    naming only tokens already listed, archive copies not read (prior-print column) and print notes (partly in print)."""
    keep = []
    for c in split_semis(text):
        if not c or re.match(r"none\b", c, flags=re.I) or c == "-":
            continue
        if re.search(r"archival copies|public in clear|clear text is printed|\bprinted\b|\bin print\b", c, flags=re.I):
            continue
        ws = [w.lower() for w in re.findall(r"[A-Za-z][A-Za-z'-]*", c)]
        named = [w for w in ws if w not in U_STOP]
        if named and all(w.strip("'") in token_words for w in named):
            continue
        keep.append(c)
    return keep


# ---------------------------------------------------------------- plain-text reading

def _plural(base):
    low = base.lower()
    if low in SAME_PLURAL or low.endswith("s"):
        return base
    if low in PLURAL_NOUNS or low.split()[-1] in PLURAL_NOUNS:
        if re.search(r"[^aeiou]y$", low):
            return base[:-1] + "ies"
        return base + "s"
    return base + "'s"


def _with_end(base, end):
    if not end:
        return base
    if end in ("s", "'s"):
        return _plural(base)
    if end in ("ed", "d"):
        return base + ("d" if base.endswith("e") else "ed")
    if end in ("er", "ers"):
        if base.endswith("s") and not base.endswith("ss"):  # '[Troops]ers' = troopers
            base = base[:-1]
        return base + ("r" if base.endswith("e") else "er") + ("s" if end == "ers" else "")
    if end in ("ing",):
        return (base[:-1] if base.endswith("e") and not base.endswith("ee") else base) + "ing"
    if end == "es":
        return base + "es"
    return base + end


def plain_meaning(m, end=""):
    """A key meaning as plain words: the book's grammar notes dropped, '[sic: X]' -> X, 'Command = Er' -> Commander."""
    m = re.sub(r"\s*\((?:-[^()]*|ing[^()]*)\)", "", m)
    m = re.sub(r"\s*\[#\]", "", m)
    m = re.sub(r"\s*\((?:numeral|time word)\)", "", m)
    m = re.sub(r"^\(Fort\) ", "Fort ", m)
    m = re.sub(r"^(.*?) \[sic: ([^\]]+)\]$", r"\2", m)
    m = re.sub(r"\s*\[sic\]$", "", m)
    m = re.sub(r";.*$", "", m)
    m = m.replace("[?]", "(?)")
    if re.search(r" = Er$", m):
        m = re.sub(r" = Er$", "er", m)
        if end in ("er", "ers"):
            end = "s" if end == "ers" else ""
    return _with_end(m.strip(), end)


PUNCT_PLAIN = {".": ".", ",": ",", ";": ";", ":": ":", "?": "?", "!": "!", '"': '"', "-": "-",
               "(paragraph)": "(new paragraph)", "( )": "( )"}


def plain_reading(r):
    """The marked-up reading in plain words (the marked-up column stays the record)."""
    def tail(m):
        body = m.group(1).replace("[signed]", "Signed:")
        return " / " + body
    r = re.sub(r"\s*\{tail: (.*)\}\s*$", tail, r)
    r = re.sub(r"\{time: ([^{}]*)\}", r"(time \1)", r)
    r = re.sub(r"\{date: ([^{}]*)\}", r"(date \1)", r)
    r = re.sub(r"\[signed\]", "Signed:", r)
    r = re.sub(r"(?<=\s)\[\?\](?=\s|$)", "?", " " + r)[1:]          # a lone [?] is the question-mark code word
    r = re.sub(r"\[\?(\d+)\]", r"<\1>", r)                          # Blathwayt unread groups, kept visible

    def br(m):
        inner, end, q = m.group(1), m.group(2) or "", m.group(3) or ""
        if inner in PUNCT_PLAIN:
            return PUNCT_PLAIN[inner] + q
        if re.fullmatch(r"\d+", inner):
            return inner + end + q.replace("[?]", "(?)")
        return plain_meaning(inner, end.replace("'s", "s") if end == "'s" else end) + q.replace("[?]", "(?)")
    r = re.sub(r"\[((?:[^\[\]]|\[[^\[\]]*\])*)\]('s|ers|er|ing|ed|es|s|d|th)?(\[\?\])?", br, r)
    r = re.sub(r"<(\d+)>", r"[?\1]", r)
    r = r.replace("[?]", "(?)")
    r = re.sub(r"\s+([.,;:?!])", r"\1", r)
    r = re.sub(r"([.,;:?!])\1+", r"\1", r)
    return re.sub(r"\s+", " ", r).strip()


# ---------------------------------------------------------------- audited counts

def audited_counts(text):
    """Grade counts and total from a 'completeness' cell, where it gives figures; {} when it does not."""
    t = text or ""
    out = {}
    m = re.search(r"\(H (\d+)((?:, [A-Z] \d+)*)\)", t)               # '17 H/C of 21 (H 15, C 2, M 2, I 1)'
    if m:
        out["H"] = int(m.group(1))
        for g, n in re.findall(r"([A-Z]) (\d+)", m.group(2)):
            out[g] = int(n)
    else:
        m = re.match(r"\s*(?:about )?(\d+)\s*/\s*(\d+) code[- ]word(?: groups?|s)? H\b", t)
        if m:
            out["H"] = int(m.group(1))
            out["_total"] = int(m.group(2))
        else:
            head = re.split(r"\bof\b", t, maxsplit=1)
            for n, g in re.findall(r"(\d+)\s+([HCSIMU])\b", head[0]):
                out[g] = out.get(g, 0) + int(n)
    if not out:
        return {}
    if "_total" not in out:
        mt = re.search(r"\bof (\d+) code[- ]word", t)  # 'of 22 code words', not '15 H by hand of 16 decoder H'
        if mt:
            out["_total"] = int(mt.group(1))
    out["_approx"] = bool(re.match(r"\s*about\b", t))
    return out


def count_difference(mine, audited):
    """'' when the token counts agree with the audited figures (every grade the audit names, and the total)."""
    if not audited or audited.get("_approx"):
        return ""
    diffs = []
    for g in GRADE_ORDER:
        if g in audited and audited[g] != mine.get(g, 0):
            diffs.append(f"{g} {mine.get(g, 0)} vs audited {audited[g]}")
    tot = sum(mine.values())
    if "_total" in audited and audited["_total"] != tot:
        diffs.append(f"total {tot} vs audited {audited['_total']}")
    return "; ".join(diffs)


# ---------------------------------------------------------------- selection drift

def selection_drift(status, listed_docs, classes, min_audits, scopes, folders):
    def passes(r):
        why = []
        m = re.search(r"\bN([0-5])\b", r.get("grade", ""))
        if classes and (not m or "N" + m.group(1) not in classes):
            why.append("class " + (("N" + m.group(1)) if m else "none"))
        k = re.match(r"(\w+) audits?", r.get("audit_status", "") or "")
        if min_audits and (not k or NUMBER_WORDS.get(k.group(1).lower(), 0) < min_audits):
            why.append("audits '" + (r.get("audit_status") or "") + "'")
        if scopes and r.get("claim_scope") not in scopes:
            why.append("scope " + str(r.get("claim_scope")))
        if r.get("superseded_by"):
            why.append("superseded")
        return why
    res = [r for r in status.get("results", []) if not folders or any(f in (r.get("link") or "") for f in folders)]
    by_doc = {r.get("document_id"): r for r in res}
    gone = []
    for d in listed_docs:
        r = by_doc.get(d)
        why = passes(r) if r else ["no status.json result"]
        if why:
            gone.append((d, ", ".join(why)))
    new = [r.get("document_id") for r in res if not passes(r) and r.get("document_id") not in listed_docs]
    return gone, new


# ---------------------------------------------------------------- links

def github_slugs(md_text):
    """GitHub heading anchors for every heading of a markdown file, duplicates numbered as GitHub numbers them."""
    seen, out = {}, {}
    fence = False
    for l in md_text.splitlines():
        if l.startswith("```"):
            fence = not fence
            continue
        m = re.match(r"^(#{1,6})\s+(.*?)\s*#*\s*$", l)
        if fence or not m:
            continue
        text = re.sub(r"[`*_]", "", m.group(2))
        base = re.sub(r"[^\w\- ]", "", text.lower()).replace(" ", "-")
        n = seen.get(base, 0)
        seen[base] = n + 1
        slug = base if n == 0 else f"{base}-{n}"
        out.setdefault(m.group(2).strip(), slug)
    return out


_SLUGS = {}


def audit_link(folder, rel, rec, pin):
    audit = folder / "AUDIT.md"
    if not audit.exists():
        return ""
    if audit not in _SLUGS:
        _SLUGS[audit] = github_slugs(audit.read_text(encoding="utf-8"))
    slugs = _SLUGS[audit]
    for ref in rec.get("audit_refs") or []:
        m = re.search(r"'#+\s*(.*?)'", str(ref))
        if m and m.group(1).strip() in slugs:
            return f"{REPO_URL}/blob/{pin}/{rel}/AUDIT.md#{slugs[m.group(1).strip()]}"
    return f"{REPO_URL}/blob/{pin}/{rel}/AUDIT.md"


# ---------------------------------------------------------------- build

def book_cell(row, holder_short, book_objects, alias, url_template):
    """'Cipher No. 1 (mssEC 41)' -> ('Cipher No. 1, Huntington mssEC 41', its Digital Library URL)."""
    k = row.get("key", "")
    m = re.match(r"^(.*?)\s*\((mss[A-Za-z]+ ?\d+[A-Za-z]*)\)\s*$", k)
    if not m:
        return k, ""
    call = m.group(2)
    url = ""
    ptr = book_objects.get(call)
    al = next((v for p, v in alias.items() if call.startswith(p)), "")
    if ptr and al and url_template:
        url = url_template.format(alias=al, pointer=ptr)
    who = f"{holder_short} " if holder_short != "holder" else ""
    return f"{m.group(1)}, {who}{call}", url


def build_rows(list_rows, status, repo_root, meta, args):
    by_doc = {r.get("document_id"): r for r in status.get("results", [])}
    layouts, out, checks = {}, [], []
    alias = dict(a.split("=", 1) for a in (args.alias or []))
    for row in list_rows:
        rec = by_doc.get(row["document"], {})
        if not rec:
            warn("no status.json result for: " + row["document"])
        folder = folder_path(row["folder"], repo_root)
        if folder not in layouts:
            lay = None
            try:
                if (folder / "decode.json").exists():
                    lay = DecodeKey(folder)
                elif list(folder.glob("reading*.md")):
                    lay = MdBlocks(folder)
            except Exception as e:  # a folder that cannot be read is warned, the row still written
                warn(f"cannot read {folder}: {e}")
            layouts[folder] = lay
        lay = layouts[folder]
        docs = rec.get("documents") or [row["document"]]
        items = []
        if lay:
            for d in docs:
                for i in lay.match(d):
                    if i not in items:
                        items.append(i)
        try:
            ndocs = int(row.get("documents") or len(docs))
        except ValueError:
            ndocs = len(docs)
        if not items:
            warn("no item found in the folder for: " + row["document"])
            items = [None]
        split = len(items) > 1
        if split and ndocs != len(items):
            warn(f"{row['document']}: documents {ndocs} but {len(items)} items found")
        for iid in items:
            doc_for_item = next((d for d in docs if iid and lay and iid in lay.match(d)), row["document"])
            c, check = item_cells(row, rec, lay, iid, doc_for_item, split, ndocs, items, alias, args, meta)
            if check:
                checks.append(check)
            m = meta.get(iid or "", {})
            for mk, ck in META_KEYS.items():
                if m.get(mk):
                    c[ck] = "" if m[mk] == "-" else m[mk]
            if m.get("note"):
                c["reading"] = "Note: " + m["note"] + " -- " + c["reading"]
            if not c["url"] and args.url_template and c["number"] and c["alias"]:
                c["url"] = args.url_template.format(alias=c["alias"], pointer=c["number"])
            if not c["iso"]:
                c["iso"] = iso_date(c["date"])
            if c["prior"] and not prior_print_ok(c["prior"]):
                warn(f"{iid}: the prior-print cell names no source and date of search: {c['prior'][:80]}")
            out.append([clean(c[k]) for k in KEYS])
    ids = [r[KEYS.index("row_id")] for r in out]
    for d in sorted({i for i in ids if ids.count(i) > 1}):
        warn(f"row id {d} is not unique")
    return out, checks


def item_cells(row, rec, lay, iid, doc, split, ndocs, items, alias, args, meta):
    c = {k: "" for k in KEYS}
    m_item = meta.get(iid or "", {})
    title = rec.get("title", "")
    others = [i for i in items if i and i != iid]
    folder = lay.folder if lay else folder_path(row["folder"], args.repo_root)
    rel = folder_rel(folder, args.repo_root)
    pin = args.pin or "main"
    c["row_id"] = iid or ""
    c["credit"] = args.credit
    c["class"] = class_cell(rec, row)
    c["prior"] = dejargon(prior_print_sentence(rec.get("line", ""))) if rec else ""
    c["inprint"] = print_clauses(rec, (iid or "").replace("BLA", "BLA "), [o.replace("BLA", "BLA ") for o in others]) \
        if rec else ""
    c["book"], c["book_url"] = book_cell(row, args.holder_short, dict(b.split("=", 1) for b in args.book_object or []),
                                         alias, args.url_template)
    c["alink"] = audit_link(folder, rel, rec, pin) if rec else ""
    c["summary"] = clean(rec.get("depth_sentence", "")) if (rec and not split) else ""
    unres_src = m_item.get("unresolved") or ("; ".join(x for x in (row.get("unresolved", ""),) if x))
    if m_item.get("unresolved") == "-":
        unres_src = ""
    unresolved = filter_unresolved(plain_grades(unres_src), (iid or "").replace("BLA", "BLA "),
                                   [o.replace("BLA", "BLA ") for o in others])
    depth = depth_words(row.get("depth (", ""))
    m_part = re.search(r"\((first|second) telegram\)", doc + " " + row["document"])
    part = {"first": 1, "second": 2}[m_part.group(1)] if m_part else 0
    check = None
    if isinstance(lay, MdBlocks) and iid:
        it = lay.items[iid]
        ptrs = pointers_from_header(it["header"])
        ptrs = ptrs + continuation(folder, it["header"], ptrs)
        recd = holder_record(folder, ptrs[0] if ptrs else "")
        c["call"] = record_callid(recd) or call_from_text(doc) or call_from_text(it["header"])
        page = record_title(recd) or page_from_header(it["header"])
        if len(ptrs) > 1:
            more = [record_title(holder_record(folder, p)) or p for p in ptrs[1:]]
            page += "; continues on " + ", ".join(f"{t} (CONTENTdm {p})" for t, p in zip(more, ptrs[1:]))
        c["page"] = page
        c["number"] = ptrs[0] if ptrs else ""
        c["level"] = "page (of a compound object)"
        c["telnum"] = record_field(recd, "telnum")
        c["alias"] = recd.get("collectionAlias") or next((v for k, v in alias.items() if c["call"].startswith(k)), "")
        c["date"] = header_date(it["header"]) or date_and_rest(title)[0]
        cands = ([(doc_parenthetical(doc), "before")] if split else [(title, "before")]) + [
            (s, "before") for s in summary_cells(folder, iid)] + [(it["header"].split("|")[-1], "after"),
                                                                  (it["reading"], "tail")]
        frm, to = correspondents(cands)
        c["from"], c["to"] = normal_name(frm), normal_name(to)
        place = header_place(it["header"]) or ledger_place(it["lines"])
        if place and place != "Washington" and place.lower() in c["to"].lower():
            place = ""  # the receiving operator's slot of the ledger header, not the place of sending
        c["place"] = normal_place(place)
        if re.search(r"\btranscription only\b", it["header"]):
            c["source"] = f"the {args.holder_short}'s volunteer transcription only (page image not checked)"
        else:
            c["source"] = (f"page image (the {args.holder_short}'s volunteer transcription used as a second "
                           "witness)")
        toks = lay.tokens(iid)
        ledger = lay.ledger_text(iid)
        reading = it["reading"]
        cut = lay.split_index(iid, toks) if part else None
        if part and cut is not None:
            toks = [t for t in toks if (t[0] >= cut if part == 2 else t[0] < cut)]
            ledger = cut_ledger(ledger, part)
            reading = cut_reading(reading, part)
        elif part:
            warn(f"{iid}: no 'another' after the signature, so the row keeps the whole entry")
        c["ledger"] = ledger
        if not split and ndocs > 1:
            reading = f"({ndocs} telegrams in this entry) " + reading
        c["reading"] = reading
        c["plain"] = plain_reading(reading)
        c["codes"] = pair_list([(w, m, g) for _, w, m, g, _ in toks])
        mine = {}
        for t in toks:
            mine[t[3]] = mine.get(t[3], 0) + 1
        whole = {}
        for t in lay.tokens(iid):
            whole[t[3]] = whole.get(t[3], 0) + 1
        if it["counts"] and whole != it["counts"]:
            warn(f"{iid}: token pass {whole} differs from the reading's count line {it['counts']}")
        diff = count_difference(mine, audited_counts(row.get("completeness", "")))
        if diff:
            check = (iid, diff, row.get("completeness", ""))
        unc = [token_label(w, m, g) for _, w, m, g, _ in toks if g in ("M", "I", "U")]
        tw = {w.lower() for _, w, _, _, _ in toks} | {re.sub(r"\W", "", m).lower() for _, _, m, _, _ in toks}
        extra = extra_unresolved(unresolved, tw) if not m_item.get("unresolved") else \
            ([] if unresolved == "" else [unresolved])
        c["uncertain"] = "; ".join(dict.fromkeys(unc + extra)) or "none"
        c["read"] = count_phrase(mine) + (f". Overall: {depth}" if depth else "")
        c["adds"] = weak_reason(rec, row, lay.word_count(iid, part, cut), sum(mine.values()), args.holder_short)
        c["rlink"] = (f"{REPO_URL}/blob/{pin}/{rel}/{it['reading_file']}?plain=1#L{it['line']}" if it["line"] else
                      f"{REPO_URL}/blob/{pin}/{rel}/{it['reading_file']}")
    elif isinstance(lay, DecodeKey) and iid:
        it = lay.items[iid]
        c["call"] = call_from_text(doc)
        pages = [(p, lay.manifest.get((iid, p), {}).get("pointer", "")) for p in it["pages"]]
        c["page"] = "pages read: " + ", ".join(f"{p} (CONTENTdm {ptr})" if ptr else p for p, ptr in pages)
        c["level"] = "compound object (letter)"
        c["alias"] = next((v for k, v in alias.items() if c["call"].startswith(k)), "")
        c["date"] = date_and_rest(doc)[0]
        c["source"] = "page image"
        c["ledger"] = " / ".join(" ".join(g) for _, g in sorted(it["cipher"].items()))
        c["reading"] = " / ".join(it["reading"])
        c["plain"] = plain_reading(c["reading"])
        c["codes"] = pair_list([(g, v, gr) for g, v, gr in it["tokens"]])
        unc = [token_label(g, v, gr) for g, v, gr in it["tokens"] if gr in ("M", "I", "U")]
        tw = {g.lower() for g, _, _ in it["tokens"]}
        extra = extra_unresolved(unresolved, tw) if not m_item.get("unresolved") else [unresolved]
        c["uncertain"] = "; ".join(dict.fromkeys(unc + [x for x in extra if x])) or "none"
        counts = {}
        for _, _, gr in it["tokens"]:
            counts[gr] = counts.get(gr, 0) + 1
        phrase = count_phrase(counts, "cipher groups")
        if split:
            whole = (f". Depth was set for the {len(items)} items together, not for each: together they are "
                     f"{depth}" if depth else "")
            if counts and sum(counts.get(g, 0) for g in "HCS") * 2 < sum(counts.values()):
                whole = ". No depth is set for this item on its own (the depth set for the items together does not " \
                        "apply to it)"
        else:
            whole = f". Overall: {depth}" if depth else ""
        c["read"] = phrase + whole
        c["adds"] = weak_reason(rec, row, 0, None, args.holder_short)
        c["rlink"] = (f"{REPO_URL}/blob/{pin}/{rel}/{it['reading_file']}?plain=1#L{it['line']}" if it["line"] else
                      f"{REPO_URL}/tree/{pin}/{rel}")
    else:
        c["call"] = call_from_text(row["document"])
        c["reading"] = row.get("title", "")
        c["read"] = "; ".join(x for x in (row.get("completeness", ""), f"Overall: {depth}" if depth else "") if x)
        c["adds"] = weak_reason(rec, row, 0, None, args.holder_short)
        c["rlink"] = f"{REPO_URL}/tree/{pin}/{rel}"
    if not c["from"] and not c["to"] and not isinstance(lay, MdBlocks):
        frm, to = correspondents([(doc_parenthetical(doc), "before"), (title, "before")])
        c["from"], c["to"] = normal_name(frm), normal_name(to)
    return c, check


_SUMMARY_CACHE = {}


def summary_cells(folder, iid):
    """Second column of a '| ID | sender, addressee, date | ...' summary table row in the folder's reading*.md."""
    if folder not in _SUMMARY_CACHE:
        d = {}
        for p in sorted(folder.glob("reading*.md")):
            for l in p.read_text(encoding="utf-8").splitlines():
                m = re.match(r"^\|\s*([A-Za-z0-9-]+)\s*\|\s*([^|]*)\|", l)
                if m:
                    d.setdefault(m.group(1), []).append(m.group(2).strip())
        _SUMMARY_CACHE[folder] = d
    return _SUMMARY_CACHE[folder].get(iid, [])


# ---------------------------------------------------------------- README

ABBREVIATIONS = ("OR = The War of the Rebellion: A Compilation of the Official Records of the Union and Confederate "
                 "Armies (1880-1901); 'OR ser. I vol. 33', 'OR I/33' = series I, volume 33; 'pt' = part; 'p.', 'pp.' "
                 "= page(s); ORN = Official Records of the Union and Confederate Navies in the War of the Rebellion; "
                 "Butler Corr. or Butler's printed correspondence = Private and Official Correspondence of Gen. "
                 "Benjamin F. Butler (1917); Grant Papers = The Papers of Ulysses S. Grant; Plum = W. R. Plum, The "
                 "Military Telegraph during the Civil War (1882); IA = Internet Archive; HMC = Historical Manuscripts "
                 "Commission; TNA = The National Archives (UK); LoC = Library of Congress; NARA = U.S. National "
                 "Archives; Chronicling America = the Library of Congress's digitized newspapers; open scholarship "
                 "indexes = OpenAlex, Semantic Scholar, CORE and CrossRef; Zooniverse Talk = the discussion boards of "
                 "the volunteer transcription project; QMG = Quartermaster General; AAG = Assistant Adjutant General.")


def readme_rows(args, rows):
    h = args.holder or "the holder"
    short = args.holder_short
    own = f"the {short}'s" if short != "holder" else "the holder's"
    k = {key: i for i, key in enumerate(KEYS)}
    md = [r for r in rows if r[k["level"]].startswith("page")]
    other = [r for r in rows if not r[k["level"]].startswith("page")]
    two = [r for r in md if r[k["reading"]].startswith("(2 telegrams")]
    tel = len(md) + len(two)
    nums = [(r[k["alias"]], r[k["number"]]) for r in rows]
    dup = sorted({n for a, n in nums if nums.count((a, n)) > 1}, key=lambda x: int(x) if x.isdigit() else 0)
    books = sorted({r[k["book"]] for r in rows if r[k["book"]] and "rebuilt" not in r[k["book"]]})
    rebuilt = sorted({r[k["book"]] for r in rows if "rebuilt" in r[k["book"]]})
    counts = f"{len(rows)} rows: {len(md)} for {tel} telegrams in the ledgers"
    if two:
        counts += (f" ({len(two)} rows hold two telegrams each and say so in the reading)" if len(two) > 1 else
                   " (1 row holds two telegrams and says so in the reading)")
    if other:
        counts += f", and {len(other)} for cipher passages in letters (" + ", ".join(
            r[k["call"]] for r in other) + ")"
    pinned = (f"; the links in each row are pinned to the repository version this file was made from ({args.pin})"
              if args.pin else "")
    who = (f"Cipher Lab is one person, who directs the project and sends every message, working with AI agents "
           f"(Claude models) in an open repository ({REPO_URL}), every step logged there. The transcriptions, "
           "readings, code-word grades and searches in this file were made by the agents; each item was then "
           "checked by separate AI review passes (sessions other than the one that made the reading), which searched "
           "for prior print. No human specialist has checked these readings yet.")
    what = ((args.about.rstrip(".") + ". ") if args.about else "") + counts + "." + (
        f" Prepared {args.prepared}" if args.prepared else "") + (
        "; the repository holds the current version and readings may be revised" + pinned + ".")
    vol = f" ('{args.volunteer_project}')" if args.volunteer_project else ""
    ours = (f"The page images, the catalogue records and the volunteer transcription{vol} are {h}'s, used here under its "
            "Digital Library terms. We claim nothing in the column 'ledger/page text as we transcribed it': it is "
            f"made from those page images, with the volunteer transcription as a second witness, and it is {h}'s to "
            "use under its own terms. ")
    if books:
        ours += (f"The meanings of the code words come from {h}'s own cipher books (" + "; ".join(books) + "); our key "
                 "files only index them, page by page. ")
    ours += ("What is ours: the readings, the code-word grades and the search notes" + (
        ", and the " + "; ".join(rebuilt) if rebuilt else "") + ". These are public under the MIT licence (the "
        "LICENSE file in the repository), which asks that its short copyright notice travel with substantial copies; "
        f"a credit line in the record is welcome. Suggested: '{args.credit}'.")
    imp = ("The .tsv file is tab-delimited UTF-8 text, for loading; the .csv holds the same rows (UTF-8 with a "
           "byte-order mark, so that Excel opens it correctly); this README is also in the -README.txt file beside "
           "them. One header row; no tab or line break inside any cell. Each row is keyed by 'CONTENTdm collection "
           "alias' together with 'CONTENTdm number' (CONTENTdm numbers are unique only within a collection). 'record "
           "level' says whether the number is a page of a compound object (the ledger rows) or the compound object "
           "itself (the letters), since CONTENTdm edits these differently. 'row id' is unique. ")
    if dup:
        imp += (f"Some pages hold two telegrams: those pages have two rows with the same CONTENTdm number (" +
                ", ".join(dup) + "); combine them before loading into one record. ")
    imp += ("Where an entry runs onto a second page, the row is keyed to the first page and the page cell names the "
            "continuation. Map only the columns you want (for example the readings, the code words and the credit "
            "line) to your own fields; the others are there for checking.")
    grades = (f"{GRADE_LABEL['H']} = the meaning is written in the period cipher book named in 'cipher book or key "
              "used'; from a printed or period decipherment = only a printed edition, or a decipherment made at the "
              "time, gives it; cryptanalytic = worked out from the cipher itself, with a control test; inferred = not "
              "read directly from the book: worked out from context, from another message, or a repair of a clerk's "
              "slip; uncertain = a reading we are not sure of; unread = a code word or group we could not read; "
              "'as written' = the word is kept as the clerk wrote it (a plain word, or a group whose meaning is not "
              "settled) and counted with the grade given.")
    classes = ("; ".join(f"{a} = {b}" for a, b in CLASS_MEANING.items()) + ". Each class was set by a separate AI "
               "review pass after a logged search, and a second pass then tried again to find the text in print.")
    read = ("The cell first counts the code words (or cipher groups) and how each was read, then gives the depth in "
            "words: deciphered = every code word read and checked against an outside source; largely deciphered = "
            "at least 80% of the code words read, with an outside check of the content (a printed reply or "
            "related print, or a control test); partially deciphered = at least one passage reads and one true "
            "sentence about the content can be written, but the checks for 'largely' are not all met, so a "
            "telegram whose every code word is read is still 'partially deciphered' when no outside check of its "
            "content was found; fragments read = scattered words only.")
    adds = ("yes = the AI review passes noted that our reading adds less than usual: much of the message is already "
            f"readable in the clear in {own} volunteer transcription (the clerks wrote many words in plain English), "
            "or its outcome, reply or a related message is already in print. The share of words written in the "
            "clear is counted from our transcription.")
    conv = ("In 'reading (marked up)': [..] = a code word replaced by its meaning as the book gives it, with the "
            "book's own notes kept: '(-ed, -ing)' = the word also stands for its -ed and -ing forms; '[#]' = the book "
            "marks the word in its margin; '[sic: X]' = the book's spelling, X the word meant; 'Command = Er' = the "
            "book's entry for 'commander'; [n] = a number written in numeral code words; [.] [,] [\"] and the like = "
            "punctuation code words, and a [?] standing alone = the code word for a question mark; [?] after a word "
            "= a doubtful reading of the handwriting (or of the book); 's after a bracket = the code word carries an "
            "s (a plural or a possessive); {time: ..} and {date: ..} = time and date code words; {tail: ..} = "
            "everything from the signature code word on ([signed] = the signature code word; a second telegram in "
            "the same ledger entry follows the clerk's word 'another'). In the letters' rows the reading is given "
            "syllable by syllable as the cipher groups stand, and [?73] = cipher group 73, unread. 'reading (plain "
            "text)' renders the same text in plain words (endings joined, punctuation as punctuation); where the two "
            "differ, the marked-up reading is the record. In the transcription: lines are separated by ' / '; "
            "<del>..</del> = struck through; <ins>..</ins> = written above the line; word[?] = doubtful; ' = ' joins "
            "a word the clerk split; for number ciphers, the cipher groups line by line.")
    dates = ("'date and time as written' comes from the ledger header or the letter ('12 M' = noon; a date in "
             "brackets is the catalogue's); 'date (YYYY-MM-DD)' gives the day, or a range of years as 1727/1728. "
             "Places are normalized (Ft Monroe = Fort Monroe; Hd Qrs A. of J. = Headquarters, Army of the James); "
             "the ledger's own spelling stays in the transcription. Senders and addressees are as the review passes "
             "name them.")
    out = [("Who made this", who), ("What this file is", what), ("What is ours and what is theirs", ours),
           ("How to import", imp), ("Grades of a code word", grades),
           ("Classes (prior-publication check)", classes), ("How much is read", read), ("Adds less? (and why)", adds),
           ("Conventions in the readings and the transcription", conv), ("Dates, places and names", dates),
           ("Abbreviations", ABBREVIATIONS)]
    help_ = column_help(short)
    covered = {"how much is read", "adds less? (and why)"}
    for col in columns(short):
        if col not in covered:
            out.append((col, help_[col]))
    return out


def column_help(short):
    cols = columns(short)
    text = {
        "alias": "The Digital Library collection the record belongs to (CONTENTdm alias).",
        "number": "The record's CONTENTdm number in that collection; with the alias, the key to import by.",
        "level": "'page (of a compound object)' for a ledger page, 'compound object (letter)' for a whole letter.",
        "row_id": "Our id for the telegram or letter (unique; the same id is used in the repository).",
        "call": "The call number of the volume or item.",
        "page": "The page title in the Digital Library record (and the continuation page, if any); for a letter, the "
                "pages read, with each page's own CONTENTdm number.",
        "telnum": "The page record's own 'Telegram Number' field, as the Digital Library gives it, for the whole "
                  "page; filled only where our cached copy of the record carries the field (a blank does not mean "
                  "the record lacks it).",
        "url": "The record's page in the Digital Library.",
        "date": "See 'Dates, places and names'.",
        "iso": "See 'Dates, places and names'.",
        "from": "The sender, as the review passes name them (an operator or forwarding office may be named with "
                "'via').",
        "to": "The addressee, as the review passes name them.",
        "place": "The place of sending the ledger heads the entry with (normalized); blank where the page gives none.",
        "source": "What our transcription was made from: the page image, or the volunteer transcription alone.",
        "ledger": "Our transcription of the ledger entry or the cipher passage; see 'Conventions'.",
        "reading": "The decoded text with its markup; see 'Conventions'.",
        "plain": "The same reading in plain words; see 'Conventions'.",
        "summary": "One true sentence about the content, written by a review pass from the reading.",
        "codes": "Each code word or cipher group as written = its meaning (grade); 'xN' = it occurs N times. "
                 "Punctuation, time and signature code words are included. The 'Code words' sheet of the .xlsx gives "
                 "one code word per line.",
        "book": "The period cipher book (with its call number) whose meanings the code words were read from, or the "
                "key we rebuilt.",
        "book_url": "The cipher book's record in the Digital Library.",
        "uncertain": "Code words graded uncertain, inferred or unread, and other doubtful words, with the review "
                     "passes' notes.",
        "read": "See 'How much is read'.",
        "adds": "See 'Adds less? (and why)'.",
        "prior": "Where the review passes searched for the text in print, and when; 'not found in' is a search "
                 "result, not a claim of priority.",
        "inprint": "Related text that is in print (an outcome, a reply, a sequel, or the clear part of the letter), "
                   "as the review passes name it; blank if they name none.",
        "class": "See 'Classes'.",
        "rlink": "The reading in the repository, at this entry.",
        "alink": "The search log (AUDIT.md) in the repository, at the review section for this entry.",
        "credit": "A credit line, if you wish to use one.",
    }
    return {col: text[key] for col, key in zip(cols, KEYS)}


# ---------------------------------------------------------------- output

def write_text(rows, stem, readme, short):
    """STEM.csv (BOM, quoted where needed), STEM.tsv (plain tab-joined) and STEM-README.txt."""
    head = columns(short)
    with open(f"{stem}.csv", "w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(head)
        w.writerows(rows)
    with open(f"{stem}.tsv", "w", encoding="utf-8", newline="") as f:
        for r in [head] + rows:
            f.write("\t".join(clean(c) for c in r) + "\n")
    with open(f"{stem}-README.txt", "w", encoding="utf-8", newline="") as f:
        for topic, text in readme:
            f.write(topic + "\n")
            f.write(wrap(text, 100, "    ") + "\n\n")


def wrap(text, width, indent):
    out, line = [], indent
    for w in text.split():
        if len(line) + len(w) + 1 > width and line.strip():
            out.append(line.rstrip())
            line = indent
        line += w + " "
    if line.strip():
        out.append(line.rstrip())
    return "\n".join(out)


def code_word_rows(rows):
    """Long form of the 'code words and meanings' column: one line per code word."""
    k = {key: i for i, key in enumerate(KEYS)}
    out = []
    for r in rows:
        for part in [p.strip() for p in r[k["codes"]].split("; ") if p.strip()]:
            m = re.match(r"^(.*?)(?: x(\d+))?$", part)
            body, n = m.group(1), int(m.group(2) or 1)
            gm = re.match(r"^(.*?) \(([^()]*)\)$", body)
            word_mean, grade = (gm.group(1), gm.group(2)) if gm else (body, "")
            word, _, meaning = word_mean.partition(" = ")
            out.append([r[k["alias"]], r[k["number"]], r[k["row_id"]], word, meaning, grade, n])
    return out


def write_xlsx(rows, stem, readme, args):
    """Return True when the .xlsx was written, False when openpyxl is not importable."""
    try:
        import openpyxl
        from openpyxl.styles import Alignment, Font
        from openpyxl.utils import get_column_letter
    except ImportError:
        return False
    head = columns(args.holder_short)
    wb = openpyxl.Workbook()
    rd = wb.active
    rd.title = "Read me first"
    rd.append(["Topic", "Explanation"])
    for t, v in readme:
        rd.append([t, v])
    rd.column_dimensions["A"].width = 34
    rd.column_dimensions["B"].width = 120
    wrap_ = Alignment(wrap_text=True, vertical="top")
    for row in rd.iter_rows():
        for cell in row:
            cell.alignment = wrap_
    for cell in rd[1]:
        cell.font = Font(bold=True)
    rd.freeze_panes = "A2"

    ws = wb.create_sheet("Readings")
    ws.append(head)
    num = KEYS.index("number")
    for r in rows:
        ws.append([int(v) if (i == num and v.isdigit()) else v for i, v in enumerate(r)])
    widths = {"alias": 14, "number": 11, "level": 16, "row_id": 9, "call": 12, "page": 22, "telnum": 14, "url": 30,
              "date": 18, "iso": 12, "from": 24, "to": 24, "place": 16, "source": 24, "ledger": 60, "reading": 70,
              "plain": 70, "summary": 50, "codes": 90, "book": 24, "book_url": 30, "uncertain": 40, "read": 40,
              "adds": 40, "prior": 50, "inprint": 40, "class": 40, "rlink": 30, "alink": 30, "credit": 30}
    for i, key in enumerate(KEYS):
        ws.column_dimensions[get_column_letter(i + 1)].width = widths.get(key, 20)
    for row in ws.iter_rows():
        for cell in row:
            cell.alignment = wrap_
    for cell in ws[1]:
        cell.font = Font(bold=True)
    ws.freeze_panes = "E2"  # alias, number, record level and row id stay in view
    ws.auto_filter.ref = ws.dimensions
    link_font = Font(underline="single", color="0072B2")  # Okabe-Ito blue; the underline carries the cue
    for r in range(2, ws.max_row + 1):
        for key in ("url", "book_url", "rlink", "alink"):
            cell = ws.cell(row=r, column=KEYS.index(key) + 1)
            if str(cell.value or "").startswith("http"):
                cell.hyperlink = str(cell.value)
                cell.font = link_font

    cw = wb.create_sheet("Code words")
    cw.append(["CONTENTdm collection alias", "CONTENTdm number", "row id (our entry)", "code word or group as written",
               "meaning", "grade", "times"])
    for r in code_word_rows(rows):
        cw.append([int(v) if (i == 1 and str(v).isdigit()) else v for i, v in enumerate(r)])
    for i, wdt in enumerate((14, 11, 9, 24, 40, 30, 7)):
        cw.column_dimensions[get_column_letter(i + 1)].width = wdt
    for cell in cw[1]:
        cell.font = Font(bold=True)
    cw.freeze_panes = "A2"
    cw.auto_filter.ref = cw.dimensions
    wb.active = 0
    wb.properties.title = f"Cipher Lab readings for {args.holder or 'the holder'}"
    wb.properties.creator = "Cipher Lab"
    wb.properties.lastModifiedBy = "Cipher Lab"
    fixed = datetime.datetime(2026, 1, 1)
    wb.properties.created = wb.properties.modified = fixed
    wb.save(f"{stem}.xlsx")
    return True


def build(args):
    list_rows = read_list(args.list)
    status = json.loads(Path(args.status).read_text(encoding="utf-8"))
    meta = read_meta(args.meta)
    gone = []
    if args.select_class or args.select_min_audits or args.select_scope or args.select_folder:
        sp = (lambda s: [x.strip() for x in s.split(",") if x.strip()])
        gone, new = selection_drift(status, [r["document"] for r in list_rows], sp(args.select_class),
                                    args.select_min_audits, sp(args.select_scope), sp(args.select_folder))
        print(f"selection drift: {len(gone)} listed row(s) no longer pass, {len(new)} passing result(s) not listed")
        for d, why in gone:
            print(f"  listed, now fails ({why}): {d}")
        for d in new:
            print(f"  passes, not listed (adding it to an outward list needs Outreach gates 2 and 7): {d}")
    rows, checks = build_rows(list_rows, status, args.repo_root, meta, args)
    accepted = {a for x in (args.accept_count or []) for a in x.split(",") if a}
    open_checks = [c for c in checks if c[0] not in accepted]
    print(f"count check: {len(checks)} row(s) differ from the audited completeness, "
          f"{len(checks) - len(open_checks)} accepted")
    for iid, diff, comp in checks:
        print(f"  {iid}: {diff} ('{comp}')" + (" [accepted]" if iid in accepted else ""))
    return rows, gone, open_checks


def write_all(rows, out, args):
    Path(out).parent.mkdir(parents=True, exist_ok=True)
    readme = readme_rows(args, rows)
    write_text(rows, out, readme, args.holder_short)
    made = False
    if not args.no_xlsx:
        made = write_xlsx(rows, out, readme, args)
        if not made:
            warn("openpyxl not importable: wrote .csv, .tsv and -README.txt only (pip install openpyxl for the .xlsx)")
    return made


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0], formatter_class=argparse.RawDescriptionHelpFormatter,
                                 epilog=__doc__.split("\n\n", 1)[1])
    ap.add_argument("list", help="list TSV (one row per entry; see the docstring for the columns)")
    ap.add_argument("--out", required=True, help="output path without extension (writes .csv, .tsv, -README.txt and "
                    ".xlsx)")
    ap.add_argument("--status", default=str(ROOT / "status.json"),
                    help="status.json with the verifier's results (default: the repository's status.json)")
    ap.add_argument("--repo-root", default=str(ROOT),
                    help="directory the list's folder links resolve against (default: this repository)")
    ap.add_argument("--meta", help="per-item overrides TSV: item plus any of " + ", ".join(list(META_KEYS) +
                    list(META_EXTRA)) + " ('-' blanks a cell)")
    ap.add_argument("--url-template", default="", help="e.g. https://host/digital/collection/{alias}/id/{pointer}")
    ap.add_argument("--alias", action="append", help="CALLPREFIX=collection alias, e.g. mssEC=p16003coll11 "
                    "(repeatable)")
    ap.add_argument("--holder", default="", help="the holder's name for the README sheet, e.g. 'the Huntington Library'")
    ap.add_argument("--holder-short", default="holder", help="short name used in headers and cells, e.g. Huntington "
                    "(default: holder)")
    ap.add_argument("--volunteer-project", default="", help="name of the holder's volunteer transcription project")
    ap.add_argument("--book-object", action="append", help="'CALL=POINTER' of a cipher book's Digital Library record, "
                    "e.g. 'mssEC 41=351' (repeatable)")
    ap.add_argument("--book-label", default="", help="the H grade in words (default: 'from the cipher book'; e.g. "
                    "'from the Huntington cipher book')")
    ap.add_argument("--about", default="", help="the selection rule in one sentence, for the README's first rows")
    ap.add_argument("--prepared", default="", help="the date the file is prepared, e.g. '9 Oct 2026' (no clock is "
                    "read, so --check is repeatable)")
    ap.add_argument("--pin", default="", help="commit the repository links are pinned to (default: main)")
    ap.add_argument("--credit", default="", help="suggested credit line (default: 'Decipherment: Cipher Lab, <year of "
                    "--prepared or this year>, " + REPO_URL + "')")
    ap.add_argument("--no-xlsx", action="store_true", help="write the text files only")
    ap.add_argument("--check", action="store_true", help="regenerate to a temporary directory and exit 1 if the "
                    "committed files differ, a listed row fails the selection, or a count difference is not accepted")
    ap.add_argument("--accept-count", action="append", help="row id(s) whose count difference from the audited "
                    "completeness is already reported (comma list, repeatable)")
    ap.add_argument("--select-class", default="", help="comma list of classes a listed result must have, e.g. N3,N4")
    ap.add_argument("--select-min-audits", type=int, default=0, help="minimum number of audits (default 0: not "
                    "checked)")
    ap.add_argument("--select-scope", default="", help="comma list of claim scopes, e.g. completed-reading,"
                    "recovered-passages")
    ap.add_argument("--select-folder", default="", help="comma list of folder names a result's link must contain")
    args = ap.parse_args(argv)
    if not args.credit:
        year = re.search(r"\b(\d{4})\b", args.prepared)
        args.credit = (f"Decipherment: Cipher Lab, {year.group(1) if year else datetime.datetime.now(datetime.timezone.utc).year}"
                       f", {REPO_URL}")
    GRADE_LABEL["H"] = args.book_label or "from the cipher book"

    rows, gone, open_checks = build(args)
    if args.check:
        tmp = Path(tempfile.mkdtemp())
        try:
            stem = tmp / Path(args.out).name
            write_all(rows, stem, args)
            stale = []
            for ext in (".csv", ".tsv", "-README.txt"):
                a, b = Path(f"{args.out}{ext}"), Path(f"{stem}{ext}")
                if not a.exists() or not filecmp.cmp(a, b, shallow=False):
                    stale.append(a.name)
        finally:
            shutil.rmtree(tmp)
        bad = bool(stale or gone or open_checks)
        for s in stale:
            print(f"stale: {s} differs from what the list, status.json and the folders give now")
        if gone:
            print("stale list: a listed row no longer passes the selection (fix the list, then regenerate)")
        if open_checks:
            print("count difference not accepted: report it to a verifier, then name it with --accept-count")
        print("check: " + ("FAIL" if bad else "ok") + f" ({len(rows)} rows)")
        return 1 if bad else 0
    made = write_all(rows, args.out, args)
    print(f"wrote {len(rows)} rows to {args.out}.csv, .tsv, -README.txt" + (", .xlsx" if made else ""))
    return 0


if __name__ == "__main__":
    sys.exit(main())

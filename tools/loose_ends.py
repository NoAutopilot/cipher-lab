#!/usr/bin/env python3
"""Loose ends: material a target folder's own prose says was never fetched, read or decoded, and that no step
register carries (LOOSE-ENDS, 8 Oct 2026; CLAUDE.md Usage 8a, rules become tools).

    python3 tools/loose_ends.py                         # whole repository -> LOOSE-ENDS.tsv
    python3 tools/loose_ends.py --untracked-only        # keep only hits no register carries
    python3 tools/loose_ends.py --folder na-oldenbarnevelt-2442-1605 --out -
    python3 tools/loose_ends.py --root DIR --today 2026-10-08   # tests: another tree, a fixed clock

Why it exists. na-oldenbarnevelt-2442-1605 NOTES.md section 1 recorded on 25 Sept 2026 that leaves 4, 5 and 7
"carry heavy cipher that reads as a different correspondence" and that scans 9-11 were never fetched. The sentence sat
in a body section, not in "## Remaining gaps" / "## Escalation", so tools/gaps_check.py passed, tools/next_steps.py
never listed it, and the 3 Oct reading of blocks B/C1 never triggered a look at the rest of the volume; the owner had
to spot it (8 Oct 2026). Two system gaps: observations in prose never reach the step registers, and a success never
propagates to its siblings. This tool covers the first; tools/gaps_check.py's "## Siblings" check covers the second.

What it scans, per ciphers/<folder>/:
  (a) phrases in NOTES.md, AUDIT.md and HYPOTHESES.md, matched per paragraph (a sentence wrapped over two lines and
      markdown emphasis such as "a **different** correspondence" still match), one hit per paragraph listing every
      kind found in it. Kinds: unfetched (not fetched, never fetched, scans N-M not fetched), unread (never
      read/opened/decoded/transcribed, left unread, not yet read/decoded), other-correspondence (a different or
      another correspondence/letter), more-cipher (further/other/more cipher leaves/letters/pages), carries-cipher
      (carries heavy cipher, also in cipher), unread-sibling, out-of-scope ("out of scope for this"), unread-block
      (unread blocks), next-in-body (a "next:" outside the step sections). Lines inside "## Remaining gaps",
      "## Escalation", "## While waiting" and "## Siblings" sections, and inside fenced code, are not scanned:
      those sections ARE the registers.
  (b) structure: image files at the top of images/ (or named in images/manifest.json) whose file name, stem or
      long id part no transcription, ciphertext, script, crop list or other non-prose file in the folder mentions
      (kind image-untranscribed: on disk, never transcribed), one row per folder with the count and names. Crops,
      overlays, thumbnails and contact sheets are skipped. Tracked when a register names at least half of them.

tracked = yes when the same material is named in a register: the folder's "## Escalation" / "## Remaining gaps" /
"## While waiting" / "## Siblings" sections, its NEXT-STEPS.tsv row, an open WORK-QUEUE.tsv row naming the folder
(and that row's brief file), or a ROOM.md line naming the folder in the last 7 days. "Same material" is decided by
a register line citing the hit's own location (file:line, as tools/loose_ends.py's triage lines do), or the hit's
material keys (leaf/scan/folio numbers and ranges, file names, rare words of the sentence): every number key
(up to two) must appear in a register sentence that also names one of the hit's words, or, with no number keys, two
word keys must. It is a heuristic for a model to triage, never a verdict; the 'material' column shows what was
matched.

Output: LOOSE-ENDS.tsv (folder, status, file:line, snippet, kind, tracked, material), sorted by folder and line, then
one summary line on stderr. Exit 0 always (it is a finder, not a gate); 2 on a usage error.

What it is meant to CATCH (offline tests in tools/tests/test_loose_ends.py): the 2442 section-1 sentence (wrapped,
with **emphasis**) when no register names leaves 4/5/7; an image on disk that no transcription file names.
What it must NOT flag as untracked: the same sentence when the folder's Escalation already carries "leaves 4, 5 and
7"; any line inside an Escalation/Remaining gaps section itself; an image a transcription file names.
Offline; reads files only.
"""
import argparse
import datetime
import glob
import json
import os
import re
import sys

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
from next_steps import first_status_word  # noqa: E402

PROSE_FILES = ("NOTES.md", "AUDIT.md", "HYPOTHESES.md")
REGISTER_HEAD_RE = re.compile(r'^#{1,4}\s*(Remaining gaps|Escalation|While waiting|Siblings)\b', re.I)
HEAD_RE = re.compile(r'^#{1,6}\s')

PHRASES = [
    ("unfetched", r"\b(?:not|never)\s+(?:yet\s+)?(?:been\s+)?fetched\b|\bunfetched\b|"
                  r"\bscans?\s+\d+\s*[-–]\s*\d+\s+(?:were\s+|are\s+)?not\s+fetched"),
    ("unread", r"\bnever\s+(?:been\s+)?(?:read|opened|decoded|transcribed|deciphered)\b|\bleft\s+unread\b|"
               r"\bnot\s+yet\s+(?:been\s+)?(?:read|opened|decoded|transcribed|deciphered|fetched)\b|"
               r"\b(?:was|were|is|are)\s+not\s+(?:read|decoded|transcribed|deciphered)\b"),
    ("other-correspondence", r"\b(?:a\s+)?(?:different|another|second|separate)\s+(?:correspondence|letter|dispatch)\b"),
    ("more-cipher", r"\b(?:further|other|more|additional)\s+(?:cipher(?:ed)?|coded|encrypted)\s+"
                    r"(?:leaves|leaf|letters?|pages?|folios?|documents?|passages?|blocks?|lines)\b"),
    ("carries-cipher", r"\bcarr(?:y|ies|ying)\s+(?:heavy\s+|more\s+|some\s+)?cipher\b|\balso\s+in\s+cipher\b"),
    ("unread-sibling", r"\bunread\s+siblings?\b|\bsiblings?\b[^.]{0,40}\bunread\b"),
    ("out-of-scope", r"\bout\s+of\s+scope\s+for\s+this\b"),
    ("unread-block", r"\bunread\s+blocks?\b|\bblocks?\s+[A-Z0-9, and]{1,20}\s+(?:are\s+|were\s+|remain\s+)?unread\b"),
    ("next-in-body", r"(?:^|[\s;(])next:\s"),
]
PHRASES = [(k, re.compile(p, re.I)) for k, p in PHRASES]

IMG_EXT = (".jpg", ".jpeg", ".png", ".tif", ".tiff", ".webp", ".gif", ".jp2")
SKIP_IMG_RE = re.compile(r'crop|overlay|debug|thumb|contact|sheet|strip|_line|preview|montage|mosaic', re.I)
REF_EXT = (".txt", ".tsv", ".csv", ".json", ".py", ".sh", ".js", ".yaml", ".yml", ".md")
REF_SKIP = {"NOTES.md", "AUDIT.md", "HYPOTHESES.md", "REQUEST.md", "manifest.json"}

MONTHS = r"(?:Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Sept|Oct|Nov|Dec)[a-z]*"
STOP = set("""about above after again against because before being below between could doesn during
further having itself might other should their there these those through under until where which while
whose would cipher letter letters leaves leaf scans scan pages page folio folios reads carry carries heavy
different correspondence never fetched opened decoded transcribed unread block blocks material another
second including already section notes still never images image found nothing worker brief status""".split())


def today_from(arg):
    if arg:
        return datetime.date.fromisoformat(arg)
    return datetime.datetime.now(datetime.timezone.utc).date()


def clean(text):
    return re.sub(r'[*_`]+', '', text)


def material_keys(sentence, anchor=None):
    """(number keys, word keys) naming the material a sentence talks about; numbers nearest `anchor` first."""
    s = clean(sentence)
    blank = lambda m: " " * len(m.group(0))                       # keep offsets so distances stay true
    s = re.sub(r'\b\d{1,2}\s+' + MONTHS + r'\b', blank, s)       # "25 Sept" is a date, not a leaf
    s = re.sub(r'\b(1[4-9]|20)\d\d\b', blank, s)                  # years
    s = re.sub(r'\$\s?\d+(?:\.\d+)?', blank, s)                   # dollar figures
    anchor = len(s) if anchor is None else anchor
    found = []                                                    # (position, key)
    for m in re.finditer(r'\b(\d{1,4})\s*[-\u2013]\s*(\d{1,4})\b', s):
        a, b = int(m.group(1)), int(m.group(2))
        if 0 < b - a <= 30:
            found.extend((m.start(), str(i)) for i in range(a, b + 1))
    found.extend((m.start(), m.group(0)) for m in re.finditer(r'\b\d{1,4}[rv]?\b', s))
    for m in re.finditer(r'\b(?:blocks?|letters?|parts?)\s+([A-Z]\d?(?:\s*(?:,|and|/|&)\s*[A-Z]\d?)*)\b', s):
        found.extend((m.start(1) + x.start(), x.group(0)) for x in re.finditer(r'[A-Z]\d?', m.group(1)))
    found.sort(key=lambda t: abs(t[0] - anchor))
    nums = [k for _, k in found]
    files = re.findall(r'[\w.-]+\.(?:jpe?g|png|tiff?|webp)', s, re.I)
    words = [w.lower() for w in re.findall(r'[A-Za-z][A-Za-z\'-]{4,}', s)]
    words = [w for w in words if w not in STOP and (len(w) >= 7 or w[0].isupper())]
    caps = [w.lower() for w in re.findall(r'\b[A-Z][a-z]{3,}\b', s) if w.lower() not in STOP]
    seen, out_n = set(), []
    for n in nums:
        n = (n.lstrip('0') or '0').lower()
        if n not in seen:
            seen.add(n)
            out_n.append(n)
    wk = []
    for w in files + caps + words:
        if w.lower() not in wk:
            wk.append(w.lower())
    return out_n, wk


def sentences(text):
    return [x for x in re.split(r'(?<=[.;!?])\s+(?=[A-Z(])|\n\s*[-*]\s+', clean(text)) if x.strip()]


def is_tracked(nums, words, register_text):
    """The heuristic in the module docstring: a register sentence carries the hit's numbers with one of its words."""
    if not register_text:
        return False
    low = clean(register_text).lower()
    if nums:
        need = nums[:2]
        for sent in sentences(low):
            toks = set(re.findall(r'\b0*([0-9a-z]?\d{0,4}[rv]?)\b', sent)) - {""}
            if all(n in toks for n in need) and (not words or any(w in sent for w in words) or
                                                  re.search(r'\b(leaf|leaves|scan|scans|folio|ff?\.|page|block|letter)', sent)):
                return True
        return False
    hits = [w for w in words if re.search(r'\b' + re.escape(w) + r'\b', low)]
    return len(hits) >= min(2, len(words)) and len(words) > 0


def paragraphs_with_lines(text):
    """Yield (start_line, paragraph_text, in_register) for blank-line-separated paragraphs, skipping fenced code."""
    lines = text.splitlines()
    in_reg = False
    in_fence = False
    buf, start = [], None
    for i, line in enumerate(lines, 1):
        if line.strip().startswith("```"):
            in_fence = not in_fence
            if buf:
                yield start, "\n".join(buf), in_reg
                buf, start = [], None
            continue
        if in_fence:
            continue
        if HEAD_RE.match(line):
            if buf:
                yield start, "\n".join(buf), in_reg
                buf, start = [], None
            in_reg = bool(REGISTER_HEAD_RE.match(line))
            continue
        if not line.strip():
            if buf:
                yield start, "\n".join(buf), in_reg
                buf, start = [], None
            continue
        if start is None:
            start = i
        buf.append(line)
    if buf:
        yield start, "\n".join(buf), in_reg


def register_sections(text):
    out = []
    for _, para, in_reg in paragraphs_with_lines(text):
        if in_reg:
            out.append(para)
    return "\n\n".join(out)


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as fh:
            return fh.read()
    except OSError:
        return ""


def external_registers(root, today):
    """{folder: text} from NEXT-STEPS.tsv, open WORK-QUEUE.tsv rows (+ their briefs) and ROOM.md's last 7 days."""
    reg = {}

    def add(folder, text):
        reg[folder] = reg.get(folder, "") + "\n\n" + text

    ns = read(os.path.join(root, "NEXT-STEPS.tsv")).splitlines()
    for row in ns[1:]:
        cells = row.split("\t")
        if cells and cells[0]:
            add(cells[0], " ".join(cells[1:]))
    folders = set(os.path.basename(p) for p in glob.glob(os.path.join(root, "ciphers", "*")) if os.path.isdir(p))
    wq = read(os.path.join(root, "WORK-QUEUE.tsv")).splitlines()
    head = wq[0].split("\t") if wq else []
    si = head.index("status") if "status" in head else 6
    bi = head.index("brief") if "brief" in head else 2
    for row in wq[1:]:
        cells = row.split("\t")
        if len(cells) <= si or cells[si].startswith(("done", "cancel", "dropped", "superseded")):
            continue
        brief = read(os.path.join(root, cells[bi])) if len(cells) > bi and cells[bi] else ""
        blob = row + "\n" + brief
        for f in folders:
            if f in blob:
                add(f, blob)
    cutoff = today - datetime.timedelta(days=7)
    for line in read(os.path.join(root, "ROOM.md")).splitlines():
        m = re.match(r'(\d{4}-\d{2}-\d{2})', line)
        if not m:
            continue
        try:
            d = datetime.date.fromisoformat(m.group(1))
        except ValueError:
            continue
        if d < cutoff:
            continue
        for f in folders:
            if f in line:
                add(f, line)
    return reg


def phrase_hits(folder_dir, fname, text):
    out = []
    for start, para, in_reg in paragraphs_with_lines(text):
        if in_reg:
            continue
        flat = clean(para.replace("\n", " "))
        kinds, first = [], None
        for kind, rx in PHRASES:
            m = rx.search(flat)
            if m:
                kinds.append(kind)
                if first is None or m.start() < first.start():
                    first = m
        if not kinds:
            continue
        # line of the first match inside the paragraph
        offs = clean(para).count("\n", 0, min(first.start(), len(clean(para))))
        line = start + offs
        # the sentence holding the match names the material
        # the material is what sits nearest the match: a window cut at sentence ends, numbers nearest first
        lo = max(flat.rfind(". ", 0, first.start()), flat.rfind("; ", 0, first.start()), first.start() - 100)
        hi = flat.find(". ", first.end())
        hi = min(hi if hi >= 0 else len(flat), first.end() + 60)
        sent = flat[max(lo, 0): hi]
        anchor = first.start() - max(lo, 0)
        snippet = flat[max(0, first.start() - 110): first.end() + 110].replace("\t", " ").strip()
        out.append({"file": fname, "line": line, "snippet": snippet, "kind": ",".join(kinds), "sentence": sent,
                    "anchor": anchor})
    return out


def image_hits(folder_dir):
    imgdir = os.path.join(folder_dir, "images")
    if not os.path.isdir(imgdir):
        return []
    names = set()
    for p in os.listdir(imgdir):
        if p.lower().endswith(IMG_EXT) and os.path.isfile(os.path.join(imgdir, p)):
            names.add(p)
    man = os.path.join(imgdir, "manifest.json")
    if os.path.isfile(man):
        def walk(o):
            if isinstance(o, dict):
                for k, v in o.items():
                    if isinstance(k, str) and k.lower().endswith(IMG_EXT) and "/" not in k:
                        names.add(k)
                    walk(v)
            elif isinstance(o, list):
                for v in o:
                    walk(v)
            elif isinstance(o, str) and o.lower().endswith(IMG_EXT) and not o.startswith("http"):
                b = os.path.basename(o)
                if os.path.dirname(o) in ("", "images", "."):
                    names.add(b)
        try:
            walk(json.loads(read(man)))
        except ValueError:
            pass
    names = sorted(n for n in names if not SKIP_IMG_RE.search(n))
    if not names:
        return []
    ref = []
    for dp, dn, fn in os.walk(folder_dir):
        dn[:] = [d for d in dn if d != ".git"]
        for f in fn:
            if f in REF_SKIP or not f.lower().endswith(REF_EXT):
                continue
            p = os.path.join(dp, f)
            if os.path.getsize(p) > 5_000_000:
                continue
            ref.append(read(p))
        # crop folders named after their source count as a reference
        if os.path.abspath(dp) == os.path.abspath(imgdir):
            ref.extend(dn)
    blob = "\n".join(ref)
    unnamed = []
    for n in names:
        stem = os.path.splitext(n)[0]
        parts = [x for x in re.split(r'[_.\-]', stem) if len(x) >= 8]
        if n in blob or stem in blob or any(x in blob for x in parts):
            continue
        unnamed.append(n)
    if not unnamed:
        return []
    # one row per folder: a page series fetched whole would otherwise drown every phrase hit
    shown = ", ".join(unnamed[:6]) + (", ..." if len(unnamed) > 6 else "")
    return [{"file": "images/", "line": 0, "kind": "image-untranscribed", "names": unnamed,
             "snippet": "%d of %d images on disk named by no transcription/ciphertext/script file: %s" % (
                 len(unnamed), len(names), shown), "sentence": ""}]


def scan(root, today, only=None):
    reg_ext = external_registers(root, today)
    rows = []
    for d in sorted(glob.glob(os.path.join(root, "ciphers", "*"))):
        folder = os.path.basename(d)
        if not os.path.isdir(d) or folder.startswith("_") or (only and folder not in only):
            continue
        notes = read(os.path.join(d, "NOTES.md"))
        status = first_status_word(notes) or "?"
        register = reg_ext.get(folder, "")
        for f in PROSE_FILES:
            register += "\n\n" + register_sections(read(os.path.join(d, f)))
        hits = []
        for f in PROSE_FILES:
            t = read(os.path.join(d, f))
            if t:
                hits.extend(phrase_hits(d, f, t))
        hits.extend(image_hits(d))
        for h in hits:
            if h["kind"] == "image-untranscribed":
                # tracked when a register names at least half the unnamed images (by file, stem or leading number)
                low = clean(register).lower()
                named = 0
                for n in h["names"]:
                    stem = os.path.splitext(n)[0]
                    m = re.match(r'0*(\d+)_', stem)
                    if n.lower() in low or stem.lower() in low or (m and is_tracked([m.group(1)], [], register)):
                        named += 1
                tracked = named * 2 >= len(h["names"])
                mat = " ".join(h["names"][:12])
            else:
                nums, words = material_keys(h["sentence"], h.get("anchor"))
                # a register line that cites this hit's own location ("noted in the body at NOTES.md:29") carries it
                cites = re.search(r'\b%s:%d\b' % (re.escape(h["file"]), h["line"]), register)
                tracked = bool(cites) or is_tracked(nums, words[:8], register)
                mat = " ".join(nums[:6]) + (" | " if nums else "") + " ".join(words[:6])
            rows.append([folder, status, "%s:%s" % (h["file"], h["line"]), h["snippet"][:300], h["kind"],
                         "yes" if tracked else "no", mat.strip()])
    return rows


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0],
                                 formatter_class=argparse.RawDescriptionHelpFormatter, epilog=__doc__)
    ap.add_argument("--root", default=os.path.dirname(HERE))
    ap.add_argument("--out", default=None, help="output TSV (default ROOT/LOOSE-ENDS.tsv; '-' for stdout)")
    ap.add_argument("--folder", action="append", help="limit to this folder (repeatable)")
    ap.add_argument("--untracked-only", action="store_true")
    ap.add_argument("--today", default=None, help="YYYY-MM-DD for the 7-day ROOM window (default: UTC clock)")
    a = ap.parse_args(argv)
    if not os.path.isdir(os.path.join(a.root, "ciphers")):
        print("no ciphers/ under %s" % a.root, file=sys.stderr)
        return 2
    rows = scan(a.root, today_from(a.today), set(a.folder) if a.folder else None)
    if a.untracked_only:
        rows = [r for r in rows if r[5] == "no"]
    text = "folder\tstatus\tfile:line\tsnippet\tkind\ttracked\tmaterial\n" + "".join("\t".join(r) + "\n" for r in rows)
    out = a.out or os.path.join(a.root, "LOOSE-ENDS.tsv")
    if out == "-":
        sys.stdout.write(text)
    else:
        with open(out, "w", encoding="utf-8") as fh:
            fh.write(text)
    unt = sum(1 for r in rows if r[5] == "no")
    print("loose_ends: %d hits in %d folders, %d untracked (%d image-untranscribed)" % (
        len(rows), len(set(r[0] for r in rows)), unt,
        sum(1 for r in rows if r[5] == "no" and r[4] == "image-untranscribed")), file=sys.stderr)
    return 0


if __name__ == "__main__":
    sys.exit(main())

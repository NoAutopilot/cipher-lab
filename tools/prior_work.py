#!/usr/bin/env python3
"""prior_work.py: has this item, or this step, already been read or done -- by us, its clerk, its holder, a portal, a
solver repository or a printed edition? The per-item prior-work gate, v1 (PRIOR-WORK v1, 8 Oct 2026).

  prior_work.py <slug> --item ID [--step-type read] [--known-answer item:<id>|gate:<name>] [--network] [--fetch]
  prior_work.py <slug> --item-spec 'shelfmark=BnF fr.3040;folio=18r;date=1530-03-28;sender=Gramont;recipient=Montmorency'
  prior_work.py <slug> --item ID --reading reading.txt --network      G3: after decode, before any class or SO row
  prior_work.py <slug> --brief .claude/briefs/runs/<brief>.md         every item the brief names
  prior_work.py -      --register NEXT-STEPS.tsv --columns next_step,parallel   (also SIBLINGS-*.tsv, LOOSE-ENDS-*.md)
  prior_work.py <slug> --record ROWID 'CLEAR: f.18r, f.17v, f.19r read at native size, no gloss'
  prior_work.py <slug> --derive        propose ciphers/<slug>/items.pending.tsv (catalogue-only; never writes items.tsv)

Why: research/PRIOR-WORK-LEAK-2026-10-08.md found 310 records of work spent on items already read (143 plaintext in
print, 72 a period gloss or clear copy on the leaf or a sibling, 49 our own earlier work, 19 the holder's transcription,
14 a modern decipherment; about USD 1,600), two thirds catchable by a script before reading (owner, 8 Oct 2026: "must be
applicable to other work not just Eckert"). This is that script cut to v1; .claude/briefs/prior-work-step.md is the hand
checklist for what it does not reach.

Items: ciphers/<slug>/items.tsv (item_id, shelfmark, folio, canvas, decode, ptr, wvo, date YYYY-MM-DD, calendar os|ns,
sender, recipient, office, place, language, kind, holder_url, clear_words, verified) or --item-spec with those keys. A unit
is volume + folio + canvas, never the folio alone (tools/shelfmark.py). Target state is read at origin/main with git
(--fetch first runs `git fetch origin main`, the only network call outside --network); a ref that does not resolve makes
own work UNCHECKED. Caches (sources/, djvu texts) and the gate's own prior-work.tsv are read from disk. Paths under any
restricted/ folder (ciphers/debosnys-1883/restricted) and the private repository are never read.

Checks (scope step = the job itself; scope plaintext = the item's text):
 1 own work, always (step): DONE only from typed evidence for the same unit and step -- a [x] / [done / [already run /
   [retired] marker heading a NOTES/ITERATE/HYPOTHESES bullet that names the unit and the step's verb and does not say
   part is still open; a WORK-QUEUE.tsv done row naming slug and unit; for crop, a crop file for the leaf; for --step-type
   audit, an AUDIT.md/status.json class for this item; for read/decode on Eckert ledgers, a known_blocks() entry; for
   --brief, a WORK-QUEUE done row whose brief column is this very brief (a re-queued brief exits 3 at once). A marker
   for another step, an unnamed volume in a multi-volume folder, or prose naming the unit with a completion word is LEAD
   done-candidate (file:line); a ROOM claim under 6 h with no later done line from the same tag, naming slug and unit, is
   LEAD live-claim (--me TAG skips yours). An AUDIT/status class of already-known text, or PROGRESS.tsv txt=k, is KNOWN;
   an audited reading of ours or PROGRESS R=x is LEAD done-candidate. propagate-revision, upgrade-audit and
   new-family-audit are never DONE.
 2 leaf and neighbours (read/transcribe/decode/crop): look.tsv lists the cipher page, facing page, two before and four
   after (images/manifest.json, else folio/canvas/pointer arithmetic) and every image of a unit of <= 8. LOOK until
   --record answers it or a NOTES/AUDIT line already records the gloss check for this leaf: a gloss for THIS letter is
   KNOWN, checked-and-none is CLEAR, a gloss on another letter CONTEXT, an unattributed gloss on a neighbouring leaf
   KEY-SOURCE (nearby sheet); catalogue notes are check 3's.
 3 holder, portal and solver caches (tools/data/prior_portals.tsv): Tomokiyo (volume + exact folio with 'deciphered' /
   'attached' / 'dechiffre' = KNOWN; folio within 2 = LEAD fuzzy-match; 'can be read with' = KEY-SOURCE; 'undeciphered'
   = no evidence); DECODE listings ('Partially decrypted' = KNOWN-PART; 'Decrypted' = LEAD, it may be a key only;
   'Non-decrypted' = CONTEXT, a status is evidence of nothing; a cached record page with a cleartext document = LEAD);
   solver caches and --clone dirs (a reading file naming the unit, not citing cipher-lab and not later than ours = KNOWN;
   any other mention CONTEXT duplicate-effort-risk); holder notes quoted in NOTES/sources naming the unit with
   decipherment wording = LEAD. Sentences are classed with a negation lexicon ('no separate dechiffrement', 'sans le
   dechiffrement', 'Non-decrypted') and a partial lexicon ('gedeeltelijk', 'en partie').
 4 editions (tools/data/prior_editions.tsv, matched by slug glob, year span and correspondents): cached djvu text is
   searched for the date +-1 day (Old and New Style both ways in 1582-1752 unless `calendar` says) with name tokens of
   both correspondents in one window = LEAD edition-hit, with the hit count at +-30 days beside it (KNOWN only by --record
   after someone opens the page; a calendar printing only the clear part is recorded KNOWN-PART). Each row's positive
   control runs in the same pass: a missed or missing control is UNCHECKED, never CLEAR; a volume not on disk, a row with
   no IA route or no matching row at all (core-only) is UNCHECKED-NET. --network downloads the djvu through
   print_check.Net into --cache (outside the repository) and adds one OpenAlex identity query with a host control.
 5 civil-war adapter (eckert-* slugs with a pointer): reuses ciphers/eckert-1864/entries_mssEC19.py (load_vocab,
   segment, toks, day_month, known_blocks; orcheck with --or-dir). The holder's own transcription of the pointer: no code
   word in the entry = KNOWN (step 0 skip); code words = KNOWN-PART with the code words as residue (the E78 shape, never
   KNOWN); it also answers the leaf LOOK. Same-page entries already read or with an OR hit are LEAD.
 6 G3 (--reading FILE): distinctive decoded phrases through the cached editions (print_check.search_text) and, with
   --network, print_check's ia-global and Google Books routes: a hit within +-3 days sharing >= 2 rare entities is
   SUBSTANCE (decoding proceeds; N3+ wording, SO rows and 'not located' sentences wait for the verifier's diff); other
   hits LEAD; the offline network family is UNCHECKED-NET, which blocks at G3.

Output: rows appended to ciphers/<slug>/prior-work.tsv (append-only: utc, origin_main_commit, item_id, scope, check,
route, query, control, hits, evidence <= 200 chars with file:line or URL, verdict, requests_by_host, valid_until, row_id),
look.tsv, one line per row and one verdict per scope on stdout (--json for machines, --dry-run writes nothing).
Verdicts: DONE KNOWN KNOWN-PART LOOK LEAD UNCHECKED UNCHECKED-NET SUBSTANCE KEY-SOURCE CONTEXT CLEAR; a check that did not
run is UNCHECKED, never CLEAR. --record ROWID 'VERDICT: what was seen' (DONE, KNOWN, KNOWN-PART, CLEAR, CONTEXT,
KEY-SOURCE or SUBSTANCE) answers an owed row; the newest answer replaces that row on every later run. Network rows carry
a 14-day valid_until and offline runs reuse them. Rule 10: the tool never assigns a novelty class, and N-class tokens and
novelty words in quoted evidence are masked as [*].
Exit (item, spec and brief modes): 3 the step is DONE; 2 the step works the text, the plaintext is KNOWN and no
--known-answer consumer is named (item:<unread id> or gate:<name>; another string is accepted with a warning); 4 a worked
scope is LOOK, LEAD or UNCHECKED (UNCHECKED-NET too with --strict or at G3) -- this item only, never the lane; 0 proceed
on the listed residue. Register, record and derive modes exit 0; a usage error exits 1.

Must catch (tools/tests/test_prior_work.py, offline, sockets guarded): a NOTES '[x]' bullet naming the same leaf (exit
3); a ROOM claim 2 h old without done (LEAD live-claim, exit 4); Tomokiyo 'f.18 (no.6) ... both deciphered' for fr.3040
(KNOWN, exit 2; --known-answer key-check exit 0); an AUDIT line classing the item as already known (KNOWN); a NOTES period
gloss on THIS leaf (KNOWN); --register flagging the NEXT-STEPS row whose step is done; an edition window with its control
hit (LEAD); a decoded phrase printed within 3 days (SUBSTANCE).
Must NOT block: the E78 shape (KNOWN-PART, exit 0, code words as residue); a gloss on a DIFFERENT letter on a neighbouring
leaf (CONTEXT); DECODE 'Non-decrypted' (no KNOWN, no CLEAR); fr.16104 vs fr.16105 at the same folio (no match); a check
that could not run (UNCHECKED, never CLEAR); a claim on another slug that merely contains this one.

Rollout: warn-first -- workers run it and paste the output; enforcement on new briefs waits for the leave-one-target-out
replay and a measured false-block rate on research/PRIOR-WORK-SURVIVORS-2026-10-08.tsv.
TODO v2 (research/PRIOR-WORK-LEAK-2026-10-08.md): the office-keyed edition scan at scale (per-volume controls for every
seeded row, the OR/ORN compact index, calendar-number/Groen/footnote segmenters, feast-day, regnal and Republican date
generators, an alias table from KEY-OFFICES.tsv, --learn); the printed-cipher span router (Birch/Thurloe exact-length
votes against a within-span null, Japikse spaced type, Groen roman stretches); the leave-one-target-out replay harness;
WEB rows with same-blog controls; HOLD; be-api snippet routes for lending-only volumes; cache and clone freshness (48 h /
7 days) and shallow-clone --deepen; WVO print codes and RAH copia classes; the classed clear-share test beyond Eckert;
ARTEFACTS.tsv for typed artefacts beyond crops; work_queue.check() in room.py --push; --point; intake_gate_check reading
prior-work.tsv. Predicted classes are deliberately absent (rule 10).
"""
import argparse, csv, datetime, fnmatch, glob, gzip, hashlib, importlib.util, json, os, re, subprocess, sys, tempfile

TOOLS = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, TOOLS)
import shelfmark as sm  # noqa: E402
import print_check as pc  # noqa: E402
import next_steps_fresh as nsf  # noqa: E402
from html2text import Extractor  # noqa: E402

ROOT = os.path.dirname(TOOLS)
VERDICTS = ("DONE", "KNOWN", "KNOWN-PART", "LOOK", "LEAD", "UNCHECKED", "UNCHECKED-NET", "SUBSTANCE", "KEY-SOURCE",
            "CONTEXT", "CLEAR")
STEP_TYPES = ("read", "transcribe", "decode", "crop", "lookup", "audit", "upgrade-audit", "new-family-audit",
              "propagate-revision")
NEVER_DONE = {"propagate-revision", "upgrade-audit", "new-family-audit"}
WORKS_TEXT = {"read", "transcribe", "decode", "crop"}
COLUMNS = ["utc", "origin_main_commit", "item_id", "scope", "check", "route", "query", "control", "hits", "evidence",
           "verdict", "requests_by_host", "valid_until", "row_id"]
ITEM_COLUMNS = ["item_id", "shelfmark", "folio", "canvas", "decode", "ptr", "wvo", "date", "calendar", "sender",
                "recipient", "office", "place", "language", "kind", "holder_url", "clear_words", "verified"]
STEP_RE = {
    "read": r"read|decod|decipher|transcri|reconcil",
    "transcribe": r"transcri|blind pass|reconcil|ciphertext",
    "decode": r"decod|decipher|reading|key applied|applied the key",
    "crop": r"crop|iiif_lines",
    "lookup": r"look(?:ed)?[ -]?up|catalogue|search|print[- ]check|grep|checked",
    "audit": r"audit|verif|class",
}
STEP_RE = {k: re.compile(v, re.I) for k, v in STEP_RE.items()}
DONE_MARK = re.compile(r"^\s*(?:[-*+]|\d+\.)\s*(?:\*\*)?\[(?:[xX]\]|done|already run|retired\])", re.I)  # on the bullet itself
COMPLETED = re.compile(r"\b(?:done|finished|completed|reconciled|transcribed|decoded|deciphered|read in full|"
                       r"read and|was read|were read)\b", re.I)
LEAF_GLOSS = re.compile(r"gloss|interlinea|clear cop|en clair|clerk'?s copy|(?:period|contemporary|marginal|attached|"
                        r"clerk'?s|leaf'?s own)\s+(?:decipher|d[ée]chiffr|descifr|ontcijfer)\w*|d[ée]chiffr\w+ (?:en marge|"
                        r"interlin)|decipherment (?:on|over|above|beside|attached|written)", re.I)
OTHER_LETTER = re.compile(r"\b(?:different|another|other|separate)\s+(?:letter|item|piece|despatch|dispatch|"
                          r"correspondence)\b|\bnot (?:this|the same) letter\b|\bbelongs to\b", re.I)
DEC_POS = re.compile(r"(?<![a-z])(?:deciphered|decrypted|decoded|decipherment|d[ée]chiffr\w*|descifrad[oa]s?|"
                     r"ontcijferd|gedecodeerd|entziffert|decifrat[oa]|attached|glossed|clear copy|gloss(?:es)? (?:of|on|"
                     r"over|for))", re.I)
DEC_NEG = re.compile(r"\bun(?:deciphered|decrypted|decoded|glossed)\b|\bnon[- ]?(?:decrypted|deciphered|"
                     r"d[ée]chiffr\w*)\b|\b(?:not|never|nor)\s+(?:yet\s+)?(?:been\s+)?(?:deciphered|decrypted|decoded|"
                     r"glossed)\b|\bsans\s+(?:le\s+|son\s+)?d[ée]chiffr\w*|\bwithout\s+(?:a\s+|the\s+|any\s+)?"
                     r"(?:decipher\w*|gloss\w*)|\bniet\s+(?:ontcijferd|gedecodeerd)|\bnicht\s+entziffert|"
                     r"\bsin\s+descifrar|\bno\s+(?:period\s+)?(?:decipher\w*|gloss\w*|interlinear\w*|clear cop\w*)|"
                     r"key not found|sleutel[^.]{0,40}niet", re.I)
NEGATOR = re.compile(r"\b(?:no|not|never|nor|without|sans|niet|nicht|kein\w*|sin|aucun\w*|pas|ni|none|non)\b"
                     r"[\w\s'-]{0,25}$", re.I)
PARTIAL = re.compile(r"\bpartial(?:ly)?\b|\bpartly\b|\ben partie\b|\bgedeeltelijk\b|\bteilweise\b|\bin parte\b|"
                     r"\ben parte\b", re.I)
KEYSRC = re.compile(r"can be read with|\bkey (?:is |was )?(?:found|known|printed|published)\b|reconstructed (?:key|"
                    r"table)", re.I)
HOLDER = re.compile(r"catalog|notice|scopecontent|finding aid|inhoud|description|analyse|regest|copia|calendar|"
                    r"inventaire|inventory", re.I)
R10 = re.compile(r"\bN[0-5]\b(?!-)")
R10W = re.compile(r"\b(?:new|novel\w*|first|unpublished|never printed)\b", re.I)
CLASS_RE = re.compile(r"\b(?i:class(?:ed|ified|es)?)\b[^.|]{0,40}?\bN([0-5])\b(?!-)|\|\s*\**N([0-5])\**\s*\||"
                      r"\*\*N([0-5])\b(?!-)")
PARTICLES = set("de du des la le van von der den het zu of the and to a al el y e di da dal del count comte conde graf "
                "duke duc duca earl lord lady sir king roi rey queen prince prinz cardinal bishop eveque bisschop "
                "colonel general genl gen col lt capt captain major hon mr mrs saint sainte".split())
MONTHS = {1: "january ian ianuary janvier ianuier enero gennaio januari januar ianuarius jan",
          2: "february feb fevrier febrero febbraio februari februar februarius",
          3: "march mar mars marzo maart marz martius", 4: "april apr auril avril abril aprile",
          5: "may mai mayo maggio mei maius", 6: "june jun iuin juin junio giugno juni iunius",
          7: "july jul iuillet juillet julio luglio juli iulius",
          8: "august aug aout agosto augustus augusti", 9: "september sept sep septembre septiembre settembre",
          10: "october oct octobre octubre ottobre oktober octob", 11: "november nov novembre noviembre",
          12: "december dec decembre diciembre dicembre dezember"}
ROMAN = ["", "i", "ii", "iii", "iiii", "v", "vi", "vii", "viii", "ix", "x", "xi", "xii", "xiii", "xiiii", "xv", "xvi",
         "xvii", "xviii", "xix", "xx", "xxi", "xxii", "xxiii", "xxiiii", "xxv", "xxvi", "xxvii", "xxviii", "xxix", "xxx",
         "xxxi"]


def safe(text):
    """Rule 10: quoted evidence never carries a novelty class or a novelty word."""
    return R10W.sub("[*]", R10.sub("[*]", re.sub(r"\s+", " ", str(text or "")))).strip()


class UsageError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):           # exit 2 means KNOWN here, so a usage error exits 1
        self.print_usage(sys.stderr)
        print(f"prior_work.py: error: {message}", file=sys.stderr)
        sys.exit(1)


# ------------------------------------------------------------------ state at origin/main

class State:
    """Files of the repository at one ref (default origin/main), read with git; 'WORKTREE' reads the checkout."""

    def __init__(self, root, ref="origin/main"):
        self.root, self.ref, self._cache = root, ref, {}
        self.commit = "" if ref == "WORKTREE" else (self._git("rev-parse", "--verify", "-q", ref + "^{commit}") or "").strip()
        self.ok = bool(self.commit) or ref == "WORKTREE"
        self.when = (self._git("log", "-1", "--format=%cI", self.commit) or "").strip() if self.commit else ""

    def _git(self, *args, binary=False):
        try:
            r = subprocess.run(["git", "-C", self.root, *args], capture_output=True, timeout=120)
        except Exception:
            return None
        if r.returncode:
            return None
        return r.stdout if binary else r.stdout.decode("utf-8", "replace")

    def read(self, rel):
        if re.search(r"(^|/)restricted(/|$)", rel):
            return None
        if rel not in self._cache:
            data = self._git("show", f"{self.commit}:{rel}", binary=True) if self.commit else None
            if data is None and not self.commit:
                p = os.path.join(self.root, rel)
                data = open(p, "rb").read() if os.path.isfile(p) else None
            self._cache[rel] = None if data is None else data.decode("utf-8", "replace")
        return self._cache[rel]

    def ls(self, prefix):
        if self.commit:
            out = self._git("ls-tree", "-r", "--name-only", self.commit, "--", prefix) or ""
            names = out.splitlines()
        else:
            names = [os.path.relpath(os.path.join(d, f), self.root) for d, _, fs in os.walk(os.path.join(self.root, prefix))
                     for f in fs]
        return [n for n in names if not re.search(r"(^|/)restricted(/|$)", n)]


def disk_text(path):
    """A cached page on disk as text: Tomokiyo .htm (Shift_JIS) through html2text's Extractor, others as UTF-8."""
    raw = open(path, "rb").read()
    if not path.lower().endswith((".htm", ".html")):
        return raw.decode("utf-8", "replace")
    m = re.search(rb"charset=[\"']?([\w-]+)", raw[:2000], re.I)
    enc = m.group(1).decode().lower() if m else "utf-8"
    enc = "cp932" if enc in ("shift_jis", "shift-jis", "sjis", "x-sjis") else enc
    try:
        html = raw.decode(enc)
    except (UnicodeDecodeError, LookupError):
        html = raw.decode("utf-8", "replace")
    p = Extractor()
    p.feed(html)
    return "".join(p.out)


def walk_files(dirs, exts=(".htm", ".html", ".txt", ".md", ".tsv", ".json", ".csv"), max_bytes=3_000_000):
    for d in dirs:
        for dp, dn, fs in os.walk(d):
            dn[:] = [x for x in dn if x not in (".git", "restricted", "img", "images")]
            for f in fs:
                p = os.path.join(dp, f)
                if f.lower().endswith(exts) and os.path.getsize(p) <= max_bytes:
                    yield p


# ------------------------------------------------------------------ items and rows

def parse_date(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    return datetime.date(*map(int, m.groups())) if m else None


def item_unit(item):
    ids = set()
    if item.get("decode"):
        ids.add("R" + re.sub(r"\D", "", item["decode"]))
    if item.get("ptr"):
        ids.add("ptr:" + item["ptr"].strip())
    if item.get("wvo"):
        ids.add("wvo:" + re.sub(r"\D", "", item["wvo"]))
    if sm.LABEL_RE.fullmatch(item.get("item_id", "")):
        ids.add("label:" + item["item_id"])
    return sm.unit(item.get("shelfmark", ""), item.get("folio", ""), item.get("canvas", ""), ids)


def read_tsv(text):
    lines = [l for l in (text or "").splitlines() if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t")) if lines else []


def item_from_spec(spec):
    item = {k: "" for k in ITEM_COLUMNS}
    for part in spec.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            k = k.strip().lower()
            if k not in ITEM_COLUMNS:
                raise UsageError(f"--item-spec key {k!r} is not one of {', '.join(ITEM_COLUMNS)}")
            item[k] = v.strip()
    if not item["item_id"]:
        item["item_id"] = "adhoc-" + hashlib.sha1(spec.encode()).hexdigest()[:6]
    item["verified"] = item["verified"] or "ad hoc"
    return item


class Ctx:
    def __init__(self, a, state):
        self.a, self.state, self.slug, self.root = a, state, a.slug, a.root
        self.now = (datetime.datetime.strptime(a.now, "%Y-%m-%dT%H:%M").replace(tzinfo=datetime.timezone.utc)
                    if a.now else datetime.datetime.now(datetime.timezone.utc))
        self.today, self.utc = self.now.date(), self.now.strftime("%Y-%m-%d %H:%M")
        self.folder = f"ciphers/{self.slug}"
        self.net = None
        items = read_tsv(state.read(f"{self.folder}/items.tsv"))
        vols = set().union(*[sm.volume_keys(i.get("shelfmark", "")) for i in items]) if items else set()
        notes_vols = sm.volume_keys(state.read(f"{self.folder}/NOTES.md") or "")
        self.multi_volume = len(vols) > 1 or len(notes_vols) > 1
        self.items, self.unit_pages, self.leaf_answered = items, None, None

    def row(self, item, scope, check, route, verdict, evidence="", query="", control="", hits="", net=False, residue=""):
        rid = f"{item['item_id']}:{check}:{hashlib.sha1((route + '|' + query).encode()).hexdigest()[:6]}"
        valid = (self.today + datetime.timedelta(days=14)).isoformat() if net else self.today.isoformat()
        return dict(utc=self.utc, origin_main_commit=self.state.commit[:12], item_id=item["item_id"], scope=scope,
                    check=check, route=route, query=safe(query)[:160], control=control, hits=str(hits),
                    evidence=safe(evidence)[:200], verdict=verdict, requests_by_host="", valid_until=valid, row_id=rid,
                    residue=safe(residue)[:200])


def sentences(line):
    return [s for s in re.split(r"(?<=[.;!?])\s+|\s*\*\s*", line) if s.strip()]


def classify(text):
    """'pos' | 'partial' | 'keysrc' | 'neg' | None for one line, the strongest sentence winning. A decipherment word is
    negated by a negator up to three words before it ('no separate dechiffrement', 'sans le dechiffrement', 'not yet
    deciphered', 'Non-decrypted') or by a fixed phrase ('undeciphered', 'key not found')."""
    found = set()
    for s in sentences(text):
        rest = DEC_NEG.sub(" ", s)
        pos = [m for m in DEC_POS.finditer(rest) if not NEGATOR.search(rest[max(0, m.start() - 40):m.start()])]
        if pos and PARTIAL.search(s):
            found.add("partial")
        elif pos:
            found.add("pos")
        elif KEYSRC.search(s):
            found.add("keysrc")
        elif DEC_NEG.search(s) or DEC_POS.search(rest):
            found.add("neg")
    for k in ("pos", "partial", "keysrc", "neg"):
        if k in found:
            return k
    return None


def has_slug(slug, text):
    return re.search(rf"(?<![\w-]){re.escape(slug)}(?![\w-])", text or "") is not None


def lines_of(state, rel):
    return (state.read(rel) or "").splitlines()


# ------------------------------------------------------------------ check 1: own work

def check_own(ctx, item, u, step):
    rows, st, f = [], ctx.state, ctx.folder
    if not st.ok:
        rows.append(ctx.row(item, "step", "1-own", "state", "UNCHECKED",
                            f"{ctx.a.ref} does not resolve in {ctx.root}: own work not read at current state"))
    for fn in ("NOTES.md", "ITERATE.md", "HYPOTHESES.md"):
        prose = None
        for i, line in enumerate(lines_of(st, f"{f}/{fn}"), 1):
            m = sm.match(u, line, ctx.multi_volume)
            if not m or m == "fuzzy":
                continue
            loc = f"{fn}:{i}"
            if DONE_MARK.search(line):
                if m == "exact" and STEP_RE.get(step, re.compile("^$")).search(line) and step not in NEVER_DONE \
                        and not OPEN_WORDS.search(line):
                    rows.append(ctx.row(item, "step", "1-own", loc, "DONE", f"{loc} {line.strip()}"))
                else:
                    why = ("volume not named in a multi-volume folder" if m == "ambiguous" else
                           "the bullet says part is still open" if OPEN_WORDS.search(line) else "marker for this unit, other step")
                    rows.append(ctx.row(item, "step", "1-own", loc, "LEAD", f"done-candidate ({why}): {loc} {line.strip()}"))
            elif m == "exact" and step in STEP_RE and STEP_RE[step].search(line) and COMPLETED.search(line):
                prose = (loc, line)
        if prose and step not in NEVER_DONE:
            rows.append(ctx.row(item, "step", "1-own", prose[0], "LEAD", f"done-candidate (prose): {prose[0]} {prose[1].strip()}"))
    rows += audit_classes(ctx, item, u, step)
    # WORK-QUEUE: a done row naming slug and unit
    for r in read_tsv(st.read("WORK-QUEUE.tsv")):
        blob = " ".join(r.values()) if r else ""
        if has_slug(ctx.slug, blob) and str(r.get("status", "")).startswith("done") and sm.match(u, blob, ctx.multi_volume) == "exact":
            v = "DONE" if (STEP_RE.get(step) and STEP_RE[step].search(blob) and step not in NEVER_DONE) else "LEAD"
            rows.append(ctx.row(item, "step", "1-own", f"WORK-QUEUE:{r.get('job_id')}", v,
                                f"WORK-QUEUE {r.get('job_id')} {r.get('status')}: {r.get('note', '')}"))
    # artefact the step would produce (v1: crop files for this leaf)
    if step == "crop":
        for p in st.ls(f"{f}/images"):
            if "crop" in p.lower() or re.search(r"_L\d+\.", p):
                if sm.match(u, os.path.basename(p), ctx.multi_volume) == "exact":
                    rows.append(ctx.row(item, "step", "1-own", "artefact", "DONE", f"crop on file: {p}"))
                    break
    rows += room_claims(ctx, item, u)
    return rows


def audit_classes(ctx, item, u, step):
    """AUDIT.md and status.json lines classing this exact item."""
    rows, found = [], None
    lines = lines_of(ctx.state, f"{ctx.folder}/AUDIT.md")
    other = {k for l in lines for k in sm.parse(l).leaves} - set(u.leaves)
    single = not other
    head = ""
    for i, line in enumerate(lines, 1):
        if line.startswith("#"):
            head = line
        m = CLASS_RE.search(line)
        if not m:
            continue
        names = sm.match(u, line, ctx.multi_volume) == "exact" or sm.match(u, head, ctx.multi_volume) == "exact"
        if names or (single and not sm.parse(line).leaves):
            found = (f"AUDIT.md:{i}", int(next(g for g in m.groups() if g)), line)
    res = (json.loads(ctx.state.read("status.json") or "{}") or {}).get("results", []) if ctx.state.read("status.json") else []
    for r in res if isinstance(res, list) else []:
        if str(r.get("link", "")).rstrip("/").endswith(f"/ciphers/{ctx.slug}"):
            blob = f"{r.get('document_id', '')} {r.get('title', '')}"
            cls = re.search(r"N([0-5])", str(r.get("plaintext_novelty") or r.get("novelty") or ""))
            if cls and sm.match(u, blob, ctx.multi_volume) == "exact":
                known_text = str(r.get("text", "")).startswith("known")
                found = ("status.json", int(cls.group(1)), blob + (" (text: known)" if known_text else ""))
    prog = [r for r in read_tsv(ctx.state.read("PROGRESS.tsv")) if r.get("folder") == ctx.slug]
    for r in prog:
        blob = " ".join(str(r.get(c, "")) for c in ("name", "note", "source"))
        if len(prog) == 1 or sm.match(u, blob, ctx.multi_volume) == "exact":
            if r.get("txt") == "k":
                rows.append(ctx.row(item, "plaintext", "1-own", f"PROGRESS:{r.get('name')}", "KNOWN",
                                    f"PROGRESS.tsv row {r.get('name')!r}: txt=k (plaintext known): {r.get('source', '')}"))
            elif r.get("R") == "x" and step in ("read", "decode", "transcribe"):
                rows.append(ctx.row(item, "step", "1-own", f"PROGRESS:{r.get('name')}", "LEAD",
                                    f"done-candidate: PROGRESS.tsv row {r.get('name')!r} says the whole letter reads (R=x)"))
    if not found:
        return rows
    loc, n, line = found
    if step == "audit":
        rows.append(ctx.row(item, "step", "1-own", loc, "DONE", f"an audit already classes this item: {loc} {line}"))
    elif step in NEVER_DONE:
        rows.append(ctx.row(item, "step", "1-own", loc, "CONTEXT", f"existing audit {loc}; {step} is never DONE"))
    if n <= 2:
        rows.append(ctx.row(item, "plaintext", "1-own", loc, "KNOWN", f"audit classes the text as already printed/read: {loc} {line}"))
    elif "(text: known)" in line:
        rows.append(ctx.row(item, "plaintext", "1-own", loc, "KNOWN-PART", f"{loc} text known; reading covers part",
                            residue="the spans status.json lists as unresolved"))
    elif step in ("read", "decode", "transcribe"):
        rows.append(ctx.row(item, "step", "1-own", loc, "LEAD", f"done-candidate: an audited reading of ours exists, {loc}"))
    return rows


def room_claims(ctx, item, u):
    rows, room = [], lines_of(ctx.state, "ROOM.md")[-2000:]
    for i, l in enumerate(room):
        m = nsf.ROOM_RE.match(l)
        if not m or not has_slug(ctx.slug, l) or not re.search(r"\bclaim", m.group(3), re.I):
            continue
        if sm.match(u, m.group(3), ctx.multi_volume) != "exact":
            continue
        t = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)
        age = (ctx.now - t).total_seconds() / 3600
        tag = (m.group(2).split() or [""])[0]
        if not 0 <= age < 6 or (ctx.a.me and tag == ctx.a.me):
            continue
        done = any(tag in x.split("|")[1] and has_slug(ctx.slug, x) and re.search(r"\bdone\b", x)
                   for x in room[i + 1:] if x.count("|") >= 2)
        if not done:
            rows.append(ctx.row(item, "step", "1-own", f"ROOM {m.group(1)}", "LEAD",
                                f"live-claim ({age:.1f} h, no done line): {l}"))
    return rows


# ------------------------------------------------------------------ check 2: leaf and neighbours

def manifest_images(text):
    """[(name, (folio, side) or None, canvas or None)] from any of the repository's manifest.json shapes."""
    out = []
    try:
        data = json.loads(text or "")
    except ValueError:
        return out

    def walk(o, key=None):
        if isinstance(o, dict):
            name = next((o[k] for k in ("file", "crop", "source_file", "image", "name", "path") if isinstance(o.get(k), str)),
                        key if key and re.search(r"\.(jpe?g|png|tiff?|webp)$", key, re.I) else None)
            if name:
                lv = sm.leaves(f"f.{o['folio']}") if o.get("folio") else sm.leaves(name)
                cv = o.get("canvas")
                if cv is None:
                    mm = re.search(r"canvas[_-]?(\d+)|_f(\d+)_", name)
                    cv = int(next(g for g in mm.groups() if g)) if mm else None
                out.append((name, sorted(lv)[0] if lv else None, int(cv) if str(cv).isdigit() else None))
            for k, v in o.items():
                walk(v, k)
        elif isinstance(o, list):
            for v in o:
                walk(v)
    walk(data)
    return out


def neighbours(leaf):
    """[(role, (folio, side))]: cipher page, facing page, two before, four after."""
    n, side = leaf[0], leaf[1] or "r"
    seq = lambda k: (n + (k + (side == "v")) // 2, "rv"[(k + (side == "v")) % 2])   # k pages from n-recto
    pages = [("cipher-page", (n, side)), ("facing", (n - 1, "v") if side == "r" else (n + 1, "r"))]
    pages += [("before-1", seq(-1)), ("before-2", seq(-2))] + [(f"after-{k}", seq(k)) for k in range(1, 5)]
    seen, out = set(), []
    for role, p in pages:
        if p not in seen and p[0] > 0:
            seen.add(p)
            out.append((role, p))
    return out


def check_leaf(ctx, item, u, step):
    if step not in WORKS_TEXT:
        return [], []
    rows, look, answered = [], [], None
    for fn in ("NOTES.md", "AUDIT.md"):
        for i, line in enumerate(lines_of(ctx.state, f"{ctx.folder}/{fn}"), 1):
            clearpages = DONE_MARK.search(line) and re.search(r"clear[- ]pages", line, re.I)
            if not (LEAF_GLOSS.search(line) or clearpages) or (HOLDER.search(line) and not clearpages):
                continue
            m, mf = sm.match(u, line, ctx.multi_volume), sm.match(u, line, ctx.multi_volume, tol=4)
            loc, cls = f"{fn}:{i}", classify(line)
            if m == "exact":
                if OTHER_LETTER.search(line):
                    v = "CONTEXT"
                elif cls == "pos":
                    v = "KNOWN"
                elif cls == "partial":
                    v = "KNOWN-PART"
                else:
                    v = "CLEAR" if (cls == "neg" or clearpages) else None
                if v:
                    answered = ctx.row(item, "plaintext", "2-leaf", loc, v, f"gloss check recorded: {loc} {line.strip()}",
                                       residue="the glossed lines' uncovered spans" if v == "KNOWN-PART" else "")
            elif mf in ("exact", "fuzzy") and cls in ("pos", "partial"):
                v = "CONTEXT" if OTHER_LETTER.search(line) else "KEY-SOURCE"
                rows.append(ctx.row(item, "plaintext", "2-leaf", loc, v,
                                    ("gloss on another letter, not this one: " if v == "CONTEXT" else
                                     "unattributed gloss on a neighbouring leaf (nearby sheet): ") + f"{loc} {line.strip()}"))
    if ctx.leaf_answered:
        answered = ctx.leaf_answered
    leaf = sorted(u.leaves)[0] if u.leaves else None
    canvas = sorted(u.canvases)[0] if u.canvases else None
    q = f"{sorted(u.vols)}|{leaf}|{canvas}|{item.get('ptr', '')}|{item.get('decode', '')}"
    if answered:
        rows.append(answered)
        return rows, look
    lrow = ctx.row(item, "plaintext", "2-leaf", "leaf-look", "LOOK", "", query=q)
    imgs = manifest_images(ctx.state.read(f"{ctx.folder}/images/manifest.json"))
    pages = [i for i in imgs if not re.search(r"crop|_L\d+\.|overlay|thumb|contact", i[0], re.I)]
    if leaf:
        for role, p in neighbours(leaf):
            hit = next((i[0] for i in pages if i[1] and i[1][0] == p[0] and (i[1][1] in ("", p[1]))), "")
            look.append([role, f"{p[0]}{p[1]}", "", hit, "manifest" if hit else "folio arithmetic"])
    elif canvas:
        for k, role in ((0, "cipher-page"), (-1, "before-1"), (-2, "before-2"), (1, "after-1"), (2, "after-2"),
                        (3, "after-3"), (4, "after-4")):
            hit = next((i[0] for i in pages if i[2] == canvas + k), "")
            look.append([role, "", str(canvas + k), hit, "manifest" if hit else "canvas arithmetic"])
    elif item.get("ptr"):
        p0 = int(re.match(r"\d+", item["ptr"]).group(0))
        for k in (0, -2, -1, 1, 2, 3, 4):
            look.append(["cipher-page" if k == 0 else f"ptr{k:+d}", "", "", f"ptr {p0 + k}", "pointer arithmetic"])
    listed = {x[3] for x in look}
    if 0 < len(pages) <= 8:
        look += [["unit", "", "", i[0], "manifest"] for i in pages if i[0] not in listed]
    elif ctx.unit_pages and ctx.unit_pages <= 8:
        look.append(["unit", "", "", f"all {ctx.unit_pages} DECODE record images", "DECODE listing"])
    if not look:
        look.append(["unit", "", "", "no folio, canvas or pointer in items.tsv: name the leaf to narrow the look", "none"])
    lrow["evidence"] = safe(f"no gloss/clear-copy check recorded for this leaf; look.tsv lists {len(look)} crop(s) owed "
                            f"({sum(1 for x in look if x[3] and x[4] == 'manifest')} on disk)")
    rows.append(lrow)
    return rows, [[item["item_id"], lrow["row_id"]] + x + ["owed"] for x in look]


# ------------------------------------------------------------------ check 3: holder, portal, solver repositories

def check_portals(ctx, item, u):
    rows = []
    nums = sorted({v.rsplit(" ", 1)[-1] for v in u.vols if re.search(r"\d+$", v)})
    rids = sorted(i for i in u.ids if re.fullmatch(r"R\d+", i))
    mirror = portal_dirs(ctx, "tomokiyo", ["sources/cryptiana/web"])[0]
    if nums or rids:
        if not os.path.isdir(mirror):
            rows.append(ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "UNCHECKED", "sources/cryptiana/web not on disk"))
        else:
            rows += tomokiyo(ctx, item, u, mirror, nums, rids)
    if rids:
        rows += decode_listing(ctx, item, rids[0])
    rows += solver_caches(ctx, item, u, nums + rids + sorted(i[4:] for i in u.ids if i.startswith("ptr:")))
    for fn in ("NOTES.md", "sources.tsv", "SOURCES.md"):
        for i, line in enumerate(lines_of(ctx.state, f"{ctx.folder}/{fn}"), 1):
            if HOLDER.search(line) and sm.match(u, line, ctx.multi_volume) == "exact" and classify(line) in ("pos", "partial"):
                if not re.match(r"\s*[-*]\s*\[", line):
                    rows.append(ctx.row(item, "plaintext", "3-holder", f"{fn}:{i}", "LEAD",
                                        f"holder/catalogue note with decipherment wording: {fn}:{i} {line.strip()}"))
    return rows


def tomokiyo(ctx, item, u, mirror, nums, rids):
    exact, fuzzy = [], []
    pat = re.compile(r"(?<![0-9A-Za-z])(?:%s)(?![0-9])" % "|".join(map(re.escape, nums + rids)))
    for path in walk_files([mirror], exts=(".htm", ".html", ".txt")):
        if not pat.search(open(path, "rb").read().decode("latin-1")):
            continue
        rel, head_vols = os.path.relpath(path, ctx.root), set()
        for i, line in enumerate(disk_text(path).splitlines(), 1):
            k = sm.parse(line)
            if line.lstrip().startswith("#") and k.vols:
                head_vols = k.vols
            vols = k.vols | head_vols
            hit = "exact" if set(rids) & k.ids else None
            if not hit and u.vols & vols:
                for n, side in u.leaves:
                    for m, s2 in k.leaves:
                        if m == n and not (side and s2 and side != s2):
                            hit = "exact"
                        elif abs(m - n) <= 2 and hit is None:
                            hit = "fuzzy"
            if not hit:
                continue
            cls = classify(line)
            v = {"pos": "KNOWN", "partial": "KNOWN-PART", "keysrc": "KEY-SOURCE"}.get(cls, "CONTEXT")
            if hit == "fuzzy" and v in ("KNOWN", "KNOWN-PART"):
                v = "LEAD"
            note = "undeciphered: no evidence either way; " if cls == "neg" else ("fuzzy-match (folio within 2); " if hit == "fuzzy" else "")
            r = ctx.row(item, "plaintext", "3-tomokiyo", f"{rel}:text{i}", v, f"{note}{rel} (text line {i}) {line.strip()}",
                        residue="spans the page does not cover" if v == "KNOWN-PART" else "")
            (exact if hit == "exact" else fuzzy).append(r)
    rows = exact or fuzzy
    if not rows:
        rows = [ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "CLEAR",
                        f"cached mirror (sources/cryptiana/web, snapshot 19 Sept 2026) names no folio of this unit; terms {nums + rids}")]
    return rows


def decode_listing(ctx, item, rid):
    num, rows, seen = rid[1:], [], set()
    bases = portal_dirs(ctx, "decode-listing", ["sources/decode"])
    for path in walk_files(bases, exts=(".tsv",)):
        for r in read_tsv(open(path, encoding="utf-8", errors="replace").read()):
            if str(r.get("id", "")).strip() != num or "status" not in r:
                continue
            st, pages = r.get("status", ""), r.get("number_of_pages") or r.get("pages") or ""
            if str(pages).strip().isdigit():
                ctx.unit_pages = int(pages)
            rel = os.path.relpath(path, ctx.root)
            if re.search(r"partial", st, re.I):
                v, ev = "KNOWN-PART", f"DECODE {rid} '{st}': part read; residue from the documents and the image"
            elif re.fullmatch(r"\s*decrypted\s*", st, re.I):
                v, ev = "LEAD", f"DECODE {rid} 'Decrypted', {pages} page(s): fetch the documents (may be a key only)"
            else:
                v, ev = "CONTEXT", f"DECODE {rid} '{st}', {pages} page(s): a status is not evidence either way; the record images are in look.tsv"
            if st not in seen:
                seen.add(st)
                rows.append(ctx.row(item, "plaintext", "3-decode", rel, v, f"{ev} ({rel})",
                                    residue="spans the DECODE documents do not cover" if v == "KNOWN-PART" else ""))
            break
    for path in [p for b in bases for p in glob.glob(os.path.join(b, "**", f"record_{num}.html"), recursive=True)]:
        html = open(path, encoding="utf-8", errors="replace").read()
        if re.search(r"Cleartext Publication|PLAINTEXT", html):
            rows.append(ctx.row(item, "plaintext", "3-decode", os.path.relpath(path, ctx.root), "LEAD",
                                f"DECODE record page lists a cleartext/transcription document: fetch it ({os.path.relpath(path, ctx.root)})"))
    if not rows:
        rows.append(ctx.row(item, "plaintext", "3-decode", "listing", "UNCHECKED",
                            f"{rid} is in no cached DECODE listing under sources/decode (refresh with tools/decode_list.py)"))
    return rows


def our_first_reading(ctx):
    out = ctx.state._git("log", "--diff-filter=A", "--format=%cs", ctx.state.commit or "HEAD", "--",
                         f"{ctx.folder}/reading*", f"{ctx.folder}/*/reading*") or ""
    dates = sorted(out.split())
    return dates[0] if dates else ""


def solver_caches(ctx, item, u, terms):
    dirs = portal_dirs(ctx, "solver-repo", ["sources/cyphersolver", "sources/bourdeau", "sources/cyphersolver-site"]) + list(ctx.a.clone)
    dirs = [d for d in dirs if os.path.isdir(d)]
    if not terms:
        return []
    if not dirs:
        return [ctx.row(item, "plaintext", "3-solver", "caches", "UNCHECKED", "no solver-repository cache or clone on disk")]
    pat = re.compile(r"(?<![0-9A-Za-z])(?:%s)(?![0-9])" % "|".join(map(re.escape, terms)))
    rows, ours = [], None
    for path in walk_files(dirs):
        text = open(path, encoding="utf-8", errors="replace").read()
        if not pat.search(text):
            continue
        folder = os.path.dirname(path)
        ctxt = text + " ".join(open(p, encoding="utf-8", errors="replace").read()[:20000]
                               for p in glob.glob(os.path.join(folder, "*")) if re.search(r"profile\.json|NOTES\.md$", p))
        if sm.match(u, ctxt) != "exact" and not (set(t for t in terms if t.startswith("R")) & sm.parse(text).ids):
            continue
        rel = os.path.relpath(path, ctx.root) if path.startswith(ctx.root) else path
        when = (re.search(r"20\d\d-\d\d-\d\d", path) or [""])[0]
        if re.search(r"cipher-lab|NoAutopilot|issue\s*#?\d+", ctxt, re.I):
            v, ev = "CONTEXT", "copies or cites our work, excluded"
        elif re.search(r"reading|decipher|plaintext|decrypt", os.path.basename(path), re.I):
            ours = our_first_reading(ctx) if ours is None else ours
            v = "CONTEXT" if (ours and when and ours < when) else "KNOWN"
            ev = f"solver reading file (snapshot {when or '?'}; ours first {ours or 'none'})"
        else:
            v, ev = "CONTEXT", "duplicate-effort-risk (catalogue/planning line, not a reading)"
        rows.append(ctx.row(item, "plaintext", "3-solver", rel, v, f"{ev}: {rel}"))
    return rows or [ctx.row(item, "plaintext", "3-solver", "caches", "CLEAR",
                            "no cached solver file names this unit: " + ", ".join(os.path.relpath(d, ctx.root) if d.startswith(ctx.root) else d for d in dirs))]


# ------------------------------------------------------------------ check 4: editions (and G3 phrases)

def registry(root, name):
    path = os.path.join(root, "tools", "data", name)
    return read_tsv(open(path, encoding="utf-8").read()) if os.path.isfile(path) else []


def load_editions(root):
    """prior_editions.tsv rows, the last row per edition_id winning (the file is append-only)."""
    return list({r.get("edition_id"): r for r in registry(root, "prior_editions.tsv")}.values())


def portal_dirs(ctx, kind, default):
    rows = [r for r in registry(ctx.root, "prior_portals.tsv") if r.get("kind") == kind]
    rels = [p for r in rows for p in (r.get("cache_paths") or "").split()] if rows else default
    return [os.path.join(ctx.root, p) for p in rels]


def names(s):
    return {w for w in pc.norm(s or "").split() if len(w) >= 4 and w not in PARTICLES}


def edition_matches(ed, item, slug):
    d = parse_date(item.get("date"))
    y = d.year if d else None
    lo, hi = int((ed.get("date_from") or "0")[:4] or 0), int((ed.get("date_to") or "9999")[:4] or 9999)
    if y is not None and not lo <= y <= hi:
        return False
    if any(fnmatch.fnmatch(slug, p) for p in (ed.get("match_slugs") or "").split() if p):
        return True
    who = names(" ".join(item.get(k, "") for k in ("sender", "recipient", "office")))
    return bool(who & names(ed.get("correspondents", "").replace(";", " ")))


def date_variants(d, calendar=""):
    """[(date, label)]: d +-1 day, plus the other calendar style for 1582-1752 (Old/New Style noted)."""
    out = [(d + datetime.timedelta(days=k), "as written") for k in (-1, 0, 1)]
    if 1582 <= d.year <= 1752:
        shift = 10 if d.year < 1700 else 11
        styles = {"os": [shift], "ns": [-shift]}.get(calendar.lower(), [shift, -shift])
        out += [(d + datetime.timedelta(days=s + k), "other style") for s in styles for k in (-1, 0, 1)]
    return out


def date_regex(dates):
    alts = []
    for d, _ in dates:
        months = "|".join(re.escape(pc.norm(w)) for w in MONTHS[d.month].split())
        day = rf"(?:{d.day}|{ROMAN[d.day]})(?:st|nd|rd|th|d|e|er|me|eme|o)?"
        alts.append(rf"\b(?:{months})\s+{d.day}(?:st|nd|rd|th|d)?\b|\b{day}\s+(?:iour\s+)?(?:de\s+|of\s+|d\s+)?(?:{months})\b")
    return re.compile("|".join(alts))


_TEXTS = {}


def edition_text(path):
    if path not in _TEXTS:
        _TEXTS[path] = pc.norm(pc.dehyphen(pc.read_text(path)))
    return _TEXTS[path]


def find_letter(text, d, calendar, who_a, who_b, window=(300, 1000)):
    """Positions where a date variant (+-1 day, both styles where they differ) and name tokens of both correspondents
    fall in one window; a date whose nearby year conflicts with the item's is skipped."""
    hits, years = [], {str(d.year + k) for k in (-1, 0, 1)}
    for m in date_regex(date_variants(d, calendar)).finditer(text):
        near = set(re.findall(r"\b1[4-9]\d\d\b", text[max(0, m.start() - 40):m.end() + 40]))
        if near and not near & years:
            continue
        w = set(text[max(0, m.start() - window[0]):m.end() + window[1]].split())
        if (not who_a or w & who_a) and (not who_b or w & who_b) and (who_a or who_b):
            hits.append(m.start())
    return hits


_IDX = {}


def djvu_index(root, cache):
    """identifier -> cached _djvu.txt(.gz) path: tracked files (git ls-files) plus the --cache folder."""
    if root not in _IDX:
        r = subprocess.run(["git", "-C", root, "ls-files", "*_djvu.txt", "*_djvu.txt.gz"], capture_output=True, text=True)
        paths = [os.path.join(root, p) for p in r.stdout.splitlines()] if r.returncode == 0 else \
            glob.glob(os.path.join(root, "**", "*_djvu.txt*"), recursive=True)
        _IDX[root] = {re.sub(r"_djvu\.txt(\.gz)?$", "", os.path.basename(p)): p for p in reversed(paths)
                      if not re.search(r"(^|/)restricted(/|$)", p)}
    idx = dict(_IDX[root])
    for p in glob.glob(os.path.join(cache, "*_djvu.txt*")):
        idx.setdefault(re.sub(r"_djvu\.txt(\.gz)?$", "", os.path.basename(p)), p)
    return idx


def ia_path(ctx, idx, ident):
    """Cached djvu path; with --network, one download through print_check.Net into --cache (never the repository)."""
    if idx.get(ident) or not ctx.net or not ident:
        return idx.get(ident), "not on disk"
    body, st = ctx.net.get(f"https://archive.org/download/{ident}/{ident}_djvu.txt", raw=True)
    if not body:
        return None, st
    os.makedirs(ctx.a.cache, exist_ok=True)
    path = os.path.join(ctx.a.cache, f"{ident}_djvu.txt.gz")
    with gzip.open(path, "wb") as f:
        f.write(body)
    return path, "downloaded"


def check_editions(ctx, item, phrases=None):
    rows, eds = [], [e for e in load_editions(ctx.root) if edition_matches(e, item, ctx.slug)]
    d, who_a, who_b = parse_date(item.get("date")), names(item.get("sender")), names(item.get("recipient"))
    if not eds:
        return [ctx.row(item, "plaintext", "4-editions", "registry", "UNCHECKED-NET",
                        "core-only: no tools/data/prior_editions.tsv row matches this slug, year and correspondents; "
                        "check-solved names the editions read or records that none exists")]
    if d and not (who_a or who_b) and phrases is None:
        return [ctx.row(item, "plaintext", "4-editions", "identity", "UNCHECKED",
                        f"{len(eds)} edition row(s) match, but the item names no sender or recipient: the date+correspondent "
                        "search cannot run (add them to items.tsv)")]
    idx, missing, clean = djvu_index(ctx.root, ctx.a.cache), [], []
    for ed in eds:
        title, ids = ed.get("title", "?"), (ed.get("ia_ids") or "").split()
        if not ids:
            rows.append(ctx.row(item, "plaintext", "4-editions", f"registry:{ed.get('edition_id')}", "UNCHECKED-NET",
                                f"{title}: no IA route in v1 (access {ed.get('access_tier')}); {ed.get('verified', '')}"))
            continue
        cd, ctl = parse_date(ed.get("control_date")), None
        if cd:
            cpath = ia_path(ctx, idx, ed.get("control_ia"))[0]
            if cpath:
                ctl = bool(find_letter(edition_text(cpath), cd, "", names(ed.get("control_sender")),
                                       names(ed.get("control_recipient"))))
        ctl_note = {True: f"control hit in {ed.get('control_ia')}", False: f"control MISSED in {ed.get('control_ia')}",
                    None: "no positive control" if not cd else "control volume not on disk"}[ctl]
        unchecked = []
        for ident in ids:
            path, why = ia_path(ctx, idx, ident)
            if not path:
                (missing.append(ident) if not ctx.net else rows.append(ctx.row(
                    item, "plaintext", "4-editions", f"net:ia:{ident}", "UNCHECKED-NET",
                    f"{title} ({ident}): djvu text not fetched ({why}); lending-only volumes need the be-api snippet route (v2)",
                    net=True)))
                continue
            text = edition_text(path)
            if phrases is not None:
                rows += g3_phrases(ctx, item, ed, ident, text, phrases, ctl)
                continue
            if not d:
                rows.append(ctx.row(item, "plaintext", "4-editions", f"ia:{ident}", "LEAD",
                                    f"undated item inside {title}'s span: search it by correspondents by hand"))
                continue
            hits = find_letter(text, d, item.get("calendar", ""), who_a, who_b)
            q = f"{d} +-1 day{' (both styles)' if 1582 <= d.year <= 1752 else ''}, {sorted(who_a)} & {sorted(who_b)}"
            if hits:
                null = [len(find_letter(text, d + datetime.timedelta(days=k), "", who_a, who_b)) for k in (-30, 30)]
                snip = text[max(0, hits[0] - 80):hits[0] + 120]
                rows.append(ctx.row(item, "plaintext", "4-editions", f"ia:{ident}", "LEAD",
                                    f"edition-hit {ident}: {len(hits)} window(s), null at +-30 days {null}; open the page, "
                                    f"then --record: {snip}", query=q, control=ctl_note, hits=len(hits)))
            elif ctl:
                clean.append(ident)
            else:
                unchecked.append(ident)
        if unchecked:
            rows.append(ctx.row(item, "plaintext", "4-editions", f"ed:{ed.get('edition_id')}", "UNCHECKED",
                                f"{title}: no window in {' '.join(unchecked)}, but {ctl_note}: a miss is not a negative",
                                query=f"{d} +-1 day, {sorted(who_a)} & {sorted(who_b)}", control=ctl_note))
    if missing:
        rows.append(ctx.row(item, "plaintext", "4-editions", "not-cached", "UNCHECKED-NET",
                            f"not on disk ({' '.join(missing)}); --network fetches the djvu text"))
    if clean:
        rows.append(ctx.row(item, "plaintext", "4-editions", "cached", "CLEAR",
                            "date +-1 day and both correspondents searched, control hit, no window: " + " ".join(clean)))
    if ctx.net and phrases is None:
        rows += openalex_identity(ctx, item)
    return rows


def openalex_identity(ctx, item):
    out, ctl = [], []
    pc.check_openalex([("control", "cipher diplomatic correspondence decipherment")], ctx.net, ctl)
    q = " ".join(x for x in (item.get("sender"), item.get("recipient"), (item.get("date") or "")[:4], "cipher") if x)
    if not ctl or not ctl[0][2][:1].isdigit():
        return [ctx.row(item, "plaintext", "4-net", "net:openalex", "UNCHECKED-NET", "OpenAlex host control failed",
                        query=q, control="missed", net=True)]
    pc.check_openalex([("item", q)], ctx.net, out)
    res = out[0] if out else ["", "", "not searched", "", ""]
    who = names(item.get("sender")) | names(item.get("recipient"))
    v = "LEAD" if (res[2][:1].isdigit() and who & set(pc.norm(res[3]).split())) else ("CLEAR" if res[2].startswith("no hits") else "CONTEXT")
    return [ctx.row(item, "plaintext", "4-net", "net:openalex", v, f"OpenAlex '{q}': {res[2]}; {res[3]}", query=q,
                    control="host control hit", hits=res[2], net=True)]


def reading_phrases(text, k=6):
    words = re.findall(r"[A-Za-zÀ-ÿ']+|\d{2,}", text)
    rare = {w for w in words if (w[:1].isupper() and len(w) >= 4) or w.isdigit() or len(w) >= 8}
    cands = [" ".join(words[i:i + 5]) for i in range(0, max(0, len(words) - 4), 3) if rare & set(words[i:i + 5])]
    step = max(1, len(cands) // k) if cands else 1
    return cands[::step][:k], {pc.norm(w) for w in rare if w.lower() not in PARTICLES}


def g3_phrases(ctx, item, ed, ident, text, phrases, control_ok):
    ph, rare = phrases
    d, rows = parse_date(item.get("date")), []
    for p in ph:
        n, ctxs, near = pc.search_text(text, p)
        if not (n or near):
            continue
        pos = text.find(pc.norm(p)) if n else -1
        win = text[max(0, pos - 2000):pos + 2000] if pos >= 0 else " ".join(ctxs)
        shared = rare & set(win.split())
        dated = bool(d and date_regex([(d + datetime.timedelta(days=k), "") for k in range(-3, 4)]).search(win))
        v = "SUBSTANCE" if (dated and len(shared) >= 2) else "LEAD"
        rows.append(ctx.row(item, "plaintext", "6-g3", f"ia:{ident}", v,
                            f"{ed['title']} ({ident}): '{p}' {n} exact/{near} near; within +-3 days: {dated}; "
                            f"shared entities {sorted(shared)[:6]}", query=p, control="hit" if control_ok else "none", hits=n or near))
    if not rows:
        rows.append(ctx.row(item, "plaintext", "6-g3", f"ia:{ident}", "CLEAR" if control_ok else "UNCHECKED",
                            f"{ed['title']} ({ident}): {len(ph)} decoded phrases, no hit" + ("" if control_ok else "; no control hit")))
    return rows


def check_g3(ctx, item, reading_path):
    phrases = reading_phrases(open(reading_path, encoding="utf-8", errors="replace").read())
    if not phrases[0]:
        return [ctx.row(item, "plaintext", "6-g3", "phrases", "UNCHECKED", f"no distinctive phrase extracted from {reading_path}")]
    rows = check_editions(ctx, item, phrases=phrases)
    if ctx.net:
        out = []
        pc.check_ia_global(phrases[0], ctx.net, out)
        pc.check_gbooks(phrases[0], set(), ctx.net, out)
        for p, src, res, det, url in out:
            v = "UNCHECKED-NET" if res.startswith("not searched") else ("CLEAR" if res.startswith("no hits") else
                ("SUBSTANCE" if len(phrases[1] & set(pc.norm(det).split())) >= 2 else "LEAD"))
            rows.append(ctx.row(item, "plaintext", "6-g3", f"net:{src}", v, f"'{p}' {src}: {res}; {det}", query=p, net=True))
    else:
        rows.append(ctx.row(item, "plaintext", "6-g3", "net:ia-global+gbooks", "UNCHECKED-NET",
                            "G3 network phrase search not run (offline); run with --network before any class or SO row"))
    return rows


# ------------------------------------------------------------------ check 5: civil-war adapter

def civil_war(ctx, item, u, step):
    rows, path = [], os.path.join(ctx.root, "ciphers", "eckert-1864", "entries_mssEC19.py")
    try:
        spec = importlib.util.spec_from_file_location("entries_mssEC19", path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        codes = mod.load_vocab()
    except Exception as e:      # noqa: BLE001 -- any failure means the adapter did not run
        return [ctx.row(item, "plaintext", "5-civil-war", "adapter", "UNCHECKED", f"entries_mssEC19 not usable: {e}")]
    ptr, entry = (item.get("ptr", "") + "/").split("/")[:2]
    d = parse_date(item.get("date"))
    dm = (d.month, d.day) if d else None
    try:
        for kid, (kptr, kdm) in mod.known_blocks().items():
            if ptr and str(kptr) == ptr and kdm == dm and step in ("read", "decode", "transcribe"):
                rows.append(ctx.row(item, "step", "5-civil-war", f"known_blocks:{kid}", "DONE", f"already read as {kid} (pointer {ptr}, {d})"))
    except Exception:           # noqa: BLE001 -- known_blocks needs the ciphertext files; absence is not evidence
        pass
    src = glob.glob(os.path.join(ctx.root, "ciphers", ctx.slug, "sources", "*", f"p{ptr}.json")) if ptr else []
    if not src:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", "holder-transcription", "UNCHECKED-NET",
                            f"no cached Huntington transcription for pointer {ptr or '?'} (tools/huntington_transc.py)"))
        return rows
    j = json.load(open(src[0], encoding="utf-8"))
    rel = os.path.relpath(src[0], ctx.root)
    if not (j.get("transc") or "").strip():
        rows.append(ctx.row(item, "plaintext", "5-civil-war", rel, "CONTEXT",
                            f"the holder's record for pointer {ptr} carries no transcription text: the clear-share route has nothing to test"))
        return rows
    ents = mod.segment([(int(ptr), j.get("title"), j.get("transc") or "")])
    ent = next((e for e in ents if dm and mod.day_month(e["header"]) == dm), None)
    if ent is None and entry.isdigit():
        ent = next((e for e in ents if e["entry_on_page"] == int(entry)), None)
    if ent is None:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", rel, "LEAD", f"pointer {ptr} transcription cached but no entry matches {d}"))
        return rows
    toks = mod.toks(" ".join(ent["lines"]))
    code = [t for t in toks if t in codes]
    if not code:
        v = "KNOWN" if len(toks) >= 3 else "CONTEXT"
        rows.append(ctx.row(item, "plaintext", "5-civil-war", rel, v,
                            ("clear in the holder's own transcription (step 0 skip): " if v == "KNOWN" else
                             "entry too short to judge: ") + f"{ent['header']} | {' '.join(ent['lines'])[:120]}"))
    else:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", rel, "KNOWN-PART",
                            f"clear words public in the holder transcription, {len(set(code))} code word(s) not: {ent['header']}",
                            residue="code words: " + ", ".join(sorted(set(code)))))
    ctx.leaf_answered = ctx.row(item, "plaintext", "2-leaf", rel, "CLEAR",
                                f"leaf look answered by the holder's full-page transcription ({rel}); later pencil ignored")
    tsv = os.path.join(ctx.root, "ciphers", ctx.slug, "entries-mssEC19.tsv")
    if os.path.isfile(tsv):
        for r in read_tsv(open(tsv, encoding="utf-8").read()):
            if r.get("pointer") == ptr and r.get("entry_on_page") != str(ent["entry_on_page"]) and \
                    (r.get("already_read") or r.get("or_hit", "none") != "none"):
                rows.append(ctx.row(item, "plaintext", "5-civil-war", f"entries-mssEC19.tsv:{ptr}/{r['entry_on_page']}", "LEAD",
                                    f"same-page sibling {r.get('already_read') or ''} or_hit {r.get('or_hit')}: read it before this entry"))
    if ctx.a.or_dir:
        res = mod.orcheck([ent], set(codes), ctx.a.or_dir, os.path.join(ctx.a.cache, "or_hits_prior_work.json"))
        best = res.get(0)
        if best and best[0] >= mod.MINCOV:
            rows.append(ctx.row(item, "plaintext", "5-civil-war", f"orcheck:{best[1]}", "LEAD",
                                f"OR rare 3-gram cover {best[0]} in {best[1]} leaf {best[2]} (a ranking, not a verdict)"))
    return rows


# ------------------------------------------------------------------ records, decision, output

def prior_rows(ctx):
    path = os.path.join(ctx.root, ctx.folder, "prior-work.tsv")
    return read_tsv(open(path, encoding="utf-8").read()) if os.path.isfile(path) else []


def apply_records(ctx, rows):
    old = prior_rows(ctx)
    rec = {r["route"]: r for r in old if r.get("check") == "record"}
    for r in rows:
        a = rec.get(r["row_id"])
        if a and r["verdict"] in ("LOOK", "LEAD", "UNCHECKED", "UNCHECKED-NET"):
            r.update(verdict=a["verdict"], evidence=safe(f"recorded {a['utc']}: {a['evidence']}")[:200])
            if a["verdict"] == "DONE":
                r["scope"] = "step"
    for r in rows:      # offline: reuse a still-valid network row for the same route
        if r["verdict"] == "UNCHECKED-NET" and not ctx.net:
            prev = [o for o in old if o.get("item_id") == r["item_id"] and o.get("check") == r["check"]
                    and o.get("route", "").startswith("net:") and o.get("valid_until", "") >= ctx.today.isoformat()]
            if prev:
                r.update(verdict=prev[-1]["verdict"], evidence=safe(f"cached network row {prev[-1]['utc']}: {prev[-1]['evidence']}")[:200])
    return rows


def decide(rows, step, consumer, strict, g3):
    steps = [r for r in rows if r["scope"] == "step"]
    text = [r for r in rows if r["scope"] != "step"]
    if step not in NEVER_DONE and any(r["verdict"] == "DONE" for r in steps):
        return 3, "the step is DONE"
    works = step in WORKS_TEXT or g3
    if works and any(r["verdict"] == "KNOWN" for r in text):
        return (0, f"KNOWN, known-answer work for consumer {consumer}") if consumer else \
               (2, "KNOWN, no consumer (pass --known-answer item:<unread id> or gate:<name>)")
    block = {"LOOK", "LEAD", "UNCHECKED"} | ({"UNCHECKED-NET"} if strict or g3 else set())
    owed = [r for r in steps + (text if works else []) if r["verdict"] in block]
    if owed:
        return 4, "owed first: " + ", ".join(sorted({f"{r['verdict']} {r['row_id']}" for r in owed}))
    residue = sorted({r["residue"] for r in text if r.get("residue")})
    return 0, "proceed on the residue: " + ("; ".join(residue) if residue else "whole item (no KNOWN-PART scope)")


def append_rows(ctx, rows):
    path = os.path.join(ctx.root, ctx.folder, "prior-work.tsv")
    new = not os.path.isfile(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write("# tools/prior_work.py rows, append-only (a search result and a routing verdict, never a novelty class)\n")
            f.write("\t".join(COLUMNS) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in COLUMNS) + "\n")


def write_look(ctx, item_id, look):
    path = os.path.join(ctx.root, ctx.folder, "look.tsv")
    cols = ["item_id", "look_row_id", "role", "folio", "canvas", "image", "source", "status"]
    keep = [r for r in read_tsv(open(path, encoding="utf-8").read())] if os.path.isfile(path) else []
    keep = [[r.get(c, "") for c in cols] for r in keep if r.get("item_id") != item_id]
    with open(path, "w", encoding="utf-8") as f:
        f.write("\t".join(cols) + "\n")
        for r in keep + look:
            f.write("\t".join(map(str, r)) + "\n")


def run_item(ctx, item, step):
    u, rows = item_unit(item), []
    ctx.unit_pages = ctx.leaf_answered = None
    ctx.net = pc.Net(False, ctx.a.max_requests) if ctx.a.network else None       # one budget per item
    if ctx.slug.startswith("eckert-") and (item.get("ptr") or item.get("kind") == "ledger-entry"):
        rows += civil_war(ctx, item, u, step)
    rows += check_own(ctx, item, u, step)
    if ctx.a.reading:
        rows += check_g3(ctx, item, ctx.a.reading)
    else:
        rows += check_portals(ctx, item, u)
        rows += check_editions(ctx, item)
    leaf_rows, look = check_leaf(ctx, item, u, step)
    rows += leaf_rows
    if ctx.net:
        hosts = ";".join(f"{h}:{n}" for h, n in ctx.net.count.items())
        for r in rows:
            r["requests_by_host"] = hosts
    rows = apply_records(ctx, rows)
    code, why = decide(rows, step, ctx.a.known_answer, ctx.a.strict, bool(ctx.a.reading))
    if not ctx.a.dry_run:
        append_rows(ctx, rows)
        if look or os.path.isfile(os.path.join(ctx.root, ctx.folder, "look.tsv")):
            write_look(ctx, item["item_id"], look)
    return code, why, rows


def report(ctx, item, step, code, why, rows):
    if ctx.a.json:
        print(json.dumps(dict(item_id=item["item_id"], step=step, exit=code, why=why, rows=rows), ensure_ascii=False))
        return
    when = ctx.state.when[:16] if ctx.state.when else "working tree"
    desc = "; ".join(f"{k}={item[k]}" for k in ("shelfmark", "folio", "canvas", "decode", "ptr", "wvo", "date") if item.get(k))
    print(f"prior_work {ctx.slug} item {item['item_id']} ({desc or 'no identity fields'}) step {step} @ {ctx.a.ref} "
          f"{ctx.state.commit[:9] or '-'} ({when})")
    for r in rows:
        print(f"  {r['scope']:<9} {r['verdict']:<13} {r['check']:<13} [{r['row_id']}] {r['evidence']}")
    rank = {v: i for i, v in enumerate(("DONE", "KNOWN", "LOOK", "LEAD", "UNCHECKED", "UNCHECKED-NET", "SUBSTANCE",
                                        "KNOWN-PART", "KEY-SOURCE", "CONTEXT", "CLEAR"))}
    for scope in sorted({r["scope"] for r in rows}):
        best = min((r["verdict"] for r in rows if r["scope"] == scope), key=lambda v: rank.get(v, 99))
        print(f"  verdict {scope}: {best}")
    if ctx.a.known_answer and not re.match(r"(item|gate):\S+", ctx.a.known_answer):
        print(f"  warning: consumer {ctx.a.known_answer!r} is not item:<unread id> or gate:<name>")
    print(f"exit {code}: {why}")


# ------------------------------------------------------------------ step modes: register, brief, derive, record

def md_tables(text):
    rows, head = [], None
    for line in text.splitlines():
        if not line.startswith("|"):
            head = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if head is None:
            head = [c.lower() for c in cells]
        elif not set("".join(cells)) <= set("-: "):
            rows.append(dict(zip(head, cells)))
    return rows


OPEN_WORDS = re.compile(r"\bnot yet\b|\bremains?\b|\bpending\b|\bstill (?:to|un)\w*|\bunread\b|\bnot (?:done|run)\b", re.I)
TAG_RE = re.compile(r"\b[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+\b")


def step_part(text):
    """The step a register cell names: the part after its last 'next:' when there is one, parentheticals (history:
    'settled 2 Oct 2026, NEXT-LIN') removed."""
    m = list(re.finditer(r"(?:cheapest\s+)?next(?:\s+step)?\s*:", text, re.I))
    return re.sub(r"\([^)]*(?:\)|$)", " ", text[m[-1].end():] if m else text)


def step_verdict(ctx, slug, text, since):
    """DONE / LEAD / CLEAR for one register row's step text in folder slug (own work only)."""
    st, step = ctx.state, step_part(text)
    k, tags = sm.parse(step), set(TAG_RE.findall(step))
    for r in read_tsv(st.read("WORK-QUEUE.tsv")):
        if r.get("job_id") in tags and str(r.get("status", "")).startswith("done"):
            return "DONE", f"WORK-QUEUE {r['job_id']} {r['status']}"
    kw, u, lead = nsf.keywords(step), sm.Keys(k.vols, k.leaves, k.canvases, k.ids), None
    for fn in ("NOTES.md", "ITERATE.md", "HYPOTHESES.md"):
        for i, line in enumerate(lines_of(st, f"ciphers/{slug}/{fn}"), 1):
            if not DONE_MARK.search(line):
                continue
            hits, share = nsf.overlap(kw, line)
            named = (k.leaves or k.ids) and sm.match(u, line) == "exact"
            if (named or tags & set(TAG_RE.findall(line))) and len(hits) >= 2 and not OPEN_WORDS.search(line):
                return "DONE", f"{fn}:{i} {line.strip()}"
            if len(hits) >= nsf.MIN_HITS and share >= nsf.MIN_SHARE and not lead:
                lead = f"done-candidate {fn}:{i} {line.strip()}"
    for l in lines_of(st, "ROOM.md")[-2000:]:
        m = nsf.ROOM_RE.match(l)
        if m and has_slug(slug, l) and re.search(r"\bdone\b", l) and m.group(1) > since and nsf.is_stale(kw, m.group(3))[0]:
            lead = lead or f"done-candidate ROOM {l}"
    return ("LEAD", lead) if lead else ("CLEAR", "no done evidence for this step at current state")


def run_register(ctx, path, columns):
    text = open(path, encoding="utf-8", errors="replace").read()
    rows = md_tables(text) if path.endswith(".md") else read_tsv(text)
    rel = os.path.relpath(os.path.abspath(path), ctx.root)
    since = (ctx.state._git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d %H:%M", "--", rel) or "").strip() or "0000"
    print("line\tslug\tverdict\tevidence")
    for n, r in enumerate(rows, 2):
        slug = ""
        for c in ("folder", "target", "slug"):
            tok = (re.findall(r"[a-z0-9][a-z0-9-]{3,}", r.get(c, "") or "") or [""])[0]
            if tok and os.path.isdir(os.path.join(ctx.root, "ciphers", tok)):
                slug = tok
                break
        if not slug or (ctx.slug not in ("-", "all") and slug != ctx.slug):
            continue
        step = " ".join(r.get(c, "") or "" for c in columns)
        v, ev = step_verdict(ctx, slug, step, since) if step.strip() else ("UNCHECKED", "empty step cells")
        print(f"{n}\t{slug}\t{v}\t{safe(ev)[:200]}")
    return 0


def brief_items(ctx, text):
    items, vols = [], sorted({v for i in ctx.items for v in sm.volume_keys(i.get("shelfmark", ""))})
    for i in ctx.items:
        if sm.match(item_unit(i), text) == "exact":
            items.append(i)
    if items:
        return items
    for line in text.splitlines():
        k = sm.parse(line)
        lv = sorted(v for v in k.vols if not v.startswith("hint:")) or (vols if len(vols) == 1 else [""])
        for n, side in sorted(k.leaves):
            items.append(item_from_spec(f"shelfmark={lv[0]};folio={n}{side}"))
        for rid in sorted(i for i in k.ids if re.fullmatch(r"R\d+", i)):
            items.append(item_from_spec(f"decode={rid}"))
    seen, out = set(), []
    for i in items:
        if i["item_id"] not in seen:
            seen.add(i["item_id"])
            out.append(i)
    return out


def derive(ctx):
    out, seen = [], set()
    res = json.loads(ctx.state.read("status.json") or "{}").get("results", [])
    for r in res:
        if str(r.get("link", "")).rstrip("/").endswith(f"/ciphers/{ctx.slug}"):
            out.append((r.get("document_id") or r.get("title", ""), "status.json"))
    for i, line in enumerate(lines_of(ctx.state, f"{ctx.folder}/NOTES.md"), 1):
        if line.startswith("#") and sm.parse(line).leaves:
            out.append((line.lstrip("# "), f"NOTES.md:{i}"))
    rows = []
    for text, src in out:
        k = sm.parse(text)
        vol = sorted(v for v in k.vols if not v.startswith("hint:"))
        for n, side in sorted(k.leaves)[:1] or [(None, "")]:
            key = (tuple(vol), n, side)
            if key in seen or (n is None and not k.ids):
                continue
            seen.add(key)
            it = {c: "" for c in ITEM_COLUMNS}
            it.update(item_id=f"d{len(rows) + 1}", shelfmark=(vol or [""])[0], folio=f"{n}{side}" if n else "",
                      decode=next((x for x in sorted(k.ids) if re.fullmatch(r"R\d+", x)), ""), verified="catalogue-only")
            rows.append([it[c] for c in ITEM_COLUMNS] + [src])
    path = os.path.join(ctx.root, ctx.folder, "items.pending.tsv")
    if not ctx.a.dry_run:
        with open(path, "w", encoding="utf-8") as f:
            f.write("# proposed by tools/prior_work.py --derive; every field catalogue-only until one review moves a row to items.tsv\n")
            f.write("\t".join(ITEM_COLUMNS + ["source"]) + "\n")
            for r in rows:
                f.write("\t".join(r) + "\n")
    print(f"derive {ctx.slug}: {len(rows)} proposed row(s) -> {os.path.relpath(path, ctx.root)} (items.tsv untouched)")
    return 0


def record(ctx, rowid, answer):
    v = answer.split(":", 1)[0].strip().upper()
    if v not in ("DONE", "KNOWN", "KNOWN-PART", "CLEAR", "CONTEXT", "KEY-SOURCE", "SUBSTANCE"):
        raise UsageError("--record ANSWER must start with DONE, KNOWN, KNOWN-PART, CLEAR, CONTEXT, KEY-SOURCE or SUBSTANCE and a colon")
    prev = [r for r in prior_rows(ctx) if r.get("row_id") == rowid]
    if not prev:
        raise UsageError(f"row id {rowid} is not in {ctx.folder}/prior-work.tsv")
    item = {"item_id": prev[-1]["item_id"]}
    r = ctx.row(item, prev[-1]["scope"], "record", rowid, v, answer.split(":", 1)[-1].strip())
    r["route"], r["valid_until"] = rowid, ""
    append_rows(ctx, [r])
    print(f"recorded {v} for {rowid} in {ctx.folder}/prior-work.tsv")
    return 0


def main(argv=None):
    ap = Parser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="ciphers/<slug> folder name ('-' with --register for every row)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--item", help="item_id, a row of ciphers/<slug>/items.tsv")
    g.add_argument("--item-spec", help="ad hoc item: 'shelfmark=..;folio=..;canvas=..;date=..;sender=..;recipient=..;decode=R..;ptr=..;kind=..'")
    g.add_argument("--derive", action="store_true", help="propose items.pending.tsv rows (catalogue-only), never items.tsv")
    g.add_argument("--register", metavar="FILE", help="step mode: NEXT-STEPS.tsv, SIBLINGS-*.tsv or LOOSE-ENDS-*.md")
    g.add_argument("--brief", metavar="FILE", help="extract the items a brief names and check each")
    g.add_argument("--record", nargs=2, metavar=("ROWID", "ANSWER"), help="answer an owed LOOK/LEAD/UNCHECKED row")
    ap.add_argument("--columns", default="next_step,parallel", help="register columns holding the step text")
    ap.add_argument("--step-type", default="read", choices=STEP_TYPES,
                    help="the job's step (default read); audit refuses a same-families re-audit; the last three are never DONE")
    m = ap.add_mutually_exclusive_group()
    m.add_argument("--offline", action="store_true", help="the default: no network at all")
    m.add_argument("--network", action="store_true", help="add check 4's network routes (print_check as a library)")
    ap.add_argument("--reading", metavar="FILE", help="G3: re-search the editions with the decoded phrases")
    ap.add_argument("--known-answer", metavar="CONSUMER", help="lowers exit 2 to 0: item:<unread id> or gate:<name>")
    ap.add_argument("--strict", action="store_true", help="UNCHECKED-NET blocks (it always does at G3)")
    ap.add_argument("--me", help="your own ROOM.md tag: your claims are not someone else's live work")
    ap.add_argument("--clone", action="append", default=[], help="a local solver-repository clone to search (repeatable)")
    ap.add_argument("--or-dir", help="civil-war adapter: a folder of OR _djvu.txt files for entries_mssEC19.orcheck()")
    ap.add_argument("--cache", default=os.path.join(tempfile.gettempdir(), "cipher-lab-prior-work"),
                    help="network downloads go here, never into the repository")
    ap.add_argument("--max-requests", type=int, default=12, help="network requests per item (default 12)")
    ap.add_argument("--fetch", action="store_true", help="git fetch origin main first (network)")
    ap.add_argument("--json", action="store_true", help="one JSON object per item (exit, why, rows)")
    ap.add_argument("--dry-run", action="store_true", help="write nothing (no prior-work.tsv, look.tsv or pending file)")
    ap.add_argument("--root", default=ROOT, help="repository root (default: this checkout; tests pass a fixture repo)")
    ap.add_argument("--ref", default="origin/main", help="ref the target state is read at; WORKTREE reads the checkout itself")
    ap.add_argument("--now", help="fixed UTC clock YYYY-MM-DDTHH:MM for the ROOM claim age (tests)")
    a = ap.parse_args(argv)
    a.slug = a.slug.rstrip("/").removeprefix("ciphers/")
    if a.fetch or a.network:
        subprocess.run(["git", "-C", a.root, "fetch", "-q", "origin", "main"], capture_output=True, timeout=300)
    state = State(a.root, a.ref)
    ctx = Ctx(a, state)
    try:
        if a.register:
            return run_register(ctx, a.register, [c.strip() for c in a.columns.split(",") if c.strip()])
        if a.slug in ("-", "all") or not os.path.isdir(os.path.join(a.root, ctx.folder)) and not state.ls(ctx.folder):
            raise UsageError(f"no folder ciphers/{a.slug}")
        if a.record:
            return record(ctx, *a.record)
        if a.derive:
            return derive(ctx)
        if a.brief:
            text = open(a.brief, encoding="utf-8", errors="replace").read()
            rel = os.path.relpath(os.path.abspath(a.brief), a.root)
            ran = [r for r in read_tsv(state.read("WORK-QUEUE.tsv")) if r.get("brief") == rel
                   and str(r.get("status", "")).startswith("done")]
            if ran and a.step_type not in NEVER_DONE:
                print(f"prior_work {a.slug}: this brief already ran: WORK-QUEUE {ran[-1].get('job_id')} {ran[-1].get('status')}")
                print("exit 3: the step is DONE (a re-queued brief)")
                return 3
            items = brief_items(ctx, text)
            if not items:
                print(f"prior_work {a.slug}: the brief names no item key (volume+folio, R-id, pointer); nothing checked")
                return 0
        elif a.item:
            items = [i for i in ctx.items if i.get("item_id") == a.item]
            if not items:
                raise UsageError(f"item {a.item!r} is not a row of ciphers/{a.slug}/items.tsv (use --item-spec or --derive)")
        else:
            items = [item_from_spec(a.item_spec)]
    except UsageError as e:
        print(f"prior_work.py: error: {e}", file=sys.stderr)
        return 1
    codes = []
    for item in items:
        code, why, rows = run_item(ctx, item, a.step_type)
        report(ctx, item, a.step_type, code, why, rows)
        codes.append(code)
    for c in (3, 2, 4):
        if c in codes:
            return c
    return 0


if __name__ == "__main__":
    sys.exit(main())

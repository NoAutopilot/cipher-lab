#!/usr/bin/env python3
"""Split every target folder (ciphers/*) into HOT (a key source is on disk for it, or for a sign-pool member) and
COLD (nothing to read it from but cryptanalysis), and write HOT-COLD.tsv.

    python3 tools/hot_cold.py [--root DIR] [--out FILE] [--check] [--folder NAME]

Built 5 Oct 2026 (LANE-SYS1 job 2, SYS1-HC) so a default lane can take HOT rows first (`next_steps.py --hot-only`,
`.claude/briefs/default-lane.md`): every reading on the board so far came from a key source or a pool of siblings
(CLAUDE.md pipeline 3, pools first).

HOT kinds (one per row, strongest first; the evidence cell names file + phrase, up to two items):
  key            a period or published key: NOTES.md status `found-solved` (someone else's decipherment of this very
                 item is published); PROGRESS.tsv ksrc p/b; an AUDIT.md "Key (source):" line reading `period`
                 or `published`; status.json `key` period/published; a key*.tsv whose provenance header names a
                 published/period key or reconstruction (Tomokiyo, Aymeloglu, Bourdeau, period key sheet) or whose
                 grade column carries >= 3 H rows (rule 4: H = read from a key source); a key file named
                 key_period / key_tomokiyo / key_published / key_brienne_*; an affirmative NOTES.md sentence
                 ("Key source: period", "read with the period key", "Tomokiyo's key").
  decipherment   a period/contemporary decipherment or deciphered copy (key.tsv source column, AUDIT key line or
                 affirmative NOTES.md sentence).
  gloss          an interlinear or marginal gloss (key.tsv source column / >= 3 C rows sourced from a gloss,
                 key_gloss.tsv, or affirmative NOTES.md sentence).
  clear          a clear copy / plain-text twin (key.tsv >= 3 C rows not sourced from a gloss; NOTES.md sentence).
  pool:<member>  no direct evidence, but the folder's NOTES.md names a HOT folder in the same sentence as a pool word
                 (same key/cipher/office/nomenclator/code/system, sign pool, key family, sibling key/cipher, shares the
                 key) in an affirmative sentence (no negator or hedge anywhere in it, no question mark). A sentence that
                 only names a sibling's key file being *tried* is not a pool link (trials usually fail). Also any
                 POOLS.tsv group whose shelfmarks_arks cell names >= 2 target folders, one of them HOT.

What it catches: folders with a key source recorded only in a structured file (key.tsv grades, AUDIT key line,
PROGRESS ksrc) as well as those that say so in prose.

What it must NOT count (each has a test in tools/tests/test_hot_cold.py):
  - a bare mention of "key" in prose ("no key survives", "the key is lost", "look for a key", "if a period key
    exists", "no clear copy or slip", "none is a decipherment") -- negated, hedged or searching sentences are dropped;
  - an `ours` key (AUDIT "Key: ours", ksrc o, a key.tsv graded only S/M/I from an anneal): cryptanalysis is not a
    key source, so a folder with only that is COLD;
  - a key.tsv header that merely uses a published *numbering* ("Working key for Tomokiyo's sign numbers, recovered by
    crib-matching") without calling the key itself published/reconstructed;
  - a pool link to a folder that is itself COLD, or a mention of another folder with no pool word in the sentence.
The NOTES.md matcher is conservative by design: a HOT that only prose supports is listed with that sentence so a
spot-check can overturn it; COLD means "no evidence found on disk", not "no key exists".

--check exits 1 when HOT-COLD.tsv differs from what the folders on disk give now. Offline; reads files only.
Test: tools/tests/test_hot_cold.py. Does not touch any NOTES.md status line.
"""
import argparse
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
HEADER = ("# HOT-COLD.tsv -- built by tools/hot_cold.py (do not edit by hand; rerun it, --check for staleness). HOT = a key "
          "source on disk (period/published key, clear copy, period decipherment, gloss) or a sign-pool member with one; "
          "COLD = none found. kind: key|decipherment|gloss|clear|pool:<member>. evidence: file: phrase.\n")
COLUMNS = ["folder", "hot_cold", "kind", "evidence", "pool"]
KIND_ORDER = ["key", "decipherment", "gloss", "clear"]

NEG = re.compile(r"\b(no(?!\.\s*\d)|not|none|nor|neither|without|lacks?|lacking|absent|never|missing|lost|any|whether|if|unless|"
                 r"may|might|could|would|possibl[ey]|perhaps|probabl[ey]|likely|suspected|candidate|uncertain|"
                 r"unconfirmed|unclear|hypothes\w*|look(?:ing|ed)? for|search\w*|quer\w*|grep\w*|snippet\w*|hunt\w*|seek\w*|"
                 r"request\w*|ask\w*|order\w*|wait\w*|pending|until|once|unknown|unread|cannot|can't|isn't|wasn't|"
                 r"didn't|doesn't|nothing|fails?|failed|zero|0|need\w*|requir\w*|route|expect\w*|hope\w*|fetch\w*|find\w*|will|when|later|for an?|or|blocker)\b", re.I)
POST_NEG = re.compile(r"^[^.;]{0,40}\b(not found|not located|is not|was not|are not|were not|absent|missing|none|"
                      r"unlocated|unknown|wrong|does not survive|lost|likely|may|might|probably|would|could|will|exists? in the|not applicable|not run)\b", re.I)

NAMES = "tomokiyo|lasry|bourdeau|aymeloglu|bergenroth|cryptiana"
NOTE_PATTERNS = [
    ("key", re.compile(r"\bkey source:?\s*\**`?\s*(period|published)\b", re.I)),
    ("key", re.compile(r"\b(?:read|reads|decoded|decodes|applied|applies|applying|rebuilt|reconstructed|opens|opened)"
                       r"\b[^.;]{0,40}\b(?:period|published|printed|contemporary|tomokiyo's|bourdeau's|aymeloglu's) "
                       r"(?:key|cipher table|key sheet|key book)\b", re.I)),
    ("key", re.compile(r"\b(?:tomokiyo|bourdeau|aymeloglu|lasry)'s (?:published )?(?:key|reconstruction)\b(?![- ]numbering|-)",
                       re.I)),
    ("key", re.compile(r"^\W*key(?: source)?\**\s*[:.]\**\s[^.;]{0,100}\b(?:%s|period key|published|printed key|"
                       r"reconstruct\w*)" % NAMES, re.I)),
    ("key", re.compile(r"\b(?:%s)\b[^.;]{0,60}\breconstruct\w*|\breconstruct\w*\b[^.;]{0,40}\b(?:%s)\b" % (NAMES, NAMES),
                       re.I)),
    ("key", re.compile(r"\bkey (?:is |was |has been )?(?:published|printed)\b|\b(?:tagged|attached) \[key\]|\bkey \((?:%s)'s\)" % NAMES, re.I)),
    ("key", re.compile(r"\bkey\b[^.;]{0,30}\b(?:transcribed|reconstructed|rebuilt|printed|published)\b[^.;]{0,20}\bby\b"
                       r"[^.;]{0,30}\b(?:%s)\b" % NAMES, re.I)),
    # a located period key with its shelfmark: "the key (BnF fr.3642) is not on Gallica" -- the trailing negative is
    # about access, not existence, so this pattern skips the post-match check (see SKIP_POST)
    ("key", re.compile(r"\b(?:the|its|a period) key \((?:BnF|BL|TNA|SP|Add|fr\.|Clair|NA|ANTT|AGS|Simancas|HStA|"
                       r"RA|ASV|BAV)[^)]{0,40}\)", re.I)),
    ("decipherment", re.compile(r"\b(?:images?|pages?|copy|copies) of the decipherment\b|\bdeciphered on separate pages\b",
                                re.I)),
    ("decipherment", re.compile(r"\b(?:period|contemporary|interlinear)[- ]decipherments?\b(?! (?:was|is) (?:not|never))",
                                re.I)),
    ("decipherment", re.compile(r"\bdeciphered copy\b", re.I)),
    ("gloss", re.compile(r"\b(?:interlinear|marginal|period|contemporary) gloss(?:es)?\b", re.I)),
    ("clear", re.compile(r"\b(?:clear copy|plain[- ]?text (?:copy|twin)|en clair copy)\b", re.I)),
]
POOL_WORDS = re.compile(r"\b(same (?:key|cipher|office|nomenclator|code|key family|cipher family|system)\b|sign pool|"
                        r"key family|sibling(?:'s)? (?:key|cipher)|shares? (?:the|its|a) (?:key|cipher))", re.I)


# a sentence that opens negatively ("No decipherment ...", "Nothing in second-opinions/ names a ...") stays negative
LEAD_NEG = re.compile(r"^\W*(?:no(?!\.\s*\d)|none|nothing|neither|not found|not located|result first: \W*not found)\b", re.I)
# a sentence about our own cryptanalytic key is not a key source even if it names a published numbering
SELF_KEY = re.compile(r"\b(anneal\w*|crib-match\w*|hill-climb\w*|recovered by (?:us|lane|this project)|key: ours|"
                      r"key source:?\W*ours)\b", re.I)


def read(path):
    try:
        with open(path, encoding="utf-8", errors="replace") as f:
            return f.read()
    except OSError:
        return ""


def sentences(text):
    """Split prose into sentence-ish units (on '. ', ';', blank line, bullet/newline)."""
    text = re.sub(r"`", "", text)
    text = re.sub(r"~~.*?~~", " ", text, flags=re.S)  # struck-through (retracted) text is not evidence
    parts = re.split(r"(?<=[.;!?])\s+|\n\s*\n|\n\s*[-*|] |\n#+ ", text)
    return [p.strip().replace("\n", " ") for p in parts if p and p.strip()]


SKIP_POST = {i for i, (_, p) in enumerate(NOTE_PATTERNS) if p.pattern.startswith(r"\b(?:the|its|a period) key \(")}


def affirmative(sent, start, end, check_post=True):
    """True if the match at sent[start:end] is not negated, hedged, a question or a search instruction.

    The 60 chars before the match (and the match itself) are checked across commas and colons, not just the clause:
    list negations ("no decipherment, gloss or clear copy", "Not found: a key, a decipherment, a clear copy") put the
    negator several items back; a negator further away ("not merely ... -- it already has a published reconstruction")
    belongs to another clause."""
    pre = sent[max(0, start - 60):end]
    if NEG.search(pre) or LEAD_NEG.match(sent):
        return False
    post = sent[end:end + 60]
    if SELF_KEY.search(sent):
        return False
    if check_post and (POST_NEG.search(post) or "?" in post[:40]):
        return False
    return True


def notes_evidence(text):
    """[(kind, phrase)] from affirmative NOTES.md sentences."""
    out = []
    sents = sentences(text)
    for j, s in enumerate(sents):
        # "...: a clear copy of letters that X sent. It is not a decipherment of ..." -- the next sentence retracts it
        retracted = j + 1 < len(sents) and re.match(r"^(?:it|this|that|which) (?:is|was) not\b", sents[j + 1], re.I)
        for i, (kind, pat) in enumerate(NOTE_PATTERNS):
            if retracted:
                break
            for m in pat.finditer(s):
                if affirmative(s, m.start(), m.end(), check_post=i not in SKIP_POST):
                    a = max(0, m.start() - 50)
                    out.append((kind, s[a:m.end() + 50].strip()))
                    break
    return out


def tsv_rows(path):
    lines = [l.rstrip("\n") for l in read(path).splitlines()]
    comments = [l for l in lines if l.startswith("#")]
    body = [l.split("\t") for l in lines if l.strip() and not l.startswith("#")]
    return comments, body


KEYFILE_NAME = re.compile(r"key_(period|tomokiyo|published|brienne|gloss)", re.I)
HDR_KEY = re.compile(r"(published key|period key|key sheet|\breconstruct(?:ed|ion)\b[^.]{0,40}\b(tomokiyo|aymeloglu|"
                     r"bourdeau|lasry)|(tomokiyo|aymeloglu|bourdeau|lasry)'s (key|reconstruction|key\.json)|"
                     r"aymeloglu's key|cryptiana|credited|bergenroth|\breconstruction\b|key source)", re.I)
HDR_GLOSS = re.compile(r"(interlinear|gloss|decipherer|decipherment)", re.I)
SRC_GLOSS = re.compile(r"(gloss|interlinear)", re.I)
SRC_DECIPH = re.compile(r"(decipherment|aligned|deciphered)", re.I)
SRC_KEY = re.compile(r"(published|period|tomokiyo|key ?\d|key sheet|bourdeau|aymeloglu|hcportal key|lasry|krauske)", re.I)


def keyfile_evidence(folder_dir, folder):
    out = []
    paths = sorted(set(glob.glob(os.path.join(folder_dir, "key*.tsv")) + glob.glob(os.path.join(folder_dir, "keys", "*.tsv"))
                     + glob.glob(os.path.join(folder_dir, "key", "*.tsv"))))
    for p in paths:
        rel = os.path.relpath(p, os.path.dirname(os.path.dirname(folder_dir)))
        base = os.path.basename(p)
        if base.startswith(("key_conflicts", "keytrial", "keysource")):
            continue
        m = KEYFILE_NAME.search(base)
        if m:
            out.append(("gloss" if m.group(1).lower() == "gloss" else "key", f"{rel}: file name {base}"))
            continue
        comments, body = tsv_rows(p)
        hdr = " ".join(comments[:6])
        if hdr and not SELF_KEY.search(hdr) and not re.search(r"best-scoring|not a reading", hdr, re.I):
            mk = HDR_KEY.search(hdr)
            if mk:
                out.append(("key", f"{rel}: header '{mk.group(0)}'"))
                continue
            mg = HDR_GLOSS.search(hdr)
            if mg and re.search(r"(contemporary|period|interlinear|leaf's own|own interlinear)", hdr, re.I):
                out.append(("gloss", f"{rel}: header '{mg.group(0)}'"))
                continue
        if not body:
            continue
        h = [x.strip().lower() for x in body[0]]
        if "grade" not in h:
            continue
        gi = h.index("grade")
        si = h.index("source") if "source" in h else None
        nH = nC = 0
        srcs = []
        for r in body[1:]:
            if len(r) <= gi:
                continue
            g = r[gi].strip()[:1]
            if g == "H":
                nH += 1
            elif g == "C":
                nC += 1
            else:
                continue
            if si is not None and len(r) > si:
                srcs.append(r[si])
        srctext = " ".join(srcs)
        if nH >= 3:
            sm = SRC_KEY.search(srctext)
            out.append(("key", f"{rel}: {nH} H-graded rows" + (f" (source '{sm.group(0)}')" if sm else "")))
        elif nC >= 3:
            if SRC_GLOSS.search(srctext):
                out.append(("gloss", f"{rel}: {nC} C-graded rows (source '{SRC_GLOSS.search(srctext).group(0)}')"))
            elif SRC_DECIPH.search(srctext):
                out.append(("decipherment", f"{rel}: {nC} C-graded rows (source '{SRC_DECIPH.search(srctext).group(0)}')"))
            else:
                out.append(("clear", f"{rel}: {nC} C-graded rows (known plaintext)"))
    return out


AUDIT_KEY = re.compile(r"\bkey(?: source)?\**\s*:\s*\**\s*`?\s*\**(period|published|ours)\b", re.I)


def audit_evidence(text):
    out = []
    for m in AUDIT_KEY.finditer(text):
        v = m.group(1).lower()
        if v == "ours":
            continue
        ctx = text[m.start():m.end() + 100].replace("\n", " ")
        kind = "key"
        if re.search(r"interlinear|gloss", ctx, re.I):
            kind = "gloss"
        elif re.search(r"decipherment", ctx, re.I):
            kind = "decipherment"
        out.append((kind, f"AUDIT.md: '{ctx[:90].strip()}'"))
    return out


def progress_ksrc(root):
    comments, body = tsv_rows(os.path.join(root, "PROGRESS.tsv"))
    res = {}
    if not body:
        return res
    h = [x.strip() for x in body[0]]
    if "folder" not in h or "ksrc" not in h:
        return res
    fi, ki = h.index("folder"), h.index("ksrc")
    for r in body[1:]:
        if len(r) > max(fi, ki):
            ks = r[ki].strip()
            if "p" in ks or "b" in ks:
                res.setdefault(r[fi].strip(), []).append(ks)
    return res


def status_keys(root):
    res = {}
    try:
        d = json.load(open(os.path.join(root, "status.json"), encoding="utf-8"))
    except (OSError, ValueError):
        return res
    for t in d.get("targets", []):
        k = t.get("key")
        if isinstance(k, str) and k.lower() in ("period", "published"):
            res[os.path.basename(t.get("folder", "").rstrip("/"))] = k.lower()
    return res


def target_folders(ciphers_dir):
    out = []
    for d in sorted(os.listdir(ciphers_dir)):
        p = os.path.join(ciphers_dir, d)
        if d.startswith(("_", ".")) or not os.path.isdir(p):
            continue
        if not os.path.exists(os.path.join(p, "NOTES.md")):
            continue
        out.append(d)
    return out


def direct_evidence(root, folder, ksrc=None, skeys=None):
    """Sorted [(kind, evidence)] for one folder, structured sources first."""
    fdir = os.path.join(root, "ciphers", folder)
    ev = []
    for ks in (ksrc or {}).get(folder, []):
        ev.append(("key", f"PROGRESS.tsv: ksrc {ks}"))
    if skeys and folder in skeys:
        ev.append(("key", f"status.json: key {skeys[folder]}"))
    notes = read(os.path.join(fdir, "NOTES.md"))
    st = status_word(notes)
    if st == "found-solved":
        ev.append(("key", "NOTES.md: status found-solved (a published decipherment of this item exists)"))
    ev += audit_evidence(read(os.path.join(fdir, "AUDIT.md")))
    ev += keyfile_evidence(fdir, folder)
    ev += [(k, f"NOTES.md: '{p[:110]}'") for k, p in notes_evidence(notes)]
    seen, out = set(), []
    for k, e in ev:
        if e not in seen:
            seen.add(e)
            out.append((k, e))
    return out


def status_word(notes_text):
    """Rule-5 status word of a NOTES.md (next_steps.py's own parser, so the two tools never disagree)."""
    try:
        import next_steps
        return next_steps.first_status_word(notes_text) or ""
    except Exception:  # noqa: BLE001 -- a parser failure leaves the status unknown, never crashes the split
        return ""


def pool_links(notes_text, folder, hot_set):
    """HOT members named in a pool sentence (or whose key file is applied) in this folder's NOTES.md."""
    found = []
    others = sorted(hot_set - {folder}, key=len, reverse=True)
    if not others:
        return found
    name_re = re.compile(r"(?<![\w-])(" + "|".join(re.escape(o) for o in others) + r")(?![\w-])")
    for s in sentences(notes_text):
        names = name_re.findall(s)
        if not names:
            continue
        pw = POOL_WORDS.search(s)
        if not pw or "?" in s or NEG.search(s) or re.search(r"\b(different|unlike|only)\b", s, re.I):
            continue
        found.append((names[0], s[:110]))
    return found


def pools_tsv(root, folders):
    """{folder: set(co-members)} from POOLS.tsv rows whose shelfmarks_arks cell names >= 2 target folders."""
    _, body = tsv_rows(os.path.join(root, "POOLS.tsv"))
    res = {}
    if not body or "shelfmarks_arks" not in body[0]:
        return res
    ci = body[0].index("shelfmarks_arks")
    fs = set(folders)
    for r in body[1:]:
        if len(r) <= ci:
            continue
        members = {x for x in re.split(r"[;,\s]+", r[ci]) if x in fs}
        if len(members) >= 2:
            for m in members:
                res.setdefault(m, set()).update(members - {m})
    return res


def classify(root):
    ciphers_dir = os.path.join(root, "ciphers")
    folders = target_folders(ciphers_dir)
    ksrc, skeys = progress_ksrc(root), status_keys(root)
    direct = {f: direct_evidence(root, f, ksrc, skeys) for f in folders}
    hot = {f for f, ev in direct.items() if ev}
    ptsv = pools_tsv(root, folders)
    rows = []
    for f in folders:
        ev = direct[f]
        if ev:
            ev.sort(key=lambda kv: KIND_ORDER.index(kv[0]))
            kind = ev[0][0]
            evid = " ; ".join(e for _, e in ev[:2])
            links = pool_links(read(os.path.join(ciphers_dir, f, "NOTES.md")), f, hot)
            pool = ",".join(sorted({m for m, _ in links} | (ptsv.get(f, set()) & hot)))
            rows.append({"folder": f, "hot_cold": "HOT", "kind": kind, "evidence": evid, "pool": pool})
            continue
        links = pool_links(read(os.path.join(ciphers_dir, f, "NOTES.md")), f, hot)
        links += [(m, "POOLS.tsv: same group") for m in sorted(ptsv.get(f, set()) & hot)]
        if links:
            m, s = links[0]
            evid = s if s.startswith("POOLS.tsv") else f"NOTES.md: '{s}'"
            rows.append({"folder": f, "hot_cold": "HOT", "kind": f"pool:{m}", "evidence": evid,
                         "pool": ",".join(sorted({x for x, _ in links}))})
        else:
            rows.append({"folder": f, "hot_cold": "COLD", "kind": "", "evidence": "", "pool": ""})
    return rows


def clean(s):
    return re.sub(r"\s+", " ", s.replace("\t", " ")).strip()


def render(rows):
    out = [HEADER, "\t".join(COLUMNS) + "\n"]
    for r in rows:
        out.append("\t".join(clean(r[c]) for c in COLUMNS) + "\n")
    return "".join(out)


def load_hot(path):
    """Set of HOT folder names from an existing HOT-COLD.tsv (used by next_steps.py --hot-only)."""
    _, body = tsv_rows(path)
    if not body:
        return set()
    h = body[0]
    fi, hi = h.index("folder"), h.index("hot_cold")
    return {r[fi] for r in body[1:] if len(r) > hi and r[hi] == "HOT"}


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--root", default=ROOT)
    ap.add_argument("--out", default=None, help="default <root>/HOT-COLD.tsv")
    ap.add_argument("--check", action="store_true", help="exit 1 if --out is stale")
    ap.add_argument("--folder", help="print one folder's evidence and exit (debug)")
    args = ap.parse_args()
    out = args.out or os.path.join(args.root, "HOT-COLD.tsv")
    if args.folder:
        ev = direct_evidence(args.root, args.folder, progress_ksrc(args.root), status_keys(args.root))
        for k, e in ev:
            print(f"{k}\t{e}")
        print(f"{len(ev)} direct evidence item(s)")
        return 0
    rows = classify(args.root)
    fresh = render(rows)
    nh = sum(r["hot_cold"] == "HOT" for r in rows)
    summary = f"HOT {nh} / COLD {len(rows) - nh} / total {len(rows)}"
    if args.check:
        if read(out) != fresh:
            print(f"STALE: {out} differs from the folders on disk ({summary}); rerun without --check.")
            return 1
        print(f"OK: {out} is current ({summary})")
        return 0
    with open(out, "w", encoding="utf-8") as f:
        f.write(fresh)
    print(f"wrote {out}: {summary}")
    return 0


if __name__ == "__main__":
    sys.exit(main())

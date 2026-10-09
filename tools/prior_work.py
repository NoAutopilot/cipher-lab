#!/usr/bin/env python3
"""prior_work.py: has this item, or this step, already been read or done -- by us, its clerk, its holder, a portal, a
solver repository or a printed edition? The per-item prior-work gate, v1 (PRIOR-WORK v1, 8 Oct 2026; review fixes 8 Oct).

  prior_work.py <slug> --item ID [--step-type read] [--known-answer item:<id>|gate:<name>] [--network] [--fetch]
  prior_work.py <slug> --item-spec 'shelfmark=BnF fr.3040;folio=18r;date=1530-03-28;sender=Gramont;recipient=Montmorency'
  prior_work.py <slug> --item ID --reading reading.txt --network      G3: after decode, before any class or SO row
  prior_work.py <slug> --brief .claude/briefs/runs/<brief>.md         every item the brief names (per-item exit table)
  prior_work.py -      --register NEXT-STEPS.tsv      (also SIBLINGS-*.tsv, LOOSE-ENDS-*.md; step columns autodetected)
  prior_work.py <slug> --record ROWID 'CLEAR: f.18r, f.17v, f.19r read at native size, no gloss'
  prior_work.py <slug> --derive        propose ciphers/<slug>/items.pending.tsv (catalogue-only; never writes items.tsv)

Why: research/PRIOR-WORK-LEAK-2026-10-08.md found 310 records of work spent on items already read (143 plaintext in
print, 72 a period gloss or clear copy on the leaf or a sibling, 49 our own earlier work, 19 the holder's transcription,
14 a modern decipherment; about USD 1,600), two thirds catchable by a script before reading (owner, 8 Oct 2026: "must be
applicable to other work not just Eckert"). This is that script cut to v1; .claude/briefs/prior-work-step.md is the hand
checklist for what it does not reach.

Items: ciphers/<slug>/items.tsv (item_id, shelfmark, folio, canvas, decode, ptr, wvo, date YYYY-MM-DD, calendar os|ns,
sender, recipient, office, place, language, kind, holder_url, clear_words, verified) or --item-spec with those keys. A unit
is volume + folio + canvas, never the folio alone, and a folio is bound to the volume named nearest it in its clause
(tools/shelfmark.py). Target state is read at origin/main with git (--fetch runs `git fetch origin main` before reading, the
only network call outside --network; an items.tsv not yet pushed needs --ref WORKTREE); a ref that does not resolve makes own
work UNCHECKED and the report says the working tree was read instead. Caches (sources/, djvu texts) and the gate's own
prior-work.tsv / look.tsv are read from disk. Paths under any restricted/ folder and the private repository are never
read: every path given on the command line (--reading, --brief, --register, --clone, --root, --or-dir, --cache) is
refused when it has a `restricted` component or sits in a git checkout whose remote names cipher-lab-private; for a
folder with a RESTRICTED.md, --reading with --network is refused and decoded phrases are written only as hashes.

Step types: read, transcribe, decode, crop (work the text: the leaf look applies, KNOWN stops without a consumer); key,
align (KNOWN text is their input: exit 0 on KNOWN); lookup; audit (DONE when an AUDIT.md/status.json class already
covers this item -- a re-audit); never DONE: second-audit (the second adversarial audit, Outreach gate 2 / VERIFY-BACKLOG
Audit 2), upgrade-audit (a class upgrade), new-family-audit (new source families), propagate-revision (rule 10's
propagation of a revised reading).

Checks (scope step = the job itself; scope plaintext = the item's text):
 1 own work, always (step): DONE only from typed evidence for the same unit and step -- a [x] / [done / [already run /
   [retired] marker heading a NOTES/ITERATE/HYPOTHESES bullet that names the unit and the step's verb (a whole word in
   the bullet's done part: after the marker, before 'next'/'then'/'later'; a fetch / crop / image-check marker is never
   DONE for read, decode or transcribe) and does not say part is still open; a WORK-QUEUE.tsv done row naming slug and
   unit; for crop, a crop file or an images/manifest.json crop entry for the leaf or canvas; for --step-type audit, an
   AUDIT.md/status.json class for this item; for read/decode on Eckert ledgers, an already-read block for the same
   pointer and entry. A marker for another step, an unnamed volume in a multi-volume folder, prose naming the unit with
   a completion word, or (for a unit with no folio) a line naming its volume and date is LEAD done-candidate; a ROOM
   claim under 6 h with no later done line from the same tag (whole-token role tag), naming slug and unit -- or naming
   the slug and no unit at all (a target-level claim) -- is LEAD live-claim (--me TAG skips yours). An AUDIT class is
   attributed only from the row's own leading cell or bold label, or a section heading naming exactly this unit (a folder
   with one derived item excepted); a class of already-known text or PROGRESS.tsv txt=k is KNOWN, an audited reading of
   ours or PROGRESS R=x is LEAD done-candidate.
 2 leaf and neighbours (read/transcribe/decode/crop): look.tsv lists the cipher page, facing page, two before and four
   after (images/manifest.json, else folio/canvas/pointer arithmetic) and every image of a unit of <= 8. LOOK until
   --record answers it or a NOTES/AUDIT paragraph already records the gloss check for this leaf. Paragraphs (hard-wrapped
   lines joined) are split into clauses; a clause counts for this unit when it names the unit, or sits under a label
   (bold lead, a table row's leading cell, the opening clause) naming it and names no other unit. Our own depth lines (D0-D4, outward
   wording) and modal or hypothetical clauses ('likely', 'not excluded', 'may', 'would', 'if') are no evidence. A gloss
   for THIS letter is KNOWN, a partial one KNOWN-PART, checked-and-none CLEAR, a gloss of another letter CONTEXT; the
   strongest wins (KNOWN > KNOWN-PART > CONTEXT > CLEAR) and a disagreement is named in the evidence. An unattributed
   gloss on a neighbouring leaf is KEY-SOURCE (nearby sheet); catalogue notes are check 3's.
 3 holder, portal and solver caches (tools/data/prior_portals.tsv, last row per portal id wins): Tomokiyo (volume +
   exact folio with 'deciphered' / 'attached' / 'dechiffre' = KNOWN; folio within 2 = LEAD fuzzy-match; 'can be read
   with' = KEY-SOURCE; 'undeciphered' = no evidence; a volume-level line naming no folio = KEY-SOURCE or CONTEXT; the
   item's date with a correspondent's name = LEAD date-match); DECODE listings ('Partially decrypted' = KNOWN-PART;
   'Decrypted' = LEAD, it may be a key only; 'Non-decrypted' = CONTEXT, a status is evidence of nothing; a cached record
   page with a cleartext document = LEAD); solver caches and --clone dirs, matched line by line (a reading file naming
   the unit, not citing cipher-lab and not later than ours = KNOWN; any other mention CONTEXT duplicate-effort-risk; a
   solver folder named for this target = CONTEXT, LEAD when it holds reading files and the unit has no folio); a
   registry solver repository with no cache and no --clone is UNCHECKED; holder notes quoted in NOTES/sources naming the
   unit with decipherment wording = LEAD. Sentences are classed with a negation lexicon ('no separate dechiffrement',
   'no interlinear gloss on the leaf', 'sans le dechiffrement', 'Non-decrypted') and a partial lexicon ('gedeeltelijk',
   'en partie'). A unit with no folio, R-id or pointer makes the folio-keyed checks UNCHECKED, never CLEAR.
 3a active editions (MQS-SCOUT, 9 Oct 2026): `active-edition` rows of prior_portals.tsv (the Mary Stuart - Castelnau corpus, Lasry's
   second Mary collection) match the item's shelfmark list or keyword regex = LEAD 'active project, contact before work' (the word 'first' is masked by rule 10) with the contact
   route (never KNOWN or CLEAR); scope and tests in check_active_edition's docstring.
 4 editions (tools/data/prior_editions.tsv, matched by slug glob, year span and correspondents): cached djvu text is
   searched for the date +-1 day (Old and New Style both ways in 1582-1752 unless `calendar` says) with name tokens of
   both correspondents in one window = LEAD edition-hit, with the hit count at +-30 days beside it (KNOWN only by --record
   after someone opens the page; a calendar printing only the clear part is recorded KNOWN-PART). Each row's positive
   control runs in the same pass: a missed or missing control is UNCHECKED, never CLEAR; a volume not on disk, a row with
   no IA route or no matching row at all (core-only) is UNCHECKED-NET (offline, one row naming every volume not on
   disk, reused from cached network rows only when every one of those routes has one). --network downloads the djvu
   through print_check.Net into --cache (outside the repository) and adds one OpenAlex identity query with a host control.
 5 civil-war adapter (eckert-* slugs with a pointer): reuses ciphers/eckert-1864/entries_mssEC19.py (load_vocab,
   segment, toks, day_month; orcheck with --or-dir). The holder's own transcription of the pointer ('transc' or 'text'):
   the entry is chosen by ptr P/N, else by a date only one entry on the page carries (several = LEAD ambiguous entry);
   no code word in the entry = KNOWN (step 0 skip); code words = KNOWN-PART with the code words as residue (the E78
   shape, never KNOWN); it also answers the leaf LOOK. Already-read blocks (ciphertext*.txt headers, read at the ref)
   are DONE only for the same pointer and entry ('row P/N', the item's own label, or a date and header time that pick
   one entry); same page and date without that is LEAD. Same-page entries already read or with an OR hit are LEAD.
 6 G3 (--reading FILE): distinctive decoded phrases through the cached editions (print_check.search_text) and, with
   --network, print_check's ia-global and Google Books routes (one row per route, the most blocking result): a hit
   within +-3 days sharing >= 2 rare entities is SUBSTANCE (decoding proceeds; any class sentence, SO row or 'not
   located' sentence waits for the verifier's diff); other hits LEAD; the offline network routes are UNCHECKED-NET,
   which blocks at G3, and an offline run reuses a still-valid network row only for the same route and query (row id).

Output: rows appended to ciphers/<slug>/prior-work.tsv (append-only: utc, origin_main_commit, item_id, scope, check,
route, query, control, hits, evidence <= 200 chars with file:line or URL, verdict, requests_by_host, valid_until, row_id,
residue); rows with the same id (the same bullet copied into several sections) are printed once with every location.
look.tsv is append-only too (utc, item_id, look_row_id, role, folio, canvas, image, source, status): a row is added when a
crop's status changes (owed -> answered), never removed. One line per row, a holds summary (specific rows vs generic
LOOK/UNCHECKED holds -- never a recall figure) and one verdict per scope on stdout (--json for machines; --dry-run
writes nothing, --record included).
Verdicts: DONE KNOWN KNOWN-PART LOOK LEAD UNCHECKED UNCHECKED-NET SUBSTANCE KEY-SOURCE CONTEXT CLEAR; a check that did not
run is UNCHECKED, never CLEAR. --record ROWID 'VERDICT: what was seen' (DONE, KNOWN, KNOWN-PART, CLEAR, CONTEXT,
KEY-SOURCE or SUBSTANCE) answers any row that is not DONE (a false KNOWN can be recorded CLEAR); the newest answer
replaces that row on every later run. Row ids hash the line's text, not its number, so an edit above it keeps the answer.
Network rows carry a 14-day valid_until. Rule 10: the tool never assigns a novelty class; N-class tokens and novelty
words in quoted evidence are masked as [*] ('New Orleans' and other capitalised names are left alone).
Exit (item and spec modes): 3 the step is DONE; 2 the step works the text, the plaintext is KNOWN and no --known-answer
consumer is named (item:<unread id> or gate:<name>; another string is accepted with a warning); 4 a worked scope is LOOK,
LEAD or UNCHECKED (UNCHECKED-NET too with --strict or at G3) -- this item only, never the lane; a live claim or an owed
own-work row still exits 4 when a consumer is named; 0 proceed on the listed residue. --brief prints a per-item exit
table and exits with the common code when every item agrees, 4 when any item owes work, and 5 for a mix of 0 with 2/3
(proceed only on the items marked 0). Register, record and derive modes exit 0; a usage error exits 1.
Network (--network): one print_check.Net for the whole run (a host blocked on item 1 is skipped for item 2; one 1.5 s
spacing clock; --max-session-requests, default 200) with --max-requests per item on top.

Must catch (tools/tests/test_prior_work.py, offline, sockets guarded): a NOTES '[x]' bullet naming the same leaf (exit
3); a ROOM claim 2 h old without done (LEAD live-claim, exit 4); Tomokiyo 'f.18 (no.6) ... both deciphered' for fr.3040
(KNOWN, exit 2; --known-answer key-check exit 0); an AUDIT line classing the item as already known (KNOWN); a NOTES period
gloss on THIS leaf (KNOWN); a hard-wrapped AUDIT paragraph recording a partial period decipherment (KNOWN-PART);
--register flagging the NEXT-STEPS row whose step is done; an edition window with its control hit (LEAD); a decoded
phrase printed within 3 days (SUBSTANCE).
Must NOT block: the E78 shape (KNOWN-PART, exit 0, code words as residue, chosen by entry number on the real page shape);
a gloss on a DIFFERENT letter on a neighbouring leaf (CONTEXT); 'no interlinear gloss on the leaf' / 'no decipherment
attached' (CLEAR, never KNOWN); our own depth line and a modal 'more likely to have existed' (no KNOWN); DECODE
'Non-decrypted' (no KNOWN, no CLEAR); fr.16104 vs fr.16105 at the same folio, also in one sentence (no match); a fetch
or image-check marker, or 'already'/'thread'/'spread', for a read step (no DONE); a different same-day entry on the same
ledger page (no DONE); a check that could not run (UNCHECKED, never CLEAR); a claim on another slug that merely contains
this one; a second-audit on an already-classed item (never DONE).

Rollout: warn-first -- workers run it and paste the output; enforcement on new briefs waits for the leave-one-target-out
replay and a measured false-block rate on research/PRIOR-WORK-SURVIVORS-2026-10-08.tsv.
TODO v2 (research/PRIOR-WORK-LEAK-2026-10-08.md): the office-keyed edition scan at scale (per-volume controls for every
seeded row, the OR/ORN compact index, calendar-number/Groen/footnote segmenters, feast-day, regnal and Republican date
generators, an alias table from KEY-OFFICES.tsv, --learn); the printed-cipher span router (Birch/Thurloe exact-length
votes against a within-span null, Japikse spaced type, Groen roman stretches); the leave-one-target-out replay harness;
WEB rows with same-blog controls; HOLD; be-api snippet routes for lending-only volumes; cache and clone freshness (48 h /
7 days) and shallow-clone --deepen; WVO print codes and RAH copia classes; the classed clear-share test beyond Eckert;
ARTEFACTS.tsv for typed artefacts beyond crops; work_queue.check() in room.py --push; --point; intake_gate_check reading
prior-work.tsv; HCPortal ids. Predicted classes are deliberately absent (rule 10).
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
STEP_TYPES = ("read", "transcribe", "decode", "crop", "key", "align", "lookup", "audit", "second-audit", "upgrade-audit",
              "new-family-audit", "propagate-revision")
NEVER_DONE = {"second-audit", "propagate-revision", "upgrade-audit", "new-family-audit"}
WORKS_TEXT = {"read", "transcribe", "decode", "crop"}
KNOWN_INPUT = {"key", "align"}
SPECIFIC = {"DONE", "KNOWN", "KNOWN-PART", "LEAD", "SUBSTANCE", "KEY-SOURCE"}
GENERIC = {"LOOK", "UNCHECKED", "UNCHECKED-NET"}
COLUMNS = ["utc", "origin_main_commit", "item_id", "scope", "check", "route", "query", "control", "hits", "evidence",
           "verdict", "requests_by_host", "valid_until", "row_id", "residue"]
LOOK_COLS = ["utc", "item_id", "look_row_id", "role", "folio", "canvas", "image", "source", "status"]
ITEM_COLUMNS = ["item_id", "shelfmark", "folio", "canvas", "decode", "ptr", "wvo", "date", "calendar", "sender",
                "recipient", "office", "place", "language", "kind", "holder_url", "clear_words", "verified"]
STEP_RE = {
    "read": r"\b(?:read|re-?read|decod(?:e|ed|ing)|deciphered|transcribed|transcription|reconciled)\b",
    "transcribe": r"\b(?:transcri(?:be|bed|ption|ptions)|blind pass(?:es)?|reconcil(?:e|ed|iation)|ciphertext)\b",
    "decode": r"\b(?:decod(?:e|ed|ing)|deciphered|decipher|key applied|applied the key|decode_key)\b",
    "crop": r"\b(?:crop(?:s|ped)?|iiif_lines)\b",
    "key": r"\b(?:key(?:ed)?|key rebuild|key recovery|interlinear_align)\b",
    "align": r"\b(?:align(?:s|ed|ment)?|interlinear_align)\b",
    "lookup": r"\b(?:look(?:ed)?[ -]?up|catalogue|search(?:ed)?|print[- ]check(?:ed)?|grep(?:ped)?|checked|located|"
              r"refuted)\b",
    "audit": r"\b(?:audit(?:ed)?|verif\w*|class(?:ed|ified)?)\b",
    "fetch": r"\b(?:fetch\w*|download\w*|image[- ]?check\w*|montage|thumbnail\w*)\b",      # register mode only
}
STEP_RE = {k: re.compile(v, re.I) for k, v in STEP_RE.items()}
STEP_PRIORITY = ("transcribe", "crop", "align", "decode", "read", "audit", "fetch", "lookup", "key")
FETCHY = re.compile(r"\b(?:image[- ]?check\w*|fetch\w*|crop\w*|download\w*|thumbnail\w*|montage)\b", re.I)
DONE_MARK = re.compile(r"^\s*(?:[-*+]|\d+\.)\s*(?:\*\*)?\[(?:[xX]\]|done\b|already run\b|retired\])", re.I)
COMPLETED = re.compile(r"\b(?:done|finished|completed|reconciled|transcribed|decoded|deciphered|read in full|"
                       r"read and|was read|were read)\b", re.I)
OPEN_WORDS = re.compile(r"\bnot yet\b|\bremains?\b|\bpending\b|\bstill (?:to|un)\w*|\bunread\b|"
                        r"\bnot (?:done|run|checked|searched|opened|fetched)\b", re.I)
LOOKUP_DONE = re.compile(r"\blists? no\b|\bnot borne out\b|\bnot located\b|\bnot found\b|\bno such\b|\brefuted\b|"
                         r"\bdoes not (?:list|exist)\b|\bno trace\b|\blooked up\b|\bsearched\b", re.I)
LEAF_GLOSS = re.compile(r"gloss|interlinea|clear cop|en clair|clerk'?s copy|(?:period|contemporary|marginal|attached|"
                        r"clerk'?s?|secretary'?s?|leaf'?s own|its)\s+(?:decipher|d[ée]chiffr|descifr|ontcijfer)\w*|"
                        r"d[ée]chiffr\w+ (?:en marge|interlin)|decipherment (?:on|over|above|beside|attached|written)|"
                        r"decipherments?\s+(?:found|exists?|located|at\s+ff?\.)", re.I)
OTHER_LETTER = re.compile(r"\b(?:different|another|other|separate|sibling|neighbouring|neighboring)\s+(?:letters?|items?|"
                          r"pieces?|despatch(?:es)?|dispatch(?:es)?|correspondence)\b|\bnot (?:this|the same) letter\b|"
                          r"\bbelongs to\b|\b(?:of|on|from) (?:the |its |a )?siblings?\b|\bcontext,? not\b", re.I)
REFERENCE_USE = re.compile(r"\b(?:calibrat\w+|checked|tested|compared|aligned|rebuilt|built|derived|reconstructed|recovered|"
                           r"valued)\s+(?:\w+\s+)?(?:against|from|with)\b|\bkey sources?\b|\bas (?:a |the )?(?:control|crib|"
                           r"key source)\b|\bknown-answer\b|\bglossed (?:tokens|words|codes|groups|values)\b|\bsame (?:design|key|table|cipher|hand|system|nomenclator)\b"
                           r"[^.;]{0,25}\bas\b", re.I)
PLAN = re.compile(r"\bnext\s*(?:step)?\s*[:(]|\bcheapest\b|\btodo\b|\bto do\b|\bnot done here\b|\bwould\b", re.I)
SOUGHT = re.compile(r"\bwaiting-on\b|\bdid not locate\b|\bnot (?:yet )?located\b|\bto be located\b|\bsought\b|"
                    r"\bASKS row\b|\bif (?:one|it) exists\b", re.I)
FOUND = re.compile(r"\bfound\b|\bexists?\b|\bon file\b|\battached\b|\bon the leaf\b|\bcarries\b", re.I)
THIS_LEAF = re.compile(r"\bon (?:the|this) (?:leaf|page|sheet|letter)\b|\bitself\b|\bthis letter\b|\bits (?:own )?"
                       r"(?:period |contemporary |interlinear )?(?:decipher|d[ée]chiffr|gloss|clear)|\binterlinea\w*|"
                       r"\bin the margins?\b|\bmarginal\b|\b(?:over|above|below|beside) (?:the |its )?(?:cipher|lines|text)\b|"
                       r"\battached\b|\bclerk'?s?\b|\bsame leaf\b", re.I)
DEC_POS = re.compile(r"(?<![a-z])(?:deciphered|decrypted|decoded|decipherments?|d[ée]chiffr\w*|descifrad[oa]s?|"
                     r"ontcijferd|gedecodeerd|entziffert|decifrat[oa]|attached|glossed|clear cop(?:y|ies)|gloss(?:es)? (?:of|on|"
                     r"over|for))", re.I)
DEC_NEG = re.compile(r"\bun(?:deciphered|decrypted|decoded|glossed)\b|\bnon[- ]?(?:decrypted|deciphered|"
                     r"d[ée]chiffr\w*)\b|\b(?:not|never|nor)\s+(?:yet\s+)?(?:been\s+)?(?:deciphered|decrypted|decoded|"
                     r"glossed|attached)\b|\bsans\s+(?:le\s+|son\s+)?d[ée]chiffr\w*|\bwithout\s+(?:a\s+|the\s+|any\s+)?"
                     r"(?:decipher\w*|gloss\w*)|\bniet\s+(?:ontcijferd|gedecodeerd)|\bnicht\s+entziffert|"
                     r"\bsin\s+descifrar|\b(?:no|nothing|none)\s+(?!doubt\b)(?:\w+\s+){0,2}?(?:decipher\w*|gloss\w*|interlinear\w*|"
                     r"clear cop\w*|d[ée]chiffr\w*)(?:\s+(?:of|on|over|for|attached|beside|above|piece))?|"
                     r"key not found|sleutel[^.]{0,40}niet", re.I)
NEGATOR = re.compile(r"\b(?:no|not|never|nor|nothing|without|sans|niet|nicht|kein\w*|sin|aucun\w*|pas|ni|none|non|"
                     r"negnot)\b[\w\s'-]{0,25}$", re.I)
MODAL = re.compile(r"\b(?:likely|unlikely|possibl[ey]|possibility|perhaps|probabl[ey]|presumabl[ey]|might|would|could|"
                   r"whether|hypothe\w*|suppos\w*|not excluded|cannot be excluded|can't be excluded|if any|if a|if the)\b|"
                   r"(?-i:\bmay\b)", re.I)
OWN_DEPTH = re.compile(r"\*\*D[0-4]\*\*|\bD[0-4]\s*\((?:Partially|Largely|Fully|Fragments|Deciphered|Partial)|\boutward\b|"
                       r"\bdepth\b|\b[HCS]\s+\d+\s+of\s+\d+\b|\bdepth_pct\b|\b(?:un)?safe sentences?\b", re.I)
PARTIAL = re.compile(r"\bpartial(?:ly)?\b|\bpartly\b|\ben partie\b|\bgedeeltelijk\b|\bteilweise\b|\bin parte\b|"
                     r"\ben parte\b", re.I)
KEYSRC = re.compile(r"can be read with|\bkey (?:is |was )?(?:found|known|printed|published)\b|reconstructed (?:key|"
                    r"table)|use the following cipher|\bthe cipher used\b", re.I)
HOLDER = re.compile(r"catalog|notice|scopecontent|finding aid|inhoud|description|analyse|regest|copia|calendar|"
                    r"inventaire|inventory", re.I)
R10 = re.compile(r"\bN[0-5]\b(?!-)")
R10W = re.compile(r"\b(?:[Nn]ew|NEW|[Nn]ovel\w*|NOVEL\w*|[Ff]irst|FIRST|[Uu]npublished|UNPUBLISHED|[Nn]ever printed)\b"
                  r"(?!\s+[A-Z])")
CLASS_RE = re.compile(r"\b(?i:class(?:ed|ified|es)?)\b[^.|]{0,40}?\bN([0-5])\b(?!-)|\|\s*\**N([0-5])\**\s*\||"
                      r"\*\*N([0-5])\b(?!-)")
TIME_RE = re.compile(r"(?<![\d.])(\d{1,2})(?:[.:]?\s?(\d{2}))?\s*(?:([ap])\.?\s*m\b\.?|(m)\b)", re.I)
PARTICLES = set("de du des la le van von der den het zu of the and to a al el y e di da dal del count comte conde graf "
                "duke duc duca earl lord lady sir king roi rey queen prince prinz cardinal bishop eveque bisschop "
                "colonel general genl gen col lt capt captain major hon mr mrs saint sainte".split())
GENERIC_SLUG = set("cipher ciphers printed papers letter letters spain france rome london paris holland decode bnf "
                   "fr espagnol colbert baluze clair dupuy naf huntington tomokiyo decrypt".split())
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
STRENGTH = {"KNOWN": 4, "KNOWN-PART": 3, "CONTEXT": 2, "CLEAR": 1}


def safe(text, novelty=True):
    """Rule 10: quoted evidence never carries a novelty class or a novelty word (a capitalised name such as 'New
    Orleans' is left alone). novelty=False masks only N-class tokens (the tool's own query strings)."""
    s = R10.sub("[*]", re.sub(r"\s+", " ", str(text or "")))
    return (R10W.sub("[*]", s) if novelty else s).strip()


def nkey(text):
    return re.sub(r"\W+", " ", str(text or "").lower()).strip()[:400]


class UsageError(Exception):
    pass


class Parser(argparse.ArgumentParser):
    def error(self, message):           # exit 2 means KNOWN here, so a usage error exits 1
        self.print_usage(sys.stderr)
        print(f"prior_work.py: error: {message}", file=sys.stderr)
        sys.exit(1)


# ------------------------------------------------------------------ paths the user supplies

def guard_path(path, what, root=None):
    """Refuse a path with a 'restricted' component, or inside a git checkout whose remote names cipher-lab-private."""
    if not path:
        return
    rp = os.path.realpath(path)
    if "restricted" in rp.split(os.sep) or "restricted" in os.path.normpath(path).split(os.sep):
        raise UsageError(f"{what} {path}: a restricted/ path is never read (RESTRICTED.md rules 1-3)")
    d = rp if os.path.isdir(rp) else os.path.dirname(rp)
    while d and not os.path.isdir(d):
        d = os.path.dirname(d)
    try:
        r = subprocess.run(["git", "-C", d, "remote", "-v"], capture_output=True, text=True, timeout=30)
        remotes = r.stdout if r.returncode == 0 else ""
    except Exception:           # noqa: BLE001 -- no git: nothing to compare against
        remotes = ""
    if "cipher-lab-private" in remotes:
        raise UsageError(f"{what} {path}: inside the private repository, never read by this tool")


# ------------------------------------------------------------------ state at origin/main

class State:
    """Files of the repository at one ref (default origin/main), read with git; 'WORKTREE' reads the checkout."""

    def __init__(self, root, ref="origin/main"):
        self.root, self.ref, self._cache = root, ref, {}
        self.commit = "" if ref == "WORKTREE" else (self._git("rev-parse", "--verify", "-q", ref + "^{commit}") or "").strip()
        self.ok = bool(self.commit) or ref == "WORKTREE"
        self.fallback = not self.commit and ref != "WORKTREE"      # unresolvable ref: the working tree is read, said aloud
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
            dn[:] = sorted(x for x in dn if x not in (".git", "restricted", "img", "images"))
            for f in sorted(fs):
                p = os.path.join(dp, f)
                if f.lower().endswith(exts) and os.path.getsize(p) <= max_bytes:
                    yield p


# ------------------------------------------------------------------ items and rows

def parse_date(s):
    m = re.match(r"(\d{4})-(\d{2})-(\d{2})", s or "")
    if not m:
        return None
    try:
        return datetime.date(*map(int, m.groups()))
    except ValueError:
        return None


def norm_ptr(p):
    """'9714', 'ptr 9714/2', 'p9714' -> ('9714', '2' or '')."""
    m = re.search(r"(\d{4,5})(?:\s*/\s*(\d{1,2}))?", p or "")
    return (m.group(1), m.group(2) or "") if m else ("", "")


def item_unit(item):
    ids = set()
    if item.get("decode") and re.sub(r"\D", "", item["decode"]):
        ids.add("R" + re.sub(r"\D", "", item["decode"]))
    p, e = norm_ptr(item.get("ptr"))
    if p:
        ids.add(f"ptr:{p}/{e}" if e else f"ptr:{p}")
    if item.get("wvo") and re.sub(r"\D", "", item["wvo"]):
        ids.add("wvo:" + str(int(re.sub(r"\D", "", item["wvo"]))))
    if sm.LABEL_RE.fullmatch(item.get("item_id", "")):
        ids.add("label:" + item["item_id"])
    return sm.unit(item.get("shelfmark", ""), item.get("folio", ""), item.get("canvas", ""), ids)


def read_tsv(text):
    lines = [l for l in (text or "").splitlines() if l.strip() and not l.startswith("#")]
    return list(csv.DictReader(lines, delimiter="\t")) if lines else []


def row_text(r):
    """All string cells of a DictReader row (a ragged row puts extra cells under None and missing ones as None)."""
    out = []
    for k, v in (r or {}).items():
        if isinstance(v, str):
            out.append(v)
        elif isinstance(v, list):
            out += [x for x in v if isinstance(x, str)]
    return " ".join(out)


def item_from_spec(spec):
    item = {k: "" for k in ITEM_COLUMNS}
    for part in spec.split(";"):
        if "=" in part:
            k, v = part.split("=", 1)
            k = k.strip().lower()
            if k not in ITEM_COLUMNS:
                raise UsageError(f"--item-spec key {k!r} is not one of {', '.join(ITEM_COLUMNS)}")
            item[k] = v.strip()
    if item["date"] and not parse_date(item["date"]):
        raise UsageError(f"--item-spec date {item['date']!r} is not a real YYYY-MM-DD date")
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
        self.net, self.session_net = None, None
        items = read_tsv(state.read(f"{self.folder}/items.tsv"))
        vols = set().union(*[sm.volume_keys(i.get("shelfmark", "")) for i in items]) if items else set()
        notes_vols = sm.volume_keys(state.read(f"{self.folder}/NOTES.md") or "")
        self.multi_volume = len(vols) > 1 or len(notes_vols) > 1
        self.items, self.unit_pages, self.leaf_answered = items, None, None
        self.restricted = state.read(f"{self.folder}/RESTRICTED.md") is not None or \
            os.path.isfile(os.path.join(self.root, self.folder, "RESTRICTED.md"))
        self._single = None

    @property
    def single_item(self):
        """True when the folder holds exactly one item (items.tsv, else the derived catalogue list)."""
        if self._single is None:
            self._single = len(self.items) == 1 if self.items else len(derived_units(self)) == 1
        return self._single

    def row(self, item, scope, check, route, verdict, evidence="", query="", control="", hits="", net=False, residue="",
            key=None):
        rid = rid_of(item["item_id"], check, route, query, key)
        valid = (self.today + datetime.timedelta(days=14)).isoformat() if net else self.today.isoformat()
        return dict(utc=self.utc, origin_main_commit=self.state.commit[:12], item_id=item["item_id"], scope=scope,
                    check=check, route=route, query=safe(query, novelty=False)[:160], control=control, hits=str(hits),
                    evidence=safe(evidence)[:200], verdict=verdict, requests_by_host="", valid_until=valid, row_id=rid,
                    residue=safe(residue)[:200])


def rid_of(item_id, check, route, query="", key=None):
    """A row id: the item, the check and a hash of the line's normalised text (prose rows) or the route and query."""
    basis = f"{check}|{key}" if key is not None else f"{route}|{query}"
    return f"{item_id}:{check}:{hashlib.sha1(basis.encode()).hexdigest()[:6]}"


NET_RANK = {"SUBSTANCE": 6, "LEAD": 5, "UNCHECKED-NET": 4, "UNCHECKED": 3, "KEY-SOURCE": 2, "CONTEXT": 1, "CLEAR": 0}


def sentences(line):
    return [p for c in sm.clauses(line) for p in re.split(r"\s*\*(?!\*)\s*(?=[A-Z])", c) if p.strip()]


def classify(text):
    """'pos' | 'partial' | 'keysrc' | 'neg' | None for one line, the strongest sentence winning. A decipherment word is
    negated by a negator up to three words before it ('no separate dechiffrement', 'sans le dechiffrement', 'not yet
    deciphered', 'Non-decrypted', 'no interlinear gloss on the leaf', 'no decipherment attached') or by a fixed phrase
    ('undeciphered', 'key not found'); a modal or hypothetical sentence ('more likely to have existed', 'not excluded')
    is no evidence either way."""
    found = set()
    for s in sentences(text):
        if MODAL.search(s):
            continue
        rest = DEC_NEG.sub(" negnot ", s)
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


def date_in(text, d, window=1):
    """The date d (day and month name, either order; a list such as '5 or 13 July' too) in text; a year written beside
    it must be within one of d's."""
    if not d:
        return False
    months = "|".join(re.escape(w) for w in MONTHS[d.month].split())
    day = rf"0?{d.day}(?:st|nd|rd|th|er|e)?"
    alt = rf"\b{day}(?:\s*(?:,|/|or|and|&|et|-)\s*\d{{1,2}}(?:st|nd|rd|th)?)*\.?\s+(?:de\s+|of\s+)?(?:{months})\b\.?|" \
          rf"\b(?:{months})\.?\s+(?:\d{{1,2}}(?:st|nd|rd|th)?\s*(?:,|/|or|and|&|-)\s*)*{day}\b"
    for m in re.finditer(alt, text, re.I):
        near = re.findall(r"\b1[4-9]\d\d\b", text[m.end():m.end() + 12])
        if not near or any(abs(int(y) - d.year) <= window for y in near):
            return True
    return False


# ------------------------------------------------------------------ paragraphs, labels, attribution

def label_of(line):
    """A table row's leading cell, a bullet's or paragraph's bold lead, or None."""
    s = line.strip()
    if s.startswith("|"):
        cells = [c.strip() for c in s.strip("|").split("|")]
        return re.sub(r"\*+", "", cells[0]) if cells else ""
    m = re.match(r"^(?:[-*+]|\d+\.)?\s*\*\*(.+?)\*\*", s)
    return m.group(1) if m else None


def paragraphs(lines):
    """[(first_line_no, text, label, cells)]: a bullet, heading, table row or bold-led line starts one; hard-wrapped
    continuation lines are joined to it (at most 15)."""
    out, cur = [], None
    for i, line in enumerate(lines, 1):
        s = line.strip()
        if not s:
            cur = None
            continue
        table = s.startswith("|")
        starts = table or s.startswith(("#", "- ", "* ", "+ ", "**")) or re.match(r"\d+\.\s", s) or cur is None
        if starts or len(cur[1]) >= 15:
            if table and set(s) <= set("|-: "):
                cur = None
                continue
            cells = [c.strip() for c in s.strip("|").split("|")] if table else None
            cur = [i, [line], cells]
            out.append(cur)
            if table:
                cur = None
        else:
            cur[1].append(line)
    res = []
    for i, ls, cells in out:
        text = " ".join(x.strip() for x in ls)
        lab = label_of(ls[0])
        if lab is None and cells is None and not text.startswith("#"):
            first = sm.clauses(re.sub(r"^\s*(?:[-*+]|\d+\.)\s*", "", text))
            lab = first[0] if first else None
        res.append((i, text, lab, cells))
    return res


def segments(text, cells):
    """Clauses of a paragraph (a table row: each cell after the first, split again)."""
    if cells is not None:
        return [c for cell in cells[1:] for c in sm.clauses(cell)]
    return sm.clauses(re.sub(r"^\s*(?:[-*+]|\d+\.)\s*", "", text))


def nearest_owner_other(u, seg):
    """True when the clause names other units too and every decipherment word in it sits nearest to another unit's
    mention ('WVO 124 (Loc. 8510/5 f.134 cipher, f.135 contemporary decipherment)' beside '126's reading')."""
    words = [m.start() for m in DEC_POS.finditer(seg)] + [m.start() for m in re.finditer(r"\bgloss\w*|\bdecipherments?\b", seg, re.I)]
    marks = [((mt.start + mt.end) // 2, sm.mention_is_unit(u, mt)) for mt in sm.mentions(seg)]
    marks += [(p + 2, x) for p, x in sm.bare_wvo_positions(u, seg)]
    if not words or not marks or all(x for _, x in marks):
        return False
    marks.sort()

    def owner(w):          # 'its decipherment ff.162r-163r': the possessive points back to the clause's subject
        if re.search(r"\b(?:its|their)\s+(?:own\s+)?(?:\w+\s+)?$", seg[max(0, w - 30):w], re.I):
            return marks[0][1]
        return min(marks, key=lambda mk: abs(mk[0] - w))[1]
    return all(not owner(w) for w in words)


def gloss_owner_other(u, seg):
    """True when every decipherment word in seg is followed by 'of/over/on/for <a unit that is not u>'."""
    ms = list(DEC_POS.finditer(seg)) + list(re.finditer(r"\bgloss\w*|\bdecipherments?\b", seg, re.I))
    if not ms:
        return False
    owners = []
    pieces = set(re.findall(r"\b(?:no|nr|n°)\.?\s?(\d{1,4})\b", seg, re.I))
    for m in ms:
        tail = seg[m.end():m.end() + 110]
        pm = re.match(r"\s*(?:of|for|on|over)\s+(?:the\s+)?(?:letter\s+)?(?:no|nr|n°)\.?\s?(\d{1,4})\b", tail, re.I)
        if pm:                  # 'the period decipherment of no.87' in a clause about no.86
            owners.append(False if pieces - {pm.group(1)} or not sm.match(u, seg) == "exact" else None)
            continue
        t = re.match(r"\s*(?:\w+\s+){0,1}?(?:of|over|on|for|to|above|under)\s+(?:the\s+)?(?:letter\s+|leaf\s+)?(.{0,90})", tail)
        if not t:
            owners.append(None)
            continue
        k = sm.parse(t.group(1))
        if not (k.leaves or k.ids or k.canvases):
            owners.append(None)
        else:
            owners.append(sm.match(u, t.group(1)) == "exact")
    return bool(owners) and all(o is False for o in owners)


# ------------------------------------------------------------------ check 1: own work

def done_part(line):
    """The text a done bullet says was done: after the marker, cut at 'next' / 'then' / 'later' / 'todo'."""
    m = DONE_MARK.search(line)
    rest = line[m.end():] if m else line
    cut = re.search(r"\bnext\b|\bthen\b|\btodo\b|\bto do\b|\blater\b", rest, re.I)
    return rest[:cut.start()] if cut else rest


def step_done(step, line):
    dp = done_part(line)
    if step in ("read", "decode", "transcribe") and FETCHY.search(re.sub(r"^\W*\d{1,2}\s+\w+\.?(?:\s+\d{4})?\W*", "", dp)[:60]):
        return False
    return step in STEP_RE and bool(STEP_RE[step].search(dp))


def check_own(ctx, item, u, step):
    rows, st, f = [], ctx.state, ctx.folder
    if not st.ok:
        rows.append(ctx.row(item, "step", "1-own", "state", "UNCHECKED",
                            f"{ctx.a.ref} does not resolve in {ctx.root}: own work not read at current state "
                            "(the working tree was read instead)"))
    keyed = bool(u.leaves or u.canvases or u.ids)
    d = parse_date(item.get("date"))
    for fn in ("NOTES.md", "ITERATE.md", "HYPOTHESES.md"):
        prose = None
        if not keyed:           # no folio, canvas or id: a paragraph naming the unit's volume and date is a LEAD
            for i, text, _, _ in paragraphs(lines_of(st, f"{f}/{fn}")) if (u.vols and d) else []:
                if (u.vols & sm.volume_keys(text)) and date_in(text, d) and (
                        DONE_MARK.search(text) or (step in STEP_RE and STEP_RE[step].search(text) and COMPLETED.search(text))
                        or (step == "lookup" and LOOKUP_DONE.search(text) and not OPEN_WORDS.search(text))):
                    rows.append(ctx.row(item, "step", "1-own", f"{fn}:{i}", "LEAD",
                                        f"done-candidate (date-keyed, the unit has no folio): {fn}:{i} {text.strip()}",
                                        key=nkey(text)))
            continue
        for i, line in enumerate(lines_of(st, f"{f}/{fn}"), 1):
            loc = f"{fn}:{i}"
            m = sm.match(u, line, ctx.multi_volume)
            if not m or m == "fuzzy":
                continue
            if DONE_MARK.search(line):
                if m == "exact" and step not in NEVER_DONE and step_done(step, line) and not OPEN_WORDS.search(done_part(line)):
                    rows.append(ctx.row(item, "step", "1-own", loc, "DONE", f"{loc} {line.strip()}", key=nkey(line)))
                else:
                    why = ("volume not named in a multi-volume folder" if m == "ambiguous" else
                           "the bullet says part is still open" if OPEN_WORDS.search(done_part(line)) else
                           "marker for this unit, other step")
                    rows.append(ctx.row(item, "step", "1-own", loc, "LEAD", f"done-candidate ({why}): {loc} {line.strip()}",
                                        key=nkey(line)))
            elif m == "exact" and step in STEP_RE and STEP_RE[step].search(line) and COMPLETED.search(line):
                prose = (loc, line)
            elif m == "exact" and step == "lookup" and LOOKUP_DONE.search(line) and not OPEN_WORDS.search(line):
                prose = (loc, line)
        if prose and step not in NEVER_DONE:
            rows.append(ctx.row(item, "step", "1-own", prose[0], "LEAD", f"done-candidate (prose): {prose[0]} {prose[1].strip()}",
                                key=nkey(prose[1])))
    rows += audit_classes(ctx, item, u, step)
    for r in read_tsv(st.read("WORK-QUEUE.tsv")):
        blob = row_text(r)
        if has_slug(ctx.slug, blob) and str(r.get("status") or "").startswith("done") and keyed and \
                sm.match(u, blob, ctx.multi_volume) == "exact":
            v = "DONE" if (step in STEP_RE and STEP_RE[step].search(blob) and step not in NEVER_DONE) else "LEAD"
            rows.append(ctx.row(item, "step", "1-own", f"WORK-QUEUE:{r.get('job_id')}", v,
                                f"WORK-QUEUE {r.get('job_id')} {r.get('status')}: {r.get('note') or ''}"))
    if step == "crop":
        rows += crop_artefacts(ctx, item, u)
    rows += room_claims(ctx, item, u)
    return rows


def crop_artefacts(ctx, item, u):
    """A committed crop file for the leaf, or an images/manifest.json crop entry for the leaf or canvas (the canvas from
    the IIIF source_url's /fN/ or a cNNN_ crop-name prefix)."""
    f = ctx.folder
    for p in ctx.state.ls(f"{f}/images"):
        if ("crop" in p.lower() or re.search(r"_L\d+\.", p)) and sm.match(u, os.path.basename(p), ctx.multi_volume) == "exact":
            return [ctx.row(item, "step", "1-own", "artefact", "DONE", f"crop on file: {p}")]
    for rel in [p for p in ctx.state.ls(f"{f}/images") if p.endswith("manifest.json")]:
        try:
            data = json.loads(ctx.state.read(rel) or "")
        except ValueError:
            continue
        for e in _walk_dicts(data):
            name = e.get("crop") or ""
            if not isinstance(name, str) or not name:
                continue
            src = str(e.get("source_url") or e.get("source_file") or "")
            cv = re.search(r"/f(\d{1,4})/", src) or re.search(r"_f(\d{1,4})_", src) or re.match(r"c(\d{1,4})_L\d", name)
            canvas = int(cv.group(1)) if cv else None
            if (canvas is not None and canvas in u.canvases) or (u.leaves and sm.match(u, name, ctx.multi_volume) == "exact"):
                return [ctx.row(item, "step", "1-own", "artefact", "DONE", f"crop entry in {rel}: {name} (canvas {canvas})")]
    return []


def _walk_dicts(o):
    if isinstance(o, dict):
        yield o
        for v in o.values():
            yield from _walk_dicts(v)
    elif isinstance(o, list):
        for v in o:
            yield from _walk_dicts(v)


def derived_units(ctx):
    """Distinct (volume, folio) / id keys the folder's catalogue names: status.json rows and NOTES headings."""
    keys = set()
    try:
        res = json.loads(ctx.state.read("status.json") or "{}").get("results", [])
    except ValueError:
        res = []
    for r in res if isinstance(res, list) else []:
        if str(r.get("link", "")).rstrip("/").endswith(f"/ciphers/{ctx.slug}"):
            k = sm.parse(f"{r.get('document_id', '')} {r.get('title', '')}")
            keys.add((tuple(sorted(v for v in k.vols if not v.startswith("hint:"))),
                      tuple(sorted(k.leaves))[:1], tuple(sorted(k.ids))) if (k.leaves or k.ids) else ("status", r.get("title", "")))
    for line in lines_of(ctx.state, f"{ctx.folder}/NOTES.md"):
        if line.startswith("#"):
            k = sm.parse(line)
            if k.leaves:
                keys.add((tuple(sorted(v for v in k.vols if not v.startswith("hint:"))), tuple(sorted(k.leaves))[:1], ()))
    return keys


def audit_classes(ctx, item, u, step):
    """AUDIT.md and status.json lines classing this exact item: a class line counts only from its own label (table first
    cell, bold lead) or a section heading naming exactly this unit; a folder with one item takes unlabelled lines."""
    rows, found = [], None
    lines = lines_of(ctx.state, f"{ctx.folder}/AUDIT.md")
    head_this = False
    for i, line in enumerate(lines, 1):
        if line.startswith("#"):
            head_this = sm.match(u, line, ctx.multi_volume) == "exact" and not sm.names_other(u, line)
            continue
        m = CLASS_RE.search(line)
        if not m:
            continue
        lab = label_of(line)
        lk = sm.parse(lab) if lab else None
        if lk is not None and (lk.leaves or lk.ids or lk.canvases or lk.vols):
            names = sm.match(u, lab, ctx.multi_volume) == "exact"
        else:
            k = sm.parse(line)
            names = head_this and not sm.names_other(u, line) or \
                (ctx.single_item and not (k.leaves or k.ids or k.canvases))
        if names:
            found = (f"AUDIT.md:{i}", int(next(g for g in m.groups() if g)), line)
    try:
        res = json.loads(ctx.state.read("status.json") or "{}").get("results", [])
    except ValueError:
        res = []
    for r in res if isinstance(res, list) else []:
        if str(r.get("link", "")).rstrip("/").endswith(f"/ciphers/{ctx.slug}"):
            blob = f"{r.get('document_id', '')} {r.get('title', '')}"
            cls = re.search(r"N([0-5])", str(r.get("plaintext_novelty") or r.get("novelty") or ""))
            if cls and sm.match(u, blob, ctx.multi_volume) == "exact":
                known_text = str(r.get("text", "")).startswith("known")
                found = ("status.json", int(cls.group(1)), blob + (" (text: known)" if known_text else ""))
    prog = [r for r in read_tsv(ctx.state.read("PROGRESS.tsv")) if r.get("folder") == ctx.slug]
    for r in prog:
        blob = " ".join(str(r.get(c) or "") for c in ("name", "note", "source"))
        if (len(prog) == 1 and ctx.single_item) or sm.match(u, blob, ctx.multi_volume) == "exact":
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
        rows.append(ctx.row(item, "step", "1-own", loc, "DONE",
                            f"an audit already classes this item (a re-audit; Audit 2 is --step-type second-audit): {loc} {line}"))
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


ROLE_TAG = re.compile(r"\b(?=[A-Z0-9-]*\d)[A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*\b|\b[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+\b")


def role_tag(role):
    m = ROLE_TAG.search(role or "")
    return m.group(0) if m else (role or "").strip()


def tag_in(tag, role):
    if not tag:
        return False
    if ROLE_TAG.fullmatch(tag):
        return re.search(rf"(?<![\w-]){re.escape(tag)}(?![\w-])", role or "") is not None
    return (role or "").strip() == tag


def room_claims(ctx, item, u):
    rows, room = [], lines_of(ctx.state, "ROOM.md")[-2000:]
    for i, l in enumerate(room):
        m = nsf.ROOM_RE.match(l)
        if not m or not has_slug(ctx.slug, l) or not re.search(r"\bclaim", m.group(3), re.I):
            continue
        body = m.group(3)
        k = sm.parse(re.sub(re.escape(ctx.slug), " ", body))
        names = sm.match(u, body, ctx.multi_volume) == "exact"
        target_level = not (k.leaves or k.ids or k.canvases)
        if not names and not target_level:
            continue
        t = datetime.datetime.strptime(m.group(1), "%Y-%m-%d %H:%M").replace(tzinfo=datetime.timezone.utc)
        age = (ctx.now - t).total_seconds() / 3600
        tag = role_tag(m.group(2))
        if not 0 <= age < 6 or (ctx.a.me and (tag == ctx.a.me or tag_in(ctx.a.me, m.group(2)))):
            continue
        done = False
        for x in room[i + 1:]:
            mx = nsf.ROOM_RE.match(x)
            if mx and tag_in(tag, mx.group(2)) and has_slug(ctx.slug, x) and re.search(r"\bdone\b", mx.group(3)):
                done = True
                break
        if not done:
            what = "live-claim" if names else "live-claim (target-level: names the slug, no unit; check it does not cover this item)"
            rows.append(ctx.row(item, "step", "1-own", f"ROOM {m.group(1)}", "LEAD", f"{what} ({age:.1f} h, no done line): {l}",
                                key=nkey(l)))
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


def leaf_records(ctx, u, folder=None, multi_volume=None):
    """[(verdict, loc, seg)] attributed to this unit, and [(verdict, loc, seg)] for neighbouring leaves."""
    mine, near = [], []
    folder = folder or ctx.folder
    multi = ctx.multi_volume if multi_volume is None else multi_volume

    ctx = type("LeafCtx", (), {"state": ctx.state, "folder": folder, "multi_volume": multi})()
    for fn in ("NOTES.md", "AUDIT.md"):
        for i, text, lab, cells in paragraphs(lines_of(ctx.state, f"{ctx.folder}/{fn}")):
            if not (LEAF_GLOSS.search(text) or re.search(r"clear[- ]pages", text, re.I)):
                continue
            clearpages = DONE_MARK.search(text) and re.search(r"clear[- ]pages", text, re.I)
            label_hit = bool(lab) and sm.match(u, lab, ctx.multi_volume) == "exact" and not sm.names_other(u, lab)
            sought = SOUGHT.search(text) and not FOUND.search(text)
            loc = f"{fn}:{i}"
            for seg in segments(text, cells):
                if not (LEAF_GLOSS.search(seg) or clearpages):
                    continue
                if (HOLDER.search(seg) and not clearpages) or OWN_DEPTH.search(seg) or MODAL.search(seg) or PLAN.search(seg):
                    continue
                cls = classify(seg)
                if sought and cls in ("pos", "partial"):
                    continue                    # a gap list's 'a contemporary decipherment of P4 -- waiting-on ...'
                m = sm.match(u, seg, ctx.multi_volume)
                other = sm.names_other(u, seg)
                explicit = m == "exact" and (cells is None or label_hit)   # a table row is about its leading cell
                if explicit or (label_hit and not other):
                    if not explicit and cls in ("pos", "partial") and not THIS_LEAF.search(seg):
                        continue                # under a label, a positive needs a this-leaf cue ('on the leaf itself')
                    if OTHER_LETTER.search(seg) or (cls in ("pos", "partial") and (gloss_owner_other(u, seg) or
                                                                         (other and nearest_owner_other(u, seg)))) or \
                            (cls in ("pos", "partial") and REFERENCE_USE.search(seg) and
                             (other or not explicit or not THIS_LEAF.search(seg))):
                        v = "CONTEXT"
                    elif cls == "pos":
                        v = "KNOWN"
                    elif cls == "partial":
                        v = "KNOWN-PART"
                    else:
                        v = "CLEAR" if (cls == "neg" or clearpages) else None
                    if v:
                        mine.append((v, loc, seg))
                else:
                    mf = sm.match(u, seg, ctx.multi_volume, tol=4)
                    if mf in ("exact", "fuzzy") and cls in ("pos", "partial"):
                        near.append(("CONTEXT" if OTHER_LETTER.search(seg) else "KEY-SOURCE", loc, seg))
    return mine, near


def check_leaf(ctx, item, u, step):
    if step not in WORKS_TEXT:
        return [], []
    rows, look = [], []
    mine, near = leaf_records(ctx, u)
    for v, loc, seg in near:
        rows.append(ctx.row(item, "plaintext", "2-leaf", loc, v,
                            ("gloss on another letter, not this one: " if v == "CONTEXT" else
                             "unattributed gloss on a neighbouring leaf (nearby sheet): ") + f"{loc} {seg.strip()}",
                            key=nkey(seg)))
    answered = None
    if mine:
        best = max(mine, key=lambda r: (STRENGTH[r[0]], int(r[1].split(":")[1])))
        v, loc, seg = best
        conflict = sorted({f"{l} {vv}" for vv, l, _ in mine if (vv == "CLEAR") != (v == "CLEAR")})
        ev = f"gloss check recorded: {loc} {seg.strip()}" + (f" (conflicting: {', '.join(conflict)[:60]})" if conflict else "")
        answered = ctx.row(item, "plaintext", "2-leaf", loc, v, ev, key=nkey(seg),
                           residue="the glossed lines' uncovered spans" if v == "KNOWN-PART" else "")
    if ctx.leaf_answered and (answered is None or STRENGTH.get(answered["verdict"], 0) <= 1):
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
    ptr, _ = norm_ptr(item.get("ptr"))
    if leaf:
        for role, p in neighbours(leaf):
            hit = next((i[0] for i in pages if i[1] and i[1][0] == p[0] and (i[1][1] in ("", p[1]))), "")
            look.append([role, f"{p[0]}{p[1]}", "", hit, "manifest" if hit else "folio arithmetic"])
    elif canvas:
        for k, role in ((0, "cipher-page"), (-1, "before-1"), (-2, "before-2"), (1, "after-1"), (2, "after-2"),
                        (3, "after-3"), (4, "after-4")):
            hit = next((i[0] for i in pages if i[2] == canvas + k), "")
            look.append([role, "", str(canvas + k), hit, "manifest" if hit else "canvas arithmetic"])
    elif ptr:
        p0 = int(ptr)
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

def registry(root, name):
    path = os.path.join(root, "tools", "data", name)
    return read_tsv(open(path, encoding="utf-8").read()) if os.path.isfile(path) else []


def portal_rows(ctx, kind):
    """prior_portals.tsv rows of one kind, the last row per portal id winning (the file is append-only)."""
    rows = {r.get("portal"): r for r in registry(ctx.root, "prior_portals.tsv")}
    return [r for r in rows.values() if r.get("kind") == kind]


def portal_dirs(ctx, kind, default):
    rows = portal_rows(ctx, kind)
    rels = [p for r in rows for p in (r.get("cache_paths") or "").split()] if rows else default
    return [os.path.join(ctx.root, p) for p in rels]


def check_portals(ctx, item, u):
    rows = []
    nums = sorted({v.rsplit(" ", 1)[-1] for v in u.vols if re.search(r"\d+$", v)})
    rids = sorted(i for i in u.ids if re.fullmatch(r"R\d+", i))
    mirrors = [d for d in portal_dirs(ctx, "tomokiyo", ["sources/cryptiana/web"]) if os.path.isdir(d)]
    if not mirrors:
        rows.append(ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "UNCHECKED", "sources/cryptiana/web not on disk"))
    else:
        rows += tomokiyo(ctx, item, u, mirrors[0], nums, rids)
    if rids:
        rows += decode_listing(ctx, item, rids[0])
    rows += solver_caches(ctx, item, u, nums + rids + sorted(i[4:].split("/")[0] for i in u.ids if i.startswith("ptr:")))
    for fn in ("NOTES.md", "sources.tsv", "SOURCES.md"):
        for i, line in enumerate(lines_of(ctx.state, f"{ctx.folder}/{fn}"), 1):
            if HOLDER.search(line) and sm.match(u, line, ctx.multi_volume) == "exact" and classify(line) in ("pos", "partial"):
                if not re.match(r"\s*[-*]\s*\[", line):
                    rows.append(ctx.row(item, "plaintext", "3-holder", f"{fn}:{i}", "LEAD",
                                        f"holder/catalogue note with decipherment wording: {fn}:{i} {line.strip()}",
                                        key=nkey(line)))
    return rows


def active_fields(text):
    """'a=x; b=y z' -> {'a': 'x', 'b': 'y z'} (the sub-format of an active-edition row's keyed_on and source cells)."""
    return {k.strip(): v.strip() for k, v in (p.split("=", 1) for p in (text or "").split(";") if "=" in p)}


def check_active_edition(ctx, item, u):
    """3-active-edition (MQS-SCOUT, 9 Oct 2026): `active-edition` rows of prior_portals.tsv name a project preparing an
    edition of a corpus (shelfmark list and/or keyword regex). A match on the item's shelfmark, or a keyword in its sender,
    recipient, office, place or shelfmark, is a LEAD 'active project: contact first' with the project's contact route.
    Catches: fr.2988 f.38 (listed shelfmark); a letter from Castelnau (keyword). Must NOT: an unrelated BnF volume
    (fr.3413), or a volume whose number merely begins with a listed one (fr.29880); never KNOWN, never CLEAR."""
    rows = []
    shelf = item.get("shelfmark") or ""
    for r in portal_rows(ctx, "active-edition"):
        k, src = active_fields(r.get("keyed_on")), active_fields(r.get("source"))
        why = ""
        for sh in (k.get("shelfmark") or "").split("|"):
            keys = sm.volume_keys(sh)
            want = set(pc.norm(sh).split()) - {"bnf", "de"}
            if (keys and keys & u.vols) or (not keys and want and want <= set(pc.norm(shelf).split())):
                why = f"shelfmark {sh.strip()}"
                break
        if not why and k.get("keyword"):
            cells = " ".join(item.get(c) or "" for c in ("sender", "recipient", "office", "place", "shelfmark"))
            m = re.search(k["keyword"], cells, re.I)
            if m:
                why = f"keyword {m.group(0)!r}"
        if why:
            rows.append(ctx.row(item, "plaintext", "3-active-edition", r.get("portal"), "LEAD",
                                f"active project, contact the authors before work ({why}): {src.get('project', r.get('portal'))}; contact: "
                                f"{src.get('contact', 'see the registry row')}; {src.get('url', '')} checked {src.get('date_checked', '')}",
                                query=why, key=f"active|{r.get('portal')}|{why}"))
    return rows


_TOMO = {}


def tomokiyo_pages(mirror):
    """[(path, raw latin-1 text)] of the cached mirror, read once per process."""
    if mirror not in _TOMO:
        _TOMO[mirror] = [(p, open(p, "rb").read().decode("latin-1"))
                         for p in walk_files([mirror], exts=(".htm", ".html", ".txt"))]
    return _TOMO[mirror]


_TOMO_TEXT = {}


def tomokiyo_lines(path):
    if path not in _TOMO_TEXT:
        _TOMO_TEXT[path] = disk_text(path).splitlines()
    return _TOMO_TEXT[path]


def tomokiyo(ctx, item, u, mirror, nums, rids):
    d = parse_date(item.get("date"))
    who = names(item.get("sender")) | names(item.get("recipient"))
    folio_keyed = bool(u.leaves or u.canvases or rids)
    terms = nums + rids + ([str(d.year)] if d and who else [])
    if not terms:
        return [ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "UNCHECKED",
                        "the unit has no volume number, R-id or dated correspondents: the cached Tomokiyo pages were not searched")]
    exact, fuzzy, vol_level, dated = [], [], [], []
    pat = re.compile(r"(?<![0-9A-Za-z])(?:%s)(?![0-9])" % "|".join(map(re.escape, terms)))
    for path, raw in tomokiyo_pages(mirror):
        if not pat.search(raw):
            continue
        rel, head_vols = os.path.relpath(path, ctx.root), set()
        for i, line in enumerate(tomokiyo_lines(path), 1):
            if line.lstrip().startswith("#"):
                head_vols = sm.volume_keys(line) or head_vols
            if not re.search(r"\d", line):
                continue
            k = sm.parse(line)
            hit = "exact" if set(rids) & k.ids else None
            if not hit and (u.leaves or u.canvases):
                mm = sm.match(u, line, False, tol=2, context_vols=head_vols)
                hit = mm if mm in ("exact", "fuzzy") else None
            cls = classify(line)
            if hit:
                v = {"pos": "KNOWN", "partial": "KNOWN-PART", "keysrc": "KEY-SOURCE"}.get(cls, "CONTEXT")
                if hit == "fuzzy" and v in ("KNOWN", "KNOWN-PART"):
                    v = "LEAD"
                note = "undeciphered: no evidence either way; " if cls == "neg" else ("fuzzy-match (folio within 2); " if hit == "fuzzy" else "")
                r = ctx.row(item, "plaintext", "3-tomokiyo", f"{rel}:text{i}", v, f"{note}{rel} (text line {i}) {line.strip()}",
                            residue="spans the page does not cover" if v == "KNOWN-PART" else "", key=nkey(line))
                (exact if hit == "exact" else fuzzy).append(r)
            elif u.vols & {v for v in k.vols if not v.startswith("hint:")} and not k.leaves and cls:
                v = "KEY-SOURCE" if cls == "keysrc" else "CONTEXT"
                vol_level.append(ctx.row(item, "plaintext", "3-tomokiyo", f"{rel}:text{i}", v,
                                         f"volume-level (no folio named): {rel} (text line {i}) {line.strip()}", key=nkey(line)))
            elif d and who and date_in(line, d, window=0) and who & set(pc.norm(line).split()):
                v = {"pos": "LEAD", "partial": "LEAD", "keysrc": "KEY-SOURCE"}.get(cls, "CONTEXT")
                dated.append(ctx.row(item, "plaintext", "3-tomokiyo", f"{rel}:text{i}", v,
                                     f"date-match (date + correspondent, not a shelfmark: open it): {rel} (text line {i}) "
                                     f"{line.strip()}", key=nkey(line)))
    rows = (exact or fuzzy) + vol_level[:3] + dated[:3]
    if not rows:
        if folio_keyed:
            rows = [ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "CLEAR",
                            f"cached mirror (sources/cryptiana/web, snapshot 19 Sept 2026) names no folio of this unit; terms {terms}")]
        elif not u.vols and u.ids and d and who:
            rows = [ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "CLEAR",
                            f"the unit is keyed by {sorted(u.ids)[0].split(':')[0]}, which the pages do not index: its date with "
                            f"a correspondent's name was searched, no line (snapshot 19 Sept 2026)")]
        else:
            rows = [ctx.row(item, "plaintext", "3-tomokiyo", "mirror", "UNCHECKED",
                            f"the unit has no folio or R-id: the folio-keyed search could not run (volume/date terms {terms} "
                            "found nothing classed)")]
    return rows


def decode_listing(ctx, item, rid):
    num, rows, seen = rid[1:], [], set()
    bases = portal_dirs(ctx, "decode-listing", ["sources/decode"])
    for path in walk_files(bases, exts=(".tsv",)):
        for r in read_tsv(open(path, encoding="utf-8", errors="replace").read()):
            if str(r.get("id") or "").strip() != num or "status" not in r:
                continue
            st, pages = r.get("status") or "", r.get("number_of_pages") or r.get("pages") or ""
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


def slug_keywords(ctx, item):
    kw = {w for w in re.split(r"[-_]", ctx.slug) if len(w) >= 5 and w.isalpha() and w not in GENERIC_SLUG}
    kw |= {w for w in names(item.get("sender")) | names(item.get("recipient")) if len(w) >= 5}
    years = set(re.findall(r"(?<!\d)1[4-9]\d\d(?!\d)", ctx.slug))
    d = parse_date(item.get("date"))
    if d:
        years.add(str(d.year))
    return kw, years


def solver_caches(ctx, item, u, terms):
    rows, dirs = [], []
    for p in portal_rows(ctx, "solver-repo") or [{"portal": "solver", "cache_paths": "sources/cyphersolver sources/bourdeau"}]:
        paths = [os.path.join(ctx.root, x) for x in (p.get("cache_paths") or "").split()]
        have = [x for x in paths if os.path.isdir(x)]
        if not have and not ctx.a.clone:
            rows.append(ctx.row(item, "plaintext", "3-solver", f"registry:{p.get('portal')}", "UNCHECKED-NET",
                                f"{p.get('portal')} ({p.get('source') or 'solver repository'}): no cache on disk, not "
                                "searched; pass --clone <local clone> to search it"))
        dirs += have
    dirs += [c for c in ctx.a.clone if os.path.isdir(c)]
    if not dirs:
        return rows + [ctx.row(item, "plaintext", "3-solver", "caches", "UNCHECKED", "no solver-repository cache or clone on disk")]
    keyable = bool(terms) and bool(u.leaves or u.canvases or u.ids)
    if not keyable:
        rows.append(ctx.row(item, "plaintext", "3-solver", "caches", "UNCHECKED",
                            "the unit has no folio, canvas, R-id or pointer: solver caches were not searched by unit "
                            "(a folder named for this target is still reported below)"))
    pat = re.compile(r"(?<![0-9A-Za-z])(?:%s)(?![0-9])" % "|".join(map(re.escape, terms))) if terms else None
    hits, ours, folders_hit = [], None, set()
    for path in walk_files(dirs):
        text = open(path, encoding="utf-8", errors="replace").read()
        base = os.path.basename(path)
        if not keyable or not (pat.search(text) or pat.search(base)):
            continue
        folder = os.path.dirname(path)
        cvols = set()
        for p in glob.glob(os.path.join(folder, "*")):
            if re.search(r"profile\.json|NOTES\.md$|README\.md$", p):
                cvols |= sm.volume_keys(open(p, encoding="utf-8", errors="replace").read()[:20000])
        named = sm.match(u, base, ctx.multi_volume, context_vols=cvols) == "exact"
        if not named:
            for line in text.splitlines():
                if pat.search(line) and sm.match(u, line, ctx.multi_volume, context_vols=cvols) == "exact":
                    named = True
                    break
        if not named:
            continue
        rel = os.path.relpath(path, ctx.root) if path.startswith(ctx.root) else path
        when = (re.search(r"20\d\d-\d\d-\d\d", path) or [""])[0]
        ctxt = text[:20000] + " ".join(open(p, encoding="utf-8", errors="replace").read()[:20000]
                                       for p in glob.glob(os.path.join(folder, "*")) if re.search(r"profile\.json|NOTES\.md$", p))
        if re.search(r"cipher-lab|NoAutopilot|issue\s*#?\d+", ctxt, re.I):
            v, ev = "CONTEXT", "copies or cites our work, excluded"
        elif re.search(r"reading|decipher|plaintext|decrypt", base, re.I):
            ours = our_first_reading(ctx) if ours is None else ours
            v = "CONTEXT" if (ours and when and ours < when) else "KNOWN"
            ev = f"solver reading file (snapshot {when or '?'}; ours earliest {ours or 'none'})"
        else:
            v, ev = "CONTEXT", "duplicate-effort-risk (catalogue/planning line, not a reading)"
        folders_hit.add(folder)
        hits.append(ctx.row(item, "plaintext", "3-solver", rel, v, f"{ev}: {rel}"))
    kw, years = slug_keywords(ctx, item)
    seen = set()
    for d0 in dirs:
        for dp, dn, fs in os.walk(d0):
            dn[:] = [x for x in dn if x not in (".git", "restricted", "img", "images")]
            name = os.path.basename(dp).lower()
            if dp in folders_hit or dp in seen or not any(k in name for k in kw):
                continue
            if years and not any(y in name for y in years) and not any(
                    y in open(os.path.join(dp, f), encoding="utf-8", errors="replace").read()[:20000]
                    for f in fs if f.endswith((".md", ".json")) for y in years):
                continue
            seen.add(dp)
            rel = os.path.relpath(dp, ctx.root) if dp.startswith(ctx.root) else dp
            readings = [f for f in fs if re.search(r"reading|decipher|plaintext|decrypt", f, re.I)]
            v = "LEAD" if (readings and not (u.leaves or u.canvases)) else "CONTEXT"
            hits.append(ctx.row(item, "plaintext", "3-solver", rel, v,
                                f"solver folder named for this target ({rel}; {len(readings)} reading file(s)): "
                                + ("open them, the unit has no folio to key on" if v == "LEAD" else "duplicate-effort-risk")))
    if hits:
        return rows + hits
    if keyable:
        rows.append(ctx.row(item, "plaintext", "3-solver", "caches", "CLEAR",
                            "no cached solver file names this unit: " + ", ".join(os.path.relpath(d, ctx.root) if d.startswith(ctx.root) else d for d in dirs)))
    return rows


# ------------------------------------------------------------------ check 4: editions (and G3 phrases)

def load_editions(root):
    """prior_editions.tsv rows, the last row per edition_id winning (the file is append-only)."""
    return list({r.get("edition_id"): r for r in registry(root, "prior_editions.tsv")}.values())


def names(s):
    return {w for w in pc.norm(s or "").split() if len(w) >= 4 and w not in PARTICLES}


def edition_matches(ed, item, slug):
    d = parse_date(item.get("date"))
    y = d.year if d else None
    try:
        lo, hi = int((ed.get("date_from") or "0")[:4] or 0), int((ed.get("date_to") or "9999")[:4] or 9999)
    except ValueError:
        lo, hi = 0, 9999
    if y is not None and not lo <= y <= hi:
        return False
    if any(fnmatch.fnmatch(slug, p) for p in (ed.get("match_slugs") or "").split() if p):
        return True
    who = names(" ".join(item.get(k, "") for k in ("sender", "recipient", "office")))
    return bool(who & names((ed.get("correspondents") or "").replace(";", " ")))


def date_variants(d, calendar=""):
    """[(date, label)]: d +-1 day, plus the other calendar style for 1582-1752 (Old/New Style noted)."""
    out = [(d + datetime.timedelta(days=k), "as written") for k in (-1, 0, 1)]
    if 1582 <= d.year <= 1752:
        shift = 10 if d.year < 1700 else 11
        styles = {"os": [shift], "ns": [-shift]}.get((calendar or "").lower(), [shift, -shift])
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
    idx, clean, missing = djvu_index(ctx.root, ctx.a.cache), [], []
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
            if not path and not ctx.net:
                missing.append(ident)
                continue
            if not path:      # one row per volume online; offline one row naming every route, reused only route by route
                rows.append(ctx.row(item, "plaintext", "4-editions", f"net:ia:{ident}", "UNCHECKED-NET",
                                    f"{title} ({ident}): djvu text not fetched ({why}); lending-only volumes need the "
                                    "be-api snippet route (v2)", net=True))
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
        r = ctx.row(item, "plaintext", "4-editions", "not-cached", "UNCHECKED-NET",
                    f"not on disk ({' '.join(missing)}); --network fetches the djvu text")
        r["_net_routes"] = [f"net:ia:{i}" for i in missing]
        rows.append(r)
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


def phrase_shown(ctx, p):
    """A decoded phrase as written to the public prior-work.tsv: a hash for a folder under RESTRICTED.md."""
    return f"sha1:{hashlib.sha1(p.encode()).hexdigest()[:10]}" if ctx.restricted else p


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
        ent = f"{len(shared)} shared entities" if ctx.restricted else f"shared entities {sorted(shared)[:6]}"
        rows.append(ctx.row(item, "plaintext", "6-g3", f"ia:{ident}", v,
                            f"{ed['title']} ({ident}): '{phrase_shown(ctx, p)}' {n} exact/{near} near; within +-3 days: "
                            f"{dated}; {ent}", query=phrase_shown(ctx, p), control="hit" if control_ok else "none",
                            hits=n or near))
    if not rows:
        rows.append(ctx.row(item, "plaintext", "6-g3", f"ia:{ident}", "CLEAR" if control_ok else "UNCHECKED",
                            f"{ed['title']} ({ident}): {len(ph)} decoded phrases, no hit" + ("" if control_ok else "; no control hit")))
    return rows


G3_RANK = {"SUBSTANCE": 3, "LEAD": 2, "UNCHECKED-NET": 1, "CLEAR": 0}


def check_g3(ctx, item, reading_path):
    phrases = reading_phrases(open(reading_path, encoding="utf-8", errors="replace").read())
    if not phrases[0]:
        return [ctx.row(item, "plaintext", "6-g3", "phrases", "UNCHECKED", f"no distinctive phrase extracted from {reading_path}")]
    rows = check_editions(ctx, item, phrases=phrases)
    q = " | ".join(phrase_shown(ctx, p) for p in phrases[0])
    out = []
    if ctx.net:
        pc.check_ia_global(phrases[0], ctx.net, out)
        pc.check_gbooks(phrases[0], set(), ctx.net, out)
    for src in ("ia-global", "gbooks"):
        if not ctx.net:
            rows.append(ctx.row(item, "plaintext", "6-g3", f"net:{src}", "UNCHECKED-NET",
                                f"G3 {src} phrase search not run (offline); run with --network before any class or SO row",
                                query=q))
            continue
        best = None
        for p, s, res, det, url in [o for o in out if o[1] == src]:
            v = "UNCHECKED-NET" if res.startswith("not searched") else ("CLEAR" if res.startswith("no hits") else
                ("SUBSTANCE" if len(phrases[1] & set(pc.norm(det).split())) >= 2 else "LEAD"))
            ev = f"'{phrase_shown(ctx, p)}' {src}: {res}" + ("" if ctx.restricted else f"; {det}")
            if best is None or G3_RANK[v] > G3_RANK[best[0]]:
                best = (v, ev)
        v, ev = best or ("UNCHECKED-NET", f"{src}: no result rows")
        rows.append(ctx.row(item, "plaintext", "6-g3", f"net:{src}", v, f"most blocking of {len(phrases[0])} phrases: {ev}",
                            query=q, net=True))
    return rows


# ------------------------------------------------------------------ check 5: civil-war adapter

def hdr_time(s):
    """Minutes after midnight of a ledger header's hour ('3.30 PM', '330 P. M', '10 am', '12 M'), or None."""
    m = TIME_RE.search(s or "")
    if not m:
        return None
    h, mm, ap, noon = m.groups()
    h, mm = int(h), int(mm or 0)
    if h > 12 or mm > 59:
        return None
    if noon:
        return 12 * 60 + mm
    return (h % 12 + (12 if ap.lower() == "p" else 0)) * 60 + mm


def load_eckert(ctx):
    path = os.path.join(ctx.root, "ciphers", "eckert-1864", "entries_mssEC19.py")
    spec = importlib.util.spec_from_file_location("entries_mssEC19", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def ledger_blocks(ctx, mod):
    """Already-read ledger entries from ciphertext*.txt headers, read through State (so --ref is honoured):
    [{id, ptr, dm, time, entry}] -- entry from 'row P/N' when the header names it."""
    out = []
    folders = ["ciphers/eckert-1864"] + ([ctx.folder] if ctx.folder != "ciphers/eckert-1864" else [])
    for f in folders:
        for fn in ("ciphertext.txt", "ciphertext-no2.txt", "ciphertext-no9.txt"):
            for l in lines_of(ctx.state, f"{f}/{fn}"):
                m = re.match(r"### (\S+) \| (.*)", l)
                if not m:
                    continue
                rest = m.group(2)
                pm = re.search(r"\|\s*(\d{4,5})\s*\||\bpointer\s*(\d{4,5})", rest)
                if not pm:
                    continue
                ptr = pm.group(1) or pm.group(2)
                tail = re.sub(r"^\s*\|?\s*", "", rest[pm.end():])
                dm = None
                dd = re.match(r"\s*(\d{1,2})(?:st|nd|rd|th)?\s+([A-Za-z]{3,})", tail)
                if dd:
                    dm = mod.day_month(f"{dd.group(2)} {dd.group(1)}")
                if dm is None:
                    dm = mod.day_month(tail)
                rowm = re.search(r"\brow (\d{4,5})/(\d+)", rest)
                out.append(dict(id=m.group(1), ptr=ptr, dm=dm, time=hdr_time(tail),
                                entry=int(rowm.group(2)) if rowm and rowm.group(1) == ptr else None, src=f"{f}/{fn}"))
    return out


def page_entries(ctx, mod, ptr):
    """(entries, source) for a pointer: the cached holder JSON ('transc' or 'text') segmented, else entries-mssEC19.tsv."""
    for f in [ctx.folder, "ciphers/eckert-1864"]:
        for rel in [p for p in ctx.state.ls(f"{f}/sources") if os.path.basename(p) == f"p{ptr}.json"]:
            try:
                j = json.loads(ctx.state.read(rel) or "")
            except ValueError:
                continue
            text = (j.get("transc") or j.get("text") or "").strip()
            if not text:
                return [], rel, j
            return mod.segment([(int(ptr), j.get("title"), text)]), rel, j
    rows = [r for r in read_tsv(ctx.state.read("ciphers/eckert-1864/entries-mssEC19.tsv")) if r.get("pointer") == ptr]
    ents = [{"entry_on_page": int(r["entry_on_page"]), "header": r.get("header") or "", "lines": []}
            for r in rows if str(r.get("entry_on_page") or "").isdigit()]
    return ents, ("ciphers/eckert-1864/entries-mssEC19.tsv" if ents else None), None


def resolve_entry(mod, ents, dm, time=None):
    """The one entry on the page with this date (and header hour), else None."""
    c = [e for e in ents if dm and mod.day_month(e["header"]) == dm]
    if time is not None and len(c) > 1:
        t = [e for e in c if hdr_time(e["header"]) == time]
        c = t or c
    return c[0]["entry_on_page"] if len(c) == 1 else None


def civil_war(ctx, item, u, step):
    rows = []
    try:
        mod = load_eckert(ctx)
        codes = mod.load_vocab()
    except Exception as e:      # noqa: BLE001 -- any failure means the adapter did not run
        return [ctx.row(item, "plaintext", "5-civil-war", "adapter", "UNCHECKED", f"entries_mssEC19 not usable: {e}")]
    ptr, entry = norm_ptr(item.get("ptr"))
    entry = int(entry) if entry else None
    d = parse_date(item.get("date"))
    dm = (d.month, d.day) if d else None
    ents, src, j = page_entries(ctx, mod, ptr) if ptr else ([], None, None)
    blocks = ledger_blocks(ctx, mod)
    own_label = item["item_id"] if sm.LABEL_RE.fullmatch(item.get("item_id", "")) else None
    if step in ("read", "decode", "transcribe"):
        for b in blocks:
            if own_label and b["id"] == own_label:
                rows.append(ctx.row(item, "step", "5-civil-war", f"known_blocks:{b['id']}", "DONE",
                                    f"already read as {b['id']} ({b['src']}, pointer {b['ptr']})"))
                continue
            if not ptr or b["ptr"] != ptr:
                continue
            be = b["entry"] if b["entry"] is not None else resolve_entry(mod, ents, b["dm"], b["time"])
            ie = entry if entry is not None else resolve_entry(mod, ents, dm)
            if be is not None and ie is not None:
                if be == ie:
                    rows.append(ctx.row(item, "step", "5-civil-war", f"known_blocks:{b['id']}", "DONE",
                                        f"already read as {b['id']} (pointer {ptr}, entry {be})"))
            elif dm and b["dm"] == dm:
                rows.append(ctx.row(item, "step", "5-civil-war", f"known_blocks:{b['id']}", "LEAD",
                                    f"done-candidate: {b['id']} was read on pointer {ptr} the same day ({d}); the entry is not "
                                    f"resolved (block entry {be}, this item {ie}): give ptr {ptr}/N"))
    if not src:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", "holder-transcription", "UNCHECKED-NET",
                            f"no cached Huntington transcription for pointer {ptr or '?'} (tools/huntington_transc.py)"))
        return rows
    if j is not None and not ents:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", src, "CONTEXT",
                            f"the holder's record for pointer {ptr} carries no transcription text: the clear-share route has nothing to test"))
        return rows
    if j is None:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", "holder-transcription", "UNCHECKED-NET",
                            f"pointer {ptr} is segmented in {src} but its transcription JSON is not cached: the clear-share "
                            "test cannot run (tools/huntington_transc.py)"))
        return rows
    if entry is not None:
        ent = next((e for e in ents if e["entry_on_page"] == entry), None)
    else:
        cands = [e for e in ents if dm and mod.day_month(e["header"]) == dm]
        if len(cands) > 1:
            rows.append(ctx.row(item, "plaintext", "5-civil-war", src, "LEAD",
                                f"ambiguous entry: {len(cands)} entries on pointer {ptr} are dated {d} "
                                f"({'; '.join(e['header'][:40] for e in cands)}): give ptr {ptr}/N"))
            return rows
        ent = cands[0] if cands else None
    if ent is None:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", src, "LEAD",
                            f"pointer {ptr} transcription cached but no entry matches {('entry ' + str(entry)) if entry is not None else d}"))
        return rows
    toks = mod.toks(" ".join(ent["lines"]))
    code = [t for t in toks if t in codes]
    if not code:
        v = "KNOWN" if len(toks) >= 3 else "CONTEXT"
        rows.append(ctx.row(item, "plaintext", "5-civil-war", src, v,
                            ("clear in the holder's own transcription (step 0 skip): " if v == "KNOWN" else
                             "entry too short to judge: ") + f"{ent['header']} | {' '.join(ent['lines'])[:120]}"))
    else:
        rows.append(ctx.row(item, "plaintext", "5-civil-war", src, "KNOWN-PART",
                            f"clear words public in the holder transcription, {len(set(code))} code word(s) not: {ent['header']}",
                            residue="code words: " + ", ".join(sorted(set(code)))))
    ctx.leaf_answered = ctx.row(item, "plaintext", "2-leaf", src, "CLEAR",
                                f"leaf look answered by the holder's full-page transcription ({src}); later pencil ignored")
    for r in read_tsv(ctx.state.read("ciphers/eckert-1864/entries-mssEC19.tsv")):
        if r.get("pointer") == ptr and r.get("entry_on_page") != str(ent["entry_on_page"]) and \
                (r.get("already_read") or (r.get("or_hit") or "none") != "none"):
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

def prior_rows(ctx, name="prior-work.tsv"):
    path = os.path.join(ctx.root, ctx.folder, name)
    return read_tsv(open(path, encoding="utf-8").read()) if os.path.isfile(path) else []


def apply_records(ctx, rows):
    """--record answers replace any row that is not DONE; an offline run reuses a still-valid network row only for the
    same row id (same check, route and query)."""
    old = prior_rows(ctx)
    rec = {r["route"]: r for r in old if r.get("check") == "record"}
    for r in rows:
        a = rec.get(r["row_id"])
        if a and r["verdict"] != "DONE":
            r.update(verdict=a["verdict"], evidence=safe(f"recorded {a['utc']}: {a['evidence']}")[:200])
            if a["verdict"] == "DONE":
                r["scope"] = "step"
    if not ctx.net:
        today = ctx.today.isoformat()
        valid = {}
        for o in old:
            if (o.get("route") or "").startswith("net:") and (o.get("valid_until") or "") >= today and \
                    o.get("check") != "record" and (o.get("requests_by_host") or ""):
                valid[o.get("row_id")] = o          # the newest row per id
        for r in rows:
            routes = r.get("_net_routes")
            if r["verdict"] != "UNCHECKED-NET":
                continue
            if routes:              # an offline row standing for several routes: reused only when every route is cached
                got = [valid.get(rid_of(r["item_id"], r["check"], rt, "")) for rt in routes]
                if all(got):
                    best = max(got, key=lambda o: NET_RANK.get(o["verdict"], 0))
                    r.update(verdict=best["verdict"], evidence=safe(
                        f"cached network rows ({len(got)} route(s), most blocking shown) {best['utc']}: {best['evidence']}")[:200])
            elif r["row_id"] in valid:
                o = valid[r["row_id"]]
                r.update(verdict=o["verdict"], evidence=safe(f"cached network row {o['utc']}: {o['evidence']}")[:200])
    for r in rows:
        r.pop("_net_routes", None)
    return rows


def dedupe(rows):
    """Rows with the same id (one bullet copied into several sections) once, the newest location kept, others listed."""
    by, order = {}, []
    for r in rows:
        if r["row_id"] in by:
            first = by[r["row_id"]]
            first.setdefault("_also", []).append(first["route"])
            first["route"] = r["route"]
        else:
            by[r["row_id"]] = r
            order.append(r["row_id"])
    out = []
    for rid in order:
        r = by[rid]
        also = r.pop("_also", [])
        if also:
            r["evidence"] = safe(f"(also at {', '.join(also[:4])}{' ...' if len(also) > 4 else ''}) " + r["evidence"])[:200]
        out.append(r)
    return out


def decide(rows, step, consumer, strict, g3):
    steps = [r for r in rows if r["scope"] == "step"]
    text = [r for r in rows if r["scope"] != "step"]
    block = {"LOOK", "LEAD", "UNCHECKED"} | ({"UNCHECKED-NET"} if strict or g3 else set())
    if step not in NEVER_DONE and any(r["verdict"] == "DONE" for r in steps):
        return 3, "the step is DONE"
    works = step in WORKS_TEXT or g3
    if (works or step in KNOWN_INPUT) and any(r["verdict"] == "KNOWN" for r in text):
        if not consumer and step not in KNOWN_INPUT:
            return 2, "KNOWN, no consumer (pass --known-answer item:<unread id> or gate:<name>)"
        owed = [r for r in steps if r["verdict"] in block]
        if owed:
            return 4, "owed before this step (the text is KNOWN, but): " + ", ".join(sorted({f"{r['verdict']} {r['row_id']}" for r in owed}))
        return 0, f"KNOWN, known-answer work for {('consumer ' + consumer) if consumer else 'step ' + step}"
    owed = [r for r in steps + (text if works else []) if r["verdict"] in block]
    if owed:
        return 4, "owed before this step: " + ", ".join(sorted({f"{r['verdict']} {r['row_id']}" for r in owed}))
    residue = sorted({r["residue"] for r in text if r.get("residue")})
    return 0, "proceed on the residue: " + ("; ".join(residue) if residue else "whole item (no KNOWN-PART scope)")


def append_rows(ctx, rows):
    if ctx.a.dry_run:
        return
    path = os.path.join(ctx.root, ctx.folder, "prior-work.tsv")
    new = not os.path.isfile(path)
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "a", encoding="utf-8") as f:
        if new:
            f.write("# tools/prior_work.py rows, append-only (a search result and a routing verdict, never a novelty class)\n")
            f.write("\t".join(COLUMNS) + "\n")
        for r in rows:
            f.write("\t".join(str(r.get(c, "")).replace("\t", " ").replace("\n", " ") for c in COLUMNS) + "\n")


def write_look(ctx, item_id, look, answered_by=None):
    """look.tsv is append-only: a row is added when an entry's status changes (owed -> answered), never removed."""
    if ctx.a.dry_run:
        return
    path = os.path.join(ctx.root, ctx.folder, "look.tsv")
    latest = {}
    for r in prior_rows(ctx, "look.tsv"):
        latest[tuple(r.get(c) or "" for c in ("item_id", "role", "folio", "canvas", "image"))] = r
    new = []
    if answered_by:
        for k, r in latest.items():
            if k[0] == item_id and (r.get("status") or "") == "owed":
                new.append([ctx.utc] + [r.get(c) or "" for c in LOOK_COLS[1:-1]] + [f"answered by {answered_by}"])
    for x in look:
        k = (x[0], x[2], x[3], x[4], x[5])
        if (latest.get(k) or {}).get("status") != x[-1]:
            new.append([ctx.utc] + x)
    if not new:
        return
    fresh = not os.path.isfile(path)
    with open(path, "a", encoding="utf-8") as f:
        if fresh:
            f.write("# tools/prior_work.py leaf looks, append-only: the newest row per (item, role, folio, canvas, image) is current\n")
            f.write("\t".join(LOOK_COLS) + "\n")
        for r in new:
            f.write("\t".join(str(c).replace("\t", " ") for c in r) + "\n")


class ItemNet:
    """The run's one print_check.Net with a per-item request budget on top (hosts blocked earlier stay skipped)."""

    def __init__(self, net, cap):
        self.net, self.cap, self.start = net, cap, dict(net.count)

    @property
    def offline(self):
        return getattr(self.net, "offline", False)

    @property
    def status(self):
        return self.net.status

    @property
    def count(self):
        return {h: n - self.start.get(h, 0) for h, n in self.net.count.items() if n - self.start.get(h, 0)}

    def get(self, url, **kw):
        if sum(self.count.values()) >= self.cap:
            return None, "max-requests (item) reached"
        return self.net.get(url, **kw)

    def json(self, url, **kw):
        body, st = self.get(url, **kw)
        if body is None:
            return None, st
        if isinstance(body, (dict, list)):
            return body, st
        try:
            return json.loads(body), "ok"
        except (ValueError, TypeError):
            return None, "not JSON"


def run_item(ctx, item, step):
    u, rows = item_unit(item), []
    ctx.unit_pages = ctx.leaf_answered = None
    ctx.net = ItemNet(ctx.session_net, ctx.a.max_requests) if ctx.session_net else None
    if ctx.slug.startswith("eckert-") and (item.get("ptr") or item.get("kind") == "ledger-entry"):
        rows += civil_war(ctx, item, u, step)
    rows += check_own(ctx, item, u, step)
    if ctx.a.reading:
        rows += check_g3(ctx, item, ctx.a.reading)
    else:
        rows += check_portals(ctx, item, u)
        rows += check_active_edition(ctx, item, u)
        rows += check_editions(ctx, item)
    leaf_rows, look = check_leaf(ctx, item, u, step)
    rows += leaf_rows
    if ctx.net:
        hosts = ";".join(f"{h}:{n}" for h, n in ctx.net.count.items())
        for r in rows:
            r["requests_by_host"] = hosts or "none"
    rows = dedupe(apply_records(ctx, rows))
    lrow = next((r for r in rows if r["check"] == "2-leaf" and r["route"] == "leaf-look"), None)
    answered_by = None
    if lrow and lrow["verdict"] != "LOOK":
        look = [x[:-1] + [f"answered {lrow['verdict']} (recorded)"] for x in look]
    elif not look:
        ans = next((r for r in rows if r["check"] == "2-leaf" and r["verdict"] in STRENGTH), None)
        answered_by = ans["row_id"] if ans else None
    code, why = decide(rows, step, ctx.a.known_answer, ctx.a.strict, bool(ctx.a.reading))
    append_rows(ctx, rows)
    if look or answered_by:
        write_look(ctx, item["item_id"], look, answered_by)
    return code, why, rows


def holds(rows):
    spec = {}
    gen = {}
    for r in rows:
        if r["verdict"] in SPECIFIC:
            spec[r["verdict"]] = spec.get(r["verdict"], 0) + 1
        elif r["verdict"] in GENERIC:
            gen[r["verdict"]] = gen.get(r["verdict"], 0) + 1
    return spec, gen


def report(ctx, item, step, code, why, rows):
    spec, gen = holds(rows)
    if ctx.a.json:
        print(json.dumps(dict(item_id=item["item_id"], step=step, exit=code, why=why, specific=spec, generic=gen, rows=rows),
                         ensure_ascii=False))
        return
    when = ctx.state.when[:16] if ctx.state.when else "working tree"
    desc = "; ".join(f"{k}={item[k]}" for k in ("shelfmark", "folio", "canvas", "decode", "ptr", "wvo", "date") if item.get(k))
    print(f"prior_work {ctx.slug} item {item['item_id']} ({desc or 'no identity fields'}) step {step} @ {ctx.a.ref} "
          f"{ctx.state.commit[:9] or '-'} ({when})")
    if ctx.state.fallback:
        print(f"  warning: ref {ctx.a.ref} does not resolve; the working tree was read instead (own work UNCHECKED)")
    for r in rows:
        print(f"  {r['scope']:<9} {r['verdict']:<13} {r['check']:<13} [{r['row_id']}] {r['evidence']}")
    fmt = lambda d: ", ".join(f"{k} {v}" for k, v in sorted(d.items())) or "none"
    print(f"  holds: specific {sum(spec.values())} ({fmt(spec)}); generic {sum(gen.values())} ({fmt(gen)})")
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
    """[(file line number, row dict)] for every markdown table row."""
    rows, head = [], None
    for n, line in enumerate(text.splitlines(), 1):
        if not line.startswith("|"):
            head = None
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if head is None:
            head = [c.lower() for c in cells]
        elif not set("".join(cells)) <= set("-: "):
            rows.append((n, dict(zip(head, cells))))
    return rows


def tsv_rows(text):
    """[(file line number, row dict)]; comment lines skipped, ragged rows tolerated."""
    head, out = None, []
    for n, line in enumerate(text.splitlines(), 1):
        if not line.strip() or line.startswith("#"):
            continue
        cells = line.split("\t")
        if head is None:
            head = cells
            continue
        out.append((n, dict(zip(head, cells + [""] * (len(head) - len(cells))))))
    return out


TAG_RE = re.compile(r"\b[A-Z][A-Z0-9]+(?:-[A-Z0-9]+)+\b")
REGISTER_COLS = ("next_step", "parallel", "sibling", "cheap_step", "step")


def step_part(text):
    """The step a register cell names: the part after its last 'next:' when there is one, parentheticals (history:
    'settled 2 Oct 2026, NEXT-LIN') removed."""
    m = list(re.finditer(r"(?:cheapest\s+)?next(?:\s+step)?\s*:", text, re.I))
    return re.sub(r"\([^)]*(?:\)|$)", " ", text[m[-1].end():] if m else text)


def step_type_of(text):
    for t in STEP_PRIORITY:
        if STEP_RE[t].search(text):
            return t
    return None


def register_dates(text):
    """Dates a register row names ('5/13 July 1592', '7 Sept 1572')."""
    out = []
    names = {w: m for m, ws in MONTHS.items() for w in ws.split()}
    for m in re.finditer(r"\b(\d{1,2}(?:\s*(?:/|or|and|&|,)\s*\d{1,2})*)\s+([A-Za-z]{3,9})\.?\s+(1[4-9]\d\d)\b", text or ""):
        mo = names.get(m.group(2).lower()) or names.get(m.group(2).lower()[:3])
        for dd in re.findall(r"\d{1,2}", m.group(1)) if mo else []:
            try:
                out.append(datetime.date(int(m.group(3)), mo, int(dd)))
            except ValueError:
                pass
    return out


def step_verdict(ctx, slug, text, since, ident=""):
    """DONE / LEAD / CLEAR for one register row's step text in folder slug (own work only). DONE needs the step's verb
    class and its unit (or its job tag) in a done bullet; keyword overlap alone is a LEAD. ident is the row's identity
    cells (sibling, where): their volumes, folios and dates key the premise and plaintext checks."""
    st, step = ctx.state, step_part(text)
    k, tags = sm.parse(text + " " + ident), set(TAG_RE.findall(step))
    for r in read_tsv(st.read("WORK-QUEUE.tsv")):
        if r.get("job_id") in tags and str(r.get("status") or "").startswith("done"):
            return "DONE", f"WORK-QUEUE {r['job_id']} {r['status']}"
    stype = step_type_of(step)
    kw, u, lead = nsf.keywords(step), sm.Keys(k.vols, k.leaves, k.canvases, k.ids), None
    keyed = bool(k.leaves or k.ids or k.canvases)
    for fn in ("NOTES.md", "ITERATE.md", "HYPOTHESES.md"):
        for i, line in enumerate(lines_of(st, f"ciphers/{slug}/{fn}"), 1):
            marked = DONE_MARK.search(line)
            if not marked:
                if stype == "lookup" and keyed and LOOKUP_DONE.search(line) and not OPEN_WORDS.search(line) \
                        and sm.match(u, line) == "exact":
                    lead = lead or f"done-candidate (lookup answered in prose) {fn}:{i} {line.strip()}"
                continue
            hits, share = nsf.overlap(kw, line)
            named = keyed and sm.match(u, line) == "exact"
            tagged = bool(tags & set(TAG_RE.findall(line)))
            verb = stype is not None and bool(STEP_RE[stype].search(done_part(line)))
            if stype in ("read", "decode", "transcribe") and verb and not step_done(stype, line):
                verb = False
            open_ = OPEN_WORDS.search(done_part(line))
            if not open_ and ((tagged and verb) or (named and verb and len(hits) >= 2)):
                return "DONE", f"{fn}:{i} {line.strip()}"
            if not lead and (named or tagged or (len(hits) >= nsf.MIN_HITS and share >= nsf.MIN_SHARE)):
                why = "other step or open" if (named or tagged) else "keyword overlap"
                lead = f"done-candidate ({why}) {fn}:{i} {line.strip()}"
    for l in lines_of(st, "ROOM.md")[-2000:]:
        m = nsf.ROOM_RE.match(l)
        if m and has_slug(slug, l) and re.search(r"\bdone\b", l) and m.group(1) > since and nsf.is_stale(kw, m.group(3))[0]:
            lead = lead or f"done-candidate ROOM {l}"
    dates = register_dates(text + " " + ident)
    real = {v for v in k.vols if not v.startswith("hint:")}
    if not lead and dates and real:     # the row's premise already answered ('the finding aid lists no letters of 5 or 13 July')
        for fn in ("NOTES.md", "AUDIT.md"):
            for i, ptext, _, _ in paragraphs(lines_of(st, f"ciphers/{slug}/{fn}")):
                if LOOKUP_DONE.search(ptext) and not OPEN_WORDS.search(ptext) and (real & sm.volume_keys(ptext)) and \
                        any(date_in(ptext, d) for d in dates):
                    lead = f"done-candidate (premise or lookup answered, date-keyed) {fn}:{i} {ptext.strip()}"
                    break
            if lead:
                break
    if not lead and keyed and stype in ("transcribe", "read", "decode", "crop", "align", "key"):
        multi = len(sm.volume_keys(st.read(f"ciphers/{slug}/NOTES.md") or "")) > 1
        mine, _ = leaf_records(ctx, u, folder=f"ciphers/{slug}", multi_volume=multi)
        kn = [r for r in mine if r[0] in ("KNOWN", "KNOWN-PART")]
        if kn:
            v, loc, seg = max(kn, key=lambda r: STRENGTH[r[0]])
            lead = f"plaintext {v} on file (gloss record), the step reads known text: {loc} {seg.strip()}"
    return ("LEAD", lead) if lead else ("CLEAR", "no done evidence for this step at current state")


def run_register(ctx, path, columns):
    text = open(path, encoding="utf-8", errors="replace").read()
    rows = md_tables(text) if path.endswith(".md") else tsv_rows(text)
    head = set(rows[0][1].keys()) if rows else set()
    if not columns:
        columns = [c for c in REGISTER_COLS if c in head]
        print(f"# step columns (autodetected): {','.join(columns) or 'none found'}")
    missing = [c for c in columns if c not in head]
    if missing and rows:
        print(f"# warning: column(s) {', '.join(missing)} not in {os.path.basename(path)} (has: {', '.join(sorted(head))})")
    rel = os.path.relpath(os.path.abspath(path), ctx.root)
    since = (ctx.state._git("log", "-1", "--format=%cd", "--date=format:%Y-%m-%d %H:%M", "--", rel) or "").strip() or "0000"
    print("line\tslug\tverdict\tevidence")
    for n, r in rows:
        slug = ""
        for c in ("folder", "target", "slug"):
            tok = (re.findall(r"[a-z0-9][a-z0-9-]{3,}", r.get(c, "") or "") or [""])[0]
            if tok and (os.path.isdir(os.path.join(ctx.root, "ciphers", tok)) or ctx.state.ls(f"ciphers/{tok}/NOTES.md")):
                slug = tok
                break
        if not slug or (ctx.slug not in ("-", "all") and slug != ctx.slug):
            continue
        step = " ".join(r.get(c, "") or "" for c in columns)
        ident = " ".join(r.get(c, "") or "" for c in ("sibling", "where") if c not in columns)
        v, ev = step_verdict(ctx, slug, step, since, ident) if step.strip() else \
            ("UNCHECKED", f"empty step cells ({','.join(columns)})")
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
        for mt in sm.mentions(line):
            if mt.kind != "leaf":
                continue
            vol = mt.vol if (mt.vol and not mt.vol.startswith("hint:")) else lv[0]
            for n, side in sorted(mt.leaves):
                if side or not any(n == x and s for x, s in mt.leaves):
                    items.append(item_from_spec(f"shelfmark={vol};folio={n}{side}"))
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
    try:
        res = json.loads(ctx.state.read("status.json") or "{}").get("results", [])
    except ValueError:
        res = []
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
    print(f"derive {ctx.slug}: {len(rows)} proposed row(s) -> {os.path.relpath(path, ctx.root)} (items.tsv untouched)"
          + (" [dry run: nothing written]" if ctx.a.dry_run else ""))
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
    print(f"{'would record' if ctx.a.dry_run else 'recorded'} {v} for {rowid} in {ctx.folder}/prior-work.tsv"
          + (" [dry run: nothing written]" if ctx.a.dry_run else ""))
    return 0


def aggregate(codes):
    """One exit for several items: the common code, 4 when any item owes work, 3/2 when every item stops, else 5."""
    s = set(codes)
    if len(s) == 1:
        return codes[0]
    if 4 in s:
        return 4
    if s <= {2, 3}:
        return 2
    return 5


def main(argv=None):
    ap = Parser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("slug", help="ciphers/<slug> folder name ('-' with --register for every row)")
    g = ap.add_mutually_exclusive_group(required=True)
    g.add_argument("--item", help="item_id, a row of ciphers/<slug>/items.tsv")
    g.add_argument("--item-spec", help="ad hoc item: 'shelfmark=..;folio=..;canvas=..;date=..;sender=..;recipient=..;decode=R..;ptr=..;kind=..'")
    g.add_argument("--derive", action="store_true", help="propose items.pending.tsv rows (catalogue-only), never items.tsv")
    g.add_argument("--register", metavar="FILE", help="step mode: NEXT-STEPS.tsv, SIBLINGS-*.tsv or LOOSE-ENDS-*.md")
    g.add_argument("--brief", metavar="FILE", help="extract the items a brief names and check each (per-item exit table)")
    g.add_argument("--record", nargs=2, metavar=("ROWID", "ANSWER"), help="answer an owed row (any row that is not DONE)")
    ap.add_argument("--columns", default=None,
                    help="register columns holding the step text (default: autodetected -- next_step,parallel for "
                         "NEXT-STEPS, sibling,cheap_step for SIBLINGS, step for LOOSE-ENDS)")
    ap.add_argument("--step-type", default="read", choices=STEP_TYPES,
                    help="the job's step (default read). audit is DONE when a class already covers the item (a re-audit); "
                         "the second adversarial audit is second-audit; second-audit, upgrade-audit, new-family-audit and "
                         "propagate-revision are never DONE; key and align take KNOWN text as their input")
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
                    help="network downloads go here; a path inside --root is refused")
    ap.add_argument("--max-requests", type=int, default=12, help="network requests per item (default 12)")
    ap.add_argument("--max-session-requests", type=int, default=200, help="network requests for the whole run (default 200)")
    ap.add_argument("--fetch", action="store_true", help="run git fetch origin main before reading (network)")
    ap.add_argument("--json", action="store_true", help="one JSON object per item (exit, why, holds, rows)")
    ap.add_argument("--dry-run", action="store_true", help="write nothing (no prior-work.tsv, look.tsv, pending file or record)")
    ap.add_argument("--root", default=ROOT, help="repository root (default: this checkout; tests pass a fixture repo)")
    ap.add_argument("--ref", default="origin/main", help="ref the target state is read at; WORKTREE reads the checkout itself")
    ap.add_argument("--now", help="fixed UTC clock YYYY-MM-DDTHH:MM for the ROOM claim age (tests)")
    a = ap.parse_args(argv)
    a.slug = a.slug.rstrip("/").removeprefix("ciphers/")
    try:
        guard_path(a.root, "--root")
        for what, p in (("--reading", a.reading), ("--brief", a.brief), ("--register", a.register),
                        ("--or-dir", a.or_dir), ("--cache", a.cache)) + tuple(("--clone", c) for c in a.clone):
            guard_path(p, what)
        rc, rr = os.path.realpath(a.cache), os.path.realpath(a.root)
        if rc == rr or rc.startswith(rr + os.sep):
            raise UsageError(f"--cache {a.cache} is inside --root: network downloads never go into the repository")
    except UsageError as e:
        print(f"prior_work.py: error: {e}", file=sys.stderr)
        return 1
    if a.fetch or a.network:
        subprocess.run(["git", "-C", a.root, "fetch", "-q", "origin", "main"], capture_output=True, timeout=300)
    state = State(a.root, a.ref)
    ctx = Ctx(a, state)
    try:
        if a.reading and a.network and ctx.restricted:
            raise UsageError(f"ciphers/{a.slug} has a RESTRICTED.md: decoded phrases never leave the machine "
                             "(--reading with --network refused; run --reading offline, phrases are logged as hashes)")
        if a.register:
            return run_register(ctx, a.register, [c.strip() for c in (a.columns or "").split(",") if c.strip()])
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
                   and str(r.get("status") or "").startswith("done")]
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
                raise UsageError(f"item {a.item!r} is not a row of ciphers/{a.slug}/items.tsv at {a.ref} (an items.tsv not "
                                 "yet pushed needs --ref WORKTREE; otherwise use --item-spec or --derive)")
        else:
            items = [item_from_spec(a.item_spec)]
    except UsageError as e:
        print(f"prior_work.py: error: {e}", file=sys.stderr)
        return 1
    ctx.session_net = pc.Net(False, a.max_session_requests) if a.network else None
    codes = []
    for item in items:
        code, why, rows = run_item(ctx, item, a.step_type)
        report(ctx, item, a.step_type, code, why, rows)
        codes.append((item["item_id"], code, why))
    final = aggregate([c for _, c, _ in codes])
    if len(codes) > 1 and not a.json:
        print("per-item exits:")
        for iid, c, why in codes:
            print(f"  {iid}\texit {c}\t{why[:120]}")
        print(f"exit {final}: " + {3: "every item is DONE", 2: "every item stops (DONE or KNOWN)",
                                   4: "some item owes a look or read before this step (that item only; proceed on items marked 0)",
                                   0: "every item proceeds",
                                   5: "mixed: proceed only on the items marked 0; items marked 2/3 stop"}[final])
    return final


if __name__ == "__main__":
    sys.exit(main())

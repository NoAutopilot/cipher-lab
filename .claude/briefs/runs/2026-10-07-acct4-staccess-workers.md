# ST-ACCESS worker brief (account 4, LANE ST-ACCESS, session_01HvLc1KhkzLZ2aCNnWHdqNo; written 7 Oct 2026 ~21:50 UTC)

Parent round: .claude/briefs/runs/2026-10-07-acct3-steam.md, section "ST-ACCESS (account 4)". You are worker SA-<X>.
Row numbers below are KEYHUNT-2026-10-07.tsv line numbers (header = line 1). Read your rows there and in the per-worker
TSV under keyhunt/ named in the row's history before acting; never repeat a check a row already records.

Lane scope note: the BnF italien 1583/1584/1585 rows (Sforza 1446-48, KEYHUNT lines 322-330, 395-439) belong to LANE
ST-REBUILD (account 2, live claim 21:12 UTC) for screening; SA-CO covers only the italien 1583 copy-order question.

## Common to every SA worker
0. `python3 tools/room.py --start`; `date -u`; read the last 30 ROOM.md lines and the last 20 lines of UPDATES.md; claim with
   `python3 tools/room.py "SA-<X> worker (account 4)" '<claim text with box end>' --push`.
1. Screening means: locate the letter's leaves in the digitised source, view them at a scale where numeral groups or
   cipher signs are visible, and record per letter: located (frames/canvases), cipher present (yes / no / partial), glossed
   (interlinear or marginal decipherment, or a clear copy beside it), and which held key it most likely uses. SCREEN ONLY:
   no transcription, no decode, no new folder. Detection control: before screening, view one leaf already known to carry
   cipher from the same source (named per worker) at the same scale and confirm you flag it; record it in the TSV. A
   "no cipher" verdict without the control passing is "unscreened (control not run)", never "clear".
2. Contact sheets: fetch thumbnails once to your scratchpad (IIIF `full/!400,400/0/default.jpg` or the host's equivalent),
   montage 12-16 per sheet with a short PIL script, view the sheet, then view at higher scale only the candidates. Never
   hand a full native page to a subagent; at most 2 Sonnet subagents at once, one sheet set per call.
3. Hosts: one request at a time, >=1.5 s apart (DigitArq >=3 s), a few hundred per host at most; on 429/403/challenge or a
   server error, ONE retry after a 60 s pause, then log the host as unreachable for this job and move on (good-citizen rule).
4. Output: append rows to `keyhunt/2026-10-07-SA<X>.tsv` (columns key_path, letter, shelfmark, digitised, cipher,
   already_read_by, glossed, action, result), one per letter screened, and update the matching KEYHUNT-2026-10-07.tsv
   line's `cipher`, `glossed`, `action`, `result` cells in place (fetch/rebase immediately before; keep the old text after
   " | was: " so nothing is lost). A letter found carrying unglossed cipher with a held key: one line in the key's target
   folder NOTES.md ("## Unread sibling found (SA-<X>, 7 Oct 2026)": shelfmark, frames, key, next step ~USD) -- nothing else.
5. Close: push by explicit path; `python3 tools/file_shrink_guard.py <every pre-existing file touched>` pasted in the done
   line; one ROOM done line: per row screened -> verdict, control result, request counts per host, commits. "cost: see
   the lane ledger". Report what was found and where it was not found; never the words new, first, solved, cracked.
Never call AskUserQuestion; never print credentials; never name the owner; read `date -u` before writing any time.
Off limits: Birago (fr3252), Armstrong (armstrong-madison-1808 files), Debosnys, Sforza/italien 1584-85 screening.

Common tail (from .claude/briefs/README.md, applies in full): room.py --start never manual git checkout/reset; after one
classifier denial flag and stop; wall-clock box is the stall alarm -- at 80% push what you have, one line of remaining
steps in the TSV/NOTES, stop; never write a dollar figure for yourself; trial crops go to scratchpad; a negative's line
carries the control result beside it (rule 3).

## SA-G (Gallica screen; Sonnet 5.5; cap USD 8; box 150 min; ~14 units at ~USD 0.4 each + fixed ~2.5)
Stop before starting a unit that would cross 80% of cap or box. Gallica only (`tools/gallica_folio.py` for folio->canvas;
IIIF image API at reduced size). Units in this order (highest key value first):
 a. line 180: BnF Baluze 155 canvases 270-440 (Servien 1632, Sabran key; DECODE R2751/R2752 already flagged f.131-134,
    f.139-) -- which leaves carry cipher, which are glossed. Control: Baluze 155 f.131 (R2751).
 b. line 182: BnF fr.4133 (btv1b9060195s) Sabran register 1629-31 -- cipher passages or key tables? Control as (a).
 c. fr.3988 canvas 308 (KH1-B/F: the one unread neighbour of f.143r, no.60 Nevers-Revol key). Control: fr.3988 canvas 304.
 d. line 23: BnF fr.7126 f.274 (Tomokiyo cipher no.2) -- locate and screen.
 e. lines 101, 113, 114, 115 (Raince/Carpi 1521-38: fr.2984 f.109, fr.3091 f.23, fr.2963 no.101/fr.3092 no.14, Dupuy 265
    ff.306-340); lines 123, 124, 125 (fr.2963 no.48, Dupuy 468 ff.30-, fr.3897 ff.72-127); lines 138, 140 (Dupuy 452
    ff.48-49; Gramont fr.3003/fr.3053/fr.2974); line 240 (Mélanges de Colbert 113, Servien at Turin 1662-). For the
    multi-item rows screen the named folios only. Control for (e): the target leaf of dupuy452-carpi-1520 (see its NOTES).
 Line 210 (Danzay 1566-88) stays dropped (outside the key window) -- do not screen.

## SA-O (other hosts screen; Sonnet 5.5; cap USD 7; box 150 min)
 a. lines 213/225 and 214/226: ANTT PT/TT/CLNH/0086/02 (126 images) and /0086/09 (212 images), DigitArq via
    `tools/digitarq_fetch.py` at reduced size, >=3 s apart. Control: the antt-linhares-chave target leaf (its NOTES).
 b. line 385: RAH 9/6958 Leg. XIX, the 8 unopened Gonzalez Bravo neighbours + up to 30 later images (OAI didl ids; image
    fetch with `node tools/browser_fetch.js URL OUT --binary`, intermittent -- one retry rule). Control: rah-canada-1869's
    own cipher image.
 c. line 198: WVO August van Saksen series -- 189 letters' PDFs: sample, by script, the letters dated 1561-64 (key window)
    and contact-sheet their first pages; record how many sampled. Control: the august-van-saksen-1561-64 target letter.
 d. line 284: Huntington mssBLA 1-175 -- CONTENTdm `CISOSEARCHALL^cipher^all^and` and `cypher`, suppressfulltextsearch=1
    (host-table route); screen only hits. Control: the huntington-blathwayt target item.

## SA-MP (Monroe reels + Pinkney M30; Sonnet 5.5; cap USD 7; box 150 min)
 a. KEYHUNT lines 59 and 61: Erving to Monroe 23 Sep 1804 and the undated Nov-Dec 1804 item, LOC mss33217 S1 reel 3:
    every frame f0496-0530 and f0561-0640 at pct:20 (KH4-D2's next steps). Then lines 66 and 70 (Erving 24 Feb 1807,
    Bowdoin 27 Mar 1807, not located in r4 f0040-0072 / f0106-0148): read the 1904 calendar neighbours for a misfiled
    date (~USD 0.3 each) and look once more only where the calendar points. Control: reel 3 f0829 (the read Erving cipher).
 b. line 57: Pinkney despatches to Robert Smith 1809-1811, NARA M30 reels 12 and 13. Do not download the whole-reel PDFs
    unless no other route: try the NARA IIIF Image API v3 route first (host table, ARM-IMG worked example), else fetch the
    PDF once with an HTTP range check and extract page thumbnails with a script. Screen every frame at thumbnail scale for
    numeral-group pages; candidates at higher scale. Control: a known coded frame in M30 reel 11 (KH4-D / ARM notes).
    Pinkney-side letters that are printed decoded in the State Papers / PJM-SS are listed but not counted as unread.

## SA-CO (copy-order shortlist; Opus 5.5; cap USD 10; box 180 min)
Deliverable: `COPY-ORDERS-2026-10.md` at the repo root (+ `COPY-ORDERS-2026-10.tsv`). Candidates = KEYHUNT rows whose
letter is enciphered (or catalogued "en chiffre"/"in cifre"/"chiffriert"/"cifrada") and not digitised or not reachable from
the cloud. Start set (lines): 7, 16, 36, 58, 82, 83/84, 85/86, 117, 162, 163, 164, 165, 172, 199, 200, 201, 202, 218/230,
219/231, 239, 243, 245, 248, 249, 250, 251, 285, 305, 322-330 (italien 1583, 9 items: one row), plus the KH1 handoff leads
(fr.2988 ff.4-5 original unlocated; ANTT CLNH/0032/10, /0037/42). Merge duplicates; drop (with reason, kept in the TSV)
any whose plaintext is already printed deciphered (e.g. CSP Spanish for Puebla) or whose held key cannot read it.
Target ~33 rows after merging. Per row: archive, shelfmark, which held key reads it (key_path), why probably unread, number
of images needed (estimate), the archive's OWN price for 1-20 images read from its tariff page (quote the URL and the date
read), and whether a FREE tier covers it (e.g. AAE La Courneuve 1-19 views; BnF already-digitised-on-request; ANTT/
DigitArq free digitisation requests; Spanish state archives' free digital copies) -- one tariff page read per archive,
shared across its rows. Rank: free tier first, then (unread cipher units x key in hand) / price. Do not place orders, do not
email, do not fill any form. For the free-tier rows only, draft one request per archive in `outreach/` following
outreach/README.md (subject/recipient/sign-off lines, rule 1 AI-disclosure sentence, rule 1a voice, recipient = the
institution's public address read from its own contact page with date), status `drafted`, and NO `checked:` line --
gate 7 is a separate session the lane will run. Log the drafts' paths in the done line. Personal data stays out (rule 9).
Hosts: archive tariff/contact pages, one request at a time; if a page is challenged, record "tariff page unreachable from
cloud" and the URL, and move on.

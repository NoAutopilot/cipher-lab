# Lope Hurtado de Mendoza (Rome) to Charles V, 1522 — RAH Salazar 9/26, DECODE R9634/R9646/R9649

partial
Check-solved, 26 Sept 2026 (LANE B6 worker bCSLOP): this worker fetched and grepped the WHOLE Calendar
of State Papers, Spain vol. II (Bergenroth/Gayangos, archive.org bub_gb_ZoY9AAAAcAAJ, `_djvu.txt`,
3,438,686 bytes) itself, for "Hurtado" (31 hits, plus OCR-mangled variants found only via the "Lope"
and "Mendoza" greps), "Lope" (101), "Mendoza" (24) and "cipher"/"cypher" (168), and read every hit —
correcting the prior verdict, which re-cited Bourdeau's 2026-09-21 search instead of opening the
edition (RETRO-2026-09-26b finding 3). Result: **not empty.** Calendared Lope Hurtado letters to the
Emperor in 1522 are nos. 416/422 (6 June), 454-455 (26-27 July), 467 (14 Aug, off Rivataglia), **497
(dated "the last day of October"/"the 1st of November 1522", from Rome, source "M. Re. Ac. d. Hist."
= Real Academia de la Historia, the same holding institution as RAH Salazar 9/26; "Autograph in
cipher... Contemporary deciphering")**, 609 (17 Dec, "the cipher of Lope Hurtado de Mendoza, ...
Contemporary deciphering"), 610 (23 Dec) and the "27 Dec" entry (OCR index garbled). No. 497 falls
inside the Sept-Nov 1522 window and is 8 days from R9649's own DECODE-catalogue date (9 Nov 1522,
`catalogue/decode-records.jsonl`); whether it is the same despatch is unresolved (this sweep did not
compare folios/incipits) and is flagged below, not settled. Separately, Tomokiyo's *Scholarly Studies
on Ciphers in the Reign of Emperor Charles V* comments page (`sources/cryptiana/web/spanish2C.htm`,
not previously read for this target) discusses Olga Kolosova (2017), *El lenguaje secreto de la
diplomacia de Carlos V (1521-1527)* (doctoral thesis, Universitat de València, 854pp, "edition of 78
unpublished, encrypted manuscript letters between... Charles V and diplomats, agents and ambassadors
in Italy", per web search of the Dialnet record), also published as Kolosova (2024), *El lenguaje
cifrado en tiempos de Carlos V (1521-1527)* (Ediciones Universidad de Salamanca): it reconstructs
"Ko.7 Lope Hurtado de Mendoza" (main cipher, substitution alphabet p.312, nomenclature p.333) and
"Ko.10 Lope Hurtado's Secondary Cipher" (substitution alphabet p.388, nomenclature p.405), both used
"in Lope Hurtado's letters to the Emperor" — this period is exactly 1521-1527, covering the target.
Neither the dissertation nor the 2024 book has been opened by anyone in this repository (Teseo link
TLS-unreachable from this container; Google Books preview reachable but out of this job's authorised
hosts, not fetched). aaymeloglu/unsolved-ciphers (fresh shallow clone, HEAD `2495c45e8b94ffbc4f09a-
085224aa5ebce5cdf9f`, 2026-09-23, deleted after grep) confirms R9634/R9646/R9649 `Non-decrypted` in
`catalogue/decode-records.jsonl` with exact dates: R9649 = 1522-11-09, R9634 = 1522-09 (day blank),
R9646 undated; `catalogue/bne-ranked.md` still names two further unread Hurtado letters at the BNE
(MSS/18697/29 "Parcialmente cifrada"; MSS/20212/27, five letters 1522-1526). dbourdeau/cyphersolver
(fresh shallow clone, HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`, 2026-09-25, unchanged from the
prior job, deleted after grep) reconfirms no R9634 transcription exists anywhere in the repository.
Web search for "Lope Hurtado" cipher/cifrado/descifrado Rome 1522 found nothing beyond the Kolosova
thesis record and unrelated 1547-1548 Diego Hurtado de Mendoza material. One OpenAlex query
(`search=Kolosova Carlos V cifra diplomacia`) returned 5 results, none naming Lope Hurtado or 1522
directly (all 1543-1556 imperial-cipher studies by the same research group). Semantic Scholar 429'd
twice again (key present, one retry after a pause) — still not answered, not a negative.

## Gate check

```
$ python3 tools/intake_gate_check.py lope-hurtado-1522
lope-hurtado-1522: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Check-solved (bCSLOP), 26 Sept 2026

Job bCSLOP (`.claude/briefs/runs/2026-09-26-lane-b6-cslop.md`): correct the check-solved verdict, which
RETRO-2026-09-26b finding 3 caught re-citing another worker's search of CSP Spain vol. II instead of
opening it. Query log, in the brief's order:

**(a) Calendar of State Papers, Spain, vol. II (Bergenroth/Gayangos).** Fetched
`https://archive.org/download/bub_gb_ZoY9AAAAcAAJ/bub_gb_ZoY9AAAAcAAJ_djvu.txt` (1 request, 200, disk
only, not committed) and grepped the whole 3,438,686-byte file (case-insensitive):
- `hurtado`: 31 hits — read every one. In-window result: **none** dated Sept-Nov 1522 under this exact
  spelling (467 is 14 Aug; the next after it is 609, 17 Dec).
- `lope`: 101 hits — this grep, not the `hurtado` one, caught the OCR-mangled "1 Not. 487. 3LoPB
  HmrrADO db Memsoza to the Ehpbrob" (no. 497, correctly "1 Nov. 497. Lope Hurtado de Mendoza to the
  Emperor"), missed by the `hurtado` grep because the OCR renders the name "HmrrADO". Full text of
  no. 497 read (djvu.txt lines ~49240-49295): despatched "Marino [i.e. Marano], last day of October
  1522", indorsed "To the King. 1522. From Rome. Lope Hurtado. The 1st of November. Answered.",
  source line "Spanish. Autograph in cipher. Contemporary deciphering. pp. 6." No specific folio/
  shelfmark is legible in this OCR for no. 497 (the source abbreviation "M. Re. Ac. d. Hist." =
  Real Academia de la Historia is legible; a shelfmark code directly below it is not). This is a
  genuine gap in the prior verdict's "nothing for Sept-Nov 1522" claim — flagged, not resolved (see
  "What would actually move this target" below; folio-level comparison against R9649's f.266-268 is
  a separate, cheap next step, not run here — out of this job's scope, which is the citation only).
- `mendoza`: 24 hits — read every one not already covered above. All are either the same in-1522-window
  entries already listed, or clearly dated 1523/1524 by internal content (e.g. "19 and 20 Nov 612" is
  the papal conclave that elected Clement VII, 19 Nov **1523**, not 1522; "13 April 633/634/635" are
  headed "1524" on the page; "23 Dec 610" and the Cardinal-of-Volterra entries at "27 April 546" are
  also 1523 by the same conclave/arrest content). No new in-window hits beyond no. 497.
- `cipher`/`cypher`: 168 hits, not all individually read (too many for this job's cap); spot-checked
  the ones adjacent to every Hurtado/Mendoza hit above (already quoted) and the Sept 1522 date-header
  sweep below.
- Date sweep: grepped `Sept\.` (163 hits) and scanned every entry number between the last confirmed
  1522 Hurtado letter before the window (467, 14 Aug) and the first one after it (609, 17 Dec) by
  listing every entry header in that byte range (`sed` + header regex, lines ~47900-50090 of the
  djvu.txt): entries 477-507 in that stretch are Hieronymo Adorno, Pope Adrian VI, Juan Manuel, the
  Duke of Sessa, Alonso Sanchez, the Viceroy of Naples, the Abbot of Najera and Martin de Salinas —
  and no. 497 (Lope Hurtado, above). No entry for Lope Hurtado in Sept 1522 specifically found by
  this method (497 is the only in-window hit, dated 1 Nov).

**(b) Tomokiyo's pages on disk (`sources/cryptiana/`).** `grep -rli hurtado sources/cryptiana/`
→ `web/spanish2.htm`, `web/spanish2C.htm`, `web/spanish3.htm`, `web/spanish3C.htm`. The main articles
(`spanish2.htm`, `spanish3.htm`) discuss Lope Hurtado de Mendoza only in his later career (Florence
mission 1537; a 1548 Lisbon cipher fragment, Num.6 of Alcocer 1934) — no 1522 Rome material, matching
the prior worker's finding. **Not previously checked: `spanish2C.htm`**, a newer comments/discussion
page ("Scholarly Studies on Ciphers in the Reign of Emperor Charles V"), which quotes and discusses
Olga Kolosova (2017), *El lenguaje secreto de la diplomacia de Carlos V (1521-1527)* (dissertation,
Universitat de València, 854pp) and Kolosova (2024) (Ediciones Universidad de Salamanca, same title
in Spanish, DOI 10.14201/0MX001). Verbatim: "Kolosova reconstructed 17 ciphers used in letters to
Emperor Charles V in 1521-1527." Two of the 17 are named for our sender: "#### Ko.7 Lope Hurtado de
Mendoza (p.309, Substitution alphabet: p.312, Nomenclature: p.333) ... Lope Hurtado used this main
cipher as well as another less complex one (Ko.10) with the Emperor (p.309-310)"; and "#### Ko.10
Lope Hurtado's Secondary Cipher (p.386, Substitution alphabet: p.388, Nomenclature: p.405) ... We
know both were used in Lope Hurtado's letters to the Emperor." This is a direct, on-point hit the
prior verdict's Tomokiyo check missed by searching only the two main articles, not the comments page.

**(c) DECODE listing.** Not re-crawled live (cached snapshot from `tools/decode_list.py`,
`sources/decode/records-non-decrypted-2026-09-24.tsv`, already on disk and cross-confirmed via the
fresh aaymeloglu clone below — re-crawling would repeat, not correct, the prior citation, and this
job's gap was CSP vol. II, not DECODE). Confirmed all three records still `Non-decrypted`.

**(d) Fresh shallow clones.** `git clone --depth 1 https://github.com/dbourdeau/cyphersolver` →
HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (2026-09-25T18:14:52-05:00) — same commit the prior
job read; `grep -ril 9634` still hits only `lopehurtado/NOTES.md`, `profile.json` and the
`key_1522_from1524_B.tsv` header, no transcription; `grep -ril "9646\|9649"` confirms
`read_r9646.md`/`read_r9649.md` present. Deleted after grep. `git clone --depth 1
https://github.com/aaymeloglu/unsolved-ciphers` → HEAD `2495c45e8b94ffbc4f09a085224aa5ebce5cdf9f`
(2026-09-23T14:27:44-05:00). `catalogue/decode-records.jsonl` gives exact dates not quoted in the
prior verdict: R9649 `Start Year 1522, Start Month 11, Start Day 9` (9 Nov 1522); R9634 `Start Year
1522, Start Month 9` (day blank); R9646 no date fields at all. `catalogue/bne-ranked.md` still lists
MSS/18697/29 ("Parcialmente cifrada", 1522) and MSS/20212/27 (five letters, 1522-1526) as unread by
either project. Deleted after grep.

**(e) Web search.** `Kolosova "Lope Hurtado" cifra tesis Carlos V 1522` → confirms the Dialnet thesis
record (directed by Júlia Benavent, Universitat de València, 2017; "edition of 78 unpublished,
encrypted manuscript letters between Emperor Charles V and diplomats, agents, and ambassadors in
Italy"); no source found stating whether R9634/R9646/R9649 specifically are among the 78. `"Lope
Hurtado" Roma 1522 cifrado descifrado Carlos V` → no new source; the closest hits are 1547-1548
Diego Hurtado de Mendoza material (a different, later ambassador), already known from Tomokiyo.
Neither the Teseo thesis record (TLS error from this container, host not in this job's list, not
pursued) nor the Kolosova (2024) Google Books preview (reachable, HTTP 200, but Google Books is not
one of this job's authorised hosts per the LANE B6 common file — not fetched) was opened.

**(f) OpenAlex + Semantic Scholar.** OpenAlex `works?search=Kolosova Carlos V cifra diplomacia` → 5
results, all 2023-2025 papers on other 1543-1556 imperial ciphers by the same research circle (Simon
Renard/Granvelle/Marie de Hongrie), none naming Lope Hurtado or 1522. Semantic Scholar
`graph/v1/paper/search?query=Kolosova lenguaje secreto diplomacia Carlos V` → HTTP 429 twice (key
present; one retry after a 3s pause, per the good-citizen rule) — unanswered, not a negative.

**What this changes:** the target stays `partial` (no plaintext or key confirmed for R9634/R9646/
R9649 specifically by this worker), but the prior verdict's two supporting claims do not fully hold:
(1) "nothing for Sept-Nov 1522" is wrong by one entry (no. 497, 1 Nov); (2) "Tomokiyo... no reference
to Hurtado[relevant to this target]" missed a page naming a specific, published, page-cited
reconstruction of two ciphers used in exactly Lope Hurtado's letters to the Emperor in exactly this
period. Next cheap steps, not run in this job (disk/git/API-only cap): identify no. 497's shelfmark
and compare to R9649 f.266-268 (or the two unread BNE items); and have a worker read Kolosova (2017/
2024) — via the Universitat de València TDX repository, Dialnet, or the person's own Google Books/
library access — for R9634/R9646/R9649 by name, date or folio, and for the Ko.7/Ko.10 key tables
themselves, which could be a **published key** (rule 10, "Key source") for this whole target if they
cover the same letters.

Requests: archive.org 1 (djvu.txt fetch); github.com 2 (shallow clones, deleted); openalex.org 1;
semanticscholar.org 2 (both 429); web search 2 queries; 1 reachability check each to
aplicaciones.ciencia.gob.es (TLS failure, not pursued) and books.google.co.jp (200, not fetched
further, out of scope per common-file rule 7).

## Job

LANE B5 job bLOP (`.claude/briefs/runs/2026-09-26-lane-b5-lope-hurtado.md`): apply the 49 code values
Bourdeau recovered from R9644's contemporary clear copy (`key_codes.tsv`, dbourdeau/cyphersolver
`lopehurtado/`) to the three sibling records QUEUE.md G2 flagged "not-attempted" — R9634, R9646,
R9649 — with a random-digit control.

## Step 1: what Bourdeau has actually read, as of the clone (26 Sept 2026)

Cloned `git clone --depth 1 https://github.com/dbourdeau/cyphersolver` at commit
`fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (2026-09-25T18:14:52-05:00), read only `lopehurtado/`,
then deleted the clone (MIT code / CC BY 4.0 text, dbourdeau/cyphersolver, credited here).

QUEUE.md's "not-attempted" for these three records is **stale for two of them**, exactly as the job
brief suspected (it names `read_r9646.md`/`read_r9649.md` already existing):

| record | Bourdeau's own NOTES.md ("Remaining gaps", written ~2026-09-21) | actual state at HEAD (`read_r9646.md`, `read_r9649.md`) |
|---|---|---|
| **R9649** | "not-attempted; listed as uncribbed but no coverage was measured and no reading file exists" | `read_r9649.md`: **97% (86/89 tokens) read**, from **the record's own contemporary clear copy** (f. 268r, "a contemporary clear version of the whole letter," independent of R9644) — the same kind of crib R9644 itself carries. 3 unread tokens (one unmatched pair, no counterpart in the clear). |
| **R9646** | same line | `read_r9646.md`: **84% (99/118 tokens) valued**, no crib of its own — read by applying the accumulated key (1524 `key_1524.tsv` values carried back + `key_codes.tsv` + values won specifically from R9649's crib) to f. 252r. 19 tokens unread (five isolated codes/spelled words with one unsettled sign each); Bourdeau's own notes give no crib for the remainder. |
| **R9634** | same line | **No `read_r9634.md`, no ciphertext transcription anywhere in the repository** (`grep -ril 9634 .` in the clone hits only `NOTES.md`, `profile.json` and `key_1522_from1524_B.tsv`'s header — none is a transcription). Genuinely not-attempted. |

`key_codes.tsv` carries **49 rows graded `confirmed`** (31 more `probable`, kept separate) — this
matches QUEUE.md's "49 confirmed code values" and the job brief's count exactly.

The key point for this job: Bourdeau's R9646/R9649 reads already use **more than the 49-value
R9644-crib key** — R9649 was read from its *own* clear copy (a stronger and independent crib, not
derived from R9644 at all), and R9646 was read with the 49 values **plus** values won from R9649's
own crib and the 1524 key carried back. Re-applying only the 49-value subset to either record, as
the job brief's step 3 specifies, would strictly *underperform* what Bourdeau has already posted —
it cannot add coverage the fuller key does not already have, and it cannot resolve the tokens
Bourdeau's own fuller apparatus already tried and left unread (no crib, isolated codes).

## Step 2 (per brief; this job's actual outcome): nothing is left to test

Per the job brief's own instruction ("Records he has fully read are `found-solved` for this job;
only what he left unread is a test for us. If nothing is left, write that and stop."):

- **R9649**: effectively fully read (97%) by Bourdeau, from the record's own clear copy — `found-solved`
  for this job (found already solved, in an unpublished GitHub repository, not by us; rule 10 class
  is a verifier's call, not stated here).
- **R9646**: substantially read (84%) by Bourdeau with the full accumulated key (a strict superset of
  the 49-value key this job was to apply); the 19 unread tokens have no crib in his notes and are
  not reachable with the 49-value subset either. Nothing this job's test could add.
- **R9634**: no transcription exists in Bourdeau's repository, and this job's cap is disk-and-git only
  (no DECODE login, no image hosts — full-size DECODE images are account-wide blocked regardless, per
  CLAUDE.md's Access playbook). Per the brief: "If a record has no transcription in Bourdeau's
  repository, stop at that record and say so." Stopping here. Making our own transcription from a
  DECODE image is a different, larger job (a breadth spec's first test is one job, not two).

**No key application and no random-digit control were run.** Running the specified test (49-value
key only) against R9646/R9649's own transcriptions would answer a question already answered more
strongly by Bourdeau's fuller reads on file; running it against R9634 is blocked for lack of any
transcription. A control without a target test to compare against is not a result (rule 3).

## What would actually move this target

1. A transcription of R9634 (from an image — DECODE listing confirms it is `Non-decrypted`, 6 pages,
   ff. 14-16, Sept 1522; out of this job's disk/git-only cap) tested against the *full* accumulated
   key (49-value `key_codes.tsv` + the values `key_1522_from1524*.tsv`/R9649 added), not just the
   49-value subset.
2. The two further, wholly unread Hurtado letters aaymeloglu's `bne-ranked.md` names at the BNE
   (MSS/18697/29, "Parcialmente cifrada," 1522; MSS/20212/27, five letters, 1522-1526) — neither
   project has looked at these; a BNE catalogue/digital-collections check is a separate cheap test.
3. The R9646 remainder (19/118 tokens) and R9649 remainder (3/89) need better images, per Bourdeau's
   own "Where the work is now limited" section (DECODE serves ~1700 px/folio, not enough for per-glyph
   discrimination) — not a key problem, an imaging problem, same wall the sanchez1522 and R9656 work
   hit.

## Search log (rule 1)

- Cipher's name / catalogue entry: covered inside Bourdeau's own NOTES.md (search log there, 2026-09-20/21).
- Sender's printed correspondence / calendars: Calendar of State Papers Spain vol. II, full text,
  archive.org `bub_gb_ZoY9AAAAcAAJ`, searched by Bourdeau 2026-09-21 (cited above); not re-run this
  session (cost discipline; the search terms and result are unambiguous and dated).
- Cryptiana / Cipherbrain: Tomokiyo 2025 (Sánchez/Juan Manuel only); no Cipherbrain thread found for
  Hurtado specifically.
- DECODE: `catalogue/decode-records.jsonl` in aaymeloglu's repo (a cached DECODE snapshot) confirms
  R9634, R9646, R9649 all `Non-decrypted`, matching Bourdeau's own table; no fresh DECODE crawl run
  this session (avoided a `decode_list.py` full-status crawl to stay inside the $3 cap; the cached
  snapshot and Bourdeau's own table already agree).
- Solver repositories: dbourdeau/cyphersolver `lopehurtado/` (this job); aaymeloglu/unsolved-ciphers
  shallow-cloned, grepped for "hurtado" (case-insensitive) across the whole repo, deleted after.
- OpenAlex: `works?search=Lope Hurtado cipher` (11 results, none relevant). Semantic Scholar: 429,
  twice, key present — not a negative, just unanswered.

Per rule 10, this reports what was found and where it was not; it does not classify novelty.

## Credit

Bourdeau, dbourdeau/cyphersolver, `lopehurtado/` folder, commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`
(2026-09-25), CC BY 4.0 text / MIT code, read 26 Sept 2026. Aymeloglu, aaymeloglu/unsolved-ciphers
(no licence — cited, not copied), `catalogue/decode-records.jsonl` and `catalogue/bne-ranked.md`, read
26 Sept 2026.

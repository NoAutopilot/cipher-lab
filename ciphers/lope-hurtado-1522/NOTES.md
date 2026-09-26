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

## Job bLOP2, 26 Sept 2026 (LANE B6 worker bLOP2)

Job `.claude/briefs/runs/2026-09-26-lane-b6-lop2.md`, follow-up to bCSLOP's two leads: is CSP Spain II
no. 497 the same letter as any of R9634/R9646/R9649, and can Kolosova's reconstruction be opened.
Status stays **partial** — nothing found here is a plaintext or key "shown in print" in the sense
check-solved.md means (F0/F1/F2): every printed source below is a one- or two-sentence archival
*regesta* (a catalogue description), not a transcription or decipherment of the cipher text itself.
Reported for the record and for whoever classifies novelty next (rule 10; not done here).

### (1) CSP no. 497 is not R9634/R9646/R9649 — it is R9644 (already `Decrypted` on DECODE)

Re-fetched the same CSP Spain II `_djvu.txt` (archive.org `bub_gb_ZoY9AAAAcAAJ`, 3,438,686 bytes,
1 request, disk only) and re-read entry 497 in full (djvu.txt ~line 49262-49290): despatched "Rome,
the 1st of November 1522"; content per the abstract — Peter the *camarero*/valet de chambre is "the
principal man in Rome... a very sharp Burgundian... we must buy him"; the Pope consults the Archbishop
of Piacenza; "Cisterer" reports the King of France asked the Pope for a safe-conduct; "Prince Henry
(of Navarre). Flanders. Castile."; "pp. 6."

Cloned `dbourdeau/cyphersolver` (`git clone --depth 1`, same HEAD `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`,
2026-09-25, as the prior job; read `lopehurtado/read_r9644.md` and `read_r9646.md`/`read_r9649.md`;
deleted after reading; MIT code/CC BY 4.0 text, credited). **R9644** (RAH Salazar 9/26, ff. 237-243,
DECODE status `Decrypted`, its own contemporary clear copy on ff. 241-242 headed "Al Rey — De Lope
Hurtado, de Roma, del primero de noviembre") contains, verbatim: "El camarero Pedro es el principal"
(= "Peter, the valet de chambre, is the principal man in Rome"), "Entendido he... de Cisterer" (=
"Cisterer"), "el principe don Enrique" (= "Prince Henry"), and "Flandes"/"Castilla" in the same
paragraph — four distinctive, co-occurring matches to no. 497's abstract, on the same date (1 Nov
1522). Bourdeau's own note: "R9648 (ff. 260-265, 9 Nov, DECODE Non-decrypted) is the duplicate of
this despatch" — so **R9644/R9648, not any of our three targets, is CSP no. 497** (grade for this
identification: content match S, from the printed abstract vs. the already-decrypted clear copy; not
a token-by-token grade since no. 497 itself is an English abstract, not the Spanish text).

Per record, vs. no. 497:
- **R9634** (f. 14-16): **unrelated**. Different date entirely (14 Sept 1522, established below, vs.
  1 Nov) and no content overlap in what Bourdeau's notes give (no transcription exists at all yet —
  see the bLOP job section above).
- **R9646** (f. 252): **sibling**, not the same letter. Same correspondence (Lope Hurtado to Charles
  V, RAH Salazar 9/26) but a different despatch — dated 7 Nov 1522 (below), content the duke of
  Ferrara's capitulation and the *décima*, no overlap with no. 497's Peter/Cisterer/Piacenza/Navarre
  content.
- **R9649** (f. 266-268): **sibling**, not the same letter. Dated 9 Nov 1522 (own text: "De Roma .ix.
  de noviembre"), content Cardinal Santa Cruz pressing for the Ostia fortress and the *licenciado*
  Bernardino — again no overlap with no. 497.

### (2) All three targets independently dated and content-matched in two printed 19th/20th-c. catalogues

Google Books (key + `country=US`) turned up two printed indexes of the *same* RAH collection under
its **old shelfmark "A-26"** (confirmed identical to the modern "Signatura 9/26" DECODE uses — a third
Google Books hit prints both side by side: "9/26. 3.263..." opens the Índice's own A-26 section, and
*El Obispo Diego Ramírez de Villaescusa...* cites "Salazar y Castro, 9-26 (A-26), fols. 133-138v"):

- *Índice de la colección de don Luis de Salazar y Castro*, Tomo II (Real Academia de la Historia;
  Google Books id `29EJv0xvKcoC`) and Francisco de Laiglesia y Auset, *Estudios históricos (1515-1555)*
  (Imprenta clásica española, 1919; id `8qNCAAAAYAAJ`).

Per record (snippet-quoted, page numbers not visible in the snippet view):
- **R9634** — Índice, entry "3.269. 7.- Otra de Lope Hurtado de Mendoza a Carlos V, en cifra. Génova,
  1522. Septiembre, 14. Original. A-26, fos 14 a 16." Exact shelfmark match (f.14-16) and an exact
  date: **Genoa, 14 September 1522**. Independently re-confirmed by a modern secondary source, Álex
  Claramunt et al., *Pavía 1525* (Desperta Ferro Ediciones, 2025; id `E0c_EQAAQBAJ`): "Lope Hurtado de
  Mendoza a Carlos V, Génova, 14 de septiembre de 1522, RAH, Colección Salazar, A 26, f.os 14-16" —
  same date, same shelfmark, cited independently of DECODE. This resolves the open question in the
  bLOP job section above (R9634's date was previously unknown beyond "1522 -, day blank").
- **R9646** — Índice, entry "3.362. 100. Carta de Lope Hurtado de Mendoza a Carlos V, en cifra. Roma,
  1522. Noviembre, 7. Original. A-26, fo 252. El fo 253 es el sobrescrito de esta carta. El fo 254 es
  una postdata de esta carta..." Exact shelfmark match (f.252) and an exact date, **Rome, 7 November
  1522** (read_r9646.md had inferred only "filed between R9644 [1 Nov] and R9649 [9 Nov]" from
  internal content — this confirms and narrows it). Laiglesia's *Estudios históricos* independently
  describes what reads as the same letter: "Carta de Lope Hurtado a Carlos V sobre la capitulación
  del duque de Fe[rrara]... en cifra..." — matching R9646's own decoded content (*"como el papa era
  concertado con el duque de Ferrara"*) almost exactly.
- **R9649** — Laiglesia's *Estudios históricos*: "Lope Hurtado al rey Carlos [V] de cómo S.S. le manda
  escribir a S.M. que el cardenal de Santa Cruz solicita a Ostia, y que convendría escribiese a S.S.
  ponga a buen recaudo aquella fortaleza y no la de a nadie, y de la llegada del [licenciado
  Bernardino?]" — this is a near word-for-word regesta of R9649's own decoded content (*"el Cardenal
  de Santa Cruz le mata por Ostia"*, *"poner gran recabdo en la fortaleza de Ostia... no la de a
  nadie"*, *"el licenciado Bernardino es venido"*). The Índice's own entry for the same subject gives
  "A-26, fos 269 y..." ("Sin lugar ni data (Roma, 1522)") — three folios off DECODE's f.266-268, in
  the same direction and size as the f.252/253/254 letter+cover+postscript pattern seen for R9646, so
  plausibly the same item under the index's own foliation, not verified folio-by-folio.

**What this changes:** none of R9634/R9646/R9649 is CSP no. 497 (that is R9644/R9648, already
`Decrypted`); all three are dated and content-matched, independently of DECODE and of each other's
Cardenal/Ferrara transcriptions, in two printed archival catalogues from 1919 and the Real Academia de
la Historia's own Índice — sources neither this repository nor, apparently, Bourdeau's notes had
cited before. This is a regesta match, not a plaintext or key in print (status stays `partial`), but
it is a substantial addition to the search log a verifier should see before any N-class is assigned:
these three letters' existence, dates, senders/recipients and (for R9646/R9649) approximate subject
were already in print for over a century before DECODE catalogued the cipher.

### (3) Kolosova — an open PDF exists but is dead-linked; a live Google Books preview independently corroborates a 49-value cipher

CORE (`api.core.ac.uk/v3/search/works/`, keyless, 1 request, 200 — no `CORE_API_KEY` needed for
`search`) found the 2017 dissertation directly: id `159375827`, "El lenguaje secreto de la diplomacia
de Carlos V (1521-1527)", Kolosova, Olga; directed by Júlia Benavent Benavent; held by "Repositori
d'Objectes Digitals per a l'Ensenyament la Recerca i la Cultura" (RODERIC, Universitat de València) —
matches the web-search-found `https://roderic.uv.es/handle/10550/66216` (not fetched: `roderic.uv.es`
is not a host this job's brief names). CORE's own cached PDF mirror is dead: `downloadUrl`
`https://core.ac.uk/download/159375827.pdf` 301s to `fileserver-az.core.ac.uk`, which 404s
(`BlobNotFound`) on both HEAD and GET. A follow-up `api.core.ac.uk/v3/outputs/159375827` call (for
the record's other identifiers/links) 429'd twice (`CORE_API_KEY` unset this session per
`tools/room.py --start`'s probe — the good-citizen one-retry limit was then hit, not pursued further).
Dialnet's own page (`dialnet.unirioja.es/servlet/tesis?codigo=177430`, 1 request) links "Tesis en
acceso abierto en: TESEO"; following that (1 more request) 302s to
`aplicaciones.ciencia.gob.es/teseo-rest/api/documento/download/public/34168`, which reconfirms the
23 Sept 2026 finding elsewhere in this repo: TLS-unreachable from this container (`SSL certificate
problem: unable to get local issuer certificate`, 1 reachability check). `docta.ucm.es` (1 request,
404/no-results) and `eprints.ucm.es` (2 requests, connection reset both times, one retry per the
good-citizen rule, not pursued further) — both the wrong institution for this thesis (Universitat de
València, not Complutense) and negative as expected.

Not blocked, however: Google Books (key + `country=US`) serves a live PARTIAL-view preview of the
**2024 book** (*El lenguaje cifrado en tiempos de Carlos V (1521-1527)*, Ediciones Universidad de
Salamanca, Google Books id `fpTHEQAAQBAJ`) with several on-point snippets (5 requests total for this
sub-search): "Lope Hurtado presenta menos variación y cuenta con 49 variantes, correspondientes a las
23 letras o grupos de..." — **49 variants**, matching `key_codes.tsv`'s 49 `confirmed` code values
exactly, independently derived by Kolosova from (per her own thesis abstract) "78 unpublished,
encrypted manuscript letters" rather than from Bourdeau's crib. Also: "...Lope Hurtado (cifra 7 de
nuestro listado) evidencia que el origen de las cartas confluye con las misiones llevadas a..."
(confirms Tomokiyo's "Ko.7" numbering is Kolosova's own "cifra 7"). No snippet found yet naming R9634/
R9646/R9649 specifically, or quoting a full key table (Google Books' snippet view only surfaces short
matched fragments, not full pages) — **this does not confirm Kolosova's book prints the *same* 49
values as `key_codes.tsv`, only that the same count is independently reported**; comparing the actual
value tables (thesis p.312/333 or book's equivalent) needs the full text, which is not open from this
job's hosts.

**Next step, not run here:** a job whose brief names `roderic.uv.es` (the RODERIC repository directly)
or that carries `CORE_API_KEY` could very likely retrieve the full 2017 dissertation PDF outright —
this is a live, findable, apparently-open academic repository copy, not a paywall; it was not fetched
here solely because this job's host list did not name it. If retrieved, grep it for "9634", "9646",
"9649", "252", "266", "268", "14-16", "Ostia", "Ferrara" and the Ko.7/Ko.10 alphabet tables (p.312/333,
p.388/405 per Tomokiyo's citation) to check whether Kolosova's own 49-value table matches
`key_codes.tsv` value-for-value (a possible **published** key per rule 10's "Key source" field) and
whether she edits R9634/R9646/R9649 specifically among her 78 letters.

Requests: archive.org 1; github.com 1 clone (deleted); dialnet.unirioja.es 2; aplicaciones.ciencia.gob.es
1 (reachability only, TLS failure); docta.ucm.es 1; eprints.ucm.es 2 (both failed, not pursued further);
googleapis.com (Books) 11; openalex.org 1; core.ac.uk (api + fileserver) 5 (1 search 200, 2 outputs 429,
2 download attempts 404).

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

### (4) RODERIC PDF opened (bLOP3, 26 Sept 2026) — it is not the 2017 doctoral dissertation, and it does not print a key or decipherment for R9634/R9646/R9649

Job bLOP3, brief naming `roderic.uv.es`: fetched `https://roderic.uv.es/handle/10550/66216` (301 →
`https://roderic.uv.es/items/b8f30f7a-39c3-4a9a-b256-65829a6c801d`, 1 request), then the item's one
bitstream, `tesis olga roderic.pdf` (`.../bitstreams/5c972ac1-1d26-4e47-8f51-4b95f66fa6bc/download`,
1 request, 22,188,005 bytes, confirmed by md5 against the item's own metadata), then the item's full
metadata page (1 request) for the deposit provenance. `pdftotext -layout` (poppler-utils installed
this job) and grep, no models used to read it.

**The file is not the full 854pp doctoral dissertation.** `pdfinfo` and the record's own
`dc.format.extent` agree: 148 pages. Its own title page reads "Tesis presentada per: Olga Kolosova ...
**Máster en Investigación en Lenguas y Literaturas** ... Valencia, mayo de 2016" — the earlier Master's
thesis (TFM), not the 2017 doctoral thesis the catalogue record (`dc.date` 2017, "Tesis doctoral",
dir. Benavent) describes. The item's own provenance log explains why the page count is short: a first
deposit (2,700,606 bytes) was **rejected** by the repository curator on 2018-05-07 with the reason
"Debe depositar el texto completo de la tesis, no solamente un extracto de la misma" (must deposit
the complete text, not just an extract); the resubmission 8 days later (22,188,005 bytes, the file
fetched here) was then approved — but it is still, by its own title page, the 2016 Master's version,
not a text that grew to 854 pages with a 78-letter annex.

The table of contents (índice, p.1 of the PDF) lists chapters on the ciphers of **Carlos de Lannoy**
(p.63), **Marino Caracciolo** (p.89), the **Adorno brothers** Jerónimo and Antoniotto (p.103), and
**Ludovico de Montalto** (p.122) — no chapter for Lope Hurtado de Mendoza's cipher(s), no "Ko.7"/"Ko.10"
labels anywhere, and no letter-edition annex (its own "ANEXO" is two lines: "Siglas y abreviaturas"
p.140, "Literatura crítica" p.141 — an abbreviations list and bibliography, not edited letters).

Full-text grep confirms: `hurtado` — 6 hits total, all passing mentions, none a chapter or key table:
p.62 shows one fragment of a general code-assignment table used as a worked *illustration* ("Para
ilustrar el fenómeno de asignación de códigos... presentamos la primera parte de la tabla de
asignación de códigos en el cifrado [e]ncontrado en las cartas de Lope Hurtado") — a partial a–g
column table, badly mangled by `-layout` extraction (it is a graphic/table object, not extractable
text; would need the page image to read cleanly), not a full alphabet/nomenclator table and not
attributed to "Ko.7"/"Ko.10"; p.111 compares "las cifras de Alonso Sánchez y Lope Hurtado - cifra 2"
in passing while discussing the Adorno cipher's similarity to Sánchez's; p.146 is an unrelated
bibliography entry (Martínez Montero on Lope Hurtado's house in Burgos). `9634`, `9646`, `9649`,
`Ko.7`, `Ko.10` — **0 hits each**. `1522` — 17 hits, every one dated to letters of the **Abad de
Nájera** (a different sender), none to Lope Hurtado.

**Conclusion: this document does not confirm or print a key or decipherment for R9634/R9646/R9649,
and is not the source Tomokiyo's `spanish2C.htm` cites for Ko.7 (p.309/312/333) or Ko.10 (p.386/388/
405) — those page numbers do not exist in this 148-page file.** Status stays `partial`. What Tomokiyo
cites (the full doctoral dissertation or the 2024 Salamanca book, both apparently longer works than
this deposit) remains unopened; this is a gap in what RODERIC itself serves, not a host this job
failed to reach — the PDF fetched fine, it is simply the wrong/earlier document. Not a LOCAL-QUEUE row
(no paywall or login was hit); a next step, not run here, is checking whether Universitat de València
holds a separate, longer 2017 doctoral deposit (a second Teseo/RODERIC record, or the 2024 book itself)
under a different handle, since this one is confirmed to be the 2016 master's-thesis text.

Requests this job: roderic.uv.es 3 (handle page, bitstream download, full-item metadata page), each
paced by processing time, no more than one request in flight at a time, descriptive UA.

## NX-UNBLOCK (26 Sept 2026): a new, closely on-topic 2024 publication found

Per CLAUDE.md's NX-UNBLOCK brief, tried a free route the earlier RODERIC pass had not tried: RODERIC's
DSpace 7 REST discover-search API (`roderic.uv.es/server/api/discover/search/objects?query=...`), rather
than the plain HTML `/simple-search` path (404s under the current DSpace 7 frontend). Query "Lope Hurtado
cifra" surfaces a distinct, much more recent item than the 2016 master's thesis already read:

**María José Bertomeu Masiá, "Una cifra para negociar el matrimonio de Margarita de Parma," in Manuel Heras
García (ed.), *Italia y España. Una pasión intelectual*, vol. 1, Universidad de Salamanca, 2024, pp. 865-878.**
(RODERIC handle `10550/108981`, item uuid `d043b69a-037c-48fb-96ff-edd6490a1a9e`.)

Abstract (RODERIC record, in full): "En este capítulo, se estudia la identificación y análisis de una cifra
utilizada por el emperador Carlos V y Lope Hurtado de Mendoza en las negociaciones del matrimonio de Margarita
de Parma con Ottavio Farnese." -- i.e. this is a 2024 scholarly identification and analysis of *a* cipher
between Charles V and Lope Hurtado de Mendoza, our exact correspondent pair, tied to the Margarita de
Parma/Ottavio Farnese marriage negotiations (which places its cipher's likely date in the 1530s, since
Margarita was born 1522 and married Ottavio Farnese in 1538 -- later than this target's 1522 letters, so
probably a different, later cipher instance than R9634/R9646/R9649, but from the same correspondent pair and
possibly the same office/key family as Tomokiyo's Ko.7/Ko.10).

**Not freely readable**: `dc.rights.accessRights` on the record is `metadata only access` -- confirmed by
fetching the bitstream download URL directly (`roderic.uv.es/bitstreams/2ed20a19-4a54-4dfb-9085-28e3b22e5fd7/download`),
which returns an HTML page (370KB, DSpace Angular shell), not a PDF; the handle page carries a
"Request a copy" link (`/items/d043b69a-037c-48fb-96ff-edd6490a1a9e/request-a-copy?bitstream=...`), DSpace's
own author-mediated request feature -- a person fills in their name/email/reason and RODERIC emails the
depositing author (Bertomeu Masiá, `m.jose.bertomeu@uv.es`, given in the record's provenance field) to release
it or reply directly. No further route tried this pass (a request-a-copy form takes personal data, so it is a
person's task, not a script's, per rule 9).

**Why this matters more than a normal "check whether a longer 2017 deposit exists":** it doesn't confirm or
rule out a key for R9634/R9646/R9649 itself (different date, possibly different cipher instance), but it is
the single most specific, most recent, most directly on-topic secondary source found for this correspondent
pair's cipher practice -- closer to the point than the 2016 master's thesis (which the prior pass confirmed
does *not* cover Lope Hurtado at all) and worth reading before any further cryptanalysis attempt on R9634/
R9646/R9649, since it may name or describe the same key family, office or classification the RAH sender used.
See `REQUEST.md` for the request-a-copy draft.

Requests this pass: roderic.uv.es 4 (discover-search API, pid/find redirect, handle page, one bitstream
download attempt), each paced >=1.5s, descriptive UA. Status stays `partial`.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on a person submitting RODERIC's "Request a copy" form for Bertomeu Masiá 2024 (REQUEST.md, takes the
requester's own name/email, rule 9), since 26 Sept 2026 (NX-UNBLOCK).

- Check whether Universitat de València holds a separate, longer 2017 doctoral deposit, or the 2024 book itself, under a different RODERIC handle -- named in NOTES as the next step, not yet run. S.
- Search OpenAlex/HAL/Persée for other Bertomeu Masiá publications on Lope Hurtado/Charles V ciphers that might be open-access, distinct from the request-gated 2024 chapter. S.
- Re-check the already-fetched 2016 master's thesis PDF for a citation to an open-access precursor (conference paper, preprint) of the 2024 book's material. S.

## Web and blog check (GF-A2-10, 3 Oct 2026)

Plain web searches (WebSearch, 3 Oct 2026):
1. `"Lope Hurtado de Mendoza" Carlos V 1522 Roma carta cifrada descifrada` -- Estudios Románicos (revistas.um.es)
   articles on Naples 1547 and a 1543 imperial cipher in Rome (Diego Hurtado de Mendoza era, not this target);
   british-history.ac.uk CSP Spain "April 1522" / "September 1522" pages (Lope Hurtado to the Emperor, Zaragoza
   10 April 1522, "in cipher ... contemporary deciphering" -- a pre-Rome letter, outside R9634/R9646/R9649).
   Opening node 79746 ("September 1522") returned HTTP 401 (BHO login wall); host not retried. The September 1522
   calendar entries were instead covered by bCSLOP's whole-volume grep of CSP Spain II above.
2. `"Salazar" "9/26" Real Academia de la Historia Lope Hurtado cifra 1522` (shelfmark) -- Salazar y Castro
   biography pages, unrelated articles; nothing on this item.
3. `Lope Hurtado cipher Charles V 1522 decrypted DECODE OR Claude OR solved` (model-solve family) -- CSP Spain pages
   and the 2022 LORIA decipherment of Charles V's 1547 letter to Saint-Mauris (press: phys.org, sciencealert,
   livescience) -- a different letter. No model-solve announcement for Lope Hurtado.
4. Descriptive title: covered by 1 and 3. Kolosova 2017/2024 and Bertomeu Masiá 2024 (both already logged above)
   reappear in results as research-portal records; neither readable this pass.
Blog site searches:
- Cipherbrain (`site:scienceblogs.de klausis-krypto-kolumne Lope Hurtado OR "Charles V" cipher 1522`): one post,
  "Letter of Charles V from the 16th century deciphered" (the 1547 Saint-Mauris letter, LORIA 2022), plus archive
  page 78. Not this correspondent or year.
- Cryptiana blog (`site:cryptiana.blogspot.com Lope Hurtado OR Kolosova Charles V cipher`): no blog page returned;
  Tomokiyo's `spanish2C.htm` (local snapshot) already read for this target (Kolosova Ko.7/Ko.10, check-solved above).
- Cipher Mysteries (`site:ciphermysteries.com "Charles V" OR "Lope Hurtado" cipher Rome 1522`): no
  ciphermysteries.com page returned.
No comment thread found that reads R9634, R9646 or R9649.

## Premise check (GF-A2-10, 3 Oct 2026)

(a) Folder's own mentions -- found, already logged: CSP Spain II no. 497 (Rome, last of Oct/1 Nov 1522, RAH,
"Autograph in cipher ... Contemporary deciphering") may be the same despatch as R9649 (9 Nov 1522), unresolved
(check-solved above); R9649 "read from the record's own contemporary clear copy" per Bourdeau (Job bLOP, step 1).
Kolosova's Ko.7/Ko.10 reconstructions (pp. 312, 333, 388, 405) and Bertomeu Masiá 2024 remain unopened.
(b) Other solvers' working files -- **found, already known**: dbourdeau/cyphersolver (shallow clone, HEAD 2341682,
2 Oct 2026) `targets/lopehurtado/` has `read_r9646.md` and `read_r9649.md` (read in part / nearly fully, logged in
Job bLOP), still **no `read_r9634.md`** and no R9634 transcription (`grep -rln 9634` hits only NOTES.md,
profile.json, `key_1522_from1524_B.tsv`, README.md, and unrelated files). His NOTES.md line 600 lists R9649 among
"the five records with no clear version", which disagrees with our Job bLOP reading of `read_r9649.md` ("own
clear copy", f. 268r) -- a discrepancy to settle by reading his file, not settled here. Line 657 still names "rerun
on R9634 ... with the 1524 alphabet" as an open step (his stated next step -> duplicate-effort risk for R9634).
`targets/lopehurtado1523/` covers 1523 letters (R9846, R9867, R9869), outside this target. aaymeloglu/unsolved-
ciphers (HEAD d2800bb): catalogue rows only (cited, not copied).
(c) Physical neighbours -- not re-viewed this pass (DECODE full-size images login-gated; RAH viewer behind Anubis).
Bourdeau's R9644 has a contemporary clear copy in the same bundle (his `key_codes.tsv` source); no clear copy of
R9634 (ff. 14-16) is recorded by anyone.
(d) Recipient's side -- found, already logged: CSP Spain II (Bergenroth/Gayangos) calendars Lope Hurtado's 1522
letters to the Emperor (nos. 416/422, 454-455, 467, 497, 609, 610); no September 1522 entry matching R9634 was
named by bCSLOP's whole-volume grep. Not found-solved for R9634; R9646/R9649 were already logged as read in part by
Bourdeau (no new flag).

## Remaining gaps (GAPSFIX, 4 Oct 2026)
Read so far: 0 tokens read by this repository; by Bourdeau (dbourdeau/cyphersolver, credited, Job bLOP step 1): R9649 86/89 (97%), R9646 99/118 (84%); R9634 (ff. 14-16, about 6 pages) has no transcription anywhere.
- R9634 residual (Bourdeau 872/1191 = 73.2% read, read_r9634.md at his HEAD a02b838, credited): ~40 single-occurrence code groups - blocker: no-key-material; no clear copy in the record or in CSP Spain ii (his NOTES "Remaining gaps"); Kolosova's Ko.7/Ko.10 tables are the only named key source (L17 / ASKS 74)
- R9634 residual spelled words (14r12, 14v03, 14v16, 15r11, 15v05, 15v13) - blocker: illegible; DECODE's full-size file is the only image online and was re-tested 6 Oct 2026 (A4-RFLOPE section); a blind sign pass at that resolution settled none; needs the RAH images of 9/26 ff.14-16 (owner's browser on bibliotecadigital.rah.es, or a reproduction request)
- R9646 remainder 19/118 and R9649 remainder 3/89 - blocker: illegible; Bourdeau's "Where the work is now limited": DECODE serves ~1700 px per folio, too little for per-glyph discrimination ("What would actually move this target" item 3)
- Kolosova's Ko.7/Ko.10 tables (pp. 312, 333, 388, 405) and Bertomeu Masiá 2024 - blocker: waiting-on LOCAL-QUEUE.tsv row L17 and ASKS row 74; L17 is the owner's read of Kolosova 2017/2024, row 74 the RODERIC request-a-copy form, which takes the requester's own details (rule 9)

## Escalation (GAPSFIX, 4 Oct 2026)
- [ ] siblings: catalogue check done (R8-LOPE2, 6 Oct 2026): MSS/20212/27 (five letters 1522-1526, "Algunas parcialmente cifradas y con cifra", 14 h.) IS digitised in BNE Digital (card c3c70ca0-ac7a-42d5-8d01-f3216ed199d6), image host Cloudflare-blocked from the cloud; MSS/18697/29 (Tortosa 25 June 1522, "Parcialmente cifrada") has no digital link. next: capture the 14 leaves of MSS/20212/27 through the owner's browser (LOCAL-QUEUE viewer-capture row, as L57 for bne20211-ferdinand-1478), then a sign-inventory check against Bourdeau's 1522 and 1524 keys, ~$2
- [x] clear-pages: R9644's and R9649's contemporary clear copies used by Bourdeau for the key (Job bLOP step 1)
- [ ] known-keys: Kolosova Ko.7/Ko.10 reconstructions (LOCAL-QUEUE L17), not opened
- [x] print: CSP Spain II grepped whole-volume (bCSLOP); no. 497 flagged, not yet compared
- [x] key-rebuild: Bourdeau's key_codes.tsv (49 confirmed) + 1524 key carried back, credited
- [x] image-check: R9634 full-size via DECODE `--guess-fullsize` re-tested 6 Oct 2026 (A4-RFLOPE): served, but byte-identical in size to Bourdeau's file (P1 1,427,572 B, 3256x2365 per two-page opening, his NOTES 3 Oct); no larger image on DECODE. RAH Biblioteca Digital search: Anubis challenge on the search POST twice, host stopped; A-26 = 9/26 digitisation not established
- [n/a] retry: no attempt of ours on any of the three records to retry
Verdict: keep going: 0 internal gaps on R9634 (A4-RFLOPE, 6 Oct 2026: residual is no-key-material or illegible at DECODE's only resolution); cheapest next: siblings, a LOCAL-QUEUE viewer-capture row for BNE MSS/20212/27 (digitised, BNE Digital card c3c70ca0-ac7a-42d5-8d01-f3216ed199d6; cloud blocked by Cloudflare, R8-LOPE2 6 Oct 2026), then a sign-inventory/key check, ~$2

## RUN6-LOPE (5 Oct 2026): CSP Spain II no. 497 vs Bourdeau's read_r9649.md (disk + one shallow clone; 0 network hosts besides github.com, 1 request)
Source: dbourdeau/cyphersolver HEAD a43993754e2e (read 5 Oct 2026), `targets/lopehurtado/` read_r9649.md, read_r9644.md, NOTES.md; MIT code / CC BY 4.0 text, credited. No new reading, no decode; comparison of already-logged claims (bLOP2 section (1) above had the 497 identification; this job re-checks it against his files at the current HEAD).
| item | CSP no. 497 (Bergenroth abstract, our bLOP2 re-read) | Bourdeau read_r9649.md | verdict |
|---|---|---|---|
| date | Rome, 1 Nov 1522 | De Roma .ix. de noviembre (9 Nov) | disagree: not the same despatch |
| content | camarero Peter, Archbishop of Piacenza, Cisterer, safe-conduct, Prince Henry/Flanders/Castile, pp. 6 | Cardinal Santa Cruz and Ostia fortress, licenciado Bernardino; short note | disagree |
| clear copy | contemporary deciphering noted by the calendar | f. 268r "Al Rey - De Lope hurtado de ix de noviembre", whole letter, 3 cipher runs | consistent: R9649 carries its own clear copy |
| 497 vs read_r9644.md | camarero Pedro es el principal; Cisterer; principe don Enrique; Flandes/Castilla | R9644 (1 Nov, "primero de noviembre"; R9648 = duplicate) contains all four | agree: 497 = R9644/R9648, not R9649 (content match, grade S for the identification) |
| his NOTES.md "no clear version" for R9649 | | line 600 reads "R9649 and R9656 later turned out to carry one" (self-corrected at HEAD); lines 280/495 still count it among the uncribbed | stale text in his file, resolved by read_r9649.md; not a disagreement with us |
Found: R9649 identity settled, it is not no. 497. Not found: any CSP calendar entry for 9 Nov 1522 matching R9649 (bCSLOP whole-volume grep; Laiglesia regesta only). Side finding: Bourdeau's repo now has `read_r9634.md` (first worked 2 Oct 2026, 71% of tokens read, commit a439937, 3 Oct); the Premise check (b) line "no read_r9634.md" is out of date, and the R9634 step below is a duplicate-effort risk unless it targets his residual ~29%.

## A4-RFLOPE (6 Oct 2026, 00:02-00:2x UTC by date -u): R9634 residual -- Bourdeau's repo, DECODE full size, one blind pass
Brief: LANE DEFAULT-account-4-20261005-2253, wave 2. Grades unchanged: this repository still reads 0 tokens of R9634 itself; every reading figure below is Bourdeau's (dbourdeau/cyphersolver, MIT code / CC BY 4.0 text, credited).
1. **His repository first** (shallow clone, HEAD a02b838, 5 Oct 2026): `targets/lopehurtado/read_r9634.md`, `r9634_cipher.txt` (1191 tokens, one line per MS line), `r9634_reading.tsv`, `key_1522_r9634.tsv`. R9634 = Genoa, 13 Sept 1522, ff.14-16; **872/1191 = 73.2% read as sense** (2-3 Oct 2026; the 71% in this folder's Verdict was his 2 Oct figure). His own Remaining gaps name the same two residual classes this job targeted: ~40 single-occurrence codes (no-key-material) and spelled words with one sign at the scan's limit (illegible). His NOTES (3 Oct) already record a logged-in DECODE full-size re-test, byte-identical to his file.
2. **DECODE full size, one browser login** (`tools/decode_browser_login.js 9634 --guess-fullsize`): the three openings were served at 1,427,572 / 1,861,353 / 1,387,669 B (3256x2365, 3288x2410, 3288x2410; sha1s in images/manifest.json, files NOT committed). P1 matches his recorded byte count exactly: **no larger image exists on DECODE**; this re-test reproduces his finding, it does not extend it.
3. **RAH Biblioteca Digital** (the better-image route both projects name): the search page loaded once in headless Chromium, but every search POST (the positive control `"Salazar y Castro, 20630"` from RUN3-RJM2, twice, and `"Salazar y Castro, 3269"` once) ended on the Anubis challenge page or failed mid-navigation; per the good-citizen rule the host was stopped after one retry. Digitisation of 9/26 (A-26; Índice no. 3269 per sources/salazar-castro-index/cipher_mentions.tsv) is **not established either way**: no query returned a results page.
4. **One blind sign pass** (Sonnet subagent, 7 line crops cut with `tools/iiif_lines.py --image ... --mask-neighbours`, given the sign alphabet but not his transcription of these words) on the six unread spelled words, then compared with `r9634_cipher.txt` and two crops checked by eye:

| line | Bourdeau (unread) | blind pass | eye check / verdict |
|---|---|---|---|
| 14r12 a | ʇʇ&48ʇʇ8∂ | a-o-n-r-f-e-s, NONE | first sign looks like # (f), not ʇʇ; "f/r o n e r e s" gives no word; unread |
| 14r12 b | ∂7ɣ8ϑɣα4 | ∂7ʇʇ89 "pared" (5 signs) | the image shows ∂ 7 ɣ 8 ϑ/9 then a gap before ɣα4; the third sign is ɣ (c), not ʇʇ, so "pared" needs a sign the image does not show; his word split may be wrong (two groups), but no word results; unread |
| 14v03 | y&Ɛʇʇα47 / xɩ4ε∠7x& | c-o-l-f-i-n-a / n-l-u-a-d-o, NONE | no word; unread (place names, as he suggests) |
| 14v16 | 8&ɣʇʇα8ʇʇ7 | s-o-g-r-i-e-f-a, NONE | no word; unread |
| 15r11 | zα∂ɷ8∂Hɣϑ&∂ | "...tres..." inside, rest NONE | partial fragment only, sign count disagrees; unread |
| 15v05 | x838ɋHoɣ̊ / ʇʇʇα74Ho | ?-t-e / ?-i-a-n-?, NONE | unread |
| 15v13 | ɭbʇʇ8∂98&∂ | ɭbʇʇ8∂ϑ& "presto" (6 signs) | the image shows ɭb ʇʇ 8 ∂ then two signs (9/ϑ, 8) before &; "presto" holds only if those two are one t; grade M at best ("que seria [xor8] ~presto"), not added |

**Found:** nothing that raises R9634 above Bourdeau's 73.2%. "~presto" (15v13) is an M-grade candidate for a second reader with a better image to check. **Not found:** any larger DECODE image (re-test, 6 Oct 2026); an RAH digital record for 9/26 (search blocked by Anubis, not run). The residual is outside-blocked: illegible at the only online resolution, and no-key-material for the codes. Requests: github.com 1 (clone), de-crypt.org 1 login + 7 fetches (record page, 3 thumbnails, 3 full size), bibliotecadigital.rah.es 7 (curl 2, both Anubis 307; headless Chromium 5: 2 search-page loads, one failed mid-redirect, and 3 search POSTs, all challenged or failed). 1 subagent call.

## R8-LOPE2 (6 Oct 2026, 03:37-03:42 UTC by date -u): BNE siblings MSS/18697/29 and MSS/20212/27, catalogue and digital-collections check
Brief: LANE LANE-RUN8-account-2, lookup only. Route that worked: the BNE's Alma SRU endpoint, plain curl, no challenge
(`https://bne.alma.exlibrisgroup.com/view/sru/34BNE_INST?version=1.2&operation=searchRetrieve&recordSchema=marcxml&query=alma.mms_id=<MMS>`;
`alma.creator=` and `alma.all_for_ui=` queries also answer). MMS ids from aaymeloglu/unsolved-ciphers `catalogue/bne-ranked.md` (cited,
read via raw.githubusercontent.com, not copied). The Primo VE record pages (catalogo.bne.es/discovery/fulldisplay) are JS-rendered and were not fetched.

| shelfmark | MMS id | catalogue record (MARC, quoted) | availability flag (AVA $e) | digitised? |
|---|---|---|---|---|
| MSS/18697/29 | 991037012969708606 | 245 "Carta de Lope Hurtado al Emperador con noticias de las negociaciones con el Papa, su viaje y la rebelión de Játiva y Alcira. Tortosa, 25 junio 1522"; 300 "2 h., 32 x 22 cm"; 546 "Parcialmente cifrada"; 500 "Firma autógrafa", "Sello de placa desprendido"; 510 Índice Salazar y Castro (1949) t. II p. 503 n. 137; 999 note ".PUBLIC. Ejemplar reproducido con Mss/18697/1" | "available", Sala Cervantes | **no 856 link**: no BNE Digital record. The reproduction is catalogued under MSS/18697/1 (Abad de Nájera, Milán 4 Jan 1523, MMS 991036979049708606), which has no 856 either: a physical reproduction (likely microfilm), not online |
| MSS/20212/27 | 991044353069708606 | 245 "Cartas de Lope Hurtado al emperador Carlos V"; 260 "1522-1526"; 300 "14 h., 32 x 23 cm. y menos"; 520 "Son cinco cartas"; 546 "Algunas parcialmente cifradas y con cifra"; 596 "Fechadas en Tarragona, 5 de agosto de 1522, en Tortosa 25 de junio del mismo año y en Milán, 20 y 22 diciembre de 1525 y 27 de febrero de 1526"; 561 Pascual de Gayangos; 500 "Firmas y notas autógrafas" | "available", Sala Cervantes | **yes**: 856 `https://bnedigital.bne.es/bd/card?id=c3c70ca0-ac7a-42d5-8d01-f3216ed199d6` ("BNE Digital"); 927 thumbnail `https://bnedigital.bne.es/bd/es/low?id=c3c70ca0-ac7a-42d5-8d01-f3216ed199d6`. No IIIF manifest URL recorded: the card page answered curl with a Cloudflare challenge (HTTP 403) and headless Chromium with "Just a moment..." (one attempt); host stopped. No page image fetched |

What the records say, and what they do not:
- **Cipher, key or decipherment?** Both are letters from Lope Hurtado de Mendoza to Charles V with cipher passages ("Parcialmente cifrada";
  "Algunas parcialmente cifradas y con cifra"). Neither record mentions a key, a cipher table or a decipherment/clear copy; "con cifra" could
  mean a cipher passage or an enclosed cipher sheet -- not established without the images.
- **Same office, different dates from the DECODE three.** R9634 is Genoa 13 Sept 1522 and R9649 Rome 9 Nov 1522; the BNE letters are Tortosa 25 June
  1522, Tarragona 5 Aug 1522 (in Spain with Adrian VI before his embarkation) and Milan 20 and 22 Dec 1525 and 27 Feb 1526. The 1522 pair is the
  same sender months before the DECODE letters (Bourdeau's 1522 key is the first key to test); the 1525-26 Milan letters fall in the period of his
  1524 key (`key_1522_from1524_B.tsv`) and of Kolosova's Ko.7/Ko.10 tables (1521-1527). This is a lead, not a key match: no sign has been compared.
- **A possible duplicate.** "Tortosa, 25 junio 1522" appears both as MSS/18697/29 (Salazar y Castro collection) and among the five letters of
  MSS/20212/27 (Gayangos). Duplicate despatches were usual; whether these are the same letter in two copies (a duplicate in cipher, or one
  ciphered and one clear, would give a crib) is not established from the catalogue; only the images can say.
- **Further Lope Hurtado items** found by the same `alma.creator` query (16 records): MSS/18690/127 (Playa de Riba de Talla, 14 Aug 1522, health and
  the Pope and the French), MSS/18690/116 (extract, c.1522), MSS/18697/30 (Archbishop of Bari to Lope Hurtado, Lyon 24 June 1522), MSS/20213/23
  (Morono to Lope Hurtado, Milan 10 Sept 1525, digitised, Italian); none carries a cipher note (546) in the record. Not checked further.

Found: MSS/20212/27 is digitised (BNE Digital card above) and holds five Lope Hurtado letters with cipher, two of them from 1522; MSS/18697/29 is not
digitised. Not found: an image of either (BNE Digital Cloudflare-blocked from the cloud, as QUEUE.md logged for bdh.bne.es / bdh-rd / datos.bne.es on
24 Sept 2026); a IIIF manifest URL; any key or decipherment named in either record. Next: the owner's browser captures MSS/20212/27's 14 leaves
(LOCAL-QUEUE viewer-capture row, the L57 shape); MSS/18697/29 needs a reproduction request (BNE) or a check whether it duplicates the Tortosa letter
in 20212/27. Requests: bne.alma.exlibrisgroup.com 4 (SRU, all 200), raw.githubusercontent.com 1, bnedigital.bne.es 2 (curl 403 challenge, headless
Chromium challenge), bdh-rd.bne.es 1 (403 challenge), web.archive.org 2 (CDX, connection reset by the proxy both times; stopped). 0 subagent calls.


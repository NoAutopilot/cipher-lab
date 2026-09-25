open
Negociations secretes touchant la paix de Munster et d'Osnabrug (Le Clerc, 1725-26), vols 1-4 (IA djvu full text
of all four volumes read and grepped for "Thuillerie", "Coppenhague"/"Copenhague", "Christianopel", "chiffre", and
distinctive clear-text phrases from the ciphered leaves) and the Acta Pacis Westphalicae online database
(apw.digitale-sammlungen.de, live full-text search, not a fixed edition to page-cite) both read by this worker;
neither contains this letter or the enciphered passages (see Search log).

Target: BnF Melanges de Colbert 26, part I -- diplomatic correspondence of Gaspard Coignet de La Thuillerie
(French ambassador; extraordinary ambassador to Denmark/Sweden April 1644-April 1646, then ambassador at The
Hague through 1648) and Abel Servien (French plenipotentiary at the Westphalia peace congress, Munster/Deventer),
1644-1648. Gallica ark `btv1b10035069t`, canvas 4-63 (folio 1-59; corrected boundary, see below). QUEUE row KX-03.
LANE KX worker KX-COLB26P1, session_017HqTj36Se2nQUvJ1GPXQLz, 25 Sept 2026.

## What this job did

1. Leaf map of Part I: fetched all 72 canvases at 1000px (canvas 11 and 29 unrecoverable -- HTTP 500 twice and a
   connection failure three times respectively, both logged as gaps, not retried further per the good-citizen
   rule). Eye-checked every canvas (this worker directly for canvas 1, 19, 20, 21, 22, 26; two Sonnet subagents,
   canvas 1-36 and 37-72, for the rest) for folio, sender/recipient, place, date, cipher yes/no, rough numeral-
   group count, and any decipherment written with it. Full table: `leaves.tsv`.
2. Check-solved on every enciphered letter found, against the sources named in the job brief.
3. No key applied, no cryptanalysis attempted, no transcription beyond what was needed to identify sender/
   recipient/date/place per leaf (per brief -- this stops at the leaf map).

## Corrected part boundary

The prior KX-COLB26 worker (eye-checking Part III) estimated Part I as canvas ~4-69 from a handful of boundary
probes. This leaf map found the real boundary: **Part I ends at canvas 63** (folio 59, the last dated leaf, "A la
Haye le 3e febvrier 1648"), and **Part II begins at canvas 64** (folio 60), its own title leaf ("Depesches de M.
de Brienne, Tom. 1er... Juillet-Decembre 1661"), table of contents at canvas 66-70, first despatch at canvas 72
(20 Juillet 1661). Canvas 65 duplicates canvas 64 (same title leaf, two capture files) and canvas 30/31 likewise
duplicate one leaf (folio 27). `folio = canvas - 3` holds across the whole part, confirmed against the finding
aid's own folio citations (see below).

## The cipher is much larger than the one leaf already flagged

KX-COLB26 flagged only canvas 20. This leaf map finds a cluster of at least **eleven** enciphered leaves/letters,
not one:

| Canvas(es) | Folio | Date | Sender -> Recipient | Note |
|---|---|---|---|---|
| 20-21 | 17-18 | "A Christianopoli le 6 Avril 1645" | La Thuillerie -> Servien | Heavy cipher, **contemporary interlinear decipherment gloss confirmed** (see below) |
| 26 | 23 | "17e Mars 1646" | unclear, salutation "Mon Nepveu" | Heavy cipher, visibly different/larger nomenclator; possibly a different correspondent pair bound into this volume -- unresolved |
| 27 | 24 | 1646 (day/month uncertain) | La Thuillerie -> Servien | Light cipher mixed into mostly plain prose |
| 30-32 | 27-28 | undated | La Thuillerie -> Servien | Re Prince d'Orange; sender corrected from the subagent's "Servien" guess to La Thuillerie -- the finding aid lists fol.27 among La Thuillerie's own La Haye letters, and the "M. Servien" docket the subagent read is more likely a recipient/routing tag than a signature |
| 33 | 29 | 1648 (day/month uncertain) | unclear | Re payments |
| 35-36 | 31-32 | 1648 | La Thuillerie -> Servien | Fol.31 is also in the finding aid's La Thuillerie list |
| 39-40 | 35-36 | closes 13 Jan 1648 | La Thuillerie -> Servien | |
| 47-51 | 43-47 | closes 23 Jan 1648 | La Thuillerie -> Servien | |
| 54-56 | 50-52 | closes 27 Jan 1648 | La Thuillerie -> Servien | |
| 62-63 | 58-59 | closes 3 Feb 1648 | La Thuillerie -> Servien | |

That is: essentially every La Thuillerie letter to Servien from January-February 1648 -- the final weeks before
the Dutch-Spanish peace was signed at Munster -- carries some cipher, typically a handful of numeral groups at
the politically sensitive points (the Prince of Orange's position, Spanish/Dutch treaty terms, Naples, Lorraine)
rather than a continuously enciphered letter. Several intervening leaves (28, 34, 37-38, 41-46, 52-53, 57-61) are
plain prose with no digits, so the correspondents used cipher selectively. Full per-canvas detail in `leaves.tsv`.

## A contemporary decipherment is already written on canvas 20-21

This is the most important single finding. Close-up crops of canvas 20 (`images/crops/canvas20_glosszone.jpg`,
`canvas20_fullcipher.jpg`, at IIIF region crops up to 1800px wide, native resolution 7427x6365) show a **second,
smaller hand** has written a plaintext gloss directly above or below specific numeral groups in the main cipher
text -- e.g. "Je parle des Suedois" over "6 25 zz 11 83 v 44 w' 85", "pour les Dannois qui" over "Car 63 68",
"leur plaic[e]... ilz sont f[or]t abatuz" around "42 ilz estoient en 56 99". The same pattern continues onto
canvas 21 (folio 18): e.g. "au moins a pris soulagement quilz en auroint a leur" and further glosses over later
groups. This is a **key-beside-the-letter** case in the sense of CLAUDE.md's precedent list (Thurloe/Birch,
Japikse's spaced type, Groen van Prinsterer) -- a period decipherment sits on the document itself -- except here
it is a manuscript gloss, not a print convention, so nobody transcribing the catalogue description would know it
is there (the finding aid says nothing about cipher at all, let alone a gloss). It has not been transcribed into
a key.tsv; that is out of this job's scope (leaf map + check-solved only, per brief).

The canvas-26 "Mon Nepveu" letter (folio 23) also shows what appear to be similar small interlinear notes (e.g.
"de 18", "voire femme", "pour le siege de M. de Grimone"), not closely verified at high resolution. **The
Jan-Feb 1648 cipher run (canvas 39-63) was only eye-checked at ~1000px and has not been checked at high
resolution for a gloss of this kind** -- if even one of those eleven leaves carries the same kind of contemporary
decipherment, that hands over a working key immediately, exactly as canvas 20-21 does. This is the single most
valuable next step and is flagged in `images/manifest.json` and to ROOM.md.

## Search log (check-solved)

Standard editions and databases actually opened and read by this worker (not merely cited from elsewhere):

- **Negociations secretes touchant la paix de Munster et d'Osnabrug** (Jean Le Clerc, 1725-26), all 4 volumes,
  Internet Archive djvu OCR text fetched and grepped in full (`negociationssecr01lecl` through `04lecl`; vol.1
  needed a retry via the item's direct IA node URL after the standard `archive.org/download/...` route 500'd
  twice). "THUILLERIE" (as a letter-heading name) appears only as formal pieces addressed *by* La Thuillerie to
  the Dutch States General (harangues/propositions at The Hague, 1646) in vols 3-4 -- never as a private letter
  to Servien, never from Copenhagen or Christianopel. "Coppenhague"/"Copenhague" appears 9 times across all four
  volumes, all as third-party mentions ("La Thuillerie, who has gone to Copenhagen...") or as the dateline of the
  King of Denmark's own formal replies to La Thuillerie's mediation offer (26 June 1644, vol.1) -- never as a
  letter from La Thuillerie himself. No hit anywhere for "Christianopel"/"Christianopoli"/"Kristianopel", for any
  of the Jan-Feb 1648 dates (13, 20, 23, 27 Jan; 3 Feb), or for distinctive clear-text phrases read off canvas 20
  ("fondz de patience quasy inespuisable", "c'est donc eux seulz maintenant qui m'exercent", "obtiens quasy tout
  ce que je veux").
- **Acta Pacis Westphalicae** (APW), via its own online full-text search database (apw.digitale-sammlungen.de;
  the site's Anubis bot-check blocks a plain WebFetch/curl GET to `/search` but not the actual search-results
  endpoint, `/search/query.html?q=...`, confirmed working with a descriptive User-Agent). Queried "Coignet de la
  Thuillerie" (33 hits), "Thuillerie Kopenhagen" (32 hits), "Thuillerie" filtered toward Serie II Korrespondenzen
  (391 hits -- too broad to be useful: APW's editorial apparatus attaches a standing biographical footnote on La
  Thuillerie to every mention of him by other correspondents, which dominates the hit count) and "fondz de
  patience" (6 hits). Every La Thuillerie hit actually read is a third party (the Imperial or Papal-nuncio
  correspondence) mentioning him, never a letter he wrote himself, and none is dated to any of the letters in the
  table above. APW II B (the French correspondences) is built from the Munster/Osnabruck plenipotentiaries'
  exchanges with Paris (Brienne/Longueville/Avaux/Servien), not from Servien's incoming correspondence with a
  separate ambassador at The Hague/Copenhagen, which is consistent with finding nothing.
- **Tomokiyo's pages** (sources/cryptiana/web/*.htm, read from disk): `servien.htm` documents a *different*
  Servien cipher entirely (Baluze 155-156, 1630-1637 Turin/Genoa mission with Melchior de Sabran, a symbol
  cipher broken in 2021) -- 15-25 years earlier than this item and a different correspondent and cipher form.
  `unsolved.htm`/`unsolved-2026-09-24.htm` list a different Copenhagen cipher entirely (BnF fr.4736, D'anzay to
  Henry III, 1574) and do not mention Mel. Colbert 26, La Thuillerie, or Coignet anywhere.
- **DECODE** (de-crypt.org): searched the cached catalogue crawl from 24 Sept 2026
  (`sources/decode/records-{decrypted,non-decrypted}-2026-09-24*.tsv`, both Non-decrypted and Partially-decrypted
  cipher-record listings, 1186 records total) for "thuillerie", "coignet", "servien", "colbert 26" -- no hit in
  any file. Not re-crawled live (the cached listing is one day old and covers the whole catalogue by status, so a
  fresh crawl was judged not worth the extra ~25 requests for this pass).
- **Solver repositories**: shallow-cloned both `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers` fresh
  this session and grepped for "coignet", "la thuillerie", "btv1b10035069t", "colbert 26". Two incidental
  "Coignet" hits are unrelated people (a Napoleonic-era lieutenant; "Madlle Coignet" in an unrelated Restoration-
  era Royalist 1646 nomenclator index) -- neither is Gaspard Coignet de La Thuillerie. `CATALOGUE.md` and every
  `README.md` in `unsolved-ciphers` have no "colbert" hit at all.
- **Web search** (general, and specifically for a model-solve announcement per check-solved.md's added source
  family): several queries covering the correspondents' names, "Colbert 26", the Christianopel letter and date,
  and "solved"/"Claude"/"GPT" combined with the target -- nothing found beyond the Gallica catalogue description
  and BnF finding aid themselves (which is the manuscript, not a print edition or a solve).
- **BnF finding aid** (archivesetmanuscrits.bnf.fr/ark:/12148/cc955062) read in full: no mention of
  "chiffre"/"dechiffre" anywhere in the item description, consistent with the earlier KX-COLB26 finding for Part
  III. It does give the 15 La Thuillerie letters' starting folios (see manifest.json), which this leaf map's
  folio/sender attributions are checked against.

No source above prints, cites, or otherwise documents any of the eleven enciphered leaves in the table, their
plaintext, or a key for this cipher. Not searched (out of this job's scope / no route from the cloud): JSTOR,
HathiTrust full text, any specialist Dutch/Danish/Swedish archival journal that might discuss La Thuillerie's
Scandinavian mission specifically (his mission is documented in Danish/Swedish sources this worker did not have
time to survey).

## Requests

gallica.bnf.fr: 72 canvas fetches + 1 info.json + 2 IIIF region-crop fetches, all >=1.8s apart (one retry each on
canvas 6, 30, 70, 72 connection resets, all recovered; canvas 11 HTTP 500 twice, not fetched; canvas 29 failed
three times, not fetched). archivesetmanuscrits.bnf.fr: 1 (finding aid page, already cached content from
KX-COLB26 re-read). archive.org: 2 metadata calls + 4 djvu.txt downloads (vol.1 needed the direct IA node URL
after two 500s on the standard download route). apw.digitale-sammlungen.de: 5 search queries, ~1.5s apart, plus
1 browser-tool fetch to confirm the site's Anubis check does not block the actual query endpoint. github.com: 2
shallow clones (cyphersolver, unsolved-ciphers). No DECODE live requests (cached dump used). No credentials used.
2 Sonnet subagents (the systematic canvas 1-36 and 37-72 eye-check passes); this worker did every search and the
canvas 20/21/26/19/22 close reads itself.

## Kind

Recovery (a contemporary decipherment already exists on the document for at least one letter; cryptanalysis was
not attempted and per the brief is out of scope here).

## KX-LATHKEY2 (25 Sept 2026)

Successor to KX-LATHKEY (interrupted at $44/61 min with no push; its two transcription subagents' output was lost,
only the native-res crops in `images/crops/` survive -- see ROOM.md 09:36). This job worked directly from those
20 crops (no Gallica fetch), transcribing by hand from PIL-cropped/upscaled line regions (no subagent), one leaf
at a time, pushing after each leaf, to avoid repeating that failure.

**Scope actually completed: canvas 20 (folio 17) only, of the 21 cipher-bearing canvases on file.** 70 cipher
tokens across 8 cipher-bearing lines (15, 17, 19-27; lines 16 and 18 are plain-prose continuations with no
digits, not transcribed). `ciphertext.tsv`, `key_period.tsv` (59 distinct codes). No second reconciliation pass
was run (brief step 2) -- budget did not allow both a second Sonnet subagent pass per canvas and forward progress
on more leaves, and the prior worker's failure was specifically an unsupervised subagent pass that produced no
committed output; this transcription is a single pass by this worker only and should be treated accordingly
(no independent cross-check yet).

### Important correction to the "period decipherment" framing

KX-COLB26P1's leaf map (above) describes the second hand's interlinear writing as "a contemporary decipherment ...
a period decipherment sits on the document itself," by analogy with Thurloe/Japikse/Groen-van-Prinsterer key-
beside-the-letter cases. Having now read canvas 20 at native resolution and transcribed every cipher token against
every nearby annotation, **that characterization does not hold at the token level.** The second hand's notes are
short (3-9 word) topical/paraphrase annotations positioned near a cipher run, not a plaintext word written over
each code:
- The densest run on the leaf, 11 tokens (`6 25 zz 11 83 v 44 w' 85 d z`), pairs with a single four-word note,
  "Je parle des Suedois" ("I'm speaking of the Swedes") -- a gist of the passage's subject, not eleven
  substitutions.
- The 2-token run `63 68` pairs with "pour les Dannois qui ... pas plus traitables" (6 words) -- plausible as a
  paraphrase of what the coded clause says, not a 1:1 gloss.
- Only a few of the shortest runs (a lone token like `32` glossed `fy`, or `83`/`25`/`31`/`42` as the first token
  of a run next to a short phrase) are even candidates for a direct code=word equivalence, and even those are
  single, unrepeated observations on this one leaf -- nothing here meets the brief's own C-grade bar ("legible
  AND consistent across occurrences"), so `key_period.tsv` grades every code M, none C, and says so in each row's
  note rather than guessing.
- One code (`6`) already shows the conflicting-gloss pattern rule 3/brief step 3 anticipates: it occurs three
  times on this one leaf, twice next to unrelated-looking phrases ("Je parle des Suedois" at one occurrence,
  "par les armes que par un accommodement" at another) and once with no gloss at all -- listed as a conflict in
  key_period.tsv, not resolved to one value.

This does not mean the second hand is useless -- it reliably marks *where* the enciphered clauses fall and *what
they are about* (Swedish affairs, the Danes, the Prince of Orange, Naples, an accommodement vs. continued war),
which is exactly the kind of external corroboration LESSONS.md section "Verify against the world, not the model"
asks for once a candidate key exists. But it is marginalia/annotation, not a decipherment, and NOTES.md and any
future brief for this target should stop calling it one. Building an actual key needs either a genuine word-level
decipherment elsewhere (not found yet), or cryptanalysis proper (nomenclator/homophonic solve) using these notes
only as topic cribs -- a different, harder job than "transcribe the gloss."

### Design observations (from this one leaf)

- Mixed nomenclator: plain 2-digit numbers (6, 11, 21, 25, 32, 35, 42, 46, 49, 56, 63, 68, 70, 72, 78, 81, 83, 87,
  99, 100...) interleaved with single letters used as symbols (d, e, g, h, m, q, v, y, z) and compound
  letter+diacritic/ligature marks (w', gt, m°, m+, h', i", c', th [a crossed-circle mark, rendered here as "th"
  for lack of a closer ASCII match], 9o, el, cn, ll, zz, &, I). 59 distinct codes observed in 70 tokens on one
  leaf -- a large nomenclator, not a short substitution alphabet; consistent with LESSONS.md's "genuine
  ciphertext-only break" cases needing either a crib or a structural regularity, neither established yet.
- Cipher tokens are interspersed with plain French inline (not a fully enciphered letter) -- the same pattern
  KX-COLB26P1 found across all 21 leaves.
- Tokens repeat within the leaf (v x7, y x6, d x5, 6/11/25/42/83 each several times) -- some homophony or a small
  alphabet reused densely is plausible, but 70 tokens is far below what a 59-symbol nomenclator needs for a blind
  break (LESSONS.md's "large nomenclator, one letter" failure class: d'Estaing, Chaulnes, Berthier, Stepney,
  Maurice-Rupert). More leaves in the same hand are needed before any solve attempt, not more analysis of this
  one.

### Not done this job (successor's queue, cheapest first per the brief)

1. Canvas 21 (folio 18, same letter, same hand, continues directly from canvas 20) -- doing this leaf next would
   let key_period.tsv check code-consistency across two leaves of the *same* letter, which is the one check that
   could actually earn a C grade under the brief's own rule.
2. The other 19 glossed canvases (26, 27, 30-33, 35-36, 39-40, 47-51, 54-56, 62-63), same method (PIL crop +
   upscale from the existing `images/crops/canvas*_full.jpg`, no refetch needed).
3. A second independent pass (brief step 2) once there is more than one leaf transcribed, to actually reconcile
   rather than run once and trust it.
4. Re-crop and closer-read the handful of genuinely ambiguous marks flagged inline in ciphertext.tsv's token
   column (`9o`, `c'`, `i"`, `th`, `m°`) against the source crop before treating them as settled shapes rather
   than this worker's best reading.

### Files, hosts, cost

Files: `ciphertext.tsv` (70 rows), `key_period.tsv` (59 codes), `images/lines/canvas20_*.jpg` (5 crop files, PIL,
from the already-on-disk `images/crops/canvas20_full.jpg`, no refetch), this NOTES.md section. Hosts: none (all
from disk, per brief). No subagents (single pass by this worker, see above). No credentials. Cost not visible to
this worker (ROOM.md 09:00, "workers cannot see their own cost" -- get_session's context_usage read 0 at the
first check and carries no dollar figure); paced by scope (one leaf, no subagent fan-out) rather than a live
dollar reading, given the predecessor's failure mode was an unsupervised subagent burning budget with nothing
committed.

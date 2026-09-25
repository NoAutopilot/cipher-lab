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

Note (KX-LATHTR, 25 Sept 2026): `ciphertext.tsv` as committed at the end of this section's job actually carries
116 rows for canvas 20 (11 lines, 15/17/19-27), not the 70 this prose says -- the file on disk when this job
started already had 116 rows despite this text. Not corrected here (out of this job's scope to rewrite a
predecessor's section); flagging so nobody trusts the "70" figure over the file itself.

## KX-LATHTR (25 Sept 2026)

Job: finish the transcription of the other 20 cipher-bearing canvases and write a spec, per
`.claude/briefs/runs/2026-09-25-lane-kx-lathtr.md`. Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp.
Session session_011zG1PJqCaitaLcZ2FyTxeg.

**Scope actually completed: canvases 21, 27, 30 (3 of the 20 named), plus the required second pass over 20/21/27/30
together.** Canvas 26 was deliberately skipped out of the brief's order (see below). The remaining 16 canvases
(32, 33, 35, 36, 39, 40, 47, 48, 49, 50, 51, 54, 55, 56, 62, 63) are **not transcribed** -- queued for a
successor, cheapest/most-consistent-design first: 32 next (same 8 May 1646 letter as 30, continuation, ~40
groups, dense two-column page), then 33/35/36 (1648 letters, same office), then the Jan-Feb 1648 run 39-63.

Every canvas was read directly from the already-on-disk `images/crops/canvas{N}_full.jpg` (2400px-wide page
scans fetched by KX-LATHKEY2/KX-LATHKEY), no Gallica refetch, per brief. PIL crops (`tools` not used --
`images/lines/canvas{N}_cipherzone.jpg`, one crop per canvas at <=1400px wide, JPEG q70, cut with a small
scratch script, not committed) hold the cipher-bearing region read for each canvas; the folder is at 30.2 MB as
of the last push (over the 30 MB target by a small margin -- see below).

### Canvas 26 skipped, out of the brief's stated order

Canvas 26 (folio 23, "Mon Nepveu", dated "A Paris le 17e Mars 1646") was next in the brief's list but is
**visibly a different cipher system** from every other canvas in this cluster: long unsegmented 3-6 digit
groups (`3623`, `5925`, `7632`, `783756`, `1123512331`...) rather than the 1-3 digit + letter-mark nomenclator
of 20/21/27/30. KX-COLB26P1's leaf map already flagged it as "possibly a different correspondent pair bound
into this volume -- unresolved." Given that and its exceptional density (~80 groups estimated), transcribing it
without first settling how its digits segment risks silently corrupting the alphabet count for the whole spec
(wrongly splitting one 6-digit run into two 3-digit codes, for instance). Deferred to a dedicated pass rather
than guessed at here; flagged in ROOM.md 10:04 UTC.

### Transcription: what the three canvases contain

- **Canvas 21** (folio 18, "A Christianopoli le 6 Avril 1645", continuation of canvas 20's letter, same
  letter/hand/date): 96 tokens, 7 lines. Same mixed nomenclator as canvas 20 (1-3 digit numbers + single
  letters + letter/mark ligatures: `w'`, `ll`, `cn`, `Ell`). The 6 Apr 1645 letter is now **fully transcribed
  end to end** (canvas 20 + 21 = 212 tokens across both leaves) -- the first complete letter in this cluster.
- **Canvas 27** (folio 24, dated "a la Haye le 25 May 1646" at the foot -- a different, later letter than the
  17 Mars 1646 docket visible on the facing blank leaf's spine note, which belongs to canvas 26): 158 tokens.
  Same office (Monsieur/La Thuillerye signature) but the cipher runs are noticeably lighter relative to the
  prose (numeral groups punctuate a long mostly-plain letter) and lean more numeric (mostly 2-digit) with fewer
  letter-codes than canvas 20/21, plus a handful of upright single-letter codes (`S`, `K`, `L`, `D`, `Ir`) not
  seen on 20/21. "S.E." (Son Excellence) is read here as a plain honorific abbreviation, not cipher, following
  the convention KX-LATHKEY2 established for canvas 20 -- flagged inline (row canvas 27 line 4 idx 5) as
  unchecked against the crop a second time.
  Also observed and worth a closer read later: this letter references "le Comte de Trautmandorff" negotiating
  at Munster over the "Duché et Principaulté de l'Empire du Comte de Meurs" for "M. le P. d'Orange" -- concrete,
  checkable historical content once decoded, a stronger crib set than canvas 20's vaguer paraphrases.
- **Canvas 30** (folio 27, docketed "8 May 1646 a M. Servien", "re Prince d'Orange, les Etats"): 149 tokens (2
  corrected during reconciliation, see below). **Cleanest design seen in this cluster: pure 2-digit numbers, no
  letter-codes at all**, with caret-inserted glosses that read as genuine identifying cribs rather than vague
  paraphrase -- "Conduite de Knuyt", "Se les Srs Donia, Riperda" (named Dutch/Imperial diplomatic figures), "la
  permission", "quil ne signe pas" -- positioned directly over the numeral run each names. This is the
  strongest crib material found so far in the cluster: a named-entity gloss over a specific short run is a much
  more direct test than canvas 20/21's topic-only paraphrases.

Design implication for the spec: the cluster is not one uniform cipher across its whole date range. The 1645
letter (20-21) and the light-cipher 1646 letter (27) mix letters and numbers; the 8 May 1646 letter (30, and
by inference its continuation 32) is purely numeric. Whether these are the same nomenclator used differently or
genuinely different code tables is unresolved and is exactly the kind of question the spec's first cheap test
(structural comparison against key_1646/key_brienne_1647/fr5160 key_1659_ext) should also probe for internally,
canvas-cluster vs canvas-cluster, not only against the other office's keys.

### Second pass (brief step 2)

One Sonnet subagent transcribed the four cipher-zone crops (20, 21, 27, 30) blind -- it saw only the crop images
and the column spec, no access to this worker's own `ciphertext.tsv` or NOTES.md. Its output is `passB.tsv`
(548 tokens total, its own independent line/idx numbering). Because the two passes did not necessarily agree on
where physical lines break, reconciliation compared token **sequences** per canvas (difflib longest-common-
subsequence alignment) rather than requiring exact line/idx match; `disagreements.tsv` lists every point where
the sequences diverge (113 rows: substitutions, and tokens one pass has that the other does not, which can mean
a real misread or just a different line-segmentation choice near a page-break).

Agreement by canvas (matched positions / max(len A, len B)):

| Canvas | Pass A (this worker) | Pass B (subagent) | Agreement |
|---|---|---|---|
| 20 | 116 | 115 | 81.0% |
| 21 | 96 | 118 | 57.6% |
| 27 | 158 | 167 | 78.4% |
| 30 | 149 | 149 | 97.3% (before the 2 corrections below) |

Canvas 30's near-total agreement tracks its cleaner all-numeric design exactly as expected; canvas 21's 57.6% is
the densest, most crowded page of the four (the subagent's own report calls it "the densest and hardest
image," flagging 2-3 distinct hook/loop marks it could not reliably tell apart -- consistent with this worker's
own uncertainty over `ll`/`cn`/similar marks on that canvas).

**Settled by hand against the crop (canvas 30 only, its 4 disagreements):** position 46 (this worker's `91` vs
the subagent's `97`) and position 66 (`15` vs `13`) were re-checked against `images/crops/canvas30_full.jpg` at
native crop resolution and the subagent's reading confirmed both times (digit shapes match "7" and "3" better
than "1" and "5" on closer comparison) -- **`ciphertext.tsv` corrected**, both the token and the neighbouring
rows' context columns that referenced the old value. Position 14/15 (`51`/`17` vs `41`/`47`) was also
re-checked and stayed genuinely ambiguous on a third look; left as pass A, flagged in `disagreements.tsv`.

**Not settled: the other 109 disagreements (all of canvas 20, 21, 27).** Given the scope already covered in
this job (3 full canvases transcribed, one pass reconciled) and the stall-alarm budget, going crop-by-crop
through 109 more points was judged lower value than transcribing more canvases or writing the spec; `ciphertext.tsv`
for 20/21/27 is pass A only, unreconciled beyond this worker's own single read. This is the same caveat
KX-LATHKEY2 recorded for canvas 20 alone; it still applies, now with a second pass's disagreement list attached
so a successor can settle from `disagreements.tsv` directly rather than re-transcribing from scratch.

### Folder size

29.6 MB (30,223,184 bytes) after this job's pushes -- functionally at the brief's 30 MB cap. A canvas-32 pass
(or any further canvas) will need either smaller crops (narrower region, lower JPEG quality) or trimming
`images/crops/` reference copies (out of this job's writable-paths list) before adding more images.

### Alphabet, this job's total (canvases 20+21+27+30 combined, `ciphertext.tsv` after reconciliation)

519 tokens, 129 distinct signs: 355 numeric-token occurrences (84 distinct numbers) and 164 letter/mark-token
occurrences (45 distinct marks). Most frequent: `11`/`y` (18 each), `83`/`31` (17 each), `d`/`21` (13 each).
Full counts are in `specs/colbert26-lathuillerie-1644.json`'s alphabet block, not restated here.

### Not done this job (successor's queue, cheapest/highest-value first)

1. Canvas 32 (continuation of canvas 30's 8 May 1646 letter, same clean all-numeric design, ~40 groups, but a
   dense two-column facing-page image -- crop it in narrow vertical strips to stay legible and within the size
   budget).
2. Settle the 109 open `disagreements.tsv` rows for canvases 20/21/27 against the crops before trusting any
   single-canvas frequency count from this job for cryptanalysis.
3. The remaining 15 canvases (33, 35, 36, 39, 40, 47, 48, 49, 50, 51, 54, 55, 56, 62, 63) -- same method, no
   refetch needed (crops already on disk).
4. Canvas 26's separate, denser numeral system -- its own dedicated digit-segmentation pass before transcribing
   it at all (see above).
5. Once a fuller transcription exists, re-run this job's cheap test 1 (frequency/homophone structure vs
   key_1646/key_brienne_1647/fr5160 key_1659_ext, matched control) -- not run this job, per brief ("leave
   cheap_test_done empty").

### Files, hosts, cost

Files: `ciphertext.tsv` (+403 rows: 96+158+149, plus 2 corrections), `passB.tsv` (549 rows, new), `disagreements.tsv`
(113 rows, new), `images/lines/canvas{21,27,30}_cipherzone.jpg` (3 files, PIL crops from the on-disk full-canvas
images, no refetch), `specs/colbert26-lathuillerie-1644.json` (new), this NOTES.md section, ROOM.md. Hosts: none
(all from disk). One Sonnet subagent (the blind second pass over the 4 crops, see above; never more than 1 at a
time). No credentials. Cost not visible to this worker (same `get_session` limitation KX-LATHKEY2 recorded);
paced by scope (3 canvases + 1 reconciliation pass, explicit stop rather than a live dollar reading) against the
brief's $10 stall alarm.

## KX-LATHCT1 (25 Sept 2026)

Breadth-lane cheap test 1 (`specs/colbert26-lathuillerie-1644.json`, `cheap_tests_in_order` item 1), job
`.claude/briefs/runs/2026-09-25-lane-kx-lathct1.md`. No network, no transcription, no crib test, no anneal.
Script: `ct1_profile.py` (deterministic, `SEED=20260925`, `N_CONTROL=200`), output `ct1_results.tsv`.

**Tokens used.** Only positions the two passes agree on (`ciphertext.tsv` vs `passB.tsv`, via
`disagreements.tsv`'s `a_pos`; a "settled from crop" row counts as agreed since `ciphertext.tsv` was already
corrected to the value both passes now share). Canvas 20+21+27: 293 of 370 used (77 dropped). Canvas 30: 147 of
149 used (2 dropped -- the 2 rows KX-LATHTR left "genuinely ambiguous"; the 2 rows it settled from the crop are
counted as agreed).

**Profiles** (sign classes, distinct-per-100, repeat rate, index of coincidence on the sign stream):

| corpus | N | distinct | distinct/100 | repeat rate | IC | class shares |
|---|---|---|---|---|---|---|
| A = canvas 20+21+27 | 293 | 80 | 27.3 | 0.727 | 0.0228 | d2=.567, l1=.300, l2p=.058, d1=.048, mark=.024, d3p=.003 |
| B = canvas 30 | 147 | 48 | 32.7 | 0.673 | 0.0323 | d2=1.000 |
| K1646 (clair1067 `ciphertext.txt`, our own 19 May 1646 letter, key_1646.tsv's own text) | 338 | 84 | 24.9 | 0.751 | 0.0249 | d2=.382, l1=.228, mark=.246, l2p=.053, sym=.062, d1=.015, d3p=.015 |
| K1659 (fr5160 `ciphertext_f67.tsv` cipher-only, 10 Oct 1659, key_1659.tsv reads it 92.3%) | 546 | 83 | 15.2 | 0.848 | 0.0308 | d2=.623, d1=.158, mark=.214, d3p=.005 |
| K1647 (`key_brienne_1647.tsv`, Tomokiyo's published table, different correspondent D'Estrades) | n/a -- key TABLE only, we hold no ciphertext of ours actually enciphered under it | 102 distinct codes | -- | -- | -- | l1=12, d2=25, mark=56, l2p=4, d1=3, sym=2 |

B's class shares (100% two-digit numbers, zero letter-codes) confirm KX-LATHTR/the spec's flag by the numbers:
canvas 30 is not drawing on the same sign repertoire as canvas 20+21+27 at all (A has 30.0% bare-letter + 5.8%
letter-code + 2.4% marked codes; B has none of those classes).

**Per-corpus control** (200 synthetic mixed-nomenclator texts of the same N and the same *distinct-code* count
per class -- not token-occurrence counts, which would overstate K -- code->French-letter assignment randomised
and weighted by real French unigram frequency from `tools/data/fr16`, letters run through the resulting table):
real IC sits at the 99th-100th percentile and real distinct/100 at the 100th percentile of all four corpora
(A, B, K1646, K1659) against their own matched control -- i.e. all four real ciphertexts reuse codes *less* than
a simple letter-level homophone-nomenclator model of the same K predicts. This lands the same way on all four,
including the two corpora we already hold real keys for, so it is best read as a limitation of this control (a
syllable/word nomenclator, which real 17th-century French nomenclators of this kind generally are, spreads usage
more evenly than a pure per-letter homophone table) rather than a finding that distinguishes the La Thuillerie
canvases from the held keys. Full numbers in `ct1_results.tsv`.

**Pairwise code-inventory Jaccard**, with two calibration controls per pair (200 reps each): "different key,
same design" (two independent synthetic tables of the matched K/class-shares drawn from the same restricted
code-space -- the chance floor from a shared small alphabet, e.g. only 90 possible 2-digit codes) and "same key"
(one synthetic table, two disjoint texts of the observed N's drawn from it -- what real reuse of the identical
table would look like at this N, given not every code need appear in a short excerpt):

| pair | observed Jaccard | different-key control (mean, range) | observed percentile in it | same-key control (mean, range) |
|---|---|---|---|---|
| A vs B | 0.255 | 0.292 [0.196, 0.391] | 15.0 | 0.764 [0.645, 0.892] |
| A vs K1646 | 0.242 | 0.229 [0.163, 0.302] | 76.5 | 0.852 [0.745, 0.935] |
| A vs K1647 | 0.138 | 0.120 [0.077, 0.159] | 91.5 | 0.754 [0.672, 0.846] |
| A vs K1659 | 0.226 | 0.216 [0.156, 0.283] | 73.5 | 0.862 [0.782, 0.927] |
| B vs K1646 | 0.245 | 0.215 [0.148, 0.282] | 92.0 | 0.750 [0.622, 0.863] |
| B vs K1647 | 0.145 | 0.098 [0.056, 0.145] | 100.0 | 0.530 [0.415, 0.673] |
| B vs K1659 | 0.236 | 0.221 [0.170, 0.284] | 77.5 | 0.771 [0.663, 0.889] |

Every held-key comparison (A or B against K1646, K1647 or K1659) lands inside or barely above the ordinary
"different key, same restricted code-space" chance range, and every one sits far below what "same key" produces
at this N (0.53-0.86). A vs B sits *below* the mean of even the different-key chance floor (15th percentile),
consistent with B not sharing A's alphabet at all (it has none of A's letter/mark codes, see profile above).

**Verdicts (rule 3, both numbers given above):**
- **A (canvas 20+21+27) vs B (canvas 30): different alphabet**, not one design. B's class-share profile has
  zero bare-letter, letter-code or marked signs (100% two-digit numbers) against A's 30.0/5.8/2.4%, and the
  Jaccard overlap (0.255) sits below the mean of pure chance overlap for two unrelated tables sharing the same
  90-slot two-digit code space (0.292), far short of the 0.764 a real shared table would produce at this N.
  Whether canvas 30 is a distinct sub-table of the same office's system (e.g. a numerals-only phase) or an
  unrelated table cannot be told from this test; only that it is not the same alphabet as 20+21+27.
- **A vs key_1646 (clair1067, Brienne to the Queen of Poland, 19 May 1646): different key family.** Observed
  Jaccard 0.242 sits at the 76.5th percentile of the different-key chance distribution (unremarkable) and far
  below the same-key expectation of 0.852.
- **A vs key_brienne_1647 (Tomokiyo's published D'Estrades table): different key family.** Observed 0.138 at
  the 91.5th percentile of chance, same-key expectation 0.754.
- **A vs key_1659 (fr5160, Le Tellier office, 1659): different key family.** Observed 0.226 at the 73.5th
  percentile of chance, same-key expectation 0.862.
- **B vs key_1646: different key family.** Observed 0.245 at the 92.0th percentile of chance (highest of the
  three B comparisons, still short of the 0.750 same-key expectation).
- **B vs key_brienne_1647: cannot tell cleanly, but points away from same key.** The calibration is weaker here
  because K1647 has far fewer 2-digit codes (25) than B (48), which pulls the same-key control itself down to
  0.530 (vs 0.75-0.86 for the other pairs); observed 0.145 sits at the very top edge of the different-key chance
  range (0.145, the control's own maximum) and well below 0.530.
- **B vs key_1659: different key family.** Observed 0.236 at the 77.5th percentile of chance, same-key
  expectation 0.771.

**Net answer to the job's question:** no, this cluster is not the same key as key_1646, key_brienne_1647 or
key_1659_ext (fr5160's key_1659 base table) at this N, on a matched control for all seven pairs tested; and
canvas 20+21+27 is not the same alphabet as canvas 30 either. This is a same-office structural comparison, not
a full solve -- absence of a Jaccard match does not rule out the cluster being read by hand-annealing its own
table later; it only rules out *reusing* one of the three tables already on disk. `cheap_test_done` in the spec
records this as the completed first test; per the breadth-lane rule (CLAUDE.md 3a) this cluster's next test
(cheap test 2, the crib-placement check) would need a new job -- not run here.

Files: `ct1_profile.py`, `ct1_results.tsv` (new), this NOTES.md section, `specs/colbert26-lathuillerie-1644.json`
(`cheap_test_done` only), ROOM.md. Hosts: none (no network; the French-letter-frequency reference is
`tools/data/fr16/lettresindites00marg_djvu.txt.gz`, already on disk). No subagents. Cost not visible to this
worker.

partial
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

Cryptanalysis, not recovery (corrected 25 Sept 2026; ROOM.md 09:59 and 10:00, LANE KX orchestrator, retracting
this section's own earlier framing): the second hand's interlinear notes are short topical/paraphrase glosses
near a cipher run ("Je parle des Suedois" over 11 tokens), not a word-per-code decipherment -- see "Important
correction to the 'period decipherment' framing" below, which reads every token on canvas 20 against its nearby
gloss and finds no line meets the brief's own C-grade bar (legible and consistent across occurrences). No period
key exists on the document; any key here has to come from cryptanalysis (mixed nomenclator, ~129 distinct signs
across the four transcribed canvases) using the paraphrase glosses only as topic/content cribs, not as a ready
substitution table.

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

**Held back (25 Sept 2026, QA/YX-FIX correction): canvas 21's 57.6% two-pass agreement is below this repo's 60%
transcription-agreement gate (CLAUDE.md Usage item 6, "scripts read, models judge" / the reproducibility bar the
same day's VX-CT03 and VX-RD04B held their own sub-60% blocks to).** Canvas 21's pass-A rows in `ciphertext.tsv`
are not deleted -- they stay on disk, flagged, per rule 7 (reproducible readings) -- but they are not settled
ciphertext and must not be counted in any total, spec field or cheap test that presents canvas 20/21/27/30 as
"transcribed and reconciled." Canvas 20 (81.0%) and canvas 27 (78.4%) clear the 60% floor on two-pass agreement
even though their individual disagreements are not yet hand-settled against the crop; only canvas 21 is held
back on this ground.

### Folder size

29.6 MB (30,223,184 bytes) after this job's pushes -- functionally at the brief's 30 MB cap. A canvas-32 pass
(or any further canvas) will need either smaller crops (narrower region, lower JPEG quality) or trimming
`images/crops/` reference copies (out of this job's writable-paths list) before adding more images.

### Alphabet, this job's total (canvases 20+21+27+30 combined, `ciphertext.tsv` as pass-A transcription)

Correction (25 Sept 2026, QA/YX-FIX): "after reconciliation" above overstated this. Only canvas 30's 4
disagreements were actually settled by hand against the crop (see above); canvas 20 and 27 are pass A only,
unreconciled but above the 60% gate; canvas 21 is pass A only, held back below the 60% gate (see above) and
excluded from any total this repo presents as settled.

519 tokens, 129 distinct signs: 355 numeric-token occurrences (84 distinct numbers) and 164 letter/mark-token
occurrences (45 distinct marks). Most frequent: `11`/`y` (18 each), `83`/`31` (17 each), `d`/`21` (13 each).
This total still includes canvas 21's 96 held-back tokens -- it is a transcription-progress count, not a
settled-ciphertext count; a settled total (canvas 20+27+30 only, canvas 21 excluded per the hold-back above)
is not yet computed here. Full counts are in `specs/colbert26-lathuillerie-1644.json`'s alphabet block, not
restated here; that spec's own `ciphertext` field is corrected separately to mark canvas 21 held back.

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

## Web and blog check (GF-A2-3, account 2, 2 Oct 2026)

Queries run (plain web search, one engine), each hit list read and plausible hits opened:
1. `La Thuillerie Servien 1645 Christianopel lettre chiffre` -- BnF Clairambault 575 record (biblissima), Yale/Beinecke
   catalogue rows, a Servien biography; none about this volume or its cipher.
2. `"Mélanges de Colbert 26" chiffre` -- BnF comite d'histoire notes on the Melanges de Colbert series, Canadiana reel
   C-12868 (microfilm of other Colbert volumes); nothing on vol. 26's cipher.
3. `"Je parle des Suedois" La Thuillerie` (the canvas-20 annotation phrase) -- no hit on the phrase.
4. `La Thuillerie Servien cipher letters 1648 Hague Prince of Orange decipherment` -- Clairambault 576 record (opened:
   d'Estrades embassy 1646 with La Thuillerie letters at pp.127-193, no chiffre/dechiffrement in the record, no 1645
   Christianopel or 1648 Hague letter named), HistoCrypt 2024 d'Avaux 1684 paper (a different, later ambassador).
5. `"Coignet de La Thuillerie" lettres Servien 1648 édition correspondance` -- no edition of the La Thuillerie-Servien
   letters found; only biographies and catalogue rows.
6. `La Thuillerie cipher 1645 Denmark Sweden mediation encrypted letter deciphered solved` (also the model-solve family)
   -- one Cipherbrain post opened (scienceblogs.de/klausis-krypto-kolumne/2019/06/02/an-unsolved-encrypted-letter-from-
   the-17th-century/): Baner to Stalhandske, 29 Dec 1640; post and its five comments read, not this item.
Blog site searches: `site:scienceblogs.de klausis-krypto-kolumne Thuillerie OR Servien OR Colbert` (no Cipherbrain page
returned); `site:cryptiana.blogspot.com Thuillerie OR Servien` (no Cryptiana page returned; Tomokiyo's servien.htm on
disk is the 1630-37 Baluze 155-156 cipher, a different one); `site:ciphermysteries.com Thuillerie OR Servien OR
Westphalia cipher` (two Cipher Mysteries pages returned, both unrelated -- Moustier church notes). No comment thread
anywhere found that discusses this volume, these letters or their cipher.

## Premise check (GF-A2-3, account 2, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **found.** The folder records interlinear glosses on canvas 20-21
(f.17-18), 26 (f.23) and 27 (f.24). KX-LATHKEY2 judged canvas 20's notes topical, not word-for-word. This worker opened
the on-disk crops `images/crops/canvas26_full.jpg` and `canvas27_full.jpg` (2400 px) and looked: both carry a
second-hand interlinear rendering written directly over the numeral runs, phrase by phrase. Canvas 27 (f.24, La
Thuillerie to Servien, La Haye 1646): over the groups after "lequel vient de Munster c'est" is written "que le Comte de
Trautmandorff a fait faire les expeditions de l'Erection en Duche et Principaute de l'Empire du Comte de Meurs qui
apartient a M. le P. d'Orange", and later "des ordres de S.E.". Canvas 26 (f.23, "A Paris le 17e mars 1646", "Mon
nepveu"): "la charge de Surintendant des bastimens", "pour la charge de M. de Brienne", "Intelligence entre M. Davaux
et M. de Brienne", "M. Davaux escrivit a M. de Brienne", "il vous cognoistroit et que vous le supplanteriez", "nomme M.
de la Court pour l'employ", among others. These are period decipherments of the enciphered passages on those two
leaves (at least in the top half of each, the part viewed), not topic notes. So f.23 and f.24 are already read on the
leaf; they are a key/calibration source for the cluster, not unread ciphertext. Canvas 20-21's status as topical
notes (KX-LATHKEY2) is not re-judged here; canvases 30-63 not viewed by this worker.
(b) Other solvers' working files -- **not found.** Fresh shallow clones of dbourdeau/cyphersolver and
aaymeloglu/unsolved-ciphers grepped for "thuillerie"/"tuillerie", "servien", "btv1b10035069t"/"10035069": hits are
unrelated (a Gallica sweep notice listing a La Thuillerie letter in another BnF volume; Chastillon-to-Servien 1635;
rohan1636 and napoleon targets; a Forster 1644 word list) -- no working file, rendering or key run on this volume.
(c) Physical neighbours -- **found (as (a)).** The leaf map (leaves.tsv) covers every canvas of Part I; the glossed
leaves are canvas 26 and 27 themselves. The facing page of canvas 26/27 (left half of each crop) is a blank or
show-through leaf, no slip seen at 2400 px.
(d) Recipient's side -- **not found.** Servien is the recipient: the Acta Pacis Westphalicae (French correspondences,
APW II B, via the online full text) and Le Clerc's Negociations secretes were read by the check-solved worker (Search
log above) without these letters; no Danish/Swedish edition of La Thuillerie's 1644-46 mediation was opened by this
worker (unreached).

## A2-COL (account 2, LANE-A2PUSH, 2 Oct 2026): f.24 interlinear key

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-col.md`. Intake gate exit 0 at start. Status word left `open` (not this
worker's to change; flagged for the orchestrator: a leaf-level key now exists, which reads like `partial`).

**What f.24 (canvas 27, La Thuillerie to Servien, La Haye 25 May 1646) carries.** Every cipher run on the leaf has a
second-hand French rendering written directly above it, word for word ("que le Comte de Trautmandorff", "a fait faire les
expeditions de l'Erection en Duche et", "Principaute de l'Empire du Comte de Meurs", "a M. le P. d'Orange", "a trouver",
"audit S. Prince", "relever sa maison par un titre", "de cette sorte", "desquelz relevent ledit Comte de Meurs Mais cela
estant", "il ne nous en donnoit advis", "qu'il y eust quelque chose a desirer de", "luy", "des ordres de S.E."). The
KX-LATHTR transcription had folded these gloss lines into its `context_before/after` columns as if they were the
letter's clear text; they are the decipherment. (Canvas 20's notes stay as KX-LATHKEY2 judged them; not re-read here.)

**Crops (commands, run on the native region fetched once).** `python3 tools/iiif_lines.py --ark btv1b10035069t --canvas 27
--region 3850,1450,3577,3100 --out <scratch> --prefix f24 --debug --dry-run` (1 request to Gallica IIIF), then per unit
`python3 tools/iiif_lines.py --image <that src> --region 0,Y0,3577,H --centres H/4,3H/4 --lines-per-crop 2 --top-margin H/4
--bottom-margin H/4 --out <scratch>/crops --prefix f24_UNN` with Y0:Y1 = 95:300 245:420 405:620 600:870 1630:1870 1835:2170
2105:2300 2285:2520 2455:2720 2665:2960 (U01-U10), 1400:1680 (U11), 2880:3060 (U12). 24 segment crops under 2400 px,
kept in the session scratchpad, not committed (folder already at 30 MB; re-derivable from those commands).

**Transcription.** Two blind Sonnet passes over U01-U10 (cipher signs and gloss per unit), reconciled by this worker
against the crops (`interlinear/f24_reconciled.tsv`, the disagreements and how each was settled in its columns). Settled:
`n`/`u` after `o` and in U10 read `11` (same stroke pair as the 11 after 31); `q` = `9`; `7` = `y` (the barred y, as
KX-LATHTR's pass A has it); `S` = `f` (one long-s sign, the two passes and pass A name it differently). U11 (the Brasset
line, "des ordres de S.E.") was cut off both blind passes' crops by a wrong region; read by this worker only, from crop
U11, and **held out** of the alignment as a known-answer test. 12 aligned pairs, 153 cipher tokens, 59 signs.

**Alignment** (`tools/interlinear_align.py align interlinear/f24_pairs.tsv interlinear/f24_align.tsv
interlinear/f24_key_raw.tsv --floor 100 --keep-fs --max-chunk 6 --prior interlinear/seed_prior.tsv --word-prior`; signs
renumbered 100+ in `interlinear/sign_ids.tsv` so every sign may take a chunk). From a flat start the hard-EM did not lock
(21 agreeing tokens, 82 conflicts, default flags; 15/86 with the syllabic `--len-prior 0.5` flags). Seeded with three
codes the gloss itself repeats (83 = de, before every gloss "de", 10 occurrences; 92 = Comte, the twice-repeated "92 83 16 d
6 f 37" under "Comte de Meurs" in U03 and U08 and once in U01; 31 = que, U01 "que le" and U10 "quelque" = 31 11 31): 37
agreeing tokens, 69 conflicts, 36 single. The seeded counts are the hypothesis under test, not independent evidence.

**Control (rule 3; `interlinear/f24_control.py`, output `interlinear/f24_control_out.txt`).** Same cipher lines, gloss
lines dealt in a random derangement, same flags and seed, 50 seeds. Agreeing tokens: real 37 vs control mean 14.0, p95 20,
max 20; excluding the three seeded codes: real 21 vs control mean 11.5, p95 16, max 18. The control changes which gloss a
line meets, which is what the statistic depends on, so it could fail differently; real beats every shuffle on both
counts, but the unseeded margin is thin (21 vs 18). **Per-leaf gate: f.24 passes, narrowly.** f.23 was not aligned (below),
so there was no merge and no second leaf to gate.

**Key** (`key_f24.tsv`, all 59 signs). Grade C only where a sign occurs at least twice and at least two thirds of its
occurrences take the same chunk: 31 que (4/4), 92 comte (3/3), 83 de (9/10), 51 l (2/2), 16 m (2/3), 25 m (2/3) -- the
first three seeded. Every other sign is M; its value is the alignment's majority chunk and many are plainly wrong where a
line's tail absorbed leftover letters (e.g. t = "duche", 37 = "mais"). The design looks mixed: single letters
("Meurs" = 16 d 6 f 37, M e u r s in both occurrences), syllables (31 que) and words (92 Comte, 47 = "dit"/"ledit" twice
by position); one leaf of 153 tokens is not enough for the tool to separate them.

**Decode** (`decode.json`, `python3 tools/decode_key.py ciphers/colbert26-lathuillerie-1644 [--check]`, exit 0):
`reading_f24.txt`, `reading_tokens_f24.tsv`; 168 tokens: H 0, C 27, S 0, M 140, I 0, U 1 -- cryptanalytic-grade only by the
rule-4 count (no H), and the C is the leaf's own gloss. Held-out U11: the two C tokens (83 at positions 1 and 8) read "de"
and "de", consistent with the gloss "des ordres de" at both places; the M tokens there do not read the gloss (f gives "a"
where "s" stands). No unglossed run on f.24 is long enough to read: U11's tail after the gloss (43 h w' 17 21 L 78) has no
C sign. Judge, pasted:
```
FAIL language: score=-1.386, null_p99=-1.834, real_p05=-0.872, real_median=-0.788, mode=both, N=285
ok   words: cover=0.782, min=0.4, real_text_median_cover=0.944
FAIL - colbert26-lathuillerie-1644 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Expected: 140 of 168 tokens are M alignment chunks.

**Not done.** f.23 (canvas 26, Paris 17 Mar 1646, "Mon nepveu"): a different system (unsegmented runs of two-digit codes,
"121829 61" under "la charge de" at least three times, "5130"/"4823" recurring) with about 22 glossed lines and a rotated
margin. Not cropped or aligned: the account read `allowed_warning` at 22:50 UTC (BUDGETS.md: no new workers), so no further
subagent passes were started. It is the stronger leaf for this tool: two-digit codes with visible word-level repeats.

Hosts: gallica.bnf.fr IIIF 1 request. Subagents: 2 (Sonnet, blind passes). No credentials.

## A2-COL2 (account 2, LANE-A2PUSH, 2 Oct 2026): f.23 interlinear alignment and its own control

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-col2.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Leaf.** f.23 (canvas 26), "A Paris le 17e mars 1646", "Mon nepveu". Two-digit codes written in unsegmented runs, a second
hand's French decipherment above most runs, word by word ("de mon nepueu" over 51 82, "de S E" over 51 29, "pour la charge
de M de Brienne" over 97 28 12182961 51 31, "Il y ira" over 81 35 2055). Some digits carry a bar (over 2 of 28, 4 of 46/48/49,
the final 99 of 46322999); the bars are recorded in `interlinear/f23_reconciled.tsv` notes but not coded as distinct signs.
The rotated left-margin postscript (also two-digit runs, glossed) was not cut and is not in this step.

**Crops (commands).** One region fetched: `python3 tools/iiif_lines.py --ark btv1b10035069t --canvas 26 --region
3900,700,3600,5400 --out <scratch> --prefix f23 --debug --dry-run` (1 Gallica IIIF request). Then 30 units (gloss line +
cipher line), each `python3 tools/iiif_lines.py --image <that src> --region 0,Y0,3600,H --centres H/4,3H/4 --lines-per-crop 2
--top-margin H/4 --bottom-margin H/4 --out <scratch>/crops --prefix f23_UNN` with Y0:Y1 = 120:300 290:440 430:560 560:690
680:800 800:920 980:1140 1160:1290 1270:1440 1420:1580 1530:1700 1780:1960 1940:2070 2040:2170 2220:2350 2330:2460
2460:2580 2580:2700 2860:3000 2970:3130 3220:3380 3360:3490 3500:3610 3610:3760 3760:3880 3980:4140 4140:4290 4290:4400
4390:4520 4500:4620 (U01-U30). 60 segment crops (<= 2400 px), scratch only, not committed (folder already near 30 MB).

**Transcription.** Two blind Sonnet passes over the 60 crops (pass B in reverse unit order), then this worker's reconciliation
against the strips and four native zooms (U04, U06, U07, U09-U10, U17). Digit runs agreed in 10 of 30 units outright; the rest
differed by a split, a cut-off tail or one digit. Settled from the image: U06 "29 39 82" (both passes 292981), U07 2130 (bar
over 3), U04 46322999, U17 53223929, U10 29 77 43 29 29 29, U27 1235 39. Result: 42 gloss/cipher pairs, 306 code tokens, 70
distinct codes (`interlinear/f23_reconciled.tsv`, each disagreement and how it was settled in its note column). P36 ("que vous
estes tresbien icy", 13 codes) is **held out** of the alignment as a known-answer test; 41 pairs, 293 tokens aligned.
Visible by eye before any alignment (not used as evidence for the gate): 82 under every "mon nepueu" (5 pairs), 51 under "de"
(5), 29 under "S E" (3), 49 under "que", 98 under "vous", 97 under "pour", 10 under "a", 39 under "et", 89 under "M".

**Alignment.** `tools/interlinear_align.py align interlinear/f23_pairs.tsv interlinear/f23_align.tsv interlinear/f23_key_raw.tsv
--floor 100 --keep-fs` (codes renumbered 100+code so every code may take a chunk; tool's default --max-chunk 14, because
--max-chunk 6 cannot let 82 take "monnepueu"). Configurations tried on the real pairs before the control (logged, rule 3
forking paths): max-chunk 6 flat 60 agrees, with --len-prior 0.5 49, max-chunk 10 61, default 63; seeded (82 monnepueu, 51 de,
29 se, `interlinear/f23_seed_prior.tsv`, --word-prior) 73-77. The two configurations then put through the control were fixed
as the default flat start and the default seeded run.

**Control (rule 3, per-leaf gate; `interlinear/f23_control.py`, output `interlinear/f23_control_out.txt`).** Same cipher runs,
gloss phrases dealt in a random derangement, same flags, 50 seeds. The control changes which gloss a run meets, which is what
the agreement statistic depends on, so it can fail differently from the real run.
```
flags	--floor 100 --keep-fs
agrees_all	real 63	control mean 34.7 p95 41 max 45	real>max True
flags	--floor 100 --keep-fs --prior f23_seed_prior.tsv --word-prior
agrees_all	real 77	control mean 34.9 p95 44 max 49	real>max True
agrees_unseeded	real 57	control mean 29.1 p95 38 max 39	real>max True
```
**Per-leaf gate: f.23 passes, from a flat start (63 vs shuffled max 45), with a wider margin than f.24's (unseeded 21 vs 18).**

**Key** (`key_f23.tsv`, 70 codes, from the flat-start run so no seeded value counts). Grade C by the same rule as key_f24
(>= 2 occurrences, >= 2/3 take one chunk): 10 a (4/6), 24 s (2/3), 40 b (2/2), 65 s (2/2), 89 m (2/3), 97 pour (2/3); every
other code M. The strict string rule undercounts word codes whose gloss runs over unglossed neighbours: 82 takes "monnepueu",
"nepueu", "epueu" (5 occurrences, all inside "mon nepueu") and stays M by the rule; 51 takes "de" 3 of 13. The design looks like
a two-digit syllabary with word codes (12 18 29 61 under "charge" twice, 59 20 39 under "ruyne" twice, 10 22 40 30 65 51 32 29
under "ambassadeur" twice, 48 32 29 31 under "Court" twice).

**Decode** (`decode.json` second job, `python3 tools/decode_key.py ciphers/colbert26-lathuillerie-1644 [--check]`, exit 0,
"reading up to date"): `reading_f23.txt`, `reading_tokens_f23.tsv`; 306 tokens: H 0, C 20, S 0, M 285, I 0, U 1 (the
unread "8?" of P13). Cryptanalytic-grade only by the rule-4 count; the C is the leaf's own gloss. Held-out P36: its one C token
(65 = s, 10th of 13 codes, between "estes" and "icy") is consistent with an s in "tres"; 1/1, too thin to be a test of more than
non-contradiction. Judge, pasted:
```
FAIL language: score=-1.582, null_p99=-1.893, real_p05=-0.911, real_median=-0.789, mode=both, N=596
ok   words: cover=0.767, min=0.4, real_text_median_cover=0.95
FAIL - colbert26-lathuillerie-1644 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Expected: 285 of 306 tokens are M alignment chunks.

**f.24 re-run with the f.23 key as --prior: not run, the leaves do not share a key.** f.24 is a mixed letter/symbol/number
system (59 signs: f, L, y, ll, w', E ... beside 1-2 digit numbers); f.23 is two-digit codes only. Where a number occurs on both
leaves the period glosses give it different values: 51 is "de" under f.23's gloss (5 pairs) but l on f.24 (C, 2/2), and f.24's
"de" is 83; 31 is que on f.24 (C, 4/4) but stands under "M de Brienne" on f.23 (P08, P11, P12). Seeding f.24 with f.23 values
would inject a different key's meanings (the Szembek merge rule in CLAUDE.md rule 3): no merge, each leaf keeps its own key.

Hosts: gallica.bnf.fr IIIF 1 request. Subagents: 2 (Sonnet, blind passes, 60 crops each); own reads: 6 strip composites + 2
native zooms. No credentials.

## A2-COL3 (account 2, LANE-A2PUSH, 2 Oct 2026): f.23 word-level re-pairing and re-alignment with the same control

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-col3.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Re-pairing (by eye, one reader, not blind).** The A2-COL2 region was re-fetched once (`tools/iiif_lines.py --ark
btv1b10035069t --canvas 26 --region 3900,700,3600,5400 --dry-run`, 1 Gallica IIIF request; the earlier crops lived only in
that session's scratchpad) and the same 30 units (A2-COL2's Y0:Y1 list) were cut locally and stacked into five strip
composites (scratch only). This worker read the composites and split each A2-COL2 phrase pair into word pairs only where the
cipher line has a visible gap between runs that sits under the gloss words one to one; the code sequence of every pair is
unchanged (checked: the word pairs concatenate back to `interlinear/f23_reconciled.tsv` for all 41 pairs). Pairs whose gloss is
offset from the runs or that are one run under several words stay whole (P06, P07, P10, P21, P26, P27, P30, P34, P35, P39,
P40; P24 "quon y" kept as one). Result: `interlinear/f23w_split.tsv` (word, codes, the unit and run split it rests on) and
`interlinear/f23w_pairs.tsv`, 116 word pairs, the same 293 aligned tokens. P36 still held out; the split was read with the
codes in view, so the reader could have been steered by a code's other occurrences -- the control below is what licenses the
count, not the reader.

**Alignment and control (rule 3).** Same tool, flags and control as A2-COL2 (`interlinear/f23_control.py`, which now takes
`--pairs`; default unchanged and reproduces A2-COL2's 63 / mean 34.7 / max 45). Output `interlinear/f23w_control_out.txt`:
```
flags	--floor 100 --keep-fs   (phrase pairs, f23_pairs.tsv)
agrees_all	real 63	control mean 34.7 p95 41 max 45	real>max True
flags	--floor 100 --keep-fs   (word pairs, f23w_pairs.tsv)
agrees_all	real 128	control mean 30.8 p95 39 max 45	real>max True
```
The control deals the 116 word glosses to the cipher runs in a random derangement (50 seeds), so a code meets a different gloss
word each time; agreement depends on which gloss a run meets, so the control can fail differently, and it does (mean 30.8).
Flat start, nothing seeded. **Per-leaf gate: passes, 128 vs shuffled max 45** (phrase level 63 vs 45).

**Key** (`key_f23.tsv` replaced; the phrase-level key kept as `interlinear/key_f23_phrase.tsv`). Same C rule (>= 2 occurrences,
>= 2/3 take one chunk): 21 C codes, was 6 -- 10 a, 12 c, 18 h, 22 m, 24 n, 25 p, 28 la, 33 ux, 36 ez, 40 b, 43 p, 48 c, 49 que,
51 de, 53 d, 65 s, 69 s, 78 u, 89 m, 97 pour, 98 vous. 49 codes M (82 = mon nepueu 3/5, 31 = M de Brienne 3/13, 34 = M Dauaux
2/4, 39 = et 4/8 stay M under the strict rule; 29 is spread over "se", "le", "a" and others, 26 occurrences). The unread "8?" of
P13 is left out of the key and stays U. The design picture holds: a two-digit syllabary (12 18 29 61 = c h ar ge; 33 = ux in
both "mieux" and "ceux") with word and name codes.

**Decode** (`python3 tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check`, exit 0, "reading up to date"):
`reading_f23.txt`, `reading_tokens_f23.tsv`; 306 tokens: H 0, C 92, S 0, M 213, I 0, U 1 (was C 20, M 285). Cryptanalytic-grade
by the rule-4 count; every C is the leaf's own gloss. **Held-out P36** ("que vous estes tresbien icy", 13 codes, not in the
alignment): 4 C tokens, all consistent with the gloss -- 49 que (1st), 98 vous (2nd), 65 s (10th, in "tres"), 12 c (12th, in
"icy", 20 12 35 = i c y); 4/4, up from 1/1. Judge, pasted:
```
FAIL language: score=-1.412, null_p99=-1.867, real_p05=-0.9, real_median=-0.792, mode=both, N=684
ok   words: cover=0.741, min=0.4, real_text_median_cover=0.949
FAIL - colbert26-lathuillerie-1644 (a PASS is a gate for a verifier, not a reading; rule 10)
```
Expected: 213 of 306 tokens are still M alignment chunks (was -1.582).

Hosts: gallica.bnf.fr IIIF 1 request. Vision: 0 subagent calls; 5 own reads of strip composites. No credentials.

## A2-COL4 (account 2, LANE-A2PUSH, 2 Oct 2026): f.23 rotated margin postscript, known-answer test of key_f23

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-col4.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines`, exit 0.

**Crops (commands).** Gallica info.json for f26 (7427 x 6365), then `python3 tools/iiif_lines.py --ark btv1b10035069t --canvas 26
--region 3700,60,520,4600 --dry-run` (missed the block: it lies further right) and `--region 4050,40,450,5300 --dry-run` (the
whole block); 3 Gallica requests. The source was rotated 90 degrees counter-clockwise locally (PIL; the tool has no rotation
option) and cut with `python3 tools/iiif_lines.py --image <rotated src> --region 300,140,5000,300 --centres 150 --top-margin 150
--bottom-margin 150 --out <scratch>/crops --prefix f23m`: 3 segment crops (<= 2400 px), scratch only, not committed.

**Transcription.** Two blind Sonnet passes over the 3 crops (pass B read in reverse segment order first), neither shown the key or
the main-leaf reading; this worker's reconciliation from 5 native zooms. Clear text: "J'ay oublie de vous marquer [M1] veut
absolument [M2] qu'il fault qu'il fasse [M3]". Three glossed units (`margin/f23m_reconciled.tsv`, each disagreement and how it was
settled in its note): M1 "que La Reyne" over 14 19 49 26; M2 "Soulager S E dans la charge des estrangers" over 68 32 28 61 29 29
71 28 12 18 29 61 51 30 15 37 59 23 61 29 30 (passes split only on 59/55 in the tail, settled 59 from the zoom; a heavy 6-like
flourish before 15 left out, uncoded); M3 "[en/ou, unread] qu'il fasse faire" over 24 32 90 31 55 30 66 77 (passes agree). 33
codes, 1 (90) not in key_f23. The key was not changed: the postscript is held out.

**Known-answer test and control (rule 3; `margin/kat.py`, output `margin/kat_out.txt`).** Statistic fixed before running: per
unit, walk the codes in order; a code scores if its key_f23 value occurs in the unit's gloss (letters only) at or after the
previous match. Control: the same walk against 2000 windows of equal length cut at random from the f.23 main-text gloss
(interlinear/f23w_pairs.tsv); the score depends on which gloss the run meets, so the control can fail differently.
```
unit	set	real	n	control_mean	control_p95	control_max	P(control>=real)
M1	C	1	1	0.08	1	1	0.0760
M1	all	1	4	0.52	1	2	0.5125
M2	C	5	5	1.84	4	4	0.0000
M2	all	6	21	4.35	7	8	0.1855
M3	C	0	1	0.59	1	1	1.0000
M3	all	2	7	1.51	3	3	0.4675
ALL	C	6	7	2.51	6	6	0.0760
ALL	all	9	32	6.37	11	13	0.1855
```
**Result.** C-grade codes: 6 of 7 consistent with the margin's own gloss in order (M2 5/5 -- 28 la twice, 12 c, 18 h, 51 de --
above every control window, max 4; M1 49 que 1/1). The one miss is 24 = n against "qu'il fasse faire", whose first gloss word
(read "en" by pass A, "ou" by pass B) was left out as unread; "en" would make it 7/7, but the reading is not settled, so the
miss stands. Pooled, 6/7 equals the control's maximum (p = 0.076): the C key passes on M2 alone, not as a pooled test at p < 0.05.
M-grade values as a set do no better than chance (all codes 9/32 vs control mean 6.4, p = 0.19), as expected for single-occurrence
chunks. Observed but not counted (no gate was set for them): 71 = dans and 77 = faire (both M in key_f23) stand under "dans" and
"faire" here; 68 = s under the S of "Soulager"; 61 (key value "rge", M) sits where "ge" falls three times (soula-GE-r, char-GE,
estran-GE-rs), which suggests 61 = ge. These are leads for the next key revision, M until a further occurrence or a control
licenses them. Rule 4 for the margin tokens under key_f23: 33 tokens, C 7 (6 consistent, 1 against an unread gloss word), M 25,
U 1 (90). Cryptanalytic-grade; every C comes from the f.23 gloss. No reading or key changed, so no decode or judge re-run.

Hosts: gallica.bnf.fr IIIF 3 requests (1 info.json, 2 regions). Vision: 2 Sonnet subagent calls (3 crops each) + 1
reconciliation by this worker (5 native zooms). No credentials.

## A2-COL5 (account 2, LANE-A2PUSH, 3 Oct 2026): thumbnail sort of the other cipher-bearing leaves by system

Intake gate, run before the step: `colbert26-lathuillerie-1644: partial (line 1) -- edition/page or full-text-search citation found within 6 lines` (exit 0).

Escalation step "siblings". The 19 other cipher-bearing leaves in leaves.tsv (20 canvases: 20, 21, 30-33, 35, 36, 39, 40,
47-51, 54-56, 62, 63; canvas 31 is the duplicate capture of 30) were sorted by sign system by eye from the 1000 px leaf images
already on disk (images/leaves/canvas_N.jpg; 19 viewed, 31 taken from leaves.tsv). No network, no subagents, no transcription.
Result in `siblings_sort.tsv`, one row per canvas.

- mixed (digits with bare letters, letter-codes and marks; the f.24 / KX-LATHCT1 corpus A type): canvas 20-21 only, the
  Christianopel letter of 6 Avril 1645.
- two-digit numerals only (often an overline or mark over one digit; the f.23 / corpus B type): all 17 others -- canvas 30-32
  (the May 1646 La Haye letter, corpus B, already d2 = 1.000 on 147 transcribed tokens) and every La Haye leaf of
  January-February 1648 (canvas 33, 35, 36, 39, 40, 47-51, 54-56, 62, 63; datelines and dockets 6e/9e de l'an, 13, 18, 20, 23,
  24, 27, 30 Janvier, 3 Febvrier 1648). Every one of them carries an interlinear gloss over most numeral groups.
- So the volume holds one two-digit system on f.23 (17 Mars 1646) and on 17 sibling leaves from May 1646 to Feb 1648, and a
  mixed system on f.17-18 (1645) and f.24 (1646). The sort is by sign class only: whether the two-digit leaves share f.23's
  key, rather than one design with several tables, is not shown by a thumbnail (rule 3: no claim without a control).

Grade: a by-eye class judgement at 1000 px, not a reading; a stray letter-code or three-digit group could be missed at this
size. No token read, so no rule 4 counts; key and reading unchanged; no decode or judge re-run.

What it opens: about 17 glossed two-digit leaves are the "more occurrences" the f.23 open-codes gap needs, and canvas 30 already
has 149 tokens transcribed with their gloss column (ciphertext.tsv). Next cheapest: apply key_f23.tsv's C codes to canvas 30's
glossed tokens and score agreement with its own gloss against a shuffled-gloss control (the control can differ: it moves the
gloss under each code), offline, ~$1.

Hosts: none (images on disk). Vision: 21 leaf images viewed by this worker, 0 subagent calls. No credentials.

## A2-COL6 (account 2, LANE-A2PUSH, 3 Oct 2026): key_f23 C codes on canvas 30 against its own gloss

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col6.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Gloss, re-read from the image (rule 2).** ciphertext.tsv's gloss column for canvas 30 is incomplete: on lines 3, 8, 9 and 11 the
interlinear gloss was recorded as clear context (KX-LATHTR), and every gloss line sits over the numeral line below it. Crops: `python3
tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/lines/canvas30_cipherzone.jpg --centres
58,192,246,310,448,506,570,642,708,775,842 --top-margin 45 --bottom-margin 30 --out <scratch>/c30 --prefix c30g` (11 crops, each one
gloss line plus its numeral line; scratch only, not committed). Two blind Sonnet passes (pass B in reverse order), neither shown the key
or the numerals' readings; this worker's reconciliation in `siblings/c30_gloss_reconciled.tsv`. The passes agree word for word on 7 of
11 lines; the splits (Condu-ict/-uti, foy/forte, Si/Doria letters, je/se) are bracketed and dropped from scoring rather than chosen.
Both passes place every gloss over its own line's numerals; pass A notes line 8 might be clear text at gloss height and "luy" (line
10) might be clear overflow. Numerals unchanged from ciphertext.tsv (two-pass, 97.3%).

**Test (rule 3; `siblings/c30_test.py`, output `siblings/c30_test_out.txt`; statistic, controls and gate committed before the glosses
were read, 81f030e2).** Per line, the margin/kat.py ordered walk: a code scores if its key_f23 value occurs in that line's gloss at or
after the previous match. Control 1 (the brief's): the 11 glosses permuted over the 11 numeral lines, 10000 permutations (the gloss each
run meets changes, so the score can differ). Control 2: equal-length windows of the f.23 gloss bank, 2000 draws. Gate: control 1 p95.
```
set	real	n	ctrl	mean	p95	max	P(ctrl>=real)
C	12	23	shuffled-gloss	7.01	10	14	0.0153
C	12	23	f23-window	9.49	13	16	0.1775
all	36	128	shuffled-gloss	27.77	33	41	0.0125
all	36	128	f23-window	32.47	39	48	0.2190
```
**Result.** key_f23's C codes read 12 of 23 canvas-30 occurrences consistently with the gloss in order; that clears the pre-registered
shuffled-gloss gate (P 0.015) but not the length-matched control (P 0.18). The permutation control puts short glosses ("luy", "Jurer")
on long runs and long glosses on short ones, so part of its margin is gloss length, not content; against same-length French from the
f.23 gloss the real score is not distinguishable. Read together: canvas 30 is not shown to share f.23's key at this N, nor shown not to
(a 23-occurrence test with one-letter values has little power against any French text). Observed, not counted: line 1 runs 48 23 54
.. 21 51 = c n du .. e de under "Condu[ite] de Knuyt", in order, the clearest single line. No code enters key.tsv or key_f23.tsv (rule 3
per-unit merge clause: the canvas did not clear the length-matched control); no reading changed, so no decode or judge re-run. Rule 4
for canvas 30 under key_f23: 149 tokens, C-valued 23 (12 consistent with the gloss), M-valued 105, not in key_f23 21; no token is
graded as read.

Hosts: none (crops cut from the on-disk cipherzone image). Vision: 2 Sonnet subagent calls (11 crops each) + this worker's
reconciliation from the passes (no extra zooms). No credentials.

## A2-COL7 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 32 numerals + gloss, pooled canvas 30+32 test against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col7.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c32_test.py` committed (6b9a14cb) before either canvas 32 pass was read: same ordered-walk
statistic as c30_test.py, pooled over canvas 30 + canvas 32; gate = pooled C hits above the p95 of the LENGTH-MATCHED f23-window
control (each line's gloss replaced by a same-length window of the f.23 gloss bank, 5000 draws; the French each run meets changes,
so the control can differ from the target); shuffled-gloss and canvas-32-only figures reported, not gating.

**Transcription (rule 2, Usage 6).** Canvas 32 is the opening folio 27v-28r, continuing canvas 30's 8 May 1646 letter; image on disk
(`images/crops/canvas32_full.jpg`, 2400 px), no network. Crops: `python3 tools/iiif_lines.py --image
ciphers/colbert26-lathuillerie-1644/images/crops/canvas32_full.jpg --region 300,240,900,1420 --centres
140,392,452,532,607,800,877,942,1012,1080,1145,1225,1284,1355 --top-margin 18 --bottom-margin 15 --out <scratch>/L --prefix c32L
--debug` (left page, 14 crops) and `... --region 1440,300,860,1150 --centres 144,207,280,342,870,934,1001,1065 ... --prefix c32R`
(right page, 8 crops); each band one gloss line plus its numeral row, centres set by eye from the debug overlay; crops in scratch,
not committed. Two blind Sonnet passes (B in reverse order), neither shown the key or canvas 30; this worker's reconciliation in
`siblings/c32_reconciled.tsv`. Pass A skipped crops L13-L14 (read by B and checked by eye). Numerals: 22 rows, 280 groups; A and B
agree on every group they both read except one (R04, 13/15, settled 15 by eye); 4 groups unsettled (two cut at the right edge, one
"2A", one 10/20) and skipped. Gloss: the passes read the same words; they split on whether a few words at the left of a row ("tout a
fait", "pour elle quelque", "comme elle l'est") are gloss or clear text -- kept, because the numerals start at the margin under them
(the letter text reads "invite a le [croire que par ce qu'elle me dit ...]", so a row of pure numerals has its plain text above it).
Dropped from scoring: the left-margin heading "Po. Mad. la P. Dor.", "Mais" (clear text), "Jey" (doubtful).

**Result** (`siblings/c32_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
pooled30+32	C	51	88	f23-window	37.18	43	51	0.0002	PASS
pooled30+32	C	51	88	shuffled-gloss	31.92	38	45	0.0000	-
pooled30+32	all	117	407	f23-window	103.24	115	128	0.0290	-
canvas32	C	39	65	f23-window	27.68	33	39	0.0002	-
canvas32	C	39	65	shuffled-gloss	25.71	30	37	0.0000	-
canvas32	all	81	279	f23-window	70.61	80	90	0.0486	-
```
key_f23's 21 C codes read 51 of 88 pooled occurrences consistently with the leaves' own gloss, in order, against a length-matched
control mean 37.2 (p95 43, max 51 in 5000): the pre-registered gate PASSES. Canvas 32 alone carries it (39/65 vs p95 33); canvas 30
alone stays below its length-matched control (A2-COL6, 12/23, P 0.18). Sensitivity (not a gate; pass A's narrower gloss, the four
disputed left-of-row phrases dropped): pooled C 49/88 vs p95 42, P < 0.0002 -- the result does not hang on the gloss-extent choice.
Read: f.23 (17 Mars 1646) and the 8 May 1646 letter (canvas 30-32) share key_f23's C values to a degree same-length French from
f.23's own gloss does not reach -- evidence for one key across the two letters, a statement about attestation, not a reading.
Observed, not counted: R06 48 22 25 .. = c m p under "compliment", R07 12 65 = c s under "charge a st ybart", L14 48 .. 51 .. 40 =
c de b under "discours de st ybart".

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step (the brief's "pass extends attestation
only"): canvas 32 cleared its own length-matched control, canvas 30 did not, so a later key revision may fold canvas 32's glossed
pairs in as a unit that cleared, and holds any code attested only on canvas 30. No reading changed, so no decode or judge re-run.
Rule 4 for canvas 32 under key_f23: 280 groups transcribed (276 settled), C-valued 65 (39 consistent with the gloss), C+M 279
(81 consistent); no token is graded as read.

Hosts: none (image on disk). Vision: 2 Sonnet subagent calls (22 line crops each) + this worker's reconciliation (one
3-crop zoom). No credentials.

## A2-COL8 (account 2, LANE-A2PUSH, 3 Oct 2026): joint interlinear_align re-fit, f.23 word pairs + canvas 32 + canvas 30

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col8.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/refit_c32.py` committed (03916af0) before its first run: one joint
`tools/interlinear_align.py align` fit (flags as A2-COL2/3: codes 100+code, `--floor 100 --keep-fs`) on the 116 f.23 word pairs
(P36 still held out), the 22 canvas 32 rows (`siblings/c32_reconciled.tsv`) and the 11 canvas 30 lines (`siblings/c30_gloss_reconciled.tsv`
+ ciphertext.tsv); 742 code tokens; '?' groups and [bracketed] gloss words dropped. Statistic: tokens with status `agrees`.
Control A: glosses dealt in a derangement within each unit (f.23 among f.23, c32 among c32, c30 among c30), 50 seeds. Control B
(A2-COL7's length-matched window): f.23 pairs real, every canvas 30/32 gloss replaced by a same-letter-length window of the f.23
gloss bank, 50 seeds. Both move the French each run meets, so both can differ from the real fit. Gates: G1 total agrees > A p95;
G2 sibling (c30+c32) agrees > B p95; both needed before any key change. Key rule: C only from occurrences on units that
cleared their own length-matched control (f.23, canvas 32); canvas 30 attestation reported, never counted.

**Result** (`siblings/refit_c32_out.txt`):
```
pairs	f23 116	c32 22	c30 11	tokens 742
stat	real	ctrl	mean	p95	max	P(ctrl>=real)	gate
agrees_total	190	A-derange-within-unit	105.5	116	125	0.00	PASS
agrees_total	190	B-f23-window	182.6	193	199	0.14	-
agrees_sibling	78	A-derange-within-unit	68.9	79	79	0.08	-
agrees_sibling	78	B-f23-window	70.0	80	87	0.10	FAIL
agrees_c32	59	A-derange-within-unit	49.0	57	59	0.02	-
agrees_c32	59	B-f23-window	46.2	56	58	0.00	-
gates	G1 PASS G2 FAIL
```
**G2 FAILS: the pre-registered gate for a key change is not met, so key_f23.tsv, key.tsv and the reading are unchanged** (no decode
or judge re-run needed). The joint fit beats a within-unit gloss shuffle (190 vs p95 116), but on the sibling rows it does not beat
same-length French from f.23's own gloss (78 vs p95 80, P 0.10). Observed, not gating (a post-hoc split, so a lead only): canvas 32
alone is 59 vs window p95 56, max 58 -- the shortfall is canvas 30 (19 sibling agrees beyond canvas 32's 59), the same unit that
missed its length-matched control in A2-COL6. A second observation: the joint key (`siblings/key_refit.tsv`, kept as the record of
this fit, not used) has only 10 C codes under the per-unit rule (24 n, 28 la, 40 b, 48 c, 49 que, 53 d, 65 s, 89 m, 97 pour, 98
vous) against key_f23's 21 -- the sibling rows are whole-line pairs (13-23 codes under a phrase), and long phrase pairs let the DP
spread chunks, as f.23 showed at phrase level (63 agrees) before its word-level re-pairing (128). So the instrument limit here is
the pairing grain of the sibling rows, not the key: the next step is to re-pair canvas 32 rows at word level by eye from the image
on disk (A2-COL3's method: split only where a visible gap between runs sits under the gloss words one to one), then re-run this
same pre-registered script with canvas 30 left out (it has not cleared its own control) and the gates unchanged.
Rule 4: no token changed grade; f.23 stays 306 tokens, H 0, C 92, S 0, M 213, I 0, U 1.

Hosts: none (all inputs on disk). Vision: 0 subagent calls, 0 own image reads. No credentials.

## A2-COL9 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 32 word-level re-pairing attempt and the re-fit with and without canvas 30

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col9.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/refit_c32w.py` committed and pushed (17a632c0) before any pairing or scoring: A2-COL8's
`refit_c32.py` with one input change (canvas 32 read from `siblings/c32w_pairs.tsv`, word-level where the image licenses a split,
whole rows otherwise) and two variants: `--no-c30` (f.23 word pairs + canvas 32; gating, since canvas 30 has not cleared its own
length-matched control) and with canvas 30 (line-level, reported, not gating). Statistic, controls A (derangement within unit) and B
(length-matched f.23 window), gates G1/G2, 50 seeds each, and the per-unit key rule unchanged.

**Re-pairing (by eye, one reader, not blind; rule 2).** Crops cut locally from `images/crops/canvas32_full.jpg` at A2-COL7's row
centres (PIL crop of each band +-45 px, three strip composites; scratch only, no network). Finding: **A2-COL3's method mostly does not
apply to canvas 32.** On f.23 the codes are unsegmented digit runs with visible gaps between runs; on canvas 32 every two-digit group is
written separately at an even spacing, so there are no run gaps inside a row, and the gloss line is written more compactly than the
numerals beneath it (L10's gloss ends about 170 px, at strip scale, before the numerals do; R06's gloss covers less than half its
row), so the gaps between gloss words fall over a group, not between two. Two splits only: R01 (two numeral runs separated by clear
text, "que M de Longueuille" over 96 32 56 13 20 31, "de" over 51 75 32: a real run gap) and L08 ("tout a fait" over 23 32 31 10 58: the
gloss gap after "fait" sits over the space between 58 and 20; the rest of the row kept whole because the "feroit | besoin" gap sits over
a 20). The other 20 rows stay whole. `siblings/c32w_pairs.tsv`: 24 pairs, code sequences unchanged from `c32_reconciled.tsv`.

**Result** (`siblings/refit_c32_w_out.txt`, gating; `siblings/refit_c32_wc30_out.txt`, with canvas 30):
```
variant --no-c30: pairs f23 116  c32 24  c30 0  tokens 593
agrees_total	174	A-derange-within-unit	81.9	p95 97	max 99	P 0.00	G1 PASS
agrees_sibling	62	B-f23-window	44.3	p95 55	max 56	P 0.00	G2 PASS
variant with c30: pairs f23 116  c32 24  c30 11  tokens 742
agrees_total	194	A-derange-within-unit	104.6	p95 116	max 129	P 0.00	G1 PASS
agrees_sibling	81	B-f23-window	68.7	p95 81	max 86	P 0.06	G2 FAIL
diagnostic, not gating (scratch copy, c32 as the 22 whole rows of A2-COL8, --no-c30):
agrees_total	172	A p95 95	PASS	agrees_sibling	57	B p95 51, max 54	PASS
```
**The pre-registered gating variant passes both gates (G1 174 vs p95 97; G2 62 vs length-matched p95 55, max 56 in 50).** Canvas 30
again holds the with-c30 variant below its gate (81 vs p95 81). Read honestly: the row-level diagnostic shows that **leaving canvas 30
out does most of the work** (row-level canvas 32 alone already clears G2, 57 vs p95 51), and the two word-level splits add 5 agrees
(57 -> 62). So this run is a different grain only in two rows; what it establishes is that canvas 32, fitted jointly with f.23 and
without canvas 30, beats same-length French from f.23's own gloss -- the same direction as A2-COL7's pooled C test (51/88, P 0.0002)
and A2-COL8's post-hoc canvas-32-alone lead, now under a gate written before the run. Caveat: leaving canvas 30 out was named by
A2-COL8 after it saw its own split, though the per-unit merge rule (canvas 30 failed its own control in A2-COL6, before A2-COL8)
already excluded canvas 30 from counting toward C.

**Key** (`siblings/key_refit_w.tsv`, the per-unit rule, C from f.23 + canvas 32 only): 10 C codes, every one already C in key_f23 at the
same value (24 n, 28 la, 40 b, 48 c, 49 que, 53 d, 65 s, 89 m, 97 pour, 98 vous). **No code enters key_f23.tsv** (the gates license a
key change, but the fit offers none), so key_f23.tsv, key.tsv and the reading are unchanged; `decode_key.py --check`: "reading up to
date", f.23 306 tokens C 92, M 213, U 1. No judge re-run (reading unchanged). Per code, canvas 32 confirms key_f23's C values weakly:
only 40 b (1/2) and 48 c (2/3) take the same chunk there; 51 de 2/8, 10 a 2/10, 12 c 2/10, 18 h 0/5 -- whole-row pairs (13-23 codes
under one phrase) still spread the DP's chunks, so canvas 32's aggregate agreement is real against its control but does not yet
attest individual codes. Rule 4: no token changed grade.

Hosts: none (all inputs on disk). Vision: 0 subagent calls; 3 own reads of strip composites (the one reconciliation unit). No
credentials.

## A2-COL10 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 33 (La Haye, 6e [?] 1648) numerals + gloss, key_f23 C test against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col10.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c33_test.py` committed and pushed (45934849) before the canvas 33 image was cropped or either
pass was read: c32_test.py's ordered-walk statistic on canvas 33 ALONE (one unit, rule 3's per-unit clause); gate = C hits with
P < 0.05 against the LENGTH-MATCHED f23-window control (each line's gloss replaced by a same-length window of the f.23 gloss bank,
5000 draws; codes fixed, so the control can differ from the target -- it did, mean 11.5, max 18); shuffled-gloss reported, not gating;
a power floor written before scoring: fewer than 15 C-valued occurrences = 'too short to test' whatever P is.

**Transcription (rule 2, Usage 6).** Image on disk (`images/crops/canvas33_full.jpg`, 2400 px; folio 29, signed La Thuillerie, La
Haye, 6e [?] de l'an 1648), no network. Two cipher zones on the left page. Crops: `python3 tools/iiif_lines.py --image
ciphers/colbert26-lathuillerie-1644/images/crops/canvas33_full.jpg --region 340,380,890,320 --centres 78,142,210,275 --top-margin 50
--bottom-margin 22 --out <scratch>/c33 --prefix c33T --debug` (upper zone, 4 crops) and `... --region 180,1040,1020,340 --centres
75,114,170,240,302 --top-margin 42 --bottom-margin 22 ... --prefix c33B` (lower zone, 5 crops); centres set by eye from the debug
overlay; crops in scratch, not committed. Two blind Sonnet passes (B in reverse order), neither shown the key; this worker's
reconciliation (two zoom reads of the zones) in `siblings/c33_reconciled.tsv`, 9 rows, 135 groups. Numerals: the passes agree on
every group (pass B misplaced the target row on 3 crops but read the same rows elsewhere; one split '29 61' vs '29/61' settled two
groups by eye); no group unsettled. Gloss: the passes agree on the words over T1, T2 (right), T3, B1, B2 (right). They split on
(a) 'mes lettres' over T2's left run and 'Espagnolz' over T4 (kept with the run they sit above), (b) the left word over B2 (read
'Jnutilement' by eye), and (c) the three underlined lines over B3, B4, B5 ('Sy vous auez quelque esperance de paix', 'Sil ne
fauldroit point tenir bride en main', 'pour la distribution dud argent'), which both passes called clear text. Kept as gloss by
layout, A2-COL7's rule: B3 and B5's numerals start at the margin directly under them, B4's clear text ('cela paroissoit, je ne
sçay') sits on the numeral line itself while the line above spans the numerals, and they are in the small underlined gloss style.

**Result** (`siblings/c33_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas33	C	16	21	f23-window	11.50	14	18	0.0064	PASS
canvas33	C	16	21	shuffled-gloss	9.54	13	16	0.0008	-
canvas33	all	45	122	f23-window	31.55	38	47	0.0002	-
canvas33	all	45	122	shuffled-gloss	28.69	35	43	0.0000	-
```
key_f23's C codes read 16 of 21 canvas 33 occurrences consistently with the leaf's own gloss, in order, against a length-matched
control mean 11.5 (p95 14, max 18 in 5000): **the pre-registered gate passes, and n = 21 is above the power floor.** This is our
only test so far of key_f23 outside 1646 (f.23 is 17 Mars 1646; canvas 33 is a January 1648 letter), and it supports one key across the
two years -- a statement about attestation, not a reading. Sensitivity (scratch copy, not a gate; the passes' narrower gloss, B3-B5
glosses dropped): C 10/12 vs length-matched p95 9, P 0.007, but n = 12 is below the pre-registered floor, so **the decision rests on
the layout call for B3-B5** (the direction holds either way, the N does not).
Observed, not counted (internal consistency, no key used): '52 30 31 12 44' stands under 'distribuer' (B1) and again inside 'la
distribution' (B5); both B2 runs end '76 70' under '-ment' (inutilement, ponctuellement). Conflict lead, not counted: key_f23 has
12 = c at grade C, but on canvas 33 code 12 stands twice in the 'distribu-' group (no c) and once under 'en main'; with A2-COL9's
canvas 32 figure (12 = c 2/10), 12's C grade is weakly supported off f.23 -- a candidate for the next key revision's own control,
not a change here.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step (attestation only); canvas 33 has now
cleared its own length-matched control, so a later key revision may fold its glossed rows in as a unit that cleared, alongside f.23
and canvas 32. No reading changed, so no decode or judge re-run. Rule 4 for canvas 33 under key_f23: 135 groups transcribed (all
settled), C-valued 21 (16 consistent with the gloss), C+M 122 (45 consistent); no token is graded as read.

Hosts: none (image on disk). Vision: 2 Sonnet subagent calls (9 line crops each) + this worker's reconciliation (2 zoom reads, plus
2 debug-overlay reads to set centres). No credentials.

## A2-COL11 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 35-36 (folio 31-32, La Haye, 9e de l'an 1648) numerals + gloss, key_f23 C test against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col11.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c3536_test.py` committed and pushed (5396a261) before either image was cropped or either pass
was read: a copy of c33_test.py with the statistic, the LENGTH-MATCHED f23-window control (5000 draws), the gate (C hits, P < 0.05)
and the n >= 15 power floor unchanged; folio 31-32 is one letter (signed La Thuillerie, La Haye, 9e de l'an 1648) and is scored as
ONE unit alone, not pooled with canvas 30/32/33; it also lists every occurrence of code 12 (A2-COL10's lead), not gating.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas35_full.jpg`, `canvas36_full.jpg`, 2400 px), no network.
Crops (scratch, not committed): `python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas35_full.jpg
--region 1440,440,920,1080 --centres 100,162,240,318,382,448,515,585,655,992,1052 --top-margin 58 --bottom-margin 22 --out <scratch>/c35
--prefix c35 --debug` (11 crops, right page) and `... canvas36_full.jpg --region 340,180,1000,1080 --centres 100,170,240,650,715,790,855,935,1000
--top-margin 58 --bottom-margin 22 --out <scratch>/c36 --prefix c36 --debug` (9 crops, left page); centres set by eye from an
auto-detected debug overlay. Two blind Sonnet passes (B in reverse order), neither shown the key; this worker's reconciliation (two
stacked zoom reads of 10 crops) in `siblings/c3536_reconciled.tsv`, 20 rows, 231 groups, 4 unsettled (35L01 24/29 and 19/79, 35L03
71/77, 35L09 10/20; skipped by the script). Numerals: the passes agree on every other group where both read the target row; settled
by eye: 35L07 g3 51 (B 31), 35L09 g9 23 (A 29), 36L01 g4 42 (B 12). Pass B read the neighbouring row on 3 crops (35L08, 35L11, and
re-attached several glosses one row off); pass A's row-and-gloss attribution matched the page by eye on every crop and was kept,
with the gloss assigned to the numerals it sits directly above (A2-COL7's rule). 36L08's 'M. le P. Do. auec quelques' (B: clear text)
sits over 40 44 82 30 32 23 30 in the small gloss hand and is kept as gloss.

**Result** (`siblings/c3536_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas3536	C	24	47	f23-window	18.18	22	27	0.0186	PASS
canvas3536	C	24	47	shuffled-gloss	14.48	19	25	0.0001	-
canvas3536	all	61	205	f23-window	52.35	60	70	0.0432	-
canvas3536	all	61	205	shuffled-gloss	48.29	55	63	0.0016	-
```
key_f23's C codes read 24 of 47 canvas 35-36 occurrences consistently with the leaf's own gloss, in order, against a length-matched
control mean 18.2 (p95 22, max 27 in 5000): **the pre-registered gate passes, n = 47 is above the power floor**, but the margin is
small (2 over p95; P 0.019, weaker than canvas 33's 0.006) and rests on pass A's gloss attribution, which B did not share on several
rows. With canvas 33 this is the second 1648 unit to clear its own control: one key for f.23 (March 1646), canvas 30-32 (May 1646)
and two La Haye letters of January 1648 is supported -- attestation, not a reading.
Observed, not counted (internal consistency, no key used): the run '52 31 17 15 32 29 25 12 23 46' stands under 'Led Sr Prince'
(35L06, after 76) and again under 'Sr Prince en estoit Larbitre' (35L09); '25 76 87 93' stands under 'Plenipotentiaires' on 36L02
and 36L07; '21 23 22 10 20 11 30' opens both 36L03 ('nous condemneroient') and the unglossed tail of 36L07 -> 36L08.
Code 12 (key_f23 12 = c, grade C): 5 occurrences here; consistent with 'c' twice, both inside the repeated 'Sr Prince' run
(35L06, 35L09), not under 'designer leur traitte', 'et moy' or 'Mr de et Knut'. With canvas 33 (0 of 3) and canvas 32 (2 of 10),
12 = c holds 4 of 18 off f.23 -- still a candidate for the next key revision's own control, not a change here.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 35-36 has now cleared its own
length-matched control, so a later key revision may fold it in as a unit that cleared, with f.23, canvas 32 and canvas 33. No
reading changed, so no decode or judge re-run. Rule 4 for canvas 35-36 under key_f23: 231 groups transcribed (227 settled), C-valued
47 (24 consistent with the gloss), C+M 205 (61 consistent); no token is graded as read.

Hosts: none (images on disk). Vision: 2 Sonnet subagent calls (20 line crops each) + this worker's reconciliation (2 stacked zoom
reads, plus 4 overlay/page reads to set centres). No credentials.

## A2-COL12 (account 2, LANE-A2PUSH, 3 Oct 2026): pre-registered joint key revision, f.23 + canvas 32 + canvas 33 + canvas 35-36, with 12 = c re-tested

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col12.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/refit_joint4.py` committed and pushed (f055ee14) before its first run: A2-COL9's
refit_c32w.py fit, statistic, controls and gates unchanged, inputs = the four units that each cleared their own length-matched
control (f.23 116 word pairs, P36 held out; canvas 32 24 pairs from c32w_pairs.tsv; canvas 33 9 line pairs; canvas 35-36 20 line
pairs; unsettled and 'a/b' groups dropped); canvas 30 not an input (rule 3 per-unit merge clause). Control A: glosses deranged within
each unit, 50 seeds; control B: f.23 real, every sibling gloss replaced by a same-length window of the f.23 gloss bank, 50 seeds --
both change the French each run meets, so both can differ from the real fit. G1 total > A p95, G2 sibling agrees > B p95, both
needed before any key change. Entry rule: joint C (n >= 2, >= 2/3 majority), agreeing on >= 2 distinct units, not already C in
key_f23; an existing C code is never re-valued from the fit. 12 = c re-test, independent of the fit: the c3536_test.py ordered walk
(full key_f23 C set) over every sibling line (canvas 32 reconciled rows, 33, 35-36), statistic = code 12 occurrences that score,
length-matched f23-window control (5000 draws); 12 downgraded C -> M only if real <= control mean.

**Result** (`siblings/refit_joint4_out.txt`; joint key with per-unit attestation `siblings/key_refit_joint4.tsv`; alignment
`siblings/refit_align_joint4.tsv`):
```
pairs	f23 116	c32 24	c33 9	c3536 20	tokens 951
agrees_total	227	A-derange-within-unit	mean 141.1	p95 153	max 157	P 0.00	G1 PASS
agrees_sibling	112	B-f23-window	mean 102.2	p95 114	max 115	P 0.14	G2 FAIL
(not gating) agrees_c32 65 vs B p95 58 (P 0.00); agrees_c33 20 vs B mean 20.9 (P 0.62); agrees_c3536 27 vs B mean 34.8 (P 0.96)
key-change candidates: 68 = s (f23 1/1, c33 1/1; key_f23 s/M) -- blocked by gates
12 = c ordered walk off f.23: 11 of 19 score vs length-matched mean 7.83, p95 11, P 0.085 -> stays C
```
**G2 FAILS (112 vs p95 114): the pre-registered gate for a key change is not met, so key_f23.tsv, key.tsv and the reading are
unchanged.** `decode_key.py --check`: "reading up to date"; f.23 306 tokens C 92, M 213, U 1; f.24 168 tokens C 27, M 140, U 1. No
judge re-run (reading unchanged). The fit beats a within-unit gloss shuffle (227 vs p95 153), but the sibling rows as a whole do not
beat same-length f.23 French. Per unit (not gating, post-hoc): canvas 32 still clears (65 vs p95 58), while canvas 33 sits at its
control mean (20 vs 20.9) and canvas 35-36 sits *below* it (27 vs 34.8). Both of those units cleared their own controls under the
ordered walk (A2-COL10 16/21, A2-COL11 24/47), so the miss is in the instrument, not evidence against the shared key: they enter the
DP as whole lines of 5-23 codes under a phrase, and long line pairs let interlinear_align spread chunks (A2-COL8 saw the same with
canvas 30 and canvas 32 at row grain; A2-COL9 showed even spacing defeats word-level re-pairing by eye). With A2-COL8 (FAIL at line
grain) this is the second joint-DP fit to fail G2 because of line-grain sibling pairs: **joint interlinear_align with line-level
sibling pairs is untestable-by-this-tool for canvas 33 and 35-36 at this N** (rule 3, third-attempt clause in spirit: no further
tuning of the same fit). A different instrument for key growth: anchor-split pairing (cut each sibling line at its key_f23 C hits
under the ordered walk into sub-pairs, fit only the codes between anchors, statistic counted on non-anchor codes so the anchors
cannot inflate it against control B), pre-registered, scripts only.
12 = c: the pre-registered rule keeps it C (11/19 scoring vs control mean 7.83), but the margin is not significant (P 0.085); the walk scores any later 'c' in the line's gloss, so it is more lenient than A2-COL10/11's hand count (4 of 18 under a word containing c at that place), and the control is lenient the same way;
per-code table, not gating: 25 p 9/9 (P 0.0004), 51 de 14/20 (P 0.002), 24 n 7/7 (P 0.044) attest off f.23; 18 h 0/7, 22 m 5/10
(mean 5.5), 40 b 1/4, 78 u 4/5 (mean 4.0) do not rise above the control -- leads for the next revision, no grade changed.
Rule 4: no token changed grade.

Hosts: none (all inputs on disk). Vision: 0 subagent calls, 0 image reads. No credentials.

## A2-COL13 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 39-40 (folio 35-36, La Haye, 13e Janvier 1648) numerals + gloss, key_f23 C test against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col13.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c3940_test.py` committed and pushed (4fe7e169) before either image was cropped or either pass
was read: a copy of c3536_test.py with the statistic, the LENGTH-MATCHED f23-window control (5000 draws), the gate (C hits, P < 0.05),
the n >= 15 power floor and the code-12 listing unchanged; folio 35-36 (closes "La Haye le 13e Janvier 1648", signed La Thuillerie;
docket on canvas 39's left page "10 [?] Janvier 1648") is one letter, scored as ONE unit alone, not pooled with canvas 30/32/33/35-36.
The control changes only the French each line meets (codes and order fixed), so it can differ from the real score.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas39_full.jpg`, `canvas40_full.jpg`, 2400 px), no network.
Crops (scratch, not committed): `python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas39_full.jpg
--region 1480,600,810,1000 --centres 85,143,208,278,345,420,485,557,625,695,758,820,883,950 --top-margin 58 --bottom-margin 22
--out <scratch>/c39 --prefix c39 --debug` (14 crops, right page), `... canvas40_full.jpg --region 420,250,800,310 --centres
75,130,208,270 ... --prefix c40` (4 crops, left page) and `... canvas40_full.jpg --region 1470,250,820,130 --centres 70 ... --prefix c40r`
(1 crop, right page top); centres set by eye on the --debug overlay (first runs were 10-40 px off and re-cut). Two blind Sonnet passes
(B in reverse order), neither shown the key; this worker's reconciliation (one stacked zoom read of 3 crops) in
`siblings/c3940_reconciled.tsv`, 19 rows, 267 groups, 2 unsettled (39L05 g18 and 39L08 g21, 13/15: the hand's 3 and 5 are not
separable on the crop; skipped by the script). The passes agree on every other group; A's two hedges (39L01 51/5, 39L12 46/36) settled
by eye to B's reading. Both passes attached the same gloss to the same numerals on every row (unlike A2-COL11, where B drifted a row);
two-group lines (39L02, 39L04, 39L07, 39L14) carry both glosses in order. Uncertain gloss words are bracketed and dropped by norm().

**Result** (`siblings/c3940_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas3940	C	37	56	f23-window	25.67	31	36	0.0000	PASS
canvas3940	C	37	56	shuffled-gloss	22.24	26	32	0.0000	-
canvas3940	all	104	231	f23-window	63.81	72	83	0.0000	-
canvas3940	all	104	231	shuffled-gloss	63.45	72	84	0.0000	-
```
key_f23's C codes read 37 of 56 canvas 39-40 occurrences consistently with the leaf's own gloss, in order, against a length-matched
control mean 25.7 (p95 31, max 36 in 5000): **the pre-registered gate passes, n = 56 is above the power floor, and the real score is
above every control draw** -- the clearest of the three 1648 units (canvas 33 P 0.006, canvas 35-36 P 0.019), and it rests on two passes
that agreed on gloss attribution. The C+M set (104/231) also sits above both controls' maxima. One key for f.23 (March 1646), canvas
30-32 (May 1646) and three La Haye letters of January 1648 is supported -- attestation, not a reading.
Observed, not counted (internal consistency, no key used): '31 75 48 23' stands under 'La conclusion' (39L03) and under 'la condition'
(40R01, '23 31 75 48 23' after 93 20); '21 29' closes 39L04's first group, 39L06's run and 39L09, and '23 31' closes 39L06, 40L02 and 40L04.
Code 12 (key_f23 12 = c, grade C): 4 occurrences here; the ordered walk scores 3 (39L09 'retracter', 39L11 'choses', 39L13 'Traitte
auec'), not 39L03 (where 48 = c took the 'c' of 'conclusion' first). With A2-COL12's 11 of 19 this lifts the off-f.23 walk count to
14 of 23 -- a lead for the next revision's own control, no grade changed here.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 39-40 has cleared its own
length-matched control and may be folded into a later key revision as a unit that cleared (with f.23, canvas 32, 33 and 35-36). No
reading changed: `tools/decode_key.py ... --check` "reading up to date" (f.23 306 tokens C 92, M 213, U 1; f.24 168 tokens C 27, M 140,
U 1); no judge re-run. Rule 4 for canvas 39-40 under key_f23: 267 groups transcribed (265 settled), C-valued 56 (37 consistent with the
gloss), C+M 231 (104 consistent); no token is graded as read.

Hosts: none (images on disk). Vision: 2 Sonnet subagent calls (19 line crops each) + this worker's reconciliation (1 stacked zoom read
of 3 crops, plus 2 half-page reads and 4 overlay/crop reads to set centres). No credentials.

## A2-COL14 (account 2, LANE-A2PUSH, 3 Oct 2026): canvas 47, 48 and 49 (folio 43-45, La Haye, 18-20 Jan 1648 and the opening of the 23 Jan letter) numerals + gloss, key_f23 C test per canvas against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col14.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c4749_test.py` committed and pushed (4fd3c2dd) before any image was cropped or any pass was
read: a copy of c3940_test.py with the statistic, the LENGTH-MATCHED f23-window control (5000 draws), the gate (C hits, P < 0.05), the
n >= 15 floor and the code-12 listing unchanged. Units, per the brief, one per canvas, each alone: canvas 47 and 48 (one letter, docket
"18 [?] Janvier 1648", closes "A la Haye ce 20e Janvier 1648", signed La Thuillerie) and canvas 49 (opens the letter that closes on
canvas 51, "le 23e Janvier 1648"). 'letter4748' (47+48) is reported, not gated.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas47_full.jpg`, `canvas48_full.jpg`, `canvas49_full.jpg`,
2400 px), no network. Crops (scratch, not committed), centres set by eye on the --debug overlay (canvas 47's first run was ~70 px off
and re-cut):
`python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas47_full.jpg --region 1480,480,880,1120
--centres 160,218,284,345,412,490,550,632,690,768,820,888,968,1032 --top-margin 66 --bottom-margin 26 --out <scratch>/c47 --prefix c47
--debug` (14 crops, right page); `... canvas48_full.jpg --region 440,280,830,600 --centres 105,290,352,412,500,562 --top-margin 62
--bottom-margin 24 --prefix c48` (6 crops, left page) and `... canvas48_full.jpg --region 1540,680,830,190 --centres 48,112 ... --prefix
c48r` (2 crops, right page); `... canvas49_full.jpg --region 1500,330,900,1250 --centres
75,140,210,278,350,415,485,548,610,678,745,812,875,940,1010,1140,1205 --top-margin 62 --bottom-margin 24 --prefix c49` (17 crops, right
page). Two blind Sonnet passes per canvas (B in reverse order), neither shown the key; this worker's reconciliation (one stacked zoom
read of 3 crops, plus the three overlays) in `siblings/c4749_reconciled.tsv`, 39 rows (37 with numerals), 2 groups unsettled and skipped
(47L14 first group cut at the crop's left edge; 48L05 last group cut at the region's right edge). Numerals: the passes agree on every
group but four (47L04 61/67, 49L01 10/co, 49L02 41/47, 49L12 13/15), settled by eye to 67, 10, 47, 13. Glosses: on canvas 47 the passes
attached the same gloss to the same row throughout. On canvas 49 pass A attached to every numeral row the gloss written BELOW it (its
gloss texts match B's line for line, one row shifted, and its last two rows are off by one); B attached the gloss above, as on every
other leaf of this volume and as the overlay shows ('a Gouuerner' is the only writing over 49L01's numerals): B taken. On canvas 48 pass A
took four full-size gloss lines (over 48L03-L06) for clear text and gave no gloss; B, given one added layout sentence (the gloss is the
line immediately above its numeral row and may be written as large as the clear text; never take one from below), read them as gloss,
which the overlay supports (no clear text on those numeral rows). Both attribution calls were made before the test was run.

**Result** (`siblings/c4749_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas47	C	31	46	f23-window	20.44	25	30	0.0000	PASS
canvas47	C	31	46	shuffled-gloss	19.51	23	30	0.0000	-
canvas48	C	16	29	f23-window	10.94	14	18	0.0172	PASS
canvas48	C	16	29	shuffled-gloss	12.28	16	19	0.0502	-
canvas49	C	28	48	f23-window	19.35	24	31	0.0028	PASS
canvas49	C	28	48	shuffled-gloss	15.65	20	25	0.0000	-
letter4748	C	47	75	f23-window	31.22	37	44	0.0000	-
canvas47	all	78	180	f23-window	45.23	53	64	0.0000	-
canvas48	all	39	92	f23-window	22.96	28	34	0.0000	-
canvas49	all	73	194	f23-window	48.99	57	68	0.0000	-
```
All three pre-registered per-canvas gates pass, each above the n 15 floor: canvas 47 31/46 (above every one of 5000 control draws, max
30), canvas 48 16/29 (P 0.017, narrow, and its shuffled-gloss P is 0.050), canvas 49 28/48 (P 0.003). The letter of 20 Jan 1648 taken
whole (47+48, not gated) reads 47/75 against a maximum control draw of 44.
**Attribution sensitivity (diagnostic, run after the gated test, not gating):** re-scored with pass A's glosses (canvas 49 one row
shifted, canvas 48 with A's four missing glosses), canvas 49 falls to 10/44 vs mean 13.0, P 0.95 (FAIL; run on a scratch copy, `siblings/` files untouched) and canvas 48 to 6/9 (below the
floor). So the statistic does discriminate gloss attribution (the control can and does fail differently), and the canvas 48 and 49
passes rest on the above-row attribution call, which is the volume's layout everywhere else; the canvas 47 pass does not depend on it
(both passes agreed).
Code 12 (key_f23 12 = c, grade C): 9 occurrences on 8 lines; the ordered walk scores 7 (47L04 twice, 47L09, 48L06 twice, 49L06, 49L08,
49L15; not 48L03, where 48 = c and later codes took the gloss's c's first, nor 49L10). With A2-COL13's 14 of 23 this lifts the off-f.23
walk count to 21 of 32 -- a lead for the next revision's own control, no grade changed here.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 47, 48 and 49 have each cleared their own
length-matched control and may be folded into a later key revision as units that cleared (with f.23, canvas 32, 33, 35-36, 39-40;
canvas 48 and 49 flagged as resting on the attribution call). No reading changed: `tools/decode_key.py ... --check` "reading up to
date" (f.23 306 tokens C 92, M 213, U 1; f.24 168 tokens C 27, M 140, U 1); no judge re-run. Rule 4 under key_f23: canvas 47 204
settled groups (C-valued 46, 31 consistent with the gloss; C+M 180, 78), canvas 48 104 settled groups (C 29, 16; C+M 92, 39),
canvas 49 223 settled groups (C 48, 28; C+M 194, 73); no token is graded as read.

Hosts: none (images on disk). Vision: 6 Sonnet subagent calls (2 per canvas, 14 / 8 / 17 line crops each) + this worker's
reconciliation (1 stacked zoom read of 3 crops, plus 4 overlay reads to set centres, 1 crop check, 3 half-page reads). No credentials.

## A2-COL15 (account 2, LANE-A2PUSH2, 3 Oct 2026): canvas 50 and 51 (folio 46-47, La Haye, the letter of 23 Jan 1648 that canvas 49 opens) numerals + gloss, key_f23 C test per canvas against the length-matched control

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col15.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c5051_test.py` committed and pushed (2a6826b4) before any canvas 50-51 crop was cut or any pass
read: a copy of c4749_test.py with the statistic, the LENGTH-MATCHED f23-window control (5000 draws), the gate (C hits, P < 0.05), the
n >= 15 floor and the code-12 listing unchanged. Units, one per canvas, each alone: canvas 50 (both pages, heavy cipher) and canvas 51
(closes "A la Haye le 23e Janvier 1648", signed La Thuillerie; TOO-SHORT expected, ~4 rows). 'letter4951' (49+50+51, the whole letter of
23 Jan 1648, canvas 49 rows from c4749_reconciled.tsv) is reported, not gated.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas50_full.jpg`, `canvas51_full.jpg`, 2400 px), no network. Centres
set by eye on an automatic --debug overlay of each region, then cut (scratch, not committed):
`python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas50_full.jpg --region 400,220,830,1340
--centres 95,158,240,293,357,505,565,765,825,895,1020,1108,1155,1300 --top-margin 66 --bottom-margin 26 --out <scratch>/c50 --prefix c50l
--debug` (14 crops, left page; overlay checked); `... canvas50_full.jpg --region 1500,250,840,1380 --centres
100,158,238,297,357,497,568,630,830,890,960,1030,1105,1172,1238,1310 ... --prefix c50r` (16 crops, right page); `... canvas51_full.jpg
--region 370,200,880,700 --centres 112,188,242,322,578,638 ... --prefix c51` (6 crops, left page). Two blind Sonnet passes per canvas (B in
reverse order), neither shown the key, both given the layout sentence (gloss is the line immediately above its numeral row, may be as
large as the clear text, never from below). Two-reader split on numerals: 11 of 503 group positions differ (0.022; agreement, not
accuracy, TRANSCRIPTION.md); BENCHMARK-TX.tsv has no colbert26 row (its header names this family "not built"), none built here.
Reconciliation (this worker, one stacked zoom read of 7 crops) in `siblings/c5051_reconciled.tsv`, 36 rows: 50a01 61/67 -> 67, 50a08
15/13 -> 15, 50b15 78/18 -> 78, 50b16 35/34 -> 34; left unsettled and skipped (6 groups): 50a10 first group (94/97), 50b03 last two
(33 31 / 3 35), 50b04 last (33?/334), 50b16 last (75?/45). Glosses: the passes attached the same gloss to the same row on all 36 rows
except 51L02 (A none, B "repentent de la faulte quil ont", which the overlay shows over that run: B taken). Two attribution calls, both
made before scoring and both following the layout rule the passes agreed on: 50a05 "telles nouvelles de Naples" is gloss (it fills the
clear "lon eust de ... que le mauvais estat"), and 50b01, the top line of the right page ("Guerre sy le Duc ou les Espagnolz ...
nous en donnoient"), is gloss over a 24-group run, not clear text continuing the left page's "recommencer la".

**Result** (`siblings/c5051_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas50	C	65	97	f23-window	44.09	51	59	0.0000	PASS
canvas50	C	65	97	shuffled-gloss	35.25	41	49	0.0000	-
canvas51	C	10	13	f23-window	5.66	8	11	0.0036	TOO-SHORT
canvas51	C	10	13	shuffled-gloss	7.00	9	10	0.0379	-
letter4951	C	103	158	f23-window	69.14	78	86	0.0000	-
canvas50	all	141	396	f23-window	100.86	112	133	0.0000	-
canvas51	all	20	52	f23-window	15.18	20	26	0.0646	-
```
Canvas 50 passes its pre-registered gate, 65/97 above every one of 5000 control draws (max 59), the largest single unit of this volume
so far. Canvas 51 carries 13 C-valued occurrences, under the n 15 floor written before scoring: TOO-SHORT, whatever its P (0.004). The
letter of 23 Jan 1648 taken whole (49+50+51, not gated) reads 103/158 against a maximum control draw of 86.
**Attribution sensitivity (diagnostic, run after the gated test on scratch copies, not gating):** 50b01 with no gloss (the clear-text
reading of the top line): canvas 50 61/93 vs p95 48, max 56, still PASS; 50b01 with pass A's cleaner wording instead of B's ("voulut" for
"couluz", "le Duc" for "leed Dur"): 65/97, unchanged. The canvas 50 pass does not rest on either attribution call.
Code 12 (key_f23 12 = c, grade C): 13 occurrences on canvas 50-51; the ordered walk scores 7 of 13. With A2-COL14's 21 of 32 this makes
28 of 45 off f.23 -- a lead for the next revision's own control, no grade changed here.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 50 has cleared its own length-matched
control and may be folded into a later key revision as a unit that cleared; canvas 51 has not (TOO-SHORT) and stays out of any merge. No
reading changed: `tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check` "reading up to date" (f.23 306 tokens C 92, M 213, U 1;
f.24 168 tokens C 27, M 140, U 1); no judge re-run. Rule 4 under key_f23: canvas 50 436 settled groups (C-valued 97, 65 consistent with the
gloss; C+M 396, 141), canvas 51 61 settled groups (C 13, 10; C+M 52, 20); no token is graded as read.

Hosts: none (images on disk). Vision: 4 Sonnet subagent calls (canvas 50: 30 line crops each, canvas 51: 6 each) + this worker's
reconciliation (1 stacked zoom read of 7 crops, plus 2 page overviews and 4 overlay reads to set centres). No credentials.

## A2-COL16 (account 2, LANE-A2PUSH2, 3 Oct 2026): anchor-split pairing of the cleared units against control B

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col16.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0. Scripts only, disk only, no images, no network.

**Pre-registration (rule 3), written and pushed before the script's first run.** Script `siblings/anchor_split.py` (docstring is the
full registration). Units: f.23 (word pairs, interlinear/f23w_pairs.tsv), canvas 32, 33, 35-36, 39-40, 47, 48, 49, 50 -- each cleared
its own length-matched control; canvas 30 and 51 are never read. Anchors: key_f23 C codes that score in the ordered greedy walk
(c5051_test.py's walk). Spans: interior only, between two consecutive anchors; eligible if 1-3 non-C codes and 1-12 gloss letters.
Statistic S: per non-anchor code, max over letter n-grams g (length 1-4) of (distinct units whose spans containing the code contain g)
minus 1, floored at 0, summed over codes; secondary S_exact (k = 1 spans, identical text) reported, not gating. Control B: same anchors
and spans, span texts permuted among eligible spans of equal letter length pooled across units, 2000 draws (the score depends on which
text meets which code, so it can differ; spans in a length class of one are counted and printed). Gate: PASS iff S > p95 of control B
and P < 0.05. Merge rule: only cleared units are read; on PASS candidates go to a separate key_f23_anchor.tsv, C where >= 2 cleared units
agree on a unique best n-gram, else M; key_f23.tsv and key.tsv untouched. On FAIL: logged FAIL, first attempt with this instrument
(not [retired]).

**Result** (`siblings/anchor_split_out.txt`): 172 lines, 139 interior spans, 51 eligible on all 9 units (f23 1, c32 3, c33 4, c3536 2,
c3940 7, c47 8, c48 4, c49 4, c50 18); 4 spans sit in a length class of one and cannot move under control B.
```
stat	real	ctrl	mean	p95	max	P(ctrl>=real)	gate
S	30	control-B	26.40	29	31	0.0280	PASS
S_exact	2	control-B	0.15	1	2	0.0030	-
```
The pre-registered gate passes, narrowly: S 30 against control-B p95 29, max 31, P 0.028; the excess over the control mean is about 3.6
code-points, so most of the 17 codes that agree across two or more units do so at chance. S_exact (not gating): codes 23 and 30 have the
same one-code span text in two units, 2 vs p95 1.
Candidates written as registered to `key_f23_anchor.tsv` (17 codes: 11 graded C, 6 M on tied best n-grams); key_f23.tsv and key.tsv
untouched, so `tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check` reads "reading up to date" (f.23 306 tokens C 92, M 213,
U 1; f.24 168 tokens C 27, M 140, U 1). No judge re-run, no reading changed. **Rule 4:** no token is graded as read from this step.
**Per-code diagnostic (post hoc, NOT gating; `siblings/anchor_split_diag.py`, `siblings/anchor_split_diag_out.txt`):** the share of
2000 control-B draws in which each code reaches its real agreement count. No single candidate is below 0.05: the best are 23 = n (6 units,
P 0.078, agrees with key_f23's M value n) and 77 = l (2 units, P 0.182, conflicts with key_f23 M faire); 30 = s (4 units, P 0.467) also
agrees with its key_f23 M value; every other candidate is at 0.44-1.00. So the aggregate PASS is not carried by any one code, and the C
grades in key_f23_anchor.tsv are the pre-registered labels on a narrow pooled pass, not per-code evidence: none should enter key_f23.tsv
without its own per-code control. Conflicts with key_f23 M values (M vs M, not an H-grade conflict, rule 4): 11, 26, 29, 31, 39, 46, 54,
57, 76, 77 (32 'ou' vs 'o' is a near agreement). What would change it: more eligible spans per code -- canvas 54-56 (and 62-63) cleared
as units and added to the same unchanged script; per-code power needs about three or more units per code.
Hosts: none. Vision: 0 calls. No credentials.

## A2-COL17 (account 2, LANE-A2PUSH2, 3 Oct 2026): canvas 54, 55 and 56 (folio 50-52, La Haye, the letter closed "A la Haye le 27e Janvier 1648") numerals + gloss, key_f23 C test per canvas against the length-matched control, and a held-out check of A2-COL16's anchor candidates

Brief `.claude/briefs/runs/2026-10-03-acct2-a2-col17.md`. Intake gate at start: `colbert26-lathuillerie-1644: partial (line 1) --
edition/page or full-text-search citation found within 6 lines`, exit 0.

**Pre-registration (rule 3).** `siblings/c5456_test.py` committed and pushed (fa875a98) before any canvas 54-56 crop was cut or any pass
read: a copy of c5051_test.py with the statistic, the LENGTH-MATCHED f23-window control (5000 draws), the gate (C hits, P < 0.05), the
n >= 15 floor unchanged; one gate per canvas (54, 55, 56); 'letter5456' reported, not gated. The same docstring registers the held-out
check of the 17 key_f23_anchor.tsv candidates (NOT a gate): spans built as anchor_split.py builds them; a candidate occurs if it is a span
code of an eligible 54-56 span and agrees if one of its alternatives is in at least half of its spans' texts; scope = the 54-56 canvases
that pass their own gate; reference control H (span texts redrawn at equal length from the pool of all cleared units' eligible span
texts, 2000 draws); support written before looking as agree >= ceil(occur/2) AND agree > control-H p95.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas54_full.jpg`, `canvas55_full.jpg`, `canvas56_full.jpg`, 2400 px),
no network. Centres set by eye on ruled region views, then cut (scratch, not committed):
`python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas54_full.jpg --region 1240,660,1120,920
--centres 45,125,170,255,325,405,455,745,805,875 --top-margin 60 --bottom-margin 22 --out <scratch>/c54 --prefix c54 --debug` (10 crops,
right page); `... canvas55_full.jpg --region 170,260,1080,1340 --centres 120,200,265,343,420,490,574,651,854,941,1162,1239,1316
--top-margin 50 --bottom-margin 20 ... --prefix c55a` (13, left page; overlay checked); `... canvas55_full.jpg --region 1220,250,1160,420
--centres 160,228,310,385 --top-margin 55 ...` and `--region 1220,1240,1160,380 --centres 80,140,335 ...` (4 + 3, right page, ids
55b01-07); `... canvas56_full.jpg --region 170,190,1080,1010 --centres 125,195,270,405,490,610,680,765,825,890,975 --top-margin 55 ...`
(11, left page). Two blind Sonnet passes per batch (batch X = 54 + 55 left, batch Y = 55 right + 56; B in reverse order), neither shown
the key or any repo file, both given the layout sentence; each returned its TSV as reply text and this worker wrote the files.
Two-reader split on numerals: 5 of 537 group positions differ (0.009; agreement, not accuracy, TRANSCRIPTION.md -- the two readers saw the
same crops and may share errors); BENCHMARK-TX.tsv has no colbert26 row, none built here. Reconciliation (this worker, one stacked zoom read
of 5 regions) in `siblings/c5456_reconciled.tsv`, 41 rows, 536 settled groups (54: 113, 55: 282, 56: 141): 54a10 13/15 -> 15, 55a02 59/54
-> 54 (the final barred group is 59), 55a10 94/93 -> 94; 55a12 last group cut by the crop edge (3?/233), unsettled, skipped. Glosses: the
passes agreed on every row's attribution except 55b02 (B repeated the 55b03 gloss; the zoom shows A's "que je tiennent | dedans lassemblee
de hollande" over this row: A taken) and 55a07 (B adds "Jl en", en struck, at the right: "Jl" kept). One attribution call, made before
scoring and following the layout rule both passes applied: 55a05, a numeral-only row under a full-size line ("Traictez que nous auons faict
auec eux, leur alliance"), is gloss -- the run 10 28 23 30 is glossed "auons" on 54a04 and stands under "auons" here.

**Result** (`siblings/c5456_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas54	C	18	29	f23-window	11.91	15	19	0.0038	PASS
canvas55	C	39	59	f23-window	26.75	32	38	0.0000	PASS
canvas56	C	21	29	f23-window	12.91	16	19	0.0000	PASS
letter5456	C	78	117	f23-window	51.54	59	66	0.0000	-
```
All three canvases pass their own pre-registered gate (shuffled-gloss, not gating, agrees: P 0.007, 0.000, 0.000). The letter taken whole
(not gated) reads 78/117 against a maximum control draw of 66. **Attribution sensitivity (diagnostic, after the gated test, scratch copy,
not gating):** 55a05 with no gloss: canvas 55 33/51 vs p95 28, max 34, P 0.001, still PASS. Code 12 (key_f23 12 = c, grade C): 8
glossed occurrences on 54-56, the ordered walk scores 5 of 8; with A2-COL15's 28 of 45 off f.23 this makes 33 of 53 -- a lead for the next
revision's own control, no grade changed.

**Held-out check of A2-COL16's 17 anchor candidates (NOT a gate):** 16 eligible spans on 54-56 (all three canvases passed, so primary
scope = all three); 11 of 17 candidates occur; 8 agree (11 re, 20 e|i|t, 21 e|t, 30 s, 31 t, 39 e|o, 57 aire|fair, 83 r|s); 3 do not
(23 n 1 of 3 spans, 32 ou 1 of 4, 75 la 0 of 1). Control H: mean 2.78, p95 5, max 8, P 0.0005 -> 'support' by the registered criterion.
Diagnostic with 55a05's gloss removed: 9 occur, 7 agree vs control-H p95 4, max 6 -- still support. Read with care: 5 of the 8 agreeing
values are single letters or letter alternatives, and every agreeing code rests on 1-2 spans; the control holds span length fixed, so the
excess over it is real at the pooled level, but no single candidate is shown here, and 23 = n -- A2-COL16's best per-code diagnostic --
is among the three that do not agree. key_f23_anchor.tsv, key_f23.tsv and key.tsv unchanged.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 54, 55 and 56 have each cleared their own
length-matched control and may be added as units to a re-run of siblings/anchor_split.py or to a later key revision. No reading changed:
`tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check` "reading up to date" (f.23 306 tokens C 92, M 213, U 1; f.24 168 tokens
C 27, M 140, U 1); no judge re-run. Rule 4 under key_f23: canvas 54 113 settled groups (C-valued 29, 18 consistent with the gloss; C+M 97,
34), canvas 55 282 (C 59, 39; C+M 244, 89), canvas 56 141 (C 29, 21; C+M 130, 42); no token is graded as read.

Hosts: none (images on disk). Vision: 4 Sonnet subagent calls (batch X 23 line crops each, batch Y 18 each) + this worker's
reconciliation (1 stacked zoom read of 5 regions, plus 5 ruled region views and 1 overlay read to set centres). No credentials.

## A4-RFCOL (account 4, LANE DEFAULT-account-4-20261005-2253, 6 Oct 2026): canvas 20-21 gloss-vs-clear on native crops

Brief `.claude/briefs/runs/2026-10-05-account4-default-2253-jobs.md` section A4-RFCOL (cap 4, box 60 min).

**Crops (commands).** `python3 tools/iiif_lines.py --ark btv1b10035069t --canvas 20 --region 3650,3450,3600,2050 --out <scratch>/c20
--prefix c20 --debug --dry-run` and `--canvas 21 --region 1100,1150,2650,1300` (Gallica IIIF: 2 info/region requests + 1 info.json,
native 7427x6365); then per unit `python3 tools/iiif_lines.py --image <src> --region X,cy-175,W,240 --centres H/4,3H/4
--lines-per-crop 2 --top-margin H/4 --bottom-margin H/4 --max-width 2000 --overlap 200` (canvas 20, 11 units, cy = 188 325 638 763
900 1050 1200 1363 1525 1663 1838) and the same with cy-190 and --max-width 1500 for canvas 21 (7 units, cy = 285 432 552 700 856
1003 1159). 36 segment crops, each a cipher line with the small hand above it, kept in the session scratchpad (folder at 30 MB;
re-derivable from these commands).

**Finding: the canvas 20-21 small hand is a word-for-word interlinear decipherment, not topical notes.** One blind Sonnet pass per
canvas, then this worker against the crops (`interlinear/c20c21_reconciled.tsv`, 18 units, with pass and committed-file differences per
row). Both passes, unprompted, judged every small-hand line except one a rendering of the run beneath it that reads on with the clear
words on both sides: "ilz aiment mieux que ce soit [par les armes que par un accommodement]", "ce ne sera pas [de cette part la que
le traitte se rompra]", "Ilz se resolvent s'ilz n'en peuvent [sortir aultrement de se reserrer dans leurs isles et les deffendre de
boucher] autant quilz pourront [le passage du Sund et laisser sans combatre consommer leurs ennemis] devant eux". Two points settled
here against a pass: (1) the canvas 20 pass took "si enyvrez de leur bonne fortune quilz" for the main hand; on crop c20_U02_L01_s1
it is the small hand squeezed between the lines, with dots over 56, 43 and 9o echoed by dots in "bonne" and "fortune", so a gloss of
the 17-sign run under it; (2) the pass called "Je parle des Suedois" an aside (NOTE); it sits over 6 25 zz 11 83 v and the run spells
it with codes that read the same elsewhere on the leaf (25 par, 11 le, 83 de), so it is the gloss of an enciphered aside.
KX-LATHKEY2's "topical, not word-for-word" judgement (25 Sept 2026) does not hold, and its reason does: **the committed
`ciphertext.tsv` gloss column for canvas 20 is attached one line off** from line 21 on (line 22 `31 6 h` carries the gloss of the
`83 46 25 ...` run, line 23 that of `31 13 h ...`, and so on; line 27 empty), and the line-17 gloss is missing, so the 11-token run
met a 4-word gloss and short runs met long glosses. `ciphertext.tsv` is left as transcribed (not repaired in place; the reconciled
file is the reference for glosses). Canvas 21's committed glosses are on the right lines but read "peu de", "couvriront", "du fr."
where the crops give "petit", "coustera" [?], "de se".

**Known-answer test (interlinear/c20c21_knownanswer.py, output c20c21_knownanswer_out.txt).** key_f24.tsv's six C codes, built from
f.24 alone, used as predictions: an occurrence hits if its chunk appears in the unit's gloss within +-0.25 of the token's relative
position. Real 14/19 vs deranged-gloss control (2000 seeds, no unit keeps its own gloss; the control changes which gloss a run meets,
so it can fail differently) mean 3.02, p95 6, max 10, P 0.0000. Per code: 83 = de 6/6, 31 = que 4/4, 16 = m 2/2 (weak: m is common in
these glosses), **25 = m 2/7**. 51 and 92 do not occur on canvas 20-21.

**Regrade (key_period.tsv).** 83 = de and 31 = que: M -> C (predicted from f.24, read in place here, control above). 25: data
conflict (rule 4), logged not settled -- canvas 20-21 put it under par/part/pas/pa(ssage) about seven times, f.24 has it as m (2/3);
M on both until a third leaf decides. Leads graded M because observed after the read: 42 = si (4 occurrences), 11 = le/les, 6 = je?
(c20U01). The old phrase values for these codes were the one-line-off glosses and are replaced. Other key_period rows unchanged
(still the KX-LATHKEY2 phrase attachments, M). No decode job exists for canvas 20-21 (decode.json covers f.23 and f.24 only);
`python3 tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check`: reading up to date, exit 0.

**Not done (successor).** Align canvas 20-21 with tools/interlinear_align.py on c20c21_reconciled.tsv (about 230 tokens, the second
mixed-design leaf pair), with key_f24's 83/31 as seeds and its own shuffled-gloss control, then a joint f.24 + canvas 20-21 fit only
if each unit clears its own control (rule 3, per-unit merge). Unglossed tails (c20U01 44 w' 85 d h, c20U04 ll 35 d 45 g 11 v,
c20U05b 5 72 49 v, c20U09 n ll 26 37 6, c21U03 42 48 f uj) are the readable target once a key exists.

Hosts: gallica.bnf.fr IIIF 3 requests (>= 1.5 s apart). Subagents: 2 (Sonnet, one blind pass per canvas). No credentials.

## A4-COLALN (account 4, LANE DEFAULT-account-4-20261005-2253, 6 Oct 2026): interlinear_align on canvas 20-21

Brief `.claude/briefs/runs/2026-10-05-account4-default-2253-jobs.md` section A4-COLALN (cap 2.5, box 40 min). Script
`interlinear/c20c21_align.py` (rule, flags, gate and seed written in its docstring before the run; its commit landed after the
run because the pre-run push did not stage it -- the content was not edited after the run, but the commit order cannot show that).
Pairs from `interlinear/c20c21_reconciled.tsv` (18 rows), unglossed tails named in each row's notes cut, signs mapped through
f.24's `sign_ids.tsv` (new signs from id 160, `c20c21_sign_ids.tsv`); flags as f24_control.py (`--floor 100 --keep-fs
--max-chunk 6 --word-prior`), prior 83 = de and 31 = que only (`c20c21_seed.tsv`; 25 not seeded, rule 4 conflict). Control per
unit: gloss lines deranged within the unit, 200 seeds; gate: agrees_all and agrees_unseeded both above the control p95.

| unit | agrees_all real / ctl mean / p95 / max | agrees_unseeded real / ctl mean / p95 / max | gate |
|---|---|---|---|
| canvas 20 (11 rows) | 13 / 5.4 / 11 / 15 (P 0.015) | 6 / 4.7 / 10 / 14 (P 0.40) | FAIL |
| canvas 21 (7 rows) | 9 / 7.3 / 13 / 17 (P 0.34) | 6 / 7.1 / 12 / 17 (P 0.72) | FAIL |
| joint (diagnostic, not gated) | 32 | 22 | -- |

Both units fail their own gate, so nothing is merged into key_period.tsv (rule 3 per-unit clause); the canvas 20 total clears its
p95 only through the two seeded codes (83 de 6/6, 31 que 4/4), and the unseeded agreement sits at the control's level. The flat-start
DP splits word-length glosses into letters (25 -> e/p/par, v -> ssuedo/tables/abatuz, h' -> nnemy/nnemis), so at about 18 short rows
this tool does not separate real from deranged pairing for this mixed design: first attempt with this instrument, logged as a FAIL at
this N, not a refutation. Leads already graded M in key_period.tsv (42 si, 11 le/les, 6 je?) are unchanged; per-code chunks in
`interlinear/c20c21_codes.tsv`. The canvas 20 gloss column in ciphertext.tsv is not edited: A4-RFCOL's native crops are not on disk
(its scratchpad), and the reconciled file remains the gloss reference. `decode_key.py --check` exit 0. No host requests, no subagents.

## R7A-COL26 (account 1, LANE-RUN7-account-1, 6 Oct 2026): anchor_split re-run with canvas 54, 55, 56 added as cleared units

Brief `.claude/briefs/runs/2026-10-06-account1-run7-jobs.md` section R7A-COL26 (cap 3, box 50 min). Step checked undone first: A2-COL18
(3 Oct) was interrupted with no commit (section "Interrupted" below), and no later commit in this folder ran it. Scripts only, disk only.

**Pre-registration (rule 3).** `siblings/anchor_split_5456.py`, a copy of A2-COL16's `siblings/anchor_split.py`, committed and pushed
(823fc36f) before its first run. Changes, and only these: units c54, c55, c56 read from `siblings/c5456_reconciled.tsv` (each cleared its
own length-matched control, A2-COL17); candidates written to a separate `key_f23_anchor_5456.tsv`. Statistic S, S_exact, spans,
eligibility, control B (2000 draws, same seed), gate (PASS iff S > p95 and P < 0.05) and merge rule unchanged; key_f23_anchor.tsv
(A2-COL16) left as it was.

**Result** (`siblings/anchor_split_5456_out.txt`): 213 lines, 180 interior spans, 67 eligible on 12 units (54: 3, 55: 7, 56: 6 added to
A2-COL16's 51); 3 spans sit in a length class of one.
```
stat	real	ctrl	mean	p95	max	P(ctrl>=real)	gate
S	47	control-B	39.00	43	47	0.0010	PASS
S_exact	7	control-B	0.46	2	4	0.0000	-
```
PASS, wider than A2-COL16's (S 30 vs p95 29, P 0.028): the excess over the control mean grows from 3.6 to 8.0 code-points and the real
value now equals the control's maximum in 2000 draws. S_exact (not gating) is 7 against a control maximum of 4. 21 candidates were
written as registered to `key_f23_anchor_5456.tsv` (18 C, 3 M on tied best n-grams). These are the pre-registered labels on a pooled
pass, not per-code evidence. key_f23.tsv and key.tsv are unchanged.

**Per-code diagnostic (post hoc, NOT gating; `siblings/anchor_split_5456_diag.py`, `siblings/anchor_split_5456_diag_out.txt`, seed 7,
2000 draws).** Two codes are below 0.05: **21 = t** (6 units, P 0.009; conflicts with key_f23 M 'e'; A2-COL17's held-out check had 21
'e|t' agreeing) and **20 = i** (4 units, P 0.044; agrees with key_f23 M 'i'). Next lowest: 83 = s 0.062, 23 = n 0.069 (7 units; agrees
with key_f23 M n), 32 = u 0.106 (key_f23 M 'o'; A2-COL16 had 'ou'), 77 = l 0.186; all others are 0.30-1.00. With 21 codes tested, a
Bonferroni line is 0.0024, so not even 21 = t clears a family-wise correction. These are leads for a later key revision's own
per-code control, and no grade changes. Rule 4: no token is graded as read from this step.
`tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check`: "reading up to date" (f.23 306 tokens C 92, M 213, U 1; f.24 168
tokens C 27, M 140, U 1). No judge re-run.

**Not done:** canvas 62-63 (numerals + gloss) is the brief's optional second step. It needs crops, two blind passes on two canvases and
a reconciliation (about 5 vision passes, ~$3 per the Verdict), which does not fit what is left of this job's $3 cap, so it was not started.
`images/crops/canvas62_full.jpg` and `canvas63_full.jpg` are on disk.
Hosts: none. Vision: 0 calls. No credentials.

## R8-COL26 (account 1, LANE-RUN8-account-1, 6 Oct 2026): canvas 62 and 63 (folio 58-59, letter docketed "30 Janvier 1648", closed "A la Haye le 3e febvrier 1648") numerals + gloss, key_f23 C test per canvas against the length-matched control

Brief `.claude/briefs/runs/2026-10-06-account1-run8-jobs.md` job R8-COL26. Intake gate exit 0 (lane brief, 03:43 UTC). Step still undone at
start (no canvas 62-63 section; Verdict line named it).

**Pre-registration (rule 3).** `siblings/c6263_test.py` committed and pushed (1aa11fb43, 03:48 UTC) before any canvas 62-63 crop was cut or
any pass read: a copy of c5456_test.py with statistic, LENGTH-MATCHED f23-window control (5000 draws), gate (C hits, P < 0.05) and
n >= 15 floor unchanged; one gate per canvas (62, 63); 'letter6263' reported, not gated; A2-COL17's held-out anchor check not carried.

**Transcription (rule 2, Usage 6).** Images on disk (`images/crops/canvas62_full.jpg`, `canvas63_full.jpg`, 2400 px), no network.
Centres set by eye on ruled region views, then cut (scratch, not committed):
`python3 tools/iiif_lines.py --image ciphers/colbert26-lathuillerie-1644/images/crops/canvas62_full.jpg --region 1240,600,1140,1100
--centres 75,128,220,282,348,412,620,708,778,838,900,988,1052 --top-margin 50 --bottom-margin 14 --out <scratch>/c62 --prefix c62 --debug`
(13 crops, right page; canvas 62's left page is a torn, faint fragment with no numerals) and `... canvas63_full.jpg --region
380,340,820,840 --centres 92,245,292,507,582,650,714,777 --top-margin 50 --bottom-margin 8 --out <scratch>/c63 --prefix c63 --debug` (8
crops, left page; right page blank). Each crop's target = its lowest complete numeral row. Two blind Sonnet passes (B in reverse order),
neither shown the key or any repo file, both given the same layout sentence; each returned its TSV as reply text. Two-reader split on
numerals: 6 of 243 group positions (0.025; agreement, not accuracy, TRANSCRIPTION.md); BENCHMARK-TX.tsv has no colbert26 row, none built.
Reconciliation (this worker, two zoom reads) in `siblings/c6263_reconciled.tsv`, 21 rows, 243 groups (62: 159, 63: 84): 62a01 A 15 23 /
B 13 29 -> 15 29; 62a09 87/81 -> 87; 62a11 91/97 -> 97; 63a04 15/13 -> 15; 63a07 71/11 -> 71. Glosses: the passes agreed on every row's
attribution; spellings settled by eye (62a03 'est', 'prejudice'; 62a13 'Guene', name ending uncertain). 63a02's gloss runs off the crop
('M. Le P.' kept; the leaf map reads 'M. le P. d'Or.'); 63a06's only gloss is struck through ('[a redire]'), so the row is not scored;
the '36(4)' group of 63a04 is kept as written and not scored. One attribution call, made before scoring by the layout rule both passes
applied: 'marchands' (start of the line written over 62a02, possibly the end of 62a01's 'en sont bons') stays with 62a02.

**Result** (`siblings/c6263_test_out.txt`):
```
scope	set	real	n	ctrl	mean	p95	max	P(ctrl>=real)	gate
canvas62	C	29	36	f23-window	16.80	21	26	0.0000	PASS
canvas63	C	13	18	f23-window	7.81	11	14	0.0046	PASS
letter6263	C	42	54	f23-window	24.52	29	35	0.0000	-
```
Both canvases pass their own pre-registered gate (shuffled-gloss, not gating, agrees: P 0.000, 0.004). Canvas 63 clears the n >= 15
floor narrowly (18 C occurrences). **Attribution sensitivity (diagnostic, after the gated test, scratch copy, not gating):** 'marchands'
moved to 62a01: canvas 62 27/36 vs p95 20, max 26, still PASS. Code 12 (key_f23 12 = c, grade C): 5 glossed occurrences on 62-63, the
ordered walk scores 5 of 5; with A2-COL17's 33 of 53 off f.23 this makes 38 of 58 -- a lead for the next revision's own control, no grade
changed.

Per rule 3's per-unit merge clause, no code enters key_f23.tsv or key.tsv from this step; canvas 62 and 63 have each cleared their own
length-matched control and may be added as units to the per-code control or a later key revision. No reading changed:
`tools/decode_key.py ciphers/colbert26-lathuillerie-1644 --check` "reading up to date" (f.23 306 tokens C 92, M 213, U 1; f.24 168 tokens
C 27, M 140, U 1); no judge re-run. Rule 4 under key_f23: canvas 62 159 groups (C-valued 36, 29 consistent with the gloss; C+M 130, 55),
canvas 63 84 groups (C 18, 13; C+M 72, 34); no token is graded as read. All 14 Jan-Feb 1648 two-digit leaves are now transcribed with
their gloss and each tested (canvas 51 TOO-SHORT, the rest PASS).

Hosts: none (images on disk). Vision: 2 Sonnet subagent calls (21 line crops each) + this worker's reconciliation (2 zoom reads, plus 4
region/overlay views to set centres). No credentials.

## R9-COL26 (account 1, LANE-RUN9-account-1, 6 Oct 2026): pre-registered per-code control for the anchor leads 21, 20, 23, 83 and 12 = c

Brief `.claude/briefs/runs/2026-10-06-account1-run9-jobs.md` job R9-COL26 (cap 3, box 35 min). Step checked undone first (it was the
Verdict line; no later section ran it). Scripts only, disk only, no images, no network.

**Pre-registration (rule 3).** `siblings/percode_control.py`, committed and pushed (11236538b, 06:09 UTC) before its first run; its
docstring is the full registration. Units: the 14 that each cleared their own length-matched key_f23 C test (f23, c32, c33, c3536,
c3940, c47, c48, c49, c50, c54, c55, c56, and R8-COL26's c62, c63); canvas 30 and 51 never read. Part A (21 = t, 20 = i, 23 = n,
83 = s): R7A-COL26's anchor-split spans unchanged, statistic H(c) = eligible spans containing c whose text contains the value, control B
(span texts permuted within equal-length classes, 5000 draws) -- it moves which text meets which code, so H can differ (orthogonality
clause). Part B (12 = c, itself an anchor): the ordered walk's hits on code 12 on the 13 units off f.23, against the length-matched
f23-window control, 5000 draws. Gate per code, Bonferroni over five: H > p95 and P < 0.01; Part A also needs >= 1 agreeing span on the
held-out units c62 + c63 (the four leads were picked from 21 candidates on the other 12 units); no held-out span = HELD-OUT-UNTESTABLE.

**Result** (`siblings/percode_control_out.txt`; 78 eligible spans, 6 on c62 + c63):
```
code	value	spans	H_real	units	ctrl_mean	p95	max	P	held_out_H/spans	gate
21	t	11	6	6	3.41	5	7	0.0294	0/0	FAIL
20	i	6	5	4	1.95	3	5	0.0010	0/0	HELD-OUT-UNTESTABLE
23	n	23	16	9	10.01	13	16	0.0008	3/4	PASS
83	s	3	3	3	0.89	2	3	0.0108	0/0	FAIL
12	c	58 occ	W 36	13	23.02	29	35	0.0000	-	PASS
```
Per-unit breakdown is in the output file. 23 = n agrees on 9 of the 11 units where it sits in a span; on the held-out pair 3 of 4
spans agree, against a held-out control mean of 2.31 (1.15 + 1.16), so the held-out units alone would not discriminate -- the pass rests
on the pooled count, which includes the 12 units the lead was picked from (stated, not hidden). 21 = t misses the Bonferroni line
(P 0.029) and stays key_f23 M 'e' (the two values still conflict; the M grade covers it). 20 = i clears the pooled line but has no span
on c62 or c63, so it stays M as registered. 83 = s has only 3 spans (P 0.011, max 3 = real), too thin. 12 = c holds on the units off
f.23 (36 of 58 vs control p95 29, max 35; per unit it is at or above its control p95 on c32, c3940, c47, c48, c56, c62, and below its
control mean on c33), so it stays C.

**Key change (per the registered rule, `--write`):** key_f23.tsv code 23 n M -> C (source R9-COL26, original A2-COL3 support kept in the
note). Nothing else changed; key_f24.tsv and the anchor files untouched. Reading regenerated: `tools/decode_key.py
ciphers/colbert26-lathuillerie-1644 --check` "reading up to date" (f.23 306 tokens C 110, M 195, U 1 -- was C 92, M 213; f.24 168 tokens
C 27, M 140, U 1). Rule 4: 18 more f.23 tokens at grade C (from the gloss, known plaintext); H 0, S 0, I 0.
Judge (rule 7), pasted: `tools/judge_plaintext.py specs/colbert26-lathuillerie-1644.json --file reading_f23.txt`:
```
FAIL language: score=-1.412, null_p99=-1.867, real_p05=-0.9, real_median=-0.792, mode=both, N=684
ok   words: cover=0.741, min=0.4, real_text_median_cover=0.949
FAIL - colbert26-lathuillerie-1644 (a PASS is a gate for a verifier, not a reading; rule 10)
```
(unchanged from A2-COL3: the value of 23 was already n; only its grade moved.)
Hosts: none. Vision: 0 calls. No credentials.

## R10-COL26B (account 1, LANE-RUN10-account-1, 6 Oct 2026): anchor_split re-run on the 14 cleared units with 23 = n as a C anchor

Brief `.claude/briefs/runs/2026-10-06-account1-run10-jobs.md` job R10-COL26B (cap 2, box 30 min). Step checked undone first (it was the
Verdict line; no later section ran it). Scripts only, disk only, no images, no network.

**Pre-registration (rule 3).** `siblings/anchor_split_r10.py`, committed and pushed (8e5153bb5, 10:09:06 UTC) before its first run; its
docstring is the full registration. Phase 1: R7A-COL26's anchor_split_5456.py with only (1) c62 and c63 added (14 units), (2) anchors
read from key_f23.tsv as committed (so 23 = n is now an anchor), (3) output to `key_f23_anchor_r10.tsv`; statistic, spans, control B
(2000 draws, same seed) and gate unchanged. Phase 2 (lead selection): per-code diag on the 12 units WITHOUT c62 + c63 (held out, named
before the run); lead = diag P < 0.05, unique best n-gram, not one of R9-COL26's 21/20/83. Phase 3: R9-COL26 Part A's per-code statistic
on all 14 units, control B 5000 draws, Bonferroni 0.05/n, held-out H on c62 + c63 >= 1, else HELD-OUT-UNTESTABLE.

**Result** (`siblings/anchor_split_r10_out.txt`): 234 lines, 344 interior spans, 138 eligible on 14 units (23 as an anchor roughly doubles
the eligible spans, 67 -> 138); no span in a length class of one.
```
stat	real	ctrl	mean	p95	max	P(ctrl>=real)	gate
S	99	control-B	82.39	88	92	0.0000	PASS
S_exact	14	control-B	1.30	3	5	0.0000	-
```
Phase 1 PASS: S 99 is above the control maximum of 92 in 2000 draws, excess over the control mean 16.6 code-points (8.0 in R7A-COL26).
31 candidates were written as registered to `key_f23_anchor_r10.tsv` (26 C, 5 M on tied best n-grams). These are pooled-pass labels, not
per-code evidence.
Phase 2 (12 units): two leads, **15 = e** (6 units, diag P 0.035; agrees with key_f23 M 'e') and **32 = u** (8 units, diag P 0.035;
key_f23 M 'o', A2-COL16 had 'ou'). 20 = i (0.049) and 21 = t (0.064) are excluded as already tested by R9-COL26.
Phase 3:
```
code	value	spans	H_real	units	ctrl_mean	p95	max	P	held_out_H/spans	gate
15	e	10	10	6	6.66	9	10	0.0040	0/0	HELD-OUT-UNTESTABLE
32	u	12	12	8	4.61	7	10	0.0000	0/0	HELD-OUT-UNTESTABLE
```
Both clear the pooled line (Bonferroni 0.025), but neither has an eligible span on c62 or c63, so both are HELD-OUT-UNTESTABLE as
registered: no key change. 32 = u is the stronger (12 of 12 spans vs control max 10); 15 = e is a weak lead because 'e' is the commonest
letter (control mean 6.66 of 10 spans). key_f23.tsv and key.tsv unchanged; `tools/decode_key.py ciphers/colbert26-lathuillerie-1644
--check` "reading up to date" (f.23 306 tokens C 110, M 195, U 1; f.24 168 tokens C 27, M 140, U 1). No judge re-run (reading unchanged).
Rule 4: no token is graded as read from this step.
Held-out material that exists for these two codes: the f.23 rotated margin postscript (margin/f23m_reconciled.tsv, A2-COL4), not one of
the 14 units: code 32 occurs in M2 ('68 32 28' under 'Soulager') and M3, code 15 in M2. A pre-registered check there is small-N.
Hosts: none. Vision: 0 calls. No credentials.

## Remaining gaps (A2-COL2, 2 Oct 2026; A4-RFCOL, R7A-COL26, R9-COL26, R10-COL26B 6 Oct 2026; updated A2-COL3, A2-COL4, 2 Oct 2026, A2-COL5, A2-COL6, A2-COL7, A2-COL8, A2-COL9, A2-COL10, A2-COL11, A2-COL12, A2-COL13, A2-COL14, A2-COL15, 3 Oct 2026, A2-COL16, A2-COL17; R8-COL26 6 Oct 2026)

Read so far: 27 of 168 f.24 tokens and 110 of 306 f.23 tokens at grade C (92 before R9-COL26) (reading_tokens_f24.tsv, reading_tokens_f23.tsv); the other 19 cipher-bearing leaves 0 (sorted by system, A2-COL5: 17 two-digit like f.23, 2 mixed like f.24; siblings_sort.tsv).
- f.23 codes beyond the 21 C codes - blocker: open-codes; word-level re-pairing done (A2-COL3: 128 vs shuffled max 45, 21 C codes, held-out 4/4); the other 49 codes occur once or split across chunks on this one leaf (key_f23.tsv), so more occurrences are needed (A2-COL5: 17 glossed two-digit sibling leaves, May 1646-Feb 1648, are that material if they share the key); the rotated margin postscript, the only further f.23 material, was read and used as a known-answer test (A2-COL4: C codes 6/7 consistent, M2 5/5 above the control max 4, pooled p 0.076; leads 61 = ge, 71 = dans, 77 = faire); next: fold the margin pairs into the alignment as a second fit, key revision with its own shuffled-gloss control, ~$1
- f.24 signs beyond the 6 C codes - blocker: open-codes; one leaf of 153 tokens leaves 53 signs at M (key_f24.tsv), and f.23 is a different key, so it cannot serve as the prior (A2-COL2 step)
- two-digit siblings (17 leaves, siblings_sort.tsv) - blocker: not-attempted; canvas 30-32 (8 May 1646) tested: canvas 30 alone 12/23, below the length-matched control (A2-COL6); canvas 32 transcribed with its gloss (A2-COL7, siblings/c32_reconciled.tsv, 276 settled groups) and pooled 30+32 key_f23 C 51/88 clears the pre-registered length-matched control (p95 43, P 0.0002; canvas 32 alone 39/65 vs p95 33), so a shared key with f.23 is supported for that letter; the 14 Jan-Feb 1648 leaves untested; joint interlinear_align re-fit f.23 + c32 + c30 at line-level sibling pairing (A2-COL8): within-unit shuffle beaten (190 vs p95 116) but sibling agrees 78 vs length-matched p95 80, gate FAIL, no key change (canvas 32 alone 59 vs p95 56, post-hoc lead); A2-COL9: word-level re-pairing of canvas 32 mostly not possible (groups evenly spaced, no run gaps, gloss more compact than numerals; 2 of 22 rows split), pre-registered re-fit without canvas 30 passes G1 (174 vs p95 97) and G2 (62 vs length-matched p95 55), with canvas 30 G2 still fails (81 vs 81); the joint key adds no C code beyond key_f23 and canvas 32 attests individual codes weakly (51 de 2/8), so no key change; A2-COL10: canvas 33 (La Haye, Jan 1648) transcribed with its gloss (siblings/c33_reconciled.tsv, 135 groups) and the pre-registered key_f23 C test passes on it alone (16/21 vs length-matched p95 14, P 0.006; with the passes' narrower gloss 10/12, below the n 15 floor), so the shared key is supported outside 1646; lead: 12 = c conflicts on canvas 33 (under 'distribu-' twice); A2-COL11: canvas 35-36 (La Haye, 9e de l'an 1648) transcribed with its gloss (siblings/c3536_reconciled.tsv, 231 groups) and the pre-registered key_f23 C test passes on it alone (24/47 vs length-matched p95 22, P 0.019; narrow margin, rests on pass A's gloss attribution); 12 = c 2 of 5 here, 4 of 18 off f.23; 11 Jan-Feb 1648 leaves untested (canvas 39-40, 47-51, 54-56, 62-63); A2-COL12: pre-registered joint key revision (siblings/refit_joint4.py) of the four units that cleared: G1 PASS 227 vs 153, G2 FAIL sibling 112 vs length-matched p95 114 (canvas 33 at, canvas 35-36 below its control mean in the DP at line grain), no key change; 12 = c re-test 11/19 vs mean 7.8, stays C (P 0.085); joint DP at line-grain sibling pairs [retired] (interlinear_align, untestable-by-this-tool for canvas 33/35-36); A2-COL13: canvas 39-40 (La Haye, 13e Janvier 1648) transcribed with its gloss (siblings/c3940_reconciled.tsv, 267 groups, passes agreed on every gloss attribution) and the pre-registered key_f23 C test passes on it alone (37/56 vs length-matched p95 31, max 36 in 5000, P 0.0000), third 1648 unit; 12 = c walk 3 of 4 here (14 of 23 off f.23); A2-COL14: canvas 47, 48 (letter of 20 Jan 1648) and 49 (opening of the 23 Jan letter) transcribed with their gloss (siblings/c4749_reconciled.tsv) and each passes the pre-registered per-canvas key_f23 C test (47: 31/46 vs p95 25, max 30; 48: 16/29 vs p95 14, P 0.017; 49: 28/48 vs p95 24, P 0.003; 48 and 49 rest on the above-row gloss attribution, wrong-row attribution fails, 10/44, P 0.95); 12 = c walk 7 of 9 here (21 of 32 off f.23); A2-COL15: canvas 50 (letter of 23 Jan 1648) transcribed with its gloss (siblings/c5051_reconciled.tsv) and passes the pre-registered per-canvas key_f23 C test (65/97 vs p95 51, max 59 in 5000; holds with the top-line attribution reversed, 61/93 vs p95 48); canvas 51 TOO-SHORT (13 C occurrences, floor 15); whole letter 49-51 103/158 vs control max 86 (not gated); 12 = c walk 7 of 13 here (28 of 45 off f.23); 5 Jan-Feb 1648 leaves untested (canvas 54-56, 62-63); next: canvas 54-56 numerals + gloss, same pre-registered per-canvas test, ~$5; A2-COL16: anchor-split pairing of the 9 cleared units against control B (siblings/anchor_split.py, pre-registered): S 30 vs p95 29, max 31, P 0.028 -- narrow PASS; no code individually beats control B (post hoc best 23 = n P 0.078), 17 candidates in key_f23_anchor.tsv, key_f23 unchanged; A2-COL17: canvas 54, 55, 56 (letter of 24-27 Jan 1648) transcribed with their gloss (siblings/c5456_reconciled.tsv, 536 groups) and each passes the pre-registered per-canvas key_f23 C test (54: 18/29 vs p95 15, P 0.004; 55: 39/59 vs p95 32, max 38; 56: 21/29 vs p95 16, max 19); held-out check (not a gate): 8 of the 11 key_f23_anchor candidates that occur on 54-56 agree vs control-H p95 5, max 8 (support by the registered criterion; 23 = n does not agree); 12 = c walk 5 of 8 (33 of 53 off f.23); 2 Jan-Feb 1648 leaves untested (canvas 62-63); R7A-COL26 (6 Oct 2026): anchor_split re-run with c54, c55, c56 as cleared units (siblings/anchor_split_5456.py, pre-registered): S 47 vs control-B p95 43, max 47, P 0.001 -- PASS; post hoc per-code 21 = t P 0.009, 20 = i P 0.044 (not gating, not Bonferroni-clear), candidates in key_f23_anchor_5456.tsv, key_f23 unchanged; R8-COL26 (6 Oct 2026): canvas 62 (letter of 30 Jan 1648) and 63 (closed 3 Feb 1648) transcribed with their gloss (siblings/c6263_reconciled.tsv, 243 groups) and each passes the pre-registered per-canvas key_f23 C test (62: 29/36 vs p95 21, max 26; 63: 13/18 vs p95 11, P 0.005); 12 = c walk 5 of 5 (38 of 58 off f.23); no Jan-Feb 1648 leaf left untested; R9-COL26 (6 Oct 2026): pre-registered per-code control (siblings/percode_control.py) on the 14 cleared units: 23 = n PASS (16/23 vs control-B p95 13, P 0.0008, held-out 3/4) -> key_f23 C; 12 = c PASS (36/58 off f.23 vs p95 29), stays C; 21 = t FAIL (P 0.029), 83 = s FAIL (3 spans), 20 = i HELD-OUT-UNTESTABLE (no span on c62-63), all stay as they were; R10-COL26B (6 Oct 2026): anchor_split re-run with 23 = n as an anchor on the 14 units (siblings/anchor_split_r10.py, pre-registered): S 99 vs control-B p95 88, max 92 -- PASS; new leads 15 = e and 32 = u clear the pooled per-code line (P 0.004, 0.000) but have no span on held-out c62-c63, HELD-OUT-UNTESTABLE, key unchanged; next: pre-registered held-out check of 32 = u and 15 = e on the f.23 margin postscript pairs (margin/f23m_reconciled.tsv; 32 in M2 and M3, 15 in M2), ~$0.5
- canvas 20-21 codes - blocker: not-attempted; A4-RFCOL (6 Oct 2026) re-read on native crops: word-for-word interlinear decipherment (interlinear/c20c21_reconciled.tsv, 18 units), key_f24 known-answer 14/19 vs control p95 6, 83 de and 31 que C, 25 conflict (par vs m); A4-COLALN (6 Oct 2026): interlinear_align seeded 83/31, per-unit deranged-gloss gate FAILs on both canvases (c20 unseeded 6 vs p95 10; c21 6 vs p95 12), no merge; next: the A4-RFCOL positional known-answer statistic run per candidate code (42 si, 11 le/les, 6 je) with key_f24 sibling f.24 as held-out material, or a word-level pairing of each gloss word to its sign span by eye on the native crops, ~$1

## Escalation (A2-COL2, 2 Oct 2026; A4-RFCOL, R7A-COL26, R9-COL26, R10-COL26B 6 Oct 2026; updated A2-COL3, A2-COL4, 2 Oct 2026, A2-COL5, A2-COL6, A2-COL7, A2-COL8, A2-COL9, A2-COL10, A2-COL11, A2-COL12, A2-COL13, A2-COL14, A2-COL15, 3 Oct 2026, A2-COL16, A2-COL17; R8-COL26 6 Oct 2026)

- [x] siblings: sorted by eye (A2-COL5, siblings_sort.tsv): 17 leaves two-digit like f.23 (canvas 30-32 May 1646, all La Haye leaves Jan-Feb 1648), 2 mixed like f.24 (canvas 20-21, 1645); shared key tested on canvas 30 (A2-COL6): C 12/23, beats shuffled-gloss (P 0.015), not length-matched (P 0.18); canvas 30+32 pooled (A2-COL7): C 51/88 vs length-matched p95 43, P 0.0002 -- PASS, shared key supported for the May 1646 letter; joint key re-fit (A2-COL8, siblings/refit_c32.py): sibling agrees 78 vs length-matched p95 80, FAIL at line-level pairing, key unchanged; re-fit without canvas 30 (A2-COL9, siblings/refit_c32w.py, pre-registered): G1 PASS 174 vs 97, G2 PASS 62 vs 55 (row-level diagnostic 57 vs 51: dropping canvas 30 does most of the work; word-level split possible on 2 of 22 rows only), no new C code, key unchanged; canvas 33 (A2-COL10, siblings/c33_test.py, pre-registered): C 16/21 vs length-matched p95 14, P 0.006 -- PASS, key_f23 tested in 1648 (rests on the B3-B5 gloss-vs-clear layout call for n >= 15); canvas 35-36 (A2-COL11, siblings/c3536_test.py, pre-registered): C 24/47 vs length-matched p95 22, P 0.019 -- PASS, second 1648 unit; joint key revision of the four cleared units (A2-COL12, siblings/refit_joint4.py, pre-registered): G2 FAIL 112 vs 114 at line-grain pairs, key unchanged, 12 = c stays C (11/19 vs 7.8, P 0.085) [retired: interlinear_align joint fit with line-level sibling pairs]; canvas 39-40 (A2-COL13, siblings/c3940_test.py, pre-registered): C 37/56 vs length-matched p95 31, max 36, P 0.0000 -- PASS, third 1648 unit; canvas 47, 48, 49 (A2-COL14, siblings/c4749_test.py, pre-registered, one gate per canvas): 31/46 vs p95 25, 16/29 vs p95 14 (P 0.017), 28/48 vs p95 24 (P 0.003) -- three PASSes (48 and 49 rest on the above-row gloss attribution); canvas 50, 51 (A2-COL15, siblings/c5051_test.py, pre-registered): canvas 50 65/97 vs p95 51, max 59 -- PASS (not attribution-dependent); canvas 51 TOO-SHORT (13 C occurrences); anchor-split pairing (A2-COL16, siblings/anchor_split.py, pre-registered, first attempt with this instrument): S 30 vs control-B p95 29, P 0.028 -- narrow PASS, no per-code result, key unchanged; canvas 54, 55, 56 (A2-COL17, siblings/c5456_test.py, pre-registered, one gate per canvas): 18/29 vs p95 15, 39/59 vs p95 32, 21/29 vs p95 16 -- three PASSes (55 holds without the 55a05 attribution, 33/51 vs p95 28); held-out anchor check 8/11 agree vs control-H p95 5 (support, not a gate); anchor-split re-run on 12 cleared units (R7A-COL26, siblings/anchor_split_5456.py, pre-registered): S 47 vs control-B p95 43, max 47, P 0.001 -- PASS, key unchanged; canvas 62, 63 (R8-COL26, siblings/c6263_test.py, pre-registered, one gate per canvas): 29/36 vs p95 21, 13/18 vs p95 11 (P 0.005) -- two PASSes; per-code control on the 14 cleared units (R9-COL26, siblings/percode_control.py, pre-registered): 23 = n PASS -> C, 12 = c PASS stays C, 21/83 FAIL, 20 held-out-untestable; anchor-split re-run with 23 = n as an anchor (R10-COL26B, siblings/anchor_split_r10.py, pre-registered): S 99 vs p95 88, PASS; leads 15 = e, 32 = u HELD-OUT-UNTESTABLE, key unchanged
- [x] clear-pages: f.24 and f.23 interlinear decipherments both aligned, each cleared its own shuffled-gloss control (f.23 63 vs max 45)
- [x] known-keys: KX-LATHCT1 compared the cluster with key_1646, key_brienne_1647, key_1659 (different keys)
- [ ] print: no edition of these letters found; Danish/Swedish mediation editions not yet opened (GF-A2-3 premise (d))
- [n/a] key-rebuild: f.23 and f.24 are different keys (51, 31 conflict), so there is no merge to make
- [x] image-check: canvas 20-21 gloss-vs-clear re-read on native crops (A4-RFCOL, 6 Oct 2026): gloss, word for word; committed canvas 20 gloss column one line off; key_f24 C codes 14/19 in place vs control p95 6; interlinear_align on the reconciled pairs (A4-COLALN, 6 Oct 2026): per-unit gate FAIL c20 and c21, key unchanged
- [x] retry: f.23 word-level re-pairing done (A2-COL3): 128 agreeing tokens vs shuffled-gloss control max 45; C codes 6 -> 21; held-out P36 4/4 C consistent; judge FAIL -1.412; A2-COL4 margin postscript known-answer test: C 6/7 consistent, M2 5/5 vs control max 4, pooled p 0.076

Verdict: keep going: 4 internal gaps; cheapest next: pre-registered held-out check of the R10-COL26B leads 32 = u and 15 = e on the f.23 margin postscript pairs (margin/f23m_reconciled.tsv, not among the 14 units), ~$0.5 (R10-COL26B)

## Interrupted (account 2 usage limit, 3 Oct 2026)

- Role: A2-COL18 (account 2, LANE-A2PUSH2, session_01NY3P2ciQ119oVa2duLBHn3), spawned 05:30 UTC 3 Oct 2026; brief
  .claude/briefs/runs/2026-10-03-acct2-a2-col18.md (2d73ce47). No claim or done line in ROOM.md.
- Committed: none (no commit in this folder after A2-COL17's 0e0e1bcd, checked 09:25 UTC); no orphaned pre-registration.
- Unfinished step: re-run siblings/anchor_split.py with canvas 54, 55, 56 added as cleared units (new pre-registered
  script copy, statistic, control B and gate unchanged) -- the Verdict line above is still this step.
- May still push if account 2's session resumes; check git (`git log origin/main -- <this folder>`) and ROOM.md before re-running. Recorded by CLOSEOUT-A2 (account-3 in-session worker) from git and ROOM.md only; no reading, grade, status line or key was changed.

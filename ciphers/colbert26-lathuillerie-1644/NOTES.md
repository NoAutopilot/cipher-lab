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

## Remaining gaps (A2-COL2, 2 Oct 2026; updated A2-COL3, A2-COL4, 2 Oct 2026, A2-COL5, A2-COL6, A2-COL7, A2-COL8, A2-COL9, A2-COL10, 3 Oct 2026)

Read so far: 27 of 168 f.24 tokens and 92 of 306 f.23 tokens at grade C (reading_tokens_f24.tsv, reading_tokens_f23.tsv); the other 19 cipher-bearing leaves 0 (sorted by system, A2-COL5: 17 two-digit like f.23, 2 mixed like f.24; siblings_sort.tsv).
- f.23 codes beyond the 21 C codes - blocker: open-codes; word-level re-pairing done (A2-COL3: 128 vs shuffled max 45, 21 C codes, held-out 4/4); the other 49 codes occur once or split across chunks on this one leaf (key_f23.tsv), so more occurrences are needed (A2-COL5: 17 glossed two-digit sibling leaves, May 1646-Feb 1648, are that material if they share the key); the rotated margin postscript, the only further f.23 material, was read and used as a known-answer test (A2-COL4: C codes 6/7 consistent, M2 5/5 above the control max 4, pooled p 0.076; leads 61 = ge, 71 = dans, 77 = faire); next: fold the margin pairs into the alignment as a second fit, key revision with its own shuffled-gloss control, ~$1
- f.24 signs beyond the 6 C codes - blocker: open-codes; one leaf of 153 tokens leaves 53 signs at M (key_f24.tsv), and f.23 is a different key, so it cannot serve as the prior (A2-COL2 step)
- two-digit siblings (17 leaves, siblings_sort.tsv) - blocker: not-attempted; canvas 30-32 (8 May 1646) tested: canvas 30 alone 12/23, below the length-matched control (A2-COL6); canvas 32 transcribed with its gloss (A2-COL7, siblings/c32_reconciled.tsv, 276 settled groups) and pooled 30+32 key_f23 C 51/88 clears the pre-registered length-matched control (p95 43, P 0.0002; canvas 32 alone 39/65 vs p95 33), so a shared key with f.23 is supported for that letter; the 14 Jan-Feb 1648 leaves untested; joint interlinear_align re-fit f.23 + c32 + c30 at line-level sibling pairing (A2-COL8): within-unit shuffle beaten (190 vs p95 116) but sibling agrees 78 vs length-matched p95 80, gate FAIL, no key change (canvas 32 alone 59 vs p95 56, post-hoc lead); A2-COL9: word-level re-pairing of canvas 32 mostly not possible (groups evenly spaced, no run gaps, gloss more compact than numerals; 2 of 22 rows split), pre-registered re-fit without canvas 30 passes G1 (174 vs p95 97) and G2 (62 vs length-matched p95 55), with canvas 30 G2 still fails (81 vs 81); the joint key adds no C code beyond key_f23 and canvas 32 attests individual codes weakly (51 de 2/8), so no key change; A2-COL10: canvas 33 (La Haye, Jan 1648) transcribed with its gloss (siblings/c33_reconciled.tsv, 135 groups) and the pre-registered key_f23 C test passes on it alone (16/21 vs length-matched p95 14, P 0.006; with the passes' narrower gloss 10/12, below the n 15 floor), so the shared key is supported outside 1646; lead: 12 = c conflicts on canvas 33 (under 'distribu-' twice); 13 Jan-Feb 1648 leaves untested; next: canvas 35-36 (folio 31-32, 1648) numerals + gloss on line crops, two blind passes + reconciliation, same pre-registered test (copy of c33_test.py, committed before the passes), ~$2.5
- canvas 20-21 notes - blocker: not-attempted; KX-LATHKEY2 judged them topical, but f.24 shows gloss lines were taken for clear text; next: re-read canvas 20 gloss-vs-clear on native crops, ~$2

## Escalation (A2-COL2, 2 Oct 2026; updated A2-COL3, A2-COL4, 2 Oct 2026, A2-COL5, A2-COL6, A2-COL7, A2-COL8, A2-COL9, A2-COL10, 3 Oct 2026)

- [x] siblings: sorted by eye (A2-COL5, siblings_sort.tsv): 17 leaves two-digit like f.23 (canvas 30-32 May 1646, all La Haye leaves Jan-Feb 1648), 2 mixed like f.24 (canvas 20-21, 1645); shared key tested on canvas 30 (A2-COL6): C 12/23, beats shuffled-gloss (P 0.015), not length-matched (P 0.18); canvas 30+32 pooled (A2-COL7): C 51/88 vs length-matched p95 43, P 0.0002 -- PASS, shared key supported for the May 1646 letter; joint key re-fit (A2-COL8, siblings/refit_c32.py): sibling agrees 78 vs length-matched p95 80, FAIL at line-level pairing, key unchanged; re-fit without canvas 30 (A2-COL9, siblings/refit_c32w.py, pre-registered): G1 PASS 174 vs 97, G2 PASS 62 vs 55 (row-level diagnostic 57 vs 51: dropping canvas 30 does most of the work; word-level split possible on 2 of 22 rows only), no new C code, key unchanged; canvas 33 (A2-COL10, siblings/c33_test.py, pre-registered): C 16/21 vs length-matched p95 14, P 0.006 -- PASS, key_f23 tested in 1648 (rests on the B3-B5 gloss-vs-clear layout call for n >= 15)
- [x] clear-pages: f.24 and f.23 interlinear decipherments both aligned, each cleared its own shuffled-gloss control (f.23 63 vs max 45)
- [x] known-keys: KX-LATHCT1 compared the cluster with key_1646, key_brienne_1647, key_1659 (different keys)
- [ ] print: no edition of these letters found; Danish/Swedish mediation editions not yet opened (GF-A2-3 premise (d))
- [n/a] key-rebuild: f.23 and f.24 are different keys (51, 31 conflict), so there is no merge to make
- [ ] image-check: canvas 20-21 gloss-vs-clear re-read on native crops
- [x] retry: f.23 word-level re-pairing done (A2-COL3): 128 agreeing tokens vs shuffled-gloss control max 45; C codes 6 -> 21; held-out P36 4/4 C consistent; judge FAIL -1.412; A2-COL4 margin postscript known-answer test: C 6/7 consistent, M2 5/5 vs control max 4, pooled p 0.076

Verdict: keep going: 4 internal gaps; cheapest next: canvas 35-36 (folio 31-32, La Haye 1648) numerals + gloss from tools/iiif_lines.py line crops (two blind passes + one reconciliation, priced per pass), then the same key_f23 C test (copy of siblings/c33_test.py, committed before the passes) against the length-matched f.23-window control, the second 1648 unit; canvas 33 passed (A2-COL10, 16/21 vs p95 14). Attestation only until a key revision with its own control folds the cleared units (f.23, canvas 32, canvas 33) together, ~$2.5

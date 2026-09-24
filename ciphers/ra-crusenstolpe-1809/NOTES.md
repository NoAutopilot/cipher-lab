# ra-crusenstolpe-1809

Status: open

## What this is

Spy reports and cipher documents concerning the 1809 revolution (the coup against Gustav IV Adolf), held among
the papers of Magnus Jakob Crusenstolpe (1795-1865). Riksarkivet i Stockholm/Täby, Ericsbergsarkivet, "Smärre
enskilda arkiv och arkivfragment / Crusenstolpe-papper", reference code `SE/RA/720266/03/08/~/2,5`. Catalogue
note (verbatim): "Ink brev och skrivelser, diverse utkast och anteckningar m m. Spionrapporter, chiffer
handlingar rörande revolutionen 1809." Crusenstolpe was 14 in 1809 and a well-known later writer/censor/
politician; the note describes material *about* 1809 gathered in his papers, not necessarily material *by* him,
and does not attribute authorship of the cipher documents themselves. QUEUE.md row R6.

No transcription exists anywhere the searches below reached; `ciphertext.txt` is not created.

## Check-solved sweep, 24 September 2026

1. **Web.** WebSearch `"Crusenstolpe 1809 revolutionen chiffer spionrapporter Riksarkivet"`. Hits: Crusenstolpe's
   Svenskt Biografiskt Lexikon entries, the Ericsberg-palace/Ericsbergsarkivet Wikipedia and Nättidningen Svensk
   Historia pages, a Historisk tidskrift PDF on "märkesåret 1809", and the English Wikipedia "Coup of 1809"
   article. All confirm Crusenstolpe was "one of the most active forces in Gustav IV Adolf's deposition in
   1809" (his biographical fact, already well known) but none names or quotes this specific bundle of spy
   reports or cipher documents. Not found.
2. **Print — Crusenstolpe's own published works.** Crusenstolpe's own document collection "Portefeuille,
   utgifven af författaren till Skildringar ur det inre af dagens historia" (parts 1-4, 1837-1844, plus
   "Portefeuille, belysande det inre af tidernas historia", 1840) is a printed primary-source collection, full
   text on Project Runeberg (`runeberg.org/portef/`). It was not read cover-to-cover this pass — that is an
   edition-search job for a solver/verifier, not this check-solved sweep — but its existence is recorded as the
   standing candidate for a facing-page/interlinear check if this target is ever promoted: whether the specific
   cipher documents in `SE/RA/720266/03/08/~/2,5` were themselves printed (deciphered or in cipher) in
   Portefeuille is unresolved and flagged as a next step, not closed either way.
3. **Print — Swedish 1809 historiography.** Not separately searched by name (Odhner, Hjärne, Almqvist, etc.) —
   out of scope for a check-solved pass's budget; flagged as the same open next step as (2), one edition search,
   not run here.
4. **Lists.** `sources/cryptiana/` grepped for `crusenstolpe|1809`: no relevant hits (a `1809`-adjacent false
   positive in an unrelated file was checked and is not about this item). Live community-list sites not
   separately fetched (same reasoning as ra-morner-welin: the local snapshot is the productive check and
   returned nothing for a name this specific).
5. **DECODE.** `sources/decode/` grepped for `crusenstolpe`: no hits. Live de-crypt.org not queried this pass.
6. **Bourdeau/Aymeloglu.** Same fresh shallow clones as ra-morner-welin. `grep -n -i "crusenstolpe"` against both
   repos' `README.md`/`TARGETS.md`/`SOLVED_CATALOGUE.md`/`SHORTLIST.md`/`CATALOGUE.md`: no matches. A
   repo-wide grep for "1809" alone returned only unrelated numeric/data-file false positives (napoleon-era
   digit files, glyph-segmentation JSON, etc.), none naming Crusenstolpe or this shelfmark. Not found.

**Riksarkivet digitisation check** (`data.riksarkivet.se/api/records`, `text=Crusenstolpe chiffer`, one request):
confirms the record at `SE/RA/720266/03/08/~/2,5` with `"onlyDigitisedMaterials":false` and reproduces the
catalogue note above verbatim. Not digitised.

## Verdict

**Open.** No source located a solution, key, plaintext, transcription or documented attempt specific to this
item. Unlike ra-morner-welin, this row carries a real, unclosed edition risk: Crusenstolpe's own printed
Portefeuille collection and the general Swedish 1809-coup historiography have not been searched for this
material, only judged out of scope for this pass's budget. **Before any campaign or promotion past stage 2, run
that edition search** (Portefeuille full text on runeberg.org, plus a named search of the standard 1809
historiography) — this is exactly the Raince/Thurloe-lesson gap the brief and CLAUDE.md rule 1 warn about, left
open rather than silently closed.

Copy-order (not digitised). REQUEST.md below drafts the Riksarkivet reading-room request.

Requests this pass: data.riksarkivet.se 1, WebSearch 1, github.com clones shared with the batch (grepped only),
sources/cryptiana and sources/decode local grep only. No Google Books, no TNA, no DECODE login.

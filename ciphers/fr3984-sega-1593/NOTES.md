blocked (fr.3984 nos.6, 8, 88, 90); found-solved (fr.3985 no.7)

**LANE N3 csCS2c, 24 Sept 2026 (session_0113dPptSGXZiBF5uwvtKmtc):** fr.3985 no.7 confirmed against the Gallica
leaf and split off below ("Leaf check confirms found-solved: fr.3985 no.7"). The four fr.3984 items are
unaffected and stay `blocked`.

**LANE N3 orchestrator, 24 Sept 2026 16:34 UTC:** status corrected from `partial` (csED2) to `blocked`: `partial` in this repo means a partial reading, and nothing here is read. The four fr.3984 items stay blocked on Acta Nuntiaturae Gallicae (Sega legation, not reachable). fr.3985 no.7 is a probable `found-solved`: Mémoires de la Ligue (Goujet 1758) vol.5 pp.411-414 prints a Mauclerc-to-Creil letter of 4 Aug 1593 matching its correspondents and date; confirm against the Gallica leaf (a verifier or image check, not a solver) before splitting it off.

**Edition check (LANE N3 csED2, 24 Sept 2026 16:17 UTC):** fr.3985 no. 7 (Mauclerc to Creil) has a strong print
match -- see section below, "possible found-solved: fr.3985 no. 7." The four fr.3984 items (Baudouin-Desportes)
stay `blocked`: the named edition (Acta Nuntiaturae Gallicae, Sega legation) is a modern critical series not
digitised on archive.org (0 hits for "acta nuntiaturae gallicae" in title, checked 24 Sept 2026) or found on
HathiTrust. Brief `.claude/briefs/runs/2026-09-24-lane-n3-csED2.md`.

# Papal-side letters of the week of Henri IV's abjuration, 14 May - 4 Aug 1593 — BnF fr. 3984 nos. 6, 8, 88, 90; fr. 3985 no. 7

QUEUE row: CS2-04 (`sources/solver-diffs/2026-09-24-cyphersolver-site.tsv`, LANE N3 scout scCS2, 24 September
2026 — catalogue item 20 at dbourdeau.github.io/cyphersolver/catalogue.html). Check-solved run 24 September 2026
by LANE N3 csCS2a (session_01JrahDoApcsEHgiQigjaJPY), brief `.claude/briefs/runs/2026-09-24-lane-n3-csCS2a.md`.

Sender(s): Baudouin-Desportes (to Pope Clement VIII, to Pietro Aldobrandini, to Girolamo Frachetta), and
Mauclerc (to Creil), written in the week around Henri IV's abjuration (25 July 1593) and the truce of Suresnes.
Catalogued nos. 6, 8, 88 (f.186), 90 (f.189) in BnF fr. 3984, and no. 7 in fr. 3985.

## Six-source search log (24 September 2026)

1. **Tomokiyo (sources/cryptiana/ on disk).** `nevers.htm` (local snapshot) documents the same "League
   polyphonic" cipher used across this fr. 3983-3986 run of volumes, but for *different* correspondents bound in
   the same books (Duke of Mayenne to Commander de Diou, 13 May 1593, fr.3984 f.7; Nicolas Brulart de Sillery to
   Duke of Nevers, 25 July 1593, fr.3984 f.198; Gondy to Nevers letters in fr.3983/3986/3988) -- not the same
   items as nos. 6/8/88/90/no.7. `savoy.htm` documents a *third*, unrelated correspondence bound in the same
   physical volumes (Ambassador Lebel to the Duke of Savoy, using fr.3983/3984/3985, including fr.3984 f.182 and
   fr.3985 f.23) -- again a different sender/cipher, not this item. Tomokiyo's *mayenne.htm* ("A Polyphonic
   Substitution Cipher of the Catholic League, 1592-1593", per Bourdeau's citation below) is the article that
   actually covers this specific Baudouin-Desportes correspondence and gives the reconstructed key; not
   independently re-fetched this pass (Bourdeau's quote of it, below, is taken as read). No sentence located
   anywhere claiming these four folios (nos. 6/8/88/90, fr.3984) or fr.3985 no.7 are deciphered.
2. **Standard printed edition / calendar for the date.** Not located or read this pass: no printed edition of
   the League/nunciature correspondence for this exact week was identified or checked (the papal nunciature
   series for 1593 France, named in this row's brief, was not reached -- flagged below). **This gate is not
   met, so the verdict is `blocked`, not `open`, per the check-solved brief's rule 9.**
3. **Lasry's publications.** No Lasry solution of this correspondence found.
4. **DECODE (sources/decode/ on disk) + both solver-repo clones.** No DECODE record for fr.3984/fr.3985 in the
   local snapshot. dbourdeau/cyphersolver (shallow clone, 24 Sept 2026) has a dedicated working folder,
   `sega1593/`, session of 17 September 2026, quoted in full since it is the most current and detailed source:
   *"Outcome: **not read**. The key is known (Tomokiyo's League polyphonic cipher), the deciphered sibling is
   aligned glyph by glyph, but the two target letters are c. 5,000 hand-drawn glyphs whose classes a classifier
   trained on the sibling reads at 75-79%, and the polyphonic decoder needs better than 90%. The item is closed
   as *not solvable with the present tools*."* Detail: f.186 (no. 88, to Aldobrandini) and f.189 (no. 90, to
   Frachetta) are unread; f.184-185 and f.177 are the office's own contemporary decipherments of *sibling*
   letters (f.188, f.176) in the same hand and key -- so the key and a large labelled sample exist, but a CNN
   classifier trained on 597-718 aligned glyphs peaks at 73-79% top-1 accuracy, and end-to-end soft decoding of
   held-out lines recovers only 30-40% of letters, well short of readable text (25% class error becomes
   unreadable once a polyphonic layer collapses two letters per glyph). A crib search against the deciphered
   sibling found no verbatim-repeated line in either target letter. Explicitly unresolved: fr.3985 no. 7
   (Mauclerc to Creil) -- "fetched by the previous session but not examined here; the catalogue's 'no. 4
   deciphered' sibling claim is unverified." So no. 7 has not actually been checked against its claimed
   deciphered sibling by anyone yet. aaymeloglu/unsolved-ciphers: no hit for fr.3984/fr.3985 in this shallow
   clone. WebSearch corroborates the same Baudouin-Desportes/fr.3984 ff.186,189 read state, dated by Bourdeau to
   17 September 2026.
5. **Ciphertext confirmed present on the Gallica leaf.** IIIF fetches, gallica.bnf.fr, 24 Sept 2026, 2 requests:
   - `https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060633d/f347/full/500,/0/native.jpg` (fr.3984, canvas 347,
     Bourdeau's canvas-to-folio convention "canvas = folio - 26" for f.186/no.88 in this stretch): full page of
     dense polyphonic glyph cipher, matching the sega1593 description. Leaf:
     https://gallica.bnf.fr/ark:/12148/btv1b9060633d/f347.item
   - `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606498/f8/full/500,/0/native.jpg` (fr.3985, near no. 7):
     ordinary secretary-hand prose, dated "3 di agosto 1593" visible mid-page, no obvious cipher block on this
     specific canvas -- fr.3985's cipher passages are not necessarily on this exact folio; presence in the
     volume is otherwise well established by Bourdeau's own fetch of the same ark. Leaf:
     https://gallica.bnf.fr/ark:/12148/btv1b90606498/f8.item

## Verdict

**Blocked.** Six of six independent sources were checked as far as this budget allowed, and none claims a
decipherment of nos. 6/8/88/90 (fr.3984) or no. 7 (fr.3985) -- so this would otherwise score `open`. But per
this check-solved brief's rule 9 ("If the standard edition or calendar for the date cannot be located or read,
the verdict is `blocked`, never `open`"), the papal nunciature series for France 1593 (named explicitly in this
row's brief as the edition to check) was not located or read this pass, so the verdict is held at `blocked`
rather than promoted to `open`. **No ROOM nomination line is posted for this row** (per the brief: no
nomination without a stage-2 `open` verdict).

Separately and worth recording regardless of the edition gate: this is a genuinely hard cryptanalysis target
even with the key in hand and 1,100+ aligned training glyphs -- Bourdeau's own session, working it most
recently, closed it as unsolvable with present tools, not merely untried (unlike CS2-01/CS2-02 above). What
would reopen it per Bourdeau: a paleographer's transcription of the f.177 decipherment (to triple the labelled
training set) or a human glyph-by-glyph transcription of f.189/f.186, or the Aldobrandini/Frachetta papers'
own clear copies if they survive (Archivio Aldobrandini, Frascati; Vatican Fondo Borghese) -- none located this
pass.

Credit: D. Bourdeau, cyphersolver, https://dbourdeau.github.io/cyphersolver/ (catalogue item 20; `sega1593/`
working folder), CC BY 4.0 -- prior attempt (not a solution; closed-negative by his own session, with the
CNN-classifier and matched-control numbers reported). S. Tomokiyo, "A Polyphonic Substitution Cipher of the
Catholic League (1592-1593)" (cryptiana.web.fc2.com/code/mayenne.htm, per Bourdeau's citation) for the key.

## Next step (one line, not pursued further this pass per brief scope)

The series is identified -- *Acta Nuntiaturae Gallicae* (Universite Pontificale Gregorienne / Ecole Francaise de
Rome), the Filippo Sega legation volume for 1592-94 (Sega was legate 15 Apr 1592 - 12 Mar 1594, en.wikipedia.org
"Filippo Sega") -- but a WebSearch for it on archive.org or HathiTrust (24 Sept 2026) returned no direct link to
that specific volume; it is a modern critical edition, likely print-only or paywalled. Reaching it (interlibrary
loan or a library copy) is the next step before this row can be promoted past `blocked`.

## Edition check, LANE N3 csED2, 24 September 2026 (IA + Gallica SRU slots)

Brief: locate and read the edition(s) for the date and decide whether the cipher passages are printed. Route
used: archive.org advancedsearch + direct `_djvu.txt` downloads (IA slot), Gallica SRU (text-only metadata
search, Gallica slot), WebSearch, a fresh shallow clone of dbourdeau/cyphersolver (grep only). No Google Books
(excluded by this brief).

**Acta Nuntiaturae Gallicae (Sega's French legation, 1592-94), the volume this row's own brief names.**
`archive.org/advancedsearch.php?q=title:(acta nuntiaturae gallicae)` returns 0 results (checked 24 Sept 2026);
no HathiTrust record found by WebSearch either. The series is a 20th-century critical edition (École Française
de Rome / Université Pontificale Grégorienne), still being published as late as 2003 for other legations in the
same house style -- consistent with being under copyright and not digitised on an open archive. **Still
unreachable; still the gate for the four fr.3984 items.**

**Substitute route named in this brief: *Mémoires de la Ligue* (Goujet, 1758), vol. 5-6.** Both located on
archive.org and read as full djvu text: `memoiresdelaligu05goul` (1758) and `memoiresdelaligu06goul` (1758).
Grepped for "Baudouin", "Desportes", "Aldobrandini", "Frachetta", "Creil", "Mauclerc", "Sega": no hit for
Baudouin-Desportes, Aldobrandini or Frachetta in either volume (the "Baudouin" hits in vol. 5 are all a
different man, the Duc de Mayenne's own chancery secretary Baudouin, e.g. p.412 "Par Monsieur, Baudouin" --
unrelated). Philippe Sega himself is mentioned several times in vol. 5 (as the League's papal legate, e.g.
"Philippe Sega, Cardinal de Plaisance", pp. ~9270/10058/14452/15386/16773/22340/26547/31149) but only as an actor
in the narrative, never as the source of a printed cipher or a decipherment of his own correspondence.

**Possible found-solved: fr.3985 no. 7 (Mauclerc to Creil).** `memoiresdelaligu05goul`, pp. 411-414 (table of
contents entry: "Copie des Lettres du Docteur Mauclerc, envoyées de Paris au Docteur de Creil à Rome. 411"),
prints one letter in full under that exact heading: sender "Mauclerc" (a Sorbonne doctor), addressee "Docteur de
Creil à Rome", **dated "A Paris, le quatre d'Août 1593"** -- 4 August 1593, the last day of this row's own
14 May-4 Aug 1593 window, and a correspondent pair (a doctor named Mauclerc writing to a doctor named Creil in
Rome) that is otherwise unattested anywhere else searched. dbourdeau/cyphersolver's `sega1593/NOTES.md` (fresh
shallow clone, 24 Sept 2026) independently confirms fr.3985 no. 7 is catalogued as "Mauclerc -> Creil" and states
explicitly it "was fetched by the previous session but not examined" -- so no one has checked this letter's
content against a print before now. The letter's subject matter (League secrets: Mayenne's stalling over the
Guise-Infanta marriage project, the Estates, Spanish demands, a Sorbonne informant reporting to a companion at
Rome) is exactly the kind of material that would travel enciphered from Paris to a papal-circle recipient in
1593, and the printer's own frame calls it "ce qu'écrivit un Sorboniste à certain sien compagnon à Rome" (secret
correspondence revealing League plans), consistent with an intercepted/deciphered dispatch rather than an open
letter.

**Not independently confirmed and flagged for whoever picks this up:** (1) this pass did not fetch the fr.3985
Gallica leaf itself (canvas range c.6-13, `btv1b90606498`) to check the date and hand against the print --
gallica.bnf.fr IIIF/image fetch is outside this brief's granted hosts (SRU only); the prior check-solved pass's
own leaf fetch (canvas f8, "3 di agosto 1593" visible) may not even be no. 7's actual folio, since that pass
itself says "fr.3985's cipher passages are not necessarily on this exact folio." (2) No sentence in the print,
in Bourdeau's notes, or found by WebSearch explicitly says this printed letter *is* the deciphered form of the
BnF fr.3985 manuscript -- the match rests on correspondent-pair + date coincidence, which is strong (a two-name
match plus a same-day date is not the kind of thing that happens by chance) but not a citation naming the
manuscript. A worker with the image (or a verifier) should compare the print's text against the clear-French
portions visible on the leaf before this is called solved outright.

Credit for this find: none claimed -- the letter was already in print (Goujet 1758); this pass only located and
read the volume. Rule 10: no novelty claim made; this is a search result (a print located), not a verifier's
classification, and not a claim that fr.3985 no. 7 is "unpublished" (the opposite is being reported).

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made.

## Leaf check confirms found-solved: fr.3985 no.7 (LANE N3 csCS2c, 24 Sept 2026)

Fetched the fr.3985 Gallica IIIF manifest (ark `btv1b90606498`, 485 canvases, all labelled "NP" -- no folio
labels, so canvases were paged and read by eye) and read canvases f6 through f16 at reduced/native resolution
(image URLs `https://gallica.bnf.fr/iiif/ark:/12148/btv1b90606498/f{6..16}/full/1000,/0/native.jpg`) to walk
forward from the bundle's start and identify item "no.7" by its own marginal numbering. The bundle's items run
roughly two canvases (address leaf + letter) apiece: item "3" (Italian, ff.7-8, dated "8 d'aoust 1593" [sic],
signed "Giovan Piemarino," addressed "Carissimo Miser Giagino/Giacino" -- unrelated, not enciphered), item "4"
(address leaf f10, "Abiagino... notario in Tortona"), item "5" (French, ff.11-12, dated "3 aoust 1593," signed
illegibly, addressed to a "Monseigneur," re: a captain at Montsaugeon and a King's declaration -- unrelated), a
blank docket leaf numbered "6" (f13) and an address leaf to "Monseigneur le Duc de Nevers... Lieutenant Général
... en son pays de Champaigne & Brye" (f14, presumably item 6's own wrapper), then **canvas f15**: full page in a
clear, fluent secretary-hand French, numbered "7" at the top right margin, dated at the head "3 [or possibly 4,
period numeral shapes for 3/4 are easily confused at this resolution] d'aoust 1593," running through League
politics -- the Duc de Mayenne's stalling, the Duc de Guise, an oath ("Iurez... Iuratem... quod... Iuraverunt")
sworn before a papal legate not to reveal the Estates' secret articles, Spanish demands, the Cardinal-Legate,
"Roy de Navarre" -- and **signed "Mauclerc"** at the foot (confirmed again as a vertical docket label "Mauclerc"
on canvas f16, the leaf's verso/address side).

**Finding: canvas f15 (BnF fr.3985 no.7) carries no cipher at all -- it is written in ordinary legible French
secretary hand from the first line to the signature, with no digit groups, symbol substitutions or any other
enciphered passage visible anywhere on the leaf.** This matches Goujet 1758 vol.5 pp.411-414's printed heading
("Copie des Lettres du Docteur Mauclerc, envoyées de Paris au Docteur de Creil à Rome") on sender (Mauclerc),
date (3 or 4 August 1593, within one day either by an editorial normalisation or a misreading of the manuscript's
numeral, not independently resolved this pass) and subject matter (League secrets: Mayenne's stalling, the
oath before the legate, Spanish demands) -- the same match csED2 already established from the print side, now
confirmed from the image side as csED2's own flag asked for.

**Verdict: found-solved, grade F2** (README's F0/F1/F2: the plaintext is already in print, Goujet 1758, but no
catalogue, database or solver-repo entry links this specific BnF fr.3985 no.7 manuscript folio to that print --
Bourdeau's own catalogue instead bundles it, unread, into CS2-04's "attempted, open... ~5,000 polyphonic
glyphs" total alongside the four genuinely enciphered fr.3984 items). More precisely this item was never a
cipher to begin with: it is a **clear-text copy** ("Copie des Lettres...", per Goujet's own heading) that
happens to sit in a bundle of otherwise-enciphered League correspondence, so "found-solved" here means "not
enciphered, already in print," not "a decipherment recovered." No decoding, transcription or novelty
classification performed (rule 10; out of scope for check-solved). The four fr.3984 items (genuinely enciphered,
Baudouin-Desportes) are untouched by this finding and stay `blocked`.

Credit: none claimed for this pass beyond confirming csED2's print match against the image; the print itself
(Goujet 1758) and its location (csED2, 24 Sept 2026) are the finds. Requests this section: gallica.bnf.fr IIIF
manifest x1 (`btv1b90606498`), image fetches f6-f16 inclusive (11 canvases, several needed one retry after a
`ws_closed_mid_exchange` proxy reset, logged per the good-citizen rule) plus 2 high-resolution region crops on
f15 to try to resolve the "3" vs "4" date reading (inconclusive, not pursued further -- Gallica request budget
for this brief, <=25, was reached here and no further Gallica calls were made this session).

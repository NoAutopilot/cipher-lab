blocked

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

Not decoded, not transcribed here (out of scope for check-solved). Rule 10: no novelty claim made.

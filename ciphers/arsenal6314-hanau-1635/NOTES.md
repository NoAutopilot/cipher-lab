open

# Instruction to the comte Jacob de Hanau, 28 October 1635 -- Bibliothèque de l'Arsenal, Ms-6314

QUEUE row: M23 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

Bibliothèque de l'Arsenal, **Ms-6314** (184quater. H.F, "Recueil de pièces"), archivesetmanuscrits ark
`cc86280s`. QUEUE catalogue note: "Coppie (chiffrée et déchiffrée) de l'instruction donnée au sieur comte
Jacob de Hanau," 28 Oct 1635 -- cipher and its own contemporary decipherment both named in the same item, the
M1/M15/M21 cheap-transcription pattern. Thirty Years' War era; "comte Jacob de Hanau" not further identified
this pass (a French instruction *to* a count of Hanau, or possibly a French agent operating in/for Hanau --
not resolved).

## Check-solved sweep (24 September 2026)

1. **Web search.** Two queries (`"Arsenal" "6314" chiffre déchiffrée Hanau 1635`; `"comte Jacob de Hanau" 1635
   instruction chiffre`) returned only the archivesetmanuscrits catalogue record itself (ark cc86280s) and
   unrelated Hanau-Münzenberg genealogy pages (Philipp Moritz, Johann Ernst, Philipp Ludwig III, Balthasar --
   none named "Jacob," none tied to a 1635 French instruction). No solver or blog claim.
2. **Printed correspondence.** Not searched this pass. An "instruction" of this kind (French court to/
   concerning a foreign count, Thirty Years' War) is exactly the genre collected in Avenel's edition of
   Richelieu's *Lettres, instructions diplomatiques et papiers d'État* -- a natural next place to check, not
   yet done. Flagged as a gap, not a negative.
3. **Calendars/state-paper series.** Not reached (see item 2).
4. **Cryptiana / Cipherbrain.** No hit for "Hanau" tied to this item. The one "Hanau" occurrence in the local
   snapshot (`sources/cryptiana/web/german.htm` and `unsolved.htm`, an 1646 undeciphered letter of Carl von
   Rabenhaupt to Amalie Elisabeth, *regent of Hesse-Kassel, née Countess of Hanau-Münzenberg*) is a different
   item, different year (1646 vs 1635), different correspondent and different cipher -- confirmed as
   unrelated, flagged here so a future search does not conflate the two (same convention as the
   Clairambault1225 "two different Pagets" note). No Cipherbrain page found.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone, 1360 Decrypted +
   non-decrypted rows) grepped for "6314" and "Hanau": no hit.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "6314" and "Hanau": the only "Hanau" hit is `cyphersolver/CATALOGUE.md`'s entry for BL Add MS
   32305 (DECODE R2978-R2979, a Dresden/Hague correspondence unrelated to this item, and itself already
   removed from that repo's active catalogue on 21 Sept 2026). No hit for "6314".

Requests: WebSearch 2 queries. github.com 2 shallow clones (shared across this worker's six rows). No
gallica.bnf.fr or archivesetmanuscrits.bnf.fr fetches (per brief, LANE G2 has fetchers there already).

## Verdict

**Open.** Genuine gap: the Richelieu printed-instructions edition (Avenel) most likely to already contain this
"instruction" in print was not checked this pass, for budget reasons -- flagged, not scored as a source-family
negative.

`python3 tools/room.py ... "nomination: ciphers/arsenal6314-hanau-1635 | copy-free | recovery | own
decipherment present (cheap-transcription pattern); Avenel's Richelieu Lettres/instructions edition not yet
checked for this instruction; 'comte Jacob de Hanau' unidentified"`

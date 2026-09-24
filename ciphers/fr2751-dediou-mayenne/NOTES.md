open

# Sieur de Diou to duc de Mayenne, League era -- BnF Français 2751

QUEUE row: M32 (sources/solver-diffs/2026-09-24-lane-g2-gallica4.tsv, "Fourth pass, 24 September 2026").

## Source

BnF, Département des Manuscrits, **Français 2751** ("Recueil de pièces du XVIe siècle, 1549 à 1599", ancien
8357(43)), archivesetmanuscrits ark `cc49202m`. QUEUE catalogue note: "Lettre du sieur DE DIOU à monsieur le
duc de Maienne...escripte en chiffre," with its own decipherment; League era (Charles de Lorraine, duc de
Mayenne, League leader 1589-96). A WebSearch summary (not independently verified against the source page this
pass) places it at f.116-120 and gives the fuller title "Letter from Sieur de Diou to the Duke of Mayenne,
lieutenant general of the crown and State of France, written in cipher."

## Check-solved sweep (24 September 2026)

1. **Web search.** `"fr.2751" OR "Français 2751" chiffre Diou Mayenne déchiffrement` returned only the
   archivesetmanuscrits catalogue record (ark cc49202m) and unrelated Mayenne-the-place/dcode.fr noise; no
   solver or blog claim.
2. **Printed correspondence.** Not searched this pass for a dedicated Mayenne/League printed edition (e.g. a
   Goulart-type *Mémoires de la Ligue* compilation) -- flagged gap, not a negative.
3. **Calendars/state-paper series.** None identified for this miscellany; not applicable beyond item 2.
4. **Cryptiana / Cipherbrain.** Strong related lead, not a direct hit on this item. `sources/cryptiana/web/
   nevers.htm` (BnF fr.3995, a "genealogy of ciphers" survey volume Tomokiyo catalogued) no.55 (fol.98, 1592),
   quoted verbatim: *"'Chiffre de monsieur duma[yne] auec le Chevalier de Dyou.' Substitution by symbols.
   Homophones. Symbols for double letters and nulls. Special symbols for names and words. This is used in Duke
   of Mayenne to Commander de Diou, Paris, 13 May 1593 (BnF fr.3984, f.7). I posted my reconstruction of this
   cipher in another article [mayenne.htm#SEC2]."* `mayenne.htm` was not in the local snapshot and was fetched
   live this pass (`https://cryptiana.web.fc2.com/code/mayenne.htm`, 1 request, cipher-lab UA, saved to
   `sources/cryptiana/web/mayenne.htm`): it documents an *earlier* (1592-93) **polyphonic** Mayenne/de Diou
   cipher, independently reconstructed from six named letters -- BnF fr.3982 (f.97, f.101, f.124), fr.3983
   (f.106, f.108v, f.211) and fr.4715 (f.61, undeciphered but flagged as the same cipher) -- including
   "commander de Diou to Duke of Mayenne, Rome, 12 November 1592" (fr.3982 f.124), the same direction as M32
   (de Diou -> Mayenne) but a different date and a different volume. **Neither Tomokiyo page names Français
   2751 or quotes this specific item**, so this is not found-solved -- but it shows the Mayenne/de Diou
   correspondence already has **two independently published cipher tables** (the 1592-93 polyphonic one in
   mayenne.htm, and the May-1593-onward homophonic one keyed from fr.3995 no.55/fr.3984 ff.7-10). No
   Cipherbrain page found; not swept independently beyond item 1.
5. **DECODE.** Cached catalogue (`unsolved-ciphers/catalogue/decode-catalog.csv`, fresh clone, 1360 Decrypted +
   non-decrypted rows) grepped for "2751", "Diou", "Mayenne" (as a correspondent name, not the place-name
   false positives already ruled out): no hit tied to this shelfmark.
6. **Solver repositories.** Fresh shallow clones of `dbourdeau/cyphersolver` and `aaymeloglu/unsolved-ciphers`
   grepped for "2751", "de Diou", "dediou", "duma[yne]": no hit in either repo's curated catalogues or target
   folders (the repos' existing League-era targets -- nevers1587/, nevers1589/, mercoeur1586/, mercoeur1587/,
   matignon1586/, lorraine1592/, segur/, sega1593/, pelissier1592/, lebel1593/ -- are all different items,
   mostly the neighbouring fr.3982-3995 cluster, none this shelfmark).

Requests: WebSearch 1 query. cryptiana.web.fc2.com 1 (mayenne.htm, new fetch, saved to the shared snapshot for
future workers). github.com 2 shallow clones (shared across this worker's six rows). archive.org 0 for this row.

## Verdict

**Open**, scored as the recovery/cheap-transcription target QUEUE already identifies it as (the item carries
its own period decipherment, so reading it is a transcription task, not cryptanalysis). Flag for whoever
extracts it: once transcribed, cross-check the plaintext and cipher symbols against Tomokiyo's two published
Mayenne-de-Diou cipher tables (`nevers.htm` no.55 and `mayenne.htm`'s 1592-93 polyphonic table) as an
independent verification step -- not a substitute for reading the item's own decipherment.

`python3 tools/room.py ... "nomination: ciphers/fr2751-dediou-mayenne | copy-free | recovery | own
decipherment present (cheap-transcription pattern); 2 published Mayenne-de-Diou cipher tables exist (different
volumes/dates) for cross-check once transcribed, item itself not found in either"`

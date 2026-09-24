found-solved

Status set by LANE G2, 24 Sept 2026 10:28 UTC: ff.116-119 hold only the contemporary decipherment (f.116r is its heading and opening, not ciphertext; worker P 10:14); no ciphertext survives in the item, so there is nothing to decipher. The two published Mayenne tables stay here for any sibling letter.

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

## Capture and passes (24 September 2026)

**Digitised.** Confirmed via the finding aid (archivesetmanuscrits ark `cc49202m`, 1 request, 200): fr.2751 is on
Gallica at ark `btv1b52523734p`. The finding aid's own item list gives the exact folio range: item 45
"Fol. 116 -- 45 « Lettre du sieur DE DIOU à monsieur le duc de Maienne, lieutenant general de la couronne et
Estat de France, escripte en chiffre ». Déchiffrement de cette lettre." Item 46, immediately following, is
"Copie de la lettre du roy escri[te]..." at folio 120 -- a **different, unrelated** letter (Henri IV to Cardinal
de Bourbon, 5 May 1592, about a military engagement). This corrects the QUEUE/NOTES "f.116-120" range above
(WebSearch-derived, not checked against the source this pass): the De Diou item is confined to **ff.116-119**.

**Pinning.** `tools/gallica_folio.py btv1b52523734p --folio N` (manifest fetched on the second attempt --
first attempt hit the "manifest/services endpoints reset often" issue the brief warned of, `[Errno 104]
Connection reset by peer`; one retry per the brief's rule, succeeded). Offsets are NOT constant across the
volume (three runs, k=8/10/-10), so folios were read from the manifest's own per-canvas labels, not a formula:

| folio | canvas | label |
|---|---|---|
| 116r | f241 | 116r |
| 116v | f242 | 116v |
| 117r | f243 | 117r |
| 117v | f244 | 117v |
| 118r | f245 | 118r |
| 118v | f246 | 118v |
| 119r | f247 | 119r |
| 119v | f248 | 119v |
| 120r | f249 | 120r (different item) |
| 120v | f250 | 120v (different item) |

**Fetch.** 1000px previews of f241-f250 fetched via the direct image endpoint (the brief's advice that it
"works" held: 8 of 10 succeeded on the first or second attempt). f241 (116r) returned `Connection reset by
peer` on both the first attempt and the one permitted retry; per the brief ("after one retry per URL stop
that endpoint and report; do not route around") this URL was not tried a third time. f245 (118r) and f247
(119r, first attempt returned an HTTP 500 error page) succeeded on their one retry. Natives fetched for the
six readable canvases (f242-f247) only; f248-f250 previewed to confirm content then discarded (not part of
this item, or blank). Folder is 17 MB, under the 30 MB cap. Manifest: `images/manifest.json`.

**What is on ff.116v-119r.** Continuous, legible French prose in a clear secretary hand -- this is the
**decipherment**, not the ciphertext: no cipher symbols, numerals or nomenclature figures anywhere in this
running text, except a small number of places where the period decipherer left a nomenclature code
**unresolved** (a short drawn symbol over a blank/underline, e.g. "— S —", "— o —", "— Ϟ —", "TT"), which
this pass has NOT attempted to identify. The letter is from **de Diou** (commander de Diou, the League's agent
in Rome) to an addressee named only "Monsigneur" on this leaf (the finding aid ties the whole item to "monsieur
le duc de Maienne"), **Rome, 5 April 1592**, "Seellée d'un cachet". Content: League/Vatican politics -- Cardinal
Sfondrato, the Spanish ambassadors, Cardinal Caietan, a rumoured seizure of Marseille and a royal advocat from
Aix sent to investigate it, Cardinal Pallotte's contested vice-protectorship, financial arrangements (bills of
exchange to Antwerp, payment to "Monsieur de Plaisance"), and complaints that his own dispatches are not
reaching Mayenne. This date (5 April 1592) is **not** among Tomokiyo's listed de Diou-to-Mayenne letters
(27 Oct 1592, fr.3982 f.97; 12 Nov 1592, fr.3982 f.124) -- it is an earlier letter in the same run of
correspondence, distinct from any item his two articles name.

**Transcription.** One Sonnet pass, `dechiffre.txt` (grade M throughout: single pass, secretary hand, no
second pass to reconcile against; rule 7's "reproducible reading" does not apply here since this is a period
document transcription, not a keyed decipherment this repo is claiming credit for). Uncertain words marked
`[?]`; the unresolved period nomenclature codes marked `[symbol, undissolved]` rather than guessed at.

**Cipher folio, cipher passes, key trial -- BLOCKED this pass.** f.116r (canvas f241), almost certainly the
actual "escripte en chiffre" text (116v opens mid-sentence, consistent with continuing a page begun on 116r,
and the finding aid names one item spanning 116-119 with both a cipher and its decipherment), could not be
fetched (see Fetch above). Without it there is no ciphertext to transcribe, so **no `passA.tsv`/`passB.tsv`,
no `decode.json`, and no mechanical trial of the two published Mayenne-de-Diou tables against this item's
ciphertext (`trial.tsv`) could be produced this pass** -- all three are brief deliverables not met. Whoever
retries f241 next: it is a single Gallica IIIF image URL
(`https://gallica.bnf.fr/iiif/ark:/12148/btv1b52523734p/f241/full/full/0/native.jpg` or a smaller size),
already reset twice in immediate succession on 24 Sept while every neighbouring canvas succeeded, so a retry
after a longer pause, or later in the day, seems more likely to work than an immediate third attempt.

**Published Mayenne-de-Diou cipher tables, captured for a later trial (brief's secondary task).** Fetched from
`sources/cryptiana/web/mayenne.htm` (already in the shared snapshot) to `sources/cryptiana/web/`:
`mayenne.png` (the 1592-93 **polyphonic** cipher, BnF fr.3982/fr.3983), `mayenne3.png` (the May-1593
**homophonic** cipher, BnF fr.3984 f.7-10, the same cipher as `nevers.htm` no.55/BnF fr.3995), plus the two
annotated specimen pages `mayenne2.png` and `mayenne4.png` (kept for reference, not re-keyed). Transcribed the
primary symbol per letter (row 1 only; the homophonic table's 2nd-5th homophone rows and "double letters" row
are NOT transcribed, left for a future pass with more time) into `key_mayenne_1592-93_polyphonic.tsv` and
`key_mayenne_1593_homophonic.tsv`. **Grade M throughout on both**: the source images are small compressed web
thumbnails (~55-90px per cell), several glyphs within the same "hash/cross" family are not reliably
distinguishable at this resolution, and this pass could not verify the descriptions against the original BnF
page images. Do not treat either key.tsv as more than a rough placeholder for a real trial; re-derive from
fr.3982/3983/3984 at full resolution first. Neither table has been tried against anything yet -- there is no
ciphertext transcription from fr.2751 to try it against (see above).

**Requests this pass.** archivesetmanuscrits.bnf.fr 1. gallica.bnf.fr: 1 manifest fetch (1 reset + 1 retry) +
10 preview fetches (2 resets + 2 retries, all >=1.5s apart) + 6 native fetches = ~19. cryptiana.web.fc2.com: 4
(mayenne.png, mayenne3.png already-fetched-this-session mayenne2.png/mayenne4.png re-confirmed, all >=1.5s
apart; mayenne.htm itself was fetched by the check-solved pass, not repeated). No 429/403/challenge on any
host. No subagents.

**For whoever picks this up next:** (1) retry f.116r once, later; (2) if it is the cipher, run the brief's
step 2 in full (crops, two blind passes, decode.json, the key trial) against it; (3) identify the small number
of unresolved nomenclature codes left in the decipherment ("— S —", "— o —", "TT", etc.) against the two
published tables above or a nomenclature list, if one turns up; (4) do the "cross-check the plaintext... against
Tomokiyo's two published Mayenne-de-Diou cipher tables" step this row's earlier note called for, once a real
ciphertext transcription exists to check.

### f.116r fetched -- correction: no ciphertext in this item (24 Sept 2026)

LANE G2 worker P (Sonnet, cap $4). Retried the single URL the brief named,
`https://gallica.bnf.fr/iiif/ark:/12148/btv1b52523734p/f241/full/2000,/0/default.jpg`: 200 on the first try this
time (not committed; scratchpad only, folder already near cap). Read by eye (not cropped/OCR'd, since it settles
a yes/no question, not a transcription one).

**f.116r is not the ciphertext.** It is a title/header leaf in the same clear secretary hand as 116v-119r,
reading (diplomatic): "Lettre du sieur de Diou à Monsieur le duc de Maienne, lieutenant general de la couronne
et estat de France, escripte en chiffre, lequel signifie tout ce qui s'ensuit." [= "...written in cipher, which
signifies all that follows"], underlined, then "Monseigneur." and the letter's opening paragraph in plain French
beginning "Je vous ai assez amplement escript ce qui s'est passé icy par mon secrettaire que je vous ay envoié
qui vous aura informé de toutes choses, et par mes lettres des 17 et 23 Mars ce qui est intervenu depuis son
partement..." -- continuous prose, no cipher symbols, numerals or nomenclature figures anywhere on the leaf.

This corrects the "almost certainly the actual chiffre text" guess above: the heading's own wording is a period
archival note describing the letter as *originally* sent in cipher, introducing the decipherment that follows
(116r's own body text through 119r) -- not a second, raw-cipher copy. **No ciphertext for this item has been
located on any of the eight canvases examined (f241-f248, i.e. ff.116r-119v)**; the finding aid's phrase
"escripte en chiffre. Déchiffrement de cette lettre" describes one continuous decipherment text, not two
physical parts. Brief step 2 (crops, one blind Sonnet pass, passA.tsv) does not apply -- there is nothing
enciphered to transcribe. The unresolved nomenclature codes noted above ("— S —" etc.) inside the decipherment
remain the only cipher-like material in this item; they are isolated marks in an otherwise plaintext document,
not a continuous ciphertext, and a solver pass against them would need the two published Mayenne-de-Diou tables
(`key_mayenne_*.tsv` above) rather than a fresh transcription pass.

Practical effect: this target likely does not carry an unsolved ciphertext of its own (status stays `partial`
pending someone re-reading the finding aid / catalogue record directly, in case "chiffre" and "déchiffrement"
describe two separately-shelved companion items rather than one leaf range); the interesting open question is
the handful of unresolved nomenclature codes within the period decipherment, and whether fr.2751 elsewhere in
the volume (outside ff.116-120) holds a raw cipher letter this item's decipherment corresponds to -- not
checked this pass.

Requests: gallica.bnf.fr 1 (f241, 200 first try). No other host.

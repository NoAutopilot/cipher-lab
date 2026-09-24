partial

# August van Saksen (Sachsen) and Willem van Oranje, three cipher letters/postscripts, 1561-1564

QUEUE row: NB2 (`QUEUE.md`, "Dutch and Belgian archives (LANE N scout of 24 September 2026)").

## Source

Three letters/postscripts in the correspondence between Elector August of Saxony and William of Orange (Anna
of Saxony, August's niece, married William in 1561 -- the marriage this correspondence surrounds), "in
cijferschrift", no solution recorded in the WVO database:

| briefnr | date | direction | place | WVO record |
|---|---|---|---|---|
| 53 | 24 Oct 1561 | Willem -> August | Breda | https://resources.huygens.knaw.nl/wvo/app/brief?nr=53 |
| 57 | 18 Nov 1561 | August -> Willem | Torgau | https://resources.huygens.knaw.nl/wvo/app/brief?nr=57 |
| 126 | 16 Sep 1564 | Willem -> August | Brussel | https://resources.huygens.knaw.nl/wvo/app/brief?nr=126 |

Primary sources: Sächsisches Hauptstaatsarchiv Dresden, Geheimer Rat (Geheimes Archiv), Locat 9941/3 (53, 57)
and Locat 8510/5 (126); Koninklijk Huisarchief Den Haag holds copies/excerpts of some. Free PDF scans, no
login: `resources.huygens.knaw.nl/media/wvo/images/00000-00999/000{53,57,126}.pdf`.

**Confirmed by eye this pass** (`images/00053_p1-1.png`): 00053 is a German secretary-hand plaintext letter
(courtesy/family news, dogs and ferrets sent as gifts, per WVO's Inhoud field) with a cipher postscript at the
foot of the page in an **arbitrary-symbol cipher** (glyphs including X, V, Λ, ϖ, Δ, combined with digits) --
visibly a different design from the Lodewijk van Nassau numeral cipher of NB1, consistent with WVO's own note
"Een gedeelte van de brief is in cijferschrift" (part of the letter is in cipher). 00057 and 00126 not fetched
as images this pass (budget; both confirmed reachable by the scout, HTTP 200).

Four other letters from the same correspondence circle and years (briefnrs 74, 98, 153, 175) **do** carry a
contemporary solution or decipherment, per the scout's control sweep (QUEUE.md) -- not re-verified by this
worker, cited as background only.

## Check-solved sweep, 24 September 2026

Run directly by this worker (Sonnet, no Workflow tool, no subagents).

1. **Editions first / printed excerpt found for 57.** Briefnr 57's Brongegevens field (fetched and read this
   pass) cites: **"Demandt, Nassau-oranische Korrespondenzen, I, 78 nr. 113 -- excerpt"**. This is Karl E.
   Demandt's *Nassau-oranische Korrespondenzen 1553-1570*, published as **Regesten** (calendar-style summaries,
   not full transcriptions) in *Hessisches Jahrbuch für Landesgeschichte* 38 (1988), p. 49ff, and 39 (1989),
   p. 87ff, itself based on 18th-century Dillenburg archivists' own summaries of the originals (per WebSearch
   snippets of the work's own subtitle: "...in Gestalt der von den Dillenburger Archivaren Johannes von Arnoldi
   und Heinrich Westerburg Ende des 18. [Jahrhunderts]..."). **This worker could not locate or read Demandt's
   text itself this pass** -- *Hessisches Jahrbuch für Landesgeschichte* is a specialist regional journal, not
   found on Internet Archive, HathiTrust or Google Books by WebSearch, and not fetched. Given it is described
   as a Regest (a calendar entry summarising a letter's contents and archival location, in the same genre as an
   English "calendar of state papers" entry, not a diplomatic edition printing full text), a full cipher
   decipherment inside it would be unusual but is not ruled out by this worker's search. **Flagged as an open
   gap, not resolved**: WVO's own field labels the Demandt reference "excerpt" (not "editie", the label used for
   Groen van Prinsterer's full edition -- see NB4/`ciphers/la-garde-1577/NOTES.md`), which is weak positive
   evidence it is a summary, not a full/deciphered text, but this is inferred from the database's own citation
   genre labels, not from reading Demandt directly. 53 and 126 have no printed-edition citation in Brongegevens
   at all (manuscript only).
   No other candidate edition was located and read for this specific correspondence (Kluckhohn's "Briefe",
   named in CLAUDE.md's editions-first list for August of Saxony, was searched by WebSearch and found to concern
   a different Kluckhohn edition -- the WebSearch surfaced only August von Kluckhohn's biographical details, no
   locatable "Briefe" volume matching this correspondence; not pursued further, flagged as a second gap).
2. **WVO curatorial field.** As with NB1, the Opmerkingen field for 53, 57 and 126 carries no "oplossing" /
   "ontcijferd" / "ontcijfering" marker (contrast the four already-excluded siblings 74/98/153/175 in the same
   correspondence circle, confirmed by the scout to carry such markers).
3. **Community lists.** `sources/cryptiana/web/dutch.htm` read in full (see NB1 notes): no mention of this
   correspondence. WebSearch (`Kluckhohn Briefe August von Sachsen Wilhelm von Oranien 1561 1564 Chiffre`)
   found nothing relevant beyond genealogical pages confirming the 1561 marriage date.
4. **DECODE.** `sources/decode/records-non-decrypted-2026-09-24.tsv` grepped for the same terms as NB1: zero
   hits.
5. **Solver repositories.** Same fresh clones as NB1 (24 Sept 2026), grepped the same way: no hits relevant to
   this correspondence circle in either repository.
6. **General web search.** As item 3; also `Demandt "Nassau-oranische Korrespondenzen" Wiesbaden 1955 Band 1
   review` and `Demandt "Nassau-oranische Korrespondenzen" August von Sachsen Wilhelm von Oranien 1561 Chiffre`
   -- surfaced only the HessJb 38/39 (1988/1989) citation above and unrelated genealogy/biography pages; no
   solution claim found for any of the three letters.

## Verdict

**Status: open** (53, 126 firmly; 57 open but with an unread printed excerpt citation flagged as a genuine gap
-- see item 1). No solution, key or full deciphered plaintext found in six sources for any of the three.

**Copy status: copy-free.** Free PDF scans confirmed reachable; 53 viewed by eye, cipher confirmed present
(symbol design). 57 and 126 confirmed reachable (HTTP 200) but not opened this pass. No REQUEST.md needed for
the manuscripts; **a REQUEST.md-style follow-up worth naming for the next worker: access to Hessisches Jahrbuch
für Landesgeschichte 38 (1988) and 39 (1989) to read Demandt's regest of letter 57 directly**, not chased this
pass (not a personal-data request, so not written up as a formal REQUEST.md row this pass -- flagged here
instead as it needs a library/journal-access route, not a manuscript copy order).

**Kind: cryptanalysis** (no sibling decipherment identified for this specific trio this pass, unlike NB1;
the four already-solved circle-mates 74/98/153/175 are a possible future alignment lead, not chased here).

## Image capture, 24 September 2026 (LANE R worker R9)

Targets 57 (4pp) and 126 (5pp) fetched in full. All four siblings named in the brief -- 74, 98, 153, 175 --
opened as WVO records first (all "Willem -> August", same correspondence run and direction as 53/126, each
already flagged with an explicit cipher+solution note in Opmerkingen before fetching) then fetched in full (7,
6, 9 and 10 pages respectively) and rendered to PNG at 100dpi (lower than NB1/NB4's 150dpi, to fit 44 pages
under the 30MB folder cap -- re-fetch pdf_url at higher resolution for a solver pass). `images/manifest.json`
and `images/inventory.tsv` (per-page content, cipher type, approx tokens, decipherment location) written.

**Kind should be revisited: this is now also a recovery target, at least for a subset.** Confirmed by eye:
- **74**: cipher (f.18-18v) AND its contemporary decipherment (f.19-20, clear German, headed with the
  cipher's evident subject) are both imaged -- exactly the sibling pattern WVO's Opmerkingen promised.
- **98**: cipher (f.66) and a probable decipherment (f.68-69, headed "Zeittunge auss Franckreich") imaged;
  not confirmed word-for-word against the cipher's length, flagged for the solver.
- **153**: cipher (f.4) AND **two independent** contemporary decipherments (f.5, f.6 -- near-duplicate but not
  identical opening sentences) imaged. WVO's "waarvan 2 oplossingen" note is confirmed literally.
- **175**: cipher is not block-form but interlinear, run inline within clear German prose at several points in
  the letter, several with small marginal glosses in a different hand/ink directly above -- consistent with
  WVO's "(opgelost)" note but not confirmed as a full decipherment by this worker (flagged for a solver pass;
  see inventory.tsv per-page notes).

**Six distinct cipher designs observed across this one correspondence circle** (53/57: letters + arbitrary
symbols incl. Λ, Δ; 74/126: different arbitrary-symbol repertoires from 53/57 and from each other; 98: numerals
+ a few symbols; 153: pure overlined numerals, no symbols; 175: interlinear). **A solver should not assume one
key covers 53/57/126 just because 74/98/153 share a recoverable key with their own decipherments** -- the
designs differ letter to letter even within "Willem -> August" in this eight-year window. The alignment lead
is strongest for 153 (cipher + 2 decipherments) and 74 (cipher + 1 decipherment); 53/57/126 (the actual
targets) do not yet have a confirmed matching design to any deciphered sibling -- this needs eye comparison of
glyph repertoires once a solver pass runs, not assumed from correspondence direction alone.

Host: resources.huygens.knaw.nl, 10 requests this pass (4 WVO record pages + 6 PDF fetches, >=2s apart).
Folder kept at 24MB under the 30MB cap.

## R14: atlas and passes (24 September 2026, stopped over cap)

Done and pushed: `glyphs/atlas.md` (glyph codebook built from 74 p3-p4, 98 p2, 126 p4 by eye, no
pixel-crop segmentation available in this container -- see atlas.md's method note; 53/57 share G1/G3/G4
with 74/126 but also show G2 and G13 not confirmed elsewhere, so repertoire overlap is partial, not
identical, matching R9's "six distinct cipher designs" note above); `plaintext_74.txt` (ff.19-20,
briefnr 74's decipherment leaf) and `plaintext_98.txt` (ff.68-69, briefnr 98's decipherment leaf),
both best-effort palaeography, German as written, [?] on uncertain words, not aligned or decoded.

Left undone: the two blind passes (passA.tsv, passB.tsv) over 126 p4, 74 p3-p4, 98 p2, 53 p1 postscript,
57 p3 block (both blocks -- 57 p3 has two separately-signed cipher blocks, not one, noted to the pass
workers). Two Sonnet subagents were launched to do these blind from the atlas and had not written their
output files when this worker was stopped at cap ($10.70 against a $7 cap); neither passA.tsv nor
passB.tsv exists on disk. Their agent sessions may still be running in the orchestrator's environment
and could still land results; if so, whoever picks this target up next should check for them before
re-running the passes, then `tools/reconcile_passes.py passA.tsv passB.tsv` (header `line pos sign
briefnr page lineno`, matching the tool's "long" format) into `recon/`. No sign count or agreement
percentage is available -- the passes never completed. No H/C/S/M/I grades apply here (no decoding
attempted this pass).

## R21: key from 74/98, reading of 126 (24 September 2026, LANE R worker R21, Opus, aligner)

Method: aligner, as in rah-canada-1869 and lodewijk R18: no blind passes. Worked from **native-resolution
scans** (the page JPEGs inside the Huygens PDFs, 3600-4400 px wide, about 5x the 100dpi PNGs in images/). The PDFs
were fetched once to the scratchpad and not committed (74, 98, 126, 53; URLs in images/manifest.json).

**Two cipher systems, not one.** 
- **System A (74, f.18r-v, 1562)**: German written letter by letter. Digits, Latin letters and invented signs,
  one sign per letter, with homophones: s = T or G4, h = 5 or S, u/v = X, w = XX. Also sch = TL and st = J, plus
  word signs for König, zu, Frankreich, Engelland, und, Bapst, Hertzog, Beyern, Niderland, Hispanien, E.L. and
  Ital-. Aligned against the contemporary decipherment on f.19r: **864 signs**, `align_74.txt` ->
  `ciphertext_74.tsv`, `pairs_74.tsv`. The f.19r text is a close decipherment, not a paraphrase, but its
  wording differs in places (cipher "so hatt", f.19 "Er hat"; cipher "uff der", f.19 "bey der"; one name
  at 74 p4 l.2 left unpaired). Where they differ, the pairs record the cipher's own German, checked word
  by word against f.19. The f.19 paragraphs are the Le Havre cession of 1562 ("einen hafen genant la haver
  de gras verkaufft"), followed by Spanish, Italian, papal and Bavarian troops for the French king. (This worker's
  own gloss, not a search result.) f.20 was not used.
- **System B (98, f.66, 1563; the same system reads 126, 1564)**: a different key over a similar repertoire
  (3 = e, 0 = a, Or = r, Qg = g, ...; see atlas "R21 codes, 98 system"). **Its decipherment is f.67 (p3), not
  ff.68-69.** plaintext_98.txt (ff.68-69, "Zeittunge auss Franckreich") is an enclosed newsletter and does
  not correspond to the cipher. f.67 reads "Es wirdt bey uns fur gewiss gesagt, das Wilhelm von Grumbach
  ... und Staupitz ... vom Konige zu Frankreich bestallung haben sol, wir bitten aber E.L. ...". It is a
  free decipherment: it adds "fur" and smooths the troop numbers. **184 signs** aligned, `align_98.txt` ->
  `ciphertext_98.tsv`, `pairs_98.tsv`. Units marked `~` are pairings the aligner is unsure of.
  f.67 was read at native resolution but not transcribed to a file; the words used are in align_98.txt's
  header.

**Key** (`build_key.py`, --check 0): `key_74.tsv` 38 signs, `key_98.tsv` 33 signs, `key.tsv` both (system
column), `key_conflicts.tsv` 8 rows. Grade C where every sure pairing agrees. Otherwise M: all word signs
in 98, and Λ, which is l or m in 98 (the l/m split, L vs filled Lf, cannot be seen in 126's hand).

**126 p4 (f.139, Willem -> August, Brussel 16 Sept 1564)**: one careful reading in System B codes,
`ciphertext_126.tsv` (240 signs, 4 marked M on the image), `exceptions_126.tsv` (15 context values, all
M), `decode.json`; `tools/decode_key.py . --check` exits 0. **Tokens 240: H 0, C 214, S 0, M 26, I 0, U 0.**
The C grades come from the 98 decipherment. No sign of 126 is unkeyed, apart from K (word sign, "die") and
the down-arrow (k / ge), which are given M by context. Result: cryptanalytic reading with a sibling key
(C from known plaintext of 98, applied to 126). The interlinear letters above 126 l.1 ("e e r e", a later
hand?) contradict the key (they give e for N and r for 3) and were not used.

German rendering (`reading_126.txt`; brackets = word signs; u/v normalised to u by the key):

> [Wir] konnen auch [E.L.] in freundtlichem vertrauen nit verhalten, [das] [wir] seidhero auss Hispanien
> andere zeitung bekommen haben, welche vermelden, [das] [die] Konnigin so heftig kranc[k] [ge]worden sei,
> [das] man ir [die] ade[r]n zwei mahl s[ch]lagen [und] auch zwei mahl purgieren mussen, dermassen [das]
> sie irer frucht erlediget worden sei.

In short: news from Spain that the Queen fell so ill that she was bled twice and purged twice, and so lost
the child she was carrying. Gaps: "adesn" (Sb read s where r is expected; one sign), "slagen" (no c/h
sign written). Nothing else is missing.

**53 p1 and 57 p3: not read.** 53's postscript (native scan, 2633x4175, fetched once) shares System A's
sign shapes (XX, ϖ, Δ, λ, ƒ, Ƶ, ε) but not its values. Under key_74, 53 l.2 gives "uettelah?e.znnregu...".
It also uses dots as word separators and a frequent "15" ending. It is a third key over the same
repertoire. 57 was not opened. Suggestion: an aligner or solver for 53/57 could start from System A's sign
inventory and treat 53 as a fresh monoalphabetic German substitution with homophones, about 400 signs.
Suggestion: transcribe f.67 (98's decipherment) to a file and settle the `~` pairings. Superseded:
plaintext_74.txt f.19 l.1 "dreyhundert" should read "dreythaussent" (cipher and f.19 agree).

Requests: resources.huygens.knaw.nl 5 (PDFs 74, 98, 126 [one 404 on a mistyped 3-digit path, then 200], 53),
>=2 s apart. No other host.

## Verifier V3 audit, 24 September 2026 (LANE V2)

126 classed **N3** in AUDIT.md (no prior decipherment or printed plaintext located; principal editions searched, see
its log). Correction to the check-solved sweep above and to `images/inventory.tsv` ("decipherment location: none"):
WVO lists two more witnesses for 126 beyond the Dresden original. They are the **KHA minute A 11/XIV I/4 nr. 26,
recorded "met een 'Zeitung'"**, and a 20th-century copy in the Collectie Japikse. The minute may hold the
postscript's text in clear. Neither has been seen. Status word moved from open to partial because 126 is read
(C 214 of 240) and 53/57 are not.

## S1: 53 and 57 (24 September 2026, LANE R2 worker S1, Opus, two Sonnet passes per letter)

**57 p3 (August -> Willem, Torgau 18 Nov 1561; the scan is the KHA copy A 11/XIV B/41-6) is System A: it reads
with key_74.** `ciphertext_57.tsv` (reconciled from passA_57/passB_57, 84.8% column agreement; settlements
decided on the crops and logged row by row in `settle_57.py`), `exceptions_57.tsv` (5 unkeyed word signs, by
context), `reading_57.txt`. **Tokens 300: H 0, C 247, S 0, M 53, I 0, U 0** (C = key_74 from the 74 decipherment).
57 p3 has one cipher block, not two. The "two blocks" in R14 were the plaintext postscript and the cipher, each
signed. New System A signs seen here: OQ (circle with a tail, "wir" by context), THE (circle under a cross,
"Keiser", twice), BOX (square, "Churfurs[ten]"), G1h (hooked tent, x in "Maximilianum"), all M. VmV (König)
occurs twice, once abbreviated before a colon ("König: Ma x imilianum"). A colon stands for a nasal
abbreviation ("zu ei:em" = einem).
> auff freundtlich hoch vertrawen wollen [wir] E.L. nitt bergen, das der [Keiser] fur wenig tagen durch seine
> stadtliche gesanndten hen bei uns suchen lasen, seinen sohn König Maximilianum noch bei seinem, des Keisers,
> leben zu einem römischen Könige zu erwelen, konnen erachten, solchs werde bei den andern [Churfürs]ten gleicher
> gestalt auch gesucht werden, welchs E.L. bei sich inn geheim werden zu halten wisenn.

In short: the Emperor had envoys ask August to elect his son Maximilian King of the Romans in the Emperor's
lifetime, and the same was probably being asked of the other Electors. This is this worker's gloss, not a search result.

**53 p1 postscript (Willem -> August, Breda 24 Oct 1561; Dresden Loc. 9941/3 f.266) is a third key, read
cryptanalytically.** [A2 correction, 24 Sept 2026: the cipher does not end on p1. PDF 00053 has two pages; f.266v
(`images/00053_p2.png`) carries three more cipher lines (about 90 signs), then the end of the letter and an autograph
postscript in clear. The reading below covers p1 only; "mrch" is a line end, not the end of the text.] 10 lines, not 12. The first crop set mixed lines and was replaced by deskewed crops. Two
blind passes (passA_53/passB_53, 90.9% agreement), `settle_53.py` → `ciphertext_53.tsv`: 282 letters, 20
distinct signs, dots as word separators. Solver: `tools/homophonic_anneal.py` (new, pure Python, trigram +
KL letter term, w folded to uu), LM = `tools/data/de16/composed_enhg.txt` (composed text, see its README) +
plaintext_98.txt. The 74 text is kept out of the LM because it is the control.
- **Matched control (rule 3):** the cipher's own 1562 German (align_74.txt), first 282 letters, homophonic key
  with 20 signs, same settings: **280/282 letters (99.3%)** (`solve_53_control.json`; `tools/tests/test_homophonic_anneal.py` reruns it).
- **Target:** 4 of 6 restarts converge on the same key (score -655.6), and it gives connected German (`solve_53_target.json`).
  One correction by context: G6 = k (the annealer gave f; its 3 occurrences read khomen, konigreich, krieg).
  `key_53.tsv` (20 signs, grade S). G1 and G7 both = s. 77 = w (uu). **Tokens 282: H 0, C 0, S 163, M 119,
  I 0, U 0.** The M tokens are signs that a pass flagged as doubtful. `decode_key.py . --check` exits 0.
- Reading (`reading_53.txt`, no repairs):
> neiuuer zeittung hab ich itcmals nicht zu bergen zu schreiben, dan das dem printzen zu hispanien seines hern
> vatters schwester ehlich vermahlet werden und hieruber diese lande zu regieren khomen sollen, und dan ein
> gemein geschret ist, es wolle der hertzog von Vandosmen sein konigreich Navarra mit der gute oder krieg
> wiederholen mrch
  Doubtful spots: "itc(mals)" (4 = c where z/itzmals is expected), "geschret" (geschrey?), "mrch" at the end
  (mich?). Read with the image, not repaired. In short: news that the Prince of Spain would marry his father's sister and
  come to govern these lands, and that the Duke of Vendôme would recover his kingdom of Navarre by agreement or
  war. This is this worker's gloss.
- This is a cryptanalytic result: no H or C tokens. 53 shares System A's sign shapes but has its own
  alphabet, e.g. 1 = e (e in 74 too), 5 = n, 7 = u, X = i, V = r, Xk = t, G3 = h.

**Search log (on disk only, no network):** the committed sources (`sources/`, Cryptiana pages, IA full-text run
tables, WVO notes) were grepped on 24 Sept 2026 for vandosme/vendosme, nauarra/navarra, maximilian, "vatters
schwester", hispanien and "romischen konig". No hit concerns these letters: Cryptiana german/habsburg/nevers
only name the persons in unrelated contexts, and the IA run tables hold index lines of other books. Not searched: the printed
Groen van Prinsterer *Archives*, Kluckhohn, and Demandt's regest of 57 (Hess. Jb. Landesgesch. 38, p.78 nr.113),
which the check-solved sweep names as open gaps. None is on disk. No novelty is classified here (rule 10).
Suggestions: a verifier should read Demandt nr.113 and the Groen/Kluckhohn volumes for 53 and 57, and
phrase-search "Vandosme" / "Maximilianum" / "vatters schwester". A native-resolution re-read of 53 (Huygens PDF 00053)
would settle the 119 M tokens.
Requests: none (no network). Subagents: 4 Sonnet passes (2 for 57, 2 for 53), plus 2 discarded passes over the mis-cut 53 crops.

## A2: second audit of 126, first verification of 53 and 57 (24 Sept 2026, Auditor A2 for LANE V2)

Classes in AUDIT.md: 126 N3 (second audit, unchanged), 53 N3, 57 N3. Findings: 53 has an unread second page of cipher
(f.266v, now `images/00053_p2.png`, about 90 signs); Demandt's regests of 57 (HessJb 38, 1988, nrs. 113 and 115, read
through Google Books snippets) summarise only the clear letter and its 23 Nov postscript, so the check-solved gap on
Demandt is closed; 57's Dresden witness is August's minute "met een 'Zettel'", unseen, the likeliest place for the
plaintext in clear; V3's "Rachfahl II.1" was vol. II part 2, and II.1 (1907) was checked only through HTRC token counts.
Suggestions: a solver pass on f.266v with key_53; Dresden inquiry for Loc. 9941/3 f.268-269; KHA inquiry for A 11/XIV
I/4 nr. 26.

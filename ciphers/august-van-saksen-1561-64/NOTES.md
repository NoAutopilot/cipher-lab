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
postscript in clear. The reading below covers p1 only; "mrch" is a line end, not the end of the text. F1 read p2 below.] 10 lines, not 12. The first crop set mixed lines and was replaced by deskewed crops. Two
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
- **F1 extension, 24 Sept 2026 (LANE R2 worker F1, Opus, one careful reading, no passes, no network):** f.266v's three
  cipher lines (`images/00053_p2.png`, read at 3-5x from the 100 dpi render) are appended to `ciphertext_53.tsv` as
  `53p2_L01`-`L03` (86 rows, 82 letters, same codes) and read with key_53 unchanged. One sign absent from key_53, `9`,
  occurs twice and is set to f by context in `exceptions_53.tsv` ("zu [9]ranckreich", "[9]urgang"), grade M.
  **p2 tokens 82: S 75, M 7. Whole letter (p1+p2) tokens 364: H 0, C 0, S 238, M 126, I 0, U 0.** `decode_key.py --check` exits 0.
> dunck aber die uueil der konnig zu franckreich noch so iung ist, es uuerde keinen furgang geuuinnen.
  In short: "but it seems to me that, as the King of France is still so young, it will make no progress" (this
  worker's gloss). p2 opening "dunck aber" suggests p1's last word "mrch" is "mich" ("mich dunck aber"): L10 pos 26 is
  a 'differ' row (V vs another sign); an image re-check of that one sign is suggested, not repaired here. Doubtful on
  p2: G7 in "so" (lambda-like, could be X), the blotted 1 in "uuerde", the barred Z in "zu".
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

## A3: second audit of 53 and 57 (24 Sept 2026, Second Auditor A3 for LANE V2)

Classes in AUDIT.md "Second audit 53/57 (A3)": 53 N3, 57 N3 (A2's classes stand; neither raised nor lowered).
Findings: Japikse, *Correspondentie van Willem den Eerste* I (1934) ends with letters of September 1561 (chronological
list pp.386-389, read on the Huygens retroboeken viewer), so it prints neither 53 (24 Oct) nor 57 (18 Nov); the KHA
"Collectie Japikse" copies are preparation for an unpublished continuation. Goetz 1891 (the 1562 election), Weiss VI-VII,
Ritter I (weak OCR) and Kruse 1934 (search-inside counts only) print neither cipher passage. Phrase searches on the
f.266v sentence (F1's reading) returned nothing. 53's reading is S grade only (M 126 of 364), so its class covers the
text as read. Gaps for an N4 decision: Kluckhohn I clean read, Rachfahl II.1 as text, OpenAlex and Semantic Scholar
(429 twice), Kervyn II.

## D2: N4 decision for 53 and 57 (24 Sept 2026, N4-decision verifier D2 for LANE V2)

Classes in AUDIT.md "N4 decision (D2)": 53 N4 (no prior decipherment located; for a cryptanalytic reading, S 238 M 126
of 364), 57 N4 (no prior decipherment located). Gaps closed: Kluckhohn I read at sentence level for Oct-Dec 1561 (IA
`briefefriedrichd00frie`; nr. 148 is the Palatine side of the election approach, with no August or Orange item);
Kervyn *Relations politiques* II (IA, nothing); Rachfahl II.1 text unreachable (not on IA, Google NO_PAGES), so its
HTRC tokens were scanned for co-occurrence of the gist (nothing; the "chiffrierter Zettel" pages are 1562). OpenAlex and
Semantic Scholar 429 a third time (do not block). 24 Google Books API gist queries: nothing. Unpublished witnesses
remain: the Dresden minute of 57 with its 'Zettel' (could lower 57), the KHA Japikse copy of 53. Outreach held at gate 2
(ASKS row 39). Follow-ups: Dresden inquiry f.268-269; Namèche 1884 wedding pages; von Weber, Archiv f. sächs. Gesch. 3 [done 24 Sept 2026, V3d: pp. 309-339, IA bub_gb_lFwAAAAAcAAJ, nothing for 1561].

## csWV3: two further circle letters, not candidates (LANE N2, 24 September 2026)

Print-status pass across all 73 un-nominated WVO cipher letters (`.claude/briefs/runs/2026-09-24-lane-n2-csWV3.md`;
full table `sources/wvo/print-status-2026-09-24.tsv`). Two August van Saksen letters in `sources/wvo/cipher-letters-
2026-09-24.tsv` were never in this folder's original seven-letter table (53/57/74/98/126/153/175) and are not
existing solved siblings already used by S1/R21/A2/A3/D2 above:

- **Briefnr 58** (31 Dec 1561, "to August van Saksen", Breda, KHAG;SAD, no edition code). WVO Opmerkingen
  (fetched 24 Sept 2026, https://resources.huygens.knaw.nl/wvo/app/brief?nr=58): "Met een ontcijferd gedeelte in
  geheimschrift" (with a deciphered portion in cipher) -- a decipherment is attached to/accompanies the document
  itself, not via a printed edition. Not fetched or imaged this pass. **Flag for LANE R3**: a possible further
  key source for this circle, alongside 74/98 (already used by R21's aligner) -- worth a capture pass if the
  circle's key work continues.
- **Briefnr 124** (16 Apr 1564, "to August van Saksen", Brussel, DNOK;GPA;HHSAWB;KHAG). WVO's own remark:
  "solved elsewhere (Groen van Prinsterer, Archives (GPA))". Not individually page-checked this pass (budget);
  classified Class A by pattern only, consistent with the rest of this same GPA-cited correspondence. Not a
  candidate either way.

Neither changes this folder's own N4 verdicts for 53/57/126 above. Requests this pass: resources.huygens.knaw.nl
1 (briefnr 58 detail page, shared with the wider 9-page batch logged in `sources/wvo/NOTES.md`).

## Reading suggestions from SO-SAXONY-126 (logged by verifier V3c, 24 Sept 2026; not applied)

- 126: 'adesn' (l.6) and 'slagen' (l.6) print as emended 'adern', 'schlagen' in the prompt; a solver should check on f.139 whether the s/r sign and the missing 'ch' are transcription or key issues, and whether the down-arrow read 'k' (l.5 pos 11) and 'ge' (l.5 pos 17) is one sign or two forms.

## Second opinion SO-SAXONY-53-57 (24 Sept 2026, V3d for LANE V4)

Checked in AUDIT.md: no prior print found; 53 and 57 stay N4. Prompt excerpt for 53 relabelled as normalised with the
sign-level output verbatim. Solver suggestion (not done): settle 53's M tokens behind "zuberzuschreiben" (l.2),
"geschret" (l.7) and "mrch" (l.10) from the image before any quotation; the normalised "zu bergen zu schreiben",
"geschrey" and "mich" are emendations, not readings.

## While waiting (27 Sept 2026, WAIT-PASS-A)

Waits on the Dresden (Loc. 9941/3 f.268-269) and KHA (A 11/XIV I/4 nr. 26) inquiries named in D2's follow-ups,
since 24 Sept 2026.

- Run the solver pass on f.266v with key_53 (already built in this folder, never applied) to settle more of 53's 126 M-tokens. S, tools/decode_key.py.
- Eye-check SO-SAXONY-126's unapplied sign candidates (l.5 pos 11/17, l.6 'adesn'/'slagen') against images/00053_p2.png already on disk. S.
- Re-scan the Rachfahl II.1 HTRC token counts (already fetched) for the 1561/1564 window more closely than D2's one gist pass. S, tools/htrc_ef_headwords.py.

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 699 of 904 cipher tokens firm (77.3%: C 461 + S 238), M 205, U 0, from `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` (rerun 2 Oct 2026 00:2x UTC, exit 0, "reading up to date"): 126 C 214 of 240 (89.2%, key_98 from the decipherment f.67), 57 C 247 of 300 (82.3%, key_74 from f.19), 53 S 238 of 364 (65.4%, no H or C: a cryptanalytic result; matched control 280/282, 99.3%, solve_53_control.json)
- 53 p1+p2 (f.266r-v, 13 cipher lines; 126 M, incl. 'zuberzuschreiben' l.2, 'geschret' l.7, 'mrch' L10 pos 26) - blocker: not-attempted; passes cut from the 100 dpi images/00053_p1.png (passbrief_s1.md, 90.9% agreement, recon53/disagreements.tsv 28 rows), p2 read once at 100 dpi (F1); the native JPEG (2567x4187, about 309 dpi, images/manifest.json) was never used for passes, and S1's own suggestion ("a native-resolution re-read ... would settle the 119 M tokens") and SO-SAXONY-53-57's spot checks were never run; next: fetch 00053.pdf once, `tools/iiif_lines.py --image` crops pasted, two blind passes per page + one reconciliation (5 subagent calls at about $1.46 each), tools/reconcile_passes.py, then decode_key.py --check and regrade, ~$9
- 53 key (key_53.tsv, 20 signs all S; sign 9 = f by context, exceptions_53.tsv) - blocker: not-attempted; WVO 58 (Orange to August, Breda 31 Dec 1561, two months after 53, WVO note "Met een ontcijferd gedeelte in geheimschrift") was flagged by csWV3 for capture and never fetched (no 00058 file or fetch anywhere in the repo; sources/wvo/cipher-letters-2026-09-24.tsv carries its pdf_url); next: fetch 00058.pdf (1 request), compare its glyphs with key_53, key_74 and glyphs/atlas.md, trial-decode under key_53 and key_74; if one matches, align its decipherment (build_pairs.py/build_key.py pattern) and regrade 53 (S to C) or 57, ~$4 for the test
- 57 p3 (KHA A 11/XIV B/41-6, 7 lines; 48 transcription-doubt M) - blocker: not-attempted; passA_57/passB_57 agree on 84.8% of columns (recon57/disagreements.tsv, 49 rows), cut from the 100 dpi images/00057_p3.png (passbrief_s1.md); R21 fetched native scans for 74/98/126/53 only, never 57 (R21 "Requests"); next: fetch 00057.pdf, crop p3's 7 lines with `tools/iiif_lines.py --image`, two blind passes + one reconciliation (3 subagent calls), decode_key.py --check, regrade, ~$6
- 57 p3 word signs outside key_74 (OQ 'wir', THE x2 'Keiser', BOX 'Churfurs-', G1h 'x'; 5 tokens M by context, exceptions_57.tsv) - blocker: not-attempted; reclassified from waiting-on: the Dresden reply (Loc. 9941/3 Bl. 268r-269v 'Zettel', request sent 26 Sept 2026 18:20 UTC, CONTRIBUTIONS.md 'Dresden minute of WVO 57', outreach/dresden-wvo57-minute.md 'reply pending') is one route, but two internal ones are untried: WVO 58 (Dec 1561, between 57 and 74, with its own decipherment, never fetched) and WVO 175 (1567, interlinear cipher runs with contemporary glosses, symbols + digits, already on disk as images/00175_p1-p8.png, never compared sign by sign with System A, images/inventory.tsv); signs absent from 74 (ciphertext_74.tsv has no OQ/THE/BOX/G1h); next: in the WVO 58 worker above, look for OQ/THE/BOX in 58; separately compare 175's glossed runs with System A's word-sign inventory on the disk images (no network), ~$2; the Dresden reply remains the fallback
- 126 p4 (f.139) key-level M (Λ as m 9, word sign K 'die' 2, down-arrow k/ge 2, sign 1 as i 2; the 15 rows of exceptions_126.tsv) - blocker: not-attempted; WVO 124 (Orange to August, Brussel 16 Apr 1564, five months before 126, "solved elsewhere (Groen van Prinsterer, Archives (GPA))", sources/wvo/cipher-letters-2026-09-24.tsv) was classed by pattern only (csWV3) and never fetched; next: fetch 00124.pdf (1 request), check whether its cipher is System B (glyphs/atlas.md "R21 codes, 98 system"); if so, align it against Groen's printed text (Archives I, IA full-text route) to settle K, the down-arrow and the l/m split, then regrade 126, ~$5
- 126 p4: 11 M tokens inherited from key_98's uncertain pairings (EL8 'das~' 4, NW 'wir~' 2, Pf 2, R 'E.L.~' 1, Qf 1, 9 t/d~ 1) plus SO-SAXONY-126's spots ('adesn' Sb as s, 'slagen' no ch, down-arrow at l.5 pos 11/17 one sign or two) - blocker: not-attempted; f.67 was read at native resolution by R21 but never transcribed to a file, and align_98.txt carries 24 '~' units (not 7) over 6 lines, with key_conflicts.tsv 8 rows; R21's "transcribe f.67 ... and settle the ~ pairings" was never done; the SO-SAXONY-126 suggestions are logged "not applied"; the "While waiting" bullet 2 points this check at images/00053_p2.png, the wrong leaf (126's cipher is images/00126_p4.png, f.139); next: one native-resolution worker (PDFs 00098 and 00126, 2 requests): transcribe f.67 to plaintext_98_f67.txt, settle the 24 '~' units, build_key.py --check, re-read the three f.139 spots, decode_key.py --check, regrade 126, ~$5
- 53 and 126 as whole texts, independent period witness (KHA Collectie Japikse copies of 53 and 126; KHA minute A 11/XIV I/4 nr. 26 of 126 "met een 'Zeitung'") - blocker: waiting-on ASKS row 67 (dr. Huysman's reply on a KHA route, asked 26 Sept 2026 about 15:00 UTC, outreach/huygens-reply-2026-09-26.md); the KHA is not online; AUDIT.md V-GATE2 ruling keeps N4 with the copies named as an unseen witness; the internal key-level routes for these letters are the WVO 58 and WVO 124 gaps above

## Escalation (1 Oct 2026)
- [ ] siblings: opened 74, 98, 153, 175 (R9, images/inventory.tsv); 74 (f.18/f.19) and 98 (f.66/f.67) are the key sources for 57 and 126 (R21); 153 (1566, overlined numerals) is a different design; Orange's 1561 Schwarzburg key is not an August system (ciphers/gunther-van-schwarzburg-1561/NOTES.md step 2). Not tried: WVO 58 (31 Dec 1561, "met een ontcijferd gedeelte") and WVO 124 (16 Apr 1564, printed by Groen) never fetched; 175's glossed interlinear runs (on disk) never compared sign by sign with System A, System B or key_53. Planned: fetch 58, then 124; compare 175 from the disk images
- [x] clear-pages: 74 f.19 and 98 f.67 identified as the contemporary decipherments and aligned (R21); plaintext_98.txt (ff.68-69) shown to be an enclosed newsletter, not 98's decipherment; the clear text beside each target (53 p2 autograph postscript, 57 p3 signed clear postscript, 126 pp1-3) checked and none is the decipherment (inventory.tsv, S1, A2). The minutes that may carry plaintext are outside: Dresden 'Zettel' of 57 (reply pending), KHA minute and Japikse copies of 126 and 53 (ASKS 67). 126's interlinear "e e r e" above l.1 (later hand?) contradicts the key and was not used (R21)
- [x] known-keys: tools/key_crossmatch.py ran every on-disk key against ciphertext_53/57/126 (KEY-CROSSMATCH.tsv); only each text's own key reads it (key_74 on 53: z -4.47, "uettelah?e.znnregu..."; key_98 on 53: z 0.74); the Schwarzburg 1561 key differs in form; the four keys are in KEY-OFFICES.tsv and KEY-DESIGN.tsv; Cryptiana dutch.htm, DECODE and both solver repositories: no hits (check-solved)
- [x] print: Groen, Gachard, Rachfahl (II.1 through HTRC tokens only), von Weber, Kluckhohn I, Goetz 1891, Japikse I (ends Sept 1561), Demandt nrs 113/115 (clear text only), Kervyn II, Weiss, Ritter, Kruse, 24 Google Books gist queries, phrase searches, JSTOR rows 48/49/55/56/63/64/69; no prior decipherment located (AUDIT.md V3, A2, A3, D1, D2, V-GATE2). Groen's printed text of WVO 124 not yet used as a key source (siblings). "While waiting" bullet 3 (closer Rachfahl II.1 HTRC scan) is optional print work, not a reading step
- [ ] key-rebuild: done for 53 (tools/homophonic_anneal.py, 4 of 6 restarts converge, matched control 280/282; G6 = k by context). Not done: 57's five word signs and 126's K, down-arrow and Λ l/m are context-only; key_98's 24 '~' units are unsettled because f.67 was never transcribed. Planned: settle them from an f.67 transcription; extend key_53 from WVO 58 and key_98 from WVO 124 if either shares the system. No instrument here has failed its own gate even once, so nothing is retired
- [ ] image-check: R21 read 126 once at native resolution; S1 settled pass disagreements on 100 dpi crops (settle_53.py, settle_57.py). Not done: native-resolution passes for 53 (p1 and p2) and 57 p3; the SO-SAXONY-53-57 spots (l.2, l.7, L10 pos 26) and SO-SAXONY-126 spots (adesn, slagen, down-arrow) never applied. Planned: native crops and two passes for 53 and 57, a native spot re-check on f.139 (against images/00126_p4.png / 00126.pdf, not images/00053_p2.png). "While waiting" bullet 1 (run key_53 on f.266v) is stale: F1 did it 24 Sept 2026
- [ ] retry: no unread groups (U 0); decode_key.py --check exits 0 on an unchanged key and transcription (unchanged since 24 Sept 2026). Planned: rerun decode_key.py --check and regrade all three letters after each image-check or key extension above
Verdict: keep going: 6 internal gaps; cheapest next: fetch WVO 58 (1 request) and trial-decode it under key_53 and key_74, also looking for 57's word signs OQ/THE/BOX, ~$4

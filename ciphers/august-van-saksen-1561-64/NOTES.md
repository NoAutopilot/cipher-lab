partial
Editions read in this repository for these letters (not by GF-A2-1): Demandt, HessJb 38 (1988) p.78 nrs. 113/115 (A2, Google Books snippets: clear text of 57 only) and Japikse, Correspondentie I chronological list pp.386-389 (A3, Huygens retroboeken viewer: ends Sept 1561, prints neither 53 nor 57); sections A2/A3 below and AUDIT.md.

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

- Run the solver pass on f.266v with key_53 (already built in this folder, never applied) to settle more of 53's 126 M-tokens. S, tools/decode_key.py. [Stale: F1 applied key_53 to f.266v on 24 Sept 2026; the regrade was run by AVS53, 3 Oct 2026: 51 tokens M->S, 53 now S 289 M 75.]
- Eye-check SO-SAXONY-126's unapplied sign candidates (l.5 pos 11/17, l.6 'adesn'/'slagen') against images/00053_p2.png already on disk. S.
- Re-scan the Rachfahl II.1 HTRC token counts (already fetched) for the 1561/1564 window more closely than D2's one gist pass. S, tools/htrc_ef_headwords.py.

## NEXT-AVS: WVO 58 fetched and trial-decoded (2 Oct 2026, parent worker NEXT-AVS, account 2)

The cheapest next step named by the Verdict line below (brief `.claude/briefs/runs/2026-10-02-acct3-next-avs.md`).

**Fetched** (1 request, resources.huygens.knaw.nl, 01:11 UTC): `00058.pdf`, 5 pages, embedded JPEGs at 251-461 dpi.
WVO briefnr 58, Willem -> August, Breda 31 Dec 1561 (Dresden Loc. 9941/3, "Printzen", f.270r-272r). Content by eye:
p1-p2 = f.270r-v clear German letter, signed; **p3 = f.271, a cipher block of 15 lines in two paragraphs** (7 + 8),
signed "Wilhelm printz zu Uranien"; **p4 = f.272, the contemporary decipherment** in clear German, 15 lines, one
hand (WVO's "ontcijferd gedeelte"); p5 = address leaf. Kept at 100 dpi as `images/00058_p3.jpg` and `00058_p4.jpg`
(JPEG, folder at 28 MB under the cap); native pages were read from the PDF in the scratchpad and not committed
(re-fetch `pdf_url` in `images/manifest.json`). Line crops cut with `tools/iiif_lines.py --image ... --region
60,100,2080,2050` (15 bands, pitch 122 px); the decipherment with `--region 0,100,2073,1500 --lines-per-crop 2`.

**Glyphs.** f.271 is System A: the same repertoire as 74 and 57 (digits, T V X Z S J, G1 Λ, G2 Δ, G3 ϖ, G4 π, G6 ε,
TL, Zb, XX, VmV, Wm), none of 126/98's System B marks. Not a third repertoire like 53's (53 writes dots as word
separators and ends words in "15"; 58 writes gaps and ends words in "17" = en, as 74 does).

**Trial decode** (rule 3, both numbers): `ciphertext_58_sample.tsv`, 10 of the 15 lines (L01-03, L08-11, L13-15;
301 signs, one reader at native resolution, 9 signs M), word signs coded `NEW1`-`NEW7` by shape only so the decode is
blind to f.272. `tools/decode_key.py . --ciphertext ciphertext_58_sample.tsv --key key_74.tsv --style words` ->
`trial58/reading_58_trial_key74.txt`; the same with `key_53.tsv` -> `trial58/reading_58_trial_key53.txt`.
`trial58/score_trial58.py` counts the letter-words (60 units with no word sign) that are words of my f.272 reading
(`trial58/plaintext_58_f272.txt`, grade M, u/v and ai/ei and ss/s normalised):

| key | letter-words matching f.272 | decode of L01 |
|---|---|---|
| key_74 (System A, C from 74's f.19) | **46/60 (76.7%)** | es lest sich in [NEW1] undt in diesen [NEW2] undt |
| key_53 (53's cryptanalytic key) | **0/60** | e??e??kcnku?iuzskuzkepeu?iuzs |
| control: key_74 with its letter values shuffled (200 draws) | mean 0.18/60, max 7/60 | |

The 14 key_74 misses are the cipher's own spellings against the decipherment's (undt/unnd, Frankreich/Franckreich,
standt/stand, wurdet/wirdet, scharpffer/scharffer, dien-st-lichen split by a gap) and two signs I read wrongly
(L03 "ubainen", L08 "istd"), not key errors: the same cipher-vs-decipherment drift R21 found on 74. **58 is read by
key_74 and not by key_53.** f.272 is a close decipherment, as 74's f.19 is: "Es lest sich in Hispania unnd in diesen
Niderland und auch in Franckreich dermassen ansehen, das fried zwischen beiden Konigen ... langen bestandt haben
werde ... Der Religion und Inquisition halben ist noch allenthalben im alten stand und wirdet in Hispania viel
scharffer gehalten als ummer beschehen, so sicht man in diesen Niderland vleissiger zu als hiebevorn, dieweill sich
die secten in Franckreich also vermheren, welchs alles ich E.L. bey sich in geheimbt zu behalten dienstlichen
anzeigen wollen" (my reading, M; peace expected between the two kings; religion and the Inquisition unchanged,
stricter in Spain, watched more closely in the Netherlands since the sects in France multiply).

**Word signs in 58** (value from f.272 at the matching position, grade M until aligned; shape in
`ciphertext_58_sample.tsv`'s `#NEWn` rows): NEW1 S+Z ligature = Hispanien (key_74 `HISP`, n=1), NEW2 oval with a
bar = Niderland (`NL`, n=1), NEW3 double-barred cross = fried (not in key_74), NEW4 S with two bars = Religion (not in
key_74), NEW5 trident = und (`UND`, n=2), NEW7 three bars crossed = E.L. (`EL`, n=1); NEW6 is the single letter q
(Inquisition), absent from 74. Whether NEW1/2/5/7 are the same shapes as 74's own HISP/NL/UND/EL was not checked on
74's 100 dpi image; their meanings match. Also seen: the F (p) sign written as a loop with a cross below (L10
"scharpffer"), Xy = y in "bey" (L14).

**57's word signs: not in 58.** All 15 lines of f.271 were scanned on the native crops for 57's three shapes
(`exceptions_57.tsv`: OQ circle with a tail = wir, THE circle under a cross = Keiser, BOX square = Churfurs-):
none occurs. 58 writes "wir" with letters where it needs it (not in the sample) and never names the Emperor or an
Elector. The one circle-and-cross sign in 58 (L10) is the p of "scharpffer", not an orb. 58 therefore settles
nothing for 57's five M tokens; the remaining internal route for them is 175's glossed runs (on disk), then the
Dresden reply.

**What this changes.** The "53 key" gap's WVO 58 route is closed: 58 cannot extend key_53 (different system). No
token of 53, 57 or 126 is regraded; `tools/decode_key.py . --check` still exits 0 on the unchanged decode.json (the
58 sample is not a decode.json job). Follow-up, not run (Workers rule 7): a full alignment of f.271 against f.272
(`build_pairs.py`/`build_key.py` pattern, about 560 signs, ~$6) would add C-grade counts to key_74's letters and
two word signs (fried, Religion) at grade C, and give the circle a fourth System A letter with its decipherment;
it changes no grade on the three targets, so it is a key-register job (KEY-OFFICES/KEY-DESIGN at close-out), not
a reading step. 58's cipher text is a candidate for the Dresden/KHA print check only if someone needs it.

Requests: resources.huygens.knaw.nl 1 (00058.pdf). No other host. Status line unchanged (`partial`); status.json,
STATUS.md and NEAR.md not touched (flagged to the parent).

## A2-AVS: intake gate stops the WVO 175 comparison (2 Oct 2026, worker A2-AVS, account 2, LANE-A2PUSH)

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-avs.md` step 2, run 2 Oct 2026 about 20:55 UTC before any deep work:

    $ python3 tools/intake_gate_check.py august-van-saksen-1561-64
    august-van-saksen-1561-64: partial (line 1) with no standard-edition citation (page number or full-text-search phrase) within 6 lines -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead
    EXIT 1

Two things fail, the second hidden behind the first. (1) The head-only gate (RETRO-2026-10-02-account4 proposal 2)
reads only the first 12 lines, and the edition citations already logged further down (A2: Demandt HessJb 38, 1988,
p.78 nrs. 113/115 via Google Books snippets; A3: Japikse I pp.386-389 on the Huygens retroboeken viewer) sit outside
it. A trial copy in the scratchpad with one pointer line under the status word cleared that check. (2) The same trial
copy then failed the CHECK-SOLVED-WEB rule (28 Sept 2026): this file logs no open-web and blog-comment check (no "Web
and blog check" heading, no paragraph naming Cipherbrain, the Cryptiana blog and Cipher Mysteries; the 24 Sept sweep
read Cryptiana's dutch.htm page only). Fixing (2) means running check-solved.md's "Open web and blog comment threads"
step, a network check-solved job, which is outside this brief (an on-disk comparison only), so per the brief the worker
stopped here: the WVO 175 comparison was not run, nothing on disk changed except this section and the Verdict line,
no token regraded, no request made, no subagent or vision call.

## A2-AVS-2: WVO 175's glossed runs compared with 57's word signs (2 Oct 2026, worker A2-AVS second spawn, account 2, LANE-A2PUSH)

Brief `.claude/briefs/runs/2026-10-02-acct2-a2-avs.md`, rerun after GF-A2-1 cleared the intake gate. Step 2, 21:51 UTC:

    $ python3 tools/intake_gate_check.py august-van-saksen-1561-64
    august-van-saksen-1561-64: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    EXIT 0

**What was compared.** All ten pages of WVO 175 (Willem -> August, 9 Apr 1567, Dresden Loc. 9819/5 ff.348r-352v)
from the 100 dpi disk images `images/00175_p1-p10.png`, no network. Cipher runs with interlinear glosses in a second
hand occur on p1 (f.348r, about 13 lines), p2 (f.348v, two runs), p3 (f.349r, 7 lines), p4 (f.349v, 4 lines; the
inventory's "p4 none" is wrong), p5 (f.350r, 3 lines), p6 (f.350v, 6 lines) and p8 (f.351v, 6 lines); p7, p9 (closing,
signature) and p10 (address) carry none. Each run was cut into 3x-upscaled region crops (scratchpad, not committed)
and read by eye for the three shapes in `exceptions_57.tsv`: OQ (a circle with an inner loop/tail, "@"-like, 57 L01),
THE (an orb: circle with a cross standing on top, 57 L02 and L04) and BOX (an open square, 57 L06).

**Positive detection control (rule 3).** The same eye at the same resolution (the S1 crops `images/crops_s1/57_L01.png`,
`57_L02.png`, `57_L06.png`, cut from the 100 dpi `images/00057_p3.png`) finds the OQ, the orb and the square at once on
57's own lines, so a 100 dpi scan can see these shapes where they exist. The control can fail differently from the
target on this statistic (present vs absent), unlike a coverage-on-shuffle control.

**Result: none of the three shapes occurs in any 175 run (0 of about 45 cipher lines).** Shapes that do occur and
could be confused: a plain O (p1 "KOtBOv", "NHOΛ"; p3), a capital B (p1, p5 "B.ad"), and a circle standing on a cross
(Venus-like, written here as ♀), which is a frequent letter-level sign (several per line on every page) and is the
inverse of 57's orb, not the orb. The glosses give the meanings 57 needs, and none of them is carried by a single
sign: "Chur und Fürsten" is glossed three times (p5 "lobliche Chur und Fürsten", p6 "Religion verwandten Chur und
Fürsten", p8 "die deutsche lobliche Chur und Fürsten") over runs with no square; "wir" is glossed at least four times
(p1 twice, p3, p4) over runs with no "@"-circle; no gloss contains Keiser (the Emperor appears only in the clear text,
"Kay: Mat:", p2 and p3). **175 settles nothing for 57's five M tokens; no token regraded.**

**Why: 175 is not System A** (by eye, grade M, one reader at 100 dpi, no transcription file). System A writes the
"-en" ending as 17 (key_74 1 = e, 7 = n) and "und" as a trident; 175 closes most cipher words in "3v" and uses a free-
standing M at "und" positions (for example between "Chur" and "Fürsten" on p8), which is key_98's M = und. Two run-final
words read with digit values shared by the keys: p5 "83+[d]3v" under the gloss "... werden" and p6 "85+[d]3v" under
"... wurden": key_98 (8 w, 3 e, 5 u) gives we?[d]en / wu?[d]en; key_74 (8 b, 3 a, 5 h) and key_53 (8 b, 3 a) give
ba?[d]a? / bh?[d]a?. Five digit tokens only, so this is a pointer, not a test: **175 may be a glossed System B
letter** (98 and 126's system), which would make it a key source for 126's key-level M (K 'die', down-arrow, Λ as m),
not for 57. Not pursued (Workers rule 7); written into the 126 gap below as a second route after WVO 124.

**What this changes.** The 57 word-sign gap's last internal route is closed (58 on 2 Oct 01:2x UTC, 175 now); its only
remaining route is the Dresden reply, so its blocker moves to waiting-on. `tools/decode_key.py . --check` unchanged
(no file it reads was touched). Vision: 17 image reads by this worker (pages and region crops), 0 subagents. Requests: none.

## A2-AVS3: WVO 124 is System B with its own decipherment; 126's key-level M regraded (2 Oct 2026, worker A2-AVS3, account 2, LANE-A2PUSH)

Intake gate (`python3 tools/intake_gate_check.py august-van-saksen-1561-64`, 2 Oct 2026 22:2x UTC):
`august-van-saksen-1561-64: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Fetched once (scratchpad, not committed): `00124.pdf` (8 leaves, about 540 ppi, 15.7 MB) and the WVO record
brief?nr=124; then `00126.pdf` (1 request) for a native re-check of f.139. WVO's record for 124 (Dresden Loc. 8510/5
f.130r-135v, the same file as 126's f.139): "Het origineel met een bijlage in (ontcijferd) geheimschrift".

- **f.134 is a full cipher page (about 21 lines), f.135 its contemporary decipherment** ("Ferner will E.L. ich in
  geheimbden vertrauen nit verhalten, das mir kurtz auff einander von dreien unterschiedlichen orten gleichlautende
  Zeitunge ... zukommen sindt, welcher massen Hertzog Johans Friderich und Hertzog Johans Wilhelm zu Sachssen ...").
  Same secretary hand and same sign set as 126's f.139. **System B, confirmed by alignment, not by pattern:** with
  key_98 values the cipher reads wil E.L. ich in ... vertrauen nit verhalten das mir kurtz uf einander ... verhalten,
  welcher massen, als, unversehen, erneuerung, furderung, wan, desto, bei zeiten, wollen, schreiben, anders, meinung,
  vermerckhen, hiervon, allzeit, gerne (3 e, 8 w, Z i, D c, 1 h, N n, R E.L., Or r, Qg g, 5 u/v, 4 o, 0 a, 9 t, Yz z,
  Dp p, M und, EL8 das). Like 126 it writes sch as s ('undersiedlichen', 's r e i b e n'), so 126's 'slagen' is the
  cipher's own spelling, not a lost sign. Word signs outside key_98 also occur (a long bar sign, 'PAPE'/'pa pe', 'B.',
  'S:'), apparently names; not aligned this pass.
- **Groen does not print the enclosure.** Archives I (1835 ed., IA `archivesoucorre00housgoog`, LETTRE LXXXII,
  pp.231-233, read from the djvu text already on disk in sources/ia-fulltext/print-check/) prints only the clear letter
  ff.131-133 ("Eur Churf. G. antwortt ... Datum Brussell ahm 16 Aprilis A. 64"), with an ellipsis; no cipher, no
  decipherment. The key source is therefore f.135 (period decipherment, image), not a print.
- **Settled for 126 (the gap's four key-level questions), from line crops cut with `tools/iiif_lines.py --image`
  (f.134: 11 bands; f.139: 5 bands), read by this worker, no subagent:**
  1. Λ l/m: in 124 a *filled* Λ is m every time it is aligned (gehaim, mir, khommen, massen, bemelte, -men,
     meinung, vernhemen: 8 of 8, no filled Λ = l); an *open* Λ is l (about 14: wil, verhalten, -lich- x3,
     gleichlautende x2, welcher, sollen, etliche, also, wollen, allzeit, slagen) or m (4: möchten, niemandt, damit,
     vermerckhen). This matches 98 (Lf = m 5 of 7). On the native f.139 scan eight of 126's nine Λ-as-m are the filled
     form (bekommen x2, vermelden, man, mahl x2, mussen, dermassen) -> **C**; l.1 pos 32 (freundtlichem) shows a lighter
     fill and its sign was already conf M -> stays M. Discrimination check: the fill/open split is tested against
     known plaintext on 124 (filled 8/8 m; open 14 l / 4 m), so the shape can and does fail to predict for open Λ.
  2. Down-arrow: 124 writes 'ck' as D + the down-arrow in 'vermerckhen' (f.135 'vermerckhen'), and the same stemmed V
     for k throughout (kurtz, khommen, khamen, konnen). On f.139 the arrow follows D and closes 'kranck' (gap after it
     on the native scan), so the reading is 'kranck worden', not 'kranc [ge]worden'. ciphertext_126.tsv l.5: pos 11
     recoded ARR -> V (the word-initial k of 'kranck', key_98 V = k, C); the arrow and the word divider swapped (pos
     16/17) -> **C** (k).
  3. Sign 1 as i: 124 attests 1 = i once ('81ΛΛ' = will, f.135) beside 1 = h (verhalten, hiervon, nhu, mahl). Both
     values are period-attested; in 126 the choice ('ihr', 'zwei') is by context -> stays **M**, reason updated.
  4. Word sign K: in 124 K aligns to **'der'** ('dieweil K weldt', f.135 'dieweil der Weldt', n=1), not 'die'. 126's
     two K are 'die' by context ('die Konnigin', 'die adern'). A conflict, n=1 against context; held **M**, not merged.
- Result: `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` -> "reading up to date";
  **126 tokens 240: H 0, C 224, S 0, M 16, I 0, U 0** (was C 214, M 26). reading_126.txt l.5 now "so heftig kranck worden
  sei". No judge spec exists for this target (specs/ has none).
- Not done (outside this step): a full transcription of f.134 aligned to f.135 into align_124.txt / key_124 (it would
  also test key_98's '~' units: EL8 'das' is aligned at least three times in 124, R 'E.L.' four times, M 'und' three
  times). Requests: resources.huygens.knaw.nl 3 (00124.pdf, brief?nr=124, 00126.pdf; one retroboeken viewer page,
  a JS shell, 1). Vision: no subagent calls; this worker read 22 f.134 crops, 8 f.139 crops, 5 f.135 crops.

## A2-AVS4: WVO 124 f.134 aligned against f.135; key_98 rebuilt from 98 + 124 (2 Oct 2026, worker A2-AVS4, account 2, LANE-A2PUSH)

Intake gate (`python3 tools/intake_gate_check.py august-van-saksen-1561-64`, 2 Oct 2026 22:46 UTC):
`august-van-saksen-1561-64: partial (line 1) -- edition/page or full-text-search citation found within 6 lines`, exit 0.

Route: `00124.pdf` fetched once more to the scratchpad (1 request, resources.huygens.knaw.nl, not committed); page 6 = f.134
(cipher), page 7 = f.135 (decipherment). Crops with `tools/iiif_lines.py --image` (f.134: 10 bands of 2 lines x 2 segments;
f.135: 8 bands of 3 lines x 2 segments), read by this worker; no subagent, so no blind second pass (rule 2: image, one reader).

- **`align_124.txt`** (18 cipher lines, **679 signs**) -> `ciphertext_124.tsv`, `pairs_124.tsv` (`build_pairs.py`, default now
  74 98 124). f.135 is a free decipherment like f.67: it expands the word sign PAPE to "Hertzog Johans Friderich und Hertzog
  Johans Wilhelm zu Sachssen" / "hertzogen zu Sachssen", writes "auff" for the cipher's "uf", "zukhommen" for "ein khomen",
  "der fuss sei" for "die fuess"; units are the cipher's own German checked word by word against f.135 (header of the file).
  New word signs in System B: PAPE = the Saxon (Ernestine) dukes (3x), S = zu (2x, one '~'), K = der (1), B = der (1, '~'),
  a looped long bar 'Reutern' (coded BAR?, 98's BAR is 'hundert_pferde~'; not merged), OM + Sb 'landtsknechten' ('~'), TT 'b'
  in 'bit-' ('~'). Ma (б with an overbar) = st 3x more (desto, dienstlich, verstendigen).
- **Held '~' on purpose (a verifier may overrule):** sign 1 = i in 'will' (l.17; already noted by A2-AVS3) and open Λ as m
  ('gehaimbtem', 'mochten', 'vermerckhen', coded `L?`): the pairing is sure, but a firm count would turn 1 (h, 37 firm) and L
  (l, 40 firm) into two-valued M signs on one occurrence each; recorded in key_conflicts.tsv either way. A looped d without a
  visible cross read as d ('die', 'dem', 'deiss') is coded `D?` (D = c firm 21x).
- **Controls (rule 3), both able to differ from the target:**
  1. `control_124.py`: of 124's sure pairings on signs key_98 (98 alone, snapshot `key_98_from98.tsv`) grades C, **611/611 =
     1.000** agree with key_98; units shuffled within line, 1000 seeds: **mean 0.100, p95 0.119, max 0.138**. Caveat: the
     cipher-side units were written by a reader who knew key_98, so this mainly shows the two texts are one system read
     consistently; check 2 is the independent one.
  2. `dp_check_124.py` (tools/interlinear_align.py `align`, letter signs numbered below --floor 100 and seeded from key_98, word
     signs 100+ never seeded): aligning the cipher to **f.135's own wording**, the DP hands the word signs align_124's meaning on
     **17/21 occurrences** (R 5/6, EL8 3/3, M 6/6, PAPE 2/3, K 1/1, S 0/2 -- f.135 has no 'zu' at l.7 and the DP splits 'zu' at
     l.11); cipher tokens shuffled within line, 5 seeds: **2, 3, 1, 1, 0 of 21 (mean 1.4)**. Letter signs: DP chunk = align_124 unit
     on 576/618 (0.932; seeded from key_98, so not independent of it). Outputs in dp_124/ are regenerated, not committed.
- **key_98 rebuilt** (`build_key.py` now reads pairs_98 + pairs_124 for System B; --check 0): EL8 das M n=1 -> **C n=4** (das:3
  firm), R E.L. M n=1 -> **C n=7**, M und C n=1 -> C n=7, 9 t C n=39 (the t/d~ pairing stays one loose row), Pf f C n=18, Ma st
  n=5, new PAPE C n=3, K der C n=1, S zu C n=2. Unchanged: NW 'wir' (absent from f.134), Qf (only the doubtful l.1 F), Lf
  m|l M (98's one firm l), Mf, HX, Dl, Sg.
- **126 regraded:** `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` -> "reading up to date" after
  regeneration; **126 tokens 240: H 0, C 229, S 0, M 11, I 0, U 0** (was C 224, M 16: EL8 x4 and R x1 now C). The German text of
  reading_126.txt is unchanged. Left M: NW 'wir' 2, Qf 1, K 'die' 2, 1 as i 2 (key/context), and 4 transcription-doubt signs
  on f.139 (Λ l.1 pos 32, Pf l.5 pos 6 and l.8 pos 6, 9 l.5 pos 7). 'adesn' (Sb as s) was not re-read (outside this step).
  No judge spec exists for this target (specs/ has none).
- Not found: no NW ('wir') and no K-as-'die' anywhere on f.134; Groen I 231-233 prints only the clear letter (A2-AVS3).
  Requests: resources.huygens.knaw.nl 1 (00124.pdf). Vision: 0 subagent calls; this worker read 20 f.134 crops, 16 f.135 crops.

### VERIFY-AVS4: verifier on A2-AVS4's WVO 124 alignment and its three held pairings (2 Oct 2026, account 2, LANE-A2PUSH)

Separate session from A2-AVS4. `00124.pdf` fetched once to the scratchpad (resources.huygens.knaw.nl, 1 request, not committed);
f.134 (page 6, 3745x5836) and f.135 (page 7) read by this verifier from native-resolution crops of the named spots only; 0 subagent calls.
- **Sample:** f.134 line 2, first 20 signs (`5 3 Or 1 0 L 9 3 N | Td 0 Sb | Lf Z Or | V 5 Or 9 Yz`, verhalten das mir kurtz):
  20/20 as align_124.txt has them, and f.135 reads "verhalten, das mir kurtz".
- **Controls (rule 3):** control_124.py re-run: 611/611 vs shuffled mean 0.100 (p95 0.119); the within-line unit shuffle changes
  which unit sits on which sign, so it can fail differently from the target. It is not independent of key_98 (A2-AVS4's own caveat
  stands); the DP check (17/21 vs mean 1.4) is the independent one and was not re-run.
- **Ruling on the held pairings** (rule 4: C only where f.135 supplies the value):
  1. *Sign 1 = i in 'will' (l.17): keep held (M).* The native crop shows a plain 1 (`8 1 L L`, no Z), and f.135's "das will E.L. Ich"
     supplies i at this token; but one occurrence against 37 firm h cannot tell a slip from a second value, and a firm i would
     turn sign 1 into a two-valued M sign on 126. 126's two 1-as-i tokens stay M.
  2. *Open Λ as m: reject as a value of L.* At native resolution the three Λ (gehaimbtem, mochten, vermerckhen) carry the solid
     apex wedge of Lf (same form as Lf in 'mir' l.2 and 'meinung' l.16), not the thin open Λ of 'wil' l.1 and 'will' l.17. Recoded
     `Lf?` (fill partial). f.135 supplies m at 'möchten' and 'vermercken' (units now plain m on a doubtful sign, so loose in
     build_key); f.135 writes 'geheimbden', so 'gehaimbtem''s m is not supplied and stays m~. L is now l:40, m~:1 (the one m~ is
     98's, untouched); Lf stays M m|l because of 98's one firm l.
  3. *Looped d without a cross = d: keep held (M).* No cross visible on any of the three ('die' l.4, 'dem' l.9, 'deiss' l.15), so the
     shape is D, not a doubtful Td: recoded `D` with the unit `d~`. f.135 supplies d at 'dem' and 'dieses' but has no 'die' at l.4;
     three tokens on one page against D = c firm 21x do not separate an omitted cross from a homophone.
- **Effect:** build_pairs.py, build_key.py (--check 0), `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check`
  "reading up to date": 126 still C 229, M 11; no reading or grade changed, so AUDIT.md gets a one-line propagation note and the
  SECOND-OPINIONS-QUEUE rows (SO-SAXONY-126, SO-SAXONY-53-57) need no update.

## AVS53: key_53 dictionary regrade of 53's M tokens (3 Oct 2026, worker AVS53, account 2, LANE-A2PUSH3)

Intake gate: `python3 tools/intake_gate_check.py august-van-saksen-1561-64` -> "august-van-saksen-1561-64: partial (line 1)
-- edition/page or full-text-search citation found within 6 lines", exit 0.

**Premise.** The brief (and "While waiting" bullet 1) asked for key_53 to be applied to f.266v. That was already done by F1 on
24 Sept 2026: f.266v is 53 p2 (`images/00053_p2.png`, rows `53p2_L01`-`L03` in `ciphertext_53.tsv`), 53's own system, read
with key_53 unchanged. Nothing was re-decoded. What was left of the step is the regrade: whether key_53's decodes support
moving any of 53's 126 M tokens (all transcription-doubt flags: 118 agree-flagged, 10 pass splits, 2 sign-9) to S.

**Pre-registered** in `prereg_avs53.md` (commit 3221d9bb for test A; test B appended in 34751adb after A's result and before
any B score). Dictionary: genuine period German only -- `tools/data/de17` word types (count >= 2) plus the sibling
decipherment texts on disk (align_74, plaintext_74, plaintext_98, align_124); `tools/data/de16/composed_enhg.txt` excluded
(model-composed, topic-overlapping). Control (rule 3): key_53 values permuted within four frequency bands, 1000 draws, seed 53;
it can differ, since permuting values changes the decoded letters whose dictionary membership is counted.

| test | statistic | key_53 | control mean | control p99 / max | gate | tokens moved M->S |
|---|---|---|---|---|---|---|
| A (`regrade_53.py`) | share of DOT-units in dictionary (24 units) | 0.500 | 0.070 | 0.208 / 0.250 | PASS | 20 of 124 eligible |
| B (`regrade_53b.py`) | share of letters covered by dictionary pieces >= 3 (DP segmentation) | 0.863 | 0.270 | 0.437 / 0.516 | PASS | 31 of the remaining 104 |

Per-token conditions: the token's unit (A) or covering piece of length >= 4 (B) is in the dictionary under key_53, the same
position reaches the dictionary in <= 5% of control draws, and for a pass-split row the other pass's sign does not also reach
it. Per-token rows with control rates: `regrade_53.tsv`, `regrade_53b.tsv`. Of the 10 pass-split rows, 3 moved (test B: 53_L05 pos 3, 53_L08
pos 4, 53_L10 pos 22, all SG read l vs pass B's sign 6, which is not in key_53, so condition (c) could not test the other
reading -- weaker support than the agree-flagged rows); none of the 6 splits whose other reading is in key_53 moved (G1/G7
splits both read s, so (c) blocks them by design; the split changes no letter of the reading). Moved tokens are mostly in zeittung, khomen sollen, hertzog
von, hab, werden (A) and in printzen, hispanien, wolle, konigreich, gute oder, mals, zuberzu- (B).

The 51 moved tokens are exception rows (grade S, reason "AVS53 test A/B") in `exceptions_53.tsv`, with
`exception_grade_overrides_conf` set for job 53 only; `ciphertext_53.tsv` is not edited and keeps every doubt flag.
`python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check`: "ciphertext_53.tsv: tokens 364: M 75, S 289",
"reading up to date", exit 0. `regrade_53.py --check` and `regrade_53b.py --check` exit 0. The reading text is unchanged.

**53 grades now: H 0, C 0, S 289, M 75, I 0, U 0** (was S 238, M 126). Still a cryptanalytic result (no H or C). No judge:
no `specs/` file for this target.

**Limit.** key_53 was annealed from this same transcription, so dictionary words are partly a consequence of the fit; the
control measures chance, not fitting. S here means "key_53 reads this flagged sign into a period-German word beyond chance";
the image was not re-read. The 75 M left are mostly in names and unsegmented runs (neiuuer, itc-, Vandosmen, Navarra,
geschret, mrch) and the 3 pass splits and 2 sign-9 tokens -- what the native-resolution re-read (Remaining gaps) settles.
Searched: on disk only, no network. Not found: nothing on disk extends key_53 (as NEXT-AVS found).

## AVS-SPOT: native spot re-read on f.139 (3 Oct 2026, worker AVS-SPOT, account 2, LANE-A2PUSH3)

Intake gate: `python3 tools/intake_gate_check.py august-van-saksen-1561-64` -> "august-van-saksen-1561-64: partial (line 1) --
edition/page or full-text-search citation found within 6 lines", exit 0. Pre-registration committed before the look:
prereg_avs_spot.md (06a98e4e): five spots, candidates, decision rule.
Source: 00126.pdf (resources.huygens.knaw.nl, 1 request), page 4 embedded JPEG 3840x6040 (549 ppi) extracted with pdfimages
to the scratchpad; `python3 tools/iiif_lines.py --image <scratch>/p4-000.jpg --out <scratch>/crops --prefix f139 --debug`
(9 bands, cipher lines 1-8 at region y 414-1894; overlay checked); spot crops cut from the same native image. For the f-sign
question, 00098.pdf (1 request) page 2 (f.66, 3868x2990) cut the same way (`--prefix f66 --debug`) as the reference for
98's Pf (l.2 pos 13-14, 19-20, 'ff') beside its Dp (l.2 pos 26). Nothing committed from either PDF.
Reads (this worker, 2 image reads of composite crops, no subagent; about 16 signs examined):
| spot | sign | native read | decision |
|---|---|---|---|
| S1 l.1 pos 32 | L (M) | Λ with a small dark apex but thin legs; the open Λ of l.1 pos 27 is thinner, the filled Λ of l.3 pos 30-31 (C m) carry a solid wedge; intermediate | stays M (m from 'freundtlichem') |
| S2 l.5 pos 6 | Pf (M) | loop on top of a descending stem, no stem above the loop: 98's Pf ('ff' f.66 l.2), not Dp (stem through the loop, f.139 l.3 pos 4 'Hispanien', l.7 pos 1 'purgieren') | Pf, C f ('heftig') |
| S3 l.5 pos 7 | 9 (M) | one closed upper loop and an open tail, no lower loop (not 8); same form as l.1 pos 37 | 9, C t ('heftig') |
| S4 l.8 pos 6 | Pf (M) | same loop-on-stem as S2 | Pf, C f ('frucht') |
| S5 l.6 pos 6 | Sb | clear Sb (6-shaped loop with the top flourish, as l.3 pos 3 'His-'), not Or (crossed circle) | Sb kept; 'adesn' as written, a writer's s for r (not emended) |
Why S2/S4 were M: the f-sign Pf and the p-sign Dp are both stemmed loops; the native scan separates them by whether the stem
runs through the loop. No reconciliation call was needed (the read did not split).
Effect: ciphertext_126.tsv conf M cleared at 5/6, 5/7, 8/6; `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64`
then `--check` -> "reading up to date", exit 0: **126 tokens 240: H 0, C 232, S 0, M 8, I 0, U 0** (was C 229, M 11). The German
text of reading_126.txt is unchanged. M left on 126: NW 'wir' 2, Qf 1, K 'die' 2, 1 as i 2, Λ l.1 pos 32 1.
Rule 3: this is a transcription spot check with a pre-registered rule, no solver or gate statistic; no control applies. No judge spec exists.
Requests: resources.huygens.knaw.nl 2 (00126.pdf, 00098.pdf). Vision: 2 composite reads by this worker, 0 subagent calls.

## AVS175: WVO 175 p1 aligned against key_98, gate PASS, nothing regraded (3 Oct 2026, worker AVS175, account 2, LANE-A2PUSH3)

Intake gate: `python3 tools/intake_gate_check.py august-van-saksen-1561-64` -> "partial (line 1) -- edition/page or full-text-search
citation found within 6 lines", exit 0. Pre-registration committed before any read: prereg_avs175.md (7609a09b); addendum cutting the
scope to three p1 runs, committed before the blind reads: 71de6e7c. A 15:02 ROOM line called the job halfway and stopping. That was a
clock misread, corrected in ROOM.
Source: 00175.pdf (resources.huygens.knaw.nl, 1 request), p1 f.348r 2600x4021 (366 ppi); 00098.pdf (1 request), f.66 3868x2990 for the
reference sheet. Crops: `python3 tools/iiif_lines.py --image <scratch>/p-00N.jpg --out <scratch>/crops --prefix p00N --debug` (pp.1, 3,
4, 5, 6, 8; p1 overlay checked) and `--image <scratch>/p98/q-000.jpg --prefix f66 --debug`. The cipher-only and gloss-only strips c1
(y 893-978, x 1270-2600), c2 and c3 (y 1035-1110 and 1405-1480, two halves each) were cut from p1 at native size. Nothing from either
PDF is committed.
**What p1 is:** every one of its about 14 cipher lines has a continuous gloss line above it in a second hand. So 175's glosses are a
line-by-line decipherment, not scattered word glosses. Pages 3-8 were not looked at beyond the band cut.
Reads (TRANSCRIPTION.md, one crop batch per call): 2 blind Sonnet subagent reads of c1-c3 against a reference sheet (the f.66 cipher
area with align_98.txt's codes), 1 Sonnet gloss read of the gloss strips, and reconciliation by this worker. Read A vs read B: c1 20/25,
c2 26/31, c3 25/40 signs agree (71/96, 74%). Disagreements were set to '?' (unknown), except at the two 'wir' positions (c2 pos 17,
c3 pos 1): A wrote NW, B wrote N, and this worker reconciled both as NW. The sign there is a capital-N shape, distinct from the 'v'-shaped
n later in the same lines, as on f.66 l.4. About 96 cipher signs were read. Files are in avs175/ (recon.py, recon.json, mk.py, enc.json,
prior.tsv, pairs_real.tsv, al_real.tsv, k_real.tsv, gate.py).
Gloss read (subagent; confidence c1 low, c2 medium, c3 low): c1 'Jm Crass verwardacht auch wi[?]sbrauch'; c2 'Todts vnd grosse
gefahr Leibs vnd vnser fraundlich lieb gemahl'; c3 'Vnnd Vns alltzeit [?]ersenget haben dann das die frawe Kostantin will'. This
worker's own read of the same strips: c2 'Leibs vnd gutes gefahr wir [struck: vnd] vnd vnser ...', c3 'wir vns allzeit besorget haben ...'.
Rule 3, side by side (`cd avs175 && python3 gate.py --check` -> "check OK"; tools/interlinear_align.py align --prior prior.tsv --keep-fs):
| statistic | target (175 p1 c1-c3) | rotated-gloss null (200) | shuffled-gloss null (200) |
|---|---|---|---|
| gloss-letter agreement at key_98 letter-sign positions | **0.615** (n = 65) | mean 0.345, p95 0.385 | mean 0.380, p95 0.446 |
Gate (real >= 0.60 and above both p95s): **PASS**, only just over 0.60 at n = 65. The nulls use the same key_98 prior, so they can
differ from the target, and they do. What the PASS supports: 175 p1 is written in the 98 system (key_98's letter values match its gloss
well above chance). With n this small, it supports only the values seen at aligned positions where the gloss is H-read.
The four sign questions (pre-registered rule: C only where the gloss is H-read and every aligned occurrence agrees):
| question | 175 p1 evidence | decision |
|---|---|---|
| Q1 NW 'wir' | NW twice (c2 pos 17, c3 pos 1). This worker reads 'wir' above both; the gloss reader read 'Leibs' and 'Vnnd', so the aligner paired NW with those | **stays M**: the gloss is not H-read at either position (the two reads disagree) |
| Q2 Qf | no Qf among the reconciled signs; the f of 'gefahr' (c2 pos 10) split (A Pf?, B Qg?), and this worker sees a 4-like sign there | stays M |
| Q3 K | no K among the reconciled signs (B 'NEW:K' and A 'k-like' in the c3 tail, both set to '?') | stays M |
| Q4 sign 1 | 5 aligned occurrences (c1 pos 11 and 16, c2 pos 14 and 29, c3 pos 17), all 'h' | 126's two 1-as-i stay M (context 'ihr', 'zwei'); 175 gives 1 = h at 5 of 5 and no i |
Logged only, because not pre-registered: HX aligns to 'vns' at c3 pos 1 (both gloss reads agree), matching key_98's HX = uns (98, n=1, M).
126 has no HX, so this does not affect the targets. Sign 4 aligns once to 'e' (c3 pos 12), against key_98's 4 = o (n=28). That is a single
position next to a '?' and was not acted on.
`python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` -> "reading up to date", exit 0: 126 C 232 M 8, 57 C 247 M 53,
53 S 289 M 75 (unchanged; no key or exception file touched).
Requests: resources.huygens.knaw.nl 2 (00175.pdf, 00098.pdf). Vision: this worker made 9 image reads (2 overlays, 7 crops/strips) and
3 subagent calls (2 cipher reads, 1 gloss read), covering about 96 cipher signs and 3 gloss lines.
Next (named, costed): Q1 turns on one gloss word, so the cheapest step is a second independent gloss read of the c2 and c3 strips by a
German palaeography pass (1 call, ~$1.5). If it reads 'wir' at both positions, NW moves to C under this same gate. After that, the other
11 p1 lines (about 450 signs: 2 blind reads in 4-line batches, 1 gloss read, 1 reconciliation, ~$12, box 75 min) for Qf and K, then pp.3-8.

## AVS175B: second gloss read of WVO 175 p1 c2/c3, NW moves to C (3 Oct 2026, worker AVS175B, account 2, LANE-A2PUSH3)

Pre-registration: prereg_avs175.md addendum "AVS175B", committed 368e1578 before the read. Rule: NW goes from M to C only if this read gives
'wir' (clear or probable) over both NW positions (c2 pos 17, c3 pos 1) AND AVS175's reconciliation read 'wir' there. AVS175's gate
(0.615 vs null p95 0.385/0.446) is not re-run. Q2 Qf and Q3 K cannot move (no cipher re-read), and Q4 is untouched.
Source: AVS175's c2/c3 strips were in its own container's scratchpad and were not on disk here, so 00175.pdf was fetched again
(resources.huygens.knaw.nl, 1 request) and its p1 extracted (2600x4021, 366 ppi). Crops: `python3 tools/iiif_lines.py --image
<scratch>/p-000.jpg --region 0,850,2600,700 --out <scratch>/crops --prefix p1 --debug` (overlay checked: gloss c2 at y~985, cipher c2
y~1066, gloss c3 y~1379, cipher c3 y~1465), then gloss-only strips `--region 400,945,2200,95 --prefix g2` and `--region
400,1335,2200,85 --prefix g3` (2200x90 and 2200x85). Nothing from the PDF is committed.
Read: 1 blind Opus subagent call (German palaeography), given only the two gloss strips. It saw no cipher, no key and no earlier read.
| gloss word | AVS175 gloss read | AVS175 reconciliation | AVS175B read (legibility) | H-read 'wir'? |
|---|---|---|---|---|
| c2 word over NW (pos 17) | 'Leibs' (aligner pairing) | wir | **wir** (probable; alt 'wie'/'wer', short last stroke) | yes |
| c3 word over NW (pos 1) | 'Vnnd' | wir | **wir** (probable; run together with the next word, 'vns') | yes |
Full AVS175B gloss: c2 'leibs vnd gutes gefahr wir [struck: wol?] vnd vnser freuntlich lieb gemahl'; c3 'wir vns allzeit befingt[?]
habenn das die fraw Koppentin[?] mitt'. This matches AVS175's reconciliation word for word at the two positions, and at 'vns' (c3, HX).
Decision under the rule: both positions H-read 'wir', so **NW = wir moves to C**. Implemented as pairs_175.tsv, which holds only the two
licensed NW rows (no other 175 sign enters), with build_key.py's System B now taking pairs_175.tsv. `python3 build_key.py` changed
only NW (key.tsv: 'NW wir M 1' -> 'NW wir C 3 wir:2,wir~:1'), and `build_key.py --check` exits 0.
`python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` -> "reading up to date", exit 0: **126 tokens 240: C 234, M 6**
(was C 232, M 8; the German text of reading_126.txt is unchanged), 57 C 247 M 53, 53 S 289 M 75. 126 M left: Qf 1, K 'die' 2, 1 as i 2,
Λ l.1 pos 32 1. Rule 3: the control for this decision is AVS175's passed gate (target 0.615 vs rotated-gloss p95 0.385 and
shuffled-gloss p95 0.446, n = 65). This read adds no new statistic.
Logged only, not pre-registered: the c3 cipher line on the iiif_lines overlay seems to carry a K-shaped sign in its tail ('... v e K q
...'), where AVS175's two reads split (B 'NEW:K', A 'k-like', set to '?'), with the gloss 'fraw Koppentin[?]' running above it. This may
help Q3 when the other p1 lines are read; nothing was regraded on it.
Requests: resources.huygens.knaw.nl 1. Vision: this worker made 3 image reads (1 overlay, 2 strips), plus 1 subagent call covering 2
gloss lines (21 words).

## Remaining gaps (finish-or-blocker pass, 1 Oct 2026)
Read so far: 770 of 904 cipher tokens firm (85.2%: C 481 + S 289), M 134, U 0 (AVS175B, 3 Oct 2026: NW = wir C from WVO 175 p1, 126 C 234 M 6; AVS-SPOT, 3 Oct 2026: 126's three f.139 spots C; AVS53, 3 Oct 2026: 53's regrade, decode_key.py --check exit 0; figures below from earlier runs except 53's), from `python3 tools/decode_key.py ciphers/august-van-saksen-1561-64 --check` (rerun 2 Oct 2026 23:0x UTC by A2-AVS4, exit 0, "reading up to date"): 126 C 234 of 240 (97.5%, AVS175B 3 Oct 2026; key_98 from the decipherments f.67 and, since A2-AVS4, WVO 124 f.135; filled-Λ m and down-arrow k from A2-AVS3), 57 C 247 of 300 (82.3%, key_74 from f.19), 53 S 238 of 364 (65.4%, no H or C: a cryptanalytic result; matched control 280/282, 99.3%, solve_53_control.json)
- 53 p1+p2 (f.266r-v, 13 cipher lines; 126 M, 75 since AVS53's key_53 dictionary regrade on 3 Oct 2026 (51 to S, prereg_avs53.md; the regrade does not replace an image re-read), incl. 'zuberzuschreiben' l.2, 'geschret' l.7, 'mrch' L10 pos 26) - blocker: not-attempted; passes cut from the 100 dpi images/00053_p1.png (passbrief_s1.md, 90.9% agreement, recon53/disagreements.tsv 28 rows), p2 read once at 100 dpi (F1); the native JPEG (2567x4187, about 309 dpi, images/manifest.json) was never used for passes, and S1's own suggestion ("a native-resolution re-read ... would settle the 119 M tokens") and SO-SAXONY-53-57's spot checks were never run; next: fetch 00053.pdf once, `tools/iiif_lines.py --image` crops pasted, two blind passes per page + one reconciliation (5 subagent calls at about $1.46 each), tools/reconcile_passes.py, then decode_key.py --check and regrade, ~$9
- 53 key (key_53.tsv, 20 signs all S; sign 9 = f by context, exceptions_53.tsv) - blocker: not-attempted on the only route left; the WVO 58 route was run 2 Oct 2026 (NEXT-AVS step above): 58 is System A, read by key_74 (46/60 letter-words match its f.272 decipherment; key_53 0/60; shuffled-key control mean 0.18/60), so 58 cannot extend key_53 and no sibling with a decipherment shares 53's system (74, 98, 153, 175, 58 all checked); next: the 53 native re-read (gap above) and the KHA Japikse copy of 53 (ASKS 67); a solver re-run is not a next step while the transcription carries 126 M
- 57 p3 (KHA A 11/XIV B/41-6, 7 lines; 48 transcription-doubt M) - blocker: not-attempted; passA_57/passB_57 agree on 84.8% of columns (recon57/disagreements.tsv, 49 rows), cut from the 100 dpi images/00057_p3.png (passbrief_s1.md); R21 fetched native scans for 74/98/126/53 only, never 57 (R21 "Requests"); next: fetch 00057.pdf, crop p3's 7 lines with `tools/iiif_lines.py --image`, two blind passes + one reconciliation (3 subagent calls), decode_key.py --check, regrade, ~$6
- 57 p3 word signs outside key_74 (OQ 'wir', THE x2 'Keiser', BOX 'Churfurs-', G1h 'x'; 5 tokens M by context, exceptions_57.tsv) - blocker: waiting-on the Dresden Hauptstaatsarchiv's reply on the minute of WVO 57 (Loc. 9941/3 Bl. 268r-269v 'Zettel', request sent 26 Sept 2026 18:20 UTC, CONTRIBUTIONS.md 'Dresden minute of WVO 57', outreach/dresden-wvo57-minute.md 'reply pending'); both internal sibling routes are now run and negative: WVO 58 (NEXT-AVS, 2 Oct 2026: System A, OQ/THE/BOX absent from all 15 lines) and WVO 175 (A2-AVS-2, 2 Oct 2026: OQ/THE/BOX absent from all of its about 45 glossed cipher lines, p1-p8, while the same 100 dpi eye finds all three on 57's own crops; 'Chur und Fürsten' glossed 3 times and 'wir' 4+ times over runs with no such sign; 175 is not System A, it writes -en as 3v and und as M); signs absent from 74 (ciphertext_74.tsv has no OQ/THE/BOX/G1h); no other deciphered System A sibling is known
- 126 p4 (f.139) key-level M left after A2-AVS3 (word sign K 'die' 2, sign 1 as i 2, Λ l.1 pos 32 1; exceptions_126.tsv) - blocker: waiting-on ASKS row 67 (the KHA copies and minute of 126 would give these words in clear); WVO 124 was fetched and aligned 2 Oct 2026 (A2-AVS3 step above): it is System B with its own decipherment f.135, and it settled the filled-Λ m (8 tokens) and the down-arrow (k, 'kranck worden'), but it attests K once as 'der' (a conflict with 126's context 'die', held M) and 1 = i once (both values now period-attested, the choice in 126 is context); no further K or 1-as-i occurs on f.134 to align, and Groen I 231-233 prints only the clear letter. The remaining route inside the session for these five is WVO 175 (see the next gap and siblings)
- 126 p4: 1 M token left from key_98 (Qf 1; NW 'wir' 2 moved to C by AVS175B, 3 Oct 2026: a second blind gloss read gives 'wir' over both NW positions of WVO 175 p1, prereg_avs175.md addendum) plus 1 transcription-doubt M on f.139 (Λ l.1 pos 32: AVS-SPOT, 3 Oct 2026, read it at native resolution and found the apex fill intermediate between the open Λ and the filled Λ of l.3 pos 30-31, so it stays M under the pre-registered rule; Pf l.5 pos 6, Pf l.8 pos 6 and 9 l.5 pos 7 moved to C, and 'adesn' l.6 pos 6 confirmed as a clear Sb, a writer's s for r) - blocker: not-attempted; NW and Qf have no aligned occurrence yet, and the one Λ is a stroke-weight call the native scan does not settle (context 'freundtlichem' gives m, the KHA copies of ASKS 67 would give it in clear); NW done (AVS175B, 3 Oct 2026); next: the other 11 lines of WVO 175 p1 for Qf (and K: a K-shaped sign sits in the c3 tail under 'Koppentin[?]'), 2 blind reads in 4-line batches + 1 gloss read + 1 reconciliation, ~$12, box 75 min
- 53 and 126 as whole texts, independent period witness (KHA Collectie Japikse copies of 53 and 126; KHA minute A 11/XIV I/4 nr. 26 of 126 "met een 'Zeitung'") - blocker: waiting-on ASKS row 67 (dr. Huysman's reply on a KHA route, asked 26 Sept 2026 about 15:00 UTC, outreach/huygens-reply-2026-09-26.md); the KHA is not online; AUDIT.md V-GATE2 ruling keeps N4 with the copies named as an unseen witness; the internal key-level routes for these letters are the WVO 58 and WVO 124 gaps above

## Escalation (1 Oct 2026)
- [ ] siblings: opened 74, 98, 153, 175 (R9, images/inventory.tsv); 74 (f.18/f.19) and 98 (f.66/f.67) are the key sources for 57 and 126 (R21); 153 (1566, overlined numerals) is a different design; Orange's 1561 Schwarzburg key is not an August system (ciphers/gunther-van-schwarzburg-1561/NOTES.md step 2). WVO 58 (31 Dec 1561) fetched and trial-decoded 2 Oct 2026 (NEXT-AVS): System A, key_74 reads it against its own f.272 decipherment (46/60 letter-words; key_53 0/60); a fifth deciphered System A witness for the key register, nothing for 53's system or 57's word signs. WVO 175 compared 2 Oct 2026 (A2-AVS-2) from the 100 dpi disk images: no OQ/THE/BOX in any glossed run (detection control: all three seen on 57's own crops), not System A, possibly System B (two run-end words read with key_98's digits). WVO 124 (16 Apr 1564) fetched 2 Oct 2026 (A2-AVS3): f.134 is System B, f.135 its decipherment (Groen prints only the clear letter); it settled 126's filled Λ and down-arrow, not K or 1-as-i. align_124.txt written 2 Oct 2026 (A2-AVS4): 679 signs against f.135, key_98 rebuilt from 98 + 124 (EL8, R now C; PAPE, K, S added). WVO 175 fetched at native resolution and cropped 3 Oct 2026 (AVS175): p1 carries a line-by-line gloss over about 14 cipher lines (6 pages, about 45 lines), so 175 is a near-full interlinear decipherment. Three p1 runs aligned against key_98 (avs175/gate.py): gate PASS 0.615 (n=65) vs rotated p95 0.385 and shuffled p95 0.446, so 175 is the 98 system; NW seen twice under a gloss word the two reads split on (M kept), sign 1 = h 5 of 5, no Qf or K among the reconciled signs. AVS175B (3 Oct 2026): second gloss read gives 'wir' at both NW positions, NW = wir C. Planned: the other 11 p1 lines for Qf and K
- [x] clear-pages: 74 f.19 and 98 f.67 identified as the contemporary decipherments and aligned (R21); plaintext_98.txt (ff.68-69) shown to be an enclosed newsletter, not 98's decipherment; the clear text beside each target (53 p2 autograph postscript, 57 p3 signed clear postscript, 126 pp1-3) checked and none is the decipherment (inventory.tsv, S1, A2). The minutes that may carry plaintext are outside: Dresden 'Zettel' of 57 (reply pending), KHA minute and Japikse copies of 126 and 53 (ASKS 67). 126's interlinear "e e r e" above l.1 (later hand?) contradicts the key and was not used (R21)
- [x] known-keys: tools/key_crossmatch.py ran every on-disk key against ciphertext_53/57/126 (KEY-CROSSMATCH.tsv); only each text's own key reads it (key_74 on 53: z -4.47, "uettelah?e.znnregu..."; key_98 on 53: z 0.74); the Schwarzburg 1561 key differs in form; the four keys are in KEY-OFFICES.tsv and KEY-DESIGN.tsv; Cryptiana dutch.htm, DECODE and both solver repositories: no hits (check-solved)
- [x] print: Groen, Gachard, Rachfahl (II.1 through HTRC tokens only), von Weber, Kluckhohn I, Goetz 1891, Japikse I (ends Sept 1561), Demandt nrs 113/115 (clear text only), Kervyn II, Weiss, Ritter, Kruse, 24 Google Books gist queries, phrase searches, JSTOR rows 48/49/55/56/63/64/69; no prior decipherment located (AUDIT.md V3, A2, A3, D1, D2, V-GATE2). Groen's printed text of WVO 124 not yet used as a key source (siblings). "While waiting" bullet 3 (closer Rachfahl II.1 HTRC scan) is optional print work, not a reading step
- [ ] key-rebuild: done for 53 (tools/homophonic_anneal.py, 4 of 6 restarts converge, matched control 280/282; G6 = k by context). Not done: 57's five word signs and 126's K and 1-as-i are context-only (Λ filled = m and the down-arrow = k settled from WVO 124, A2-AVS3, 2 Oct 2026); key_98 extended from WVO 124 (align_124.txt, A2-AVS4, 2 Oct 2026: EL8 das and R E.L. now C, PAPE/K/S added; 9, Pf, M, Ma confirmed); the 98-only '~' units that 124 does not contain (NW, Qf, Mf, HX, Dl, Sg, BAR) stay M because f.67 was never transcribed. Planned: settle the rest from an f.67 transcription or WVO 175 (WVO 58 does not share 53's system, 2 Oct 2026, so key_53 cannot be extended from a sibling; 58 would extend key_74 by two word signs, fried and Religion, at grade C once aligned, a key-register job with no effect on the three targets). No instrument here has failed its own gate even once, so nothing is retired
- [ ] image-check: R21 read 126 once at native resolution; S1 settled pass disagreements on 100 dpi crops (settle_53.py, settle_57.py). Not done: native-resolution passes for 53 (p1 and p2) and 57 p3; the SO-SAXONY-53-57 spots (l.2, l.7, L10 pos 26) never applied ('slagen' and the down-arrow settled on the native f.139 scan by A2-AVS3, 2 Oct 2026; 'adesn' and the four f.139 conf-M signs re-read natively by AVS-SPOT, 3 Oct 2026: 3 to C, 'adesn' a clear Sb, Λ l.1 pos 32 stays M). Planned: native crops and two passes for 53 and 57. "While waiting" bullet 1 (run key_53 on f.266v) is stale: F1 did it 24 Sept 2026
- [ ] retry: AVS53 (3 Oct 2026) re-ran decode_key.py --check after a pre-registered key_53 dictionary regrade of 53 (tests A and B, band-permuted control, 1000 draws, both gates PASS; 51 tokens M->S, 53 now S 289 M 75; NOTES "AVS53"). no unread groups (U 0); decode_key.py --check exits 0 on an unchanged key and transcription (unchanged since 24 Sept 2026). Planned: rerun decode_key.py --check and regrade all three letters after each image-check or key extension above
Verdict: keep going: 4 internal gaps (126's '~' key units EL8 and R settled at C from WVO 124 f.134/f.135, A2-AVS4, 2 Oct 2026; 126 now C 234 M 6 after AVS-SPOT's native f.139 spot re-read and AVS175B's NW decision (WVO 175 p1 second gloss read), 3 Oct 2026; 53 now S 289 M 75 after AVS53's pre-registered key_53 dictionary regrade, 3 Oct 2026); cheapest next: the other 11 lines of WVO 175 p1 for Qf and K (2 blind reads in 4-line batches, 1 gloss read, 1 reconciliation), ~$12, box 75 min; for 53, the native-resolution re-read of its 75 M (names, unsegmented runs, 3 SG/6 splits), ~$9

## Web and blog check (GF-A2-1, 2 Oct 2026)

Run 2 Oct 2026, 21:14-21:19 UTC (date -u; committed 59dd17c3), by worker GF-A2-1 (account 2, LANE-A2PUSH). Plain web searches (one search engine):
1. `"August" Sachsen "Wilhelm von Oranien" 1561 Chiffre Brief Geheimschrift` (sender + recipient + date) -- hits: WVO edition PDFs
   01309/05175 (other letters), Sternberg *Land Nassau*, BMGN 2009, generic Geheimschrift PDFs, and Anne-Simone Rous,
   "Geheimschriften in sächsischen Akten der Neuzeit", *Neues Archiv für sächsische Geschichte* (nasg.publia.org, article 781,
   pp. c.243-253). Rous opened and read in full (pdftotext): see the Premise check, item (a) -- a period cipher alphabet "zwischen
   dem sächsischen Kurfürsten und dem Prinzen von Oranien" in Dresden Loc. 8485/4 fol. 25, 44; no decipherment of any letter in
   this folder.
2. `"Locat 9941" Dresden Oranien cijferschrift OR Chiffre` (shelfmark + cipher) -- hits: WVO PDFs 00010-00078 and one DDB item;
   catalogue scans only, no solution text.
3. `Willem van Oranje August van Saksen cijferschrift brief 1564 ontcijferd` (folder title, Dutch) -- hits: school material,
   Prinsenhof Delft, WVO edition PDFs for other letters, the WVO project pages; nothing on 53/57/126.
4. `"Kurfürst August" "Oranien" Chiffrenbriefe entziffert 1561 Torgau Breda` (distinctive terms) -- hits: Rous again, Groen
   Archives III on DBNL (1567-1572, outside these dates), CSP Foreign 1579, unrelated cipher pages; nothing on these letters.
5. `"8485/4" Characteres verborgene Ziphern Hauptstaatsarchiv Dresden` (Rous's key file) -- only WVO PDFs and one DDB item;
   the file's own online catalogue record not located this pass.
No distinctive decoded phrase was searched in quotes beyond the above: the readings are German chancery prose with no
phrase distinctive enough to search (e.g. 'Churfurs-', 'Keiser').
Blog site searches: **Cipherbrain** (`site:scienceblogs.de klausis-krypto-kolumne Oranien Sachsen`) -- author index pages
only and a 1797 cryptogram post, no post on Orange/Saxony; **Cryptiana blog** (`site:cryptiana.blogspot.com Orange Saxony
cipher`) -- no blogspot hit at all (search returned Wikipedia's list, a Cipherbrain post on Tomokiyo's list, Tartu items);
Tomokiyo's dutch.htm page was read in full on 24 Sept 2026 (check-solved item 3) with no mention; **Cipher Mysteries**
(`site:ciphermysteries.com William of Orange cipher Saxony`) -- one plausible-looking hit, ciphermysteries.com/?p=4842,
opened: "Historical Cryptography Conference in Gotha" (Feb 2013), post and comments read, no mention of Orange, August or
these letters. No comment thread anywhere carries a decipherment or plaintext of 53, 57 or 126.
Requests: nasg.publia.org 1 (plus 2 redirects from journals.qucosa.de), ciphermysteries.com 1, search engine 6.

## Premise check (GF-A2-1, 2 Oct 2026)

(a) Decipherments the folder already mentions -- **found, all already used or already pending; one key lead not on file.**
Opened in the files: 74 f.19 and 98 f.67 are the contemporary decipherments of the siblings and are the key sources for 57
and 126 (R21, key_74/key_98); plaintext_98.txt ff.68-69 is an enclosed newsletter, not 98's decipherment; 126's interlinear
"e e r e" contradicts the key (R21); none of these decipher 53, 57 p3 or 126 p4 themselves. Pending outside: Dresden
'Zettel' of 57 (Loc. 9941/3 Bl. 268r-269v, reply pending) and the KHA Japikse copies and minute of 126/53 (ASKS 67).
New lead from the web check: Rous (NASG, above, footnote 9) reports that Dresden, Geheimer Rat, **Loc. 8485/4** "Characteres
vnnd verborgene Ziphern so inn der Churfürstlichen sächsischen Canzley ... gebraucht worden seindt" holds, among many
nomenclators, "eines [Alphabets] zwischen dem sächsischen Kurfürsten und dem Prinzen von Oranien" at **fol. 25, 44**. This
is a period key sheet for the very correspondence (which system -- A, B or 53's -- is not said, nor the date); it is a key
source, not a decipherment of any of the three letters, so it does not make the item found-solved. Not in this folder, not
in any ciphers/*/NOTES.md (grep '8485', 2 Oct 2026). Next: ask Dresden for fol. 25 and 44 alongside the pending 57 'Zettel'
request (outreach/dresden-wvo57-minute.md) -- an owner-side step, the parent decides.
(b) Other solvers' working files -- **not found.** Shallow clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers
(2 Oct 2026, 21:16 UTC) grepped for August/Orange/Oranien/Sachsen/Saxony pairings and 'wvo': no target folder, no
rendering, no key for this correspondence in either (cs/targets has no Saxon or WVO folder; Aymeloglu: no hit; cited only).
(c) Physical neighbours -- **partly checked, nothing found.** The WVO scans are per letter; 58 (Loc. 9941/3 f.271-272, the
next letter of the same file) was fetched and read 2 Oct 2026 (NEXT-AVS): its decipherment is of 58 only. The clear
pages beside each cipher (53 p2 autograph, 57 p3 signed clear postscript, 126 pp.1-3) were checked and none is the
decipherment (A2, inventory.tsv). Leaves of Loc. 9941/3 and 8510/5 outside the WVO PDFs are not online (not viewed).
(d) Recipient side -- **not found.** 53 and 126 went to August (Saxon side: von Weber, Kluckhohn I, Goetz 1891, Ritter,
Kruse read in the print sweep, AUDIT.md V3/A2/A3/D1/D2); 57 went to Willem (Groen, Gachard, Japikse I, Demandt nrs 113/115,
Kervyn II read). No recipient-side edition prints a decipherment of the cipher passages.

## N4-XM (key_crossmatch lead of 4 Oct 2026 02:53, account 2 worker for LANE-NEAR4, 4 Oct 2026)
Lead: `ciphers/fr3993-villeroy-1595/keys/key_f159_letters.tsv` (fr.3995 f159 letter strip) reaching the calibrated
key_crossmatch gate (stat >= 3.292) on AVS ciphertext_58_sample / 74 / 57. Pre-registered in
`ciphers/august-van-saksen-1561-64/xmatch/PREREG.md` (commit fff1002d; amendment A ed5e6de1 before any control
statistic), script `xmatch/xm_control.py`, numbers `xmatch/xm_control.json`, eye read `xmatch/eye74.tsv`.
Target vs control, same tool functions (`pair_stats`, 20 class-shuffled keys, seed 0): f159 reproduces the nightly
exactly, stat 8.66 / 7.22 / 6.48 (cov 0.565 / 0.515 / 0.573; all from the letter 4-gram z, value-frequency z only
2.0 / 1.96 / 1.71). Size-matched control: no other letter-alphabet key of 20-58 letters on disk (84 checked) reaches
coverage 0.5 on any of the three texts, so under amendment A the three real distinct-folder keys with the highest
coverage were scored with the floor bypassed: dupuy468-anhalt key_from_gloss (cov 0.41-0.43) stat -0.70 to -0.37;
decode-1168-modena-costabili key (0.39-0.48) -0.25 to 0.14; na-suriname-map key_period_codes (0.36-0.40) 1.47 to
1.93 (under f159's fr model: all <= 0.89). By the pre-registered rule the lead survives the size-matched control
(control max 1.93 vs gate 3.292). Read by eye: f159 covers only 8 AVS sign types (1, 3-8 and V) and sends all
445 covered ct74 tokens to four letters (o, i, l, t); under AVS's own key_74 the same tokens are e, a, n, l, h, c,
b, r. Agreement letter for letter: 0 of 30 (first 30 tokens) and 0 of 445 (all covered tokens). The first 60
tokens decode under key_74 as "die drey thausent spanier welche unser K dem frantzosen zhulff sickt..." and under
f159 as "..o.to..lo..oi...oi.ot.oillo.i.ot.." -- no text. f159 is a homophonic letter alphabet (figures 1-19 as
homophones of a b c d e i l o; named symbols for the other letters) whose figures overlap the AVS notation by
form only. Verdict: the tool's statistic reaches the gate and the size-matched controls do not, but the eye read
shows no shared alphabet; the stat is driven by a key that puts only frequent letters (o, i, l, t) on the few AVS
signs it covers, which the class-shuffled null (it moves q, x, y, z onto those figures too) cannot match. Not a
lead. Suggestion for the tool (one line, not done): add a minimum count of distinct covered sign types, or shuffle
the null only among the codes the ciphertext actually covers. Requests: none (offline). Subagent calls: 0.

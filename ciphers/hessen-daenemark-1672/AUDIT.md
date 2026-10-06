# AUDIT -- hessen-daenemark-1672 (HStAM 4 f Staaten D, Dänemark 125, ff.2-4; HCPortal cryptogram 494)

Verifier: VERIFY-HDK (account-4 verifier session, 3 Oct 2026, 16:55-17:25 UTC). Separate from the solver sessions
(A2-HDK, GAPS152/155/159/163/168). Brief: re-derive (rule 7), audit the controls (rule 3), grade (rule 4), classify
novelty (rule 10).

Claim under audit (GAPS159/163/168, ROOM 16:07-16:37 UTC 3 Oct 2026): "pages 1-3 (65 groups) decoded with a key built
from the letters' own period interlinear glosses (key_gloss.tsv 19 rows: C 11, M 7, I 1); tokens C 9 I 1 M 23 S 30 U 2;
pooled gloss held-out 8/8 vs shuffled-gloss mean 0.36, P<0.0001 (6/6 without the 690 override); 229/303 conflict with
key 255."

## Verdict table

| item | what it is | N-class | key | grade counts after audit |
|---|---|---|---|---|
| Nomenclator readings, ff.2-4 (26 tokens) | the period gloss over each code, transcribed | **N0** | period | carried in the 65-token totals below |
| Letter-cipher runs 1-2, f.4 (37 tokens) | key 255's 1666 letter table applied; the leaf's own margin/interlinear gloss already gives the same text | **N0** | period | as below |
| Key identification: HCPortal key 255's letter table reads cryptogram 494's 2-digit groups | a mapping between two catalogued items | not a novelty item (a contribution); HCPortal 494 carries `cipher_key_id: null` and no repository or catalogue searched links the two | period (key 255 = HStAM 4 d Nr. 1234 ff.13-16, "Clavis ... mit Secretario Lincker 1666") | -- |

Token grades after this audit: **65 tokens: C 9, I 1, M 25, S 28, U 2** (was S 30, M 23: two contradicted cells
regraded, below). Key source: `period` -- the nomenclator values come from the bold glosses written on the leaf, the
letter values from a Kassel chancery key of 1666 endorsed for the same secretary. `text: known` -- the plaintext of every
enciphered passage is already written on the document itself.

**Did we first-decipher?** No. The leaf carries its own decipherment: every nomenclator group but four (625 p3:4, 602
p3:26.3, 634, 68) has a gloss over it, and both letter-cipher runs carry a margin or interlinear gloss ("disgustirt /
unvertanin / Holstein"; "gott geb das amm.. / w o .. a b l au t"). HCPortal labels the item "Partially solved" for
the same reason. What the repository adds is a two-pass transcription of the codes and glosses, the identification of
the 1666 letter table as the one in use, and the logged conflicts between this letter's nomenclator and key 255's.

## 1. Re-derivation (rule 7)

From committed files only:
```
$ python3 tools/decode_key.py ciphers/hessen-daenemark-1672 --check      (before this audit)
ciphertext.tsv: tokens 65: C 9, I 1, M 23, S 30, U 2
reading up to date                                                        EXIT 0
$ python3 ciphers/hessen-daenemark-1672/keys/merge_pages.py --check       EXIT 0
$ python3 keys/gloss_heldout.py --seed 31          held-out 8/8; control mean 0.369, p95 2, P(ctrl>=8) 0.0000
$ python3 keys/gloss_heldout.py --seed 31 --set p2:25.2=650      6/6; control mean 0.280, p95 2, P 0.0000
$ python3 keys/gloss_heldout.py --seed 4242        8/8; control mean 0.380, p95 2, P 0.0000
$ python3 keys/gloss_heldout.py --seed 4242 --set p2:25.2=650    6/6; control mean 0.288, P 0.0001
$ python3 keys/key255_gloss_test.py --notes --quiet
pairs 26  key255 matches 21  control mean 1.05  control max 10  p(control>=real) 0.00005
```
key_gloss.tsv counted by hand: C 11 (229 447 601 605 651 653 681 774 775 834 5756), M 7 (303 437 641 602 625 690 768),
I 1 (634) -- matches the claim. **Reproduced exactly**, with new seeds. After this audit's exceptions.tsv:
`tokens 65: C 9, I 1, M 25, S 28, U 2`, `reading up to date`, exit 0.

## 2. Control audit (rule 3)

Script: `keys/verify_hdk_controls.py` (new, committed; `--seed`).

**(a) Gloss held-out.** The control can vary on the statistic (glosses permuted over fixed codes), and its floor is low
(0.37 of 8), so this is not the AX-NAMES majority-class shape. But "8/8" counts each agreeing pair twice (each
occurrence predicts the other). Per code:

| code | occurrences | glosses | agree | note |
|---|---|---|---|---|
| 690 | p1:21.1, p2:25.2 | Bleinenk??l / Bleinenk?fl | yes | **circular**: p2:25.2 was read 650 by both passes and changed to 690 by the reconciler partly on the gloss |
| 651 | p2:3.1, p2:25.1 | Cur Brandenburg x2 | yes | p2:3.1 sign M (alt 657) |
| 229 | p2:17.1, p3:5.1 | Berlin x2 | yes | both signs M |
| 601 | p3:3.1, p3:17.3 | Dennemarck x2 | yes | |

So the honest figure is **4/4 agreeing pairs, 3/3 without the 690 override**. A random pair of the 20 glosses agrees
with probability 9/190 = 0.047 (the Kurbrandenburg variants make up 6 of the 9 matching pairs), so three independent
agreements by chance is about 1e-4 -- the claim's P holds at the pair level. What it licenses is narrow: the glossing
hand writes the same value over the same code on three codes. It says nothing about any singly attested code (12 of the
16 glossed values occur once), and it cannot test whether a gloss is correct, only that it is code-consistent. That is
what GAPS159 itself said; the "8/8" headline should be quoted as "3 recurring codes (4 with 690), all consistent".

**(b) The 30 S tokens.** S rests on A2-HDK's relabelled-table control (21/26 on readings fixed before key 255 was seen,
control max 10). That test's 26 (token, gloss-letter) pairs were **chosen by the solver after seeing key 255** (its own
caveat), and they omit exactly the run tokens where table and gloss disagree (60, 66, 113, LL, 55, 69, 76, 6, NN), so its
P-value is inflated by selection. Selection-free re-test here: decode **every** 2-digit/doubled-letter token of each run
in order and score the longest common subsequence against the gloss string; control = the same 24-label permutation,
20,000 draws, seeds 4 and 99:

| run | tokens | gloss string | LCS real | control mean | control p99 / max | P |
|---|---|---|---|---|---|---|
| 1 | 19 | disgustirtundertanin | 17 | 4.71 | 8 / 11-12 | <5e-5 |
| 1 | 19 | disgustirtunvertanin | 16 | 4.48 | 8 / 10-11 | <5e-5 |
| 2 | 18 | gottgebdasammwoablaut | 14 | 4.42 | 7 / 9-11 | <5e-5 |

The 1666 table survives the selection-free test decisively, so S is licensed for the table as a whole (a key of the
same office tested against an independent known plaintext with a control). **Not licensed at S: the cells the letter's
own gloss contradicts.** Regraded S -> M in `exceptions.tsv` (value unchanged): p3_20 pos 2 (55: table h, gloss g;
GAPS168 zoom says the sign is clearly 55) and p3_21 pos 7 (6: table NULL, gloss t). 69 (table k, under "ott") was
already M. Note: S here is a key-identification grade, not cryptanalysis; were the table dated 1672 it would be H.

**(c) Gloss hand.** One look by this verifier at crop `images/crops_p3/p3_L08.jpg`: the margin gloss "disgustirt /
unvertanin / Holstein" is in brown iron-gall ink of the same tone as the letter, in a 17th-century hand -- period in
appearance (M, one eye). That supports the `period` key label; it does not name the decipherer (Vultejus's chancery is
the obvious candidate, not established).

**(d) Conflicts with key 255** (229 Berlin vs Frankreich, C 2/2 vs key; 303 allian?e vs Munster, M vs M): correctly
logged in HYPOTHESES.md as data conflicts with witnesses and not merged (rule 4). No change.

## 3. Novelty search log (3 Oct 2026, 16:58-17:10 UTC)

| family | searched | result |
|---|---|---|
| Solver repos (Bourdeau, Aymeloglu), Cryptiana, HCPortal API, DECODE | relied on the solvers' logged checks of 26 Sept and 2 Oct 2026 (NOTES.md search log, siblings lookup, A2-HDK); not re-cloned | Bourdeau #341 "partly solved on HCPortal", no key or reading; Aymeloglu 0; HCPortal 494 "Partially solved", `cipher_key_id` null; DECODE: no 4 f record |
| Holding archive (Arcinsys Hessen) | solvers' record v1881503 read 2 Oct 2026 | summary "schreibt über auswärtige Politik (z. Th. in Chiffern)", no decipherment noted |
| Google Books API (key, country=US) | "Lincker" Vultejus 1672; "Linker" Vultejus Hamburg 1672; "disgustirt"; Lyncker Rendsburg Landtag 1672 Hessen; Hessen-Kassel Dänemark 1672 Chiffre; "Hertzog von Ploen" 1672; "Lincker" Dänemark 1672; "Linker" Kopenhagen Hessen 1672; "Lincker" Hamburg 1672 Kassel; Rommel ... Lincker Dänemark | no print of this letter. Leads: *Repertorien des Hessischen Staatsarchivs Marburg* (1960, the finding aid); *Repertorium der diplomatischen Vertreter* (1936: Lincker Georg, Sekr.); Laursen, *Danmark-Norges Traktater* (1923) and Wegener, *Aarsberetninger fra Geheimearchiv* (1882) mention Lincker's 1672 mission from the Danish side; *Frankreich und die Reichsstände 1672-1675* (1981) mentions Lincker; UA Friedrich Wilhelm (Krosigk, Sept 1672, Plön) |
| Internet Archive full text (be-api fts) | "Lincker" Vultejus; "Linker" Vultejus; disgustirt Holstein; "Secretarius Lincker"; Lyncker Rendsburg 1672; "Lincker" Dennemarck; "Linker" Landgräfin 1672 Dänemark; "Ahlefeldt" Lincker; Ribbeck Lincker | no print of this letter. Lead: UA Friedrich Wilhelm vol. (urkundenundacte30kommgoog) footnote "Georg Lincker. S. Ribbeck, Aus Berichten des hessischen Sekretärs Lincker (Forsch. XII ...)" -- Ribbeck's article in *Forschungen zur brandenburgischen und preussischen Geschichte* 12 prints extracts of Lincker's reports; its date range was not confirmed here (the footnote context is Berlin; this letter is Hamburg, May 1672) |
| OpenAlex (key, header) | Hessen-Kassel Lincker Denmark 1672; Hessian chancery cipher seventeenth century Marburg; Hessen-Kassel Dänemark 1672 Gesandtschaft | 0 / 0 / 5 unrelated |
| Semantic Scholar (key) | same three | 0 / none / 0 |
| JSTOR | not reachable from the cloud | 2 rows queued in JSTOR-QUEUE.tsv (family i metadata; family ii exact phrase) |
| HathiTrust full text | not reachable from the cloud (Cloudflare) | not searched |

No printed edition, article or project page reproducing this letter's enciphered passages or a decipherment of them was
located. That does not move the class: the decipherment is on the leaf itself (N0). Unsearched and relevant if anyone
wants the letter's context: Ribbeck, *FBPG* 12 (check whether it reaches 1672); Rommel, *Geschichte von Hessen*.

## Safe and unsafe sentences

- **Safe:** "The enciphered passages of Lyncker's letter from Hamburg to Chancellor Vultejus, 4/14 May 1672 (HStAM 4 f
  Dänemark 125), are deciphered on the leaf itself by period glosses; we transcribed the codes and glosses in two blind
  passes and showed, against a permuted-table control, that the 2-digit groups follow the Kassel chancery's 1666 letter
  table (HCPortal key 255), while its 3-digit nomenclator is a different list from key 255's."
- **Unsafe:** "decoded", "deciphered by us", "first reading", "new decipherment", or "a key built from the glosses reads
  the letter" stated without saying the glosses are the period decipherment already on the document; "8/8 held-out" quoted
  as eight independent tests.

## Postmortem and corrections

- The held-out figure double-counts pairs and rests on 3 codes (+1 circular); corrected in NOTES.md (verifier note under
  GAPS159).
- Two S tokens contradicted by the letter's own gloss were left at S; regraded M via exceptions.tsv.
- A2-HDK's 26-pair key-255 test chose its pairs after seeing the key; superseded by the selection-free LCS test above,
  which agrees.
- NOTES.md's "Reading ready" paragraph (GAPS163) is accurate in substance ("the period gloss restated ... not an
  independent decipherment"); a verifier note is added stating the class.
- Class N0 < N3: no SECOND-OPINIONS-QUEUE.tsv row is due. No outreach gate is met by an N0 item; the key identification
  could be offered to HCPortal as a contribution (link 494 to key 255) through the owner, not by this session.

Requests this session: www.googleapis.com 11, be-api.us.archive.org 11, api.openalex.org 3, api.semanticscholar.org 3,
all one at a time, >=1.2 s apart, no 429/403. Vision: 2 crop looks. No subagents.

## Addendum: print check (GAPS188, account-4, 3 Oct 2026, 18:06-18:12 UTC)

Ran `tools/print_check.py` with `phrases.txt` and `sources.tsv` (both in this folder). The output is in `print-check.tsv` and `print-check-hosts.tsv`.
There were four target phrases: the clear prose at p2:7 ("hierbey signalirte dienste gethan"), the run-1 margin gloss
("disgustirt und vertanin holstein"), the run-2 gloss as context-read I ("gott geb dass alles wol ablauft") and
the p3:25-26 nomenclator glosses ("hertzog von ploen alliance kayser"). Each host also got a positive control. The first control was a sentence quoted
verbatim from UA Friedrich Wilhelm (urkundenundacte30kommgoog: "Lincker abgefertigt, um zusammen mit dem Gesandten in
Celle"). The second was the title of Ribbeck's Lincker article.

| host | positive control | target phrases |
|---|---|---|
| IA listed item urkundenundacte30kommgoog (djvu text, exact + proximity) | read (1 exact) | 0/4 |
| IA full text, all items (be-api) | read (2 items; Ribbeck title 11 items) | 0/3 no hits; "disgustirt..." not searched (HTTP 502, not retried) |
| Google Books API (key, country=US) | read (4 volumes, UA Friedrich Wilhelm; Ribbeck title 2) | "disgustirt..." 0. The other three return only scattered-word matches, which are not phrase hits: "hierbey signalirte dienste gethan" gave 6 volumes, all the Allgemeines historisches Lexicon 1722/1730, and the snippets show the words in different entries (Castagno, etc.); "gott geb..." gave 312 and "hertzog von ploen..." 243 generic volumes |
| OpenAlex (key, header) | **missed** (0 for both controls) | 0/4 + keywords 0. This is a non-test for phrases, because the control does not read |
| Semantic Scholar (key) | not run (HTTP 429 after 3 requests, not retried) | 0/2 searched, rest not searched |
| CrossRef (keywords) | n/a (keyword relevance only) | top 5 unrelated (Hessen-Kassel general) |

**Ribbeck lead (AUDIT section 3, "date range not confirmed"): settled.** The IA full-text hits for the title give "Aus
Berichten des hessischen Sekretärs Lincker am Berliner Hofe während der Jahre 1666-1669" (friedrichipreuss0000lfre;
baclac_1007322804 "(1666-1669)"). So Ribbeck, *FBPG* 12, S. 465 ff., covers Lincker at Berlin in 1666-69. This letter was
written at Hamburg in May 1672, so the article cannot contain it. UA Friedrich Wilhelm vol. (urkundenundacte30kommgoog) mentions Lincker in a later
Danish mission (Celle, Stade) and the Plön duke, and no target phrase occurs in it.

Result: no printed text of this letter's clear prose or of its glosses was located by this method on 3 Oct 2026. The
class stays **N0**, because the decipherment is the period gloss on the leaf itself. Print adds no prior decipherment, and it also adds nothing
that would change the class. Requests: be-api.us.archive.org 7 (incl. 1 to find Ribbeck's IA item), archive.org 2 (advancedsearch
1, djvu download 1), www.googleapis.com 7, api.openalex.org 7, api.semanticscholar.org 3 (429), api.crossref.org 2.

## R12D-HDKV: rule-7 fresh re-derivation and the gloss-hand question (account-4 verifier, 6 Oct 2026, 16:03-16:09 UTC by date -u)

Verifier R12D-HDKV, a separate session from every solver on this folder (A2-HDK*, GAPS152-199) and from VERIFY-HDK. Brief:
`.claude/briefs/runs/2026-10-06-account4-run12-jobs.md` "### R12D-HDKV". No key value and no reading was changed.

**1. Re-derivation (rule 7).**
```
$ python3 tools/decode_key.py ciphers/hessen-daenemark-1672 --check
ciphertext.tsv: tokens 65: C 9, I 1, M 25, S 28, U 2
reading up to date                                                  EXIT 0
$ python3 -I ciphers/hessen-daenemark-1672/keys/r12d_rederive.py ciphers/hessen-daenemark-1672
mine      [C 9, I 1, M 25, S 28, U 2]
committed [C 9, I 1, M 25, S 28, U 2]
diffs 0 value diffs 0                                               EXIT 0
```
`keys/r12d_rederive.py` (new) was written from the file formats only, without reading decode_key.py's token loop: value from
exceptions.tsv, else key.tsv / key_gloss.tsv, else `?`/U; grade lowered to M on an M-confidence sign or a `?` value. It
agrees with the committed reading_tokens.tsv on all 65 tokens, values and grades. **No token differs, M-graded or otherwise.**

**1a. Key cells against the period key image.** The re-derivation trusts key.tsv, so this verifier read by eye every
letter-table cell the reading uses (33 distinct letter groups on f.4) against `keys/hcportal_key255_0013.jpg` (key 255
f.13, letter table cropped at native resolution, two crops): 20 30 60 a, 22 32 b, 26 66 d, 28 38 68 e, 33 63 g, 55 h,
37 67 i, 69 k, 110 l, 74 104 n, 76 96 o, 83 113 r, 75 85 s, 117 t, 119 u; doubled row (one column offset: CC under A)
FF d, LL i, NN l, WW t, XX u, YY w; 6 in the f.13 null line "von 1. biß 20.". **33/33 agree with key.tsv.** (A2-HDK3's
120/120 against the DECODE 4690 decipher scale is a second witness; this is a third, by a different eye.) The two cells the
letter's own gloss contradicts (55 h vs gloss g; 6 null vs gloss t) are the table's values correctly copied: the
contradiction is between the 1666 table and the 1672 encipherer, as VERIFY-HDK graded them (M), not a key.tsv error.

**2. Gloss hand: period or modern (M, one eye, this verifier; method of manteuffel GAPS158).** Material: the existing
`tools/iiif_lines.py` crops (`images/crops_p2/p2_L01, L03`, `images/crops_p3/p3_L08, L14`; commands and boxes in their
manifest.json, GAPS155/GAPS159), viewed at native resolution, against the letter's clear text on the same lines and
against the Kassel chancery hand of key 255 f.13 (1666; entries 180-185). Compared:
- **Orthography.** Every gloss uses the 17th-century spelling, none the modern one: *Dennemarck* (not Dänemark),
  *Kayser* (Kaiser), *Hertzog* (Herzog), *Franckreich* (Frankreich), *Cur Brandenburg* (Kurbrandenburg), *Gen. Staden*,
  *Rex Daniae*. Key 255 (1666) writes the same forms: "Kön. dennemarck" 184, "Kayser" 180.
- **Script choice.** The interlinear name glosses (K. Dennemarck, Dennemarck, Holstein) are in German Kurrent; the margin
  gloss of run 1 writes the French loanword *disgustirt* in a Latin hand. That is the clear text's own convention on the
  same leaf (loanwords *tractiren*, *present*, *affection* in Latin script, German words in Kurrent) and the chancery
  convention of the period.
- **Literalness.** The margin gloss copies the decryption letter by letter, spaced as decoded ("dis gustirt / unv ertanin")
  and keeping the encipherer's spelling slips ("unvertanin" for unterthanin); a working decipherer's note, not an editor's
  normalised reading.
- **Ink and pen.** Iron-gall-type ink, brown-black, with no graphite sheen and no uniform modern stroke; the interlinear
  glosses are blacker and heavier than the letter's brown ink and are squeezed between its lines, so they were written
  in a different session from the letter, over the finished text (consistent with deciphering on receipt). The margin
  gloss is lighter, nearer the letter's tone. (VERIFY-HDK's one look at p3_L08 called the margin ink "same tone as the
  letter"; that holds for the margin, not for the interlinear glosses.)
- **Hand.** Not the letter writer's hand (smaller, more angular, heavier pen). Not shown to be the key-255 scribe either:
  the spelling and Kurrent forms agree, the pen does not; it does not name the decipherer.

**Verdict: period (17th-century), M.** Every compared feature is of the period and none is modern; the most likely
writer is a decipherer at the recipient's chancery in Kassel, not established. What would raise it above M: a
palaeographer, or a dated Kassel chancery decipherment in the same hand. **Effect on grades: none.** The glosses are the
known plaintext already graded C (rule 4: a period decipherment written on the leaf is plaintext, not a key source, so H
does not apply); a modern hand would have weakened the `period` label of the key-source field, and this verdict
supports it. Class stays **N0**, key `period`, text `known`.

**3. Depth (rule 4a).** No grade changed (65 tokens: C 9, I 1, M 25, S 28, U 2; H/C/S 37/65 = 57%), so no depth field is
written: status.json carries none for this target, and the brief allows a write only on a change. `tools/depth_check.py`
not run for that reason.

**Requests:** none (disk only). Vision: 4 looks by this verifier on native crops (2 key-255 table crops, 1 four-line gloss
montage, 1 zoom/comparison montage); no subagents.

# AUDIT: BnF fr.5160 f.86 and f.88 readings (Brienne to Servien, 21 Nov 1659): novelty class

Verifier session (LANE V, Opus), 24 Sept 2026, 04:21-04:35 UTC (`date -u` read at start and before writing).
Audits `reading_f86.{txt,tsv}`, `reading_f88.{txt,tsv}`, `key_1659.tsv`, `dechiffre_f87.txt`, `decode_1659.py` and
the NOTES.md sections "Folio 86-88: key from the f.87 decipherment" and "Joint key from f.86 + f.88", as of commit
f282f62, and the fr5160 results row in status.json. This session did no decoding and wrote no reading or key; it
does not protect the solver's conclusions. Classes are those of CLAUDE.md rule 10.

## 1. Verdict

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| f.86 cipher block (268 groups), = f.87 paragraph 1 | **yes, in manuscript:** f.87, "Dechiffré de la lettre de M.r le Comte de Brienne du 21 9.bre 1659", paragraph 1. Not found in print (section 3). | **yes:** f.87 is the contemporary decipherment of this very passage, bound beside it, and the BnF catalogue says the letters of item 1 are "souvent accompagnées du déchiffrement". | **N0** |
| f.88 cipher block as transcribed (153 groups, to "celle la"), = f.87 paragraph 2 | same: f.87 paragraph 2 | same | **N0** |

**Did we first-decipher? No.** The two passages were deciphered in 1659, on f.87 of the same volume. Every C token
in both readings is the f.87 text read back through a key estimated from it (NOTES.md says so itself: "not new
text"). What the solver produced is a **reconstructed key** (`key_1659.tsv`, 74 groups, a mixed table of letters,
digraphs and syllables, overlined series) recovered from known plaintext. Rule 10 classes readings, not keys; for
the key, the search result is: no Brienne-Servien 1659 table found in Tomokiyo's pages (local mirror:
`louisxiv0.htm` has Brienne ciphers 1 and 2, 1647 and 1651, to D'Estrades; `servien.htm` is Servien-Sabran 1632)
or in either solver repository (grepped 24 Sept 2026). That is a search result, not a novelty verdict.

The part of f.88's cipher that continues on canvas 173 (unfetched) is not classified by this audit. If it runs
past the end of f.87 paragraph 2 ("... quoy y pense"), that remainder has no located decipherment and needs its own
audit.

## 2. Central question: does a manuscript decipherment make N0, or does N0 need print?

Rule 10: "N0 plaintext and decipherment of this very item already known". Only N1 says "published". The rule's
own contrast between N0 ("known") and N1 ("published anywhere") means N0 does not require print.

Precedents:
- **Raince, Dupuy 452 (`ciphers/dupuy452-carpi-1520/AUDIT.md`), N0.** Jacqueton 1892 printed the plaintext from
  "déchiffrement au f° 31" of the same volume. There, print and a same-volume decipherment coincided, so it does
  not settle whether print is necessary.
- **Dupuy 468 (`ciphers/dupuy468-anhalt/AUDIT.md`), first audit N3, superseded by N1.** The first audit declined
  N0 because the decipherment was "a manuscript gloss that nobody has printed **or described**" (not in Dorez or the
  BnF notice), and it still answered "did we first-decipher? no". The second audit found a print (N1) and noted
  that "N0 could be argued in substance".

**Ruling: N0.** fr.5160 differs from Dupuy 468 on the point that audit relied on. The decipherment is described:
the BnF notice for this volume (Gallica OAI record; archivesetmanuscrits.bnf.fr cc58150z, fol. 1-110) says the
letters are "souvent accompagnées du déchiffrement". It is also not an interlinear gloss but a separate leaf with its
own heading naming the letter by sender and date. It has been publicly viewable on Gallica
(ark:/12148/btv1b9060495t). N3 would also be false on its own terms: N3 means "no prior plaintext or decipherment
located", and this project located one, on f.87. N1 and N2 describe plaintext known from another source, not a
decipherment of the item itself. So N0, with the qualifier that the known decipherment is manuscript and
catalogued at volume level, not at item level, and that no print of it was found (section 3).

## 3. Item extract and search

**Item.** Brienne (heading: "M.r le Comte de Brienne"; père Henri-Auguste or fils Henri-Louis, who held the
survivance, not settled from the leaf) to **Servien**, 21 November 1659. Place of writing not on the leaf; the court
was in the south at the time (Mazarin writes from Toulouse on 19 Dec 1659, Chéruel IX). Court addressed: **Savoy
(Turin)**, from the text: Madame [Royale], M. de Savoye, his sister going to Parma, M. d'Ambrun, M. de Mantoue and
Montferrat (f.86 clear prose). Distinctive phrases: see `phrases.txt`.

**Recipient correction (grade I, verifier's inference for a historian to confirm).** The catalogue, and this
folder's title, name the recipient as **Abel** Servien. Abel Servien died on 17 February 1659, nine months before
this letter. The Servien at Turin in 1659 is his brother **Ennemond Servien**, "le président Servien", ambassador
to Savoy 1648-1676 (Recueil des instructions XIV, Savoie-Sardaigne et Mantoue I, "Le président Servien, 1648-1676";
Chéruel, Lettres de Mazarin IX p.445, n.1: "Ennemond Servien, frère de l'ancien surintendant, Abel Servien", in a
letter of 19 Dec 1659 on Madame Royale, M. de Savoye, Mantoue and Montferrat). Parma fits: Marguerite-Yolande of
Savoy, sister of Charles-Emmanuel II, married Ranuccio II Farnese, Duke of Parma, in 1660 (Chéruel IX, notes
at djvu lines 6486 and 21405). So at least the 1659-1661 letters of item 1 are almost certainly to Ennemond, not
Abel. This widens the edition search to Ennemond's embassy.

**Search log (24 Sept 2026).**

| family | what was searched | result |
|---|---|---|
| (a) canonical series | Chéruel, *Lettres du cardinal Mazarin* IX (1658-1661), IA `lettresducardina09maza`, full djvu text: 12 phrases exact and proximity (`print_check.py`), plus grep for Servien, Parme, Embrun/Ambrun, Marguerite | no phrase; context only (Dec 1659 Mazarin to Navailles on Madame Royale; Ennemond Servien identified) |
| (a) | *Recueil des instructions* XIV (Savoie-Sardaigne et Mantoue I, Horric de Beaucaire 1898), IA `recueildesinstr00diplgoog`, full text, 12 phrases + grep | no phrase; the editor states the day-to-day dispatches to Servien are **not reproduced** ("Il n'entre pas dans le cadre de cette publication de reproduire ces instructions") |
| (b) sender's printed memoirs | *Mémoires* of Henri-Louis de Loménie de Brienne, 1916 ed. II-III (IA `memoiresdelouish02brie`, `03brie`); *Mémoires inédits* 1828 I-II (`mmoiresinditsde00/01barrgoog`); 12 phrases each | no hits |
| (b) recipient's correspondence | no printed Ennemond Servien correspondence located (IA advancedsearch title:servien: nothing relevant); Depping, *Correspondance administrative* (prior pass, NOTES.md) no link | none located |
| (c) state papers | AE Correspondance politique Turin (the ministry copies, e.g. "Corr. Turin LXIV" cited in Recueil XIV) is manuscript, not searched | unreachable here |
| (d) holding archive | BnF notice cc58150z and Gallica OAI record (read by earlier passes, quoted in NOTES.md); Gallica itself is LANE G's, not fetched | volume-level "déchiffrement" note only |
| (e) full text | `print_check.py`: IA global full-text (be-api) 12 phrases, Google Books 12 phrases | no genuine hit. One GB hit, "l'alliance est si disproportionnée" in *Pouvoirs et littoraux du XVe au XXe siècle* (2000), is about Marguerite de Coëtivy (15th c.): unrelated |
| (f) solver repos, blogs | fresh anonymous clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep Servien / 5160 / Ennemond / Turin 1659 (deleted after); Tomokiyo local mirror (`unsolved`, `louisxiv0`, `crypto`, `servien`) | Servien hits are Servien-Sabran 1632, D'Avaux-Servien 1644-45, Mazarin 1652, Rohan 1636: none is this item |
| (g) scholarship | HAL: "Servien AND (Turin OR Savoie)" (114 records); OpenAlex and Semantic Scholar: **HTTP 429**, stopped (the OpenAlex rows in print-check.tsv are blocked too); CrossRef: 3 keyword queries, nothing on this letter; WebSearch 3 | **Lead, not read:** Élodie Conti, "Justine de Bressac, une ambassadrice entre France et Savoie (1648-1664)", *Histoire, économie et société* 2024/4, p.51 (Cairn; HAL hal-04861752, no file), and Conti, "Justine de Bressac, une exception ?" (HAL hal-04958179); Matthieu Gellard, "Un ambassadeur dans la tourmente", in *De Paris à Turin. Christine de France* (2014; HAL hal-03916168, no file). These study the Servien embassy and may cite or quote fr.5160. Full text not reached (Cairn is not on this worker's host list). |
| JSTOR | 3 rows added to `JSTOR-QUEUE.tsv` | queued; does not block |

**What the solver searched** (NOTES.md): the prior print check (Depping, Google Books, solver repos, Tomokiyo
mirror); the key and reading sections searched nothing further, and made no novelty claim.

## 4. Grade check (C = from known plaintext, the f.87 decipherment)

- `python3 decode_1659.py --check` exits 0 (readings current). Totals: f.86 C 72 / M 196 / P 12; f.88 C 65 / M 88 / P 5.
- All 74 key rows are grade C, each with evidence at least 1. No H is claimed anywhere, correctly: no key source
  exists; the key comes from the f.87 plaintext.
- No C token sits on a `conflict` key row. 58 C tokens sit on `minor conflict` rows and 11 on single-attestation
  rows: allowed by the solver's stated rule, but a single attestation is thin support for grade C.
- **Over-grade, 4 tokens:** C tokens whose key value is not the f.87 text aligned at that position
  (`align_f8x.tsv`): f.86 L07 pos 2 `_16` read "se" where the alignment has "es"; f.86 L07 pos 14 `_0` "pa" / "ei";
  f.88 L01 pos 16 `4` "c" / "cc"; f.88 L07 pos 14 `2` "e" / "fr". At these positions f.87 does not support the value, so they
  should be M. (Two further mismatches, `115` = "M." against the aligner's `#` title placeholder, are consistent.)
  For the LANE G solver; this audit does not change readings.

## 5. Safe and unsafe sentences

- **Safe (f.86):** "The cipher passage on BnF fr.5160 f.86 (Brienne to Servien, 21 Nov 1659) has a contemporary
  decipherment on f.87 of the same volume (N0). From that decipherment we reconstructed the 74-group key that
  reads the passage back (C 72 / M 196). No printed edition of the letter was located."
- **Safe (f.88):** "The cipher passage on f.88 is deciphered by paragraph 2 of the same f.87 decipherment (N0).
  The key recovered from f.86 reads it at 114 of 143 keyed groups against a shuffled control of 28-35."
- **Unsafe (both):** "We deciphered / read Brienne's 1659 letter to Servien"; "first decipherment"; "previously
  unread"; "letter to Abel Servien" (Abel was dead by then).

Confidence: high on the N0 facts (the f.87 heading, the pairing shown by repeats and the held-out check, the
catalogue note). Medium on the recipient correction, which rests on dates and editions, not on the leaf. The open
gap is Conti 2024, which could at most add a print (still N0).

## 6. Postmortem and corrections

**Postmortem (one line):** no novelty over-claim. The solver said "not new text" twice, and the results row says
"a recovery of an existing decipherment". The real error is older: the catalogue's recipient, Abel Servien, is
impossible for a 21 Nov 1659 letter.

Corrections made:
- NOTES.md: a correction note under the title (recipient of the 1659 letters: Ennemond, not Abel, grade I).
- status.json, fr5160 results row: class N0 and the key/grade figures brought to the current joint key.
  Not changed: the `targets` entry name ("to Abel Servien"), which is the orchestrator's; flagged in ROOM.md.
- Not changed: the 4 over-graded tokens (section 4), which are the LANE G solver's.

## 7. Requests

archive.org 14 (print_check 6 djvu/metadata, this session 6 advancedsearch + 2 metadata), be-api.us.archive.org 12
(print_check); www.googleapis.com 13 (key and country=US, key never printed); api.openalex.org 2 (both 429, stopped);
api.semanticscholar.org 1 (429, stopped); api.archives-ouvertes.fr 2; api.crossref.org 3; github.com 2 anonymous
clones (grep only, deleted); WebSearch 3. No Gallica, no logins, no credentials printed, no subagents.

---

# f.67: BnF fr.5160 f.67 (canvas 129/130), Brienne to Servien, "A Paris ce 10 8bre 1659": novelty class

Verifier V5 (LANE V2, Opus), 24 Sept 2026, 09:48-10:01 UTC (`date -u` read at start and before writing). Audits
LANE G2 worker M's claim (ROOM 09:27; NOTES.md "Folio 67: reconciled and read"; `reading_f67.{txt,tsv}`,
`exceptions_f67.tsv`, `control_f67.tsv`, `decode_f67.json`; the f.67 results row in status.json). No decoding was
done here and no reading, key or grade was changed. The 1653 letters (f.1-3, f.9) are a separate negative and are not
covered.

## F67.1 Verdict

> **Superseded 24 Sept 2026 by 'f.67 re-class (V5b)' below: f.67 is N0 (clear text on f.68r of the same volume).**

| item | what is actually read | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|---|
| f.67 cipher (546 groups, canvas 129 L01 to canvas 130 block B) | a **partial cryptanalytic reading**: S 107, M 416, I 9, U 14 of 546 groups, **no H or C** on this letter. The words are M-grade as a whole; what is established is the **gist** (Savoy; is the reported rift between the Duke and his mother real; is Madame Royale withdrawing from the "maniement des affaires"; the Duke's marriage, a "Mademoiselle" named), not a verbatim text | none located (F67.3) | none located: no interlinear or facing decipherment on f.67 (cipher numeral-only, no gloss, per two passes and the reconciler); f.66 is blank; f.68r is unseen at full resolution (F67.2) | **N3** |

**N3 applies to the gist and the S-grade words, not to a verbatim plaintext.** 416 of 546 tokens are M (homophone or
syllable-level rows of key_1659 whose value is not settled on this letter, plus conflict rows). Nobody should quote a
sentence of `reading_f67.txt` as Brienne's words. The clear French on the leaf (row 1, the canvas 130 middle passage,
the close) is legible to anyone. It is not a decipherment and gets no class.

**Did we first-decipher?** Not established. No prior decipherment or print was located. Two things are not excluded
and are likely to exist in manuscript: (i) a clear minute or register copy of this dispatch among the Secretary of State's
papers (AE, Correspondance politique Sardaigne/Piémont for 1659: Cosnac cites "Aff. étr., Piémont, vol. 50" for the
Servien correspondence of 1656 and "Aff. étr., France, vol. 900" for a Brienne-to-Servien letter), and (ii) a decipherment
on a leaf not yet seen at full resolution (f.68r). Either would move the class to N0 or N2.

## F67.2 Item extract and the leaf question

- **Item.** "M. de Servien" at Turin (Ennemond Servien; Abel died 17 Feb 1659, see section 3 above), from "de Brienne",
  dateline "A Paris ce 10 8bre 1659" (canvas 130). Cipher numeral-only with overlined digits, the table of f.86-88
  (`key_1659`, grade C from the f.87 decipherment of a different letter, 21 Nov 1659).
- **Sender, grade I (verifier's inference for a historian to check).** The neighbouring letters are dated "a Bourdeaux le
  30e 7bre 1659" (canvas 126) and "a Thoulouze ce 19e 8bre 1659" (canvas 136), with the court. A letter "A Paris" of 10 Oct
  1659 between them suggests the other Brienne, the one not travelling with the court. This matters for the search:
  the letter is not in the court's travelling register if it was written in Paris.
- **Distinctive phrases** (`phrases_f67.txt`, 13 phrases, diplomatic and modern forms): "retirer du maniement des
  affaires", "mesintelligence d'entre le filz et la mere", "leurs principaux ministres", "de la verite desquelles il
  importeroit", "quelle peut estre l'inclination", "en devrez parler a leurs Altesses Royalles", "Desja ie vous ay mandé
  ce qui s'est", "il est du service du Roy que vous nous mandiez".
- **Neighbouring leaves** (`walk_37_159.tsv`, thumbnail resolution): f.66r (canvas 127) blank; f.67 verso (canvas 130)
  carries the end of this letter; **f.68r (canvas 131) plain text on "Madame/duc/fils mesintelligence, duc de Parme
  marriage prospects", no date, verso blank**; f.69 blank; f.70 opens the 19 Oct letter. f.68r shares the subject of
  f.67's second cipher block. The walk read it at thumbnail size and misclassified f.67 itself ("symbol+numeral", in
  fact numeral-only), so its "decipherment: n" for f.68 is weak. It has no "Dechiffré" heading visible at that size,
  and its Parma content is not in f.67's reading, which points to a separate enclosure or a letter's final page. Asked of LANE G2
  (ROOM 09:55, "for LANE G2": canvas 131 native, and a Gallica full-text search). **If f.68r proves to be a
  decipherment or clear duplicate of f.67, the class is N0 and this section must be revised.**

## F67.3 Principal families

| family | searched / unreachable | what | result |
|---|---|---|---|
| holding volume, same and neighbouring leaves | partly | walk rows canvas 124-136; passes and reconciliation of f.67; the f.86-88 precedent (f.87 decipherment on its own leaf) | no decipherment on f.67 or f.66; **f.68r unseen at native resolution** (requested of LANE G2) |
| (a) canonical series | searched | Chéruel, *Lettres de Mazarin* IX (IA `lettresducardina09maza`, full djvu): 13 phrases (`print_check.py`), grep Servien, "Madame Royale", "octobre 1659", mésintelligence | no phrase; Mazarin's letters and analyses only, no Brienne dispatch printed |
| (a) | searched | *Recueil des instructions* XIV, Savoie-Sardaigne et Mantoue I (Horric de Beaucaire 1898, IA `recueildesinstr00diplgoog`): 13 phrases, grep 1659 | no phrase; the editor does not reproduce the day-to-day dispatches to Servien (section 3); 1659 mentions only Servien's May 1659 compliment on the Infanta marriage |
| (b) sender's printed memoirs | searched | Brienne fils, *Mémoires* 1916 II-III (IA `memoiresdelouish02brie`, `03brie`): 13 phrases | no hits |
| (b) recipient's correspondence | none located | no printed Ennemond Servien correspondence (section 3); Cosnac (next row) prints individual Brienne-to-Servien and Servien letters from AE | searched as below |
| (c) documentary editions for the period | searched | Cosnac, *Mazarin et Colbert* (1892) I-II (IA `mazarinetcolbert01cosn`, `02cosn`): 13 phrases normalised, grep "10 octobre 1659", "maniement des affaires", mésintelligence, Servien | no phrase, no 10 Oct 1659 letter. Vol. II p.55 prints a **different** Brienne-to-Servien letter (1656, Queen Christina's etiquette) from AE France 900, and p.99-100 summarises Servien's Nov 1656 dispatches on Madame Royale keeping power (AE Piémont 50). This family prints Brienne-Servien letters, so it was the right one to search. The Google Books hit "Servien" + "10 octobre 1659" in this work is two separate occurrences, not a print of f.67 |
| (c) Savoy side | searched | Claretta, *Storia del regno e dei tempi di Carlo Emanuele II* (1877-78) I-III (IA `storiadelregnoe02/00/01clargoog`); Saint-Genis, *Histoire de Savoie* (1869) I-III (IA `bub_gb_ivpiUnR_CIAC`, `histoiredesavoi00/01/02gngoog`): 13 phrases, grep Servien, Brienne, Montpensier, maniement | no phrase. Claretta works from Turin (A.S.T. "Lettere Ministri, Francia"), narrates the Orléans/Montpensier marriage soundings of 1658-59 (vol. I pp.239-242) with no Brienne-Servien dispatch; Saint-Genis II: Madame Royale kept "une grande part au maniement des affaires" to 1663 (context, not this letter) |
| Claretta, *Storia della reggenza di Cristina di Francia* | not searched in full | covers 1637-1648, before this letter; one volume (`storiadellaregg00clargoog`) listed in `sources_f67.tsv` gave no hit | out of period |
| AE Correspondance politique Sardaigne/Piémont (minutes, register copies) | unreachable | manuscript at La Courneuve; the printed *Inventaire sommaire* on IA covers Mémoires et documents, not CP | not searched; likely home of a clear minute |
| (d) BnF / Gallica | requested | Gallica full text and canvas 131 are LANE G2's; posted "for LANE G2" in ROOM | pending |
| (e) full text | searched | IA global full text (be-api) 13 phrases; Google Books 13 phrases (`print-check-f67.tsv`) + 6 metadata queries (date, correspondents, subject) | generic hits only ("retirer du maniement des affaires": Plutarch translations, Motley's *Barnevelt*, Saint-Simon; "leurs principaux ministres": 525 unrelated). GB metadata: Saint-Genis 1869 (checked, above), Cosnac 1892 (checked, above), *Revue d'histoire diplomatique* 2009 (id `1yFDAQAAIAAJ`, snippet-only, not read; JSTOR row) |
| (f) solver repos, blogs, DECODE | searched | fresh anonymous clones of dbourdeau/cyphersolver and aaymeloglu/unsolved-ciphers, grep 5160 / Servien / Ennemond / Brienne (deleted); Tomokiyo mirror (section 3: Brienne 1647/1651 only); `sources/decode/records-non-decrypted-2026-09-24*.tsv` | Servien hits are Rohan 1636 and German "Servien" (Serbia); no DECODE record for fr.5160 (the folder appears only as a cross-link tag on BL Add MS 4200 and Mélanges de Colbert 11 rows) |
| (g) scholarship | partly | HAL "(Servien OR Madame Royale) AND 1659 AND (Savoie OR Turin)": 0; CrossRef 1 query: nothing relevant; OpenAlex **429**, stopped; S2 not tried (429 all morning per ROOM). Leads from section 3 still unread: Conti 2024 (HES 2024/4), Gellard 2014 (*De Paris à Turin*) | nothing located; two leads unread |
| JSTOR | queued | 2 rows added to `JSTOR-QUEUE.tsv` | does not block |

## F67.4 Evidence and grades

- Grades as committed (`read_f67.py`, `decode_key.py --config decode_f67.json --check` exit 0 per worker M): S 107,
  M 416, I 9, U 14; H 0, C 0. That is a cryptanalytic result (CLAUDE.md rule 4), with a word-level control of 0.721
  against 200 derangements (mean 0.488, max 0.647) and worker H's n-gram trial z 3.57 (0/20). The control shows the
  table is right for this letter. It does not make the individual M words right.
- Kind: the key was recovered from a contemporary decipherment of another letter, so applying it here is a recovery
  of the key, but the reading of f.67 itself is cryptanalytic (S/M) and partial.

## F67.5 Safe and unsafe sentences

- **Safe:** "BnF fr.5160 f.67 (Brienne to [Ennemond] Servien, Paris, 10 Oct 1659) is enciphered in the same table as the
  21 Nov 1659 letter whose contemporary decipherment is on f.87. Using the table recovered from that decipherment, we can
  partly read it (S 107 / M 416 of 546 groups, no H or C). The gist concerns the Savoy court: the reported rift between
  the Duke and Madame Royale, whether she will withdraw from affairs, and the Duke's marriage. No prior decipherment or
  printed text of this letter was located in Chéruel IX, the Recueil des instructions XIV, Cosnac, Claretta, Saint-Genis,
  the Brienne memoirs, IA or Google Books full text (N3, 24 Sept 2026); the ministry's minute and f.68 were not seen."
- **Unsafe:** "We deciphered Brienne's letter of 10 Oct 1659"; "the full text reads ..." (quoting M words as the letter);
  "first decipherment", "previously unread", "unpublished"; "letter to Abel Servien".

Confidence: medium. The negative is from printed editions whose scope is known (Recueil XIV says it does not
reproduce the dispatches; Chéruel prints Mazarin, not Brienne; Cosnac and Claretta quote selectively). What most
limits the class is manuscript, not print: f.68r, and the AE minute.

## F67.6 Postmortem and corrections

**Postmortem (one line):** no novelty over-claim by the solver, who wrote "novelty is not classified here". Two wording
over-reaches were corrected: "read" for a mostly M reading, and "new letter" in the walk's notes, meaning "not flagged by
earlier passes".

Corrections made (24 Sept 2026):
- status.json, f.67 results row: title "read" -> "partly read"; grade adds "N3 (verifier, AUDIT.md f.67)"; line keeps
  the gist and adds that no H/C and the M share limit it to a gist.
- NOTES.md "Canvas walk 37-159": "one new letter" -> "one letter not flagged by earlier passes"; "Canvas 129/130":
  "flagged as new" -> "flagged as not seen before" (walk-internal sense only).
- Not changed: readings, key, grades (the solver's); the f.86/f.88 N0 above.

## F67.7 Requests

archive.org 21 (print_check 4, advancedsearch 5, metadata 6, djvu 6),
be-api.us.archive.org 26 (print_check), www.googleapis.com 19 (13 print_check + 6 targeted, 3 s apart; key and
country=US, key never printed; D1 held the host at 09:49 for ~4 q, overlap small), api.archives-ouvertes.fr 1,
api.crossref.org 1, api.openalex.org 1 (429, stopped), github.com 2 anonymous clones (grep, deleted). No Gallica, no
logins, no subagents.

## f.67 re-class (V5b)

Verifier V5b (LANE V2, Opus), 24 Sept 2026, 10:17-10:25 UTC (`date -u` read before writing). Checks LANE G2 worker P's
finding (commit 93db371, NOTES.md "f.68r and f.66r checked") against `reading_f67.txt`, from the committed files only.
The canvas 131 image is **not on disk** (P kept it in a scratchpad; the folder is at its 30 MB cap), so this check rests
on P's diplomatic transcription of f.68r, a single Sonnet reading. No decoding, no network.

**Verdict: f.67 moves from N3 to N0.** Superseded: F67.1's N3, and the F67.5 safe sentence.

| item | prior plaintext | prior decipherment of this item | class |
|---|---|---|---|
| f.67 cipher (546 groups) | **yes, in manuscript:** f.68r of the same volume (canvas 131) carries the letter's text in clear, in what P judged the same secretary hand | **yes, in substance:** f.68r gives the clear text of exactly the passages f.67 enciphers. Whether it is a contemporary decipherment or the clear minute that was enciphered is not settled (no "Dechiffré" heading seen). Either way the plaintext of this very item sits beside it in the holding volume | **N0** |

**Why the match counts as the same letter, not the same subject.** P's f.68r text follows `reading_f67.txt` in order
through a run of distinctive clauses, not only its topic words:

| f.67 reading (line) | f.68r (P) |
|---|---|
| "qu[e je] v ou s di e qu n pu b i e de s n ou ve l le s de ... la ve i te de s ques l le s oi l ... m q r te r oi t fo r t de s t re e s c la oi s c y" (f129 L02-L05) | "le vous die qu'on publie des nouvelles de la verité desquelles il importeroit fort d'estre esclairay" |
| "s c a v oi r ques la f e c t i n du fi l je ... de la me re n e s t pr lu s si gn ... de ... pa s se" (L05-L07) | "scavoir que la affection du fils a l'endroit de la mere n'est plus si grande qu'au passé" |
| "e t ques M. se r oi t e n [154] pe n se e de se re t re r du ar ni e me n t de s le fa oi re s PARCEQUE SIL POUVOIT ESTRE c st oi n t ... l m b la b le c ha n ge me n t n ou s ... de s me su re s qu pr re n e re a le [80]" (L07-L11) | "et que Madame seroit en quelque pensée de se retirer du maniement des affaires parceque s'il pouvoit estre craint qu'il arrivast un semblable changement nous aurions des mesures a prendre avec le duc" |
| "i n fi i a t i n [79] [80] p ou r se ar i e r ... la pe e s n ne e t q ou r le te m pr s ... fo n de me n t ques lo n pu b i e ar da mo oi se l le qu re n du t re s ar ou [_25] ... ar da mo oi se l le d r le" (f130a L02-L06) | "l'inclination du duc pour se marier, pour la personne et pour le temps, et si c'est avec quelque fondement que l'on publie que mademoiselle a rendu tres mauvais office a mademoiselle d'Orleans sa soeur" |
| "ce q l di t de la me s oi n re i ge n ce de n t re le fi l je e t la me re oi t ve i ta b le si le ar r q s de [_2] qu ne je de me ou re st c [51] e de s le f fa oi re s ... su r q le [80] se ... c ha r ... qu n ju ge e n pe n se e pr lu s ... di ve r t r ques de s y qu pr pr i ques r" (f130b L01-L07) | "que ce qui se dit de la mesintelligence d'entre le fils et la mere soit veritable, si le marquis de Pianese demeurera [chef] des affaires ou bien sur qui le duc se [pourvoira de charge], qu'on juge en pensée plustost de se divertir que de s'y appliquer" |

Five consecutive stretches agree in order and in wording (not only in subject), including the plain-text words
f.67 carries in clear ("parceque s'il pouvoit estre"). f.68r also fills slots our key left open: `[80]` = "le duc",
`[_2]` = "Pianese", and "d r le" = "d'Orleans sa soeur". It is not a different letter on a similar subject. The walk's
"duc de Parme marriage prospects" for canvas 131 was a thumbnail misreading: P's text has "l'inclination du duc
pour se marier" and no Parma.

**Precedents.** The f.86/f.88 N0 above (decipherment on f.87 of the same volume, manuscript only, section 2 ruling:
N0 does not need print) and `ciphers/clair1067-brienne-poland-1646/AUDIT.md` (decipherment on the leaf = N0). f.68r is
the same case: the plaintext of this very item is in the holding volume beside it, and the BnF describes the item-1
letters as "souvent accompagnées du déchiffrement". The one difference: f.68r carries no "Dechiffré" heading, so it may
be the clear minute rather than a decipherment. That does not change the class. Either way the ciphertext-to-plaintext
mapping was known to the office and survives in the volume.

**Did we first-decipher?** No. Our partial reading is a re-decipherment of a letter whose clear text lies two leaves on.

**Confidence:** high that f.68r is the same letter (five ordered stretches of wording). Medium on how exactly the leaf
relates to f.67, since no heading was seen and the relation is P's single reading. It rests on one transcription. A second eye
on canvas 131 at native resolution (LANE G2) should confirm the text and look for a heading. That could refine the
wording. It would change the class only if f.68r proved to be a different letter, and the table above makes that unlikely.

**Safe (f.67):** "BnF fr.5160 f.67 (Brienne to [Ennemond] Servien, Paris, 10 Oct 1659) is enciphered in the table
recovered from the f.87 decipherment; its clear text survives on f.68r of the same volume (N0, manuscript, 24 Sept 2026).
Our partial reading (S 107 / M 416 of 546 groups) agrees with it and is a re-decipherment, useful as a check on the key."

**Unsafe (f.67):** "we deciphered a previously unread letter"; "no prior decipherment located" (superseded); anything
presenting the f.67 reading as the only source of the text; "letter to Abel Servien".

**For LANE G2 (not done here):** f.68r gives known plaintext for f.67. Aligning P's (or a second) transcription of
f.68r to `ciphertext_f67.tsv` would turn many of the 416 M tokens and the 14 U into C-grade checks (as f.87 did for
f.86/f.88), and would test key_1659's homophone rows on a second letter. That needs `dechiffre_f68.txt` committed with
a second pass.

**Corrections made (24 Sept 2026):**
- F67.1 and F67.5 above: superseded by this section (a pointer line added under F67.1). The text is kept for the record.
- NOTES.md, "Folio 67" verifier blockquote: N3 -> N0 with pointer here.
- status.json, f.67 results row: grade "N3 ... no prior decipherment ... located" -> "N0 (verifier, AUDIT.md f.67 V5b):
  clear text on f.68r of the same volume"; line's "No prior decipherment or print located ... f.68 ... not seen"
  replaced with the f.68r fact.
- SECOND-OPINIONS-QUEUE.tsv: SO-FR5160-F67 marked `withdrawn` (N0; a second opinion on print is moot). The prompt
  file is left in place for the record. JSTOR rows 32, 61 and 62 are left as they are. They cannot change an N0.
- NOTES.md status line: stays `open`. The folder's 1653 letters are unresolved, so no change is within the vocabulary.

Requests: none (no network beyond git).

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

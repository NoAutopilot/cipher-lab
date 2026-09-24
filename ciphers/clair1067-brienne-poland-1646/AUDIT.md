# AUDIT: Loménie de Brienne to the Queen of Poland, 19 May 1646 (BnF Clairambault 1067, fol.226r-227r)

Verifier session_01Udgi32LVQHdPhEgPKEf6fe (Opus, for LANE V / cipher-lab-7a), 24 Sept 2026, 07:50-08:20 UTC by `date -u`.
Adversarial audit under CLAUDE.md rule 10. No decoding done; no reading, key or ciphertext changed.

Claim under audit (ROOM.md, LANE G2, 24 Sept 2026 07:44): "Brienne to the Queen of Poland, 19 May 1646, Clairambault
1067 fol.226r-227r; interlinear decipherment, key_1646.tsv, C307 M31 of 338, decode_key --check 0; French".

## 1. Verdict

| item | class | prior plaintext | prior decipherment of this item | evidence | confidence |
|---|---|---|---|---|---|
| Cipher passages of fol.226r (last 2 lines), 226v and 227r (30 cipher lines, 338 tokens) | **N0** | yes, in manuscript: the interlinear French written over every cipher line on the leaf itself; not found in print (section 4) | **yes:** the same interlinear gloss is the decipherment of this very item, word over group-run | strong: gloss over all 30 lines, pairing consistency 0.863 against shuffled 0.402-0.448 (NOTES.md, control_1646.txt) | high on N0; medium on "contemporary" (section 3) |

**Safe sentence.** "The cipher passages of Brienne's letter to the Queen of Poland of 19 May 1646 (BnF Clairambault 1067,
fol.226-227) carry an interlinear decipherment on the leaf itself (N0). Aligning that decipherment with the groups gives
an 84-code key (grade C, from known plaintext) that regenerates the reading: C 307, M 31 of 338 tokens. No print of the
letter or its plaintext was located."

**Unsafe sentences.** "We deciphered Brienne's 1646 letter to the Queen of Poland." "First reading / previously unread
cipher letter." "Key recovered cryptanalytically." (The plaintext was on the leaf; the key rests on the gloss; there is
no H and no S.)

**Did we first-decipher? No.** The leaf was deciphered when it was glossed. What this project added is the sign-by-sign
key table and a reproducible alignment (a recovery from the document, like rah-canada-1869), not a decipherment.

## 2. Why N0 and not N1, N3 or "unclassifiable without print"

Rule 10: N0 is "plaintext and decipherment of this very item already known"; only N1 says "published". Precedents:

- **fr5160-letellier-1653 (AUDIT.md s.2), N0:** a manuscript decipherment of the item, bound beside it, publicly
  viewable, is enough; print is not needed. That ruling also leaned on the BnF notice saying the letters are "souvent
  accompagnées du déchiffrement".
- **rah-canada-1869 (AUDIT.md), N0:** clear text on the item itself, "catalogued at item level, contents not described",
  still N0.
- **thurloe-printed P3 (AUDIT.md), N0:** an interlinear decipherment above each cipher line (there, printed by Birch).
- **Dupuy 468 (dupuy468-anhalt/AUDIT.md), counter-precedent:** the first audit declined N0 because the interlinear gloss
  was "a manuscript gloss that nobody has printed or described"; the second audit (N1 on a print) noted "N0 could be
  argued in substance".

This item sits between fr5160 and Dupuy 468 on one point: the BnF finding aid describes the item only as "Lettre avec
chiffres adressée par de Brienne à la reine de Pologne (19 mai 1646)" and does **not** mention a decipherment. Ruling
**N0** nonetheless, because (a) the gloss stands over every cipher line of this very leaf, in the same volume and on
the same folios, which is closer to the item than fr5160's separate f.87; (b) the leaf has been publicly viewable on
Gallica (ark:/12148/btv1b90008551, canvases 48-50); (c) N3 would be false on its own terms, since this project located
a decipherment of the item; N1 and N2 describe plaintext from another source, which this is not. Qualifier, stated
wherever the class is repeated: *the known decipherment is a manuscript interlinear gloss on the leaf, not mentioned in
the catalogue entry, and no print of it was found.* If a later audit prefers the Dupuy 468 reading, the fallback is
not N3/N4 but "N0 in substance"; either way no novelty wording is available.

## 3. Grades and the gloss

- **Grades checked.** `key_1646.tsv`: 84 codes, all grade C, none H. `python3 tools/decode_key.py
  ciphers/clair1067-brienne-poland-1646 --check` (run 24 Sept 2026): "tokens 338: C 307, M 31 / reading up to date",
  exit 0. That matches the claim and LANE W's ruling (interlinear gloss = known plaintext = C, never H). No H claimed
  anywhere in the folder or in status.json. Correct.
- **Contemporary?** Probable, not established. For: 17th-century orthography in the gloss (*ilz*, *renouuelleroient*,
  *Niuernois*, *regres*); the gloss completes the letter's own clear sentences grammatically; a nomenclator of 84 codes
  with nulls and homophones is not something a later reader glosses fluently without the key. The hand is described
  (NOTES.md) as "second, heavier upright", not identified, not compared with any Brienne-office or Warsaw-secretariat
  hand. **The class does not depend on this:** a later decipherment written on the leaf is still a decipherment of this
  very item.
- **Leaf provenance note (for whoever writes it up).** The letter is signed and dated at Compiègne but is now in Paris
  in the Clairambault genealogical series. Whether it is the received original (glossed by the Queen's secretary and
  later returned among Nevers/Gonzague papers) or the office's retained copy is not established; nothing in the
  repository settles it. Do not describe the gloss as "the Queen's decipherment" or "Brienne's office's decipherment".

## 4. Search log (24 Sept 2026)

Solver's log (NOTES.md "Check-solved sweep"): web search x2, Wikisource article on Marie de Gonzague at Warsaw,
Tomokiyo louisxiv0 (Brienne ciphers 1647/1651, different correspondent), sources/cryptiana grep, DECODE catalogue grep,
Bourdeau and Aymeloglu clones, Gallica ContentSearch 0. No print check, no phrase search. This audit added:

| family | what was searched | result |
|---|---|---|
| (a) canonical series | Chéruel, *Lettres du cardinal Mazarin* t.2 (IA lettresducardina02maza), 11 phrases (print_check) + be-api fts "Nivernois", "Nivernais", "19 mai 1646", "regrès", "Mantoue", "reine de Pologne" | phrases 0; "reine de Pologne" and "Mantoue" hit only Mazarin's own letters to the Queen and Mantua matters (index lines "A la reine de Pologne"); nothing on Nivernois/the government of Nivernais or a Brienne letter of 19 May 1646 |
| (a) | Farges, *Recueil des instructions*, Pologne t.1 and t.2 (1888; IA pologne01farggoog, pologne00farggoog) | phrases 0; fts "Nivernais"/"Nivernois"/"Nevers" 0; "Mantoue" hits concern the 1645 marriage negotiation only |
| (a) | *Négociations secrètes touchant la paix de Munster* t.2, t.3 (IA negociationssecr02lecl, 03lecl; Brienne's 1646 correspondence with the plenipotentiaries) | phrases 0; fts "Nivernois" 0; one "Reine de Pologne" hit (an unrelated discourse) |
| (b) sender/recipient editions | Des Noyers, *Lettres* (1859; lettresdepierre00noyegoog; begins 1655); *Lettres inédites à Marie-Louise de Gonzague* (1920; lettresindites00cond; 1660-67); *Mémoires inédits* of Brienne le jeune t.1 (1828; mmoiresinditsde01barrgoog) | phrases 0 in each |
| (c) documentary editions / full text | IA full text across all items (ia-global), 11 phrases | 0 |
| (e) Google Books | 11 phrases (print_check), plus 3 metadata queries: "reine de Pologne" + "gouvernement de Nivernois" 1646 (0), Brienne + reine de Pologne + Mantoue + Nivernois (0), intitle Louise-Marie de Gonzague correspondance (2: *La cour savante de Louise-Marie de Gonzague* 1982; Grell, *Louise Marie de Gonzague, reine de Pologne* 2024) | no text hit; the 2024 Grell volume is a lead (JSTOR/owner row) |
| (d) holding archive | BnF finding aid entry via WebSearch (archivesetmanuscrits cc137820/cd0e4456): "Lettre avec chiffres ... (19 mai 1646)"; no mention of a decipherment or of any edition. Gallica and archivesetmanuscrits themselves not fetched (LANE G2's host; the solver's fetch of the finding aid is in NOTES.md) | catalogue note only |
| (f) solver repos, cipher blogs | solver's greps (Bourdeau, Aymeloglu, Cryptiana, DECODE catalogue) accepted; not re-run, since no find there could lower N0 | 0 (solver) |
| (g) scholarship | CrossRef 3 keyword queries: top hits Grell, "Louise Marie de Gonzague (1611-1667) reine de Pologne" (10.19195/2658-2082.80.3.9), Mantuan marriage celebrations, Gaspard de Tende; HAL 1 query (2 hits: Tende 2008, Polish nobility 2010); OpenAlex **429 on first call, host stopped**; Semantic Scholar **429 on first call, host stopped**; Persée not queried | no print of the letter found; Grell's studies not read (JSTOR-QUEUE rows) |
| WebSearch | 1 query (Brienne, reine de Pologne, 1646, chiffre, Nivernois, Mantoue, Clairambault) | only the BnF catalogue entry and general context |

Unreachable or not searched: OpenAlex (429), Semantic Scholar (429), Persée, JSTOR (two rows queued), Gallica and
archivesetmanuscrits (other lane's host). None of these can move the class below N0; a print found there would only
add a citation (N0 with a print).

Files: `phrases.txt`, `sources.tsv`, `print-check.tsv`, `print-check-hosts.tsv` in this folder.

## 5. Postmortem

Failure named: the solver's early sections (2, "What the leaf shows", and "Status and next step") said there was no
interlined decipherment and that this was a blind-cryptanalysis target; the reconciler corrected both in place. The
check-solved "Verdict: Open. No published plaintext, decipherment ... found" is a time-stamped search result, but it
reads as current; annotated below. The status.json row said "novelty not yet classified"; now N0. No sentence in the
folder used new/unpublished/first wording; the H/C grading was already right.

Corrections made:
- NOTES.md: verifier block under the status line; the check-solved "Verdict" paragraph annotated as superseded.
- status.json: this item's results row, grade field states N0 and its qualifier.
- Status word: the line stays `open` (orchestrator's call), but by the rah-canada-1869 precedent (plaintext on the
  item, reading complete) `solved` is the fitting word; recommended to the orchestrator in ROOM.md.

Requests this audit: archive.org 15 (8 advancedsearch by hand, 7 by print_check), be-api.us.archive.org 25 (11
print_check, 14 fts by hand), www.googleapis.com 11 + 3, api.crossref.org 3, api.openalex.org 1 (429), api.semanticscholar.org 1 (429),
api.archives-ouvertes.fr 1, WebSearch 1. Gallica 0, de-crypt.org 0.

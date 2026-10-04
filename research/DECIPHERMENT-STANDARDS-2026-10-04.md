# Decipherment depth and acceptance: what the field actually does (research, 4 Oct 2026)

Research job for the owner's question: is there a best-practice standard for grading *how much* of a cipher has
been read, and for calling something "deciphered" rather than "partially deciphered"? It also checks the proposed
D0-D4 depth scale. Clock read at start: Sun 4 Oct 2026 04:09 UTC. Every quotation below comes from a page or PDF
opened in this session. Anything marked **[memory]** was not opened and must not be cited outward as it stands.
This file changes no rule. Nothing was committed.

## Summary

1. **There is no published standard.** Nobody in the field has a depth scale like D0-D4, and nobody uses a numeric
   threshold for "deciphered". DECODE, the main catalogue, has three status values per cipher record (Decrypted,
   Non-decrypted, Partially decrypted; keys get N/A). Its founding paper gives no definition or threshold for any of
   them. Each uploader's own judgement decides.
2. **In published decipherments, the word "deciphered" is looser than our proposed D4.** Lasry and Bonavoglia (2021)
   call a papal letter deciphered while some homophones and three nomenclature codes are still unread. Their
   transcription is marked "approximately", with `?` signs. Knight, Megyesi and Schaefer call the Copiale
   deciphered while eight logograms are still unread. By the field's own usage, a text with only names and codes
   left unread counts as "deciphered".
3. **Correctness is argued in four ways, usually together:**
   - (a) the plaintext is coherent and the key is consistent with itself;
   - (b) an external match: an original key table found later (Desenclos/Lasry, Nevers 1592), letters that match
     dated letters already known (Mary Stuart), or confirmation by an authority (the FBI for Z340);
   - (c) a known-answer test of the method on a synthetic cipher (Copiale, the same idea as our rule 3);
   - (d) Shannon's unicity distance, for short or contested texts (von zur Gathen on Z340; Shapiro, HistoCrypt 2026).
4. **The field measures depth as a share of tokens, and separately as a share of key types.** Lasry (2024) reports
   "decrypted text accuracy" (the share of ciphertext symbols decrypted correctly) apart from "reconstructed key
   accuracy" (the share of distinct symbol types assigned). Our % should use tokens as the denominator, with key
   coverage reported beside it.
5. **Unicity distance can set a minimum for D2.** It applies only to the cipher part, not to code groups: Shannon
   wrote "ciphers (not codes)". Shapiro proposes an "authentication distance" at 25-50% above unicity, and says a
   claim that fails it is "uncertain rather than necessarily false".
6. **For documentary editing (TEI P5 4.12.0) the vocabulary already exists:** `<unclear>`, `<supplied>` and `<gap>`,
   with reason and extent attributes, plus `@cert` (high/medium/low/unknown). The Jefferson Papers record who did
   the decoding. These cover "edition-ready" (D4) and how gaps are reported.

**Verdict:** keep D0-D4 and the rule "unique solve = N3+ and D2+". Make six changes:

1. Stop using "key identified" as the outward wording for D0-D1.
2. Define the percentage, giving its denominator.
3. Add a unicity or authentication-distance minimum to D2, for cipher (not code) material.
4. Allow D4 with a listed residue of unread names and codes, in line with Copiale.
5. Give DECODE's three values as a mapping.
6. Make depth a per-item verifier verdict, which is lowered whenever the reading is revised.

The exact wording is in the last two sections.

---

## 1. DECODE and the DECRYPT project

**Status values (confirmed).** The live search form's `<select name="x_status">` gives four codes: 1 Decrypted,
2 Non-decrypted, 3 Partially decrypted, 4 N/A. This was read from the form on 24 Sept 2026 and recorded in
`sources/decode/NOTES.md` lines 14-15, and the repo's harvest
`sources/decode/records-non-decrypted-2026-09-24.tsv` uses the same strings. At that harvest there were
801 Non-decrypted and 385 Partially decrypted cipher records.

**Definition in the founding paper.** Megyesi, Blomqvist and Pettersson, "The DECODE Database: Collection of
Historical Ciphers and Keys", *HistoCrypt 2019*, LECP 158, p. 71. Opened in the proceedings PDF
https://ep.liu.se/ecp/158/ecp19158.pdf :

> "Each cipher can also be marked on the basis of its Status, in terms of whether the cipher is decrypted,
> nondecrypted, or partly decrypted. For keys, the value of Status is non-applicable (N/A)."

That is the whole definition. No threshold, no evidence requirement and no note on who decides are given.

**Version 2.** Héder and Megyesi, "The DECODE Database of Historical Ciphers and Keys: Version 2", *HistoCrypt
2022*, doi:10.3384/ecp188397. The PDF was opened at https://ecp.ep.liu.se/index.php/histocrypt/article/download/397/355 .
Its metadata section names only these changes: creator vs owner, split dates, publications attached to records,
and key-cipher links. It says nothing about status. On future work:

> "This way several plaintext suggestions may be proposed by different groups or individuals for any given
> ciphertext record."

So DECODE expects competing readings and gives no rule for choosing between them.

**Transcription convention (DECRYPT).** Megyesi, "Transcription of Historical Ciphers and Keys", *HistoCrypt 2020*,
LECP 171, opened at https://ep.liu.se/ecp/171/014/ecp2020_171_014.pdf :

> "Uncertain symbols are transcribed with added question mark '?' immediately following the uncertain symbol.
> Possible interpretations of a symbol can be transcribed using the delimiter '/'. For example, if it is not clear
> if a symbol represents a 0 or 6, it is transcribed as '0/6?'. It is highly desirable that all symbols are
> transcribed somehow, and no symbols are left out in the transcription for reliable decryption."

Side note: `sources/lasry/PAPERS.tsv` gives the URL `ep.liu.se/ecp/171/014/...` for the Tunny paper, but that URL
serves this Megyesi paper. The row is mislabelled. It is reported here and not edited.

**Bearing on our scale:** DECODE's three values are the only shared vocabulary. Map onto them, and do not adopt
them as definitions, because they have none.

## 2. Acceptance in published decipherments

### Copiale: Knight, Megyesi, Schaefer 2011

"The Copiale Cipher", ACL BUCC workshop, opened at https://aclanthology.org/W11-1202.pdf .

- **Known-answer control before the target, the same idea as our rule 3:** "We confirmed that our computer attack
  does in fact work on a synthetic homophonic cipher, i.e., it correctly identifies the plaintext language, and
  yields a reasonable, if imperfect, decipherment. We then loosed the same attack on the Copiale cipher.
  Unfortunately, all resulting decipherments were nonsense".
- **Native-speaker correction step** ("hyp" vs "corr" lines). This was followed by: "This allowed us to virtually
  complete our table of substitutions".
- **Residue that does not stop the claim:** "The only remaining undeciphered symbols were the large ones: 9, @, #,
  %, 2, *, ±, and ¬. These appear to be logograms, standing for the names of (doubly secret) people and
  organizations". Three cipher letters are listed as ambiguous (SS/S, H/K, EN/EM).
- **Scope stated:** "It remains to transcribe the rest of the manuscript and to do a careful translation."
  The cipher system was declared deciphered on a sample, with the full transcription still to do.

### Lasry and co-authors, HistoCrypt (all PDFs opened)

- **Short Papal Cipher 1721** (Lasry and Bonavoglia, doi:10.3384/ecp188401,
  https://ecp.ep.liu.se/index.php/histocrypt/article/download/401/359). The paper is titled "Deciphering…", yet:
  "Some homophones could not be reliably assigned to letters (e.g., 67, 45) … The nomenclature elements (9336,
  9485, 9356) could not be identified, as additional material (e.g., additional or longer ciphertexts) is required
  for that task. The deciphered text can be approximately transcribed and as follows: Sopra il curato 45? 9441? 43?
  te diuinis 67? …". This is the field's working standard: the unread residue is listed inline with `?`, and the
  text is still published as a decipherment.
- **Letter from the French Wars of Religion** (doi:10.3384/ecp188402,
  https://ecp.ep.liu.se/index.php/histocrypt/article/download/402/360): "some partial results, that confirmed the
  hypothesis of a homophonic cipher, but this was not enough to read the encoded parts … the majority of the
  enciphered text could be finally deciphered so that it was mostly readable. The recovered (tentative) key … the
  meaning of several symbols could not be successfully identified … A tentative decryption of the deciphered
  passages … Work is in progress". This sits at our D3, reported with "tentative" and "mostly readable", without a
  percentage.
- **d'Avaux 1684** (doi:10.3384/ecp183162,
  https://ecp.ep.liu.se/index.php/histocrypt/article/download/162/118): "fragments of the ciphertext … were
  deciphered, and produced meaningful fragments of plaintext, validating the hypothesis." Meaningful fragments
  are used to validate the hypothesis about the cipher's structure, not to claim a reading. This matches our D1.
- **Armand de Bourbon 1649** (doi:10.3384/ecp195699,
  https://ecp.ep.liu.se/index.php/histocrypt/article/download/699/605): a key that is consistent with itself is
  treated as the test. "there is no way to 'fix' the key so that all those errors (we spotted over 150 such
  discrepancies) may be corrected", which led to a new hypothesis about the cipher's structure. The paper also
  says "The complete decipherment, after correcting the remaining errors…"
- **Deciphering Historical Syllabic Ciphers** (Lasry, HistoCrypt 2024, doi:10.58009/aere-perennius0106,
  https://dspace.ut.ee/server/api/core/bitstreams/75a7d17c-2e05-435a-a9ed-9d60f1e4ce10/content). This is the
  clearest *metric*: "The accuracy numbers refer to the decrypted text accuracy – the percentage of the ciphertext
  symbols in the documents correctly decrypted, and the reconstructed key accuracy – the percentage of the symbol
  types (distinct ciphertext symbols) correctly assigned. The accuracy of the decrypted text is always higher than
  the accuracy of the reconstructed key, as lower frequency symbol types are often ignored … In general, an initial
  accuracy of 40% or above is most often enough to decipher a ciphertext with the semiautomated process". The 40%
  figure is a point where the work can be finished by hand. It is not a threshold for accepting a reading. The
  accuracies were measured against keys already known.
- **External check by finding the original key** (Desenclos, Lasry et al., "An early French digit cipher … Duke of
  Nevers (1592)", HistoCrypt 2024, doi:10.58009/aere-perennius0090,
  https://dspace.ut.ee/server/api/core/bitstreams/db2fc9d2-8deb-4cb0-b049-68567b7ad161/content): "we were able to
  recover the full key"; one group "could be interpreted ('Picardye') only after finding the original table"; "The
  reconstructed key is essentially correct, but incomplete, as would have been expected given that it was
  recovered from a short letter with only 742 groups." This is our D3/D4 external check in practice: a key
  recovered by cryptanalysis was later compared with the period table.

### Mary Stuart: Lasry, Biermann, Tomokiyo 2023

*Cryptologia* 47(2):101-202, doi:10.1080/01611194.2022.2160677. The volume and pages come from OpenAlex. The
tandfonline full text answered 403 to the cloud, so the paper itself was **not opened**. What was opened is
Tomokiyo's own summary on disk, `sources/cryptiana/web/mary_castelnau_e.htm`. It says the letters "are entirely in
cipher, with nothing to indicate who wrote them to whom and when. Codebreaking revealed that most (54) of the
letters are letters written during 1578-1584 from Mary to Castelnau … more than 40 up to the middle of 1583 are
hitherto unknown letters", and also: "Four of them match the dates of known letters to Beaton and have some similar
contents."

Two kinds of external corroboration appear here: content matched to dated letters already known, and the
identification of sender and recipient from the plaintext alone.

**[memory]** Some of the post-mid-1583 letters overlap with copies already in English state papers, and the paper
compares against them. This is not verified here; read the paper's section on known copies before citing it.

### Zodiac 340: Oranchak, Blake, Van Eycke 2020

Von zur Gathen, "Unicity Distance of the Zodiac-340 Cipher", HistoCrypt 2022, opened at
https://ecp.ep.liu.se/index.php/histocrypt/article/download/395/353 :

> "Among the many solutions of Zodiac-340 that were proposed, which one is a 'better' one, or 'the correct' one?
> … there is a scientific answer to this question, based on Shannon's theory of unicity distance. It requires the
> description of a system of encryption using a secret key … any decipherment of a text which is longer than this
> value is highly likely to be unique and, within this theory, is accepted as correct."

> "The unicity distance for a ciphertext encrypted with a method as the Zodiac-340 cryptogram is between 80 and 152
> … The actual length 340 is much larger than this value. Our findings show that the solution is correct beyond
> doubt."

He counts every degree of freedom the solvers used (homophonic substitution, split into sections, transposition,
"a certain number of arbitrary changes in individual letters, such as spelling mistakes") in the key space. Each
liberty a solver allows raises the unicity distance.

**FBI confirmation:** the search-result snippets quote Oranchak: "We solved the 340 and submitted it to the FBI …
They have confirmed the solution." That comes from a search snippet of news coverage; the primary page was not
opened.

**[memory]** The plaintext's reference to a TV show matches a documented 1969 broadcast. This was a further
historical-fact corroboration; not opened here.

### Bogus solutions and authentication: Shapiro, HistoCrypt 2026

Shapiro, "A Brief Guide to the Authentication of Cryptanalytic Claims", *HistoCrypt 2026*, opened at
https://dspace.ut.ee/bitstreams/4d49cce0-b5b7-4429-893a-1eaa90de31fa/download . This is the nearest thing to a
published acceptance standard.

- "How does one know that a cryptanalytic solution is valid? Might another key have produced a different message?
  This uncertainty most frequently arises when the ciphertext is relatively short."
- "pseudo-cryptography can be most persuasively discredited using quantitative methods rather than qualitative
  arguments … demanding that claimants meet an objective standard based on quantitative measurement."
- **Authentication distance (AD):** following Reeds (1977), `AD = H(K)/R + 20/R`, giving no spurious solution at
  about 99.8%, about 25% above unicity for simple substitution. On top of this: "One might argue for a higher
  threshold, say, 50% above the unicity distance".
- The claimant "must carefully consider every arbitrary path taken to produce the putative plaintext". This is the
  same point von zur Gathen makes about liberties inflating the key space.
- **Bayesian point:** probability arguments must count all plausible plaintexts, not only the hoped-for one.
- **Conclusion:** "Might cryptologists set a standard threshold for authentication distance at, say, 50% above the
  unicity distance? … If a cryptographic claim meets the standard, it may then be presented as 'authenticated.' …
  Claims that fail authentication are uncertain rather than necessarily false. This is especially true when
  historical or literary context is present".
- He cites Schmeh (2012) on pseudo-cryptographic claims in the press, and Láng, "A Typology of
  Pseudo-Cryptology", HistoCrypt 2025, pp. 90-100. Neither was opened here.

**Schmeh / Cipherbrain:** no post laying out explicit criteria was found and opened in this session. The search
returned only index pages. The 27 local Cipherbrain snapshots in `sources/schmeh/` are item posts, not a methods
post. **[memory]** Schmeh's blog repeatedly rejects claimed solutions that need a flexible key or that read
different "plaintexts" from the same ciphertext. Treat that as unverified.

## 3. Documentary editing and TEI

TEI P5 4.12.0 (last updated 28 July 2026). Pages opened at tei-c.org/release/doc/tei-p5-doc/en/html/:

- **`<unclear>`** (ref-unclear.html): "Contains a word, phrase, or passage which cannot be transcribed with certainty
  because it is illegible or inaudible in the source." Its `@reason` takes values such as illegible and faded.
- **`<supplied>`** (ref-supplied.html): "signifies text supplied by the transcriber or editor for any reason; for
  example because the original cannot be read due to physical damage, or because of an obvious omission by the
  author or scribe." It carries `@reason`, `@source`, `@cert` and `@resp`. The page adds that "damage, gap, del,
  unclear and supplied elements may be closely allied in use".
- **`<gap>`** (ref-gap.html): "indicates a point where material has been omitted in a transcription … because the
  material is illegible". It takes `@reason` and the dimensions `@unit`, `@quantity`, `@extent` and
  `@atLeast/@atMost`. Example: `<gap quantity="4" unit="chars" reason="illegible"/>`.
- **`@cert`** (ref-att.global.responsibility.html): "signifies the degree of certainty associated with the
  intervention or interpretation". Its datatype `teidata.probCert` accepts a probability or a `teidata.certainty`
  value: **high | medium | low | unknown**. `@resp`: "indicates the agency responsible for the intervention or
  interpretation".

**Papers of Thomas Jefferson, editorial practice** (https://jeffersonpapers.princeton.edu/about/editorial-practice/):

- "For letters written in code, textual notes with superscript numerals are used and may be supplemented by the
  use of italics."
- "Textual notes also indicate whether the decoding was done by the recipient, someone else, or the editors."
- "Bracketed ellipses indicate missing, damaged, or undecipherable text."

Founders Online pages returned a 202 challenge to curl, so that host was not retried.

**Bearing on our scale:** editions do not grade depth. They mark each unread span where it occurs, with a reason and
an extent, and they name who decoded. Our H/C/S/M/I token grades already do more than `@cert`. What "edition-ready"
(D4) adds is that every unread or uncertain span is marked in place, as `<unclear>`/`<gap>`/`<supplied>` would be,
with its extent, and that the decoder is named.

## 4. Unicity distance as a criterion

Shannon, "Communication Theory of Secrecy Systems", *Bell System Technical Journal* 28 (1949), opened at
https://pages.cs.wisc.edu/~rist/642-spring-2014/shannon-secrecy.pdf :

> "with ordinary languages and the usual types of ciphers (not codes) this 'unicity distance' is approximately
> H(K)/D … Thus unicity occurs at about 30 letters." [for simple substitution, English]

> "the material was so meager that the question arose as to whether the cryptanalyst had 'read a solution' into
> the cryptogram. See, for example, the Bacon-Shakespeare ciphers and the 'Roger Bacon' manuscript. In general we
> may say that if a proposed system and key solves a cryptogram for a length of material considerably greater than
> the unicity distance the solution is trustworthy. If the material is of the same order or shorter than the
> unicity distance the solution is highly suspicious."

Applied to historical ciphers:

- Lasry, "Solving a 40-Letter Playfair Challenge with CrypTool 2", HistoCrypt 2019 (same proceedings PDF):
  "The unicity distance can be viewed as a theoretical lower-bound for the length of a cryptogram, so that its key
  may be recovered via cryptanalysis." Unicity is 22.69 letters for Playfair in English, after Deavours (1977).
  He also reports that "Initial runs only produced spurious solutions".
- Von zur Gathen on Z340, and Shapiro, are covered in section 2.

**Limits for our material, from the sources:**

- Shannon excludes codes. A nomenclator's code groups have no unicity distance in this sense, because each group is
  its own key entry. A code reading is supported by the same value recurring and reading sensibly across
  occurrences, or by an H/C source. Length alone does not support it.
- Every liberty a reading allows (nulls chosen afterwards, homophone splits, "spelling errors", segmentation
  choices) adds to H(K). That is von zur Gathen's and Shapiro's central warning.
- Language redundancy for 16th-18th century orthography is lower and less certain than for modern English. Shapiro
  notes that redundancy estimates "assume (possibly inaccurately) that a clean plaintext is under test". Our rule 3
  already requires language corpora matched to the era, and the same corpus should give R.

---

## Verdict on D0-D4 and the wording

**Keep:** the five levels, "unique solve = N3+ AND D2+", and an external check for D3/D4. Every source supports the
idea of external corroboration (Nevers original table, Mary Stuart dated letters, Z340 FBI and unicity, Copiale
synthetic control). Depth as a separate axis from novelty is also sound. The field mixes the two, and that is how
over-claims happen.

**Change:**

1. **D0 outward wording.** "Key identified" over-claims for D0. If nothing reads, no key has been *identified*, only
   ranked first by our scorer. Shannon's "highly suspicious" and Lasry's "spurious solutions" describe exactly this
   case. Proposed outward words:
   - D0: "not deciphered (a candidate key ranks first; nothing reads)", normally not reported outward at all;
   - D1: "fragments read".
   - Reserve "key identified" for a key matched to a *period* key source (H grade) or a published key, whatever the
     depth. That is a statement about where the key came from, which AUDIT.md already records as
     ours/period/published.
2. **Define the %.** Follow Lasry (2024): the share of *ciphertext tokens* (excluding transcribed cleartext and
   nulls) whose reading is graded H, C or S. Report beside it the share of distinct cipher/code types assigned, and
   the count of unread tokens split into (a) name/code groups and (b) other. "About 80% firm" then becomes
   measurable from `tools/decode_key.py`'s grades.
3. **D2 minimum length.** The read passage must be unambiguous on more than chance. For *cipher* material (letters,
   syllables), the contiguous stretch graded S or better must exceed the authentication distance for the design,
   ≈1.5 × unicity per Shapiro, with H(K) counting every liberty the reading took. The alternative is an external
   check. For *code* material, at least one value must recur in ≥2 independent contexts that both read sensibly,
   or carry H/C grade.
4. **D4 may carry a listed residue.** Copiale and the papal 1721 letter are both called deciphered with names,
   logograms or nomenclature codes unread. D4 = every cipher-letter token read (H/C/S), with only listed name/code
   groups unresolved. Each of those is marked in place with its extent, TEI-style, and counted. Outward wording:
   "deciphered; N code groups (names) unidentified". Without this, D4 is unattainable for almost any nomenclator
   letter, and D3 would absorb texts the field calls deciphered.
5. **D3 vs D4 external check.**
   - D3: an external check, **or** a passed authentication distance plus a rule-3 matched control at the target's
     length and design.
   - D4: a non-statistical external check (a period key/table, a period decipherment or gloss, a known-answer copy
     of the plaintext, or a historical fact in the plaintext confirmed in an independent source) **and** a fresh-
     session re-derivation under rule 7.
   - Statistics alone never give D4. Shapiro: a failed authentication is "uncertain rather than necessarily
     false", but a passed one is evidence about uniqueness, not about content.
6. **DECODE mapping, for contributions:**

   | Our depth | DECODE status |
   |---|---|
   | D0, D1 | Non-decrypted |
   | D2, D3 | Partially decrypted |
   | D4 | Decrypted |

   State it as a mapping. DECODE itself defines nothing (HistoCrypt 2019, p. 71).
7. **Per item, verifier-set, and lowered on revision.** Depth is given per letter or leaf, not per folder. It is set
   by the verifier, never by the solver, the same as the N-class. A rule-7 re-derivation or blind-pass correction
   that lowers the firm % propagates into AUDIT.md and status.json, the same as rule 10's propagation clause.

**Outward wording (replaces the proposal's):**

| Depth | Meaning | Outward words |
|---|---|---|
| D0 | candidate key ranks first, nothing reads | none (internal only) |
| D1 | scattered words, below authentication distance | "fragments read" |
| D2 | ≥1 clause above AD (or code recurring/H); verifier writes one true specific sentence | "partially deciphered (about N% of the cipher text)" |
| D3 | ≥80% of tokens H/C/S; gaps mostly names/codes; external check or AD + matched control | "largely deciphered (about N%)" |
| D4 | all cipher-letter tokens read; residue = listed name/code groups only; external non-statistical check + re-derivation | "deciphered" / "deciphered; N name codes unidentified" |

"Key identified" is used only for a key matched to a period or published key, whatever the depth.

## Suggested verifier-template step

Insert after step 3 of the CLAUDE.md verifier template (proposed; this file edits nothing):

```
3a. Depth, per item: count ciphertext tokens (excluding cleartext and nulls) and the share graded H/C/S by
    tools/decode_key.py; list unread tokens as name/code groups vs other. Assign D0-D4:
    D1 if no S-or-better cipher stretch exceeds the authentication distance (about 1.5 x unicity for the
    design, counting every liberty the reading took in H(K)) and no code value recurs readably in two
    contexts; D2 if one does and you can write one true, specific sentence about the content; D3 if >=80%
    of tokens are H/C/S, the gaps are mostly names/codes, and there is an external check or a passed
    authentication distance plus a rule-3 matched control at this length and design; D4 only if every
    cipher-letter token is H/C/S, the residue is listed name/code groups marked in place with extent, a
    non-statistical external check is named (period key/table, period decipherment or gloss, known-answer
    copy, independently confirmed historical fact), and a fresh-session --check re-derivation agrees.
    Write the depth, the %, the residue counts and the check used into AUDIT.md beside the N-class; outward
    words follow the depth table (D0 none, D1 "fragments read", D2 "partially deciphered (about N%)", D3
    "largely deciphered (about N%)", D4 "deciphered"). "Key identified" only for a period/published key.
```

## Suggested status.json fields (on the result object, beside `key` and `text`)

```json
"depth": "D0" | "D1" | "D2" | "D3" | "D4",
"depth_pct": 0-100,                      // share of ciphertext tokens graded H/C/S
"depth_key_pct": 0-100,                  // share of distinct cipher/code types assigned (Lasry 2024)
"depth_unread": {"names_codes": n, "other": n},
"depth_check": "none" | "auth-distance" | "known-answer" | "period-key" | "period-gloss" | "historical-fact" | "authority",
"depth_by": "<verifier session id>",
"depth_date": "4 Oct 2026",
"decode_status": "Non-decrypted" | "Partially decrypted" | "Decrypted"   // derived: D0-1 / D2-3 / D4
```

`unique_solve` = `nclass >= N3 && depth >= D2`, computed, not typed.

## Requests made (good-citizen log)

| Host | Requests | Result |
|---|---|---|
| ecp.ep.liu.se | 7 | all 200 |
| ep.liu.se | 2 | 200 |
| dspace.ut.ee | 4 | 200 |
| aclanthology.org | 1 | 200 |
| pages.cs.wisc.edu | 1 | 200 |
| tei-c.org | 5 | 200 |
| jeffersonpapers.princeton.edu | 1 | 200 |
| tandfonline.com | 2 | 403, not retried |
| founders.archives.gov | 2 | empty, then 202 challenge; stopped |
| diva-portal.org | 1 | connection reset, not retried |
| api.openalex.org | 1 | keyed |
| api.semanticscholar.org | 1 | keyed |
| web searches | 6 | |

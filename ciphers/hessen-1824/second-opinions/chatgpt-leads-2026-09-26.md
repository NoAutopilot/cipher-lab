label: SO-HESSEN1824-LEADS
model: GPT-5 (Codex)
date: 2026-09-27 UTC
prompt: PROMPT-chatgpt-leads.md in this folder

# Leads, not verdicts

## Adversarial check on the present framing

- I located no source that transcribes or solves HStAM 9 a Nr. 259, f. 249. HCPortal record 513 still reports the item as not solved and supplies no key; Daniel Bourdeau's catalogue entry is a discovery record, not a decipherment. Bibliographic authorship of the HCPortal record is **unverified** in the public interface; the repository's live-API check identifies Eugen Antal as its creator. [HCPortal, "Database of Cryptograms and Cipher Keys," record 513 (metadata accessed 2026), https://api.hcportal.eu/api/cryptograms/513; Daniel Bourdeau, "The Unsolved Catalogue," item 340 (2026), https://dbourdeau.github.io/cyphersolver/catalogue.html; NoAutopilot/cipher-lab, "Hessian polyalphabetic message, 20 Feb 1824," NOTES.md (2026), https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/hessen-1824/NOTES.md.]
- The label "polyalphabetic" is not an independently demonstrated algorithm identification. It may derive from the German annotation on the leaf. The current solver record excludes periodic Vigenère/Beaufort-style shifted alphabets at periods 2–20 on one uncertain transcription; it does **not** exclude a period-7 general polyalphabetic substitution with seven independently permuted alphabets. The annotation's top-row sequence `bcdefg(h)`, its instruction to write those "resolution letters" continuously above the cipher, and the seven-column example make that omitted family the strongest technical lead.
- The running-key hypothesis is now weaker than the queued prompt implies. After the prompt was written, the repository ran a separate dictionary crib-drag whose matched control recovered all five planted words within the top 11 candidates, while the target produced no comparable score or positional cluster. That is a control-backed negative for the tested natural-language running-key design, although it does not address an unknown tableau, a non-language key, or transcription error. [NoAutopilot/cipher-lab, NOTES.md, section "HES-DRAG" (2026), https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/hessen-1824/NOTES.md; NoAutopilot/cipher-lab, HYPOTHESES.md, section "HES-DRAG" (2026), https://github.com/NoAutopilot/cipher-lab/blob/main/ciphers/hessen-1824/HYPOTHESES.md.]
- Every negative remains conditional on the M-grade blind transcription. Three digit-like signs, uncertain word/group boundaries, and an unresolved Kurrent annotation are enough to spoil a 164-character test. A second image transcription and a diplomatic transcription of the annotation have higher expected value than another unconstrained solver run.

## 1. More ciphertext from the same system

### Highest-value archival request

Request or inspect the **entire archival unit HStAM 9 a Nr. 259**, not only f. 249. Ask for:

1. f. 249 recto and verso at native resolution;
2. at least the neighboring leaves f. 245–255, preserving archival order;
3. every enclosure or slip marked `No. 1`, `No. 2`, `Zettel`, `Chiffre`, `Schlüssel`, `Auflösung`, `Anmerkung`, or `Concept`;
4. transmitted-light or multispectral imaging if any leaf appears blank or interleaved, because the annotation explicitly mentions writing between lines with invisible/sympathetic ink;
5. the file cover, old foliation, accession notes, and any later archivist's description.

This request is unusually well supported by the page itself: the annotation reportedly refers to "No. 1" and to two kinds of slips. That language points to a small packet or worked example rather than an isolated ciphertext. Even one sibling carrying the same seven heading letters, a clearer copy of the table, or a plaintext/ciphertext pair would be more useful than multiplying generic corpora.

### Search the creating office, not just the date

Best. 9 a is the **Kurhessisches Ministerium der auswärtigen Angelegenheiten und des kurfürstlichen Hauses**. In 1821 the state's highest authority was reorganized as a collegial Staats-Ministerium under the ruler, with ministerial departments rather than purely personal ministries. That provenance suggests searching the registry and business-process records for cipher instructions, copying practices, and incoming enclosures, rather than assuming the leaf is an ordinary diplomatic dispatch. [Niklas Lenhard-Schramm, "Behördenbezeichnungen im Wandel" in *Archivnachrichten aus Hessen* 23/1 (2023), p. 58, https://landesarchiv.hessen.de/sites/landesarchiv.hessen.de/files/2023-06/hla_archivnachrichten_1-2023_6.pdf.]

Within Arcinsys and the paper finding aids, search Best. 9 a and closely related Bestände for the stems `Chiffr-`, `Ziffer-`, `Geheimschrift`, `Schlüssel`, `unsichtbare Tinte`, `sympathetische Tinte`, `Drohbrief`, `anonyme Briefe`, `Zettel`, and `Auflösung`, with a date window of 1821–1831. Do not limit the query to Nr. 259: a key or sibling message may have been separated into a correspondence, personnel, police, or cabinet series.

### A concrete contextual fork: the Kassel threat-letter affair

The date, 20 February 1824, falls inside the investigation of anonymous letters directed against Elector Wilhelm II and Countess Reichenbach. Friedrich Murhard was arrested in January 1824 after being suspected in that affair; the state formed a special commission, and related records survive in HStAM Best. 267, Best. 261, and Best. 250 Nr. 780. The leaf's reference to hidden writing and multiple slips makes this a serious provenance lead, but **not evidence that Murhard wrote the cipher**. [Peter Michael Ehrle, "Murhard, Friedrich Wilhelm August," *Neue Deutsche Biographie* 18 (1997), pp. 610–611, https://www.deutsche-biographie.de/downloadPDF?url=sfz67436.pdf; Hans-Jürgen Kahlfuß, "Der Prozeß gegen Friedrich Murhard 1843–1848," *Zeitschrift des Vereins für hessische Geschichte* 108 (2003), pp. 123–147, especially p. 140 on the 1823 suspicion, https://www.vhghessen.de/inhalt/zhg/ZHG_108/09_Kahlfuss_Prozess%20gegen%20Friedrich%20Murhard.pdf; Hessisches Institut für Landesgeschichte, "Festnahme des Oberpolizeidirektors Ludwig von Manger in Kassel, 10. Juli 1824" (version dated 2025), archival links to HStAM Best. 267, 261, and 250 Nr. 780, https://www.lagis-hessen.de/de/subjects/idrec/sn/edbx/id/6185.]

Actionable comparison: ask whether Best. 267 or 261 contains encrypted slips, invisible-ink tests, handwriting exemplars, deciphering memoranda, or an inventory using the same "No. 1"/"No. 2" labels. Compare paper, hand, headings, and the seven-column table before comparing textual content. A provenance match would sharply narrow vocabulary and candidate correspondents; a mismatch would close this contextual fork.

### Pooling design

If siblings are found, preserve each message's lineation, punctuation, anomalous digits, headings, and phase. Pool only after testing whether the same cipher-to-plain relations recur in the same modulo-7 columns. A safe pooling criterion is held-out consistency: infer a mapping from all but one message and require it to decode the held-out message above a shuffled-message control. Messages should not be concatenated blindly because each may restart the seven-letter cycle at a different phase.

## 2. Catalogue descriptions, finding aids, and archival-history leads

- **Arcinsys/Hessisches Landesarchiv:** obtain the full scope note, old signatures, registry order, and digitization manifest for HStAM 9 a Nr. 259. The web-indexed material identifies Best. 9 a as the foreign-affairs/electoral-house ministry, but I did not recover an item-level description beyond the current repository/HCPortal metadata. The precise request to the archive is: "What is the complete title and extent of Nr. 259; what do ff. 245–255 contain; and are there detached enclosures, old foliation, or cross-references to Best. 267/261?" This catalogue lead is **unverified** until the archive supplies the file-level entry.
- **A contemporary technical comparator:** Johann Ludwig Klüber's 1809 *Kryptographik* is a 502-page German manual on ciphering and deciphering in state and private business, with tables and discussion of Vigenère-style systems, key words, and practical correspondence. It predates the leaf by fifteen years and is a better vocabulary/template source for interpreting `Auflösungsbuchstaben`, `Schlüssel`, and table layout than a modern English cipher taxonomy. Do not presume the Hessian clerk used Klüber's exact system; compare the annotation's wording and diagram against Klüber's plates and table instructions. [Johann Ludwig Klüber, *Kryptographik: Lehrbuch der Geheimschreibekunst (Chiffrir- und Dechiffrirkunst) in Staats- und Privatgeschäften* (Tübingen: Cotta, 1809), https://books.google.lk/books?id=nKtfAAAAcAAJ.]
- **Regional cipher practice:** Anne-Simone Rous shows that German chancelleries retained packets of obsolete and current cipher tables and that allied courts exchanged cipher material; her examples are Saxon and mostly earlier, so they are analogues, not proof about Kurhessen. Her archival method—searching accumulated "Allerhand Chiffren"/"Verschiedene Chiffren" packets rather than only named correspondents—is directly transferable to HStAM. [Anne-Simone Rous, "Geheimschriften in sächsischen Akten der Neuzeit," *Neues Archiv für sächsische Geschichte* 83 (2012), pp. 243–253, especially pp. 252–253, https://nasg.journals.qucosa.de/nasg/article/download/781/695/744.]
- **Correspondence-form scholarship:** the 2024 Hessian volume *Fürstliche Korrespondenzen des 19. und 20. Jahrhunderts* includes Karsten Uhde on archival forms and Rouven Pons on concealment/self-disclosure. The table of contents does not establish treatment of Nr. 259, so any relevance to this leaf is **unverified**; the authors are nevertheless well-placed leads for provenance, enclosure practice, and how coded material was filed. [Rainer Maaß and Rouven Pons, eds., *Fürstliche Korrespondenzen des 19. und 20. Jahrhunderts* (Marburg: Historische Kommission für Hessen, 2024), contents pp. 3–4, https://landesarchiv.hessen.de/sites/landesarchiv.hessen.de/files/2024-08/furstl_korrespondenzen_inhalt.pdf.]

### Prior-print and prior-decipherment check

The accessible HCPortal metadata, Bourdeau catalogue, Klüber manual, Rous article, Hessian archival-history pages, and Murhard/threat-letter studies do not supply a transcription, plaintext, or key for f. 249. That is only a search result for this pass, not a novelty judgment. The strongest prior-art risk is not a cryptology publication but an unnoticed plaintext, key table, or clerk's solution elsewhere in Nr. 259 or in the special-commission records.

## 3. Scholars and custodians worth contacting

1. **Hessisches Staatsarchiv Marburg reference archivist responsible for Best. 9 a and Best. 267.** Ask the file-structure questions above and request the neighboring leaves before asking for cryptanalysis. The HIL/LAGIS event page already points to Best. 267 and 261 as the core threat-letter holdings. [Hessisches Institut für Landesgeschichte, "Festnahme des Oberpolizeidirektors Ludwig von Manger" (2025), URL above.]
2. **Anne-Simone Rous.** Her article is the closest identified scholarly match for German chancery cipher packets, exchange of tables, and archival survival patterns. Ask whether she knows a Kurhessian counterpart to the Saxon "Allerhand Chiffren"/"Verschiedene Chiffren" bundles or recognises the vocabulary `Auflösungsbuchstaben`.
3. **Rainer Maaß, Rouven Pons, or Karsten Uhde.** Their 2024 Hessian correspondence volume makes them strong provenance and record-form leads; whether any has worked directly with Best. 9 a Nr. 259 is **unverified**. [Maaß and Pons, eds., *Fürstliche Korrespondenzen* (2024), URL above.]
4. **Eugen Antal / HCPortal cryptogram database team.** The repository's API capture attributes record 513 to Eugen Antal, while HCPortal's contributors page lists E. Antal among the cryptogram/key database contributors. Ask what source justified the "polyalphabetic" classification, whether any sibling images were omitted from the public record, and whether the three digit-like signs were transcribed elsewhere. Item-level authorship and current contact details are **unverified**. [HCPortal, "Contributors" (page accessed 2026), https://hcportal.eu/contributors.html.]
5. **Sravana Reddy and Kevin Knight, or a researcher reproducing their method.** Their blocked Gibbs sampler jointly models plaintext and running-key language and explicitly discusses unknown keyed substitution functions. This is useful if archive work confirms a natural-language running key, but it is secondary to reconstructing the seven-column table. [Sravana Reddy and Kevin Knight, "Decoding Running Key Ciphers," *Proceedings of ACL 2012*, pp. 80–84, https://aclanthology.org/P12-2016.pdf.]

## 4. Solver and method recommendation at N=164

### A. Test the omitted seven-phase family

Model the note literally before applying any generic running-key solver:

- Assume a repeating phase sequence of six or seven "resolution letters" (`bcdefg` or `bcdefgh`), with all seven starting phases.
- Allow each phase to have an independent monoalphabetic permutation, rather than requiring Caesar shifts as Vigenère/Beaufort does.
- Encode the small table as hard or soft constraints only after a second Kurrent transcription. Test both orientations: cipher pair → plaintext row label, and plaintext row label → cipher pair.
- Treat `4` and `3` as separate symbols, nulls, numerals, or misread letters in separate pre-registered variants.
- Use a German character/word model appropriate to 1810–1830, but judge only against matched synthetic controls with N=164, K≈24, identical punctuation loss, and the same number of constrained table cells.
- Require the recovered seven mappings to generalize to held-out lines or a sibling message. A readable-looking single fit is not enough.

This family explains why the current tests can all fail simultaneously: a general period-7 substitution is neither a standard shifted-alphabet Vigenère cipher nor one global simple substitution. Its cosets are only about 23–24 letters each, so the annotation or pooled siblings are essential.

### B. Reconstruct the page mechanism as a constraint problem

The annotation appears closer to an operational deciphering instruction than to a casual archivist's label. Build a facsimile table from the image:

1. transcribe every heading, row label, and pair with uncertainty sets;
2. enumerate table geometries consistent with seven columns;
3. generate the implied cipher/plain relations;
4. score only relations licensed by a geometry;
5. compare against geometries with shuffled headings and shuffled pair placements.

This can identify whether the note operates on the ciphertext even before fluent plaintext emerges. It also distinguishes a periodic alphabet table from a running text key.

### C. If running key survives the archival check, use blocked word sampling

Reddy and Knight's blocked Gibbs method is the best documented alternative to the present two-stream beam: it samples word boundaries and words in both plaintext and key, with interpolated word- and letter-level language models. On their English benchmarks, average accuracy at length 100 was 42% on Gutenberg and 58% on Wall Street Journal text; at length 1000 it rose to 88–93%. Those results warn that N=164 is underdetermined and register-sensitive, but they justify a German matched-control implementation. [Reddy and Knight, "Decoding Running Key Ciphers" (2012), pp. 80–84, especially Table 2, https://aclanthology.org/P12-2016.pdf.]

A reproduction should train on multiple independent 1810–1830 German folds, include historical spelling, and test tabula recta, Beaufort, variant Beaufort, and any table reconstructed from the annotation. Report recovery over many N=164 controls, not one. Alexander Griffing's 6-gram Viterbi method is another baseline, but its strong published results concern 1000-character English texts and an in-domain language model, not a 164-character German leaf. [Alexander Griffing, "Solving the Running Key Cipher with the Viterbi Algorithm," *Cryptologia* 30:4 (2006), pp. 361–367, https://www.cs.mcgill.ca/~mpayne/docs/Griffing-Viterbi.pdf.]

### D. Candidate key texts only after provenance narrows the case

If the threat-letter connection is confirmed, build a small, documented candidate corpus from texts plausibly available to the participants: Murhard's *Allgemeine politische Annalen* (1821–1824), the Kurhessian Gesetz-Sammlung, political proclamations, and Klüber's 1809 manual. This is a constrained source-search lead, not a claimed key. Murhard's editorship of the *Annalen* and his January 1824 arrest are documented; connection of f. 249 to him is **unverified**. [Ehrle, "Murhard" (1997), pp. 610–611, URL above; Kahlfuß, "Der Prozeß gegen Friedrich Murhard" (2003), pp. 123–147, URL above.]

If the archive instead identifies a diplomatic correspondent, replace that corpus with the correspondent's office print: state calendars, protocol volumes, dispatch registers, and frequently quoted books. Searching millions of generic German characters is lower value than locating the actual sibling slip or table.

## Confidence and ordering

- **High confidence:** obtain a second transcription; read the annotation diplomatically; inspect all of Nr. 259 and its "No. 1"/slip context.
- **High confidence:** the existing tests do not cover a seven-phase general substitution with independent alphabets.
- **Medium confidence:** Best. 267/261 threat-letter records are a valuable provenance cross-check because of the date, anonymous-letter investigation, and hidden-writing language.
- **Medium confidence:** a control-backed German blocked-Gibbs implementation is the remaining serious running-key algorithmic test.
- **Low confidence:** Murhard, his journal, or any named contemporary text is the actual key source.

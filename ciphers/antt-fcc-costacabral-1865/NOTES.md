solved

> **Verifier, 25 Sept 2026 (AUDIT.md, V6-COSTA): N0, key `period`.** The encipherer's own Portuguese plaintext is
> written above every code on m0113-m0114, so the plaintext of this very item is on the leaf; no printing of the letter
> or its text was located (search log in AUDIT.md). Status `solved`, not `found-solved` (nothing in print; precedent
> clair1067-brienne-poland-1646). Recipient: Costa Cabral, Conde de Thomar, envoy to the Holy See. [V6 25 Sept 2026]

Read by this worker, 25 Sept 2026: the item's own three images (m0112 the plaintext cover letter; m0113-m0114 the
cipher draft, with the plaintext syllable written directly above almost every number) -- no printed edition or
calendar was located for this archival draft [V6 25 Sept 2026: "unpublished" struck; the 1887 Livro Branco,
Negocios externos (Santa Sé), prints the surrounding papal-letter affair but not this letter -- AUDIT.md s.4]. Full-text search
(be-api.us.archive.org/fts/v1/search, 0 hits for `"Costa Cabral" "Conde d'Avila" 1865 cifrada`; advancedsearch.php
by title+date range, 0 items) and Google Books (`GOOGLE_BOOKS_KEY`, 0/300 relevant hits across `"Costa Cabral"
"Conde d'Ávila" 1865 carta cifrada`, `"Caetano de Magalhães" 1865 Padroado`, `"Costa Cabral" correspondencia 1865`;
the 300-hit query returned only unrelated catalogues and an unrelated Fonseca Magalhães correspondence volume)
found no prior print or decipherment. BNP bndigital's `?q=` search parameter does not restrict results (every
query, including this one, returned "51732 Resultados" -- the whole catalogue, the same non-functional-search-box
shape CLAUDE.md's Access playbook already logs for the Huntington CONTENTdm naive query -- so this route is logged
as unreachable, not read as a negative). DECODE's public RecordsList crawled in full and login-free
(`tools/decode_list.py --status non-decrypted,partially-decrypted,decrypted,n/a --record-type cipher`, 2897 cipher
records to `/tmp/decode-costacabral-check.tsv`, not committed since it is a general catalogue snapshot not specific
to this item) has no Costa Cabral or FCC row. Web search (Portuguese and English) for the letter, the correspondents
(Caetano de Magalhães, Conde d'Ávila) and the 1865 Padroado/Santa Sé negotiation found nothing specific to this item
-- only unrelated Costa Cabral family letters and 20th-century ambassador lists. Cryptiana and Cipherbrain checked
by web search (`cryptiana OR cipherbrain "Costa Cabral" OR "FCC" Torre do Tombo cipher`), no hit. Both solver
repositories grepped (`dbourdeau/cyphersolver`, `aaymeloglu/unsolved-ciphers`, depth-1 clones 25 Sept 2026,
`grep -ril -i "costa cabral\|FCC/001/0021\|costacabral"`), zero hits in either. No calendar or state-paper series
applies to a private family-fonds draft with no independent print history, so this check-solved sweep is over the
item and its correspondents, not a datable letter in a numbered series.

## The unit

ANTT `PT/TT/FCC/001/0021/00026` -- fonds Família Costa Cabral, sub-fonds "Documentação pertencente a António
Bernardo da Costa Cabral -- correspondência de várias pessoas sobre assuntos políticos". Viewer:
`https://digitarq.arquivos.pt/fileViewer/b482fac086d54e2bae791264bb78b79f` (docId
`b482fac086d54e2bae791264bb78b79f`), CC BY-SA 4.0, no login. Catalogue note: "Inclui um rascunho de uma cópia de
carta cifrada: (...) pa-pa (419-419), di-ga-mo (926-923-1212) [...]". Scouted by scDIGI2 (LANE N4, 24 Sept 2026,
ROOM.md 21:26) via DigitArq unit-description search; re-fetched full-resolution here with `tools/digitarq_fetch.py`
(3 requests, `--list` + `--full`, >=3 s apart, no retries needed).

3-image item, all now on disk at `images/full_PT-TT-FCC-001-0021-00026_m01{12,13,14}.jpg.jpg` with
`images/filelist.json` (ids 13958080-13958082, one `representationID`):

- **m0112**: plaintext (Portuguese, H grade -- read directly off the image), headed "Reservadíssimo" and "1865",
  addressed "Meo Caro Conde". Body: the Secretaria writes on behalf of the ill Foreign Minister, the Conde d'Ávila,
  about a matter needing "grande segredo e reserva". It refers to a letter from "Sua Santidade" (the Pope) whose
  reply goes with the official dispatch; that reply had been left with the former minister, the Duque de Loulé, and
  never reached the Secretaria. The recipient ("Conde") is asked to obtain, with the greatest discretion and
  without the Pontifical government suspecting the reason, a copy of the Pope's letter, and to forward it to the
  Minister as "um bom serviço e um obséquio especial" -- an unrelated-to-cipher but historically dense item: a
  covert Portugal-Vatican channel over what appears to be a stalled or missing papal communication during the
  Padroado dispute, 8 July 1865, signed "Secretaria, 8 Julho 1865, Caetano de Magalhães" (the sender), self-
  described as a friend "dos bellos tempos de Coimbra" (of the old Coimbra days) -- i.e. an old university friend
  of the addressee, not a formal diplomatic register between strangers.
- **m0113-m0114**: the cipher draft itself (H grade for the plaintext syllables, read directly off the image; the
  numeric groups are the ciphertext, transcription not attempted this pass -- out of this brief's scope). A
  4-digit-max nomenclator worksheet: the plaintext syllable or short word is written directly above almost every
  number, e.g. "con-fi-dev-ci-ar" / "99-629-737-20-428", "el-Rei-de-se-ja" / "903-342-456-103-870",
  "pa-dri-nho-do-prin-ci" / "419-135-151-25-204-20" (m0113), "sou-ber-al-ge-ma" / "618-323-428-2111-742",
  "as-elo-pa-pa-di-ga-mo" / "12-25-419-619-926-923-1212" (m0114, matching the catalogue's quoted
  "di-ga-mo (926-923-1212)" and "pa-pa (419-419)" fragments). This is a self-glossed encoding worksheet -- the
  clerk's own scratch copy while enciphering, not a later, independent decipherment -- so it hands over roughly
  four to five dozen syllable/word-to-number pairs directly, several numbers repeating across lines (419, 617,
  988, 1087 each appear more than once, consistent with a fixed nomenclator rather than a one-time pad). Numbers
  observed range from two digits (e.g. 11, 12, 20, 25, 60) to four digits (max seen 2111, on "ge"); most syllables
  are 1-3 letters, with a few full short words ("Rei", "que", "de"). No independent ciphertext (a version without
  the interlined gloss) is visible on these three images -- the draft itself, gloss and numbers together, is all
  that was fetched. Two faint crosses ("+") mark two of the number groups on m0113, cause not established this
  pass.

## Next step (not this brief)

Per the brief, no key extraction this pass. The natural next step is a transcription of every syllable-number pair
into a `key.tsv` (recovery kind, key source `ours`: rebuilt from the clerk's own contemporary worksheet, not a
later or published key) -- this is a straightforward reading task, not cryptanalysis, since the plaintext is
already interlined; the harder part is confirming trim/joining rules where syllables run together across a line
break, and locating (or accepting the absence of) a "live" ciphertext-only copy of the same letter elsewhere in
this fonds to check the key against.

## P5: key and reading from the draft (25 Sept 2026, LANE R6)

Status moved to `found-solved`: the codes and their plaintext syllables sit on the same leaf, so this is a
transcription-and-reconciliation task, not cryptanalysis. Process: pass A (this worker, direct image read with
PIL crops enlarged 3-6x) and one blind Sonnet subagent pass B (same two raw images, no access to pass A or any
existing transcription), both written to `passes/passA.tsv` / `passes/passB.tsv` (page/line/pos/code/syllable/conf,
one row per code-syllable pair), then reconciled by hand against the image rather than `tools/reconcile_passes.py`
(that tool's Needleman-Wunsch aligner is built for one sign per position in a plain ciphertext transcription; here
every position carries two independent readings -- a digit code and a gloss syllable -- so a straight join on
page/line/pos and a per-position comparison was more direct, `disagreements.tsv`, 25 rows). 12 lines on m0113
(63 pairs), 4 usable lines on m0114 (21 pairs; a 5th row is illegible under a printed "T" watermark overlay in
this scan and is not transcribed). `key.tsv` (52 rows, one per code observed -- three codes get two rows each
because the two occurrences carry different values, see Collisions below) and `ciphertext.tsv` (84 tokens, the
codes in drafting order) feed `decode.json`; `tools/decode_key.py ciphers/antt-fcc-costacabral-1865 --check`
exits 0.

**Grade counts (rule 4): C 63, M 19, U 2, of 84 tokens.** [V6: the basis of C is the leaf's own gloss, known
plaintext; the checks below are transcription checks on it.] C = the code's value is read consistently across its
occurrences and/or confirmed by a second source (both blind passes, the archival catalogue's own quoted pairs, or
LANE R6 P4's independent earlier read of the m0114 R1 line in ROOM.md, 25 Sept 2026). M = a single low-confidence
reading, a pass-A/pass-B disagreement not settled from the image at the resolution this scan allows, or a code
that collides with a different value elsewhere (both readings kept, `key.tsv` lets `tools/decode_key.py`'s own
`merge_key_row` combine them into `value1|value2`, auto-downgraded to M, rather than one silently overwriting the
other). U = 2 codes (206 on m0113 L8, 836 on m0114 R2) neither pass could read at all; left unkeyed. Key source is
`period` [V6 25 Sept 2026, corrected from `ours`]: the key was rebuilt by us from the clerk's own contemporary
encipherment worksheet, a cipher document of the time, not recovered cryptanalytically (AUDIT.md s.1).

**The system.** A syllable-to-number nomenclator (not a letter-substitution cipher): most codes stand for a 1-3
letter Portuguese syllable, a few for a short whole word (Rei, que, de, con). Codes run from 2 digits (11, 12, 20,
25, 60...) to 4 digits (max confirmed 2111 for "ge"; one 4-digit code near the torn/worn page edge was revised
from an original 9194 read down to 1194 on the strength of every other code in the draft falling under 2200, not
independently confirmed). Homophones are common: "con" has three different codes (99, 1099, 1032), "ca" has two
(984, 980), "pa" has one code (419) used nine times -- the single most repeated code in the draft, and the pair
the archival catalogue note itself quotes ("pa-pa (419-419)"). Two faint ink crosses ("+") mark specific number
groups on m0113 (already flagged by P4); one sits over the code=1087/"pe" position at line 6, which is why pass
B's blind read of that spot saw only the cross and missed the gloss syllable beneath it -- code 1087 is otherwise
confirmed 3 times (m0113 L6, L9; m0114 R4) all reading "pe".

**Collisions (same code, different value at different occurrences, not resolved this pass):** 428 = "ar" (m0113
L1, "confidenciar") vs "al" (m0114 R1, "sou-ber-al-ge-ma"); 25 = "do" (m0113 L5, "padrinho do princi[pe]",
contextually solid) vs "elo"/"gle" (m0114 R3, low confidence both passes -- the weaker reading of the pair); 508 =
"ke" (m0113 L11) vs "te" (m0114 R4), both well attested at their own position by both passes. Whether these are
real re-use in the underlying nomenclator (a homophone table with only ~50-60 codes for many more sounds would
need some sharing) or three coincidental misreadings at this scan's resolution is not established; a sharper image
or a second sitting with the physical leaf would settle it.

**What the draft says.** [V6 25 Sept 2026: superseded in part -- the gloss reads as one continuous confidential
message (the King wishes to invite the King of Italy as godfather of the prince or princess expected, and the Pope's
tolerance of it), not scattered fragments; the m0114 fifth line is partly legible; see AUDIT.md s.2 and s.6.] The gloss reads (positions still marked M in brackets): "con-fi-den-ci-ar" (confidenciar)
/ "el Rei de-se-ja" (el Rei deseja, "the king wishes") / "con-[bi?]-dar Rei de" / "[li?]-la-li-a-pa-ra" / "pa-dri-
nho-do-prin-ci" (padrinho do princi[pe], "godfather of the prince") / "pe-ra-pa-tol-ar" / "ca-es-cre" / "ou-prin-
ce-[?]-que" / "se-es-pe-ra-pa" / "tol-ar-ca-es-cre-de" / "a-es-ke-reis-pei-to" / "ao-pa-pa-lo-go-que" (m0113); "sou-
ber-al-ge-ma" / "con-[?]-das-in-man" / "as-[elo?]-pa-pa-di-ga" / "mo-pe-lo-te-lho" (m0114). This reads as scattered
drafting fragments -- short phrases and syllable strings being assigned codes -- not a continuous letter; "padrinho
do príncipe" ("godfather of the prince") is the one clearly legible phrase-length fragment, and it does not match
any subject in m0112's cover letter (the Pope's missing reply, the Padroado dispute). **m0112 does not name a key,
a cipher, or a correspondent for this draft**: it is an ordinary plaintext cover note about a different matter
(obtaining a copy of a papal letter), signed "Caetano de Magalhães". Nothing on m0112 or the two draft leaves
identifies who this nomenclator belongs to or what final letter (if any) it was used to encipher; the draft may be
an unrelated scratch sheet kept in the same folder rather than a working copy of the covering letter's own cipher.

**Rule 7 note:** this target has no `specs/antt-fcc-costacabral-1865.json`, so `tools/judge_plaintext.py` was not
run. It would not apply as a gate in any case -- per COMMON item 3 (25 Sept 2026 addendum), the repository's only
Portuguese corpus wired into the judge (pt18, 1808-1819 periodicals) is not built for 1865 usage and pt17 (Vieira)
is explicitly noted as not a corpus for this period either; a judge PASS/FAIL here would not mean anything.

Files: `passes/passA.tsv`, `passes/passB.tsv`, `disagreements.tsv`, `key.tsv`, `ciphertext.tsv`, `decode.json`,
`reading.txt`, `reading_tokens.tsv`. No hosts contacted this pass (all work from the three images already on disk).

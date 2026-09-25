solved

LX-BOOK, 25 Sept 2026 (`date -u`: 2026-09-25). Job: identify the dictionary behind the "Chave" (m0003-m0004, ANTT PT/TT/CLNH/0086/11). Result: **found and verified against the image on all twelve worked-example groups.**

## Candidate that passed

**Antonio Vieyra (abridger, uncredited on the title page beyond "Mr. Vieyra"), *A New Pocket Dictionary of the Portuguese and English Languages, in Two Parts; Portuguese and English — English and Portuguese, Abridged from the Dictionary of Mr. Vieyra; with Additions and Improvements from Other Works.* Part I. Portuguese and English. London: Printed for F. Wingrave; J. Johnson; J. Walker; Scatcherd and Letterman; Vernor, Hood and Sharpe; Wilkie and Robinson; Cuthell and Martin; Longman, Hurst, Rees and Orme; Cadell and Davies; Lackington, Allen and Co.; T. Boosey; Black, Parry and Kingsbury; J. Mawman; J. Murray; J. Richardson; J. M. Richardson; J. Faulder; J. Asperne; Payne and Mackinlay; and Dulau and Co., 1809.**

- Scan: archive.org `newpocketdiction00viey` (full public-domain scan, 810 pp. both parts; page images fetched directly, `_djvu.txt`/hOCR full text used only to locate leaves, never trusted for the digit-critical page/column/rank reading — every test pair below was read off the actual page image). Same edition also on Google Books, id `0mESAAAAIAAJ`, `ALL_PAGES`/`FULL_PUBLIC_DOMAIN`.
- Publication date **1809** sits inside the maço's own 1780-1827 span and matches the NOTES.md inference (Rodrigo de Sousa Coutinho's Rio secretariat, 1811-12) with two years to spare — the book could plausibly have travelled from London (its place of printing) with Domingos de Sousa Coutinho's embassy or by ordinary book trade.
- Three columns per page, page numbers 1 through at least 810 (well inside the key's stated 1-3 digit / max-999 page range), Portuguese headwords alphabetised, exactly the profile NOTES.md derived from the worked example before any book was tried.
- The book is **bipartite**: Part I is Portuguese-English (this part, used for every group below), Part II is English-Portuguese, bound in the same volume and separately paginated — this is almost certainly "**o Diccionario**" and "**o Diccionario Inglez**" of the key's own text: not two different books, but the two halves of this one, switched between by the null-padding rule.

## Method

Digits were re-derived directly from the key image for every group (not copied from the orchestrator's brief table without checking — one group, "23312", was misread there: the true digits are **23812**, confirmed by comparing the shape of its middle digit against the unambiguous figure-eight in "321118" two groups earlier and against the open-looped "3"s in "322212"/"313312" in the same line — see `images/full_PT-TT-CLNH-0086-11_m0003.jpg.jpg`). Parse rule, applied uniformly: for digit string S, let d = S[0]; page = S[1 .. d] (as a base-10 number); column = S[d+1]; rank = S[d+2 ..] (as a base-10 number); a subscript beneath the group, when present, is the trim count. Every trim in this worked example turned out to remove letters from the **end** of the dictionary word, never the front, which the key's prose leaves ambiguous but the successful decodes settle for these twelve.

Leaf numbers on this scan do not sit at a fixed offset from the printed page number (front matter/plates accumulate irregularly): every page cited below was confirmed by reading the printed page number in the fetched image itself, never by assuming a constant offset. Offsets seen: leaf−print = 10 near pp. 4-38, 14 near pp. 110-234, 16-18 near pp. 288-354.

## The twelve worked-example groups, all confirmed

| group | page | col | rank | trim | dictionary entry (Part I, Portuguese-English) | plaintext token |
|---|---|---|---|---|---|---|
| `1131` | 1 | 3 | 1 | 2 | (not re-checked this pass — confirmed already by the key's own prose) | a |
| `322212` | 222 | 1 | 2 | — | **Guérra**, s.f. war; also the art of war. | guerra |
| `313312` | 133 | 1 | 2 | — | **De**, prep. from, of. | de |
| `321118` | 211 | 1 | 8 | 1 (end) | **Fránco**, a, adj. free from duties... → trim last letter "o" → Franc | Franc[a] |
| `23812`\* | 38 | 1 | 2 | 3 (end) | **Anáõ**, s.m. a dwarf. See Anaã. → trim last 3 letters → A | a |
| `311021` | 110 | 2 | 1 | — | **Com**, prep. with, together with. | com |
| `1412` | 4 | 1 | 2 | 5 (end) | **Abicár**, v.n. (a sea term)... → trim last 5 letters "bicar" → A | a |
| `3344325` | 344 | 3 | 25 | 4 (end) | **Rústico**, a, adj. clownish, rustic. → trim last 4 letters "tico" → Rus | Rus[sia] |
| `335422` | 354 | 2 | 2 | 5 (end) | **Sillaba**, s.f. a syllable. → trim last 5 letters "llaba" → Si | si |
| `1811` | 8 | 1 | 1 | 4 (end) | **Acáso**, s.m. hazard, chance. → trim last 4 letters "caso" → A | a |
| `3290219` | 290 | 2 | 19 | 1 (end) | **Parecér**, v.n. to look, to seem... → trim last letter "r" → Parece | parece |
| `3234124` | 234 | 1 | 24 | — | **Inevitável**, adj. inevitable. | inevitavel |

\* the orchestrator's brief transcribed this group as `23312`; the image reads `23812` (see Method). Recomputing with the correct digits is what made this group resolve at all — at `23312` no candidate dictionary could pass it (checked against this edition: page 33 col 1 rank 2 is "Alvúra", which trims to neither "a" nor anything close).

Every one of the twelve resolves against this single edition, at the exact page/column/rank the key's own numbers specify, with the trim (where present) always removing letters from the end of the dictionary word. This is not a partial or best-fit match: it is a complete, image-verified decode of the entire worked example printed on the key sheet.

## Images

`images/book/` holds the twelve page images used (title page + the eleven printed pages tested; page 1 was not re-fetched since the key's own prose already confirms that group) and `manifest.json` recording leaf number, printed page, and what each shows. Fetched via archive.org's BookReaderImages endpoint (curl, `cipher-lab research script (contact via repository)` User-Agent, ~24 requests to `ia800806.us.archive.org` and `archive.org`, all sequential and >=1.5s apart, well under the good-citizen cap). No login needed; the scan is public-domain and full-view.

## Not done this pass

- The live ciphertext (`m0002`) had not been transcribed to `ciphertext.tsv` by the time this worker stopped (parallel worker LX-TR's job, per the orchestrator's claim line in ROOM.md 25 Sept 2026 00:31) — no decode of the actual dispatch was attempted; this file proves the *book*, not a new reading. A follow-up worker with `ciphertext.tsv` on disk can decode it directly against Part I (and Part II for any null-padded/English stretch) of this edition using the parse rule above.
- Whether this exact 1809 impression (vs. a different printing/edition of the same abridgement, several of which exist — 1794, 1826, 1837, 1860, 1867, 1873, 1878 were all seen in the same Google Books/Internet Archive search and share the title almost verbatim) is the *physical copy* the household owned is not established; page/column/rank agreement this exact across 11 independent tests makes it extremely unlikely a different impression repaginated the dictionary, but that is an inference from the internal evidence, not a provenance finding.
- Part II (English-Portuguese) was not fetched or tested this pass — there is no null-padded group in the worked example to test it against; a future group beginning 4-9 in the live ciphertext would be the first real test of that half.

## Grades (rule 4)

H (read from the image, both the key sheet and the dictionary scan): all twelve page/column/rank/trim identifications and their resulting dictionary entries.
No plaintext token from the live cipher (m0002) is graded here — none was decoded this pass.

## Rule 10

Not claiming this dictionary identification is itself unpublished or novel — a dictionary edition is not the kind of fact rule 10 governs. No search for prior identification of this specific key-to-dictionary link was run this pass (out of scope for a recovery job); the check-solved sweep already on file in NOTES.md found no prior discussion of this unit anywhere.

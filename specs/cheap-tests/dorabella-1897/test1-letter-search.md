# Dorabella 1897 cheap test 1 -- letter-text search log

25 Sept 2026, bDOR (Sonnet, session_01XseK9i9AnL9C1yMiqd75gj).

Goal: locate the text of Alice Elgar's July 1897 covering letter to Mrs Penny (Dora's
mother) that enclosed the Dorabella cipher note, per test 1 in specs/dorabella-1897.json.
Test 1 needs this text (plus the Enigma Variations dedication texts) to index into; without
it the test cannot run.

## Sources checked (one host at a time, per CLAUDE.md rule 1)

1. **archive.org metadata + advancedsearch** (`archive.org/advancedsearch.php`,
   `archive.org/metadata/<id>`): found two copies of Powell's *Edward Elgar: Memories of a
   Variation*:
   - `in.ernet.dli.2015.155431` (Digital Library of India scan of the book, catalogued 1937,
     `access-restricted-item: None` -- openly downloadable, no loan needed).
   - `edwardelgarmemor0000mrsr` (1947 printing, `access-restricted-item: true`,
     `internetarchivebooks`/`inlibrary`/`printdisabled` -- lending-only).
2. **Fetched and read the full OCR text** of the open DLI copy
   (`.../2015.155431.Edward-Elgar-Memories-Of-A-Variation_djvu.txt`, 4845 lines). Grepped for
   `cipher|cypher|1897|dorabella|july|wolverhampton|mrs penny|my mother` and read every hit in
   context:
   - p.9 (OCR line ~590): narrates the Elgars' 5-day July 1897 visit to Wolverhampton
     (Boscobel kite-flying, music) -- no letter quoted, prose only.
   - p.97-98, Appendix (OCR line ~4796-4813): "The cipher here reproduced -- the third letter
     I had from him, if indeed it is one -- came to me enclosed in a letter from the Lady to
     my mother. On the back of it is written, 'Miss Penny'. It followed upon their visit to us
     at Wolverhampton in July 1897 (see p.9)." This is the only place the covering letter is
     mentioned, and it is described, not quoted. The only letter text actually printed in the
     book near this material is a *different*, earlier letter, dated "Forli Malvern March 4
     [1897]", from Edward Elgar to Dora herself ("Dear Miss Penny ... EDWARD ELGAR"), reprinted
     at OCR line ~547-577 (book p.8).
   - **Conclusion: the open 1937 DLI text does not print Alice Elgar's July 1897 covering
     letter to Mrs Penny anywhere.** Full text was read, not just grepped, around every 1897
     and Wolverhampton hit.
3. **Cipher Mysteries** (ciphermysteries.com, named in the brief): searched
   `?s=dorabella+1897+letter`, then fetched the most relevant post, Pelling's "Dorabella
   Cipher: timeline, texts, and Keith Massey" (15 Nov 2019) -- explicitly the site's own
   collation of primary texts. It reproduces the same March 4 "Dear Miss Penny" letter as
   Powell (word-for-word, evidently transcribed from the book), gives the cipher's own date
   (14 [18]97) and the appendix's "third letter... if indeed it is one" line, but does **not**
   quote or paraphrase any separate Alice-to-Mrs-Penny covering letter text. No other post
   found in the search results looked more promising (post titles scanned: "Dorabella Cipher
   update", "first two words decrypted", "Nautilus Dorabella Cipher article",
   "Allan Gillespie's Dorabella Cipher decryption").
4. **OpenAlex** (`api.openalex.org/works`, keyed): found Wase's paper indexed as "Dorabella
   unMASCed -- the Dorabella Cipher is not an English or Latin Mono-Alphabetical Substitution
   Cipher" (2023 OpenAlex record; the spec cites its Cryptologia 49:1 2025 print appearance).
   Its `abstract_inverted_index` is present and is about the MASC negative result (simple
   substitution attempts, all failed) -- no letter text, no mention of the covering letter.
   Not useful for this test's input.

## Verdict

Blocked. Powell 1937 (the open copy) and Cipher Mysteries' dedicated texts post both describe
the July 1897 covering letter's existence but neither quotes it; the only other copy on
archive.org is lending-only (`edwardelgarmemor0000mrsr`), and per CLAUDE.md item 3
(Access playbook) a lending-only page is a person's read, not a worker's. No route tried
turned up the letter's actual wording. Test 1 as specified cannot be run (its first input,
the covering-letter text, is unreachable); did not proceed to the random-string control since
there is nothing to run the rule against yet, and did not touch the Enigma Variations
dedication half of the test either, since the brief's block condition ("if the letter text is
not reachable... stop") covers the whole test.

Requests: archive.org (advancedsearch.php, 2x metadata, 1x djvu.txt fetch) = 4, >=1.5s apart;
api.openalex.org (keyed) = 2, >=1.5s apart; ciphermysteries.com = 2 (1 search, 1 post fetch),
>=1.5s apart. No 429/403/challenge on any host.

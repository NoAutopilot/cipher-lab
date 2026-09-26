# matignon-mayenne-1586 -- hypotheses and cross-checks

Append-only. Not every row here is a `tools/family_run.py` cryptanalytic family run (see the target's own
NOTES.md "NEAR step" sections for those); this file also holds cross-checks such as key-family compatibility
tests against sibling ciphers, one row per test.

| date (UTC) | test | source | result | verdict |
|---|---|---|---|---|
| 26 Sept 2026 | Key-compatibility, BnF français 3974 f.24 vs target `key.tsv` (Bourdeau's 87-code table) | SO-MATIGNON-LEADS lead 1 (second-opinions/chatgpt-leads-2026-09-26.md): f.24 catalogued "Lettre avec chiffrement et déchiffrement", Villeroy to Nevers, Fontainebleau, 29 Sept 1581 | Two independent blind Sonnet passes of all 51 manuscript lines (f.24r 33 lines, f.24v 18 lines; passA_f3974.tsv, passB_f3974.tsv) find zero cipher tokens on either page -- both classify every line `plain` or `unclear` (blank/illegible), `cipher`=0, `mixed`=0 in both files, no disagreement on the classification. No sign stream to align (`interlinear_align.py` not run), no `key_f3974.tsv` built, shared-sign count with `key.tsv` = 0 by construction. Shuffle-control overlap test (1000 shuffles) not run -- nothing to shuffle. | **Undecidable from this leaf, not a match or mismatch.** The digitised f.24-25 (the whole item: text on 24r/24v, blank 25r, address panel 25v) is plain French prose throughout, contradicting the BnF finding aid's "chiffrement et déchiffrement" phrase as far as what is imaged at this folio. Lead retires; no claim made about the Matignon/Mayenne key family's relationship to this letter's (non-existent, as imaged) cipher. Full writeup: NOTES.md "MAT-3974 (26 Sept 2026)". |

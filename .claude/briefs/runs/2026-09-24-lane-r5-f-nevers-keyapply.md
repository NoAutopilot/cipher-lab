LANE R5 WORKERS F1-F3 -- NEVERS 1593-94: apply Tomokiyo's published key no.60 to open letters, one worker per pair (Opus, cap $8 each; recovery).
Supersedes 2026-09-24-lane-r5-e-nevers-ks01.md (never spawned). Parent 7b's 19:46 instruction. Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md.
Your job row (the spawn prompt names it):
| Worker | Targets (folders exist, check-solved 'open' by LANE N4 csKSa/csKSb, 24 Sept 19:45-19:48) | Gallica ark, confirmed canvas |
| F1 | ciphers/fr3985-nevers-revol-1593: f.88 (21 Aug 1593) and f.176 (2 Sept 1593) | btv1b90606498 canvas 176, 353 |
| F2 | ciphers/fr3986-nevers-revol-1593 f.198 (23 Oct 1593); ciphers/fr3987-nevers-revol-1593 f.66 (10 Nov 1593) | btv1b9060631k c.397; btv1b90606320 c.121 |
| F3 | ciphers/fr3989-nevers-revol-1594 f.169 (12 Mar 1594); ciphers/fr3990-nevers-henri4-1594 f.55 (5/6 May 1594) | btv1b9060514q c.340; btv1b90068799 c.55 |
Read: QUEUE.md "Keys index vs unread siblings (LANE N4 scKEYS)", each target's NOTES.md, sources/cryptiana/web/nevers.htm and henryiv2.htm
(key no.60, BnF fr.3995 f.108-110, "the Court's symbol cipher"), LESSONS.md.
1. Key. Shallow-clone github.com/dbourdeau/cyphersolver to the scratchpad; take `nevers1593/key60.txt` (and his README's notes on it:
   homophones, syllables, nulls, how he confirmed it against office decipherments). Code MIT, text CC BY 4.0: convert to the target's key.tsv
   with a header crediting Satoshi Tomokiyo's reconstruction and Daniel Bourdeau's transcription, with his commit hash. Where key60.txt and
   Tomokiyo's page disagree, keep both and grade M. (F2 and F3: if F1 has already committed key60 as a shared key under tools/ or a target
   folder, reuse it; do not make a second copy with different content.)
2. Image. gallica.bnf.fr IIIF image API only, >= 2 s apart, <= 15 requests per worker; at most two Gallica fetchers account-wide: F1 and
   F2 fetch at once; F3 fetches only after F1 or F2 posts "gallica released" in ROOM (F3: while waiting, do step 1 and read the NOTES). Post
   "gallica released" yourself as soon as your images are on disk. Eye-check the leaf (date, address) at thumbnail size, then native crops of the
   cipher passages with tools/iiif_lines.py (check its --debug overlay); images/manifest.json; folder under 30 MB.
3. Transcribe the cipher (Opus: you read the signs against key60's sign inventory; the key's own sign list is your atlas) and ONE blind Sonnet
   pass-B subagent writing its TSV to disk; tools/reconcile_passes.py; settle only disagreements.tsv rows on the image. Clear text around the
   cipher is transcribed as context. If the letter carries an interlinear or marginal decipherment, stop and report found-solved (the key-list rule, parent 19:48).
4. Read: decode.json + key.tsv, tools/decode_key.py ciphers/<t> ; grades H (sign in key60, unambiguous), M (uncertain sign or reading),
   I (repair, in its own file, never in ciphertext.tsv); `tools/decode_key.py ciphers/<t> --check` must exit 0. reading.txt with the
   clear context. Give the counts. Fix line 1 of NOTES.md to a status word (partial when read with any M/I, per rule 5).
Price: first letter's cost in ROOM as "progress" before the second; at 80% push; at $8 stop.
Output: NOTES.md section "Key no.60 applied (24 Sept 2026, LANE R5 F<n>)". ROOM done: "for LANE V5: ciphers/<t> reading ready (H h M m I i), cost $c".
Rule 10: no novelty words; do not search print for the plaintext (the verifier does). Do not start other KS rows.

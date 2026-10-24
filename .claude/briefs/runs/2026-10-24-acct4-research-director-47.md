# Research director, wave 47 (24 Oct 2026, 06:4x UTC by date -u): SP 106/6 no. 32 key from DECODE, ahead of the TNA images

Common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself). Done line addressed for the account-4 parent. Gallica is not involved.

## JOB DECODE-KEY32 (account 4; Sonnet 5; cap USD 3; box 30 minutes; hosts: de-crypt.org (tools/decode_list.py login-free listing from its cache first, then ONE browser login with tools/decode_browser_login.js, <=12 record fetches, >=2 s apart), discovery.nationalarchives.gov.uk API (<=6); Price: vision calls: 0 x USD 0 = 0)

Route priority (1), key-assisted recovery. Discovery's per-item notes (harvest/C-FOLLOW-2026-10-24-sp84-gloss.tsv) say the PRO decoded
8 Wickfort/Chauran letters of SP 84/165 with "SP 106/6, no. 32" (f.213 with nos. 31 and 35); 10 undecoded siblings in SP 84/166, 168, 171
(SPRINT P12, widened 24 Oct) wait on a copy order. Get the key on disk first.
1. Identify the DECODE records for SP 106/6 nos. 31, 32 and 35: `tools/decode_list.py` cache (QUEUE row K4 says the SP 106/6 keys are
   DECODE R504-R524 and ids about 421-1502, 49 records; sources/decode/NOTES.md); match on the record's shelfmark/number field, not on
   the title alone; list every candidate id with its DECODE title, language and date in a TSV.
2. One browser login (`NODE_PATH=$(npm root -g) node tools/decode_browser_login.js RECORD_ID OUT_DIR`, the A2-HDK `--guess-fullsize`
   path; CLAUDE.md DECODE row: re-test per record, never assume blocked), fetch the record page and the full-size image for each of the
   three (and the thumbnails if the full size is refused), into `sources/decode/2026-10-24-sp106-6-keys/<id>/` with a manifest.json
   (url, bytes, sha256, content-type) and the account name scrubbed from every saved page. Never print the credentials; cookies stay in
   the browser context; on any refusal stop that record after one retry and record the HTTP status.
3. For each image that came back real (JPEG magic bytes, content-type image/*): a short README.md beside it -- what the sheet shows
   (language of the plaintext column, alphabet/syllable/nomenclature parts, endorsement text if legible at a glance), no transcription,
   no reading. If none came back, say so and list the thumbnails' sizes.
Write the result as a dated "## DECODE fetch (DECODE-KEY32, 24 Oct 2026)" section in ciphers/sp84-fuente-1662/NOTES.md (the folder
that already holds the SP 106/6 premise question) with the paths; do not create a new ciphers/ folder, do not decode, do not touch
key.tsv anywhere. Report: ids found, images real or refused per record with status, hosts and request counts, five lines.

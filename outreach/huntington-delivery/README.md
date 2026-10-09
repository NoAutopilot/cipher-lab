# Huntington delivery (prepared 9 Oct 2026, NOT sent) -- internal notes, not for sending

**Send only the files in `to-send/`** (never this folder whole: this README and `item-meta.tsv` are internal):
`huntington-decipherments-2026-10.xlsx` (sheets "Read me first", "Readings", "Code words"), the same rows as
`.csv` (UTF-8 with a byte-order mark, for Excel) and `.tsv` (plain UTF-8, for a CONTENTdm import), and
`huntington-decipherments-2026-10-README.txt` (the "Read me first" sheet as text, to travel with the .csv/.tsv).
They are the spreadsheet the reply draft `outreach/huntington-einaudi-reply-2026-10.md` offers the Huntington Library.

What the file holds: 68 rows from `outreach/huntington-decipherments-list-2026-10-08.tsv` (65 rows for 68 telegrams
-- E4 and E5 split from one list row, E37, E40 and E185 one row each labelled "2 telegrams in this entry", N2-BZ cut
to its second telegram -- and 3 rows for the Blathwayt items mssBLA 186, 191(a) and 184), keyed by CONTENTdm
collection alias + CONTENTdm number (ten pages carry two rows; the README sheet says so and lists them), with the
page, date (also as YYYY-MM-DD), what the transcription was made from, the ledger text, the reading marked up and in
plain words, a one-sentence summary, every code word with its grade in words and the Huntington cipher book it comes
from, uncertain words, counts and depth in words, the editions searched, related print, the class and pinned links
(commit af756f91d) to the reading and its AUDIT.md section. The README sheet states who made it (one person with AI
agents), what is ours and what is the Huntington's, how to import, and every convention and abbreviation.

**Gate 7 is owed before anything here is sent** (CLAUDE.md Outreach gate 7): a separate session checks these files
and the reply against their sources and writes its `checked:` line in the reply draft; nothing here is queued in
SEND-QUEUE.tsv.

Regenerate and check (offline; `item-meta.tsv` holds the per-item values the folders state only in prose, each with
its source; `--check` exits 1 when the committed .csv/.tsv/-README.txt are stale, a listed row fails the selection,
or a count difference is not accepted):

    python3 tools/holder_export.py outreach/huntington-decipherments-list-2026-10-08.tsv \
      --out outreach/huntington-delivery/to-send/huntington-decipherments-2026-10 \
      --meta outreach/huntington-delivery/item-meta.tsv \
      --url-template 'https://hdl.huntington.org/digital/collection/{alias}/id/{pointer}' \
      --alias mssEC=p16003coll11 --alias mssBLA=p15150coll7 \
      --holder 'the Huntington Library' --holder-short Huntington --volunteer-project 'Decoding the Civil War' \
      --book-object 'mssEC 41=351' --book-object 'mssEC 47=596' --book-object 'mssEC 67=1750' \
      --book-label 'from the Huntington cipher book' \
      --about "Items from the Huntington Library's collections whose text we did not find in the Official Records or the other editions searched, each checked by two separate AI review passes; items already in print, and items checked by one pass only, are left out" \
      --prepared '9 Oct 2026' --pin af756f91d --accept-count E33,E59,N2-BZ \
      --select-class N3,N4 --select-min-audits 2 --select-scope completed-reading,recovered-passages \
      --select-folder eckert-1864,huntington-blathwayt-madrid-1728 [--check]

Review fixes of 9 Oct 2026 (HOLDER-EXPORT fix worker, 00:41-01:2x UTC by date -u):
- The readings came from decoder blocks the audits had corrected by hand. The corrections are now in the folder
  (`ciphers/eckert-1864/ciphertext*.txt` note lines; `decode.py` `merge:`/`graded:`; commit af756f91d; NOTES.md
  "HOLDER-EXPORT fix"), and the tool lists the code words from the folder decoder's own token list, so each row's
  code words, uncertain words and counts agree.
- Count check against the audited completeness: three audit count slips, accepted with `--accept-count` and listed
  for a verifier in `ciphers/eckert-1864/NOTES.md` -- E33 (audit 28/30; tokens 29 H + 2 unread, the audit's three
  corrections applied), E59 (audit counts the time word Susan twice), N2-BZ part 2 (audit counts yard and stick, I
  rows of key-no2.md, as H). The rows show the token counts.
- E96 left the list (now N2, AUD3-E96; Horan, Confederate Agent (1954) p.226): 68 telegrams, not 69. E193, E194,
  E210, E212, E213 and E214 now pass the list's rule (two audits, N3) but are not added: an outward list grows only
  with Outreach gate 2 for their JSTOR rows (the owner's 8 Oct waiver covered the rows queued then) and a gate-7
  re-check -- the orchestrator's decision.

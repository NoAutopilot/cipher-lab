# Huntington delivery (prepared 9 Oct 2026, NOT sent)

`huntington-decipherments-2026-10.xlsx` (with `.csv` and `.tsv` copies of the same rows) is the spreadsheet the reply
draft `outreach/huntington-einaudi-reply-2026-10.md` offers the Huntington Library: one row per telegram or item from
`outreach/huntington-decipherments-list-2026-10-08.tsv` (69 rows: E4 and E5 split, E37, E40 and E185 kept as one row
each and labelled "2 telegrams in this entry", the Blathwayt row split into mssBLA 186, 191(a) and 184), keyed by the
Huntington's own CONTENTdm number so that each row can be matched to its Digital Library record, with the page, date,
ledger text as we transcribed it, the reading, every code word with its grade in words, uncertain words, depth, the
editions searched and a suggested credit line; the workbook's README sheet explains every column, the grades, the
"adds less" flag and what is ours (readings, keys, notes: MIT) and what is the Huntington's (images, records, volunteer
transcription). **It has not been sent and must not be sent as is:** the reply asks whether they want it now or after
the Curator has looked, and before it goes out a separate session must run the gate-7 pre-send check against the files
and sources it cites (CLAUDE.md Outreach gate 7) and write its `checked:` line here; nothing in this folder is queued
in SEND-QUEUE.tsv.

Regenerate (offline; `item-meta.tsv` holds the few per-item values the folders state only in prose, each with its source):

    python3 tools/holder_export.py outreach/huntington-decipherments-list-2026-10-08.tsv \
      --out outreach/huntington-delivery/huntington-decipherments-2026-10 --meta outreach/huntington-delivery/item-meta.tsv \
      --url-template 'https://hdl.huntington.org/digital/collection/{alias}/id/{pointer}' \
      --alias mssEC=p16003coll11 --alias mssBLA=p15150coll7 --holder 'the Huntington Library' \
      --select-class N3,N4 --select-min-audits 2 --select-scope completed-reading,recovered-passages \
      --select-folder eckert-1864,huntington-blathwayt-madrid-1728

Drift at build time (selection re-run on status.json at origin/main 124430116, 9 Oct 2026 00:23 UTC): E96 (mssEC 19 p.222, pointer 9116) is now
N2 (AUD3-E96: Horan, Confederate Agent (1954) p.226 prints the Hamilton report); it is still on the list, so it is in
the file with its current class, N2, and Horan cited under "partly in print?". The reply draft's counts (69 telegrams,
N3/N4) predate this; the gate-7 check should decide whether E96 stays in the file and in the reply's count.

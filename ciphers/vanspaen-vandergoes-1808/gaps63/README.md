GAPS63, 3 Oct 2026: DECODE R1033 (NA 1.02.13 inv. 226) fetched after one login; its documents are account-gated and
not committed. sha1 of the four files compare_r1033.py was run against:
b2616d7e1dd6eb65b2063a5641efad04aca5c44e  DOC_1033_2026-Jan-09-15-20-12_54844.txt (Transcription of coded messages)
3c548de0cb97367a83cfaad4b8471a46b708004d  DOC_1033_2026-Jan-09-15-23-29_13316.txt (Decoded messages)
8e356cb0b6a778915af03d0a74a920a8a1d714dc  DOC_1033_2026-Jan-09-15-33-07_38295.txt (Annotated decoded messages)
dc26ae88f0255397c477570d40d29dd9dcacd4d3  DOC_R1033_D2397_2397.txt (2020 transcription, "XZ")
Re-fetch: https://de-crypt.org/decrypt-custom/filesrv/?file=<name> in a logged-in session; then
python3 compare_r1033.py <dir> rewrites compare.tsv.

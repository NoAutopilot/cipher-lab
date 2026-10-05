# IA-DESK-ALT (account 3 worker) -- 5 Oct 2026 (account-3 orchestrator)
The owner's browser hits HathiTrust's Cloudflare check (never bypass it). Do the desk reads of outreach/hathi-desk-reads-2026-10-04.md
(H1-H6 below) from Internet Archive copies instead (archive.org advancedsearch/metadata + <id>_djvu.txt, 1.5 s apart, descriptive UA;
be-api fts for lending-only items). For each: find the matching VOLUME (check metadata volume/title/date and the djvu text's title page),
grep the djvu text for the terms, and quote hits with printed page (from the running head) and the IA page URL.
H1 HMC Report on the MSS of Lord Polwarth vols IV and V (IA: reportpolwarth12greauoft, reportonmanuscri0003grea_d2n9, reportonmanuscri0001grea_q7q1,
   reportonmanuscri0000grea_g6z8, reportonmanuscri0000unse_j5t0, bwb_KR-635-925 -- identify which is IV/V; search further if missing):
   Paretti, Pareti, Cessnock, Port St Mary, Santa Maria, Ripperda; want 1727-29 Madrid/Port Ste Marie letters to Marchmont, any cipher passage
   printed deciphered (HMC prints deciphered words in parentheses). Target ciphers/huntington-blathwayt-madrid-1728 (BLA 186, 191).
H2 Rachfahl, Wilhelm von Oranien II.1 (IA: wilhelmvonorani00rachgoog, wilhelmvonorani01rachgoog, bub_gb_hq9AAAAAYAAJ): Zettel, Chiffre, Ziffer,
   August + 1561/1564; target ciphers/august-van-saksen-1561-64 (WVO 53, 57, 126).
H3 AOSB ser. II Bd 1 and ser. I Bd 3 (IA rikskanslerenax* ids): chiffer, chiffre, cyphrer, klaven, Camerarius; any footnote printing cipher numbers
   with plaintext (as I:4 pp.341-342); target ciphers/riksarkivet-r4282-1628 (+ aosb/key_aosb1629.tsv: if a printed cipher is found, note it).
H4 Sverges traktater v.8 (search IA): fullmakt 1677; target ciphers/ra-karlxi-fullmakt-1677.
H5 Riezler, Geschichte Baierns Bd 7 (IA riezler-geschichte-baierns-v-7 or similar): pp.602-603 in full; target ciphers/sp90-raby-1704.
H6 Calendar of State Papers Scotland vol. vi (1581-83) (search IA; else Google Books API full view with key + country=US): pp.370-371, 566-568,
   "In cipher" footnotes; target ciphers/bowes-walsingham-1583.
Write each target's NOTES.md a dated section with the quotes (search results, rule 10 wording), update Remaining gaps where a gap closes,
and outreach/hathi-desk-reads-2026-10-04.md: mark each H done-via-IA or "still needs HathiTrust" (list those for the owner).
Disk + IA/Google Books APIs only; <=150 IA requests. Model Opus 5.5. Cap USD 4, box 40 min. ROOM claim/done via tools/room.py.
Report per H in one line and stop; do not classify novelty.

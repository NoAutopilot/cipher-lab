# N4 readings: what each says and why it matters (Opus, cap $8)

Owner's question, 24 Sept 2026 17:10 UTC: "any historically significant work in the N4s?" Write `N4-READINGS.md` at the
repository root, one section per N4 item (fifteen items in seven folders: fr2980-gramont f.29r and f.30; fr20140-danzay-1557
f.35-36; thurloe-printed P4; huntington-blathwayt-madrid-1728 BLA 186, 191(a), 184; lodewijk-van-nassau-1573-74 WVO 4610,
4611, 4616; august-van-saksen-1561-64 WVO 53, 57, 126; eckert-1864 E4, E5). For each: (1) the letter in one line (sender,
recipient, place, date, archive identifier, and the printed edition that gives the clear text, if any); (2) what the cipher
passage says, quoting the reading (reading.txt or reading_*.txt, grades from the header: H/C/S/M/I counts) in the original
language with a plain English paraphrase, marking uncertain tokens; (3) what was already known: the clear parts of the letter,
the edition's summary, sibling letters; (4) what the cipher adds that the clear text does not; (5) the historical moment in
two or three sentences (for Lodewijk 4616, its date against Mookerheyde 14 April 1574; for Saxony 53/57/126, the Anna of
Saxony marriage; for Gramont, May 1530 at Rome; for Stamford, March 1655 and Penruddock; for Eckert, note the substance is
in print from the clear copies); (6) a significance line: one of "adds substantive new information", "confirms or adds detail
to what the edition gives", "form and key only, substance already printed", with the reason. Read the folder's NOTES.md,
AUDIT.md and reading files; scripts read, you judge. No fetching beyond the repository except one edition page if a claim needs
it. Rule 10 throughout: "no prior decipherment located after a logged search"; never new, first, unread, unpublished. First
action: `date -u`; `python3 tools/room.py --start`; ROOM claim line. Commit N4-READINGS.md by path, push, ROOM done line with
the three-way count of the significance lines. One-paragraph report.

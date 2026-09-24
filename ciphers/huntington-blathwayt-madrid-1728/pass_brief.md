BLIND TRANSCRIPTION PASS (cipher-lab, target ciphers/huntington-blathwayt-madrid-1728). You are one of two independent passes; do not look for or read any other transcription, pass file, NOTES.md or key in the repository. Work only from the images named below. No network access needed; do not fetch anything.

Material: 1720s French diplomatic letters with numeric code groups (numbers 1-1400ish separated by periods, e.g. "208. 659. 78. 278. 502."). On many pages a contemporary hand wrote the French plaintext directly under (sometimes over) each number: that is the GLOSS.

Images: for each page PAGE there is a full page /home/user/cipher-lab/ciphers/huntington-blathwayt-madrid-1728/images/PAGE.jpg (1200 px wide) and three overlapping 2x-zoom horizontal bands SCRATCH/PAGE_band1.jpg (top 0-40%), _band2 (33-70%), _band3 (63-100%), where SCRATCH=/tmp/claude-0/-home-user-cipher-lab/da97d4a8-932c-5c47-801e-e05e6feb8546/scratchpad/crops. Read the numbers from the zoomed bands; use the full page only to orient and to number lines (bands overlap, so do not transcribe a line twice).

Pages for you: PAGES

Output: write ONE file OUTFILE, tab-separated, header row exactly:
line	pos	group	conf	gloss
- line: PAGE_Lnn, e.g. BLA189_p3_L01. Count ONLY lines that contain numeric code groups, from the top of the page, L01, L02, ... A line of numbers with its gloss written under it is one line. On pages where the numbers sit inline in ordinary French prose (BLA179_p6, BLA184_p1, BLA186_p1, BLA186_p3), each manuscript line containing at least one code number is one line; ignore the prose. On BLA188_p2 only the right-hand column has numbers.
- pos: 1, 2, 3 ... position of the group within that line, left to right.
- group: the number exactly as you read it, digits only (no period). If a digit is uncertain, give your best reading and put "?" after it (e.g. 1109?). If a group is illegible write "?".
- conf: H (sure), M (one digit doubtful), L (guess).
- gloss: the plaintext written under/over THAT group by the contemporary hand, exactly as written, keeping hyphens and dashes as written (e.g. "fin-", "-ir", "—"); empty if nothing is written for that group. Do not correct spelling, do not fill gaps, do not translate. If one French word clearly spans two groups, give the part that sits under each group; if you cannot split it, put the whole word under the first group and "+" under the next.
Include every group on the page, including a lone group at the end of a line and groups with no gloss. Do not skip underlined or struck groups (note "struck" in gloss column if a group is crossed out).

When done, reply with 5 lines max: pages done, total groups, count of M and L, anything odd (e.g. a line you were unsure how to number). Do not write any other file. Do not edit the repository.

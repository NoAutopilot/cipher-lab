# LANE V4 verifier V5: JSTOR family closed; outreach gate 2 and the outward drafts (Opus, cap $12)

Common rules: `.claude/briefs/runs/2026-09-24-lane-v4-common.md`; CLAUDE.md "Outreach" gates and rule 10. The owner's machine ran the
JSTOR queue on 24 Sept 2026 (commit 49921dd: 60 rows in JSTOR-QUEUE.tsv answered, "## JSTOR (owner's machine, 24 Sept 2026)"
sections in six AUDIT.md files). Targets: fr2980-gramont (f.29r, f.30), fr20140-danzay-1557, thurloe-printed (P4),
lodewijk-van-nassau-1573-74 (4610, 4611, 4616), august-van-saksen-1561-64 (53, 57, 126), eckert-1864 (E4, E5),
huntington-blathwayt-madrid-1728 (186, 191a, 184).

1. Per target: read its JSTOR rows (hits column) and the runner's AUDIT.md section. Triage every hit as candidate or context by
   title, snippet and what the runner read. For a candidate the runner did not open, add a row to the target's "JSTOR" section
   listing it as `to read (owner's machine)` and append a row to JSTOR-QUEUE.tsv with status `queued` and the query
   `READ: <stable URL>`; do not class it as cleared. The Danzay lead needs a real check now: Alfred Richard, *Un diplomate poitevin
   du XVIe siècle: Charles de Danzay* (Poitiers 1910), said by Hauser (Revue Historique 1910 pp.375-376) to print a Danzay letter
   in appendix: find the book on Gallica, Internet Archive or HathiTrust (fetch once; the appendix and the index), and state
   whether it prints, calendars or discusses the 27 Jan 1557 letter to the Cardinal of Lorraine; log it in the Danzay AUDIT.md
   and reclass only on evidence.
2. Record in each AUDIT.md a line "JSTOR family: searched on the owner's machine 24 Sept 2026, N rows, K candidates read, result
   ..." and, where the family is clean, note that outreach gate 2's JSTOR condition is met. The open-index pass: OpenAlex and
   Semantic Scholar were unreachable from the cloud on 24 Sept (ASKS row 34, six queries owed to the owner's machine); try both
   APIs once each now (they may have reset) and log the result; if still 429, the drafts below are `drafted` not `ready`.
3. Write the outward drafts to outreach/, one file each, header `status: drafted (gate 2: open-index rows owed, ASKS 34)` or
   `status: ready` if every gate is met, `subject:`, `to:` (an institution or a role, never a person's address; Tomokiyo's address
   stays out of the file), then the body, each carrying: the safe sentence per item from AUDIT.md, the prior print it rests on,
   links to the folder and AUDIT.md, the primary image (Gallica ark at the leaf, or the archive's viewer), and the edition page
   on archive.org or HathiTrust; a sign-off line left blank. Drafts: (a) outreach/tomokiyo-gramont-danzay.md, one email to
   S. Tomokiyo covering Gramont f.29r and f.30 and Danzay f.35-36 (readings made with keys he and Lasry published), plus the
   Carpi 1525 N0 note (ciphers/dupuy452-carpi-1520: his 1526 key opens Raince's letter, whose plaintext Jacqueton 1892 printed);
   (b) outreach/huntington-eckert-blathwayt.md to the Huntington Library's manuscripts curators (Eckert E4/E5 with the cipher
   book, the Blathwayt items); (c) outreach/huygens-nassau-saxony.md to the Huygens Instituut's Willem van Oranje correspondence
   editors (Lodewijk 4610/4611/4616 and the Saxony 53/57/126 postscripts, with the editions Groen and Kluckhohn and what the
   readings add); (d) outreach/bourdeau-issues.md: the text of GitHub issues for dbourdeau/cyphersolver, one per item he lists as
   unsolved or untried among ours (Thurloe P4 at least; check his catalogue text in sources/solver-diffs/2026-09-24-cyphersolver-site.tsv),
   which the parent posts. Also update CONTRIBUTIONS.md with one row per draft (status drafted). Do not send anything.
4. ROOM done line `for LANE V4: outreach gate -- <targets cleared>, <drafts written>, <candidates still to read>`; one-paragraph report.

# Research director, wave 44 (23 Oct 2026, 22:0x UTC by date -u): restart after the idle days -- Sherwood depth verifier, non-BnF discovery, Monluc sorter

Owner, 23 Oct 2026 ~21:5x UTC: "let's keep jamming"; document scans from orders arrive later today. Three jobs, each with its own
cap; common tail .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a
dollar figure for yourself, `python3 tools/dup_check.py <target>` pasted). Done lines addressed for the account-4 parent. Gallica
(gallica.bnf.fr) has answered 403 since 20 Oct: no job below depends on it.

## JOB SHERWOOD-VERIFY3 (account 4; Opus 5.5; cap USD 6; box 60 minutes; hosts: archive.org (11280377bsb page images only for the cells named, at most 8), Google Books API (key, country=US), OpenAlex/S2 (keys); Price: vision calls: 3 x USD 1.2 + 0 reconciliation = 3.6)

VERIFIER (CLAUDE.md template; a session separate from every Sherwood solver). ciphers/sherwood-cossit-1781, AUDIT.md "Current verdict"
(N3, key ours / design published, D2 72.7%). Since that audit, three solver jobs changed the counted reading: SHERWOOD-REREAD (three
image-confirmed digit corrections: 360-33, 165-13, 53-35), SHERWOOD-CELLS (Tan and Certainly M -> S; both doubted S rows held on a
forced-choice read), SHERWOOD-GRID (line-count rule settled from the image; 165-13 = Ha, S on a bigram margin only). Script count now
H 8, C 4, S 148, M 54, I 2 = 160/216 = 74.1%. All three gains rest on digit corrections read by the same model family.
1. Rule 7: fresh clone, `python3 decode_entick.py --check`; re-derive the three changed cells from the Entick page images yourself (one
   blind read per cell, both columns) and the two cypher digits (360-33, 53-35) from the crops in tx2/ and cells/; accept each S only if
   your read matches and the bigram margin rule the folder uses is met; say which of the three you accept.
2. Depth (rule 4a, tools/depth_check.py on the folder's own fields): D2 or D3? D3 needs >=80% H/C/S with the residue mostly names/codes;
   say plainly which side of the line the reading sits and why.
3. Novelty: do not reopen N3 (ASKS 174's chapter is not here yet); but run the one search the first audit lacked if cheap: a phrase search
   on the reading's distinctive words (Google Books API, archive.org full text) and record it.
4. Write a dated "## Depth re-check (SHERWOOD-VERIFY3, 23 Oct 2026)" section in AUDIT.md with the accepted count and the status.json
   fields the parent should set (depth_pct, grade counts); do not edit status.json. Report: accepted S of 3, final H/C/S, D-level, five lines.

## JOB SCOUT-KEYS2 (account 2; Sonnet 5; cap USD 6; box 60 minutes; hosts: discovery.nationalarchives.gov.uk API, www.nationaalarchief.nl and service.archief.nl, archive.org (advancedsearch, full text), Europeana and DPLA APIs (keys), Library of Congress loc.gov JSON, Huygens retroboeken, web search; no Gallica, no BnF; one request at a time, >=1.5 s apart, <=60 per host; Price: vision calls: 0 x USD 0 = 0)

Program C, discovery. The one route that produced a verified reading this fortnight was a scout hit with key material beside the cipher
(SCOUT-KEYS K9 -> sherwood-cossit-1781). SCOUT-KEYS (17 Oct, QUEUE.md "Key-beside-cipher candidates") is used up except the paywalled
TNA rows K5-K8. Do the same search again on hosts that are not the BnF, with one stricter filter: a candidate counts only if (a) a key,
decipherment, gloss, clear copy or code book is on file or in reach for it, AND (b) the cipher item itself has NO surviving period
decipherment and NO printed plaintext you can find (the Monluc f.138 lesson: a clear copy beside the cipher is known text, not a target).
Method: catalogue searches for "cipher"/"cypher"/"chiffre"/"cijfer"/"decipher"/"key" with digitised images (Discovery API with
`digitised=true` where it exists; NA 1.01.02 via Huygens/Nationaal Archief; LoC; Europeana/DPLA TYPE:TEXT; archive.org manuscripts), then
for each hit read the item description and the neighbouring items for a decipherment, and the standard editions by whole-volume grep
(archive.org djvu text) for the plaintext. Run `python3 tools/prior_work.py <slug>` on each candidate you would promote. Score with
tools/scout_rubric.py. Output: QUEUE.md section "## Key-beside-cipher candidates, non-BnF (23 Oct 2026, SCOUT-KEYS2)" with a table
(id, item, key-material evidence quoted, why the decipherment does not survive / is not printed, images route, estimated signs, score)
and harvest/SCOUT-KEYS2-2026-10-23.tsv. Never promote to the board; never decode. Report: candidates found, top three with their evidence,
hosts and request counts, five lines.

## JOB SORTER-KING (account 4; Sonnet 5; cap USD 4; box 45 minutes; hosts: claude.ai artifact publish and database only (crops on disk); Price: vision calls: 0 x USD 0 = 0)

ciphers/fr4735-monluc-lansac-poland-1573, king4/focus.tsv: 21 positions on c258 (f.133, Monluc to the king, 28 Apr 1573) where the
readers split on three look-alike pairs (K39|K19, K61|K38, K12|K04). MONL-KING4 parked the letter at D1 pending a person's sort. Build the
blind sorter page for those tiles with `tools/sign_sorter.py` on the FIXED template (2026-10-20.1: read-back saves, "N changes NOT
saved" banner, "Save my sort" button -- the owner lost a sort to the old template on 20 Oct), exemplars from the keysheet ids only (no
letter values, no decode, no machine guess on the page; `tools/sorter_preflight.py` and `tools/cvd_check.py` pass), publish it, verify
a test write round-trips with ArtifactData and delete your test doc, then write the ASKS.md row (about 5 minutes; never blocking; link;
"press Save at the end") and register the page in tools/data/live_sorters.tsv with the template version. Report: link, tile count,
preflight output, five lines.

## JOB SCOUT-FAGEL (account 2; Sonnet 5; cap USD 6; box 60 minutes; hosts: de-crypt.org listing cache (tools/decode_list.py, login-free), www.nationaalarchief.nl + service.archief.nl (item metadata, scans availability, <=40 requests, >=1.5 s apart), Huygens retroboeken/WVO, archive.org full text, web search; no Gallica; Price: vision calls: 0 x USD 0 = 0)

Program C, the SCOUT-KEYS2 lead NL1 run as its own pass. NA 1.10.29 Familie Fagel inv.nr. 5345 holds about 60 named Dutch diplomatic
cipher keys 1680-1758, each catalogued on DECODE (Bruyninx, Hop, Buys, Keppel, Burmania, Mauricius, Rumpf, Calmette, Larey, Bentinck,
van Rhoon, Verelst, van Berkenrode, Gebler, Swart, Cornabe ...). Only one (R2824, "Prussia 1746") was ever tested here, against a
different target (hellen-frederick-1752, rejected). Nobody has looked for these envoys' OWN enciphered letters. For each key: the envoy,
post and years from DECODE's record; then the envoy's letters in NA (toegang 1.01.02 Staten-Generaal liassen, 1.01.50 Heinsius, 1.10.29
Fagel, the envoy's own archive where one exists, e.g. Bruyninx 1.02.05, Bentinck van Rhoon 3.02.32) via the NA item pages
(drupal-settings-json -> scans availability, CLAUDE.md host table) and the Huygens editions (Heinsius Briefwisseling, retroboeken) for
a printed or in-archive decipherment. A candidate counts only with (a) digitised scans and (b) no surviving decipherment and no printed
plaintext found (grep the Heinsius volumes' djvu text for the letter's date and place). Score with tools/scout_rubric.py; run
tools/prior_work.py on each you would promote. Output: QUEUE.md "## Fagel key register: envoys' own ciphertext (23 Oct 2026,
SCOUT-FAGEL)" table (key id, envoy, post/years, letters located, scans yes/no, decipherment/print found or not, est. signs, score) and
harvest/SCOUT-FAGEL-2026-10-23.tsv. Never promote; never decode. Report: keys checked, candidates meeting both filters, top three, five lines.

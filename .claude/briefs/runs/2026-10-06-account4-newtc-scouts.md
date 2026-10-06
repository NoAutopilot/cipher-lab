# NEWT-C scout (account 4), 6 Oct 2026 23:4x UTC by date -u -- four source-partitioned scout workers

Why: NEW TARGETS round PART C (`.claude/briefs/runs/2026-10-06-acct3-newtargets.md`; owner asked to open more targets). Lane
NEWT-C-account-4 (session_01XXcLqsU7GkbYZoN7rPaBzx). The backlog is spent; this scout feeds check-solved on the top 6.

Template: `.claude/briefs/scout.md` + the common tail in `.claude/briefs/README.md` (read both). Scout only: never promote,
never solve, never transcribe, never classify novelty. Model Sonnet. Cap USD 6, box 50 minutes from your own `date -u` at start:
stop and push at the cap or at 50 minutes, whichever first; at 40 minutes push what you have. At most 2 subagents (Sonnet).
Image budget parked: no paid orders; an item needing one is a near miss.

## Selection rule (what a kept row is)
EV = P(first USD 3 cheap test moves it) x value / cost. Prefer, in order: (1) a period key or decipherment on/beside the leaf or
a sibling letter's key we can apply; (2) pools (one sender/office/key family, >= 2,000 signs); (3) images or transcription one
free fetch away (CLAUDE.md host table; Gallica: probe once first -- it was failing 6 Oct; on failure log it and use DECODE
thumbnails / other routes); (4) a language with an era-matched corpus in tools/data. BnF tie-breaker at equal value. Owner, 6 Oct:
do not spend on items whose text is already known (already deciphered on the leaf, printed in clear, read by a solver repo) --
those are near misses unless they give a key for an unread sibling (then the row is the sibling).

## Read first -- do not re-find what is on file
- `ls ciphers/` (300 folders) and grep QUEUE.md, POOLS.tsv, KEY-ADJACENT.tsv, KEY-OFFICES.tsv for every candidate's
  shelfmark/sender/record id. Already a folder or a QUEUE row = not new; a row on it only if you name letters outside it.
- `sources/pools-scout/2026-10-03/P1-P4.md` (last scout, 3 Oct) and QUEUE.md "LANE-POOLS scout, 3 Oct 2026" -- do not re-nominate.
- Exclusions: Birago/Nevers/Ceppo/Vieuville anything, armstrong-madison-1808, debosnys-1883, mercy/espagnol142, and the five
  NEWT-B items (hyde-add4166-1659, craven-rupert-1648, bagno-francia104-1652, cornwallis-pro3011-1780, charles-hm-cabinet-1645).
- Solver repos, fresh shallow clones in your scratchpad: github.com/dbourdeau/cyphersolver, github.com/aaymeloglu/unsolved-ciphers,
  AND github.com/el-descifrador/cabinet-noir (published 30 Vargas Mexia readings 2 Oct). Grep each candidate's record id,
  shelfmark, sender; a hit means read or worked -> near miss with the quoted line. Cite, never copy Aymeloglu's code.

## Parts (one worker each; your prompt names your part)
- **S1 DECODE records carrying a decipherment or key document.** `sources/decode/` (records-*.tsv, dc11-20-documents-2026-09-24.tsv,
  keys-all-2026-09-28-merged.tsv, access-modes-2026-09-26.tsv). One fresh login-free `tools/decode_list.py` pass for records added
  since 24 Sept (snapshot is older than 7 days). Wanted: a NON-decrypted cipher record whose sibling (same sender/recipient/years/
  archive series) carries a key or decipherment document (`tools/decode_neighbours.py` pairs), or a record whose own document list
  names a key while its status is not Decrypted. No DECODE login.
- **S2 Gallica fonds français + Mélanges de Colbert.** BnF fr. (ambassadors' dispatch volumes) and Mélanges de Colbert (Colbert 1-
  500 is a different fonds; both allowed) items with cipher letters AND a decipherment/key nearby; archivesetmanuscrits.bnf.fr
  dépouillement phrases ("en chiffre", "chiffre et déchiffrement", "lettre chiffrée", "avec le déchiffrement"), Gallica SRU with
  adjacency phrases (never "chiffré" alone). Probe Gallica once (`curl -sS -o /dev/null -w "%{http_code}" -A "Mozilla/5.0"
  https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060927q/manifest.json`); if it fails, log it and work from the catalogue only.
  Estimate signs from 1-3 sampled canvases when Gallica answers (`full/600,/0/default.jpg`, one look each, no transcription).
  Exclude fr.16xxx volumes already in ciphers/ (fr16104, fr16142, fr16144, fr16045 ...; check ls).
- **S3 Europeana + DPLA (keyed).** `EUROPEANA_API_KEY` (wskey=) and `DPLA_API_KEY` (api_key=); test presence with `test -n`, never
  print. Queries in en/fr/es/it/de/nl/pt/la for cipher letters with images (TYPE:TEXT/IMAGE): chiffre, en chiffre, cifra, cifrado,
  in cipher, cypher, Chiffre, Geheimschrift, ziffer, cijfer, déchiffrement, descifrado, decifrato, nomenclator. Keep only items
  with an IIIF/copy-free image and evidence of cipher text on the leaf (one vision look at a thumbnail per kept item).
- **S4 Tomokiyo key pages whose letters we do not hold.** `sources/cryptiana/` (CRYPTO-INDEX.tsv, READABLE.tsv, keys/, web/, blog/)
  and at most 25 fresh fetches of cryptiana.web.fc2.com pages: every key Tomokiyo reconstructs or prints whose letters (same key)
  are named by shelfmark but have no ciphers/ folder and no QUEUE row, and which he does not say he read in full. The 3 Oct P1
  scout kept 3 (Vargas Mexia, d'Avaux Baluze 167, Perez); go past those.

## Every kept row
Write `sources/newt-scout/2026-10-06/S<n>.tsv` (tab-separated) with these columns:
`cand_id  slug_suggested  sender  recipient  date_or_years  shelfmarks_or_records  letters  est_signs  sign_basis  image_route
availability_quote  key_status  prior_reading  solver_repo_overlap  language  corpus  first_cheap_test  test_quote  p_move  value
cost_usd  ev  notes`
- `slug_suggested`: house style `<fonds-or-sender>-<who>-<year>` (look at ls ciphers/).
- `availability_quote`: the holding catalogue's own flag or the image host's manifest URL/ark (Access playbook preamble).
- `key_status`: none / period key on file (where) / published modern key (who) / decipherment on or beside the leaf (where).
- `prior_reading` and `solver_repo_overlap`: quoted lines or "no hit for <terms> in <repo>".
- `first_cheap_test`: runnable at USD 3 with a matched control (rule 3a); `test_quote`: the exact source sentence that makes it
  possible (scout.md "Quote the source").
- `ev` = p_move x value / cost_usd. Keep at most 8 rows; the rest go in a near-miss table in S<n>.md with a one-line reason.
Also write `sources/newt-scout/2026-10-06/S<n>.md`: five-line report (raw, kept, digitised count; searches with counts per host;
near misses; unreachable hosts). Do NOT edit QUEUE.md, QUEUE-scores.json or any ciphers/ folder -- the lane orchestrator merges.

Good-citizen rule: one request at a time per host, >= 1.5 s apart (DECODE 1.5-2 s), a few hundred per host at most; stop a host
on 429/403/challenge, one retry after a pause at most. Never print credentials. Never call AskUserQuestion. Never name the owner.
Never the words new, first, novel, solved, cracked for anything this project did.

Steps: 0 `python3 tools/room.py --start`; `date -u`; ROOM claim via tools/room.py: "<S-part> scout, cap 6, box end <time>, for LANE
NEWT-C-account-4". 1 read files above. 2 harvest. 3 write S<n>.tsv/.md; `git add` those two paths only; commit; `git fetch origin
main && git rebase FETCH_HEAD && git push origin HEAD:main`. 4 done line (tools/room.py): `done (<start>-<end> UTC, brief met|box|cap):
commit <sha>. S<n>: <k> kept (top: <slug> ev <x>), <m> near misses; requests per host ...; cost: see the lane ledger, for LANE
NEWT-C-account-4`. Report in five lines (first line the answer); stop. Report what was found and where it was not found; do not
classify novelty.

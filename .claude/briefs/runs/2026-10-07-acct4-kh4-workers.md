# KH-4 worker brief (account 4, LANE KH-4, session_01DP265vPazck9n51AQqAN1V; written 7 Oct 2026 ~17:45 UTC)

Parent round: .claude/briefs/runs/2026-10-07-acct3-keyhunt.md (read it; steps 1-4 there are your job). You are worker
KH4-<X> for LANE KH-4. Model Opus 5.5. Your KEY-OFFICES.tsv rows are listed at the bottom (row numbers count the header
as row 1). Do not touch other rows' keys.

0. `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`; read the last 30
   ROOM.md lines; post a claim with `tools/room.py "KH4-<X> worker" '<claim text with box end>' --push`.
1. Per key row: read its key file, the notes_source and the target folder's NOTES.md (siblings already listed or read
   there). Then list the same office's OTHER letters within the key's window (+/- 3 years) in digitised holdings, using
   catalogue APIs and scripts (CLAUDE.md Access playbook + host table; Usage 2: scripts read, you judge hits). One host at
   a time, >=1.5 s apart, a few hundred requests per host at most, stop a host on 429/403/challenge.
2. Keep only letters that are (a) digitised and fetchable from the cloud, (b) carry cipher, (c) not already a folder in
   ciphers/ and not already read by Bourdeau/Aymeloglu/DECODE/Tomokiyo (grep sources/, sources/cryptiana/, the solver
   diffs; DECODE listing via tools/decode_list.py if useful), (d) no interlinear decipherment or printed clear text found.
3. Survivors: at most TWO leaves for the whole job (pick the best). For each: fetch once (images/manifest.json),
   crop with `tools/iiif_lines.py` (paste the command; never hand a full page to a subagent), two blind Sonnet passes on
   ONE leaf, one subagent call per pass per leaf, reconcile with tools/reconcile_passes.py, decode with the held key
   (tools/decode_key.py where a decode.json fits, else a short script beside the key), matched control = same decode
   with a shuffled key at the same N (>=20 shuffles; report real vs shuffle mean and p95 of a token-hit or judge
   score that a shuffled key CAN change -- rule 3 orthogonality), judge with tools/judge_plaintext.py where an
   era-matched corpus exists. Grade tokens H/C/S/M/I. Control passed -> new folder ciphers/<slug>/ with ciphertext.txt,
   NOTES.md (status `open` until check-solved; record that check-solved and tools/intake_gate_check.py are the next step
   before deep work), the decode script with --check (rule 7). Control failed -> one line in the key's folder NOTES.md.
4. Write every candidate considered (kept or dropped, with reason) to keyhunt/2026-10-07-KH4<X>.tsv with columns:
   key_path, letter, shelfmark, digitised, cipher, already_read_by, glossed, action, result. One row per candidate;
   a key with zero candidates still gets one row (letter "none found", with what was searched). The count of unread
   siblings per key is the deliverable.
5. Cap and box: $6.5 of usage, box 150 min from your start. Per-unit pricing: catalogue sweep ~ $0.5/key row; a decoded
   leaf ~ $2.5 (2 reads + 1 reconciliation + decode/control). Stop before starting a unit that would cross 80% of either.
6. Close: push by explicit path (fetch/rebase first); `tools/file_shrink_guard.py` on every file you touched that existed
   before; one ROOM done line naming per-key unread-sibling counts, any leaf decoded and its control numbers, commits.
   Report what was found and where it was not found; do not classify novelty (rule 10). Never the words solved, cracked,
   novel, first, new for anything this project did.
Never call AskUserQuestion; never print credentials; never name the owner; read `date -u` before writing any time.
Off limits: Birago (fr3252), Armstrong, Debosnys targets (owner sorters / private) -- note: nevers-birago-fr3251-1572 is a
different folder and is in scope for KH4-A only as a key; do not edit birago-fr3252 files.
Good-citizen rule and host table apply. Report request counts per host in the done line.

## Assignments
- KH4-A (Nevers / League French keys, BnF Gallica): rows 61 ceppo-nevers fr3251, 62 nevers-birago fr3251 1572,
  63 vieuville-nevers fr4715/fr3641, 65 mayenne 1592 fr3982/3983.
- KH4-B (Villeroy / Colbert / Brussels, BnF Gallica + DECODE listing): rows 53 fr7129 key_f274, 54 fr7129 key_f275
  (fr.7129/7131 Bongars letters), 64 colbert-croissy 1668 (Melanges de Colbert), 67 espagnol142-mercy (Espagnol 144 and
  Brussels secretariat siblings 1645-51).
- KH4-C (Dutch/German: Erlangen, Nationaal Archief, WVO/Huygens): rows 49 trew-posthius, 50 vanbeuningen-dewitt,
  51-52 willem-van-hessen key_1069 and key_174, 69-70 na-suriname key_period and key_period_nieuw.
- KH4-D (US State Dept WE028, Library of Congress / NARA IIIF): row 68 WE028 (Pinkney, Erving, Monroe, Armstrong-era
  legation letters 1803-1811 in loc.gov Madison/Monroe/Jefferson papers; Armstrong letters themselves are off limits).
- KH4-E (Spanish/Italian, RAH/DECODE/Beinecke/Mantua): rows 55-56 AlonsoSanchez_1/_2, 57-60 spanish_1..4 (Puebla),
  66 spinelli c1515, 71 gonzaga-nevers ASMN.

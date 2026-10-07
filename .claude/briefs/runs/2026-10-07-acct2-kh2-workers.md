# KH-2 worker brief (account 2, LANE KH-2, session_01R5gb64HksKMDGLo9vTiGgj; written 7 Oct 2026 ~18:20 UTC)

Parent round: .claude/briefs/runs/2026-10-07-acct3-keyhunt.md (read it; steps 1-4 there are your job). You are worker
KH2-<X> for LANE KH-2. Model Opus 5.5. Your KEY-OFFICES.tsv rows are listed at the bottom (row numbers count the header
as row 1). Do not touch other rows' keys.

0. `git fetch origin && git checkout -B main origin/main`; `python3 tools/room.py --start`; `date -u`; read the last 30
   ROOM.md lines; post a claim with `tools/room.py "KH2-<X> worker" '<claim text with box end>' --push`.
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
4. Write every candidate considered (kept or dropped, with reason) to keyhunt/2026-10-07-KH2<X>.tsv with columns:
   key_path, letter, shelfmark, digitised, cipher, already_read_by, glossed, action, result. One row per candidate;
   a key with zero candidates still gets one row (letter "none found", with what was searched). The count of unread
   siblings per key is the deliverable.
5. Cap and box: $5.5 of usage, box 140 min from your start. Per-unit pricing: catalogue sweep ~ $0.5/key row; a decoded
   leaf ~ $2.5 (2 reads + 1 reconciliation + decode/control). Stop before starting a unit that would cross 80% of either.
6. Close: push by explicit path (fetch/rebase first); `tools/file_shrink_guard.py` on every file you touched that existed
   before; one ROOM done line naming per-key unread-sibling counts, any leaf decoded and its control numbers, commits.
   Report what was found and where it was not found; do not classify novelty (rule 10). Never the words solved, cracked,
   novel, first, new for anything this project did.
Never call AskUserQuestion; never print credentials; never name the owner; read `date -u` before writing any time.
Off limits: Birago (fr3252), Armstrong, Debosnys targets (owner sorters / private).
Good-citizen rule and host table apply. Report request counts per host in the done line.

Already searched today by other lanes (read their TSVs/ROOM done lines first, do not repeat a search they logged):
keyhunt/2026-10-07-KH4C.tsv (WVO geheim/cijfer by correspondent, Aerztebriefe Geheimschrift list incl. Posthius),
KEYHUNT-2026-10-07-KH1-D.tsv (WVO geheimschrift search: WVO 1068 glossed), KEYHUNT-2026-10-07-KH1-*.tsv (Gallica sweeps).

## Assignments (KEY-OFFICES.tsv rows 26-48)
- KH2-A (BnF Gallica / archivesetmanuscrits): rows 26-28 fr5160-letellier-1653 key_1659, key_brienne_1647,
  key_brienne_1651 (Brienne office: Servien at Turin 1659, Brienne ciphers 1647/1651, Clairambault 1067 shares one --
  clair1067 is KH1-C's, do not redo its siblings), row 29 fr5761-election-1519 (1519 election embassy, fr.5761 and
  neighbours, Gallica).
- KH2-B (German/Swedish/Erlangen): row 30 gunther-van-schwarzburg-1561 (Oranje <-> Schwarzburg 1558-64: WVO by
  correspondent, Thueringisches Staatsarchiv Rudolstadt/Sondershausen online finding aids), row 38 oxenstierna-gustav-
  adolf-1632 (Riksarkivet sok.riksarkivet.se / RA digital images, AOSB printed edition for clear text), row 48
  trew-posthius key.tsv (KH4-C already logged 0 from the Aerztebriefe list -- cite it in one row, no new search unless
  the Trew Briefsammlung UB Erlangen digital catalogue adds something cheaply).
- KH2-C (Huntington CONTENTdm, CLAUDE.md Huntington recipe): row 31 huntington-blathwayt-madrid-1728 (mssBLA 1725-31),
  rows 32-33 huntington-luzerne-destouches-1781 key and key_tomokiyo (mssDE 1-120 and La Luzerne letters elsewhere
  digitised, 1778-84: LOC, Gallica Affaires etrangeres CP Etats-Unis if imaged).
- KH2-D (WVO / Huygens / Groen van Prinsterer): rows 34-35 jan-van-nassau-1572-75 key_1572, key_5549; row 36
  lodewijk-van-nassau-1573-74; row 37 orange-nassau-1572 key_nepveu (Nepveu cipher 1569-75). WVO by correspondent
  + opmerkingen (cijfer/geheim/chiffre), the folder NOTES census, Groen's Archives ou correspondance for clear text.
- KH2-E (RAH / BnF italien / DECODE): row 39 rah-canada-1869 (Conde de la Canada letters 1866-72 in RAH OAI-PMH,
  CLAUDE.md RAH recipe), row 40 sforza-maino-1446 (Sforza chancery 1443-49 in BnF italien 1583-1595 on Gallica and
  DECODE listing; ASMi Sforzesco not online).
- KH2-F (Thurloe office, printed Birch 1742 on Internet Archive full text + Bodleian Rawlinson A if digitised): rows
  41-47 thurloe-printed key_blake, key_butler, key_downing, key_fauconberg, key_montagu, key_steele, pool_1654
  key_stamford. Sibling = a cipher passage in Birch printed as cipher/undeciphered ("the rest in cipher", unglossed
  number groups) from the same correspondent and key window, not already in thurloe-printed/. Use the IA djvu text
  with scripts (tools/ia_numeral_runs.py), not a model reading volumes.

# ST-REBUILD worker brief (account 2, LANE ST-REBUILD, session_013jm31txSFKvvEoKkMWjGn8; written 7 Oct 2026 ~21:30 UTC)

Parent round: .claude/briefs/runs/2026-10-07-acct3-steam.md, section ST-REBUILD (read it). You are one of the workers
named at the bottom. Read your own section, CLAUDE.md, TRANSCRIPTION.md (if your job reads signs), the target folder's
NOTES.md, and the common tail in .claude/briefs/README.md. Model Opus 5.5 unless your section says otherwise.

0. `python3 tools/room.py --start` (if it fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B
   main HEAD`); `date -u`; read the last 30 ROOM.md lines and the last 20 of UPDATES.md; claim with
   `python3 tools/room.py "<ID> worker (account 2)" '<claim, cap, box end, for LANE ST-REBUILD>'` (single quotes).
   Post a halfway line at half your box, and a done line at the end addressed "for LANE ST-REBUILD".
1. Usage rules hold: one host at a time, >=1.5 s apart (Gallica 1-2 s), stop a host on 429/403/challenge after one
   retry; images fetched once into the folder's images/ with images/manifest.json; crops with
   `tools/iiif_lines.py --ark ... --canvas N --region ... --out ... --debug` (paste the command; check the overlay);
   never hand a full page to a subagent; one subagent call = one cipher slip's line crops; at most 4 subagents at once.
   Trial crops and throwaway runs go to your scratchpad, never under ciphers/.
2. Grading (rule 4): a value taken from a clear copy/print is C; a cryptanalytic or decoded value with a control is S;
   uncertain M; inferred I. A later-hand clear copy is a decipherment, so it gives C at best.
3. Controls (rule 3): every gate below is pre-registered here; write the numbers side by side; stop at a failed
   control (no target decode after a failed gate). The shuffled-key control must be able to change the statistic.
4. Close: push by explicit path (`python3 tools/room.py --push <paths>`), `python3 tools/file_shrink_guard.py` on every
   pre-existing file you touched, `python3 tools/gaps_check.py <target>` if you leave a target `partial`. Report what
   was found and where it was not found; do not classify novelty (rule 10); never the words solved, cracked, novel,
   first, new for anything this project did. Never call AskUserQuestion; never print credentials; never name the
   owner; read `date -u` before writing any time. Report requests per host in the done line.
5. Cap and box are yours below. Stop before starting a unit that would cross 80% of either; the box is also a minimum.

---

## SFZ-1 (Opus, cap $16, box 150 min): Amidani 1447 known-plaintext key rebuild, hold-out gate, then f.70

Why: BnF italien 1584 (Gallica ark:/12148/btv1b100373864, from microfilm, two pages per canvas) holds Vincenzo
Amidani's 1447 cipher slips with clear copies beside them (KH2-E, KH2-E2: ciphers/sforza-maino-1446/NOTES.md last two
sections; keyhunt/2026-10-07-KH2E.tsv, -KH2E2.tsv). Amidani also wrote f.70 of italien 1583 (4 May 1446), part of the
closed-negative sforza-maino-1446 target, transcribed only by Bourdeau (`ciphertext_f70.txt`, codes in `signs.tsv`).

Scope (partial-scope carve-out, CLAUDE.md briefs README: known-plaintext alignment, grade C, is allowed without the
intake gate; a decode of an unglossed letter is not -- see step 6). Work in a new folder
`ciphers/sforza-italien1584-1447/amidani/` (SFZ-0 is creating the parent folder's NOTES.md in parallel: do not write
the parent NOTES.md except one pointer line at the end, after fetch/rebase).

Units, in order (stop before a unit that would cross 80% of cap/box):
 U1 ff.366 cipher / f.365 copy (canvases ~359-360), U2 f.367 / f.368 copy, U3 f.371 / f.370 copy (canvases ~359-364;
 check folio numbers on the image, the offset drifts), U4 f.148 / f.147 copy (canvases ~140-141), U5 f.206 / f.205
 (canvases ~199-200). f.369 (clear with inline cipher) only if U1-U3 are short.
Per unit: (a) native-resolution region fetch + line crops; (b) sign reading: first try `tools/glyph_atlas.py segment`
 on the slip (no model cost); if its debug shows clean tiles, cluster and name clusters FROM THE ALIGNMENT (cluster
 sequence vs clear copy) and say so; else two blind Sonnet line-read passes, both given the same label sheet (Bourdeau's
 sign descriptions in ciphers/sforza-maino-1446/signs.tsv plus new labels allowed, described in words), reconcile with
 `tools/reconcile_passes.py`; report err_2reader (no benchmark item of this hand: err_true not measurable, say so);
 (c) the clear copy read from line crops into plain text (one pass, then check every word the alignment rejects
 against the crop); (d) align the slip to its copy with `python3 tools/interlinear_align.py stream SYMBOLS.txt TEXT.txt
 OUT_KEY.tsv` (or `align` with --code-prefix if stream does not fit); key.tsv per unit and pooled.
 Pricing per unit: about 2 read passes + 1 reconcile + 1 clear-copy pass = 4 calls at ~$1.0-1.5 = ~$5 incl. alignment.
 Expect 2-3 units inside the cap. The degenerate optimum of the alignment is "every sign null / one letter everywhere":
 keep --null-cost at its default or below and report how many signs aligned to null.
Gate G1 (pre-registered, leave-one-letter-out, needs >=2 units): key built from the other units, decode the held-out
 slip's reconciled signs, score letter accuracy against its own clear copy (edit-distance alignment, nulls excluded,
 signs absent from the training key count as wrong). PASS = mean held-out accuracy >= 0.60 AND above the p95 of 200
 shuffled-key controls (permute the training key's sign->value map). Report real, shuffle mean, p95 per held-out unit.
 Also report: is it one key across U1-U5, or do units disagree on shared signs (count conflicts)?
Step 6, only if G1 PASSes: f.70. Map Bourdeau's f.70 codes to your labels by his descriptions (signs.tsv; say which
 codes have no counterpart). Decode `ciphertext_f70.txt` with the pooled key; control = 200 shuffled keys on the same
 statistic (a language score: `tools/judge_plaintext.py` with an inline spec, language it16dip -- era mismatch, 1540s vs
 1446, flag it -- plus the fraction of 4-grams found in the clear copies' text). This is a TEST of whether f.70 shares
 the key, not a reading claim: do not grade f.70 tokens above M and do not write a reading file for it unless the
 test passes, in which case write the decode with a --check script and stop there (check-solved/premise check for
 sforza-maino-1446 and a verifier come next, from the lane). If G1 FAILs: log the numbers, no f.70 decode.
Deliverables: amidani/{ciphertext_*.txt, clear_*.txt, key.tsv, align_*.tsv, gate_g1.tsv, NOTES.md}, images manifest,
 a decode script with --check if anything is decoded. NOTES.md first line status `partial` or `open`.

## SFZ-0 (Sonnet 5.5, cap $5, box 75 min): the four 1447 cipher items without a clear copy -- copy window, check-solved

Why: KH2-E2 found four italien 1584 cipher items with no clear copy in its strip window: f.13 (Pietro Pusterla 21 Jan
1447), f.15 (Duke 23 Jan), f.143 (Marcolino 4 May, "Rome", mixed clear+cipher), f.259 (Guarna 22 Aug, mixed). "The
window may simply have missed their copies." These are the only reading targets of the lane's Sforza step.
1. Create `ciphers/sforza-italien1584-1447/NOTES.md` (status line `open`; pool folder for the 1447 cipher letters of
   italien 1584; cite KH2-E/KH2-E2 rows; SFZ-1 works in amidani/).
2. For each of the four: fetch +/-8 canvases at ~1200 px (one at a time), read folio numbers and the later-hand headers
   ("1447 21 janvier" etc.), and record whether a clear copy of THIS letter exists anywhere in that window, and whether
   the cipher part is also deciphered interlinearly or in the margin. Also confirm sender from the header/signature.
3. For each item still without a copy: list its sender's glossed pairs (cipher folio, copy folio, canvases, rough sign
   count from the 1200 px view) -- the pool a later worker rebuilds that correspondent's key from.
4. Check-solved per .claude/briefs/check-solved.md for the survivors as one pool (Mazzatinti 1883 "In cifre"; web
   search for editions of Sforza 1447 correspondence with Pusterla, Marcolino Barbavara, Nicolo Guarna and the Duke --
   e.g. Carteggio degli oratori sforzeschi, Osio *Documenti diplomatici tratti dagli archivi milanesi*, Cerioni 1970;
   IA/Google Books full text with the playbook's keys; DECODE listing via tools/decode_list.py for italien 1584; the
   two solver repos; Cryptiana/Cipherbrain), including the "## Premise check" section, then
   `python3 tools/intake_gate_check.py sforza-italien1584-1447` and paste its output in NOTES.md.
5. Rows to keyhunt/2026-10-07-SFZ0.tsv (KH2E2 columns). No transcription, no decode.

## THU-1 (Opus, cap $7, box 90 min): thurloe-printed -- extend key_montagu / key_fauconberg from glossed siblings

Why: KH2-F (keyhunt/2026-10-07-KH2F.tsv) found six glossed Montagu letters (Birch vols 1, 4, 5, 7) and two glossed
Fauconberg letters (vol 7) not yet in ciphers/thurloe-printed/, and 0 unglossed siblings. The printed glosses make the
extension a scripted job (Usage 2: scripts read, you judge).
1. For each sibling: `python3 tools/interlinear_align.py pairs <djvu> FIRST LAST <folder>/montagu_<date>_pairs.tsv`
   (djvu line ranges in the KH2F rows; fetch each volume's _djvu.txt once into your scratchpad; vol 6 via the bim_ copy
   if needed), then `align` with the existing key as --prior where the tool allows it.
2. Gate G2 (pre-registered, known-answer): before extending, decode each sibling's cipher line with the CURRENT key
   (key_montagu_extended.tsv / key_fauconberg.tsv) and score group-level agreement with its own printed gloss vs 200
   shuffled keys. PASS (same key) = agreement >= 0.70 and > shuffle p95. Only PASS letters join the extended key; a FAIL
   is a different key/channel and is logged as such.
3. Extend: write key_montagu_extended2.tsv / key_fauconberg_extended.tsv with counts and which letter attests each code;
   list codes newly attested. Then re-try the folder's known unglossed residue with the extended keys: the 14 groups
   on P10 p.620 line 10 (Blake; only if a Blake key is extended -- otherwise say not applicable) and P3's postscript
   (Butler) -- only where the extended key actually covers new codes those lines use; grade M at best unless a
   control passes.
4. Name unglossed same-channel letters beyond Birch (Bodleian MS Rawlinson A Montagu/Fauconberg cipher letters not
   printed by Birch: catalogue record + availability flag per the Access playbook, EMLO Solr notes); do not order
   anything; an ASKS.md row only through the playbook rules.
5. NOTES.md section "Key extension (THU-1, 7 Oct 2026)" with the G2 numbers; status line unchanged unless a reading
   moves. All siblings are N0 by construction (printed decipherment) -- say so; nothing here is a counted result
   unless step 3/4 reads an unglossed text.

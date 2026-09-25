LANE KX job 1: KX-XMATCH, mechanical key cross-match. Sonnet (claude-sonnet-5). Stall alarm $8 (not a budget; see COMMON).
Parent: LANE KX orchestrator session_01JPoYAFvVfraJibxQdQfrqp. Read .claude/briefs/runs/2026-09-25-lane-kx-COMMON.md first; it binds.
ROOM role: "LANE KX worker KX-XMATCH (Sonnet, <your session id>)".

Question: can any key table we hold read any ciphertext on disk it was not built for?

Files you may write: tools/key_crossmatch.py, tools/tests/test_key_crossmatch.py, KEY-CROSSMATCH.tsv (repo root),
KEY-CROSSMATCH.md (at most 40 lines: method, positive-control table, controls, hit list), ROOM.md. Nothing else:
no target folder, no QUEUE.md, no NOTES.md.

1. Keys. `find ciphers -maxdepth 3 \( -iname 'key*.tsv' -o -iname 'key*.txt' \)`, excluding names with draft,
   candidate, atlas, pass, conflicts, counts, align, crosscheck, trial (report every excluded file and why), plus the
   published key tables already on disk (sources/solver-diffs/*keys*.tsv, the Bourdeau key46/key60 tables wherever
   they sit -- grep for them -- and any Tomokiyo key transcription under sources/cryptiana or ciphers/*). About 60
   tables in 30 folders. Normalise each to rows (code, plaintext, grade) with metadata: source path, folder, office
   (sender -> recipient), years, language (from the folder's NOTES.md first lines; mark `?` when unstated), design
   (monoalphabetic / homophonic / nomenclator / code), sign type (digits, letters, symbols, mixed) and the code-length
   distribution. Keys whose columns differ (code/value/grade/source/note in most, others not) need a small adapter
   each; log any table you could not parse rather than guessing.
2. Ciphertexts. Every ciphertext*.tsv/.txt (and the tokens column of printed-ciphertext passages already transcribed,
   e.g. ciphers/thurloe-printed, sources/solver-diffs) in every ciphers/<t>/ -- include ALL of them, not only unread
   ones, because the positive control needs the solved ones; tag each with its folder's status (first lines of NOTES.md:
   open, partial, blocked, closed-negative, solved, found-solved) and whether a reading file already exists for it.
   Tokenise by the folder's own decode.json where one exists (tools/decode_key.py knows the layouts; reuse its
   parser, do not copy it), else by whitespace/tab and report the choice.
3. Compatibility filter per (key, ciphertext): same sign type; coverage = share of ciphertext tokens whose code is in
   the key (report it); length-distribution overlap. Keep pairs with coverage >= 0.5 for the scoring step; list the rest
   with their coverage only.
4. Score. Decode with the key; score the resulting letter stream with tools/judge_plaintext.py's language model
   (import its functions; add a small option to judge_plaintext.py only if you must, with its --selftest still passing)
   in the key's language. Corpora on disk are de16, fr16, it16 and modern English under tools/data. For la, nl, pt, es,
   and 16th-17th c. English there is no corpus there: build one from reading*.txt / plaintext*.txt files already in
   the repo for that language (list the files used; exclude the target's own), save it under tools/data/<lang>_repo/,
   and say so in KEY-CROSSMATCH.md. Controls, each at least 20 draws: (a) the same key with its code->plaintext
   mapping shuffled; (b) the same ciphertext decoded by every other compatible key of the same design (the "unrelated
   key" null). Report the score and a z against each control. Verdict: `own` (key built for this text), `hit` (z >= 4
   against both controls and coverage >= 0.7), `weak` (z >= 2.5 against both), `none`.
5. POSITIVE CONTROL FIRST, before any other row is trusted: every key must rank its own ciphertext(s) first among all
   ciphertexts of its sign type, with a z >= 4 against both controls -- e.g. ciphers/lodewijk-van-nassau-1573-74/key.tsv
   on ciphertext_4610.tsv, Gramont's key on its own ciphertext, the Thurloe keys on their own passages. A key that
   fails its own text means the tool (tokeniser, adapter, scorer) is wrong for that design: fix it and re-run; if you
   cannot, mark the key `unusable` with the reason and exclude it from the hit list. Put the per-key positive-control
   table (key, own text, own rank, own z vs each control) in KEY-CROSSMATCH.md.
6. Output KEY-CROSSMATCH.tsv, columns: ciphertext_path, ct_status, key_path, key_office, key_years, key_lang, design,
   coverage, score, z_shuffled, z_unrelated, rank_of_this_key_for_ct, verdict. Sorted: hits, weak, then by z. Commit
   the tool (with --help and an offline test in tools/tests/ that runs the positive control on two small fixtures),
   the table and the md. Push after the positive control passes and again at the end.
7. Do not read, decode further or write anything in any target folder. Do not judge a hit a reading: a hit is a
   candidate for the orchestrator's job 3. No network needed; report 0 requests if none.

Final paragraph: first line "positive control: K of N keys rank their own text first; H hits, W weak", then the hit
rows (ciphertext, key, coverage, z, z), files touched, cost.

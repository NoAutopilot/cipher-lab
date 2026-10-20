# Research director, wave 38 (20 Oct 2026, 12:4x UTC by date -u): verifier for the Monluc Cipher 1 reading (c268 + c269)

Common tail: .claude/briefs/README.md applies (ROOM claim/done with the usage phrase, wall-clock box, no AskUserQuestion, never a dollar
figure for yourself, `python3 tools/dup_check.py fr4735-monluc-lansac-poland-1573` pasted). You are a VERIFIER (CLAUDE.md "Verifier brief
(template)"): a session other than every solver on this target; you do not protect their conclusions.

## JOB VERIFY-MONLUC (account 4; Opus 5.5; cap USD 7; box 75 minutes; hosts: archive.org full-text and be-api search, Google Books API (key, country=US), OpenAlex and Semantic Scholar (keys), the two solver repositories (shallow clone, grep only), Gallica/openapi.bnf.fr catalogue pages only if they answer (Gallica has answered 403 since 02:1x UTC); Price: vision calls: 0 x USD 0 = 0)

VERIFIER: ciphers/fr4735-monluc-lansac-poland-1573. Claim under audit: Monluc's Cipher 1 letter on BnF fr.4735 c268 (f.138r, L01-L30)
and c269 (f.138v, L01-L33) is read by aligning a period clear copy in the same volume (ff.140r-141r) to the decoded cipher, grade C
where the alignment places it (SUP-MONLUC, MONL-C269A, MONL-C269C, 20 Oct 2026; PREREGs d8b8c1d1f, a690865da, 26a27ee85); target
tokens C 984 / M 1041 / U 108 of 2133 (decode_key.py). No AUDIT.md exists yet; no status.json row.
1. Rule 7: in a fresh clone, re-derive the reading from the spec (specs/fr4735-monluc-lansac-poland-1573.json), key.tsv, decode.json and
   the ciphertext files with `python3 tools/decode_key.py ciphers/fr4735-monluc-lansac-poland-1573 --check` and the alignment scripts'
   own --check (align_c268.py, c269/align_c269 or equivalent). Then audit the alignment gates: re-run each registered score and its
   placed-shuffled control from the committed passes and confirm the PREREG commits precede the reads they govern (git log order).
   Check one thing the solvers did not: whether the C grade is earned where the alignment places a clear word against a decode that
   disagrees with it letter-for-letter (count such positions; C should mean the clear text supplies the meaning AND the decode does
   not contradict it -- report the share of C tokens with a contradicting decode, and grade those M in your count).
2. Novelty (rule 10), steps 1-5 of the verifier template: the Monluc letter's date, sender (Jean de Monluc, bishop of Valence) and
   recipient, and whether its decipherment or the clear copy's text is already printed (Noailles 1867 vols I-III; Champion and others
   on the 1573 Polish election; the BnF finding aid for fr.4735; Tomokiyo's Cryptiana pages; both solver repositories; Lasry's BnF
   cipher research published by Bourdeau 10 Oct 2026). Phrase-search the clear copy's distinctive wording. Record whose key read it
   (`period` clear copy / `published` Tomokiyo table / `ours`) and whether this is a key application (CLAUDE.md pipeline 7).
3. Depth (rule 4a) with tools/depth_check.py: % H/C/S, D-level, one true sentence about the content if D2+.
4. Write ciphers/fr4735-monluc-lansac-poland-1573/AUDIT.md (N-class, key source, depth, safe and unsafe sentence, search log per family,
   postmortem with any over-claiming sentence in NOTES.md corrected); append a SECOND-OPINIONS-QUEUE.tsv row if N3 or better. Do not
   decode anything new, do not touch other targets, do not edit status.json (the parent does).
Report: rule-7 result, gate audit, contradicting-C share, N-class, key source, depth, five lines.

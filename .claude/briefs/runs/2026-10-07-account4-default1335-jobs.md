# LANE DEFAULT-account-4-20261007-1335 jobs (account 4) -- 7 Oct 2026 13:4x UTC, lane orchestrator session_01FwjSioN4d1tryS9vCFN4aN

Lane brief: .claude/briefs/default-lane.md. Cap 60, box 13:37-23:37 UTC 7 Oct. Gate 0a: no SESSION-SWEEP-account-4 row, no wait.
Backlog a: VERIFY-BACKLOG regenerated 13:38 UTC: eckert-1864 N2-AI and N2-AJ (N3, D3, Audit 1 = D12-VP propagation) need the second
adversarial audit (Outreach gate 2); the other eckert rows are N1 or already two-audited; Birago off limits; nla-heinrich N0.
Backlog b: `tools/next_steps.py --hot-only` (exit 0), filtered against ROOM claims < 6 h and 7 Oct briefs: fr7129-villeroy-bongars-1604
READ2-RELABEL (runnable, last touched R12D-VILL 6 Oct), fr15564-mercoeur-1586 shared-scale glyph sheet (the "While waiting" step, untouched
since 3 Oct), eckert-1864 unread "(No 2)" entries pp.86-182 (the account-2 lane's named leftover).
Excluded: Birago, Armstrong, Debosnys; eckert-1862 (B1320-A1 live); folders touched by 7 Oct briefs of other accounts.
Every worker: one job, then stop. First check the named step is still undone (a later ROOM done line or NOTES section may have run it).

## Common rules for every job
- First commands: `git fetch origin && git checkout -B main origin/main`, `python3 tools/room.py --start`, `date -u`, then a ROOM claim line
  with `tools/room.py` naming your job id, folder, cap and box end time, addressed "for LANE DEFAULT-account-4-20261007-1335". If --start
  fails to push from a detached HEAD: `git push origin HEAD:main; git checkout -B main HEAD`.
- Read the folder's NOTES.md tail (Remaining gaps / Escalation / latest dated sections), HYPOTHESES.md and AUDIT.md section list first.
- Good-citizen rule and the CLAUDE.md host table for every request (one request per host at a time, >= 1.5 s apart; stop a host on
  429/403/challenge, one retry after a pause at most). Report request counts per host. Google Books API: `&country=US&key=$GOOGLE_BOOKS_KEY`.
- Rule 3/4/7 as CLAUDE.md. A reading change after AUDIT.md: say so in NOTES.md and flag in ROOM for a verifier.
- Rebase before writing shared files (status.json, PROGRESS.tsv, ROOM.md, HYPOTHESES.md, SECOND-OPINIONS-QUEUE.tsv, JSTOR-QUEUE.tsv); keep
  both facts on conflict. Several sessions may write eckert-1864 at once: commit only your own paths, fetch+rebase right before every push,
  append your own NOTES/AUDIT section rather than editing another worker's. Run `python3 tools/file_shrink_guard.py <every file you
  touched>` before the final push; push with `python3 tools/room.py --push <paths>`.
- Partial targets: update "## Remaining gaps" / "## Escalation" (Verdict line) and pass `python3 tools/gaps_check.py <target>`.
- Words: never "solved", "cracked", "novel", "first", "new" for anything this project did; rule 10 wording only. Never name the owner; never
  print credentials (test presence with `test -n`). Never call AskUserQuestion. Solver jobs: report what was found and where it was not
  found; do not classify novelty.
- Stop at the cap or at 80% of the box, whichever first; do not start a unit that would cross 80% of either. A stop with work half done
  writes what was done and what remains into the folder's files. An Opus session floor is about 1.5; caps below assume it.
- Vision work: crop step mandatory and pasted (`tools/iiif_lines.py --image FILE --out DIR ...` or the `--ark/--canvas` form); read line or
  strip crops, never a full page image; one page (or half page) per subagent call. Price ~1.5 per vision call, reconciliation one more unit.
- Done: one ROOM line `done (<start>-<end> UTC by date -u, brief met|stopped at cap): <result, commit>` "for LANE
  DEFAULT-account-4-20261007-1335", then a five-line final report.

## Wave 1 (spawned 13:4x UTC 7 Oct)
Intake gate 13:4x UTC: `eckert-1864: partial (line 3) -- edition/page or full-text-search citation found within 6 lines` exit 0;
`fr7129-villeroy-bongars-1604: blocked (line 3) -- already terminal, nothing to gate` exit 0;
`fr15564-mercoeur-1586: blocked (line 1) -- already terminal, nothing to gate` exit 0.

### D4-V2AI / D4-V2AJ -- eckert-1864 second adversarial audit of one N3 entry each (verifier, Opus; cap 3.5, box 50 min each)
You are a separate session from every solver of the entry (D12-E1) and from its first auditor (D12-VP). Your one entry: D4-V2AI = N2-AI
(mssEC 19 p.18, pointer 8910, Capt. Wm. T. Howell, A.Q.M., to Brig. Gen. Ingalls, 8 Mar 1864 3.30 PM, water transportation at Yorktown);
D4-V2AJ = N2-AJ (p.18, pointer 8910, Augur to Ingalls, 9 Mar 1864, Grant coming down to the Army of the Potomac; header noon vs time word
Viola = midnight). Follow .claude/briefs/verifier.md and CLAUDE.md "Verifier brief (template)" scoped to that entry, and Outreach gate 2:
read AUDIT.md "## AUDIT (propagation, D12-VP)" section 4 for your entry first, list the families it did NOT cover, and search those at
least: The Papers of Ulysses S. Grant vol. 10 (Jan-May 1864; editorial notes print many telegrams to and about Grant), the recipient's and
sender's papers (Ingalls; Augur's Dept. of Washington letters sent, RG 393 descriptions; Quartermaster records via Meigs), every OR ser. I
vol. 33 and ser. III vol. 4 page for 6-12 Mar 1864 by date and correspondent (not only phrase), the Huntington's own full text across mssEC
(CONTENTdm CISOSEARCHALL, CLAUDE.md host table), IA full text, Google Books, HathiTrust EF where useful, the open-index scholarship pass
(OpenAlex, Semantic Scholar, CORE, CrossRef with the keys) and JSTOR-QUEUE.tsv rows in both families (i) and (ii) (rows never block).
Re-derive the entry with `python3 ciphers/eckert-1864/decode_no2.py --check` (rule 7) and check its tokens on the strip crop (one IIIF
image, regenerable; AUDIT.md line ~1460 gives the 8910 region). Write "## AUDIT 2 (second adversarial, D4-V2A<I|J>)" in AUDIT.md for your
entry only: families searched/unreachable, class (keep N3, raise to N4 only per rule 10, or lower), key `period`, depth line, safe/unsafe
sentence. Update the entry's status.json result row (`audit_status` 'two audits') and PROGRESS.tsv if the entry has a row (rebase first); if
its SECOND-OPINIONS-QUEUE.tsv row quotes a count or class you changed, correct it. Do not decode other entries.

### D4-VILL -- fr7129-villeroy-bongars-1604 READ2-RELABEL (solver, Opus; cap 10, box 100 min)
NOTES.md "## While waiting (27 Sept 2026, WAIT-PASS-A)" first bullet and "## Next step (READ2-RELABEL, 3 Oct 2026)": transcribe f.260r's
cipher lines with the clerk's decipherment in view, sign-aligned by one reader and checked by a second, then run the shared
`tools/interlinear_align.py` on the pairs (not the private kp_key_v3.py) and compare its key with key v3 on the g/9/y/f/u/d families.
Units: re-fetch f.260r native from Gallica (`tools/gallica_folio.py` to confirm the canvas, then `tools/iiif_lines.py --ark ... --canvas
... --region ... --out ciphers/fr7129-villeroy-bongars-1604/sibling/... --debug`, command pasted; check the overlay); about 30 cipher lines
-> reader pass in 2 half-page calls, checker pass in 2 calls, 1 reconciliation unit, then the alignment run (script) = 5 vision units x
~1.5 + floor. Pre-register in a PREREG file (pushed before scoring) the hold-out test: key from f.260 lines, scored on the M9 hold-out the
earlier VB-KEY gate used (0.340 vs 0.70 bar), same metric. Grade per token; key rows C (from the clerk's gloss). If the hold-out passes,
apply the key to f.268 with the target's decode script and `--check`, judge with `tools/judge_plaintext.py` (fr16 and fr17), and report
both; if it fails, log under rule 3's third-attempt clause whether this was a genuinely different instrument. Status stays as rule 5 allows;
update Remaining gaps / Escalation. Report what was found and where it was not found; do not classify novelty.

### D4-MERC -- fr15564-mercoeur-1586 shared-scale glyph sheet vs the Lasry key (solver, Opus; cap 3.5, box 50 min)
NOTES.md "## While waiting (updated MERC151B, 3 Oct 2026)" first step. Disk only (images/f151_*.jpg crops, passes/, ciphertext_draft.tsv,
key image sources/cryptiana/web/GL/GL_BnFfr15564.png, key_lasry_gl.tsv). Build with a script (PIL) one sheet: one exemplar crop per f.151
label (48, from the settled draft's positions on the existing crops; cut boxes by script, no new fetch), rescaled to the key image's stroke
height, beside the key's glyph cells. One vision unit: match each f.151 label to a key glyph or "none", with a confidence. Write
`lasry_cells_f151_sheet.tsv` and rerun the pre-registered cells test exactly as MERC151B (`tools/partial_key_test.py` same flags, plus the
`--shuffle-target 1` control) with the sheet-matched cells; pre-register the rerun (same gate) before scoring. Report both numbers and the
overlap count (how many of 48 labels have a key counterpart). Status stays `blocked` unless rule 5 says otherwise. Report what was found
and where it was not found; do not classify novelty.

### D4-E5 -- eckert-1864, unread "(No 2)" entries of mssEC 19 pages 86-104 (solver, Opus; cap 10, box 100 min)
Entries (no2-candidates.tsv pointer/page/entry_on_page, status empty): 8983/91/0, 8986/94/0, 8986/94/1, 8988/96/0, 8989/97/1, 8996/104/2,
8978/86/1 (long, 66 k2 tokens, last). Method exactly as ECK64-NO2 / D12-E1..E4 (NOTES.md "## ECK64-NO2" and the D12-E sections): 2400 px
IIIF image to scratch, strip crops (command pasted), read with key-no2.md, the volunteer transcription (dmGetItemInfo `transc`) as second
witness, grade per token H/C/I/M, add each as the next N2 block in ciphertext-no2.txt / reading-no2.md after the last existing one (fetch
first; N2-AY was last at 13:0x UTC), mark the candidate row READ D4-E5 (N2-xx). Then per entry: locate it in print (OR ser. I by date and
correspondent, PUSG, IA full text) and record where it was and was not found. `python3 ciphers/eckert-1864/decode_no2.py --check` exit 0
before every push. ~1.2 per entry; stop before an entry that would cross 80% of cap or box. Flag the reading change for a verifier in ROOM.
Report what was found and where it was not found; do not classify novelty.

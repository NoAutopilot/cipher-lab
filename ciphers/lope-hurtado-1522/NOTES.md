# Lope Hurtado de Mendoza (Rome) to Charles V, 1522 — RAH Salazar 9/26, DECODE R9634/R9646/R9649

partial
Check-solved, 26 Sept 2026 (LANE B5 worker bLOP): full text search of the Calendar of State Papers,
Spain vol. II (Bergenroth/Gayangos, archive.org bub_gb_ZoY9AAAAcAAJ) was run by Bourdeau on 2026-09-21
and is re-cited here (not re-run, per intake gate cost discipline): Hurtado's 1522 letters calendared
are nos. 416, 422 (6 June) and 454-455 (26-27 July) only; nothing for Sept-Nov 1522, the window of
R9634/R9646/R9649. Tomokiyo's *Correspondence in Cipher of Imperial Ambassadors Alonso Sanchez and
Juan Manuel (1522)* (Cryptiana, 6 Sept 2025) covers Sánchez's and Juan Manuel's ciphers only, not
Hurtado's (checked by Bourdeau 2026-09-20, no reference to Hurtado; re-checked here by name search,
same result). aaymeloglu/unsolved-ciphers (shallow clone, HEAD at fetch time 26 Sept 2026, deleted
after grep) lists R9634, R9646, R9649 as `Non-decrypted` in `catalogue/decode-records.jsonl` and
separately names two further, unread Hurtado letters at the BNE in `catalogue/bne-ranked.md`
(MSS/18697/29, MSS/20212/27) that neither project has checked. One OpenAlex query
(`search=Lope Hurtado cipher`) returned 11 results, none relevant (security/medical/history-of-empire
papers). Semantic Scholar 429'd twice (key present; one retry after a pause, per the good-citizen
rule) — not answered, not a negative.

## Gate check

```
$ python3 tools/intake_gate_check.py lope-hurtado-1522
lope-hurtado-1522: partial (line 3) -- edition/page or full-text-search citation found within 6 lines
exit=0
```

## Job

LANE B5 job bLOP (`.claude/briefs/runs/2026-09-26-lane-b5-lope-hurtado.md`): apply the 49 code values
Bourdeau recovered from R9644's contemporary clear copy (`key_codes.tsv`, dbourdeau/cyphersolver
`lopehurtado/`) to the three sibling records QUEUE.md G2 flagged "not-attempted" — R9634, R9646,
R9649 — with a random-digit control.

## Step 1: what Bourdeau has actually read, as of the clone (26 Sept 2026)

Cloned `git clone --depth 1 https://github.com/dbourdeau/cyphersolver` at commit
`fc0c9e865d0fae67ca92d19750d2b09ab11972e0` (2026-09-25T18:14:52-05:00), read only `lopehurtado/`,
then deleted the clone (MIT code / CC BY 4.0 text, dbourdeau/cyphersolver, credited here).

QUEUE.md's "not-attempted" for these three records is **stale for two of them**, exactly as the job
brief suspected (it names `read_r9646.md`/`read_r9649.md` already existing):

| record | Bourdeau's own NOTES.md ("Remaining gaps", written ~2026-09-21) | actual state at HEAD (`read_r9646.md`, `read_r9649.md`) |
|---|---|---|
| **R9649** | "not-attempted; listed as uncribbed but no coverage was measured and no reading file exists" | `read_r9649.md`: **97% (86/89 tokens) read**, from **the record's own contemporary clear copy** (f. 268r, "a contemporary clear version of the whole letter," independent of R9644) — the same kind of crib R9644 itself carries. 3 unread tokens (one unmatched pair, no counterpart in the clear). |
| **R9646** | same line | `read_r9646.md`: **84% (99/118 tokens) valued**, no crib of its own — read by applying the accumulated key (1524 `key_1524.tsv` values carried back + `key_codes.tsv` + values won specifically from R9649's crib) to f. 252r. 19 tokens unread (five isolated codes/spelled words with one unsettled sign each); Bourdeau's own notes give no crib for the remainder. |
| **R9634** | same line | **No `read_r9634.md`, no ciphertext transcription anywhere in the repository** (`grep -ril 9634 .` in the clone hits only `NOTES.md`, `profile.json` and `key_1522_from1524_B.tsv`'s header — none is a transcription). Genuinely not-attempted. |

`key_codes.tsv` carries **49 rows graded `confirmed`** (31 more `probable`, kept separate) — this
matches QUEUE.md's "49 confirmed code values" and the job brief's count exactly.

The key point for this job: Bourdeau's R9646/R9649 reads already use **more than the 49-value
R9644-crib key** — R9649 was read from its *own* clear copy (a stronger and independent crib, not
derived from R9644 at all), and R9646 was read with the 49 values **plus** values won from R9649's
own crib and the 1524 key carried back. Re-applying only the 49-value subset to either record, as
the job brief's step 3 specifies, would strictly *underperform* what Bourdeau has already posted —
it cannot add coverage the fuller key does not already have, and it cannot resolve the tokens
Bourdeau's own fuller apparatus already tried and left unread (no crib, isolated codes).

## Step 2 (per brief; this job's actual outcome): nothing is left to test

Per the job brief's own instruction ("Records he has fully read are `found-solved` for this job;
only what he left unread is a test for us. If nothing is left, write that and stop."):

- **R9649**: effectively fully read (97%) by Bourdeau, from the record's own clear copy — `found-solved`
  for this job (found already solved, in an unpublished GitHub repository, not by us; rule 10 class
  is a verifier's call, not stated here).
- **R9646**: substantially read (84%) by Bourdeau with the full accumulated key (a strict superset of
  the 49-value key this job was to apply); the 19 unread tokens have no crib in his notes and are
  not reachable with the 49-value subset either. Nothing this job's test could add.
- **R9634**: no transcription exists in Bourdeau's repository, and this job's cap is disk-and-git only
  (no DECODE login, no image hosts — full-size DECODE images are account-wide blocked regardless, per
  CLAUDE.md's Access playbook). Per the brief: "If a record has no transcription in Bourdeau's
  repository, stop at that record and say so." Stopping here. Making our own transcription from a
  DECODE image is a different, larger job (a breadth spec's first test is one job, not two).

**No key application and no random-digit control were run.** Running the specified test (49-value
key only) against R9646/R9649's own transcriptions would answer a question already answered more
strongly by Bourdeau's fuller reads on file; running it against R9634 is blocked for lack of any
transcription. A control without a target test to compare against is not a result (rule 3).

## What would actually move this target

1. A transcription of R9634 (from an image — DECODE listing confirms it is `Non-decrypted`, 6 pages,
   ff. 14-16, Sept 1522; out of this job's disk/git-only cap) tested against the *full* accumulated
   key (49-value `key_codes.tsv` + the values `key_1522_from1524*.tsv`/R9649 added), not just the
   49-value subset.
2. The two further, wholly unread Hurtado letters aaymeloglu's `bne-ranked.md` names at the BNE
   (MSS/18697/29, "Parcialmente cifrada," 1522; MSS/20212/27, five letters, 1522-1526) — neither
   project has looked at these; a BNE catalogue/digital-collections check is a separate cheap test.
3. The R9646 remainder (19/118 tokens) and R9649 remainder (3/89) need better images, per Bourdeau's
   own "Where the work is now limited" section (DECODE serves ~1700 px/folio, not enough for per-glyph
   discrimination) — not a key problem, an imaging problem, same wall the sanchez1522 and R9656 work
   hit.

## Search log (rule 1)

- Cipher's name / catalogue entry: covered inside Bourdeau's own NOTES.md (search log there, 2026-09-20/21).
- Sender's printed correspondence / calendars: Calendar of State Papers Spain vol. II, full text,
  archive.org `bub_gb_ZoY9AAAAcAAJ`, searched by Bourdeau 2026-09-21 (cited above); not re-run this
  session (cost discipline; the search terms and result are unambiguous and dated).
- Cryptiana / Cipherbrain: Tomokiyo 2025 (Sánchez/Juan Manuel only); no Cipherbrain thread found for
  Hurtado specifically.
- DECODE: `catalogue/decode-records.jsonl` in aaymeloglu's repo (a cached DECODE snapshot) confirms
  R9634, R9646, R9649 all `Non-decrypted`, matching Bourdeau's own table; no fresh DECODE crawl run
  this session (avoided a `decode_list.py` full-status crawl to stay inside the $3 cap; the cached
  snapshot and Bourdeau's own table already agree).
- Solver repositories: dbourdeau/cyphersolver `lopehurtado/` (this job); aaymeloglu/unsolved-ciphers
  shallow-cloned, grepped for "hurtado" (case-insensitive) across the whole repo, deleted after.
- OpenAlex: `works?search=Lope Hurtado cipher` (11 results, none relevant). Semantic Scholar: 429,
  twice, key present — not a negative, just unanswered.

Per rule 10, this reports what was found and where it was not; it does not classify novelty.

## Credit

Bourdeau, dbourdeau/cyphersolver, `lopehurtado/` folder, commit `fc0c9e865d0fae67ca92d19750d2b09ab11972e0`
(2026-09-25), CC BY 4.0 text / MIT code, read 26 Sept 2026. Aymeloglu, aaymeloglu/unsolved-ciphers
(no licence — cited, not copied), `catalogue/decode-records.jsonl` and `catalogue/bne-ranked.md`, read
26 Sept 2026.

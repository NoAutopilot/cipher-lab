open

KH4-A (LANE KH-4, account 4), 7 Oct 2026, 17:42-17:55 UTC by `date -u`. Brief `.claude/briefs/runs/2026-10-07-acct4-kh4-workers.md`
(key hunt: unread siblings for held keys). **Not yet check-solved.** Before any deep work (reconciliation from the image,
key repair, word-level reading), run the check-solved workflow (`.claude/briefs/check-solved.md`, with its Premise check)
and `tools/intake_gate_check.py ceppo-nevers-fr4702-f36`; nothing below is a check-solved verdict. Rule 10: no class here.

# BnF fr.4702 f.36r, Cesare Ceppo to the Duke of Nevers (Ludovico Gonzaga), undated [c.1570-71], Ceppo-Nevers cipher

## Source

- BnF Français 4702, item 19. The BnF dépouillement (snapshot
  `ciphers/guazzo-nevers-fr4688-1571-72/catalogue/bnf-aem-cc57752b-fr4702-2026-10-02.txt`, line 148) reads: "Fol. 36 et 37 •
  19-20 Chiffres de CESARE CEPPO au duc de Nevers. Le second est accompagné du déchiffrement en italien." So f.37 carries
  the period decipherment and f.36 does not.
- Gallica ark:/12148/btv1b530546654. `tools/gallica_folio.py` gives one constant offset (k=14). Canvas f85 is labelled '36r'
  (4121x5836) and canvas f86 '36v'. Both were viewed at 1000 px: f.36r is a pasted slip of 20 lines of cipher with no
  prose and no gloss, and f.36v is blank.
- Tomokiyo, nevers.htm, section BnF fr.4702 (local mirror, cp932), verbatim: "Fols.36-37 are letters from Cesare Ceppo to
  the Duke of Nevers. One has interlined deciphering, which allows reconstruction of the cipher as follows (called
  'Ceppo-Nevers Cipher' herein). This in turn allows reading of the undeciphered letter 'io sono avisato via di Milano et
  ...' but not quite." He prints only that incipit. No fuller reading of his was found on disk.
- Key: `ciphers/ceppo-nevers-fr3251-1570s/keys/key_ceppo_nevers.tsv` (KEY-OFFICES.tsv row 61), used through that folder's
  value-blind sign sheet and map (`harvest/sign_sheet_blind.png`, `harvest/sign_id_map.json`, 55 cells).

## Searched (7 Oct 2026, KH4-A)

- Fresh shallow clones of dbourdeau/cyphersolver (1fb3c46) and aaymeloglu/unsolved-ciphers (d2800bb) were grepped for
  `4702|ceppo|btv1b530546654`. There was no fr.4702 target. Bourdeau's `targets/birago` is fr.3251 f.119, and his
  `gallica_sweep` hits are notice ids only.
- DECODE local mirrors `sources/decode/*.tsv` were grepped the same way. The only hit is record id 4702, a 1715 Marburg key,
  which is unrelated.
- This repository: there is no folder for fr.4702 f.36. BIRAGO-POOL.tsv lists it as "key source", and the
  ceppo-nevers-fr3251-1570s premise check names it as the "not quite" letter, with no work done on it.
- Not searched yet: web search, printed Nevers editions (Gomberville 1665), Italian editions of Ceppo, the Cipherbrain
  and Cryptiana comment threads. These are the check-solved steps.

## Images and transcription

Command (pasted, rule: crop before any subagent call):
`python3 tools/iiif_lines.py --ark btv1b530546654 --canvas 85 --region 380,1500,3150,2650 --out <scratch>/f36/images --debug`.
It made 1 Gallica request and gave 20 lines x 2 segments. The crops, the region source and `images/manifest.json` are in
`images/`. Note that the s1/s2 segments **overlap**: both readers found this and merged the shared run, but the brief
copied from the fr.3251 job said they do not.

Two value-blind Sonnet passes, one call each (`passes/blind_pass_brief.md`; neither reader saw the key, the map or the
other pass; KH4-A checked reader B's transcript for any access to passA.tsv or reader A's helper and found none). Reader A
read 645 signs and reader B 643. `tools/reconcile_passes.py` (wide format, `passes/wideA.tsv` and `passes/wideB.tsv`)
gives **79.1% agreement (514/650 columns), with 136 split columns** (`passes/disagreements.tsv`). Those splits are not
reconciled from the image. In `ciphertext.txt` and `ciphertext_agreed.tsv` they are '?'.
(The first run of `reconcile_passes.py` on the long-format files, header `passage pos sign_id`, misread the sign column
and reported a meaningless 99.1%. A pass file for that tool should use `line pos sign`, or the wide format.)

## Decode and controls (rule 3)

The decode is `decode.py` (rule 7: `python3 decode.py --check` exits non-zero if reading*.txt are stale). It imports
`decode()` from `../ceppo-nevers-fr3251-1570s/harvest/decode_control.py`. The control is that script's shuffled-key test:
the value column of the same 55-cell map is permuted over 200 shuffles (seed 1), the score is the mean log10 4-gram score
per letter on it16dip, and the score depends on the key, so a shuffled key can change it. The power control enciphers 20
it16dip windows of the same passage lengths with the same key at 21% sign error (the measured pass disagreement) and runs
the same test on them.

| sequence | signs | real key | shuffle mean | shuffle p95 | shuffle max | rank | z | power control (rank 1) |
|---|---|---|---|---|---|---|---|---|
| agreed only (splits '?') | 650 | -1.357 | -2.065 | -1.826 | -1.700 | 1/201 | 4.84 | 20/20, z median 7.14 |
| pass A alone | 645 | -1.463 | -2.069 | -1.844 | -1.738 | 1/201 | 5.46 | 20/20, z median 10.40 |
| pass B alone | 643 | -1.435 | -2.063 | -1.865 | -1.769 | 1/201 | 5.36 | 20/20, z median 10.52 |

**Key-level control passed**: the held Ceppo-Nevers key ranks first against every shuffle, on every transcription.

Judge (`tools/judge_plaintext.py`, a spec with only `language: it16dip`, `<scratch>/spec_f36.json`):

```
passA: FAIL language: score=-1.469, null_p99=-1.769, real_p05=-0.907, real_median=-0.828, mode=both, N=628
passB: FAIL language: score=-1.441, null_p99=-1.78, real_p05=-0.898, real_median=-0.825, mode=both, N=640
```

Both decodes are FAIL against real Italian prose and above the letter-shuffled null. This is the same shape as the fr.3251
Ceppo letters (the key identifies the leaf, but the text is not yet prose). it16dip is diplomatic Italian of the period.
Whether it is register-matched for a 1570 agent's letter has not been checked.

## Reading (grades)

`reading.txt` (agreed signs only) has **514 letter tokens, all M** (machine transcription with a FAIL judge), and **136
I** (the '?' splits). H 0, C 0, S 0. This is a cryptanalytic-control result on a key reconstructed from a period
decipherment, not a reading. Italian fragments are visible but no word is endorsed: L19 "...se esforsar...", L12
"...piu si que...", L15 "...esadiqua...", L18 "quest...". The decode does not match Tomokiyo's printed incipit
"io sono avisato via di Milano" at L01 (L01 decodes "__itso_t__ui_attn_iaesi..."). This is unexplained. Possible causes
are leaf order, a different start on the slip, or sign confusions. Settle it at check-solved or reconciliation, not here.

## Next step (named)

1. Run check-solved with its Premise check, then `tools/intake_gate_check.py`.
2. If open: reconcile the 136 splits from the crops as one priced unit (Usage 6), using the f.37 period gloss (same
   writer, same key) as the known-answer witness for sign confusions.
3. Re-run `decode.py`, the control and the judge.

Requests this job: gallica.bnf.fr 4 (manifest 1, two 1000-px views, 1 native region); github.com 2 shallow clones (read
only). Subagents: 2 Sonnet blind passes.

## CEPPO-4702 (account 4): intake gate failed, no deep work done (08 Oct 2026, 13:38 UTC by date -u)

The brief (`.claude/briefs/runs/2026-10-08-acct3-sibs-ledger3.md`, section CEPPO-4702) asked for the 136 splits to be reconciled, then a re-decode and the judge.
The intake gate was run first, as required:
`python3 tools/intake_gate_check.py ceppo-nevers-fr4702-f36` printed "open (line 1) names an edition not read ('unread' within 6
lines) -- CLAUDE.md's Pipeline intake gate says this must read `blocked` instead" and exited 1. This folder still has no
check-solved verdict and no "## Premise check". The edition and threads not yet read are Gomberville 1665, the Italian Ceppo
editions, web search and the Cipherbrain/Cryptiana threads (see "Searched" above). SIBS-PREMISE (8 Oct 2026) read only the disk, so it is not a check-solved verdict.
No reconciliation, decode or judge run was done, and no file other than this section changed. The WORK-QUEUE row is bounced.
Next: run the check-solved workflow with its Premise check on this folder (~$2-3). Then re-queue CEPPO-4702 unchanged.

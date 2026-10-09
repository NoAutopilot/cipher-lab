# RESULTS TXE-R: fr.3252 f.117r re-transcribed with today's pipeline, decoded under the committed config (9 Oct 2026, 08:26-08:4x UTC by date -u)

LANE TX-ENGINEER round 3, Amendment 2 guard 3; worker account 4, Opus 5.5. Brief `.claude/briefs/runs/2026-10-09-account4-txe-r.md`,
PREREG `PREREG-TXE-R.md` (pushed 508cf4417 before any crop or read). Disk only, 0 hosts.

**Verdict: no licensed change.** err_2reader 0.134 (was 0.25 for f.117r's own earlier pair; the brief's 0.56 is f.47r L01-04, NOTES.md:135-138).
S tokens 207 vs the committed 190 (+17 net: 32 aligned positions newly S, 15 no longer S), M 50, U 23. Power: licensed by the
D2-B117KAPC curve (0.134 <= 0.183; the curve reads 18/20 at 0.126 and 16/20 at 0.183, seed 1). Judge FAIL -1.234 vs the committed
reading's -1.224: 0.010 worse, so gate (d) fails and the +17 is **not** reported as "the key now licenses N more tokens at grade S".
The committed reading, RD7 and the D2-B117KAPC grades (S 217 / M 36 / U 26) stay as they are.

## Gates (pasted)
    $ python3 tools/intake_gate_check.py birago-fr3252-1571-72
    birago-fr3252-1571-72: partial (line 1) -- edition/page or full-text-search citation found within 6 lines
    $ python3 tools/prior_work.py birago-fr3252-1571-72 --item f117r --step-type transcribe --offline
    prior_work.py: error: item 'f117r' is not a row of ciphers/birago-fr3252-1571-72/items.tsv at origin/main ...
    $ python3 tools/prior_work.py birago-fr3252-1571-72 --item-spec 'shelfmark=BnF fr.3252;folio=117r;date=1572-03-13;sender=Birago;recipient=Nevers' --step-type transcribe --offline
      holds: specific 19 (KNOWN 1, LEAD 18); generic 2 (UNCHECKED-NET 2)
      verdict plaintext: KNOWN      (the one KNOWN is the f.36-37 clerk gloss, NOTES.md:64 -- another leaf)
      verdict step: LEAD            (our own earlier work on this leaf, which this job re-does by design)
    exit 2: KNOWN, no consumer     (warn-first; not a block)

## 1. Crops (`images/f117_txer/`, README there)
    python3 tools/iiif_lines.py --image ciphers/birago-fr3252-1571-72/images/f117/src_ark_12148_btv1b9060232m_f118_4380_1400_3150_1300.jpg \
      --out ciphers/birago-fr3252-1571-72/images/f117_txer --prefix f117r --centres 103,223,347,462,580,702,815,944,1062,1210 \
      --max-width 1100 --overlap 60 --band-extent 0.1 --mask-neighbours --overlap-note --note-scale 2 --follow-slope 300 \
      --only-lines 1,2,3,4,5,6,7,8,9 --check-boxes ciphers/nevers-birago-fr3251-1572/atlas/signs.tsv --check-page f117r --debug
    + L10 flat: --region 0,0,1170,1300 --max-width 1240 --only-lines 10  (one crop)
Box check: the flat-band first cut, ink rule, cut 19 (6.5%) / admitted 79 (27.1%); the overlay showed every line falling to the right
(+33 to +125 px over the region, pitch 120) and L07-L09 leaving their bands, so `--follow-slope` went on L01-L09 (box rule: cut 21 (7.2%),
admitted 50 (17.2%)). L10's own slope fit was -0.022 (the tracker jumped onto L09's tail) and a flat full-width L10 band admitted
L09's sloped tail into s2/s3, so L10 is one flat crop of the left 1170 px. The atlas has 9 lines on f117r against our 10 bands, so its
per-line figures for L09/L10 are a line-assignment mismatch, not a measured cut. Crops note (generated): overlap 75 native px, about 1 sign.

## 2. Passes (Opus 5.5, value-blind, one call each)
Reader brief `txer/blind_pass_brief_txer.md` = the folder's `blind_pass_brief_f117.md` with the hand-typed overlap sentence replaced by
the generated crops note. Task text, reader A (B identical but "L10 first ... down to L01", output passB.tsv):
> Blind transcription pass A. Read and follow exactly the brief at .../txer/blind_pass_brief_txer.md. Open ONLY that brief, the sign
> sheet .../harvest/f117/sign_sheet_blind_1572.png, and these crops in .../images/f117_txer/lines2x/ : f117r_L01_s1.jpg, ... L09 s1-s3,
> then f117r_L10.jpg. Read the lines in order L01 to L10. Do not open any other file. Write exactly one TSV to .../txer/passA.tsv in the
> brief's format, and use the passage ids L01..L10. Do not run git. Report as the brief says.

passA 278 signs (26 X_), passB 280 (30 X_); committed 64cedb398 / cf61fde59 before reconciling.

## 3. Reconcile + adjudication
`reconcile_passes.py` does not recognise the reader brief's `passage/sign_id` header (it aligned the pos column, "99.3%"); the passes were
re-headed to `line pos sign conf alt note` (`txer/pass?_long.tsv`, content unchanged) and re-run:

    $ python3 tools/reconcile_passes.py passA_long.tsv passB_long.tsv --crops ../../../images/f117_txer --out-dir rec
    lines 10  signs A 278  B 280  agree 245/283 = 86.6%  (nw)
    agreed-H 158  agreed-uncertain 87  disagree 38

**(a) err_2reader = 38/283 = 0.134** (earlier f.117r pair, two Sonnet readers, NEVBIR-3252-B: 0.25). Splits are class pairs: T76/T66 x10,
T81/X_NEW x6, X_S/X_NEW x4, T51/T95 x3, T60/T86 x2, T18/T98/T36 x3, one reader only (a sign the other did not see) x8.
One Sonnet third-reader call (`txer/adjudicate_brief.md`, queue `txer/adjudicate_queue.tsv`: the 38 splits + 7 both-L rows, agreed
neighbours as landmarks, crops + sheet only): reader1 19, reader2 20, other 3, none 3, unsure 0. `txer/build_ciphertext.py` applies the
PREREG conf rule -> `ciphertext_f117_txer.tsv`: 280 signs, conf H 226 / M 51 / L 3.

## 4. Decode (`decode_txer.json` = decode_apply.json job 1, ciphertext and outputs changed only)
    $ python3 tools/decode_key.py ciphers/nevers-birago-fr3251-1572 --config ciphers/birago-fr3252-1571-72/harvest/f117/decode_txer.json
    ../birago-fr3252-1571-72/harvest/f117/ciphertext_f117_txer.tsv: tokens 280: M 50, S 207, U 23
    (secondary, no exceptions file: tokens 280: M 34, S 223, U 23)
```
f117 L01 | ···mguilam·uelguen·psenua·arde
f117 L02 | laenintentiondeconuenibaued··
f117 L03 | poursuoiblegouebneaentde···pitb
f117 L04 | ceguisestperso·eguiserendroit
f117 L05 | ·susfacile[et]s·indeletertoutesies
f117 L06 | sionsdestre·lusenpsbeilespeines
f117 L07 | guec·deuantieuoussu·sieda·deb
f117 L08 | [et]·auorisercesta·airesilenest
f117 L09 | ·esoing[et]sisuoussemblietantguis
f117 L10 | reosise·[quello][quello]··
```
Exceptions check (the PREREG's shift caveat): only L10 changes length (11 -> 12, one sign inserted after pos 8), so all 31 exception rows
land on the same sign position; 22 of 31 carry the value the new readers' sign has in the key; the other 9 are BIR-APPLY's owner-sorter
conflicts (8 M, one S at L05.9) which the exceptions hold by design. The primary (with exceptions, S 207) is the smaller S count and the
one carried to the gates.

**(b) grades vs the committed RD7 (S 190 / M 63 / U 26), aligned per line (`txer/compare_grades.py`, rows in `txer/changes_vs_rd7.tsv`):**
M->S 29, U->S 2, (new)->S 1 = 32 newly S; S->M 15 (eight T66=e rows the readers split T76/T66 and the third reader settled -> M,
one T66 -> T98, one T83 r -> T81 b; and T45 e, T95 s, T25 i, T92 s, T96 i at conf M); S->S 175, M->M 32, U->U 21; value changed at the same grade 8.
Newly S, by sign: T83=r 10, T60=n 4, T45=e 3, T76=n 3, T85=a 2, T86=e 2 (was T60 n), T90=p 2 (was T45 e), T92=s 2, T51=l, T18=d, T27=t, T57=s.
Net: **S 207 = 190 + 17**; against the current D2-B117KAPC grades (S 217) it is 10 fewer.

**(c) power:** err_2reader 0.134 <= 0.183 -> licensed on the D2-B117KAPC curve (HYPOTHESES D2-B117KAPC, seed 1: 18/20 at 0.126,
16/20 at 0.183, 6/20 at 0.25). Caveat: err_2reader is a disagreement, not a measured error; KAPC's 0.126 / 0.183 were known-answer errors.

**(d) judge** (letters only, word codes dropped; the committed line reproduces at -1.224, N=246 with this extraction):

    $ python3 tools/judge_plaintext.py specs/birago-fr3252-f117.json --file <reading_f117_txer letters>
    FAIL language: score=-1.234, null_p99=-1.853, real_p05=-0.898, real_median=-0.783, mode=both, N=251
    (no-exceptions decode: FAIL score=-1.329, N=252)

Gate (d) "not worse than -1.224": -1.234 FAILS by 0.010. **No licensed change.** No grade above S was written; the new reading is not
posted as "reading ready".

## Calls and cost
Vision calls: crops 0, passes 2 (Opus), adjudication 1 (Sonnet). Hosts 0. Cost: read by the lane from get_session.

## Follow-up (one line, not done)
The T76/T66 class split is now the largest reader disagreement on this hand (10 of 38) and the main source of the 15 S->M losses (9 of them T66); a
known-answer T76/T66 tile check on no.87 (clerk sheet) would say which way the third reader should lean before a re-run.

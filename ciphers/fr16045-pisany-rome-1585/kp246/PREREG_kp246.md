# PREREG kp246 -- fr16045 f.246r (second 17 Sept 1586 letter, opening page) half-page passes vs Colbert 16 pt II pp.52-55 (PIS-246, 13 Oct 2026)

Written and pushed before any blind pass of f.246r and before any decode. Same instrument as kp86g (PIS1-247, f.247r):
kp86d/kp86d.py unchanged through a thin wrapper, kp246/kp246.py = kp86g/kp86g.py with file paths changed only. Nothing in the
statistic, nulls, seeds, arms, control or gate changes; only the page, its copy span and the reader-call unit (one half-page per
call, per the PIS-246 brief and the lane's common rules, instead of one line per call).

Material.
- Cipher: fr.16045 f.246r = btv1b9060906j canvas 504 (3922 x 5775, openapi.bnf.fr info.json). Native region 900,1220,2850,4300
  fetched once from openapi.bnf.fr (images/scratch/src_c504.jpg, untracked; re-fetch
  `https://openapi.bnf.fr/iiif/image/v3/ark:/12148/btv1b9060906j/f504/900,1220,2850,4300/max/0/default.jpg`).
  The page is all cipher: **22 lines** (the notes' "~26" was an estimate), opened by "Sire" in clear left of line 1 (outside the
  region), a small interlinear "la" above the end of line 1 (later hand; readers skip it). No clear words inside the block:
  --inms not used. Left margin (native 60,1550,420,1200) viewed: faint show-through and stray strokes only, no gloss.
- Crops: `python3 tools/iiif_lines.py --image ciphers/fr16045-pisany-rome-1585/images/scratch/src_c504.jpg --out ciphers/fr16045-pisany-rome-1585/images/scratch --prefix f246rL --debug --max-width 1600 --overlap 100 --centres 120,293,478,632,784,958,1127,1291,1467,1636,1796,1960,2147,2332,2498,2668,2827,3008,3187,3345,3517,3670`
  (fixed-y for every band: a first run with --follow-slope 400 --slope-local --slope-margin 20 gave unstable fits on L03, L05,
  L06, L11, L12 -- drifts of -226 to +182 px on a page whose stable bands drift under 20 px -- so all were re-cut without slope).
  Centres from the row ink profile (6th-percentile threshold, 41-row box, local maxima) plus L01 set by eye. Montages of all
  44 crops checked by eye: each crop's middle row holds its own line. Crops untracked (lane rule: no image file in git);
  the command above regenerates them from the re-fetched region.
- Clear copy (primary known answer): kp246/colbert_f246r.txt = Colbert 16 pt II p.52 l.15 "Disnant hier auec moy" to p.55 l.3
  "Il m'a dict qu'il demanderoit" (where f.247r's decode begins), read by this worker from c445 and c446 at 1400 px
  (openapi.bnf.fr). Doubtful words: "confiroit", "feu nier", "l'eust prié". The span covers f.246r AND f.246v; nw_score is
  semi-global with free leading/trailing gaps on the clear side, as on every earlier page, so the unread f.246v part is free.
- Keys: arm A key86.tsv as at HEAD; arm B key86 + RUN4-PIS1 remap (T31->o, T45->u, T47->f, T57->n), beside A only.

Transcription: two blind Sonnet readers (A, B), tx246/PASS_BRIEF246.md (= tx86g's brief with the unit changed to a half page),
ONE subagent call per half page per reader (L01-L11, L12-L22; 2 + 2 = 4 calls), each given only those lines' crop paths
(s1, s2) and tx86g/SIGNSHEET86.png. Replies verbatim to tx246/lines/{A,B}_h{1,2}.txt, assembled to tx246/passA.tsv, passB.tsv.
A reply that is not label rows is re-asked once; the second reply stands.
Reconciliation (mechanical, no vision): `python3 tools/reconcile_passes.py tx246/passA.tsv tx246/passB.tsv --out-dir tx246` then
`python3 kp86d/reconcile_d.py tx246` (RUN3 shape rules, unchanged; output renamed tx246/ciphertext_f246r.tsv).
err_2reader = 1 - agree share from reconcile_passes.py.

Test: `python3 kp246/kp246.py --err <measured err_2reader>` = kp86d/kp86d.py UNCHANGED (nw_score; key-shuffle 1000 and
order-shuffle 1000 nulls, p99; seeds as kp86d; positive control at the measured err, 5 seeds, 200/200 nulls, pass >= 4/5)
-> kp246/kp246_result.json.
Gate per arm (as kp86d/e/f/g): PASS if the reconciled target > p99 of both nulls AND that arm's control passes; control fails ->
NON-TEST; target fails at err > 0.10 with the control passing -> FAIL at that e (not a refutation of the table).
Blind A and B scored too (not gating).

Grades (rule 4): only if arm A is a licensed PASS, decoded letters aligned identically to the copy are C, the rest M; T31 tokens
M (HYPOTHESES.md data conflict) -- via kp246/t31_grades_246.py (kp86e/t31_grades.py with paths changed). If NON-TEST or FAIL,
every token stays M. `tools/decode_key.py ... --check`; judge pasted.

T40 tally (descriptive, no gate): `python3 d1apis/t40_f246r.py` runs d1apis/t40_align.py's witness() unchanged on f.246r and
writes the f.246r rows beside the committed seven-page table (D1A-PIS's power control failed, 0/50, so no T40 gate is run and
key86.tsv is not touched). No parameter changes after the first run.

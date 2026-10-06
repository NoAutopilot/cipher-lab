# PREREG -- R14-RJM9526, rah-juan-manuel-1521: R9526 retest with f.150's clerk lines and settled splits
Written 6 Oct 2026, clock 15:4x UTC (`date -u` 15:39 at the start of writing); committed and pushed BEFORE the f.150 read or the
look-alike re-read has returned and BEFORE any scored run. Brief: .claude/briefs/runs/2026-10-06-account2-run14-jobs.md job R14-RJM9526.
The second attempt on this page (the first: R12-RJM147, witness/PREREG_f147.md, calibration 0.491 = 52/106 < 0.50, non-test).

## Can the calibration reach its gate? (answered before anything is read)
Gate 0 is unchanged: share of nomenclator code tokens whose aligned chunk equals their own table word >= 0.50. R12-RJM147 missed it
by one code word (52/106; 53 needed). Per pass line (passes/align_f147_codoin.tsv): lines 2-3 already 13/13; lines 4-8 15/35; lines
9-18 24/58. The f.150 clerk's decipherment (P2 right, its last 7 crop lines, located by eye at low resolution before any pass) runs
from "// Los de genova dizen rehusan ..." to "... puede venir con seguridad", i.e. over pass lines 2-8 (f.147 L08-L09 + f.147v
L01-L05, where f.147v L05 carries the clear "puede venir"). So 48 code tokens (28 hit, 20 missed) sit where the gloss text changes,
and the split settlement changes cipher tokens on every line. One more hit (or a smaller code denominator) reaches the gate, so it is
not out of reach by arithmetic; the run goes ahead. If the code-token denominator changes (settled splits that are table codes),
the gate is the same share on the new denominator.

## Inputs (fixed now)
1. f.150 read: one Sonnet pass over 7 line crops (tools/iiif_lines.py, P2 region 1990,1690,1480,500), written to
   passes/f150_clerk.tsv. Gloss rule: the clerk's text from the first word after "//" ("Los") to the last word of crop L07, spelling as
   the reader gives it, with only these normalisations: "q"/"q~"/"que" abbreviations -> "que"; "v. md."/"V. M." -> "V. M." (as the
   print); "S." / "Sd." -> "santidad"; numerals as words ("ij" / "2" / "dos" -> as written, lettered). Words the reader marks
   illegible ("[?]") are dropped. Then the print (passes/gloss_codoin26_p49.tsv) continues from the first print word after the print's
   counterpart of the clerk's last legible word; the counterpart is the first print occurrence, at or after "puede venir", of that word
   (fold accents/case); if no print word matches within 6 words after "venir", the join is at "seguridad" (print) and the rest of the
   print follows. The f.150 text replaces the print's text up to the join; nothing else in the print changes.
2. Splits: tools/lookalike_pass.py windows (85 split tiles, lookalike/f147_tiles.tsv from scripts/lookalike_tiles147.py, 15
   montages, label hidden), one blind Sonnet re-read (lookalike/f147_reread.tsv), then `lookalike_pass.py reconcile` unchanged ->
   lookalike/f147_passD.tsv. A tile settled 2-of-3 replaces its '~' in the reconciled stream with the settled label; an unsettled tile
   stays '~'. A settled label then goes through test1.to_pair unchanged (symbol -> scored symbol; table code -> code token; bracketed
   clear text -> clear words; anything else -> miss). The 2-of-3 residual is reported as agreement, not error.
3. Aligner, spans, keys, statistic, control and gates: identical to PREREG_f147.md (tools/interlinear_align.py settings, PRIMARY
   lines 2-18 gated, SENSITIVITY line 1 tail reported only; Gate 0 >= 0.50; per key S > control max of 200 permuted-value keys AND
   S >= 0.24; keys alphabet.tsv and key_tomokiyo_alpha.tsv). Script: scripts/test147b.py imports test147.py's run() unchanged.

## Runs
- GATED run: both changes together (f.150 gloss + settled splits), primary span. Gate 0 decides whether the keys are scored.
- Reported only (diagnostics, license nothing): gloss change alone, splits change alone.
- If Gate 0 FAILs again: R9526 vs the print is logged "untestable by this alignment at this reader error" (CLAUDE.md rule 3,
  same-instrument re-attempt clause); no third attempt on the same aligner and gate; the next step needs a different instrument or
  the owner's sort (ASKS 138). No looser gate.
- A key PASS licenses no key, grade or reading change in this job; it goes to a verifier.

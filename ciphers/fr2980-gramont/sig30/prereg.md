# SIG-GRA30 pre-registration (8 Oct 2026, account 1, for LANE SIG-1)

Committed before any reader pass, before any crop of the chosen lines was opened by this worker.
Brief: .claude/briefs/runs/2026-10-08-acct1-sig1-jobs.md, section SIG-GRA30.

## Lines (chosen by script, `sig30/linescore.py --rank` -> `sig30/rank.tsv`)
Ranked on the current extended reading (reading_f30_extended_tokens.tsv) by rank(M+U tokens) + rank(fr16 bits/char,
test_f30r_top.py's linescore scorer); f30r L01, L02, L11, L12 excluded. Worst 8:
f30r_L06, f30r_L09, f30r_L05, f30r_L03, f30r_L23, f30v_L06, f30r_L25, f30r_L24.
Out of scope inside these lines: positions holding HASH, TRI, INF, B8, ev, CROSSp/CROSS2/CROSSo, and the f30r_L05
ehx position named in Remaining gaps -- no change is applied there whatever the passes say.

## Control (known answer, same hand, same protocol)
fr.3040 f.18r L11 and L15 = block rows f18rB_L01 and f18rB_L05 (chosen by script: the two rows whose N9-GRA4
per-row agreement is closest to the block's 0.812; `sig30/ctl_score.py n9gra4/recon.tsv`). On file (N9-GRA4
recon.tsv, whole-block alignment to N8-GRA2's S1 with N8-GRA2's registered functions): L01 25/31, L05 21/26,
pooled **46/57 = 0.807**.
Protocol on the control: the same two blind Sonnet passes as the target (one call per row = its two half-crops,
same brief text, same atlas), reconciled by this worker from the crops without opening the print or key.tsv;
the two rows are substituted into n9gra4/recon.tsv and the whole block re-aligned (`sig30/ctl_score.py
n9gra4/recon.tsv --replace sig30/ctl_recon.tsv`).
**Gate: pooled keyed-sign agreement on the two rows >= 0.757 (0.807 - 0.05).** Below it: stop, no f.30 change is
applied, the protocol is not better than what is on file. (Reader `zb` on fr.3040 is relabelled `zh` by
relabel_zh.py's registered rule before scoring.)

## Reader protocol
Sonnet subagent (claude-sonnet-5-5), one call per line holding that line's two half-crops (images/crops_f30/<L>a.jpg,
<L>b.jpg; images/fr3040_f18/<row>_a.jpg, _b.jpg), the atlas images atlas/atlas_f29.png and atlas/atlas_f30add.png
(the codebook ciphertext_f30.tsv and the fr.3040 recon files use; legend_sheet.png carries key-image k-codes with no
mapping to these codes, so it is not used -- deviation from the brief's wording, logged here), and a text list of the
reconciler's extra codes (reconciliation_f30.md classes 3-6). Two independent passes per line (A, B); neither sees the
other, the current ciphertext, key.tsv, a reading or the print.

## Change rule (target)
Passes aligned to ciphertext_f30.tsv per line (difflib on base codes). Reader codes are compared through registered
equivalence families (a reader code inside the current code's family is agreement, not a change):
eh~{eh,ehx,re,c}; 2~{2,zb,n,nq}; n6~{n6,nq}; D~{D,nq}; br~{br,nq}; r/nr~{nr}; sq~{BOX}; 5~{5,Sx}; sl~{sl,Sx,ST};
ST~{ST,sl}; yt~{yt,v}; oi~{oi,ev}; dl~{dl,lz}; A2~{A2,lz}; INF~{INF,B8}; z~{z,zb,z3}; CROSS~{CROSSp,CROSS2,CROSSo};
a trailing '?' is stripped. A sign changes only where (a) both passes agree on a code outside the current code's
family and this worker's crop check does not contradict it, or (b) the passes split and this worker's crop check
settles it against the current sign. Insertions/deletions follow the same rule. Every change is logged in
sig30/changes.tsv (line, position, before, after, evidence). Applied through ciphertext_f30.tsv only.

## Scoring (target)
Statistic: mean over the 8 lines of fr16 bits/char (sig30/linescore.py, unchanged after this commit), before minus
after (positive = gain). Null: 200 draws, each logged change relocated to a uniformly random position of its own line
(out-of-scope positions excluded), same new sign and same operation, scored the same way; seed 20261008.
**A real gain <= the null's p95 is "no change", not a gain.** Rule 7: decode.py --check and tools/decode_key.py --check
exit 0 after the change.

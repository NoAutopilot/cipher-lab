# PREREG D4-COST, 7 Oct 2026 (written and pushed before any crop is cut or read by a reader, and before any score)

Target: R1167 (b.2/20 no.44, Strigonio Dec 1491) cipher P1 vs its clear copy P5-P6. Images: one DECODE browser login 14:03 UTC,
R1167 P1/P2/P3/P5/P6 and R1165 P1, sha1 = images_manifest.tsv, scratch only, nothing committed. This worker has looked at P1 and P5 at
contact scale (864 px) to place crops; nothing was transcribed at that scale.

Step 1, completeness (reported, licenses nothing, not a gate): opening, date line, the clear words left in the cipher letter and their
order in the copy, at contact/line-crop scale by this worker.

Step 2, alignment of short anchored spans. Spans are cut at clear words the cipher letter itself leaves in clear and the copy also has
(e.g. P1 "V.ra Ex.tia" ... "hora li significo per questa come"), so each span is a few cipher lines against one clause of the copy.
Readers: two blind Sonnet calls over the same line crops of P1 (pass A top-down, pass B bottom-up), shapes from align/labels.tsv and the
RUN3-COSK2 dash convention, no value, no clear copy, no key. The clear span is read by this worker from the copy's line crops (it is the
plaintext source, grade C by construction; abbreviations expanded only where the copy writes them out elsewhere; spans with
unresolved abbreviations are dropped before scoring).
Statistic (per pass, per span, then pooled): global alignment (Needleman-Wunsch) of the pass's sign string (Z, W kept as single signs; a
"?" kept as a wildcard) against the clear span's letters (spaces/punctuation removed), score +2 when a sign's C value in
align/key_n9cos2.tsv equals the letter, -1 when it differs, 0 for a sign with no C value, gap -1. Real = share of C-valued sign tokens
aligned to their own letter. Null: the same alignment against the clear span's letters shuffled within the span (same composition,
order destroyed -- the statistic depends on order, so the control can fail differently), 20 seeds.
Gate per pass: pooled real >= shuffle p95 + 0.20 and >= 4 C-valued tokens per span on average. A pass that fails licenses nothing.
New sign values (only from passes that cleared the gate; key changes only this way): a sign without a C value goes to C only if
(a) both passes cleared the gate, (b) the sign is aligned to a letter >= 3 times in each pass, (c) the modal letter is the same in both
passes with share >= 0.6 in each, and (d) held-out: the modal letter also occurs for that sign in at least two different spans (a value
seen in one span only stays M). Otherwise M. Existing C values are not changed; a C value whose agreement falls below 0.5 in both passes
is reported (a flag for a verifier), not demoted here.
Reconciliation by this worker (copy in view) is reported and licenses M at most.
Units: 2 Sonnet reader calls (~1.5 each) + 1 reconciliation/scoring unit; floor ~1.5; cap 6.

# LANE-POOLS2 PIS-T -- fr16045-pisany-rome-1585: spec + first cheap test with a matched control (account 1), 4 Oct 2026 07:1x UTC

Why: LANE-POOLS2 item 2. PIS-M measured ~7,000 open cipher signs in Pisany's nine 1585 letters (pool bar PASS on point estimate).
Tomokiyo `sources/cryptiana/web/henryiii.htm` lines ~270-280 publish the table Pisany used for the King in 1585 (letters of 4 June
f.50, 7 June f.63, 16 June f.69, 17 June f.75, 2 July f.93/f.97, 17 July f.105/f.114, ...) as `henryiii_Vivonne4.png`
(sources/cryptiana/keys/IMAGE-QUEUE.tsv rows 198-199 say Vivonne4 = 1586-87 and Vivonne5 = a specimen: READ the htm and settle which
image is the 1585 table before using it). A published key is not a reading: the test asks whether that table reads an open 1585 page.
Read `ciphers/fr16045-pisany-rome-1585/NOTES.md` in full first. Never write to `ciphers/fr3983-pisany-nevers-1593`.

Model Opus 5.5 (you), Sonnet subagents for passes, at most 2 at once. Cap USD 8, box 70 min. Per-pass pricing: ~USD 1.5 per page-pass;
plan = 1 cipher page x 2 blind passes + 1 reconciliation = 3 units ~4.5, plus table fetch/transcription and scripting ~2. Stop before
a unit that would cross 80% of cap or box. Gallica browser UA >= 2 s apart, <= 30 requests; cryptiana.web.fc2.com 1-2 requests.

1. Gate: `python3 tools/intake_gate_check.py fr16045-pisany-rome-1585` (paste). Fetch the table image once (save unmodified under
   sources/cryptiana/web/ with sha256 + IMAGE-QUEUE note, as A3V2-ES132C4 did for spanish3vargas4.png), transcribe it to
   `ciphers/fr16045-pisany-rome-1585/key.tsv` (grade: published key; credit Tomokiyo). If no 1585 table is published, stop: NON-TEST.
2. Write `specs/fr16045-pisany-rome-1585.json` (Pipeline 3a fields; judge block on the fr16 corpus in tools/data -- check its held-out
   false-negative rate with `tools/judge_plaintext.py --holdout` at the page's N and report per-fold spread, rule 3).
3. Page: f.75 (17 June 1585, densest; or f.121) -- the cipher lines only. Crops: paste `python3 tools/iiif_lines.py --ark
   btv1b9060906j --canvas <N> --region <x,y,w,h> --out ciphers/fr16045-pisany-rome-1585/images --prefix f75 --debug`, overlay checked,
   2 blind Sonnet passes on crop paths + the table's sign list only (no plaintext), `tools/reconcile_passes.py`, reconcile from crops;
   err_2reader reported.
4. PRE-REGISTER (commit + push `PREREG_test1.md` before decoding): statistic = fr16 judge score (per-char 4-gram) of the decode;
   nulls computed first: (a) value-shuffled key (>= 500), (b) token-order shuffles of the decode (>= 200); positive control = the same
   table on Tomokiyo's quoted specimen (or any glossed passage on c134/c252) scored in the same run. Gate: real > both p99 and positive
   control passes. One line per null on why it can differ from the target on this statistic (rule 3 orthogonality). A FAIL near the gate
   with a high held-out FN rate is "judge cannot decide", not a negative.
5. Decode with `tools/decode_key.py` (decode.json if needed), write the reading with per-token grades (S if the gate passes, else M;
   codes left as codes), `--check` (rule 7). Spec `cheap_test_done` = both numbers. Gaps/Escalation refreshed, gaps_check passes. Do not
   touch status.json / NEAR.md / QUEUE.md.

Done line (tools/room.py, role "LANE-POOLS2 PIS-T (account-1 worker)"): `done (<start>-<end> UTC, brief met|box|cap): commit <sha>.
fr16045 f.75 (<date>): <n> signs, err_2reader <x>; table <image> <k> values; judge <real> vs key-shuffle p99 <a> / order p99 <b>;
positive control <c> -> PASS|FAIL|NON-TEST; grades S/M/codes; gaps_check <r>; requests ...; cost: see the lane ledger`. Report what
was found and where it was not found; do not classify novelty.

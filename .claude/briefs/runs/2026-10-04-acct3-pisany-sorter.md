# PISANY-SORTER (account 3 worker) -- 4 Oct 2026 07:4x UTC (account-3 orchestrator)

Target ciphers/fr16045-pisany-rome-1585 (PIS-T, LANE-POOLS2: fr.16045 f.75, 17 Jun 1585, canvas 156, 22 cipher lines; err_2reader 0.430,
inventory unsettled, 4 confusable groups named in its NOTES.md). Follow ciphers/fr16106-vivonne-longlee-1579/sorter/ (build_inputs.py, build.sh) as the worked example. Build the owner sign-sorter inputs exactly as
ciphers/nevers-birago-fr3251-1572/sorter/README.md and ciphers/fr16142-noailles-constantinople-1571/sorter/build.sh do: signs.tsv,
labels.tsv (piles from the two blind passes / an atlas over-split), focus.tsv (columns where the passes split), pages/ as line crops
named <leaf>_L<nn> (so the sorter shows lines above and below). Gallica public images only. Build the page with tools/sign_sorter.py
in scratch, check it renders with no script errors, keep it under 16 MB (--thumb/--tile-quality/--page-scale), commit only the
inputs + a sorter/README.md + build.sh (never the HTML if over 30 MB). ROOM line for the account-3 orchestrator to publish. Cap 6,
box 60 min. ROOM claim/done.

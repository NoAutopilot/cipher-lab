# SORT-A2o sorter inputs (10 Oct 2026, account 2, LANE FAMILY-A2o)
Built, not published (an account-2 artifact would be private to account 2, cf. ASKS 145). `sh ciphers/na-oldenbarnevelt-2442-1605/sorter/a2o/build.sh OUTDIR`
writes the page (default blind mode: no key, no value, no machine label; starting piles are shape clusters) and runs
`tools/sorter_preflight.py`. Publish with capabilities {"db": {}} after eyeing the preflight contact sheet; export, then
`tools/sign_sorter_apply.py`. ASKS 161. See NOTES.md "SORT-A2o".

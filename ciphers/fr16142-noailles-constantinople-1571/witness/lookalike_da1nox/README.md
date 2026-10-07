# DA1-NOX look-alike re-read of c510 L05-L14 splits (7 Oct 2026)

Inputs built from witness/c510_recon.tsv and c510_recon_log.tsv (62 non-gap, not-both-unread split columns mapped to recon positions,
0 mismatches). Tiles whose split was one-named-vs-unread got the named glyph plus two distractors from the D07-NOXREAD named split set
(W:sieur, q2, t1, h1, f2, i3, r2) so the re-read is a choice. Crops and montages are not committed (regenerable, 7.8 MB):

    curl -A "Mozilla/5.0" -o c510.jpg https://gallica.bnf.fr/iiif/ark:/12148/btv1b9060927q/f510/full/full/0/native.jpg   # sha1 3a81f5c8...
    python3 tools/iiif_lines.py --image c510.jpg --region 1050,250,3780,5450 --centres <run2/nxatl/line_centres.json "510"> \
      --follow-slope 300 --slope-margin 15 --max-width 1400 --overlap 100 --prefix c510r --out crops --debug
    python3 tools/lookalike_pass.py windows --tiles da1nox510_tiles_in.tsv --passc c510_passC_long.tsv --manifest crops/manifest.json \
      --crop-pattern 'c510r_{line}_s*' --out lk --run da1nox510w --scale 1 --half 4

Re-reader: one Opus subagent, the montages + Tomokiyo's table image (cryptiana CharlesIX_Acqs2.png, not committed), shape only.
Settled by `tools/lookalike_pass.py reconcile` (2-of-3 rule). Its residual is agreement, not accuracy (LESSONS.md "Look-alike pass").

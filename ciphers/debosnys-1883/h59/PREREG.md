# H59 pre-registration (29 Sept 2026, DEBOSNYS-RUNNER-3b; pushed before any real score)

Row: CAMPAIGN.md H59 (swarm DIGEST-2 row 1, the D2 split lead from R2-5). Instrument: R2-5's D2 statistic unchanged
(swarm/R2/R2-5/boxnull.py zscore: D's order features, box-level within-line shuffles, then split; score = z(mi1) +
z(bg2) + z(rep3) - z(dbl)), summed over the four cryptograms instead of two.
Text: settled drafts c1, c2, c3, c4 (settled_lines, drop_clear=True); RULE.md marks dropped (BLOB, BAR-SOLID, HOOK-L,
DASH-V, `_`, MULTI, MARK); RULE.md's stroke folds applied BEFORE splitting (PCT-SLASH->PCT, X-DOT->X, X-CURL->X);
then each of R2-5's two split maps (real-T, real-N) applied to the remaining composites.
Noise mix, page-weighted, 3:1 replace:indel (r21.mixnoise): c1 0.16, c2 0.155, c3 0.09, c4 0.09 (the settled floors).
Nulls, per map: NULL-SPLIT 500 draws (ids drawn iid from the pooled unsplit counts, noise as above, cut to the real
line lengths, split); NULL-HABIT 200 draws (same, but each id has two favourite successors taken with prob 0.25, as
dcore's NULL-HABIT, on the real id names, at box level before the split). Shuffles: 100 per text per null draw, 400
for the real text (5 seeds, median).
Control first: R2-5's planted French ligature text (r25.planted, composite share 0.24), cut to the four texts' line
lengths with the same page-weighted noise, 40 instances, scored against the NULL-SPLIT of the real-N map; power =
share of instances above that null's p95. If power < 0.80: log "no passable control at this N" and stop without
scoring the real text.
Two-order correction: the real text is scored under both maps; the lead (real-N) must exceed the p99 of its own
NULL-SPLIT (two maps tried, so p <= 0.01 each keeps the family at about 0.02) AND the p95 of its NULL-HABIT.
Kill: real-N at or below its NULL-SPLIT p99, or not above its NULL-HABIT p95. A survivor is a lead for between-box
order after composite splitting, not a reading.

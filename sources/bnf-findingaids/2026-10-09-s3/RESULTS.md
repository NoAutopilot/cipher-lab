# MQS-BNF-S3 results (9 Oct 2026, 07:50 UTC by date -u; disk only, 0 requests)

Option: `tools/bnf_findingaid.py --pile ... --prior-work` (own work across ciphers/ by tools/shelfmark.py exact match, plus
prior_work.py check 3a active edition). Pre-registration: tools/tests/PREREG-MQS-BNF-S3.md (202813819, amendment A
c7d3df002), pushed before any score. Regenerate: `python3 sources/bnf-findingaids/2026-10-09-s3/run_controls.py`
(writes s3-pile-real.tsv, s3-pile-n1-shift37.tsv, s3-pile-n2-swap.tsv here).

| control | statistic | number | gate | result |
|---|---|---|---|---|
| K1 volume recall (29 volumes with a notice on disk and a ciphers/ folder for that volume) | share with >= 1 item ours/ours? | 25/29 = 0.862 | >= 0.60 | PASS |
| N1 folio shift +37 | items ours+ours? vs real | 44 vs 115 = 0.383 | <= 0.25 | **FAIL** |
| N2 volume swap | items ours+ours? vs real | 2 vs 115 = 0.017 | <= 0.10 | PASS |
| K2 active edition | volumes with contact_first | fr.2988 only (mary-castelnau-edition); fr.3413 none | exactly fr.2988 | PASS |

K1 missed fr.2751, fr.4102, fr.5160, fr.5761 (not diagnosed). K1 volumes recalled only through a range notice (ours?, not
taken out of the open counts): fr.3974-3995, fr.4133-4138, fr.4734-4736. Hits outside K1 (our folders name a leaf of the
volume although no folder is named for it): fr.3019 fr.3040 fr.3045 fr.3091 fr.3096 fr.3251 fr.3252 fr.3484 fr.3623.

Reading of the N1 FAIL (descriptive, after the gate; no threshold changed): the volume match is precise (N2), the folio
match is not -- 24 of the 44 null hits come from the 22-volume Nevers range notice (ours?, already kept in the open counts),
and the other 20 from volumes whose folders name many leaves (fr.4715 4, fr.3251 5, fr.2988 4, fr.2980 2, fr.3252 2, ...):
a shifted folio lands on another leaf we also worked. So `ours` says "a folder of ours names a leaf with this volume and
folio", not "this item was worked"; a finding-aid folio and our ink folio can also differ. Use it as a lead to open the
named folder, never as an exclusion of an item from a pile. Grade weak (pre-registered: a missed gate ships weak, not
re-briefed).

Pile effect on the S2A/S2B corpus: fr.3029 (the one pile-class volume, 6 open bare) has no own-work hit; fr.2988 has 6
items named by our folders (already open_bare 0 through Tomokiyo) and contact_first set. No status, key, reading or AUDIT.md
changed.

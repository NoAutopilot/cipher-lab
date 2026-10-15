# PREREG OBRED-9453 (15 Oct 2026, 12:0x UTC by date -u; written before the scan is fetched at native size or any score)

Item: NL-HaNA 1.01.02 inv. 9453 scan 24 (letter to Langerak, margin date 15-1-1616 or 1617, M; OBRED-NA2 flag), read at 900 px only so far
(codes 92, 47, 424, 47, 10, 49, 41, 3, 244, 32, M; margin decodes Hert. van Bouillon, De Coninck van Engelant, Churfurst Paltz, Wesel / de
Churfurst, M. d'Oldenbarnevelt, Troenes, De Coninck v. Spaegne). Question: does any no. 92/187 name code (37 tokens, 20 distinct values,
588-751, obred187/band/reading_92_187.tsv) match this nomenclator in form or context? Known-keys rung; not a key merge.

Steps (service.archief.nl <= 6 requests, ROOM take/release, >= 3.2 s apart):
1. Fetch scan 24 once at native size (IIIF full/max, or full/2400 if max is refused); crops stay in scratch, sha1 to na_obredna_scans.tsv.
2. One Opus read (this worker) of every numeral in the letter body and every margin decode; table obred9453/table_9453_s24.tsv
   (code, name, line, grade: C where the margin decode sits against that code, M otherwise).
3. T1 form test: exact value overlap k between the 9453 code set (distinct values, n) and the 20 no. 92/187 name-code values.
   Control (can vary with the statistic): 10,000 draws of n distinct values uniform on [1, max(9453 code)]; also a second null on
   [1, 999] (a three-digit table of the no. 92 size). p = P(k_null >= k_real). Also report whether the two value ranges are disjoint.
4. T2 name test: every person/place named both in the 9453 decodes and in the no. 92 family glosses (OBRED-556: 605 Palsgrave /
   Fredrich Palsgrave C, 594 Bohemen C, 600 prince M, 587 Gr. van M... M, 732 d' Fran... M) or in the no. 92 context leads
   (605 "heeft bij 605 geobtineert", Palsgrave M): same code = agreement, different code = conflict. Conflicts go to HYPOTHESES.md
   with witnesses (sender, recipient, direction, date; rule 4).
Gate: a match is S only if T1 k >= 3 with p < 0.01 under both nulls and T2 shows no conflict; otherwise every match is M, and a T2
conflict between differently dated, differently addressed letters is logged as evidence of a different key, not settled.
Expectation stated in advance: at 900 px the 9453 values look small (3-424) and the no. 92 name codes are 588-751, so k = 0 is expected;
a k = 0 result is a "different key (form)" finding for this one leaf, not a statement about other Oldenbarnevelt keys.

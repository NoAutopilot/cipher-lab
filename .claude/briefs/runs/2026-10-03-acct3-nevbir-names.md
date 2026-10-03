# NEVBIR-NAMES (account-3 orchestrator, 3 Oct 2026): fill the gaps with the names Birago would have written

Owner's idea (3 Oct 2026): many unread spans in nos.71/86/90 (and fr.3252 f.47/f.117) sit where proper nouns belong.
Targets ciphers/nevers-birago-fr3251-1572 and ciphers/birago-fr3252-1571-72. Model Opus 5.5. Cap $7, box 60 min.
Disk + Gallica/IA/Google Books text search only (>=1.5 s per host). Distinct instrument from NEVBIR-OFFSHEET (which fit
single signs by language score): this one tests WHOLE NAMES against the letter pattern around each gap.
1. Gazetteer, built BEFORE looking at any gap (pre-register: commit the list first). Sources, in order: (a) the clear
   (uncoded) prose of every Birago letter on disk and its neighbours in fr.3251/3252 -- every person, place and office
   named there; (b) the 1665 Mémoires de Nevers parts 1-2 (Gallica full text) for 1570-72 Piedmont/Saluzzo names;
   (c) standard context: the Duke of Savoy (Emanuele Filiberto) and his ministers, Turin, Carmagnola, Revello,
   Dronero, Savigliano, Pinerolo, Cuneo, Geneva, Bellegarde (Saint-Lary), the Montmorency (Damville, Thoré, Méru),
   Coligny, Navarre, Condé, Anjou, the King, the Queen [Mother], des Adrets, Gordes, Lesdiguières, Sanfrè, Coconato,
   Valletta, Scipione Carego, Francesco Ga...o, and Italian spellings (Momoransi, Turino, Ugonotti...). Each name in
   period Italian/French spellings, tagged with source.
2. Gap inventory: every run of U/M signs of length >=3 in the readings, with its fixed flanking letters (the S-graded
   neighbours) and length range (off-sheet signs may be one letter each or a name code).
3. Pattern match: for each gap, every gazetteer name whose letters agree with every S-graded sign inside the span and
   whose length fits; score by how many fixed letters it matches. Control (rule 3, must be able to fail): the same
   matching with (i) a gazetteer of the same size of random Italian/French words and names of equal length
   distribution, and (ii) the gaps' flanking letters shuffled; a name fill counts only if its match strength beats
   both controls' p95. Report each surviving fill with the English context, grade M (inferred), never S.
4. Bonus check: if a fill assigns a value to a recurring off-sheet sign consistently across >=2 gaps, list it as a
   candidate key value (M) for a later verifier; do not apply it to the key.
NOTES both folders, HYPOTHESES rows (both control numbers), gaps_check, PROGRESS notes. Report what was found and
where it was not found; do not classify novelty. Done line "for the account-3 orchestrator".

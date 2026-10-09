# eckert-1864 HYPOTHESES

## Key conflicts (rule 4: two witnesses disagree on one code; logged, not resolved by frequency)

### Harry (key-no2.md) -- 8 Oct 2026, LS4-R2b
- Key row: Harry = Washington, grade C, one witness: A3V3-ECKC (mssEC 18 entry 9902.402, 30 Nov 1864, to Sheridan, "Left for Harry [?]").
- Conflict: N2-CD (mssEC 19 p.94-95, pointers 8986/8987, 17 June 1864, "cars run from Harry to Bravo and Stanton") is printed in OR I/40 pt 2 (`warofrebellion402unit`, Washington, June 17, 1864 -- 3 p.m., Halleck to Grant) as "cars run from Richmond to Charlottesville ..."; there Harry reads Richmond. (Richmond is already Horace, p.16 l.2.)
- Status: graded M in N2-CD (H -> M); in any letter whose context is not the 9902.402 one, "Harry" is M. Unresolved: two senses (Washington / Richmond) from two letters of different direction and date.

### Pickets / Picket (key-no2.md, key.md) -- 8 Oct 2026, LS4-R2b
- Key rows: Picket = Demoralize (-ed, -ing) (key-no2.md p.20 l.18, H), Picket = Defeat (-ed, -ing) (key.md p.19 l.18, H); "Pickets" decodes by the stem+ending rule to the verb.
- Conflict: N2-CD "Pickets queen about Clarke Dwight Sugar ..." is printed (same OR page) as "Pickett's division about 6000 infantry"; the clerk wrote the general's name as the plain word, which collides with a keyed verb.
- Status: M in N2-CD (H -> M). Rule for later readers: a plain proper name that equals a key word is read from context and graded M.

## Mint / Mogul: McPherson or Steedman (FM-R1, 8 Oct 2026)
Witness A: key.md, Mint / Mogul = Maj Gen J. B. McPherson (H, mssEC 41 p.17 l.19, undated). Witness B: E169 (mssEC 25 / obj 5952, pointer 5782, Eckert to Sheldon, Beckwith and Caldwell, 9 Sept 1864): "in place of McPherson place [Gen] James [B.] Steedman: Mint and Mogul". Not settled by frequency: an entry keeps McPherson before 9 Sept 1864 and Steedman after only on B's single witness; grade M for either value until a second dated witness. Next: grep filed entries with Mint/Mogul by date.
Settled (FV-FM2, 8 Oct 2026, AUDIT.md "## AUDIT (FV-FM2)" section 3): witness C, the key copy mssEC 43 (object 428) p.[17], pointer 413, reads "Mint ... do J. B. Steadman ... Mogul" in the main hand, no strike (image read). A (mssEC 41) is the book before the change, C the book after it, B the dated order between them: a key change, not a data conflict. Grade Mint/Mogul = McPherson (H) before 9 Sept 1864 and Steedman (H) from 9 Sept 1864. Grep of ciphertext*.txt: no Cipher No. 1 entry other than E169 uses Mint or Mogul, so no reading changes. Supporting: the printed addenda to No. 1 dated 9 Sept 1864 in the Friedman copy (Tomokiyo, civilwar1; not read here).

### Hero (key.md) -- 9 Oct 2026, FIX-FM3 (from AUDIT FV-MS18 s.3)
- Key row: Hero = Johnston, grade H (key.md p.15 l.17, the period book's value).
- Conflict: E202 (mssEC 18, 24 Oct 1864, Van Duzer to Maj. Gen. Thomas) needs Brig. Gen. R. W. Johnson, the cavalry officer relieved by Chambliss (OR I/39 pt 3 pp.301, 462, 511); the clerk used the near-homophone, a different man from the book's Johnston.
- Status: key.md untouched. In E202 only, "Hero" carries a `gloss:` note (Brig. Gen. R. W. Johnson, grade C from the print); in any other letter Hero stays Johnston H.

### Orphan / Endless (key.md has no row) -- 9 Oct 2026, FIX-FM3 (from AUDIT FV-MS18 s.3)
- Witnesses: E168 (period instruction, Halleck to Sheldon 17 Mar 1864, "orphan Endless for Maj. Gen. Franz Sigel") and E206 (Kelton to the commander at Martinsburg, printed OR I/37 pt 1 p.557, addressee Sigel). No conflicting value located.
- Status: no key row added (key.md is the period book's table, not edited); E206 carries a `gloss:` note (Sigel, grade C: printed addressee). E168 and E108 are not changed by this job; E108's "Orphan" (McCaine to Hunter, 6 July 1864) is a separate letter with another direction and date and stays as decoded until a verifier rules.

## Known-plaintext key test: Cipher No. 1 on Porter's four 8 Dec 1864 telegrams (CONF-FM, 9 Oct 2026, account 1)
| date | hypothesis | material | target number | control number | verdict | script |
|---|---|---|---|---|---|---|
| 9 Oct 2026 | the Fort Monroe ledger's 8 Dec 1864 Porter entries were enciphered with War Dept Cipher No. 1 (key.md) | mssEC 25 pointers 5820 entries 2-3, 5821 entries 1-2 (eye-checked against line crops) vs ORN I/11 pp.155-156 (four Porter telegrams: Howlett battery; monitors to Hampton Roads; "Go down the river yourself"; Miami to City Point / Pagan Creek, to Grant) | **46 of 52** hand-aligned code words read to the printed word (grade C, not a reading) | meaning-shuffled key, 1000 seeds: mean 0.12, p99 3, max 6 | key confirmed on known text; the 6 misses are 2 x Tulip (stands where the print has a full stop; key Open), Tower in "money towers" (= "monitors" by sound), and 3 plain place names that collide with key words (Pagan x2 = Pagan Creek, Ragged = Ragged Island) | `fortmonroe/conf_fm_porter.py` -> `conf_fm_porter.out` |

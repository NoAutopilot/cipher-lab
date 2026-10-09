# PREREG-MANT-NAMES136 (9 Oct 2026, 07:2x UTC by date -u; LANE FAMILY-A2g account 2)

Pushed in its own commit BEFORE any crib_list_fit.py score is computed. Lists built by names136/build_pool.py (sha256
prefixes: pool_names.tsv de3297bd34f06c1f, 4640 words; pool_names_var.tsv af0d416292401498, 7894; pool_fr.tsv
7d5ac58d8b7181e1, 48554; codes.tsv a0a99e1f892a4c67; key_cl.tsv 4382fa95c39efbac), all from disk (folder files + tools/data/fr18).
Disclosed: the target decodes (r01 'l?lhovel', r02 'ilg', r09 'acepusnce', 0103 r04 'lolh') were seen before the lists were
built (MANT-0136, MANT-UNGL); the f->v variant rule in pool_names_var.tsv was chosen after seeing 'lhovel'; the folder's
attested spelling 'Lolhoffel' (frame_inventory 694/08 0370) is in the strict list. A PASS under the var list is weaker for that.

Instrument: tools/crib_list_fit.py (name_candidates.py is for whole-name codes only, its own docstring routes spelled
windows here; decode_key.py --try sets one code's value and has no letter-run form). Settings for every run:
--codes names136/codes.tsv --key names136/key_cl.tsv --fixed-grades C --anchor free --wild-span 2 and the tool's default
rule (unique best, P < 0.05, agree >= 0.6, mismatch <= 1, fit >= 6). Fixed: key C single letters; wild: M rows, multi-letter
or name values (16 o|ou|ous, 15, 30, 55, 97, 170 ...).

Controls (run first):
- C1 positive, f468_g13:1-7 = 3 35 44 12 34 21 7, period gloss 'Welling' (34 = p is a known 9/4 misread, the 'Welling' row
  of HYPOTHESES.md); list pool_names.tsv; pass = 'welling' named candidate.
- C2 positive, 694-09_0136_r04:3-9 (44 39 5 22 21 9 10), read 'livonie'; list pool_names.tsv; pass = 'livonie' candidate.
- N1 negative, 694-09_0136_r08:5-12 (55 9 2 21 100 50 67 59), read French 'ierendaut' (not a name); list pool_names.tsv;
  pass = no candidate.
Gate: the target runs license anything only if C2 passes and N1 names no candidate. C1 is reported either way.

Targets:
- T1 694-09_0136_r01:1-8 vs pool_names.tsv, then vs pool_names_var.tsv.
- T2 694-09_0136_r02:1-3 and T3 694-09_0103_r04:1-4: max possible fit 3 and 4 < 6, so they cannot pass the rule by
  construction: rank reported, logged too-short for this instrument.
- T4 694-09_0136_r09:1-9 vs pool_fr.tsv and vs pool_names.tsv.
Outcome: a candidate is a crib, graded M at best; nothing enters key.tsv.

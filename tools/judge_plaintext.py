#!/usr/bin/env python3
"""judge_plaintext.py: score a candidate plaintext mechanically against a spec (specs/<slug>.json) and print PASS or FAIL.

Written 24 Sept 2026 (survey worker). Our version of the Lean check in the 2025-26 Erdős-problem work: a solver session
(or a hundred of them) proposes a plaintext; this script, not a person, says whether it clears the bar. It never says a
reading is *right* (rule 10: that is a verifier's job); it says whether the reading is worth a verifier's time.

Usage:
  python3 tools/judge_plaintext.py specs/koehler-1944.json --text "DER ANGRIFF ..."        one candidate
  python3 tools/judge_plaintext.py specs/koehler-1944.json --file candidate.txt [--json]  from a file
  python3 tools/judge_plaintext.py --selftest                                              offline test
  python3 tools/judge_plaintext.py --holdout F1 F2 ... --N 1066 [--alphabet ru-s3-soft]      rule 3 fold check

Checks, all read from the spec's "judge" block (missing keys are skipped):
  length        exact letter count ("letters": N) or a range ("letters_min"/"letters_max"), letters only (a-z after folding)
  lines         "line_letters": [n1, n2, ...] exact letters per line of the candidate (form check, e.g. Dorabella 29/31/27)
  cribs         "cribs": ["BERLIN", ...] each must occur (letters only, folded); "cribs_at": {"22": "EASTNORTHEAST"} at a
                0-based letter offset
  language      "language": one of en, de, fr, it, la (corpora on disk, tools/data), or "corpora": [paths]. The candidate's
                mean log10 4-gram probability per letter is compared with (a) real text windows of the same length from the
                same corpus (the matched control) and (b) letter-shuffled windows (the null). PASS on language needs the
                candidate to score above the null's 99th percentile AND above the real-text 5th percentile, unless the spec
                sets "language_pass": "null_only" (for texts expected to be telegraphese, initials or a code list).
  initials      "initials_regex": "^[MW]RGOABABD$" the candidate's word-initial sequence (letters, upper-cased, one
                string across all lines) must match; for initialism targets such as the Somerton code
  words         "min_word_cover": 0.6  fraction of the candidate's letters covered by a greedy segmentation into corpus words
                (>= 3 letters, plus a/i and common 2-letter words); compared with the same statistic on real text.
  alphabet      "alphabet": a plaintext alphabet other than a-z (A2P4-KAL4, 3 Oct 2026): a name from
                homophonic_anneal.ALPHABETS (ru-s3p-soft, ru-s3-soft) or a literal string of distinct characters. Every
                check then folds by keeping only those characters, case-sensitive (an upper-case letter is its own
                letter), and the 4-gram's add-k runs over len(alphabet) letters instead of 26; the corpora must be
                written in that alphabet already (tools/data/ru19_soft). Absent: the a-z fold, unchanged.
Verdict: PASS if every present check passes; exit 0. Otherwise FAIL, exit 1, with the failing checks named.
The language model is a plain add-k 4-gram over letters; it is a gate, not a proof.
"""
import argparse, gzip, json, math, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
LANG_CORPORA = {
    # en (rule 3 fold-count amendment, parent worker EN-FOLDS, 25 Sept 2026 22:17 UTC): leave-one-file-out
    # false-negative spread is 0.635 at N=200 / 0.745 at N=500 across these 2 files plus 3 more tried in
    # tools/data/en/ (Huck Finn, Gatsby, Pride and Prejudice) -- adding sources made the spread WORSE, not
    # better, driven by Moby-Dick reading as a bigger outlier against a more homogeneous 4-book "standard
    # prose" model. Unresolved: a FAIL/PASS against "en" is of unknown reliability by the amendment's own
    # rule. See tools/data/en/README.md before trusting a FAIL/PASS that cites this corpus.
    "en": [DATA / "pg1661_holmes.txt", DATA / "pg2701_mobydick.txt"],
    # en18 (26 Sept 2026, LANE ARM ARM-EN18): 1795-1815 American diplomatic/official English --
    # Monroe (Hamilton) vols II/V, Gallatin (Adams) vol I, Madison (Hunt) vols VII/VIII, Jefferson
    # (Ford) vol IX -- for armstrong-madison-1808 (a 1808 Paris despatch), which "en"'s own two
    # 19th-c. British/American novels do not register-match. See tools/data/en18/README.md for the
    # leave-one-file-out false-negative spread at N=1000/1500 (this target's own ~369-code length)
    # beside the same check for "en" -- record the spread before trusting a FAIL/PASS from either.
    "en18": [DATA / "en18" / "writingsjamesmo02unkngoog.txt.gz", DATA / "en18" / "writingsjamesmo11monrgoog.txt.gz",
             DATA / "en18" / "writingsalbertg01gallgoog.txt.gz", DATA / "en18" / "writingsofjamesm0007unse_s2a1.txt.gz",
             DATA / "en18" / "writingsofjamesm0008unse.txt.gz", DATA / "en18" / "writingsofthomas09jeffiala.txt.gz"],
    "de": [DATA / "de16" / "composed_enhg.txt"],
    "fr": [DATA / "fr16" / "lettresdecatheri01cathuoft_djvu.txt.gz"],
    "it": [DATA / "it16" / "alcuneletteredip00ferr.txt", DATA / "it16" / "delleletterefam02seghgoog.txt",
           DATA / "it16" / "lettereinedited00tassgoog.txt", DATA / "it16" / "lettereinedited01cibrgoog.txt",
           DATA / "it16" / "lettereineditedi01carouoft.txt", DATA / "it16" / "letterescrittea01vanzgoog.txt"],
    # it16dip (26 Sept 2026, LANE SALV SALV-CTX): 16th-c. Italian DIPLOMATIC letters nearer Toledo 1525 than "it"'s
    # later familiar letters -- Castiglione's Lettere (Serassi 1769-71, incl. the Negozi of his 1525-29 nunciature at
    # Charles V's court), Desjardins/Canestrini tome II's Italian despatches (1510s-1530s), Lettere di principi I-III
    # (1564); long-s OCR repaired, letter paragraphs only. Leave-one-file-out false-negative spread at N=2500 beside
    # "it"'s in tools/data/it16dip/README.md -- read it before trusting a FAIL/PASS. "it" stays the default.
    "it16dip": [DATA / "it16dip" / f for f in ("bub_gb_laRnTtJmsDAC.txt.gz", "bub_gb_ZJMxff7r4LUC.txt.gz",
                "gri_33125010469852.txt.gz", "letterediprincip01char.txt.gz", "letterediprincip02char.txt.gz",
                "letterediprincip03char.txt.gz")],
    # it19 (2 Oct 2026, A2-CAS7, LANE-A2PUSH account 2): Italian political, historical and epistolary prose of about
    # 1800-1830 -- Botta's Storia d'Italia dal 1789 al 1814 t.I, Colletta's Storia del reame di Napoli, Cuoco's Saggio
    # storico (1806), Foscolo's Epistolario vols 1 and 3 (the latter his London letters of 1816-27), each capped at 650k
    # folded letters -- for castelcicala-1816 (1816-23 Neapolitan despatches), which it16/it16dip (16th c.) do not
    # era-match. See tools/data/it19/README.md for the leave-one-file-out false-negative spread before trusting a FAIL/PASS.
    "it19": [DATA / "it19" / f"{i}.txt.gz" for i in ("storiaditaliadal01bottuoft", "storiadelreamedi00coll",
             "saggiostoricosul00cuoc", "bub_gb_ODloWJYQNSYC", "bub_gb_jVdaVPIiH8sC")],
    # sco16 (2 Oct 2026, GAPS6-moray-wood-1568, account-4): 1550-1600 Middle Scots prose -- Knox's History (Laing, Works
    # I-II), the Diurnal of Remarkable Occurrents (1513-1575, long-s repaired), the Historie of King James the Sext, and
    # the Register of the Privy Council of Scotland vol. 2 (1569-1578), each capped at 700k folded letters, editors' modern
    # English dropped by a Scots-vs-modern spelling-marker filter (tools/data/sco16/build.py) -- for ciphers/moray-wood-1568
    # (13 July 1568), which no other corpus here era- or variety-matches (en16_repo is 1650s English). See
    # tools/data/sco16/README.md for the leave-one-file-out false-negative spread at N=134 before trusting a FAIL/PASS.
    "sco16": [DATA / "sco16" / f"{i}.txt.gz" for i in ("worksofjohnkn01knox", "worksofjohnkn02knox",
              "adiurnalremarka00thomgoog", "historielifeofki00colvuoft", "registerofprivyc0002jjoh")],
    "pt": [DATA / "pt17" / "vieira_cartas_tomoIV_1855.txt.gz", DATA / "pt17" / "vieira_cartas_1912.txt.gz"],
    # nl18 (3 Oct 2026, NL18-CORPUS, account-4): 1770-1799 Dutch prose, colonial/official register -- Hartsinck's
    # Beschryving van Guiana (1770, 2 vols), Stedman's Reize naar Surinamen (Dutch tr. 1799), Batavia (1799), Marsden's
    # Sumatra (Dutch 1789), Reizen naa Ceilon (1796), Verzameling van stukken ... Noord-America (1781) -- for
    # na-suriname-map-1781 (1781 Suriname fortification legends). OCR long-s repaired at build (build_nl18.py).
    # Read tools/data/nl18/README.md for the leave-one-file-out false-negative rate and per-fold spread first.
    "nl18": [DATA / "nl18" / f for f in ("beschryvingvangu01hart.txt.gz", "beschryvingvangu02hart.txt.gz",
             "bub_gb_mGdCAAAAcAAJ.txt.gz", "bataviaindeszelf02amst.txt.gz", "beschryvingvanh00esch.txt.gz",
             "reizennaaceilon00roosgoog.txt.gz", "verzamelingvanst01vand.txt.gz")],
    # pl18 (4 Oct 2026, A3V3-SANGP, account 3): Polish memoir/letter prose of 1683-c.1790 in 19th-c. editions --
    # Otwinowski's Pamietniki do panowania Augusta II (1838), Pasek's Pamietniki (1860), Jan III's Listy (1823),
    # Ojczyste spominki I (1845), Kitowicz's Pamietniki (1882); Polish diacritics pre-folded to a-z at build
    # (tools/data/pl18/build.py), French/Latin lines dropped -- for sanguszkow-mniszech-dunin-1714 (1714), which pl19
    # (19th-20th-c. fiction) does not era-match. Leave-one-file-out FN 42.2% blended at N=232, spread 11.0-80.5% (pl19:
    # 91.5%, 78.5-98.0%): a FAIL/PASS against the p05 gate is of unknown reliability; read tools/data/pl18/README.md.
    "pl18": [DATA / "pl18" / f"{i}.txt.gz" for i in ("bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967",
             "bc.radom.pl.11-359", "bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549", "ojczystespomink01johngoog",
             "pamitnikiksakit01kitogoog")],
    "pt18": [DATA / "pt18" / "correiobrazilie00unkngoog.txt.gz", DATA / "pt18" / "correiobrazilie02unkngoog.txt.gz",
             DATA / "pt18" / "oinvestigadorpo03unkngoog.txt.gz", DATA / "pt18" / "oinvestigadorpo05unkngoog.txt.gz"],
    # fr18 (25 Sept 2026, LANE ZX2 ZX2-FR18): French diplomatic/official prose c.1680-1790 -- Torcy's and
    # Villars' memoirs, Mme de Maintenon's letters, La Gazette de France 1786 -- for this lane's French
    # targets (clair1161, clairambault296, hellen-1752, destaing-gerard-1779), which are 100-200 years later
    # than fr16 (fr's default, 16th-c.) and a different register than fr19 (19th-c. novels). See
    # tools/data/fr18/README.md. "fr" stays the default; a spec opts in with "judge": {"language": "fr18", ...}.
    "fr18": [DATA / "fr18" / "memoiresdemonsie01torc.txt.gz", DATA / "fr18" / "memoiresdemonsie02torc.txt.gz",
             DATA / "fr18" / "mmoiresduducde01invill.txt.gz", DATA / "fr18" / "mmoiresduducde02vill.txt.gz",
             DATA / "fr18" / "mmoiresetlettre01margoog.txt.gz", DATA / "fr18" / "lagazettedefran01unkngoog.txt.gz"],
    # fr1810 (1 Oct 2026, account-4 worker BER-FRCORP): Napoleonic-era official/military French, 1800-1811 --
    # Correspondance de Napoleon Ier tomes XI, XVI, XX (1805-06, 1807-08, 1809-10; 1858-70 edition), Correspondance
    # du marechal Davout tomes II and III cut before 1812 (Mazade 1885), Lettres inedites de Napoleon Ier tome I
    # (an VIII-1809, Lecestre 1897) -- for berthier-napoleon-1812 (22 Dec 1812), which fr18 (1680-1790) and fr19
    # (19th-c. novels) do not era- or register-match. Nothing from Dec 1812 (tome XXIV and Davout's 1812-13
    # letters are deliberately excluded as the target's own month). See tools/data/fr1810/README.md for the
    # leave-one-file-out false-negative rate and per-fold spread at N=325 beside fr18's -- read it before
    # trusting a FAIL/PASS. "fr" stays the default; a spec opts in with "judge": {"language": "fr1810", ...}.
    "fr1810": [DATA / "fr1810" / f for f in ("correspondancede11napouoft.txt.gz", "correspondancede16napouoft.txt.gz",
               "correspondancede20napouoft.txt.gz", "correspondanced01davogoog.txt.gz",
               "correspondanced00davogoog.txt.gz", "lettresindites01napo.txt.gz")],
    # fr17 (3 Oct 2026, account-4 worker TOOL-FR17): French diplomatic/administrative/epistolary prose of about 1617-1644
    # in its own period spelling -- Richelieu's Lettres (Avenel) tomes III (1628-30) and VI (1638-42), Peiresc's letters
    # to the Dupuy brothers tomes I-II (1617-33), Chapelain's Lettres tome I (1632-40), Mazarin's Lettres tome I (1642-44)
    # -- editors' modern-French notes dropped by a period-vs-modern spelling-marker filter (tools/data/fr17/build.py),
    # each file capped at 650k folded letters. For 1630s-1650s French targets (first: decode-2754-bnf-baluze156-1636),
    # which fr16 (c.1560-1615) and fr18 (1680-1790) do not era-match. Read tools/data/fr17/README.md for the
    # leave-one-file-out false-negative rate and per-fold spread before trusting a FAIL/PASS.
    "fr17": [DATA / "fr17" / f"{i}.txt.gz" for i in ("bub_gb_OIQItRIybmIC", "bub_gb_wBJLsV8B_BgC",
             "lettresdepeiresc01peiruoft", "lettresdepeiresc02peiruoft", "lettresdejeancha01chap",
             "lettresducardina01maza")],
    "es": [DATA / "es17" / "donquijote00cervuoft.txt.gz", DATA / "es17" / "vidadelbuscn01quevuoft.txt.gz"],
    "da19": [DATA / "da19" / "historisktidsskriftdk1s6.txt"],  # 1845 Historisk Tidsskrift, 1.04M letters (B2 bCPH, 25 Sept 2026); 19th-c. register
    "es17c": [DATA / "es17c" / "memorialhistri17realuoft.txt.gz", DATA / "es17c" / "memorialhistri18realuoft.txt.gz",
              DATA / "es17c" / "memorialhistri19realuoft.txt.gz"],
    # es17c7 (27 Sept 2026, MERCY-JUDGE2): all seven Cartas tomes (MHE tomes XIII-XIX = Cartas I-VII, 1634-1648),
    # widening es17c's three (V-VII, 1643-1647) with the four earlier ones (I-IV, 1634-1643) to give the
    # leave-one-file-out fold check more, and more varied, folds. Does not replace es17c (kept as its own key
    # per CLAUDE.md rule 3's "second/third attempt" convention -- a wider corpus is new material, not a tuning
    # of the same knob). See tools/data/es17c7/README.md.
    # es18 (2 Oct 2026, GAPS5-na-schonenberg-1678-1716, account-4): 1690-1725 Spanish letters, gazette and
    # diplomatic prose -- San Felipe's Comentarios de la guerra de Espana I-II (1700-1725, 1792 print), Caraffa's
    # El embaxador politico-christiano (1691), Crisol de la espanola lealtad (1708), Nuevo estilo y formulario de
    # escrivir cartas missivas (c.1700), Gaceta de Madrid 1710, Vera Tassis's Noticias historiales (1690) -- for
    # na-schonenberg-1678-1716 (a 1702-1716 Spanish letter), which es17c7 (1634-1648) is 55-80 years off. The five
    # original printings are long-s repaired (tools/data/es18/build.py). See tools/data/es18/README.md for the
    # leave-one-file-out false-negative rate and per-fold spread at N=245 beside es17c7's -- read it before trusting
    # a FAIL/PASS. "es" stays the default; a spec opts in with "judge": {"language": "es18", ...}.
    "es18": [DATA / "es18" / f for f in ("comentariosdelag01sanfuoft.txt.gz", "comentariosdelag02sanfuoft.txt.gz",
             "elembaxadorpolit00cara.txt.gz", "A092002.txt.gz", "A022134.txt.gz", "A11100924.txt.gz",
             "noticiashistoria00vera.txt.gz")],
    # es18p: the five 1690-1710 original printings of es18 only (period orthography, long-s repaired), without the two
    # 1792-print San Felipe volumes that dominate es18's model (49% of its letters, modernised spelling, cleaner OCR)
    # and set its real_p05 from their own register -- es18's own fold check (tools/data/es18/README.md) false-negatives
    # the held-out period originals at 19-79% against that threshold. Same fold check, same README; read both before
    # trusting a FAIL/PASS from either key.
    "es18p": [DATA / "es18" / f for f in ("elembaxadorpolit00cara.txt.gz", "A092002.txt.gz", "A022134.txt.gz",
              "A11100924.txt.gz", "noticiashistoria00vera.txt.gz")],
    "es17c7": [DATA / "es17c7" / "memorialhistri13realuoft.txt.gz", DATA / "es17c7" / "memorialhistri14realuoft.txt.gz",
               DATA / "es17c7" / "memorialhistri15realuoft.txt.gz", DATA / "es17c7" / "memorialhistri16realuoft.txt.gz",
               DATA / "es17c7" / "memorialhistri17realuoft.txt.gz", DATA / "es17c7" / "memorialhistri18realuoft.txt.gz",
               DATA / "es17c7" / "memorialhistri19realuoft.txt.gz"],
    # es17a (3 Oct 2026, OLD-ES17A, account 1): 1590-1625 Spanish state, diplomatic and court prose -- Cabrera de
    # Cordoba's Relaciones 1599-1614 (1857 print), San Clemente's embassy letters 1581-1608 (1892 print), Coloma 1625,
    # Mendoza 1592 and Antonio Perez's Relaciones 1624 (the three originals long-s repaired with tools/data/es18's
    # cleaner), each capped at 650k folded letters -- for na-oldenbarnevelt-2442-1605 (a 23 Dec 1605 letter), which
    # es17c (1643-47) misses by 40 years and es17 (fiction) by register. A spec opts in with "judge": {"language":
    # "es17a"}. See tools/data/es17a/README.md (leave-one-file-out false-negative rate and per-fold spread).
    "es17a": [DATA / "es17a" / f"{i}.txt.gz" for i in ("relacionesdelasc00cabr", "correspondencia01clemgoog",
              "bub_gb_zb0d4P6LU2oC", "bub_gb_54G5MclHRpUC", "bub_gb_CujQp6gW1dQC")],
    # nl (25 Sept 2026, YX-PTJUDGE): tools/data/nl_repo holds only a target's own committed reading (a few KB,
    # nowhere near the ~200k-character floor a language check needs) -- circular per CLAUDE.md "never use a
    # target's own reading as its corpus". Not wired. A future worker who fetches a real nl period corpus
    # (Internet Archive djvu.txt or a Google Books full-view volume, never the target's own material) of at
    # least ~200k letters can add it here the way "it"/"pt"/"es" are done.
    # la, la18 (26 Sept 2026, LANE B7 bLAJ): tools/data/la_repo was the same kind of placeholder (a different
    # target's own reading, circular, a few KB) -- "la" was commented out unwired. Replaced with a real period
    # corpus: three volumes (1709-1711) of Zaluski's Epistolarum historico-familiarium, Polish crown-chancery
    # Latin letters, era- and office-matched to ciphers/szembek-bk1560 (Jan Szembek, Crown Chancellor of
    # Poland 1700-1731; Zaluski held the same chancery offices in the same years). 7.27M folded letters. See
    # tools/data/la18/README.md (sources, cleaning, held-out false-negative rates per CLAUDE.md rule 3). "la"
    # now points at la18; a future target from a different era/register adds its own key rather than
    # overwriting this one.
    "la": [DATA / "la18" / "zaluski_epistolae_t1.txt.gz", DATA / "la18" / "zaluski_epistolae_t2.txt.gz",
           DATA / "la18" / "zaluski_epistolae_t3.txt.gz"],
    "la18": [DATA / "la18" / "zaluski_epistolae_t1.txt.gz", DATA / "la18" / "zaluski_epistolae_t2.txt.gz",
             DATA / "la18" / "zaluski_epistolae_t3.txt.gz"],
    # la17 (3 Oct 2026, GAPS57, account-4): Latin letters of about 1590-1649 -- Grotius to the Oxenstiernas and the Swedish
    # crown (1806 and 1829 editions), Vossius's correspondence (1693), Casaubon's letters (1638), the Epistolae
    # celeberrimorum virorum (1715: Grotius, Vossius and circle) and Bongars-Lingelsheim (1660), each capped at 650k folded
    # letters, register and OCR filtered -- for riksarkivet-r4282-1628 (a 1628 Swedish-court letter), which la18 (1709-11)
    # does not match by about 80 years. "la" stays la18; a spec opts in with "judge": {"language": "la17", ...}.
    # See tools/data/la17/README.md (per-fold false-negative rates and spread).
    "la17": [DATA / "la17" / f"{i}.txt.gz" for i in ("hugonisgrotiiepi00grot", "hugonisgrotiiad00oxengoog",
             "bub_gb_WTkBFjX6G_UC", "bub_gb_FK3cWikzFwsC", "bub_gb_mBpUAAAAcAAJ", "epistolaecelebe00grotgoog")],
    # de17 (3 Oct 2026, GAPS62, account-4): German chancery and diplomatic documents of about 1630-1660 as printed in their
    # own words by Irmer, Die Verhandlungen Schwedens ... mit Wallenstein 1631-1634 (3 vols, 1888-91) and two volumes of
    # Urkunden und Actenstuecke zur Geschichte des Kurfuersten Friedrich Wilhelm (1640s-1650s; a third, bub_gb_PggKAAAAIAAJ,
    # dropped for OCR and editorial regests), period-spelling filtered,
    # each capped at 450k folded letters -- for riksarkivet-r4282-1628 (1628 Swedish court) tested as German. "de" stays
    # de16; a spec opts in with "judge": {"language": "de17"}. See tools/data/de17/README.md (per-fold FN and spread).
    "de17": [DATA / "de17" / f"{i}.txt.gz" for i in ("dieverhandlungen01irme", "dieverhandlungen02irme",
             "dieverhandlungen03irme", "urkundenundacten1601berluoft", "urkundenundacte32kommgoog")],
    # de1600 (3 Oct 2026, CORP-DE16, account-4): German princely letters and chancery acts of about 1575-1611 as printed in
    # their own spelling by Bezold, Briefe des Pfalzgrafen Johann Casimir I-II (1575-1586) and four volumes of Briefe und
    # Acten zur Geschichte des Dreissigjaehrigen Krieges (Stieve/Ritter, 1599-1611), period-spelling filtered (vnd, dz,
    # seind, woellen, gnedig, nit, uff ...), each ~190k folded letters -- for decode-1411-hhsta-vienna-1600 (c.1575-1600
    # Habsburg chancery), which de17 (1630-60) and de (de16, model-composed) do not era-match. "de" stays de16; a spec opts
    # in with "judge": {"language": "de1600"}. Read tools/data/de1600/README.md (per-fold FN and spread at N=176/62) first.
    "de1600": [DATA / "de1600" / f"{i}.txt.gz" for i in ("briefedespfalzgr01joha", "briefedespfalzgr02joha",
               "bub_gb_zc4FAAAAQAAJ", "bub_gb_6M4FAAAAQAAJ", "briefeundactenz01mayrgoog", "bub_gb__s4FAAAAQAAJ")],
    # sv17 (3 Oct 2026, GAPS67, account-4): Swedish chancery letters of about 1620-1650 as printed in their own spelling in
    # Rikskansleren Axel Oxenstiernas skrifter och brefvexling (six archive.org volumes, 1888-97 Google scans), Latin and
    # German letters and editors' prose filtered out, å folded to a at build time, each capped at 450k folded letters --
    # for riksarkivet-r4282-1628 tested as Swedish. A spec opts in with "judge": {"language": "sv17"}. See
    # tools/data/sv17/README.md (per-fold FN and spread).
    "sv17": [DATA / "sv17" / f"{i}.txt.gz" for i in ("rikskanslerenax00akadgoog", "rikskanslerenax00palagoog",
             "rikskanslerenax00styfgoog", "rikskanslerenax01palagoog", "rikskanslerenax02akadgoog",
             "rikskanslerenax03akadgoog")],
    # es (25 Sept 2026, LANE R6 Y8): tools/data/es17/ -- early-17th-c. Spanish prose (Cervantes, Quevedo),
    # ~1.92M letters folded, built for espagnol142-mercy-1648 (a 1648 letter). See tools/data/es17/README.md.
    # es17c (25 Sept 2026, LANE R6 MJ): tools/data/es17c/ -- 1643-1647 Spanish court-newsletter prose
    # (Cartas de algunos PP. de la Compania de Jesus sobre los sucesos de la Monarquia), ~2.1M letters
    # folded, register-matched to espagnol142-mercy-1648 (chancery/diplomatic Spanish, June 1648) after
    # es17's literary-fiction corpus (Cervantes/Quevedo) FAILed the target's own clear words (CLAUDE.md
    # rule 3, V6-PTCORP era/register lesson). "es" stays the default; a spec opts in with
    # "judge": {"language": "es17c", ...}. See tools/data/es17c/README.md.
}
FOLD = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "é": "e", "è": "e", "ê": "e", "à": "a", "ç": "c",
                      "ù": "u", "û": "u", "î": "i", "ô": "o", "â": "a", "ë": "e", "ï": "i",
                      "á": "a", "ã": "a", "â": "a", "í": "i", "ó": "o", "õ": "o", "ú": "u", "ñ": "n"})


_ALPHA = None  # judge block "alphabet" (A2P4-KAL4): set for the duration of one judge() call, else the a-z fold


def _resolve_alphabet(a):
    if not a or a == "default":
        return None
    try:
        import homophonic_anneal as ha
        a = ha.ALPHABETS.get(a, a)
    except ImportError:
        pass
    if len(set(a)) != len(a):
        raise SystemExit(f"judge alphabet {a!r}: characters must be distinct")
    return a


def fold(s):
    if _ALPHA is not None:
        keep = set(_ALPHA)
        return "".join(c for c in s if c in keep)
    s = s.lower().translate(FOLD)
    return re.sub(r"[^a-z]", "", s)


def read_corpus(p):
    p = Path(p)
    if p.suffix == ".gz":
        t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read()
    else:
        t = p.read_text(encoding="utf-8", errors="replace")
    a, b = t.find("*** START OF"), t.find("*** END OF")
    if a >= 0 and b > a:
        t = t[t.find("\n", a) + 1:b]
    return t


class NgramModel:
    def __init__(self, texts, n=4, k=0.01):
        self.n, self.k = n, k
        self.V = len(_ALPHA) if _ALPHA is not None else 26
        self.c = Counter(); self.ctx = Counter()
        words = Counter()
        self.raw = ""
        for t in texts:
            L = fold(t); self.raw += L
            for i in range(len(L) - n + 1):
                g = L[i:i + n]; self.c[g] += 1; self.ctx[g[:-1]] += 1
            if _ALPHA is not None:
                words.update(re.findall("[" + re.escape(_ALPHA) + "]+", t))
            else:
                words.update(w.lower().translate(FOLD) for w in re.findall(r"[A-Za-zäöüßéèêàçùûîôâëï]+", t))
        two = {"is", "it", "in", "to", "of", "on", "at", "be", "by", "he", "we", "me", "my", "no", "so", "up", "us", "an",
               "as", "am", "do", "go", "if", "or", "er", "es", "zu", "im", "du", "le", "la", "de", "et", "un", "il", "je"}
        self.words = {w for w, n_ in words.items() if n_ >= 2 and (len(w) >= 3 or w in ("a", "i") or w in two)}
        self.maxw = max((len(w) for w in self.words), default=1)

    def score(self, s):
        """mean log10 P(letter | 3 previous) over folded s; add-k over 26 letters."""
        s = fold(s)
        if len(s) < self.n:
            return -9.9
        tot = 0.0
        for i in range(self.n - 1, len(s)):
            g = s[i - self.n + 1:i + 1]
            tot += math.log10((self.c.get(g, 0) + self.k) / (self.ctx.get(g[:-1], 0) + self.V * self.k))
        return tot / (len(s) - self.n + 1)

    def cover(self, s):
        """fraction of letters covered by a greedy longest-word segmentation (with restarts on failure)."""
        s = fold(s); i = 0; covered = 0
        while i < len(s):
            best = 0
            for L in range(min(self.maxw, len(s) - i), 0, -1):
                if s[i:i + L] in self.words:
                    best = L; break
            if best:
                covered += best; i += best
            else:
                i += 1
        return covered / len(s) if s else 0.0

    def controls(self, N, samples=200, seed=1):
        """(real-text scores, shuffled-text scores, real-text cover) for windows of N letters."""
        rnd = random.Random(seed); real, null, cov = [], [], []
        for _ in range(samples):
            j = rnd.randrange(0, max(1, len(self.raw) - N))
            w = self.raw[j:j + N]
            real.append(self.score(w)); cov.append(self.cover(w))
            ws = list(w); rnd.shuffle(ws); null.append(self.score("".join(ws)))
        return sorted(real), sorted(null), sorted(cov)


def pct(xs, q):
    if not xs:
        return float("nan")
    return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]


def judge(spec, text):
    global _ALPHA
    prev = _ALPHA
    _ALPHA = _resolve_alphabet((spec.get("judge") or {}).get("alphabet"))
    try:
        return _judge(spec, text)
    finally:
        _ALPHA = prev


def _judge(spec, text):
    j = spec.get("judge", {})
    out = {"checks": {}, "pass": True}
    lines = [ln for ln in text.splitlines() if fold(ln)]
    letters = fold(text)

    def rec(name, ok, detail):
        out["checks"][name] = {"pass": bool(ok), **detail}
        if not ok:
            out["pass"] = False

    if "letters" in j:
        rec("length", len(letters) == j["letters"], {"got": len(letters), "want": j["letters"]})
    if "letters_min" in j or "letters_max" in j:
        lo, hi = j.get("letters_min", 0), j.get("letters_max", 10 ** 9)
        rec("length", lo <= len(letters) <= hi, {"got": len(letters), "min": lo, "max": hi})
    if "line_letters" in j:
        got = [len(fold(ln)) for ln in lines]
        rec("lines", got == j["line_letters"], {"got": got, "want": j["line_letters"]})
    if "cribs" in j:
        missing = [c for c in j["cribs"] if fold(c) not in letters]
        rec("cribs", not missing, {"missing": missing, "count": len(j["cribs"])})
    if "cribs_at" in j:
        bad = {}
        for off, c in j["cribs_at"].items():
            o = int(off)
            if letters[o:o + len(fold(c))] != fold(c):
                bad[off] = c
        rec("cribs_at", not bad, {"wrong": bad})
    if "initials_regex" in j:
        ini = "".join(w[0] for w in re.findall(r"[A-Za-z]+", text)).upper()
        rec("initials", re.search(j["initials_regex"], ini) is not None, {"got": ini, "regex": j["initials_regex"]})
    corpora = j.get("corpora") or LANG_CORPORA.get(j.get("language", ""), None)
    if j.get("language") and not corpora:  # an unwired code used to skip the language check silently (B2, 25 Sept 2026)
        rec("language", False, {"error": f"language code {j['language']!r} has no corpus in LANG_CORPORA; wire it or use 'corpora'"})
    if not corpora and not any(k in j for k in ("cribs", "cribs_at", "initials_regex")):
        # fail closed: a block with only length/line checks PASSed letter salad on mccormick-1999 (LANE B2 bMCC2, 25 Sept 2026)
        rec("content", False, {"error": "no language, corpora, cribs, cribs_at or initials_regex in the judge block: a length-only gate is not a judge"})
    if corpora:
        model = NgramModel([read_corpus(p) for p in corpora])
        N = max(len(letters), 20)
        real, null, cov = model.controls(N, samples=int(j.get("control_samples", 200)))
        sc = model.score(letters)
        null99, real05 = pct(null, 0.99), pct(real, 0.05)
        mode = j.get("language_pass", "both")
        ok = sc > null99 and (mode == "null_only" or sc > real05)
        rec("language", ok, {"score": round(sc, 3), "null_p99": round(null99, 3), "real_p05": round(real05, 3),
                             "real_median": round(pct(real, 0.5), 3), "mode": mode, "N": N})
        if "min_word_cover" in j:
            cv = model.cover(letters)
            rec("words", cv >= j["min_word_cover"], {"cover": round(cv, 3), "min": j["min_word_cover"],
                                                     "real_text_median_cover": round(pct(cov, 0.5), 3)})
    return out


def selftest():
    spec = {"judge": {"language": "en", "letters_min": 60, "letters_max": 400, "cribs": ["STREET"], "min_word_cover": 0.6,
                      "control_samples": 100}}
    good = "I had called upon my friend Sherlock Holmes upon the second morning after Christmas in Baker Street with the intention of wishing him the compliments of the season"
    r1 = judge(spec, good)
    assert r1["pass"], r1
    ws = list(fold(good)); random.Random(3).shuffle(ws)
    r2 = judge(spec, "".join(ws))
    assert not r2["pass"] and not r2["checks"]["language"]["pass"], r2
    r3 = judge(spec, good.replace("Street", "Road"))
    assert not r3["pass"] and r3["checks"]["cribs"]["missing"] == ["STREET"], r3
    r4 = judge({"judge": {"line_letters": [5, 4]}}, "hello\nwo ld\n")
    assert r4["checks"]["lines"]["pass"] and not r4["pass"], r4  # form ok, but a lines-only block fails closed (content)
    r5 = judge({"judge": {"line_letters": [5, 4]}}, "hello\nworld\n")
    assert not r5["pass"], r5
    r6 = judge({"judge": {"initials_regex": "^[MW]LIAOI$"}}, "my love is always only Irene")
    assert r6["pass"], r6
    print("selftest ok: real text PASS, shuffled FAIL (language), missing crib FAIL, line form check ok")


def holdout(files, N, samples=200, alphabet=None, seed=1):
    """Leave-one-file-out real-prose false-negative check (CLAUDE.md rule 3 fold-count paragraph; A2P4-KAL5, 3 Oct 2026).

    The shared form of the 16 tools/data/*/holdout_check.py copies, with the judge-block alphabet: for each file, build
    the model from the OTHER files, take that model's own real_p05 as judge() does, and score `samples` N-letter windows
    of the held-out file; a window at or below real_p05 is a false negative. Returns (per-fold rows, blended rate,
    held-out score list). A fold shorter than N + 1 letters is skipped and reported."""
    global _ALPHA
    prev = _ALPHA
    _ALPHA = _resolve_alphabet(alphabet)
    try:
        texts = {f: read_corpus(f) for f in files}
        rows, held_scores, tot_fn, tot = [], [], 0, 0
        for f in files:
            model = NgramModel([texts[g] for g in files if g != f])
            real, _null, _cov = model.controls(N, samples=samples, seed=seed)
            r05 = pct(real, 0.05)
            held = fold(texts[f])
            if len(held) <= N:
                rows.append({"file": Path(f).name, "letters": len(held), "skipped": True}); continue
            rnd = random.Random(seed + 1); sc = []
            for _ in range(samples):
                j = rnd.randrange(0, len(held) - N)
                sc.append(model.score(held[j:j + N]))
            fn = sum(1 for x in sc if x <= r05)
            tot_fn += fn; tot += len(sc); held_scores += sc
            rows.append({"file": Path(f).name, "letters": len(held), "real_p05": round(r05, 3), "fn": fn, "n": len(sc),
                         "fn_pct": round(100 * fn / len(sc), 1), "held_p05": round(pct(sorted(sc), 0.05), 3),
                         "held_min": round(min(sc), 3)})
        return rows, (100 * tot_fn / tot if tot else float("nan")), sorted(held_scores)
    finally:
        _ALPHA = prev


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--text"); ap.add_argument("--file"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    ap.add_argument("--holdout", nargs="+", metavar="FILE", help="leave-one-file-out false-negative check over these "
                    "corpus files (no spec needed): per-fold rate, blended rate, spread, held-out p05/p01/min")
    ap.add_argument("--N", type=int, default=1000, help="--holdout window length in folded letters")
    ap.add_argument("--samples", type=int, default=200, help="--holdout windows per fold and real_p05 control samples")
    ap.add_argument("--alphabet", help="--holdout plaintext alphabet (judge-block 'alphabet' name or literal)")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return
    if a.holdout:
        rows, blend, hs = holdout(a.holdout, a.N, a.samples, a.alphabet)
        for r in rows:
            print("\t".join(f"{k}={v}" for k, v in r.items()), flush=True)
        fp = [r["fn_pct"] for r in rows if not r.get("skipped")]
        print(f"N={a.N} samples={a.samples} folds={len(fp)} blended_fn={blend:.1f}% spread={min(fp):.1f}-{max(fp):.1f}% "
              f"held_out_p05={pct(hs, 0.05):.3f} p01={pct(hs, 0.01):.3f} min={hs[0]:.3f}")
        return
    if not a.spec or not (a.text or a.file):
        ap.error("spec and --text or --file are required")
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    text = a.text if a.text else Path(a.file).read_text(encoding="utf-8")
    if a.file:  # reading files carry "#" header lines (source, grades); score the decode only (LX-JUDGE, 25 Sept 2026)
        text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    r = judge(spec, text)
    r["spec"] = spec.get("slug", a.spec)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        for k, v in r["checks"].items():
            print(f"{'ok  ' if v['pass'] else 'FAIL'} {k}: {', '.join(f'{kk}={vv}' for kk, vv in v.items() if kk != 'pass')}")
        print("PASS" if r["pass"] else "FAIL", "-", r["spec"], "(a PASS is a gate for a verifier, not a reading; rule 10)")
    sys.exit(0 if r["pass"] else 1)


if __name__ == "__main__":
    main()

"""Offline test for tools/family_run.py --langs (MQS-LANGS, 9 Oct 2026). No network, no solver run.
Must catch: a language whose own control missed its gate is never ranked; ranking is by margin, highest first.
Must NOT block: a gated language with a negative margin is still ranked (listed below zero, not dropped); an unknown
language key or --corpus beside --langs is refused before anything runs."""
import os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), ".."))
import family_run as fr
import judge_plaintext as jp

rows = [{"lang": "fr", "gated": True, "margin": -0.2}, {"lang": "it", "gated": True, "margin": 0.05},
        {"lang": "la18", "gated": False, "margin": 0.3}, {"lang": "en", "gated": True, "margin": None}]
r = fr.rank_langs(rows)
assert [x["lang"] for x in r][:2] == ["it", "fr"] and r[0]["rank"] == 1 and r[1]["rank"] == 2, r
assert all(x["rank"] is None for x in r if x["lang"] in ("la18", "en")), r
assert fr._strip_langs(["s.json", "--langs", "fr,it", "--family", "masc", "--langs=en"]) == ["s.json", "--family", "masc"]
assert "fr16" in jp.LANG_CORPORA and len(jp.LANG_CORPORA["fr16"]) == 3 and all(p.exists() for p in jp.LANG_CORPORA["fr16"])
assert len(jp.LANG_CORPORA["fr"]) == 1  # "fr" unchanged: no existing French judge figure moves
assert fr.main(["x.json", "--family", "masc", "--langs", "fr,zz"]) == 2
assert fr.main(["x.json", "--family", "masc", "--langs", "fr", "--corpus", "a.txt"]) == 2
print("ok family_run --langs: rank by margin, ungated unranked, fr16 3 files, refusals")

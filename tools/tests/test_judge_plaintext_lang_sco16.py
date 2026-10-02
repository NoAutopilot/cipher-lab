"""Offline test for tools/judge_plaintext.py's "sco16" corpus (2 Oct 2026, GAPS6-moray-wood-1568, account-4): a held-out
Middle Scots passage -- Register of the Privy Council of Scotland vol. 2 (archive.org registerofprivyc0002jjoh), taken
from text AFTER the 700,000-letter cap tools/data/sco16/build.py applies to that volume, so it is not in the corpus
(run through the same build.py cleaning, running header left as the corpus has them) -- passes the language gate; the
same passage shuffled, and a random-letter string of the same length, both fail it. 2 Oct 2026: -0.746 vs real_p05
-0.870 at N=680. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold, LANG_CORPORA

HELD_OUT_SCO16 = (
    "and in the menetyme hantis and resortis to and fra in the cuntrie as gif he wer our Soverane Lordis frie liege "
    "usand all kynde of creweltie and oppressioun his Hienes gude subjectis lyke as laitlie upoun the fyft day of Junii "
    "instant the said Johne accumpanyit with his sonnis and utheris brokin men of the cuntrie come to the landis of "
    "Erve occupiit be Hew Cathcart and thair reft certain cattell and utheris guidis pertening to him and siclike oft "
    "and diverse tymes of befoir hes hereit and opprest sindrie REGISTER OF THE COUNCIL pure bodyis of the barony of "
    "Dalmellingtoun pertening to Allane Lord Cathcart quhilk is alsua addebtit in pament of certane teindis and utheris "
    "dewiteis yeirlie to the said complenar usand thame selffis and thair guidis as pray to him at all tymes not "
    "sparing to ryde upoun thame in foraying "
)
SPEC = {"judge": {"language": "sco16", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_sco16_wired_and_on_disk():
    assert len(LANG_CORPORA["sco16"]) == 5 and all(p.exists() for p in LANG_CORPORA["sco16"])


def test_sco16_real_passage_passes():
    r = judge(SPEC, HELD_OUT_SCO16)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_sco16_shuffled_and_random_fail():
    L = list(fold(HELD_OUT_SCO16)); random.Random(5).shuffle(L)
    assert not judge(SPEC, "".join(L))["checks"]["language"]["pass"]
    rnd = random.Random(6)
    assert not judge(SPEC, "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in L))["checks"]["language"]["pass"]


if __name__ == "__main__":
    test_sco16_wired_and_on_disk(); test_sco16_real_passage_passes(); test_sco16_shuffled_and_random_fail(); print("ok")

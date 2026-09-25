"""Offline test for tools/judge_plaintext.py's "pt18" language corpus (25 Sept 2026, V6-PTCORP): a held-out
Portuguese passage -- Dom João VI's 1807 decree transferring the court to Brazil, as printed in
correiobrazilie04unkngoog (archive.org), an identifier NOT among the four files
(correiobrazilie00unkngoog, correiobrazilie02unkngoog, oinvestigadorpo03unkngoog, oinvestigadorpo05unkngoog)
committed to tools/data/pt18/ -- passes the language gate; the same passage shuffled, and a random-letter
string of the same length, both fail it. Left as raw OCR (long-s/digit misreads, hyphenation artifacts)
rather than hand-corrected, since that is what tools/data/pt18's own corpus looks like too. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_PT18 = (
    "T, ENOO procurado, por todos o» meios possíveis, con- servar a Neutralidade, de que até agora tem "
    "gozado .os IVieus Fieis, e Amados Vassallos, e a j^ezar de ter exhaurido o Meu Real Erário, e de todos "
    "os mais Sacrifícios, a que me tenho sugeitado, chegando ao excesso de fechar os Portos dos Meus "
    "Reynos àos Yassallos do Meu antigo e Leal Alliado o Rey de Gram Bretanha, expondo o Com- mercio dos "
    "Meus Vassillos a total ruína, e a sofFrec por este motivo grave prejiiizo nos rendimentos da Minha "
    "Coroa : Vejo que pelo interior do Meu Reyno marcham Tropas do Imperador dos Francezes e Rey de Itália, "
    "a quem Eu Me havia unido no Continente, na persuasão de naõ ser mais inquietado; e que as mesmas se "
    "dirigem a esta Capital : E querendo Eu evitar as funestas consequências, que^e po- dem seguir de uma "
    "defeza, que seria mais nociva que pro- veitosa, servindo s6 de derramar sangue em prejuizo da "
    "humanidade, e capaz de accender mais' a dissençaõ de amas Tropas, que tem transitado por este Reyno, "
    "com o açriuncio, e promessa de naõ commettercni a menor hosti- lidade ; conhecendo igualmente, "
    "queellas ^e dirigern muito particularmente confra a Minha Real Pessoa, e que os Meus Leaes Vasiallos "
    "seraõ oicnos inquietados, ausen- tando.Me Eu deste Reyno : Tenho resolvido, em beneficio dos mesmos "
    "Meus Vassallos, cassar com a Raynha Minha Senhora e May, e com toda a Real Família, p»ra os Estados "
    "da Atnerica, e estabelecer- Mc na Cid ide do Kio de Janeiro,"
)

SPEC = {"judge": {"language": "pt18", "letters_min": 50, "letters_max": 5000, "control_samples": 100}}


def test_pt18_real_passage_passes():
    r = judge(SPEC, HELD_OUT_PT18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_pt18_shuffled_fails():
    letters = list(fold(HELD_OUT_PT18))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_pt18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_PT18))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_pt18_corpus_folds_to_at_least_1m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["pt18"])
    assert total >= 1_000_000, total


if __name__ == "__main__":
    test_pt18_real_passage_passes()
    test_pt18_shuffled_fails()
    test_pt18_random_string_fails()
    test_pt18_corpus_folds_to_at_least_1m_letters()
    print("ok")

"""Offline test for tools/judge_plaintext.py's "en18" language corpus (26 Sept 2026, ARM-EN18): a
held-out passage of James Madison's own 1796 remarks on the Jay Treaty, from `writingsjames06madirich`
(archive.org) -- an identifier NOT among the six files (writingsjamesmo02unkngoog, writingsjamesmo11monrgoog,
writingsalbertg01gallgoog, writingsofjamesm0007unse_s2a1, writingsofjamesm0008unse, writingsofthomas09jeffiala)
committed to tools/data/en18/ -- passes the language gate; the same passage shuffled, and a random-letter
string of the same length, both fail it. Left as raw OCR (word-wrap hyphenation split across lines collapsed
to spaces, "oft" for "of" at one point) rather than hand-corrected, matching what tools/data/en18's own corpus
looks like. No network."""
import random
import sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from judge_plaintext import judge, fold

HELD_OUT_EN18 = (
    "ed the mean ing put by the United States on that article. In reply he made two remarks. First, "
    "that it was not true that Great Britain had uniformly denied the American construction of that "
    "article ; on the contrary, he believed, it could be proved, that till of late, Great Britain had "
    "uniformly admitted this construction, and had rejected the claim on no other ground than the "
    "alleged violation of the fourth article on the part of the United States. But had it been true "
    "that Great Britain had uniformly asserted a different construction of the article, and refused "
    "to accede to ours, what ought to have been done? Ought we to have at once acceded to hers ? By "
    "no means. Each party had an equal right to interpret the compact ; and if they could not agree, "
    "they ought to have done in this what they did in other cases where they could not agree; that is, "
    "have referred the settlement of the meaning of the compact to an arbitra tion. To give up the "
    "claim altogether, was to admit, either that Great Britain had a better right than the United "
    "States to explain the controverted point, or that the United States had done something which in "
    "justice called for a sacrifice of their equal right. It was evident, he thought, from this view "
    "of the subject, that the arrangements with respect to the Treaty of Peace were frequently wanting "
    "both in justice and reciprocity. It would seem, from the face of the Treaty, and the order of the "
    "articles, that the compensation for the spoliations on our trade had been combined with the "
    "execution of the Treaty of Peace; and might therefore have been viewed as a substitute for the "
    "compensation for the negroes, &c. If this was the meaning of the instrument, it could not be the "
    "less obnoxious to reasonable and fair judges. No man was more thoroughly convinced than himself "
    "of the perfect justice on which the claims of the merchants against Great Britain were founded, "
    "nor any one more desirous to see them fully in demnified. But compensation to them could never be "
    "a just substitute for the compensation due to others. It was im possible that any claims could be "
    "better founded than those of the sufferers under the seventh article of the Treaty of Peace; "
    "because they were supported by positive and ac knowledged stipulation, as well as by equity and "
    "right. Just and strong as the claims of the merchants might be, and certainly were, the United "
    "States could not be obliged to take more care of them than of the claims equally just and strong "
    "of other citizens; much less to sacrifice to them the claims for property wrongfully carried off "
    "at the close of the war, and obtaining stipulations in favor of the mercantile claims, the "
    "mercantile claims had been relinquished, and the other claims provided for ; he asked whether the "
    "complaints of the merchants would not have been as universal and as loud as they would have been "
    "just ? Besides the omissions in favor of Great Britain, already pointed out with respect to the "
    "execution of the Treaty of Peace, he observed, that conditions were annexed to the partial "
    "execution of it in the surrender of the Western posts, which increased the general inequality oft "
    "this part of the Treaty, and essentially affected the value of those objects. The value of the "
    "posts to the United States was to be estimated by their influence -- ist, on the Indian trade; "
    "2d, on the conduct and temper of the Indians towards the United States. Their influence on the "
    "Indian trade depended, principally on the exclusive command they gave to the several carrying "
    "places connected with the posts. These places were under stood to be of such importance in this "
    "respect, that those who possessed them exclusively would have a monopoly, or nearly a monopoly, "
    "of the lucrative intercourse with a great part of the savage nations. Great Britain having "
    "hitherto possessed these places exclusively, has possessed this advantage. It was expected that "
    "the exclusive transfer of them would trans fer the advantage to the United States. By the Treaty "
    "now concluded, the carrying places are to be enjoyed in common, and it will be determined by the "
    "respective advantages under which British and American traders will engage in the trade, which "
    "of them is to share most in it. In this point of view he thought the regulation highly impolitic "
    "and injurious. He would say little of the advantage which the British would have in their "
    "superior capital: that must be encountered in all our commercial rivalships. But there was "
    "another con sideration which ought to have great weight on this subject. The goods imported for "
    "the Indian trade through Canada pay no duties. Those imported through the United States for "
    "-that trade, will have paid duties from seven to ten per cent., and every one must see that a "
    "drawback is impracti cable, or would be attended with an expense which the busi ness would not "
    "bear. So far, then, as the importance of the posts is to be considered in a commercial view, "
    "they are, in a very great measure, stripped of it by the condition annexed to the surrender of t"
)

SPEC = {"judge": {"language": "en18", "letters_min": 600, "letters_max": 5000, "control_samples": 100}}


def test_en18_real_passage_passes():
    r = judge(SPEC, HELD_OUT_EN18)
    assert r["checks"]["language"]["pass"], r["checks"]["language"]


def test_en18_shuffled_fails():
    letters = list(fold(HELD_OUT_EN18))
    random.Random(7).shuffle(letters)
    r = judge(SPEC, "".join(letters))
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_en18_random_string_fails():
    rnd = random.Random(11)
    s = "".join(rnd.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(len(fold(HELD_OUT_EN18))))
    r = judge(SPEC, s)
    assert not r["checks"]["language"]["pass"], r["checks"]["language"]


def test_en18_corpus_folds_to_at_least_1_5m_letters():
    from judge_plaintext import LANG_CORPORA, read_corpus
    total = sum(len(fold(read_corpus(p))) for p in LANG_CORPORA["en18"])
    assert total >= 1_500_000, total


if __name__ == "__main__":
    test_en18_real_passage_passes()
    test_en18_shuffled_fails()
    test_en18_random_string_fails()
    test_en18_corpus_folds_to_at_least_1_5m_letters()
    print("ok")

"""Offline tests for tools/sameday.py (MQS-SAMEDAY, 9 Oct 2026). Run: python3 -m pytest tools/tests/test_sameday.py"""
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import sameday as sd  # noqa: E402

LETTERS = [
    ("A", "1586-07-10", "Babington", "the queen of scots desires the sixe gentlemen to proceed with speed and secrecy"),
    ("B", "1586-07-12", "Morgan", "tell paget the sixe gentlemen must proceed with speed in this enterprise"),
    ("C", "1586-09-30", "Mendoza", "the sixe gentlemen must proceed with speed and the spanish forces land"),
    ("D", "1586-07-11", "Curle", "of the said and to the of the said and to the"),
]


def write(tmp_path):
    p = tmp_path / "letters.tsv"
    p.write_text("id\tdate\trecipient\ttext\n" + "".join("\t".join(r) + "\n" for r in LETTERS), encoding="utf-8")
    return str(p)


def idx_and(path):
    letters = sd.load_letters(path)
    return letters, sd.Index(letters), [L["d"] for L in letters]


def test_window_letter_ranked_and_crib(tmp_path):
    letters, idx, dates = idx_and(write(tmp_path))
    rtoks = sd.tokens("he says the sixe gentlemen must ? with speed")
    ids = sd.window_ids(dates, sd.date(1586, 7, 11), 7, set())
    score, found = sd.window_score(idx, {g for g, _ in sd.trigrams(rtoks)}, ids)
    assert ("sixe", "gentlemen", "must") in found and score > 0
    props = sd.cribs(idx, rtoks, ids)
    assert [(w, src) for _, w, _, src in props] == [("proceed", [1])]


def test_outside_window(tmp_path):
    letters, idx, dates = idx_and(write(tmp_path))
    ids = sd.window_ids(dates, sd.date(1586, 7, 11), 7, set())
    assert 2 not in ids  # C, 30 Sept, is 81 days away


def test_stopword_and_gap():
    grams = [g for g, _ in sd.trigrams(sd.tokens("of the said ? speed and secrecy"))]
    assert ("of", "the", "said") not in grams
    assert all(None not in g for g in grams)
    assert ("said", "speed", "and") not in grams


def test_exclude_self(tmp_path):
    letters, idx, dates = idx_and(write(tmp_path))
    rtoks = sd.tokens(LETTERS[0][3])
    ex = sd.excluded(letters, ["A"])
    ids = sd.window_ids(dates, dates[0], 7, ex)
    assert 0 not in ids
    _, found = sd.window_score(idx, {g for g, _ in sd.trigrams(rtoks)}, ids)
    assert ("desires", "the", "sixe") not in found  # only in A itself


def test_date_rank(tmp_path):
    letters, idx, dates = idx_and(write(tmp_path))
    rtoks = sd.tokens("tell paget the sixe gentlemen must ? with speed in this enterprise")
    rgrams = {g for g, _ in sd.trigrams(rtoks)}
    scores = sd.date_ranks(idx, rgrams, dates, 3, sd.excluded(letters, []), sorted(set(dates)))
    assert scores[sd.date(1586, 7, 12)] > scores[sd.date(1586, 9, 30)]


def test_parse_date_and_edition():
    assert sd.parse_date("Sir, Fort William, 15th Sept. 1798.") == sd.date(1798, 9, 15)
    assert sd.parse_date("My Lorp, Fort William, October 11, 1798.") == sd.date(1798, 10, 11)
    text = "No. I.\nThe Earl of Mornington to Mr. Dundas.\nSir, Fort William, 2d July, 1798.\n" + "word " * 130 + \
           "\nNo. II.\nMr. Dundas to the Earl of Mornington.\nSir, London, 3d July, 1798.\n" + "word " * 130
    rows = sd.parse_edition(text, "Mornington to", 120, "v1 ")
    assert [(r["id"], r["date"], r["recipient"]) for r in rows] == [("v1 No. I", "1798-07-02", "Mr. Dundas")]

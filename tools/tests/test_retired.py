#!/usr/bin/env python3
"""Offline pytest test for tools/retired.py (RETIRED-REGISTER, 9 Oct 2026).

Builds fixture ciphers/<t>/NOTES.md, HYPOTHESES.md and research/TX-REGISTER.tsv under tmp_path and checks the
docstring's scope: must catch a [retired] line with no reopen condition (--check exits 1), must not block a
[retired] line naming "a different instrument or new material" (--check exits 0); repeated identical lines are
written once; negations are skipped. No network, no dependence on the real repository's folders.

Run: /root/.local/bin/pytest tools/tests/test_retired.py -q
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(ROOT, "tools"))
import retired  # noqa: E402

GOOD = ("- [retired] key-rebuild: tools/homophonic_anneal.py failed its control three times (0.31, 0.29, 0.33), "
        "3 Oct 2026, rule 3 third-attempt clause; reopened only by a different instrument or new material\n")
BAD = "- [retired] image-check: the crop compare is [retired] after three FAILs.\n"
HYP = ("| masc | X1 | 0.41 | not run | **retired: untested-by-this-tool** (rule 3) | needs longer ciphertext |\n"
       "No instrument here has failed its gate, so nothing is retired.\n")
TX = ("id\tcampaign\tfamily\tmechanism_attacked\tunit_or_pool\tdev_result\teval_result\teval_looks\tverdict\treason"
      "\tsource_file\tdate\n"
      "M9\ttxeng\tFour-times tile read\tC3\tdev\tfixed 1 / broken 3\tnot taken\t0\tretired\tretired (three fixes, "
      "all wrong way); reopen only with a new reference sheet\tx.md:1\t2026-10-09\n"
      "M10\ttxeng\tOther\tC1\tdev\tfixed 2\tnot taken\t0\tdev-FAIL\tFAIL\tx.md:2\t2026-10-09\n")


def make(tmp_path, notes):
    d = tmp_path / "ciphers" / "t1"
    d.mkdir(parents=True)
    (d / "NOTES.md").write_text("# t1\n\nStatus: partial\n\n" + notes)
    (d / "HYPOTHESES.md").write_text(HYP)
    (tmp_path / "research").mkdir()
    (tmp_path / "research" / "TX-REGISTER.tsv").write_text(TX)
    return str(tmp_path)


def test_must_not_block_named_reopen(tmp_path):
    root = make(tmp_path, GOOD + GOOD)
    rows = retired.build_rows(root)
    notes = [r for r in rows if r["source"].startswith("ciphers/t1/NOTES.md")]
    assert len(notes) == 1 and "(+1 identical)" in notes[0]["source"]
    r = notes[0]
    assert r["step"] == "key-rebuild"
    assert "homophonic_anneal.py" in r["instrument"]
    assert r["date"] == "3 Oct 2026"
    assert "0.31" in r["attempts"]
    assert r["why"] == "rule 3 third-attempt clause"
    assert "different instrument or new material" in r["reopen_when"]
    hyp = [r for r in rows if "HYPOTHESES" in r["source"]]
    assert len(hyp) == 1  # the negation line is skipped
    assert "longer ciphertext" in hyp[0]["reopen_when"]
    tx = [r for r in rows if r["folder"] == "transcription"]
    assert len(tx) == 1 and tx[0]["step"] == "Four-times tile read"
    assert retired.main(["--root", root, "--check"]) == 0
    assert (tmp_path / "RETIRED.tsv").read_text().splitlines()[0].split("\t") == retired.COLS


def test_must_catch_missing_reopen(tmp_path, capsys):
    root = make(tmp_path, GOOD + BAD)
    rows = retired.build_rows(root)
    bad = [r for r in rows if r["reopen_when"] == "not stated"]
    assert len(bad) == 1 and bad[0]["step"] == "image-check"
    assert retired.main(["--root", root, "--check"]) == 1
    assert "not stated: ciphers/t1/NOTES.md" in capsys.readouterr().out


def test_unparseable_line_kept(tmp_path):
    root = make(tmp_path, "[retired]\n")
    rows = [r for r in retired.build_rows(root) if "NOTES" in r["source"]]
    assert len(rows) == 1  # never dropped

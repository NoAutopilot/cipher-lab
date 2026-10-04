"""Offline tests for ciphers/eckert-1864/decode.py's possessive option and CollisionGuard (RUN3-ECK62, 4 Oct 2026).

Must catch: a possessive code word ("Kettle's" = Longstreet's); a code word the clerk wrote in clear inside a joined
word ("bush whack hers") or in a common English phrase ("the opinion of"). Must NOT block: a code word whose meaning
reads better in context than the clear word ("to Grapes" = to Washington), numerals, or anything when the options are off.
"""
import sys, unittest
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[2] / "ciphers" / "eckert-1864"))
import decode  # noqa: E402

KEY = {"kettle": ("Longstreet", "H", "word"), "whack": ("Towards", "H", "word"), "opinion": ("Field", "H", "word"),
       "grapes": ("Washington", "H", "word"), "persons": ("5 (numeral)", "H", "numeral")}
CORPUS = ["the bushwhackers were driven off. to bushwhack them. bushwhack again. in the opinion of the general, the opinion of all. "
          "it is my opinion of it. go to washington at once. to washington. the grapes are ripe. five persons came."]


class TestPossessive(unittest.TestCase):
    def test_off_by_default(self):
        r, c = decode.decode_entry("Kettle's corps", KEY)
        self.assertEqual(r, "Kettle's corps")
        self.assertEqual(c["H"], 0)

    def test_on(self):
        r, c = decode.decode_entry("Kettle's corps", KEY, possessive=True)
        self.assertEqual(r, "[Longstreet]'s corps")
        self.assertEqual(c["H"], 1)

    def test_possessive_numeral_terminates(self):
        # RUN3-ECK62 bug: a possessive numeral ("persons's") matched in the main lookup but not in the numeral-run
        # loop, which then never advanced (infinite loop on mssEC 18 book 2, "Brown's" = 1)
        r, c = decode.decode_entry("persons's men", KEY, possessive=True)
        self.assertEqual(r, "[5]'s men")
        self.assertEqual(c["H"], 1)

    def test_curly(self):
        r, _ = decode.decode_entry("Kettle’s corps", KEY, possessive=True)
        self.assertEqual(r, "[Longstreet]'s corps")


class TestGuard(unittest.TestCase):
    def setUp(self):
        self.g = decode.CollisionGuard(CORPUS)

    def test_joined_word(self):
        got = []
        r, c = decode.decode_entry("the bush whack hers fled", KEY, guard=self.g, guarded=got)
        self.assertIn("whack", r)
        self.assertNotIn("[Towards]", r)
        self.assertEqual([x[3] for x in got], ["J"])
        self.assertEqual(c["H"], 0)

    def test_phrase(self):
        r, _ = decode.decode_entry("in the opinion of the general", KEY, guard=self.g)
        self.assertNotIn("[Field]", r)

    def test_meaning_fits_better_not_blocked(self):
        r, c = decode.decode_entry("go to Grapes at once", KEY, guard=self.g)
        self.assertIn("[Washington]", r)
        self.assertEqual(c["H"], 1)

    def test_numeral_never_guarded(self):
        r, _ = decode.decode_entry("five persons came", KEY, guard=self.g)
        self.assertIn("[5]", r)

    def test_off_by_default(self):
        r, _ = decode.decode_entry("in the opinion of the general", KEY)
        self.assertIn("[Field]", r)


if __name__ == "__main__":
    unittest.main()

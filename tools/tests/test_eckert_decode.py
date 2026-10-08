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


class TestFixFm1Notes(unittest.TestCase):
    """FIX-FM1 (8 Oct 2026): per-entry "variant:" / "split:" / "plain:" notes and the ordinal ending, from the
    FV-FM1 audit of E160/E163/E164. Must catch: a variant spelling (poney = Pony = 9, graded as the note says), a count
    and calibre written side by side ("six 3-inch"), an ordinal ("Glory" + th = 17th). Must NOT: split a run without
    the note, or read a variant token that carries no note."""
    K = {"pony": ("9 (numeral)", "H", "numeral"), "pledge": ("6 (numeral)", "H", "numeral"),
         "pebble": ("3 (numeral)", "H", "numeral"), "glory": ("17 (numeral)", "H", "numeral"),
         "weasel": ("Steam", "H", "word")}

    def run_entry(self, lines):
        return decode.decode_entry(decode.entry_text(["hdr"] + lines), self.K)

    def test_variant_numeral(self):
        r, c = self.run_entry(["down poney compare", "variant: poney=Pony:H"])
        self.assertIn("down [9] compare", r)
        self.assertEqual(c["H"], 1)

    def test_variant_grade_override(self):
        r, c = self.run_entry(["weasler ok", "variant: weasler=Weaseler:M"])
        self.assertEqual(r, "[Steam]er ok")
        self.assertEqual((c["M"], c["H"]), (1, 0))

    def test_no_note_no_variant(self):
        r, c = self.run_entry(["down poney compare"])
        self.assertIn("poney", r)
        self.assertEqual(c["H"], 0)

    def test_split_and_default_sum(self):
        r, _ = self.run_entry(["pledge pebble inch", "split: pebble"])
        self.assertEqual(r, "[6] [3] inch")
        r, _ = self.run_entry(["pledge pebble inch"])
        self.assertEqual(r, "[9] inch")

    def test_ordinal(self):
        r, c = self.run_entry(["gloryth Amos"])
        self.assertEqual(r, "[17]th Amos")
        self.assertEqual(c["H"], 1)

    def test_th_on_non_numeral_untouched(self):
        r, _ = self.run_entry(["weaselth"])
        self.assertEqual(r, "weaselth")


if __name__ == "__main__":
    unittest.main()

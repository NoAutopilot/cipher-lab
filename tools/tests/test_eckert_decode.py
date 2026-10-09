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



class TestFixFm3Notes(unittest.TestCase):
    """FIX-FM3 (9 Oct 2026): "plain-at:", "gloss:" and "join:" notes from the FV-FM3a/FM3c/MS18 and AUD2-LEDGER audits.
    Must catch: the n-th occurrence of a word plain while another stays a code word (E171 Washington, E177 Webster);
    a printed-source meaning no key row has (E202 Hero = Johnson, E206 Orphan = Sigel) graded as the note says;
    "one hundred and three" joined across a plain "and" (E171). Must NOT: touch a word with no note, drop an "and"
    that is not before a joined numeral, or read a gloss token with no note."""
    K = {"washington": ("Volunteer", "H", "word"), "plug": ("1 (numeral)", "H", "numeral"),
         "publish": ("100 (numeral)", "H", "numeral"), "pebble": ("3 (numeral)", "H", "numeral"),
         "pony": ("9 (numeral)", "H", "numeral")}

    def run_entry(self, lines):
        return decode.decode_entry(decode.entry_text(["hdr"] + lines), self.K)

    def test_plain_at_first_only(self):
        r, c = self.run_entry(["to Washington then Washington end", "plain-at: washington#1"])
        self.assertEqual(r, "to Washington then [Volunteer] end")
        self.assertEqual(c["H"], 1)

    def test_plain_at_absent_means_both_read(self):
        r, c = self.run_entry(["to Washington then Washington end"])
        self.assertEqual(r.count("[Volunteer]"), 2)

    def test_gloss_grade_and_meaning(self):
        r, c = self.run_entry(["that Hero be relieved", "gloss: hero=R._W._Johnson:C"])
        self.assertEqual(r, "that [R. W. Johnson] be relieved")
        self.assertEqual((c["C"], c["H"]), (1, 0))

    def test_gloss_needs_note(self):
        r, c = self.run_entry(["that Hero be relieved"])
        self.assertEqual(r, "that Hero be relieved")

    def test_join_across_and(self):
        r, c = self.run_entry(["the plug publish and pebble men", "join: pebble"])
        self.assertEqual(r, "the [103] men")
        self.assertEqual(c["H"], 3)
        r, _ = self.run_entry(["the plug publish and pebble men"])
        self.assertEqual(r, "the [100] and [3] men")

    def test_join_leaves_other_and(self):
        r, _ = self.run_entry(["bread and butter plug", "join: pebble"])
        self.assertEqual(r, "bread and butter [1]")

    def test_split_after_join_independent(self):
        r, _ = self.run_entry(["pony publish pebble", "split: publish"])
        self.assertEqual(r, "[9] [103]")


class TestHolderExportNotes(unittest.TestCase):
    """HOLDER-EXPORT fix (9 Oct 2026): "merge:" and "graded:" notes, and the tokens list, for carrying the audits' hand
    grades into the derived block (E33 pan-a-ma, E57 Ann/collared I, E68 Jones M, E122 pos/Joke unread).
    Must catch: a code word the clerk split across a space or a line ("pana. ma" = Panama) read once; a word the audit
    grades by hand kept as written and counted with that grade (I, M or U); every counted token listed once in reading
    order. Must NOT: merge the same words when they are not adjacent, touch a word with no note, or change the reading
    or counts when a tokens list is passed."""
    K = {"panama": ("Cavalry", "H", "word"), "ann": ("1 AM (time word)", "H", "time"),
         "harrow": ("20 (numeral)", "H", "numeral"), "peach": ("2 (numeral)", "H", "numeral"),
         "weasel": ("Steam", "H", "word")}

    def run_entry(self, lines, tokens=None):
        return decode.decode_entry(decode.entry_text(["hdr"] + lines), self.K, tokens=tokens)

    def test_merge_across_space_and_line(self):
        r, c = self.run_entry(["for your pan - a.", "ma here", "the pan -", "a ma Division", "merge: pana+ma"])
        self.assertEqual(r, "for your [Cavalry] here the [Cavalry] Division")
        self.assertEqual(c["H"], 2)

    def test_merge_needs_adjacent(self):
        r, c = self.run_entry(["pana went ma", "merge: pana+ma"])
        self.assertEqual(r, "pana went ma")
        self.assertEqual(c["H"], 0)

    def test_graded_kept_as_written(self):
        r, c = self.run_entry(["call at Ann a pol is for collared men", "graded: ann:I collared:I pos:U"])
        self.assertEqual(r, "call at Ann a pol is for collared men")
        self.assertEqual((c["I"], c["H"]), (2, 0))
        r, c = self.run_entry(["insert Jones cipher", "graded: jones"])
        self.assertEqual((r, c["M"]), ("insert Jones cipher", 1))
        r, c = self.run_entry(["at pos there", "graded: pos:U"])
        self.assertEqual((r, c.get("U")), ("at pos there", 1))

    def test_no_note_reads_key(self):
        r, c = self.run_entry(["call at Ann a pol is"])
        self.assertIn("{time: 1 AM}", r)

    def test_tokens_list(self):
        toks = []
        r, c = self.run_entry(["harrow peach weaselers Jones", "graded: jones:M"], tokens=toks)
        self.assertEqual(r, "[22] [Steam]ers Jones")
        self.assertEqual([(t[1], t[2], t[3]) for t in toks],
                         [("harrow", "20 (numeral)", "H"), ("peach", "2 (numeral)", "H"), ("weaselers", "Steam", "H"),
                          ("Jones", "", "M")])
        self.assertEqual(self.run_entry(["harrow peach weaselers Jones", "graded: jones:M"]), (r, c))

if __name__ == "__main__":
    unittest.main()

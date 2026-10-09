"""Offline tests for tools/pile_register.py (MQS-PILE-REGISTER, 9 Oct 2026).

Must catch: held rows built through holder_export.build_rows (the holder_export fixture); a referenced letter that is
already held reported 'held?', not counted twice; timeline order by date with undated last; 'your favour of the 19°
instant' resolved to the letter's month; 'of the 24 ult' to the month before; 'of Oct. 20' given the letter's year (or
the year before when that date is after the letter); 'votre lettre du 3 mars'; --check failing on a stale register.
Must NOT flag: a date line that is not a reference (a segment boundary, never a lead); 'your letter' with no date after
it; a reference whose date matches a DATES row (status 'held', not 'lead').
"""
import io
import shutil
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from datetime import date
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import pile_register as pr  # noqa: E402

FIX = HERE / "fixtures" / "holder_export"

EDITION = """WILLIAM SHEPARD TO JAMES BOWDOIN.
NorTHAMPTON, 30th Decemr, 1786.
Sir, -- I have the honour to inform your Excellency of our march.

JAMES BOWDOIN TO WILLIAM SHEPARD.
Boston, Jany 21, 1787.
Sir, --I have received your favour of the 19° instant. Your letter came late.
In your letter of the 24 ult you said more.

BOWDOIN TO ARMSTRONG.
Paris, Feb. 2, 1806.
Sir, -- your letter of Oct. 20 and my letter of Dec 31 are both lost; your letter of the 3d we have.

UN AMI A BOWDOIN.
Paris, 10 avril 1806.
J'ai recu votre lettre du 3 mars.
"""


def quiet(fn, *a):
    so, se = io.StringIO(), io.StringIO()
    with redirect_stdout(so), redirect_stderr(se):
        rc = fn(*a)
    return rc, so.getvalue(), se.getvalue()


class Scan(unittest.TestCase):
    def setUp(self):
        self.dates = [date(1787, 1, 21), date(1806, 2, 2), date(1806, 4, 10), date(1786, 12, 30)]
        self.leads = pr.scan_refs(EDITION, self.dates, window=0, tol=1)
        self.by = {(x["letter"], x["refers_to"]): x for x in self.leads}

    def test_segments_at_date_lines(self):
        segs = pr.segments(EDITION)
        self.assertEqual([s[0] for s in segs], [date(1786, 12, 30), date(1787, 1, 21), date(1806, 2, 2),
                                                date(1806, 4, 10)])

    def test_instant_and_ult(self):
        self.assertEqual(self.by[("1787-01-21", "1787-01-19")]["how"], "instant")
        self.assertEqual(self.by[("1787-01-21", "1786-12-24")]["how"], "ult")

    def test_explicit_month_year_rolls_back(self):
        self.assertEqual(self.by[("1806-02-02", "1805-10-20")]["how"], "explicit")
        self.assertIn(("1806-02-02", "1805-12-31"), self.by)

    def test_bare_day_inferred(self):
        x = self.by[("1806-02-02", "1806-01-03")]
        self.assertEqual(x["how"], "inferred")

    def test_french(self):
        self.assertEqual(self.by[("1806-04-10", "1806-03-03")]["how"], "explicit")

    def test_no_date_no_lead(self):
        # 'Your letter came late.' and the date lines themselves give no lead
        self.assertEqual(sum(x["letter"] == "1787-01-21" for x in self.leads), 2)
        self.assertEqual(sum(x["letter"] == "1786-12-30" for x in self.leads), 0)
        self.assertEqual(len(self.leads), 6)

    def test_held_vs_lead(self):
        dates = self.dates + [date(1787, 1, 19)]
        leads = pr.scan_refs(EDITION, dates, window=0, tol=1)
        st = {x["refers_to"]: x["status"] for x in leads}
        self.assertEqual(st["1787-01-19"], "held")
        self.assertEqual(st["1786-12-24"], "lead")

    def test_window_selects_letters(self):
        leads = pr.scan_refs(EDITION, [date(1806, 4, 12)], window=3)
        self.assertEqual({x["letter"] for x in leads}, {"1806-04-10"})
        self.assertEqual(pr.scan_refs(EDITION, [date(1806, 4, 20)], window=3), [])

    def test_dateline_not_body(self):
        self.assertIsNone(pr.parse_dateline("we marched on the 21 Jany 1787 and the troops were in good order, sir"))
        self.assertEqual(pr.parse_dateline("Paris, Noy. 34, 1805."), date(1805, 11, 3))


class Register(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def argv(self, *extra):
        return [str(FIX / "list.tsv"), "--status", str(FIX / "status.json"), "--repo-root", str(FIX),
                "--out", str(self.tmp / "reg")] + list(extra)

    def test_held_rows_from_holder_export(self):
        rc, out, _ = quiet(pr.main, self.argv())
        self.assertEqual(rc, 0)
        rows = (self.tmp / "reg.tsv").read_text().splitlines()
        self.assertEqual(rows[0].split("\t"), pr.REG_COLS)
        ids = [r.split("\t")[6] for r in rows[1:]]
        self.assertEqual(sorted(ids), ["DN7", "T1", "T2", "T3"])  # T1/T2 split by holder_export's own rule

    def test_referenced_and_held_question(self):
        refs = self.tmp / "refs.tsv"
        refs.write_text("date\tfrom\tto\tmentioned_in\tnote\n1864-01-02\tGamma\tBeta\tT3\tsays 'my wire of the 2d'\n"
                        "1864-01-09\tBeta\tAlpha\tT3\tanswer not held\n\tX\tY\tT1\tundated mention\n")
        quiet(pr.main, self.argv("--refs", str(refs)))
        rows = [r.split("\t") for r in (self.tmp / "reg.tsv").read_text().splitlines()[1:]]
        cls = {r[6]: r[0] for r in rows}
        self.assertEqual(cls["ref1"], "held?")
        self.assertEqual(cls["ref2"], "referenced")
        tl = (self.tmp / "reg-timeline.txt").read_text().splitlines()
        body = [l for l in tl if not l.startswith("#")]
        self.assertTrue(body[-1].startswith("undated"))
        isos = [l[:10] for l in body if not l.startswith("undated")]
        self.assertEqual(isos, sorted(isos))
        self.assertIn("4 held, 2 referenced-not-held, 1 references matching a held row", tl[-1])

    def test_check_stale(self):
        quiet(pr.main, self.argv())
        self.assertEqual(quiet(pr.main, self.argv("--check"))[0], 0)
        p = self.tmp / "reg-timeline.txt"
        p.write_text(p.read_text() + "edited\n")
        self.assertEqual(quiet(pr.main, self.argv("--check"))[0], 1)

    def test_refs_scan_cli(self):
        ed, dates, out = self.tmp / "ed.txt", self.tmp / "dates.tsv", self.tmp / "leads.tsv"
        ed.write_text(EDITION)
        dates.write_text("iso\n1787-01-21\n")
        rc, _, err = quiet(pr.main, ["--refs-scan", str(ed), "--dates", str(dates), "--scan-out", str(out)])
        self.assertEqual(rc, 0)
        self.assertIn("leads, not decisions", err)
        self.assertEqual(len(out.read_text().splitlines()), 3)


if __name__ == "__main__":
    unittest.main()

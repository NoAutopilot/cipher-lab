"""Offline tests for tools/holder_export.py (HOLDER-EXPORT, 9 Oct 2026; review fixes the same night).

Must catch: a change in the column order a holder imports by (alias and number first); a list row naming two telegrams
the reading keeps apart not split into two rows; a ledger entry holding two telegrams not labelled '2 telegrams in this
entry'; a '(second telegram)' row not cut to its part (text, reading, code words and counts); a 'graded:' token of the
folder's decoder not listed and counted as written; a count that differs from the audited completeness not reported,
and --check passing over it unless it is accepted; --check passing over stale outputs; the .xlsx step failing the whole
run when openpyxl is missing; '[SIGN-OFF]' or an e-mail address (rule 9) leaking into any output; a grade letter left
unexplained; a tab or line break inside a cell; a CSV without the byte-order mark Excel needs; a prior-print cell with
no source or no search date passing as complete; the plain-text reading keeping code-book markup.
Must NOT block: a list row with no status.json result (written from the list's own fields, warned only); a passing
result missing from the list (printed as drift, not fatal).
Fixture: tools/tests/fixtures/holder_export/ (three list rows, a toy ledger with its own decode.py, a number cipher in
the tools/decode_key.py layout); the 'graded:' and part tests build a one-entry ledger in a temporary directory with
the real ciphers/eckert-1864/decode.py.
"""
import csv
import io
import json
import re
import shutil
import subprocess
import sys
import tempfile
import unittest
from contextlib import redirect_stderr, redirect_stdout
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE.parent))
import holder_export as he  # noqa: E402

FIX = HERE / "fixtures" / "holder_export"
ECKERT_DECODE = HERE.parents[1] / "ciphers" / "eckert-1864" / "decode.py"
EXPECTED = [
    "CONTENTdm collection alias", "CONTENTdm number", "record level", "row id (our entry)", "holder call number",
    "page title (Digital Library) or pages read", "telegram numbers on this page (holder 'Telegram Number' field)",
    "Digital Library URL", "date and time as written", "date (YYYY-MM-DD)", "from", "to", "place", "transcribed from",
    "ledger/page text as we transcribed it", "reading (marked up)", "reading (plain text)", "summary (one sentence)",
    "code words and meanings", "cipher book or key used", "cipher book (Digital Library URL)",
    "uncertain or unread words", "how much is read", "adds less? (and why)", "prior print checked",
    "partly in print?", "prior-publication check (class)", "reading (repository link)",
    "search log (repository link)", "suggested credit line",
]
EMAIL = re.compile(r"[\w.+-]+@[\w-]+\.[\w.]+")


def run(out, status=None, extra=(), lst=None, root=None):
    argv = [str(lst or FIX / "list.tsv"), "--out", str(out), "--status", str(status or FIX / "status.json"),
            "--repo-root", str(root or FIX), "--url-template", "https://example.org/{alias}/id/{pointer}",
            "--alias", "Demo=demo1", "--alias", "mssDN=demo2", "--holder", "the Demo Library",
            "--prepared", "1 Oct 2026",
            "--select-class", "N3,N4", "--select-min-audits", "2"] + list(extra)
    so, se = io.StringIO(), io.StringIO()
    with redirect_stdout(so), redirect_stderr(se):
        rc = he.main(argv)
    return rc, so.getvalue(), se.getvalue()


def rows_of(stem):
    with open(f"{stem}.csv", encoding="utf-8-sig") as f:
        rows = list(csv.reader(f))
    return rows[0], [dict(zip(rows[0], r)) for r in rows[1:]]


class TestHolderExport(unittest.TestCase):
    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        self.stem = self.tmp / "out" / "demo"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def test_column_order(self):
        self.assertEqual(he.COLUMNS, EXPECTED)
        run(self.stem, extra=["--no-xlsx"])
        head, _ = rows_of(self.stem)
        self.assertEqual(head, EXPECTED)
        tsv = Path(f"{self.stem}.tsv").read_text(encoding="utf-8").splitlines()
        self.assertEqual(tsv[0].split("\t"), EXPECTED)
        for line in tsv:  # no tab or line break inside a cell: every line has exactly the header's field count
            self.assertEqual(len(line.split("\t")), len(EXPECTED))
        self.assertEqual(he.columns("Demo")[4], "Demo call number")

    def test_csv_bom_tsv_plain(self):
        run(self.stem, extra=["--no-xlsx"])
        self.assertTrue(Path(f"{self.stem}.csv").read_bytes().startswith(b"\xef\xbb\xbf"))
        self.assertFalse(Path(f"{self.stem}.tsv").read_bytes().startswith(b"\xef\xbb\xbf"))
        readme = " ".join(Path(f"{self.stem}-README.txt").read_text(encoding="utf-8").split())
        self.assertIn("Who made this", readme)
        self.assertIn("AI agents (Claude models)", readme)

    def test_split_and_two_telegram_note(self):
        rc, out, _ = run(self.stem, extra=["--no-xlsx"])
        self.assertEqual(rc, 0)
        _, rows = rows_of(self.stem)
        self.assertEqual(len(rows), 4)  # T1 and T2 split, T3 one row, DN7 one row
        self.assertEqual([r["row id (our entry)"] for r in rows], ["T1", "T2", "T3", "DN7"])
        t1, t2, t3, dn = rows
        self.assertEqual((t1["from"], t1["to"]), ("Alpha", "Beta"))
        self.assertEqual((t2["from"], t2["to"]), ("Gamma", "Beta"))
        self.assertEqual(t1["date and time as written"], "1 Jan 1864, 9 AM")
        self.assertEqual(t1["date (YYYY-MM-DD)"], "1864-01-01")
        self.assertEqual(t2["date and time as written"], "2 Jan 1864, 10 AM")
        self.assertFalse(t1["reading (marked up)"].startswith("("))
        self.assertTrue(t3["reading (marked up)"].startswith("(2 telegrams in this entry)"), t3["reading (marked up)"])
        # holder keys: alias + number, page title from the cached record, first pointer, continuation named
        self.assertEqual(t1["CONTENTdm number"], "101")
        self.assertEqual(t1["CONTENTdm collection alias"], "demo1")
        self.assertEqual(t1["record level"], "page (of a compound object)")
        self.assertEqual(t1["holder call number"], "Demo vol 1")
        self.assertEqual(t1["Digital Library URL"], "https://example.org/demo1/id/101")
        self.assertEqual(t3["page title (Digital Library) or pages read"], "Page 2; continues on Page 3 (CONTENTdm 103)")
        self.assertEqual(t1["place"], "Washington")
        # ledger lines kept apart with ' / ', orchestrator notes dropped
        self.assertIn(" / ", t1["ledger/page text as we transcribed it"])
        self.assertNotIn("note:", t1["ledger/page text as we transcribed it"])
        # decode-key layout: page pointer from the manifest, groups line by line, unread group marked [?n]
        self.assertEqual(dn["page title (Digital Library) or pages read"], "pages read: p1 (CONTENTdm 701)")
        self.assertEqual(dn["record level"], "compound object (letter)")
        self.assertEqual(dn["ledger/page text as we transcribed it"], "10 11 / 12 13")
        self.assertIn("13 = part or parti (uncertain)", dn["code words and meanings"])
        self.assertIn("12 (unread)", dn["uncertain or unread words"])
        self.assertNotRegex(dn["reading (marked up)"], r"\[\d+\]")
        # selection drift is reported (DN7 has one audit), not fatal
        self.assertIn("listed, now fails", out)

    def test_grades_and_wording(self):
        run(self.stem, extra=["--no-xlsx"])
        _, rows = rows_of(self.stem)
        t1 = rows[0]
        self.assertIn("Apple = General Beta (from the cipher book)", t1["code words and meanings"])
        self.assertIn("Plum = Richmond (uncertain)", t1["uncertain or unread words"])
        self.assertIn("Lime = Alpha (inferred)", t1["uncertain or unread words"])
        self.assertEqual(t1["how much is read"],
                         "3 of 5 code words read from the cipher book; 1 inferred, 1 uncertain. Overall: deciphered")
        self.assertNotRegex(t1["how much is read"], r"\bD\d\b|%")
        self.assertTrue(t1["adds less? (and why)"].startswith("yes: much of the message"))
        self.assertNotIn("audit flag", " ".join(r["adds less? (and why)"] for r in rows))
        self.assertTrue(t1["prior print checked"].startswith("Not found in the Demo Records"))
        self.assertTrue(t1["prior-publication check (class)"].startswith("N4: no prior decipherment located"))
        self.assertIn("two separate AI review passes", t1["prior-publication check (class)"])
        self.assertEqual(rows[2]["partly in print?"], "Its reply is printed in Demo Records vol. 2 p.7.")
        for r in rows:
            for col in ("code words and meanings", "uncertain or unread words", "how much is read"):
                self.assertIsNone(re.search(r"\([HCSIMU]\)", r[col]), (col, r[col]))
            # rule 10: no priority claim (the N4 meaning's own caveat 'unpublished work not excluded' is allowed)
            text = " ".join(r.values()).lower()
            self.assertIsNone(re.search(r"first decipherment|previously unread|newly recovered|never printed|"
                                        r"unpublished plaintext|\bis unpublished", text), text)

    def test_no_signoff_or_email_leak(self):
        run(self.stem)
        for ext in ("csv", "tsv"):
            text = Path(f"{self.stem}.{ext}").read_text(encoding="utf-8")
            self.assertNotIn("[SIGN-OFF]", text)
            self.assertIsNone(EMAIL.search(text), ext)
        if Path(f"{self.stem}.xlsx").exists():
            import openpyxl
            wb = openpyxl.load_workbook(f"{self.stem}.xlsx")
            for ws in wb.worksheets:
                for row in ws.iter_rows(values_only=True):
                    for v in row:
                        self.assertNotIn("[SIGN-OFF]", str(v or ""))
                        self.assertIsNone(EMAIL.search(str(v or "")), v)

    def test_fallback_without_openpyxl(self):
        saved = {k: sys.modules[k] for k in list(sys.modules) if k == "openpyxl" or k.startswith("openpyxl.")}
        sys.modules["openpyxl"] = None  # import openpyxl now raises ImportError
        try:
            rc, out, err = run(self.stem)
        finally:
            del sys.modules["openpyxl"]
            sys.modules.update(saved)
        self.assertEqual(rc, 0)
        self.assertTrue(Path(f"{self.stem}.csv").exists())
        self.assertTrue(Path(f"{self.stem}.tsv").exists())
        self.assertFalse(Path(f"{self.stem}.xlsx").exists())
        self.assertIn("openpyxl not importable", err)

    def test_xlsx_when_available(self):
        try:
            import openpyxl
        except ImportError:
            self.skipTest("openpyxl not installed")
        run(self.stem)
        wb = openpyxl.load_workbook(f"{self.stem}.xlsx")
        self.assertEqual(wb.sheetnames, ["Read me first", "Readings", "Code words"])
        self.assertEqual(wb.active.title, "Read me first")
        self.assertEqual(wb.properties.creator, "Cipher Lab")
        ws = wb["Readings"]
        self.assertEqual([c.value for c in ws[1]], EXPECTED)
        self.assertEqual(ws.freeze_panes, "E2")
        self.assertTrue(ws.auto_filter.ref)
        self.assertIsInstance(ws.cell(row=2, column=2).value, int)  # CONTENTdm number stored as a number
        self.assertTrue(ws.cell(row=2, column=16).alignment.wrap_text)
        url = ws.cell(row=2, column=8)
        self.assertEqual(url.font.u, "single")  # a link is marked by an underline, not by colour alone
        topics = [r[0] for r in wb["Read me first"].iter_rows(min_row=2, values_only=True)]
        self.assertEqual(len(topics), len(set(topics)))  # no topic twice
        for col in EXPECTED:  # every column is explained, in its own row or a named section
            self.assertTrue(col in topics or col in ("how much is read", "adds less? (and why)"), col)
        for t in ("Who made this", "How to import", "What is ours and what is theirs", "Abbreviations",
                  "Conventions in the readings and the transcription"):
            self.assertIn(t, topics)
        cw = [r for r in wb["Code words"].iter_rows(min_row=2, values_only=True)]
        self.assertIn(("demo1", 101, "T1", "Apple", "General Beta", "from the cipher book", 1), cw)

    def test_row_without_status_is_written(self):
        st = json.loads((FIX / "status.json").read_text(encoding="utf-8"))
        st["results"] = st["results"][1:]  # drop T1/T2's result
        sp = self.tmp / "status.json"
        sp.write_text(json.dumps(st), encoding="utf-8")
        rc, _, err = run(self.stem, status=sp, extra=["--no-xlsx"])
        self.assertEqual(rc, 0)
        self.assertIn("no status.json result", err)
        _, rows = rows_of(self.stem)
        self.assertEqual(rows[0]["row id (our entry)"], "T1")

    def test_meta_override(self):
        meta = self.tmp / "meta.tsv"
        meta.write_text("item\tpointer\tfrom\tin_print\tnote\tunresolved\tsource\n"
                        "DN7\t700\tsigned 'N'\t-\tlines 1-2 only\tthe name codes are unread\tfixture\n",
                        encoding="utf-8")
        run(self.stem, extra=["--no-xlsx", "--meta", str(meta)])
        _, rows = rows_of(self.stem)
        dn = rows[-1]
        self.assertEqual(dn["CONTENTdm number"], "700")
        self.assertEqual(dn["Digital Library URL"], "https://example.org/demo2/id/700")
        self.assertEqual(dn["from"], "signed 'N'")
        self.assertEqual(dn["partly in print?"], "")
        self.assertTrue(dn["reading (marked up)"].startswith("Note: lines 1-2 only -- "))
        self.assertIn("the name codes are unread", dn["uncertain or unread words"])
        self.assertNotIn("DN 7's group 12 unread", dn["uncertain or unread words"])

    def test_check_detects_stale_output(self):
        rc, _, _ = run(self.stem, extra=["--no-xlsx"])
        self.assertEqual(rc, 0)
        rc, out, _ = run(self.stem, extra=["--no-xlsx", "--check"])
        self.assertEqual(rc, 1)  # DN7 is listed but fails the selection (one audit): a stale list
        self.assertIn("stale list", out)
        lst = self.tmp / "list.tsv"
        lst.write_text("\n".join(l for l in (FIX / "list.tsv").read_text(encoding="utf-8").splitlines()
                                 if "mssDN 7" not in l) + "\n", encoding="utf-8")
        run(self.stem, extra=["--no-xlsx"], lst=lst)
        rc, out, _ = run(self.stem, extra=["--no-xlsx", "--check"], lst=lst)
        self.assertEqual(rc, 0, out)
        p = Path(f"{self.stem}.tsv")
        p.write_text(p.read_text(encoding="utf-8").replace("Alpha", "Omega", 1), encoding="utf-8")
        rc, out, _ = run(self.stem, extra=["--no-xlsx", "--check"], lst=lst)
        self.assertEqual(rc, 1)
        self.assertIn("stale: demo.tsv", out)

    def test_print_clauses(self):
        rec = {"line": "No prior decipherment or printed text located in Butler's printed correspondence (vols. III-V); "
                       "its reply is printed in OR I/2 p.3",
               "depth_check": "re-derivation (LS-V5); external: Biggs's printed replies (OR I/35 pt 2 pp.37-38, the "
                              "Montauk and two other propellers) answer it",
               "gap": "second audit AUD2-LS-A held N3 (OR I/33 read through, printed accounts)"}
        out = he.print_clauses(rec)
        self.assertIn("Its reply is printed in OR I/2 p.3.", out)
        self.assertIn("(OR I/35 pt 2 pp.37-38, the Montauk and two other propellers)", out)  # no cut inside (), no
        self.assertNotIn("printed correspondence", out)                                        # 'PROP' false hit
        self.assertNotIn("AUD2", out)

    def test_sentences_keep_abbreviations(self):
        s = he.sentences("not located in OR ser. I vol. 34 pt 4 (searched 7 Oct 2026); its reply is printed. Next one")
        self.assertEqual(s[0], "not located in OR ser. I vol. 34 pt 4 (searched 7 Oct 2026)")
        self.assertEqual(len(s), 3)

    def test_prior_print_ok(self):
        self.assertTrue(he.prior_print_ok("Not found in the Official Records (ser. I vol. 33) (searched 8 Oct 2026)."))
        self.assertTrue(he.prior_print_ok("Not found in Google Books (24 Sept 2026)."))
        self.assertFalse(he.prior_print_ok("No prior mapping of this telegram to that print was located."))
        self.assertFalse(he.prior_print_ok("Thirteen printed volumes print neither telegram."))
        self.assertEqual(he.prior_print_sentence("no prior decipherment located after two independent searches "
                                                 "(8 Oct 2026) of the Official Records or CORE."),
                         "Not found in the Official Records or CORE (two independent searches, 8 Oct 2026).")

    def test_plain_reading(self):
        r = ("[Washington] {time: 12.30} for [Maj Gen B. F. Butler] [.] the [Unite (-ed, -ing)]d States [Steam]ers "
             "[300] [Men]'s and [Horse]'s of [Hill]'s [Corps] [Advance (-ed, -ing) [#]] [Roanoke] [Inland [sic: Island]]"
             " Is it coming [?] [Command = Er (-ed, -ing)]er Parker [Quarter[?] Master General] [\"] I [Telegraph "
             "(-ed, -ing)]d  {tail: [signed] [Secretary of War]}")
        p = he.plain_reading(r)
        self.assertEqual(p, "Washington (time 12.30) for Maj Gen B. F. Butler. the United States Steamers 300 Men and "
                            "Horses of Hill's Corps Advance Roanoke Island Is it coming? Commander Parker Quarter(?) "
                            "Master General \" I Telegraphed / Signed: Secretary of War")
        self.assertEqual(he.plain_reading("l' ambassadeur [?73] a ete"), "l' ambassadeur [?73] a ete")

    def test_iso_date(self):
        self.assertEqual(he.iso_date("21 Apr 1864, 9.30 PM"), "1864-04-21")
        self.assertEqual(he.iso_date("13 Sept 1728"), "1728-09-13")
        self.assertEqual(he.iso_date("[1727-1728] (catalogue date)"), "1727/1728")
        self.assertEqual(he.iso_date("undated (enclosure (a); the covering letter is dated 8 Aug 1729)"), "")

    def test_extra_unresolved(self):
        self.assertEqual(he.extra_unresolved("'Wreath' unread", {"wreath"}), [])
        self.assertEqual(he.extra_unresolved("none (one token graded inferred; the decoder H on presume set aside)",
                                             set()), [])
        self.assertEqual(he.extra_unresolved("none among the code words; archival copies (NARA M504) unread; most "
                                             "words already public in clear since 2018", set()), [])
        self.assertEqual(he.extra_unresolved("addressee word 'beverage' (not in the book)", {"grunt"}),
                         ["addressee word 'beverage' (not in the book)"])

    def test_audited_counts(self):
        self.assertEqual(he.count_difference({"H": 28, "U": 2}, he.audited_counts("28/30 code words H; x unread")), "")
        self.assertEqual(he.count_difference({"H": 13, "I": 1}, he.audited_counts("13 H + 1 I of 14 code words")), "")
        self.assertEqual(he.count_difference({"H": 15, "C": 2, "M": 2, "I": 1, "U": 1}, he.audited_counts(
            "17 H/C of 21 code-word groups (H 15, C 2, M 2, I 1)")), "")
        self.assertEqual(he.count_difference({"H": 15}, he.audited_counts(
            "15 H by hand of 16 decoder H ('Washington' an artefact)")), "")
        self.assertIn("H 11 vs audited 12", he.count_difference({"H": 11, "M": 1},
                                                                he.audited_counts("12 H + 1 M of 13 code words")))
        self.assertEqual(he.audited_counts("about 20 H of code-word groups").get("_approx"), True)


@unittest.skipUnless(ECKERT_DECODE.exists(), "ciphers/eckert-1864/decode.py not in this checkout")
class TestWithEckertDecoder(unittest.TestCase):
    """A one-entry ledger read with the real ciphers/eckert-1864/decode.py: 'graded:' tokens, the tokens list, a
    '(second telegram)' part, and the count check against the audited completeness."""

    def setUp(self):
        self.tmp = Path(tempfile.mkdtemp())
        root = self.tmp / "repo"
        f = root / "ciphers" / "led"
        f.mkdir(parents=True)
        shutil.copy(ECKERT_DECODE, f / "decode.py")
        (f / "key.md").write_text(
            "| code word | meaning | grade | source |\n|---|---|---|---|\n| Apple | General Beta | H | p.1 |\n"
            "| Pear | Period | H | p.1 |\n| Fig | Signature | H | p.1 |\n| Plum | Richmond | H | p.1 |\n"
            "| Panama | Cavalry | H | p.1 |\n", encoding="utf-8")
        (f / "ciphertext.txt").write_text(
            "### Z1 | Page 5 | 501 | 4 Jan 1864 9 AM, to Beta (operator Omega)\nOmega Washn Jan 4th 1864 9 AM\n"
            "For Apple Pear the pan - a. / ma go to Plum at once Jones Fig Alpha another\n"
            "to Gamma Pear hold Plum Fig Delta\nmerge: pana+ma\ngraded: jones:M\nnote: test\n", encoding="utf-8")
        (f / "ciphertext.txt").write_text((f / "ciphertext.txt").read_text().replace(" / ", "\n"), encoding="utf-8")
        (f / "reading.md").write_text("# r\n\n<!-- decode.py: derived block starts -->\n"
                                      "<!-- decode.py: derived block ends -->\n", encoding="utf-8")
        subprocess.run([sys.executable, str(f / "decode.py"), "--write"], check=True, capture_output=True)
        self.root, self.folder = root, f
        self.status = self.tmp / "status.json"

    def tearDown(self):
        shutil.rmtree(self.tmp)

    def build(self, doc, completeness, extra=()):
        link = "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/led"
        lst = self.tmp / "list.tsv"
        lst.write_text("document\ttitle\tclass\tdepth (rule 4a)\tdepth_pct\tcompleteness\tunresolved\tweak\tkey used\t"
                       f"documents\tfolder\n{doc}\tt\tN3\tD3\t90\t{completeness}\tnone\t\tbook\t1\t{link}\n",
                       encoding="utf-8")
        self.status.write_text(json.dumps({"results": [
            {"document_id": doc, "documents": [doc], "title": "Alpha to Beta, 4 Jan 1864", "grade": "N3",
             "audit_status": "two audits", "claim_scope": "completed-reading", "superseded_by": "",
             "line": "Not located in the Demo Records (searched 1 Oct 2026).", "link": link}]}), encoding="utf-8")
        stem = self.tmp / "out" / "z"
        rc, out, err = run(stem, status=self.status, extra=["--no-xlsx"] + list(extra), lst=lst, root=self.root)
        return rc, out, rows_of(stem)[1]

    def test_graded_and_merge_whole_entry(self):
        rc, out, rows = self.build("Demo p.5, Z1", "8 H + 1 M of 9 code words")
        r = rows[0]
        self.assertIn("panama = Cavalry (from the cipher book)", r["code words and meanings"])
        self.assertIn("Jones (as written; uncertain)", r["code words and meanings"])
        self.assertIn("Jones (as written; uncertain)", r["uncertain or unread words"])
        self.assertTrue(r["how much is read"].startswith("8 of 9 code words read"), r["how much is read"])
        self.assertIn("count check: 0 row(s) differ", out)

    def test_second_telegram_part(self):
        rc, out, rows = self.build("Demo p.5, Z1 (second telegram)", "3 H of 3 code words")
        r = rows[0]
        self.assertTrue(r["ledger/page text as we transcribed it"].startswith("another"))
        self.assertTrue(r["reading (marked up)"].startswith("to Gamma [.] hold [Richmond]"), r["reading (marked up)"])
        self.assertNotIn("General Beta", r["code words and meanings"])
        self.assertTrue(r["how much is read"].startswith("3 of 3 code words read"), r["how much is read"])

    def test_count_difference_fails_check_unless_accepted(self):
        rc, out, _ = self.build("Demo p.5, Z1", "9 H of 9 code words")
        self.assertIn("Z1: H 8 vs audited 9", out)
        rc, out, _ = self.build("Demo p.5, Z1", "9 H of 9 code words", extra=["--check"])
        self.assertEqual(rc, 1)
        self.assertIn("count difference not accepted", out)
        rc, out, _ = self.build("Demo p.5, Z1", "9 H of 9 code words", extra=["--check", "--accept-count", "Z1"])
        self.assertEqual(rc, 0, out)


if __name__ == "__main__":
    unittest.main()

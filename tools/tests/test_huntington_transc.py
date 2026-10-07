import json, os, sys, tempfile, unittest
from unittest import mock
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
import huntington_transc as h

FIX = os.path.join(os.path.dirname(__file__), "fixtures", "huntington_item.json")

class T(unittest.TestCase):
    def test_fetch_caches_and_skips(self):
        item = json.load(open(FIX))
        calls = []
        def fake(path):
            calls.append(path); return item
        with tempfile.TemporaryDirectory() as d, mock.patch.object(h, "get", fake):
            h.main(["--alias", "x", "--range", "1", "2", "--out", d, "--delay", "0"])
            h.main(["--alias", "x", "--range", "1", "3", "--out", d, "--delay", "0"])
            self.assertEqual(len(calls), 3)
            j = json.load(open(os.path.join(d, "p1.json")))
            self.assertEqual(j["transc"], item["transc"])
            self.assertNotIn("descri", j)
    def test_compound(self):
        with mock.patch.object(h, "get", lambda p: {"page": [{"pageptr": "5"}, {"pageptr": "6"}]}):
            self.assertEqual(h.pointers_from_compound("x", 1), [5, 6])
if __name__ == "__main__":
    unittest.main()

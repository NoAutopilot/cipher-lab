"""Offline test for ciphers/lodewijk-van-nassau-1573-74/gaps43/word_anneal.py --objective bigram (SIG-4612B, 8 Oct 2026)."""
import importlib.util, math, os, unittest

P = os.path.join(os.path.dirname(__file__), '..', '..', 'ciphers', 'lodewijk-van-nassau-1573-74', 'gaps43', 'word_anneal.py')

def load():
    spec = importlib.util.spec_from_file_location('word_anneal', P)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

LEX = {'DE': 2.0, 'LA': 3.0, 'LE': 3.0, 'ROY': 5.0}

class TestBigram(unittest.TestCase):
    def test_no_bigram_data_equals_unigram(self):
        m = load()
        bi = ({}, {}, {})
        for s in ('DELA', 'DEXLA', 'ZZ', '', 'LEROY'):
            self.assertAlmostEqual(m.bigram_cost(s, LEX, 3, 10.0, bi, {}), m.unigram_cost(s, LEX, 3, 10.0))

    def test_bigram_prices_word_order(self):
        m = load()
        # context DE seen 4 times: DE LA x4 (one follower); lambda = 0.75 * 1 / 4
        bi = ({('DE', 'LA'): 4}, {'DE': 4}, {'DE': 0.75 / 4})
        la = -math.log2((4 - 0.75) / 4 + (0.75 / 4) * 2 ** -3.0)
        le = -math.log2(0 + (0.75 / 4) * 2 ** -3.0)
        self.assertAlmostEqual(m.bigram_cost('DELA', LEX, 3, 10.0, bi, {}), 2.0 + la)
        self.assertAlmostEqual(m.bigram_cost('DELE', LEX, 3, 10.0, bi, {}), 2.0 + le)
        self.assertLess(m.bigram_cost('DELA', LEX, 3, 10.0, bi, {}), m.bigram_cost('DELE', LEX, 3, 10.0, bi, {}))
        # an OOV character resets the context to unigram
        self.assertAlmostEqual(m.bigram_cost('DEXLA', LEX, 3, 10.0, bi, {}), 2.0 + 10.0 + 3.0)

    def test_switch_and_precheck_only(self):
        m = load()
        self.assertEqual(m.OBJECTIVE, 'seg')
        m.OBJECTIVE = 'bigram'
        self.assertEqual(m.suffix('precheck.json'), 'precheck_bigram.json')
        with self.assertRaises(SystemExit): m.control()

if __name__ == '__main__':
    unittest.main()

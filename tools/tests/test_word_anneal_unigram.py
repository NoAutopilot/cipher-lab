"""Offline test for ciphers/lodewijk-van-nassau-1573-74/gaps43/word_anneal.py --objective unigram (SIG-4612, 8 Oct 2026)."""
import importlib.util, math, os, unittest

P = os.path.join(os.path.dirname(__file__), '..', '..', 'ciphers', 'lodewijk-van-nassau-1573-74', 'gaps43', 'word_anneal.py')

def load():
    spec = importlib.util.spec_from_file_location('word_anneal', P)
    m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m

class TestUnigram(unittest.TestCase):
    def test_viterbi_picks_cheapest_segmentation(self):
        m = load()
        lex = {'DE': 2.0, 'LA': 3.0, 'DELA': 4.0, 'A': 6.0}
        self.assertAlmostEqual(m.unigram_cost('DELA', lex, 4, 10.0), 4.0)      # one word beats DE+LA (5.0)
        self.assertAlmostEqual(m.unigram_cost('DEXLA', lex, 4, 10.0), 15.0)    # DE + OOV X + LA
        self.assertAlmostEqual(m.unigram_cost('', lex, 4, 10.0), 0.0)
        self.assertAlmostEqual(m.unigram_cost('ZZ', lex, 4, 7.5), 15.0)        # all OOV

    def test_cost_fn_switch_and_default(self):
        m = load()
        self.assertEqual(m.OBJECTIVE, 'seg')                                  # GAPS43 stays the default
        m.OBJECTIVE = 'unigram'
        f = m.cost_fn(({'ET': 1.0}, 9.0), 2)
        self.assertAlmostEqual(f('ETX'), 10.0)
        self.assertEqual(m.suffix('control.json'), 'control_unigram.json')

    def test_anneal_incremental_cost_matches_recomputed(self):
        m = load(); m.OBJECTIVE = 'unigram'
        lex = ({'DE': 2.0, 'LA': 2.5, 'ET': 2.5, 'LE': 2.5, 'DELA': 3.0}, 8.0)
        subs = [[1, 2, 3, 4, 2, 5, 3, 2], [3, 4, 1, 2], [2, 5]]
        start = {1: 'D', 2: 'E', 3: 'L', 4: 'Z', 5: 'T'}
        s0 = m.State(subs, start, lex, 4).total
        cost, k = m.anneal(subs, start, lex, 4, seed=1, iters=3000, restarts=2)
        self.assertAlmostEqual(cost, m.State(subs, k, lex, 4).total, places=6)  # incremental bookkeeping is exact
        self.assertLess(cost, s0)                                                 # the OOV Z is annealed away

if __name__ == '__main__':
    unittest.main()

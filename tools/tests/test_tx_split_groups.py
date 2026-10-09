"""Offline test for tools/tx_split_groups.py (TXE-P, 9 Oct 2026): a synthetic line of five digit groups, two of them
glued by a 2-px gap; the sweep finds 4 pieces at gap 3 and 5 at gap 1, and the flag names the glued pair."""
import os, sys, tempfile, unittest

import numpy as np

sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..'))
import tx_split_groups as T  # noqa: E402


def synthetic():
    g = np.full((160, 400), 230, np.uint8)
    xs = [(20, 50), (80, 110), (140, 170), (200, 230), (232, 262)]     # groups 4 and 5 glued: a 2-px blank run
    for x0, x1 in xs:
        g[50:110, x0:x1] = 30
    return g


class TestSplit(unittest.TestCase):
    def test_sweep(self):
        g = synthetic()
        top, bot = T.band(g, 120, 100)
        sw = T.sweep(g, top, bot, [1, 2, 3, 4], 120, 2, 0.55)
        self.assertEqual(len(sw[1]), 5)
        self.assertEqual(len(sw[3]), 4)

    def test_flag_names_glued_pair(self):
        g = synthetic()
        five = [(str(i + 1), s) for i, s in enumerate('abcde')]
        four = [(str(i + 1), s) for i, s in enumerate('abcd')]          # reads the glued pair as one sign
        passes = {'Y': {'L': five}, 'Z': {'L': five}, 'X': {'L': four}}
        with tempfile.TemporaryDirectory() as d:
            sw, fl, rep = T.run({'L': g}, passes, [3, 4, 5, 6], 120, 2, 0.55, 100, d)
            self.assertEqual(rep['L']['pieces'], 4)
            xf = [f for f in fl if f['pass'] == 'X']
            self.assertEqual([(f['pos'], f['kind'], f['piece']) for f in xf], [('4', 'under', 4)])
            self.assertFalse([f for f in fl if f['pass'] != 'X'])          # the five-sign reads are not flagged
            self.assertTrue(os.path.exists(os.path.join(d, 'flags.tsv')))

    def test_score_catches_flagged_deletion(self):
        g = synthetic()
        five = [(str(i + 1), s) for i, s in enumerate('abcde')]
        four = [(str(i + 1), s) for i, s in enumerate('abcd')]
        passes = {'Y': {'L': five}, 'Z': {'L': five}, 'X': {'L': four}}
        with tempfile.TemporaryDirectory() as d:
            T.run({'L': g}, passes, [3, 4, 5, 6], 120, 2, 0.55, 100, d)
            tp = os.path.join(d, 't.tsv')
            with open(tp, 'w') as f:
                f.write('line\tpos\tref_sign\ttruth\tstatus\tplain\n')
                for i, s in enumerate('abcde'):
                    f.write(f'L\t{i + 1}\t{s}\t{s}\tscored\t{s}\n')
            ev = T.score(tp, None, passes, d)
            dele = [e for e in ev if e['kind'] == 'deleted']
            self.assertEqual(len(dele), 1)
            self.assertEqual((dele[0]['pass_'], dele[0]['caught']), ('X', 1))

    def test_dp_puts_extra_sign_in_widest_piece(self):
        self.assertEqual(T.dp_assign(4, [1.0, 1.1, 1.9]), [1, 1, 2])
        self.assertEqual(T.dp_assign(2, [1.0, 1.4, 0.6]), [1, 1, 0])


if __name__ == '__main__':
    unittest.main()

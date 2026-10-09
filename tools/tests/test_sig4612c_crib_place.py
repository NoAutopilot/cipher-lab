"""Offline test for ciphers/lodewijk-van-nassau-1573-74/sig4612c/crib_place.py (SIG-4612C, 9 Oct 2026): synthetic crib placement."""
import os, subprocess, sys, unittest
P = os.path.join(os.path.dirname(__file__), '..', '..', 'ciphers', 'lodewijk-van-nassau-1573-74', 'sig4612c', 'crib_place.py')

class T(unittest.TestCase):
    def test_selftest(self):
        r = subprocess.run([sys.executable, P, 'selftest'], capture_output=True, text=True)
        self.assertEqual(r.returncode, 0, r.stderr); self.assertIn('selftest OK', r.stdout)

if __name__ == '__main__':
    unittest.main()

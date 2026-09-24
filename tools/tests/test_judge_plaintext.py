"""Offline test for tools/judge_plaintext.py (24 Sept 2026): real English passes, shuffled letters fail the language
gate, a missing crib fails, the per-line form check works. Runs the script's own --selftest, no network."""
import subprocess, sys
from pathlib import Path

def test_selftest():
    r = subprocess.run([sys.executable, str(Path(__file__).resolve().parents[1] / "judge_plaintext.py"), "--selftest"],
                       capture_output=True, text=True)
    assert r.returncode == 0, r.stdout + r.stderr
    assert "selftest ok" in r.stdout

if __name__ == "__main__":
    test_selftest(); print("ok")

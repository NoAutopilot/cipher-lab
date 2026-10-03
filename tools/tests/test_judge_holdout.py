#!/usr/bin/env python3
"""Offline test for tools/judge_plaintext.py --holdout (A2P4-KAL5, 3 Oct 2026): three real English folds and one
letter-shuffled fold; the shuffled fold must false-negative on (nearly) every window, the real folds far less often."""
import random
import sys
import tempfile
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
import judge_plaintext as jp  # noqa: E402


def main():
    t = jp.fold(jp.read_corpus(jp.LANG_CORPORA["en"][0]))[:240000]
    d = Path(tempfile.mkdtemp())
    files = []
    for i in range(3):
        p = d / f"real{i}.txt"; p.write_text(t[i * 60000:(i + 1) * 60000]); files.append(p)
    s = list(t[180000:240000]); random.Random(5).shuffle(s)
    p = d / "shuffled.txt"; p.write_text("".join(s)); files.append(p)
    rows, blend, hs = jp.holdout(files, N=300, samples=30)
    by = {r["file"]: r for r in rows}
    assert by["shuffled.txt"]["fn_pct"] >= 95, by
    assert all(by[f"real{i}.txt"]["fn_pct"] <= 60 for i in range(3)), by
    assert len(hs) == 120 and 0 < blend < 100
    print("ok: --holdout shuffled fold FN", by["shuffled.txt"]["fn_pct"], "real folds",
          [by[f"real{i}.txt"]["fn_pct"] for i in range(3)])


if __name__ == "__main__":
    main()

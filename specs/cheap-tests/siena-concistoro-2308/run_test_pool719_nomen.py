"""R13-SIENA719 (6 Oct 2026): nos. 7 + 19 pooled (agent J transcripts, 481 tokens, K=62 union) under R10-SIENA7N's
homophonic + nomenclator design, unchanged except the material: the pooling assumes one key across the two letters (same
sign name = same value), so the seven C glosses of no. 7 (glosses_no07.tsv) are held fixed wherever the sign occurs.
Pre-registered in ciphers/siena-concistoro-2308/PREREG-R13-SIENA719.md (pushed before the scored run). Everything else
(solver, corpus, VOCAB/NOMEN, knobs, control construction, statistics) is run_test_no07_nomen.py's, imported, not copied;
only runs() (no. 7's runs then no. 19's, "|" clear-text breaks splitting a run), the token sha and OUT are replaced.
The matched control is therefore built at the pooled N=481 and K=62, cut into the pool's 25 run lengths.

  python3 run_test_pool719_nomen.py control --err 0 0.035 0.07 --seeds 1 2 3 4 5   # control first
  python3 run_test_pool719_nomen.py target --seeds 1 2 3                            # only if both gates pass
  python3 run_test_pool719_nomen.py shuffled --seeds 1 2 3
  python3 run_test_pool719_nomen.py --check
"""
import hashlib
import sys
from pathlib import Path

import run_test_no07_nomen as R

TX = R.ROOT / "ciphers/siena-concistoro-2308/transcripts"
TOKS = [TX / "no07.tok", TX / "no19.tok"]


def runs():
    out = []
    for f in TOKS:
        for line in open(f, encoding="utf-8"):
            if not line.strip() or line.startswith("#"):
                continue
            out.extend(seg.split() for seg in line.split("|") if seg.split())
    return out


def tok_sha():
    return hashlib.sha1(b"".join(f.read_bytes() for f in TOKS)).hexdigest()


R.runs, R.tok_sha = runs, tok_sha
R.OUT = Path(__file__).with_name("results_pool719_nomen.json")

if __name__ == "__main__":
    sys.argv[0] = __file__
    R.main()

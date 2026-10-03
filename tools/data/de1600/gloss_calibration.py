#!/usr/bin/env python3
"""Calibration only (CORP-DE16, 3 Oct 2026): score decode-1411-hhsta-vienna-1600's own period interlinear gloss text
(ciphers/decode-1411-hhsta-vienna-1600/gaps150/gloss_text.txt, 62 letters, as GAPS141/GAPS150 reconciled it) through the
judge's language check under de17 and de1600, beside 200 letter-shuffles of the same text (CLAUDE.md rule 3, ZX-DEC349
paragraph). It does NOT score the R1411 decode (that is the next job's pre-registered gate).
Usage: python3 tools/data/de1600/gloss_calibration.py
"""
import random, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "tools"))
from judge_plaintext import judge, LANG_CORPORA, NgramModel, read_corpus, fold, pct  # noqa: E402

text = (ROOT / "ciphers/decode-1411-hhsta-vienna-1600/gaps150/gloss_text.txt").read_text().strip()
for lang in ("de17", "de1600"):
    r = judge({"judge": {"language": lang}}, text)["checks"]["language"]
    model = NgramModel([read_corpus(p) for p in LANG_CORPORA[lang]])
    rnd, letters, shuf = random.Random(1600), list(fold(text)), []
    for _ in range(200):
        rnd.shuffle(letters); shuf.append(model.score("".join(letters)))
    d = r["detail"] if "detail" in r else r
    print(f"{lang}: {'PASS' if r['pass'] else 'FAIL'} gloss N={len(fold(text))} {d}; "
          f"letter-shuffled mean {sum(shuf)/len(shuf):.3f} max {max(shuf):.3f}")
# Where the gloss sits among genuine held-out de1600 windows of its own length (leave-one-file-out, 200 per fold)
files, held = LANG_CORPORA["de1600"], []
for f in files:
    m = NgramModel([read_corpus(g) for g in files if g != f])
    t, rnd = fold(read_corpus(f)), random.Random(2)
    g = m.score(text)
    sc = [m.score(t[j:j + 62]) for j in (rnd.randrange(0, len(t) - 62) for _ in range(200))]
    held.append((f.name, g, sum(x <= g for x in sc), min(sc)))
for name, g, k, lo in held:
    print(f"de1600 LOO fold {name}: gloss {g:.3f}; held-out N=62 windows at or below it {k}/200; lowest window {lo:.3f}")

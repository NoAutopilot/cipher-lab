"""CHECK-GOLDBAR (3 Oct 2026): could Kim's design (each line Swiss-K Enigma-enciphered under its own key and ring)
produce the bars' near-flat letter counts (chi-squared 1.251, 25 df, 263 letters; bGLD/Bourdeau)? Encipher 1000 random
English windows cut to the bars' 16 line lengths, each line under a random key and ring, and report chi-squared."""
import random, sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parent)); sys.path.insert(0, str(Path(__file__).resolve().parents[3] / "tools"))
from enigma_k import A, Enigma, KIM_CFG
import judge_plaintext as J
lines = [l.strip() for l in open(Path(__file__).resolve().parents[1] / "ciphertext.txt") if l.strip()]
lens = [len(l) for l in lines]; N = sum(lens)
raw = "".join(J.fold(J.read_corpus(p)) for p in J.LANG_CORPORA["en"]).upper()
def chi(s):
    e = len(s) / 26; return sum((s.count(c) - e) ** 2 / e for c in A)
rnd = random.Random(20261003); xs = []
for _ in range(1000):
    j = rnd.randrange(len(raw) - N); pt = raw[j:j + N]; ct = ""; k = 0
    for L in lens:
        r = lambda: "".join(rnd.choice(A) for _ in range(3))
        ct += Enigma(key=r(), ring=r(), **KIM_CFG).run(pt[k:k + L]); k += L
    xs.append(chi(ct))
xs.sort()
print("target chi2 %.3f (N=%d); Enigma-of-English control: min %.2f p5 %.2f median %.2f p95 %.2f; draws <= target: %d/1000"
      % (chi("".join(lines)), N, xs[0], xs[50], xs[500], xs[950], sum(x <= chi("".join(lines)) for x in xs)))

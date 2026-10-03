#!/usr/bin/env python3
"""H73 diagnostic (after the gate, not a tuning step): is the control's TRUE plaintext preferred by V1's objective
over V1's own best decode? LM log-probability of the true sequence vs the decode (wildcards as <unk>), per seed.
truth > decode => the search fell short; truth < decode => the objective itself prefers the wrong reading at this N."""
import contextlib, io, os, sys
HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import run_h73 as R  # noqa: E402
nm = R.nm
C = R.corpora(); tm = R.target_msgs()
lm = nm.get_lm(C, 3)
for tag in sys.argv[1:]:
    name, book, prior, thin, s = tag.split("-")
    with contextlib.redirect_stdout(io.StringIO()):
        cm, plain, _ = nm.make_control({}, int(s[1:]), C, {"vocab_order": 1, "book": book, "prior": prior, "target_msgs": tm})
    dec = open(os.path.join(HERE, "out", tag + ".txt")).read().split()
    def lp(ws):
        ws = [nm.UNK if w == "*" else lm.norm(w) for w in ws]
        return sum(lm.lp3(w, ws[i - 2] if i >= 2 else "<s>", ws[i - 1] if i >= 1 else "<s>") for i, w in enumerate(ws))
    t, d = lp(plain.split()), lp(dec)
    print(f"{tag}\ttruth_lm\t{t:.1f}\tdecode_lm\t{d:.1f}\t{'objective prefers decode' if d > t else 'search short of truth'}")

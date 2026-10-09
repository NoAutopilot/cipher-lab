#!/usr/bin/env python3
"""Offline tests for homophonic_anneal.py --participation (MQS-PARTICIPATION, 9 Oct 2026). No network.
Must catch: a sign whose occurrences never sit inside a lexicon word (an unmarked nomenclature sign).
Must NOT flag: letter signs whose occurrences sit in words at the text's own rate; signs under --part-min-count."""
import os, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import homophonic_anneal as ha

# word_windows: every occurrence, overlaps allowed, a gap never matches
assert ha.word_windows("xxlesxx", ["les"]) == [0, 0, 1, 1, 1, 0, 0]
assert ha.word_windows("le?s", ["les"]) == [0, 0, 0, 0]
assert ha.word_windows("dele", ["de", "ele"], minlen=2) == [1, 1, 1, 1]

# a decoded stream of words; the sign N is planted between words and decodes to 'q' (no word holds it)
words = ["pour", "les", "que", "dans", "vostre", "nous", "avec", "estre"] * 30
dec, seq = "", []
for i, w in enumerate(words):
    dec += w
    seq += [f"L{c}" for c in w]
    if i % 3 == 0:
        dec += "q"
        seq.append("N")
lex = ["pour", "les", "que", "dans", "vostre", "nous", "avec", "estre"]
part = ha.participation(seq, [dec, dec], lex, shuffles=100, seed=1)
assert part["N"]["flag"] and part["N"]["share"] == 0.0, part["N"]
letters = [x for x in part if x != "N"]
assert not any(part[x]["flag"] for x in letters), [x for x in letters if part[x]["flag"]]  # must NOT flag

# min_count: a once-seen sign is never flagged even at share 0
part2 = ha.participation(seq + ["R"], [dec + "q"] * 2, lex, shuffles=50, min_count=2)
assert not part2["R"]["flag"]

# the null can differ: shuffle the stream -> N no longer separated (AUC near chance, not 1)
assert ha.auc([0.0], [0.9, 0.8]) == 1.0 and ha.auc([0.5], [0.5]) == 0.5

# classfile is --as-unknown readable and lists only flagged signs
d = tempfile.mkdtemp()
cf = os.path.join(d, "c.tsv")
ha.write_classfile(cf, part)
assert ha.read_sign_list(cf) == {"N"}

# CLI, marked control in plain mode with --participation (tiny, no network)
open(os.path.join(d, 'p.txt'), 'w').write(" ".join(words) * 3)
open(os.path.join(d, 'c.txt'), 'w').write(" ".join(words) * 20)
cmd = [sys.executable, os.path.join(R, 'tools', 'homophonic_anneal.py'), '--control', os.path.join(d, 'p.txt'),
       '--signs', '20', '--length', '300', '--corpus', os.path.join(d, 'c.txt'), '--restarts', '1', '--iters', '300',
       '--control-homs', '1-2', '--marked', '0.2:3', '--marked-mode', 'plain', '--participation', cf,
       '--part-shuffles', '20', '--part-null-shuffle']
o = subprocess.run(cmd, capture_output=True, text=True)
assert o.returncode == 0 and "participation: AUC" in o.stdout and "null (position-shuffled" in o.stdout, o.stdout + o.stderr
print("all MQS-PARTICIPATION tests passed")

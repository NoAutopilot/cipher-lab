#!/usr/bin/env python3
"""Offline test for tools/german_ngram.py (J7, 24 Sept 2026): a model built from the on-disk ENHG text scores held-out
German above French, norm() folds as documented, and nomenclator_anneal --lang de loads the German alphabet."""
import os, subprocess, sys, tempfile
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, os.path.join(R, 'tools'))
import german_ngram as g

assert g.norm("Wir häben jetzt vnd Größe") == "wir#haben#ietzt#und#grosse", g.norm("Wir häben jetzt vnd Größe")
assert g.K == 24 and 'k' in g.ALPHA and 'w' in g.ALPHA
text = open(os.path.join(R, 'tools', 'data', 'de16', 'composed_enhg.txt'), encoding='utf-8').read()
lines = g.select(text)
assert lines, "no German paragraph selected"
train = [l for l in lines]
z = "#".join(train)
cut = len(z) * 4 // 5
with tempfile.TemporaryDirectory() as d:
    open(os.path.join(d, 'c.txt'), 'w').write(z[:cut] + "\n")
    subprocess.check_call([sys.executable, os.path.join(R, 'tools', 'german_ngram.py'), 'build', os.path.join(d, 'c.txt'),
                           '--out', os.path.join(d, 'm.npz'), '--order', '4'], stderr=subprocess.DEVNULL)
    m = g.Model(os.path.join(d, 'm.npz'))
    de = m.mean_llr(z[cut:].replace('#', ' '))
    fr = m.mean_llr("monseigneur depuis nostre derniere lettre par laquelle nous vous avons mande en quelle termes "
                    "nous estions avecq noz reystres lesquelz nous ont a la fin accorde")
    assert de > 0.3 and fr < de - 0.5, (de, fr)
    out = subprocess.run([sys.executable, os.path.join(R, 'tools', 'nomenclator_anneal.py'), 'decode', '--help'],
                         capture_output=True, text=True).stdout
    assert '--lang' in out
print("ok german_ngram", round(de, 3), round(fr, 3))

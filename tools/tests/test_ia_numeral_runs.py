"""Offline tests for tools/ia_numeral_runs.py --markers (MQS-IA-MARKERS, 9 Oct 2026). No network."""
import os, subprocess, sys, tempfile
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..'))
import ia_numeral_runs as T

TOOL = os.path.join(os.path.dirname(__file__), '..', 'ia_numeral_runs.py')
LETTER = """Madame, j'ay receu vostre lettre du dernier du moys.
Quant a l'affaire que vous scavez . . . . . et le seigneur
de Mauvissiere m'a dict que ... sans plus attendre
que le roy vostre frere . . . . de quoy je vous prie
me donner advis au plus tost que pourrez."""
NOTE = "Je vous prie de faire tenir ceste lettre [en chiffre] a mon cousin."
TOC = """Lettre au roi de France . . . . . . . . . . 45
Lettre a M. de Mauvissiere ............ 47
Lettre a l'archevesque de Glasgow . . . . . . xii
Instructions au sieur de Fontenay . . . . . . . p. 52"""
ONE = "Il est escript au dos : Pour vous seul ... et rien plus.\n" + "Texte clair sans marque aucune.\n" * 20

def flagged(text, gap=6, k=3):
    return [(c, m) for c, m in T.marker_clusters(text.split('\n'), gap) if m >= k]

def test_catch_ellipses():
    f = flagged(LETTER)
    assert len(f) == 1 and f[0][1] == 3, f

def test_catch_note():
    f = flagged(NOTE)
    assert len(f) == 1 and f[0][1] == 3, f
    assert T.marker_count("(in cipher) the rest") == 3 and T.marker_count("[Chiffre.]") == 3

def test_not_toc():
    assert flagged(TOC) == [], [T.marker_count(l) for l in TOC.split('\n')]

def test_not_single():
    assert flagged(ONE) == []

def test_unchanged_without_flag():
    with tempfile.TemporaryDirectory() as d:
        txt = "intro words here\n" + "12 45 12 78 45 12 33 45\n" * 3 + LETTER + "\n"
        open(os.path.join(d, 'x_djvu.txt'), 'w').write(txt)
        out = subprocess.run([sys.executable, TOOL, 'x', '--cache', d], capture_output=True, text=True).stdout
        hdr = out.split('\n')[0]
        assert hdr == 'identifier\tline\tn_lines\tnumerals\tdistinct\trepeat_rate\tprose_words\tcontext', hdr
        assert 'marker' not in out and len(out.strip().split('\n')) == 2
        out2 = subprocess.run([sys.executable, TOOL, 'x', '--cache', d, '--markers'], capture_output=True, text=True).stdout
        rows = out2.strip().split('\n')
        assert rows[0].endswith('\tkind\tmarkers') and rows[1].split('\t')[8] == 'numeral'
        assert rows[2].split('\t')[8] == 'marker' and rows[2].split('\t')[9] == '3', rows

def test_inline_run():
    ln = "wee are meditating to 215. 345. 196. 501. 105. not anchor at all".split('\n')
    prose = ["wee shall gaine Lagos in 2 dayes, April 5, 1656, about the hour"] * 3
    assert T.clusters(ln, 6, 0.7) == [] and T.clusters(ln, 6, 0.7, 4) == [[0]]
    assert T.clusters(prose, 6, 0.7, 4) == []

if __name__ == '__main__':
    bad = 0
    for n, f in sorted(globals().items()):
        if n.startswith('test_'):
            try:
                f(); print('ok', n)
            except AssertionError as e:
                bad += 1; print('FAIL', n, e)
    sys.exit(1 if bad else 0)

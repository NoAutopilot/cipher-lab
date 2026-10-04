#!/usr/bin/env python3
"""build.py: rebuild tools/data/pl18 from five Internet Archive _djvu.txt files (A3V3-SANGP, 4 Oct 2026).

Polish prose of the Saxon era and its neighbours (1683-c.1790), for sanguszkow-mniszech-dunin-1714 (a 1714 letter).
Usage: python3 tools/data/pl18/build.py RAW_DIR   (RAW_DIR holds <identifier>.txt as fetched from
archive.org/download/<identifier>/<file>_djvu.txt; see MANIFEST.tsv). Steps per file: drop scanner boilerplate lines
("Digitized by", "Google"), drop lines that read as French or Latin (more French/Latin function words than Polish
ones), fold Polish letters the judge's fold() would otherwise DROP (ą ę ć ł ń ś ź ż -> a e c l n s z z; ó is folded by
the judge itself), join hyphenated line breaks, cap at CAP folded letters taken from the middle of the body (skipping
the editor's front matter), gzip."""
import gzip, re, sys
from pathlib import Path

CAP = 650_000
FILES = ["bc.wbp.lodz.pl.Pamietniki_do_panowania_Augusta_II_91967", "bc.radom.pl.11-359",
         "bc.wbp.lodz.pl.Listy_Jana_III_Krola_Polskiego_a_96549", "ojczystespomink01johngoog",
         "pamitnikiksakit01kitogoog"]
PL = str.maketrans({"ą": "a", "ę": "e", "ć": "c", "ł": "l", "ń": "n", "ś": "s", "ź": "z", "ż": "z",
                    "Ą": "A", "Ę": "E", "Ć": "C", "Ł": "L", "Ń": "N", "Ś": "S", "Ź": "Z", "Ż": "Z"})
FR = set("le la les que est vous des une sont pour avec dans qui pas mais".split())
LA = set("est sunt quod cum enim atque etiam esse nobis vobis ad ut sed".split())
POL = set("się sie nie jest iest który ktory to na do że ze jako przez tak już iuz był byl".split())


def keep_line(ln):
    if re.search(r"digitized|google", ln, re.I):
        return False
    w = re.findall(r"\w+", ln.lower())
    f = sum(x in FR for x in w) + sum(x in LA for x in w)
    p = sum(x in POL for x in w)
    return not (f >= 2 and f > p)


def build(raw):
    out = Path(__file__).resolve().parent
    for ident in FILES:
        t = (Path(raw) / f"{ident}.txt").read_text(encoding="utf-8", errors="replace")
        lines = [ln for ln in t.splitlines() if keep_line(ln)]
        body = re.sub(r"-\s*\n\s*", "", "\n".join(lines)).translate(PL)
        n = len(re.sub(r"[^a-z]", "", body.lower()))
        if n > CAP:  # take a CAP-letter span from the middle, cut at line ends
            start = int(len(body) * (n - CAP) / (2 * n))
            end = start + int(len(body) * CAP / n)
            body = body[body.find("\n", start) + 1: body.rfind("\n", 0, end)]
        with gzip.open(out / f"{ident}.txt.gz", "wt", encoding="utf-8") as g:
            g.write(body)
        print(ident, len(re.sub(r"[^a-z]", "", body.lower())))


if __name__ == "__main__":
    build(sys.argv[1])

"""Language-model corpus and synthetic-control plaintext for the Fauconberg benchmark.

LM corpus: tools/data Gutenberg texts (english_score.py's DEFAULT_CORPORA) plus the English lines of
Thurloe vols 2, 3, 5 (never vol 7, which holds the Fauconberg letters and the control text).
Control plaintext: English lines of vol 7 read in order from djvu line 2000, skipping 500 lines either side
of every extracted cipher window (all P rows), until enough letters. Both pass through repair_long_s():
the OCR reads long s as f or l ("bufinefle"); a word absent from the Gutenberg vocabulary whose f/l->s
variant is present takes the variant. Sources: sources/ia-fulltext/<id>_djvu.txt, restored from
sources/ia-fulltext/thurloe-gz/ when missing.
"""
import gzip, itertools, re, sys
from functools import lru_cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
IA = ROOT / "sources" / "ia-fulltext"
sys.path.insert(0, str(ROOT / "tools"))
import english_score  # noqa: E402

EN = set("the and of to that in is it for with be have not his this which but you they will as by at "
         "from are was all my your their them been would shall there so if what we our me".split())


def djvu(vol):
    p = IA / f"collectionofstat{vol}thur_djvu.txt"
    if not p.exists():
        p.write_bytes(gzip.decompress((IA / "thurloe-gz" / (p.name + ".gz")).read_bytes()))
    return p.read_text(encoding="utf-8", errors="replace").split("\n")


def english(line):
    w = re.findall(r"[A-Za-z]+", line)
    return len(w) >= 5 and sum(x.lower() in EN for x in w) / len(w) >= 0.25 \
        and sum(ch.isdigit() for ch in line) < 3


@lru_cache(None)
def vocab():
    v = set()
    for p in english_score.DEFAULT_CORPORA:
        v.update(w.lower() for w in re.findall(r"[A-Za-z]+", english_score._read(p)))
    return v


def repair_long_s(text):
    V = vocab()
    def fix(m):
        w = m.group(0); lw = w.lower()
        if lw in V:
            return w
        pos = [i for i, c in enumerate(lw) if c in "fl"]
        if not pos or len(pos) > 4:
            return w
        for k in range(1, len(pos) + 1):
            for sub in itertools.combinations(pos, k):
                t = "".join("s" if i in sub else c for i, c in enumerate(lw))
                if t in V:
                    return t
        return w
    return re.sub(r"[A-Za-z]+", fix, text)


def lm_texts():
    th = "\n".join(l for v in ("02", "03", "05") for l in djvu(v) if english(l))
    return [english_score._read(p) for p in english_score.DEFAULT_CORPORA] + [repair_long_s(th)]


def windows():
    out = []
    for f in (ROOT / "ciphers" / "thurloe-printed").glob("P*/ciphertext.txt"):
        t = f.read_text(encoding="utf-8")
        if "collectionofstat07thur" in t:
            ls = [int(x) for x in re.findall(r"^L(\d+)", t, re.M)]
            out.append((min(ls) - 500, max(ls) + 500))
    return out


def control_plain(nletters, start=2000):
    W = windows()
    lines = djvu("07")
    buf, n, used = [], 0, []
    for i, l in enumerate(lines[start - 1:], start):
        if any(a <= i <= b for a, b in W) or not english(l):
            continue
        l = repair_long_s(l)
        buf.append(l); used.append(i)
        n += len(re.sub(r"[^a-z]", "", l.lower()))
        if n >= nletters:
            break
    return " ".join(buf), (used[0], used[-1])


if __name__ == "__main__":
    t, span = control_plain(3100)
    print(span, t[:600])

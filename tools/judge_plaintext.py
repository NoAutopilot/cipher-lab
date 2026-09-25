#!/usr/bin/env python3
"""judge_plaintext.py: score a candidate plaintext mechanically against a spec (specs/<slug>.json) and print PASS or FAIL.

Written 24 Sept 2026 (survey worker). Our version of the Lean check in the 2025-26 Erdős-problem work: a solver session
(or a hundred of them) proposes a plaintext; this script, not a person, says whether it clears the bar. It never says a
reading is *right* (rule 10: that is a verifier's job); it says whether the reading is worth a verifier's time.

Usage:
  python3 tools/judge_plaintext.py specs/koehler-1944.json --text "DER ANGRIFF ..."        one candidate
  python3 tools/judge_plaintext.py specs/koehler-1944.json --file candidate.txt [--json]  from a file
  python3 tools/judge_plaintext.py --selftest                                              offline test

Checks, all read from the spec's "judge" block (missing keys are skipped):
  length        exact letter count ("letters": N) or a range ("letters_min"/"letters_max"), letters only (a-z after folding)
  lines         "line_letters": [n1, n2, ...] exact letters per line of the candidate (form check, e.g. Dorabella 29/31/27)
  cribs         "cribs": ["BERLIN", ...] each must occur (letters only, folded); "cribs_at": {"22": "EASTNORTHEAST"} at a
                0-based letter offset
  language      "language": one of en, de, fr, it, la (corpora on disk, tools/data), or "corpora": [paths]. The candidate's
                mean log10 4-gram probability per letter is compared with (a) real text windows of the same length from the
                same corpus (the matched control) and (b) letter-shuffled windows (the null). PASS on language needs the
                candidate to score above the null's 99th percentile AND above the real-text 5th percentile, unless the spec
                sets "language_pass": "null_only" (for texts expected to be telegraphese, initials or a code list).
  initials      "initials_regex": "^[MW]RGOABABD$" the candidate's word-initial sequence (letters, upper-cased, one
                string across all lines) must match; for initialism targets such as the Somerton code
  words         "min_word_cover": 0.6  fraction of the candidate's letters covered by a greedy segmentation into corpus words
                (>= 3 letters, plus a/i and common 2-letter words); compared with the same statistic on real text.
Verdict: PASS if every present check passes; exit 0. Otherwise FAIL, exit 1, with the failing checks named.
The language model is a plain add-k 4-gram over letters; it is a gate, not a proof.
"""
import argparse, gzip, json, math, random, re, sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent
DATA = ROOT / "data"
LANG_CORPORA = {
    "en": [DATA / "pg1661_holmes.txt", DATA / "pg2701_mobydick.txt"],
    "de": [DATA / "de16" / "composed_enhg.txt"],
    "fr": [DATA / "fr16" / "lettresdecatheri01cathuoft_djvu.txt.gz"],
    "it": [DATA / "it16" / "alcuneletteredip00ferr.txt", DATA / "it16" / "delleletterefam02seghgoog.txt",
           DATA / "it16" / "lettereinedited00tassgoog.txt", DATA / "it16" / "lettereinedited01cibrgoog.txt",
           DATA / "it16" / "lettereineditedi01carouoft.txt", DATA / "it16" / "letterescrittea01vanzgoog.txt"],
    "pt": [DATA / "pt17" / "vieira_cartas_tomoIV_1855.txt.gz", DATA / "pt17" / "vieira_cartas_1912.txt.gz"],
    "pt18": [DATA / "pt18" / "correiobrazilie00unkngoog.txt.gz", DATA / "pt18" / "correiobrazilie02unkngoog.txt.gz",
             DATA / "pt18" / "oinvestigadorpo03unkngoog.txt.gz", DATA / "pt18" / "oinvestigadorpo05unkngoog.txt.gz"],
    "es": [DATA / "es17" / "donquijote00cervuoft.txt.gz", DATA / "es17" / "vidadelbuscn01quevuoft.txt.gz"],
    "es17c": [DATA / "es17c" / "memorialhistri17realuoft.txt.gz", DATA / "es17c" / "memorialhistri18realuoft.txt.gz",
              DATA / "es17c" / "memorialhistri19realuoft.txt.gz"],
    # nl, la (25 Sept 2026, YX-PTJUDGE): tools/data/nl_repo, la_repo each hold only one or two target's own
    # committed readings/plaintext-print files (a few KB each, nowhere near the ~200k-character floor a
    # language check needs, and for la_repo the sole file *is* the target's own reading -- circular per
    # CLAUDE.md "never use a target's own reading as its corpus"). Not wired. A future worker who fetches a
    # real nl/la period corpus (Internet Archive djvu.txt or a Google Books full-view volume, never the
    # target's own material) of at least ~200k letters can add it here the way "it"/"pt"/"es" are done.
    # es (25 Sept 2026, LANE R6 Y8): tools/data/es17/ -- early-17th-c. Spanish prose (Cervantes, Quevedo),
    # ~1.92M letters folded, built for espagnol142-mercy-1648 (a 1648 letter). See tools/data/es17/README.md.
    # es17c (25 Sept 2026, LANE R6 MJ): tools/data/es17c/ -- 1643-1647 Spanish court-newsletter prose
    # (Cartas de algunos PP. de la Compania de Jesus sobre los sucesos de la Monarquia), ~2.1M letters
    # folded, register-matched to espagnol142-mercy-1648 (chancery/diplomatic Spanish, June 1648) after
    # es17's literary-fiction corpus (Cervantes/Quevedo) FAILed the target's own clear words (CLAUDE.md
    # rule 3, V6-PTCORP era/register lesson). "es" stays the default; a spec opts in with
    # "judge": {"language": "es17c", ...}. See tools/data/es17c/README.md.
}
FOLD = str.maketrans({"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss", "é": "e", "è": "e", "ê": "e", "à": "a", "ç": "c",
                      "ù": "u", "û": "u", "î": "i", "ô": "o", "â": "a", "ë": "e", "ï": "i",
                      "á": "a", "ã": "a", "â": "a", "í": "i", "ó": "o", "õ": "o", "ú": "u", "ñ": "n"})


def fold(s):
    s = s.lower().translate(FOLD)
    return re.sub(r"[^a-z]", "", s)


def read_corpus(p):
    p = Path(p)
    if p.suffix == ".gz":
        t = gzip.open(p, "rt", encoding="utf-8", errors="replace").read()
    else:
        t = p.read_text(encoding="utf-8", errors="replace")
    a, b = t.find("*** START OF"), t.find("*** END OF")
    if a >= 0 and b > a:
        t = t[t.find("\n", a) + 1:b]
    return t


class NgramModel:
    def __init__(self, texts, n=4, k=0.01):
        self.n, self.k = n, k
        self.c = Counter(); self.ctx = Counter()
        words = Counter()
        self.raw = ""
        for t in texts:
            L = fold(t); self.raw += L
            for i in range(len(L) - n + 1):
                g = L[i:i + n]; self.c[g] += 1; self.ctx[g[:-1]] += 1
            words.update(w.lower().translate(FOLD) for w in re.findall(r"[A-Za-zäöüßéèêàçùûîôâëï]+", t))
        two = {"is", "it", "in", "to", "of", "on", "at", "be", "by", "he", "we", "me", "my", "no", "so", "up", "us", "an",
               "as", "am", "do", "go", "if", "or", "er", "es", "zu", "im", "du", "le", "la", "de", "et", "un", "il", "je"}
        self.words = {w for w, n_ in words.items() if n_ >= 2 and (len(w) >= 3 or w in ("a", "i") or w in two)}
        self.maxw = max((len(w) for w in self.words), default=1)

    def score(self, s):
        """mean log10 P(letter | 3 previous) over folded s; add-k over 26 letters."""
        s = fold(s)
        if len(s) < self.n:
            return -9.9
        tot = 0.0
        for i in range(self.n - 1, len(s)):
            g = s[i - self.n + 1:i + 1]
            tot += math.log10((self.c.get(g, 0) + self.k) / (self.ctx.get(g[:-1], 0) + 26 * self.k))
        return tot / (len(s) - self.n + 1)

    def cover(self, s):
        """fraction of letters covered by a greedy longest-word segmentation (with restarts on failure)."""
        s = fold(s); i = 0; covered = 0
        while i < len(s):
            best = 0
            for L in range(min(self.maxw, len(s) - i), 0, -1):
                if s[i:i + L] in self.words:
                    best = L; break
            if best:
                covered += best; i += best
            else:
                i += 1
        return covered / len(s) if s else 0.0

    def controls(self, N, samples=200, seed=1):
        """(real-text scores, shuffled-text scores, real-text cover) for windows of N letters."""
        rnd = random.Random(seed); real, null, cov = [], [], []
        for _ in range(samples):
            j = rnd.randrange(0, max(1, len(self.raw) - N))
            w = self.raw[j:j + N]
            real.append(self.score(w)); cov.append(self.cover(w))
            ws = list(w); rnd.shuffle(ws); null.append(self.score("".join(ws)))
        return sorted(real), sorted(null), sorted(cov)


def pct(xs, q):
    if not xs:
        return float("nan")
    return xs[min(len(xs) - 1, int(q * (len(xs) - 1)))]


def judge(spec, text):
    j = spec.get("judge", {})
    out = {"checks": {}, "pass": True}
    lines = [ln for ln in text.splitlines() if fold(ln)]
    letters = fold(text)

    def rec(name, ok, detail):
        out["checks"][name] = {"pass": bool(ok), **detail}
        if not ok:
            out["pass"] = False

    if "letters" in j:
        rec("length", len(letters) == j["letters"], {"got": len(letters), "want": j["letters"]})
    if "letters_min" in j or "letters_max" in j:
        lo, hi = j.get("letters_min", 0), j.get("letters_max", 10 ** 9)
        rec("length", lo <= len(letters) <= hi, {"got": len(letters), "min": lo, "max": hi})
    if "line_letters" in j:
        got = [len(fold(ln)) for ln in lines]
        rec("lines", got == j["line_letters"], {"got": got, "want": j["line_letters"]})
    if "cribs" in j:
        missing = [c for c in j["cribs"] if fold(c) not in letters]
        rec("cribs", not missing, {"missing": missing, "count": len(j["cribs"])})
    if "cribs_at" in j:
        bad = {}
        for off, c in j["cribs_at"].items():
            o = int(off)
            if letters[o:o + len(fold(c))] != fold(c):
                bad[off] = c
        rec("cribs_at", not bad, {"wrong": bad})
    if "initials_regex" in j:
        ini = "".join(w[0] for w in re.findall(r"[A-Za-z]+", text)).upper()
        rec("initials", re.search(j["initials_regex"], ini) is not None, {"got": ini, "regex": j["initials_regex"]})
    corpora = j.get("corpora") or LANG_CORPORA.get(j.get("language", ""), None)
    if j.get("language") and not corpora:  # an unwired code used to skip the language check silently (B2, 25 Sept 2026)
        rec("language", False, {"error": f"language code {j['language']!r} has no corpus in LANG_CORPORA; wire it or use 'corpora'"})
    if not corpora and not any(k in j for k in ("cribs", "cribs_at", "initials_regex")):
        # fail closed: a block with only length/line checks PASSed letter salad on mccormick-1999 (LANE B2 bMCC2, 25 Sept 2026)
        rec("content", False, {"error": "no language, corpora, cribs, cribs_at or initials_regex in the judge block: a length-only gate is not a judge"})
    if corpora:
        model = NgramModel([read_corpus(p) for p in corpora])
        N = max(len(letters), 20)
        real, null, cov = model.controls(N, samples=int(j.get("control_samples", 200)))
        sc = model.score(letters)
        null99, real05 = pct(null, 0.99), pct(real, 0.05)
        mode = j.get("language_pass", "both")
        ok = sc > null99 and (mode == "null_only" or sc > real05)
        rec("language", ok, {"score": round(sc, 3), "null_p99": round(null99, 3), "real_p05": round(real05, 3),
                             "real_median": round(pct(real, 0.5), 3), "mode": mode, "N": N})
        if "min_word_cover" in j:
            cv = model.cover(letters)
            rec("words", cv >= j["min_word_cover"], {"cover": round(cv, 3), "min": j["min_word_cover"],
                                                     "real_text_median_cover": round(pct(cov, 0.5), 3)})
    return out


def selftest():
    spec = {"judge": {"language": "en", "letters_min": 60, "letters_max": 400, "cribs": ["STREET"], "min_word_cover": 0.6,
                      "control_samples": 100}}
    good = "I had called upon my friend Sherlock Holmes upon the second morning after Christmas in Baker Street with the intention of wishing him the compliments of the season"
    r1 = judge(spec, good)
    assert r1["pass"], r1
    ws = list(fold(good)); random.Random(3).shuffle(ws)
    r2 = judge(spec, "".join(ws))
    assert not r2["pass"] and not r2["checks"]["language"]["pass"], r2
    r3 = judge(spec, good.replace("Street", "Road"))
    assert not r3["pass"] and r3["checks"]["cribs"]["missing"] == ["STREET"], r3
    r4 = judge({"judge": {"line_letters": [5, 4]}}, "hello\nwo ld\n")
    assert r4["checks"]["lines"]["pass"] and not r4["pass"], r4  # form ok, but a lines-only block fails closed (content)
    r5 = judge({"judge": {"line_letters": [5, 4]}}, "hello\nworld\n")
    assert not r5["pass"], r5
    r6 = judge({"judge": {"initials_regex": "^[MW]LIAOI$"}}, "my love is always only Irene")
    assert r6["pass"], r6
    print("selftest ok: real text PASS, shuffled FAIL (language), missing crib FAIL, line form check ok")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("spec", nargs="?")
    ap.add_argument("--text"); ap.add_argument("--file"); ap.add_argument("--json", action="store_true")
    ap.add_argument("--selftest", action="store_true")
    a = ap.parse_args()
    if a.selftest:
        selftest(); return
    if not a.spec or not (a.text or a.file):
        ap.error("spec and --text or --file are required")
    spec = json.loads(Path(a.spec).read_text(encoding="utf-8"))
    text = a.text if a.text else Path(a.file).read_text(encoding="utf-8")
    if a.file:  # reading files carry "#" header lines (source, grades); score the decode only (LX-JUDGE, 25 Sept 2026)
        text = "\n".join(l for l in text.splitlines() if not l.lstrip().startswith("#"))
    r = judge(spec, text)
    r["spec"] = spec.get("slug", a.spec)
    if a.json:
        print(json.dumps(r, indent=1))
    else:
        for k, v in r["checks"].items():
            print(f"{'ok  ' if v['pass'] else 'FAIL'} {k}: {', '.join(f'{kk}={vv}' for kk, vv in v.items() if kk != 'pass')}")
        print("PASS" if r["pass"] else "FAIL", "-", r["spec"], "(a PASS is a gate for a verifier, not a reading; rule 10)")
    sys.exit(0 if r["pass"] else 1)


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""Build specs/fr2933-salviati-1525.json from the eight settled leaf transcriptions (LANE R8 DSN, 25 Sept 2026).

The spec's ciphertext is one line per SIGN RUN (a maximal stretch of sign boxes between plain boxes or line ends),
each token written code^marks exactly as transcribed (a bare sign is "code^"), so tools/family_run.py reads it in
"space" mode with N = 2,820 sign tokens and K = 223 code+mark types. The interleaving with the plain Italian text
is kept in "row_pattern": one character per box in reading order, S for a sign box and _ for a plain box, and
f.57r line 17 pos 15-24 (a later marginal note, leafnotes/f57r.md) is dropped, both as control/codemark_curve.py
does. Families lay their controls out on that pattern (tools/families/syllabary.py).

  python3 ciphers/fr2933-salviati-1525/build_spec.py            writes specs/fr2933-salviati-1525.json
  python3 ciphers/fr2933-salviati-1525/build_spec.py --check    exits 1 if the committed spec's ciphertext differs
"""
import csv, json, os, sys

D = os.path.dirname(os.path.abspath(__file__))
ROOT = os.path.dirname(os.path.dirname(D))
OUT = os.path.join(ROOT, "specs", "fr2933-salviati-1525.json")
LEAVES = ("f54r", "f54v", "f55r", "f55v", "f56r", "f56v", "f57r", "f57v")


def rows():
    for lf in LEAVES:
        for x in csv.DictReader(open(os.path.join(D, f"ciphertext_{lf}.tsv")), delimiter="\t"):
            if lf == "f57r" and x["line"] == "17" and float(x["pos"]) >= 15:
                continue
            yield lf, x


def build():
    runs, pattern, cur, prev = [], [], [], None
    for lf, x in rows():
        key = (lf, x["line"])
        if key != prev and cur:
            runs.append(cur); cur = []
        prev = key
        if x["code"] != "_":
            cur.append(f"{x['code']}^{x['marks']}"); pattern.append("S")
        else:
            if cur:
                runs.append(cur); cur = []
            pattern.append("_")
    if cur:
        runs.append(cur)
    return runs, "".join(pattern)


def main():
    runs, pattern = build()
    toks = [t for r in runs for t in r]
    spec = {
        "slug": "fr2933-salviati-1525",
        "name": "Cardinal Giovanni Salviati, legate in Spain, to [the papal court], Toledo 16 Oct 1525, BnF Francais 2933 "
                "no.11 f.54r-57v (a nomenclator letter: plain Italian with runs of invented signs, many carrying a "
                "superscript mark)",
        "language_candidates": ["it"],
        "ciphertext_source": "Gallica ark btv1b90600674, canvases 55-59 (images/manifest.json); two blind box-keyed passes per "
                             "leaf against glyphs/atlas_part1.png-atlas_part2.png, reconciled and settled from the image "
                             "(ciphertext_f54r.tsv .. ciphertext_f57v.tsv; NOTES.md sections 'Capture and passes' through "
                             "'Leaves f.55v-f.57v completed'); measured residual error about 5 percent per sign token "
                             "(NOTES 'CM3' sec.1)",
        "ciphertext_date": "transcription 24-25 Sept 2026; spec built 25 Sept 2026 by build_spec.py (LANE R8 DSN)",
        "alphabet": "36 base codes (atlas names: S7 w y g bh lam nt tee o. rz S Z S4 ] phi e dl psi # Lx m eps wd L + f a H p sq v U K [ N ch) "
                    "each optionally carrying a superscript mark string (~ 1 dot # 5 o 7 ot + 3 and their combinations joined "
                    "by |); 223 code+mark types over 2,820 sign tokens; plain boxes (_) are legible Italian words, not transcribed",
        "ciphertext": [" ".join(r) for r in runs],
        "row_pattern": pattern,
        "constraints": [
            "one sign per letter-sized box; 381 sign runs (mean 7.4 signs) interleaved with 1,233 plain-Italian boxes (360 plain runs)",
            "marks concentrate on a few bases: g 51%, e 68%, eps 69%, ] 88%, m 78%, a 82%, H 77% of their tokens marked; "
            "w, tee, nt, bh, rz, S, dl, psi under 10%",
            "the five marks ~ 1 dot 5 7 recur on g, lam, eps, m, a, H (4-5 of the five on each): 528 of the 894 marked tokens",
            "strong bigram structure among bare types (S4^ dl^ 30 of 60 S4; S7^ #^ 28 of 46 #; f^ w^ 19); 55 adjacent identical tokens",
            "no key on file fits (NOTES 'Solver' sec.1, 'Key search'); Meister 1906 keys nos. 8 and 55 name Salviati but are 1540s and a different design"
        ],
        "cheap_tests_in_order": [
            "base codes only, marks ignored, homophonic anneal (LANE R4 I, f.54r N=370): control 75-92%, target no Italian",
            "vi: every consonant+vowel as code+mark (LANE R4 P, N=720): control 93-96%, target no Italian, -2.57/symbol vs -2.30",
            "cm: code+mark as distinct letters, pooled N=2,820, measured 5% error (LANE R7 CM3): control 62-86%, target -2.66/symbol vs -2.38 to -2.51, no Italian",
            "syllabary: base = letter, mark on a consonant base = following vowel, use rate matched to the target's 31.7% marked share, "
            "measured 5% error (LANE R8 DSN, tools/families/syllabary.py)"
        ],
        "cheap_test_done": [],
        "judge": {"language": "it", "letters_min": 2500, "letters_max": 4500, "control_samples": 60},
        "written": "25 Sept 2026, LANE R8 DSN (Fable), .claude/briefs/runs/2026-09-25-lane-r8-dsn-salviati-design.md"
    }
    if "--check" in sys.argv:
        old = json.load(open(OUT, encoding="utf-8"))
        if old.get("ciphertext") != spec["ciphertext"] or old.get("row_pattern") != spec["row_pattern"]:
            print("STALE: committed spec ciphertext differs from the leaf transcriptions"); return 1
        print(f"ok: {len(toks)} tokens, {len(set(toks))} types, {len(runs)} runs, pattern {len(pattern)} boxes"); return 0
    if os.path.exists(OUT):  # keep cheap_test_done rows already recorded
        old = json.load(open(OUT, encoding="utf-8"))
        spec["cheap_test_done"] = old.get("cheap_test_done", [])
    json.dump(spec, open(OUT, "w", encoding="utf-8"), indent=1, ensure_ascii=False)
    print(f"wrote {OUT}: {len(toks)} tokens, {len(set(toks))} types, {len(runs)} runs, pattern {len(pattern)} boxes "
          f"({pattern.count('_')} plain)")
    return 0


if __name__ == "__main__":
    sys.exit(main())

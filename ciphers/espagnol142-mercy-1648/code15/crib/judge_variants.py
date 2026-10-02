#!/usr/bin/env python3
"""judge_variants.py -- run tools/judge_plaintext.py on v04 candidate readings (code 15, issue 16, 1 Oct 2026).

(a) whole reading: reading.txt with only the v04 line replaced, against specs/espagnol142-mercy-1648.json (es corpus);
(b) window: v03-v06 cipher letters (with the trimmed-edge restoration su[ma]no only) against an ad hoc spec in this
    folder (language es17c7, letters_min 40) -- the judge's own real-text windows of the same length are the control.
Also sweeps code 15 over 22 letters x v04:11 in {32 n, 31 i} on the window.
Writes judge_variants.tsv beside this script.
"""
import json, re, subprocess, sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
T = ROOT / "ciphers/espagnol142-mercy-1648"
JUDGE = ROOT / "tools/judge_plaintext.py"

V = {
    "V0 committed (15=n)": "NOLADIRENTNONYSIIUN",
    "V1 15=c, no glyph moved": "NOLADIRECTNONYSIIUC",
    "V2 15=z, no glyph moved": "NOLADIREZTNONYSIIUZ",
    "V3 15=c, v04:11 re-read 31": "NOLADIRECTIONYSIIUC",
    "V4 15=z, v04:11 re-read 31": "NOLADIREZTIONYSIIUZ",
    "V5 V4 + lost [g] at the edge": "NOLADIREZTIONYSIIUZG",
    "V6 Bourdeau word-model (2 glyphs moved)": "NOLADIRECTIONYSIUN",
    "V7 15=c, 31, edge 15 read as c, lost [ion]? (direction only)": "NOLADIRECTIONYSIIUC",
}
W_PRE, W_POST = "EDELLAYQUECORRAPORSUMA", "ASERAMASCONUENIENTAROTRATANTAGENTEDE"

def run(spec, text):
    p = subprocess.run([sys.executable, str(JUDGE), str(spec), "--text", text, "--json"], capture_output=True, text=True)
    try:
        j = json.loads(p.stdout)
    except Exception:
        return None, p.stdout + p.stderr
    return j["checks"].get("language"), None

def main():
    win_spec = HERE / "window_spec.json"
    win_spec.write_text(json.dumps({"slug": "mercy-v04-window", "judge": {"language": "es17c7", "letters_min": 40,
                                                                          "control_samples": 400}}, indent=1))
    lines = (T / "reading.txt").read_text(encoding="utf-8").splitlines()
    body = [l for l in lines if not l.startswith("#")]
    rows = []
    for name, v04 in V.items():
        full = "\n".join(("v04  " + v04) if l.startswith("v04 ") else l for l in body)
        a, ea = run(ROOT / "specs/espagnol142-mercy-1648.json", full)
        b, eb = run(win_spec, W_PRE + v04 + W_POST)
        rows.append((name, v04, a, b))
        print(name, "|", v04)
        print("   full  :", json.dumps(a)[:220] if a else ea[:300])
        print("   window:", json.dumps(b)[:220] if b else eb[:300])
    # sweep
    LET = "abcdefghilmnopqrstuxyz"
    sweep = []
    for mid_tag, mid in (("32", "TNON"), ("31", "TION")):
        for c in LET:
            v04 = "NOLADIRE" + c.upper() + mid + "YSIIU" + c.upper()
            b, _ = run(win_spec, W_PRE + v04 + W_POST)
            sc = None
            if b:
                sc = b.get("score")
            sweep.append((mid_tag, c, sc))
    with open(HERE / "judge_variants.tsv", "w") as fh:
        fh.write("variant\tv04\tfull_language\twindow_language\n")
        for name, v04, a, b in rows:
            fh.write(f"{name}\t{v04}\t{json.dumps(a)}\t{json.dumps(b)}\n")
        fh.write("\n# sweep: window score, code 15 = letter in both v04 places, v04:11 as 32 or 31\nv04_11\tletter\twindow_score\n")
        for r in sorted(sweep, key=lambda r: -(r[2] or -99)):
            fh.write("\t".join(map(str, r)) + "\n")
    for t in ("32", "31"):
        top = sorted([r for r in sweep if r[0] == t], key=lambda r: -(r[2] or -99))[:6]
        print(f"sweep v04:11={t}: " + "  ".join(f"{c}:{s}" for _, c, s in top))

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""judge_input.py: letters-only judge inputs from the committed fr.5160 readings (SPEC-FR17, 3 Oct 2026).

Writes judge_f67_C.txt, judge_f86.txt, judge_f88.txt beside this script: line labels, header lines, the
manuscript's own clear words (upper-case tokens in reading_f67_C.txt, except the key value 'M.', [bracketed] in reading_f86/f88.txt) and '?'
(unkeyed) are dropped, so tools/judge_plaintext.py scores only the deciphered cipher passages.
Also writes judge_gloss_f87.txt (f.87 contemporary decipherment of f.86+f.88, heading dropped) and
judge_gloss_f68.txt (f.68r clear copy of f.67's cipher passages), the rule-3 period-gloss controls.
--check exits 1 if a committed judge_*.txt differs from what the readings regenerate.
"""
import re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent
JOBS = {"judge_f67_C.txt": ("reading_f67_C.txt", "upper"),
        "judge_f86.txt": ("reading_f86.txt", "bracket"),
        "judge_f88.txt": ("reading_f88.txt", "bracket")}

def extract(src, mode):
    out = []
    for line in (HERE / src).read_text(encoding="utf-8").splitlines():
        if not line.strip() or line.startswith("#"):
            continue
        body = re.sub(r"^\S+(\s+L\d+)?\s+", "", line, count=1)  # 'f129 L01<TAB>' or 'L01  '
        body = re.sub(r"\[[^\]]*\]", " ", body).replace("?", " ") if mode == "bracket" else \
            " ".join(t for t in body.split() if t == "M." or not (t.upper() == t and any(c.isalpha() for c in t)))
        body = re.sub(r"\s+", " ", body).strip()
        if body:
            out.append(body)
    return "\n".join(out) + "\n"

def gloss(src, skip):  # period decipherment / clear copy: rule-3 gloss control
    out = []
    for line in (HERE / src).read_text(encoding="utf-8").splitlines()[skip:]:
        if line.startswith("#"):
            continue
        line = re.sub(r"\[del:[^\]]*\]", " ", line)
        line = re.sub(r"\[ins:([^\]]*)\]", r" \1 ", line).replace("[?]", "")
        line = re.sub(r"\s+", " ", line).strip()
        if line:
            out.append(line)
    return "\n".join(out) + "\n"

GLOSS = {"judge_gloss_f87.txt": ("dechiffre_f87.txt", 2), "judge_gloss_f68.txt": ("dechiffre_f68.txt", 0)}

def main():
    stale = 0
    todo = [(d, extract(*a)) for d, a in JOBS.items()] + [(d, gloss(*a)) for d, a in GLOSS.items()]
    for dst, text in todo:
        p = HERE / dst
        if "--check" in sys.argv:
            if not p.exists() or p.read_text(encoding="utf-8") != text:
                print(f"STALE {dst}"); stale = 1
            else:
                print(f"ok {dst}")
        else:
            p.write_text(text, encoding="utf-8"); print(f"wrote {dst}: {sum(c.isalpha() for c in text)} letters")
    sys.exit(stale)

if __name__ == "__main__":
    main()

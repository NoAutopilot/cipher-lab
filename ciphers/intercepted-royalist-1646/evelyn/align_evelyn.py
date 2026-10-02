#!/usr/bin/env python3
"""Known-answer check of key129 against Nicholas's printed interlinear decipherment (GAPS-intercepted-royalist-1646, 2 Oct 2026).

Witness: Evelyn, Diary and Correspondence (1857) iv 178-179 (the King to Nicholas, 24 June and 16 Aug 1646), archive.org
item diarycorresponde41evel, leaves 185-186 (NOT 186-187 as the folder's LIKELY-9 note had it: leaf 186 is p.179, 187 is
p.180, checked on the page images 2 Oct 2026). Input: words_leaf185_186.tsv, the item's own djvu.xml word boxes for those
two leaves (page frame 2098x3570, the same frame as leaf_n186.jpg on disk). A figure line is a line with >= 3 all-digit
tokens; its gloss line is the nearest non-figure line above it within 110 px. Each gloss word is assigned to the figure
token on its figure line whose left edge is nearest the gloss word's left edge (the printer set each gloss flush with its
figure group). Output: gloss_align.tsv (page, y, gloss, figure as OCR'd, dx) and a comparison with ../key.tsv.

Rule 3 control: the same comparison against 20 value-shuffled copies of key.tsv (seeds 1-20), counting how many
(code, value) pairs the gloss table confirms. The control CAN vary (which value sits on which code decides a match),
so it is a test, not a non-test.

Conditional on the OCR (rule 2): the digits are the item's OCR, not the image; where the OCR digit string differs from
Aymeloglu's reading of the same scan (122/422, 102/162, 85G/356) the gloss position is checked but the digits are not.

  python3 ciphers/intercepted-royalist-1646/evelyn/align_evelyn.py            # prints the tables, writes gloss_align.tsv
"""
import csv, os, random, re, sys
from collections import defaultdict

HERE = os.path.dirname(os.path.abspath(__file__))
WORDS = os.path.join(HERE, "words_leaf185_186.tsv")
KEY = os.path.join(HERE, "..", "key.tsv")
OUT = os.path.join(HERE, "gloss_align.tsv")
PAGE = {185: 178, 186: 179}
# OCR digit strings that Aymeloglu's reading of the same scan gives differently (gloss position checked, digits not)
OCR_FIX = {"122": "422", "102": "162", "85G": "356"}
# gloss normalisation: the print's abbreviations and OCR noise -> the key's spelling
GLOSS = {"-word": "word", "-w^^": "which", "■w^''": "which", "-w''>": "with", "vou": "you", "MTite": "write",
         "IT.": "H.", "f<>i*": "for", "liauiiif^": "having", "had,": "had", "not.": "not", "Marq:": "Marquis",
         "Cabinet*": "Cabinet", "I.": "I.H.", "H.": "H."}


def load_words():
    rows = []
    with open(WORDS, encoding="utf-8") as f:
        for r in csv.DictReader(f, delimiter="\t"):
            w = r["word"].strip()
            if not w:
                continue
            rows.append((int(r["leaf"]), int(r["x0"]), int(r["y0"]), int(r["x1"]), int(r["y1"]), w))
    return rows


def lines(rows, leaf):
    """Cluster a leaf's words into lines by y0 (25 px)."""
    ws = sorted([r for r in rows if r[0] == leaf], key=lambda r: (r[2], r[1]))
    out = []
    for r in ws:
        if out and abs(r[2] - out[-1][0]) <= 25:
            out[-1][1].append(r)
        else:
            out.append([r[2], [r]])
    for l in out:
        l[1].sort(key=lambda r: r[1])
    return out


def is_figure_line(words):
    return sum(1 for r in words if re.fullmatch(r"\d+", r[5])) >= 3


SPELLED = {"word", "Cabinet", "desire", "burned", "Jewells", "Southampton", "having", "nor"}


def align():
    """Walk each page's figure lines in reading order. A gloss that is a single word code (not in SPELLED) anchors the
    figure whose left edge is nearest its own. A SPELLED gloss covers the run of figures from the previous anchor on
    its line to the next anchor (across the line break); when the run has exactly as many figures as the gloss has
    letters, each figure gets one letter; otherwise the run is reported as a segmentation ambiguity, unassigned."""
    rows = load_words()
    table = []  # (page, y, gloss, figure_ocr, figure, dx)
    for leaf in (185, 186):
        ls = lines(rows, leaf)
        seq = []  # figures in reading order: dict(page, y, x, fo, fc, gloss, spelled)
        for i, (y, words) in enumerate(ls):
            if not is_figure_line(words):
                continue
            g = None
            for j in range(i - 1, -1, -1):
                if y - ls[j][0] > 110:
                    break
                if not is_figure_line(ls[j][1]):
                    g = ls[j][1]
                    break
            seen_digit = False
            figs = []
            for r in words:
                if re.fullmatch(r"\d+|85G", r[5]):
                    seen_digit = True
                    figs.append(r)
                elif seen_digit and re.fullmatch(r"[A-Za-z]{1,2}", r[5]):
                    figs.append(r)  # an OCR-garbled figure inside the figure run (or, p, at, ad, if, in, no)
            ents = [dict(page=PAGE[leaf], y=y, x=r[1], fo=r[5], fc=OCR_FIX.get(r[5], r[5]), gloss="", spelled="")
                    for r in figs]
            if g is not None:
                for gw in g:
                    gl = GLOSS.get(gw[5], gw[5])
                    if gl == "H." and gw[1] > 1800 and leaf == 185:
                        continue  # the "H." of "I. H." on p.178, one gloss with "I."
                    best = min(ents, key=lambda e: abs(e["x"] - gw[1]))
                    if gl in SPELLED:
                        best["spelled"] = gl
                    else:
                        best["gloss"] = gl
                    best["dx"] = best["x"] - gw[1]
            seq.extend(ents)
        # spelled runs: from the figure after the previous anchor (or the spelled gloss's own line start) to the next anchor
        k = 0
        while k < len(seq):
            e = seq[k]
            if e["spelled"]:
                a = k
                while a > 0 and not seq[a - 1]["gloss"] and seq[a - 1]["y"] == e["y"] and not seq[a - 1]["spelled"]:
                    a -= 1
                b = k
                while b + 1 < len(seq) and not seq[b + 1]["gloss"] and not seq[b + 1]["spelled"] \
                        and seq[b + 1]["page"] == e["page"] and seq[b + 1]["fc"] != "258":
                    b += 1  # 258 opens p.179's undeciphered block ([erased]); stop there
                run = seq[a:b + 1]
                letters = re.sub(r"[^A-Za-z]", "", e["spelled"])
                if len(run) == len(letters):
                    for r, L in zip(run, letters):
                        r["gloss"] = f"{e['spelled']}:{L}"
                else:
                    e["gloss"] = (f"{e['spelled']}[{len(letters)} letters over {len(run)} figures: "
                                  + " ".join(r["fc"] for r in run) + "]")
                k = b + 1
            else:
                k += 1
        for e in seq:
            table.append((e["page"], e["y"], e["gloss"], e["fo"], e["fc"], e.get("dx", 0)))
    with open(OUT, "w", encoding="utf-8") as f:
        f.write("page\ty\tgloss\tfigure_ocr\tfigure\tdx\n")
        for t in table:
            f.write("\t".join(str(x) for x in t) + "\n")
    return table


def load_key():
    key = []
    with open(KEY, encoding="utf-8") as f:
        for r in csv.DictReader((l for l in f if not l.startswith("#")), delimiter="\t"):
            key.append((r["code"], r["value"], r["grade"], r["source"]))
    return key


def norm(v):
    return v.lower().rstrip(".")


def compare(key, gloss_by_code, quiet=False):
    """Count key rows whose (code, value) the gloss table confirms / contradicts / does not reach."""
    conf = contra = unreached = 0
    detail = []
    for code, value, grade, source in key:
        gl = gloss_by_code.get(code)
        if not gl:
            unreached += 1
            detail.append((code, value, grade, source, "unreached", ""))
        elif any(norm(x.split(":")[-1]) == norm(value) for x in gl):
            conf += 1
            detail.append((code, value, grade, source, "confirmed", "|".join(gl)))
        else:
            contra += 1
            detail.append((code, value, grade, source, "contradicted", "|".join(gl)))
    return conf, contra, unreached, detail


def main():
    table = align()
    print("gloss -> figure (page, gloss, figure as OCR'd [-> corrected], dx):")
    for p, y, gl, fo, fc, dx in table:
        if gl:
            print(f"  p.{p} y{y:4d}  {gl:14s} over {fo:>5s}" + (f" -> {fc}" if fc != fo else "") + f"  dx {dx:+d}")
    gloss_by_code = defaultdict(list)
    for p, y, gl, fo, fc, dx in table:
        if gl:
            gloss_by_code[fc].append(gl)
    key = load_key()
    conf, contra, unreached, detail = compare(key, gloss_by_code)
    print(f"\nkey.tsv ({len(key)} rows) vs the gloss table: confirmed {conf}, contradicted {contra}, unreached {unreached}")
    by = defaultdict(lambda: [0, 0, 0])
    for code, value, grade, source, verdict, gl in detail:
        by[(grade, source)][["confirmed", "contradicted", "unreached"].index(verdict)] += 1
        if verdict != "unreached":
            print(f"  {code:>4s} {value:22s} {grade} {source:13s} {verdict:12s} gloss={gl}")
    print("\nper grade/source (confirmed, contradicted, unreached):")
    for k in sorted(by):
        print(f"  {k[0]} {k[1]:13s} {by[k]}")
    # rule 3 control: 20 value-shuffled copies of the key
    codes = [k[0] for k in key]
    values = [k[1:] for k in key]
    confs = []
    for seed in range(1, 21):
        rnd = random.Random(seed)
        v = values[:]
        rnd.shuffle(v)
        shuffled = [(c,) + tuple(val) for c, val in zip(codes, v)]
        confs.append(compare(shuffled, gloss_by_code, quiet=True)[0])
    print(f"\ncontrol: confirmed count on 20 value-shuffled keys: mean {sum(confs)/len(confs):.2f}, max {max(confs)}, "
          f"values {confs}; real {conf}")
    glossed_codes = sorted(gloss_by_code, key=lambda c: (len(c), c))
    print(f"\ngloss table: {sum(1 for t in table if t[2])} gloss words over {len(glossed_codes)} distinct figures; "
          f"figures glossed but not in key.tsv: "
          + ", ".join(f"{c}={'|'.join(gloss_by_code[c])}" for c in glossed_codes if c not in codes))
    return 0


if __name__ == "__main__":
    sys.exit(main())

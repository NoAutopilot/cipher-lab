#!/usr/bin/env python3
"""A3V3-ECKC (4 Oct 2026): word-align the 26 print-matched fully keyed mssEC 18 entries (14 Cipher No. 1, 12 Cipher
No. 2; ec18/matches.tsv, ec18/matches_b2.tsv) against the Official Records text of the same telegram, grade each keyed
token C where the print fixes it, and list key-vs-print disagreements (rule 4: a data conflict, not an error to settle).

Usage: ec18_align.py DATA_DIR OR_DIR [--rows align_free_rows.tsv] [--write | --check]
  --rows (D2-ECK62M, 5 Oct 2026): align the rows ec18.py --print-q wrote (print-free 1f/2f dated matches and the '?'
  entries the print decided), anchors given; writes align_free_{tokens,entries,summary}.tsv; 1f/2f non-AGREE tokens S.
  D2-ECK62R (5 Oct 2026): the output suffix comes from the rows file name (align_flip_rows.tsv -> align_flip_*.tsv);
  a source 'flip-*' row (book flipped against the alignment's evidence) caps non-AGREE tokens at S like print-free.
  DATA_DIR/vol18.json and OR_DIR/<vol>.txt exactly as for ec18.py (not committed; URLs and sha256 in
  ../pilot1864/manifest.tsv and or_volumes.tsv; only the 16 volumes named in the two matches files are needed).
  --write rewrites align_tokens.tsv, align_entries.tsv and align_summary.tsv; --check exits 1 if any is stale.

Method (the folder's or_align.py method: a word-level difflib diff, since both sides are English words and most are
identical; tools/interlinear_align.py aligns cipher groups to letters of a plain line and does not fit). Each entry is
read token by token with ciphers/eckert-1864/decode.py's lookup (imported; key.md for book 1, key-no2.md for book 2);
a keyed token is a code word with a key row of kind word/numeral/time/punct/sig (blind and line indicators are left as
written, as decode_entry does). A possessive "'s" is stripped before the lookup ("Kettle's" = Longstreet's), which
decode.py's lookup does not do, so ec18.py's readings leave such tokens unread. The entry becomes a word sequence (a keyed token contributes its meaning's words, rank
and parenthesised notes dropped; punctuation/signature tokens contribute nothing but are kept for the count). The print
window is the OR text from 120 words before the match anchor to 400 after; difflib aligns the two word sequences.
A keyed word token whose meaning words fall inside an 'equal' block, or inside a replace block whose words are OCR
variants (difflib ratio >= 0.8 pairwise), is AGREE (grade C: the print fixes it); one inside a replace block with
other printed words (at most 3 ledger words against at most 4 printed) is CONFLICT (key value vs print, both listed); one opposite nothing (a delete block), or inside a replace block longer than 3 ledger / 4
printed words (a misalignment, not a substitution), is UNFIXED (keeps its key grade); PARTIAL = some of a multi-word
meaning's words agree. Punctuation, signature and numeral tokens are not scored (OR punctuation is OCR noise; numerals
are scored only when the printed number word or digits match, reported apart). Plain (unkeyed) words opposite other
printed words are listed as candidate code words (kind 'plain-replaced'), never graded.

Control (rule 3; it can fail differently, since only the print window changes): each entry aligned, by the same code,
to a different OR telegram of the same week -- the nearest dated heading in the same volume, 3 days either side of the
entry's date, whose position is more than 700 words from the true anchor (else the next volume of the same set). The
statistic is the share of scored keyed word tokens that AGREE, target vs control, per entry and pooled.
"""
import re, sys, difflib, collections
from pathlib import Path

HERE = Path(__file__).resolve().parent
sys.path.insert(0, str(HERE))
import ec18  # noqa: E402
d1 = ec18.d1

RANK = {"general", "gen", "maj", "major", "brig", "brigadier", "lieut", "lieutenant", "col", "colonel", "capt",
        "captain", "genl", "in", "chief"}


def mwords(meaning):
    m = re.sub(r"\(.*?\)", " ", meaning.lower())
    return re.findall(r"[a-z]+|\d+", m)


def tokens(text, key):
    """[(code word as written, meaning or None, grade or None, kind or 'plain')] for an entry body."""
    out = []
    for w in text.split(" "):
        core = w.strip(" .,;:'\"()")
        if not core:
            continue
        stem, flag, row = d1.lookup(core, key)
        if row is None and re.search(r"['\u2019]s$", core):  # possessive: "Kettle's" (decode.py's lookup misses it)
            core = core[:-2]
            stem, flag, row = d1.lookup(core, key)
        if row is not None and row[2] in ("blind", "line"):
            row = None
        if row is None:
            for p in re.findall(r"[a-z]+|\d+", core.lower()):
                out.append((p, None, None, "plain"))
        else:
            out.append((core, row[0], row[1], row[2]))
    return out


def seq(toks):
    """Flatten to words; owner[i] = token index of word i."""
    ws, own = [], []
    for k, (cw, mean, g, kind) in enumerate(toks):
        if kind == "plain":
            ws.append(cw); own.append(k)
        elif kind in ("word", "time", "month-free", "numeral"):
            for x in mwords(mean):
                if kind != "numeral" and x in RANK:
                    continue
                ws.append(x); own.append(k)
    return ws, own


NUMS = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve",
        "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
ORD = ["", "first", "second", "third", "fourth", "fifth", "sixth", "seventh", "eighth", "ninth", "tenth"]
TENS = {20: "twenty", 30: "thirty", 40: "forty", 50: "fifty", 60: "sixty", 70: "seventy", 80: "eighty", 90: "ninety"}


def numforms(x):
    """A digit string and its number-word forms (cardinal; ordinal for 1-10)."""
    f = {x}
    if x.isdigit():
        n = int(x)
        if n < 20:
            f.add(NUMS[n])
        if n in TENS:
            f.add(TENS[n])
        if 0 < n <= 10:
            f.add(ORD[n])
    return f


def sim(a, b):
    return a == b or difflib.SequenceMatcher(None, a, b).ratio() >= 0.8


def ocr_same(a, b):
    return len(a) == len(b) and all(sim(x, y) for x, y in zip(a, b))


def joined_in(word, pr):
    """The meaning word is a stretch of the printed block joined without spaces (OCR splits 're enforce ments', or a
    clerk's code-word-plus-suffix split 'Paxton paining' = camp+aign), allowing OCR noise."""
    j = "".join(pr)
    if len(word) < 3 or not j:
        return False
    if word in j or sim(word, j):
        return True
    m = difflib.SequenceMatcher(None, word, j, autojunk=False).find_longest_match(0, len(word), 0, len(j))
    return m.size >= 0.8 * len(word) and len(word) >= 5


def content(w):
    """Words that carry a meaning's identity: digits, or letters of length >= 3 that are not rank or a.m./p.m.
    (initials and ranks of a name meaning are not scored; the surname is)."""
    return w.isdigit() or (len(w) >= 3 and w not in RANK and w not in ("the", "and"))


def align(toks, window):
    ws, own = seq(toks)
    st = {}  # token -> list of (status, printed words)
    sm = difflib.SequenceMatcher(None, ws, window, autojunk=False)
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        pr = window[j1:j2]
        for i in range(i1, i2):
            k = own[i]
            cw, mean, g, kind = toks[k]
            if op == "equal":
                s = "AGREE"
            elif op == "replace":
                if (ocr_same(ws[i1:i2], pr) or any(sim(ws[i], x) for x in pr)
                        or any(f in pr for f in numforms(ws[i])) or joined_in(ws[i], pr)):
                    s = "AGREE"
                elif i2 - i1 <= 3 and j2 - j1 <= 4:
                    # the code word itself stands in the print: the clerk wrote it in clear, the lookup over-read it
                    s = "COLLISION" if kind != "plain" and any(sim(cw.lower(), x) or joined_in(cw.lower(), [x])
                                                                for x in pr) else "CONFLICT"
                else:
                    s = "UNFIXED"
            else:
                s = "UNFIXED"
            st.setdefault(k, []).append((s, " ".join(pr[:12]) if op == "replace" else "", content(ws[i])))
    res = []
    for k, (cw, mean, g, kind) in enumerate(toks):
        ss = st.get(k, [])
        if not ss:
            status, pr = ("NOTSCORED" if kind in ("punct", "sig") else "UNFIXED"), ""
        else:
            if any(c for _, _, c in ss):  # score the content words; a meaning with none ("Of the") on all its words
                ss = [x for x in ss if x[2]]
            stats = [s for s, _, _ in ss]
            status = ("AGREE" if all(s == "AGREE" for s in stats) else "PARTIAL" if "AGREE" in stats else
                      "COLLISION" if "COLLISION" in stats else "CONFLICT" if "CONFLICT" in stats else "UNFIXED")
            pr = next((p for s, p, _ in ss if p), "")
        res.append((cw, mean, g, kind, status, pr))
    return res


ST = ("AGREE", "CONFLICT", "UNFIXED", "PARTIAL", "COLLISION")


def score(res):
    c = collections.Counter()
    for cw, mean, g, kind, status, pr in res:
        if kind in ("word", "time", "month-free"):
            c[status] += 1
        elif kind == "numeral":
            c["num_" + status] += 1
    return c


def heading_positions(vw, date):
    y, mo, d = date
    out = []
    for dd in range(d - 3, d + 4):
        if dd < 1 or dd > 31 or dd == d:
            continue
        pat = [ec18.MONTHS[mo - 1].lower(), str(dd)]
        for i in range(len(vw) - 2):
            if vw[i] == pat[0] and vw[i + 1] == pat[1] and vw[i + 2] in (str(y), "18" + str(y)[2:]):
                out.append(i)
    return sorted(out)


def find_anchor(vw, ctx):
    c = ctx.split()
    probe = c[15:25]
    for i in range(len(vw) - len(probe)):
        if vw[i:i + len(probe)] == probe:
            return i
    return None


def main(argv):
    data, ordir = argv[0], argv[1]
    vols, _ = ec18.or_index(ordir, set())
    es = {e["id"]: e for e in ec18.entries(data)}
    keys = {"1": d1.load_key(ec18.ROOT / "ciphers/eckert-1864/key.md"),
            "2": d1.load_key(ec18.ROOT / "ciphers/eckert-1864/key-no2.md")}
    rows, src, sfx = [], {}, ""
    if "--rows" in argv:  # D2-ECK62M: align_free_rows.tsv from ec18.py --print-q (anchor given, no context probe)
        rf = argv[argv.index("--rows") + 1]  # align_<X>_rows.tsv -> align_<X>_*.tsv (D2-ECK62R: _flip, _flipctl)
        sfx = "_" + rf.split("_")[1]
        for line in (HERE / rf).read_text().splitlines()[1:]:
            i, bk, how, date, v, pg, j, n = line.split("\t")
            rows.append((bk, i, date, v, pg, int(j)))
            src[i] = how
    else:
        for bk, f in (("1", "matches.tsv"), ("2", "matches_b2.tsv")):
            for line in (HERE / f).read_text().splitlines()[1:]:
                i, date, v, pg, n, ctx = line.split("\t")
                rows.append((bk, i, date, v, pg, ctx))
    tok_out = ["id\tbook\tor_vol\tor_page_ocr\tside\tidx\tcode_word\tmeaning\tkey_grade\tkind\tstatus\tprinted"]
    ent_out = ["id\tbook\tdate\tor_vol\tor_page_ocr\tscored\tagree\tconflict\tunfixed\tpartial\tcollision\tagree_rate\t"
               "ctl_vol\tctl_offset\tctl_agree\tctl_rate\tnum_agree\tnum_scored\tgrades_after"]
    tot = collections.Counter(); ctot = collections.Counter(); gtot = collections.Counter()
    for bk, i, date, v, pg, ctx in rows:
        e = es[i]
        text = re.sub(r"\s+", " ", " ".join(e["body"])).strip()
        toks = tokens(text, keys[bk])
        vw = vols[v]
        j = ctx if isinstance(ctx, int) else find_anchor(vw, ctx)
        assert j is not None, i
        res = align(toks, vw[max(0, j - 120):j + 400])
        sc = score(res)
        # control: nearest other heading of the same week, > 700 words from the anchor
        cands = [(abs(p - j), v, p) for p in heading_positions(vw, e["date"]) if abs(p - j) > 700]
        if not cands:
            for v2 in sorted(vols):
                if v2 != v:
                    cands += [(10 ** 9, v2, p) for p in heading_positions(vols[v2], e["date"])]
        cv, cp = sorted(cands)[0][1:] if cands else (None, None)
        cres = align(toks, vols[cv][cp:cp + 520]) if cv else []
        csc = score(cres)
        scored = sum(sc[x] for x in ST)
        cscored = sum(csc[x] for x in ST)
        g = collections.Counter()
        for k, (cw, mean, gr, kind, status, pr) in enumerate(res):
            if kind in ("word", "time", "month-free", "numeral", "punct", "sig"):
                # a print-free book (1f/2f) is grade S: its non-AGREE key-row tokens are capped at S
                g["C" if status == "AGREE" else "S" if (src.get(i) == "print-free" or src.get(i, "").startswith("flip-")) and gr in ("H", "C") else gr] += 1
            if kind != "plain" or status == "CONFLICT":
                tok_out.append(f"{i}\t{bk}\t{v}\t{pg}\ttarget\t{k}\t{cw}\t{mean or ''}\t{gr or ''}\t"
                               f"{'plain-replaced' if kind == 'plain' else kind}\t{status}\t{pr}")
        g.pop(None, None)
        gtot.update(g)
        tot.update(sc); ctot.update(csc)
        ent_out.append(f"{i}\t{bk}\t{date}\t{v}\t{pg}\t{scored}\t{sc['AGREE']}\t{sc['CONFLICT']}\t{sc['UNFIXED']}\t"
                       f"{sc['PARTIAL']}\t{sc['COLLISION']}\t{sc['AGREE'] / max(1, scored):.3f}\t{cv}\t{(cp - j) if cv == v else 'other'}\t"
                       f"{csc['AGREE']}\t{csc['AGREE'] / max(1, cscored):.3f}\t{sc['num_AGREE']}\t"
                       f"{sum(x for k, x in sc.items() if k.startswith('num_'))}\t"
                       + ", ".join(f"{k} {g[k]}" for k in "HCSIM" if g[k]))
    s = sum(tot[x] for x in ST)
    cs = sum(ctot[x] for x in ST)
    ents = ent_out[1:]
    above = sum(1 for r in ents if float(r.split("\t")[11]) > float(r.split("\t")[15]))
    summ = ["statistic\tvalue", f"entries\t{len(rows)}",
            f"keyed_word_tokens_scored\t{s}",
            f"target_agree\t{tot['AGREE']}/{s} = {tot['AGREE'] / max(1, s):.3f}",
            f"target_conflict\t{tot['CONFLICT']}", f"target_unfixed\t{tot['UNFIXED']}", f"target_partial\t{tot['PARTIAL']}",
            f"target_collision\t{tot['COLLISION']}",
            f"control_agree\t{ctot['AGREE']}/{cs} = {ctot['AGREE'] / max(1, cs):.3f}",
            f"entries_target_rate_above_control\t{above}/{len(rows)}",
            f"numerals_agree\t{tot['num_AGREE']}/{sum(x for k, x in tot.items() if k.startswith('num_'))}",
            f"grades_after_all_tokens\t" + ", ".join(f"{k} {gtot[k]}" for k in ("HCSIM" if sfx else "HCIM"))]
    outs = {f"align{sfx}_tokens.tsv": "\n".join(tok_out) + "\n", f"align{sfx}_entries.tsv": "\n".join(ent_out) + "\n",
            f"align{sfx}_summary.tsv": "\n".join(summ) + "\n"}
    if "--write" in argv:
        for k, val in outs.items():
            (HERE / k).write_text(val)
    elif "--check" in argv:
        stale = [k for k, val in outs.items() if not (HERE / k).exists() or (HERE / k).read_text() != val]
        if stale:
            sys.stderr.write("stale: " + ", ".join(stale) + "\n")
            return 1
        print("current")
    print(outs[f"align{sfx}_summary.tsv"])
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

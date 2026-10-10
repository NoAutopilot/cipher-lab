#!/usr/bin/env python3
"""Re-derive the readings in reading.md from ciphertext.txt and the tables in key.md (Cipher No. 1, mssEC 41).

An mssEC 19 entry is dictionary-coded plaintext written in the order the sender gave it (no route transposition
is recorded in the ledger): a blind word (the column indicator of the route pages), a time word, the month and
the day in numeral words, the text with names, places, ranks, punctuation and many common words replaced by the
book's arbitraries, the word for "signature", the coded signature, and filler. The reading replaces every code
word by its meaning in brackets and grades each code-word token with the grade of its table row (H = read from
mssEC 41, C = known plaintext, I = inferred from another entry, M = uncertain). Numeral words are combined the
English way (twenty + six = 26; two + thousand + five + hundred = 2500). A code word carrying "ed", "ing" or "s"
is read as the stem plus the ending (the book's own rule, foot of page 24). Words not in any table are left as
written: they are the sender's plain words (including the phonetic spellings "tooth", "toby", "canby").

Usage:  python3 decode.py            # print the readings and the grade counts
        python3 decode.py --check    # exit 1 if the block in reading.md differs from what is derived now
        python3 decode.py --write    # rewrite the derived block inside reading.md
"""
import re
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
START = "<!-- decode.py: derived block starts -->"
END = "<!-- decode.py: derived block ends -->"

PUNCT = {"period": ".", "comma": ",", "semicolon": ";", "semi colon": ";", "colon": ":", "interrogation": "?",
         "interogation": "?", "paragraph": "(paragraph)", "quotation": '"', "exclamation": "!", "dash": "-",
         "parenthesis": "( )", "hyphen": "-"}
MONTHS = {"jany": "Jan", "jan": "Jan", "feby": "Feb", "feb": "Feb", "mch": "Mar", "march": "Mar", "mar": "Mar",
          "april": "Apr", "apl": "Apr", "apr": "Apr", "may": "May", "june": "June", "july": "July", "aug": "Aug",
          "sept": "Sept", "sep": "Sept", "oct": "Oct", "nov": "Nov", "novr": "Nov", "dec": "Dec", "decr": "Dec"}


def load_key(path=HERE / "key.md"):
    """Return {code word (lower): (meaning, grade, kind)} from every '| code word |' table in key.md.

    kind is one of: word, numeral, time, blind, line, punct, sig, month-free. It is taken from a parenthesised
    tag at the end of the meaning ("(numeral)", "(time word)", "(blind word ...)", "(line indicator ...)") or
    from the meaning itself for punctuation and "Signature"."""
    table = {}
    in_table = False
    for line in path.read_text(encoding="utf-8").splitlines():
        if line.startswith("| code word |"):
            in_table = True
            continue
        if not in_table:
            continue
        if not line.startswith("|"):
            in_table = False
            continue
        cells = [c.strip() for c in line.strip().strip("|").split("|")]
        if len(cells) < 3 or set(cells[0]) <= {"-"}:
            continue
        word, meaning, grade = cells[0], cells[1], cells[2]
        low = meaning.lower()
        kind = "word"
        if low.endswith("(numeral)"):
            kind = "numeral"
        elif "(time word)" in low:
            kind = "time"
        elif low.startswith("blind word"):
            kind = "blind"
        elif low.startswith("line indicator"):
            kind = "line"
        elif low in PUNCT:
            kind = "punct"
        elif low in ("signature", "signed"):
            kind = "sig"
        for w in word.split("/"):
            table[w.strip().lower()] = (meaning, grade[0], kind)
    if not table:
        sys.exit("no vocabulary table found in key.md")
    return table


def load_ciphertext(path=HERE / "ciphertext.txt"):
    """Return a list of (header, lines) for every '### ' block in ciphertext.txt."""
    blocks = []
    header, lines = None, []
    for raw in path.read_text(encoding="utf-8").splitlines():
        if raw.startswith("### "):
            if header:
                blocks.append((header, lines))
            header, lines = raw[4:].strip(), []
        elif header is not None:
            if raw.startswith("#") or raw.startswith("<!--") or raw.startswith("note:"):
                continue
            lines.append(raw.rstrip())  # "plain:" lines are kept and read by entry_text
    if header:
        blocks.append((header, lines))
    if not blocks:
        sys.exit("no '### ' blocks found in ciphertext.txt")
    return blocks


def entry_text(lines):
    """Join the manuscript lines after the header line, dropping <del>..</del>, the <ins> tags and the '=' joins.

    A line "plain: word word" (the orchestrator's note that these tokens are the sender's plain English although
    they are printed in the book, e.g. "person" in "one additional person") is not text: its words are marked
    with a trailing backslash so that lookup() leaves them alone.

    Two further per-entry note lines (FIX-FM1, 8 Oct 2026; the transcription itself is never edited):
    "variant: surface=Key[:G]" reads the token as written as key row Key (a clerk's spelling variant; G overrides the
    row's grade, e.g. M for a variant spelling; "'s" and the endings s/ed/ing/er after Key still apply);
    "split: word" ends a numeral run before that token (a count and a calibre written side by side, "six 3-inch").

    Three more (FIX-FM3, 8-9 Oct 2026): "plain-at: word#n" marks only the n-th occurrence (1-based, in reading order)
    of that word plain (the same word is a code word elsewhere in the entry); "gloss: surface=Meaning_words[:G]"
    reads a token no key row supplies (a meaning from a printed or period source; underscores are spaces; G defaults
    to M), rendered "[Meaning]" and graded G; "join: word" lets the numeral run at that token continue across a
    plain "and" just before it (one hundred and three = 103), the "and" being dropped from the reading.

    Two more (HOLDER-EXPORT fix, 9 Oct 2026; for carrying an audit's hand grades into the derived block):
    "merge: a+b[+c]" joins consecutive tokens written apart into one token before it is looked up (a code word the clerk
    split across a space or a line, "pan - a. / ma" = Panama); "graded: word[:G]" leaves the token as written (no key row
    is applied) but counts it as a code-word token of grade G (default M): a plain sound-alike standing where a code word
    was expected (I), a token whose status the audit leaves uncertain (M), or a group nobody has read (U).

    One more (FIX-FM7, 9 Oct 2026): "cut-after: word#n" drops every token after the n-th occurrence of that word (1-based,
    reading order): a struck or cancelled entry that follows the real text on the same leaf (E252's 1 Sept entry),
    recorded in NOTES.md instead of the reading.

    One more (FIX-FM8, 9 Oct 2026): "unjoin: word" keeps the ' - ' just after that word a printed dash between two
    words instead of the dis - missed style join (E280 "immediately - wrangle" is two words, not "immediatelywrangle").

    One more (FIX-N2IC-DATE, 10 Oct 2026; AUDIT AUD2-LEDGER10-4): "year: word" starts a numeral run at that token that is
    read as a year, the first value as hundreds and the rest combined the English way ([18, 60, 1] -> 1861, "eighteen
    sixty-one"), instead of summed ([79]); the tokens and their grades are unchanged."""
    plain = set()
    cut_after = None
    variant = {}
    split = set()
    plain_at = {}
    gloss = {}
    join = set()
    merge = []
    graded = {}
    unjoin = set()
    year = set()
    body = []
    for l in lines[1:]:
        if l.startswith("plain:"):
            plain.update(w.lower() for w in l[6:].split())
        elif l.startswith("variant:"):
            for pair in l[8:].split():
                sf, tg = pair.split("=", 1)
                variant[sf.lower()] = tg if ":" in tg else tg + ":"
        elif l.startswith("split:"):
            split.update(w.lower() for w in l[6:].split())
        elif l.startswith("plain-at:"):
            for t in l[9:].split():
                wd, n = t.rsplit("#", 1)
                plain_at.setdefault(wd.lower(), set()).add(int(n))
        elif l.startswith("gloss:"):
            for pair in l[6:].split():
                sf, tg = pair.split("=", 1)
                m, g = tg.rsplit(":", 1) if ":" in tg else (tg, "M")
                gloss[sf.lower()] = (m, g)
        elif l.startswith("join:"):
            join.update(w.lower() for w in l[5:].split())
        elif l.startswith("merge:"):
            merge.extend([p.lower() for p in t.split("+")] for t in l[6:].split())
        elif l.startswith("cut-after:"):
            wd, n = l[10:].split()[0].rsplit("#", 1)
            cut_after = (wd.lower(), int(n))
        elif l.startswith("year:"):
            year.update(w.lower() for w in l[5:].split())
        elif l.startswith("unjoin:"):
            unjoin.update(w.lower() for w in l[7:].split())
        elif l.startswith("graded:"):
            for t in l[7:].split():
                wd, g = t.rsplit(":", 1) if ":" in t else (t, "M")
                graded[wd.lower()] = g
        elif l.strip():
            body.append(l)
    text = " ".join(body)
    text = re.sub(r"<del>.*?</del>", " ", text)
    text = re.sub(r"<deletion>(.*?)</deletion>", r"\1", text)  # a struck-through ending is read as written (polka<deletion>er</deletion> = polkaer, FIX-FM5)
    text = re.sub(r"</?ins>", "", text)
    text = re.sub(r"\s+=\s+", "", text)  # "Lock = wood" -> "Lockwood"
    for w in unjoin:
        text = re.sub(r"\b(%s)\s+-\s+" % re.escape(w), r"\1 ", text, flags=re.I)
    text = re.sub(r"\s+-\s+", "", text)  # "dis - missed" -> "dismissed"
    text = re.sub(r"\s+", " ", text).strip()
    if cut_after:
        ws, seen = text.split(" "), 0
        for k, w in enumerate(ws):
            if w.strip(" .,;:'\"()").lower() == cut_after[0]:
                seen += 1
                if seen == cut_after[1]:
                    text = " ".join(ws[:k + 1])
                    break
    for parts in merge:
        ws, out, i = text.split(" "), [], 0
        while i < len(ws):
            seg = ws[i:i + len(parts)]
            if len(seg) == len(parts) and [x.strip(" .,;:'\"()").lower() for x in seg] == parts:
                out.append("".join(x.strip(" .,;:'\"()") for x in seg) + seg[-1][len(seg[-1].rstrip(" .,;:'\"()")):])
                i += len(parts)
            else:
                out.append(ws[i])
                i += 1
        text = " ".join(out)
    if plain_at or join:
        seen, out = {}, []
        for w in text.split(" "):
            c = w.strip(" .,;:'\"()").lower()
            seen[c] = seen.get(c, 0) + 1
            if c in join and out and out[-1].strip(" .,;:'\"()").lower() == "and":
                out.pop()
            if seen[c] in plain_at.get(c, ()):
                w += "\\"
            out.append(w)
        text = " ".join(out)
    if plain:
        text = " ".join(w + "\\" if w.strip(" .,;:'\"()").lower() in plain else w for w in text.split(" "))
    if variant or split or gloss or graded or year:
        out = []
        for w in text.split(" "):
            c = w.strip(" .,;:'\"()").lower()
            if c in split:
                out.append("|")
            if c in year:
                out.append("^")
            if c in gloss:
                w = f"{w}~!{gloss[c][0]}~{gloss[c][1]}"
            elif c in graded:
                w = f"{w}~=~{graded[c]}"
            elif c in variant:
                tg, g = variant[c].rsplit(":", 1)
                w = f"{w}~{tg}~{g}"
            out.append(w)
        text = " ".join(out)
    return text


def lookup(core, key, possessive=False):
    """Return (stem, ending, row) for a token, allowing the doubtful flag [?] and the endings s, es, ed, d, ing.

    possessive=True (RUN3-ECK62, 4 Oct 2026; off by default): a core ending in "'s" that is not itself keyed is looked
    up without it, and the ending comes back as "'s" ("Kettle's" -> Kettle, "'s"; key-no2.md Kettle = Longstreet)."""
    flag = ""
    if core.endswith("\\"):
        return core[:-1], "", None
    if possessive and re.search(r"['\u2019]s$", core) and core.lower() not in key:
        stem, end, row = lookup(core[:-2], key)
        if row is not None and not end:
            return stem, "'s", row
    if core.endswith("[?]"):
        core, flag = core[:-3], "[?]"
    low = core.lower()
    if low in key:
        return core, flag, key[low]
    for end in ("s", "es", "ed", "d", "ing", "ers", "er"):
        if low.endswith(end) and low[: -len(end)] in key:
            return core[: -len(end)], end + flag, key[low[: -len(end)]]
    if low.endswith("th") and low[:-2] in key and key[low[:-2]][2] == "numeral":
        return core[:-2], "th" + flag, key[low[:-2]]  # ordinal: Glory + th = 17th (FIX-FM1)
    if low.endswith("ing") and low[:-3] + "e" in key:
        return core[:-3] + "e", "ing" + flag, key[low[:-3] + "e"]
    return core, flag, None


class CollisionGuard:
    """Leave a keyed word-kind token as the clerk wrote it when the clear reading is ordinary English in context
    (RUN3-ECK62, 4 Oct 2026; pre-registered in ciphers/eckert-1862/ec18/PREREG-ECK62.md).

    Built from word unigram/bigram counts of a corpus (lowercased [a-z]+ after deleting apostrophes). For code word w
    (as written, lowercase), p / n the previous / next word as read, m1 / m2 the first / last word of the meaning:
    rule J: w joined with its plain left and/or right neighbour forms a corpus word of >= 7 letters, count >= 2;
    rule B: P = c(p,w) + c(w,n) >= 3 and P > 2 * (c(p,m1) + c(m2,n)).
    Catches "bush whack hers" (J) and "the opinion of" (B); must not block a code word whose meaning reads better in
    context ("[Washington]" for Grapes after "to"). Tests: tools/tests/test_eckert_decode.py."""

    def __init__(self, texts):
        import collections
        self.uni, self.bi = collections.Counter(), collections.Counter()
        for t in texts:
            ws = re.findall(r"[a-z]+", t.lower().replace("'", "").replace("\u2019", ""))
            self.uni.update(ws)
            self.bi.update(zip(ws, ws[1:]))

    def why(self, p, w, n, meaning, p_plain=None, n_plain=None):
        """Return 'J', 'B' or '' for code word w between read words p and n (None = no word)."""
        w = w.lower().replace("'", "")
        for a, b in ((p_plain, None), (None, n_plain), (p_plain, n_plain)):
            if a is None and b is None:
                continue
            j = (a or "") + w + (b or "")
            if len(j) >= 7 and self.uni[j.lower()] >= 2:
                return "J"
        mw = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", meaning.lower()))
        if not mw:
            return ""
        P = (self.bi[(p, w)] if p else 0) + (self.bi[(w, n)] if n else 0)
        K = (self.bi[(p, mw[0])] if p else 0) + (self.bi[(mw[-1], n)] if n else 0)
        return "B" if P >= 3 and P > 2 * K else ""


def _read_word(token, key, possessive, first=True):
    """The word a token reads as (lowercase): the meaning's first/last word if keyed (word kind), else the plain word;
    None for punctuation/numeral/time/signature/brace tokens. Second value: the plain word if unkeyed, else None."""
    core = token.strip(" .,;:'\"()").replace("\\", "")
    if not core or core.startswith("{"):
        return None, None
    stem, flag, row = lookup(core, key, possessive)
    if row is not None and row[2] not in ("blind", "line"):
        if row[2] != "word":
            return None, None
        mw = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", row[0].lower()))
        return (mw[0] if first else mw[-1]) if mw else None, None
    low = re.sub(r"[^a-z]", "", core.lower())
    return (low or None), (low or None)


def number(values):
    """Combine numeral values the English way: [20, 6] -> 26; [2, 1000, 5, 100] -> 2500."""
    total, cur = 0, 0
    for v in values:
        if v in (100, 1000):
            cur = (cur or 1) * v
            if v == 1000:
                total, cur = total + cur, 0
        else:
            cur += v
    return total + cur


def decode_entry(text, key, possessive=False, guard=None, guarded=None, tokens=None):
    """Return (reading, counts). The tail (signature marker onwards) is set apart in braces.

    possessive: see lookup(). guard: a CollisionGuard; a word-kind token it fires on is left as written, ungraded,
    and (index, word, meaning, rule) is appended to the list `guarded` when one is given. Both off by default.
    tokens: a list; when given, one (index, word as written, meaning, grade, kind) tuple is appended for every counted
    code-word token, in reading order (tools/holder_export.py lists the code words from it; meaning '' and kind
    'as-written' for a "graded:" token). The reading and counts do not depend on it."""
    words = text.split(" ")
    out = []
    counts = {"H": 0, "C": 0, "I": 0, "M": 0}
    i = 0
    signed = False
    tail = []
    as_year = False
    while i < len(words):
        w = words[i]
        if w == "|":  # "split:" note: only ends the numeral run before it
            i += 1
            continue
        if w == "^":  # "year:" note: the numeral run starting at the next token is a year
            as_year = True
            i += 1
            continue
        ovr = None
        if "~" in w:  # "variant:" note: surface~Key~Grade
            surface, target, ovr = w.split("~")
            if target == "=":  # "graded:" note: kept as written, counted with the audit's grade
                counts[ovr] = counts.get(ovr, 0) + 1
                if tokens is not None:
                    tokens.append((i, surface.strip(" .,;:'\"()"), "", ovr, "as-written"))
                (tail if signed else out).append(surface)
                i += 1
                continue
            if target.startswith("!"):  # "gloss:" note: a meaning no key row supplies
                w = core = surface
                stem, flag, row = core.strip(" .,;:'\"()"), "", (target[1:].replace("_", " "), ovr, "word")
            else:
                w, core = surface, target.strip(" .,;:'\"()")
                stem, flag, row = lookup(core, key, True)
                if row is not None and ovr:
                    row = (row[0], ovr, row[2])
        else:
            core = w.strip(" .,;:'\"()")
            stem, flag, row = lookup(core, key, possessive)
        if row is not None and row[2] == "word" and guard is not None and not signed:
            prev = None
            if out and not out[-1].startswith("{") and not out[-1].endswith("}"):
                po = out[-1]
                mm = re.findall(r"\[([^\]]*)\]", po)
                if mm:
                    pw = re.findall(r"[a-z]+", re.sub(r"\(.*?\)", " ", mm[-1].lower()))
                    prev, pplain = (pw[-1] if pw else None), None
                else:
                    prev = re.sub(r"[^a-z]", "", po.lower()) or None
                    pplain = prev
            else:
                pplain = None
            nxt, nplain = _read_word(words[i + 1], key, possessive) if i + 1 < len(words) else (None, None)
            rule = guard.why(prev, core, nxt, row[0], pplain, nplain)
            if rule:
                if guarded is not None:
                    guarded.append((i, core, row[0], rule))
                row = None
        if row is not None and row[2] in ("blind", "line"):
            # route indicators are never used inside an untransposed entry, and the printed words collide with
            # plain English ("must", "wait", "week", "June", "Army"): left as written, not graded
            row = None
        if row is None:
            w = w.replace("\\", "")
            if core.lower() in MONTHS and i + 1 < len(words):
                # month followed by numeral words: read the date
                j, vals = i + 1, []
                while j < len(words):
                    s2, f2, r2 = lookup(words[j].strip(" .,;:'\"()"), key, possessive)
                    if r2 and r2[2] == "numeral":
                        vals.append(int(r2[0].split()[0]))
                        counts[r2[1]] += 1
                        if tokens is not None:
                            tokens.append((j, words[j].strip(" .,;:'\"()"), r2[0], r2[1], r2[2]))
                        j += 1
                    else:
                        break
                if vals:
                    out.append(f"{{date: {MONTHS[core.lower()]} {number(vals)}}}")
                    i = j
                    continue
            (tail if signed else out).append(w)
            i += 1
            continue
        meaning, grade, kind = row
        counts[grade] = counts.get(grade, 0) + 1
        if tokens is not None:
            tokens.append((i, w.strip(" .,;:'\"()"), meaning, grade, kind))
        if kind == "numeral":
            j, vals = i, []
            while j < len(words):
                if j == i and ovr is not None:  # a "variant:" token: its row is already resolved above
                    s2, f2, r2 = stem, flag, row
                else:
                    s2, f2, r2 = lookup(words[j].strip(" .,;:'\"()"), key, possessive)
                if r2 and r2[2] == "numeral":
                    vals.append(int(r2[0].split()[0]))
                    if j > i:
                        counts[r2[1]] += 1
                        if tokens is not None:
                            tokens.append((j, words[j].strip(" .,;:'\"()"), r2[0], r2[1], r2[2]))
                    j += 1
                else:
                    break
            if as_year and len(vals) > 1:
                rendered = "[" + str(vals[0] * 100 + number(vals[1:])) + "]" + flag
            else:
                rendered = "[" + str(number(vals)) + "]" + flag
            as_year = False
            i = j
        elif kind == "time":
            rendered = "{time: " + meaning.split("(")[0].strip() + "}" + flag
            i += 1
        elif kind == "punct":
            rendered = "[" + PUNCT[meaning.lower()] + "]" + flag
            i += 1
        elif kind == "sig":
            signed = True
            rendered = "[signed]"
            i += 1
        else:
            end = flag.replace("[?]", "")
            q = "[?]" if flag.endswith("[?]") else ""
            rendered = "[" + meaning + "]" + ("'" + end if end == "s" and meaning[:1].isupper() else end) + q
            i += 1
        (tail if signed else out).append(rendered)
    reading = " ".join(out)
    if tail:
        reading += "  {tail: " + " ".join(tail) + "}"
    return reading, counts


def derive(key, blocks):
    parts = []
    total = {"H": 0, "C": 0, "I": 0, "M": 0}
    for header, lines in blocks:
        text = entry_text(lines)
        reading, counts = decode_entry(text, key)
        for k, v in counts.items():
            total[k] = total.get(k, 0) + v
        grade_line = ", ".join(f"{k} {v}" for k, v in counts.items() if v)
        parts.append(f"**{header}**\n\n{reading}\n\nCode-word tokens: {grade_line or 'none'}.\n")
    parts.append(f"Totals over the {len(blocks)} entries: " + ", ".join(f"{k} {v}" for k, v in total.items()) + ".")
    return "\n".join(parts).rstrip() + "\n"


def main(argv):
    key = load_key()
    blocks = load_ciphertext()
    derived = derive(key, blocks)
    reading_path = HERE / "reading.md"
    if "--write" in argv:
        current = reading_path.read_text(encoding="utf-8") if reading_path.exists() else f"{START}\n{END}\n"
        if START not in current or END not in current:
            sys.exit("reading.md lacks the derived-block markers")
        head, rest = current.split(START, 1)
        _, foot = rest.split(END, 1)
        reading_path.write_text(head + START + "\n" + derived + END + foot, encoding="utf-8")
        print("reading.md updated")
        return 0
    if "--check" in argv:
        current = reading_path.read_text(encoding="utf-8")
        inside = current.split(START, 1)[1].split(END, 1)[0].strip("\n") + "\n"
        if inside != derived:
            sys.stderr.write("reading.md is stale: the derived block differs from decode.py output\n")
            return 1
        print("reading.md is current")
        return 0
    print(derived)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))

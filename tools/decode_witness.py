#!/usr/bin/env python3
"""Score a symbol/nomenclator key against a witness leaf that carries a period clerk's plaintext
decipherment (CLAUDE.md rule 3, LESSONS.md "Symbol ciphers: known plaintext first, then a reader").

Three inputs, all TSV:
  key    header 'sign  value  kind  grade  source  note' (kind: letter | word | name), one row per drawn
         homophone; '#'-prefixed lines and blank lines are skipped and do not count towards the 1-based
         data-row numbering that --signs' key_row column refers to.
  signs  header 'line  pos  key_row  shape_note  confidence': one row per cipher sign transcribed from the
         witness image. key_row is either an integer (1-based row number in the key file), '?' (sign not
         placed in the key), or 'nNN' for a plain two-digit number kept as drawn (looked up by an exact
         match, after stripping surrounding whitespace, against the key's own 'sign' column, e.g. 'n85'
         against a row whose sign text is exactly "85" -- not a substring match, which would let a 1-digit
         sign resolve against an unrelated earlier row whose sign merely contains those digits, MONT-4715B,
         27 Sept 2026; a number with no matching row decodes as unknown, same as '?').
  plain  header 'line  text  confidence': the clerk's plaintext decipherment, one row per line (its own line
         numbers if the witness has no interlinear correspondence -- decode_witness only needs the running
         text, not a line-for-line correspondence, since alignment is global over the whole passage).

    python3 tools/decode_witness.py --key K.tsv --signs S.tsv --plain P.tsv [--shuffles 20] [--seed 1]
            [--sample-lines 2,5,9] [--key-rows-out witness/key_rows_f178.tsv]

Decoding: key_row -> value (a letter for kind=letter, the whole word's letters for kind=word/name; '?' and
an unmatched numeral -> '_', a character that cannot match anything). The decoded stream and the clerk
stream are each normalized (lower-case, letters only, j->i, v->u -- the period Italian i/j and u/v pairs)
then aligned once, globally, over the whole passage (not per line) by a match/mismatch/no-gap dynamic
program (equivalent to longest common subsequence): every clerk letter is either matched by one decoded
letter, in the same order, or left unmatched. agreement = matches / len(clerk letters).

Control (rule 3): the same score under --shuffles keys whose values are permuted among the letter-kind
rows only (the multiset of letter values, hence each letter's homophone count, is preserved; word/name
rows are never shuffled). Reports the shuffled mean, sd, z of the real score, and the real key's rank
among itself plus the shuffled keys (1 = best of all).

--sample-lines restricts both streams to the named line ids first (the honest error measure on a blind
transcription sample with no clerk gloss visible to the reader) and runs its own --shuffles-key control.

--key-rows-out writes one row per key-file row: how many times its value was confirmed (the aligned clerk
letter equals it) vs contradicted (aligned to a different clerk letter), from the same alignment.

--label-diffs (MQS-WITNESS-LABELS, 9 Oct 2026; Lasry, Biermann and Tomokiyo 2023, Cryptologia 47:2, pp.102,
110, 122-124: printed plaintext copies diffed against the decipherment). Instead of only reconciling a decode
with a printed or clear witness, label every difference:

    python3 tools/decode_witness.py --label-diffs --decode reading.txt --witness copy.txt
            [--abbrev abbrev.tsv] [--names names.txt] [--min-addition 2] [--labels-out diffs.tsv]

  --decode is a reading as tools/decode_key.py writes it ('#' lines skipped, an optional 'line<TAB>' prefix,
  space-separated tokens, word division optional: the decode may be letter by letter). '[/]' and '<...>' tags
  are dropped; any other bracketed token, '?', '_' or a token with a digit is an unread sign or code and
  becomes one code mark. --witness is running text (a printed edition, a clear copy, a clerk's gloss).
  Both are reduced to a letter stream (lower case, accents stripped, long s -> s) and aligned once, globally,
  by edit distance (match 0, substitution 1, gap 1); every difference is then projected onto the witness
  words and labelled:
    omission       a witness word with no decode letter aligned to it (the decode, or the cipher, lacks it)
    addition       a run of >= --min-addition decode letters between two witness words
    substitution   a witness word whose aligned decode letters differ after normalisation
    name/code      a code mark (unread sign, numeral, nomenclature group) aligned to the word or in the run,
                   or a --names word the decode renders otherwise
    spelling-only  differs letter for letter but equal after normalisation (rule 3, PX-BRODEC: j->i, v->u,
                   y->i, doubled letters single, --abbrev expansions on witness words) -- notation, not error
    equal          the rest (listed in --labels-out, not counted as a difference)
  Meant to catch: dropped and inserted words, wrong words, unread codes, and spelling-only variants that a raw
  diff would count as errors. Must NOT do: call a one-letter change outside the normalisation pairs (pas/par,
  roy/loy) spelling-only -- normalisation must not hide a substitution (offline test; planted control in
  tools/tests/PREREG-MQS-WITNESS-LABELS.md). A label is a description of the difference, never a verdict on
  which side is right (the copyist may expand, the cipher may omit: Pisany kp86, NOTES.md).

  Known limit (planted control, PREREG-MQS-WITNESS-LABELS.md, shelf weak): the letter-level alignment spreads a
  dropped or inserted word onto its neighbours, so omissions and additions are often labelled substitution (arm A
  omission 37/80, addition 48/80; overall 0.786 vs gate 0.90; real Pisany decode 0.610 vs 0.70). Read the per-item TSV.

  --plant-control N runs the planted-difference control instead: N seeds; at witness words the unplanted run
  labels equal, plant omission / addition / substitution (half whole-word, half one-letter) / spelling-only /
  name/code in equal numbers, re-label, and score label accuracy at the planted sites against a label-shuffled
  null (the tool's own labels permuted across sites, --shuffles times). --plant-base witness uses the witness
  letters themselves as a clean decode.

--criteria-scan FILE (MQS-WITNESS-LABELS) flags sentences of a clear copy that meet the 'sent in cipher'
criteria of Lasry, Biermann and Tomokiyo 2023 p.131 n.70 (tools/data/sent_in_cipher_criteria.tsv: references to
the cipher channel, to other cipher letters, hostile statements) as a LEAD that the passage may have been in
cipher -- never a verdict; graded weak on the shelf (no known answer of its own). --lang picks the rows.

Exit 2 on a malformed key/signs/plain file (missing header column, a key_row that is neither an integer,
'?', nor 'nNN', or a plain-file line id that duplicates one already read). Exit 0 otherwise, report on stdout.
"""
import argparse
import os
import random
import re
import sys
import unicodedata


def _read_tsv(path, required_cols):
    rows = []
    with open(path, encoding="utf-8") as f:
        lines = [ln.rstrip("\n") for ln in f]
    header = None
    for ln in lines:
        if not ln.strip() or ln.startswith("#"):
            continue
        cols = ln.split("\t")
        if header is None:
            header = cols
            missing = [c for c in required_cols if c not in header]
            if missing:
                raise ValueError(f"{path}: missing column(s) {missing} in header {header}")
            continue
        row = dict(zip(header, cols))
        rows.append(row)
    if header is None:
        raise ValueError(f"{path}: no header row found")
    return rows


def load_key(path):
    """Returns (rows, letter_row_idxs) -- rows is a 1-based dict {row_num: {sign,value,kind,...}}."""
    raw = _read_tsv(path, ["sign", "value", "kind"])
    rows = {}
    for i, r in enumerate(raw, start=1):
        rows[i] = r
    letter_idxs = [i for i, r in rows.items() if r["kind"] == "letter"]
    return rows, letter_idxs


def _numeral_lookup(rows, digits):
    for i, r in rows.items():
        if r["sign"].strip() == digits:
            return r["value"]
    return None


def key_row_value(rows, key_row):
    key_row = key_row.strip()
    if key_row in ("", "?"):
        return "_"
    if key_row.startswith("n") and key_row[1:].isdigit():
        v = _numeral_lookup(rows, key_row[1:])
        return v if v is not None else "_"
    if key_row.lstrip("-").isdigit():
        idx = int(key_row)
        if idx not in rows:
            raise ValueError(f"signs file: key_row {idx} is out of range for the key file")
        return rows[idx]["value"]
    raise ValueError(f"signs file: malformed key_row {key_row!r} (want an integer, '?', or 'nNN')")


def load_signs(path, key_rows):
    raw = _read_tsv(path, ["line", "pos", "key_row"])
    out = []
    for r in raw:
        value = key_row_value(key_rows, r["key_row"])
        out.append({"line": r["line"], "pos": r["pos"], "key_row": r["key_row"], "value": value})
    return out


def load_plain(path):
    raw = _read_tsv(path, ["line", "text"])
    seen = set()
    out = []
    for r in raw:
        if r["line"] in seen:
            raise ValueError(f"{path}: duplicate line id {r['line']!r}")
        seen.add(r["line"])
        out.append(r)
    return out


NORM_TABLE = str.maketrans({"j": "i", "v": "u"})


def normalize(text):
    return "".join(ch for ch in text.lower().translate(NORM_TABLE) if ch.isalpha())


def decoded_stream(signs, lines=None):
    """Returns a list of (char, key_row) in line/pos order, restricted to `lines` if given."""
    items = signs if lines is None else [s for s in signs if s["line"] in lines]

    def sort_key(s):
        try:
            pos = int(s["pos"])
        except ValueError:
            pos = s["pos"]
        return (s["line"], pos)

    items = sorted(items, key=sort_key)
    out = []
    for s in items:
        for ch in normalize(s["value"]):
            out.append((ch, s["key_row"]))
    return out


def clerk_stream(plain_rows, lines=None):
    items = plain_rows if lines is None else [p for p in plain_rows if p["line"] in lines]
    text = "".join(p["text"] for p in items)
    return list(normalize(text))


def lcs_align(decoded_chars, clerk_chars):
    """decoded_chars: list of chars (or (char, tag) tuples). clerk_chars: list of chars.
    Longest common subsequence by dynamic programming; returns (match_count, pairs) where pairs is a
    list of (decoded_index, clerk_index) for each matched position, in order."""
    a = [c if isinstance(c, str) else c[0] for c in decoded_chars]
    b = clerk_chars
    n, m = len(a), len(b)
    # DP table sized (n+1) x (m+1); fine at the sizes a witness passage reaches (low thousands).
    dp = [[0] * (m + 1) for _ in range(n + 1)]
    for i in range(1, n + 1):
        ai = a[i - 1]
        row, prow = dp[i], dp[i - 1]
        for j in range(1, m + 1):
            if ai == b[j - 1]:
                row[j] = prow[j - 1] + 1
            else:
                row[j] = row[j - 1] if row[j - 1] >= prow[j] else prow[j]
    pairs = []
    i, j = n, m
    while i > 0 and j > 0:
        if a[i - 1] == b[j - 1] and dp[i][j] == dp[i - 1][j - 1] + 1:
            pairs.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif dp[i - 1][j] >= dp[i][j - 1]:
            i -= 1
        else:
            j -= 1
    pairs.reverse()
    return dp[n][m], pairs


def score(signs, plain_rows, key_rows, lines=None):
    dec = decoded_stream(signs, lines)
    clk = clerk_stream(plain_rows, lines)
    if not clk:
        raise ValueError("no clerk letters in scope (empty plain text for the given lines)")
    matches, pairs = lcs_align(dec, clk)
    agreement = matches / len(clk)
    return agreement, matches, len(clk), dec, clk, pairs


def shuffled_key_rows(key_rows, letter_idxs, rng):
    values = [key_rows[i]["value"] for i in letter_idxs]
    shuffled_values = values[:]
    rng.shuffle(shuffled_values)
    new_rows = {i: dict(r) for i, r in key_rows.items()}
    for idx, v in zip(letter_idxs, shuffled_values):
        new_rows[idx] = dict(new_rows[idx])
        new_rows[idx]["value"] = v
    return new_rows


def control(signs_raw, plain_rows, key_rows, letter_idxs, shuffles, seed, lines=None):
    """signs_raw: the raw signs rows (line/pos/key_row) before key lookup, so each shuffled key can be
    applied fresh. Returns (real_agreement, shuffled_scores)."""
    real_signs = [dict(s, value=key_row_value(key_rows, s["key_row"])) for s in signs_raw]
    real_agreement, real_matches, clerk_n, _, _, real_pairs = score(real_signs, plain_rows, key_rows, lines)
    shuffled_scores = []
    rng = random.Random(seed)
    for k in range(shuffles):
        sk_rows = shuffled_key_rows(key_rows, letter_idxs, rng)
        sk_signs = [dict(s, value=key_row_value(sk_rows, s["key_row"])) for s in signs_raw]
        agr, _, _, _, _, _ = score(sk_signs, plain_rows, sk_rows, lines)
        shuffled_scores.append(agr)
    return real_agreement, real_matches, clerk_n, shuffled_scores, real_pairs, real_signs


def summarize(label, real_agreement, real_matches, clerk_n, shuffled_scores):
    n = len(shuffled_scores)
    mean = sum(shuffled_scores) / n if n else 0.0
    var = sum((x - mean) ** 2 for x in shuffled_scores) / n if n else 0.0
    sd = var ** 0.5
    z = (real_agreement - mean) / sd if sd > 0 else float("inf") if real_agreement > mean else 0.0
    rank = 1 + sum(1 for x in shuffled_scores if x > real_agreement)
    lines = [
        f"{label}: real key {real_agreement:.4f} ({real_matches}/{clerk_n} aligned letters); "
        f"{n} shuffled keys mean {mean:.4f} sd {sd:.4f} min {min(shuffled_scores):.4f} max {max(shuffled_scores):.4f}; "
        f"z {z:.2f}; rank {rank} of {n + 1}"
    ]
    return "\n".join(lines), {"agreement": real_agreement, "matches": real_matches, "clerk_n": clerk_n,
                               "shuffled_mean": mean, "shuffled_sd": sd, "z": z, "rank": rank, "n": n}


def key_rows_report(key_rows, real_pairs, dec, clk):
    """One row per key-file row: how often its aligned decoded letters matched (confirmed) or
    mismatched (contradicted) the clerk. Since decoded chars carry a key_row tag, walk the alignment
    pairs (which are always matches under lcs_align) for 'confirmed', and separately count every decoded
    character NOT in the matched set as 'contradicted' for its key_row (it lost to a different clerk
    letter or to no letter at all -- lcs_align only returns matched pairs, so unmatched decoded
    characters are exactly the complement)."""
    matched_dec_idx = {p[0] for p in real_pairs}
    confirmed = {}
    contradicted = {}
    for idx, (ch, tag) in enumerate(dec):
        bucket = confirmed if idx in matched_dec_idx else contradicted
        bucket[tag] = bucket.get(tag, 0) + 1
    rows = []
    for i in sorted(key_rows):
        r = key_rows[i]
        rows.append({
            "row": i, "sign": r["sign"][:40], "value": r["value"], "kind": r["kind"],
            "confirmed": confirmed.get(str(i), 0), "contradicted": contradicted.get(str(i), 0),
        })
    return rows


def write_key_rows_tsv(path, rows):
    with open(path, "w", encoding="utf-8") as f:
        f.write("row\tvalue\tkind\tconfirmed\tcontradicted\tsign\n")
        for r in rows:
            f.write(f"{r['row']}\t{r['value']}\t{r['kind']}\t{r['confirmed']}\t{r['contradicted']}\t{r['sign']}\n")


# ---------------------------------------------------------------- --label-diffs (MQS-WITNESS-LABELS)
CODE = "#"
LABELS = ("omission", "addition", "substitution", "name/code", "spelling-only")


def light(text):
    """Lower case, accents stripped, long s -> s, letters (and the code mark) only."""
    t = unicodedata.normalize("NFD", text.replace("ſ", "s").lower())
    return "".join(ch for ch in t if (ch.isalpha() and ord(ch) < 0x250) or ch == CODE)


def full(text):
    """light() plus the spelling-only equivalences (PX-BRODEC): j->i, v->u, y->i, doubled letters single."""
    t = light(text).translate(str.maketrans({"j": "i", "v": "u", "y": "i"}))
    out = []
    for ch in t:
        if not out or out[-1] != ch:
            out.append(ch)
    return "".join(out)


def load_abbrev(path):
    """TSV 'abbrev<TAB>expansion' (header optional, '#' lines skipped); keys compared after light()."""
    table = {}
    if not path:
        return table
    with open(path, encoding="utf-8") as f:
        for ln in f:
            if not ln.strip() or ln.startswith("#"):
                continue
            cols = ln.rstrip("\n").split("\t")
            if len(cols) >= 2 and cols[0] != "abbrev":
                table[light(cols[0])] = cols[1]
                table["raw:" + cols[0]] = cols[1]
    return table


def load_names(path):
    if not path:
        return set()
    with open(path, encoding="utf-8") as f:
        return {full(ln.strip()) for ln in f if ln.strip() and not ln.startswith("#")}


def decode_chars(text):
    """A decode_key.py reading (or any text) -> list of light chars, unread signs/codes as CODE."""
    out = []
    for ln in text.splitlines():
        if not ln.strip() or ln.startswith("#"):
            continue
        if "\t" in ln:
            ln = ln.split("\t", 1)[1]
        for tok in ln.split():
            if tok == "[/]" or (tok.startswith("<") and tok.endswith(">")):
                continue
            if tok.startswith("[") or "?" in tok or "_" in tok or any(c.isdigit() for c in tok):
                out.append(CODE)
                continue
            out.extend(light(tok))
    return out


WORD_RE = re.compile(r"[^\W\d_]+|\d+|[#\[\]?_]+", re.UNICODE)


def witness_words(text, abbrev=None):
    """Witness text -> list of (raw word, light form); apostrophes and punctuation split words."""
    abbrev = abbrev or {}
    for k in sorted((k for k in abbrev if k.startswith("raw:")), key=len, reverse=True):
        text = text.replace(k[4:], " " + abbrev[k] + " ")
    out = []
    for m in WORD_RE.finditer(text):
        raw = m.group(0)
        if any(c.isdigit() for c in raw) or set(raw) <= set("#[]?_"):
            out.append((raw, CODE))
            continue
        lt = light(raw)
        if lt in abbrev:
            lt = light(abbrev[lt])
        if lt:
            out.append((raw, lt))
    return out


def edit_align(a, b):
    """Global edit-distance alignment (match 0, substitution 1, gap 1) of char lists a (decode) and
    b (witness). Returns ops [(i or None, j or None)] in order. Ties prefer diagonal, then a witness gap
    (decode lacks), then a decode insertion."""
    n, m = len(a), len(b)
    prev = list(range(m + 1))
    back = [bytearray(m + 1) for _ in range(n + 1)]  # 0 diag, 1 up (decode insert), 2 left (witness del)
    for j in range(1, m + 1):
        back[0][j] = 2
    for i in range(1, n + 1):
        cur = [i] + [0] * m
        ai = a[i - 1]
        bk = back[i]
        bk[0] = 1
        for j in range(1, m + 1):
            d = prev[j - 1] + (0 if ai == b[j - 1] else 1)
            left = cur[j - 1] + 1
            up = prev[j] + 1
            if d <= left and d <= up:
                cur[j] = d
            elif left <= up:
                cur[j] = left
                bk[j] = 2
            else:
                cur[j] = up
                bk[j] = 1
        prev = cur
    ops = []
    i, j = n, m
    while i > 0 or j > 0:
        mv = back[i][j]
        if mv == 0:
            ops.append((i - 1, j - 1))
            i -= 1
            j -= 1
        elif mv == 1:
            ops.append((i - 1, None))
            i -= 1
        else:
            ops.append((None, j - 1))
            j -= 1
    ops.reverse()
    return ops


def label_diffs(dec, words, names=None, min_addition=2):
    """dec: decode char list (light, CODE marks). words: witness_words() output.
    Returns (items, word_spans): items is a list of dicts {kind: 'word'|'gap', w (word index; a gap
    follows word w, w=-1 before the first), label, decode, witness}; word_spans[w] = (lo, hi) decode
    index range aligned to word w, or None."""
    names = names or set()
    wit, wid = [], []
    for k, (_, lt) in enumerate(words):
        for ch in lt:
            wit.append(ch)
            wid.append(k)
    ops = edit_align(dec, wit)
    span = [None] * len(words)
    gaps = {}
    last_w = -1
    for idx, (i, j) in enumerate(ops):
        if j is not None:
            last_w = wid[j]
            if i is not None:
                lo, hi = span[last_w] or (i, i)
                span[last_w] = (min(lo, i), max(hi, i))
            continue
        # decode insertion: inside a word if the witness chars on both sides belong to the same word
        nxt = next((jj for (_, jj) in ops[idx + 1:] if jj is not None), None)
        if nxt is not None and last_w >= 0 and wid[nxt] == last_w:
            lo, hi = span[last_w] or (i, i)
            span[last_w] = (min(lo, i), max(hi, i))
        else:
            gaps.setdefault(last_w, []).append(i)
    items = []
    gap_before = gaps.get(-1)
    if gap_before:
        items.append(_gap_item(-1, gap_before, dec, min_addition))
    for k, (raw, lt) in enumerate(words):
        sp = span[k]
        got = "".join(dec[sp[0]:sp[1] + 1]) if sp else ""
        if not got:
            lab = "omission"
        elif CODE in got or lt == CODE:
            lab = "equal" if got == lt else "name/code"
        elif got == lt:
            lab = "equal"
        elif full(got) == full(lt):
            lab = "spelling-only"
        elif full(lt) in names:
            lab = "name/code"
        else:
            lab = "substitution"
        items.append({"kind": "word", "w": k, "label": lab, "decode": got, "witness": raw})
        if k in gaps:
            items.append(_gap_item(k, gaps[k], dec, min_addition))
    return [it for it in items if it is not None], span


def _gap_item(w, idxs, dec, min_addition):
    got = "".join(dec[i] for i in idxs)
    if CODE in got:
        lab = "name/code"
    elif len(got) >= min_addition:
        lab = "addition"
    else:
        lab = "gap-noise"
    return {"kind": "gap", "w": w, "label": lab, "decode": got, "witness": ""}


def write_labels_tsv(path, items):
    with open(path, "w", encoding="utf-8") as f:
        f.write("n\tkind\tafter_word\tlabel\tdecode\twitness\n")
        for n, it in enumerate(items, 1):
            f.write(f"{n}\t{it['kind']}\t{it['w']}\t{it['label']}\t{it['decode']}\t{it['witness']}\n")


def label_counts(items):
    c = {}
    for it in items:
        c[it["label"]] = c.get(it["label"], 0) + 1
    return c


# planted-difference control ------------------------------------------------------------------------
NORM_LETTERS = set("ijyuv")


def _minimal_sub(word, rng):
    """One letter changed outside the normalisation pairs, no double created or removed."""
    pos = [p for p, ch in enumerate(word) if ch not in NORM_LETTERS]
    rng.shuffle(pos)
    for p in pos:
        for new in rng.sample("abcdefghlmnopqrst", 17):
            if new == word[p] or new in NORM_LETTERS:
                continue
            if (p > 0 and word[p - 1] in (new, word[p])) or (p + 1 < len(word) and word[p + 1] in (new, word[p])):
                continue
            cand = word[:p] + new + word[p + 1:]
            if full(cand) != full(word):
                return cand
    return None


def _spelling_variant(word, rng):
    """A change full() undoes but light() sees: i->j, u->v, i->y, a doubled consonant, or a double undone."""
    opts = []
    for p, ch in enumerate(word):
        if ch == "i":
            opts += [word[:p] + "j" + word[p + 1:], word[:p] + "y" + word[p + 1:]]
        if ch == "u":
            opts.append(word[:p] + "v" + word[p + 1:])
        if ch in "bcdfglmnprst" and (p == 0 or word[p - 1] != ch) and (p + 1 == len(word) or word[p + 1] != ch):
            opts.append(word[:p + 1] + ch + word[p + 1:])
        if p > 0 and word[p - 1] == ch:
            opts.append(word[:p] + word[p + 1:])
    opts = [o for o in opts if o != word and full(o) == full(word)]
    return rng.choice(opts) if opts else None


def plant_once(dec, words, rng, per_class, names=None, min_addition=2, spacing=2):
    """Plant per_class differences of each label at isolated witness words labelled equal in the
    unplanted run. Returns (planted decode, sites [(w, truth, subkind)])."""
    items, span = label_diffs(dec, words, names, min_addition)
    eq = [it["w"] for it in items if it["kind"] == "word" and it["label"] == "equal" and len(words[it["w"]][1]) >= 3]
    rng.shuffle(eq)
    chosen = []
    for w in eq:
        if all(abs(w - c) > spacing for c in chosen):
            chosen.append(w)
    vocab = sorted({lt for _, lt in words if len(lt) >= 3 and lt != CODE})
    classes = []
    for lab in LABELS:
        classes += [lab] * per_class
    rng.shuffle(classes)
    sites = []
    edits = []  # (lo, hi, replacement chars) with hi exclusive; insertion when lo == hi
    for w, lab in zip(chosen, classes):
        lo, hi = span[w]
        word = "".join(dec[lo:hi + 1])
        sub = ""
        if lab == "omission":
            rep = []
        elif lab == "name/code":
            rep = [CODE]
        elif lab == "addition":
            # insert after the word; make sure the inserted word cannot merge with its neighbours by letters
            nxt = words[w + 1][1] if w + 1 < len(words) else ""
            pool = [v for v in vocab if v != word and v != nxt]
            ins = rng.choice(pool)
            edits.append((hi + 1, hi + 1, list(ins)))
            sites.append((w, lab, "insert"))
            continue
        elif lab == "spelling-only":
            v = _spelling_variant(word, rng)
            if v is None:
                continue
            rep = list(v)
        else:
            if rng.random() < 0.5:
                v = _minimal_sub(word, rng)
                sub = "one-letter"
            else:
                pool = [x for x in vocab if abs(len(x) - len(word)) <= 1 and full(x) != full(word)]
                v = rng.choice(pool) if pool else None
                sub = "whole-word"
            if v is None:
                continue
            rep = list(v)
        edits.append((lo, hi + 1, rep))
        sites.append((w, lab, sub))
    out = list(dec)
    for lo, hi, rep in sorted(edits, key=lambda e: -e[0]):
        out[lo:hi] = rep
    return out, sites


def predicted_at(items, w, truth):
    word = {it["w"]: it["label"] for it in items if it["kind"] == "word"}
    gaps = {it["w"]: it["label"] for it in items if it["kind"] == "gap"}
    if truth == "addition":
        if gaps.get(w) == "addition":
            return "addition"
        for k in (w, w + 1):
            if word.get(k, "equal") != "equal":
                return word[k]
        return gaps.get(w, "equal")
    return word.get(w, "equal")


def plant_control(dec, words, seeds, per_class, shuffles, seed0=1, names=None, min_addition=2):
    rows = []
    for s in range(seeds):
        rng = random.Random(seed0 + s)
        pdec, sites = plant_once(dec, words, rng, per_class, names, min_addition)
        items, _ = label_diffs(pdec, words, names, min_addition)
        for w, truth, sub in sites:
            rows.append({"seed": seed0 + s, "w": w, "truth": truth, "sub": sub,
                         "pred": predicted_at(items, w, truth)})
    acc = sum(r["pred"] == r["truth"] for r in rows) / len(rows) if rows else 0.0
    per = {}
    for lab in LABELS:
        rr = [r for r in rows if r["truth"] == lab]
        per[lab] = (sum(r["pred"] == lab for r in rr), len(rr))
    one = [r for r in rows if r["sub"] == "one-letter"]
    hidden = sum(r["pred"] == "spelling-only" for r in one)
    rng = random.Random(seed0 + 9999)
    preds = [r["pred"] for r in rows]
    null = []
    for _ in range(shuffles):
        p = preds[:]
        rng.shuffle(p)
        null.append(sum(a == r["truth"] for a, r in zip(p, rows)) / len(rows) if rows else 0.0)
    null.sort()
    p95 = null[int(0.95 * (len(null) - 1))] if null else 0.0
    mean = sum(null) / len(null) if null else 0.0
    return {"n": len(rows), "accuracy": acc, "per_class": per, "one_letter": (len(one) - hidden, len(one)),
            "one_letter_hidden": hidden, "null_mean": mean, "null_p95": p95, "rows": rows}


def format_control(label, r):
    per = "; ".join(f"{k} {a}/{n}" for k, (a, n) in r["per_class"].items())
    return (f"{label}: planted {r['n']} sites, label accuracy {r['accuracy']:.3f} vs label-shuffled null mean "
            f"{r['null_mean']:.3f} p95 {r['null_p95']:.3f}; per class {per}; one-letter substitutions labelled "
            f"substitution {r['one_letter'][0]}/{r['one_letter'][1]}, hidden as spelling-only {r['one_letter_hidden']}")


# 'sent in cipher' criteria scan -------------------------------------------------------------------------
CRITERIA_DEFAULT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "data", "sent_in_cipher_criteria.tsv")


def load_criteria(path, lang):
    rows = _read_tsv(path, ["id", "criterion", "lang", "pattern"])
    return [r for r in rows if r["lang"] in (lang, "any")]


def split_sentences(text):
    flat = re.sub(r"\s+", " ", text)
    return [s.strip() for s in re.split(r"(?<=[.;:!?])\s+", flat) if s.strip()]


def criteria_scan(text, criteria):
    """Returns [(sentence index, sentence, [criterion ids])] for sentences matching any pattern.
    Patterns are matched against the accent-stripped lower-case sentence."""
    out = []
    comp = [(c["id"], re.compile(c["pattern"])) for c in criteria]
    for k, s in enumerate(split_sentences(text)):
        flat = unicodedata.normalize("NFD", s.lower().replace("ſ", "s"))
        flat = "".join(ch for ch in flat if not unicodedata.combining(ch))
        hits = [cid for cid, rx in comp if rx.search(flat)]
        if hits:
            out.append((k, s, hits))
    return out


def main_label(args):
    try:
        abbrev = load_abbrev(args.abbrev)
        names = load_names(args.names)
        with open(args.witness, encoding="utf-8") as f:
            words = witness_words(f.read(), abbrev)
        if args.plant_base == "witness":
            dec = [ch for _, lt in words for ch in lt]
        else:
            if not args.decode:
                raise ValueError("--decode is required unless --plant-base witness")
            with open(args.decode, encoding="utf-8") as f:
                dec = decode_chars(f.read())
    except (ValueError, OSError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    if not words:
        print("error: no witness words", file=sys.stderr)
        return 2
    if args.plant_control:
        r = plant_control(dec, words, args.plant_control, args.plant_per_class, args.shuffles, args.seed,
                          names, args.min_addition)
        print(format_control(f"plant-control (base {args.plant_base}, {args.plant_control} seeds)", r))
        if args.labels_out:
            with open(args.labels_out, "w", encoding="utf-8") as f:
                f.write("seed\tword\ttruth\tsubkind\tpredicted\n")
                for row in r["rows"]:
                    f.write(f"{row['seed']}\t{row['w']}\t{row['truth']}\t{row['sub']}\t{row['pred']}\n")
        return 0
    items, _ = label_diffs(dec, words, names, args.min_addition)
    c = label_counts(items)
    nw = len(words)
    print(f"label-diffs: {nw} witness words, {len(dec)} decode letters; "
          + ", ".join(f"{k} {c.get(k, 0)}" for k in ("equal",) + LABELS + ("gap-noise",)))
    if args.labels_out:
        write_labels_tsv(args.labels_out, items)
        print(f"wrote {args.labels_out} ({len(items)} rows)")
    return 0


def main_criteria(args):
    try:
        crit = load_criteria(args.criteria, args.lang)
        with open(args.criteria_scan, encoding="utf-8") as f:
            text = f.read()
    except (ValueError, OSError, re.error) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2
    hits = criteria_scan(text, crit)
    print(f"criteria-scan: {len(split_sentences(text))} sentences, {len(hits)} flagged (a LEAD that the passage "
          f"may have been sent in cipher, never a verdict; lang {args.lang}, {len(crit)} criteria rows)")
    for k, s, ids in hits:
        print(f"{k}\t{','.join(ids)}\t{s[:200]}")
    return 0


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--key")
    ap.add_argument("--signs")
    ap.add_argument("--plain")
    ap.add_argument("--shuffles", type=int, default=20)
    ap.add_argument("--seed", type=int, default=1)
    ap.add_argument("--sample-lines", default=None, help="comma-separated line ids for the blind-check subset")
    ap.add_argument("--key-rows-out", default=None)
    ap.add_argument("--label-diffs", action="store_true", help="label decode-vs-witness differences")
    ap.add_argument("--decode", help="--label-diffs: the decode (a decode_key.py reading or plain text)")
    ap.add_argument("--witness", help="--label-diffs: the printed or clear witness text")
    ap.add_argument("--abbrev", help="--label-diffs: TSV abbrev<TAB>expansion applied to witness words")
    ap.add_argument("--names", help="--label-diffs: one name per line; a differing rendering is name/code")
    ap.add_argument("--min-addition", type=int, default=2)
    ap.add_argument("--labels-out", help="--label-diffs: per-item TSV (or per-site TSV under --plant-control)")
    ap.add_argument("--plant-control", type=int, default=0, metavar="SEEDS")
    ap.add_argument("--plant-per-class", type=int, default=4)
    ap.add_argument("--plant-base", choices=["decode", "witness"], default="decode")
    ap.add_argument("--criteria-scan", metavar="TEXT", help="flag sentences meeting the sent-in-cipher criteria")
    ap.add_argument("--criteria", default=CRITERIA_DEFAULT)
    ap.add_argument("--lang", default="fr")
    args = ap.parse_args(argv)
    if args.criteria_scan:
        return main_criteria(args)
    if args.label_diffs:
        if not args.witness:
            print("error: --label-diffs needs --witness", file=sys.stderr)
            return 2
        return main_label(args)
    if not (args.key and args.signs and args.plain):
        print("error: --key, --signs and --plain are required (or use --label-diffs / --criteria-scan)",
              file=sys.stderr)
        return 2

    try:
        key_rows, letter_idxs = load_key(args.key)
        signs_raw = _read_tsv(args.signs, ["line", "pos", "key_row"])
        plain_rows = load_plain(args.plain)
        # validate every key_row up front so a malformed row is caught before any scoring
        for s in signs_raw:
            key_row_value(key_rows, s["key_row"])
    except (ValueError, OSError, KeyError) as e:
        print(f"error: {e}", file=sys.stderr)
        return 2

    real_agreement, real_matches, clerk_n, shuffled, real_pairs, real_signs = control(
        signs_raw, plain_rows, key_rows, letter_idxs, args.shuffles, args.seed)
    text, stats = summarize("full passage", real_agreement, real_matches, clerk_n, shuffled)
    print(text)

    if args.key_rows_out:
        dec = decoded_stream(real_signs)
        clk = clerk_stream(plain_rows)
        rows = key_rows_report(key_rows, real_pairs, dec, clk)
        write_key_rows_tsv(args.key_rows_out, rows)
        print(f"wrote {args.key_rows_out} ({len(rows)} key rows)")

    if args.sample_lines:
        lines = set(args.sample_lines.split(","))
        s_agr, s_matches, s_n, s_shuffled, _, _ = control(
            signs_raw, plain_rows, key_rows, letter_idxs, args.shuffles, args.seed + 1000, lines=lines)
        text2, _ = summarize("blind-check sample", s_agr, s_matches, s_n, s_shuffled)
        print(text2)

    return 0


if __name__ == "__main__":
    sys.exit(main())

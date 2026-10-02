#!/usr/bin/env python3
"""F8-F11 against the Letter-Book private letter CCXL (31 July 1583), 2 Oct 2026 (NEXT-BOW).

Question (NOTES "Remaining gaps", gap 1): can the four f.299 fragments F8, F9, F10, F11 be placed, in their
transcription order, on CCXL's text (Surtees Soc. vol.14 pp.530-534, corpus/) so that every sign takes one value
across all four, with F10 read as the code number 223 (02=2, 03=3 as cipher digit-signs) -- and does that fix
sign 03 in F11 too?

Placement rule. A fragment matches a span of CCXL words when, word by word, every sign's value is consistent
within the fragment and across fragments already placed (letters i=j, u=v; digits are their own class; a sign
with a letter value never takes a digit and vice versa). Clear words between the cipher words of one fragment
are allowed only where Boyd's calendar (CSP Scotland vi no.584, pp.566-568) puts two asterisks on one line:
F9 'by * late submission at *'. F11's unread pair 03 25 may be a code number followed by a clear 'and'
(Tomokiyo did not transcribe the clear 'and' of F11 if it was written out; he did transcribe F4's 'and'
abbreviation as sign 27, which he later withdrew, NOTES "Specialist reply").

Control. The placement is order-dependent: with the fragments taken in the transcription order (F8 F9 F10 F11)
and the text order of CCXL, a monotone placement exists or not. The control is the other 23 orders of the four
fragments: the share of the 24 orders that also admit a monotone placement is the chance level; with 4 fragments
the floor is 1/24 ~ 0.04 and is reported as such (gap-1 line).

  python3 align_ccxl.py        prints the placements per hypothesis and the 24-order count
"""
import itertools, os, re
HERE = os.path.dirname(os.path.abspath(__file__))
CORPUS = os.path.join(HERE, "corpus", "correspondenceof00bowerich_djvu.txt")

def norm(w):
    w = w.lower().replace("j", "i").replace("v", "u")
    return re.sub(r"[^a-z0-9]", "", w)

def ccxl_words():
    lines = open(CORPUS, encoding="utf-8", errors="replace").read().split("\n")
    # CCXL runs from its heading (line 29445, 1-based) to CCXLI's heading (29643)
    text = " ".join(lines[29444:29642])
    text = re.sub(r"BOWES CORRESPONDENCE\. \d+|\d+ BOWES CORRESPONDENCE\.|2 m 2", " ", text)
    text = text.replace("- ", "")  # hyphenated line breaks in the OCR
    return [norm(w) for w in text.split() if norm(w)]

def load_frags():
    frags = [[t for t in l.strip().split(";") if t] for l in open(os.path.join(HERE, "ciphertext.txt"))
             if l.strip() and not l.startswith("#")]
    return {8: frags[7], 9: frags[8], 10: frags[9], 11: frags[10]}

def load_key():
    key = {}
    for l in open(os.path.join(HERE, "key.tsv")):
        if l.startswith("#") or l.startswith("sign\t") or not l.strip():
            continue
        s, v, g, _ = l.rstrip("\n").split("\t", 3)
        if v not in ("?", "-", "and") and g in ("S", "M", "C"):
            key[s] = v
    return key

DIGITS_ALLOWED = True

def try_words(frag_signs, words, key):
    """Match the sign sequence against the concatenation of the given words; return the extended key or None.
    A sign takes one value; a value may be shared by at most two signs (the key already has second signs for
    a, e, g); under the letters-only hypothesis no unread sign may take a digit."""
    target = "".join(words)
    if len(target) != len(frag_signs):
        return None
    k = dict(key)
    for s, ch in zip(frag_signs, target):
        if s in k:
            if k[s] != ch:
                return None
        else:
            if ch.isdigit() and not DIGITS_ALLOWED:
                return None
            if sum(1 for v in k.values() if v == ch) >= 2:
                return None
            k[s] = ch
    return k

def candidates(fid, signs, words, key, hyp):
    """All (start_word_index, end_word_index, newkey, rendering) placements of a fragment on the word list."""
    out = []
    n = len(words)
    if fid == 9:
        # two cipher words with clear words between: 'his' ... 'ruthen' shape = sign split 3 + 6 (Boyd's asterisks)
        for i in range(n):
            for j in range(i + 1, min(n, i + 8)):
                k = try_words(signs, [words[i], words[j]], key)
                if k is not None:
                    out.append((i, j, k, f"{words[i]} .. {words[j]}"))
        return out
    if fid == 8:
        # F8 = 15 + 'glencarn' (8 read signs): sign 15 is unread and stands outside the name, so it is left free
        # (a null, a word-start mark or a misread), and the 8 read signs must match the first 8 letters of a word
        # of 8 or 9 letters (Letter-Book 'Glencarne' has 9; the fragment has no sign for the final e)
        for i in range(n):
            w = words[i]
            if len(w) in (8, 9):
                k = try_words(signs[1:], [w[:8]], key)
                if k is not None:
                    out.append((i, i, k, f"[15] {w}"))
        return out
    for i in range(n):
        for L in (1, 2):
            if i + L > n:
                continue
            span = words[i:i + L]
            if fid == 11 and hyp == "digits" and L == 2:
                # code number + clear 'and' + 'him' : signs 03 25 [and] 17 16 12
                if i + 2 < n and words[i + 1] == "and" and words[i + 2] == "him" and len(words[i]) == 2:
                    k = try_words(signs, [words[i], "him"], key)
                    if k is not None:
                        out.append((i, i + 2, k, f"{words[i]} and him"))
                continue
            k = try_words(signs, span, key)
            if k is not None:
                out.append((i, i + L - 1, k, " ".join(span)))
    return out

def monotone(order, frags, words, key, hyp):
    """Depth-first: place fragments in the given order at increasing text positions with one shared key."""
    best = []
    def rec(idx, pos, k, placed):
        nonlocal best
        if idx == len(order):
            best.append(list(placed)); return
        fid = order[idx]
        for (i, j, k2, r) in candidates(fid, frags[fid], words, k, hyp):
            if i <= pos:
                continue
            rec(idx + 1, j, k2, placed + [(fid, i, j, r)])
    rec(0, -1, key, [])
    return best

def main():
    words = ccxl_words()
    frags = load_frags()
    key = load_key()
    print(f"CCXL: {len(words)} words; key: {len(key)} signs with letter values")
    global DIGITS_ALLOWED
    for hyp in ("digits", "letters"):
        # key.tsv now carries 02 = 2, 03 = 3 (M, 2 Oct 2026); drop them (and 25) so the letters-only hypothesis
        # really leaves them free (VERIFY-BOWES-584, 2 Oct 2026: without this F10 placed as 223 under "letters")
        k = {s: v for s, v in key.items() if s not in ("02", "03", "25")}
        DIGITS_ALLOWED = hyp == "digits"
        if hyp == "digits":
            k["02"], k["03"] = "2", "3"   # F10 = 223 at Boyd's 'In this *'
        print(f"\n== hypothesis {hyp}: " + ("02=2, 03=3 (F10 = 223), 25 free" if hyp == "digits" else "02, 03, 25 free letters, no digits (T3's 'to him' shape)"))
        for fid in (8, 9, 10, 11):
            c = candidates(fid, frags[fid], words, k, hyp)
            seen = sorted(set(r for (_, _, _, r) in c))
            print(f"  F{fid} ({len(frags[fid])} signs) placements: {len(c)} -> {seen[:12]}{' ...' if len(seen) > 12 else ''}")
        n_ok, true_sol = 0, None
        for order in itertools.permutations((8, 9, 10, 11)):
            sols = monotone(order, frags, words, k, hyp)
            if sols:
                n_ok += 1
            if order == (8, 9, 10, 11):
                true_sol = sols
        print(f"  transcription order F8 F9 F10 F11: {len(true_sol)} monotone placement(s)")
        for s in true_sol[:6]:
            print("    " + " | ".join(f"F{fid}@{i}-{j} {r}" for fid, i, j, r in s))
        print(f"  control: {n_ok} of 24 fragment orders admit a monotone placement (floor 1/24 = 0.042)")

if __name__ == "__main__":
    main()

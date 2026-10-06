#!/usr/bin/env python3
"""blockc_test.py -- rubin-1953 Block C as Morse-like or binary, with shuffle null and matched English control.

Pre-registered in ../blockc/PREREG-blockc-morse-binary.md (R9-RUBIN4, 6 Oct 2026). Offline; reads ciphertext.txt and the
judge's en corpus. Writes blockc/results.tsv and blockc/target_decodes.tsv.
Usage: python3 scripts/blockc_test.py [--shuffles 3000] [--controls 200] [--check]
--check: recompute and exit 1 if the committed results.tsv differs.
"""
import argparse, random, re, sys
from pathlib import Path
HERE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(HERE.parent.parent / "tools"))
import judge_plaintext as J

MORSE = {'.-':'A','-...':'B','-.-.':'C','-..':'D','.':'E','..-.':'F','--.':'G','....':'H','..':'I','.---':'J','-.-':'K',
 '.-..':'L','--':'M','-.':'N','---':'O','.--.':'P','--.-':'Q','.-.':'R','...':'S','-':'T','..-':'U','...-':'V','.--':'W',
 '-..-':'X','-.--':'Y','--..':'Z'}
for d, c in zip('0123456789', ['-----','.----','..---','...--','....-','.....','-....','--...','---..','----.']):
    MORSE[c] = d
for c in ['.-.-.-','--..--','..--..','.----.','-.-.--','-..-.','-.--.','-.--.-','.-...','---...','-.-.-.','-...-',
          '.-.-.','-....-','..--.-','.-..-.','.--.-.']:
    MORSE[c] = '#'
ITA2 = {0:None,1:'E',2:' ',3:'A',4:' ',5:'S',6:'I',7:'U',8:' ',9:'D',10:'R',11:'J',12:'N',13:'F',14:'C',15:'K',16:'T',17:'Z',
        18:'L',19:'W',20:'H',21:'Y',22:'P',23:'Q',24:'O',25:'B',26:'G',27:None,28:'M',29:'X',30:'V',31:None}
BAC24 = "ABCDEFGHIKLMNOPQRSTUWXYZ"
A26 = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
PEN = -3.0


def block_c():
    L = [l.strip() for l in open(HERE / "ciphertext.txt") if re.fullmatch(r"[01.x]+", l.strip())]
    assert [len(x) for x in L] == [60, 37, 39], L
    return "x".join(L)  # line breaks act as separators


def flip(b, pol):
    return b if pol == 0 else b.translate(str.maketrans("01", "10"))


def dec_morse(s, pol):
    out = []
    for t in re.findall("[01]+", s):
        m = flip(t, pol).replace("0", ".").replace("1", "-")
        out.append(MORSE.get(m))  # None = invalid
    return out


def dec_group(s, pol):
    out = []
    for t in re.findall("[01]+", s):
        v = int(flip(t, pol), 2)
        out.append(A26[v - 1] if 1 <= v <= 26 else None)
    return out


def bits(s, pol):
    return flip(re.sub("[^01]", "", s), pol)


def dec_chunks(s, pol, off, w, table):
    b = bits(s, pol)[off:]
    return [table(b[i:i + w]) for i in range(0, len(b) - w + 1, w)]


def t_bac26(c):
    v = int(c, 2); return A26[v] if v < 26 else None
def t_bac24(c):
    v = int(c, 2); return BAC24[v] if v < 24 else None
def t_ita(c, lsb):
    v = int(c[::-1] if lsb else c, 2); return ITA2[v]
def t_ascii(c):
    v = int(c, 2); ch = chr(v)
    return ch.upper() if ch.isascii() and ch.isalpha() else (' ' if v == 32 else None)


def encodings():
    E = []
    for pol in (0, 1):
        E.append((f"M p{pol}", "tok", lambda s, p=pol: dec_morse(s, p)))
        E.append((f"G p{pol}", "tok", lambda s, p=pol: dec_group(s, p)))
    for pol in (0, 1):
        for off in range(5):
            E.append((f"BAC26 p{pol} o{off}", "bit5", lambda s, p=pol, o=off: dec_chunks(s, p, o, 5, t_bac26)))
            E.append((f"BAC24 p{pol} o{off}", "bit5", lambda s, p=pol, o=off: dec_chunks(s, p, o, 5, t_bac24)))
            for lsb in (0, 1):
                E.append((f"ITA2 p{pol} o{off} {'lsb' if lsb else 'msb'}", "bit5",
                          lambda s, p=pol, o=off, l=lsb: dec_chunks(s, p, o, 5, lambda c: t_ita(c, l))))
        for off in range(7):
            E.append((f"A7 p{pol} o{off}", "bit7", lambda s, p=pol, o=off: dec_chunks(s, p, o, 7, t_ascii)))
        for off in range(8):
            E.append((f"A8 p{pol} o{off}", "bit8", lambda s, p=pol, o=off: dec_chunks(s, p, o, 8, t_ascii)))
    return E


def T(model, toks):
    letters = "".join(t for t in toks if t and t.isalpha())
    ninv = sum(1 for t in toks if t is None)
    n = len(letters) + ninv
    if n == 0:
        return PEN
    return (len(letters) * model.score(letters) + ninv * PEN) / n


# ---- encoders for the matched control (English -> same design) ----
RM = {v: k for k, v in MORSE.items() if v.isalpha()}


def enc_tok(words, name, ntok):
    pol = int(name.split()[1][1])
    parts = []
    for w in words:
        if name.startswith("M"):
            g = [RM[c].replace(".", "0").replace("-", "1") for c in w]
        else:
            g = [bin(A26.index(c) + 1)[2:] for c in w]
        parts.append(".".join(flip(x, pol) for x in g))
    s = "x".join(parts)
    keep, n = [], 0
    for m in re.finditer("[01]+|[.x]+", s):
        if m.group()[0] in "01":
            n += 1
            if n > ntok:
                break
        keep.append(m.group())
    return "".join(keep)


def enc_bits(words, name, nbits):
    f = name.split(); kind, pol, off = f[0], int(f[1][1]), int(f[2][1])
    txt = "".join(words)
    if kind == "BAC26":
        b = "".join(format(A26.index(c), "05b") for c in txt)
    elif kind == "BAC24":
        b = "".join(format(BAC24.index({'J': 'I', 'V': 'U'}.get(c, c)), "05b") for c in txt)
    elif kind == "ITA2":
        lsb = f[3] == "lsb"; inv = {v: k for k, v in ITA2.items() if v and v.isalpha()}
        b = "".join(format(inv[c], "05b")[::-1] if lsb else format(inv[c], "05b") for c in txt)
    else:
        w = 7 if kind == "A7" else 8
        b = "".join(format(ord(c.lower()), f"0{w}b") for c in txt)
    b = "1" * off + b  # offset: decoder skips `off` leading bits
    return flip(b[:nbits], pol)


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--shuffles", type=int, default=3000)
    ap.add_argument("--controls", type=int, default=200)
    ap.add_argument("--check", action="store_true")
    a = ap.parse_args()
    model = J.NgramModel([J.read_corpus(p) for p in J.LANG_CORPORA["en"]])
    raw_words = re.findall(r"[A-Za-z]+", " ".join(J.read_corpus(p) for p in J.LANG_CORPORA["en"]))
    raw_words = [w.upper() for w in raw_words]
    s = block_c(); ntok = len(re.findall("[01]+", s)); nbits = len(bits(s, 0))
    E = encodings(); k = len(E); alpha = 0.05 / k
    rs = random.Random(1); shuf = []
    for _ in range(a.shuffles):
        c = list(s); rs.shuffle(c); shuf.append("".join(c))
    rc = random.Random(2); ctl_starts = [rc.randrange(0, len(raw_words) - 200) for _ in range(a.controls)]
    rows, decs = [], []
    for name, kind, dec in E:
        tt = T(model, dec(s))
        sn = sorted(T(model, dec(x)) for x in shuf)
        p = (1 + sum(1 for v in sn if v >= tt)) / (len(sn) + 1)
        theta = J.pct(sn, 1 - alpha)
        cs = []
        for j in ctl_starts:
            w = raw_words[j:j + 120]
            cstr = enc_tok(w, name, ntok) if kind == "tok" else enc_bits(w, name, nbits)
            cs.append(T(model, dec(cstr)))
        cs.sort(); cp05 = J.pct(cs, 0.05)
        power = sum(1 for v in cs if v > theta) / len(cs)
        shuf_eng = sum(1 for v in sn if v >= cp05) / len(sn)
        test = power >= 0.8
        gate = test and p < alpha and tt >= cp05 and shuf_eng <= 0.05
        verdict = "PASS" if gate else ("FAIL" if test else "non-test")
        rows.append([name, f"{tt:.3f}", f"{p:.4f}", f"{theta:.3f}", f"{J.pct(sn, .5):.3f}", f"{J.pct(cs, .5):.3f}",
                     f"{cp05:.3f}", f"{power:.3f}", f"{shuf_eng:.4f}", verdict])
        decs.append([name, "".join(t if t else "?" for t in dec(s))])
    hdr = ["encoding", "T_target", "p_shuffle", "theta(1-0.05/k)", "shuffle_median", "control_median", "control_p05",
           "control_power", "shuffle_frac>=ctl_p05", "verdict"]
    out = "\t".join(hdr) + "\n" + "".join("\t".join(r) + "\n" for r in rows)
    od = HERE / "blockc"
    if a.check:
        ok = (od / "results.tsv").read_text() == out
        print("check:", "OK" if ok else "STALE"); sys.exit(0 if ok else 1)
    (od / "results.tsv").write_text(out)
    (od / "target_decodes.tsv").write_text("encoding\tdecode\n" + "".join("\t".join(d) + "\n" for d in decs))
    print(f"k={k} alpha={alpha:.5f} ntok={ntok} nbits={nbits}")
    print(out)


if __name__ == "__main__":
    main()

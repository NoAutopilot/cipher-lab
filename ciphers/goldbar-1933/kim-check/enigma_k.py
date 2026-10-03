"""Swiss-K Enigma, written from scratch for CHECK-GOLDBAR (3 Oct 2026) from the factory wiring printed in Milton Kim's
'How to Solve Chinese Gold Bar Ciphers' (github.com/milton6310/cgbCiphers, docs/, p.4) and cryptomuseum.com's wiring table.
No code from Kim's repository (no licence) or from pyEnigma is used. Conventions (rotor order, entry wheel, stepping) are
selected by `--find`, which tries every combination until Kim's own published line-4 decode is reproduced."""
import itertools, sys
A = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
ETW = "QWERTZUIOASDFGHJKPYXCVBNML"
ROT = {"I": ("LPGSZMHAEOQKVXRFYBUTNICJDW", "G"), "II": ("SLVGBTFXJQOHEWIRZYAMKPCNDU", "M"),
       "III": ("CJGDPSHKTURAWZXFMYNQOBVLIE", "V")}
UKW = "IMETCGFRAYSQBZXWLHKDVUPOJN"
NOTCH_SETS = {"kim": {"I": "G", "II": "M", "III": "V"}, "cm": {"I": "Y", "II": "E", "III": "N"}}


def inv(w):
    r = [0] * 26
    for i, ch in enumerate(w):
        r[A.index(ch)] = i
    return r


class Enigma:
    def __init__(self, order=("I", "II", "III"), key="AAA", ring="AAA", etw=True, etw_inv=False, notches="kim",
                 step_mode="std"):
        self.w = [[A.index(c) for c in ROT[n][0]] for n in order]       # left, middle, right
        self.wi = [inv(ROT[n][0]) for n in order]
        self.notch = [A.index(NOTCH_SETS[notches][n]) for n in order]
        self.pos = [A.index(c) for c in key]
        self.ring = [A.index(c) for c in ring]
        self.ukw = [A.index(c) for c in UKW]
        e = [A.index(c) for c in ETW]
        if not etw:
            e = list(range(26))
        self.e, self.ei = (inv(ETW), e) if etw_inv and etw else (e, inv(ETW) if etw else list(range(26)))
        self.step_mode = step_mode

    def step(self):
        p, n = self.pos, self.notch
        if self.step_mode == "std":
            if p[1] == n[1]:
                p[0] = (p[0] + 1) % 26; p[1] = (p[1] + 1) % 26
            elif p[2] == n[2]:
                p[1] = (p[1] + 1) % 26
            p[2] = (p[2] + 1) % 26
        else:  # gear-like, no double step
            if p[2] == n[2]:
                if p[1] == n[1]:
                    p[0] = (p[0] + 1) % 26
                p[1] = (p[1] + 1) % 26
            p[2] = (p[2] + 1) % 26

    def through(self, i, c, inverse):
        s = (self.pos[i] - self.ring[i]) % 26
        t = (self.wi if inverse else self.w)[i][(c + s) % 26]
        return (t - s) % 26

    def letter(self, ch):
        self.step()
        c = self.e[A.index(ch)]
        for i in (2, 1, 0):
            c = self.through(i, c, False)
        c = self.ukw[c]
        for i in (0, 1, 2):
            c = self.through(i, c, True)
        return A[self.ei[c]]

    def run(self, s):
        return "".join(self.letter(ch) for ch in s)


CONFIGS = [dict(order=o, etw=e, etw_inv=ei, notches=nt, step_mode=sm)
           for o in itertools.permutations(("I", "II", "III")) for e in (True, False) for ei in (False, True)
           for nt in ("kim", "cm") for sm in ("std", "gear") if not (ei and not e)]

if __name__ == "__main__":
    if "--find" in sys.argv:
        ct, want = "FEWGDRHDDEEUMFFTEEMJXZR", "OUSTGOVPBANKIZMUBMHUVOG"
        for cfg in CONFIGS:
            for key, rev in (("JQE", False), ("EQJ", True)):
                got = Enigma(key=key, ring="AAA", **cfg).run(ct)
                if got == want:
                    print("MATCH", cfg, key)


KIM_CFG = dict(order=("III", "II", "I"), etw=False, etw_inv=False, notches="kim", step_mode="std")


def kim(ct, key, ring):
    """Decode in Kim's notation: KEY and RING are written rotor I, II, III (I the fast rotor), and the fast rotor's KEY
    letter is the position at which the first letter is enciphered (no step before it). Found by `--find` plus a full
    key sweep on 3 Oct 2026: Kim's JQE/AAA on line 4 reproduces his OUSTGOVPBANKIZMUBMHUVOG exactly."""
    k = key[2] + key[1] + A[(A.index(key[0]) - 1) % 26]
    return Enigma(key=k, ring=ring[::-1], **KIM_CFG).run(ct)

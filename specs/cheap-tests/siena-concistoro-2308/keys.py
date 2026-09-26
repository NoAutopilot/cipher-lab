# Bourdeau's recovered key values for Siena nos. 25, 14, 4 (sign name -> Italian letter),
# from dbourdeau/cyphersolver siena1421/keys/{no25_key.txt,no04_key.txt}, siena1421/key14.txt
# (clone fc0c9e865d0fae67ca92d19750d2b09ab11972e0). Only the simple/short sign tokens from
# no04's evidence table are kept (its long descriptive names, e.g. "S (5-like)", cannot
# literally match another piece's own sign legend); matched case-insensitively.

key25 = {"+": "c", "3": "d", "9": "l", "B": "t", "F": "a", "G": "?", "H": "h", "HL": "s",
         "I": "i", "J": "n", "PH2": "g", "PHI": "u", "PI": "e", "Q": "p", "R": "u", "S": "o",
         "TH": "?", "U": "f", "X": "r", "X3": "q", "XB": "t", "Y": "m"}

key14 = {"2": "e", "6": "o", "7": "p", "7X": "z", "8": "n", "A": "a", "B": "c", "BO": "l",
         "C": "x", "CIRC": "d", "D": "n", "DIV": "f", "EQ": "a", "ETA": "a", "G": "r", "H": "h",
         "I": "e", "IB": "t", "L": "i", "LAMBDA": "a", "M": "l", "N": "n", "N?": "m", "O": "u",
         "OL": "m", "OP": "à", "OR": "d", "OSTEM": "i", "P": "o", "PAREN": ")", "PD": "i",
         "PLUS": "a", "Q": "a", "Q4": "i", "R": "a", "RR": "s", "T": "e", "TL": "a", "TR": "e",
         "V": "e", "VB": "r", "Y": "v", "Z": "q", "Z7": "b"}

key04 = {  # simple/short sign tokens only, from no04_key.txt's evidence table
    "A": "a", "3": "a", "4": "e", "T": "o", "q": "o", "C": "u", "c": "u", "2": "m", "a": "n",
    "N": "n", "M": "p", "H": "s", "y": "h", "L": "c", "9": "d", "h": "g", "k": "x", "x": "e",
}

KEYS = {"no25": key25, "no14": key14, "no04": key04}

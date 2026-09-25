"""
Real credit-context words for the Fair Game (2010) end-credits marked letters, transcribed by
commenter James Mulliss (Cipherbrain post 36, comments #5/#6, 9 Feb 2023; on disk at
sources/schmeh/posts/36-fair-game.txt lines ~308-448) -- the "original unmarked credits text"
needed to test the Martin Halpin ("read the letter after the marked one") hypothesis, per
specs/fair-game-2010.json cheap_tests_in_order[0]. No new fetch: already on disk from bSPEC2's
harvest this window.

TOKENS below are transcribed exactly as the commenter wrote them (one marked letter per
comment-thread line, capitalised; comment #6's correction "accoUntrants" -> "accoUntants" with
no 'r' is applied here). Item 4 (the redacted Hammad surname, "???????" in the source) carries
no real letter and is skipped -- nothing to extract a "next letter" from. Two tokens carry two
adjacent marked letters (shOPman: O then P; franCO: C then O); marked_positions() below yields
one (word, index) entry per marked capital, in the order the capitals occur, so both letters of
each such word appear as separate, ordered entries -- matching how the commenter listed them.
"""

TOKENS = [
    "produCtion",
    "sEan",
    "analySt",
    "goOdwin",
    "sAm",
    "Pope",
    "produCtion",
    "tHan",
    "Felicity",
    "Hair",
    "grEenberg",
    "shOPman",
    "bIll",
    "ramSey",
    "gaFfer",
    "Mcgrath",
    "techNicians",
    "Accounting",
    "Delaney",
    "sAar",
    "urMson",
    "dialoguE",
    "eriC",
    "lArry",
    "boOth",
    "patRick",
    "rivEr",
    "meDia",
    "mAnager",
    "waTson",
    "desigNer",
    "pRoduction",
    "mArie",
    "hamdY",
    "accoUntants",
    "fUad",
    "diRector",
    "hanNoun",
    "jacQues",
    "adaWi",
    "Kuala",
    "siNgh",
    "pUller",
    "Fei",
    "progRamming",
    "franCO",
    "benJamin",
    "cooRdinator",
    "offhollyWood",
    "cleaRances",
    "Muir",
    "proviDed",
    "Game",
    "alkhEr",
    "kHuttar",
    "mUsic",
    "abcneWs",
    "Tv",
    "brOwn",
    "Abo",
    "Kevan",
    "pieRre",
    "pArticipant",
]


def marked_positions():
    """Yield (word_lower, index) for every capital letter in TOKENS, in order.
    A token with two capitals (shOPman, franCO) yields two entries, in left-to-right order."""
    out = []
    for tok in TOKENS:
        for i, ch in enumerate(tok):
            if ch.isupper():
                out.append((tok.lower(), i))
    return out

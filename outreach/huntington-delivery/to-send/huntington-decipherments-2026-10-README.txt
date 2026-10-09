Who made this
    Cipher Lab is one person, who directs the project and sends every message, working with AI
    agents (Claude models) in an open repository (https://github.com/NoAutopilot/cipher-lab), every
    step logged there. The transcriptions, readings, code-word grades and searches in this file
    were made by the agents; each item was then checked by separate AI review passes (sessions
    other than the one that made the reading), which searched for prior print. No human specialist
    has checked these readings yet.

What this file is
    Items from the Huntington Library's collections whose text we did not find in the Official
    Records or the other editions searched, each checked by two separate AI review passes; items
    already in print, and items checked by one pass only, are left out. 68 rows: 65 for 68
    telegrams in the ledgers (3 rows hold two telegrams each and say so in the reading), and 3 for
    cipher passages in letters (mssBLA 186, mssBLA 191, mssBLA 184). Prepared 9 Oct 2026; the
    repository holds the current version and readings may be revised; the links in each row are
    pinned to the repository version this file was made from (af756f91d).

What is ours and what is theirs
    The page images, the catalogue records and the volunteer transcription ('Decoding the Civil
    War') are the Huntington Library's, used here under its Digital Library terms. We claim nothing
    in the column 'ledger/page text as we transcribed it': it is made from those page images, with
    the volunteer transcription as a second witness, and it is the Huntington Library's to use
    under its own terms. The meanings of the code words come from the Huntington Library's own
    cipher books (Cipher No. 1, Huntington mssEC 41; Cipher No. 2, Huntington mssEC 47; Cipher No.
    9 vocabulary, Huntington mssEC 67); our key files only index them, page by page. What is ours:
    the readings, the code-word grades and the search notes, and the key rebuilt by us from the
    contemporary decipherments of mssBLA 179, 185, 187, 188, 189, 190 and 194 (the same series).
    These are public under the MIT licence (the LICENSE file in the repository), which asks that
    its short copyright notice travel with substantial copies; a credit line in the record is
    welcome. Suggested: 'Decipherment: Cipher Lab, 2026,
    https://github.com/NoAutopilot/cipher-lab'.

How to import
    The .tsv file is tab-delimited UTF-8 text, for loading; the .csv holds the same rows (UTF-8
    with a byte-order mark, so that Excel opens it correctly); this README is also in the
    -README.txt file beside them. One header row; no tab or line break inside any cell. Each row is
    keyed by 'CONTENTdm collection alias' together with 'CONTENTdm number' (CONTENTdm numbers are
    unique only within a collection). 'record level' says whether the number is a page of a
    compound object (the ledger rows) or the compound object itself (the letters), since CONTENTdm
    edits these differently. 'row id' is unique. Some pages hold two telegrams: those pages have
    two rows with the same CONTENTdm number (5802, 5823, 8910, 8941, 8979, 9039, 9045, 9139, 9142,
    9717); combine them before loading into one record. Where an entry runs onto a second page, the
    row is keyed to the first page and the page cell names the continuation. Map only the columns
    you want (for example the readings, the code words and the credit line) to your own fields; the
    others are there for checking.

Grades of a code word
    from the Huntington cipher book = the meaning is written in the period cipher book named in
    'cipher book or key used'; from a printed or period decipherment = only a printed edition, or a
    decipherment made at the time, gives it; cryptanalytic = worked out from the cipher itself,
    with a control test; inferred = not read directly from the book: worked out from context, from
    another message, or a repair of a clerk's slip; uncertain = a reading we are not sure of;
    unread = a code word or group we could not read; 'as written' = the word is kept as the clerk
    wrote it (a plain word, or a group whose meaning is not settled) and counted with the grade
    given.

Classes (prior-publication check)
    N0 = the plaintext and a decipherment of this very item were already known; N1 = the plaintext
    is already published; ours is an independent re-decipherment; N2 = the plaintext is known
    elsewhere, but no prior mapping of this cipher text to it was found; N3 = no prior plaintext or
    decipherment located after a logged search; N4 = no prior decipherment located, with the
    principal editions, catalogues and project pages searched (internal or unpublished work not
    excluded); N5 = confirmed by the holding archive or a specialist. Each class was set by a
    separate AI review pass after a logged search, and a second pass then tried again to find the
    text in print.

How much is read
    The cell first counts the code words (or cipher groups) and how each was read, then gives the
    depth in words: deciphered = every code word read and checked against an outside source;
    largely deciphered = at least 80% of the code words read, with an outside check of the content
    (a printed reply or related print, or a control test); partially deciphered = at least one
    passage reads and one true sentence about the content can be written, but the checks for
    'largely' are not all met, so a telegram whose every code word is read is still 'partially
    deciphered' when no outside check of its content was found; fragments read = scattered words
    only.

Adds less? (and why)
    yes = the AI review passes noted that our reading adds less than usual: much of the message is
    already readable in the clear in the Huntington's volunteer transcription (the clerks wrote
    many words in plain English), or its outcome, reply or a related message is already in print.
    The share of words written in the clear is counted from our transcription.

Conventions in the readings and the transcription
    In 'reading (marked up)': [..] = a code word replaced by its meaning as the book gives it, with
    the book's own notes kept: '(-ed, -ing)' = the word also stands for its -ed and -ing forms;
    '[#]' = the book marks the word in its margin; '[sic: X]' = the book's spelling, X the word
    meant; 'Command = Er' = the book's entry for 'commander'; [n] = a number written in numeral
    code words; [.] [,] ["] and the like = punctuation code words, and a [?] standing alone = the
    code word for a question mark; [?] after a word = a doubtful reading of the handwriting (or of
    the book); 's after a bracket = the code word carries an s (a plural or a possessive); {time:
    ..} and {date: ..} = time and date code words; {tail: ..} = everything from the signature code
    word on ([signed] = the signature code word; a second telegram in the same ledger entry follows
    the clerk's word 'another'). In the letters' rows the reading is given syllable by syllable as
    the cipher groups stand, and [?73] = cipher group 73, unread. 'reading (plain text)' renders
    the same text in plain words (endings joined, punctuation as punctuation); where the two
    differ, the marked-up reading is the record. In the transcription: lines are separated by ' /
    '; <del>..</del> = struck through; <ins>..</ins> = written above the line; word[?] = doubtful;
    ' = ' joins a word the clerk split; for number ciphers, the cipher groups line by line.

Dates, places and names
    'date and time as written' comes from the ledger header or the letter ('12 M' = noon; a date in
    brackets is the catalogue's); 'date (YYYY-MM-DD)' gives the day, or a range of years as
    1727/1728. Places are normalized (Ft Monroe = Fort Monroe; Hd Qrs A. of J. = Headquarters, Army
    of the James); the ledger's own spelling stays in the transcription. Senders and addressees are
    as the review passes name them.

Abbreviations
    OR = The War of the Rebellion: A Compilation of the Official Records of the Union and
    Confederate Armies (1880-1901); 'OR ser. I vol. 33', 'OR I/33' = series I, volume 33; 'pt' =
    part; 'p.', 'pp.' = page(s); ORN = Official Records of the Union and Confederate Navies in the
    War of the Rebellion; Butler Corr. or Butler's printed correspondence = Private and Official
    Correspondence of Gen. Benjamin F. Butler (1917); Grant Papers = The Papers of Ulysses S.
    Grant; Plum = W. R. Plum, The Military Telegraph during the Civil War (1882); IA = Internet
    Archive; HMC = Historical Manuscripts Commission; TNA = The National Archives (UK); LoC =
    Library of Congress; NARA = U.S. National Archives; Chronicling America = the Library of
    Congress's digitized newspapers; open scholarship indexes = OpenAlex, Semantic Scholar, CORE
    and CrossRef; Zooniverse Talk = the discussion boards of the volunteer transcription project;
    QMG = Quartermaster General; AAG = Assistant Adjutant General.

CONTENTdm collection alias
    The Digital Library collection the record belongs to (CONTENTdm alias).

CONTENTdm number
    The record's CONTENTdm number in that collection; with the alias, the key to import by.

record level
    'page (of a compound object)' for a ledger page, 'compound object (letter)' for a whole letter.

row id (our entry)
    Our id for the telegram or letter (unique; the same id is used in the repository).

Huntington call number
    The call number of the volume or item.

page title (Digital Library) or pages read
    The page title in the Digital Library record (and the continuation page, if any); for a letter,
    the pages read, with each page's own CONTENTdm number.

telegram numbers on this page (Huntington 'Telegram Number' field)
    The page record's own 'Telegram Number' field, as the Digital Library gives it, for the whole
    page; filled only where our cached copy of the record carries the field (a blank does not mean
    the record lacks it).

Digital Library URL
    The record's page in the Digital Library.

date and time as written
    See 'Dates, places and names'.

date (YYYY-MM-DD)
    See 'Dates, places and names'.

from
    The sender, as the review passes name them (an operator or forwarding office may be named with
    'via').

to
    The addressee, as the review passes name them.

place
    The place of sending the ledger heads the entry with (normalized); blank where the page gives
    none.

transcribed from
    What our transcription was made from: the page image, or the volunteer transcription alone.

ledger/page text as we transcribed it
    Our transcription of the ledger entry or the cipher passage; see 'Conventions'.

reading (marked up)
    The decoded text with its markup; see 'Conventions'.

reading (plain text)
    The same reading in plain words; see 'Conventions'.

summary (one sentence)
    One true sentence about the content, written by a review pass from the reading.

code words and meanings
    Each code word or cipher group as written = its meaning (grade); 'xN' = it occurs N times.
    Punctuation, time and signature code words are included. The 'Code words' sheet of the .xlsx
    gives one code word per line.

cipher book or key used
    The period cipher book (with its call number) whose meanings the code words were read from, or
    the key we rebuilt.

cipher book (Digital Library URL)
    The cipher book's record in the Digital Library.

uncertain or unread words
    Code words graded uncertain, inferred or unread, and other doubtful words, with the review
    passes' notes.

prior print checked
    Where the review passes searched for the text in print, and when; 'not found in' is a search
    result, not a claim of priority.

partly in print?
    Related text that is in print (an outcome, a reply, a sequel, or the clear part of the letter),
    as the review passes name it; blank if they name none.

prior-publication check (class)
    See 'Classes'.

reading (repository link)
    The reading in the repository, at this entry.

search log (repository link)
    The search log (AUDIT.md) in the repository, at the review section for this entry.

suggested credit line
    A credit line, if you wish to use one.


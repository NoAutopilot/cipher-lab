# it16: 16th-c. Italian letter text for the character model

Internet Archive OCR full text (`_djvu.txt`), fetched once on 24 Sept 2026 (manifest.json). Build:

    python3 tools/italian16_corpus.py tools/data/it16/*.txt --out it16_all.txt
    python3 tools/italian_ngram.py build it16_all.txt --out it16_all.npz

The filter keeps 417 paragraphs, 282,755 letters (period letter text; editorial prose mostly dropped).
The .npz (14 MB) is not committed; rebuild it. For a matched control, hold out every 10th paragraph
(`awk 'NR%10==3'`) and build the solving model from the rest (`awk 'NR%10!=3'`).

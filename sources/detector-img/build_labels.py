#!/usr/bin/env python3
"""One-off: build sources/detector-img/labels.tsv from images already on disk
under ciphers/*/images, per the manual labeling in NOTES.md/filenames done by
worker detIMG, 24 Sept 2026 (see ROOM.md and QUEUE.md 'Image detector' for the
source of each label). Not a shared tool; rerun only if the label lists below
change. Deterministic holdout: every 3rd item (by list order) within each
class held out.
"""
import os

REPO = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

POSITIVES = [
    # Gramont (BnF fr.2980)
    "ciphers/fr2980-gramont/images/f30_item22.jpg",
    "ciphers/fr2980-gramont/images/f29_item21.jpg",
    # Danzay (BnF fr.20140)
    "ciphers/fr20140-danzay-1557/images/native_f70.jpg",
    "ciphers/fr20140-danzay-1557/images/f69_cipher.jpg",
    "ciphers/fr20140-danzay-1557/images/f71_cipher.jpg",
    # Salviati (BnF fr.2933), nomenclator letter, all 7 leaves on disk
    "ciphers/fr2933-salviati-1525/images/f54v_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f55r_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f55v_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f56r_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f56v_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f57r_ref1600.jpg",
    "ciphers/fr2933-salviati-1525/images/f57v_ref1600.jpg",
    # Seure (BnF fr.3151, f75L)
    "ciphers/fr3151-seure-1558/images/src_ark_12148_btv1b9059865k_f75_100_100_3800_5450.jpg",
    # Lodewijk van Nassau (KHA): p1 = numeral ciphertext for all 6 letters;
    # p2 = cipher continuation for 4610/4611/4612/4616 (crops confirm dense cipher)
    "ciphers/lodewijk-van-nassau-1573-74/images/04610_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04610_p2.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04611_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04611_p2.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04612_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04612_p2.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04613_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04615_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04616_p1.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04616_p2.png",
    # August van Saksen (Saxony), NOTES.md: p2 carries 3 more cipher lines (~90 signs)
    "ciphers/august-van-saksen-1561-64/images/00053_p2.png",
    # Blathwayt (Huntington), NOTES.md cipher-location table
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA191_p5.jpg",  # pure numeric cipher, no decipherment
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA188_p3.jpg",  # largest cipher table
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA188_p4.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA187_p3.jpg",  # enclosed cipher sheet, interlinear
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA190_p7.jpg",  # cipher + interlinear decipherment
    # Eckert (Huntington mssEC), telegraph code-word ledger entries confirmed in NOTES.md/AUDIT.md
    "ciphers/eckert-1864/images/mssEC19_p8941.jpg",
    "ciphers/eckert-1864/images/mssEC25_p5621.jpg",
    "ciphers/eckert-1862/images/mssEC15_p4964.jpg",
    "ciphers/eckert-1862/images/mssEC15_p4970.jpg",
    "ciphers/eckert-1862/images/mssEC15_p4971.jpg",
    "ciphers/eckert-1862/images/mssEC15_p4974.jpg",
    "ciphers/eckert-1862/images/mssEC15_p4976.jpg",
    # Letellier/Brienne (BnF fr.5160): NOTES.md "dense band walk" leaves of the ciphered letter
    "ciphers/fr5160-letellier-1653/images/native/f173.jpg",
    "ciphers/fr5160-letellier-1653/images/native/f8.jpg",
    "ciphers/fr5160-letellier-1653/images/native/f9.jpg",
    # Carpi (BnF Dupuy 452): filename-labelled cipher folio
    "ciphers/dupuy452-carpi-1520/images/btv1b10036146c_canvas23_folio20_carpi_cipher.jpg",
    "ciphers/dupuy452-carpi-1520/images/img/btv1b10036146c_f24_folio20r_full.jpg",
]

NEGATIVES = [
    # Carpi: filename-labelled plain folios, same ark
    "ciphers/dupuy452-carpi-1520/images/btv1b10036146c_canvas16_folio16_carpi_plain.jpg",
    "ciphers/dupuy452-carpi-1520/images/btv1b10036146c_canvas21_folio19_adrianvi_plain.jpg",
    # Letellier: matched plain controls from the same dossier (NOTES.md: decipherment
    # transcript, and canvases confirmed "no cipher")
    "ciphers/fr5160-letellier-1653/images/native/f168.jpg",
    "ciphers/fr5160-letellier-1653/images/native/f169.jpg",
    "ciphers/fr5160-letellier-1653/images/native/f170.jpg",
    "ciphers/fr5160-letellier-1653/images/f20.jpg",
    "ciphers/fr5160-letellier-1653/images/f100.jpg",
    "ciphers/fr5160-letellier-1653/images/f150.jpg",
    # Blathwayt: same-dossier plain pages (NOTES.md cipher-location table: no cipher on these)
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA184_p2.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA184_p3.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA184_p4.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA186_p2.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA186_p4.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA191_p1.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA191_p2.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA191_p3.jpg",
    "ciphers/huntington-blathwayt-madrid-1728/images/BLA191_p4.jpg",
    # Lodewijk: matched plain/decipherment controls, same dossier
    "ciphers/lodewijk-van-nassau-1573-74/images/04613_p2.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04613_p3.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04615_p2.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04615_p3.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04610_p3.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04610_p4.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04611_p3.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04611_p4.png",
    "ciphers/lodewijk-van-nassau-1573-74/images/04612_p3.png",
    # Saxony: other letters of the same three-letter trio, not confirmed to carry cipher
    "ciphers/august-van-saksen-1561-64/images/00126_p2.png",
    "ciphers/august-van-saksen-1561-64/images/00098_p1.png",
    "ciphers/august-van-saksen-1561-64/images/00074_p1.png",
    "ciphers/august-van-saksen-1561-64/images/00057_p1.png",
    # Gramont: a plain folio from the print-check sample of the same volume
    "ciphers/fr2980-gramont/images/fr3019_check/f86_1600.jpg",
    # Danzay: plain preview folios (f.35 recto opens in clear, per NOTES.md)
    "ciphers/fr20140-danzay-1557/images/preview_f69.jpg",
    "ciphers/fr20140-danzay-1557/images/preview_f72.jpg",
    # Printed pages (10): plain prose from the printed editions in print_check/
    "ciphers/fr2980-gramont/images/print_check/camusat_sample_f150.jpg",
    "ciphers/fr2980-gramont/images/print_check/camusat_f155.jpg",
    "ciphers/fr2980-gramont/images/print_check/camusat_f5.jpg",
    "ciphers/fr2980-gramont/images/print_check/camusat_f8.jpg",
    "ciphers/fr2980-gramont/images/print_check/camusat_f153.jpg",
    "ciphers/fr20140-danzay-1557/images/print_check/delavaud_p80.jpg",
    "ciphers/fr20140-danzay-1557/images/print_check/delavaud_p27.jpg",
    "ciphers/fr20140-danzay-1557/images/print_check/delavaud_p51.jpg",
    "ciphers/fr20140-danzay-1557/images/print_check/delavaud_p53.jpg",
    "ciphers/fr20140-danzay-1557/images/print_check/delavaud_p74.jpg",
]


def split(items):
    rows = []
    for i, path in enumerate(items):
        split_name = "holdout" if i % 3 == 2 else "train"
        rows.append((path, split_name))
    return rows


def main():
    out_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "labels.tsv")
    with open(out_path, "w") as f:
        f.write("path\tlabel\tsplit\n")
        for path, split_name in split(POSITIVES):
            full = os.path.join(REPO, path)
            assert os.path.isfile(full), f"missing: {full}"
            f.write(f"{path}\tcipher\t{split_name}\n")
        for path, split_name in split(NEGATIVES):
            full = os.path.join(REPO, path)
            assert os.path.isfile(full), f"missing: {full}"
            f.write(f"{path}\tplain\t{split_name}\n")
    print(f"wrote {out_path}: {len(POSITIVES)} cipher, {len(NEGATIVES)} plain")


if __name__ == "__main__":
    main()

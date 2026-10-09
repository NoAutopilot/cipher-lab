# CTTS working-directory format (our own note, 9 Oct 2026, MQS-CTTS-EXPORT)

Read from github.com/CrypToolProject/CTTS at commit d8b7d77b4e12e7a22d3980f8b5fb4e44c773287b (28 May 2025), one shallow
clone on 9 Oct 2026, deleted after reading (lane exception logged in ROOM.md 06:53 UTC). README.md and LICENSE beside this
note are unmodified copies (Apache-2.0). No CTTS code is copied into this repository; this note describes the files only.
Classes read: util/Positions.java, util/Colors.java, util/Icons.java, util/FileUtils.java, util/ImageUtils.java,
util/TranscribedImage.java, CTTSApplication.java (COLORS_FILE).

- Working directory = the folder CTTS is started in (`java -jar gui.jar` from it). It opens every .jpg/.png/.bmp there whose
  name does not contain "negative". `.jpeg` is not a supported extension.
- Symbol types are colours. The colour list is fixed (Colors.colorSet(): r, g over {0,85,127,170,212,255} and b over
  that set, then {42}, then {51,102,153,204,243}; black skipped; 431 colours). A colour's string is JavaFX Color.toString(),
  `0xrrggbbaa`, lower-case hex, alpha ff.
- `colors.txt` (and `colors_SECOND_COPY.txt`): one line per colour, in colorSet() order: `<colour>;<transcription value>;<ordering>`.
  Empty value = unassigned type. A value must not contain ';' or a newline.
- `positions/<image stem>_positions.txt` (and `positions_SECOND_COPY/`): one symbol per line,
  `x y w h colourIndex` (Java `%f %f %f %f %3d`; colourIndex into colorSet(); commas read as decimal points; a blank line
  between text lines). A colourIndex at or beyond the set's size makes CTTS drop the whole file. Image stems must not
  contain '.', because FileUtils.textFilename cuts the name at the first '.'.
- `icons/<colour>.png`: the reference icon of a symbol type.
- Coordinates are taken to be the image's own pixels (layoutX/Y of the rectangle on the unscaled image pane); not yet
  confirmed by opening an export in CTTS (needs 16 GB RAM and a 2560x1600 screen: the owner's desktop).

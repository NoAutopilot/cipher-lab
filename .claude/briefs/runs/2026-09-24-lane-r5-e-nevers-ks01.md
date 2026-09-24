LANE R5 WORKER E -- KS-01 BnF fr.3985 f.88, Nevers to Revol, 21 Aug 1593: apply the published key no.60 (Sonnet, cap $8; recovery).
Precondition (orchestrator checks before spawning): LANE N4's check-solved verdict (csKSa/csKSb) for KS-01 is "open" in the target's NOTES.md.
Target folder: ciphers/fr3985-nevers-revol-1593 (created by check-solved). Common rules: .claude/briefs/runs/2026-09-24-lane-r5-common.md.
Read QUEUE.md "Keys index vs unread siblings (LANE N4 scKEYS)" and the target's NOTES.md.
Key: Tomokiyo's no.60 (BnF fr.3995 f.108-110, "the Court's symbol cipher", sources/cryptiana/web/nevers.htm and henryiv2.htm), as
transcribed by D. Bourdeau in dbourdeau/cyphersolver `nevers1593/key60.txt` (MIT code, CC BY 4.0 text: copy the key file with a header
crediting Tomokiyo's reconstruction and Bourdeau's transcription, commit its source commit hash). Shallow clone to the scratchpad, grep only.
1. Image (host gallica.bnf.fr, IIIF image API only, >= 2 s apart, <= 12 requests; you are this lane's only Gallica fetcher): canvases are
   labelled 'NP'; Bourdeau's ratio c = 218 + 2.01*(folio-109) gives ~176 for f.88: fetch a 1000 px thumbnail of canvases 174-178 and
   eye-check for the letter's date and address before any native fetch. Native crops of the cipher lines only; images/manifest.json.
2. Transcribe the cipher runs: pass A by you with tools/iiif_lines.py crops, pass B by one blind Sonnet subagent writing its TSV to disk;
   tools/reconcile_passes.py; settle disagreements.tsv rows on the image. Clear text around the cipher is transcribed too (context).
3. Apply the key with tools/decode_key.py (decode.json + key.tsv); grade H where the sign is in key60 unambiguously, M where a sign or
   reading is uncertain, I for repairs; --check must exit 0. Report counts.
Price at the leaf: at $4 report cost so far in ROOM ("progress"); at 80% push a progress section; at $8 stop.
Output: NOTES.md section "Key no.60 applied to f.88 (24 Sept 2026, LANE R5 E)", reading.txt, key.tsv, decode.json, ciphertext.tsv.
ROOM done: "for LANE V5: ciphers/fr3985-nevers-revol-1593 f.88 reading ready (H h M m I i), cost $c" or the blocker. Rule 10 wording.
Do not verify, do not search print for novelty (the verifier does). Do not start KS-02..KS-07 (one-line suggestion only).

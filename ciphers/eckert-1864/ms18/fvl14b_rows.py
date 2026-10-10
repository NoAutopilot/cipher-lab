#!/usr/bin/env python3
"""FV-L14b: write the N3 rows of AUDIT (FV-L14b) -- status.json results, second-opinion prompts and SECOND-OPINIONS-QUEUE rows -- for E611 E612 E620 E621.
Idempotent (skips rows already present). Run from anywhere."""
import json, os
R = os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..', '..'))
E = {
 'E611': dict(ptr=9733, page=67, entry='second entry on the page', head='"John Horner / Wash\'n May 7th 1864 11 a.m."', sig='[Qr Master Genl U.S.]', depth='D2', pct=96.9,
   comp='31 H + 1 M of 32 code-word tokens', unread=('0', '1'), unres="'Animals' in the 60,000 clause written in clear but also a code word (M)",
   title='Eckert 1864 (mssEC 18): Quartermaster General\'s office to Capt. S. L. Brown, New York, 7 May 1864: daily forage shipments to Fort Monroe, 27,000 bushels of grain and 350 tons of hay, consigned to Col. Biggs (E611)',
   line='Read at grade H with War Department Cipher No. 1: on 7 May 1864 the Quartermaster General\'s office told Capt. S. L. Brown in New York that daily forage shipments to Fort Monroe should average 27,000 bushels of grain and 350 tons of hay, consigned to Col. Biggs; not found in the cached OR/ORN volumes, OR I/36 pts 2-3, IA full text or Google Books (searched 10 Oct 2026).',
   gap='N3 one audit (FV-L14b); not N4: OR ser. III vol. 4 unsearched (lending-only), NARA RG 92 QMG letters-sent not reached, press not searched',
   sent='On 7 May 1864, as Grant\'s army moved south, Washington told its New York forage officer to ship grain and hay daily to Fort Monroe because about 60,000 animals hitherto fed from Washington would be supplied via Monroe.',
   check='code clause: Appian/Animal = Monroe, Shade = Forage read in other filed entries; context only (Lt. Col. Herman Biggs chief quartermaster at Fort Monroe, OR I/36 pts 2-3), no external check of this telegram\'s own content (D2)',
   reading='"[11 AM] For [Captain] S. L. Brown, Asst. [Quartermaster] in charge of [forage], [New York]. The daily shipments of [forage] to [Monroe] should average until further orders [27,000] bushels of grain and [350] tons of hay. Consign this [forage] to [Colonel] Biggs, Chief [Quartermaster], [Department] of [Virginia], and use every exertion to send it forward promptly. The supply at this point has lately been low and barely sufficient for daily wants; there has been no recent accumulation. About [60,000] animals have heretofore [been] supplied from this point; [they] will probably be supplied hereafter via [Monroe]. Acknowledge this on receipt. [Signed] [Quartermaster General U.S.] Mark this confidential."',
   context='OR ser. I vol. 36 pt 2 p.587 prints Meigs to Lt. Col. Herman Biggs, chief quartermaster at Fort Monroe, 9 May 1864 (another telegram); vol. 36 pt 3 shows Biggs forwarding forage from Fort Monroe from 20 May. Neither is this telegram.',
   notyet='Official Records ser. III vol. 4 page by page (Quartermaster General\'s correspondence, 1864); NARA RG 92 letters-sent of the Quartermaster General; the Quartermaster General\'s annual report for 1864-65 (forage at New York); HathiTrust; the New York press of May 1864.',
   prtitle='Quartermaster General\'s office to Capt. S. L. Brown: daily forage shipments to Fort Monroe, 7 May 1864'),
 'E612': dict(ptr=9883, page=217, entry='first entry on the page', head='"Washn Nov 1st 1864"', sig='[Qr Master Genl U.S.]', depth='D2', pct=94.1,
   comp='16 H + 1 M of 17 code-word tokens', unread=('0', '1'), unres="signature span 'M see Me Eggs' (M)",
   title='Eckert 1864 (mssEC 18): Quartermaster General\'s office to Brig. Gen. Robert Allen, Louisville, 1 Nov 1864: the Secretary of War is not satisfied with your conduct; Captain Ferry not yet sent to Memphis under arrest (E612)',
   line='Read at grade H with War Department Cipher No. 1: on 1 Nov 1864 the Quartermaster General\'s office told Brig. Gen. Robert Allen at Louisville that the Secretary of War was not satisfied with his conduct, since Captain Ferry had not been sent to Memphis and arrested as ordered; not found in OR I/39 pt 3, the cached OR volumes, IA full text or Google Books (searched 10 Oct 2026).',
   gap='N3 one audit (FV-L14b); not N4: OR ser. III vol. 4 unsearched, NARA RG 92 / RG 107 not reached, Louisville press of Nov 1864 not searched by page',
   sent='On 1 Nov 1864 Meigs\'s office reproached Allen at Louisville for not sending Captain Ferry to Memphis under arrest as Stanton had ordered days before.',
   check='code clause: Indigo/India = Secretary of War, Drum/Drill = Memphis, Dragon = Louisville read in other filed entries; context only (Captain Ferry, Quartermaster of Transportation at Louisville, Louisville Daily Journal 5 and 7 Jan 1864) (D2)',
   reading='"[1 PM] For [Brigadier General] Robt. Allen, [Quartermaster], [Louisville]. [The Secretary of War] informs me that many days since he ordered you to order [Captain] Ferry to [Memphis] without a day\'s delay and to arrest him and to [report] to [the Secretary of War] the execution of his order. He understands that [Captain] Ferry has not yet gone to [Memphis] and you have not [reported] as ordered. I am directed to inform you that [the Secretary of War] is not satisfied with your conduct as it appears above. [Signed] M see Me Eggs [Quartermaster General U.S.] the end." The signature span is unread.',
   context='The Louisville Daily Journal of 5 and 7 Jan 1864 names "Captain Ferry, Quartermaster of Transportation at Louisville"; Allen was chief quartermaster at Louisville. Neither is this telegram.',
   notyet='Official Records ser. III vol. 4 and ser. I vols. 39 pt 3, 45 pt 1 by page; NARA RG 92 letters-sent and the Quartermaster General\'s consolidated correspondence file under Ferry; the Louisville and Memphis press of Oct-Dec 1864; any court-martial or arrest record of a Captain Ferry, assistant quartermaster, 1864; HathiTrust.',
   prtitle='Quartermaster General\'s office to Brig. Gen. Robert Allen: Captain Ferry to Memphis under arrest, 1 Nov 1864'),
 'E620': dict(ptr=9897, page=231, entry='first entry on the page', head='"John Horner New York / Washn Nov 15th 1864" (pencilled "10 PM")', sig='[C. A. Dana]', depth='D3', pct=100.0,
   comp='9 H of 9 code-word tokens (body in clear)', unread=('0', '0'), unres="none among code words; 'Niagara' and 'John' are clear on the leaf (decoder's D. D. Porter and Grant wrong)",
   title='Eckert 1864 (mssEC 18): Assistant Secretary Dana to Maj. Gen. Dix, 15 Nov 1864, 10 PM: Beverly Tucker will cross at Niagara Falls on Thursday morning; John Odell may be relied upon to arrest him (E620)',
   line='Read with War Department Cipher No. 1 (time, addressee, punctuation and signature are code; the body is in clear): on 15 Nov 1864 at 10 PM Assistant Secretary Dana told General Dix that Beverly Tucker would cross at Niagara Falls on Thursday morning and asked for an officer to help John Odell arrest him; not found in OR ser. II vol. 7 (which prints the next day\'s arrest order), IA full text or Google Books (searched 10 Oct 2026).',
   gap='N3 one audit (FV-L14b); not N4: Dix and Dana papers, NARA RG 107, the Baker papers and the New York press of Nov 1864 not searched',
   sent='On 15 Nov 1864 Dana told Dix that the Confederate agent Beverly Tucker would cross at Niagara Falls on Thursday and asked for an officer to help John Odell arrest him; the next day Dana ordered Odell to make the arrest.',
   check='code clause: Kasson = Dix, Image = Dana read in other filed entries (C by print in E142); external non-statistical check of content: Baker, History of the U.S. Secret Service (1867), Odell to arrest Tucker at Niagara under Dix\'s order; OR ser. II vol. 7 p.1132 (the 16 Nov order); the leaf\'s own 10.15 PM follow-up (D3)',
   reading='"[10 PM] [15] [Maj. Gen. John A. Dix] [.] I am confidentially informed that Beverly Tucker will cross at Niagara Falls on Thursday morning [.] I am also informed that John Odell may be relied upon to arrest him but I do not know Odell [.] Have you any officer of sufficient discretion who can at once be dispatched to the falls for the purpose [?] [Signed] [C. A. Dana]." Everything but the bracketed words is written in clear.',
   context='OR ser. II vol. 7 p.1132 prints Dana to John Odell, 16 Nov 1864 11.30 p.m., ordering Tucker\'s arrest and delivery to Dix; L. C. Baker, History of the United States Secret Service (1867), describes the plan (Tucker at St. Catharine\'s opposite Niagara Falls; John Odell with an order from Dix). Neither prints this telegram.',
   notyet='The John A. Dix papers (Columbia); Dana\'s and Stanton\'s papers (Library of Congress); NARA RG 107 telegrams sent, Nov 1864; Baker\'s papers and the Turner-Baker case files; Mogelever, Death to Traitors (1960) page by page; the New York and Buffalo press of 15-20 Nov 1864; HathiTrust.',
   prtitle='Dana to Dix: Beverly Tucker will cross at Niagara Falls, 15 Nov 1864'),
 'E621': dict(ptr=9862, page=196, entry='first entry on the page', head='"J W Sampson / Washn Oct 7th 1864"', sig='[General-in-Chief] (Halleck)', depth='D3', pct=90.9,
   comp='10 H + 1 M of 11 code-word tokens', unread=('0', '1'), unres="tail 'she went on to tell' (M); the following '(Cal) 6 P.m' is the next entry's header",
   title='Eckert 1864 (mssEC 18): Halleck to J. W. Garrett, Baltimore and Ohio Railroad, 7 Oct 1864, 4 PM: arms sent to Harper\'s Ferry on the 5th have not arrived; see whether delayed on the railroad (E621)',
   line='Read with War Department Cipher No. 1: on 7 Oct 1864 at 4 PM Halleck asked J. W. Garrett of the Baltimore and Ohio to find out why arms sent from Washington to Harper\'s Ferry on the afternoon of the 5th had not arrived; the affair is printed in OR I/43 pt 2 (6 and 10 Oct), this telegram was not found there, in IA full text or Google Books (searched 10 Oct 2026).',
   gap='N3 one audit (FV-L14b); not N4: Garrett papers (B&O Museum / Maryland Historical Society), NARA RG 107 and the Ordnance letters-sent not reached',
   sent='On 7 Oct 1864 Halleck asked Garrett to trace arms sent by rail to Harper\'s Ferry on the 5th that had not arrived; they arrived on the 8th (OR I/43 pt 2).',
   check='code clause: Cancer = Harpers Ferry, Niggard = Arms read in other filed entries; external non-statistical check of content: OR I/43 pt 2 p.303 (Halleck to Stevenson 6 Oct, arms forwarded yesterday; not arrived) and p.336 (Halleck to Garrett 10 Oct: arms shipped on the 5th reached Harper\'s Ferry on the 8th) (D3)',
   reading='"[4 PM] For J. W. Garrett [.] [Arms] were sent from here to [Harper\'s Ferry] on the afternoon [of the] [5th] inst. It is [report]ed that they have not arrived there. Please see if they have been delayed on the [rail road]. It\'s important that there should be no delay. [Signed] [General-in-Chief]" and an unread tail "she went on to tell".',
   context='OR ser. I vol. 43 pt 2 prints Halleck to Stevenson at Harper\'s Ferry, 6 Oct 1864 4.10 p.m. (arms forwarded yesterday), Stevenson\'s reply (not arrived), and Halleck to Garrett, 10 Oct 1864 (arms shipped on the 5th did not reach Harper\'s Ferry till the 8th; the delay caused by the agent Mr. Koontz). None is this telegram.',
   notyet='The John W. Garrett papers and B&O letter books; NARA RG 107 telegrams sent and RG 156 (Ordnance) letters-sent, Oct 1864; Baltimore press of 7-10 Oct 1864; HathiTrust.',
   prtitle='Halleck to J. W. Garrett: arms for Harper\'s Ferry delayed, 7 Oct 1864'),
}
st = json.load(open(os.path.join(R, 'status.json')))
have = {r.get('title', '') for r in st['results']}
for e, v in E.items():
    if v['title'] in have: continue
    doc = f"Huntington mssEC 18 (obj 10074) p.{v['page']}, pointer {v['ptr']}, {e}"
    st['results'].append({"link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/eckert-1864", "key": "period",
      "audit_refs": ["AUDIT.md '## AUDIT (FV-L14b)'"], "audit_status": "one audit", "superseded_by": "", "depth_by": "FV-L14b verifier (account 1)",
      "depth_date": "10 Oct 2026", "decode_status": "Partially decrypted", "date": "10 Oct 2026", "kind": "reading", "claim_scope": "completed-reading",
      "fields_source": "eckert-1864/AUDIT.md '## AUDIT (FV-L14b)' section 4", "grade": "N3", "plaintext_novelty": "N3", "mapping_novelty": "N3",
      "reading_version": "L14-B/L14-C 10 Oct 2026 (reading.md), corrections in AUDIT (FV-L14b) section 5 not yet applied", "unresolved_spans": v['unres'],
      "depth_unread": {"names_codes": v['unread'][0], "other": v['unread'][1]}, "depth_pct": v['pct'], "title": v['title'], "line": v['line'], "gap": v['gap'],
      "depth": v['depth'], "completeness": v['comp'], "phrases": [doc], "document_id": doc, "documents": [doc], "depth_sentence": v['sent'],
      "depth_check": v['check'], "depth_note": v['comp']})
open(os.path.join(R, 'status.json'), 'w').write(json.dumps(st, indent=2, ensure_ascii=False) + '\n')
q = os.path.join(R, 'SECOND-OPINIONS-QUEUE.tsv'); qs = open(q).read()
for e, v in E.items():
    lab = 'SO-ECKERT-' + e; low = e.lower()
    pp = os.path.join(R, f'ciphers/eckert-1864/second-opinions/PROMPT-chatgpt-{low}.md')
    if not os.path.exists(pp):
        open(pp, 'w').write(f"""SECOND OPINION REQUEST, label {lab}

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) p.{v['page']} (digital pointer {v['ptr']}), {v['entry']}, {e}, headed {v['head']}, https://hdl.huntington.org/digital/collection/p16003coll11/id/{v['ptr']}. Read with War Department Cipher No. 1 (Huntington mssEC 41).
- Reading: {v['reading']} Bracketed words are code words read from the period key; everything else is written in clear on the page.
- Context we already know: {v['context']}
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-L14b)").

WHERE WE HAVE LOOKED: 177 cached Official Records, ORN and correspondence volumes by phrase and date window; the OR volumes named in the audit; Internet Archive full-text search across the whole collection (control passed); Google Books (keyed, exact phrases); the Huntington's CONTENTdm full-text search across the whole Eckert collection.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- {v['notyet']}

HOW TO REPORT (this part is the same for every label)
- Write your answer as one Markdown file in the repository github.com/NoAutopilot/cipher-lab at the path
  `ciphers/eckert-1864/second-opinions/chatgpt-{low}-<UTC date>.md`. Do not touch any other file. Do not commit to `main`:
  create a branch named `second-opinion/{lab}` and open a pull request from it, titled exactly
  `[{lab}] second opinion: {v['prtitle']}`.
- The first lines of the file must be this header, filled in:
      label: {lab}
      model: <your model name and version>
      date: <UTC date you answered>
      prompt: PROMPT-chatgpt-{low}.md in this folder
  and then sections 1-5 in the order below.
- Every citation must be checkable from a desk: author, title, year, volume, page, and a URL to the page
  on Google Books, HathiTrust, Internet Archive, Gallica or the publisher. If you cannot give a page and a
  URL, mark the citation "unverified". Never invent a page number.
- Do not use the words "first", "new", "unpublished", "unread" or "never printed" about our reading. Our
  rule is that only a separate verifier may say that. Your job is to try to prove the opposite: that the
  text is already in print somewhere, or that our reading is wrong.

WHAT TO PUT IN THE FILE
1. Prior print: any edition, calendar, article or book that prints this telegram, quotes it, summarises it,
   or prints its decipherment. Give the earliest you can find. If you find nothing, list exactly what you
   searched (catalogue, query, date) so we can tell a real gap from a shallow search.
2. Prior decipherment: anyone who has already read this cipher entry, including blog posts, GitHub
   repositories, the Decoding the Civil War project, DECODE (de-crypt.org) records, theses, and papers.
3. Errors in our reading: any token, name, date or phrase you believe is misread, with your reason and
   the source that shows it.
4. Leads: archives, editions or scholars we should check, with a one-line reason each.
5. Confidence: one sentence on how sure you are that nothing prior exists, and what would change it.
""")
    if lab + '\t' not in qs:
        qs += f"{lab}\tciphers/eckert-1864\tciphers/eckert-1864/second-opinions/PROMPT-chatgpt-{low}.md\t2026-10-10\tqueued\t\t\n"
open(q, 'w').write(qs)
print('ok')

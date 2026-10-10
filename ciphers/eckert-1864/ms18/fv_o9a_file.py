"""FV-O9a (10 Oct 2026, account 1, for LANE LEDGER-N2): file the first audit of O9-DC, O9-DE, O9-DH, O9-DI -- AUDIT.md section, NOTES.md section,
status.json result rows, SO prompts + SECOND-OPINIONS-QUEUE.tsv rows, WORK-QUEUE.tsv AUD2-LEDGERN2-5. Idempotent (re-run after a rebase).
Usage: fv_o9a_file.py AUDIT_SECTION.md NOTES_SECTION.md SO_TAIL.md"""
import json, os, sys
R = os.path.dirname(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
T = os.path.join(R, 'ciphers', 'eckert-1864')
audit_sec, notes_sec, so_tail = (open(p).read() for p in sys.argv[1:4])

def append_once(path, text, marker):
    cur = open(path).read()
    if marker in cur:
        print('present', os.path.relpath(path, R)); return
    open(path, 'a').write(('' if cur.endswith('\n') else '\n') + text.rstrip('\n') + '\n'); print('appended', os.path.relpath(path, R))

append_once(os.path.join(T, 'AUDIT.md'), audit_sec, '## AUDIT (FV-O9a)')
append_once(os.path.join(T, 'NOTES.md'), notes_sec, '## FV-O9a (10 Oct 2026')

E = {
 'O9-DC': dict(lab='O9DC', ptr=9673, page='p.7', pos='the first entry on the page', head='John Horner 9 / Washn Feby 5th 1864', depth='D3', pct=100.0, nc='0', oth='0',
   short='Meigs to Van Vliet: a separate account for the Marcia C. Day expedition, 5 Feb 1864',
   title='Eckert 1864 (Washington sent ledger, Cipher No. 9): Quartermaster General Meigs to Major Van Vliet, New York, 5 Feb 1864: keep all costs of the Marcia C. Day (the Ile a Vache return voyage) in a separate account for reimbursement (O9-DC)',
   line="Read at grade H with the older War Department vocabulary (Cipher No. 9, Huntington mssEC 67): on 5 Feb 1864 Quartermaster General Meigs told Major Van Vliet at New York to keep every cost of chartering, fitting out and victualling the Marcia C. Day in a separate account, so that this special expedition could be reimbursed; not located in print (searched 10 Oct 2026).",
   comp='7 H of 7 code words; the rest plain; ship name plain (Maria C Day on the leaf = Marcia C. Day, I)',
   sent="Meigs had the cost of the ship sent to bring the Ile a Vache colonists home kept on a separate account so it could be charged back.",
   chk="code clause: Pagan Feby fifth Henrietta for Village Van Vliet Vincent Merlin = Washington ... 4 PM, for Major Van Vliet, Quartermaster, New York; external: New York Times 21 Mar 1864 (the Marcia C. Day sent to the Isle of Avache; 'Stewart Van Vliet, Major and Quartermaster' on the same page)",
   reading='"[Washington] Feby fifth [4 PM] for [Major] Van Vliet [Quartermaster] [New York] period Let all expenses incurred in charter and out fit and victualling manning sailing loading including Stores and rations from [Subsistence] Dept put on board Maria C Day be kept in a separate and distinct account so that the cost of this special expedition may be known and reimbursed if desirable when completed sig M C Meigs [Quartermaster General] warm cloudy like rain"',
   context='The ship Marcia C. Day was chartered in Feb 1864 to bring the surviving colonists back from the Ile a Vache, Haiti; she landed them at Alexandria on 20 March (New York Times 21 Mar 1864; Pittsburgh Post 24 Mar 1864). Major Stewart Van Vliet was Quartermaster at New York.',
   notyet='Official Records ser. III vol. 4; the Meigs papers (Library of Congress) and Quartermaster General letter books (NARA RG 92); the Edward L. Hartz papers (Duke, Rubenstein Library); the Interior Department and congressional documents on the Ile a Vache return (1864); the New York press of Feb 1864; HathiTrust; JSTOR.'),
 'O9-DE': dict(lab='O9DE', ptr=9684, page='p.18', pos='the third entry on the page', head='John Horner N.Y. (9) / Washn Mar 10th 10 30 PM 1864', depth='D2', pct=75.0, nc='0', oth='2',
   short='Fox to Olcott: seize H. D. Stover\'s books and papers, 10 Mar 1864',
   title='Eckert 1864 (Washington sent ledger, Cipher No. 9): G. V. Fox to Col. H. S. Olcott, New York, 10 Mar 1864 10.30 PM: seize the books and papers of H. D. Stover, prisoner in Fort Lafayette; no permits until consultation (O9-DE)',
   line="Read at grade H with Cipher No. 9 (period key): on 10 Mar 1864 G. V. Fox told Col. H. S. Olcott at New York to seize the books and papers of the contractor H. D. Stover, then a prisoner in Fort Lafayette, and said no permits would be issued until they had consulted; not located in print (searched 10 Oct 2026).",
   comp="6 H of 8 cipher tokens; 'dam bore' after the signature unread (M 2)",
   sent="Fox had the jailed contractor Stover's books and papers seized and froze visiting permits until Olcott came to Washington to consult.",
   chk="Husband = (Fort) La Fayette and Atlas = Fox read in two contexts (O9-DE, O9-DI), Venus ... Midas in two (O9-DE, O9-DH); external: Diary of Gideon Welles vol. I (1911) pp.524-525, 536-540 and holder 4732; 75% of cipher tokens H, under the D3 line",
   reading='"[Washington] [10.30 PM] tenth For [Colonel] H. S. Olcutt [New York] Seize all the books & papers of H. D. Stover now prisoner in [(Fort) La Fayette] period no permits will be issued until we have held consultation sig [G. V. Fox] dam bore"',
   context="Diary of Gideon Welles vol. I (1911) pp.524-525 (15 Feb 1864: Stover, 'the convict in Fort Lafayette', and the permits to visit him), pp.536-540 (7-12 Mar 1864: Olcott's arrests of contractors; Olcott comes to consult with Fox). Olcott's telegram of 20 June 1864 (Huntington Eckert papers, pointer 4732) reports a pardon for Stover.",
   notyet='the Fox papers (New-York Historical Society) and Fox, Confidential Correspondence vol. 1; the Olcott papers; NARA RG 45; the congressional reports on the Navy-contract frauds (1864-65); the New York press of 9-15 Mar 1864; HathiTrust; JSTOR.'),
 'O9-DH': dict(lab='O9DH', ptr=9684, page='p.18', pos='the first entry on the page', head='John Horner / Washn Mar 9th 1864 11 am', depth='D3', pct=100.0, nc='0', oth='0',
   short='Fox to Olcott: is Brady a Navy or an Army matter, 9 Mar 1864 11 AM',
   title='Eckert 1864 (Washington sent ledger, Cipher No. 9): G. V. Fox to Col. H. S. Olcott, New York, 9 Mar 1864 11 AM: is Brady connected with a Navy operation or the Army? (O9-DH)',
   line="Read at grade H with Cipher No. 9 (period key): at 11 a.m. on 9 Mar 1864 G. V. Fox asked Col. Olcott whether Brady's case was a Navy or an Army matter, saying the Navy would arrest him in the first case and the War Department should act in the second; not located in print (searched 10 Oct 2026).",
   comp='6 H of 6 code words; time word = header time',
   sent="Fox, asked by Olcott to have Edwin L. Brady arrested, first asked whether the case belonged to the Navy or the Army.",
   chk="code clause: Francis For Venus Ol cott Midas = 11 AM, Colonel Olcott, New York (time word = the header's 11 am); external: holder 4491 (Olcott to Fox, 8 Mar 1864 8.40 PM, asking for Edwin L. Brady's arrest)",
   reading='"[11 AM] For [Colonel] Ol cott [New York] Is Brady connected with a Navy operation or [Army] If the former this Dept will [Arrest] him If the latter the War Dept should take it up (sig) [G. V. Fox]"',
   context="Olcott to Fox, New York 8 Mar 1864 8.40 PM (Huntington Eckert papers, pointer 4491): 'papers Show Edwin L Brady is connected with savage in a thirty thousand dollars Steamboat send me order to arrest him and put in Ft Lafayette or Fort Warren have Gen Dix instructed as before'.",
   notyet='the Fox papers (New-York Historical Society) and Fox, Confidential Correspondence vol. 1; the Olcott papers; NARA RG 45 and RG 107; the congressional reports on the Navy-contract frauds (1864-65); the New York press of 9-15 Mar 1864; HathiTrust; JSTOR.'),
 'O9-DI': dict(lab='O9DI', ptr=9684, page='p.18', pos='the second entry on the page', head='Wash. D. C. / John Horner N.Y. "No 9" / mar. 9th 1864', depth='D3', pct=100.0, nc='0', oth='0',
   short='Fox to Olcott: arrest Edwin L. Brady, place him in Fort Lafayette, 9 Mar 1864',
   title='Eckert 1864 (Washington sent ledger, Cipher No. 9): G. V. Fox to Col. H. S. Olcott, New York, 9 Mar 1864 (9.30 PM by the time word): arrest Edwin L. Brady, place him in Fort Lafayette, call on General Dix (O9-DI)',
   line="Read at grade H with Cipher No. 9 (period key): on the evening of 9 Mar 1864 G. V. Fox ordered Col. Olcott to arrest Edwin L. Brady, place him in Fort Lafayette and call on General Dix for assistance, answering Olcott's request of 8 March (Huntington Eckert papers, pointer 4491); not located in print (searched 10 Oct 2026).",
   comp='5 H of 5 code words',
   sent="That evening Fox ordered Brady arrested and sent to Fort Lafayette with General Dix's help.",
   chk="code clause: place him in husband Call upon Agate for Assistance Atlas = Fort La Fayette ... General Dix ... Fox; external: holder 4491 ('put in Ft Lafayette ... have Gen Dix instructed')",
   reading='"[9.30 PM] for [Colonel] Olcott Arrest Edwin L. Brady & place him in [(Fort) La Fayette] Call upon [Jno. A. Dix] for Assistance [G. V. Fox]"',
   context="Olcott to Fox, New York 8 Mar 1864 8.40 PM (Huntington Eckert papers, pointer 4491), asking for an order to arrest Edwin L. Brady, put him in Fort Lafayette or Fort Warren and have General Dix instructed.",
   notyet='the Fox papers (New-York Historical Society) and Fox, Confidential Correspondence vol. 1; the Olcott papers; the Dix papers; NARA RG 45 and RG 107; the New York press of 10-15 Mar 1864 (an arrest of a New York oil contractor); HathiTrust; JSTOR.'),
}

# SO prompts and queue rows
q = os.path.join(R, 'SECOND-OPINIONS-QUEUE.tsv'); qcur = open(q).read()
for eid, e in E.items():
    low = e['lab'].lower(); label = 'SO-ECKERT-' + e['lab']
    pp = os.path.join(T, 'second-opinions', f'PROMPT-chatgpt-{low}.md')
    tail = (so_tail.replace('chatgpt-n2-fa', f'chatgpt-{low}').replace('SO-ECKERT-N2-FA', label)
            .replace("Dana to Warren: Felix McCloskey, Seymour's ballot commissioner for the Fifth Corps, 30 Oct 1864", e['short']))
    body = f"""SECOND OPINION REQUEST, label {label}

We are an open cipher-research repository (github.com/NoAutopilot/cipher-lab). We have read one American Civil War-era
cipher telegram and want you to try to prove that its text was already printed before us, and to find mistakes in our
reading. Be adversarial: we would rather learn now that it is in print than claim it wrongly later.

THE ITEM
- Source: Thomas T. Eckert Papers, Huntington Library, San Marino, mssEC 18 (War Department telegraph office, ciphers sent) {e['page']} (digital pointer {e['ptr']}), {e['pos']}, {eid}, headed "{e['head']}", https://hdl.huntington.org/digital/collection/p16003coll11/id/{e['ptr']}. Read with the older War Department vocabulary, Cipher No. 9 (Huntington mssEC 67); the book is in the same collection.
- Reading: {e['reading']}. Bracketed words are code words read from the period key; the rest is clear on the page.
- Context we already know: {e['context']}
- Our files: reading https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/reading-no9.md,
  key https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/key-no9.md, search log
  https://raw.githubusercontent.com/NoAutopilot/cipher-lab/main/ciphers/eckert-1864/AUDIT.md (section "AUDIT (FV-O9a)").

WHERE WE HAVE LOOKED: Official Records ser. I volumes for Feb-Mar 1864 and ser. II vols. 6-7 (phrase and name grep); Diary of Gideon Welles vol. I; Internet Archive full text (phrases, names); Google Books (4 queries); the Huntington's CONTENTdm full-text search.

WHERE WE HAVE NOT YET LOOKED PROPERLY (start here)
- {e['notyet']}

"""
    if not os.path.exists(pp):
        open(pp, 'w').write(body + tail); print('wrote', os.path.relpath(pp, R))
    else:
        print('present', os.path.relpath(pp, R))
    if label + '\t' not in qcur:
        qcur = qcur + ('' if qcur.endswith('\n') else '\n') + f"{label}\tciphers/eckert-1864\tciphers/eckert-1864/second-opinions/PROMPT-chatgpt-{low}.md\t2026-10-10\tqueued\t\t\n"
open(q, 'w').write(qcur)

# status.json
sp = os.path.join(R, 'status.json'); d = json.load(open(sp)); have = {x.get('title', '') for x in d['results']}
for eid, e in E.items():
    if e['title'] in have: print('status present', eid); continue
    doc = f"Huntington mssEC 18 (obj 10074) {e['page']}, pointer {e['ptr']}, {eid}"
    d['results'].append({
     "link": "https://github.com/NoAutopilot/cipher-lab/tree/main/ciphers/eckert-1864", "key": "period",
     "audit_refs": ["AUDIT.md '## AUDIT (FV-O9a)'"], "audit_status": "one audit", "superseded_by": "",
     "depth_by": "FV-O9a verifier (account 1)", "depth_date": "10 Oct 2026", "decode_status": "Partially decrypted", "date": "10 Oct 2026",
     "kind": "reading", "claim_scope": "completed-reading", "fields_source": "eckert-1864/AUDIT.md '## AUDIT (FV-O9a)' section 4",
     "reading_version": "O9R-1 10 Oct 2026 (reading-no9.md), grades as in AUDIT (FV-O9a) s.3 (context notes in s.5 pending a FIX job)",
     "unresolved_spans": "dam bore" if eid == 'O9-DE' else "", "depth_unread": {"names_codes": e['nc'], "other": e['oth']}, "depth_pct": e['pct'],
     "grade": "N3", "plaintext_novelty": "N3", "mapping_novelty": "N3", "title": e['title'], "line": e['line'],
     "gap": "N3 one audit (FV-O9a); not N4: " + e['notyet'].rstrip('.') + " not searched; second audit queued (AUD2-LEDGERN2-5)",
     "depth": e['depth'], "completeness": e['comp'], "phrases": [doc], "document_id": doc, "documents": [doc],
     "depth_sentence": e['sent'], "depth_check": e['chk'], "depth_note": e['comp']})
    print('status appended', eid)
open(sp, 'w').write(json.dumps(d, indent=2, ensure_ascii=False) + '\n')

# WORK-QUEUE
w = os.path.join(R, 'WORK-QUEUE.tsv'); wcur = open(w).read()
if 'AUD2-LEDGERN2-5\t' not in wcur:
    note = ('"second audit eckert-1864 O9-DC O9-DE O9-DH O9-DI (cap 2.5 per entry; first audit AUDIT.md ""## AUDIT (FV-O9a)""; Cipher No. 9, ciphertext-no9.txt, '
            'key-no9.md sample table): O9-DC N3 D3 (Meigs to Van Vliet, 5 Feb 1864: separate account for the Marcia C. Day, the Ile a Vache return; mssEC 18 p.7, '
            'pointer 9673/0; NYT 21 Mar 1864); O9-DE N3 D2 (Fox to Olcott, 10 Mar 1864 10.30 PM: seize H. D. Stover\'s books and papers; pointer 9684/1; Welles '
            'Diary I pp.524-525, 536-540; dam bore M); O9-DH N3 D3 and O9-DI N3 D3 (Fox to Olcott, 9 Mar 1864 11 AM and evening: Brady, Navy or Army; arrest Edwin L. '
            'Brady, Fort Lafayette, Dix; pointer 9684/0; holder 4491 = Olcott\'s request of 8 Mar). Not searched: Fox and Olcott papers, Fox Confidential '
            'Correspondence vol. 1, NARA RG 45/92/107, congressional fraud reports, NY press Feb-Mar 1864, HathiTrust, JSTOR. For LANE LEDGER-N2 (account 1)"')
    row = f"AUD2-LEDGERN2-5\taccount-3\t.claude/briefs/runs/2026-10-10-acct1-lane-ledger-n2-jobs.md\tOpus 5.5\t10\t110\tqueued\t2026-10-10 02:2x\t{note}\n"
    open(w, 'w').write(wcur + ('' if wcur.endswith('\n') else '\n') + row); print('work-queue appended')
else:
    print('work-queue present')

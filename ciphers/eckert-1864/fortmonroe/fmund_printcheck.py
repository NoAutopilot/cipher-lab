#!/usr/bin/env python3
"""FM-UND (10 Oct 2026): letters-only phrase grep of the readable No. 1 phrases of the undated-tail rows in the cached OR/ORN/Butler djvu texts
(sources/ia-fulltext/print-check/*.gz). A miss is a search result, not a verdict (rule 10)."""
import gzip, os, re, sys, glob
D = os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', 'sources', 'ia-fulltext', 'print-check')
norm = lambda s: re.sub(r'[^a-z]', '', s.lower())
PH = {
 'U3 5616/0': ['send steamers to Cheese a peake city to meet and escort the tows down the bay', 'canal barges average capacity', 'steam tugs Hutchins Delany Palmer Tempest Ajax', 'total propellers', 'Hutchins Delany'],
 'U4 5656/0 tel1': ['W. W. Shore is in Baltimore somewhere', 'I want him caught and arrested and sent to me under guard', 'he is the correspondent of the World from Baltimore as he was from here', 'arrest him since which we have heard nothing', 'can send you if necessary a man who knows him'],
 'U4 5656/0 tel2 (clear copy 4601)': ['we have seized Wilsons Wharf landing a brigade', 'Fort Powhatan landing two regiments of same brigade', 'Remainder of both Eighteenth and Tenth Army Corps are now being landed', 'apparently a complete surprise both army corps left Yorktown during last night'],
 'U5 5658/0': ['we have as yet no official report from General Grant', 'nothing is known of his condition except from newspaper reports', 'in respect to the reserves mentioned in your telegram there are none at the disposal', 'you will have to depend only upon such as may have been provided in your programme with him', 'your despatch will be forwarded to him to apprise him of your condition', 'your success thus far is extremely gratifying to the President and this Department', 'Ingalls telegraphed yesterday at noon to General Meigs', 'miles from Bermuda landing', 'all quiet and ready to move in the morning'],
 'U6 5689/0': ['has been entirely on the defensive', 'Wise is here also', 'can be defended when works are complete with', 'leaving 20000 free to operate', 'should not remain on the defensive', 'a skillful use of it will aid General Grant more than the numbers which might be drawn from here', 'Supplies of all kinds are abundant', 'Weitzel has just been made Chief Engineer', 'we would prefer taking another occasion to speak on this subject', 'will remain here continuing our investigations and awaiting further orders', 'Clingman Hoke Hunton', 'Gracie Corse Clingman Hoke'],
 'U7 5759/0': ['between this point and the White House', 'were sent from Lee\'s army at Richmond to reinforce Jones', 'dismounted cavalry to Gordonsville', 'rebel cavalry under Hampton and Fitz Lee', 'Picketts old division or a part of it', 'went either by the canal to', 'by way of Lynchburg to Charlottesville'],
 'U9 5902/0': ['It is impossible that the troops in his front may receive', 'wished me to press upon General Schofield the importance of his advance', 'I have the honor to be very respectfully your obedient servant', 'press upon General Schofield'],
 'U1 5568/0 (clear 10167)': ['conveyance of intelligence has been the cause of want of success', 'I will telegraph farther after examination of the papers'],
 'U2 5575/0 (clear 4483)': ['in case of disaster to receive prisoners or to cover retreat is this approved'],
 'U8 5842/0 (clear 7666)': ['I have no doubt they are all safely off', 'ten of whom were by the shells of the navy on our picket line near the fort'],
 'U10 5914/0 (clear 8602)': ['behind Town Creek where they propose to make a stand', 'only four brigades of my troops have arrived from Wilmington', 'a small force could have held them until their supplies were exhausted'],
}
texts = {}
for p in sorted(glob.glob(os.path.join(D, '*_djvu.txt.gz'))):
    texts[os.path.basename(p)[:-12]] = norm(gzip.open(p, 'rt', errors='ignore').read())
print('volumes searched:', len(texts))
for e, phs in PH.items():
    for ph in phs:
        hits = [v for v, t in texts.items() if norm(ph) in t]
        print(e, '|', ph, '|', ','.join(hits) or 'none')

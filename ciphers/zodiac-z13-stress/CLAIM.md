# The claim under test (a forum post quoted by the owner, 24 Sept 2026; poster not named)

Title: Possible Z13 solution: ARTHUR LA -- looking for people to stress-test this

I've been working on the Zodiac Killer's 13-character "My Name Is" cipher (Z13), and I've found a physical typewriter/keyboard interpretation that gives me: ARTHUR LA. I'm not claiming this proves Arthur Leigh Allen was the Zodiac. I'm posting because I want people who know the ciphers to try to break the actual mechanism.

My starting idea came from the words "MY NAME IS". I wondered whether the cipher might involve typing/typewriter movement, so I started treating the typewriter keyboard as a physical board. Viewed from the typist's position:

    Q W E R T Y U I O P
    A S D F G H J K L
    Z X C V B N M

The top row is physically away from the typist. I treat Q and M as the opposite endpoints of the letter board. For the reverse phase, the continuous track is: M N B V C X Z L K J H G F D S A P O I U Y T R E W Q

Opening: ART. I treat the first A as the anchor/start: A = A. Moving physically upward from A gives W. I then pass one key and take the next: A -> W -> pass E -> R. From E, continue on the upper row using the same pass-one/take-next idea: E -> pass R -> T. So the opening gives: ART.

Middle: HUR. Starting from the N, the repeated 8-like symbols are treated as eight-count operations in the reverse direction. Count the starting key as 1: N1 B2 V3 C4 X5 Z6 L7 K8. This lands exactly on K, which is also a literal character appearing in this section of Z13. Then pass one and take the next: K -> pass J -> H. Now repeat exactly the same operation from H: H1 G2 F3 D4 S5 A6 P7 O8; O -> pass I -> U. Repeat from U: U1 Y2 T3 R4 E5 W6 Q7. Q is the absolute endpoint. There is still one count remaining, so the physical direction reverses at the boundary: Q -> W8. Then use the same pass-one/take-next rule: W -> pass E -> R. That produces: HUR. So: ART + HUR = ARTHUR.

Final NAM. After reaching the Q boundary during the final eight-count, the direction has been restored to the normal/upward orientation. For the final N: N -> J -> pass K -> L. A remains the anchor A: A = A. M is the terminal endpoint of the physical board and is also the final character of Z13, so the procedure terminates there. That leaves: LA. Full result: ARTHUR LA.

Why I think this is worth testing: what interests me isn't simply that "Arthur" can somehow be extracted from 13 characters. It's that the operations are sequential. N + eight-count -> K; K -> H. H + eight-count -> O; O -> U. U + eight-count -> Q boundary -> W; W -> R. The output of one operation becomes the input to the next. I'm not independently selecting H, U and R. I've also tried changing nearby assumptions (direction, boundary handling, counting conventions) and those changes generally destroy HUR rather than producing another comparable name. A secondary observation: with Q and M as the two endpoints of a 26-letter board, there are 24 interior letters, while the cipher contains three repeated 8-like symbols: 8 + 8 + 8 = 24. I don't use that to construct the solution.

The obvious historical significance is that ARTHUR LA corresponds naturally to Arthur Leigh Allen. That does not establish that Allen was the Zodiac, and it doesn't by itself prove this was Zodiac's intended Z13 solution. What I'd really like is for people to attack the mechanics. Can anyone keep the original Z13 unchanged, use a comparably consistent physical typewriter/keyboard interpretation, process it sequentially, and produce a different coherent name? And more importantly: where exactly does this mechanism fail?

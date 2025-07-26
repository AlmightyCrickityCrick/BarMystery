label beginning:
    scene yuki_sofa with fade
    "She sat on a worn leather barstool in the corner of a dimly lit lounge."
    "The air smelled of whiskey, wood, and something older—like dust and time. "
    hide scene yuki_sofa  
    jump sofa
label sofa:
    scene sofa with fade 
    show yuki_mouth at right ease in
    "Yuki opened her eyes."
    "Everything felt familiar but twisted, like a dream she had dreamed too many times."
    hide yuki_mouth
    show yuki at right with fade 
    yuki_mouth "Where... am I?"
    show bartender at left with moveinleft
    "Before she could question further, a gruff voice called out from the bar."
    hide bartender with Dissolve(0.5)
    show bartender_talk at left 
    bartender_talk "What's wrong with you these days? "
    bartender_talk "You fell asleep again."
    bartender_talk "I had to do all the hard work."
    hide bartender_talk with moveoutleft
    hide yuki with fade
    hide scene sofa with fade
    jump bar
label bar:
    scene bar
    show polish_glass at right
    "Beside the counter stood an bartender, motionless except for his hand slowly polishing a glass."
    show yuki with moveinleft
    hide polish_grass
    "His face was lined with age and stories, his gaze unreadable."
    show pouring_wine at right
    "He began to prepare an elegant cocktail in reddish colors, the taste of which I could already feel on my lips."
    hide pouring_wine
    hide yuki
    show bartender_talk at left
    show yuki_drink at right

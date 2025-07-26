label beginning:
    scene yuki_sofa with fade
    "She sat on a worn leather barstool in the corner of a dimly lit lounge."
    "The air smelled of whiskey, wood, and something older—like dust and time. "
    hide scene yuki_sofa  
    jump sofa
label sofa:
    scene sofa with fade 
    show yuki_mouth at right with fade 
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
    hide yuki 
    hide scene sofa with fade
    jump bar
label bar:
    scene bar
    show polish_glass at right
    "Beside the counter stood an bartender, motionless except for his hand slowly polishing a glass."
    show yuki at left with moveinleft
    polish_glass "You look like you would rather go for something strong today,Yuki."
    hide polish_glass with Dissolve(0.5)
    show pouring_wine at right
    "His face was lined with age and stories, his gaze unreadable."
    
    "He began to prepare an elegant cocktail in reddish colors, the taste of which I could already feel on my lips."
    
    hide yuki with Dissolve(0.5)
    hide pouring_wine
label menu1:
    scene bar
    



    menu:
        "Go to the old bartender":
            "Yuki blinked. She didn\'t remember walking in, let alone sitting down."
            
            
            jump bar2
            hide scene bar
        "Try to exit the bar":
            scene dooropen
            show yuki at center
            "Clearly Yuki already stands at the door but…"
            
            "Before she can grab the doorknob, a shiver runs down her spine."
            "In the end…"
            hide yuki
            show scared2 at center
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide white
            hide scared2
            show yuki_scared at center
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide white
            show white with Dissolve(0.1)
            hide scene dooropen with Dissolve(0.1)
            hide white
            hide yuki_scared 
            show black with Dissolve(1.0)
            hide black with fade
            hide black
            jump menu1 

label bar2:
    scene bar1
    show yuki at left
    show pouring_wine at right

    "The bartender placed a dark crimson drink in front of her, the liquid swirling strangely. It shimmered, like blood and starlight mixed together."
    
    "\"I shouldn't... Should I? But why not? What could possibly happen…right?\""
    
    hide yuki
    hide pouring_wine
    show yuki_drink at left
    show bartender at right
    "She lifted the glass and drank."
    "The taste was sweet and bitter all at once. It clawed down her throat and lit a fire in her chest. "
    "The room pulsed. Her heartbeat slowed. Her vision shimmered like glass in the rain."
    hide bartender
    hide yuki_drink
    show yuki at left
    show bartender_talk at right
    bartender_talk "Now that you've refreshed a bit, you should get to work. "
    bartender_talk "DejaVu doesn’t run on lazy people."

    "\"DejaVu? Is this the bar’s name?\""

    hide bartender_talk
    show bartender_talk at right

    bartender_talk "You can start by cleaning the mess from the tables."
    "His smile is thin, polite. But there’s a weight behind it—like it’s not really a question."
    "Yuki looks at him, fingers still warming around the empty glass."

    "\"Help clean? What even is this place...?\""
label clean:
    menu:
        "Agree to help":
            "Yuki gives a slow nod."
            yuki "Alright... I’ll help."
            "The bartender’s face lights up—genuinely, this time."
            hide yuki
        "Refuse to help":
            hide yuki
            show yuki_angry_talk at left
            yuki "I’m not cleaning tables. I don’t even know why I’m here."
            "The bartender’s smile fades."
            bartender_talk "That so?"
            "He leans in slightly, voice sharpening."
            bartender_talk "Getting cheeky, are we? No cleaning, no room."
            bartender_talk "You’ll spend the night out here, in the dark, with the things that crawl in when the doors close."
            hide yuki_angry_talk
            show scared2 at left 
            "Yuki feels a cold prickle on the back of her neck. She swallows."
            "\"Okay... definitely not just a dream.\""
            yuki "...Fine. I’ll do it."
            "His face relaxes."
            bartender_talk "That’s more like it. You’ll thank me later."
            hide scared2

    show yuki at left
    
    "He tosses her a rag and nods toward the tables scattered with dusty glasses, napkins, and ashtrays."
    
    
    jump start3

    
label day1:
    scene bedroom
    show yuki at center
    "The room was small. Dusty. Timeworn. A single lamp buzzed overhead. A bed, untouched. A mirror, cracked. And on the desk..."

    "A journal."
    "Its leather cover was cracked, the pages yellowed."

    yuki " Whose is this?"
    "The first page was blank."
    "Then, as she flipped, words began to appear, ink flowing across the paper like blood from a fresh wound: \“Dear Yuki...\” "
    "Her hands trembled."
    yuki " What the hell is this...?"
    "Her breath caught."
    "And as her eyes moved across the page, she felt something stirring inside her. "
    "Something old. "
    "Something broken…"
    
    jump chapter_2_start
    return


label start:
    scene black
    "Darkness"
    "Silence"
    "The hum of memory just beyond reach"
    scene bar_yuki_kai 
    show white with Dissolve(0.1)
    hide white 
    hide bar_yuki_kai
    show bar
    show yuki_angry_talk at Position(xpos = 1600, ypos = 1080)
    show kai_inv at Position(xpos = 400, ypos = 1080)
    show white with Dissolve(0.1)
    hide white 
    hide bar
    show bar 
    show yuki at Position(xpos = 1600, ypos = 1080)
    show white with Dissolve(0.1)
    hide white
    hide yuki
    hide bar
    show bar
    show yuki_scared at Position(xpos = 1600, ypos = 1080)
    show white with Dissolve(0.1)
    hide white
    hide bar
    show bar
    show black
    show white with Dissolve(3.0)
    "Then..light"
    
    "A flicker"
    "A breath"
    hide white 

    jump beginning
    return

label beginning:
    scene bar

    show yuki at Position(xpos= 300, ypos= 1500)
    scene yukisleepbar
    "She sat on a worn leather barstool in the corner of a dimly lit lounge."
    "The air smelled of whiskey, wood, and something older—like dust and time. "

    scene yukiawakebar
    "Yuki opened her eyes."
    "Everything felt familiar but twisted, like a dream she had dreamed too many times."
    yuki "Where... am I?"
    "Before she could question further, a gruff voice called out from the bar."

    scene bar1
    show ob at Position(xpos= 300, ypos= 1500)
    ob "What's wrong with you these days? "
    ob "You fell asleep again."
    ob "I, an old man, had to do all the hard work."
    "Beside the counter stood an old bartender, motionless except for his hand slowly polishing a glass."
    "His face was lined with age and stories, his gaze unreadable."
    
    scene obpourdrink1
    "He began to prepare an elegant cocktail in reddish colors, the taste of which I could already feel on my lips."
    menu:
        "Go to the old bartender":
            "Yuki blinked. She didn’t remember walking in, let alone sitting down."
            "Still, her throat felt dry. Without replying, she nodded."
            ob "After all, you can never resist my mastery of making drinks."
        "Try to exit the bar":
            scene dooropen
            show yuki at Position(xpos= 400, ypos= 1300)
            "Clearly Yuki already stands at the door but…"
            hide yuki
            show yuki_scared at Position(xposs= 400, ypos= 1300)
            "Before she can grab the doorknob, a shiver runs down her spine."
            "In the end…"
            scene bar1
            show yuki at Position(xpos= 400, ypos= 1300)
            show obpourwine2
            "She still chooses to go to the bartender."
    
            ob "You left all the work to me and you still want to leave? How come?"
            yuki "That…ohh…I…"



    jump chapter_2_start
    return
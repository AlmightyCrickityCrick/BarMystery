
define yuki = Character(name = "Yuki", color = "#66417fff")
define kai = Character(name = "Kai", color = "#020a52ff")
define bartender = Character(name = "Bartender", color = "#f85205ff")





image bartender = im.Scale("bartender.png", 700, 1000)
image yuki_scared = im.Scale("yuki scared.png", 600, 900)
image yuki_desperated = im.Scale("desperated.png", 600, 900)

image yuki_scared = im.Scale("yuki scared.png", 600, 900)
image bar1 = im.Scale("bar1.jpg", 1920, 1080)



image bar = im.Scale("bar.png", 1920, 1080)
image black = im.Scale("black.jpeg", 1920, 1080)
image white = im.Scale("white.jpeg", 1920, 1080)
image bar_yuki_kai = im.Scale("bar yuki kai.png", 1920, 1080)
image kai_png = im.Scale("kai.png", 600, 900)

image room = im.Scale("room.jpg", 1920, 1080)

image yuki_angry_talk = im.Scale("angry talk.png", 700, 1000)
image kai_inv = im.Scale("kai inverted.png", 700, 1000)
image kai_png = "kai.png"
image yuki_scared = im.Scale("yuki scared.png", 700, 1000)


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
    scene bar
    show black
    show white with Dissolve(3.0)
    "Then..light"
    hide scene bar
    "A flicker"
    "A breath..."
    hide white with fade

    jump beginning
    return









    
    
    
    
    

    

    
    
    
    
    
    
    
    
    
    menu:
        "Go to the old bartender":
            "Yuki blinked. She didn\'t remember walking in, let alone sitting down."
            "Still, her throat felt dry. Without replying, she nodded."
            ob "After all, you can never resist my mastery of making drinks."
        "Try to exit the bar":
            scene dooropen
            show yuki at center
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

    scene bar1

    show yuki at left
    show obpourdrink3 at right

    "The bartender placed a dark crimson drink in front of her, the liquid swirling strangely. It shimmered, like blood and starlight mixed together."
    
    "\"I shouldn't... Should I? But why not? What could possibly happen…right?\""
    
    hide yuki
    show yukidrink at left
    hide obpourdrink3
    show ob at right

    "She lifted the glass and drank."
    "The taste was sweet and bitter all at once. It clawed down her throat and lit a fire in her chest. "
    "The room pulsed. Her heartbeat slowed. Her vision shimmered like glass in the rain."
    
    hide yukidrink
    show yuki at left

    ob "Now that you've refreshed a bit, you should get to work. "
    ob "DejaVu doesn’t run on lazy people."

    "\"DejaVu? Is this the bar’s name?\""

    hide ob
    show obcarpa at right

    ob "You can start by cleaning the mess from the tables."
    "His smile is thin, polite. But there’s a weight behind it—like it’s not really a question."
    "Yuki looks at him, fingers still warming around the empty glass."

    "\"Help clean? What even is this place...?\""

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
            ob "That so?"
            "He leans in slightly, voice sharpening."
            ob "Getting cheeky, are we? No cleaning, no room."
            ob "You’ll spend the night out here, in the dark, with the things that crawl in when the doors close."
            hide yuki_angry_talk
            show yuki_desperated
            "Yuki feels a cold prickle on the back of her neck. She swallows."
            "\"Okay... definitely not just a dream.\""
            yuki "...Fine. I’ll do it."
            "His face relaxes."
            ob "That’s more like it. You’ll thank me later."
            hide yuki_desperated

    show yukicarpa at left
    
    "He tosses her a rag and nods toward the tables scattered with dusty glasses, napkins, and ashtrays."
    
    
    #MINIGAME

    hide yukicarpa

    scene room
    show yukispate at center
    "At the top, a long hallway with flickering lamps greeted her. Every door was shut—except one."
    "She entered."
    
    scene bedroom
    show yukispate at center
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

define yuki = Character(name = "Yuki", color = "#66417fff")
define kai = Character(name = "Kai", color = "#020a52ff")
define ob = Character(name = "Bartender", color = "#f85205ff")
image yuki = "Yuki.png"
image bar_side = im.Scale("bar side.png", 1920, 1080)
image bar_counter = im.Scale("bar counter.png", 1920, 1080)
image ob = im.Scale("ob.png", 700, 1000)
image yuki_scared = im.Scale("yuki scared.png", 734, 1000)
image bar1 = im.Scale("bar1.jpg", 1920, 1080)

define old_bartender = Character(name = "Old bartender", color = "#66417fff")


image bar = im.Scale("bar.png", 1920, 1080)
image black = im.Scale("black.jpeg", 1920, 1080)
image white = im.Scale("white.jpeg", 1920, 1080)
image bar_yuki_kai = im.Scale("bar yuki kai.png", 1920, 1080)
image yuki_angry_talk = im.Scale("angry talk.png", 700, 1000)
image kai_inv = im.Scale("kai inverted.png", 700, 1000)
image kai_png = "kai.png"
image yuki_scared = im.Scale("yuki scared.png", 700, 1000)
image yukisleepbar = im.Scale("yukisleepbar.jpg", 1920, 1080)
image yukiawakebar = im.Scale("yukiawakebar.jpg", 1920, 1080)
image obatthebar = im.Scale("obatthebar.png", 700, 1000)
image obpourdrink1 = im.Scale("obpourdrink1.jpg", 1920, 1080)
image dooropen = im.Scale("dooropen.jpg", 1920, 1080)

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
    #show bar 
    "A flicker"
    "A breath"
    hide white 

    jump beginning
    return

label beginning:
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
            show yuki at Position(xpos= 300, ypos= 1500)
            "Clearly Yuki already stands at the door but…"
            "Before she can grab the doorknob, a shiver runs down her spine."
            "In the end…"
            scene bar1
            show yuki at Position(xpos= 300, ypos= 1500)
            "She still chooses to go to the bartender."
            ob "You left all the work to me and you still want to leave? How come?"
            yuki "That…ohh…I…"




    return
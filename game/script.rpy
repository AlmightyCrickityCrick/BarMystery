
define yuki = Character(name = "Yuki", color = "#66417fff")
define kai = Character(name = "Kai", color = "#020a52ff")
define bartender = Character(name = "Bartender", color = "#f85205ff")
image yuki = im.Scale("yuki.png", 600, 900)
define ob = Character(name = "Bartender", color = "#f85205ff")
image yuki = "Yuki.png"
image bar_side = im.Scale("bar side.png", 1920, 1080)
image bar_counter = im.Scale("bar counter.png", 1920, 1080)
image bartender = im.Scale("bartender.png", 700, 1000)
image yuki_scared = im.Scale("yuki scared.png", 600, 900)
image yuki_desperated = im.Scale("desperated.png", 600, 900)
image ob = im.Scale("ob.png", 700, 1000)
image yuki_scared = im.Scale("yuki scared.png", 734, 1000)
image bar1 = im.Scale("bar1.jpg", 1920, 1080)
image obpourwine2 = im.Scale("obpourwine2",600, 900)
image obpourdrink2 = im.Scale("obpourdrink2.png", 600, 900)
image yukidrink = im.Scale("yukidrink.png", 600, 900)

define old_bartender = Character(name = "Old bartender", color = "#66417fff")


image bar = im.Scale("bar.png", 1920, 1080)
image black = im.Scale("black.jpeg", 1920, 1080)
image white = im.Scale("white.jpeg", 1920, 1080)
image bar_yuki_kai = im.Scale("bar yuki kai.png", 1920, 1080)
image kai_png = im.Scale("kai.png", 600, 900)
image hall = im.Scale("hall.jpg", 1920, 1080)
image room = im.Scale("room.jpg", 1920, 1080)

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
    
    "A flicker"
    "A breath..."
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
            show at left ob 
            ob "After all, you can never resist my mastery of making drinks."
        "Try to exit the bar":
            scene dooropen
            show yuki at Position(xpos= 700, ypos= 1700)
            "Clearly Yuki already stands at the door but…"
            hide yuki
            show yuki_scared at Position(xposs= 400, ypos= 1300)
            "Before she can grab the doorknob, a shiver runs down her spine."
            "In the end…"
            scene bar1
            show yuki at Position(xpos= 400, ypos= 1700)
            show obpourwine2 at Position(xpos= 700, ypos=1300)
            "She still chooses to go to the bartender." 
            ob "You left all the work to me and you still want to leave? How come?"
            yuki "That…ohh…I…"

    scene bar1

    show yuki at left
    show ob at right

    "The bartender placed a dark crimson drink in front of her, the liquid swirling strangely. It shimmered, like blood and starlight mixed together."
    
    "\"I shouldn't... Should I? But why not? What could possibly happen…right?\""
    
    "She lifted the glass and drank."
    "The taste was sweet and bitter all at once. It clawed down her throat and lit a fire in her chest. "
    "The room pulsed. Her heartbeat slowed. Her vision shimmered like glass in the rain."
    
    ob "Now that you've refreshed a bit, you should get to work. "
    ob "DejaVu doesn’t run on lazy people."

    "\"DejaVu? Is this the bar’s name?\""

    ob "You can start by cleaning the mess from the tables."
    ob "His smile is thin, polite. But there’s a weight behind it—like it’s not really a question."
    ob "Yuki looks at him, fingers still warming around the empty glass."

    "\"Help clean? What even is this place...?\""






    return
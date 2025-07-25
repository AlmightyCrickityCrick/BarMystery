define yuki = Character(name = "Yuki", color = "#66417fff")
image yuki = im.Scale("Yuki.png", 700, 1000 )

image bar = im.Scale("bar.png", 1920, 1080)
image black = im.Scale("black.jpeg", 1920, 1080)
image white = im.Scale("white.jpeg", 1920, 1080)
image bar_yuki_kai = im.Scale("bar yuki kai.png", 1920, 1080)
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
    scene bar

    show yuki at Position(xpos= 300, ypos= 1500)
    "Ce faci"
    return
define yuki = Character(name = "Yuki", color = "#66417fff")
define kai = Character(name = "Kai", color = "#020a52ff")
define bartender = Character(name = "Bartender", color = "#f85205ff")
image yuki = "Yuki.png"
image bar_side = im.Scale("bar side.png", 1920, 1080)
image bar_counter = im.Scale("bar counter.png", 1920, 1080)
image bartender = im.Scale("bartender.png", 700, 1000)
image yuki_scared = im.Scale("yuki scared.png", 734, 1000)
image

image bar = im.Scale("bar.png", 1920, 1080)
image black = im.Scale("black.jpeg", 1920, 1080)
image white = im.Scale("white.jpeg", 1920, 1080)
image bar_yuki_kai = im.Scale("bar yuki kai.png", 1920, 1080)
image yuki_angry_talk = im.Scale("angry talk.png", 734, 1000)
image kai_inv = im.Scale("kai inverted.png", 734, 1000)
image kai_png = "kai.png"
image yuki_sad = "yuki scared.png"


label start:
    scene black
    "Darkness"
    "Silence"

    scene bar_yuki_kai 
    show white with Dissolve(0.2)
    hide white 
    hide bar_yuki_kai
    show bar
    show yuki_angry_talk at Position(xpos = 1600, ypos = 1080)
    show kai_inv at Position(xpos = 400, ypos = 1080)
    show white with Dissolve(0.2)
    hide white 
    hide bar
    show bar 
    show yuki at Position(xpos = 1600, ypos = 1080)
    show white with Dissolve(0.2)
    hide white
    hide yuki
    hide bar
    show bar
    show yuki_scared at Position(xpos = 1600, ypos = 1080)
    show white with Dissolve(0.2)
    hide white
    hide bar
    show bar
    show black 
    show white with Dissolve(0.2)
    hide white
    


    jump beginning

label beginning:
    scene bar

    show yuki at Position(xpos= 300, ypos= 1500)

    return
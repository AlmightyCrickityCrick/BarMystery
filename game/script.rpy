﻿
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
    play music "ambience.ogg" fadein 0.5
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
    stop music fadeout 0.5
    jump beginning
    return
    
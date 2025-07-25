image desk = im.Scale("desk.png", 1920, 1080)
image banana = im.Scale("banana.png", 600, 500)
image farfurie = im.Scale("farfurie.png", 500, 300)
image cana = im.Scale("cana.png", 400, 400) 
image hartie = im.Scale("hartie.png", 300, 200)
image memories = im.Scale("memories.png", 300, 400)

init python:
    points = 0
    objects = ["banana", "cana", "farfurie", "hartie", "memories"]
    clicked = []

    # pozițiile fixe inițiale
    object_positions = {
        "banana": (700, 600),
        "cana": (300, 300),
        "farfurie": (1200, 300),
        "hartie": (850, 100),
        "memories": (500, 50)
    }

screen click_game():

    text "Points: [points]" xpos 0.05 ypos 0.05 size 40 color "#FFFFFF"

    for obj in objects:
        if obj not in clicked:
            python:
                x, y = object_positions[obj]
            imagebutton:
                idle obj
                xpos x
                ypos y
                action [
                    SetVariable("points", points + 1),
                    SetVariable("clicked", clicked + [obj])
                ]

label start3:
    $ import random

    python:
        global object_positions

        positions = list(object_positions.values())

        random.shuffle(positions)

        new_positions = {}
        for i, obj in enumerate(objects):
            new_positions[obj] = positions[i]

        object_positions.clear()
        object_positions.update(new_positions)

    $ points = 0
    $ clicked = []

    scene desk
    "Click all 5 objects to win!"
    show screen click_game

    while len(clicked) < len(objects):
        $ renpy.pause(0.1)

    hide screen click_game
    "You did it!"
    return

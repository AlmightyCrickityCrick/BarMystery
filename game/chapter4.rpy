label chapter_4_piano:

    scene hall
    with fade
    show yuki at center with moveinright

    "Yuki wanders through the bar’s dim hallways again."

    "She feels drawn toward something—but can’t tell what. The air is heavy, like it remembers too much."

    "As she approaches the lounge area, a sound slips through the silence."

    play music "sad piano.ogg" noloop 

    "A piano plays. Not perfectly. Stumbling, hesitant… like someone relearning an old memory."

    "It comes from behind the old curtains."

    "She hesitates."

    menu:
        "Go toward it":
            jump piano_room
        "Walk away":
            jump walk_away

label walk_away:
    show yuki at center with fade
    "She turns, heart racing."

    stop music fadeout 1.0

    "But as she steps away, she hears the music suddenly stop."

    "Silence crushes her. Something feels… wrong. Lost."

    play music "creepy.ogg"  fadein 0.5 fadeout 0.5

    kai "You always walk away before the truth."

    "Yuki returns, now shaken."

    jump piano_room

label piano_room:

    scene piano
    with fade
    show yuki at center with moveinleft

    "Yuki slips behind the curtains."

    
    "A dusty piano stands in the half-light."

    menu:
        "Something romantic":
            $ selected_song = "romantic"
            jump play_song
        "Haunting classical eerie and melancholic":
            $ selected_song = "classical"
            jump play_song
        "Dark jazz/blues moody and soulful":
            $ selected_song = "jazz"
            jump play_song

label play_song:

    if selected_song == "romantic":
        play music "despair.ogg"
        "Soft and familiar. She hums along without realizing."
        "A tear slips down her cheek—her body remembers even if her mind doesn’t."
        "The melody is haunting. Her heart aches."
        "A sudden flash of a memory:\nA boy smiling… a promise… the sound of rain."
        "A strange, dissonant tune fills the room. It sounds broken—but real."
        "The air shifts. Her reflection in the piano lid looks… older."
    elif selected_song == "classical":
        play music "strange.ogg"
        "The piano moans with age. Cold and clear."
        "Yuki’s hands tremble, but the song plays through her."
        "Images flicker: running in the dark, a hospital hallway, silence."
        "The piano echoes long after she stops."
    elif selected_song == "jazz":
        play music "eerie guitar.ogg"
        "The keys groan with rhythm and sorrow."
        "She feels detached, but every note lands in her chest."
        "Something about it feels real — like someone else's pain in her hands."

    jump journal_scene

label journal_scene:

    scene bedroom
    with fade
    show yuki at center with moveinright


    "She rushes upstairs."


    "Her journal lies on the bedside table, untouched—but now, a new page glows faintly."

    show screen journal
    'Words are scribbled as if written in a dream'
    $ textjurnal ='\nI waited every night. I couldn’t leave. I couldn’t forget.' 
    yuki 'Oh... That was him... My dear one.'
    $ textjournal ='\nNot until he walked through that door again… But he never did.'

    "Yuki gasps."

    "She starts to remember small pieces of her memory."

    "Not him waiting for her—but her waiting for him."
    hide screen journal

    menu:
        "Accept and dive deeper":
            jump journal_accept
        "Close the journal":
            jump journal_refuse

label journal_accept:

    scene white
    play music 'ambient.ogg' fadein 0.5 fadeout 0.5

    "The journal burns bright. Her vision blurs. Time folds."
    scene fire
    with Dissolve(2.0)

    stop music fadeout 1.0

    jump the_truth

label journal_refuse:

    show kai_inv at right with fade
    "The glow fades. The room darkens."

    kai "You’re not ready yet."

    "She lies back down. The day resets."
    hide kai

    jump chapter_4_piano



label the_truth:

    scene bar
    with fade
    show yuki at center with moveinleft

    stop music fadeout 1.5

    "A heavy silence filled the air."

    "The bar was empty now, save for Yuki and the faint echo of the piano’s last notes."

    "She knew—something had to be uncovered. The truth was close, just beyond her reach."

    show yuki at center

    yuki "I can’t keep running from this."
    yuki "I have to find out who I really am…"

    menu:
        "Search the hidden room with the key":
            jump hidden_room_path
        "Confront the old bartender about the memories":
            jump confront_bartender
        "Try to play the piano melody again to unlock the truth":
            jump play_piano_final

label hidden_room_path:

    scene hall
    show yuki at center with fade
    "Yuki walked down the hallway, the key warm in her hand."
    "The door creaked open."

    "Inside, the room was cluttered with fragmentfs of forgotten memories: photographs, letters, a cracked mirror."

    yuki "This... this is me. And him."
    yuki "Who were we?"

    scene bar_yuki_kai 
    with fade

    menu:
        "Read the letters carefully":
            jump read_letters
        "Look into the cracked mirror":
            jump look_mirror

label read_letters:
    scene bedroom
    show yuki_desperated at center with fade
    show script at center

    "She read the letters. They spoke of loss, longing, and a promise broken by tragedy."
    "The boy had written: 'If I’m gone, remember the tune.'"
    'This is....... Kai?'

    jump embrace_or_resist

label look_mirror:
    "She looked into the cracked mirror. Her reflection shimmered—two sets of eyes stared back."
    yuki "You were always watching… weren’t you?"

    jump embrace_or_resist

label confront_bartender:

    scene bar_counter
    show bartender at left

    "Yuki found the bartender polishing glasses behind the counter."
    "His eyes met hers—calm, knowing."

    yuki "I need answers. Who am I? Why am I trapped here?"

    bartender "Some truths hurt, Yuki. But it’s time you faced them."

    menu:
        "Demand the full story":
            jump bartender_full_story
        "Ask why she’s stuck here":
            jump bartender_why

label bartender_full_story:
    scene bar_side
    with fade
    show yuki at center with moveinleft
    show bartender at right with moveinright
    bartender "You lost everything. Him… yourself. You asked to forget. But forgetting doesn’t heal."

    jump embrace_or_resist

label bartender_why:
    bartender "You’re here because part of you still refuses to let go."

    jump embrace_or_resist

label play_piano_final:

    scene hall
    with fade

    show yuki 
    play music "sad piano.ogg"

    "She sat at the piano, fingers trembling."
    "The notes filled the room—haunting, familiar."
    "The air shimmered, the walls faded away."

    yuki "It’s all coming back…"

    jump embrace_or_resist_piano


label embrace_or_resist:
    menu:
        "Yes":
            jump ending_a
        "No":
            jump ending_b

label embrace_or_resist_piano:
    menu:
        "Yes":
            jump ending_a
        "No":
            jump ending_c



label ending_a:

    stop music fadeout 2.0
    scene white
    show yuki at center with fade
    with Dissolve(3.0)

    "Yuki uncovers her past: a tragic love story, a terrible loss, and her own choice to forget to survive."

    "The memories flood in—but she accepts them."

    "The bar fades. She is free at last."

    yuki "I remember now... and I forgive myself."

    return

label ending_b:

    stop music fadeout 1.5
    scene side_bar
    show yuki at center with fade
    with Dissolve(3.0)

    "Yuki faces the harsh truth—but cannot forgive herself."

    "She remains trapped, the bar a purgatory for lost souls like her."

    yuki "Maybe someday... I’ll find peace."

    return

label ending_c:

    stop music fadeout 1.5
    scene black
    with fade

    "Yuki denies the memories. The piano falls silent. The bar resets."

    "She is doomed to live the same day, forgetting, lost forever."

    yuki "The truth waits... but not for me."

    jump the_truth  # Optional: reset loop
    return
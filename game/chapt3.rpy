label deja_vu_start:

    scene bar_counter
    with fade

    show yuki at center  

    "Yuki opened her eyes again. Third time."
    "The bar was silent. Early morning dust hung in the air like a second breath."

    yuki "Still here… Still Déjà Vu…"

    show bartender at left

    bartender "You’re getting used to this place, huh?"
    bartender "Well, don’t get too comfy. Work doesn’t do itself."

    "He threw her a rag without even looking."

    bartender "The counters, the bottles, the floors. Take your pick."

    show yuki tired at center
    yuki "Fine... Let’s get it over with."

    "Her fingers curled around the damp cloth. Same motions. Same silence. Something in the air felt different, though."

    "As she wiped down the sticky countertop, a small group of regulars gathered in the corner booth."

    "Cards shuffled. Dice clinked. Cigarette smoke rose like ghosts from their mouths."

    "Then—something strange."

    play sound "scary.ogg" fadein 0.5 fadeout 0.5

    "A low mechanical click."

    show emma at right  

    "She turned to see a strange woman in a pale suit placing something on the table: a worn key."

    hide emma

    "Yuki blinked. It wasn’t there a second ago."
    "The woman vanished the moment Yuki turned away. No goodbye. No trace."

    yuki "Did anyone else see…?"

    bartender "See what?"

    "She walked over to the booth. The key was still there, cold in her hand. Faded engraving: '206'."

    "But there were no room numbers in Déjà Vu. Not that she’d seen."

    menu:
        "What will Yuki do?":
            "Take the key":
                jump take_key
            "Leave the key":
                jump leave_key

label take_key:

    $ has_key = True

    yuki "Fine. Let’s see what this is about."

    "She decides to keep cleaning upstairs."
    "A moment later, the hallway shimmered again."
    "Another door was open now—one she hadn’t noticed before. Room 206. Faint light glowed through the crack."

    menu:
        "Do you enter the room?":
            "Enter Room 206":
                jump enter_room
            "Walk past the door":
                jump walk_past

label enter_room:

    scene bg_room206  # 🔶 Background for Room 206
    with fade

    "She stepped forward, key clenched tight."
    "The doorknob turned with a whisper. The air inside was colder."

    "The walls were covered in drawings—crude sketches of a little girl, alone in a room, always watched through a window."

    show music_box on dresser  # 🔶 Image of music box

    "There was a music box on the dresser."

    play sound "musicbox.ogg"  # 🔶 Creaky music box sound

    "She wound it. The melody was distant, broken."
    "Yuki held it up. Something fluttered inside her chest."

    yuki "Why does this… feel so…"

    "A soft glow filled the locket. A piece of a memory. She didn’t recognize it. But it hurt."

    "★ She had collected a memory fragment."

    scene bg_hallway  # 🔶 Back to hallway
    with fade

    "Yuki walks slowly back to her room, the old music box cradled gently in her hands."

    "The hallway is quieter now, but something lingers in the air — a hum, almost like a memory trying to surface."

    scene bg_yuki_room
    with dissolve

    "As she closes the door behind her, a soft chime escapes from the box, echoing faintly through the room."

    play sound "chime.ogg"  # 🔶 Optional sound

    "Without being prompted, the journal on the table flips open. Ink bleeds across the page like it's being written in real time."

    show journal_open  # 🔶 Image of open journal

    "Journal:\n\"There was a boy... a boy who always hummed the same tune every time he walked past me. I never dared ask him the name of the song. I wonder if he ever knew I noticed.\""

    "The melody coming from the music box matches the one in the memory."

    yuki "Why do I remember this now...? Who was he?"

    return

label walk_past:

    yuki "Nope. Not falling for that again."
    yuki "Just because a door opens, doesn’t mean you should walk through it."

    "She kept cleaning. The key remained cold in her pocket."
    "The hallway flickered once. The door closed on its own."

    scene bg_yuki_room
    with dissolve

    "Yuki sits down on the bed, exhausted. The journal stays closed."

    "She flips through the empty pages, but they remain blank — unresponsive."

    yuki "Why won’t you show me more...? Was I supposed to find something?"

    "A faint message is now scribbled on the journal:\n\"Try again.\""

    return

label leave_key:

    $ has_key = False

    "Yuki hesitates, staring at the small brass key tucked inside the music box."

    "Something about it feels… too deliberate, too staged."

    "She decides to leave the key untouched."

    "As she stands in the middle of the room, the air seems to grow heavier."

    voice "Some doors only open when you're ready to face what\'s behind them."

    play sound "tick_tock.ogg"

    scene black with fade

    "You wake up at the bar. The day begins again."

    jump 

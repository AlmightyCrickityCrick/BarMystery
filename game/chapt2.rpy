default textjurnal=""
label chapter_2_start:
    play music 'despair.ogg' fadein 1.0 fadeout 2.0
    scene bar
    show yuki at left with fade
    'Yuki opened her eyes to the familiar scent of aged wood and citrus cleaner. She was still here. Still in Déjà Vu.'
    yuki '\"So it was not a dream...\"'
    show bartender at right with moveinright
    stop music fadeout 1.0
    bartender 'Ah, you\'re awake. Hope you slept well. I could use an extra pair of hands downstairs. You up for helping around the bar today?'
    menu optional_name:
        'Nod and agree to help':
            yuki 'I don\'t really understand what\'s going on… but maybe if I stay close, I\'ll learn something.'
            bartender 'Good. Come on, it got lively already.'
        "Shake your head and refuse":
            bartender 'Ahaha...funny.'
            bartender 'You depend on this place and this place depends on you. It wasn\'t a question, dear.'
            hide yuki with Dissolve(0.5)
            hide bartender with Dissolve(0.5)


    
    jump downstairs
    return

label downstairs:
    scene bar1
    show yuki at left with fade
    show bartender at right with moveinright
    'Yuki follows him downstairs'
    
    show bar1

    'As she wipes the bar counter, a man with tired eyes and a broken watch enters. He sits in silence for a moment, then glances at her.'
    show s_stranger at center with moveinright
    bartender 'He comes every night. Never speaks.'
    bartender 'Just stares at that damn watch like he\'s waiting for something that\'ll never return.'
    'Yuki avoids the man, but later finds him staring at her silently.'
    hide bartender with moveoutright
    show s_stranger at center with moveinleft  
    'In the end, Yuki took heart and approached him.'
    s_stranger 'Ever notice how time can feel… frozen? Like no matter how far you walk, you\'re still stuck in the same damn hallway.'
    yuki '...That\'s oddly specific.'
    s_stranger 'I used to live in a house where the walls had ears. You\'d breathe wrong, and the silence would scream back at you.'

    menu:
        'That sounds horrible. What happened?':
            s_stranger 'My father drank memories instead of whiskey, he was never present...
            And my mother... she just watched the my world burn from the kitchen table.
            I ran away so many times I forgot what "home" meant.'
            'I can relate. I feel like I\'m stuck in a loop too.'
            s_stranger 'You ever feel like that?'
            yuki 'I\'m not sure…'
            s_stranger 'This doesn\'t tick anymore, but it remembers. You helped me tonight, even if you didn\'t know how. Take it.'
            'He hands her the broken watch.'
            hide s_stranger with Dissolve(0.5) 
            hide yuki with moveinleft

            jump yuki_room
            return

        'Everyone has problems':
            s_stranger 'Yeah. Guess that\'s what people say when they don’t want to feel too much.
            Never mind.'
            jump yuki_room
            jump no_journal
            return


        'Say nothing, just stare at him':
            s_stranger 'You look like someone who forgot how to cry.'
            'He chuckles bitterly'
            s_stranger 'Thanks for the silence. That\'s more than I used to get.'
            'He gets up and leaves'
            hide s_stranger with Dissolve(0.5)




            jump yuki_room
            yuki 'Still blank. It\'s like it\'s waiting for something...'
            'Let\'s write in journal.. Huh?? Try again'
            yuki 'Memories...?'
            yuki 'What is this place really trying to show me?'
            'She turns off the small lamp and lays back on the bed, eyes staring at the ceiling.'
            yuki 'I feel like Im forgetting something important. But… what?'


            

    return
            

screen journal:
    
    frame:
        background Null()
        add "journal open.png" xsize 800 ysize 1200
        xalign 0.3
        yalign 0
        xsize 200
        ysize 200
    frame:
        background Null()
        add "memories" xsize 200 ysize 200
        xalign 0.4
        yalign 0.17
    vbox:
        box_wrap True
        xmaximum 0.5
    hbox xalign 0.45 yalign 0.5 box_wrap True:
        xmaximum 400
        text textjurnal size 25 color "#000000" ysize 50 

label yuki_room:
    scene bedroom
    show yuki at center with fade
    'Yuki enters her room, exhausted.'
    yuki '\"Ugh... My feet are killing me. I didn\'t think this job would be so tiring.
    That man and his story really drained me too... What was that all about?\"'
    'She sits on the edge of the bed.'
    'The journal lies untouched on the nightstand, just like the night before.'
    yuki ' Huh? What\'s going on...?'
    show screen journal
    'The journal opens on its own. A new page reveals itself, written in trembling ink.'
    $ textjurnal = "I used to speak into silence. \nWords floated like dust in an empty house— \nno one there to catch them.\nNo arms ever reached out. No eyes ever stayed.\nThey were always busy, always tired,\nalways somewhere else.\nAnd I—I learned to shrink.\nTo disappear, so they wouldn’t have to.\nSome nights I’d pretend I was a ghost.\nAt least ghosts get noticed.\nAt least they make things move."
    yuki '\"I can\'t remember the last time I felt this tired. I don\'t know what\'s happening to me, but I feel like I\'m losing myself.\"'
    $ textjurnal = ""
    
#journal entry  
            
label no_journal:
    scene bedroom
    yuki 'Still blank. It\'s like it\'s waiting for something...'
    'Let\'s write in journal.. Huh?? Try again'
    yuki 'Memories...?'
    yuki 'What is this place really trying to show me?'
    'She turns off the small lamp and lays back on the bed, eyes staring at the ceiling.'
    yuki 'I feel like Im forgetting something important. But… what?'
            
            

    return
    



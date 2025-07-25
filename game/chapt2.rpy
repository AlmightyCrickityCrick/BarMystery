

label chapter_2_start:
    scene bar
    show yuki at left with fade
    'Yuki opened her eyes to the familiar scent of aged wood and citrus cleaner. She was still here. Still in Déjà Vu.'
    yuki '\"So it was not a dream...\"'
    show bartender at right with fade
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
    scene bar_side
    show yuki at left
    show bartender at right
    'Yuki follows him downstairs'

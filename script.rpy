
# ==================================================
# CARS N COFFEE
# Full Dialogue Script
# ==================================================

init:
    $ style.default.font = "jp.ttf"
    $ style.default.language = "japanese"
define config.default_text_cps = 35

# CHARACTERS

define niti = Character("Niti", color="#1683e8")
define r34 = Character("Skyline GT-R R34", color="#40aaff")
define m3 = Character("BMW M3 GTR", color="#e34b4b")
define player = Character("[player_name]")

# PLAYER PROFILE

default player_name = "Player"
default player_age = "Not specified"
default player_gender = "Not specified"

# PROGRESS

default achievements = []
default secret_niti = False
default r34_complete = False
default m3_complete = False

# BACKGROUNDS

image bg garage = "images/garage.png"

# NITI SPRITES

image niti_normal = "images/sprite_1.png"
image niti_greeting = "images/sprite_0.png"
image niti_racesuit = "images/sprite_2.png"

# CAR SPRITES

image r34_sprite = "images/skyline.png"
image m3_sprite = "images/m3gtr.png"

init python:
    g = Gallery()
    g.locked_button = "images/lockpad-cropped.png"
    #cg1
    g.button("cg1")
    g.image("images/skyline_artscene.jpg")
    g.condition("persistent.unlock_cg1")
    #cg2
    g.button("cg2")
    g.image("images/m3_gtr_artscene.jpg")
    g.condition("persistent.unlock_cg2")

# ==================================================
# START
# ==================================================

label start:

    scene bg garage
    with fade



    play music "audio/garage_music.ogg" loop fadein 2.0

    show niti_greeting at center
    with dissolve

    niti "Hey! Welcome to Cars n Coffee."

    niti "It's good to have someone new around here."

    niti "I'm Niti. I'll be your guide throughout this little garage."

    niti "Before we start, what's your name?"

    $ player_name = renpy.input("Enter your name:", length=20).strip()

    if player_name == "":
        $ player_name = "Player"

    if player_name.lower() == "niti":

        $ secret_niti = True
        $ achievements.append("SAME NAME")

        niti "Oh, your name is Niti too?"
        niti "That's quite a coincidence."

    else:

        niti "Nice to meet you, [player_name]."

    niti "Let's set up your profile."

    $ player_age = renpy.input("Enter an age range, or leave blank:", length=15).strip()

    if player_age == "":
        $ player_age = "Not specified"

    menu:

        niti "How can I identify you?"

        "Boy":
            $ player_gender = "Boy"

        "Girl":
            $ player_gender = "Girl"

        "Non-binary":
            $ player_gender = "Non-binary"

        "Prefer not to say":
            $ player_gender = "Not specified"

        "Unisex":
            $ player_gender = "Both"

    hide niti_greeting
    show niti_normal
    with dissolve

    niti "Alright."

    niti "Now, let me tell you a little about myself."

    niti "I'm interested in cars, JDM culture, racing and automotive engineering."

    niti "I enjoy learning how engines work, how cars are designed and what makes them special."

    niti "And that's exactly what we're going to explore here."

    niti "Ready?"

    menu:

        "Let's begin!":
            jump garage_intro

        "What's this garage about?":
            jump garage_explanation


# ==================================================
# GARAGE INTRODUCTION
# ==================================================

label garage_explanation:

    show niti_normal

    niti "This is Cars n Coffee."

    niti "The idea is simple."

    niti "We talk about cars, explore their engineering and learn about automotive culture."

    niti "Think of it as a small car meet where there's always something interesting to discuss."

    niti "And we have two very special guests."

    niti "You'll meet them soon."

    jump garage_intro


label garage_intro:

    show niti_normal

    niti "Alright. Let me introduce you to the garage."

    niti "We have two cars here."

    niti "One is a Japanese performance legend."

    niti "The other is a racing machine from Germany."

    niti "Let's start with the Japanese one."

    jump r34_intro


# ==================================================
# NISSAN SKYLINE GT-R R34 INTRODUCTION
# ==================================================

label r34_intro:

    hide niti_normal
    show niti_racesuit at left
    with dissolve

    niti "Ladies and gentlemen, meet the Nissan Skyline GT-R R34."

    show r34_sprite at Position(xalign=0.75, yalign=0.65)
    with dissolve

    r34 "こんにちは! (Hello!)"

    r34 "I am Nissan Skyline GTR, you can call me R34."

    niti "Alright then. Tell us about yourself."

    r34 "I'm part of the Skyline Series...."

    r34 "My generation, the R34, was produced from 1999 until 2002."

    niti "And how you are famous for your engineering?"

    r34 "Especially what's underneath my bonnet...."

    niti "Let's talk about your engine."

    jump r34_engine


# ==================================================
# R34 ENGINE LESSON
# ==================================================

label r34_engine:

    niti "The R34 GT-R uses the RB26DETT engine."

    r34 "A 2.6-litre twin-turbocharged inline-six."

    niti "Let's break that down the name of the engine, RB26DETT."

    niti "the 'RB' stands for 'Race Bred', which is Nissan's engine family, which I cant confirm unless you do a research..."

    niti "The '26' refers to the engine's displacement, which is 2.6 litres."

    niti "the DE stands for 'Dual Overhead Camshaft', which means the engine has two camshafts per cylinder bank."

    r34 "my favorite part is the 'TT', which stands for 'Twin-Turbocharged'. one 'T' means its single turbocharged. Not all Ts stick at the end. Toyota's 2JZ-GTE has a T in the middle of the name which means it came with a turbocharger from the factory."

    niti "Correct and well explained."

    r34 "ありがとうございます! (Thank you!)"

    niti "Now, let's test your knowledge."

    niti "What does 'T', 'TT', or 'TTT' mean?"

    menu:

        "Indicates the engine has turbochargers":
            jump r34_turbo_correct

        "The engine has two extra cylinders":
            jump r34_turbo_wrong

        "The engine is a hybrid":
            jump r34_turbo_wrong


label r34_turbo_wrong:

    niti "Not quite."

    niti "Twin-turbo means the engine uses two turbochargers."

    r34 "They help force more air into the engine."

    niti "More air allows the engine to burn more fuel when properly tuned."

    niti "They also make that sweeping turbo sound that car enthusiasts love. Add a Blow-Off Valve and you get that signature 'stutututututu' sound."

    niti "Let's try that question again."

    jump r34_engine


label r34_turbo_correct:

    niti "Exactly!"

    r34 "At least someone understands my engineering."

    niti "Turbochargers use exhaust energy to spin a turbine and compress incoming air."

    niti "That helps an engine produce more power."

    r34 "And that's one reason people love the RB26DETT."

    niti "But remember, the engine is only one part of the entire car."

    niti "The R34 GT-R also has an advanced all-wheel-drive system."

    r34 "Name is ATTESA E-TS AWD System."

    niti "It's an electronically controlled all-wheel-drive system."

    niti "Now let's test what you've learned."

    jump r34_quiz


# ==================================================
# R34 QUIZ
# ==================================================

label r34_quiz:

    niti "Quick question."

    niti "Which engine is found in the R34 GT-R?"

    menu:

        "RB26DETT":
            jump r34_quiz_correct

        "P60B40":
            jump r34_quiz_wrong

        "2JZ-GTE":
            jump r34_quiz_wrong

    label r34_quiz2:
    niti "Question 2."

    niti "What is ATTESA E-TS?"

    menu:

        "ATTESA E-TS is a hybrid electric motor":
            jump r34_quiz_wrong2

        "ATTESA E-TS is an all-wheel-drive system":
            jump r34_quiz_correct2

        "ATTESA E-TS is a turbocharger":
            jump r34_quiz_wrong2



label r34_quiz_wrong:

    niti "Not quite."

    r34 "Come on. You just learned that."

    niti "The correct answer is RB26DETT."

    niti "Let's review the engine lesson once more."

    menu:

        "Review the lesson":
            jump r34_engine

        "Try the quiz again":
            jump r34_quiz

        "Return to the garage":
            jump garage_hub


label r34_quiz_correct:

    niti "Correct! The RB26DETT."


    jump r34_quiz2

label r34_quiz_correct2:

    r34 "Now thats what I like to hear!"

    $ r34_complete = True
    $ persistent.unlock_cg1 = True

    if "RB26 KNOWLEDGE" not in achievements:
        $ achievements.append("RB26 KNOWLEDGE")

    niti "Achievement unlocked: RB26 KNOWLEDGE."

jump m3_intro

label r34_quiz_wrong2:

    niti "Not quite."

    r34 "Come on. You just learned that."

    niti "Its an electronic powered all-wheel-drive system."

    niti "Let's review the R34 lesson once more."

    menu:

        "Review the lesson":
            jump r34_engine

        "Try the quiz again":
            jump r34_quiz

        "Return to the garage":
            jump garage_hub

    jump garage_hub


# ==================================================
# GARAGE HUB
# ==================================================

label garage_hub:

    scene bg garage
    with dissolve

    show niti_normal at left

    niti "Welcome back."

    niti "What would you like to explore next?"

    menu:

        "Meet the next car":
            jump m3_intro

        "Visit the R34 again":
            jump r34_intro

        "View achievements":
            jump achievement_collection

        "End the visit":
            jump game_end


# ==================================================
# BMW M3 GTR INTRODUCTION
# ==================================================

label m3_intro:

    hide niti_normal
    show niti_racesuit at left
    with dissolve

    niti "Now, let's meet our German racing machine."

    show m3_sprite at right
    with dissolve

    m3 "Guten Tag, wie geht es Ihnen? (Good day, how are you?)"

    menu:
        "I'm good, thank you.":
            $ m3_greeting = "I'm good, thank you."
            jump m3_intro_continue

label m3_intro_continue:
    m3 "I am the BMV M3 GTR. You can call me M3."

    niti "BMV? I think you mean BMW."

    m3 "den Mund halten! (Shut your mouth!) In our country, we say BMV because in German, we pronounce the letter 'W' as 'V'."

    niti "Chill, M3. I didn't knew that. Thanks for the clarification."

    m3 "...Anyway, I was built for racing."

    niti "The M3 GTR is a racing version of the E46 M3."
   
    niti "It competed in the American Le Mans Series."

    niti "And it was so successful that it beaten the factory-backed Porsche 911 GT3-RS and the Dodge Viper GTS-R."

    m3 "Yeah! Don't forget that I won the 2001 ALMS GT Championship too!"

    niti "Impressive!"

    m3 "Ya'll better not mess with me!"

    niti "Ok, that was tuff at some point. Let's focus on whats running this 2000s beast..."
    jump m3_engine


# ==================================================
# BMW M3 GTR ENGINE LESSON
# ==================================================

label m3_engine:

    niti "The racing E46 M3 GTR used the P60B40 engine."

    m3 "A 4.0-litre naturally aspirated V8."

    niti "Naturally aspirated means the engine draws air in without a turbocharger or supercharger."

    m3 "Eight cylinders. Four litres. No forced induction."

    niti "The P60B40 was developed for racing."

    niti "The M3 GTR competed in the American Le Mans Series."

    m3 "And I wasn't there to finish second like a fool!"

    niti "Right...."

    niti "Let's look at another important detail."

    niti "The M3 GTR was built around endurance racing."

    niti "Endurance racing tests speed, reliability and consistency over long periods."

    m3 "It's not just about being fast. It's about being fast for the entire time!"

    niti "Exactly."

    niti "Now let's test your knowledge."

    jump m3_quiz


# ==================================================
# BMW M3 GTR QUIZ
# ==================================================

label m3_quiz:

    niti "Which engine powered the racing E46 M3 GTR?"

    menu:

        "RB26DETT":
            jump m3_quiz_wrong

        "P60B40":
            jump m3_quiz_correct

        "S54":
            jump m3_quiz_wrong

        

label m3_quiz2:

    niti "BONUS: If the RB26DETT is turbocharged, why is the P60B40 naturally aspirated?"

    menu:

        "Because BMW is too poor to afford turbochargers or superchargers for the P60B40.":
            jump m3_quiz2_wrong

        "Because the P60B40 is too fragile and prone to forced inductions of turbochargers or superchargers, causing it to constantly overheat and fail.":
            jump m3_quiz2_wrong

        "Because the P60B40 was made for endurance racing, which strictly restricts the use of turbochargers or superchargers to prevent cheaters to cheat in endurance racing.":
            jump m3_quiz2_correct


label m3_quiz_wrong:

    niti "Not quite."

    m3 "The P60B40. Remember that."

    niti "It's a 4.0-litre naturally aspirated V8."

    menu:

        "Review the lesson":
            jump m3_engine

        "Try again":
            jump m3_quiz

        "Return to the garage":
            jump garage_hub


label m3_quiz_correct:

    niti "Correct! The P60B40."


jump m3_quiz2

label m3_quiz2_wrong:

    niti "It's okay to get this wrong. I didn't told you why BMW never gave the P60B40 a turbocharger or supercharger."

    m3 "Breh...."

    niti "my bad...."

    niti "I hope you know it this time...."

    menu:
        "Review the lesson again":
            jump m3_engine

        "Try again":
            jump m3_quiz

        "Return to the garage":
            jump garage_hub

label m3_quiz2_correct:

    niti "I am impressed by your knowledge, you knew that one even though I didnt teach you that..."
     
    m3 "Now you are getting somewhere! You are a true car enthusiast!"

    $ m3_complete = True
    $persistent.unlock_cg2 = True

    if "V8 KNOWLEDGE" not in achievements:
        $ achievements.append("V8 KNOWLEDGE")

    niti "Achievement unlocked: V8 KNOWLEDGE."

    jump garage_hub


# ==================================================
# ACHIEVEMENTS
# ==================================================

label achievement_collection:

    scene bg garage
    with dissolve

    show niti_normal at left

    niti "Let's see what you've unlocked."

    if len(achievements) == 0:

        niti "Nothing unlocked yet."

        niti "Complete lessons to earn achievements."

    else:

        niti "Here are your achievements."

        python:
            for achievement in achievements:
                renpy.say(niti, achievement)

    menu:

        "Return to garage":
            jump garage_hub


# ==================================================
# ENDING
# ==================================================

label game_end:

    scene bg garage
    with fade

    show niti_normal at center

    niti "Already leaving?"

    niti "Well, thanks for visiting Cars n Coffee."

    niti "Remember, learning about cars doesn't stop here."

    niti "There's always another engine, another design and another story to discover."

    niti "See you next time."

    stop music fadeout 2.0

    return


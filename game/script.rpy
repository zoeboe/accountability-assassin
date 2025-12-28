# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define g = Character("Guyleen")

define w = Character("Womeen")

define p = Character("Perseen")

# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

   # scene black

    #pause 1.0

   # scene cg_silhouette-shoot with fade:
    #    zoom 2
    #    xalign .2 yalign .2

   # pause 3.0

    scene black with fade

    scene office with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    pause 1.0

    show guyleen with dissolve:
        zoom .8
        align (.5, .5)

    g "...."

    show womeen at right with dissolve:
        zoom .33
        align (.5, .5)
        xoffset 400
        yoffset 100

    w "...."

    show perseen at left with dissolve:
        zoom .9
        xalign .2

    p ".... which is exactly what we're looking for."

    p "I believe your service could help get our employees back in the office."

    g "That's exactly why we\'re here. Simply having a trained facilitator can make the transition a lot smoother. People need to know there are others there working with them."

    p "Even walking through your office I can tell your employees are genuinely happy to be there."

    g "Glad to hear it. I've worked hard to get our office culture where it is today."

    g "I can draw up the paperwork in the other room."

    p "Will your assistant lead the way?"

    w "...."

    g "My apologies, she's not my assistant."

    p "My deepest apologies. You are...?"
    
    g "--Right this way."

    hide guyleen
    hide perseen

    w "........."

    show guyleen at left
    show perseen at center

    p "Wonderful. I can't wait to begin."

    g "Thank you, we'll reach out to set everything up."

    hide perseen

    g "...."

    scene cg_contract-desk

    g "...."

    g "I'm so tired."

    g ".............."




    # These display lines of dialogue.

    g "You've created a new Ren'Py game."

    w "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

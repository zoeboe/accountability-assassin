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

    scene black

    pause 1.0

    scene cg_silhouette-shoot with fade:
        zoom 2
        xalign .2 yalign .2

    pause 3.0

    scene black with fade

    scene office with fade

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    pause 1.0

    show guyleen with dissolve:
        zoom .8
        xalign .4 yalign .6

    g "Hghgh"

    show womeen at right with dissolve:
        zoom .7
        xalign .8 yalign .2

    w "..."

    show perseen at left with dissolve:
        zoom .9
        xalign .2

    p "Are you okay?"


    # These display lines of dialogue.

    g "You've created a new Ren'Py game."

    w "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return

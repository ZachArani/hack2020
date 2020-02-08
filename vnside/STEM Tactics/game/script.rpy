# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define a = Character("Asparaguy")
define c = Character("Cinnamon")
define k = Character("Kohlrabi")
define w = Character("Wasabi")
define s = Character("Sugar Cane")
define b = Character("Broccoli")
define t = Character("Bamboo")
define n = Character("Narrator")

image black:
    "#000"

image classroom:
    zoom 0.7
    "classroom.png"

image char sugarcane:
    yoffset 200
    "char sugarcane.png"

image char kohlrabi:
    xoffset 100
    "char kohlrabi.png"

image char cinnamon:
    xoffset -50
    zoom 1.2
    "char cinnamon.png"

image char broccoli:
    "char broccoli.png"

image char wasabi:
    "char wasabi.png"

image char bamboo:
    "char bamboo.png"

# The game starts here.

label start:

    scene black

    s "{i}(Another day of class. It's been a rough week, but I've made it through. It's nearly the weekend, and best of all -- no tests today!){/i}"

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene classroom

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    #intro narrative

    show char sugarcane

    s "Hey, Asparaguy! How's it going?"

    a "Oh, you know, I've been preparing real hard for my classes! I don't want to fall behind in any of them. I stayed up all night studying for Biology, I'm totally exhausted."

    s "Wow, that's so dedicated, Asparaguy!"

    show char kohlrabi

    k "So are you ready for today's test, then?"

    a "Today's WHAT?"

    k "Hm."

    show char sugarcane

    s "Don't be so mean to him, Kohl. He's trying his best! I'm sure he knows enough from paying attention in class to do just fine."

    a "Uh, y-yeah, right. From paying attention in class! I totally did that!"

    show char cinnamon

    c "'I totally did that!' Was that before or after you fell asleep during all the lectures?"

    scene black

    show char cinnamon

    s "{i}(Cinnamon is one of the three people in this class that I don't like. She's always found every way possible to single me out and pick on me, but I like to think that she doesn't get to me.){/i}"

    show char broccoli

    s "{i}(Broccoli is one of her minions. He's never really put much effort into anything, including hating me, but he still isn't very nice.){/i}"

    show char wasabi

    s "{i}(And then there's Wasabi. Where Cinnamon sometimes vomits words, Wasabi is the polar opposite. His insults are sparse, calculating, and cut to the core.){/i}"

    scene classroom

    show char broccoli

    b "I don't blame him. I'd do the same myself."

    show char cinnamon

    c "Exactly my point!"

    a "Okay, I fell asleep in class, you're not wrong. But it's only because I've been studying so much!"

    show char wasabi

    w "Oh, don't give him too much trouble. I know if I were him, I'd certainly need all the help I could get."

    a "Right, that's what I'm saying!"

    show char kohlrabi

    k "I don't think Wasabi's on your side here, Asparaguy."

    a "Really?"

    show char cinnamon

    c "Ha! What kind of a--"

    a "{i}(Suddenly, Cinnamon shut up as someone walked in the room.){/i}"

    show char bamboo

    t "Good morning, students. I hope your studying has been going well for today's test, yes?"

    # This ends the game.

    return

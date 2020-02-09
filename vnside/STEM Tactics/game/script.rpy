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

style lecture:
    size 96
    color "#FFFFFF"
    bold True
    font "JosefinSans-BoldItalic.ttf"

image black:
    "#000"

image classroom:
    zoom 0.7
    "classroom.png"

image blackboard:
    zoom 1.5
    "blackboard.png"

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

    scene classroom

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

    a "{i}(Everyone murmured a noncommittal answer, filling the room with white noise.){/i}"

    scene blackboard
    show char bamboo

    t "Hm... I see. Well, in any case, today we will be reviewing some of the more pertinent aspects of the Computer History curriculum. We’re going back to the origin of computer history...even before {i}my time.{/i}"

    show text "{=lecture}LECTURE BEGIN{/=lecture}" at truecenter
    with dissolve
    pause 1
    hide text
    with dissolve


    a "{i}(Must….Focus….){/i}"

    t "Our story begins in 1837 with English mathematician Charles Babbage. Mr. Babbage proposed a system he called the 'Analytical Machine,' a mechanical computer that closely resembles our modern machines."

    a "{i}(Charles Cabbage?){/i}"

    t "Babbage’s assistant Ada Lovelace was the first computer programmer. She developed an algorithm to calculate Bernoulli Numbers using Babbage’s Analytical Machine. Her contributions to the field later earned her the title of 'the mother of programming.'"

    t "We now skip forward to the 1930s, when Alan Turing proposed a formal mathematical model for describing computation. His theoretical system, known as a Turing Machine, is capable of computing anything that’s theoretically possible to compute."

    t "Even though a Turing Machine is impossible to create, Turing proved the fundamental concepts and limitations of computers on a theoretical basis. In essence, he set the ground rules for what is possible in computing."

    t "It was not even a full year later before the first digital computer was completed at Iowa State University. A handful of math professors conceived the Atanasoff-Berry computer, or {b}ABC{/b}, in 1937."

    t "The system was created only for solving math equations, which meant it didn’t have much use as a general purpose computer. The shortcomings of the ABC would be rectified in 1951 by the release of the Universal Automatic Computer, or UNIVAC for short."

    t "The computer was the first ever general purpose machine sold to the public. Even though the computer cost nearly 15 million dollars  and took up a whole room, UNIVAC wowed the public with its never before seen power."

    t "Grace Hopper, a creator of UNIVAC, conceptualized the modern programming language while working on the system. Her work would not be considered for UNIVAC, but in 1954 she created {b}MATH-MATIC{/b}, one of the first compiler-based programming languages."

    t "Before Hopper, all digital computer programs needed to be written in Assembly language, which is the lowest level of computer programming possible. This means that each instruction the programmer writes is verbatim executed by the computer’s processing unit."

    t "Because of Assembly’s complex and verbose nature, it is essentially impossible for humans to understand programs without training. On top of this, Assembly code written for one processor would not run on a different system."

    t "Hopper revolutionized the computer world by proposing programming languages that were both human readable and machine independent."

    t "As Mrs. Hopper was working to make computers easier to develop for, Jack Kilby was working to make them smaller. Kilby along with other scientists developed the first integrated circuit in 1958."

    t "His work helped to significantly shrink the size of computers and made devices like the portable calculator possible. He was even awarded the Nobel prize in physics for his work in the field of computer processors!"

    t "Many researchers in the following years conceptualized mass communication using  computer systems as they improved in speed and size. After several years of deliberation, ARPANET was created in 1967 to standardize what we now call The Internet."

    t "ARPANET was originally only used by research universities as well as military bases, although some research laboratories were also connected by the mid 1970s."

    t "Members of Bell Laboratories were revolutionizing the computer world just as they were getting online to ARPANET."

    t "Lab members Ken Thompson and Dennis Ritchie were at work in 1969 developing UNIX, the first notable specification for computer operating systems. UNIX is the foundation for virtually all modern operating systems, including macOS and Linux."

    t "In order to implement UNIX, Dennis Ritchie developed the C programming language."

    t "Although there were other high level programming languages inspired by Grace Hopper before C, the language was by far the most successful of its time and is one of the most used programming languages to date."

    t "After bell labs revolutionized the world with UNIX and C, many other companies made great strides in computing. The IBM 5100 made computing portable in 1975. Xerox furthered programming with the first Object Oriented Language--Smalltalk--in 1972."

    t "Xerox also helped to revolutionize personal computing with the Xerox Alto in 1973. The computer was the first system to use graphical user interfaces, or GUIs for short."

    t "These GUIs made computing easier to visualize for the inexperienced and became a staple for systems that followed. The computer had a direct impact on Steve Jobs and inspired the creation of Apple’s Macintosh computer as well as Microsoft Windows."

    t ""

    # This ends the game.

    return

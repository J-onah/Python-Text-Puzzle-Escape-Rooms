import time
from game_variables import *

def printer_scene():
    print("""You wake up in another room. You stand up to take in the surroundings. Suddenly, the printer in the dark corner of room began to stir.
    You walked towards the printer with apprehension and suspense, fearing for your life, not knowing what this ominous printing means.
    After the printing is done, you see a sheet of paper with a series of lines on it. Upon closer inspection, you come across a startling discovery.
    THE MAP IS ALIVEEEEEE""")
    time.sleep(5)
    choice = input("What language do you speak? Choose either english, french, or german (spelling matters), O tormented soul in this contraption: ")
    choice = choice.lower()
    return choice

def preserved_map():
    print("""You try to understand the gibberish code on the map, realising that it is in the form of a python code. You try to decode it.
    It read: 1st code: turtle.4wed(50*2-16+32-4*4)
             2nd code: turtle.laf(8100**0.5)
             3rd code: turtle.straight(tentifi * tu)""")

def map():
    print("""You try to understand the gibberish code on the map, realising that it is in the form of a python code. You try to decode it.
    It read: 1st code: turtle.4wed(50*...
             2nd code: turtle.laf(81...0**0.5)
             3rd code: turtle.str..ig...t(tentifi * tu)""")
    
def question_3(wrong_choice, question_b, keep_map):
    question_three = question_b.format("3rd")
    turtle = input(question_three)
    if keep_map == True:
        if turtle == 'turtle.forward(50)':
            ######### Answer #########
            checker = True
        elif turtle == 'm':
            preserved_map()
            checker = False
        else:
            print(wrong_choice)
            checker = False
    elif keep_map == False:
        if turtle == 'turtle.forward(50)':
            checker = True
        else:
            print(wrong_choice)
            checker = False
    return checker

def question_2(wrong_choice, question_b, keep_map):
    turtle = input(question_b.format("2nd"))
    if keep_map == True:
        if turtle == 'turtle.left(90)':
            ######### Answer #########
            checker = True
        elif turtle == 'm':
            preserved_map()
            checker = False
        else:
            print(wrong_choice)
            checker = False
    elif keep_map == False:
        if turtle == 'turtle.left(90)':
            checker = True
        else:
            print(wrong_choice)
            checker = False
    return checker

def question_1(wrong_choice, question_b, keep_map):
    question_one = """What is first python movement code needed to move the turtle in accordance to the map. The integers used in the code are '50', '90' and '100'.
    Answers are in the form below: turtle.forward(50)  """
    turtle = input(question_one)
    if keep_map == True:
        if turtle == 'turtle.forward(100)':
            ######### Answer #########
            checker = True
        elif turtle == 'm':
            preserved_map()
            checker = False
        else:
            print(wrong_choice)
            checker = False
    elif keep_map == False:
        if turtle == 'turtle.forward(100)':
            checker = True
        else:
            print(wrong_choice)
            checker = False
    return checker

def room_3():
    time.sleep(2)
    print("""You open the next door with paranoia, fearing what may lie ahead of you. As you glanced into the black void on the other side of the room, you stop to catch your breath.
    At the moment when you let down your guard, you see the ghost of Euler drifting by, trailing behind him is the taylor series of his notorious number. You collapsed as the fear of differentiation and series overwhelm you. """)
    time.sleep(5)

    language_list = {'english':"Map Of My House", 'french':"Le carte de ma maison", 'german': "Die Karte meines Hauses"}
    choice = printer_scene()
    time.sleep(5)

    print("You read the faint words imprinted on the top of the paper. It read...")

    if choice == 'english' or choice == 'french' or choice == 'german':
            print(language_list[choice])
    elif choice != 'english' or choice != 'french' or choice != 'german':
            print("""'It appears you cannot follow instructions!'You hear a raspy voice resonating in your ears,
            saying "p = mv, I = dp/dt" incessantly. You black out as the printer flies off the surface of the table
            and collides with you with a large momentum.""")
            time.sleep(5)
            choice = printer_scene()
    time.sleep(2)

    print("""You read the map with great enthusiasm, treating it as your prized possession. You analyse the map intently...""" )
    time.sleep(2)

    print("""Unfortunately, a gale of cold air blew throught the place you were in, causing the flames of the surroundings to touch the edge of your beloved map.
    In an instance, the map went ablaze and started to burn. You understood the gravity of the situation and began to consider your options...""")
    time.sleep(2)

    answer = input("Do you want to extinguish the flames with your fire extinguisher?  ")
    answer = answer.lower()
    while answer != "yes" and answer != "no":
        answer = input("DO YOU WANT OR NOT? YES OR NO? ")
        answer = answer.lower()

    if answer == "yes":
        print("""You extinguished the flames with great valor and courage! The map has been salvaged. You look at the map again..""")
        time.sleep(2)
        preserved_map()
        print("""You can now refer to the map when u wish by pressing m!""")
        keep_map = True
    elif answer == "no":
        print("""A questionable decision was made. What are you saving the fire extinguisher for? Christmas?!""")
        time.sleep(2)
        print("""The map continues to burn while you stubbornly refuse to use the tool you have acquired. You frantically
        try to memorise the map as parts of it incinerates into ashes right before your eyes, making the gibberish even more illegible...""")
        map()
        keep_map = False

    time.sleep(2)
    print("""As you enter into the next room, you glanced around your surroundings and realise you are in a labrynth. The map that you
    have been looking at so intently is now going to come in handy. Question is: Can you get out?""")

    wrong_choice = 'You walked into a wall and regretted. You backtracked and racked your brains for the correct answer.'
    question_b = """What is the {} python movement code? Answer is in the same form as above.  """

    check_1 = question_1(wrong_choice, question_b, keep_map)
    while check_1 == False:
        check_1 = question_1(wrong_choice, question_b, keep_map)
    check_2 = question_2(wrong_choice, question_b, keep_map)
    while check_2 == False:
        check_2 = question_2(wrong_choice, question_b, keep_map)
    check_3 = question_3(wrong_choice, question_b, keep_map)
    while check_3 == False:
        check_3 = question_3(wrong_choice, question_b, keep_map)

    print("""You exited the labrynth and saw a door. As you reached forward to unlock it, the room began to cave in
    and you fell through the cavity in the floor.""")

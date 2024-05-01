import time
import sys
from utils import quit_or_continue
from game_variables import *

## Define function(s) for intro here
def instructions():                                                             # Gives instructions/info on game to players
    display = """
    Welcome to ESCAPE 2020!!

    This game comprises a series of 5 rooms to escape from - one after another.

    Collect items along the way in the first 4 rooms by completing puzzles, before
    using these items to battle boss Chu Khan in the last room to escape 2020.

    You can quit the game by typing quit, and can only do so before solving each puzzle in a room.

    Enjoy the game!
    """
    return display

def room_1(game_items_list):
    #ITEMS
    room_1_items = [game_items_list[0], game_items_list[1], game_items_list[2], game_items_list[9]]

    # MOVES AGAINST CHU CHOO LIST
    moves_against_cc = ["Chu Choo slides to your right, ready to punch you. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo flies above you. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo is about to punch your nose from the front. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo disappears from your front and spawns behind you. Press w, a, s or d to avoid its punch: "]

    #INTRODUCTION
    print("ESCAPE 2020")
    time.sleep(1)                                                                   # Time.sleep() used to let people read at a comfortable pace (by printing subsequent statements slightly later)
    print("By F05 Group 2")
    time.sleep(2)
    start_area = input("Press z to start. \nPress c for instructions, before starting the game. \nType quit to quit. \n")
    print("Loading...")
    time.sleep(3)
    if start_area.lower() == "z":                                                   # START SCREEN MENU
        pass                                                                        # Similar to quit_or_continue(), but this has instructions
    elif start_area.lower() == "c":
        run = instructions()
        print(run)
        while start_area.lower() != "z" or start_area.lower() != "quit":
            start_area = ""
            start_area = input("Press z to start. \nType quit to quit. \n")
            if start_area.lower() == "z":
                break
            elif start_area.lower() == "quit":
                sys.exit()
    elif start_area.lower() == "quit":
        sys.exit()
    else:                                                                           # USE WHILE LOOP TO CONTINUE ASKING THE UNCOOPERATIVE USER TO ENTER Z, C OR QUIT ONLY
        while start_area.lower() != "z" or start_area.lower() != "c" or start_area.lower() != "quit":
            start_area = ""
            start_area = input("""
            Please press z, c or type quit only.
            Press z to start. Press c for instructions. Type quit to quit. \n""")
            print("Loading...")
            if start_area.lower() == "z":
                break
            elif start_area.lower() == "c":
                run = instructions()
                print(run)
                while start_area.lower() != "z" or start_area.lower() != "quit":
                    start_area = input("Press z to start. \nType quit to quit. \n")
                    if start_area.lower() == "z":
                        break
                    elif start_area.lower() == "quit":
                        sys.exit()
            elif start_area.lower() == "quit":
                sys.exit()

    temp = []
    time.sleep(1)
    print("Let's begin!")
    print("Loading...")
    time.sleep(3)
                                                                                    # NARRATION
    print("""
    After sleeping for a long time, you woke up in a cold, dark room.
    """)
    time.sleep(2)
    print("""
    There's a door at the other end of the room you were in, but when you tried to open it...

    It was locked.
    """)
    time.sleep(2)
    print("""
    Near the door, you saw a piece of paper and a red button.

    The piece of paper read:

    'To leave this room of dark and cold,
    guess the answer to the riddles told.
    Fail to get the answers right?
    Answer them once more and exit your plight.

    You have to get all of the answers right.
    Press the red button to start.
    Good luck.'
    """)
    time.sleep(5)
    score_room_1 = 0
    while score_room_1 != 4:                                                         # ROOM 1 GAME BEGINS
        score_room_1 = 0                                                             # While loops used so that if player did not get all 4 questions correct, they will have to redo the quiz
        quit_or_continue()                                                          # Function to quit or continue the game is called
        red_button = input("Press 'q',the red button, to start: ")
        if red_button.lower() == "q":
            pass
        elif red_button.lower() != "q":
            while red_button.lower() != "q":                                        # While loop used so that input is alway requested if input != q
                if red_button.lower() == "q":
                    break
                else:
                    red_button = input("Press 'q',the red button, to start: ")
        print("Loading...")
        time.sleep(3)
        print("""
        There will be 4 questions.
        Good luck!
        """)

        ################### QUESTION 1 ###################
        print("""
        How can you put an elephant in a fridge in 3 simple steps?
        """)                                                                        # Requesting input/answer for q1 one line below
        response_to_1 = input("""
        1. You can't.
        2. Cut it up, put it in a box, put it in the fridge.
        3. Open the fridge, put it in, close the fridge.
        """)
        if response_to_1 == "3":                                                      # If answer is 3, it is a right answer
            ################### ANSWER ###################
            score_room_1 += 1                                                        # Add points
            print("Right!")
        else:
            score_room_1 += 0                                                        # Other than 3, the other answers are wrong, no points added shown (where +=0 is present)
            print("Wrong...")
        
        ################### QUESTION 2 ###################
        print("""
        How can you put a giraffe in a fridge in 4 simple steps?
        """)
        response_to_2 = input("""
        1. You can't.
        2. Cut it up, put it in a box, take the elephant out, put it in the fridge.
        3. Open the fridge, take the elephant out, put it in, close the fridge.
        """)
        if response_to_2 == "3":
            ################### ANSWER ###################
            score_room_1 += 1
            print("Right!")
        else:
            score_room_1 += 0
            print("Wrong...")
        
        ################### QUESTION 3 ###################
        print("""
        The lion king had a party. Which 2 animals were not present?
        """)
        response_to_3 = input("""
        1. The hare and tortoise - they were afraid to be eaten.
        2. The elephant and the giraffe - they are in the fridge.
        3. The seahorse and the fish - they cannot survive on land.
        """)
        if response_to_3 == "2":
            ################### ANSWER ###################
            score_room_1 += 1
            print("Right!")
        else:
            score_room_1 += 0
            print("Wrong...")
        
        ################### QUESTION 4 ###################
        print("""
        LAST QUESTION
        A man tried to cross a river filled with crocodiles. He survived. Why?
        """)
        response_to_4 = input("""
        1. He put the crocodiles in the fridge.
        2. The crocodiles were at the lion's party.
        3. The crocodiles were not hungry.
        """)
        if response_to_4 == "2":
            ################### ANSWER ###################
            score_room_1 += 1
            print("Right!")
        else:
            score_room_1 += 0
            print("Wrong...")

    print("Congratuations! You have passed the test.")
    time.sleep(2)
    print("""
    Since you have completed the test,
    you will be awarded with 2 out of 3 items to choose from.
    These items may come in handy when battling the boss in the last room.
    Choose wisely!
    """)
    time.sleep(3)

    r1_selection_1 = input("""
                    First, select a, b or c only.
                    a. fridge
                    b. lion
                    c. elephant tusk
                    """)
    r1_selection_1 = r1_selection_1.lower()
    while r1_selection_1!= "a" and r1_selection_1 != "b" and r1_selection_1 != "c":
        r1_selection_1 = input("""
                        First, select a, b or c only.
                        a. fridge
                        b. lion
                        c. elephant tusk
                        """)
        r1_selection_1 = r1_selection_1.lower()

    if r1_selection_1 == "a":
        temp.append(room_1_items[0])                                           # Add the zeroth element of room1_items list into player_inv list if person choses option a
    elif r1_selection_1 == "b":
        temp.append(room_1_items[1])
    elif r1_selection_1 == "c":
        temp.append(room_1_items[2])

    r1_selection_2 = input("""
                    Now, choose another option.
                    a. fridge
                    b. lion
                    c. elephant tusk
                    """)
    r1_selection_2 = r1_selection_2.lower()

    while r1_selection_2 != "a" and r1_selection_2 != "b" and r1_selection_2 != "c":
            r1_selection_2 = input("""
                            Please choose another option.
                            a. fridge
                            b. lion
                            c. elephant tusk
                            """)
            r1_selection_2 = r1_selection_2.lower()

    while r1_selection_1 == r1_selection_2:
        r1_selection_2 = input("""
                        Please choose another option.
                        a. fridge
                        b. lion
                        c. elephant tusk
                        """)
        while r1_selection_2 != "a" and r1_selection_2 != "b" and r1_selection_2 != "c":
            r1_selection_2 = input("""
                            Please choose another option.
                            a. fridge
                            b. lion
                            c. elephant tusk
                            """)
            r1_selection_2 = r1_selection_2.lower()

    if r1_selection_2 == "a":
        temp.append(room_1_items[0])                                           #Add the zeroth element of room1_items list into player_inv list if person choses option a
    elif r1_selection_2 == "b":
        temp.append(room_1_items[1])
    elif r1_selection_2 == "c":
        temp.append(room_1_items[2])

    if score_room_1 == 4:
        player_inv.append(room_1_items[3])
        print("CONGRATULATIONS ON DA FULL MARKS. The jungle is pleased with your responses, as a reward, it has granted you the most sought after artefact by the people who has perished in them. The fire extinguisher!")
    for i in temp:
        if i not in player_inv:
            player_inv.append(i)
    time.sleep(2)
    print("Items now in inventory: {}.".format(player_inv))
    time.sleep(2)
    print("The door is now open.")
    time.sleep(1)
    print("You may now move on to the next room.")
    time.sleep(1)
    print("Walk ahead?")
    walk_or_not_input = input("Press w to walk ahead: ")
    if walk_or_not_input.lower() == "w":
        pass
    else:
        print("...")
        time.sleep(1)
        print("Suddenly, the ground around you begins to shake violently.")
        time.sleep(1)
        print("""
        'WHY DIDN'T YOU PRESS W?' a deep voice hollered.

        'YOU DECIDED TO MESS WITH ME. NOW, YOU'LL HAVE TO PAY FOR WHAT YOU DID.'

        Chu Choo, Chu Khan's magical carrot, appeared right before your very eyes.
        """)
        time.sleep(3)
        print("Uh-oh... looks like you have angered Chu Choo.")
        time.sleep(1)
        print("Dodge all her attacks by pressing w, a, s and d to move forward, leftward, downward and rightward respectively. Otherwise, the consequences are dire.")
        time.sleep(3)
        quit_or_continue()
        print("3")
        time.sleep(1)
        print("2")
        time.sleep(1)
        print("1")
        time.sleep(1)
        print("GO!")
        time.sleep(1)
        punch_count = 0
        i = 0                                                                         # INDEX TO CALL OUT QUESTIONS FROM M

        while punch_count < 2 and i <= 3:                                             # While loop breaks when person gets punched the second time
            move = input(moves_against_cc[i])
            if i == 0:
                if move.lower() == "d":
                    punch_count += 1
                    print("...")
                    print("You felt a punch on your face.")
                    i += 1
                elif move.lower() == "w" or move.lower() == "a" or move.lower() == "s":
                    print("Whew, you avoided that punch!")
                    i += 1
                else:
                    while move.lower() != "w" or move.lower() != "a" or move.lower() != "s" or move.lower() != "d":
                        move = input(moves_against_cc[i])
                        if move.lower() == "d":
                            punch_count += 1
                            print("...")
                            print("You felt a punch on your face.")
                            i += 1
                            break
                        elif move.lower() == "w" or move.lower() == "a" or move.lower() == "s":
                            print("Whew, you avoided that punch!")
                            i += 1
                            break
                        else:
                            pass
            elif i == 1:
                if move.lower() == "w" or move.lower() == "a" or move.lower() == "s" or move.lower() == "d":
                    print("Whew, you avoided that punch!")
                    i += 1
                else:
                    while move.lower() != "w" or move.lower() != "a" or move.lower() != "s" or move.lower() != "d":
                        move = input(moves_against_cc[i])
                        if move.lower() == "w" or move.lower() == "a" or move.lower() == "s" or move.lower() == "d":
                            print("Whew, you avoided that punch!")
                            i += 1
                        else:
                            pass
            elif i == 2:
                if move.lower() == "w":
                    punch_count += 1
                    print("...")
                    print("You felt a punch on your face.")
                    i += 1
                elif move.lower() == "d" or move.lower() == "a" or move.lower() == "s":
                    print("Whew, you avoided that punch!")
                    i += 1
                else:
                    while move.lower() != "w" or move.lower() != "a" or move.lower() != "s" or move.lower() != "d":
                        move = input(moves_against_cc[i])
                        if move.lower() == "w":
                            punch_count += 1
                            print("...")
                            print("You felt a punch on your face.")
                            i += 1
                            break
                        elif move.lower() == "d" or move.lower() == "a" or move.lower() == "s":
                            print("Whew, you avoided that punch!")
                            i += 1
                            break
                        else:
                            pass
            elif i == 3:
                if move.lower() == "s":
                    punch_count += 1
                    print("...")
                    print("You felt a punch from behind you.")
                elif move.lower() == "w" or move.lower() == "a" or move.lower() == "d":
                    print("Whew, you avoided that punch!")
                else:
                    while move.lower() != "w" or move.lower() != "a" or move.lower() != "s" or move.lower() != "d":
                        move = input(moves_against_cc[i])
                        if move.lower() == "s":
                            punch_count += 1
                            print("...")
                            print("You felt a punch from behind you.")
                            i += 1
                            break
                        elif move.lower() == "w" or move.lower() == "a" or move.lower() == "d":
                            print("Whew, you avoided that punch!")
                            i += 1
                            break
                        else:
                            pass
                i += 1
        if punch_count >= 2:
            print("...")
            time.sleep(1)

            print("You got attacked so badly that an item fell out of your backpack inventory.")
            print("The item that fell out was the {}.".format(player_inv[1]))
            player_inv.remove(player_inv[1])
            time.sleep(2)
            print("Now, this is what is in your inventory: ")
            print(player_inv)
            time.sleep(2)
            print("Run along to room 2 now!")
        else:
            print("You managed to escape the wraths of Chu Choo!")
            time.sleep(2)
            print("Run along to room 2 now!")

        quit_or_continue()

    return player_inv
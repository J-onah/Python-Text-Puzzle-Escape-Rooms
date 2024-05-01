import turtle
import time
from random import randrange
import random
from game_variables import *
from utils import quit_or_continue

## FIRST PART: ENERGY QUESTIONS
def energy_question(question, end_time,ans):
    print ("\nQuick! You have " + str(end_time) + " seconds!")
    time.sleep(1)
    print(question)
    time.sleep(1)
    end_time_1 = end_time
    while True:
        local_time_1 = time.time()
        guess = input("yes or no?")
        if (time.time()-local_time_1) >= end_time_1:
            print("Sorry, " + str(end_time) + " seconds was up!")
            return "time up"
        elif guess.lower() != ans:
            print("That's not right...")
            return False
        if guess.lower() == ans:
            print("You got it!")
            return True

def add_to_inv(item):
    player_inv.append(item)
    print ("Added " + item + " to your inventory!")

def t2_somersault(size, direction, t2):
    if direction <= 0.5:
        t2.left(180)
        t2.circle(size,360)
        t2.left(180)
    else:
        t2.circle(size,360)
    
def room_4(player_hp, player_inv):
    ###################### SETTINGS #############################
    room_4_items = ["oxygen tank & scuba mask", "coin", "dory"]
    #############################################################
    quit_or_continue()
    narrate_1 = "A door beneath you suddenly opens. You fall down a hole into the ocean!"
    print(narrate_1)
    time.sleep(2)
    input("You shout: ")
    narrate_2 = "You use your powers to reduce impact force. However, you need to know all the forces acting on you."
    print(narrate_2)

    time.sleep(3)

    ## ENERGY QUESTION ONE
    energy_yes = "yes"
    energy_no = "no"
    qn_1 = "\nIs gravitational force acting on you?"
    et_1 = 5
    ######### Answer is yes #########
    eq_1 = energy_question(qn_1, et_1, energy_yes)
    time.sleep(1)
    if eq_1 == True:
        player_hp += 1
        if player_hp > 15:
            player_hp = 15
        print("Your powers charge up. You have " + str(player_hp) + "/15!")
    elif eq_1 == False:
        player_hp = player_hp - 1
        print("Think harder! You lost 1 HP for a total of " + str(player_hp) + " HP.")
    else:
        player_hp = player_hp - 1
        print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")

    ## ENERGY QUESTION TWO
    qn_2 = "\nIs kinetic force acting on you?"
    et_2 = 4
    ######### Answer is no #########
    eq_2 = energy_question(qn_2, et_2, energy_no)
    time.sleep(1)
    if eq_2 == True:
        player_hp += 1
        if player_hp > 15:
            player_hp = 15
        print("Your common sense appears. You have " + str(player_hp) + "/15!")
    elif eq_2 == False:
        player_hp = player_hp - 1
        print("Your common sense vanishes. You lost 1 HP for a total of " + str(player_hp) + " HP.")
    else:
        player_hp = player_hp - 1
        print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")

    ## ENERGY QUESTION THREE
    qn_3 = "\nIs the Nike AirForce 2000 on you?"
    et_3 = 3
    ######### Answer is yes #########
    eq_3 = energy_question(qn_3, et_3, energy_yes)
    time.sleep(1)
    if eq_3 == True:
        player_hp += 1
        if player_hp > 15:
            player_hp = 15
        print("You convinced yourself it is. You have " + str(player_hp) + "/15!")
    elif eq_3 == False:
        player_hp = player_hp - 1
        print("Your bare feet makes you anxious. You lost 1 HP for a total of " + str(player_hp) + " HP.")
    else:
        player_hp = player_hp - 1
        print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")

    ## SECOND PART: 02 AND SCUBA MASK
    time.sleep(2)
    print ("\nYou fell to the ocean. The winds command the currents. Fortunately, an O2 tank and scuba mask appears before you...")
    time.sleep(3)

    add_to_inv(room_4_items[0])

    print("\n\nA wild turtle appears.\n'Let's go on an adventure?'")
    ans2_1 = input ("Yes or no?")
    if ans2_1.lower() == "yes":
        print("The turtle smiles, 'Let's go!'")
    else:
        print("It kicks you to its shell, 'We need to continue the plot...'")

    turtle_2 = turtle.Turtle()

    # SET UP TURTLE DESTINATION
    turtle_2.penup()
    turtle_2.goto(400,-20)
    turtle_2.pendown()
    turtle_2.circle(40,360)
    turtle_2.penup()
    turtle_2.goto(-300,20)
    turtle_2.pendown()

    # TURTLE ADVENTURE
    turtle_2.shape("turtle")
    turtle_2.color("green")

    questions_turtle = ["Give me a hug!", "Do you love me?", "Pat me!", "Turtle is the best!", "Are we nearly there?", "Are you enjoying this...", "Do you like the sea?", "Do you like the developers?", "Swim with me!!"]
    turtle_reactions = ["Yay!","Woohoo!","Awesome!!","I love you!"]
    while turtle_2.pos() < (400,-20):
        randomc = 1
        randomc = random.random()
        inp = input(questions_turtle[randrange(len(questions_turtle)-1)] + " Yes or no? ")
        if inp.lower() == "yes" or inp.lower() == "ok" or inp.lower() == "can":
            t2_somersault(randrange(250),randomc, turtle_2)
            turtle_2.forward(100)
            print(turtle_reactions[randrange(len(turtle_reactions)-1)])
        else:
            print("okay...")
            turtle_2.forward(20)

    print( "WE'VE REACHED!")

    time.sleep(3)

    ###################################
    ###### DORY STORY ARC STARTS ######
    ###################################
    print ("\n\n'Just keep swimming... just keep swimming... just keep swimming, swimming, swimming...'")
    time.sleep(4)
    ans_inp = input("Turning around, you say hi to... ")
    if ans_inp.lower() == "dory":
        print("Dory is enlightened you remember her!")
        time.sleep(1)
        player_hp += 2
        if player_hp > 15:
            player_hp = 15
        print("Dory emits a gleeful aura. You gain 1 HP for a total of " + str(player_hp) + " HP.")
    else:
        print("I'm dory...")
        time.sleep(1)
        player_hp = player_hp - 2
        print("Dory emits a moody aura. You lose 1 HP for a total of " + str(player_hp) + " HP.")

    time.sleep(2)
    print("\nDory takes something from her back...")
    time.sleep(2)
    print("'Here, I'll give this coin to you!'")
    time.sleep(1)
    print("\nAs your hands move to take the coin, you feel a strange sensation. Although dory is not a friend, you will miss her deeply.")
    time.sleep(3)
    ans_inp_3 = input("Take dory or the coin?")
    if ans_inp_3.lower() == "dory":
        print("'Wait!! Wha-'")
        time.sleep(1)
        print(room_4_items)
        add_to_inv(room_4_items[2])
    elif ans_inp_3.lower() == "the coin" or ans_inp_3.lower() == "coin":
        add_to_inv(room_4_items[1])
    else:
        while ans_inp_3.lower() != "dory" or ans_inp_3.lower() != "the coin" or ans_inp_3.lower() != "coin":
            ans_inp_3 = input("Take dory or the coin?")
            if ans_inp_3.lower() == "dory":
                print("'Wait!! Wha-'")
                time.sleep(1)
                add_to_inv(room_4_items[2])
                break
            elif ans_inp_3.lower() == "the coin" or ans_inp_3.lower() == "coin":
                add_to_inv(room_4_items[1])
                break
            else:
                pass
    return player_hp, player_inv

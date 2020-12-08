###################################################
#                                                 #
#          Room 1 by Corliss Tay She Jie          #
#          Room 2 by Jonah Yeo Zheng              #
#          Room 3 by Darren Teng Ren Kiat         #
#          Room 4 by Fatima Co Pepito             #
#          Room 5 by Suzette Leo Mei Yen          #
#                                                 #
###################################################


import turtle
import time
import sys
from random import randrange
import random


## Define function(s) for intro here
def instructions():                                                             #Gives instructions/info on game to players
    say = """
    Welcome to ESCAPE 2020!!

    This game comprises a series of 5 rooms to escape from - one after another.

    Collect items along the way in the first 4 rooms by completing puzzles, before
    using these items to battle boss Chu Khan in the last room to escape 2020.

    You can quit the game by typing quit, and can only do so before solving each puzzle in a room.

    Enjoy the game!
    """
    return say
def quit_or_continue():                                                         #Allows player to quit game whenever
    stay_or_leave = ""
    stay_or_leave = input("Press z to continue, or type quit to quit: ")        #Receive input to determine if quit
    stay_or_leave = stay_or_leave.lower()
    if stay_or_leave == "z":
      print("Starting...")
    elif stay_or_leave == "quit":
        sys.exit("Goodbye.")                                                    #sys.exit() allows player to quit as cell is terminated
    else:                                                                       #In the case where people enter other stuff
        while stay_or_leave != "z" and stay_or_leave != "quit":  #While loop used so that input is alway requested if input != z or input != quit
            stay_or_leave = ""
            stay_or_leave = input("Press z to start. \nType quit to quit. \n")
            stay_or_leave = stay_or_leave.lower()
            if stay_or_leave == "z":
                break                                                           #Break used, otherwise while loop will continue running
            elif stay_or_leave == "quit":
                sys.exit("Goodbye.")




## Define function(s) for room 1 here
def room_1(game_items_list):
  #ITEMS

  room1_items = [game_items_list[0], game_items_list[1], game_items_list[2], game_items_list[9]]


  #MOVES AGAINST CHU CHOO LIST

  movesagainstcc = ["Chu Choo slides to your right, ready to punch you. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo flies above you. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo is about to punch your nose from the front. Press w, a, s or d to avoid its punch: ",
                    "Chu Choo disappears from your front and spawns behind you. Press w, a, s or d to avoid its punch: "]

  #INTRODUCTION

  print("ESCAPE 2020")
  time.sleep(1)                                                                   #Time.sleep() used to let people read at a comfortable pace (by printing subsequent statements slightly later)
  print("By F05 Group 2")
  time.sleep(2)
  start_area = input("Press z to start. \nPress c for instructions, before starting the game. \nType quit to quit. \n")
  print("Loading...")
  time.sleep(3)
  if start_area.lower() == "z":                                                   #START SCREEN MENU
      pass                                                                        #Similar to quit_or_continue(), but this has instructions
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
  else:                                                                           #USE WHILE LOOP TO CONTINUE ASKING THE UNCOOPERATIVE USER TO ENTER Z, C OR QUIT ONLY
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
              break


  temp = []
  time.sleep(1)
  print("Let's begin!")
  print("Loading...")
  time.sleep(3)
                                                                                  #NARRATION
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
  score_room1 = 0
  while score_room1 != 4:                                                         #ROOM 1 GAME BEGINS
      score_room1 = 0                                                             #While loops used so that if player did not get all 4 questions correct, they will have to redo the quiz
      quit_or_continue()                                                          #Function to quit or continue the game is called
      red_button = input("Press 'q',the red button, to start: ")
      if red_button.lower() == "q":
          pass
      elif red_button.lower() != "q":
          while red_button.lower() != "q":                                        #While loop used so that input is alway requested if input != q
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
      qn1 = print("""
      How can you put an elephant in a fridge in 3 simple steps?
      """)                                                                        #Requesting input/answer for q1 one line below
      responseto1 = input("""
      1. You can't.
      2. Cut it up, put it in a box, put it in the fridge.
      3. Open the fridge, put it in, close the fridge.
      """)
      if responseto1 == "3":                                                      #If answer is 3, it is a right answer
          score_room1 += 1                                                        #Add points
          print("Right!")
      else:
          score_room1 += 0                                                        #Other than 3, the other answers are wrong, no points added shown (where +=0 is present)
          print("Wrong...")
      qn2 = print("""
      How can you put a giraffe in a fridge in 4 simple steps?
      """)
      responseto2 = input("""
      1. You can't.
      2. Cut it up, put it in a box, take the elephant out, put it in the fridge.
      3. Open the fridge, take the elephant out, put it in, close the fridge.
      """)
      if responseto2 == "3":
          score_room1 += 1
          print("Right!")
      else:
          score_room1 += 0
          print("Wrong...")
      qn3 = print("""
      The lion king had a party. Which 2 animals were not present?
      """)
      responseto3 = input("""
      1. The hare and tortoise - they were afraid to be eaten.
      2. The elephant and the giraffe - they are in the fridge.
      3. The seahorse and the fish - they cannot survive on land.
      """)
      if responseto3 == "2":
          score_room1 += 1
          print("Right!")
      else:
          score_room1 += 0
          print("Wrong...")
      qn4 = print("""
      LAST QUESTION
      A man tried to cross a river filled with crocodiles. He survived. Why?
      """)


      responseto4 = input("""
      1. He put the crocodiles in the fridge.
      2. The crocodiles were at the lion's party.
      3. The crocodiles were not hungry.
      """)
      if responseto4 == "2":
          score_room1 += 1
          print("Right!")
      else:
          score_room1 += 0
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

  r1_selection1 = input("""
                  First, select a, b or c only.
                  a. fridge
                  b. lion
                  c. elephant tusk
                  """)
  r1_selection1 = r1_selection1.lower()
  while r1_selection1!= "a" and r1_selection1 != "b" and r1_selection1 != "c":
      r1_selection1 = input("""
                      First, select a, b or c only.
                      a. fridge
                      b. lion
                      c. elephant tusk
                      """)
      r1_selection1 = r1_selection1.lower()

  if r1_selection1 == "a":
      temp.append(room1_items[0])                                           #Add the zeroth element of room1_items list into player_inv list if person choses option a
  elif r1_selection1 == "b":
      temp.append(room1_items[1])
  elif r1_selection1 == "c":
      temp.append(room1_items[2])

  r1_selection2 = input("""
                  Now, choose another option.
                  a. fridge
                  b. lion
                  c. elephant tusk
                  """)
  r1_selection2 = r1_selection2.lower()
  
  while r1_selection2 != "a" and r1_selection2 != "b" and r1_selection2 != "c":
          r1_selection2 = input("""
                          Please choose another option.
                          a. fridge
                          b. lion
                          c. elephant tusk
                          """)
          r1_selection2 = r1_selection2.lower()

  while r1_selection1 == r1_selection2:
      r1_selection2 = input("""
                      Please choose another option.
                      a. fridge
                      b. lion
                      c. elephant tusk
                      """)
      while r1_selection2 != "a" and r1_selection2 != "b" and r1_selection2 != "c":
          r1_selection2 = input("""
                          Please choose another option.
                          a. fridge
                          b. lion
                          c. elephant tusk
                          """)
          r1_selection2 = r1_selection2.lower()

  if r1_selection2 == "a":
      temp.append(room1_items[0])                                           #Add the zeroth element of room1_items list into player_inv list if person choses option a
  elif r1_selection2 == "b":
      temp.append(room1_items[1])
  elif r1_selection2 == "c":
      temp.append(room1_items[2])

  if score_room1 == 4:
      player_inv.append(room1_items[3])
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
  walksorno = input("Press w to walk ahead: ")
  if walksorno.lower() == "w":
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
      i = 0                                                                         #INDEX TO CALL OUT QUESTIONS FROM M


      while punch_count < 2 and i <= 3:                                             #While loop breaks when person gets punched the second time
          move = input(movesagainstcc[i])
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
                      move = input(movesagainstcc[i])
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
                      move = input(movesagainstcc[i])
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
                      move = input(movesagainstcc[i])
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
                      move = input(movesagainstcc[i])
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




## Define function(s) for room 2 here
####### Print out slowly
def printoutslowly(message_to_print, question_or_not = False):
    for_Key_board_Interrupt = 0
    normal = 0.05
    question_speed = 0.2

    if question_or_not == False:
        try:
            for i in message_to_print:
                for_Key_board_Interrupt += 1
                print(i, end = '')                 # end = '' makes it print on the sane line, though it's another print() function. Default is --> end = '\n'
                if i.isalpha() or i.isdigit():
                    time.sleep(normal)

        except KeyboardInterrupt:                       ####### Press Ctrl + C to activate
            print(message_to_print[for_Key_board_Interrupt::], end='')



    else:
        question_split = message_to_print.split(' ')

        try:
            for j in question_split:
                for_Key_board_Interrupt += 1
                if j != '\n':
                    print(j, end = ' ')
                    time.sleep(question_speed)
                else:
                    print(j)
                    time.sleep(question_speed)


        except KeyboardInterrupt:
            for k in question_split[for_Key_board_Interrupt::]:
                if k != '\n':
                    print(k, end = ' ')
                else:
                    print(k)



def room2intro():
    message_to_print = '\nYou have reached Room 2!'
    printoutslowly(message_to_print)
    time.sleep(1)
    message_to_print = '\nAnswer a few questions correctly, and you will get pass this room.'
    printoutslowly(message_to_print)
    time.sleep(1)
    message_to_print = '\nA wrong answer would cost you 1 HP.'
    printoutslowly(message_to_print)
    time.sleep(1)
    print('\n')

def room2questions(ls, question, correct, hp, inventory):
    print('HP: ' + (('0'+ str(hp)) if hp < 10 else str(hp)) + ' / 15\n')

    #Print question
    message_to_print = question                    ## Displaying the question that inputted into this function
    printoutslowly(message_to_print, True)

    random.shuffle(ls)                           ## Shuffling the choices of the specific question

    longest_Element = 0

    for i in ls:                               ##Getting the longest length in the list of options
        if len(i) >= longest_Element:
            longest_Element = len(i)

    longest_Element = str(longest_Element)

    print(('1 {:' + longest_Element + 's} \t2 {:' + longest_Element + 's} \n3 {:' + longest_Element + 's} \t4 {:' + longest_Element + 's}').format(ls[0], ls[1], ls[2], ls[3]))
    ## Display randomised options into numbered options with changeable length of format


    a = str(input("Type correct number, or type x to exit: "))                    ## First answer

    while a != 'x' and a != 'CORRECT':
                                                                                  ## While input is not X, the letter for exit
        if a.isdigit():                                                           ## Checking the string is a non-decimal number or not
            b = int(a)                                                            ## Changing string to int

            if b in range(1,5):                                                   ## Range is meant to contain options 1 to 4
                time.sleep(0.5)
                if ls[b-1] == correct:                                            ## b - 1 is because when user chooses option 1, the option 1 in the list is element 0, not 1
                    print("Correct!\n")
                    a = 'CORRECT'
                else:
                    hp -= 1
                    #print('\nHP:', hp, '/ 15\n')
                    print('\nHP: ' + (('0'+str(hp)) if hp < 10 else str(hp)) + ' / 15\n')

                    if hp == 5:
                        print('You are running low on health. ')

                    if hp <= 0:
                        print('You died.')
                        return hp, inventory, a

                    print(question)
                    print(('1 {:' + longest_Element + 's} \t2 {:' + longest_Element + 's} \n3 {:' + longest_Element + 's} \t4 {:' + longest_Element + 's}').format(ls[0], ls[1], ls[2], ls[3]))
                    a = input("Ouch! You lost 1 HP due to a wrong answer. Please enter the correct answer: ")      ## When the user keys in the wrong number, asking another input
            else:
                a = input("Please enter 1, 2, 3, or 4, or x to exit: ")                     ## When the input is a number but not 1, 2, 3, or 4
        else:
            a = input("Please enter 1, 2, 3, or 4, or x to exit: ")                        ## When input is not a number or X.

    if a != 'x':
        a = ''


    return hp, inventory, a


####### End of this function


####### DARK ROOMS FUNCTIONS
def room2DarkRooms_Intro():
    message_to_print = '\nBefore entering, you saw a note that read:\n'
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n"In these dark rooms,'
    printoutslowly(message_to_print)
    time.sleep(1)
    message_to_print = '\n\t\tlurks a creature.'
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n Whatever it is,'
    printoutslowly(message_to_print)
    time.sleep(1)
    message_to_print = '\n\t\tno one is sure.'
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = "\n It's invincible,"
    printoutslowly(message_to_print)
    time.sleep(1)
    message_to_print = "\n\t\twhile unseeable."
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n Whatever it takes,'
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n\t\tDO NOT BE NEAR."'
    printoutslowly(message_to_print, True)

    a = input('\nPress any key to continue, or c for instructions: ')
    a = a.lower()

    if a == 'c':
        time.sleep(1)
        print('\n\nInstructions')
        time.sleep(1)
        message_to_print = "\n\nEach display shows the current room that you are in. \nAnd the door to Rooms 1, 2, 3 and 4 are on the top, left, right and bottom respectively, represented in this format, eg. [ Room 1 ]"
        printoutslowly(message_to_print)
        message_to_print = "\nKey in 1, 2, 3 or 4 to enter one room."
        printoutslowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nOn the corners of the room that you are in are boxes, each represented in this format, eg. [A]"
        printoutslowly(message_to_print)
        message_to_print = "\nKey in h to hide in a box, and then key in A, B, C, or D to hide in a box. \nPlease only key in the letter of the boxes that is shown on display."
        printoutslowly(message_to_print)
        message_to_print = "\nKey in h again to unhide."
        printoutslowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nKey in s to stay in the room, or in a box if you are hidden."
        printoutslowly(message_to_print)
        a = input('\n\nPress any key for next instructions: ')
        time.sleep(1)


        message_to_print = "\n\nYou are represented by 'YOU' on the display. The creature is represented by X if it is in the room."
        printoutslowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nThe creature makes a noise when it is near the room you are in. Therefore, get ready to hide when you hear loud sounds."
        printoutslowly(message_to_print)
        message_to_print = "\nIf it comes into the room and sees you, you would be struck and would lose 3 HP."
        printoutslowly(message_to_print)
        message_to_print = "\nIf you are hidden, it might search the boxes in the room. If it finds you, you would be struck and would lose 3 HP."
        printoutslowly(message_to_print)
        a = input('\n\nPress any key for next instructions: ')
        time.sleep(1)

        message_to_print = "\n\nWhen you enter a room, you may find items, healthpacks or injured people. \nWhen you encounter an injured personnel, enter Y to bring them with you, or N to leave them alone."
        printoutslowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nLastly, when you leave a room, it would not be the same when you enter back in."
        printoutslowly(message_to_print)
        time.sleep(1)

        a = input('\nPress any key to continue: ')


    print('Loading...')
    time.sleep(2.5)
    message_to_print = '\n\nYou have entered the darkrooms.'
    printoutslowly(message_to_print)
    time.sleep(1)

    message_to_print = '\nAll the best.\n'
    printoutslowly(message_to_print)
    time.sleep(0.5)


def room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together):
    A = False
    B = False
    C = False
    D = False
    statement_AB = ''
    statement_CD = ''

    print('\n')

    print((' ' * 13 + '{} \n').format('[ Room 1 ]'))


    for display_box_x in range(0,4):                ## Box A and B sections
        if box_letters[display_box_x] == 'A' and A == False:    # Box A
            if B == True:
                statement_AB = ' ' * 10 + '[A]' + ' ' * 9 + '[B]'
            else:
                statement_AB = ' ' * 10 + '[A]'
            A = True        # Prevent repeat

        if box_letters[display_box_x] == 'B' and B == False:    # Box B
            if A == True:
                statement_AB += ' ' * 9 + '[B]'
            else:
                statement_AB = ' ' * 18 + ' ' * 4 + '[B]'
            B = True        # Prevent repeat
    print(statement_AB)

    if hide == False:
        At_YOU_Position = 'YOU'
    elif hide == True and (It_Has_Appeared == False or It_Has_Appeared == True and search == True):
        At_YOU_Position = ' '
    elif hide == True and It_Has_Appeared == True:
        At_YOU_Position = ' X '
    else:
        At_YOU_Position = 'ERROR'


    print(('\n{:16s}{:9s}{}\n').format('[ Room 2 ]', At_YOU_Position, '[ Room 3 ]'))


    for display_box_x in range(0,4):                ## Box C and D sections
        if box_letters[display_box_x] == 'C' and C == False:    # Box C
            if D == True:
                statement_CD = ' ' * 10 + '[C]' + ' ' * 9 + '[D]'
            else:
                statement_CD = ' ' * 10 + '[C]'

            C = True        # Prevent repeat

        if box_letters[display_box_x] == 'D' and D == False:    # Box D
            if C == True:
                statement_CD += ' ' * 9 + '[D]'
            else:
                statement_CD = ' ' * 18 + ' ' * 4 + '[D]'
            D = True        # Prevent repeat
    print(statement_CD)

    print(('\n' + ' ' * 13 + '{}').format('[ Room 4 ]'))

    if player_hp < 10:
        player_hp = '0' + str(player_hp)

    print('{} {:>29s}'.format('HP', 'Persons'))
    print(('{:2}{:5s} {:>21}').format(player_hp, ' / 15', persons_together))
    print() ## Create new line

def room2DarkRooms_Creature(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together, closeness, box_hidden):

    searching_box = random.choice([box_letters[0], box_letters[1], box_letters[2], box_letters[3]])


    stage_ONE = ['\nYou heard a soft sound.\n', '\nYou heard loud footsteps.\n'] ##########, '\nThe creature has entered into the room!\n']             ## Closeness 0
    stage_TWO_soft = ['\nThe soft sound disappeared.\n', 'The sound continues...\n', '\nThe soft sound becomes louder.\n']                ## Closeness 1
    stage_THREE_loud = ['\nThe sound grew softer.\n', '\nThe sound continues...\n', '\nThe creature has entered into the room!\n']          ## Closeness 2
    stage_FOUR_entered = ['\nThe creature waited in the room.\n', 'The creature has left the room.\n', '\nThe creature searched Box']   ## Closeness 3
    stage_in_Box = ['\nThe creature stayed in the box.\n', '\nThe creature came out of the box.\n']                                       ## Closeness 4
    time_delay = 0.5
    time_died_delay = 3
    died_message = 'RAAAAAAAARRRRWWWW! \nYou lost ' + str(player_hp) +' HP and died.'

    if persons_together > 1:
        struck_message = 'Slash! You were struck and lost 3 HP but you managed to escape alone.\n'
    else:
        struck_message = 'Slash! You were struck and lost 3 HP but you managed to escape.\n'

    persons_risk = persons_together * 2





    sound_or_appearance = random.randint(0, 40)





    if closeness == 0:
        time.sleep(time_delay)
        # Setting values section
        if sound_or_appearance >= 0 and sound_or_appearance <= (19 - persons_risk):
            closeness = 0


        elif sound_or_appearance >= 20 and sound_or_appearance <= (30 - persons_risk):
            closeness = 1


        else:
            closeness = 2


        # Display section
        room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

        if closeness != 0:

            message_to_print = stage_ONE[closeness-1]
            printoutslowly(message_to_print)


            if hide == False and closeness == 3:
                player_hp -= 3
                if player_hp > 0:
                    time.sleep(time_delay)
                    message_to_print = struck_message
                    printoutslowly(message_to_print)
                    persons_together = 1

                else:
                    message_to_print = died_message
                    printoutslowly(message_to_print)
                    player_hp = 0
                It_Has_Appeared = False
                closeness = -1
                time.sleep(time_died_delay)



    elif closeness == 1:
        time.sleep(time_delay)
        if sound_or_appearance >= 0 and sound_or_appearance <= (15 - persons_risk):
            closeness = 0


        elif sound_or_appearance >= 16 and sound_or_appearance <= (25 - persons_risk):
            closeness = 1


        else:
            closeness = 2


        room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

        message_to_print = stage_TWO_soft[closeness]
        printoutslowly(message_to_print)




    elif closeness == 2:
        time.sleep(time_delay)
        if sound_or_appearance >= 0 and sound_or_appearance <= (15 - persons_risk):
            closeness = 1


        elif sound_or_appearance >= 16 and sound_or_appearance <= (25 - persons_risk):
            closeness = 2


        else:
            closeness = 3
            It_Has_Appeared = True



        room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

        message_to_print = stage_THREE_loud[closeness - 1]
        printoutslowly(message_to_print)



        if hide == False and closeness == 3:
            player_hp -= 3
            if player_hp > 0:
                time.sleep(time_delay)
                message_to_print = struck_message
                printoutslowly(message_to_print)
                persons_together = 1

            else:
                message_to_print = died_message
                printoutslowly(message_to_print)
                player_hp = 0

            It_Has_Appeared = False
            closeness = -1
            time.sleep(time_died_delay)


    elif closeness == 3:
        It_Has_Appeared = True

        time.sleep(time_delay)
        if hide == False and search == False:
            room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)
            player_hp -= 3
            if player_hp > 0:
                message_to_print = struck_message
                printoutslowly(message_to_print)
                persons_together = 1

            else:
                message_to_print = died_message
                printoutslowly(message_to_print)
                player_hp = 0

            It_Has_Appeared = False
            closeness = -1
            time.sleep(time_died_delay)

        else:
            if sound_or_appearance >= 0 and sound_or_appearance <= 15:
                closeness = 3
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

                message_to_print = stage_FOUR_entered[0]
                printoutslowly(message_to_print)


            elif sound_or_appearance >= 16 and sound_or_appearance <= 25:
                closeness = 0
                It_Has_Appeared = False
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

                message_to_print = stage_FOUR_entered[1]
                printoutslowly(message_to_print)


            else:
                closeness = 4
                search = True
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

                message_to_print = stage_FOUR_entered[2] + ' ' + searching_box + '\n'
                printoutslowly(message_to_print)





                if searching_box == box_hidden:
                    time.sleep(time_delay)
                    print('\nThe creature found you!')
                    time.sleep(time_delay)
                    player_hp -= 3
                    if player_hp > 0:

                        message_to_print = struck_message
                        printoutslowly(message_to_print)
                        persons_together = 1

                    else:
                        message_to_print = died_message
                        printoutslowly(message_to_print)
                        player_hp = 0
                    closeness = -1
                    search = False
                    time.sleep(time_died_delay)

    else:  ## In box section
        time.sleep(time_delay)
        if hide == False and search == False:
            room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)
            player_hp -= 3
            if player_hp > 0:
                message_to_print = struck_message
                printoutslowly(message_to_print)

                persons_together = 1

            else:
                message_to_print = died_message
                printoutslowly(message_to_print)
                player_hp = 0
            It_Has_Appeared = False
            closeness = -1
            time.sleep(time_died_delay)

        else:
            if sound_or_appearance >= 0 and sound_or_appearance <= 15:
                closeness = 4
                search = True
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

                message_to_print = stage_in_Box[0]
                printoutslowly(message_to_print)


            else:
                closeness = 3
                search = False
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

                message_to_print = stage_in_Box[1]
                printoutslowly(message_to_print)



                time.sleep(time_delay)
                if hide == False and search == False:
                    player_hp -= 3
                    if player_hp > 0:

                        message_to_print = struck_message
                        printoutslowly(message_to_print)
                        persons_together = 1

                    else:
                        message_to_print = died_message
                        printoutslowly(message_to_print)
                        player_hp = 0
                    It_Has_Appeared = False
                    closeness = -1
                    time.sleep(time_died_delay)

    return hide, search, It_Has_Appeared, player_hp, persons_together, closeness


def room2DarkRooms(player_hp, inventory):

    room2DarkRooms_Intro()

    items_appearing_list = ["fridge", "lion", "elephant tusk", "kfc", "leaf shield", "screwdriver", "stone",
              "flamethrower"]

    item_type_found = random.choice(items_appearing_list)

    ## Box letters section
    box_letters = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']  ## 2 Letters for shuffling


    ### ALL THE INITIALISING VARIABLES
    a = input('Press any key to proceed, or x to exit: ')
    to_Continue = True
    hide = False
    search = False
    It_Has_Appeared = False
    closeness = 0
    hide_message = ''
    options_message = ''
    item_found = 0
    roomsBeforeExit = 0
    setRooms = 5
    persons_together = 1
    box_hidden = ''
    edible_healthpack = 2

    a = a.lower()

    if a == 'skip daarrkkroom':           ###### Only for DEVELOPERS!
        return player_hp, inventory, a

    ## START OF EVERYTHING

    while a != 'x' and roomsBeforeExit != setRooms and player_hp > 0:


        if to_Continue == True or closeness == -1:


            random.shuffle(box_letters)            ## Shuffling box letters. If two same letters at the first 4 element after shuffle, means there's only 3 boxes


            ## Displaying on Screen
            to_Continue = False


            if closeness == -1:
                closeness = 0
                It_Has_Appeared = False
                room2DarkRooms_Display(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together)

            else:
                if search == True:
                    search = False
                    closeness = 0
                roomsBeforeExit += 1
                hide, search, It_Has_Appeared, player_hp, persons_together, closeness = room2DarkRooms_Creature(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together, closeness, box_hidden)

        else:
            if a != 's' and player_hp > 0:
                hide, search, It_Has_Appeared, player_hp, persons_together, closeness = room2DarkRooms_Creature(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together, closeness, box_hidden)
                if closeness != -1:
                    message_to_print = "\nYou came out.\n"
                    printoutslowly(message_to_print)



        ## Display Messages Section for Items (20,25), People (10, 15), or Healthpack (2, 7)
        if closeness != -1 and player_hp > 0:
            if (item_found >= 20 and item_found <= 25):
                message_to_print = '\nYou entered the room, and found a '+ item_type_found + '!\n'
                printoutslowly(message_to_print)
                item_type_found = random.choice(items_appearing_list)

                        ## Persons found section
            elif (item_found >= 10 and item_found <= 15):
                message_to_print = '\nAn injured person lies at a corner of the room.\n'
                printoutslowly(message_to_print)
                help_choice = input("Will you bring them with you? Please enter Y (YES)/ N (no): ")
                help_choice = help_choice.upper()
                while help_choice != 'Y' and help_choice != 'N':
                    help_choice = input("Please enter only Y or N: ")
                    help_choice = help_choice.upper()
                if help_choice == 'Y':
                    time.sleep(0.5)
                    print('Take note: The more the people, the closer the creature.')
                    persons_together += 1
                else:
                    message_to_print = '\nYou left them alone.\n'
                    printoutslowly(message_to_print)

            elif (item_found >= 2 and item_found <= 7):
                if player_hp < 15 and player_hp > 0:

                    message_to_print = '\nYou found an edible healthpack and ate it!\n+' + (str(15-player_hp) if ((player_hp + edible_healthpack)>15) else str(edible_healthpack)) + ' HP\n'
                    printoutslowly(message_to_print)

                    if (player_hp + edible_healthpack) > 15:
                        player_hp = 15
                    else:
                        player_hp += edible_healthpack

            item_found = 0



            options_message = "Please enter the next room number to enter the room, \ns to stay, h to hide, or x to exit: "
            a = input(options_message)

            if a != '1' and a != '2' and a != '3' and a != '4' and a != 'x' and a != 'h' and a != 's':
                while a != '1' and a != '2' and a != '3' and a != '4' and a != 'x' and a != 'h' and a != 's':
                    a = input(options_message)



            ## Here is after confirmed a choosable option
            if a.isdigit():          ## IF only 1, 2, 3 or 4
                item_found = random.getrandbits(5) ## 0 to 32


                ## Found item Section
                if (item_found >= 20 and item_found <= 25):
                    player_inv.append(item_type_found)


                to_Continue = True



            else:

                ## Hide Section
                if a == 'h':
                    while a != 'x' and a != 'UN-HIDE' and closeness != -1:
                        options_message = 'Please enter the letter of the box to hide in, h to no longer hide, and x to exit: '
                        box_hidden = input(options_message)

                        if box_hidden == 'x':
                            a = 'x'

                        elif box_hidden == 'h':
                            a = 'UN-HIDE'
                            box_hidden = ''

                        else:
                            box_hidden = box_hidden.upper()

                            while  box_hidden != box_letters[0] and box_hidden != box_letters[1] and box_hidden != box_letters[2] and box_hidden != box_letters[3] and box_hidden != 'h' and box_hidden != 'x':       ## Loop till get correct option
                                box_hidden = input(options_message)
                                if box_hidden != 'h' and box_hidden != 'x':
                                    box_hidden = box_hidden.upper()


                            if box_hidden == box_letters[0] or box_hidden == box_letters[1] or box_hidden == box_letters[2] or box_hidden == box_letters[3]:
                                a = ''
                                ## Displaying on Screen
                                while a != 'h' and a != 'x' and closeness != -1:

                                    hide = True
                                    hide, search, It_Has_Appeared, player_hp, persons_together, closeness = room2DarkRooms_Creature(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together, closeness, box_hidden)

                                    if closeness != -1:
                                        if a != 's':

                                            hide_message = '\nYou hid in Box ' + box_hidden + '\n'
                                            printoutslowly(hide_message)

                                        else:
                                            if player_hp > 0 and closeness != -1:
                                                message_to_print = "\nYou decided to stay...\n"
                                                printoutslowly(message_to_print)


                                        options_message = "Please enter s to stay, h to no longer hide, and x to exit: "

                                        a = input(options_message)

                                        while  a != 's' and a != 'h' and a != 'x':       ## Loop till get correct option
                                            a = input(options_message)




                                if a != 'x' or closeness == -1:
                                    a = 'UN-HIDE'
                                    hide = False
                                    box_hidden = ''




                    ## Waiting Section
                elif a == 's' and closeness != -1:
                    hide, search, It_Has_Appeared, player_hp, persons_together, closeness = room2DarkRooms_Creature(box_letters, hide, search, It_Has_Appeared, player_hp, persons_together, closeness, box_hidden)

                    if player_hp > 0:
                        message_to_print = "\nYou decided to stay...\n"
                        printoutslowly(message_to_print)


    if a != 'x' and roomsBeforeExit == setRooms and player_hp > 0:

        message_to_print = "\nCongratulations! You made it!\n"
        printoutslowly(message_to_print)

        if persons_together > 1:
            message_to_print = '\nThe injured ones have been transferred to a safe place. Terrific!\n'
            printoutslowly(message_to_print)
            if ((persons_together - 1) * 2 + player_hp) < 14:
                message_to_print = '\nYou found ' + str(persons_together-1) + ' HP packs on the way out and consumed it!\n'
                printoutslowly(message_to_print)
                player_hp += 2 * (persons_together - 1)

            else:
                message_to_print = '\nYou found 1 BIG HP pack on the way out and consumed it!'
                printoutslowly(message_to_print)
                player_hp = 15

        else:
            if player_hp < 13:
                message_to_print = '\nYou found a HP pack on the way out and consumed it!\n'
                printoutslowly(message_to_print)
                player_hp += 2

        message_to_print = '\nYou now have ' + str(player_hp) + ' HP!\nYou have reached the 3rd puzzle room.\n'
        printoutslowly(message_to_print)


        a = ''
        a = input('To proceed, enter any key, or enter x to exit: ')
        a = a.lower()

        print('')





    return player_hp, inventory, a

def room_2(player_hp, player_inv):
  a = ''                                   ## This is just the input variable, for exiting when x is entered
  ItemChosen = False
  message_item = ''


  ####


  room2intro()

  a = input('Press any key to proceed, or x to exit: ')
  print('\n')

  if a != 'x' and player_hp > 0:
      lsq1 = ['Tiger', 'Lion', 'Gorilla', 'Others']                                     ## Question 1
      q1 = 'In the jungle, the mighty jungle, the _______ sleeps tonight. \n'
      player_hp, player_inv, a = room2questions(lsq1, q1, 'Lion', player_hp, player_inv)

      if a != 'x' and player_hp > 0:
          lsq2 = ['Wimoweh', 'Uyimbube', 'Ahwimewe', 'I win-a map']                          ## Question 2
          q2 = 'Spell the original "A-wee-ma-we": \n'
          player_hp, player_inv, a = room2questions(lsq2, q2, 'Uyimbube', player_hp, player_inv)

      if a != 'x' and player_hp > 0:
          lsq3 = ['The Lion Sleeps Two Nights', 'Wowimeweh', 'Mbube', 'In the Jungle']         ## Question 3
          q3 = 'What is the original name of this song? \n'
          player_hp, player_inv, a = room2questions(lsq3, q3, 'Mbube', player_hp, player_inv)

      if a != 'x' and player_hp > 0:
          message_to_print = '\nCongratulations, you gained a map! \nYou are also able to earn one more!\n'
          printoutslowly(message_to_print)
          player_inv.append('map')

          print('1 KFC\t\t2 Leaf Shield')
          a = input("Please enter 1 or 2 to choose your item: ")

          while ItemChosen != True:
              if a == '1':
                  ItemChosen = True
                  message_item = 'kfc'

              elif a == '2':
                  ItemChosen = True
                  message_item = 'leaf shield'

              else:
                  a = input("Please enter 1 or 2 to choose your item: ")

          message_to_print = 'You have chosen ' + message_item + '\nAnd this is its stats: '
          printoutslowly(message_to_print)
          if a == '1':
              message_to_print = 'Heal 3 HP'
              printoutslowly(message_to_print)

          elif a == '2':
              message_to_print = 'Defence increased by 1 for 3 turns'
              printoutslowly(message_to_print)

          player_inv.append(message_item)
          print('\n')
          a = input('Press any key to proceed, or x to exit: ')

          if a != 'x':
              message_to_print = '\nBetween you and the next puzzle room is a series of dark rooms which you must get through.'
              printoutslowly(message_to_print)

              time.sleep(2)


  ## EXTRA STAGE

  if a != 'x' and player_hp > 0:
      player_hp, player_inv, a = room2DarkRooms(player_hp, player_inv)


  if a == 'x':
      print('Goodbye, and thanks for playing!\n')
      time.sleep(1)
      sys.exit()
  else:
    return player_hp, player_inv


## Define function(s) for room 3 here
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
    
def question_3(wrong_choice, questionb, keep_map):
    #checker3 = False
    question3 = questionb.format("3rd")
    turtle3 = input(question3)
    if keep_map == True:

        if turtle3 == 'turtle.forward(50)':
            checker3 = True

        elif turtle3 == 'm':
            preserved_map()
            checker3 = False

        else:
            print(wrong_choice)
            checker3 = False

    elif keep_map == False:

        if turtle3 == 'turtle.forward(50)':
            checker3 = True

        else:
            print(wrong_choice)
            checker3 = False

    return checker3

def question_2(wrong_choice, questionb, keep_map):
    #checker2 = False
    turtle2 = input(questionb.format("2nd"))

    if keep_map == True:

        if turtle2 == 'turtle.left(90)':
            checker2 = True

        elif turtle2 == 'm':
            preserved_map()
            checker2 = False

        else:
            print(wrong_choice)
            checker2 = False

    elif keep_map == False:

        if turtle2 == 'turtle.left(90)':
            checker2 = True

        else:
            print(wrong_choice)
            checker2 = False

    return checker2

def question_1(wrong_choice, questionb, keep_map):
    #checker1 = False
    question1 = """What is first python movement code needed to move the turtle in accordance to the map. The integers used in the code are '50', '90' and '100'.
    Answers are in the form below: turtle.forward(50)  """
    turtle1 = input(question1)


    if keep_map == True:

        if turtle1 == 'turtle.forward(100)':
            checker1 = True

        elif turtle1 == 'm':
            preserved_map()
            checker1 = False

        else:
            print(wrong_choice)
            checker1 = False

    elif keep_map == False:

        if turtle1 == 'turtle.forward(100)':
            checker1 = True

        else:
            print(wrong_choice)
            checker1 = False

    return checker1

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
  questionb = """What is the {} python movement code? Answer is in the same form as above.  """

  check1 = question_1(wrong_choice, questionb, keep_map)
  while check1 == False:
      check1 = question_1(wrong_choice, questionb, keep_map)
  check2 = question_2(wrong_choice, questionb, keep_map)
  while check2 == False:
      check2 = question_2(wrong_choice, questionb, keep_map)
  check3 = question_3(wrong_choice, questionb, keep_map)
  while check3 == False:
      check3 = question_3(wrong_choice, questionb, keep_map)

  print("""You exited the labrynth and saw a door. As you reached forward to unlock it, the room began to cave in
  and you fell through the cavity in the floor.""")

## Define function(s) for room 4 here

## FIRST PART: ENERGY QUESTIONS
def energy_question(question, end_time,ans):
    print ("\nQuick! You have " + str(end_time) + " seconds!")
    time.sleep(1)
    print(question)
    time.sleep(1)
    end_time1 = end_time
    while True:
        local_time1 = time.time()
        guess = input("yes or no?")
        if (time.time()-local_time1) >= end_time1:
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
        #randomc = 1
    

def room_4(player_hp, player_inv):
  ###################### SETTINGS #############################
  room4_items = ["oxygen tank & scuba mask", "coin", "dory"]
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
  q1 = "\nIs gravitational force acting on you?"
  et1 = 5
  eq1 = energy_question(q1,et1,energy_yes)
  time.sleep(1)
  if eq1 == True:
      player_hp += 1
      if player_hp > 15:
          player_hp = 15
      print("Your powers charge up. You have " + str(player_hp) + "/15!")
  elif eq1 == False:
      player_hp = player_hp - 1
      print("Think harder! You lost 1 HP for a total of " + str(player_hp) + " HP.")
  else:
      player_hp = player_hp - 1
      print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")

  ## ENERGY QUESTION TWO
  q2 = "\nIs kinetic force acting on you?"
  et2 = 4
  eq2 = energy_question(q2,et2,energy_no)
  time.sleep(1)
  if eq2 == True:
      player_hp += 1
      if player_hp > 15:
          player_hp = 15
      print("Your common sense appears. You have " + str(player_hp) + "/15!")
  elif eq2 == False:
      player_hp = player_hp - 1
      print("Your common sense vanishes. You lost 1 HP for a total of " + str(player_hp) + " HP.")
  else:
      player_hp = player_hp - 1
      print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")

  ## ENERGY QUESTION THREE
  q3 = "\nIs the Nike AirForce 2000 on you?"
  et3 = 3
  eq3 = energy_question(q3,et3,energy_yes)
  time.sleep(1)
  if eq3 == True:
      player_hp += 1
      if player_hp > 15:
          player_hp = 15
      print("You convinced yourself it is. You have " + str(player_hp) + "/15!")
  elif eq3 == False:
      player_hp = player_hp - 1
      print("Your bare feet makes you anxious. You lost 1 HP for a total of " + str(player_hp) + " HP.")
  else:
      player_hp = player_hp - 1
      print("Think faster! You lost 1 HP for a total of " + str(player_hp) + " HP.")


  ## SECOND PART: 02 AND SCUBA MASK
  time.sleep(2)
  print ("\nYou fell to the ocean. The winds command the currents. Fortunately, an O2 tank and scuba mask appears before you...")
  time.sleep(3)

  add_to_inv(room4_items[0])

  print("\n\nA wild turtle appears.\n'Let's go on an adventure?'")
  ans2_1 = input ("Yes or no?")
  if ans2_1.lower() == "yes":
      print("The turtle smiles, 'Let's go!'")
  else:
      print("It kicks you to its shell, 'We need to continue the plot...'")

  t2 = turtle.Turtle()

  ##SET UP TURTLE DESTINATION
  t2.penup()
  t2.goto(400,-20)
  t2.pendown()
  t2.circle(40,360)
  t2.penup()
  t2.goto(-300,20)
  t2.pendown()

  ##TURTLE ADVENTUREEEEEEEEE
  t2.shape("turtle")
  t2.color("green")

  questions_turtle = ["Give me a hug!", "Do you love me?", "Pat me!", "Turtle is the best!", "Are we nearly there?", "Are you enjoying this...", "Do you like the sea?", "Do you like the developers?", "Swim with me!!"]
  turtle_reactions = ["Yay!","Woohoo!","Awesome!!","I love you!"]
  while t2.pos() < (400,-20):
      randomc = 1
      randomc = random.random()
      inp = input(questions_turtle[randrange(len(questions_turtle)-1)] + " Yes or no? ")
      if inp.lower() == "yes" or inp.lower() == "ok" or inp.lower() == "can":
          t2_somersault(randrange(250),randomc, t2)
          t2.forward(100)
          print(turtle_reactions[randrange(len(turtle_reactions)-1)])
      else:
          print("okay...")
          t2.forward(20)

  print( "WE'VE REACHED!")

  time.sleep(3)

  ###############################
  ###### DORY STORY ARC STARTSS
  ###############################

  print ("\n\n'Just keep swimming... just keep swimming... just keep swimming, swimming, swimming...'")
  time.sleep(4)
  ansinp = input("Turning around, you say hi to... ")
  if ansinp.lower() == "dory":
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
  ansinp3 = input("Take dory or the coin?")
  if ansinp3.lower() == "dory":
    print("'Wait!! Wha-'")
    time.sleep(1)
    print(room4_items)
    add_to_inv(room4_items[2])
  elif ansinp3.lower() == "the coin" or ansinp3.lower() == "coin":
    add_to_inv(room4_items[1])
  else:
      while ansinp3.lower() != "dory" or ansinp3.lower() != "the coin" or ansinp3.lower() != "coin":
          ansinp3 = input("Take dory or the coin?")
          if ansinp3.lower() == "dory":
              print("'Wait!! Wha-'")
              time.sleep(1)
              add_to_inv(room4_items[2])
              break
          elif ansinp3.lower() == "the coin" or ansinp3.lower() == "coin":
              add_to_inv(room4_items[1])
              break
          else:
              pass
  return player_hp, player_inv


## Define function(s) for room 5 here
def chu_khan_battle(player_hp, player_atk, player_inv, boss_hp, boss_atk, yn):

    #move_count = 0                            # Leave first

    stun_turn_count = 0                        # lion, coin, you can stack stuns

    tusk_atk_buff_turn_count = 0               # elephant tusk

    stone_atk_buff_turn_count = 0              # stone
    dodge_count = 0                            # apply dodge to the player until ck decides to attack

    leaf_shield_def_turn_count = 0             # leaf shield
    fake_atk_visual = 0                        # to give illusion of a def buff when ck's atk is actually -1

    b_def_turn_count = 0                       # option b (defend)

    boss_atk_buff_count = 0

    print("""\"Did you enjoy my escape room, {}?\" A voice thundered. \"This is how I collect people to EAT.\"

A nun stepped out from the shadows. Her eyes glowed like dying embers. This was no human being, this was...
 """.format(yn))
    time.sleep(2)
    print("""C H U  C H O O  K H A N ,  D E V O U R E R  O F  S O U L S ,  A B Y S S  F L E S H  R A V A G E R
     """)
    time.sleep(2)

    while boss_hp > 0 and player_hp > 0:

        while player_hp > 0 and boss_hp > 0:

            print("{}\'s hp: {}/15".format(yn, player_hp))
            print("{}\'s atk: {}".format(yn, player_atk))

            print("Current buffs: ")
            if tusk_atk_buff_turn_count > 0:
                print("+2 atk from tusk for {} turns.".format(tusk_atk_buff_turn_count))
            if stone_atk_buff_turn_count > 0:
                print("+2 atk from stone for 1 turn.")
            if leaf_shield_def_turn_count > 0:
                print("+1 defence for {} turns.".format(leaf_shield_def_turn_count))
            if dodge_count > 0:
                print("Dodge Chu Khan\'s next attack.")

            print(" ")
            print("Chu Khan\'s hp:", boss_hp)
            print("Chu Khan\'s atk:", boss_atk + fake_atk_visual)

            player_move = input("""
            What do you wish to do?
            a: Attack  b: Defend  c: Use item
            Your move: """)
            print(" ")

            if player_move == "a":
                boss_hp = boss_hp - player_atk
                print("You dealt {} damage to Chu Khan!".format(player_atk))
                print("""END OF PLAYER TURN
             """)
                break

            elif player_move == "b":
                boss_atk -= 1
                b_def_turn_count += 1
                print("You brace yourself for Chu Khan\'s oncoming attack (+1 def).")
                print("""END OF PLAYER TURN
             """)
                break

            elif player_move == "c":
                print("Your inventory:")
                for i in range(0, len(player_inv)):
                    if player_inv[i] != "fridge":
                        print("|", i, ":", player_inv[i], end=" ")
                    elif player_inv[i] == "fridge":
                        print("|", i, ":", player_inv[i], "- you cannot use this yet", end=" ")
                print("|")
                print(" ")

                chosen_item = input("Type number of item you wish to use: ")
                while chosen_item.isnumeric() == False:
                    chosen_item = input("NUMBER ONLY: ")
                print(" ")
                chosen_item = int(chosen_item)

                if chosen_item < 0 or chosen_item >= len(player_inv):
                    print("""You waste time not being able to choose an item. Chu Khan takes the advantage and closes in.""")

                elif player_inv[chosen_item] == "dory" or player_inv[chosen_item] == "kfc":   # HEALING ITEMS
                    player_hp = player_hp + game_items[player_inv[chosen_item]]
                    print("{} has regained {} hp!".format(yn, game_items[player_inv[chosen_item]]))
                    if player_hp >= 15:
                        player_hp = 15
                    print(" ")
                elif player_inv[chosen_item] == "lion" or player_inv[chosen_item] == "coin":  # STUN ITEMS
                    stun_turn_count = stun_turn_count + game_items[player_inv[chosen_item]]
                    print("Chu Khan is stunned for {} turns!".format(game_items[player_inv[chosen_item]]))
                    print(" ")
                elif player_inv[chosen_item] == "stone":                                      # stone, buff atk and dodge
                    player_atk = player_atk + game_items[player_inv[chosen_item]]
                    dodge_count = dodge_count + game_items[player_inv[chosen_item]]
                    stone_atk_buff_turn_count = 1
                    print("""Attack increased by 2, dodge applied for 1 Chu Khan attack!
                    """)
                elif player_inv[chosen_item] == "elephant tusk":                              # elephant tusk, buff atk
                    player_atk = player_atk + game_items[player_inv[chosen_item]]
                    tusk_atk_buff_turn_count += 3
                    print("""Attack increased by 2 for 3 turns!
                    """)
                elif player_inv[chosen_item] == "screwdriver":                                # screwdriver, perm buff atk
                    player_atk = player_atk + game_items[player_inv[chosen_item]]
                    print("""Attack permanently increased by 1!
                    """)
                elif player_inv[chosen_item] == "leaf shield":                                # leaf shield, -1 to boss atk
                    boss_atk -= 1
                    fake_atk_visual = 1
                    leaf_shield_def_turn_count += 3
                    print("""Defence increased by 1 for 3 turns!
                    """)
                elif player_inv[chosen_item] == "flamethrower":                               # flamethrower
                    print("""There is no fuel inside...
                    """)
                elif player_inv[chosen_item] == "fridge":
                    print("""You can\'t seem to find a use for it... and you\'ve wasted time trying to figure it out.
                    """)

                if chosen_item < 0 or chosen_item >= len(player_inv):
                    print(" ")
                elif player_inv[chosen_item] != "fridge":
                    player_inv.remove(player_inv[chosen_item])

                while player_move == "c" or player_move != "a" or player_move != "b":
                    print("{}\'s hp: {}/15".format(yn, player_hp))
                    print("{}\'s atk: {}".format(yn, player_atk))

                    print("Current buffs: ")
                    if tusk_atk_buff_turn_count > 0:
                        print("+2 atk from tusk for {} turns.".format(tusk_atk_buff_turn_count))
                    if stone_atk_buff_turn_count > 0:
                        print("+2 atk from stone for 1 turn.")
                    if leaf_shield_def_turn_count > 0:
                        print("+1 defence for {} turns.".format(leaf_shield_def_turn_count))
                    if dodge_count > 0:
                        print("Dodge Chu Khan\'s next attack.")

                    player_move = input("""
                    What do you wish to do?
                    a: Attack  b: Defend
                    Your move: """)
                    print(" ")

                    if player_move == "a":
                        boss_hp = boss_hp - player_atk
                        print("You dealt {} damage to Chu Khan!".format(player_atk))
                        print("""END OF PLAYER TURN
                     """)
                        break

                    elif player_move == "b":
                        boss_atk -= 1
                        b_def_turn_count += 1
                        print("You brace yourself for Chu Khan\'s oncoming attack.")
                        print("""END OF PLAYER TURN
                     """)
                        break

                    else:
                        print("Choose a or b!")

            else:
                print("DUNNO HOW TO READ AH")
                print(" ")
            break
        time.sleep(2)

        while player_hp > 0 and boss_hp > 0 and stun_turn_count == 0:
            boss_move = random.randint(1, 6)

            if boss_move <= 3:

                if dodge_count > 0:
                    print("Thanks to the stone, Chu Khan is temporarily blinded in one eye and misses her attack.")
                    dodge_count = 0
                else:
                    print("Chu Khan brings back her hand and delivers a big SLAP!")
                    print("She dealt {} damage!".format(boss_atk))
                    player_hp = player_hp - boss_atk

                if boss_atk_buff_count > 0:
                    boss_atk = boss_atk - 3*boss_atk_buff_count
                    boss_atk_buff_count = 0

            elif boss_move == 4:

                if dodge_count > 0:
                    print("""Thanks to the stone, Chu Khan is temporarily blinded in one eye and misses her attack.
                    """)
                    dodge_count = 0
                else:
                    print("Chu Khan\'s eyes begin to glow an ominous red (+1 atk). She blasts you with a LASER BEAM!")
                    boss_atk = boss_atk + 1
                    print("She dealt {} damage!".format(boss_atk))
                    player_hp = player_hp - boss_atk
                    boss_atk = boss_atk - 1

                if boss_atk_buff_count > 0:
                    boss_atk = boss_atk - 3*boss_atk_buff_count
                    boss_atk_buff_count = 0

            elif boss_move == 5 and boss_hp <14:

                print("""Chu Khan tosses an explosive protractor at you. Although it misses, the fire keeps you at bay.
She begins regenerating her wounds!
 """)
                print("+2 to Chu Khan\'s hp!")
                boss_hp = boss_hp + 2

            else:
                print("""Chu Khan bellows a deafening warcry. To your horror, extra spines begin growing from her flesh.
 She buffs her attack for the next strike!
  """)
                boss_atk = boss_atk + 3
                boss_atk_buff_count += 1

            print("""END OF BOSS TURN
             """)
            break

        if stun_turn_count > 0:
            stun_turn_count -= 1
            print("Chu Khan is stunned for {} more turn(s) and cannot move!".format(stun_turn_count))
            print("""END OF BOSS TURN
             """)

        if tusk_atk_buff_turn_count > 0:
            tusk_atk_buff_turn_count -= 1
            if tusk_atk_buff_turn_count == 0:
                player_atk -= 2

        if stone_atk_buff_turn_count > 0:
            stone_atk_buff_turn_count -= 1
            player_atk -= 2

        if leaf_shield_def_turn_count > 0:
            leaf_shield_def_turn_count -= 1
            if leaf_shield_def_turn_count == 0:
                fake_atk_visual = 0
                boss_atk += 1

        if b_def_turn_count > 0:
            b_def_turn_count -= 1
            if b_def_turn_count == 0:
                boss_atk += 1

        if player_hp <= 0 and "fridge" in player_inv:
            print("""As you feel your life ebbing away...

Your HP goes back to full health.

In the process, the fridge shatters.
 """)
            player_hp = 15
            player_inv.remove("fridge")
             #--------------------------------------END OF WHILE LOOP--------------------------------------#
    if player_hp <= 0:
        print("""As you lunge at Chu Khan for an attack, you feel like you\'ve been punched in the gut. You look down and
see her hand, sharpened claws and all, buried in your stomach. The next thing you see is... blackness and then nothing.

----- Y O U  D I E D -----
""")
    else:
        print("""\"NUUUUUOOOOOOOOOOOOOOOOOOOO!!!\"
Chu Khan exploded into flames. Within seconds, she was no more. You kick open the door, eager to leave this wretched place.
But... you were greeted by another room.

----- T H E  E N D ? -----
""")
        
def room_5(player_hp, player_inv):


  yn = "FATETBIAN"

  if "map" in player_inv:
      player_inv.remove("map")
  if "oxygen tank & scuba mask" in player_inv:
      player_inv.remove("oxygen tank & scuba mask")
  if "fire extinguisher" in player_inv:
      player_inv.remove("fire extinguisher")

  

  print("""You climbed up through the trapdoor. When you removed the scuba mask from your face, you see you are in a dimly
  lit, yet ordinary looking corridor. You wondered what manner of strange games you would encounter this time. Instead, the
  only door that met your eyes was an emergency exit at the other end. The neon green "exit" sign beckoned to you with every
  flicker. You slowly approached it, scanning the walls and floor for any false panels. This seemed too good to be true...
  """)

  time.sleep(2)
  press_x = input("Press x to continue: ")              # prompt button
  press_x = press_x.lower()
  while press_x != "x":
      press_x = input("PRESS x TO CONTINUE: ")
      press_x = press_x.lower()

  if player_inv.count("dory") > 0:                             # dory punishment
      dropped_item = random.randint(0, len(player_inv)-1)

      print("""
  A wild screech erupted from the trapdoor behind you.

  \"HOW DARE YOU BETRAY ME!\" The voice of your grilled friend echoed throughout the corridor. \"NOBODY COOKS ME, EATS ME
  WITH FRIED RICE AND GETS AWAY WITH IT!\" You spun around. Water began to spill out from the open trapdoor. A horrible
  gurgling accompanied the scratching of claws as THE VENGEFUL SPIRIT OF DORY, AVENGER OF WESTERN FOOD heaved herself out.

  The creature scrambled towards you, its twisted mass leaving a trail of darkened water. You rushed to the door. In your
  haste, you fail to slow down as the passageway beyond it took a sharp turn. When you smacked into the wall, you heard a
  clatter as one of your items fell from your bag. There was no time to stop and pick it up; DORY was right on your heels.
  Just before bursting through the second emergency exit door, you turn to look at what you dropped. It was your {}.
  """.format(player_inv[dropped_item]) )
      player_inv.remove(player_inv[dropped_item])

      time.sleep(2)
      press_x = input("Press x to continue: ")              # prompt button
      press_x = press_x.lower()
      while press_x != "x":
          press_x = input("PRESS x TO CONTINUE: ")
          press_x = press_x.lower()

  print("""
  You swing the door open, expecting to see the outside world. What you saw was yet another room. But this time,
  you were not alone.
  """)

  time.sleep(2)

  chu_khan_battle(player_hp, player_atk, player_inv, boss_hp, boss_atk, yn)






## All initial variables
player_hp = 15
player_atk = 1
player_inv = []

boss_hp = 15
boss_atk = 2

game_items = {"fridge": "revive item", "lion": 2, "elephant tusk": 2, "map": "misc item", "kfc": 3, "leaf shield": -1, "screwdriver": 1, "stone": 2,
              "flamethrower": "troll item", "oxygen tank & scuba mask": "misc item", "coin": 1, "dory": 5}
## Dictionary above, list below
game_items_list = ["fridge", "lion", "elephant tusk", "map", "kfc", "leaf shield", "screwdriver", "stone", "flamethrower", "fire extinguisher", "oxygen tank & scuba mask", "coin", "dory"]




## Statements to call room 1 functions and any other statements in between here
player_inv = room_1(game_items_list)
## Statements to call room 2 functions and any other statements in between here
player_hp, player_inv = room_2(player_hp, player_inv)
## Statements to call room 3 functions and any other statements in between here
room_3()
## Statements to call room 4 functions and any other statements in between here
player_hp, player_inv = room_4(player_hp, player_inv)
## Statements to call room 5 functions and any other statements in between here
room_5(player_hp, player_inv)




########## Reference: https://www.tutorialsteacher.com/python/sys-module                                                    [for import sys and sys.exit()]
##########            https://en.wikipedia.org/wiki/The_Lion_Sleeps_Tonight#%22The_Lion_Sleeps_Tonight%22
##########            https://stackoverflow.com/questions/36962995/format-in-python-by-variable-length                      [For formatting strings using changeable lengths]
##########            https://stackoverflow.com/questions/6824681/get-a-random-boolean-in-python                            [For random choice]
##########            https://stackoverflow.com/questions/5598181/multiple-prints-on-the-same-line-in-python                [Printing characters on the same line though using multiple print functions]
##########            https://stackoverflow.com/questions/14463698/python-change-variable-value-on-exit-for-next-session    [Keyboard Interrupt]
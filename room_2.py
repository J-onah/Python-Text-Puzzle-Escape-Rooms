import time
import sys
import random
from game_variables import *
from room_2_extra_stage import *

def room_2_intro():
    message_to_print = '\nYou have reached Room 2!'
    print_out_slowly(message_to_print)
    time.sleep(1)
    message_to_print = '\nAnswer a few questions correctly, and you will get pass this room.'
    print_out_slowly(message_to_print)
    time.sleep(1)
    message_to_print = '\nA wrong answer would cost you 1 HP.'
    print_out_slowly(message_to_print)
    time.sleep(1)
    print('\n')

def room_2_questions(ls, question, correct, hp, inventory):
    print('HP: ' + (('0'+ str(hp)) if hp < 10 else str(hp)) + ' / 15\n')

    # Print question
    ## Displaying the question that is passed into this function
    message_to_print = question                    
    print_out_slowly(message_to_print, True)

    ## Shuffling the choices of the specific question
    random.shuffle(ls)                          

    longest_Element = 0

    ## Getting the longest length in the list of options
    for i in ls:                               
        if len(i) >= longest_Element:
            longest_Element = len(i)

    longest_Element = str(longest_Element)

    ## Display randomised options into numbered options with changeable length of format
    print(('1 {:' + longest_Element + 's} \t2 {:' + longest_Element + 's} \n3 {:' + longest_Element + 's} \t4 {:' + longest_Element + 's}').format(ls[0], ls[1], ls[2], ls[3]))
    
    ## First answer
    user_input = str(input("Type correct number, or type x to exit: "))                    

    ## While input is not X, the letter for exit
    while user_input != 'x' and user_input != 'CORRECT':
        ## Checking the string is a non-decimal number or not
        if user_input.isdigit():                    
            ## Changing string to int                                       
            b = int(user_input)                                                            
            ## Range is meant to contain options 1 to 4
            if b in range(1,5):                                                   
                time.sleep(0.5)
                ## b - 1 is because when user chooses option 1, the option 1 in the list is element 0, not 1
                if ls[b-1] == correct:                                            
                    print("Correct!\n")
                    user_input = 'CORRECT'
                else:
                    hp -= 1
                    print('\nHP: ' + (('0'+str(hp)) if hp < 10 else str(hp)) + ' / 15\n')

                    if hp == 5:
                        print('You are running low on health. ')

                    if hp <= 0:
                        print('You died.')
                        return hp, inventory, user_input

                    print(question)
                    print(('1 {:' + longest_Element + 's} \t2 {:' + longest_Element + 's} \n3 {:' + longest_Element + 's} \t4 {:' + longest_Element + 's}').format(ls[0], ls[1], ls[2], ls[3]))
                    ## When the user keys in the wrong number, asking another input
                    user_input = input("Ouch! You lost 1 HP due to a wrong answer. Please enter the correct answer: ")      
            else:
                ## When the input is a number but not 1, 2, 3, or 4
                user_input = input("Please enter 1, 2, 3, or 4, or x to exit: ")                    
        else:
            ## When input is not a number or X.
            user_input = input("Please enter 1, 2, 3, or 4, or x to exit: ")                        
    if user_input != 'x':
        user_input = ''
    return hp, inventory, user_input

def room_2(player_hp, player_inv):
  user_input = ''                                   ## This is just the input variable, for exiting when x is entered
  item_chosen = False
  message_item = ''

  room_2_intro()

  user_input = input('Press any key to proceed, or x to exit: ')
  print('\n')

  if user_input != 'x' and player_hp > 0:
      list_q1 = ['Tiger', 'Lion', 'Gorilla', 'Others']          
      ################### Question 1 ###################                           
      q1 = 'In the jungle, the mighty jungle, the _______ sleeps tonight. \n'
      ## Answer is 'Lion'
      player_hp, player_inv, user_input = room_2_questions(list_q1, q1, 'Lion', player_hp, player_inv)

      if user_input != 'x' and player_hp > 0:
          list_q2 = ['Wimoweh', 'Uyimbube', 'Ahwimewe', 'I win-a map']                          
          ################### Question 2 ###################   
          q2 = 'Spell the original "A-wee-ma-we": \n'
          ## Answer is 'Uyimbube'
          player_hp, player_inv, user_input = room_2_questions(list_q2, q2, 'Uyimbube', player_hp, player_inv)

      if user_input != 'x' and player_hp > 0:
          list_q3 = ['The Lion Sleeps Two Nights', 'Wowimeweh', 'Mbube', 'In the Jungle']         
          ################### Question 3 ###################   
          q3 = 'What is the original name of this song? \n'
          ## Answer is 'Mbube'
          player_hp, player_inv, user_input = room_2_questions(list_q3, q3, 'Mbube', player_hp, player_inv)

      if user_input != 'x' and player_hp > 0:
          message_to_print = '\nCongratulations, you gained a map! \nYou are also able to earn one more!\n'
          print_out_slowly(message_to_print)
          player_inv.append('map')

          print('1 KFC\t\t2 Leaf Shield')
          user_input = input("Please enter 1 or 2 to choose your item: ")

          while item_chosen != True:
              if user_input == '1':
                  item_chosen = True
                  message_item = 'kfc'
              elif user_input == '2':
                  item_chosen = True
                  message_item = 'leaf shield'
              else:
                  user_input = input("Please enter 1 or 2 to choose your item: ")

          message_to_print = 'You have chosen ' + message_item + '\nAnd this is its stats: '
          print_out_slowly(message_to_print)
          if user_input == '1':
              message_to_print = 'Heal 3 HP'
              print_out_slowly(message_to_print)
          elif user_input == '2':
              message_to_print = 'Defence increased by 1 for 3 turns'
              print_out_slowly(message_to_print)

          player_inv.append(message_item)
          print('\n')
          user_input = input('Press any key to proceed, or x to exit: ')
          if user_input != 'x':
              message_to_print = '\nBetween you and the next puzzle room is a series of dark rooms which you must get through.'
              print_out_slowly(message_to_print)
              time.sleep(2)

  ## EXTRA STAGE
  if user_input != 'x' and player_hp > 0:
      player_hp, player_inv, user_input = room_2_dark_rooms(player_hp, player_inv)

  if user_input == 'x':
      print('Goodbye, and thanks for playing!\n')
      time.sleep(1)
      sys.exit()
  else:
    return player_hp, player_inv

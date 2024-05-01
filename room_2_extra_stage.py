import time
import random
from game_variables import *

def print_out_slowly(message_to_print, question_or_not = False):
    for_keyboard_interrupt = 0
    normal = 0.05
    question_speed = 0.2
    if question_or_not == False:
        try:
            for i in message_to_print:
                for_keyboard_interrupt += 1
                print(i, end = '')                      # end = '' makes it print on the sane line, though it's another print() function. Default is --> end = '\n'
                if i.isalpha() or i.isdigit():
                    time.sleep(normal)
        except KeyboardInterrupt:                       
            # Press Ctrl + C to activate
            print(message_to_print[for_keyboard_interrupt::], end='')
    else:
        question_split = message_to_print.split(' ')
        try:
            for j in question_split:
                for_keyboard_interrupt += 1
                if j != '\n':
                    print(j, end = ' ')
                    time.sleep(question_speed)
                else:
                    print(j)
                    time.sleep(question_speed)
        except KeyboardInterrupt:
            for k in question_split[for_keyboard_interrupt::]:
                if k != '\n':
                    print(k, end = ' ')
                else:
                    print(k)

####### DARK ROOMS FUNCTIONS
def room_2_dark_rooms_intro():
    message_to_print = '\nBefore entering, you saw a note that read:\n'
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n"In these dark rooms,'
    print_out_slowly(message_to_print)
    time.sleep(1)
    message_to_print = '\n\t\tlurks a creature.'
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n Whatever it is,'
    print_out_slowly(message_to_print)
    time.sleep(1)
    message_to_print = '\n\t\tno one is sure.'
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = "\n It's invincible,"
    print_out_slowly(message_to_print)
    time.sleep(1)
    message_to_print = "\n\t\twhile unseeable."
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n Whatever it takes,'
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = '\n\t\tDO NOT BE NEAR."'
    print_out_slowly(message_to_print, True)

    user_input = input('\nPress any key to continue, or c for instructions: ')
    user_input = user_input.lower()

    if user_input == 'c':
        time.sleep(1)
        print('\n\nInstructions')
        time.sleep(1)
        message_to_print = "\n\nEach display shows the current room that you are in. \nAnd the door to Rooms 1, 2, 3 and 4 are on the top, left, right and bottom respectively, represented in this format, eg. [ Room 1 ]"
        print_out_slowly(message_to_print)
        message_to_print = "\nKey in 1, 2, 3 or 4 to enter one room."
        print_out_slowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nOn the corners of the room that you are in are boxes, each represented in this format, eg. [A]"
        print_out_slowly(message_to_print)
        message_to_print = "\nKey in h to hide in a box, and then key in A, B, C, or D to hide in a box. \nPlease only key in the letter of the boxes that is shown on display."
        print_out_slowly(message_to_print)
        message_to_print = "\nKey in h again to unhide."
        print_out_slowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nKey in s to stay in the room, or in a box if you are hidden."
        print_out_slowly(message_to_print)
        user_input = input('\n\nPress any key for next instructions: ')
        time.sleep(1)

        message_to_print = "\n\nYou are represented by 'YOU' on the display. The creature is represented by X if it is in the room."
        print_out_slowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nThe creature makes a noise when it is near the room you are in. Therefore, get ready to hide when you hear loud sounds."
        print_out_slowly(message_to_print)
        message_to_print = "\nIf it comes into the room and sees you, you would be struck and would lose 3 HP."
        print_out_slowly(message_to_print)
        message_to_print = "\nIf you are hidden, it might search the boxes in the room. If it finds you, you would be struck and would lose 3 HP."
        print_out_slowly(message_to_print)
        user_input = input('\n\nPress any key for next instructions: ')
        time.sleep(1)

        message_to_print = "\n\nWhen you enter a room, you may find items, healthpacks or injured people. \nWhen you encounter an injured personnel, enter Y to bring them with you, or N to leave them alone."
        print_out_slowly(message_to_print)
        time.sleep(1)

        message_to_print = "\n\nLastly, when you leave a room, it would not be the same when you enter back in."
        print_out_slowly(message_to_print)
        time.sleep(1)

        user_input = input('\nPress any key to continue: ')

    print('Loading...')
    time.sleep(2.5)
    message_to_print = '\n\nYou have entered the darkrooms.'
    print_out_slowly(message_to_print)
    time.sleep(1)

    message_to_print = '\nAll the best.\n'
    print_out_slowly(message_to_print)
    time.sleep(0.5)

def room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together):
    A = False
    B = False
    C = False
    D = False
    statement_AB = ''
    statement_CD = ''

    print('\n')
    print((' ' * 13 + '{} \n').format('[ Room 1 ]'))

    ## Box A and B sections
    for display_box_x in range(0,4):               
        # Box A
        if box_letters[display_box_x] == 'A' and A == False:    
            if B == True:
                statement_AB = ' ' * 10 + '[A]' + ' ' * 9 + '[B]'
            else:
                statement_AB = ' ' * 10 + '[A]'
            # Prevent repeat
            A = True        

        # Box B
        if box_letters[display_box_x] == 'B' and B == False:    
            if A == True:
                statement_AB += ' ' * 9 + '[B]'
            else:
                statement_AB = ' ' * 18 + ' ' * 4 + '[B]'
            # Prevent repeat
            B = True        
    print(statement_AB)

    if hide == False:
        player_pos_value = 'YOU'
    elif hide == True and (has_creature_appeared == False or has_creature_appeared == True and search == True):
        player_pos_value = ' '
    elif hide == True and has_creature_appeared == True:
        player_pos_value = ' X '
    else:
        player_pos_value = 'ERROR'

    print(('\n{:16s}{:9s}{}\n').format('[ Room 2 ]', player_pos_value, '[ Room 3 ]'))

    ## Box C and D sections
    for display_box_x in range(0,4):                
        # Box C
        if box_letters[display_box_x] == 'C' and C == False:    
            if D == True:
                statement_CD = ' ' * 10 + '[C]' + ' ' * 9 + '[D]'
            else:
                statement_CD = ' ' * 10 + '[C]'
            # Prevent repeat
            C = True        
        
        # Box D
        if box_letters[display_box_x] == 'D' and D == False:    
            if C == True:
                statement_CD += ' ' * 9 + '[D]'
            else:
                statement_CD = ' ' * 18 + ' ' * 4 + '[D]'
            # Prevent repeat
            D = True        
    print(statement_CD)

    print(('\n' + ' ' * 13 + '{}').format('[ Room 4 ]'))

    if player_hp < 10:
        player_hp = '0' + str(player_hp)

    print('{} {:>29s}'.format('HP', 'Persons'))
    print(('{:2}{:5s} {:>21}').format(player_hp, ' / 15', persons_together))
    print() ## Create new line

def room_2_dark_rooms_creature(box_letters, hide, search, has_creature_appeared, player_hp, persons_together, closeness, box_hidden):
    searching_box = random.choice([box_letters[0], box_letters[1], box_letters[2], box_letters[3]])

    stage_one = ['\nYou heard a soft sound.\n', '\nYou heard loud footsteps.\n'] ##########, '\nThe creature has entered into the room!\n']             ## Closeness 0
    stage_two_soft = ['\nThe soft sound disappeared.\n', 'The sound continues...\n', '\nThe soft sound becomes louder.\n']                ## Closeness 1
    stage_three_loud = ['\nThe sound grew softer.\n', '\nThe sound continues...\n', '\nThe creature has entered into the room!\n']          ## Closeness 2
    stage_four_entered = ['\nThe creature waited in the room.\n', 'The creature has left the room.\n', '\nThe creature searched Box']   ## Closeness 3
    stage_in_box = ['\nThe creature stayed in the box.\n', '\nThe creature came out of the box.\n']                                       ## Closeness 4
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
        room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)

        if closeness != 0:
            message_to_print = stage_one[closeness-1]
            print_out_slowly(message_to_print)
            if hide == False and closeness == 3:
                player_hp -= 3
                if player_hp > 0:
                    time.sleep(time_delay)
                    message_to_print = struck_message
                    print_out_slowly(message_to_print)
                    persons_together = 1
                else:
                    message_to_print = died_message
                    print_out_slowly(message_to_print)
                    player_hp = 0
                has_creature_appeared = False
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

        room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)

        message_to_print = stage_two_soft[closeness]
        print_out_slowly(message_to_print)
    elif closeness == 2:
        time.sleep(time_delay)
        if sound_or_appearance >= 0 and sound_or_appearance <= (15 - persons_risk):
            closeness = 1
        elif sound_or_appearance >= 16 and sound_or_appearance <= (25 - persons_risk):
            closeness = 2
        else:
            closeness = 3
            has_creature_appeared = True

        room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)

        message_to_print = stage_three_loud[closeness - 1]
        print_out_slowly(message_to_print)

        if hide == False and closeness == 3:
            player_hp -= 3
            if player_hp > 0:
                time.sleep(time_delay)
                message_to_print = struck_message
                print_out_slowly(message_to_print)
                persons_together = 1
            else:
                message_to_print = died_message
                print_out_slowly(message_to_print)
                player_hp = 0
            has_creature_appeared = False
            closeness = -1
            time.sleep(time_died_delay)
    elif closeness == 3:
        has_creature_appeared = True
        time.sleep(time_delay)
        if hide == False and search == False:
            room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
            player_hp -= 3
            if player_hp > 0:
                message_to_print = struck_message
                print_out_slowly(message_to_print)
                persons_together = 1

            else:
                message_to_print = died_message
                print_out_slowly(message_to_print)
                player_hp = 0
            has_creature_appeared = False
            closeness = -1
            time.sleep(time_died_delay)
        else:
            if sound_or_appearance >= 0 and sound_or_appearance <= 15:
                closeness = 3
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
                message_to_print = stage_four_entered[0]
                print_out_slowly(message_to_print)
            elif sound_or_appearance >= 16 and sound_or_appearance <= 25:
                closeness = 0
                has_creature_appeared = False
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
                message_to_print = stage_four_entered[1]
                print_out_slowly(message_to_print)
            else:
                closeness = 4
                search = True
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
                message_to_print = stage_four_entered[2] + ' ' + searching_box + '\n'
                print_out_slowly(message_to_print)
                if searching_box == box_hidden:
                    time.sleep(time_delay)
                    print('\nThe creature found you!')
                    time.sleep(time_delay)
                    player_hp -= 3
                    if player_hp > 0:
                        message_to_print = struck_message
                        print_out_slowly(message_to_print)
                        persons_together = 1
                    else:
                        message_to_print = died_message
                        print_out_slowly(message_to_print)
                        player_hp = 0
                    closeness = -1
                    search = False
                    time.sleep(time_died_delay)
    else:  
        ## In-box section
        time.sleep(time_delay)
        if hide == False and search == False:
            room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
            player_hp -= 3
            if player_hp > 0:
                message_to_print = struck_message
                print_out_slowly(message_to_print)
                persons_together = 1
            else:
                message_to_print = died_message
                print_out_slowly(message_to_print)
                player_hp = 0
            has_creature_appeared = False
            closeness = -1
            time.sleep(time_died_delay)
        else:
            if sound_or_appearance >= 0 and sound_or_appearance <= 15:
                closeness = 4
                search = True
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
                message_to_print = stage_in_box[0]
                print_out_slowly(message_to_print)
            else:
                closeness = 3
                search = False
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
                message_to_print = stage_in_box[1]
                print_out_slowly(message_to_print)

                time.sleep(time_delay)
                if hide == False and search == False:
                    player_hp -= 3
                    if player_hp > 0:
                        message_to_print = struck_message
                        print_out_slowly(message_to_print)
                        persons_together = 1
                    else:
                        message_to_print = died_message
                        print_out_slowly(message_to_print)
                        player_hp = 0
                    has_creature_appeared = False
                    closeness = -1
                    time.sleep(time_died_delay)

    return hide, search, has_creature_appeared, player_hp, persons_together, closeness

def room_2_dark_rooms(player_hp, inventory):
    room_2_dark_rooms_intro()
    items_appearing_list = ["fridge", "lion", "elephant tusk", "kfc", "leaf shield", "screwdriver", "stone", "flamethrower"]
    item_type_found = random.choice(items_appearing_list)

    ## Box letters section
    box_letters = ['A', 'A', 'B', 'B', 'C', 'C', 'D', 'D']  ## 2 Letters for shuffling

    ### ALL THE INITIALISING VARIABLES
    user_input = input('Press any key to proceed, or x to quit game: ')
    to_continue = True
    hide = False
    search = False
    has_creature_appeared = False
    closeness = 0
    hide_message = ''
    options_message = ''
    item_found = 0
    rooms_before_exit = 0
    set_rooms = 5
    persons_together = 1
    box_hidden = ''
    edible_healthpack = 2

    user_input = user_input.lower()

    ########################################################
    ################# Only for DEVELOPERS! #################
    ########################################################
    if user_input == 'skip daarrkkroom':           
        return player_hp, inventory, user_input
    ########################################################
    ########################################################

    ## START OF EVERYTHING
    while user_input != 'x' and rooms_before_exit != set_rooms and player_hp > 0:
        if to_continue == True or closeness == -1:
            ## Shuffling box letters. If two same letters at the first 4 element after shuffle, means there's only 3 boxes
            random.shuffle(box_letters)            

            ## Displaying on Screen
            to_continue = False

            if closeness == -1:
                closeness = 0
                has_creature_appeared = False
                room_2_dark_rooms_display(box_letters, hide, search, has_creature_appeared, player_hp, persons_together)
            else:
                if search == True:
                    search = False
                    closeness = 0
                rooms_before_exit += 1
                hide, search, has_creature_appeared, player_hp, persons_together, closeness = room_2_dark_rooms_creature(box_letters, hide, search, has_creature_appeared, player_hp, persons_together, closeness, box_hidden)
        else:
            if user_input != 's' and player_hp > 0:
                hide, search, has_creature_appeared, player_hp, persons_together, closeness = room_2_dark_rooms_creature(box_letters, hide, search, has_creature_appeared, player_hp, persons_together, closeness, box_hidden)
                if closeness != -1:
                    message_to_print = "\nYou came out.\n"
                    print_out_slowly(message_to_print)

        ## Display Messages Section for Items (20,25), People (10, 15), or Healthpack (2, 7)
        if closeness != -1 and player_hp > 0:
            if (item_found >= 20 and item_found <= 25):
                message_to_print = '\nYou entered the room, and found a '+ item_type_found + '!\n'
                print_out_slowly(message_to_print)
                item_type_found = random.choice(items_appearing_list)
            elif (item_found >= 10 and item_found <= 15):
                message_to_print = '\nAn injured person lies at a corner of the room.\n'
                print_out_slowly(message_to_print)
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
                    print_out_slowly(message_to_print)
            elif (item_found >= 2 and item_found <= 7):
                if player_hp < 15 and player_hp > 0:
                    message_to_print = '\nYou found an edible healthpack and ate it!\n+' + (str(15-player_hp) if ((player_hp + edible_healthpack)>15) else str(edible_healthpack)) + ' HP\n'
                    print_out_slowly(message_to_print)
                    if (player_hp + edible_healthpack) > 15:
                        player_hp = 15
                    else:
                        player_hp += edible_healthpack
            item_found = 0

            options_message = "Please enter the next room number to enter the room, \ns to stay, h to hide, or x to quit game: "
            user_input = input(options_message)
            if user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != 'x' and user_input != 'h' and user_input != 's':
                while user_input != '1' and user_input != '2' and user_input != '3' and user_input != '4' and user_input != 'x' and user_input != 'h' and user_input != 's':
                    user_input = input(options_message)

            ## After choosable option has been confirmed
            if user_input.isdigit():          ## IF only 1, 2, 3 or 4
                item_found = random.getrandbits(5) ## 0 to 32
                ## Found item Section
                if (item_found >= 20 and item_found <= 25):
                    player_inv.append(item_type_found)
                to_continue = True
            else:
                ## Hide Section
                if user_input == 'h':
                    while user_input != 'x' and user_input != 'UN-HIDE' and closeness != -1:
                        options_message = 'Please enter the letter of the box to hide in, h to no longer hide, and x to quit game: '
                        box_hidden = input(options_message)
                        if box_hidden == 'x':
                            user_input = 'x'
                        elif box_hidden == 'h':
                            user_input = 'UN-HIDE'
                            box_hidden = ''
                        else:
                            box_hidden = box_hidden.upper()
                            while  box_hidden != box_letters[0] and box_hidden != box_letters[1] and box_hidden != box_letters[2] and box_hidden != box_letters[3] and box_hidden != 'h' and box_hidden != 'x':       ## Loop till get correct option
                                box_hidden = input(options_message)
                                if box_hidden != 'h' and box_hidden != 'x':
                                    box_hidden = box_hidden.upper()

                            if box_hidden == box_letters[0] or box_hidden == box_letters[1] or box_hidden == box_letters[2] or box_hidden == box_letters[3]:
                                user_input = ''
                                ## Displaying on Screen
                                while user_input != 'h' and user_input != 'x' and closeness != -1:
                                    hide = True
                                    hide, search, has_creature_appeared, player_hp, persons_together, closeness = room_2_dark_rooms_creature(box_letters, hide, search, has_creature_appeared, player_hp, persons_together, closeness, box_hidden)
                                    if closeness != -1:
                                        if user_input != 's':
                                            hide_message = '\nYou hid in Box ' + box_hidden + '\n'
                                            print_out_slowly(hide_message)
                                        else:
                                            if player_hp > 0 and closeness != -1:
                                                message_to_print = "\nYou decided to stay...\n"
                                                print_out_slowly(message_to_print)

                                        options_message = "Please enter s to stay, h to no longer hide, and x to quit game: "
                                        user_input = input(options_message)
                                        while  user_input != 's' and user_input != 'h' and user_input != 'x':    
                                            # Loop till a correct option is entered
                                            user_input = input(options_message)
                                if user_input != 'x' or closeness == -1:
                                    user_input = 'UN-HIDE'
                                    hide = False
                                    box_hidden = ''
                    ## Waiting Section
                elif user_input == 's' and closeness != -1:
                    hide, search, has_creature_appeared, player_hp, persons_together, closeness = room_2_dark_rooms_creature(box_letters, hide, search, has_creature_appeared, player_hp, persons_together, closeness, box_hidden)

                    if player_hp > 0:
                        message_to_print = "\nYou decided to stay...\n"
                        print_out_slowly(message_to_print)

    if user_input != 'x' and rooms_before_exit == set_rooms and player_hp > 0:
        message_to_print = "\nCongratulations! You made it!\n"
        print_out_slowly(message_to_print)
        if persons_together > 1:
            message_to_print = '\nThe injured ones have been transferred to a safe place. Terrific!\n'
            print_out_slowly(message_to_print)
            if ((persons_together - 1) * 2 + player_hp) < 14:
                message_to_print = '\nYou found ' + str(persons_together-1) + ' HP packs on the way out and consumed it!\n'
                print_out_slowly(message_to_print)
                player_hp += 2 * (persons_together - 1)
            else:
                message_to_print = '\nYou found 1 BIG HP pack on the way out and consumed it!'
                print_out_slowly(message_to_print)
                player_hp = 15
        else:
            if player_hp < 13:
                message_to_print = '\nYou found a HP pack on the way out and consumed it!\n'
                print_out_slowly(message_to_print)
                player_hp += 2

        message_to_print = '\nYou now have ' + str(player_hp) + ' HP!\nYou have reached the 3rd puzzle room.\n'
        print_out_slowly(message_to_print)

        user_input = ''
        user_input = input('To proceed, enter any key, or enter x to quit game: ')
        user_input = user_input.lower()

        print('')

    return player_hp, inventory, user_input
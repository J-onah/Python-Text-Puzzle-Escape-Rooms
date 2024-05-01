###################################################
#                                                 #
#          Room 1 by Corliss Tay She Jie          #
#          Room 2 by Jonah Yeo Zheng              #
#          Room 3 by Darren Teng Ren Kiat         #
#          Room 4 by Fatima Co Pepito             #
#          Room 5 by Suzette Leo Mei Yen          #
#                                                 #
###################################################

from game_variables import *
from room_1 import * 
from room_2 import * 
from room_3 import * 
from room_4 import * 
from room_5 import * 

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
import time
import random
from game_variables import *

def chu_khan_battle(player_hp, player_atk, player_inv, boss_hp, boss_atk, yn):
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



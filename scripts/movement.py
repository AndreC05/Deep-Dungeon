# -*- coding: utf-8 -*-
"""
Created on Sat Dec 10 13:25:43 2022

@author: 100283438
"""
import random
from monsters import *
from text_colour import *
from create_items import *


def monster_spawn(character, floor_map):
    try:
        all_items()
        if character.floor < 5:
            m_level = 1
            i_level = 0
        elif 10 > character.floor >= 5:
            m_level = 2
            i_level = 0
        elif 15 > character.floor >= 10:
            m_level = 3
            i_level = 1
        elif 20 > character.floor >= 15:
            m_level = 4
            i_level = 1
        elif 25 > character.floor >= 20:
            m_level = 5
            i_level = random.choice(range(0, 3))
        elif 30 > character.floor >= 25:
            m_level = 6
            i_level = random.choice(range(0, 3))
        elif 35 > character.floor >= 30:
            m_level = 7
            i_level = 2
        elif 40 > character.floor >= 35:
            m_level = 8
            i_level = 2
        elif 45 > character.floor >= 40:
            m_level = 9
            i_level = random.choice(range(1, 4))
        elif 50 > character.floor >= 45:
            m_level = 10
            i_level = random.choice(range(1, 4))
        elif character.floor > 50:
            m_level = random.randint(11, 15)
            i_level = 3

        m_gender_list = ["m", "f"]
        m_gender = random.choice(m_gender_list)

        m_name_list = ["Abyssface", "Germling", "Cursefigure", "Poisonbeast", "Bloodfreak"]
        m_name = random.choice(m_name_list)

        m_species_list = ["Goblin", "Orc", "Spider", "Skeleton"]
        m_species = random.choice(m_species_list)

        weapon_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4]
        shield_list = [all_items.shield1, all_items.shield2, all_items.shield3, all_items.shield4]
        helmet_list = [all_items.helmet1, all_items.helmet2, all_items.helmet3, all_items.helmet4]
        armour_list = [all_items.armour1, all_items.armour2, all_items.armour3, all_items.armour4]
        leg_armour_list = [all_items.legarmour1, all_items.legarmour2, all_items.legarmour3, all_items.legarmour4]

        if random.getrandbits(1):
            m_weapon = weapon_list[i_level]
        else:
            m_weapon = None

        if random.getrandbits(1):
            m_shield = shield_list[i_level]
        else:
            m_shield = None

        if random.getrandbits(1):
            m_armour = armour_list[i_level]
        else:
            m_armour = None

        if random.getrandbits(1):
            m_helmet = helmet_list[i_level]
        else:
            m_helmet = None

        if random.getrandbits(1):
            m_leg_armour = leg_armour_list[i_level]
        else:
            m_leg_armour = None

        if m_species == "Spider":
            monster = Spider(m_name, m_gender, m_level)
        elif m_species == "Skeleton":
            monster = Skeleton(m_name, m_gender, m_level, m_helmet, m_weapon, m_shield, m_armour, m_leg_armour)
        elif m_species == "Orc":
            monster = Orc(m_name, m_gender, m_level, m_helmet, m_weapon, m_shield, m_armour, m_leg_armour)
        elif m_species == "Goblin":
            monster = Goblin(m_name, m_gender, m_level, m_helmet, m_weapon, m_shield, m_armour, m_leg_armour)

        monster.x = random.randint(1, floor_map.x_len)
        monster.y = random.randint(1, floor_map.y_len)
    except ValueError:
        print(f"{Colour.red}Error: Value error{Colour.reset}\n")

    return monster


def dungeon_move(player, target, f_map):
    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
    while True:
        try:
            if player.x == target.x and player.y == target.y:
                if target.alive:
                    decision = input(f"You are next to a {Colour.purple}level {target.level} {target.species}"
                                     f"{Colour.reset}. Would you like to battle (battle), inspect the monster "
                                     f"(inspect) or return to the town (run)?\n")
                    if decision.lower() == "battle":
                        player.battle(target)
                        continue
                    elif decision.lower() == "run":
                        player.enter_town()
                        break
                    elif decision.lower() == "inspect":
                        target.monster_display()
                        continue
                    else:
                        print(f"{Colour.red}{decision}{Colour.reset} is not a valid input.\n")
                else:
                    player.next_floor()
                    break

            else:
                if movement.lower() == "up":
                    player.move_up(f_map)
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
                elif movement.lower() == "down":
                    player.move_down(f_map)
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
                elif movement.lower() == "left":
                    player.move_left(f_map)
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
                elif movement.lower() == "right":
                    player.move_right(f_map)
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
                elif movement.lower() == "town":
                    player.enter_town()
                    break
                elif movement.lower() == "inspect":
                    print(f"{Colour.green}You find yourself in a narrow cave and can hear some scary "
                          f"noises around you. It seems that you have company, a {Colour.purple}"
                          f"{target.species}{Colour.green} can be found at "
                          f"{Colour.pink}({target.x},{target.y}){Colour.green}.{Colour.reset}\n")
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
                else:
                    print(f"{Colour.red}{movement}{Colour.reset} is not a valid input.")
                    movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
                    continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            movement = input("Where would you like to move? (up/down/left/right/town/inspect)\n")
            continue

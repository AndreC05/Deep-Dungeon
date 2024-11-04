# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:33:20 2022

@author: Andre Carreira
"""
from player_character import *
from items import *
from monsters import *
from glossary import *
from create_items import *
from leader_board import *
from shop import *
import random


def test1():
    character1 = PlayerCharacter("andre", 21, "M", "human", 183, 85, "black")

    # character1.character_display()

    armour1 = Armour("Leather armour", 500, 5)

    # armour1.display()

    helmet1 = Helmet("Leather helmet", 500, 5)

    # helmet1.display()

    helmet2 = Helmet("Iron helmet", 900, 8)

    # helmet2.display()

    weapon1 = Weapon("Short sword", 400, 3)
    # weapon1.display()

    character1.pickup_item(helmet1)
    character1.pickup_item(helmet1)

    character1.change_equipment(helmet1, "head")

    character1.save_game()

    # character1.character_display()

    character1.pickup_item(helmet1)

    # character1.character_display()

    # character1.change_equipment(helmet1, "not a place")

    character1.character_display()

    character1.pickup_item(helmet2)

    character1.save_game()

    character1.pickup_item(helmet2)

    character1.pickup_item(helmet2)

    character1.max_hp = 100

    character1.character_display()

    character1.load_game()

    character1.character_display()

    print(f"{character1.head.item_type}")
    print(f"{character1.head.item_value}")


def test2():
    weapon1 = Weapon("Short sword", 400, 3)
    weapon1.display()
    Goblin1 = Goblin("goblin1", "M", 50, 10, 1, 25, 5, 6, None, None, weapon1, None, None)
    Goblin1.monster_display()
    print(f"{Goblin1.drop_equipment()}")

    glossary()


def test3():
    character1 = PlayerCharacter("andre5", 21, "M", "human", 183, 85, "black")

    all_items()

    item_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4, all_items.sword5,
                 all_items.sword6, all_items.sword7, all_items.sword8, all_items.shield1, all_items.shield2,
                 all_items.shield3, all_items.shield4, all_items.shield5, all_items.helmet1, all_items.helmet2,
                 all_items.helmet3, all_items.helmet4, all_items.armour1, all_items.armour2, all_items.armour3,
                 all_items.armour4, all_items.legarmour1, all_items.legarmour2, all_items.legarmour3,
                 all_items.legarmour4]

    character1.pickup_item(all_items.sword2)
    character1.pickup_item(all_items.shield1)
    character1.pickup_item(all_items.helmet1)
    character1.pickup_item(all_items.armour1)
    character1.pickup_item(all_items.legarmour1)
    character1.pickup_item(all_items.sword2)

    all_items.sword2.display()

    character1.character_display()

    character1.change_equipment(all_items.sword2, "R_hand")
    character1.change_equipment(all_items.shield1, "L_hand")
    character1.change_equipment(all_items.helmet1, "head")
    character1.change_equipment(all_items.armour1, "chest")
    character1.change_equipment(all_items.legarmour1, "legs")
    character1.change_equipment(all_items.legarmour1, "head")
    character1.change_equipment(all_items.sword2, "head")

    character1.character_display()

    goblin1 = Goblin("goblin1", "M", 1, None, None, all_items.sword1, None, None)
    goblin1.monster_display()
    character1.character_stats_display()

    character1.battle(goblin1)
    character1.battle(goblin1)
    character1.battle(goblin1)
    character1.battle(goblin1)
    character1.battle(goblin1)

    spider1 = Spider("spider1", "F", 3)

    character1.battle(spider1)
    character1.battle(spider1)
    character1.battle(spider1)
    character1.battle(spider1)
    character1.battle(spider1)

    sell_item(character1, "Short sword")

    buy_item(character1, "Broken sword", item_list)

    character1.character_display()
    character1.save_game()


def test4():
    leader_board()

def test5():
    m_name = ["Abyssface", "Germling", "Cursefigure", "Poisonbeast", "Bloodfreak"]
    print(random.choice(m_name))

test3()

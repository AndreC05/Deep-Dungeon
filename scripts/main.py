# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 18:11:43 2022

@author: 100283438
"""
from character_check import *
from player_character import *
from create_items import *
from glossary import *
from help import *
from inn import *
from intro import *
from items import *
from leader_board import *
from map import *
from monsters import *
from movement import *
from shop import *
from text_colour import *


def main():
    all_items()

    item_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4, all_items.sword5,
                 all_items.sword6, all_items.sword7, all_items.sword8, all_items.shield1, all_items.shield2,
                 all_items.shield3, all_items.shield4, all_items.shield5, all_items.helmet1, all_items.helmet2,
                 all_items.helmet3, all_items.helmet4, all_items.armour1, all_items.armour2, all_items.armour3,
                 all_items.armour4, all_items.legarmour1, all_items.legarmour2, all_items.legarmour3,
                 all_items.legarmour4]
    intro()
    player_character = new_load_character()
    while True:
        try:
            if player_character.location == "town":
                comm = input(f"What would you like to do, {Colour.cyan}{player_character.name}{Colour.reset}? "
                             f"(type {Colour.pink}help{Colour.reset} for available commands)\n")

                if comm.lower() == "help":
                    town_help()
                    continue

                elif comm.lower() == "glossary":
                    glossary()
                    continue

                elif comm.lower() == "change equipment":
                    equip = input("Select an item you wish to equip:\n")
                    location = input("Select a location to equip that item:\n")
                    equip_temp = equip.lower().strip(" ")
                    invent = [i.name.lower().strip(" ") for i in player_character.inventory]
                    if equip_temp in invent:
                        # if the item is in the inventory
                        for i in item_list:
                            if i.name.lower().strip(" ") == equip_temp:
                                equip = i
                                player_character.change_equipment(equip, location)
                    else:
                        print(f"{Colour.orange}{equip}{Colour.reset} is not in your inventory.")
                    continue

                elif comm.lower() == "go to dungeon":
                    player_character.enter_dungeon()
                    continue

                elif comm.lower() == "save":
                    player_character.save_game()
                    print("The game has been saved!\n")
                    continue

                elif comm.lower() == "load":
                    player_character.load_game()
                    print("The game has been loaded!\n")
                    continue

                elif comm.lower() == "my stats":
                    player_character.character_stats_display()
                    continue

                elif comm.lower() == "my info":
                    player_character.character_display()
                    continue

                elif comm.lower() == "inn":
                    inn_recovery(player_character)
                    continue

                elif comm.lower() == "shop":
                    while True:
                        try:
                            comm3 = input("Would you like to buy or sell an item? (type back to return)\n")

                            if comm3.lower() == "buy":
                                while True:
                                    try:
                                        item_to_buy = input("What item would you like to buy? "
                                                            "(type list for items available)\n")
                                        if item_to_buy == "list":
                                            print("List of items available:")
                                            for i in item_list:
                                                print(f"{Colour.orange}{i.name}{Colour.reset}")
                                            continue
                                        else:
                                            buy_item(player_character, item_to_buy, item_list)
                                            break
                                    except ValueError:
                                        print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                                        continue
                                break
                            elif comm3.lower() == "sell":
                                while True:
                                    try:
                                        item_to_sell = input("What item would you like to sell? (type "
                                                             "list for items in inventory)\n")
                                        if item_to_sell == "list":
                                            player_character.inv_list()
                                            continue
                                        else:
                                            sell_item(player_character, item_to_sell)
                                            break
                                    except ValueError:
                                        print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                                        continue
                                break
                            elif comm3.lower() == "back":
                                break
                            else:
                                print(f"{Colour.purple}{comm3}{Colour.reset} is not a valid input.\n")
                        except ValueError:
                            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                            continue
                    continue

                elif comm.lower() == "my location":
                    player_character.character_location()
                    continue

                elif comm.lower() == "inspect":
                    while True:
                        try:
                            comm4 = input("What would you like to inspect? (location/item/back)\n")
                            if comm4.lower() == "location":
                                print(f"{Colour.green}Around you there are various small buildings. "
                                      f"You can identify a shop and an inn among them.{Colour.reset}\n")
                                continue
                            elif comm4.lower() == "back":
                                break
                            elif comm4.lower() == "item":
                                comm5 = input("What item in your inventory would you like to inspect? (type"
                                              " list for items in inventory)\n")
                                if comm5.lower() == "list":
                                    player_character.inv_list()
                                else:
                                    item_temp = comm5.lower().strip(" ")
                                    invent = [i.name.lower().strip(" ") for i in player_character.inventory]
                                    if item_temp in invent:
                                        # if the item is in the inventory
                                        for i in player_character.inventory:
                                            if i.name.lower().strip(" ") == item_temp:
                                                item = i
                                        item.display()
                                    else:
                                        print(
                                            f"{Colour.orange}{comm5}{Colour.reset} could not be found in your "
                                            f"inventory.\n")
                                continue
                            else:
                                print(f"{Colour.red}{comm4}{Colour.reset} is not a valid input\n")
                                continue
                        except ValueError:
                            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                            continue

                elif comm.lower() == "exit":
                    while True:
                        try:
                            comm2 = input(f"{Colour.red}Would you like to save the game? (Y/N){Colour.reset}\n")
                            if comm2.lower() == "y":
                                player_character.save_game()
                                leader_board()
                                print("The program will exit in 15 seconds")
                                time.sleep(15)
                                sys.exit(0)
                            elif comm2.lower() == "n":
                                leader_board()
                                print("The program will exit in 15 seconds")
                                time.sleep(15)
                                sys.exit(0)
                            else:
                                print(f"{Colour.red}Not a valid input.{Colour.reset}\n")
                                continue
                        except ValueError:
                            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                            continue
                else:
                    print(f"{comm} is not a valid input!\n")
            elif player_character.location == "dungeon":
                comm6 = input(f"What would you like to do, {Colour.cyan}{player_character.name}{Colour.reset}? "
                              f"(type {Colour.pink}help{Colour.reset} for available commands)\n")

                if comm6.lower() == "help":
                    dungeon_help()
                    continue

                elif comm6.lower() == "change equipment":
                    equip = input("Select an item you wish to equip:\n")
                    location = input("Select a location to equip that item:\n")
                    equip_temp = equip.lower().strip(" ")
                    invent = [i.name.lower().strip(" ") for i in player_character.inventory]
                    if equip_temp in invent:
                        # if the item is in the inventory
                        for i in item_list:
                            if i.name.lower().strip(" ") == equip_temp:
                                equip = i
                                player_character.change_equipment(equip, location)
                    else:
                        print(f"{Colour.orange}{equip}{Colour.reset} is not a valid equipment.")
                    continue

                elif comm6.lower() == "glossary":
                    glossary()
                    continue

                elif comm6.lower() == "go to town":
                    player_character.enter_town()
                    continue

                elif comm6.lower() == "save":
                    player_character.save_game()
                    print("The game has been saved!\n")
                    continue

                elif comm6.lower() == "load":
                    player_character.load_game()
                    print("The game has been loaded!\n")
                    continue

                elif comm6.lower() == "my stats":
                    player_character.character_stats_display()
                    continue

                elif comm6.lower() == "my info":
                    player_character.character_display()
                    continue

                elif comm6.lower() == "my location":
                    player_character.character_location()
                    continue

                elif comm6.lower() == "move":
                    f_map = Map()
                    monster = monster_spawn(player_character, f_map)
                    dungeon_move(player_character, monster, f_map)
                    continue

                elif comm6.lower() == "inspect":
                    while True:
                        try:
                            comm7 = input("What would you like to inspect? (location/item/back)\n")
                            if comm7.lower() == "location":
                                print(f"{Colour.green}You find yourself in a narrow cave and can hear some scary "
                                      f"noises around you. It seems that you have company.{Colour.reset}\n")
                                continue
                            elif comm7.lower() == "back":
                                break
                            elif comm7.lower() == "item":
                                comm8 = input("What item in your inventory would you like to inspect? (type"
                                              " list for items in inventory)\n")
                                if comm8.lower() == "list":
                                    player_character.inv_list()
                                else:
                                    item_temp = comm8.lower().strip(" ")
                                    invent = [i.name.lower().strip(" ") for i in player_character.inventory]
                                    if item_temp in invent:
                                        # if the item is in the inventory
                                        for i in player_character.inventory:
                                            if i.name.lower().strip(" ") == item_temp:
                                                item = i
                                        item.display()
                                    else:
                                        print(
                                            f"{Colour.orange}{comm8}{Colour.reset} could not be found in your "
                                            f"inventory.\n")
                                continue
                            else:
                                print(f"{Colour.red}{comm7}{Colour.reset} is not a valid input\n")
                                continue
                        except ValueError:
                            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                            continue

                elif comm6.lower() == "exit":
                    while True:
                        try:
                            comm9 = input(f"{Colour.red}Would you like to save the game? (Y/N){Colour.reset}\n")
                            if comm9.lower() == "y":
                                player_character.save_game()
                                leader_board()
                                print("The program will exit in 15 seconds")
                                time.sleep(15)
                                sys.exit(0)
                            elif comm9.lower() == "n":
                                leader_board()
                                print("The program will exit in 15 seconds")
                                time.sleep(15)
                                sys.exit(0)
                            else:
                                print(f"{Colour.red}Not a valid input.{Colour.reset}\n")
                                continue
                        except ValueError:
                            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
                            continue
                else:
                    print(f"{comm6} is not a valid input!\n")

            else:
                player_character.save_game()
                print(f"{Colour.red}The program will exit in 15 seconds due to an unexpected error{Colour.reset}")
                time.sleep(15)
                sys.exit(0)

        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}\n")
            continue


if __name__ == "__main__":
    main()

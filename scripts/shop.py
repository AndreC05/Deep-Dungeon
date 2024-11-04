# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 21:29:03 2022

@author: 100283438
"""
from text_colour import *
from player_character import *
from items import *


def sell_item(character, item):
    while True:
        try:
            if item.lower() == "back":
                break
            else:
                item_temp = item.lower().strip(" ")
                invent = [i.name.lower().strip(" ") for i in character.inventory[:]]
                if item_temp in invent:
                    # if the item is in the inventory
                    for i in character.inventory:
                        if i.name.lower().strip(" ") == item_temp:
                            item = i
                    for index1, item1 in enumerate(character.inventory[:]):
                        if item1.name == item.name:
                            break
                    character.gold = character.gold + (item.worth / 4)
                    del character.inventory[index1]
                    # remove the item sold from the inventory and add 1/4 * worth of item to player gold
                    print(f"You have sold {Colour.orange}{item}{Colour.reset} for {Colour.yellow}{item.worth / 4}"
                          f"{Colour.reset} gold.\n")
                    item = input(f"Please select a different item to sell or type back to return.\n")
                    continue
                else:
                    # if the item to sell is not in the player inventory print a message
                    item = input(f"{Colour.orange}{item}{Colour.reset} is not in your inventory. Please select a "
                                 f"different item to sell or type back to return.\n")
                    continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            item = input(f"Please select a different item to sell or type back to return.\n")
            continue


def buy_item(character, item, item_list):
    while True:
        try:
            if item.lower() == "back":
                # if player inputs back return
                break
            else:
                item_temp = item.lower().strip(" ")
                invent = [i.name.lower().strip(" ") for i in item_list]
                if item_temp in invent:
                    # if the item is in the items to sell list
                    for i in item_list:
                        if i.name.lower().strip(" ") == item_temp:
                            item = i
                    if character.gold >= item.worth:
                        # if a player has more gold that the worth of the item to buy
                        character.gold = character.gold - item.worth
                        # remove item worth from player gold
                        character.inventory.append(item)
                        # add item to player inventory
                        print(f"You have bought {Colour.orange}{item}{Colour.reset} for {Colour.yellow}{item.worth}"
                              f"{Colour.reset}gold. You have {Colour.yellow}{character.gold}{Colour.reset} "
                              f"gold remaining.\n")
                        item = input(f"Please select a different item to buy or type back to return.\n")
                        continue
                    else:
                        # if the player doesn't have enough gold print a message
                        print(f"You don't have enough gold to buy {Colour.orange}{item}{Colour.reset}. It costs "
                              f"{Colour.yellow}{item.worth}{Colour.reset} gold and you have {Colour.yellow}"
                              f"{character.gold}{Colour.reset} gold remaining\n")
                        item = input(f"Please select a different item to buy or type back to return.\n")
                        continue
                else:
                    # if the item indicated by the player is not present in the shop print a message
                    item = input(f"{Colour.orange}{item}{Colour.reset} is not available to be bought. Please select a "
                                 f"different item to buy or type back to return.\n")
                    continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            item = input(f"Please select a different item to buy or type back to return.\n")
            continue

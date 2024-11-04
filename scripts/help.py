# -*- coding: utf-8 -*-
"""
Created on Mon Dec 12 17:02:56 2022

@author: Andre Carreira
"""
from text_colour import *


def town_help():
    town_comm_dict = {"help": "list of available commands for this location",
                      "glossary": "display glossary of monsters",
                      "save": "save current game state",
                      "load": "load previous game state",
                      "go to dungeon": "enter the dungeon",
                      "my stats": "display current stats for the player character",
                      "my info": "display all the information for the player character",
                      "inspect": "inspect items or the location around you",
                      "change equipment": "Equip an item in your inventory to your character",
                      "inn": "recover health at inn",
                      "shop": "buy or sell items",
                      "my location": "display current location and coordinated of the player character",
                      "exit": "exit the game"
                      }

    print(f"{Colour.pink}List of commands:{Colour.reset}\n")
    for comm, info in town_comm_dict.items():
        print(f"{Colour.pink}{comm}: {info}{Colour.reset}")
        # print every entry in the help list


def dungeon_help():
    town_comm_dict = {"help": "list of available commands for this location",
                      "move": "move around the dungeon floor and battle monsters",
                      "glossary": "display glossary of monsters",
                      "save": "save current game state",
                      "load": "load previous game state",
                      "go to town": "return to town",
                      "my stats": "display current stats for the player character",
                      "my info": "display all the information for the player character",
                      "inspect": "inspect items or the location around you",
                      "change equipment": "Equip an item in your inventory to your character",
                      "my location": "display current location and coordinated of the player character",
                      "exit": "exit the game"
                      }

    print(f"{Colour.pink}List of commands:{Colour.reset}\n")
    for comm, info in town_comm_dict.items():
        print(f"{Colour.pink}{comm}: {info}{Colour.reset}")
        # print every entry in the help list

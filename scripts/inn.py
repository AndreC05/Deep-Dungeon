# -*- coding: utf-8 -*-
"""
Created on Sat Dec  3 01:07:15 2022

@author: Andre Carreira
"""
from text_colour import *
from player_character import *


def inn_recovery(character):
    p_in = input(f"Hi {Colour.cyan}{character.name}{Colour.reset}, would you like to recover your health for "
                 f"{Colour.yellow}50{Colour.reset} gold? (Y/N)")
    # ask for player input
    while True:
        try:
            if p_in.lower() == "y":
                # if player input y
                if character.gold >= 50:
                    # if player gold is more than 50
                    character.current_hp = character.max_hp
                    character.gold = character.gold - 50
                    # recover player health to max and remove 50 gold
                    print(f"{Colour.cyan}{character.name}{Colour.reset} you have recovered to {Colour.cyan}"
                          f"{character.current_hp}{Colour.reset} hp. Come back again!\n")
                    # print message and return
                    break
                else:
                    # if player doesn't have enough gold print a message
                    print(f"{Colour.cyan}{character.name}{Colour.reset} you only have {Colour.yellow}{character.gold}"
                          f"{Colour.reset} gold. That is not enough. Come back later!\n")
                    break

            elif p_in.lower() == "n":
                # if player input n, print a message and return
                print("Come back again!")
                break

            else:
                # if player input in not valid, print a message and ask player for new input
                print(f"{Colour.red}{p_in}{Colour.reset} is not a valid command. Please type Y or N.\n")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            p_in = input("Please input Y or N: \n")
            continue

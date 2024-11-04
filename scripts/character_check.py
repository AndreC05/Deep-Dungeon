# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:32:34 2022

@author: Andre Carreira
"""
from text_colour import *
from player_character import *


def name_check(name):
    while True:
        try:
            if len(name) < 5 or len(name) > 12:
                print("Your name must have between 5 and 12 characters.")
                name = input("Input a new name for your character:\n")
                continue
            elif any(character.isspace() for character in name):
                print("Your name must not have blank spaces.")
                name = input("Input a new name for your character:\n")
                continue
            else:
                print(f"Your character's name is: {name}.")
                break
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            name = input("Input a new name for your character:\n")
            continue
    return name


def age_check(age):
    while True:
        try:
            if str(age).isdigit():
                age = int(age)
                if age < 18:
                    print("Your character must be 18 or older.")
                    age = input("Please input a valid number: ")
                    continue
                elif age > 50:
                    print("Your character must be 50 or younger.")
                    age = input("Please input a valid number: ")
                    continue
                else:
                    print(f"Your character's age is: {age}.")
                    break
            else:
                print("Not a valid input.")
                age = input("Please input a valid number: ")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            age = input("Please input a valid number: ")
            continue
    return age


def gender_check(gender):
    while True:
        try:
            if gender.lower() == "m" or gender.lower() == "f":
                print(f"Your character's gender is: {gender.upper()}")
                break
            else:
                gender = input("Please input m or f.")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            gender = input("Please input m or f:\n")
            continue
    return gender.upper()


def species_check(species):
    while True:
        try:
            if species.lower() == "human" or species.lower() == "elf" or species.lower() == "dwarf":
                print(f"Your character's species is: {species}")
                break
            else:
                species = input("Not a valid species, please type human, elf or dwarf.\n")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            species = input("Please type human, elf or dwarf.\n")
            continue
    return species.title()


def height_check(height):
    while True:
        try:
            if str(height).isdigit():
                height = int(height)
                if height < 100:
                    print("Your character must be 100 cm or taller.")
                    height = input("Please input a valid number: ")
                    continue
                elif height > 250:
                    print("Your character must be 250 cm or smaller.")
                    height = input("Please input a valid number: ")
                    continue
                else:
                    print(f"Your character's height is: {height}.")
                    break
            else:
                print("Not a valid input.")
                height = input("Please input a valid number: ")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            height = input("Please input a valid number: ")
            continue
    return height


def weight_check(weight):
    while True:
        try:
            if str(weight).isdigit():
                weight = int(weight)
                if weight < 40:
                    print("Your character must be 40 Kg or heavier.")
                    weight = input("Please input a valid number: ")
                    continue
                elif weight > 150:
                    print("Your character must be 150 Kg or lighter.")
                    weight = input("Please input a valid number: ")
                    continue
                else:
                    print(f"Your character's weight is: {weight}.")
                    break
            else:
                print("Not a valid input.")
                weight = input("Please input a valid number: ")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            weight = input("Please input a valid number: ")
            continue
    return weight


def hair_check(hair_colour):
    while True:
        try:
            if hair_colour.lower() == "black" or hair_colour.lower() == "brown" or hair_colour.lower() == "grey":
                print(f"Your character's hair colour is: {hair_colour}")
                break
            else:
                hair_colour = input("Not a valid hair colour, please type black, brown or grey.\n")
                continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            hair_colour = input("Please type black, brown or grey.\n ")
            continue
    return hair_colour.title()


def character_values():
    values_list = []
    char_name = input("Input a name for your character:\n")
    char_name = name_check(char_name)
    values_list.append(char_name)
    char_age = input("Input the age of your character:\n")
    char_age = age_check(char_age)
    values_list.append(char_age)
    char_gender = input("Input a gender for your character:\n")
    char_gender = gender_check(char_gender)
    values_list.append(char_gender)
    char_species = input("Select your species from: human, elf, dwarf.\n")
    char_species = species_check(char_species)
    values_list.append(char_species)
    char_height = input("Input your character's height:\n")
    char_height = height_check(char_height)
    values_list.append(char_height)
    char_weight = input("Input your character's weight:\n")
    char_weight = weight_check(char_weight)
    values_list.append(char_weight)
    char_hair_colour = input("Input your character's hair colour:\n")
    char_hair_colour = hair_check(char_hair_colour)
    values_list.append(char_hair_colour)

    return values_list


def new_load_character():
    while True:
        try:
            load_or_new = input(f"{Colour.green}Please type {Colour.pink}new{Colour.green} to create a new character or "
                                f"{Colour.pink}load{Colour.green} to load a previous character:{Colour.reset}\n")
            if load_or_new.lower() == "new":
                p_list = character_values()
                p_name = p_list[0]
                dir1 = os.getcwd()
                save_dir = join(dir1, "../saves")

                all_files = []

                for file in os.listdir(save_dir):
                    if isfile(join(save_dir, file)):
                        all_files.append(file)
                        # join all save files into a list

                load_name = p_name + "_save"

                if load_name in all_files:
                    print(f"{Colour.green}A character with that name already exists{Colour.reset}\n")
                else:
                    p_character = PlayerCharacter(p_list[0], p_list[1], p_list[2], p_list[3], p_list[4], p_list[5], p_list[6])
                    print(f"{Colour.green}Welcome, {Colour.cyan}{p_character.name}{Colour.reset}\n")
                    break
            elif load_or_new.lower() == "load":
                p_name = input(f"{Colour.green}Please input the name of the character you wish to load:{Colour.reset}\n")
                dir1 = os.getcwd()
                save_dir = join(dir1, "../saves")

                all_files = []

                for file in os.listdir(save_dir):
                    if isfile(join(save_dir, file)):
                        all_files.append(file)
                        # join all save files into a list

                load_name = p_name + "_save"

                if load_name in all_files:
                    p_character = PlayerCharacter(p_name, None, None, None, None, None, None)
                    p_character.load_game()
                    p_character.location = "town"
                    # spawn player character in town when loading game from main menu
                    print(f"{Colour.green}Welcome back, {Colour.cyan}{p_name}{Colour.reset}\n")
                    break
                else:
                    print(f"{Colour.green}A save file for {Colour.cyan}{p_name}{Colour.green}, "
                          f"could not be found.{Colour.reset}\n")
                    continue
        except ValueError:
            print(f"{Colour.red}Your input is not valid!{Colour.reset}")
            continue

    return p_character

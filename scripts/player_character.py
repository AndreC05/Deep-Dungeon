# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 18:44:42 2022

@author: Andre Carreira
"""
import time
from items import *
from monsters import *
import os.path
import sys
import json
from text_colour import *
from leader_board import *
from create_items import *


def json_load(data):
    temp_list = []
    if data is not None:
        for key, value in data.items():
            if key == "name":
                temp_list.append(value)
            elif key == "worth":
                temp_list.append(value)
            elif key == "item_value":
                temp_list.append(value)
            elif key == "item_type":
                temp_list.append(value)
    else:
        return None
    return temp_list


class PlayerCharacter:

    def __init__(self, name, age, gender, species, height, weight, hair_colour):
        # basic info
        self.name = name
        self.age = age
        self.gender = gender
        self.species = species
        self.height = height
        self.weight = weight
        self.hair_colour = hair_colour
        # stats
        self.level = 1
        self.max_hp = 50
        self.current_hp = 50
        self.strength = 10
        self.defence = 10
        # gold and points
        self.gold = 0
        self.points = 0
        # exp
        self.current_exp = 0
        self.max_exp = 1000
        # equipment
        self.head = None
        self.R_hand = None
        self.L_hand = None
        self.chest = None
        self.legs = None
        # inventory
        self.inventory = []
        # location
        self.location = "town"
        self.floor = 1
        self.x = 0
        self.y = 0

    def character_info(self):
        # place all the character information in a dictionary
        return {"Name": self.name,
                "Level": self.level,
                "Current Exp": self.current_exp,
                "Exp to next level": self.max_exp,
                "Age": self.age,
                "Gender": self.gender,
                "Species": self.species,
                "Height": self.height,
                "Weight": self.weight,
                "Hair_colour": self.hair_colour,
                "Current Hp": self.current_hp,
                "Maximum Hp": self.max_hp,
                "Strength": self.strength,
                "Defence": self.defence,
                "Gold": self.gold,
                "Equipment": {"Head": self.head,
                              "L_Hand": self.L_hand,
                              "R_Hand": self.R_hand,
                              "Chest": self.chest,
                              "Legs": self.legs},
                "Inventory": self.inventory}

    def character_display(self):
        # display the dictionary created in character_info() with text of different colour
        time.sleep(1)
        # wait for 1 second to display
        try:
            for key, value in self.character_info().items():
                if key == "Equipment":
                    print(f"{Colour.cyan}{Colour.bold}{key}:{Colour.reset}")
                    for a, b in value.items():
                        print(f"    {Colour.pink}{Colour.bold}{a}:{Colour.reset}{Colour.pink} {b}{Colour.reset}")
                elif key == "Inventory":
                    print(f"{Colour.cyan}{Colour.bold}{key}:{Colour.reset}")
                    if not value:
                        print(f"    {Colour.orange}Empty{Colour.reset}")
                    else:
                        for i in value:
                            print(f"    {Colour.orange}{i}{Colour.reset}")
                else:
                    print(f"{Colour.cyan}{Colour.bold}{key}:{Colour.reset}{Colour.cyan} {value}{Colour.reset}")
        except IndexError:
            print(f"{Colour.red}Error: IndexError{Colour.reset}")

        dir1 = os.getcwd()
        resource_dir = os.path.join(dir1, "../resources")
        path = os.path.join(resource_dir, "player.txt")
        # get path to player image file

        try:
            with open(path, "r") as file:
                for line in file:
                    print(line.rstrip())
                    # print player image
            file.close()
        except FileNotFoundError:
            print(f"{Colour.red}Error: File not found.{Colour.reset}\n")

    def character_stats_display(self):
        # display only the stats of a character and the attack and defence power after adding equipment stats
        time.sleep(1)
        # wait for 1 second to display

        player_damage = self.strength
        player_defence = self.defence

        if self.R_hand is not None:
            if self.R_hand.item_type == "Weapon":
                player_damage = player_damage + self.R_hand.item_value
                # add power of weapon to the attack points
        if self.L_hand is not None:
            if self.L_hand.item_type == "Weapon":
                player_damage = player_damage + self.L_hand.item_value
                # add power of weapon to the attack points

        if self.head is not None:
            player_defence = player_defence + self.head.item_value
            # add helmet points to the defence points
        if self.chest is not None:
            player_defence = player_defence + self.chest.item_value
            # add armour points to the defence points
        if self.legs is not None:
            player_defence = player_defence + self.legs.item_value
            # add leg armour points to the defence points
        if self.R_hand is not None:
            if self.R_hand.item_type == "Shield":
                player_defence = player_defence + self.R_hand.item_value
                # add shield points to the defence points
        if self.L_hand is not None:
            if self.L_hand.item_type == "Shield":
                player_defence = player_defence + self.L_hand.item_value
                # add shield points to the defence points

        print(f"{Colour.bold}{Colour.blue}Your stats are:{Colour.reset}")
        for key, value in self.character_info().items():
            if key == "Current Hp" or key == "Maximum Hp" or key == "Strength" or key == "Defence":
                print(f"{Colour.blue}{Colour.bold}{key}:{Colour.reset}{Colour.blue} {value}{Colour.reset}")
        print(f"{Colour.blue}{Colour.bold}Attack points: {Colour.reset}{Colour.blue}{player_damage}{Colour.reset}")
        print(f"{Colour.blue}{Colour.bold}Armour points: {Colour.reset}{Colour.blue}{player_defence}{Colour.reset}")

    def character_location(self):
        # print the current location of the character
        print(f"{Colour.cyan}Location: {self.location}{Colour.reset}")
        if self.location == "dungeon":
            print(f"{Colour.cyan}Current floor: {self.floor}\nCoordinates: ({self.x},{self.y}){Colour.reset}\n")

    def change_equipment(self, item, location):
        all_items()

        item_list = [all_items.sword1, all_items.sword2, all_items.sword3, all_items.sword4, all_items.sword5,
                     all_items.sword6, all_items.sword7, all_items.sword8, all_items.shield1, all_items.shield2,
                     all_items.shield3, all_items.shield4, all_items.shield5, all_items.helmet1, all_items.helmet2,
                     all_items.helmet3, all_items.helmet4, all_items.armour1, all_items.armour2, all_items.armour3,
                     all_items.armour4, all_items.legarmour1, all_items.legarmour2, all_items.legarmour3,
                     all_items.legarmour4]
        while True:
            try:
                if isinstance(item, str):
                    item_temp = item.lower().strip(" ")
                    invent = [i.name.lower().strip(" ") for i in item_list]
                    if item_temp in invent:
                        # if the item is in the items list
                        for i in item_list:
                            if i.name.lower().strip(" ") == item_temp:
                                item = i
                elif not isinstance(item, str):
                    item_temp = item.name.lower().strip(" ")
                    invent = [i.name.lower().strip(" ") for i in item_list]
                    if item_temp in invent:
                        # if the item is in the items list
                        for i in item_list:
                            if i.name.lower().strip(" ") == item_temp:
                                item = i

                for index_item, item1 in enumerate(self.inventory):
                    if item1.name == item.name:
                        index1 = index_item
                        break

                if location.lower() == "head":
                    # if the location selected is the head continue
                    if item.item_type == "Helmet":
                        # if the equipment to equip is a helmet continue
                        if self.head is not None:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.inventory.append(self.head)
                            # if the equipment slot is not empty return the current piece of equipment to the
                            # inventory
                            self.head = item
                            # change the equipment in the head area to the desired piece of equipment
                            break
                        else:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.head = item
                            # if the equipment slot is empty just equip the desired piece of equipment
                            break
                    else:
                        # if type of equipment is not helmet ask user to input a different location to equip the
                        # item
                        location = input(
                            f"{Colour.green}{location}{Colour.reset} is not a valid location for a "
                            f"{Colour.orange}{item.item_type}{Colour.reset}, please input a different "
                            f"location to equip that piece of equipment (or type back to cancel).\n")
                        continue

                elif location.lower() == "l_hand" or location.lower() == "left hand":
                    # if the location selected is the left hand continue
                    if item.item_type == "Weapon" or item.item_type == "Shield":
                        # if the equipment to equip is a weapon or shield continue
                        if self.L_hand is not None:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.inventory.append(self.L_hand)
                            # if the equipment slot is not empty return the current piece of equipment to the
                            # inventory
                            self.L_hand = item
                            # change the equipment in the left hand area to the desired piece of equipment
                            break
                        else:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.L_hand = item
                            # if the equipment slot is empty just equip the desired piece of equipment
                            break
                    else:
                        # if the type of equipment is not a weapon or shield ask user to input a different
                        # location to equip the item
                        location = input(
                            f"{Colour.green}{location}{Colour.reset} is not a valid location for a "
                            f"{Colour.orange}{item.item_type}{Colour.reset}, please input a different "
                            f"location to equip that piece of equipment (or type back to cancel).\n")
                        continue

                elif location.lower() == "r_hand" or location.lower() == "right hand":
                    # if the location selected is the right hand continue
                    if item.item_type == "Weapon" or item.item_type == "Shield":
                        # if the equipment to equip is a weapon or shield continue
                        if self.R_hand is not None:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.inventory.append(self.R_hand)
                            # if the equipment slot is not empty return the current piece of equipment to the
                            # inventory
                            self.R_hand = item
                            # change the equipment in the right hand area to the desired piece of equipment
                            break
                        else:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.R_hand = item
                            # if the equipment slot is empty just equip the desired piece of equipment
                            break
                    else:
                        # if the type of equipment is not a weapon or shield ask user to input a different
                        # location to equip the item
                        location = input(
                            f"{Colour.green}{location}{Colour.reset} is not a valid location for a "
                            f"{Colour.orange}{item.item_type}{Colour.reset}, please input a different "
                            f"location to equip that piece of equipment (or type back to cancel).\n")
                        continue

                elif location.lower() == "chest":
                    # if the location selected is the chest continue
                    if item.item_type == "Armour":
                        # if the equipment to equip is an armour continue
                        if self.chest is not None:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.inventory.append(self.chest)
                            # if the equipment slot is not empty return the current piece of equipment to the
                            # inventory
                            self.chest = item
                            # change the equipment in the chest area to the desired piece of equipment
                            break
                        else:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.chest = item
                            # if the equipment slot is empty just equip the desired piece of equipment
                            break
                    else:
                        # if the type of equipment is not an armour ask user to input a different location to
                        # equip the item
                        location = input(
                            f"{Colour.green}{location}{Colour.reset} is not a valid location for a "
                            f"{Colour.orange}{item.item_type}{Colour.reset}, please input a different "
                            f"location to equip that piece of equipment (or type back to cancel).\n")
                        continue

                elif location.lower() == "legs":
                    # if the location selected are the legs continue
                    if item.item_type == "Leg armour":
                        # if the equipment to equip is leg armour continue
                        if self.legs is not None:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.inventory.append(self.legs)
                            # if the equipment slot is not empty return the current piece of equipment to the
                            # inventory
                            self.legs = item
                            # change the equipment in the leg area to the desired piece of equipment
                            break
                        else:
                            del self.inventory[index1]
                            # remove the item just equipped from the inventory
                            self.legs = item
                            # if the equipment slot is empty just equip the desired piece of equipment
                            break
                    else:
                        # if the type of equipment is not leg armour ask user to input a different location to
                        # equip the item
                        location = input(
                            f"{Colour.green}{location}{Colour.reset} is not a valid location for a "
                            f"{Colour.orange}{item.item_type}{Colour.reset}, please input a different "
                            f"location to equip that piece of equipment (or type back to cancel).\n")
                        continue

                elif location.lower() == "back":
                    # if the user inputs "back", return without making changes
                    break

                else:
                    location = input(
                        f"{Colour.green}{location}{Colour.reset} is not a valid location to equip an item."
                        f" Please input a different location to equip that piece of equipment"
                        f"(or type back to cancel).\n")
                    # if the location indicated by the player is not valid, ask player to input a new location
                    continue
            except ValueError:
                print(f"{Colour.red}Your input is not valid!{Colour.reset}")
                item = input(f"Please select a different item to equip.\n")
                location = input(f"Please select a different location.\n")
                continue
            except AttributeError:
                print(f"{Colour.orange}{item}{Colour.reset} is not in your inventory.\n")

    def pickup_item(self, item):
        if item is not None:
            self.inventory.append(item)
            # add item to the inventory list
            time.sleep(0.5)
            # wait 1 second before displaying message
            print(f"{Colour.orange}{item}{Colour.reset} has been placed in your inventory.\n")

    def inv_list(self):
        try:
            for key, value in self.character_info().items():
                if key == "Inventory":
                    print(f"{Colour.cyan}{Colour.bold}{key}:{Colour.reset}")
                    if not value:
                        print(f"    {Colour.orange}Empty{Colour.reset}")
                    else:
                        for i in value:
                            print(f"    {Colour.orange}{i}{Colour.reset}")
        except IndexError:
            print(f"{Colour.red}Error: IndexError{Colour.reset}")

    def level_up(self, exp):
        time.sleep(0.5)
        print(f"{Colour.bold}{Colour.orange}You have gained {exp} exp.{Colour.reset}\n")
        # print exp gained
        self.current_exp = self.current_exp + exp
        # add exp to character
        while self.current_exp >= self.max_exp:
            # level up character and add stats
            self.current_exp = self.current_exp - self.max_exp
            self.level = self.level + 1
            self.max_hp = self.max_hp + 25
            self.current_hp = self.max_hp
            self.strength = self.strength + 4
            self.defence = self.defence + 4
            time.sleep(0.5)
            print(f"{Colour.bold}{Colour.blue_back}You have leveled up to level {self.level}.{Colour.reset}\n")
            # print level up message
            self.max_exp = self.max_exp + (500 * (self.level - 1))
            # reset exp cap to level up

    def player_death(self):
        restart = input(
            f"{Colour.red}You have died! \n Would you like to load the latest save? (Y or N).{Colour.reset}\n")
        # print death message
        while True:
            if restart.lower() == "y":
                self.load_game()
                # load previous save if player requests
                break
            elif restart.lower() == "n":
                leader_board()
                print("The program will exit in 15 seconds")
                time.sleep(15)
                sys.exit(0)
                # exit game
            else:
                restart = input(f"{Colour.red}Invalid input. Please type Y or N.{Colour.reset}\n")
                # request player for valid input
                continue

    def player_attack(self, target):
        player_damage = self.strength
        # strength of the character
        monster_defence = target.defence
        # defence of the monster

        if self.R_hand is not None:
            if self.R_hand.item_type == "Weapon":
                # if weapon is equipped to right hand add weapon points to player damage
                player_damage = player_damage + self.R_hand.item_value
        if self.L_hand is not None:
            if self.L_hand.item_type == "Weapon":
                # if weapon is equipped to left hand add weapon points to player damage
                player_damage = player_damage + self.L_hand.item_value

        if target.head is not None:
            # if a helmet is equipped to the monster add armour points to its total defence
            monster_defence = monster_defence + target.head.item_value
        if target.chest is not None:
            # if an armour is equipped to the monster add armour points to its total defence
            monster_defence = monster_defence + target.chest.item_value
        if target.legs is not None:
            # if leg armour is equipped to the monster add armour points to its total defence
            monster_defence = monster_defence + target.legs.item_value
        if target.R_hand is not None:
            if target.R_hand.item_type == "Shield":
                # if shield is equipped to right hand add armour points to total defence
                monster_defence = monster_defence + target.R_hand.item_value
        if target.L_hand is not None:
            if target.L_hand.item_type == "Shield":
                # if shield is equipped to left hand add armour points to total defence
                monster_defence = monster_defence + target.L_hand.item_value

        if player_damage <= monster_defence:
            # if total monster defence is more or equal to player damage, the total damage dealt will be 1
            total_damage = 1
        else:
            # if total monster defence is less than player damage, the total damage dealt will be
            # player_damage - monster_defence
            total_damage = player_damage - monster_defence

        print(f"{Colour.cyan}{self.name}{Colour.reset} damages {Colour.purple}{target.name}{Colour.reset} for "
              f"{Colour.red}{total_damage}{Colour.reset} points of damage.\n")

        target.current_hp = target.current_hp - total_damage
        # remove damage from monster hp

        if target.current_hp <= 0:
            # if the monster has 0 or less hp
            target.monster_death()
            # change state of monster to dead
            self.level_up(target.exp_worth)
            # add exp worth of monster to character current exp
            print(f"{Colour.yellow}You have gained {target.gold_worth} gold.{Colour.reset}\n")
            print(f"{Colour.yellow}You have collected {target.points_worth} points.{Colour.reset}\n")
            # print message for gold and points gained
            self.gold = self.gold + target.gold_worth
            self.points = self.points + target.points_worth
            # add gold and points gained to character total
            i_list = target.drop_equipment()
            for item in i_list:
                self.pickup_item(item)
                # pick up equipment of monster

        else:
            # if the monster has more than 0 hp, print a message with the monster's current hp
            print(f"{Colour.purple}{target.name}{Colour.reset} Hp is now "
                  f"{Colour.purple}{target.current_hp}{Colour.reset}.\n")

    def battle(self, target):
        self.save_game()
        # save the game before the battle
        time.sleep(0.5)
        if target.alive:
            self.player_attack(target)
            # player attacks monster if monster is alive
            if target.alive:
                time.sleep(0.5)
                target.monster_attack(self)
                # monster attacks player if it is still alive
        else:
            time.sleep(0.5)
            print(f"{Colour.purple}{target.name}{Colour.reset} {Colour.red}has already died.{Colour.reset}\n")

    def enter_dungeon(self):
        inp = input(f"Would you like to enter the dungeon, {Colour.cyan}{self.name}{Colour.reset}? (Y/N)\n")
        while True:
            if inp.lower() == "n":
                self.location = "town"
                print("You have returned to the town!\n")
                break
            elif inp.lower() == "y":
                self.location = "dungeon"
                print(f"{Colour.cyan}{self.name}{Colour.reset}, you have entered the "
                      f"{Colour.blue_back}dungeon floor {self.floor}.{Colour.reset}\n")
                break
            else:
                inp = input(f"{inp} is not a valid input. Please enter Y or N.\n")
                continue

    def enter_town(self):
        inp = input(f"Would you like to return to town, {Colour.cyan}{self.name}{Colour.reset}? (Y/N)")
        while True:
            if inp.lower() == "n":
                self.location = "dungeon"
                print("You decided to stay in the dungeon!")
                break
            elif inp.lower() == "y":
                self.location = "town"
                self.y = 0
                self.x = 0
                print(f"{Colour.cyan}{self.name}{Colour.reset}, you have returned to town.")
                break
            else:
                inp = input(f"{inp} is not a valid input. Please enter Y or N.")
                continue

    def next_floor(self):
        self.floor = self.floor + 1
        print(f"You have gone down to floor {Colour.orange}{self.floor}{Colour.reset}")
        self.y = 0
        self.x = 0

    def move_up(self, f_map):
        if self.y < f_map.y_len:
            self.y = self.y + 1
            print(f"{Colour.cyan}{self.name}{Colour.reset}, your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")
        else:
            print(f"It is impossible to move up. Your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")

    def move_down(self, f_map):
        if self.y > 0:
            self.y = self.y - 1
            print(f"{Colour.cyan}{self.name}{Colour.reset}, your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")
        else:
            print(f"It is impossible to move down. Your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")

    def move_left(self, f_map):
        if self.x < f_map.x_len:
            self.x = self.x + 1
            print(f"{Colour.cyan}{self.name}{Colour.reset}, your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")
        else:
            print(f"It is impossible to move left. Your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")

    def move_right(self, f_map):
        if self.x > 0:
            self.x = self.x - 1
            print(f"{Colour.cyan}{self.name}{Colour.reset}, your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")
        else:
            print(f"It is impossible to move right. Your current position is: {Colour.green}({self.x},{self.y})"
                  f"{Colour.reset}")

    def save_game(self):

        dir1 = os.getcwd()
        save_dir = os.path.join(dir1, "../saves")
        path = os.path.join(save_dir, f"{self.name}_save")
        # get path to save file

        with open(path, 'w+') as file:
            json.dump(self.__dict__, file, default=lambda o: o.__dict__)
            # save the character status

    def load_game(self):

        dir1 = os.getcwd()
        save_dir = os.path.join(dir1, "../saves")
        path = os.path.join(save_dir, f"{self.name}_save")
        # get path to save file
        try:
            with open(path, 'r') as file:
                # load info in file to the character and create any items using the info in the save file
                jl = json.load(file)
                # basic info
                self.name = str(jl["name"])
                self.age = int(jl["age"])
                self.gender = str(jl["gender"])
                self.species = str(jl["species"])
                self.height = str(jl["height"])
                self.weight = str(jl["weight"])
                self.hair_colour = str(jl["hair_colour"])
                # stats
                self.level = int(jl["level"])
                self.max_hp = int(jl["max_hp"])
                self.current_hp = int(jl["current_hp"])
                self.strength = int(jl["strength"])
                self.defence = int(jl["defence"])
                # gold
                self.gold = int(jl["gold"])
                self.points = int(jl["points"])
                # exp
                self.current_exp = int(jl["current_exp"])
                self.max_exp = int(jl["max_exp"])
                # equipment
                head_list = json_load(jl["head"])
                if head_list is not None:
                    self.head = Helmet(head_list[0], head_list[1], head_list[3])
                else:
                    self.head = None

                R_hand_list = json_load(jl["R_hand"])
                if R_hand_list is not None:
                    if R_hand_list[2] == "Weapon":
                        self.R_hand = Weapon(R_hand_list[0], R_hand_list[1], R_hand_list[3])
                    elif R_hand_list[2] == "Shield":
                        self.R_hand = Shield(R_hand_list[0], R_hand_list[1], R_hand_list[3])
                else:
                    self.R_hand = None

                L_hand_list = json_load(jl["L_hand"])
                if L_hand_list is not None:
                    if L_hand_list[2] == "Weapon":
                        self.L_hand = Weapon(L_hand_list[0], L_hand_list[1], L_hand_list[3])
                    elif L_hand_list[2] == "Shield":
                        self.L_hand = Shield(L_hand_list[0], L_hand_list[1], L_hand_list[3])
                else:
                    self.L_hand = None

                chest_list = json_load(jl["chest"])
                if chest_list is not None:
                    self.chest = Weapon(chest_list[0], chest_list[1], chest_list[3])
                else:
                    self.chest = None

                legs_list = json_load(jl["legs"])
                if legs_list is not None:
                    self.legs = Weapon(legs_list[0], legs_list[1], legs_list[3])
                else:
                    self.legs = None

                # inventory
                self.inventory = []
                inv_list = list(jl["inventory"])
                for items in inv_list:
                    atr_list = json_load(items)

                    if atr_list is not None:
                        if atr_list[2] == "Helmet":
                            tmp_item = Helmet(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)
                        elif atr_list[2] == "Weapon":
                            tmp_item = Weapon(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)
                        elif atr_list[2] == "Weapon":
                            tmp_item = Weapon(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)
                        elif atr_list[2] == "Shield":
                            tmp_item = Shield(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)
                        elif atr_list[2] == "Armour":
                            tmp_item = Armour(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)
                        elif atr_list[2] == "Leg armour":
                            tmp_item = LegArmour(atr_list[0], atr_list[1], atr_list[3])
                            self.inventory.append(tmp_item)

                self.location = str(jl["location"])
                self.floor = int(jl["floor"])
                self.x = int(jl["x"])
                self.y = int(jl["y"])
        except FileNotFoundError:
            print(f"{Colour.red}Error: File not found.{Colour.reset}\n")

# -*- coding: utf-8 -*-
"""
Created on Tue Nov 22 21:42:44 2022

@author: Andre Carreira
"""
import time
from items import *
from text_colour import *


class Monster:

    def __init__(self, name, gender, level):
        # basic info
        self.alive = True
        self.name = name
        self.species = None
        self.gender = gender
        self.exp_worth = 200
        self.gold_worth = 20
        self.points_worth = 0
        # stats
        self.level = level
        self.max_hp = 10
        self.current_hp = self.max_hp
        self.strength = 2
        self.defence = 2
        # equipment
        self.head = None
        self.R_hand = None
        self.L_hand = None
        self.chest = None
        self.legs = None
        # location
        self.floor = 1
        self.x = 0
        self.y = 0

    def __repr__(self):
        return self.name
        # when printing the object display its name only

    def monster_info(self):
        # place all the character information in a dictionary
        return {"Name": self.name,
                "Level": self.level,
                "Gender": self.gender,
                "Species": self.species,
                "Max Hp": self.max_hp,
                "Current Hp": self.current_hp,
                "Strength": self.strength,
                "Defence": self.defence,
                "Gold Worth": self.gold_worth,
                "Exp Worth": self.exp_worth,
                "Points Worth": self.points_worth,
                "Equipment": {"Head": self.head,
                              "L_Hand": self.L_hand,
                              "R_Hand": self.R_hand,
                              "Chest": self.chest,
                              "Legs": self.legs}}

    def monster_display(self):
        time.sleep(1)
        # wait for 1 second 1 to display
        for key, value in self.monster_info().items():
            if key == "Equipment":
                print(f"{Colour.purple}{Colour.bold}{key}:{Colour.reset}")
                for a, b in value.items():
                    print(f"    {Colour.pink}{Colour.bold}{a}:{Colour.reset}{Colour.pink} {b}{Colour.reset}")
            else:
                print(f"{Colour.purple}{Colour.bold}{key}:{Colour.reset}{Colour.purple} {value}{Colour.reset}")
        # display the dictionary created in character_info()
        dir1 = os.getcwd()
        resource_dir = os.path.join(dir1, "../resources")
        path = os.path.join(resource_dir, f"generic_monster.txt")
        # get path to monster image file

        with open(path, "r") as file:
            for line in file:
                print(line.rstrip())
        file.close()

    def monster_death(self):
        time.sleep(0.5)
        print(f"{Colour.purple}{self.name}{Colour.reset} {Colour.red}has died.{Colour.reset}\n")
        self.alive = False

    def monster_attack(self, target):
        monster_damage = self.strength
        player_defence = target.defence

        if self.R_hand is not None:
            if self.R_hand.item_type == "Weapon":
                monster_damage = monster_damage + self.R_hand.item_value
        if self.L_hand is not None:
            if self.L_hand.item_type == "Weapon":
                monster_damage = monster_damage + self.L_hand.item_value

        if target.head is not None:
            player_defence = player_defence + target.head.item_value
        if target.chest is not None:
            player_defence = player_defence + target.chest.item_value
        if target.legs is not None:
            player_defence = player_defence + target.legs.item_value
        if target.R_hand is not None:
            if target.R_hand.item_type == "Shield":
                player_defence = player_defence + target.R_hand.item_value
        if target.L_hand is not None:
            if target.L_hand.item_type == "Shield":
                player_defence = player_defence + target.L_hand.item_value

        if monster_damage <= player_defence:
            total_damage = 1
        else:
            total_damage = monster_damage - player_defence

        print(f"{Colour.purple}{self.name}{Colour.reset} damages {Colour.cyan}{target.name}{Colour.reset} for "
              f"{Colour.red}{total_damage}{Colour.reset} points of damage.\n")

        target.current_hp = target.current_hp - total_damage

        if target.current_hp <= 0:
            target.player_death()
        else:
            print(f"{Colour.cyan}{target.name}{Colour.reset} Hp is now "
                  f"{Colour.red}{target.current_hp}{Colour.reset}.\n")

    def drop_equipment(self):
        drops_list = []
        # list of equipment dropped by monster after death
        #while True:
        try:
                #if self.head is not None:
                    drops_list.append(self.head)
                    #continue
                #elif self.R_hand is not None:
                    drops_list.append(self.R_hand)
                    #continue
                #elif self.L_hand is not None:
                    drops_list.append(self.L_hand)
                    #continue
                #elif self.chest is not None:
                    drops_list.append(self.chest)
                    #continue
                #elif self.legs is not None:
                    drops_list.append(self.legs)
                   # continue
               # else:
                   # break
        except IndexError:
            print(f"{Colour.red}Error: Index error{Colour.reset}\n")

        return drops_list


class Goblin(Monster):

    def __init__(self, name, gender, level, eqp_head, eqp_R_hand, eqp_L_hand, eqp_chest, eqp_legs):
        Monster.__init__(self, name, gender, level)
        self.species = "Goblin"
        self.max_hp = self.max_hp + (self.level * 15)
        self.current_hp = self.max_hp
        self.strength = self.strength + (self.level * 3)
        self.defence = self.defence + (self.level * 3)
        self.gold_worth = self.gold_worth + (self.level * 20)
        self.exp_worth = self.exp_worth + (self.level * 200)
        self.points_worth = self.level * 300
        # equipment
        self.head = eqp_head
        self.R_hand = eqp_R_hand
        self.L_hand = eqp_L_hand
        self.chest = eqp_chest
        self.legs = eqp_legs


class Orc(Monster):

    def __init__(self, name, gender, level, eqp_head, eqp_R_hand, eqp_L_hand, eqp_chest, eqp_legs):
        Monster.__init__(self, name, gender, level)
        self.species = "Orc"
        self.max_hp = self.max_hp + (self.level * 20)
        self.current_hp = self.max_hp
        self.strength = self.strength + (self.level * 4)
        self.defence = self.defence + (self.level * 4)
        self.gold_worth = self.gold_worth + (self.level * 30)
        self.exp_worth = self.exp_worth + (self.level * 300)
        self.points_worth = self.level * 500
        # equipment
        self.head = eqp_head
        self.R_hand = eqp_R_hand
        self.L_hand = eqp_L_hand
        self.chest = eqp_chest
        self.legs = eqp_legs


class Skeleton(Monster):

    def __init__(self, name, gender, level, eqp_head, eqp_R_hand, eqp_L_hand, eqp_chest, eqp_legs):
        Monster.__init__(self, name, gender, level)
        self.species = "Skeleton"
        self.max_hp = self.max_hp + (self.level * 10)
        self.current_hp = self.max_hp
        self.strength = self.strength + (self.level * 4)
        self.defence = self.defence + (self.level * 2)
        self.gold_worth = self.gold_worth + (self.level * 15)
        self.exp_worth = self.exp_worth + (self.level * 150)
        self.points_worth = self.level * 200
        # equipment
        self.head = eqp_head
        self.R_hand = eqp_R_hand
        self.L_hand = eqp_L_hand
        self.chest = eqp_chest
        self.legs = eqp_legs


class Spider(Monster):

    def __init__(self, name, gender, level):
        Monster.__init__(self, name, gender, level)
        self.species = "Spider"
        self.max_hp = self.max_hp + (self.level * 5)
        self.current_hp = self.max_hp
        self.strength = self.strength + (self.level * 6)
        self.defence = self.defence + (self.level * 1)
        self.gold_worth = self.gold_worth + (self.level * 5)
        self.exp_worth = self.exp_worth + (self.level * 50)
        self.points_worth = self.level * 100

    def monster_display(self):
        time.sleep(1)
        # wait for 1 second 1 to display
        for key, value in self.monster_info().items():
            if key == "Equipment":
                print(f"{Colour.purple}{Colour.bold}{key}:{Colour.reset}")
                for a, b in value.items():
                    print(f"    {Colour.pink}{Colour.bold}{a}:{Colour.reset}{Colour.pink} {b}{Colour.reset}")
            else:
                print(f"{Colour.purple}{Colour.bold}{key}:{Colour.reset}{Colour.purple} {value}{Colour.reset}")
        # display the dictionary created in character_info()
        dir1 = os.getcwd()
        resource_dir = os.path.join(dir1, "../resources")
        path = os.path.join(resource_dir, f"spider.txt")
        # get path to spider monster image file

        with open(path, "r") as file:
            for line in file:
                print(line.rstrip())
        file.close()

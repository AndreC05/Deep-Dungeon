# -*- coding: utf-8 -*-
"""
Created on Sun Nov 20 19:53:49 2022

@author: 100283438
"""
import time
import os.path
from text_colour import *


class Item:

    def __init__(self, name, worth):
        self.name = name
        self.worth = worth
        self.item_type = None
        self.item_value = None

    def __repr__(self):
        return self.name
        # when printing the object display its name only

    def display(self):
        time.sleep(1)
        # wait for 1 second to display
        print(
            f" Item Name: {self.name} \n Worth: {self.worth} gold \n Item type: {self.item_type} \n "
            f"Armour value: {self.item_value}\n")
        # print all the information of the item
        dir1 = os.getcwd()
        resource_dir = os.path.join(dir1, "../resources")
        path = os.path.join(resource_dir, f"{self.item_type}.txt")
        # get path to item image file

        try:
            with open(path, "r") as file:
                for line in file:
                    print(line.rstrip())
            file.close()
        except FileNotFoundError:
            print(f"{Colour.red}Error: File not found.{Colour.reset}\n")


class Armour(Item):

    def __init__(self, name, worth, armour_value):
        Item.__init__(self, name, worth)
        self.item_type = "Armour"
        self.item_value = armour_value


class Weapon(Item):

    def __init__(self, name, worth, weapon_value):
        Item.__init__(self, name, worth)
        self.item_type = "Weapon"
        self.item_value = weapon_value

    def display(self):
        time.sleep(1)
        # wait for 1 second to display
        print(
            f" Item Name: {self.name} \n Worth: {self.worth} gold \n Item type: {self.item_type} \n "
            f"Weapon value: {self.item_value}\n")
        # print all the information of the weapon. Overrides the method in item class
        dir1 = os.getcwd()
        resource_dir = os.path.join(dir1, "../resources")
        path = os.path.join(resource_dir, f"{self.item_type}.txt")
        # get path to item image file

        try:
            with open(path, "r") as file:
                for line in file:
                    print(line.rstrip())
            file.close()
        except FileNotFoundError:
            print(f"{Colour.red}Error: File not found.{Colour.reset}\n")


class Shield(Item):

    def __init__(self, name, worth, armour_value):
        Item.__init__(self, name, worth)
        self.item_type = "Shield"
        self.item_value = armour_value


class Helmet(Item):

    def __init__(self, name, worth, armour_value):
        Item.__init__(self, name, worth)
        self.item_type = "Helmet"
        self.item_value = armour_value


class LegArmour(Item):

    def __init__(self, name, worth, armour_value):
        Item.__init__(self, name, worth)
        self.item_type = "Leg armour"
        self.item_value = armour_value

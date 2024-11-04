# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 21:43:36 2022

@author: 100283438
"""
from items import *


def all_items():
    # create the weapons
    all_items.sword1 = Weapon("Broken sword", 50, 5)
    all_items.sword2 = Weapon("Short sword", 1050, 12)
    all_items.sword3 = Weapon("Steel short sword", 2500, 21)
    all_items.sword4 = Weapon("Straight sword", 3400, 33)
    all_items.sword5 = Weapon("Steel straight sword", 5600, 52)
    all_items.sword6 = Weapon("Long sword", 8750, 69)
    all_items.sword7 = Weapon("Steel long sword", 12500, 85)
    all_items.sword8 = Weapon("Excalibur", 18000, 150)

    # create the shields
    all_items.shield1 = Shield("Broken shield", 100, 2)
    all_items.shield2 = Shield("Small shield", 1500, 5)
    all_items.shield3 = Shield("Small steel shield", 2900, 11)
    all_items.shield4 = Shield("Medium shield", 5000, 20)
    all_items.shield5 = Shield("Medium steel shield", 9850, 32)

    # create the helmets
    all_items.helmet1 = Helmet("Broken helmet", 200, 2)
    all_items.helmet2 = Helmet("Leather helmet", 3200, 8)
    all_items.helmet3 = Helmet("Chainmail helmet", 5300, 17)
    all_items.helmet4 = Helmet("Steel helmet", 9850, 30)

    # create the armours
    all_items.armour1 = Armour("Broken armour", 240, 3)
    all_items.armour2 = Armour("Leather armour", 3500, 9)
    all_items.armour3 = Armour("Chainmail armour", 6000, 19)
    all_items.armour4 = Armour("Steel armour", 10000, 34)

    # create the leg armour
    all_items.legarmour1 = LegArmour("Broken leg armour", 200, 2)
    all_items.legarmour2 = LegArmour("Leather leg armour", 3400, 8)
    all_items.legarmour3 = LegArmour("Chainmail leg armour", 5500, 18)
    all_items.legarmour4 = LegArmour("Steel leg armour", 9950, 31)

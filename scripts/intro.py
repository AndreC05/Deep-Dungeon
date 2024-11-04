# -*- coding: utf-8 -*-
"""
Created on Sun Dec 11 19:51:11 2022

@author: Andre Carreira
"""
import os.path
from text_colour import *


def intro():
    dir1 = os.getcwd()
    resource_dir = os.path.join(dir1, "../resources")
    path = os.path.join(resource_dir, f"castle_intro.txt")
    # get path to intro image file

    try:
        with open(path, "r") as file:
            for line in file:
                print(line.rstrip())
                # print intro image
        file.close()
    except FileNotFoundError:
        print(f"{Colour.red}Error: File not found.{Colour.reset}\n")

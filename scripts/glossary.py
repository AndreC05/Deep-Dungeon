# -*- coding: utf-8 -*-
"""
Created on Wed Nov 22 19:45:22 2022

@author: Andre Carreira
"""
import time


def glossary():
    time.sleep(1)
    # wait for 1 second before displaying
    glossary_dict = {"Goblin": "Small and agile.Not very smart.",
                     "Ogre": "Quite strong.Can be a challenge for new adventurers.",
                     "Spider": "A cave spider capable of paralyzing it's enemies with it's fangs but is incapable of "
                               "wielding weapons. A very cunning enemy.",
                     "Skeleton": "An agile monster capable of wielding a variety of weapons. Not the smartest of the "
                                 "bunch."
                     }
    # create dictionary with monster information
    print("Glossary:\n")
    for monster, info in glossary_dict.items():
        print(f"{monster}: {info}")
        # print every entry in the glossary

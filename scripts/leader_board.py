# -*- coding: utf-8 -*-
"""
Created on Thu Dec  1 16:12:53 2022

@author: 100283438
"""
from os.path import isfile, join
import os.path
import json
import csv
from operator import *
import pandas
from text_colour import *


def leader_board():
    header = ["Name", "Level", "Score"]
    # create headers
    characters = []

    dir1 = os.getcwd()
    save_dir = join(dir1, "../saves")
    resources_dir = join(dir1, "../resources")

    all_files = []

    for file in os.listdir(save_dir):
        if isfile(join(save_dir, file)):
            all_files.append(file)
            # join all save files into a list

    for f in all_files:
        path1 = join(save_dir, str(f))
        # get the path to every save file
        try:
            with open(path1, "r") as f2:
                # get the values for name, level and points for every save file
                jl = json.load(f2)
                name = str(jl["name"])
                level = int(jl["level"])
                points = int(jl["points"])
                char_temp = (name, level, points)
                # create a tuple for every character
                characters.append(char_temp)
                # add that character to a list
            f2.close()
        except FileNotFoundError:
            print(f"{Colour.red}Error: File not found.{Colour.reset}\n")
    characters_sorted = sorted(characters, key=itemgetter(2), reverse=True)
    # sort the list of tuples in descending order by points

    path2 = join(resources_dir, "score_board")
    # get the path to the score board file

    try:
        with open(path2, "w") as f3:
            writer = csv.writer(f3)
            writer.writerow(header)
            # write the score table

            for data in characters_sorted:
                writer.writerow(data)
                # add the data to the table

        f3.close()
    except FileNotFoundError:
        print(f"{Colour.red}Error: File not found.{Colour.reset}\n")

    table = pandas.read_csv(path2)
    print(f"\n{Colour.blue_back}Score Board:{Colour.reset}\n\t{Colour.pink}{table.head(10)}{Colour.reset}")
    # print table to console




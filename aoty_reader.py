#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec 18 10:52:28 2020

@author: benjamingoodheart
"""

import numpy as np
import pandas as pd

df = pd.read_csv('aoty.csv')
d1 = df["Rating"]
s = pd.Series(['aoty.csv'])

#have the choice how to sort
readmode = input("How would you like to sort? Type --help for options \n")

if readmode.lower() == "--help":
    print("You can choose how you would like to sort by...")
    print("artist or a")
    print("album name or an")
    print("genre or g")
    print("year or y")
    print("rating or r")
    print("label or l")
    print("comments or c")
    print("all to print as is")
    print("\n")
    print("You can also add asc or desc after the choice to change how it is sorted")
    readmode = input("So what will it be, how would you like to sort?")
#sort by rating
print(df.sort_values(by="Rating", ascending=False))

#sory by year
print("Now sorting by year")
print(df.sort_values(by="Year", ascending=False))


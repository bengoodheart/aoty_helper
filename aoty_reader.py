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

print(df.head())
print(df.sort_values(by="Rating", ascending=False))
print(s.sort_values)
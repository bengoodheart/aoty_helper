#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Dec  8 20:32:14 2020

@author: benjamingoodheart

"""
import csv
from os import path

#TODO:  ADD EDIT CAPABILITY 
#       REVISIT IMPLEMENTATION IE SHOULD I MAKE CLASSES?

def fileExists(file_name):
    return path.exists(file_name)

def inputter():
    q = False
    while(q == False):
            artist = input("Please input the artist name: ")
            album = input("Please input the album name: ")
            genre = input("Please input the genre: ")  
            label = input("Please input the label: ")
            year = input("Please input the year: ")
            rating = input("Please rate from 1 to 10: ")
            
            ##makes sure the rating int is valid
            try:
                if int(rating) not in range(1,11, 1):
                    print("Error: Please put a number between 1 and 10")
                    writer.writerow([])         #writes an empty row so the loop doesn't write onto the previous entry
                    continue
                else:
                    pass
            except ValueError:
                print("Error, Please insert a number!")
                writer.writerow([])
                continue
            
            
            comments = input("Please input any comments you may have: ")
            
            #Pre-write summary
            print("Entry recorded:", album, "by", artist,"| Genre:", genre,"| Label:", label, "| Released:", year, "| You rated it a ",rating,"/10")
            print("You commented: ", comments)
            correct = input("Is this correct? y/n: ")
            if (correct.lower() != 'n'):
                writer.writerow([artist, album, genre, label, rating, year, comments])
            else:
                writer.writerow([])
                continue
            ans = input("Would you like to continue? y/n: ")
            if ans.lower() == 'n':
                q = True
            else:
                q = False

if fileExists('aoty.csv'):
    with open('aoty.csv', 'a') as csv_file:
        print("Appending....")     
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        inputter()
else:
    with open('aoty.csv', 'w') as csv_file:
        writer = csv.writer(csv_file, quoting=csv.QUOTE_ALL)
        writer.writerow(['Arist','Album Name','Genre', 'Label', 'Rating', 'Year', 'Comments'])
        inputter()
            
print("\nThe session has concluded. Goodbye.\n")


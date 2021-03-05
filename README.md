# aoty_helper
This is a command-line tool I created to help me organize my album of the year list. It came together a little too late to be useful for 2020, but I am going to use it for 2021 to keep track of everything that I listen to. 

There are two files initially, an entry tool and a reader. The entry tool outputs to a .csv that the reader then uses pandas to read. I am still working on adding functionality to the reader, i.e. allowing the user to choose what information the program prints out.

In the meantime, enjoy the entry tool and play around with the reader if you feel so inclined!

## 1: Clone
To begin, clone the repo to your local drive. 

`git clone https://github.com/bengoodheart/aoty_helper.git
cd aoty_help.git`

## 2: Virtual Environment
Activate the virtual environment so you don't have to worry about dependencies.

`source venv/bin/activate`

## 3: Using the Entry Tool

Open the entry file.

`python3 aoty_entry.py`

You will see a prompt for the artist, then the album name, the genre, the label, the year it was released, and a space for comments.

The program will confirm your entry and then you can write it to the csv by entering y. If the .csv does not already exist, it will be made. If it exists, the csv will be appended.

The program will then ask if you'd like to continue. If so, enter y. If not, it will conclude your session.

## 4: Using the Reader Tool

First, you must have created a .csv with the entry tool before opening this file. Once you have enter:

`python3 aoty_reader.py`

This will print your dataframe. The functionality is very sparse right now but I will be adding to it.


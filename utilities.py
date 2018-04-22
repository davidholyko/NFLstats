#input player name and stat, outputs results

import csv

def reverse_name(first_last):
    """Tom Brady -> Brady, Tom"""
    if ' ' in first_last:
        words = first_last.split(' ')
        last_first = words[1] + ', ' + words[0]
        return last_first
    else:
        return ""  

def get_qb_id(name):
    with open("NFL QB ID 2016.csv") as f:
        reader = csv.reader(f)
        for row in reader:
            if name == row[3] or reverse_name(name) == row[3]: # TODO: make this be case-insensitive
                return row[2] 

def reverse_reverse_name(last_first):
    """Brady, Tom -> Tom Brady"""
    if ',' in last_first:
        words = last_first.split(', ')
        first_last = words[1] + ' ' + words[0]
        return first_last
    else:
        return ""                

def get_player_names():
    player_names = []

    with open("NFL QB ID 2016.csv") as f: # assumes that this is de-duped
        reader = csv.reader(f)
        for row in reader: # contains header row
            name = row[3]
            player_names.append(name)
            player_names.append(reverse_reverse_name(name))

    return player_names

def inputQB(qb_id, stat):
    if stat == "yards":
        file_name = 'NFL 2017 QB Stats Passsing Yards.csv'
    if stat == "TD":
        file_name ='NFL 2017 QB Stats Passsing TDs.csv'
    with open(file_name) as f:
        reader = csv.reader(f)
        for row in reader:
            for i in range(len(row)):
                if row[i] == "":
                    row[i] = "0"
            if qb_id == row[0]:
                return row

# print(inputQB("2495143", "yards"))


[222,333,111,222,333,888]

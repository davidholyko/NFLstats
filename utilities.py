#input player name and stat, outputs results

import csv

def reverse_name(first_last):
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

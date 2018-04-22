#input player name and stat, outputs results

import csv

def inputQB(QB_name, stat):
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
            if QB_name == row[0]:
                return row

# print(inputQB("2495143", "yards"))


[222,333,111,222,333,888]

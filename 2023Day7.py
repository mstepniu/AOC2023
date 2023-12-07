# https://adventofcode.com/2023/day/6
# *********** NEED TO CLEAN UP *****************


import logging
import pandas
import numpy
import re
from functools import cmp_to_key

with open("2023day7.txt") as input_stream:
    data = [line.rstrip('\n') for line in input_stream]


hands = list()


def check5kind(hand):
    pattern = re.compile(r"(.)\1\1\1\1")
    matches = pattern.search(hand)
    if matches:
        return "6."+hand
    else:
        return 0


def check4kind(hand):
    test = "".join(sorted(hand))
    pattern = re.compile(r"(.)\1\1\1")
    matches = pattern.search(test)
    if matches:
        return "5."+hand
    else:
        return 0

def checkFullHouse(hand):
    test = "".join(sorted(hand))
    if test.count(test[0]) == 3 and test.count(test[4]) == 2:
        return "4."+hand
    elif test.count(test[0]) == 2 and test.count(test[4]) == 3:
        return "4."+hand
    else:
        return 0


def check3kind(hand):
    test = "".join(sorted(hand))
    pattern = re.compile(r"(.)\1\1")
    matches = pattern.search(test)
    if matches:
        return "3."+hand
    else:
        return 0


def check2pair(hand):
    test = "".join(sorted(hand))
    pattern = re.compile(r"(.)\1.*(.)\2")
    matches = pattern.search(test)
    if matches:
        return "2."+hand
    else:
        return 0


def check1pair(hand):
    test = "".join(sorted(hand))
    pattern = re.compile(r"(.)\1")
    matches = pattern.search(test)
    if matches:
        return "1."+hand
    else:
        return 0


def checkHighcard(hand):
    return "0."+hand


for i in data:
    temp = 0
    hands.append(i.split(" "))
    hands[-1][1] = int(hands[-1][1])

    hands[-1][0] = hands[-1][0].replace("A", ">")
    hands[-1][0] = hands[-1][0].replace("K", "=")
    hands[-1][0] = hands[-1][0].replace("Q", "<")
    hands[-1][0] = hands[-1][0].replace("J", ";")
    hands[-1][0] = hands[-1][0].replace("T", ":")


    temp = check5kind(hands[-1][0])
    if temp == 0:
        temp = check4kind(hands[-1][0])
        if temp == 0:
            temp = checkFullHouse(hands[-1][0])
            if temp == 0:
                temp = check3kind(hands[-1][0])
                if temp == 0:
                    temp = check2pair(hands[-1][0])
                    if temp == 0:
                        temp = check1pair(hands[-1][0])
                        if temp == 0:
                            temp = checkHighcard(hands[-1][0])

    hands[-1].append(temp)

hands = sorted(hands, key=lambda x: x[2])

total = 0

for i in range(len(hands)-1, -1, -1):
    total += hands[i][1] * (i+1)
    #print(hands[i][1], i+1)
print(total)

#part 2

hands = list()

# 6.hand
def check5kind(hand):
    pattern = re.compile(r"(.)\1\1\1\1")
    matches = pattern.findall(hand)
    if matches:
        if matches[0] != "0":
            return "6."+hand
        else:
            return 0
    else:
        return 0

# 5.hand
def check4kind(hand):
    test = "".join(sorted(hand))
    num = test.count("0")
    pattern = re.compile(r"(.)\1\1\1")
    matches = pattern.findall(test)
    if matches:
        if matches[0] != "0":
            num += 5
            return f"{num}.{hand}"

        else:
            return 0
    else:
        return 0
# 4.hand
def checkFullHouse(hand):
    test = "".join(sorted(hand))
    if test.count(test[0]) == 3 and test.count(test[4]) == 2:
        if test[0] == "0":
            return "6."+hand
        elif test[4] == "0":
            return "6."+hand
        return "4."+hand
    elif test.count(test[0]) == 2 and test.count(test[4]) == 3:
        if test[0] == "0":
            return "6."+hand
        elif test[4] == "0":
            return "6."+hand
        return "4."+hand
    else:
        return 0

# 3.hand
def check3kind(hand):
    test = "".join(sorted(hand))
    num = test.count("0")
    pattern = re.compile(r"(.)\1\1")
    matches = pattern.findall(test)
    if matches:
        if matches[0] != "0":
            if num != 0:
                num+=1
            num += 3
            return f"{num}.{hand}"
        else:
            return 0
    else:
        return 0

# 2.hand
def check2pair(hand):
    test = "".join(sorted(hand))
    num = test.count("0")
    test = test.replace("0", "")
    pattern = re.compile(r"(.)\1.*(.)\2")
    matches = pattern.search(test)
    if matches:
        if num == 0:
            return "2." + hand
        if num == 1:
            return "4."+hand
    else:
        return 0

# 1.hand
def check1pair(hand):
    test = "".join(sorted(hand))
    num = test.count("0")
    test = test.replace("0", "")
    pattern = re.compile(r"(.)\1")
    matches = pattern.search(test)
    if matches:
        if num == 1:
            num += 2
            return f"{str(num)}.{hand}"
        elif num >= 2:
            num += 3
            return f"{str(num)}.{hand}"
        else:
            num +=1
            return f"{str(num)}.{hand}"
    else:
        return 0


# 0.hand
def checkHighcard(hand):
    num = hand.count("0")
    if num <= 1:
        return f"{num}.{hand}"
    elif num == 2:
        num+=1
        return f"{num}.{hand}"
    elif num >= 3 and num <= 4:
        num+=2
        return f"{num}.{hand}"
    else:
        num+=1
        return f"{num}.{hand}"

for i in data:
    temp = 0
    hands.append(i.split(" "))
    hands[-1][1] = int(hands[-1][1])

    hands[-1][0] = hands[-1][0].replace("A", ">")
    hands[-1][0] = hands[-1][0].replace("K", "=")
    hands[-1][0] = hands[-1][0].replace("Q", "<")
    hands[-1][0] = hands[-1][0].replace("J", "0")
    hands[-1][0] = hands[-1][0].replace("T", ":")


    temp = check5kind(hands[-1][0])
    if temp == 0:
        temp = check4kind(hands[-1][0])
        if temp == 0:
            temp = checkFullHouse(hands[-1][0])
            if temp == 0:
                temp = check3kind(hands[-1][0])
                if temp == 0:
                    temp = check2pair(hands[-1][0])
                    if temp == 0:
                        temp = check1pair(hands[-1][0])
                        if temp == 0:
                            temp = checkHighcard(hands[-1][0])

    hands[-1].append(temp)

hands = sorted(hands, key=lambda x: x[2])

total = 0

for i in range(len(hands)-1, -1, -1):
    total += hands[i][1] * (i+1)
    #print(hands[i][1], i+1)
print(total)


# 251076361 - too high
# 250304320 - too low
# 250342788 - too low
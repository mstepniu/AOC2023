# https://adventofcode.com/2023/day/8

from pathlib import Path
from itertools import cycle
import math

# with open("2023day8.txt") as input_stream:
#     data = [line.rstrip('\n') for line in input_stream]

data_raw = Path(__file__).with_name("2023Day8.txt").read_text().splitlines()

LR = data_raw[0]
LR = [1 if x == "R" else 0 for x in LR]

data = dict()

for i in data_raw[2:]:

    data[i[:3]] = (i[7:10], i[12:15])

count = 0
loc = "AAA"

for i in cycle(LR):
    count += 1
    loc = data[loc][i]
    if loc == "ZZZ":
        break

print(count)

# part2
nodes = list()

for i in data:
    if i[2] == "A":
        nodes.append(i)

templist = list()
totals = list()
list2 = list()
masterlist = list()

for i, j in enumerate(nodes):
    node = j
    #print("I CANT FIND SHIT IN VSCODE OUTPUT", node)
    count = 1
    for n in cycle(LR):
        if data[node][n].endswith("Z"):
            break
        else:
            count+=1
            node = data[node][n]
    totals.append(count)
        
print(math.lcm(*totals))


# 71138995200 - too low

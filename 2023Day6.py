# https://adventofcode.com/2023/day/6

import logging
import pandas
import numpy


with open("2023Day6.txt", 'r') as file:
    data = file.readlines()

for i in data:
    i.rstrip("\n")


racetimes = data[0][10:].split()
records = data[1][10:].split()

racetimes = [int(x) for x in racetimes]
records = [int(x) for x in records]

finalspeed = dict()
totals = 1

for i, s in enumerate(racetimes):
    for t in range(s):
        speed = (s - t) * t
        if speed > records[i]:
            finalspeed[t] = speed
    #print(f"for {s} final speeds are: {finalspeed}")
    totals *= len(finalspeed)
    finalspeed.clear()

print(totals)

# part2

totals = 0

racetimes = data[0][10:].split()
records = data[1][10:].split()

racetimes = "".join([str(x) for x in racetimes])
records = "".join([str(x) for x in records])

racetimes = int(racetimes)
records = int(records)

for t in range(racetimes):
    speed = (racetimes - t) * t
    if speed > records:
        totals += 1

print("Brute: ", totals)

# quadratic
def part2q():
    time = racetimes
    distance = records

    b1 = math.floor((time + math.sqrt(pow(time, 2) - 4 * distance))/2)
    b2 = math.ceil((time - math.sqrt(pow(time, 2) - 4 * distance))/2)

    print("Quadratic: ", b1 - b2 + 1)

part2q()


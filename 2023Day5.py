# https://adventofcode.com/2023/day/5

import logging
import pandas
import numpy


with open("2023Day5.txt", 'r') as file:
    data = file.readlines()


seeds = list()
seeds2 = list()

mapping = [[],[],[],[],[],[],[]]
mapcount = 0

for i, line in enumerate(data):
    if line.startswith("seeds:"):
        seeds = [int(x) for x in line[6:].split()]
        mapcount -= 1
    elif line[0].isnumeric():
        mapping[mapcount].append([int(x) for x in line.split()])
    elif line == "\n":
        continue
    else:
        mapcount += 1
seeds2 = seeds.copy()

for i, seed in enumerate(seeds):  #loop through seeds
    for j in range(len(mapping)):  #loop through mappings (7)
        for k in range(len(mapping[j])): #loop through parts of each mapping
            src = mapping[j][k][1]
            dest = mapping[j][k][0]
            end = mapping[j][k][1] + mapping[j][k][2]
            if src <= seeds[i] <= end:
                seeds[i] = seeds[i] - src + dest
                break

print(min(seeds))

# part2
# I'm going to be honest here...  this one took me a long time because
# I did not want to have a brute force answer.  And this is NOT brute force.
# People are reporting 5-10 hours before getting an answer brute forcing.
# this takes < 1 second.  The algorithm is going to be very confusing to
# someone trying to follow; it had a lot of trial and error and swapping
# orders of "for" loops.  I'm not going to clean it up in order to preserve
# the state it was in during troubleshooting.
# the basic idea is to put seeds through the test: if a seed is changed add
# it to the list.  if a seed is not changed then do NOT add it yet.  Wait
# until processing all lines of each map and THEN check if no seeds have
# been added.  If none in the list, re-add the original seeds (because they
# have not been changed by the map).  I also don't think I need to use an
# ordereddict().  that is an artifact from an attempt to combat duplicates.

for i in range(0, len(seeds2)-1, 2):
    seeds2[i+1] = seeds2[i] + seeds2[i+1]


def intersection(start1, end1, start2, end2,t):
    if end1 < start2 or start1 > end2:
        return 0
    if start1 == start2 and end1 < end2:
        return [start1+t, end1+t]
    if start1 == start2 and end1 == end2:
        return [start1+t, end1+t]
    if start1 == start2 and end1 > end2:
        return [start1+t, end2+t, end2+1, end1]
    if start1 > start2 and end1 < end2:
        return [start1+t, end1+t]
    if start1 > start2 and end1 == end2:
        return [start1+t, end1+t]
    if start1 > start2 and end1 > end2 and start1 < end2:
        return [start1+t, end2+t, end2+1, end1]
    if start1 < start2 and end1 < end2 and start2 < end1:
        return [start1, start2-1, start2+t, end1+t]
    if start1 < start2 and end1 == end2:
        return [start1, start2-1, start2+t, end1+t]
    if start1 < start2 and end1 > end2:
        return [start1, start2-1, start2+t, end2+t, end2+1, end1]

    if start1 == end2:
        return [start1+t, start1+t, end2+1, end1]

    if end1 == start2:
        return [start1, end1-1, end1+t, end1+t]

    print("ERROR")

totals = list()

seedlist = list()
templist = list()
templist2 = list()

from collections import OrderedDict

for num in range(0, len(seeds2), 2):
    seedlist = [seeds2[num], seeds2[num+1]]
    for j in range(len(mapping)):  #loop through mappings (7)
        length = len(seedlist)-1
        templist.clear()
        for s in range(0, length, 2):
            templist.clear()
            templist2.clear()
            for k in range(len(mapping[j])): #loop through parts of each mapping
                end = mapping[j][k][1] + mapping[j][k][2]
                start = mapping[j][k][1]
                trans = (-1 * mapping[j][k][1]) + mapping[j][k][0]
                test = intersection(seedlist[s], seedlist[s + 1], start, end, trans)
                if not isinstance(test, int):
                    templist.extend(test)
            if len(templist) == 0:
                templist2.append(seedlist[s])
                templist2.append(seedlist[s+1])
            else:
                templist2.extend(templist)
        if len(templist2) != 0:
            seedlist = list(OrderedDict.fromkeys(templist2))
        templist2.clear()
    totals.append(min(seedlist))

print(min(totals))
# 3889510 - too low
# 8861329 - too low
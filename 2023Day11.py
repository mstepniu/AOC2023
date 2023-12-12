# https://adventofcode.com/2023/day/11
# pretty much a brute force day.  After yesterday using a BFS on a
# single path, I didn't want to overengineer a solution for today.
# I might come back later and clean it up.

from pathlib import Path
import re
import math

data = Path(__file__).with_name("2023Day11.txt").read_text().splitlines()


edata = list()


latitude = list()
for j, i in enumerate(data):
    if i.count("#") == 0:
        edata.append(i)
        latitude.append(j)
    edata.append(i)

vert_insert = list()

longitude = list()
for i in range(len(edata[0])):
    for j in range(len(edata)):
        if edata[j][i] == "#":
            break
    else:
        vert_insert.append(i)
        longitude.append(i)


for i in reversed(vert_insert):
    for j in range(len(edata)):
        edata[j] = edata[j][0:i] + "." + edata[j][i:]

galaxy_list = list()

for c, i in enumerate(edata):
    pattern = re.compile(r"[#]")
    matches = pattern.finditer(i)
    for m in matches:
        galaxy_list.append((c, m.start()))

count = 0
count2 = 0
for i in range(len(galaxy_list)):
    for j in range(len(galaxy_list)):
        count += abs(galaxy_list[i][0] - galaxy_list[j][0])
        count += abs(galaxy_list[i][1] - galaxy_list[j][1])

count = int(count / 2)
print(count) # part1


galaxy_list = list()

for c, i in enumerate(data):
    pattern = re.compile(r"[#]")
    matches = pattern.finditer(i)
    for m in matches:
        galaxy_list.append((c, m.start()))

# not very efficient because we are getting distances between each
# galaxy from both directions.  Which is why we only add 999998 because
# of the initial line (in both directions).
count2 = 0
for i in range(len(galaxy_list)):
    for j in range(len(galaxy_list)):
        for lat in latitude:
            if galaxy_list[i][0] < lat < galaxy_list[j][0]:
                count2 += 999998
            elif galaxy_list[i][0] > lat > galaxy_list[j][0]:
                count2 += 999998
        for lon in longitude:
            if galaxy_list[i][1] < lon < galaxy_list[j][1]:
                count2 += 999998
            elif galaxy_list[i][1] > lon > galaxy_list[j][1]:
                count2 += 999998

count2 = int(count2 / 2)


print(count2 + count)
# https://adventofcode.com/2023/day/3

with open("2023Day3.txt", 'r') as file:
    data = file.readlines()

from collections import defaultdict

total = 0
total2 = 0


cases = list()

added = defaultdict(lambda: False)
alist = list()
def getnum(ndx, linenum):
    temp = ""
    if data[linenum][ndx].isnumeric() and added[(linenum, ndx)] == False:
        if ndx < 0:
            return 0
        #print("ADJACENT IS NUMERIC", data[linenum][ndx])
        temp += data[linenum][ndx]
        added[(linenum, ndx)] = True
        i = 1
        while data[linenum][ndx-i].isnumeric():
            if ndx-i < 0:
                break
            added[(linenum, ndx-i)] = True
            temp = data[linenum][ndx-i] + temp
            i += 1
        i = 1
        while data[linenum][ndx+i].isnumeric():
            added[(linenum, ndx+i)] = True
            temp = temp + data[linenum][ndx+i]
            i += 1
    else:
        return 0
    return int(temp)

def part2(ndx, linenum):
    temp = ""
    if data[linenum][ndx].isnumeric():
        if ndx < 0:
            return 0
        temp += data[linenum][ndx]
        i = 1
        while data[linenum][ndx-i].isnumeric():
            if ndx-i < 0:
                break
            temp = data[linenum][ndx-i] + temp
            i += 1
        i = 1
        while data[linenum][ndx+i].isnumeric():
            temp = temp + data[linenum][ndx+i]
            i += 1
    else:
        return 0
    return int(temp)

starflag = False
starlist = set()

for i, line in enumerate(data):
    for j in range(len(line.rstrip())):
        if not line[j].isnumeric() and line[j] != ".":
            cases.append(j)
    else:
        if len(cases) != 0:
            for t in range(len(cases)):
                # check to the left or right
                if line[cases[t]-1].isnumeric() and cases[t]-1 >= 0:
                    if line[cases[t]] == "*": starlist.add(part2(cases[t]-1, i))
                    total += getnum(cases[t]-1, i)
                if line[cases[t]+1].isnumeric():
                    if line[cases[t]] == "*": starlist.add(part2(cases[t]+1, i))
                    total += getnum(cases[t]+1, i)
                # check higher on graph
                if data[i-1][cases[t]].isnumeric() and i-1 >= 0:
                    if line[cases[t]] == "*": starlist.add(part2(cases[t], i-1))
                    total += getnum(cases[t], i-1)
                if data[i-1][cases[t]-1].isnumeric() and i-1 >= 0:
                    if line[cases[t]] == "*": starlist.add(part2(cases[t]-1, i - 1))
                    total += getnum(cases[t]-1, i - 1)
                if data[i-1][cases[t]+1].isnumeric() and i-1 >= 0:
                    if line[cases[t]] == "*": starlist.add(part2(cases[t] + 1, i - 1))
                    total += getnum(cases[t] + 1, i - 1)
                #check lower on graph
                if data[i+1][cases[t]].isnumeric():
                    if line[cases[t]] == "*": starlist.add(part2(cases[t], i+1))
                    total += getnum(cases[t], i+1)
                if data[i+1][cases[t]-1].isnumeric():
                    if line[cases[t]] == "*": starlist.add(part2(cases[t]-1, i + 1))
                    total += getnum(cases[t]-1, i + 1)
                if data[i+1][cases[t]+1].isnumeric():
                    if line[cases[t]] == "*": starlist.add(part2(cases[t] + 1, i + 1))
                    total += getnum(cases[t] + 1, i + 1)
                if len(starlist) == 2:
                    total2 = total2 + (starlist.pop() * starlist.pop())
                starlist.clear()
            cases.clear()

print(total)
print(total2)


# 4215837 - too low

# https://adventofcode.com/2023/day/10
# part2 - https://en.wikipedia.org/wiki/Ray_casting
# part2 - https://en.wikipedia.org/wiki/Green%27s_theorem

from pathlib import Path

data = Path(__file__).with_name("2023Day10.txt").read_text().splitlines()


count = "".join([str(y) + "," + str(x.index("S")) if "S" in x else "" for y, x in enumerate(data)])

start_x, start_y = count.split(",")


above_pipes = ["|", "L", "J", "S"]
below_pipes = ["|", "F", "7", "S"]
right_pipes = ["-", "J", "7", "S"]
left_pipes = ["-", "L", "F", "S"]

visited = dict()
visited[(int(start_x), int(start_y))] = 0


def check_above(parent, step):
    if parent[0]+1 > len(data) - 1:
        return
    loc = (parent[0]+1, parent[1])
    if loc not in visited and data[loc[0]][loc[1]] in above_pipes:
        visited[loc] = step
        return loc


def check_below(parent, step):
    if parent[0]-1 < 0:
        return
    loc = (parent[0]-1, parent[1])
    if loc not in visited and data[loc[0]][loc[1]] in below_pipes:
        visited[loc] = step
        return loc


def check_right(parent, step):
    if parent[1] + 1 > len(data[0]) - 1:
        return
    loc = (parent[0], parent[1] + 1)
    if loc not in visited and data[loc[0]][loc[1]] in right_pipes:
        visited[loc] = step
        return loc


def check_left(parent, step):
    if parent[1] - 1 < 0:
        return
    loc = (parent[0], parent[1] - 1)
    if loc not in visited and data[loc[0]][loc[1]] in left_pipes:
        visited[loc] = step
        return loc


nodes_to_check = set()
nodes_to_check.add((int(start_x), int(start_y)))
temp_list = set()


step = 1
while nodes_to_check:
    for i in range(len(nodes_to_check)):
        curr_loc = nodes_to_check.pop()
        if data[curr_loc[0]][curr_loc[1]] == "|":
            temp_list.add(check_below(curr_loc, step))
            temp_list.add(check_above(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "F":
            temp_list.add(check_above(curr_loc, step))
            temp_list.add(check_right(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "L":
            temp_list.add(check_below(curr_loc, step))
            temp_list.add(check_right(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "J":
            temp_list.add(check_below(curr_loc, step))
            temp_list.add(check_left(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "-":
            temp_list.add(check_left(curr_loc, step))
            temp_list.add(check_right(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "7":
            temp_list.add(check_above(curr_loc, step))
            temp_list.add(check_left(curr_loc, step))
        elif data[curr_loc[0]][curr_loc[1]] == "S":
            temp_list.add(check_above(curr_loc, step))
            temp_list.add(check_left(curr_loc, step))
            temp_list.add(check_below(curr_loc, step))
            temp_list.add(check_right(curr_loc, step))
        else:
            print(data[curr_loc[0]][curr_loc[1]])
            print("ERROR")

        temp_list.remove(None)
        #print(temp_list, data[curr_loc[0]][curr_loc[1]], curr_loc)
    step += 1
    nodes_to_check.update(temp_list)
    temp_list.clear()

print(max(visited.values()))

# part2 *************************************************************

checked = dict()
adj = list()

for i in range(len(data)):
    for j in range(len(data[0])):
        if (i, j) not in visited:
            adj.append((i, j))


# remove outside items looking from the left and right until you hit an item
# that is in the visited list
for x in range(len(data)):
    y = 0
    y2 = len(data[0]) - 1
    while y < len(data[0]) and (x, y) not in visited and (x, y) in adj:
        adj.remove((x, y))
        y += 1
    while y2 >= 0 and (x, y2) not in visited and (x, y2) in adj:
        adj.remove((x, y2))
        y2 -= 1
# remove outside items looking from the top and bottom until you hit an item
# that is in the visited list
for y in range(len(data[0])):
    x = 0
    x2 = len(data) - 1
    while x < len(data) and (x, y) not in visited and (x, y) in adj:
        adj.remove((x, y))
        x += 1
    while x2 >= 0 and (x2, y) not in visited and (x2, y) in adj:
        adj.remove((x2, y))
        x2 -= 1

final = 0


raylist = list()

inmid = 0

for x, y in adj:
    count = 0
    for i in range(y):
        if (x,i) in visited:
            if data[x][i] == "|":
                count += 1
            elif data[x][i] == "-":
                pass
            else:
                raylist.append(data[x][i])
    while len(raylist):
        item1 = raylist.pop()
        item2 = raylist.pop()
        if item1 in below_pipes and item2 in above_pipes:
            count += 1
        elif item1 in above_pipes and item2 in below_pipes:
            count += 1
    if count % 2 != 0:
        inmid += 1

    raylist.clear()

print(inmid)

# 43 - wrong
# 45 - wrong


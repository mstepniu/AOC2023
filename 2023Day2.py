# https://adventofcode.com/2023/day/2
with open("2023Day2.txt", 'r') as file:
    data = file.readlines()

total = 0
for i in data:
    i = i.replace(",", "")
    i = i.replace(";", "")
    i = i.replace(":", "")
    temp = i.split()
    for j in range(2, len(temp), 2):
        if temp[j+1] == "blue" and int(temp[j]) > 14:
            break
        elif temp[j+1] == "green" and int(temp[j]) > 13:
            break
        elif temp[j+1] == "red" and int(temp[j]) > 12:
            break
    else:
        total += int(temp[1])
print(total)

#part2
total = 0

for i in data:
    i = i.replace(",", "")
    i = i.replace(";", "")
    i = i.replace(":", "")
    temp = i.split()
    redlist = list()
    bluelist = list()
    greenlist = list()
    for j in range(2, len(temp), 2):
        #print(int(temp[j]))
        if temp[j+1] == "blue":
            bluelist.append(int(temp[j]))
        elif temp[j+1] == "green":
            greenlist.append(int(temp[j]))
        elif temp[j+1] == "red":
            redlist.append(int(temp[j]))

    total += (max(bluelist) * max(redlist) * max(greenlist))

    redlist.clear()
    bluelist.clear()
    greenlist.clear()
print(total)

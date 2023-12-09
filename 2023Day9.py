# https://adventofcode.com/2023/day/9



from pathlib import Path

data_raw = Path(__file__).with_name("2023Day9.txt").read_text().splitlines()

linelist = list()

for i in data_raw:
    linelist.append([int(x) for x in i.split()])

total = 0
total2 = 0

for i, j in enumerate(linelist):
    count = 0
    count2 = 0
    temp = j
    temp2 = j[::-1]
    while any(temp):
        temp = [temp[x+1] - temp[x] for x in range(len(temp)-1)]
        count += temp[-1]
        temp2 = [temp2[x + 1] - temp2[x] for x in range(len(temp2) - 1)]
        count2 += temp2[-1]
    else:
        pass
        #print("Loop broken because: ", temp)
    total += count + linelist[i][-1]
    total2 += count2 + linelist[i][0]

print(total)
print(total2)
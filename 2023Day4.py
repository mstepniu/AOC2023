# https://adventofcode.com/2023/day/4

with open("2023Day4.txt", 'r') as file:
    data = file.readlines()

winningnums = list()
playingnums = list()

count = 0
count2 = 0
total = 0
winningcount = list()

for i, line in enumerate(data):
    temp = line[10:40]
    winningnums = temp.split()
    temp = line[42:]
    playingnums = temp.split()
    for w in winningnums:
        if w in playingnums:
            count2 += 1
            if count >= 1:
                count *= 2
            else:
                count += 1
    total += count
    winningcount.append(count2)
    count = 0
    count2 = 0
print(total)


#part2 
part2count = [1] * len(winningcount)

for i, j in enumerate(winningcount):
    for k in range(j):
        part2count[i+k+1] += 1 * part2count[i]

print(sum(part2count))


# 58431 - too low
# 83961 - too low
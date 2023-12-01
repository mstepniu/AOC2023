# https://adventofcode.com/2023/day/1
with open("2023Day1.txt", 'r') as file:
    data = file.read().strip().split()

totals = 0
#iterate over the string from both directions and stopping when you reach a number
# take that number and squish it together and add it to total.
for i in data:
    temp = ""
    for j in i:
        if j.isnumeric():
            temp += j
            break
    for j in reversed(i):
        if j.isnumeric():
            temp += j
            break
    if temp != "":
        totals += int(temp)

print(totals)


#PART2
# create a dictionary of numbered terms
# use the same algo as Part1 except before that we want to replace
# the words with numbers.  Use .replace() and include the text before
# and after because there are test cases such as eightwo which should
# be equal to 82.  if you use replace without including the text back
# you will get 8wo.  Python does not update the string dynamically
# so it will not be a problem during processing.  We could have also
# just added the first and last letter to the string as well.

numbers = dict()
numbers["one"] = "1"
numbers["two"] = "2"
numbers["three"] = "3"
numbers["four"] = "4"
numbers["five"] = "5"
numbers["six"] = "6"
numbers["seven"] = "7"
numbers["eight"] = "8"
numbers["nine"] = "9"

totals = 0
for i in data:

    for c in numbers:
        i = i.replace(c, c + numbers[c] + c)

    temp = ""

    for j in i:
        if j.isnumeric():
            temp += j
            break
    for j in reversed(i):
        if j.isnumeric():
            temp += j
            break

    totals += int(temp)
print(totals)

# 55194 - too low
# 55644 - too low

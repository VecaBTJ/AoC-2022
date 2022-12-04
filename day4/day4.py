import re

total = 0

for line in open("day4_input.txt", 'r'):
    line = re.split('-|,', line)
    if int(line[2]) <= int(line[1]) and int(line[3]) >= int(line[0]):
        total += 1

print("The ranges overlap in", total, "assignment pairs")
